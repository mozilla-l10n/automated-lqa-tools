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


def render(project) -> str:
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
            "open": sum(1 for f in found if f.is_open),
            "fixed": sum(1 for f in found if f.status == "fixed"),
            "suppressed": sum(1 for f in found if f.status == "suppressed"),
            "dismissed": sum(1 for f in found if f.status == "dismissed"),
            "total": len(found),
            "urgent": by_impact.get(1, 0) + by_impact.get(2, 0),
        })

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
        f"- **Findings:** {total_all:,} raised, {total_fixed:,} resolved "
        f"({pct}), {total_open:,} open",
        f"- **Closed by a person:** {sum(r['dismissed'] for r in checked):,} "
        f"dismissed, {sum(r['suppressed'] for r in checked):,} suppressed by rule",
        "",
        "Counts come from `state/`, not from the rendered reports, so they "
        "always reflect what the pipeline recorded.",
        "",
        "| Locale | Last run | Mode | Commit | Strings | Missing | Open | "
        "Impact 1–2 | Fixed | Dismissed | Suppressed |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sorted(checked, key=lambda r: (-r["urgent"], -r["open"])):
        m = r["meta"]
        out.append(
            f"| [{r['locale']}]({r['locale']}/{project.name}.md) | "
            f"{m.get('last_run', '')} | "
            f"{m.get('mode', '')} | `{m.get('l10n_sha', '')[:8]}` | "
            f"{m.get('strings', 0):,} | {m.get('missing', 0):,} | "
            f"**{r['open']}** | {r['urgent']} | {r['fixed']} | "
            f"{r['dismissed']} | {r['suppressed']} |"
        )
    for r in rows:
        if r["state"]:
            out.append(
                f"| {r['locale']} | — | — | — | — | — | — | — | — | — | _{r['state']}_ |"
            )

    out += [
        "",
        "**Impact 1–2** is the queue that matters: broken output and wrong "
        "content. Impact 3–4 is language polish and typography.",
        "",
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
    args = ap.parse_args(argv)

    project = config.load(args.project)
    text = render(project)
    if args.stdout:
        print(text)
        return 0
    print(f"wrote {write(project)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
