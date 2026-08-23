#!/usr/bin/env python3
"""Self-test for the Firefox for iOS project, against a real clone.

Same intent as the other two suites: the checks must catch the defects that
are really there, and stay silent on everything correct. The XLIFF layout
gets its own assertions, because it is the part that is genuinely new --
source and target come out of one file, and an untranslated unit is an empty
pattern rather than an absent entry.

    python firefox_ios/tools/selftest.py --l10n-dir ~/github/firefoxios-l10n
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
import selftest_lib  # noqa: E402

# Real defects in the repository today.
MUST_FIND = [
    # `%%3$@$s` -- the doubled percent escapes to a literal, so the third
    # link never renders.
    ("dsb", "placeholders", "FirefoxHome.PrivacyNotice.Body.v148"),
    # `%S` where the source passes an integer with `%d`.
    ("oc", "placeholders", "FirefoxHome.Pocket.Minutes.v99"),
    ("scn", "placeholders", "CloseTabsToast.Title.v113"),
]

# Locales and checks that must produce nothing.
MUST_BE_SILENT = [
    ("it", "placeholders", "Italian placeholders are correct"),
    ("it", "typography", "Italian typography is correct"),
    ("it", "ui_references", "Italian UI references are consistent"),
    ("de", "placeholders", "German placeholders are correct"),
    ("fr", "placeholders", "French placeholders are correct"),
    ("es-ES", "placeholders", "Spanish placeholders are correct"),
]

# Completeness, which the layout has to get right for an XLIFF where an
# untranslated unit is present-but-empty rather than missing.
#
# Stated as relationships, not counts: the reference gains strings on every
# import, and pinning 1,894 meant the suite broke the first time upstream
# added sixteen. What must hold is that `it` is complete and `bo` has barely
# started, whatever the totals are.
COMPLETENESS = [
    ("it", "complete"),
    ("bo", "barely-started"),
]


def run(l10n_dir, project) -> int:
    suite = selftest_lib.Suite()
    check = suite.check
    results = selftest_lib.load_results(
        project, checks, l10n_dir, l10n_dir,
        [loc for loc, *_ in MUST_FIND + MUST_BE_SILENT + COMPLETENESS],
    )

    print("XLIFF layout")
    trees = results["it"][2]
    check(len(trees.l10n) > 1500, f"the locale file parses ({len(trees.l10n)} units)")
    check(len(trees.source) == len(trees.l10n),
          f"the source side comes from the same run ({len(trees.source)})")
    check(len(trees.l10n_files) > 50,
          f"units are grouped by their originating .strings file ({len(trees.l10n_files)})")
    sample = next(iter(trees.l10n))
    check(sample[0].endswith(".strings") or sample[0].endswith(".stringsdict"),
          f"the group is part of the key ({sample[0]})")
    check(all(v.endswith("firefox-ios.xliff") for v in trees.locale_paths.values()),
          "every group maps back to the one physical file")

    suite.section("The source is the reference locale, not the target's own copy")
    key = next(k for k, m in trees.l10n.items() if "%1$@" in m.text())
    import common_checks as cc
    check(trees.source[key].raw[""] is not trees.l10n[key].raw[""],
          "source and target are distinct parsed messages")
    check(cc._specs(trees.source[key].raw[""]),
          "the source message still carries its placeholder specs")

    suite.section("Placeholders")
    check([m[4] for m in cc.PRINTF.findall("%@ and %1$@")] == ["@", "@"],
          "the shared regex accepts iOS's %@ and %1$@")
    check([m[4] for m in cc.PRINTF.findall("%d and %1$s")] == ["d", "s"],
          "and still accepts the Android forms")

    suite.section("Completeness")
    for locale, shape in COMPLETENESS:
        health, _, trees_ = results[locale][0], None, results[locale][2]
        units = len(trees_.source)
        check(health.strings + health.missing == units,
              f"{locale}: translated + missing = {health.strings}+{health.missing} "
              f"accounts for all {units} units")
        if shape == "complete":
            check(health.missing == 0,
                  f"{locale}: fully translated ({health.strings} of {units})")
        else:
            check(health.missing > units * 0.8,
                  f"{locale}: barely started ({health.strings} of {units}) -- an "
                  "empty target counts as untranslated, not as an empty string")

    selftest_lib.must_find(suite, results, MUST_FIND)
    selftest_lib.must_be_silent(suite, results, MUST_BE_SILENT)

    suite.section("Project wiring")
    for absent in ("plurals", "selectors", "markup", "escaping", "variables"):
        check(absent not in project.checks,
              f"`{absent}` is not run: it cannot fire in this project")
    check(project.baseline_strategy == "batched",
          "from-scratch reviews are batched, not agent-driven")

    selftest_lib.deliberate_flag_wiring(suite, project)
    return suite.report()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox_ios")
    ap.add_argument("--l10n-dir", default="~/github/firefoxios-l10n")
    args = ap.parse_args(argv)
    return run(os.path.expanduser(args.l10n_dir), config.load(args.project))


if __name__ == "__main__":
    raise SystemExit(main())
