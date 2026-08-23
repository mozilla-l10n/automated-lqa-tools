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
import re
from dataclasses import dataclass, field

import conventions as conv
import findings as findings_mod
from config import CHECKS_ONLY
from findings import CATEGORIES, IMPACT

MAX_LISTED = 60  # per category, before collapsing to a count

# Detail lines hang under their finding. Four spaces, not two: the published
# site renders with Python-Markdown, which needs a full indent level to see a
# nested list and silently flattens two spaces into one long run of siblings
# -- every finding, its quoted string and its rationale all at the same
# level. GitHub accepts four spaces too, so both renderings agree.
SUB = "    - "

@dataclass(frozen=True)
class Ctx:
    """What rendering needs about the tree, passed rather than stashed.

    ``paths`` maps a finding's *reference* path -- the one identifier every
    locale shares, and so the one state can be stored against -- to the file
    a reader would actually edit. For a mirrored layout the two are equal.

    ``source`` is the source-language text, looked up per finding rather than
    stored on it: ``suggest`` means one thing, a proposed correction, and the
    source string is shown separately. Conflating them once labelled Italian
    suggestions "en-US".

    These were module-level globals set by a pair of ``use_*`` functions the
    caller had to remember to call in the right order before every render.
    Forgetting one rendered a locale's report against the previous locale's
    paths, and nothing said so.
    """

    paths: dict = field(default_factory=dict)
    source: dict = field(default_factory=dict)

    def path(self, rel: str) -> str:
        return self.paths.get(rel, rel)


def _esc(text: str, limit: int = 220) -> str:
    text = (text or "").replace("|", "\\|").replace("\n", " ").strip()
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def fence(text: str) -> str:
    """Wrap a translation in a code span it cannot break out of.

    The values quoted in a report are real UI strings and some of them
    contain backticks. Wrapped in a fixed single backtick, such a value ends
    its own span, and everything after it is read as markdown -- so a string
    containing ``x` [click](javascript:alert(1))`` rendered an active link
    into the published page. Escaping HTML, which the site does, does not
    help: this is markdown, not HTML.

    A fence longer than the longest run inside it cannot be terminated early,
    which is the same rule ``summary.py`` uses for the pull request body.
    """
    longest = max((len(r) for r in re.findall(r"`+", text)), default=0)
    pad = " " if text.startswith("`") or text.endswith("`") else ""
    return f"{'`' * (longest + 1)}{pad}{text}{pad}{'`' * (longest + 1)}"


def quoted(text: str, limit: int = 220) -> str:
    """A translation, truncated for the report and safely fenced."""
    return fence(_esc(text, limit))


def _item(f, ctx) -> str:
    bits = [f"- `{f.string_id}` — `{ctx.path(f.file)}` — {f.summary}"]
    if f.current:
        bits.append(f"{SUB}Current: {quoted(f.current)}")
    src = ctx.source.get(f.key)
    source_text = src.text() if src is not None else ""
    if source_text and source_text.strip() != (f.current or "").strip():
        bits.append(f"{SUB}Source: {quoted(source_text)}")
    if f.suggest and f.suggest != f.current:
        bits.append(f"{SUB}Suggest: {quoted(f.suggest)}")
    if f.rationale:
        bits.append(f"{SUB}{_esc(f.rationale, 400)}")
    return "\n".join(bits)


def _group(findings: list, title: str, ctx, empty: str = "_Nothing in this category._") -> str:
    if not findings:
        return f"{title}\n\n{empty}\n"
    shown = findings[:MAX_LISTED]
    body = "\n".join(_item(f, ctx) for f in shown)
    if len(findings) > MAX_LISTED:
        body += f"\n- _…and {len(findings) - MAX_LISTED} more; see `state/` for the full list._"
    return f"{title}\n\n{body}\n"


def _deliberate_callout(open_findings: list, ctx) -> str:
    """Lead with the findings that read as an intentional edit.

    These are ordinary impact-2 mistranslations by the numbers, so they
    would otherwise sit in the middle of section B behind hundreds of
    others. They are repeated here rather than moved: the category listing
    stays complete.
    """
    flagged = findings_mod.deliberate(open_findings)
    if not flagged:
        return ""
    body = "\n".join(
        _item(f, ctx) for f in sorted(flagged, key=lambda f: (f.file, f.string_id))
    )
    return (
        f"> **Reads as a deliberate edit ({len(flagged)}).** The translation "
        "makes the product assert something the en-US never said. Whether "
        "that was intended cannot be told from the text, which is the "
        "problem: a user cannot tell either. Read these first.\n\n"
        f"{body}\n\n"
        "_Also listed under their own category below._\n"
    )


