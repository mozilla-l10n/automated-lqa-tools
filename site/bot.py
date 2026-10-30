"""The landing page: what the Pontoon suggestion bot sent, and what came of it.

Built from ``<project>/pontoon_suggestions/<locale>.json`` alone -- the
records `lib/autosuggest.py` writes when it sends a suggestion and
`lib/pontoon_review.py` updates when a Pontoon reviewer answers one. Nothing
is fetched from Pontoon at build time, so the page says what the repository
knows, as of the last QA run that read Pontoon back.

Every count is keyed to the day a suggestion was **sent**, not the day it was
answered: a week's acceptance rate is the share of that week's suggestions a
reviewer has approved so far. Recent weeks therefore start mostly pending
and fill in as reviewers get to them -- the page says so rather than quoting
a rate over answered suggestions only, which would read as final while most
of the week is still open.

The tiles and tables are rendered here; the charts are Chart.js, drawn by
`site/charts.js` from `bot.json`. Chart.js is vendored under `site/vendor/`
rather than loaded from a CDN, so the page's CSP still allows scripts from
the site alone. Every value a chart shows is also in the table under it.
"""

from __future__ import annotations

import ast
import datetime
import glob
import html
import json
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANSWERED = ("approved", "rejected")
WINDOW_DAYS = 30
FALLBACK_SERVER = "https://pontoon.mozilla.org"


def bot_user() -> str:
    """`pontoon_review.DEFAULT_USER`, read without importing it.

    Importing would pull the whole QA pipeline (and its model client) into a
    build that only installs a markdown renderer. Reading the constant keeps
    the account the page links to the one the pipeline actually queries.
    """
    path = os.path.join(_ROOT, "lib", "pontoon_review.py")
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and getattr(node.targets[0], "id", None) == "DEFAULT_USER"):
            return ast.literal_eval(node.value)
    raise SystemExit(f"DEFAULT_USER not found in {path}")


