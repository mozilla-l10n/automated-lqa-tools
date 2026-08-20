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
    # The offline message tells the user to press "Riprova"; the button it
    # names reads "Riprovare". A cross-string defect, so it is a check
    # rather than a model finding -- the pair is re-derived every run, and
    # fixing *either* string closes it.
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

    needed = sorted({loc for loc, *_ in MUST_FIND + MUST_BE_SILENT})
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

    print("\nMust stay silent")
    for locale, kind, why in MUST_BE_SILENT:
        health, _, _ = results[locale]
        n = health.counts.get(kind, 0)
        check(n == 0, f"{locale}: {kind} = {n} ({why})")

    print("\nAndroid check internals")
    from checks import PRINTF, _specs, _unescaped

    check([m[4] for m in PRINTF.findall("%1$s and %2$,d")] == ["s", "d"],
          "printf specs parse, including flags like %2$,d")
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

    print("\nProject wiring")
    check("variables" not in project.checks,
          "the redundant variables check is not run for Android")
    check(project.baseline_strategy == "batched",
          "from-scratch reviews are batched, not agent-driven")

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
