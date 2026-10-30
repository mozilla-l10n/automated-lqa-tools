#!/usr/bin/env python3
"""Fix open findings with the model and submit the fixes to Pontoon.

The unattended counterpart of ``suggest.py``, where a person makes the
edits. Here the model gives every selected finding one verdict:

``fix``
    The edit is applied to a copy of the localized file, verified -- it must
    change the string, leave every placeholder and markup element in place
    and parse -- and sent to Pontoon as a suggestion through ``suggest.py``'s
    upload, which first drops any string Pontoon has moved past since the
    clone was pulled. Each suggestion Pontoon stores is recorded in
    ``<project>/pontoon_suggestions/<locale>.json`` with its review status,
    ``pending`` until somebody updates it.

``false_positive``
    The string is written to the locale's ``dismissed.txt`` with the model's
    reason, prefixed ``auto-suggest`` so it reads as what it is. A dismissal
    covers the whole string, so this happens only when every open finding on
    it -- in any group -- was judged a false positive. None of it takes
    effect until a person merges the pull request the workflow opens.

``skip``
    Nothing. The finding stays open and is offered again on the next run.

Without ``--submit`` nothing is sent and nothing in the repository is
written: the edits are shown, and the partial files are left under
``work/autosuggest/``. With it, suggestions are published under the
``PONTOON_TOKEN`` owner's account, which cannot be undone from here.

``absorb`` folds the tracker records and dismissals produced elsewhere (the
workflow's per-locale jobs) into this tree, adding and never removing.
``summary`` writes the pull request body: what this tree records that a base
ref does not, dismissals first, because those are what a person must read.
"""

from __future__ import annotations

import argparse
import copy
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import anthropic  # noqa: E402

import config  # noqa: E402
import local_secrets  # noqa: E402
import dismiss  # noqa: E402
import findings as findings_mod  # noqa: E402
import layout  # noqa: E402
import suggest  # noqa: E402
import tracker  # noqa: E402
from llm_incremental import _call, _close, language_of  # noqa: E402

from moz.l10n.model import PatternMessage  # noqa: E402
from moz.l10n.resource import serialize_resource  # noqa: E402

PROJECTS = ("android", "firefox", "firefox_ios")
BATCH_SIZE = 10
DISMISS_TAG = "auto-suggest"

# Shown to the model as JSON escapes: raw, they are invisible in the prompt
# and the model is told to write them back the same way.
_INVISIBLE = {
    " ": "\\u00a0", " ": "\\u202f", " ": "\\u2009",
    "​": "\\u200b", "‌": "\\u200c", "‍": "\\u200d",
    "‎": "\\u200e", "‏": "\\u200f", "⁠": "\\u2060",
}


# --- dismissals --------------------------------------------------------------

def _dismissed(entries: dict, f) -> bool:
    """Whether ``dismissed.txt`` already covers finding ``f`` (as ``dismiss.apply``)."""
    return any(
        f.string_id == sid and (not where or where in f.file)
        for sid, where in entries
    )


def _dismiss_line(f, reason: str, today: str) -> str:
    return dismiss.line(f.string_id, f.file, DISMISS_TAG, today, reason)


append_dismissals = dismiss.append


# --- editing a parsed message ------------------------------------------------

def _patterns(entry) -> list[list]:
    """Every pattern of a message -- value, attributes, plural variants."""
    out = []
    for msg in [entry.value, *(entry.properties or {}).values()]:
        if isinstance(msg, list):
            out.append(msg)
        elif isinstance(msg, PatternMessage):
            out.append(msg.pattern)
        else:
            out.extend(msg.variants.values())
    return out


def apply_edits(entry, edits: list[dict]) -> str:
    """Apply ``edits`` to the text parts of ``entry`` in place.

    Returns "" on success or why it refused, in which case ``entry`` may be
    half-edited and the caller must restore it. Matching is literal and per
    text part, so a fragment spanning a placeholder never matches.
    """
    if not edits:
        return "no edits supplied"
    for e in edits:
        find, replace = e["find"], e["replace"]
        if not find:
            return "empty `find`"
        if find == replace:
            return f"edit {find!r} changes nothing"
        parts = [(p, i) for p in _patterns(entry) for i, part in enumerate(p)
                 if isinstance(part, str)]
        count = sum(p[i].count(find) for p, i in parts)
        if count == 0:
            return f"{find!r} is not in the text"
        if count != e["occurrences"]:
            return f"{find!r} occurs {count} times, the edit expected {e['occurrences']}"
        for p, i in parts:
            p[i] = p[i].replace(find, replace)
    return ""


