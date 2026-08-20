"""Render a locale's state as the markdown report.

The skeleton is the one the fourteen hand-written reviews converged on --
metadata, health check, systemic items, findings in categories A-E,
appendix -- so imported findings read exactly as they did before. What is
new is the run-delta section at the top, which answers the question the
manual process could not: *what changed since last time?*

Three conventions are inherited from those reviews and are deliberate:

* every finding is keyed by string id, never by line number, because line
  numbers drift between the locale and en-US and across syncs;
* no cross-language comparison -- a locale is assessed against en-US only;
* no closing paragraph of subjective judgement.
"""

from __future__ import annotations

import os

import conventions as conv
from findings import CATEGORIES, IMPACT

MAX_LISTED = 60  # per category, before collapsing to a count

# A finding is keyed by the *reference* path, because that is the one
# identifier every locale shares and so the one that state can be stored
# against. A reader wants the file they would actually edit, though, so
# reports translate it back. For a mirrored layout the two are the same.
_PATHS: dict = {}

# The source-language text, looked up per finding rather than stored on it.
# `suggest` means one thing -- a proposed correction -- and the source string
# is shown separately; conflating them labelled Italian suggestions "en-US".
_SOURCE: dict = {}


def use_paths(mapping: dict) -> None:
    global _PATHS
    _PATHS = mapping or {}


def use_source(messages: dict) -> None:
    global _SOURCE
    _SOURCE = messages or {}


def _path(rel: str) -> str:
    return _PATHS.get(rel, rel)


def _esc(text: str, limit: int = 220) -> str:
    text = (text or "").replace("|", "\\|").replace("\n", " ").strip()
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def _item(f) -> str:
    bits = [f"- `{f.string_id}` — `{_path(f.file)}` — {f.summary}"]
    if f.current:
        bits.append(f"  - Current: `{_esc(f.current)}`")
    src = _SOURCE.get(f.key)
    source_text = src.text() if src is not None else ""
    if source_text and source_text.strip() != (f.current or "").strip():
        bits.append(f"  - Source: `{_esc(source_text)}`")
    if f.suggest and f.suggest != f.current:
        bits.append(f"  - Suggest: `{_esc(f.suggest)}`")
    if f.rationale:
        bits.append(f"  - {_esc(f.rationale, 400)}")
    return "\n".join(bits)


def _group(findings: list, title: str, empty: str = "_Nothing in this category._") -> str:
    if not findings:
        return f"{title}\n\n{empty}\n"
    shown = findings[:MAX_LISTED]
    body = "\n".join(_item(f) for f in shown)
    if len(findings) > MAX_LISTED:
        body += f"\n- _…and {len(findings) - MAX_LISTED} more; see `state/` for the full list._"
    return f"{title}\n\n{body}\n"


def _health_table(h, counts) -> str:
    rows = [
        "| Check | Result |",
        "|---|---|",
        f"| Files | {h.files} |",
        f"| Strings | {h.strings:,} |",
        f"| Missing strings | {h.missing:,} |",
        f"| Obsolete strings | {h.obsolete:,} |",
        f"| Files absent from the locale | {len(h.missing_files)} |",
        f"| Fluent / properties syntax errors | {len(h.syntax_errors)} |",
    ]
    labels = {
        "variables": "Variable & placeholder mismatches",
        "escaping": "Android escaping (apostrophes, quotes, ampersands)",
        "translatable": "Strings marked untranslatable in the source",
        "placeholders": "printf placeholder mismatches",
        "selectors": "Plural / select selector mismatches",
        "term_params": "Term parameter mismatches",
        "plurals": "Plural variants (dead or missing forms)",
        "ui_references": "Text quoting a UI label that no longer matches",
        "variant_spelling": "Source-language spellings left unchanged",
        "accesskey": "Access keys not in their label",
        "markup": "Markup & `data-l10n-name` defects",
        "typography": "Typography deviations from this locale's own norm",
    }
    for check, label in labels.items():
        if check in h.skipped:
            rows.append(f"| {label} | _skipped for this locale_ |")
        else:
            rows.append(f"| {label} | {counts.get(check, 0)} |")
    return "\n".join(rows)


