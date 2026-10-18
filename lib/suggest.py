#!/usr/bin/env python3
"""Turn a category of open findings into Pontoon suggestions.

Three steps, each a subcommand, run in order:

``prepare``
    Copies the localized files holding a category's open findings into
    ``work/suggestions/<project>/<locale>/<category>/files/`` and writes
    ``worklist.json`` next to them. Edits happen on those copies, never on
    the clone: ``run.py`` reads the clone exactly as it is on disk, so an
    edited clone would make the next run close findings as fixed before
    anybody in Pontoon had accepted anything.

``include``
    Adds a string with no finding to the worklist, with the reason a person
    gave for fixing it anyway -- typically the same defect spotted in a
    neighbour the reviewer missed. Without it, ``diff`` refuses the edit.

``diff``
    Compares the copies with the clone and lists every string that changed,
    with the finding it addresses. Fails on an edit that does not parse,
    that changes placeholders or markup, or that touches a string with no
    finding in the worklist and no ``include``.

``upload``
    Sends each changed resource to Pontoon's ``upload/suggestions`` endpoint
    as a partial file holding only the changed strings, so nothing else in
    the file can be re-suggested from a clone that is behind Pontoon. Before
    that, each string's current approved translation is fetched and compared
    with the clone: a string that has moved in Pontoon since the clone was
    pulled is left out, because the suggestion would be built on text that
    is no longer there. Without ``--submit`` this is a dry run that writes
    the partial files and calls nothing but the read-only API.

Suggestions are authored by the owner of the token, need translator rights
for the locale, and land unreviewed: nothing is approved or rejected.
"""

from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from collections import Counter
from fnmatch import fnmatch
from json import dumps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import findings as findings_mod  # noqa: E402
import layout  # noqa: E402
import parse  # noqa: E402
import tracker  # noqa: E402

from moz.l10n.formats import Format  # noqa: E402
from moz.l10n.formats.fluent import fluent_serialize_message  # noqa: E402
from moz.l10n.formats.mf2 import mf2_serialize_message  # noqa: E402
from moz.l10n.model import (  # noqa: E402
    CatchallKey,
    Entry,
    Expression,
    Markup,
    PatternMessage,
    VariableRef,
)
from moz.l10n.resource import parse_resource, serialize_resource  # noqa: E402

DEFAULT_SERVER = "https://pontoon.mozilla.org"
# The upload endpoint allows a burst of 30 calls a minute, and rejected
# calls still count against the hourly quota, so stay well under it.
UPLOAD_PAUSE_SECONDS = 2.5
# Pontoon lists at most 100 failed and 100 undefined keys per response, so a
# larger upload could reject strings it never names. Kept at that size, every
# refusal is listed and `refused` can answer for each string.
UPLOAD_MAX_STRINGS = 100


# --- paths -------------------------------------------------------------------

def work_dir(project, locale: str, category: str) -> str:
    return os.path.join(
        config.REPO_ROOT, "work", "suggestions", project.name, locale, category
    )


def _localized_resolver(project, trees, l10n_dir: str):
    """Reference path -> clone-relative path of the localized file holding it."""
    def resolve(rel: str) -> str:
        if project.data.get("layout", "mirrored") == "mirrored":
            return os.path.relpath(os.path.join(trees.root, rel), l10n_dir)
        return trees.locale_paths.get(rel, rel)
    return resolve


def _load_worklist(wdir: str) -> dict:
    path = os.path.join(wdir, "worklist.json")
    if not os.path.exists(path):
        sys.exit(f"no worklist at {path}: run `prepare` first")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# --- Pontoon's view of a string ------------------------------------------------
#
# A port of pontoon/base/simple_preview.py, which is what the API returns as
# a translation's `string`. Applying the same function to the clone's message
# is what makes "has Pontoon moved on?" an exact comparison: Pontoon keeps
# Android escapes such as `‌` as written, which no flattening of ours
# would reproduce.