_NAMES = {
    "\u00a0": "<NBSP>", "\u202f": "<NNBSP>", "\u2009": "<THINSP>",
    "\u200b": "<ZWSP>", "\u200c": "<ZWNJ>", "\u200d": "<ZWJ>",
    "\u200e": "<LRM>", "\u200f": "<RLM>", "\u2060": "<WJ>",
}


# --- the model ---------------------------------------------------------------

def _shown(value):
    text = json.dumps(value, ensure_ascii=False, indent=1)
    for char, escape in _INVISIBLE.items():
        text = text.replace(char, escape)
    return text


def render_batch(items: list[dict]) -> str:
    blocks = []
    for ref, item in enumerate(items, 1):
        blocks.append(f"### String {ref}\n\n```json\n" + _shown({
            "ref": ref,
            "file": item["file"],
            "string_id": item["string_id"],
            "source_en_US": item["source"],
            "translation": item["translation"],
            "findings": [
                {
                    "fid": f.fid,
                    "group": f.category,
                    "impact": f.impact,
                    "summary": f.summary,
                    "quoted": f.current,
                    "reviewer_suggests": f.suggest,
                    "rationale": f.rationale,
                    **({"note": "the string changed after this finding was raised; "
                                "the defect may be gone and the quote may not match"}
                       if item["moved"].get(f.fid) else {}),
                }
                for f in item["findings"]
            ],
        }) + "\n```")
    return "\n\n".join(blocks)


def system_prompt(project, locale: str, groups: list[str]) -> str:
    with open(os.path.join(os.path.dirname(__file__), "prompts", "fix_findings.md"),
              encoding="utf-8") as fh:
        template = fh.read()
    measured_path = os.path.join(project.state_dir(locale), "conventions.json")
    measured = "{}"
    if os.path.exists(measured_path):
        with open(measured_path, encoding="utf-8") as fh:
            measured = fh.read().strip()
    return template.format(
        language=language_of(locale),
        locale=locale,
        groups="\n".join(f"- **{g}** — {findings_mod.CATEGORIES[g]}" for g in groups),
        conventions=project.conventions(locale).strip()
        or "_No conventions recorded yet for this locale._",
        measured=measured,
    )


def _tool() -> dict:
    with open(os.path.join(os.path.dirname(__file__), "prompts", "fix_schema.json"),
              encoding="utf-8") as fh:
        tool = json.load(fh)
    _close(tool["input_schema"])
    return {**tool, "strict": True}


def ask(client, project, system: str, items: list[dict]) -> dict[int, dict]:
    """``{ref: answer}`` for one batch; strings with no readable answer are absent."""
    cfg = project.llm
    response = _call(client, cfg["model"], system, render_batch(items), _tool(),
                     int(cfg.get("max_output_tokens", 16000)),
                     effort=cfg.get("effort"))
    for block in response.content:
        if getattr(block, "type", "") == "tool_use" and block.name == "report_fixes":
            return {s["ref"]: s for s in block.input.get("strings", [])
                    if isinstance(s.get("ref"), int)}
    return {}


# --- one locale --------------------------------------------------------------

def _paths(values: list[str], projects: list[str], what: str) -> dict[str, str]:
    """``--l10n-dir``/``--source-dir`` values, as ``{project: path}``."""
    out = {}
    for v in values or []:
        name, sep, path = v.partition("=")
        if sep and name in PROJECTS:
            out[name] = path
        elif len(projects) == 1:
            out[projects[0]] = v
        else:
            sys.exit(f"{what} {v!r}: with several projects, write it as project=PATH")
    return out


