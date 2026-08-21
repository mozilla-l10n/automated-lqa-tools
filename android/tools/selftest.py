#!/usr/bin/env python3
"""Self-test for the Android project, against a real android-l10n clone.

Mirrors the Firefox suite in intent: the checks must catch the defects that
are really there, and stay silent on everything that is correct. The
Android-specific ones are pinned against strings in other locales, because
`it` is clean and a check that never fires proves nothing.

    python android/tools/selftest.py --l10n-dir ~/github/android-l10n
"""

from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(_HERE)), "lib"))

import checks  # noqa: E402
import config  # noqa: E402
import conventions  # noqa: E402
import layout  # noqa: E402

# Real defects in the repository, by (locale, check, string id).
MUST_FIND = [
    # The Czech and Arabic strings drop a placeholder the source passes.
    ("cs", "placeholders", "recently_closed_tab"),
    ("ar", "placeholders", "tab_group_tabs_count_subtitle"),
    # German swapped %s for %1$s.
    ("de", "placeholders", "mozac_feature_sitepermissions_storage_access_message"),
    # Chinese added a placeholder the source does not have.
    ("zh-CN", "placeholders", "downloads_delete_dialog_title"),
    # Japanese has no `one` category, so that variant is unreachable.
    ("ja", "plurals", "downloads_delete_dialog_title"),
]

# Defects these checks caught that have since been fixed upstream. Kept
# rather than deleted, so "the check broke" stays distinguishable from "the
# defect is gone" -- which is the whole point of tracking findings.
FIXED_UPSTREAM = [
    # The offline message told the user to press "Riprova" while the button
    # read "Riprovare". A cross-string defect, so it is a check rather than
    # a model finding: the pair is re-derived every run, which is what let
    # fixing the *button* close it.
    ("it", "ui_references", "mozac_browser_errorpages_offline_message"),
]

# Locales and checks that must produce nothing.
MUST_BE_SILENT = [
    ("it", "placeholders", "Italian placeholders are correct"),
    ("it", "escaping", "Italian escaping is correct"),
    ("it", "plurals", "Italian plurals are correct"),
    ("it", "markup", "Italian markup is correct"),
    ("fr", "placeholders", "French placeholders are correct"),
    ("de", "ui_references", "German UI references are consistent"),
    ("ja", "ui_references", "Japanese UI references are consistent"),
    ("it", "ui_references", "Italian UI references are consistent again"),
    ("pt-BR", "placeholders", "Brazilian Portuguese placeholders are correct"),
]


def run(l10n_dir, project) -> int:
    passed = failed = 0

    def check(ok, label):
        nonlocal passed, failed
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if ok:
            passed += 1
        else:
            failed += 1

    needed = sorted({loc for loc, *_ in MUST_FIND + MUST_BE_SILENT + FIXED_UPSTREAM})
    results = {}
    for locale in needed:
        trees = layout.load(project, locale, l10n_dir, l10n_dir)
        counts = conventions.detect(locale, trees.l10n)
        results[locale] = checks.run_all(project, locale, trees, counts) + (trees,)

    print("Layout")
    trees = results["it"][2]
    check(len(trees.l10n_files) > 40, f"the TOML configs resolve to {len(trees.l10n_files)} files")
    check(bool(trees.locale_paths), "each reference file maps to a localized file")
    sample = next(iter(trees.locale_paths.values()))
    check("values-it/" in sample, f"the Android locale directory is used ({sample.split('/')[-2]})")
    check(len(trees.source) > 2000, f"the source side loaded ({len(trees.source)} strings)")

    print("\nPlaceholders render as the file writes them")
    key = next(
        (k for k, m in trees.l10n.items() if "%1$s" in m.text()), None
    )
    check(key is not None, "a `%1$s` placeholder survives parsing verbatim")

    print("\nDefects that are really there")
    for locale, kind, string_id in MUST_FIND:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(hit, f"{locale}: {kind} on {string_id}")

    print("\nFixed upstream — must no longer be reported")
    for locale, kind, string_id in FIXED_UPSTREAM:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(not hit, f"{locale}: {kind} on {string_id} is gone")

    print("\nMust stay silent")
    for locale, kind, why in MUST_BE_SILENT:
        health, _, _ = results[locale]
        n = health.counts.get(kind, 0)
        check(n == 0, f"{locale}: {kind} = {n} ({why})")

    print("\nAndroid check internals")
    from checks import _unescaped
    from common_checks import PRINTF

    check([m[4] for m in PRINTF.findall("%1$s and %2$,d")] == ["s", "d"],
          "printf specs parse, including flags like %2$,d")
    check([m[4] for m in PRINTF.findall("%@ and %1$@")] == ["@", "@"],
          "the shared regex also accepts iOS's %@, which Android never writes")
    check(_unescaped("Don't") == "'", "a bare apostrophe is caught")
    check(_unescaped(r"Don\'t") is None, "an escaped apostrophe is accepted")
    check(_unescaped('"Don\'t"') is None, "a fully quoted value is accepted")
    check(_unescaped("<![CDATA[Don't]]>") is None, "CDATA content is left alone")

    print("\nCross-string UI references")
    from common_checks import _is_label, _nearest
    check(_is_label("Try Again") and not _is_label("SameSite"),
          "a multi-word label is told from a technical token")
    check(not _is_label("%1$s items"), "a placeholder is not a label")
    check(_nearest(("a.xml", "foo_message"),
                   [("a.xml", "foo_button"), ("b.xml", "bar_button")]) == ("a.xml", "foo_button"),
          "the candidate in the same file wins")
    check(_nearest(("a.xml", "foo"), [("b.xml", "x"), ("c.xml", "y")]) is None,
          "an ambiguous reference across files is not guessed at")

    print("\nLanguage variants")
    import variants as _v
    for loc in ("en-GB", "en-CA"):
        if loc not in project.locales:
            continue
        trees = layout.load(project, loc, l10n_dir, l10n_dir)
        rules = _v.learn(trees.l10n, trees.source)
        check(project.is_variant(loc), f"{loc} is configured as a variant")
        check(bool(rules), f"{loc}: spelling rules are learned from the corpus ({len(rules)})")
    check(_v.learn.__module__ == "variants", "the variant machinery is shared, not duplicated")

    print("\nProject wiring")
    check("variables" not in project.checks,
          "the redundant variables check is not run for Android")
    check(project.baseline_strategy == "batched",
          "from-scratch reviews are batched, not agent-driven")
    # en-CA and en-GB died on a missing prompt after the whole tree had been
    # parsed, checked and queued -- the file is only opened at the moment
    # the reviewer is called.
    import llm_incremental as _llm
    for loc in ("en-GB", "en-CA"):
        if loc not in project.locales:
            continue
        check(bool(_llm.system_prompt(project, loc).strip()),
              f"{loc}: the variant reviewer has a prompt to run with")

    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="android")
    ap.add_argument("--l10n-dir", default="~/github/android-l10n")
    args = ap.parse_args(argv)
    return run(os.path.expanduser(args.l10n_dir), config.load(args.project))


if __name__ == "__main__":
    raise SystemExit(main())
