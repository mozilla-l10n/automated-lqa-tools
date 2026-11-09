"""Checks this project runs, composed from the shared modules.

Everything that reasons about messages in the abstract -- completeness,
placeholders, plural categories, markup, typography -- is shared, in
`lib/common_checks.py`. The one Android-specific check, unescaped
apostrophes and quotes that fail the build, is in `lib/android_checks.py`,
because Focus (`focus_android/`) reads the same format.

There is deliberately no `translatable="false"` check: the android-l10n
repository exports only translatable strings, so the attribute never appears
and the check could not fire.

Nor is there a `plurals` check, because every finding it can raise here is
wrong (checked against all 34 locales' 623 plurals on 2026-11-09):

- *A missing form.* Pontoon has the translator fill every form in the
  locale's own plural definition, and exports the last of them as Android's
  `other`. Measured against CLDR, or against the tree's majority, that read
  as gaps: cs and sk were told to add `many`, which Pontoon does not use
  for them (17 older strings each still carry one); pl, ru and uk "lack"
  `many` because it is written as `other`.
- *A variant the language never selects.* Only a language without `one`
  can have one, and each of those (id, ja, ko, th, vi, zh-CN, zh-TW) has
  only `other`. The `one` they carry comes from en-US, and a plural form
  cannot be removed from an Android string, so the finding has no fix.
"""

from __future__ import annotations

import android_checks
import common_checks as common

CHECKS = {**common.CHECKS, **android_checks.CHECKS}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
