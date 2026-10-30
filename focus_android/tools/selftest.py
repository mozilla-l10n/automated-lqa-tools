#!/usr/bin/env python3
"""Self-test for the Focus project, against a real android-l10n clone.

Focus has no deterministic defect in any locale this project covers today,
so unlike the other suites there is no MUST_FIND table: a pinned defect has
to be real, and none is. What this suite pins instead is what the split
from Firefox for Android has to keep true -- Focus is checked alone, but
its conventions are counted together with Firefox for Android's, and a
quoted label may name an Android Components string and nothing in Fenix.

    python focus_android/tools/selftest.py --l10n-dir ~/github/android-l10n
"""

from __future__ import annotations

import argparse
import glob
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(_HERE)), "lib"))

import checks  # noqa: E402
import config  # noqa: E402
import conventions  # noqa: E402
import layout  # noqa: E402
import selftest_lib  # noqa: E402

FOCUS = "mozilla-mobile/focus-android/"
COMPONENTS = "mozilla-mobile/android-components/"

# Locales and checks that must produce nothing.
MUST_BE_SILENT = [
    ("it", "placeholders", "Italian placeholders are correct"),
    ("it", "escaping", "Italian escaping is correct"),
    ("it", "markup", "Italian markup is correct"),
    ("fr", "placeholders", "French placeholders are correct"),
    ("de", "markup", "German markup is correct"),
    # Measured on Focus alone, each of these inferred a convention from one
    # or two characters, against the thousands the rest of the locale's tree
    # writes the other way: en-GB "curly-single" from one quote, es-ES "em"
    # from two dashes, sk "straight-double" from one. Counted together with
    # Firefox for Android, none of them is a majority to deviate from.
    ("en-GB", "typography", "British English quotes as the rest of its tree does"),
    ("es-ES", "typography", "Spanish dashes as the rest of its tree does"),
    ("sk", "typography", "Slovak quotes are mixed across the tree"),
    ("uk", "typography", "Ukrainian quotes are mixed across the tree"),
]


def run(l10n_dir, project) -> int:
    suite = selftest_lib.Suite()
    check = suite.check
    results = selftest_lib.load_results(
        project, checks, l10n_dir, l10n_dir,
        ["it", "en-GB"] + [loc for loc, *_ in MUST_BE_SILENT],
    )

    print("Layout")
    trees = results["it"][2]
    check(trees.l10n_files and all(f.startswith(FOCUS) for f in trees.l10n_files),
          f"only Focus files are checked ({len(trees.l10n_files)})")
    check(all(f.startswith(FOCUS) for f, _ in trees.source),
          "no Firefox for Android string is on the checked source side")
    sample = next(iter(trees.locale_paths.values()))
    check("values-it/" in sample, f"the Android locale directory is used ({sample.split('/')[-2]})")
    check(len(trees.source) > 200, f"the source side loaded ({len(trees.source)} strings)")

    suite.section("Context: read, never checked")
    check(trees.context_source and all(f.startswith(COMPONENTS) for f, _ in trees.context_source),
          f"a quoted label may name an Android Components string "
          f"({len(trees.context_source)}), and nothing in Fenix")
    check(not set(trees.context_source) & set(trees.source),
          "no string is both checked and context")
    check(len(trees.context_conventions) > 10 * len(trees.l10n),
          "conventions are counted over Firefox for Android's tree as well")
    check(not set(trees.context_conventions) & set(trees.l10n),
          "and that count does not add strings to the checked tree")
    _health, found, _ = results["it"]
    check(all(f.file.startswith(FOCUS) for f in found),
          "every finding is on a Focus string")

    suite.section("Conventions agree with Firefox for Android")
    # The point of counting both trees: the same team, the same locale, one
    # answer. If the two projects disagreed, one of them would be flagging
    # the locale for following the other.
    android = config.load("android")
    for loc in ("it", "en-GB", "sk", "es-ES"):
        mine = conventions.detect(loc, results[loc][2].measured())
        theirs = conventions.detect(loc, layout.load(android, loc, l10n_dir, l10n_dir).measured())
        groups = [g for g in mine if g != "_meta"]
        check(all(conventions.preferred(mine, g) == conventions.preferred(theirs, g)
                  for g in groups),
              f"{loc}: every inferred convention matches")

    suite.section("Language variants learn from the shared corpus")
    import variants as _v
    trees = results["en-GB"][2]
    alone = _v.learn(trees.l10n, trees.source)
    shared = _v.learn(trees.measured(), trees.measured_source())
    check(not alone and shared,
          f"Focus alone shows no substitution, the locale's tree shows {len(shared)}")

    selftest_lib.must_be_silent(suite, results, MUST_BE_SILENT)

    suite.section("Checks that cannot fire are not run")
    # Recorded in tools/checks.py. If Focus ever ships a <plurals>, this
    # fails and the two checks go back into config.yaml.
    refs = glob.glob(os.path.join(l10n_dir, FOCUS, "**", "values", "strings.xml"),
                     recursive=True)
    has_plurals = any("<plurals" in open(p, encoding="utf-8").read() for p in refs)
    check(refs and not has_plurals, "Focus's source has no <plurals>")
    check("plurals" not in project.checks and "selectors" not in project.checks,
          "so plurals and selectors are not run")

    suite.section("Project wiring")
    check("variables" not in project.checks,
          "the redundant variables check is not run, as for Firefox for Android")
    check("pt-PT" not in project.locales, "pt-PT, which Focus does not ship, is not listed")
    check(project.baseline_strategy == "batched",
          "from-scratch reviews are batched, as for Firefox for Android")
    import llm_incremental as _llm
    for loc in ("en-GB", "en-CA"):
        check(bool(_llm.system_prompt(project, loc).strip()),
              f"{loc}: the variant reviewer has a prompt to run with")

    selftest_lib.deliberate_flag_wiring(suite, project)
    selftest_lib.comment_is_evidence(suite, project)
    return suite.report()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="focus_android")
    ap.add_argument("--l10n-dir", default="~/github/android-l10n")
    args = ap.parse_args(argv)
    return run(os.path.expanduser(args.l10n_dir), config.load(args.project))


if __name__ == "__main__":
    raise SystemExit(main())
