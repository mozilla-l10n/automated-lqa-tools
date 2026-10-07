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
import json
import os
import shutil
import sys
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

    # Group by Pontoon resource, dropping strings Pontoon has moved past.
    batches: dict[tuple[str, str, str], list[dict]] = {}
    skipped = []
    for c in found:
        slug, resource = _pontoon_target(project, c["file"])
        if not args.no_verify:
            current, why = pontoon_current(
                args.server, slug, resource, c["key"], args.locale, token
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
        print(f"SKIP {c['string_id']}: {why}")

    out_dir = os.path.join(wdir, "upload")
    os.makedirs(out_dir, exist_ok=True)
    log = []
    for n, ((slug, resource, localized), items) in enumerate(sorted(batches.items())):
        content = _partial_file(
            os.path.join(wdir, "files", localized), {tuple(c["key"]) for c in items}
        )
        filename = os.path.basename(resource)
        partial = os.path.join(out_dir, slug, resource)
        os.makedirs(os.path.dirname(partial), exist_ok=True)
        with open(partial, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"{slug} {resource}: {len(items)} suggestions")
        if not args.submit:
            continue
        if n:
            time.sleep(UPLOAD_PAUSE_SECONDS)
        body, ctype = _multipart(
            {"project": slug, "locale": args.locale, "resource": resource},
            filename, content.encode("utf-8"),
        )
        req = urllib.request.Request(
            f"{args.server}/api/v2/upload/suggestions/", data=body, method="POST",
            headers={"Authorization": f"Bearer {token}", "Content-Type": ctype,
                     "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.load(resp)
        except urllib.error.HTTPError as exc:
            result = {"error": exc.code, "detail": exc.read().decode("utf-8", "replace")}
        print(f"  {json.dumps(result, ensure_ascii=False)}")
        log.append({"project": slug, "resource": resource,
                    "strings": [c["string_id"] for c in items],
                    "fids": [f for c in items for f in c["fids"]], "result": result})

    if not args.submit:
        print(f"\ndry run: partial files in {out_dir}; pass --submit to send them")
        return 0
    with open(os.path.join(wdir, "uploaded.json"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": datetime.datetime.now().isoformat(timespec="seconds"),
                             "server": args.server, "uploads": log},
                            ensure_ascii=False) + "\n")
    return 1 if any("error" in entry["result"] for entry in log) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
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
            "upload": cmd_upload}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
