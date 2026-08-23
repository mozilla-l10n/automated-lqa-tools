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
import layout  # noqa: E402
import selftest_lib  # noqa: E402

# Real defects in the repository, by (locale, check, string id).
MUST_FIND = [
    # The Czech strings drop a placeholder the source passes -- from every
    # category, so the count never reaches the user.
    ("cs", "placeholders", "recently_closed_tab"),
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
    # Numbering a placeholder the source left bare, or leaving bare one the
    # source numbered, is the same format string -- translators reach for
    # the numbered form when the target word order differs. All four of
    # these were reported as defects until the check compared arguments by
    # position instead of by how they were written.
    ("de", "placeholders", "German numbers a placeholder en-US left bare"),
    ("sl", "placeholders", "Slovenian leaves bare one en-US numbered"),
    ("fy-NL", "placeholders", "Frisian numbers a placeholder en-US left bare"),
    ("pl", "placeholders", "Polish uses one argument once where en-US used it twice"),
    # en-US writes the count into `other` and not into `one` -- "Delete
    # file?" beside "Delete %d files?" -- and Chinese has only `other`.
    # Comparing one representative variant read that as an invented
    # placeholder.
    ("zh-CN", "placeholders", "Chinese uses the argument en-US passes in `other`"),
    # The mirror image, and the reason the comparison is a union rather
    # than a category-by-category pairing: Arabic writes the numeral into
    # `few`, `many` and `other` and leaves it out of `zero`, `one` and
    # `two`, where the category already says the count. en-US does the same
    # thing in `one`. Pairing categories would call one of them a defect
    # whichever way round it was done.
    ("ar", "placeholders", "Arabic omits the numeral where the category "
                           "already carries the count"),
]


def run(l10n_dir, project) -> int:
    suite = selftest_lib.Suite()
    check = suite.check
    results = selftest_lib.load_results(
        project, checks, l10n_dir, l10n_dir,
        [loc for loc, *_ in MUST_FIND + MUST_BE_SILENT + FIXED_UPSTREAM],
    )

    print("Layout")
    trees = results["it"][2]
    check(len(trees.l10n_files) > 40, f"the TOML configs resolve to {len(trees.l10n_files)} files")
    check(bool(trees.locale_paths), "each reference file maps to a localized file")
    sample = next(iter(trees.locale_paths.values()))
    check("values-it/" in sample, f"the Android locale directory is used ({sample.split('/')[-2]})")
    check(len(trees.source) > 2000, f"the source side loaded ({len(trees.source)} strings)")

    suite.section("Placeholders render as the file writes them")
    key = next(
        (k for k, m in trees.l10n.items() if "%1$s" in m.text()), None
    )
    check(key is not None, "a `%1$s` placeholder survives parsing verbatim")

    selftest_lib.must_find(suite, results, MUST_FIND)
    selftest_lib.fixed_upstream(suite, results, FIXED_UPSTREAM)
    selftest_lib.must_be_silent(suite, results, MUST_BE_SILENT)

    suite.section("Android check internals")
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

    suite.section("Cross-string UI references")
    from common_checks import _is_label, _nearest
    check(_is_label("Try Again") and not _is_label("SameSite"),
          "a multi-word label is told from a technical token")
    check(not _is_label("%1$s items"), "a placeholder is not a label")
    check(_nearest(("a.xml", "foo_message"),
                   [("a.xml", "foo_button"), ("b.xml", "bar_button")]) == ("a.xml", "foo_button"),
          "the candidate in the same file wins")
    check(_nearest(("a.xml", "foo"), [("b.xml", "x"), ("c.xml", "y")]) is None,
          "an ambiguous reference across files is not guessed at")

    suite.section("Language variants")
    import variants as _v
    for loc in ("en-GB", "en-CA"):
        if loc not in project.locales:
            continue
        trees = layout.load(project, loc, l10n_dir, l10n_dir)
        rules = _v.learn(trees.l10n, trees.source)
        check(project.is_variant(loc), f"{loc} is configured as a variant")
        check(bool(rules), f"{loc}: spelling rules are learned from the corpus ({len(rules)})")
    check(_v.learn.__module__ == "variants", "the variant machinery is shared, not duplicated")

    suite.section("Placeholder equivalence")
    import common_checks as cc

    def _specs(text):
        return [(i or "", c.lower())
                for i, _f, _w, _p, c in cc.PRINTF.findall(text) if c != "%"]

    def _same(a, b):
        return cc._by_argument(_specs(a)) == cc._by_argument(_specs(b))

    check(_same("%s", "%1$s"),
          "a lone %s and a lone %1$s are the same format string")
    check(_same("%s %d", "%1$s %2$d"),
          "and so is numbering every placeholder in source order")
    check(_same("%1$s %2$s", "%2$s %1$s"),
          "reordering numbered arguments is what numbering is for")
    check(_same("%1$s %1$s", "%1$s"),
          "using one argument once where the source used it twice is legal")
    check(not _same("%s", ""),
          "but a dropped argument is still a dropped argument")
    check(not _same("%s", "%1$s %2$s"),
          "and so is an invented one")
    check(not _same("%s %d", "%d %s"),
          "swapping two bare placeholders of different types retypes both: "
          "String.format binds them by position, so it crashes")
    check(cc._by_argument(_specs("%s %1$s")) is None,
          "a string that mixes the two forms has no argument order to read, "
          "and is left to the check that reports the mixing")

    # A message's arguments are the union over its plural categories, not
    # whichever category happened to come first.
    def _args(*variants):
        return cc._arguments([_specs(v) for v in variants])

    check(_args("Delete file?", "Delete %d files?") == _args("删除 %d 个文件？"),
          "a locale with only `other` passes the same argument as an en-US "
          "plural that mentions the count in `other` alone")
    check(_args("%d file", "%d files") == {"1": "d"},
          "an argument named by every category is still one argument")
    check(_args("none here", "none either") == {},
          "and a plural that passes nothing reads as passing nothing")
    check(_args("%d", "%s") == {"1": None},
          "a position that means two things across categories still counts "
          "as an argument, but there is nothing to compare it against")
    check(_args("%s %1$s") is None,
          "one bad variant makes the whole message uncomparable")

    suite.section("Project wiring")
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

    selftest_lib.deliberate_flag_wiring(suite, project)
    return suite.report()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="android")
    ap.add_argument("--l10n-dir", default="~/github/android-l10n")
    args = ap.parse_args(argv)
    return run(os.path.expanduser(args.l10n_dir), config.load(args.project))


if __name__ == "__main__":
    raise SystemExit(main())
