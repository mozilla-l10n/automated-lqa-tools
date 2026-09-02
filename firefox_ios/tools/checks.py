"""Checks for Firefox for iOS.

Every check this project runs is shared, in `lib/common_checks.py`. This
module exists to compose the registry and, more usefully, to record what is
deliberately *not* run -- each decision taken against the repository rather
than assumed:

**No plural checks.** There is no plural mechanism in this project at all:
no `.stringsdict`, no plural trans-units, and moz.l10n parses no
`SelectMessage` from the localization corpus. `variables` and `selectors`
go with them, since both exist to compare plural selectors and interpolated
arguments that `placeholders` already covers here in the syntax the file
actually uses.

**No markup check.** There are no HTML-ish tags in the localization corpus.

**No escaping, term or access-key checks.** Those are Android and Fluent
concepts; XLIFF escaping is XML escaping and the parser owns it.

Shipping a check that cannot fire is worse than not shipping it: it reads
as coverage and is only noise waiting to happen. The same reasoning removed
Android's `translatable` check.

The one thing iOS shares with Android is printf placeholders, and moz.l10n
exposes them identically -- `Expression(..., attributes={'source': '%1$@'})`
-- so `check_placeholders` lives in the shared library and serves both.
"""

from __future__ import annotations

import common_checks as common

CHECKS = dict(common.CHECKS)


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