def _simple_pattern(msg):
    if isinstance(msg, list):
        return msg
    if isinstance(msg, PatternMessage):
        return msg.pattern
    return next(
        pattern
        for keys, pattern in msg.variants.items()
        if all(isinstance(key, CatchallKey) for key in keys)
    )


def _preview_part(part) -> str:
    if isinstance(part, str):
        return part
    if isinstance(ps := part.attributes.get("source", None), str):
        return ps
    if isinstance(part, Expression):
        if part.function == "html" and isinstance(part.arg, str):
            return part.arg
        if part.function == "entity" and isinstance(part.arg, VariableRef):
            return part.arg.name
    elif part.kind in ("open", "standalone"):
        res = "<" + part.name
        for name, val in part.options.items():
            valstr = dumps(val) if isinstance(val, str) else "$" + val.name
            res += f" {name}={valstr}"
        return res + (">" if part.kind == "open" else " />")
    elif part.kind == "close" and not part.options:
        return f"</{part.name}>"
    return mf2_serialize_message(PatternMessage([part]))


def pontoon_preview(fmt, entry) -> str:
    if fmt == Format.fluent:
        msg = entry.value
        if msg.is_empty():
            msg = next(
                (entry.properties[n] for n in sorted(entry.properties or {})
                 if not entry.properties[n].is_empty()),
                msg,
            )
        return fluent_serialize_message(PatternMessage(_simple_pattern(msg)))
    return "".join(_preview_part(p) for p in _simple_pattern(entry.value))


def _placeables(entry) -> Counter:
    """Every placeholder and markup element in a message, as Pontoon shows it.

    A typography fix moves spaces and punctuation around these; it never
    adds, drops or rewrites one. Counted, not listed: reordering them is a
    legitimate edit in a right-to-left or verb-final language.
    """
    out: Counter = Counter()
    messages = [entry.value, *(entry.properties or {}).values()]
    for msg in messages:
        patterns = [msg] if isinstance(msg, list) else (
            [msg.pattern] if isinstance(msg, PatternMessage)
            else list(msg.variants.values())
        )
        for pattern in patterns:
            for part in pattern:
                if isinstance(part, (Expression, Markup)):
                    out[_preview_part(part)] += 1
    return out


# --- reading files -----------------------------------------------------------

def _entries(path: str):
    """``{key: entry}`` for one resource, ``key`` being Pontoon's entity key."""
    res = parse_resource(path)
    out = {}
    for section in res.sections:
        # Pontoon does not import Android's sectioned entries (string arrays).
        if res.format == Format.android and section.id:
            continue
        for entry in section.entries:
            if isinstance(entry, Entry):
                out[tuple(section.id) + tuple(entry.id)] = entry
    return res, out


def _finding_key(project, rel: str, key: tuple) -> tuple[str, str]:
    """The ``(file, string_id)`` a finding uses for Pontoon key ``key``."""
    if project.data.get("layout") == "xliff":
        return ("/".join(key[:-1]), key[-1])
    return (rel, ".".join(key))


