"""Per-finding dismissals: "I looked at this one, it is fine."

A suppression rule describes a *class* -- every access key, every finding
quoting `critta`. It needs an id, a reason and a match expression, and
getting the scope wrong either hides real defects or fails to hide the one
you meant. That is the right amount of ceremony for a rule that will apply
to strings nobody has written yet, and far too much for a single string a
reviewer has read and judged acceptable.

So dismissals are a separate, deliberately dull file: one line per string,
in `locales/<code>/dismissed.txt`.

    browser_menu_summarize_page_badge — deliberate wording, confirmed

The reason after the dash is free text and is kept with the finding, so the
report can say why it was dropped. Where a string id occurs in more than one
file, qualify it:

    recent_tabs_header @ mozilla-mobile/fenix/... — fine in this context

Like suppression rules, the file is re-applied to the whole backlog on every
run, so adding a line retires a finding raised months ago and deleting one
brings it straight back. Nothing is deleted from `findings.json`; the
dismissal is recorded on the finding with its reason.
"""

from __future__ import annotations

import os
import re

# Any of these separates the string from the reason, so nobody has to
# remember which dash to type.
_SEPARATORS = ("—", " -- ", " – ", " - ")

# Written by the Pontoon suggestions workflow (`autosuggest`) when its model
# judged a finding wrong or could not confirm it. No person decided those,
# so they are counted apart from dismissals that a person made -- in
# Pontoon (`pontoon-rejected`) or by hand -- and they carry the hash of the
# string they were judged on, so they lapse when it changes (`withdraw_moved`).
FIXER_TAG = "auto-suggest"
_FIXER = re.compile(rf"^{FIXER_TAG} \((?P<date>\d{{4}}-\d{{2}}-\d{{2}})"
                    r"(?:, string (?P<hash>[0-9a-f]+))?\): ")


def path(project, locale: str) -> str:
    return os.path.join(project.locale_dir(locale), "dismissed.txt")


def load(project, locale: str) -> dict[tuple[str, str | None], str]:
    """``{(string_id, file_or_None): reason}`` from the locale's file."""
    p = path(project, locale)
    if not os.path.exists(p):
        return {}
    entries: dict[tuple[str, str | None], str] = {}
    with open(p, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            reason = ""
            for sep in _SEPARATORS:
                if sep in line:
                    line, reason = line.split(sep, 1)
                    break
            target, _, where = line.partition("@")
            entries[(target.strip(), where.strip() or None)] = reason.strip()
    return entries


def line(string_id: str, file: str, tag: str, date: str, reason: str,
         anchor: str = "") -> str:
    """A dismissal written by a tool, ``tag`` saying which one and ``date`` when.

    ``anchor`` is the hash of the string the judgement was made on, for a
    dismissal that should lapse once the string changes.
    """
    reason = " ".join(reason.split())
    when = f"{date}, string {anchor}" if anchor else date
    return f"{string_id} @ {file} — {tag} ({when}): {reason}"


def by_fixer(reason: str) -> bool:
    """Whether a finding's dismissal reason was written by the fixer model."""
    return bool(_FIXER.match(reason or ""))


def withdraw_moved(path: str, messages: dict, write: bool = True) -> list[str]:
    """Remove the fixer's dismissals whose string has changed; return them.

    The fixer judged one text. A dismissal keyed by string id alone would go
    on hiding every finding on that string, raised on any later text, for
    good -- so once the string moves, the line goes and the string is
    reviewed like any other. A line without an anchor, or for a string no
    longer in the tree, is left alone; a person's line is never touched.
    """
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    gone = []
    for raw in lines:
        text = raw.strip()
        head, sep, reason = text.partition(" — ")
        m = _FIXER.match(reason) if sep else None
        if not m or not m["hash"]:
            continue
        sid, _, where = head.partition(" @ ")
        msg = messages.get((where.strip(), sid.strip()))
        if msg is not None and msg.hash() != m["hash"]:
            gone.append(text)
    if gone and write:
        drop = set(gone)
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(x for x in lines if x.strip() not in drop)
    return gone


def append(path: str, lines: list[str]) -> int:
    """Add the lines ``path`` does not already hold; return how many."""
    existing = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            existing = {line.strip() for line in fh}
    new = [line for line in lines if line.strip() not in existing]
    if not new:
        return 0
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fresh = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as fh:
        if fresh:
            fh.write(TEMPLATE)
        for line in new:
            fh.write(line + "\n")
    return len(new)


def remove(path: str, prefixes: list[str]) -> int:
    """Delete the lines starting with any of ``prefixes``; return how many.

    Only ever called with a tool's own tag in the prefix, so a line a person
    wrote is never touched.
    """
    if not prefixes or not os.path.exists(path):
        return 0
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    kept = [x for x in lines if not x.strip().startswith(tuple(prefixes))]
    if len(kept) == len(lines):
        return 0
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(kept)
    return len(lines) - len(kept)


def apply(entries: dict, findings: list) -> dict[str, int]:
    """Mark listed findings dismissed, and restore ones no longer listed."""
    counts: dict[str, int] = {}
    for f in findings:
        if f.status in ("fixed", "obsolete", "suppressed"):
            continue
        reason = None
        for (string_id, where), why in entries.items():
            if f.string_id != string_id:
                continue
            if where and where not in f.file:
                continue
            reason = why or "no reason recorded"
            break
        if reason is not None:
            f.status = "dismissed"
            f.dismissed_because = reason
            counts[f.string_id] = counts.get(f.string_id, 0) + 1
        elif f.status == "dismissed":
            # The line was removed: put the finding back in view.
            f.status = "open"
            f.dismissed_because = ""
    return counts


TEMPLATE = """\
# Findings you have read and judged acceptable, one per line.
#
#   <string-id> — <why>
#
# Where the same id exists in more than one file, qualify it:
#
#   <string-id> @ <part of the path> — <why>
#
# Re-applied to the whole backlog on every run: adding a line retires a
# finding raised months ago, and deleting one brings it straight back.
# Nothing is lost -- dismissed findings stay in state/ and are listed in the
# report appendix with the reason.
#
# This is for *one string you have looked at*. For something that will keep
# recurring across strings -- a house convention, a term that is correct
# everywhere -- write a rule in suppressions.yaml instead, or better, a
# sentence in conventions.md so the reviewer never raises it.
"""