def _missing_detail(h) -> str:
    if not h.missing and not h.missing_files and not h.untranslated_files:
        return "The locale is complete against the en-US source.\n"
    out = []
    if h.missing:
        top = sorted(h.missing_by_file.items(), key=lambda kv: -kv[1])[:12]
        listed = "\n".join(f"- `{_path(f)}` — {n}" for f, n in top)
        out.append(
            f"**{h.missing:,} strings** are not translated yet, concentrated in:\n\n{listed}\n"
        )
    if h.missing_files:
        out.append(
            "**Files absent from the locale:**\n\n"
            + "\n".join(f"- `{_path(f)}`" for f in h.missing_files[:20])
            + "\n"
        )
    if h.untranslated_files:
        out.append(
            "**Files present but identical to en-US:**\n\n"
            + "\n".join(f"- `{f}`" for f in h.untranslated_files[:20])
            + "\n"
        )
    out.append(
        "_Completeness is reported, never raised as a finding: a missing string "
        "needs translating, not fixing._\n"
    )
    return "\n".join(out)


def _systemic(systemic: list[dict]) -> str:
    if not systemic:
        return "_Nothing reported._\n"
    out = []
    for item in systemic:
        ids = item["ids"]
        sample = ", ".join(f"`{i}`" for i in ids[:12])
        more = f" …and {len(ids) - 12} more" if len(ids) > 12 else ""
        out.append(
            f"- **{item['title']}** — {item['count']} strings. {item['note']}\n"
            f"  - Affected: {sample}{more}"
        )
    return "\n".join(out) + "\n"


def _delta_section(delta_report: dict) -> str:
    parts = []
    for key, title, empty in (
        ("new", "🆕 New findings", "No new findings."),
        ("fixed", "✅ Fixed since the last run", "Nothing was fixed."),
        ("withdrawn", "↩︎ Withdrawn — no longer considered a defect",
         "Nothing withdrawn."),
        ("recheck", "🔁 String changed, defect not verifiable — needs a re-read", "Nothing to re-read."),
        ("obsolete", "🗑 Retired — the string no longer exists upstream", "Nothing retired."),
    ):
        items = delta_report.get(key) or []
        if items:
            body = "\n".join(_item(f) for f in items[:MAX_LISTED])
            if len(items) > MAX_LISTED:
                body += f"\n- _…and {len(items) - MAX_LISTED} more._"
        else:
            body = f"_{empty}_"
        parts.append(f"### {title} ({len(items)})\n\n{body}\n")
    return "\n".join(parts)


def _siblings(locale: str, project: str) -> str:
    """Links to the same locale's reports for the other projects.

    Reports are grouped by locale, so a reviewer who works on Italian has
    everything about Italian in one directory; this makes that navigable.
    """
    import glob

    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.join(os.path.dirname(here), "reports", locale)
    others = sorted(
        os.path.basename(p)[:-3]
        for p in glob.glob(os.path.join(root, "*.md"))
        if os.path.basename(p)[:-3] != project
    )
    if not others:
        return ""
    links = " · ".join(f"[{name}]({name}.md)" for name in others)
    return f"Also for {locale}: {links}"