def changes(project, worklist: dict, l10n_dir: str) -> tuple[list[dict], list[str]]:
    """Every string edited in the work copies, and every reason to refuse them."""
    wdir = worklist["_dir"]
    by_key = {(w["file"], w["string_id"]): w for w in worklist["findings"]}
    extras = {(x["file"], x["string_id"]) for x in worklist.get("extras", [])}
    out, errors = [], []
    for localized, rels in sorted(worklist["files"].items()):
        orig_path = os.path.join(l10n_dir, localized)
        edit_path = os.path.join(wdir, "files", localized)
        try:
            res, edited = _entries(edit_path)
        except Exception as exc:  # noqa: BLE001 - reported, not raised
            errors.append(f"{localized}: edited copy does not parse: {exc}")
            continue
        _, original = _entries(orig_path)
        for key, entry in edited.items():
            before = original.get(key)
            if before is None:
                errors.append(f"{localized}: {'.'.join(key)} is not in the clone")
                continue
            if before.value == entry.value and before.properties == entry.properties:
                continue
            # For XLIFF one localized file holds many reference groups; for
            # every other layout it holds exactly one.
            rel = rels[0] if len(rels) == 1 else "/".join(key[:-1])
            fkey = _finding_key(project, rel, key)
            work = by_key.get(fkey)
            change = {
                "localized": localized,
                "file": fkey[0],
                "string_id": fkey[1],
                "key": list(key),
                "format": res.format.name,
                "old": pontoon_preview(res.format, before),
                "new": pontoon_preview(res.format, entry),
                "fids": [w["fid"] for w in worklist["findings"] if (w["file"], w["string_id"]) == fkey],
            }
            if work is None and fkey not in extras:
                errors.append(
                    f"{fkey[1]}: edited, but no finding in the worklist asks for it "
                    "(use `include` if a person wants it fixed anyway)"
                )
            if _placeables(before) != _placeables(entry):
                errors.append(
                    f"{fkey[1]}: placeholders or markup changed "
                    f"({dict(_placeables(before))} -> {dict(_placeables(entry))})"
                )
            out.append(change)
    return out, errors


# --- prepare -----------------------------------------------------------------

def cmd_prepare(args) -> int:
    project = config.load(args.project)
    category = args.category.upper()
    if category not in findings_mod.CATEGORIES:
        sys.exit(f"unknown category {category!r}; one of {', '.join(findings_mod.CATEGORIES)}")
    wdir = work_dir(project, args.locale, category)
    if os.path.exists(wdir):
        if not args.reset:
            sys.exit(f"{wdir} exists and may hold edits; pass --reset to start over")
        shutil.rmtree(wdir)

    source_dir = args.source_dir or args.l10n_dir
    trees = layout.load(project, args.locale, args.l10n_dir, source_dir)
    picked = [
        f for f in findings_mod.load(project, args.locale)
        if f.category == category and f.status in findings_mod.OPEN_STATUSES
    ]
    # Already suggested, by any path and in any status: not again.
    _, recorded = tracker.open_for(project, args.locale)
    done = tracker.strings(recorded)
    already = sorted({f.string_id for f in picked if f.key in done})
    picked = [f for f in picked if f.key not in done]

    work, files, missing = [], {}, []
    localized_of = _localized_resolver(project, trees, args.l10n_dir)
    for f in sorted(picked, key=lambda f: (f.file, f.string_id)):
        msg = trees.l10n.get(f.key)
        if msg is None:
            missing.append(f"{f.string_id} ({f.file})")
            continue
        src = trees.source.get(f.key)
        localized = localized_of(f.file)
        files.setdefault(localized, [])
        if f.file not in files[localized]:
            files[localized].append(f.file)
        work.append({
            "fid": f.fid,
            "check": f.check,
            "status": f.status,
            "impact": f.impact,
            "file": f.file,
            "string_id": f.string_id,
            "localized": localized,
            "summary": f.summary,
            "rationale": f.rationale,
            "current": f.current,
            "suggest": f.suggest,
            "source": src.text() if src else "",
            "translation": msg.text(),
            "line": msg.line,
            # The string moved since the finding was raised: the defect may
            # be gone, or the quote may no longer match. Read it again.
            "moved": bool(f.string_hash) and f.string_hash != msg.hash(),
        })

    os.makedirs(os.path.join(wdir, "files"), exist_ok=True)
    for localized in files:
        dest = os.path.join(wdir, "files", localized)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(args.l10n_dir, localized), dest)
    with open(os.path.join(wdir, "worklist.json"), "w", encoding="utf-8") as fh:
        json.dump({
            "project": project.name,
            "locale": args.locale,
            "category": category,
            "category_name": findings_mod.CATEGORIES[category],
            "l10n_dir": os.path.abspath(args.l10n_dir),
            "prepared": datetime.date.today().isoformat(),
            "source_dir": os.path.abspath(source_dir),
            "files": files,
            "findings": work,
            "extras": [],
        }, fh, ensure_ascii=False, indent=1)

    print(f"{len(work)} open {category} findings in {len(files)} files -> {wdir}")
    moved = sum(w["moved"] for w in work)
    if moved:
        print(f"  {moved} on strings that moved since the finding was raised")
    if missing:
        print(f"  {len(missing)} skipped, not in the clone: {', '.join(missing)}")
    if already:
        print(f"  {len(already)} skipped, already suggested "
              f"({os.path.relpath(tracker.path(project, args.locale))}): {', '.join(already)}")
    return 0