def run_locale(project, locale: str, groups: list[str], l10n_dir: str,
               source_dir: str, args, client, known: list[dict]) -> int:
    """Fix, verify and (with --submit) send one locale. Returns an error count."""
    today = datetime.date.today().isoformat()
    print(f"\n== {project.name} {locale} ({', '.join(groups)})")
    if project.pontoon_readonly(locale):
        # Before the model is asked anything: a run that could only dismiss
        # would hide findings for a locale nobody can fix through Pontoon.
        print(f"  read-only in Pontoon ({project.name}/config.yaml); skipped")
        return 0
    all_findings = findings_mod.load(project, locale)
    open_findings = [f for f in all_findings if f.status in findings_mod.OPEN_STATUSES]
    tpath, record_data = tracker.open_for(project, locale)
    # A string already in the tracker is never suggested again, whatever its
    # status: pending is waiting on a reviewer, approved is done, and
    # rejected was a person's answer.
    done = tracker.strings(record_data, *known)
    dismissed = dismiss.load(project, locale)

    picked = [f for f in open_findings if f.category in groups]
    candidates = [f for f in picked if f.key not in done and not _dismissed(dismissed, f)]
    if len(candidates) < len(picked):
        print(f"  {len(picked) - len(candidates)} already suggested or dismissed")
    if not candidates:
        print("  nothing to do")
        return 0

    trees = layout.load(project, locale, l10n_dir, source_dir)
    localized_of = suggest._localized_resolver(project, trees, l10n_dir)
    wdir = os.path.join(config.REPO_ROOT, "work", "autosuggest", project.name, locale)
    shutil.rmtree(wdir, ignore_errors=True)

    by_string: dict[tuple, list] = {}
    for f in candidates:
        by_string.setdefault(f.key, []).append(f)
    items, files, unusable = [], {}, []
    for key, fs in sorted(by_string.items()):
        msg, src = trees.l10n.get(key), trees.source.get(key)
        if msg is None or src is None:
            # No source: never review a string whose English we have not got.
            unusable.append(f"{key[1]} ({'not in the clone' if msg is None else 'no en-US'})")
            continue
        localized = localized_of(key[0])
        files.setdefault(localized, [])
        if key[0] not in files[localized]:
            files[localized].append(key[0])
        items.append({
            "file": key[0], "string_id": key[1], "localized": localized,
            "source": src.text(), "translation": msg.text(), "findings": fs,
            "moved": {f.fid: bool(f.string_hash) and f.string_hash != msg.hash() for f in fs},
        })
    if unusable:
        print(f"  {len(unusable)} string(s) left out: {', '.join(unusable)}")
    if not items:
        return 0

    # Parsed copies of each localized file, edited in memory.
    resources = {}
    for localized in files:
        dest = os.path.join(wdir, "files", localized)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(l10n_dir, localized), dest)
        resources[localized] = suggest._entries(dest)

    def locate(item):
        rels = files[item["localized"]]
        _, entries = resources[item["localized"]]
        for k, entry in entries.items():
            rel = rels[0] if len(rels) == 1 else "/".join(k[:-1])
            if suggest._finding_key(project, rel, k) == (item["file"], item["string_id"]):
                return entry
        return None

    system = system_prompt(project, locale, groups)
    errors = 0
    fixed, dismissals, skipped = [], [], []
    batch_size = args.batch_size
    for start in range(0, len(items), batch_size):
        batch = items[start:start + batch_size]
        print(f"  asking about strings {start + 1}-{start + len(batch)} of {len(items)}")
        try:
            answers = ask(client, project, system, batch)
        except Exception as exc:  # noqa: BLE001 - keep going with the next batch
            print(f"  model call failed, batch left for next time: {exc}")
            errors += 1
            continue
        for ref, item in enumerate(batch, 1):
            answer = answers.get(ref)
            fids = {f.fid for f in item["findings"]}
            verdicts = {v["fid"]: v for v in (answer or {}).get("findings", [])
                        if v.get("fid") in fids}
            if set(verdicts) != fids:
                skipped.append((item, "the model did not give a verdict on every finding"))
                continue
            to_fix = [fid for fid, v in verdicts.items() if v["verdict"] == "fix"]
            if to_fix:
                entry = locate(item)
                if entry is None:
                    skipped.append((item, "Pontoon does not import this entry"))
                    continue
                saved = (copy.deepcopy(entry.value), copy.deepcopy(entry.properties))
                before = suggest._placeables(entry)
                why = apply_edits(entry, answer["edits"])
                if not why and suggest._placeables(entry) != before:
                    why = "the edit changed a placeholder or markup"
                if not why and (entry.value, entry.properties) == saved:
                    why = "the edit left the string as it was"
                if why:
                    entry.value, entry.properties = saved
                    skipped.append((item, f"edit refused: {why}"))
                    continue
                item["fix_fids"] = to_fix
                fixed.append(item)
            others = [f for f in open_findings if f.key == (item["file"], item["string_id"])
                      and f.fid not in fids]
            if not to_fix and all(v["verdict"] == "false_positive" for v in verdicts.values()):
                if others:
                    skipped.append((item, "judged a false positive, but the string has "
                                          f"{len(others)} other open finding(s)"))
                else:
                    reason = "; ".join(v["reason"] for v in verdicts.values())
                    dismissals.append((item, _dismiss_line(item["findings"][0], reason, today)))
            for fid, v in verdicts.items():
                if v["verdict"] == "skip":
                    skipped.append((item, f"{fid} skipped: {v['reason']}"))

    for localized, (res, _) in resources.items():
        with open(os.path.join(wdir, "files", localized), "w", encoding="utf-8") as fh:
            fh.write("".join(serialize_resource(res)))

    # The same guard a person's edits go through.
    worklist = {
        "_dir": wdir, "files": files, "extras": [],
        "findings": [{"fid": f.fid, "file": i["file"], "string_id": i["string_id"]}
                     for i in fixed for f in i["findings"] if f.fid in i["fix_fids"]],
    }
    found, problems = suggest.changes(project, worklist, l10n_dir)
    suggest._print_changes(found, problems)
    if problems:
        print("  refusing to upload this locale: the edits failed verification")
        return errors + 1

    for item, line in dismissals:
        print(f"DISMISS {line}")
    for item, why in skipped:
        print(f"LEAVE {item['string_id']}: {why}")

    token = os.environ.get("PONTOON_TOKEN")
    source_of = {(i["file"], i["string_id"]): i for i in fixed}

    def record(sent: dict) -> None:
        nonlocal errors
        result = sent["result"]
        for c in sent["items"]:
            why = suggest.refused(result, c["key"])
            if why:
                print(f"  NOT STORED {c['string_id']}: {why}")
                errors += 1
                continue
            item = source_of[(c["file"], c["string_id"])]
            used = [f for f in item["findings"] if f.fid in item["fix_fids"]]
            tracker.add(record_data, tracker.entry(
                date=today, group="".join(sorted({f.category for f in used})),
                file=c["file"], string_id=c["string_id"], server=args.server,
                slug=sent["project"], resource=sent["resource"], key=c["key"],
                fids=[f.fid for f in used], findings=[f.summary for f in used],
                source=item["source"], original=c["old"], text=c["new"],
            ))
        tracker.save(tpath, record_data)

    sent = []
    if found:
        sent = suggest.upload(project, locale, wdir, found, server=args.server,
                              token=token, submit=args.submit,
                              on_sent=record if args.submit else None,
                              known=tuple(known))
    if args.submit:
        added = append_dismissals(dismiss.path(project, locale),
                                  [line for _, line in dismissals])
        print(f"  {added} dismissal(s) written to {dismiss.path(project, locale)}")
    print(f"  {sum(len(r['items']) for r in sent)} of {len(found)} fix(es) "
          f"{'sent' if args.submit else 'ready to send'}, "
          f"{len(dismissals)} dismissal(s), {len(skipped)} left open")
    return errors


