"""Checks this project runs, composed from the shared modules.

Everything that reasons about messages in the abstract -- completeness,
placeholders, plural categories, markup, typography -- is shared, in
`lib/common_checks.py`. The one Android-specific check, unescaped
apostrophes and quotes that fail the build, is in `lib/android_checks.py`,
because Focus (`focus_android/`) reads the same format.

There is deliberately no `translatable="false"` check: the android-l10n
repository exports only translatable strings, so the attribute never appears
and the check could not fire.

`plurals` does not report a dead variant in a locale whose only plural
category is `other`. A plural form cannot be removed from an Android string,
so zh-TW's and ja's unreachable `one` has no fix: the three findings raised
for it were reported as noise. A missing form is still reported (cs, sk).
"""

from __future__ import annotations

import android_checks
import common_checks as common

CHECKS = {
    **common.CHECKS,
    **android_checks.CHECKS,
    "plurals": lambda c: common.check_plurals(c.locale, c.l10n, c.source,
                                              dead_removable=False),
}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
