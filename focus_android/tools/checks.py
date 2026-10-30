"""Checks this project runs, composed from the shared modules.

Focus reads the same Android string resources as Firefox for Android, so
nothing here is its own: the message-level checks are in
`lib/common_checks.py` and Android escaping is in `lib/android_checks.py`.

Not run, and why -- each verified against the tree rather than assumed:

  plurals, selectors   focus-android's strings.xml has no <plurals> element
                       (250 <string>, 0 <plurals>), and on Android the only
                       selector is a plural's quantity
  translatable         as for android/: the repository exports only
                       translatable strings
"""

from __future__ import annotations

import android_checks
import common_checks as common

CHECKS = {**common.CHECKS, **android_checks.CHECKS}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