def cmd_run(args) -> int:
    projects = list(PROJECTS) if args.project == "all" else [args.project]
    groups = (list(findings_mod.CATEGORIES) if args.group.lower() == "all"
              else [g.strip().upper() for g in args.group.split(",") if g.strip()])
    unknown = [g for g in groups if g not in findings_mod.CATEGORIES]
    if unknown:
        sys.exit(f"unknown group {', '.join(unknown)}; one of "
                 f"{', '.join(findings_mod.CATEGORIES)} or all")
    l10n_dirs = _paths(args.l10n_dir, projects, "--l10n-dir")
    source_dirs = _paths(args.source_dir, projects, "--source-dir")
    missing = [p for p in projects if p not in l10n_dirs]
    if missing:
        sys.exit(f"--l10n-dir is needed for {', '.join(missing)}")
    if args.submit and not os.environ.get("PONTOON_TOKEN"):
        sys.exit("set PONTOON_TOKEN to a Personal Access Token from your Pontoon settings")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("fixing findings needs ANTHROPIC_API_KEY")
    known = [tracker.load(p) for p in args.known or []]
    client = anthropic.Anthropic()

    requested = None if args.locales.lower() == "all" else [
        x.strip() for x in args.locales.split(",") if x.strip()
    ]
    errors = 0
    for name in projects:
        project = config.load(name)
        if requested is None:
            locales = project.locales
        else:
            locales = [x for x in requested if x in project.locales]
            if len(locales) < len(requested):
                print(f"{name}: not configured for "
                      f"{', '.join(x for x in requested if x not in project.locales)}")
        for locale in locales:
            errors += run_locale(project, locale, groups, l10n_dirs[name],
                                 source_dirs.get(name, l10n_dirs[name]), args,
                                 client, known)
    if not args.submit:
        print("\ndry run: nothing sent and nothing written; pass --submit to send")
    return 1 if errors else 0