def _health_table(h) -> str:
    rows = [
        "| Check | Result |",
        "|---|---|",
        f"| Files | {h.files} |",
        f"| Strings | {h.strings:,} |",
        f"| Missing strings | {h.missing:,} |",
        f"| Obsolete strings | {h.obsolete:,} |",
        f"| Files absent from the locale | {len(h.missing_files)} |",
        f"| Fluent / properties syntax errors | {len(h.syntax_errors)} |",
        f"| Reference files that did not parse | {len(h.source_errors)} |",
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
    # A check the project does not run is left out entirely rather than
    # printed as zero. A zero is a result -- "we looked, there is nothing" --
    # and the one thing this table must not do is report the absence of a
    # check as the absence of defects.
    for check, label in labels.items():
        if check in h.skipped:
            rows.append(f"| {label} | _skipped for this locale_ |")
        elif check in h.ran:
            rows.append(f"| {label} | {h.counts.get(check, 0)} |")
    return "\n".join(rows)


def _missing_detail(h, ctx) -> str:
    if not h.missing and not h.missing_files and not h.untranslated_files:
        return "The locale is complete against the en-US source.\n"
    out = []
    if h.missing:
        top = sorted(h.missing_by_file.items(), key=lambda kv: -kv[1])[:12]
        listed = "\n".join(f"- `{ctx.path(f)}` — {n}" for f, n in top)
        out.append(
            f"**{h.missing:,} strings** are not translated yet, concentrated in:\n\n{listed}\n"
        )
    if h.missing_files:
        out.append(
            "**Files absent from the locale:**\n\n"
            + "\n".join(f"- `{ctx.path(f)}`" for f in h.missing_files[:20])
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
            f"{SUB}Affected: {sample}{more}"
        )
    return "\n".join(out) + "\n"


def _delta_section(delta_report: dict, ctx) -> str:
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
            body = "\n".join(_item(f, ctx) for f in items[:MAX_LISTED])
            if len(items) > MAX_LISTED:
                body += f"\n- _…and {len(items) - MAX_LISTED} more._"
        else:
            body = f"_{empty}_"
        parts.append(f"### {title} ({len(items)})\n\n{body}\n")
    return "\n".join(parts)


def _reviewer_warning(meta) -> str:
    """Said outright when the model never read a string.

    The deterministic checks still ran over the whole tree, so the report is
    not empty -- which is exactly why this has to be stated. A page headed
    "baseline" with a handful of typography findings reads as a locale that
    was reviewed and came back nearly clean, when nothing has read it yet.
    """
    if meta.get("incomplete"):
        return (
            "> **The reviewer did not finish this run.** It "
            f"{str(meta['incomplete']).rstrip('. ')}. What it read is here "
            "and is kept; the "
            "strings it never reached are unreviewed, and the next run "
            "resumes at the first of them.\n"
        )
    if meta.get("mode") != CHECKS_ONLY:
        return ""
    return (
        "> **The reviewer did not run for this report.** Only the "
        "deterministic checks were applied; no string was read. The absence "
        "of a finding here means nothing has looked, not that there is "
        "nothing to find.\n"
    )


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


def render(locale, meta, health, findings, systemic, delta_report, counts_conv, rules,
           ctx: Ctx | None = None) -> str:
    ctx = ctx or Ctx()
    open_findings = [f for f in findings if f.is_open]
    suppressed = [f for f in findings if f.status == "suppressed"]
    dismissed = [f for f in findings if f.status == "dismissed"]
    fixed_total = [f for f in findings if f.status == "fixed"]
    withdrawn_total = [f for f in findings if f.status == "withdrawn"]

    by_impact = {}
    for f in open_findings:
        by_impact[f.impact] = by_impact.get(f.impact, 0) + 1

    lines = [
        f"# {meta.get('display_name') or 'l10n'} QA — {locale}",
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
        _reviewer_warning(meta),
        _siblings(locale, meta.get("project", "")),
        "",
        "---",
        "",
        "## Changes in this run",
        "",
        _delta_section(delta_report, ctx),
        "---",
        "",
        "## 1. Health check",
        "",
        _health_table(health),
        "",
        "### Completeness",
        "",
        _missing_detail(health, ctx),
    ]

    if health.syntax_errors:
        lines += [
            "### Syntax errors",
            "",
            "\n".join(f"- `{e}`" for e in health.syntax_errors[:20]),
            "",
        ]

    if health.source_errors:
        # Not the locale's defect, and said so plainly: until these parse,
        # every comparison against them is missing.
        lines += [
            "### Reference files that did not parse",
            "",
            "\n".join(f"- `{e}`" for e in health.source_errors[:20]),
            "",
            "_These are en-US files, not this locale's. Nothing in them could "
            "be compared against, so any finding they would have produced is "
            "absent rather than clean._",
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
        _deliberate_callout(open_findings, ctx),
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
        lines.append(_group(group, f"### {code}. {title}", ctx))

    lines += [
        "---",
        "",
        "## 4. Appendix",
        "",
        f"### Dismissed by hand ({len(dismissed)})",
        "",
        (
            "\n".join(
                f"- `{f.string_id}` — `{ctx.path(f.file)}` — {f.dismissed_because}"
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
            lines.append(
                f"- **`{rule_id}`** ({len(group)}) — {reason}\n{SUB}{sample}{more}"
            )
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
                f"- `{f.string_id}` — `{ctx.path(f.file)}` — raised by `{f.check}`, "
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
        f"### Fixed to date ({len(fixed_total)})",
        "",
        (
            "\n".join(
                f"- `{f.string_id}` — `{ctx.path(f.file)}` — fixed {f.resolved_on}"
                for f in sorted(fixed_total, key=lambda f: f.resolved_on, reverse=True)[:40]
            )
            or "_Nothing fixed yet._"
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
