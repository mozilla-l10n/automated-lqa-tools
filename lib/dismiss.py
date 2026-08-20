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

# Any of these separates the string from the reason, so nobody has to
# remember which dash to type.
_SEPARATORS = ("—", " -- ", " – ", " - ")


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
