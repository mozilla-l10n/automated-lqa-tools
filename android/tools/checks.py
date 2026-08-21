"""Checks specific to Android string resources.

Everything that reasons about messages in the abstract -- completeness,
variables, plural categories, markup, typography -- is shared, in
`lib/common_checks.py`. Two things are peculiar to Android and can break an
app rather than merely read badly.

The printf placeholder check that used to live here is now shared, in
`lib/common_checks.py`: iOS needs exactly the same comparison, only with
`%@` in the conversion set. What is left is one thing, and it can break a
build rather than merely read badly.

**Escaping.** In an Android XML resource a bare apostrophe or double quote
is not merely ugly, it fails the build with "Unescaped apostrophe in
string". moz.l10n unescapes on parse, so the defect is invisible in the
model and has to be read from the file.

There is deliberately no `translatable="false"` check: the android-l10n
repository exports only translatable strings, so the attribute never appears
and the check could not fire.
"""

from __future__ import annotations

import os
import re

import common_checks as common
from common_checks import Health, _mk  # noqa: F401
from findings import Finding

# A bare apostrophe or double quote inside a string body fails the build,
# unless the whole body is wrapped in double quotes.
_COMMENT = re.compile(r"<!--.*?-->", re.S)
_STRING_EL = re.compile(
    r"<(string|item)\b([^>]*)>(.*?)</\1>", re.S
)
_CDATA = re.compile(r"<!\[CDATA\[.*?\]\]>", re.S)


def _unescaped(body: str) -> str | None:
    """The offending character, or None if the body is safely escaped."""
    text = _CDATA.sub("", body)
    if text.strip().startswith('"') and text.strip().endswith('"'):
        return None  # fully quoted: everything inside is literal
    if re.search(r"(?<!\\)'", text):
        return "'"
    if re.search(r'(?<!\\)"', text):
        return '"'
    return None


def check_escaping(project, locale, l10n, trees) -> list[Finding]:
    """Unescaped apostrophes and quotes, read from the file itself.

    moz.l10n unescapes on parse, so this cannot be done on the model.
    """
    if trees is None:
        return []
    out = []
    for rel in sorted(trees.l10n_files):
        path = os.path.join(trees.root, trees.locale_paths.get(rel, rel))
        try:
            with open(path, encoding="utf-8") as fh:
                raw = fh.read()
        except OSError:
            continue
        body_only = _COMMENT.sub("", raw)
        for _tag, attrs, body in _STRING_EL.findall(body_only):
            bad = _unescaped(body)
            if bad is None:
                continue
            name = re.search(r'name="([^"]+)"', attrs)
            if name is None:
                continue
            msg = l10n.get((rel, name.group(1)))
            if msg is None:
                continue
            out.append(_mk(
                locale, msg, "A", "escaping",
                f"`{msg.id}` contains an unescaped {bad}",
                current=body.strip()[:200],
                rationale=(
                    f"An unescaped {bad} in an Android string resource fails the build "
                    f"(“Unescaped apostrophe in string”). Write \\\\{bad}, or "
                    "wrap the whole value in double quotes."
                ),
                impact=1,
            ))
    return out


CHECKS = {
    **common.CHECKS,
    "escaping": lambda c: check_escaping(c.project, c.locale, c.l10n, c.trees),
}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
