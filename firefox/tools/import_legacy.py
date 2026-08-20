#!/usr/bin/env python3
"""One-time seeding from the hand-written reviews.

Fourteen Firefox locales were reviewed by hand between July and August 2026.
Throwing that away and re-reviewing from scratch would be wasteful and,
worse, would lose the judgement calls: the maintainer decisions, the
"this is correct, stop flagging it" notes, the upstream-en-US exemptions.

So this script reads those reports and produces, per locale:

* ``state/<loc>/findings.json`` -- every finding, classified against the
  current tree as still open or already fixed;
* ``locales/<loc>/suppressions.yaml`` -- the "do not re-flag" knowledge, as
  rules that apply to future runs;
* ``locales/<loc>/conventions.md`` -- the counted conventions plus the
  locale's standing instructions, injected into every future prompt;
* ``state/<loc>/strings.json`` and ``meta.json`` at the current tip, so the
  first automated run is an incremental one rather than a full baseline.

Extraction reuses ``.summarize.py``'s registry and heuristics, which were
tuned against these exact reports: the section-to-category map, the rule
that only the lead-in of a bullet names flagged strings, and the resolution
of the one line-number-keyed section back to string ids. Its known
limitations carry over and are printed at the end rather than hidden -- a
handful of items cite a token that resolves to no message, and strings named
only inside an explanation are missed.

Run once, locally, and commit the result:

    python firefox/tools/import_legacy.py \\
        --reports ~/Desktop/Claude_qa_l10n \\
        --l10n-dir ~/mozilla/git/firefox-l10n \\
        --source-dir ~/mozilla/git/firefox-quarantine
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import conventions  # noqa: E402
import findings as findings_mod  # noqa: E402
import parse  # noqa: E402
import repos  # noqa: E402
import snapshot  # noqa: E402
import suppress  # noqa: E402
from findings import Finding  # noqa: E402

# The legacy severity buckets map one-to-one onto the report categories.
SEVERITY_TO_CATEGORY = {"S1": "A", "S2": "B", "S3": "C", "S4": "D", "S5": "E", "Mx": "B"}

STATUS_FIXED = re.compile(r"^\s*[-*|]?\s*✅")
STATUS_DISMISSED = re.compile(r"➖|\*\*Dismissed\.?\*\*|\*\*Retracted:?\*\*", re.I)

# "Current X → Suggest Y", "`X` → `Y`", "X → Y (why)" in all the shapes the
# reports actually use.
ARROW = re.compile(r"\s*(?:→|->|=>)\s*")
CURRENT_LABEL = re.compile(r"\b(?:current|currently|now|has|says|reads)\b\s*:?\s*", re.I)
SUGGEST_LABEL = re.compile(r"\b(?:suggest|should be|expected|fix|correct)\b\s*:?\s*", re.I)


def load_summarize(reports_dir: str):
    path = os.path.join(reports_dir, ".summarize.py")
    if not os.path.exists(path):
        raise SystemExit(f"cannot find {path}")
    spec = importlib.util.spec_from_file_location("legacy_summarize", path)
    module = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ["summarize", "--quiet"]
    try:
        spec.loader.exec_module(module)
    finally:
        sys.argv = argv
    return module


def strip_markup(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    text = re.sub(r"[*_]{1,2}", "", text)
    return re.sub(r"\s+", " ", text).strip()


def split_finding_text(raw: str, summ) -> tuple[str, str, str]:
    """Pull (summary, current, suggest) out of one report line.

    The reports are handwritten prose in half a dozen shapes, so this is
    best-effort by design: a wrong ``current`` only means the finding cannot
    be auto-verified later and falls back to needing a re-read, which is the
    safe direction.
    """
    line = raw.strip().lstrip("-*").strip()
    if line.startswith("|"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        body = " — ".join(c for c in cells[1:] if c)
    else:
        body = line

    # Drop the leading `id` (and any path) so the summary reads as a sentence.
    parts = re.split(r"\s+[—–]\s+", body)
    if len(parts) > 1 and summ.is_id(strip_markup(parts[0])):
        parts = parts[1:]
    if len(parts) > 1 and summ.is_path(strip_markup(parts[0]).split(":")[0]):
        parts = parts[1:]
    body = " — ".join(parts).strip()

    current = suggest = ""
    ticked = re.findall(r"`([^`]+)`", body)
    if ARROW.search(body):
        left, right = ARROW.split(body, maxsplit=1)
        left_ticks = re.findall(r"`([^`]+)`", left)
        right_ticks = re.findall(r"`([^`]+)`", right)
        current = left_ticks[-1] if left_ticks else strip_markup(
            CURRENT_LABEL.sub("", left).split("—")[-1]
        )
        suggest = right_ticks[0] if right_ticks else strip_markup(
            SUGGEST_LABEL.sub("", right).split("(")[0]
        )
    elif len(ticked) >= 2:
        current, suggest = ticked[0], ticked[1]

    # Bold and backticks are report formatting, not part of the string.
    current = strip_markup(current)
    suggest = strip_markup(suggest)
    # A "current" that is really a string id or a path is not quotable text,
    # and using it to verify a fix later would give a false negative.
    if current and (summ.is_id(current) or summ.is_path(current)):
        current = ""
    if suggest and (summ.is_id(suggest) or summ.is_path(suggest)):
        suggest = ""

    summary = strip_markup(body)
    # Drop a leading "id (.attr) — path —" that survived the split above.
    summary = re.sub(
        r"^[a-zA-Z][\w.-]*\s*(?:\(\.[\w-]+\))?\s+[—–]\s+[\w/.-]+\.(?:ftl|properties|ini)\s+[—–]\s+",
        "", summary,
    )
    if len(summary) > 400:
        summary = summary[:399].rstrip() + "…"
    return summary, current.strip(), suggest.strip()


def extract(report_path: str, headings: dict, key: str, summ) -> list[dict]:
    """Walk a report and pull out one record per flagged string.

    Mirrors ``.summarize.py``'s parse_report -- same heading map, same
    "only the lead-in names the flagged strings" rule -- but keeps the raw
    line so the finding text survives, which the original did not need.
    """
    out: list[dict] = []
    heading = None
    unknown: set[str] = set()
    seen_prose: dict[str, set] = {}

    with open(report_path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    for line in lines:
        m = re.match(r"^#{2,4} (.+?)\s*$", line)
        if m:
            heading = m.group(1)
            if heading not in headings:
                unknown.add(heading)
            continue
        if heading is None or headings.get(heading) is None:
            continue
        severity = headings[heading]
        stripped = line.strip()
        if not stripped or "`" not in stripped:
            continue
        if stripped.startswith("|") and set(stripped) <= set("|- :"):
            continue

        tokens = summ.TICK.findall(line)
        paths = [t for t in tokens if summ.is_path(t)]
        prose = summ.PROSE_SECTIONS.get((key, heading), summ.PROSE_SECTIONS.get(heading))

        if prose is not None:
            mode, line_filter = prose
            if line_filter and not re.match(line_filter, stripped):
                continue
            ids = [t for t in tokens if summ.is_id(t)]
            if not ids:
                continue
            bucket = seen_prose.setdefault(heading, set())
            for mid in ids if mode == "ids" else [ids[0]]:
                if mode == "ids":
                    if mid in bucket:
                        continue
                    bucket.add(mid)
                out.append(_record(heading, severity, [mid] if mode == "ids" else ids,
                                   paths, line))
            continue

        is_item = bool(re.match(r"^[-*] ", stripped)) or stripped.startswith("|")
        if (key, heading) in summ.LINE_KEYED:
            ids = [t for t in tokens if summ.is_id(t)]
            refs, last = [], None
            for fn, nums in summ.LINEREF.findall(stripped):
                last = fn or last
                if last:
                    refs += [(last, int(n)) for n in nums.split(",")]
            if ids or refs:
                record = _record(heading, severity, ids, paths, line)
                record["linerefs"] = sorted(set(refs))
                out.append(record)
            continue

        if not is_item:
            ids = [t for t in tokens if summ.is_id(t)]
            if ids:
                out.append(_record(heading, severity, ids, paths, line))
            continue

        head_seg = stripped
        if stripped.startswith("|"):
            cells = stripped.strip("|").split("|")
            head_seg = cells[0] if cells else stripped
        else:
            head_seg = re.split(r"\s+[—–]\s+", stripped, maxsplit=1)[0]
        ids = [t for t in summ.TICK.findall(head_seg) if summ.is_id(t)]
        if not ids:
            ids = [t for t in tokens if summ.is_id(t)]
        if not ids:
            continue
        out.append(_record(heading, severity, ids, paths, line))

    if unknown:
        print(f"  ! unmapped headings in {os.path.basename(report_path)}:")
        for h in sorted(unknown):
            print(f"      {h!r}")
    return out


def _record(heading, severity, ids, paths, raw) -> dict:
    return {
        "heading": heading,
        "severity": severity,
        "ids": sorted(set(ids)),
        "paths": paths,
        "raw": raw,
        "fixed_in_report": bool(STATUS_FIXED.match(raw)),
        "dismissed": bool(STATUS_DISMISSED.search(raw)),
    }


def build_index(l10n: dict) -> dict[str, list[tuple[str, str]]]:
    index: dict[str, list[tuple[str, str]]] = {}
    for key in l10n:
        index.setdefault(key[1], []).append(key)
    return index


def resolve(record, index, summ):
    """Map a legacy id (possibly with an attribute suffix) onto a real key."""
    resolved = []
    for mid in record["ids"]:
        candidates = None
        for variant in summ.id_variants(mid):
            if variant in index:
                candidates = index[variant]
                break
        if not candidates:
            continue
        if len(candidates) > 1 and record["paths"]:
            hinted = [
                k for k in candidates
                if any(k[0].endswith(p.split(":")[0]) or p.split(":")[0].endswith(
                    os.path.basename(k[0])) for p in record["paths"])
            ]
            if len(hinted) == 1:
                candidates = hinted
        resolved.append(candidates[0])
    return resolved


def convert(locale, records, index, l10n, summ, date) -> tuple[list[Finding], int]:
    out: list[Finding] = []
    unresolved = 0
    seen: set[tuple] = set()
    for record in records:
        keys = resolve(record, index, summ)
        if not keys:
            unresolved += len(record["ids"]) or 1
            continue
        summary, current, suggest = split_finding_text(record["raw"], summ)
        category = SEVERITY_TO_CATEGORY.get(record["severity"], "B")
        for key in keys:
            dedup = (key, category, summary[:80])
            if dedup in seen:
                continue
            seen.add(dedup)
            msg = l10n[key]
            # Trust the report's own verdict when it recorded one; otherwise
            # decide against the tree below.
            if record["dismissed"]:
                status = "suppressed"
            elif record["fixed_in_report"]:
                status = "fixed"
            elif current and not findings_mod.still_present(current, msg.text()):
                status = "fixed"
            else:
                status = "open"
            out.append(Finding(
                locale=locale,
                file=key[0],
                string_id=key[1],
                category=category,
                check="legacy",
                summary=summary or f"Flagged in the {date} review ({record['heading']})",
                current=current,
                suggest=suggest,
                rationale="",
                status=status,
                first_seen=date,
                last_seen=date,
                resolved_on=date if status == "fixed" else "",
                suppressed_by="legacy-dismissed" if status == "suppressed" else "",
                string_hash=msg.hash(),
                origin={"report": "legacy", "section": record["heading"],
                        "severity": record["severity"]},
            ))
    return out, unresolved


# --- curated locale knowledge -------------------------------------------
# Transcribed from the reviews' "verified non-issues" sections and the
# maintainer decisions recorded alongside them. This is the part that cannot
# be extracted mechanically and is the most valuable thing being carried
# forward: without it the first automated run would re-raise everything the
# reviews already settled.

SEEDED = {
    "it": {
        "notes": [
            "Access keys are localized and correctly paired with their labels.",
            "`Elenco lettura` for Safari's Reading List is correct; it is not an "
            "inconsistency with Edge's `Elenco di lettura`.",
            "In DevTools, the CSS keyword `grid` stays English — do not suggest "
            "`griglia`.",
            "The `enterprise/` and FELT files exist only in this locale and are "
            "legitimate; they have no en-US counterpart.",
        ],
        "rules": [
            ("it-disegnata", "`disegnata` in about-private-browsing-focus-promo-text "
             "is deliberate wording, confirmed by the maintainer.",
             {"string_id": "about-private-browsing-focus-promo-text"}),
            ("it-critta", "`critta` is correct — `crittare` means to encrypt. "
             "Confirmed by the maintainer.",
             {"string_id": "credit-card-save-doorhanger-description"}),
        ],
    },
    "fr": {
        "notes": [
            "The no-break space before `? ! ; :` is U+00A0, not U+202F. Both are "
            "correct French; this locale has settled on U+00A0.",
            "Quotes are `« »` and the apostrophe is `’`.",
            "Language and region names are correctly localized.",
        ],
        "rules": [],
    },
    "de": {
        "notes": [
            "The quote convention is unsettled: the tree mixes straight `\"` with "
            "German `„…“`. Treat this as one open decision for the locale team, "
            "not as individual defects.",
        ],
        "rules": [],
    },
    "ja": {
        "notes": [
            "The ellipsis is three ASCII dots, not `…`. This is deliberate and the "
            "opposite of most locales.",
            "Access keys are unadapted English letters. This is correct: the "
            "platform appends the key in parentheses, e.g. `(W)`. Never flag them.",
            "Quotes are `“ ”`; parentheses are halfwidth with a leading space; "
            "`？` and `！` are fullwidth; sentences end with `。`.",
            "A trailing `。` where en-US has `.` is the convention, not a defect.",
            "`.label` and `.aria-label` use the noun form while `.title` uses "
            "`〜します`. This accounts for most apparent cross-file inconsistency.",
            "`toolkit/toolkit/global/neterror/nsserrors.ftl` is deliberately left "
            "in English.",
            "`マスターパスワード` for “Primary Password” is a deliberate legacy term.",
        ],
        "rules": [
            ("ja-ascii-ellipsis", "Japanese uses three ASCII dots, not `…`.",
             {"check": "typography", "text": "ellipsis"}),
            ("ja-english-accesskeys",
             "Access keys are intentionally English; the platform appends `(W)`.",
             {"check": "accesskey"}),
            ("ja-nsserrors-english",
             "nsserrors.ftl is deliberately left untranslated.",
             {"file": "toolkit/toolkit/neterror/nsserrors.ftl"}),
        ],
    },
    "zh-CN": {
        "notes": [
            "Punctuation is fullwidth: `，。？！：；` and `“ ”`.",
            "The register is formal `您`; flag only a mix of `你` and `您`.",
            "Half-width commas inside `quickactions-cmd-*` keyword lists are "
            "correct — they match en-US.",
            "Access keys are meaningless for Chinese; the check is disabled.",
        ],
        "rules": [
            ("zh-CN-accesskeys", "Access keys are not adapted in Chinese.",
             {"check": "accesskey"}),
        ],
    },
    "sl": {
        "notes": [
            "The dual is used correctly throughout: `one` / `two` / `few` / "
            "`other` are all present and right. Never flag plural coverage.",
            "Short button labels use the informal singular imperative by "
            "convention.",
            "Prompt strings in `genai.ftl` use the informal imperative on "
            "purpose — they address the model, not the user.",
            "Brand terms are declined with a `sklon` (case) parameter. This is "
            "correct Slovenian and has no en-US equivalent.",
            "The typo in `cclear-data-for-site-permissions` is upstream in en-US.",
        ],
        "rules": [
            ("sl-brand-case-params",
             "Brand terms carry a `sklon` case parameter; correct Slovenian.",
             {"check": "term_params", "text": "sklon"}),
        ],
    },
    "tr": {
        "notes": [
            "Quotes are `“…”` and the apostrophe is `’` (U+2019).",
            "The register is formal *siz*.",
            "A suffix attached to a term reference **without** an apostrophe is "
            "correct when the term is a common noun "
            "(`{ -smart-window-brand-name }yi`). Only true proper nouns take `’`.",
            "`ön izleme` as two words is settled convention.",
            "Several en-US strings are themselves defective "
            "(`import-safari-permissions-string`, the `about-logging-unknown-*` "
            "family, `about-telemetry-data-details-current`); those are upstream, "
            "not Turkish defects.",
        ],
        "rules": [],
    },
    "pl": {
        "notes": [
            "Quotes are `„…”` (U+201E/U+201D) and the ellipsis is `…`.",
            "A no-break space follows one-letter words; this is applied ~99% of "
            "the time and the remaining gaps are mostly string-initial or inside "
            "`genai.ftl` prompt bodies.",
            "Brand terms take grammatical-case parameters "
            "(`{ -brand-short-name(case: \"gen\") }`) with keys nom/gen/dat/acc/"
            "ins/loc plus lower/upper. Naive plural-category checks flag these; "
            "they are correct.",
            "Plural sets are `one` / `few` / `*[many]` with no `other`. Correct.",
            "The impersonal `Można…` construction is house style.",
            "Slang in `quickactions-cmd-*` (`apdejt`, `skrin`, `laborki`) and the "
            "unaccented `przegladarka` in `findbar-match-diacritics` are "
            "deliberate, not typos.",
        ],
        "rules": [
            ("pl-brand-case-params",
             "Brand terms carry grammatical-case parameters; correct Polish.",
             {"check": "term_params", "text": "case"}),
        ],
    },
    "nl": {
        "notes": [
            "The register is formal `u` / `uw`, used exclusively.",
            "The apostrophe is `’`; quotes are both `‘…’` and `“…”`.",
            "The **en dash** `–` is the house dash. The em dash in "
            "`browser-main-window-titles*` is the deviation, and the en dash in "
            "`downloadUtils.ftl` is deliberate despite the en-US comment saying "
            "“em dash”.",
            "Labels are sentence case; menu commands and checkboxes use the "
            "infinitive.",
            "Closed one-word compounds are correct Dutch, not typos.",
            "Where en-US wraps a single variant in `{ $n -> *[other] … }` and the "
            "Dutch flattens it, that is not a defect.",
            "A term reference passing a parameter the Dutch term ignores is "
            "harmless in Fluent.",
        ],
        "rules": [
            ("nl-en-dash", "The en dash is this locale's house dash.",
             {"check": "typography", "text": "dash"}),
        ],
    },
    "es-ES": {
        "notes": [
            "Peninsular spelling: `vídeo`, not `video`.",
            "`¿` and `¡` are required at the start of questions and exclamations.",
            "The register skews to *usted* but is not consistent; treat "
            "normalization as one decision rather than per-string defects.",
        ],
        "rules": [],
    },
    "es-MX": {
        "notes": [
            "Inverted `¿` and `¡` are used correctly throughout.",
            "Access keys were kept from English rather than remapped. This is one "
            "decision for the locale team, reported systemically.",
        ],
        "rules": [],
    },
    "ru": {
        "notes": [
            "Brand terms take a `$case` parameter; this is correct Russian "
            "declension and has no en-US equivalent.",
            "The `несколько ({ $n })` plural strategy and the extra `$count` "
            "interpolation are deliberate.",
            "Example passwords and search-keyword lists that look like defects "
            "are intentional.",
            "Access keys were kept from English rather than remapped — one "
            "systemic decision.",
        ],
        "rules": [
            ("ru-brand-case-params",
             "Brand terms carry a `case` parameter; correct Russian declension.",
             {"check": "term_params", "text": "case"}),
        ],
    },
    "pt-BR": {"notes": [], "rules": []},
    "fy-NL": {"notes": [], "rules": []},
}


def write_locale_files(project, locale, counts, date, log) -> None:
    seeded = SEEDED.get(locale, {"notes": [], "rules": []})
    directory = project.locale_dir(locale)
    os.makedirs(directory, exist_ok=True)

    conv_path = os.path.join(directory, "conventions.md")
    body = conventions.draft(locale, counts, date)
    if seeded["notes"]:
        instructions = "\n".join(f"- {n}" for n in seeded["notes"])
        body = body.replace(
            "<!-- Add rules here, e.g.:\n"
            "- Access keys are intentionally left as English letters; never flag them.\n"
            "- The en dash is the house dash; do not suggest an em dash.\n"
            '- "Primary Password" is deliberately translated with the legacy term.\n'
            "-->",
            instructions,
        )
        body = body.replace(
            "## Instructions for the reviewer",
            "## Instructions for the reviewer\n\n_Carried over from the "
            "hand-written review; these are maintainer decisions, not guesses._",
        )
    with open(conv_path, "w", encoding="utf-8") as fh:
        fh.write(body)

    lines = [suppress.TEMPLATE.format(locale=locale).replace("rules: []\n", "rules:\n")]
    if seeded["rules"]:
        for rule_id, reason, match in seeded["rules"]:
            conditions = "\n".join(f"      {k}: {v!r}" for k, v in match.items())
            lines.append(
                f"  - id: {rule_id}\n"
                f"    reason: >-\n      {reason}\n"
                f"    match:\n{conditions}\n"
            )
    else:
        lines[0] = lines[0].replace("rules:\n", "rules: []\n")
    with open(suppress.path(project, locale), "w", encoding="utf-8") as fh:
        fh.write("".join(lines))
    log(f"    conventions + {len(seeded['rules'])} suppression rules written")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox")
    ap.add_argument("--reports", default="~/Desktop/Claude_qa_l10n")
    ap.add_argument("--l10n-dir", default="~/mozilla/git/firefox-l10n")
    ap.add_argument("--source-dir", default="~/mozilla/git/firefox-quarantine")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    reports_dir = os.path.expanduser(args.reports)
    l10n_dir = os.path.expanduser(args.l10n_dir)
    source_dir = os.path.expanduser(args.source_dir)

    project = config.load(args.project)
    summ = load_summarize(reports_dir)
    originals = os.path.join(reports_dir, "originals")
    today = datetime.date.today().isoformat()

    print(f"reference: {source_dir} @ {repos.head_sha(source_dir)}")
    source = parse.parse_tree(source_dir, project.extensions, project.exclude)
    l10n_sha = repos.head_sha(l10n_dir)
    print(f"locales:   {l10n_dir} @ {l10n_sha}")

    totals = {"strings": 0, "open": 0, "fixed": 0, "suppressed": 0, "unresolved": 0}
    for filename, (locale, date, rev, headings) in summ.REPORTS.items():
        if locale not in project.locales:
            print(f"\n{locale}: not in config.yaml, skipped")
            continue
        print(f"\n{locale} — {filename} (reviewed {date} @ {rev})")
        tree = os.path.join(l10n_dir, project.locale_subpath(locale))
        l10n = parse.parse_tree(tree, project.extensions, project.exclude)
        index = build_index(l10n)

        records = extract(os.path.join(originals, filename), headings, filename, summ)
        found, unresolved = convert(locale, records, index, l10n, summ, date)

        counts = {s: sum(1 for f in found if f.status == s)
                  for s in ("open", "fixed", "suppressed")}
        print(f"    {len(records)} report items -> {len(found)} findings "
              f"({counts['open']} open, {counts['fixed']} already fixed, "
              f"{counts['suppressed']} dismissed in-report), "
              f"{unresolved} ids unresolved")
        totals["strings"] += len(found)
        for status in ("open", "fixed", "suppressed"):
            totals[status] += counts[status]
        totals["unresolved"] += unresolved

        if args.dry_run:
            continue

        counts_conv = conventions.detect(locale, l10n)
        write_locale_files(project, locale, counts_conv, today, print)

        rules = suppress.load(project, locale)
        hits = suppress.apply(rules, found)
        if hits:
            print(f"    seeded suppressions retired: {hits}")

        findings_mod.save(project, locale, found)
        conventions.save(project, locale, counts_conv)
        snapshot.save(
            os.path.join(project.state_dir(locale), "strings.json"),
            snapshot.build(l10n, source),
        )
        meta = {
            "locale": locale,
            "mode": "imported",
            "last_run": today,
            "previous_run": date,
            "previous_sha": rev,
            "l10n_repo": project.data["repos"]["l10n"]["url"],
            "l10n_sha": l10n_sha,
            "source_repo": project.data["repos"]["source"]["url"],
            "source_sha": repos.head_sha(source_dir),
            "reviewed": 0,
            "strings": len(l10n),
            "missing": sum(1 for k in source if k not in l10n),
            "open": sum(1 for f in found if f.is_open),
            "fixed_total": sum(1 for f in found if f.status == "fixed"),
            "suppressed": sum(1 for f in found if f.status == "suppressed"),
            "imported_from": filename,
        }
        path = os.path.join(project.state_dir(locale), "meta.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(meta, fh, indent=1, sort_keys=True)
            fh.write("\n")

    print("\n" + "=" * 62)
    print(f"imported {totals['strings']} findings: {totals['open']} open, "
          f"{totals['fixed']} already fixed, {totals['suppressed']} dismissed")
    print(f"{totals['unresolved']} ids could not be resolved to a message in the "
          "current tree and were dropped")
    print(
        "\nKnown limitations, inherited from the extractor these reports were\n"
        "written for: a handful of items cite a token that is prose rather than\n"
        "a string id; strings named only inside an explanation, after the em\n"
        "dash, are not counted; and `current`/`suggest` are parsed from prose,\n"
        "so a finding whose `current` came out empty cannot be auto-verified\n"
        "and will be surfaced for a re-read instead of silently closed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