# --- include -----------------------------------------------------------------

def cmd_include(args) -> int:
    project = config.load(args.project)
    wdir = work_dir(project, args.locale, args.category.upper())
    worklist = _load_worklist(wdir)
    worklist.setdefault("extras", [])
    if not args.reason.strip():
        sys.exit("--reason is required: say why a string with no finding is being fixed")
    l10n_dir = worklist["l10n_dir"]
    trees = layout.load(project, args.locale, l10n_dir, worklist.get("source_dir") or l10n_dir)
    key = (args.file, args.string_id)
    if args.file is None:
        matches = [k for k in trees.l10n if k[1] == args.string_id]
        if len(matches) != 1:
            sys.exit(f"{args.string_id}: {len(matches)} matches in the clone; pass --file")
        key = matches[0]
    msg = trees.l10n.get(key)
    if msg is None:
        sys.exit(f"{args.string_id} is not in {args.file or 'the clone'}")
    if any((w["file"], w["string_id"]) == key for w in worklist["findings"]):
        sys.exit(f"{args.string_id} already has a finding in the worklist")
    if any((x["file"], x["string_id"]) == key for x in worklist["extras"]):
        print(f"{args.string_id} is already included")
        return 0
    if key in tracker.strings(tracker.open_for(project, args.locale)[1]):
        sys.exit(f"{args.string_id} already has a suggestion recorded in "
                 f"{tracker.path(project, args.locale)}")

    localized = _localized_resolver(project, trees, l10n_dir)(key[0])
    if localized not in worklist["files"]:
        dest = os.path.join(wdir, "files", localized)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(l10n_dir, localized), dest)
        worklist["files"][localized] = []
    if key[0] not in worklist["files"][localized]:
        worklist["files"][localized].append(key[0])
    src = trees.source.get(key)
    worklist["extras"].append({
        "file": key[0], "string_id": key[1], "localized": localized,
        "reason": args.reason.strip(),
        "source": src.text() if src else "", "translation": msg.text(),
    })
    with open(os.path.join(wdir, "worklist.json"), "w", encoding="utf-8") as fh:
        json.dump(worklist, fh, ensure_ascii=False, indent=1)
    print(f"included {key[1]} ({localized})")
    return 0


# --- diff --------------------------------------------------------------------

def _print_changes(found: list[dict], errors: list[str]) -> None:
    for c in found:
        print(f"{c['string_id']}  [{', '.join(c['fids']) or 'included, no finding'}]")
        print(f"  - {c['old']}")
        print(f"  + {c['new']}")
    for e in errors:
        print(f"ERROR {e}", file=sys.stderr)


def cmd_diff(args) -> int:
    project = config.load(args.project)
    wdir = work_dir(project, args.locale, args.category.upper())
    worklist = _load_worklist(wdir)
    worklist["_dir"] = wdir
    found, errors = changes(project, worklist, worklist["l10n_dir"])
    _print_changes(found, errors)
    addressed = {fid for c in found for fid in c["fids"]}
    untouched = [w for w in worklist["findings"] if w["fid"] not in addressed]
    print(f"\n{len(found)} strings changed; {len(untouched)} of "
          f"{len(worklist['findings'])} findings left untouched")
    return 1 if errors else 0


# --- upload ------------------------------------------------------------------