def render(locale, meta, health, counts, findings, systemic, delta_report, counts_conv, rules) -> str:
    open_findings = [f for f in findings if f.is_open]
    suppressed = [f for f in findings if f.status == "suppressed"]
    dismissed = [f for f in findings if f.status == "dismissed"]
    fixed_total = [f for f in findings if f.status == "fixed"]
    withdrawn_total = [f for f in findings if f.status == "withdrawn"]

    by_impact = {}
    for f in open_findings:
        by_impact[f.impact] = by_impact.get(f.impact, 0) + 1

    lines = [
        f"# {meta.get('project', '').capitalize() or 'l10n'} l10n QA — {locale}",
        "",
        "| | |",
        "|---|---|",
        f"| **Generated** | {meta.get('last_run', '')} |",
        f"| **Locale tree** | `{meta.get('l10n_repo', '')}` @ `{meta.get('l10n_sha', '')}` |",
        f"| **en-US reference** | `{meta.get('source_repo', '')}` @ `{meta.get('source_sha', '')}` |",
        f"| **Previous run** | {meta.get('previous_run') or '_none — this is the baseline_'}"
        f" @ `{meta.get('previous_sha', '') or '—'}` |",
        f"| **Mode** | {meta.get('mode', '')} |",
        f"| **Strings reviewed this run** | {meta.get('reviewed', 0):,} of {health.strings:,} |",
        "",
        "Findings are keyed by string id, never by line number. The locale is "
        "assessed against its source only.",
        "",
        _siblings(locale, meta.get("project", "")),
        "",
        "---",
        "",
        f"## Changes in this run",
        "",
        _delta_section(delta_report),
        "---",
        "",
        "## 1. Health check",
        "",
        _health_table(health, counts),
        "",
        "### Completeness",
        "",
        _missing_detail(health),
    ]

    if health.syntax_errors:
        lines += [
            "### Syntax errors",
            "",
            "\n".join(f"- `{e}`" for e in health.syntax_errors[:20]),
            "",
        ]

    lines += [
        "### Conventions detected in this locale",
        "",
        "Counted over the whole tree. Checks flag deviations from the locale's "
        "**own** majority, so a convention that reads _mixed_ produces no "
        "findings at all.",
        "",
        conv.render(counts_conv),
        "",
        "---",
        "",
        "## 2. Systemic items (decisions, not line items)",
        "",
        _systemic(systemic),
        "---",
        "",
        f"## 3. Open findings ({len(open_findings)})",
        "",
        "| Impact | Meaning | Count |",
        "|---|---|---|",
    ]
    for level in sorted(IMPACT):
        lines.append(f"| {level} | {IMPACT[level]} | {by_impact.get(level, 0)} |")
    lines.append("")

    for code, title in CATEGORIES.items():
        group = sorted(
            (f for f in open_findings if f.category == code),
            key=lambda f: (f.file, f.string_id),
        )
        lines.append(_group(group, f"### {code}. {title}"))

    lines += [
        "---",
        "",
        "## 4. Appendix",
        "",
        f"### Dismissed by hand ({len(dismissed)})",
        "",
        (
            "\n".join(
                f"- `{f.string_id}` — `{_path(f.file)}` — {f.dismissed_because}"
                for f in sorted(dismissed, key=lambda f: f.string_id)[:40]
            )
            or "_Nothing dismissed._"
        ),
        "",
        "_One line each in `locales/"
        f"{locale}/dismissed.txt`. Delete the line and the finding returns._",
        "",
        f"### Suppressed as false positives ({len(suppressed)})",
        "",
    ]
    if suppressed:
        active = {r.id: r.reason for r in rules}
        by_rule: dict[str, list] = {}
        for f in suppressed:
            by_rule.setdefault(f.suppressed_by, []).append(f)
        for rule_id, group in sorted(by_rule.items()):
            reason = active.get(rule_id, "_rule no longer defined_")
            sample = ", ".join(f"`{f.string_id}`" for f in group[:10])
            more = f" …and {len(group) - 10} more" if len(group) > 10 else ""
            lines.append(f"- **`{rule_id}`** ({len(group)}) — {reason}\n  - {sample}{more}")
        lines.append("")
        lines.append(
            "_Suppressions live in `locales/"
            f"{locale}/suppressions.yaml`. Removing a rule brings its findings back._"
        )
    else:
        lines.append("_No suppression rules have matched._")

    lines += [
        "",
        f"### Withdrawn to date ({len(withdrawn_total)})",
        "",
        (
            "\n".join(
                f"- `{f.string_id}` — `{_path(f.file)}` — raised by `{f.check}`, "
                f"withdrawn {f.resolved_on}"
                for f in sorted(withdrawn_total, key=lambda f: f.resolved_on, reverse=True)[:20]
            )
            or "_Nothing withdrawn._"
        ),
        "",
        "_A finding is withdrawn when a check stops raising it while the "
        "string itself never changed: the check was wrong, not the "
        "translation. Kept separate from fixes so the fixed count stays "
        "honest._",
        "",
        f"### Resolved to date ({len(fixed_total)})",
        "",
        (
            "\n".join(
                f"- `{f.string_id}` — `{_path(f.file)}` — fixed {f.resolved_on}"
                for f in sorted(fixed_total, key=lambda f: f.resolved_on, reverse=True)[:40]
            )
            or "_Nothing resolved yet._"
        ),
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write(project, locale: str, text: str) -> bool:
    """Write the report, returning True only if it actually changed.

    A run that finds nothing new must not produce a commit, so the file is
    left untouched when its content is identical.
    """
    p = project.report_path(locale)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            if fh.read() == text:
                return False
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)
    return True
