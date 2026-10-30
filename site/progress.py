"""The landing page's findings chart: what QA raised each week, and what got fixed.

Read from ``<project>/state/<locale>/findings.json`` at build time. Only
weekly counts leave this module -- no finding, string or quote from
``state/`` reaches the published site, which is built from ``_site/`` alone.

A finding counts as **raised** in the week of its ``first_seen`` and as
**fixed** in the week of its ``resolved_on``, and only if its status is
``fixed``: the string changed and the defect went with it. Withdrawn,
obsolete, dismissed and suppressed findings were closed, not fixed, and are
not credited to anyone. The raised total matches the "raised" figure on each
project's cross-locale page, which counts every finding in state.

Raised spikes when a locale or project gets its first baseline run, which
reads the whole tree at once; the page says so, so the spike is not read as
a sudden drop in quality.
"""

from __future__ import annotations

import datetime
import glob
import json
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _day(value: str) -> datetime.date | None:
    # Imported findings can carry a note after the date: "2026-07-29 (undated)".
    try:
        return datetime.date.fromisoformat((value or "")[:10])
    except ValueError:
        return None


def collect(root: str = _ROOT) -> list:
    """One row per finding: project, the day raised, the day fixed (or None)."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "*", "state", "*", "findings.json"))):
        project = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(path))))
        with open(path, encoding="utf-8") as fh:
            rows = json.load(fh)
        for f in rows:
            raised = _day(f.get("first_seen", ""))
            if raised is None:
                continue
            fixed = _day(f.get("resolved_on", "")) if f.get("status") == "fixed" else None
            out.append({"project": project, "raised": raised, "fixed": fixed})
    return out


def _monday(day: datetime.date) -> datetime.date:
    return day - datetime.timedelta(days=day.weekday())


def stats(records: list, today: datetime.date) -> dict:
    raised, fixed = {}, {}
    for r in records:
        week = _monday(r["raised"])
        raised[week] = raised.get(week, 0) + 1
        if r["fixed"]:
            week = _monday(r["fixed"])
            fixed[week] = fixed.get(week, 0) + 1

    weeks = []
    if records:
        week = min(raised)
        last = _monday(max([today, *raised, *fixed]))
        while week <= last:
            weeks.append({"week": week, "raised": raised.get(week, 0),
                          "fixed": fixed.get(week, 0)})
            week += datetime.timedelta(days=7)

    by_project = {}
    for r in records:
        t = by_project.setdefault(r["project"], {"raised": 0, "fixed": 0})
        t["raised"] += 1
        t["fixed"] += bool(r["fixed"])
    return {
        "weeks": weeks,
        "by_project": by_project,
        "raised": len(records),
        "fixed": sum(1 for r in records if r["fixed"]),
    }


def chart_data(s: dict) -> dict:
    """What `site/charts.js` draws, merged into `bot.json` under ``findings``."""
    return {
        "weeks": [w["week"].isoformat() for w in s["weeks"]],
        "raised": [w["raised"] for w in s["weeks"]],
        "fixed": [w["fixed"] for w in s["weeks"]],
    }


def render(s: dict, projects: dict, row) -> str:
    """The landing page section. ``row`` is `bot._row`, so both tables match."""
    out = ["<h2>Findings raised and fixed</h2>"]
    if not s["raised"]:
        out.append('<p class="placeholder">No findings have been recorded yet.</p>')
        return "\n".join(out)

    out += [
        f"<p>{s['raised']:,} findings raised across all projects, "
        f"{s['fixed']:,} fixed. A finding is fixed when the string changed and "
        "the defect went with it; findings that were withdrawn, dismissed or "
        "whose string was removed are not counted as fixed.</p>",
        "<h3>Per week</h3>",
        "<p class=\"muted\">Raised by the week a finding was first reported, "
        "fixed by the week the fix was detected. Large raised weeks are first "
        "runs over a new locale or project, which read the whole tree at once.</p>",
        '<figure class="viz"><canvas id="chart-findings" role="img" '
        'aria-label="Findings raised and fixed per week"></canvas></figure>',
        "<table><thead>" + row(["Project", "Raised", "Fixed"], head=True)
        + "</thead><tbody>",
    ]
    for name, t in sorted(s["by_project"].items(),
                          key=lambda kv: projects.get(kv[0], kv[0]).lower()):
        out.append(row([projects.get(name, name), t["raised"], t["fixed"]]))
    out += [
        "</tbody></table>",
        "<details><summary>Weekly figures as a table</summary><table><thead>"
        + row(["Week of", "Raised", "Fixed"], head=True) + "</thead><tbody>",
    ]
    for w in s["weeks"]:
        out.append(row([w["week"].isoformat(), w["raised"], w["fixed"]]))
    out.append("</tbody></table></details>")
    return "\n".join(out)


def build(projects: dict, row, today: datetime.date | None = None) -> tuple:
    s = stats(collect(), today or datetime.date.today())
    return render(s, projects, row), chart_data(s)