def _pontoon_target(project, rel: str) -> tuple[str, str]:
    """``(project slug, resource path)`` in Pontoon for reference path ``rel``."""
    conf = project.data.get("pontoon") or {}
    for p in conf.get("projects", []):
        if any(fnmatch(rel, pattern) for pattern in p.get("paths", ["*"])):
            return p["slug"], p.get("resource") or rel
    sys.exit(f"no Pontoon project in {project.name}/config.yaml matches {rel}")


def _get_json(url: str, token: str | None):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def pontoon_current(server: str, slug: str, resource: str, key: list, locale: str,
                    token: str | None) -> tuple[str | None, str]:
    """The approved translation in Pontoon, and why it could not be read if not."""
    url = (
        f"{server}/api/v2/entities/{slug}/{urllib.parse.quote(resource)}/"
        f"{urllib.parse.quote(key[-1], safe='')}/?include_translations=true"
    )
    try:
        data = _get_json(url, token)
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code} reading the entity"
    except urllib.error.URLError as exc:
        return None, f"cannot reach Pontoon: {exc.reason}"
    if data.get("key") != key:
        return None, f"Pontoon returned a different entity {data.get('key')}"
    for t in data.get("translations", []):
        if t["locale"]["code"] == locale:
            return t["string"], ""
    return None, "no approved translation in Pontoon"