# --- absorb ------------------------------------------------------------------

def cmd_absorb(args) -> int:
    """Fold trackers and dismissals from other trees into this one."""
    for src in args.sources:
        for path in sorted(glob.glob(os.path.join(src, "*", tracker.TRACKER_DIR, "*.json"))):
            rel = os.path.relpath(path, src)
            dest = os.path.join(config.REPO_ROOT, rel)
            incoming, current = tracker.load(path), tracker.load(dest)
            for key in ("project", "locale"):
                current.setdefault(key, incoming.get(key))
            new = [s for s in incoming["suggestions"] if tracker.add(current, s)]
            if new:
                tracker.save(dest, current)
            print(f"{rel}: {len(new)} new suggestion(s)")
        for path in sorted(glob.glob(os.path.join(src, "*", "locales", "*", "dismissed.txt"))):
            rel = os.path.relpath(path, src)
            with open(path, encoding="utf-8") as fh:
                lines = [line.rstrip("\n") for line in fh
                         if line.strip() and not line.lstrip().startswith("#")]
            added = append_dismissals(os.path.join(config.REPO_ROOT, rel), lines)
            print(f"{rel}: {added} new dismissal(s)")
    return 0


# --- summary -----------------------------------------------------------------

# GitHub refuses a pull request body over 65,536 characters.
BODY_LIMIT = 60000


def _code(text: str) -> str:
    """``text`` as an inline code span, invisible characters named."""
    for char, name in _NAMES.items():
        text = text.replace(char, name)
    text = " ".join(text.split("\n"))
    fence = "`"
    while fence in text:
        fence += "`"
    return f"{fence} {text} {fence}" if text.startswith("`") or text.endswith("`") \
        else f"{fence}{text}{fence}"


