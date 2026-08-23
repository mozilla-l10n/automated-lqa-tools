#!/usr/bin/env python3
"""Roll every locale's state up into one cross-locale page.

Read straight from ``state/``, never from the rendered reports, so the
numbers cannot drift from what the pipeline actually recorded. Safe to run
at any time; it makes no API calls and changes nothing but its own output.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import findings as findings_mod  # noqa: E402
import report  # noqa: E402


def _rows(project) -> list[dict]:
    rows = []
    for locale in project.locales:
        meta_path = os.path.join(project.state_dir(locale), "meta.json")
        if not os.path.exists(meta_path):
            rows.append({"locale": locale, "state": "not yet checked"})
            continue
        with open(meta_path, encoding="utf-8") as fh:
            meta = json.load(fh)
        found = findings_mod.load(project, locale)
        by_impact = {}
        for f in found:
            if f.is_open:
                by_impact[f.impact] = by_impact.get(f.impact, 0) + 1
        rows.append({
            "locale": locale,
            "state": "",
            "meta": meta,
            "found": found,
            "open": sum(1 for f in found if f.is_open),
            "fixed": sum(1 for f in found if f.status == "fixed"),
            "suppressed": sum(1 for f in found if f.status == "suppressed"),
            "dismissed": sum(1 for f in found if f.status == "dismissed"),
            "total": len(found),
            "urgent": by_impact.get(1, 0) + by_impact.get(2, 0),
        })

    return rows


MAX_LISTED = 15


def _code(text: str, limit: int = 200) -> str:
    """Quote a translation inline without letting it end its own span.

    Shared with the report renderer -- see :func:`report.fence`. A fence has
    to be longer than the longest run of backticks inside it, or the rest of
    the finding renders as markdown.
    """
    return report.fence(report._esc(text, limit))


def _one(f, locale: str) -> str:
    """One finding, self-contained: the PR body has no report around it."""
    bits = [f"- **`{locale}`** `{f.string_id}` — `{f.file}`\n  - {f.summary}"]
    if f.current:
        bits.append(f"  - Current: {_code(f.current)}")
    if f.suggest and f.suggest != f.current:
        bits.append(f"  - Suggest: {_code(f.suggest)}")
    return "\n".join(bits)


def _listing(items: list[tuple], cap: int, per_locale: int = 0) -> str:
    """Render a bounded sample, and say plainly what was left out.

    A silent truncation reads as "that was all of them", which is the one
    thing a triage list must not imply. ``per_locale`` caps each locale's
    share first: sorted by locale, a flat cap on a backlog of hundreds
    shows the first locale alphabetically and nothing else, which looks
    like the other nineteen are clean.
    """
    shown, seen = [], {}
    for loc, f in items:
        if per_locale and seen.get(loc, 0) >= per_locale:
            continue
        if len(shown) >= cap:
            break
        seen[loc] = seen.get(loc, 0) + 1
        shown.append((loc, f))
    body = "\n".join(_one(f, loc) for loc, f in shown)
    if len(shown) < len(items):
        body += (
            f"\n- _…and {len(items) - len(shown)} more, in the per-locale "
            "reports linked below._"
        )
    return body


def _per_locale(items: list[tuple]) -> str:
    counts = {}
    for loc, _ in items:
        counts[loc] = counts.get(loc, 0) + 1
    return " · ".join(
        f"`{loc}` {n}" for loc, n in sorted(counts.items(), key=lambda kv: -kv[1])
    )


def _table(rows: list[dict], project, prefix: str = "") -> str:
    """Per-locale counts, with a link to each locale's own report.

    ``prefix`` because the same table is rendered into ``reports/`` -- where
    the locale directory sits next to the page -- and into a pull request
    body, where a relative link resolves against the repository root.
    """
    out = [
        "| Locale | Last run | Mode | Commit | Strings | Missing | Open | "
        "Impact 1–2 | Fixed | Dismissed | Suppressed |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    # Alphabetical by locale code: the table is looked up ("where is pt-BR?"),
    # not read as a ranking, and a worst-first order shuffles rows between
    # runs so the same locale is never twice in the same place.
    for r in sorted(rows, key=lambda r: r["locale"]):
        if r["state"]:
            continue
        m = r["meta"]
        out.append(
            f"| [{r['locale']}]({prefix}{r['locale']}/{project.name}.md) | "
            f"{m.get('last_run', '')} | "
            f"{m.get('mode', '')} | `{m.get('l10n_sha', '')[:8]}` | "
            f"{m.get('strings', 0):,} | {m.get('missing', 0):,} | "
            f"**{r['open']}** | {r['urgent']} | {r['fixed']} | "
            f"{r['dismissed']} | {r['suppressed']} |"
        )
    for r in sorted(rows, key=lambda r: r["locale"]):
        if r["state"]:
            out.append(
                f"| {r['locale']} | — | — | — | — | — | — | — | — | — | _{r['state']}_ |"
            )
    return "\n".join(out)


def _highlights(rows: list[dict], project) -> str:
    """What a reviewer of this pull request has to look at before merging.

    Two axes, because they are two different questions. Impact 1 is "does
    this string work"; the deliberate flag is "does this string say
    something we did not say". A finding can be alarming without being
    broken, which is why the second list is not a slice of the first.
    """
    flagged, broken_out, wrong = [], [], []
    for r in rows:
        if r["state"]:
            continue
        loc = r["locale"]
        for f in findings_mod.deliberate(r["found"]):
            flagged.append((loc, f))
        for f in findings_mod.broken(r["found"]):
            broken_out.append((loc, f))
        wrong += [f for f in r["found"] if f.is_open and f.impact == 2]

    out = ["## Read these first", ""]

    out += [f"### Reads as a deliberate edit ({len(flagged)})", ""]
    if flagged:
        out += [
            "The translation makes the product assert something the en-US "
            "never said. Nothing here says the change was intended — that "
            "cannot be read off the text, which is exactly the problem, "
            "because a user cannot read it off either.",
            "",
            _listing(sorted(flagged, key=lambda p: (p[0], p[1].file)), 30),
            "",
        ]
    else:
        out += [
            "_None. The reviewer sets this flag only on a finding where the "
            "localized text changes what the product says about itself, its "
            "users or its behaviour; it is left unset on the vast majority "
            "of mistranslations._",
            "",
        ]

    out += [f"### Broken output — impact 1 ({len(broken_out)})", ""]
    if broken_out:
        out += [
            "The value does not render as intended: a blank string, broken "
            "markup, a variable the source never passes.",
            "",
            _per_locale(broken_out),
            "",
            _listing(sorted(broken_out, key=lambda p: (p[0], p[1].file)),
                     MAX_LISTED, per_locale=2),
            "",
        ]
    else:
        out += ["_Nothing open at impact 1._", ""]

    out += [
        f"### Wrong content — impact 2 ({len(wrong)})",
        "",
        "Too many to list here; the per-locale counts are in the table "
        f"below and every one of them is in `reports/<locale>/{project.name}.md`.",
        "",
    ]
    return "\n".join(out)


def render(project) -> str:
    rows = _rows(project)
    checked = [r for r in rows if not r["state"]]
    total_open = sum(r["open"] for r in checked)
    total_fixed = sum(r["fixed"] for r in checked)
    total_all = sum(r["total"] for r in checked)
    pct = f"{100 * total_fixed // total_all}%" if total_all else "—"

    out = [
        f"# {project.data.get('name', project.name)} — l10n QA",
        "",
        f"- **Generated:** {datetime.date.today().isoformat()}",
        f"- **Locales tracked:** {len(project.locales)} "
        f"({len(checked)} with recorded state)",
        f"- **Findings:** {total_all:,} raised, {total_fixed:,} fixed "
        f"({pct}), {total_open:,} open",
        f"- **Closed by a person:** {sum(r['dismissed'] for r in checked):,} "
        f"dismissed, {sum(r['suppressed'] for r in checked):,} suppressed by rule",
        "",
        "Counts come from `state/`, not from the rendered reports, so they "
        "always reflect what the pipeline recorded.",
        "",
        _highlights(rows, project),
        _table(rows, project),
        "",
        "**Impact 1–2** is the queue that matters: broken output and wrong "
        "content. Impact 3–4 is language polish and typography.",
        "",
    ]
    partial = [r["locale"] for r in checked if r["meta"].get("incomplete")]
    if partial:
        out += [
            "**Reviewed only in part:** "
            + ", ".join(f"`{loc}`" for loc in partial)
            + ". The reviewer stopped early; the strings it never reached "
            "are unreviewed. Each locale's own page says where it stopped.",
            "",
        ]

    unread = [r["locale"] for r in checked
              if r["meta"].get("mode") == config.CHECKS_ONLY]
    if unread:
        # Their open counts are the check layer's alone, and a small number
        # there is not good news -- it is the absence of an opinion.
        out += [
            f"**Not reviewed yet:** {', '.join(f'`{loc}`' for loc in unread)}. "
            f"{'They have' if len(unread) > 1 else 'It has'} only been through "
            "the deterministic checks; the reviewer has not read "
            f"{'them' if len(unread) > 1 else 'it'}. The next run does the "
            "baseline.",
            "",
        ]

    out += [
        "## Adding a locale",
        "",
        f"Add its code to `{project.name}/config.yaml` and run the workflow. The first "
        "run has no stored state, so it takes the from-scratch baseline path "
        "over the whole tree; every run after that reviews only what changed.",
        "",
        "## Flagging a false positive",
        "",
        f"Write a rule in `{project.name}/locales/<code>/suppressions.yaml`, or "
        f"better, a sentence in `{project.name}/locales/<code>/conventions.md`. Both are "
        "re-applied to the entire backlog on the next run, so a rule added "
        "today retires findings raised months ago. See `docs/suppressions.md`.",
        "",
    ]
    return "\n".join(out)


def pr_body(project) -> str:
    """The body of the project's pull request.

    Generated rather than sliced out of the rendered page: the body used to
    be the page's first forty lines, so any edit to the header silently
    changed what the reviewer saw.
    """
    rows = _rows(project)
    return "\n".join([
        "Automated localization QA: findings, state and reports only. This "
        "workflow never modifies a locale file, and the review agent runs "
        "with read-only tools.",
        "",
        "The branch is reused, so this describes everything open on it, not "
        "only the latest commit.",
        "",
        "---",
        "",
        _highlights(rows, project),
        _table(rows, project, prefix="reports/"),
        "",
        "Each locale links to its own report, which lists every open "
        "finding with the en-US source beside it.",
    ])


def write(project) -> str:
    """Render the cross-locale page and write it. Returns the path."""
    path = project.summary_path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(render(project))
    return path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--pr-body", action="store_true",
                    help="print the pull request body instead of the page")
    args = ap.parse_args(argv)

    project = config.load(args.project)
    if args.pr_body:
        print(pr_body(project))
        return 0
    text = render(project)
    if args.stdout:
        print(text)
        return 0
    print(f"wrote {write(project)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
