#!/usr/bin/env python3
"""Self-test against real locale trees.

The deterministic checks are only worth anything if they agree with the
fourteen hand-written reviews: they must find the defects those reviews
found by hand, and stay silent on the conventions those reviews established
as correct. Both directions matter, and the second one more -- a checker
that cries wolf on correct Japanese ellipsis or Polish case declension is
worse than no checker.

Needs local clones; it reads them and writes nothing.

    python firefox/tools/selftest.py \\
        --l10n-dir ~/mozilla/git/firefox-l10n \\
        --source-dir ~/mozilla/git/firefox-quarantine
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import checks  # noqa: E402
import config  # noqa: E402
import conventions  # noqa: E402
import findings as findings_mod  # noqa: E402
import parse  # noqa: E402
import suppress  # noqa: E402

# Defects the manual reviews found by hand. Each must still be caught.
# Anything the locale team has since fixed is listed under FIXED_UPSTREAM
# instead of being quietly deleted -- the difference between "the check
# broke" and "the defect is gone" is the whole point of the system.
MUST_FIND = [
    ("tr", "term_params", "fxa-signout-dialog-body-aiwindow"),
    ("sl", "term_params", "firefox-relay-must-login-to-fxa"),
    ("de", "markup", "about-logins-import-dialog-items-no-change2"),
    ("it", "markup", "about-glean-about-data-list-item-dictionary"),
]

FIXED_UPSTREAM = [
    # The Turkish string no longer passes `plural-form` to the brand term.
    ("tr", "term_params", "ai-window-learn-from-browsing-activity"),
    # The Dutch team repaired all three malformed closing tags the nl review
    # reported; nl markup findings are now legitimately zero.
    ("nl", "markup", "genai-settings-chat-gemini-links"),
    ("nl", "markup", "about-logins-import-dialog-items-no-change2"),
    ("nl", "markup", "cfr-doorhanger-milestone-heading2"),
]

# Conventions the reviews established as correct. These checks must be
# silent, or explicitly skipped for the locale.
MUST_BE_SILENT = [
    ("ja", "typography", "Japanese uses ASCII ellipsis, not …"),
    ("ja", "accesskey", "Japanese access keys are deliberately English"),
    ("zh-CN", "accesskey", "access keys are meaningless in Chinese"),
    ("nl", "typography", "the en dash is the Dutch house dash"),
    ("pl", "accesskey", "Polish access keys are correctly remapped"),
    ("tr", "accesskey", "Turkish access keys are correctly remapped"),
    ("it", "accesskey", "Italian access keys are correctly remapped"),
    ("it", "variables", "Italian has no variable mismatches"),
    ("it", "selectors", "Italian has no selector mismatches"),
    ("sl", "variables", "Slovenian sklon case params are not mismatches"),
    ("sl", "selectors", "Slovenian sklon case params are not mismatches"),
]

# Health numbers that should stay in the right neighbourhood. Completeness
# drifts with every upstream sync, so these are bounds, not equalities.
HEALTH_BOUNDS = [
    ("it", "missing", 0, 50),
    ("nl", "missing", 0, 200),
    ("ja", "syntax", 0, 0),
    ("it", "syntax", 0, 0),
]


def run(l10n_dir, source_dir, project) -> int:
    src = parse.parse_tree(source_dir, project.extensions, project.exclude)
    print(f"en-US reference: {len(src):,} strings\n")

    needed = sorted({loc for loc, *_ in MUST_FIND + MUST_BE_SILENT + FIXED_UPSTREAM}
                    | {loc for loc, *_ in HEALTH_BOUNDS})
    results = {}
    for locale in needed:
        root = os.path.join(l10n_dir, project.locale_subpath(locale))
        tree = parse.parse_tree(root, project.extensions, project.exclude)
        counts = conventions.detect(locale, tree)
        health, found = checks.run_all(
            project, locale, root, source_dir, tree, src, counts
        )
        results[locale] = (health, found, counts)

    passed = failed = 0

    def check(ok, label):
        nonlocal passed, failed
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if ok:
            passed += 1
        else:
            failed += 1

    print("Defects the manual reviews found — must still be caught")
    for locale, kind, string_id in MUST_FIND:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(hit, f"{locale}: {kind} on {string_id}")

    print("\nDefects since fixed upstream — must NOT be reported any more")
    for locale, kind, string_id in FIXED_UPSTREAM:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(not hit, f"{locale}: {kind} on {string_id} is gone")

    print("\nConventions established as correct — must stay silent")
    for locale, kind, why in MUST_BE_SILENT:
        health, _, _ = results[locale]
        silent = kind in health.skipped or health.counts.get(kind, 0) == 0
        state = "skipped" if kind in health.skipped else health.counts.get(kind, 0)
        check(silent, f"{locale}: {kind} = {state} ({why})")

    print("\nHealth numbers in range")
    for locale, metric, low, high in HEALTH_BOUNDS:
        health, _, _ = results[locale]
        value = len(health.syntax_errors) if metric == "syntax" else health.missing
        check(low <= value <= high, f"{locale}: {metric} = {value} (expected {low}–{high})")

    print("\nFinding lifecycle")
    from findings import Finding
    f = Finding(locale="xx", file="a.ftl", string_id="s", category="A",
                summary="malformed tag", current="text</a >here")
    check(f.status == "open", "a new finding starts open")
    check(findings_mod.still_present("text</a >here", "text</a >here more"),
          "an unchanged defect is detected as still present")
    check(not findings_mod.still_present("text</a >here", "text</a>here more"),
          "a punctuation-only repair is detected as fixed")
    check(f.identity() == Finding(**{**f.__dict__, "fid": ""}).identity(),
          "identity is stable across reconstruction")

    print("\nSuppression rules")
    from suppress import Rule
    rule = Rule({"id": "r", "reason": "because", "match": {"check": "typography",
                                                           "string_id": "felt-*"}}, 0)
    g = Finding(locale="xx", file="a.ftl", string_id="felt-error-x", category="E",
                check="typography", summary="straight apostrophe")
    h = Finding(locale="xx", file="a.ftl", string_id="other-x", category="E",
                check="typography", summary="straight apostrophe")
    check(rule.applies(g), "a prefix rule matches its string")
    check(not rule.applies(h), "a prefix rule does not over-match")
    suppress.apply([rule], [g, h])
    check(g.status == "suppressed" and g.suppressed_by == "r", "matching finding is suppressed")
    check(h.status == "open", "non-matching finding stays open")
    suppress.apply([], [g, h])
    check(g.status == "open" and not g.suppressed_by, "removing the rule restores the finding")

    for bad, why in (
        ({"id": "x", "match": {"check": "typography"}}, "a rule with no reason"),
        ({"id": "x", "reason": "r"}, "a rule that matches nothing"),
        ({"id": "x", "reason": "r", "match": {"nope": 1}}, "an unknown match field"),
    ):
        try:
            Rule(bad, 0)
            check(False, f"{why} is rejected")
        except ValueError:
            check(True, f"{why} is rejected")

    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox")
    ap.add_argument("--l10n-dir", default="~/mozilla/git/firefox-l10n")
    ap.add_argument("--source-dir", default="~/mozilla/git/firefox-quarantine")
    args = ap.parse_args(argv)
    return run(
        os.path.expanduser(args.l10n_dir),
        os.path.expanduser(args.source_dir),
        config.load(args.project),
    )


if __name__ == "__main__":
    raise SystemExit(main())