def _multipart(fields: dict, filename: str, content: bytes) -> tuple[bytes, str]:
    boundary = uuid.uuid4().hex
    parts = []
    for name, value in fields.items():
        parts.append(
            f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n'
            f"{value}\r\n".encode()
        )
    parts.append(
        f'--{boundary}\r\nContent-Disposition: form-data; name="uploadfile"; '
        f'filename="{filename}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode()
        + content + b"\r\n"
    )
    parts.append(f"--{boundary}--\r\n".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def _partial_file(edit_path: str, keys: set[tuple]) -> str:
    """The edited resource with every entry but ``keys`` taken out."""
    res = parse_resource(edit_path)
    for section in res.sections:
        section.entries = [
            e for e in section.entries
            if isinstance(e, Entry) and tuple(section.id) + tuple(e.id) in keys
        ]
    res.sections = [s for s in res.sections if s.entries]
    return "".join(serialize_resource(res))


def upload(project, locale: str, wdir: str, found: list[dict], *, server: str,
           token: str | None, submit: bool, verify: bool = True,
           log=print, on_sent=None, known: tuple = ()) -> list[dict]:
    """Send ``found`` (from ``changes``) to Pontoon, one call per resource.

    Returns one record per resource: its Pontoon ``project`` and
    ``resource``, the changes it carried as ``items`` and, when submitted,
    Pontoon's ``result``. Strings Pontoon has moved past are logged as
    ``SKIP`` and left out. Without ``submit`` only the partial files are
    written. ``on_sent`` is called with each record as soon as Pontoon has
    answered for it, so a caller can persist what was published even if a
    later call dies.

    A string already in the locale's tracker -- or in one of the ``known``
    trackers -- is skipped, read from disk here rather than trusted from
    whenever the worklist was made: re-sending a suggestion a reviewer has
    since rejected would un-reject it in Pontoon.
    """
    # Group by Pontoon resource, dropping strings Pontoon has moved past.
    batches: dict[tuple[str, str, str], list[dict]] = {}
    skipped = []
    recorded = tracker.strings(tracker.open_for(project, locale)[1], *known)
    for c in found:
        if (c["file"], c["string_id"]) in recorded:
            skipped.append((c, "already suggested; listed in "
                               f"{os.path.relpath(tracker.path(project, locale))}"))
            continue
        slug, resource = _pontoon_target(project, c["file"])
        if verify:
            current, why = pontoon_current(
                server, slug, resource, c["key"], locale, token
            )
            if current is None:
                skipped.append((c, why))
                continue
            if current == c["new"]:
                skipped.append((c, "Pontoon already has this translation"))
                continue
            if current != c["old"]:
                skipped.append((c, f"Pontoon has moved on: {current}"))
                continue
        batches.setdefault((slug, resource, c["localized"]), []).append(c)

    for c, why in skipped:
        log(f"SKIP {c['string_id']}: {why}")

    out_dir = os.path.join(wdir, "upload")
    os.makedirs(out_dir, exist_ok=True)
    sent = []
    chunks = [
        (slug, resource, localized, items[i:i + UPLOAD_MAX_STRINGS], i // UPLOAD_MAX_STRINGS)
        for (slug, resource, localized), items in sorted(batches.items())
        for i in range(0, len(items), UPLOAD_MAX_STRINGS)
    ]
    for slug, resource, localized, items, part in chunks:
        content = _partial_file(
            os.path.join(wdir, "files", localized), {tuple(c["key"]) for c in items}
        )
        filename = os.path.basename(resource)
        partial = os.path.join(out_dir, *([f"part-{part + 1}"] if part else []),
                               slug, resource)
        os.makedirs(os.path.dirname(partial), exist_ok=True)
        with open(partial, "w", encoding="utf-8") as fh:
            fh.write(content)
        log(f"{slug} {resource}: {len(items)} suggestions")
        record = {"project": slug, "resource": resource, "items": items}
        sent.append(record)
        if not submit:
            continue
        # Paused before every call, not between them: a caller uploading
        # several locales in a row shares the same quota.
        time.sleep(UPLOAD_PAUSE_SECONDS)
        body, ctype = _multipart(
            {"project": slug, "locale": locale, "resource": resource},
            filename, content.encode("utf-8"),
        )
        req = urllib.request.Request(
            f"{server}/api/v2/upload/suggestions/", data=body, method="POST",
            headers={"Authorization": f"Bearer {token}", "Content-Type": ctype,
                     "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.load(resp)
        except urllib.error.HTTPError as exc:
            result = {"error": exc.code, "detail": exc.read().decode("utf-8", "replace")}
        except urllib.error.URLError as exc:
            result = {"error": "unreachable", "detail": str(exc.reason)}
        log(f"  {json.dumps(result, ensure_ascii=False)}")
        record["result"] = result
        if on_sent:
            on_sent(record)
    return sent


def refused(result: dict, key: list) -> str:
    """Why Pontoon did not store the suggestion for ``key``, or "" if it did."""
    if "error" in result:
        return f"upload failed: {result['error']}"
    for entry in result.get("failed_checks", []):
        if list(entry.get("key", [])) == list(key):
            return "failed Pontoon's checks: " + "; ".join(entry.get("errors", []))
    undefined = result.get("undefined_keys", [])
    if list(key) in [list(k) for k in undefined]:
        return "no such string in Pontoon"
    # Past 100 entries Pontoon only counts. A string missing from a truncated
    # list may still have been refused, so it is not claimed as stored.
    if (result.get("failed_checks_count", 0) > len(result.get("failed_checks", []))
            or result.get("undefined_keys_count", 0) > len(undefined)):
        return "Pontoon's answer was truncated; cannot tell whether it was stored"
    return ""


def _tracker_entry(worklist: dict, c: dict, record: dict, *, server: str,
                   date: str) -> dict:
    """The tracker record for change ``c``, sent in upload ``record``."""
    fkey = (c["file"], c["string_id"])
    works = [w for w in worklist["findings"] if (w["file"], w["string_id"]) == fkey]
    extras = [x for x in worklist.get("extras", []) if (x["file"], x["string_id"]) == fkey]
    return tracker.entry(
        date=date, group=worklist["category"], file=c["file"],
        string_id=c["string_id"], server=server, slug=record["project"],
        resource=record["resource"], key=c["key"],
        fids=[w["fid"] for w in works],
        findings=[w["summary"] for w in works]
        + [f"included without a finding: {x['reason']}" for x in extras],
        source=(works or extras)[0]["source"] if works or extras else "",
        original=c["old"], text=c["new"],
    )


def cmd_upload(args) -> int:
    project = config.load(args.project)
    category = args.category.upper()
    wdir = work_dir(project, args.locale, category)
    worklist = _load_worklist(wdir)
    worklist["_dir"] = wdir
    token = os.environ.get("PONTOON_TOKEN")
    if args.submit and not token:
        sys.exit("set PONTOON_TOKEN to a Personal Access Token from your Pontoon settings")

    found, errors = changes(project, worklist, worklist["l10n_dir"])
    if errors:
        _print_changes([], errors)
        sys.exit("refusing to upload: fix the errors `diff` reports first")
    if not found:
        print("nothing changed, nothing to upload")
        return 0

    tpath, recorded = tracker.open_for(project, args.locale)
    today = datetime.date.today().isoformat()

    def on_sent(record: dict) -> None:
        for c in record["items"]:
            why = refused(record["result"], c["key"])
            if why:
                print(f"  NOT STORED {c['string_id']}: {why}")
                continue
            tracker.add(recorded, _tracker_entry(
                worklist, c, record, server=args.server, date=today))
        tracker.save(tpath, recorded)

    sent = upload(project, args.locale, wdir, found, server=args.server,
                  token=token, submit=args.submit, verify=not args.no_verify,
                  on_sent=on_sent if args.submit else None)
    if not args.submit:
        print(f"\ndry run: partial files in {os.path.join(wdir, 'upload')}; "
              "pass --submit to send them")
        return 0
    log = [{"project": r["project"], "resource": r["resource"],
            "strings": [c["string_id"] for c in r["items"]],
            "fids": [f for c in r["items"] for f in c["fids"]],
            "result": r["result"]} for r in sent]
    with open(os.path.join(wdir, "uploaded.json"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": datetime.datetime.now().isoformat(timespec="seconds"),
                             "server": args.server, "uploads": log},
                            ensure_ascii=False) + "\n")
    return 1 if any("error" in entry["result"] for entry in log) else 0


# --- backfill ----------------------------------------------------------------

def _text(entry) -> str:
    """``Msg.text()`` for a bare entry: what ``worklist.json`` calls ``translation``."""
    props = {"": parse.flatten(entry.value)}
    for name, value in (entry.properties or {}).items():
        props[name] = parse.flatten(value)
    return parse.Msg(file="", id="", props=props).text()


def _entry_at(l10n_dir: str, localized: str, at: str, key: tuple):
    """The entry for ``key`` in the clone's last commit before ``at``, or None."""
    rev = subprocess.run(
        ["git", "-C", l10n_dir, "rev-list", "-1", f"--before={at}", "HEAD"],
        capture_output=True, text=True,
    ).stdout.strip()
    if not rev:
        return None
    shown = subprocess.run(["git", "-C", l10n_dir, "show", f"{rev}:{localized}"],
                           capture_output=True)
    if shown.returncode:
        return None
    suffix = os.path.splitext(localized)[1]
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "file" + suffix)
        with open(path, "wb") as fh:
            fh.write(shown.stdout)
        return _entries(path)[1].get(key)


def cmd_backfill(args) -> int:
    """Record suggestions submitted before the tracker existed.

    Rebuilt from each work directory's ``uploaded.json``: the submitted text
    from the partial file that was sent, which must agree with the edited
    copy, and the original from the clone's last commit before the upload,
    which must agree with the translation ``prepare`` saw. A string that
    fails either check is left out and listed, never guessed.
    """
    root = os.path.join(config.REPO_ROOT, "work", "suggestions")
    left_out = []
    for log in sorted(glob.glob(os.path.join(root, "*", "*", "*", "uploaded.json"))):
        wdir = os.path.dirname(log)
        project = config.load(os.path.relpath(wdir, root).split(os.sep)[0])
        worklist = _load_worklist(wdir)
        locale = worklist["locale"]
        tpath, recorded = tracker.open_for(project, locale)
        before = len(recorded["suggestions"])
        candidates = worklist["findings"] + worklist.get("extras", [])
        with open(log, encoding="utf-8") as fh:
            submissions = [json.loads(line) for line in fh if line.strip()]
        for sub in submissions:
            date = sub["at"][:10]
            for up in sub["uploads"]:
                slug, resource = up["project"], up["resource"]
                result = up["result"]
                _, partial = _entries(os.path.join(wdir, "upload", slug, resource))
                for sid in dict.fromkeys(up["strings"]):
                    def skip(why, sid=sid):
                        left_out.append(f"{project.name} {locale} {sid}: {why}")
                    works = [w for w in candidates if w["string_id"] == sid
                             and _pontoon_target(project, w["file"]) == (slug, resource)]
                    if not works:
                        skip("not in the worklist")
                        continue
                    fkey = (works[0]["file"], sid)
                    localized = works[0]["localized"]
                    keys = [k for k in partial
                            if _finding_key(project, fkey[0], k) == fkey]
                    if len(keys) != 1:
                        skip("not found in the partial file that was sent")
                        continue
                    key = keys[0]
                    if why := refused(result, list(key)):
                        skip(f"not stored: {why}")
                        continue
                    res_fmt = parse_resource(
                        os.path.join(wdir, "upload", slug, resource)).format
                    sent = pontoon_preview(res_fmt, partial[key])
                    edited = _entries(os.path.join(wdir, "files", localized))[1].get(key)
                    if edited is None or pontoon_preview(res_fmt, edited) != sent:
                        skip("the edited copy no longer matches what was sent")
                        continue
                    old = _entry_at(worklist["l10n_dir"], localized, sub["at"], key)
                    if old is None:
                        skip("no revision of the clone before the upload holds it")
                        continue
                    if _text(old) != works[0]["translation"]:
                        skip("the clone's history does not match what `prepare` saw")
                        continue
                    original = pontoon_preview(res_fmt, old)
                    if original == sent:
                        skip("the original equals what was sent")
                        continue
                    record = {"project": slug, "resource": resource}
                    change = {"file": fkey[0], "string_id": sid, "key": list(key),
                              "old": original, "new": sent}
                    tracker.add(recorded, _tracker_entry(
                        worklist, change, record, server=sub["server"], date=date))
        added = len(recorded["suggestions"]) - before
        if added and args.write:
            tracker.save(tpath, recorded)
        print(f"{os.path.relpath(wdir, root)}: {added} recorded")
    for line in left_out:
        print(f"LEFT OUT {line}")
    if not args.write:
        print("\ndry run: pass --write to save the records")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
    backfill = sub.add_parser(
        "backfill", help="record suggestions already submitted, from work/suggestions")
    backfill.add_argument("--write", action="store_true",
                          help="save the records; without it, only report")
    for name in ("prepare", "include", "diff", "upload"):
        p = sub.add_parser(name)
        p.add_argument("--project", required=True)
        p.add_argument("--locale", required=True)
        p.add_argument("--category", required=True, help="finding category, A-E")
        if name == "prepare":
            p.add_argument("--l10n-dir", required=True)
            p.add_argument("--source-dir", help="defaults to --l10n-dir")
            p.add_argument("--reset", action="store_true",
                           help="discard an existing work directory and its edits")
        if name == "include":
            p.add_argument("--string-id", required=True)
            p.add_argument("--file", help="reference path, if the id is not unique")
            p.add_argument("--reason", required=True,
                           help="why it is being fixed without a finding")
        if name == "upload":
            p.add_argument("--server", default=DEFAULT_SERVER)
            p.add_argument("--submit", action="store_true",
                           help="really upload; without it, a dry run")
            p.add_argument("--no-verify", action="store_true",
                           help="skip comparing each string with Pontoon first")
    args = ap.parse_args()
    return {"prepare": cmd_prepare, "include": cmd_include, "diff": cmd_diff,
            "upload": cmd_upload, "backfill": cmd_backfill}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