def collect(root: str = _ROOT) -> list:
    """Every suggestion ever sent, flattened, with its project and locale."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "*", "pontoon_suggestions", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        project = os.path.basename(os.path.dirname(os.path.dirname(path)))
        for s in data.get("suggestions", []):
            status = s.get("status")
            out.append({
                "project": data.get("project") or project,
                "locale": data.get("locale") or os.path.basename(path)[:-5],
                "date": datetime.date.fromisoformat(s["date"]),
                "status_date": s.get("status_date"),
                # Anything Pontoon has not approved or rejected is waiting,
                # the same reading pontoon_review gives it.
                "status": status if status in ANSWERED else "pending",
                "server": (s.get("pontoon") or {}).get("server"),
            })
    return out


def _tally(rows) -> dict:
    t = {"sent": 0, "approved": 0, "rejected": 0, "pending": 0}
    for r in rows:
        t["sent"] += 1
        t[r["status"]] += 1
    return t


def _monday(day: datetime.date) -> datetime.date:
    return day - datetime.timedelta(days=day.weekday())


def stats(records: list, today: datetime.date) -> dict:
    since = today - datetime.timedelta(days=WINDOW_DAYS - 1)
    recent = [r for r in records if since <= r["date"] <= today]

    weeks = []
    if records:
        week = _monday(min(r["date"] for r in records))
        last = _monday(max(today, max(r["date"] for r in records)))
        while week <= last:
            end = week + datetime.timedelta(days=6)
            weeks.append(dict(_tally(r for r in records if week <= r["date"] <= end),
                              week=week))
            week += datetime.timedelta(days=7)

    by_locale = {}
    for r in recent:
        by_locale.setdefault((r["locale"], r["project"]), []).append(r)

    answered = [r["status_date"] for r in records
                if r["status"] in ANSWERED and r["status_date"]]
    return {
        "today": today,
        "since": since,
        "recent": _tally(recent),
        "recent_locales": len({r["locale"] for r in recent}),
        "total": _tally(records),
        "weeks": weeks,
        "by_locale": [dict(_tally(rows), locale=loc, project=proj)
                      for (loc, proj), rows in sorted(by_locale.items())],
        "last_answer": max(answered) if answered else None,
        "server": next((r["server"] for r in records if r["server"]), FALLBACK_SERVER),
    }


# --- rendering -------------------------------------------------------------

E = html.escape


def _pct(n: int, d: int) -> str:
    return f"{round(100 * n / d)}%" if d else "–"


def chart_data(s: dict) -> dict:
    """What `site/charts.js` draws, written next to the page as `bot.json`.

    A week with nothing sent has no rate, so it is ``None`` -- a gap in the
    line -- rather than a zero that was never measured.
    """
    weeks = s["weeks"]
    rate = lambda k: [round(100 * w[k] / w["sent"], 1) if w["sent"] else None  # noqa: E731
                      for w in weeks]
    return {
        "weeks": [w["week"].isoformat() for w in weeks],
        "sent": [w["sent"] for w in weeks],
        "approved": [w["approved"] for w in weeks],
        "rejected": [w["rejected"] for w in weeks],
        "pending": [w["pending"] for w in weeks],
        "acceptance": rate("approved"),
        "rejection": rate("rejected"),
    }


def _tile(label: str, value, note: str = "") -> str:
    note = f'<span class="note">{E(note)}</span>' if note else ""
    return (f'<div class="tile"><span class="label">{E(label)}</span>'
            f'<span class="figure">{E(str(value))}</span>{note}</div>')


def _row(cells, head=False) -> str:
    tag = "th" if head else "td"
    return "<tr>" + "".join(
        f'<{tag}{" class=num" if isinstance(c, int) and not head else ""}>{E(str(c))}</{tag}>'
        for i, c in enumerate(cells)) + "</tr>"


def render(s: dict, user: str, projects: dict) -> str:
    profile = f"{s['server'].rstrip('/')}/contributors/{user}/"
    r, t = s["recent"], s["total"]
    answered = r["approved"] + r["rejected"]
    out = [
        "<h1>Pontoon suggestion bot</h1>",
        f'<p>Fixes for QA findings are proposed in Pontoon as suggestions by '
        f'<a href="{E(profile)}">{E(user)}</a>, and accepted or rejected there by '
        f'each locale’s reviewers. Counts are by the day a suggestion was sent; '
        f'outcomes are as last read back from Pontoon'
        + (f" (latest answer recorded {E(s['last_answer'])})." if s["last_answer"] else ".")
        + "</p>",
    ]
    if not t["sent"]:
        out.append('<p class="placeholder">No suggestions have been sent yet.</p>')
        return "\n".join(out)

    out += [
        f"<h2>Last {WINDOW_DAYS} days</h2>",
        f'<p class="muted">{s["since"].isoformat()} to {s["today"].isoformat()}</p>',
        '<div class="tiles">',
        _tile("Sent", f"{r['sent']:,}", f"{s['recent_locales']} locales"),
        _tile("Approved", f"{r['approved']:,}", f"{_pct(r['approved'], r['sent'])} of sent"),
        _tile("Rejected", f"{r['rejected']:,}", f"{_pct(r['rejected'], r['sent'])} of sent"),
        _tile("Awaiting review", f"{r['pending']:,}", f"{_pct(r['pending'], r['sent'])} of sent"),
        _tile("Accepted when reviewed", _pct(r["approved"], answered),
              f"of {answered} answered"),
        "</div>",
    ]
    if s["by_locale"]:
        out.append("<table><thead>" + _row(
            ["Locale", "Project", "Sent", "Approved", "Rejected", "Awaiting"], head=True)
            + "</thead><tbody>")
        for row in s["by_locale"]:
            out.append(_row([row["locale"], projects.get(row["project"], row["project"]),
                             row["sent"], row["approved"], row["rejected"], row["pending"]]))
        out.append("</tbody></table>")

    weeks = s["weeks"]
    out += [
        "<h2>Over time</h2>",
        f"<p>{t['sent']:,} suggestions sent in all: {t['approved']:,} approved, "
        f"{t['rejected']:,} rejected, {t['pending']:,} awaiting review.</p>",
        "<h3>Suggestions sent per week</h3>",
        '<figure class="viz"><canvas id="chart-sent" role="img" '
        'aria-label="Suggestions sent per week, by outcome"></canvas></figure>',
        "<h3>Acceptance and rejection rate</h3>",
        "<p class=\"muted\">Share of each week’s suggestions approved or rejected "
        "so far. The rest are awaiting review, so the latest weeks rise as "
        "reviewers catch up.</p>",
        '<figure class="viz"><canvas id="chart-rate" role="img" '
        'aria-label="Acceptance and rejection rate per week"></canvas></figure>',
        "<details><summary>Weekly figures as a table</summary><table><thead>"
        + _row(["Week of", "Sent", "Approved", "Rejected", "Awaiting",
                "Acceptance", "Rejection"], head=True) + "</thead><tbody>",
    ]
    for w in weeks:
        out.append(_row([w["week"].isoformat(), w["sent"], w["approved"], w["rejected"],
                         w["pending"], _pct(w["approved"], w["sent"]),
                         _pct(w["rejected"], w["sent"])]))
    out.append("</tbody></table></details>")
    return "\n".join(out)


def build(projects: dict, today: datetime.date | None = None) -> tuple:
    """The page fragment and the data its charts are drawn from."""
    s = stats(collect(), today or datetime.date.today())
    return render(s, bot_user(), projects), chart_data(s)