def _at(ref: str, path: str) -> str:
    rel = os.path.relpath(path, config.REPO_ROOT)
    out = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=config.REPO_ROOT,
                         capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def cmd_summary(args) -> int:
    """A pull request body: what this branch records that ``--base`` does not."""
    project = config.load(args.project)
    dismissals, suggestions = {}, {}
    for path in sorted(glob.glob(os.path.join(project.root, "locales", "*", "dismissed.txt"))):
        locale = os.path.basename(os.path.dirname(path))
        before = {line.strip() for line in _at(args.base, path).splitlines()}
        with open(path, encoding="utf-8") as fh:
            new = [line.strip() for line in fh
                   if DISMISS_TAG in line and line.strip() not in before]
        if new:
            dismissals[locale] = new
    for path in sorted(glob.glob(os.path.join(project.root, tracker.TRACKER_DIR, "*.json"))):
        locale = os.path.splitext(os.path.basename(path))[0]
        old = _at(args.base, path)
        have = {tracker.identity(s) for s in json.loads(old)["suggestions"]} if old else set()
        new = [s for s in tracker.load(path)["suggestions"]
               if tracker.identity(s) not in have]
        if new:
            suggestions[locale] = new

    def link(rel: str) -> str:
        return f"[`{rel}`]({args.link_base.rstrip('/')}/{rel})" if args.link_base \
            else f"`{rel}`"

    head = [f"# Pontoon suggestions: {project.display_name}", ""]
    head.append(
        "The model was asked to fix open findings. Fixes it made were verified "
        "and **have already been submitted to Pontoon** as suggestions, where "
        "the locale's reviewers accept or reject them; merging this records "
        f"them in `{project.name}/{tracker.TRACKER_DIR}/`. Findings it judged false "
        "positives are added to `dismissed.txt`, and are hidden once this is "
        "merged. The workflow merges it **as soon as its checks pass**; to "
        "undo a dismissal afterwards, delete its line."
    )
    head.append("")

    # Each section is (heading, [(locale, rel, [item, ...])]); an item is one
    # dismissal or suggestion as a block of lines. Items are added in order,
    # dismissals first, while the whole body stays under the limit; whatever
    # does not fit is counted per locale and linked instead. Room for those
    # notes is set aside up front so adding them cannot break the limit.
    sections = []
    groups = []
    for locale, lines in dismissals.items():
        by_string = {}
        for f in findings_mod.load(project, locale):
            if f.status in findings_mod.OPEN_STATUSES:
                by_string.setdefault((f.string_id, f.file), []).append(f)
        items = []
        for line in lines:
            target, _, reason = line.partition(" — ")
            sid, _, where = target.partition(" @ ")
            item = [f"- {_code(sid)} in {_code(where)}"]
            for f in by_string.get((sid, where), []):
                item.append(f"  - finding ({f.category}): {f.summary}")
            item.append(f"  - **why dismissed:** {reason.split(': ', 1)[-1]}")
            items.append(item)
        groups.append((locale, f"{project.name}/locales/{locale}/dismissed.txt", items))
    sections.append(("Dismissals to review", groups))
    groups = []
    for locale, entries in suggestions.items():
        items = [[f"- {_code(s['string_id'])} ({s['group']}): " + "; ".join(s["findings"]),
                  f"  - before: {_code(s['original'])}",
                  f"  - after: {_code(s['text'])}"] for s in entries]
        groups.append((locale, f"{project.name}/{tracker.TRACKER_DIR}/{locale}.json", items))
    sections.append(("Submitted suggestions", groups))

    reserve = 200 + sum(300 for _, gs in sections for _ in gs)
    budget = BODY_LIMIT - reserve - sum(len(x) + 1 for x in head)
    out = list(head)
    full = False
    for title, gs in sections:
        out += [f"## {title} ({sum(len(items) for _, _, items in gs)})", ""]
        if not gs:
            out += ["None.", ""]
        omitted = []
        for locale, rel, items in gs:
            shown = []
            for item in items:
                size = sum(len(x) + 1 for x in item)
                # Once one item is cut, so is everything after it: a smaller
                # one squeezed in further down would read as complete.
                if full or size > budget:
                    full = True
                    break
                budget -= size
                shown.append(item)
            if shown:
                if title.startswith("Submitted"):
                    out += [f"<details><summary>{locale}: {len(items)}</summary>", ""]
                else:
                    out += [f"### {locale}", ""]
                for item in shown:
                    out += item
                out += ["", "</details>", ""] if title.startswith("Submitted") else [""]
            if len(shown) < len(items):
                omitted.append(f"- {locale}: {len(items) - len(shown)} more in {link(rel)}")
        if omitted:
            out += ["Not listed here, for length (GitHub caps the description):", "",
                    *omitted, ""]
    print("\n".join(out))
    return 0


def main() -> int:
    local_secrets.load("ANTHROPIC_API_KEY", "PONTOON_TOKEN")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="fix findings and submit them")
    run.add_argument("--project", required=True, choices=[*PROJECTS, "all"])
    run.add_argument("--locales", default="all", help='comma-separated, or "all"')
    run.add_argument("--group", default="all", help='finding group A-E, comma-separated, or "all"')
    run.add_argument("--l10n-dir", action="append",
                     help="the clone; with --project all, repeat as project=PATH")
    run.add_argument("--source-dir", action="append",
                     help="the en-US clone where it differs (firefox); project=PATH form too")
    run.add_argument("--known", action="append",
                     help="another tracker file whose strings count as already suggested")
    run.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    run.add_argument("--server", default=suggest.DEFAULT_SERVER)
    run.add_argument("--submit", action="store_true",
                     help="really submit and record; without it, a dry run")
    absorb = sub.add_parser("absorb", help="merge trackers and dismissals from other trees")
    absorb.add_argument("sources", nargs="+", help="directories laid out like the repository")
    summary = sub.add_parser("summary", help="pull request body for what --base lacks")
    summary.add_argument("--project", required=True, choices=PROJECTS)
    summary.add_argument("--base", default="origin/main", help="git ref to compare with")
    summary.add_argument("--link-base",
                         help="URL that repository paths are appended to, for omitted items")
    args = ap.parse_args()
    return {"run": cmd_run, "absorb": cmd_absorb, "summary": cmd_summary}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
