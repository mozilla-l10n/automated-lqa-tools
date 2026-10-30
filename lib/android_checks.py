"""Checks for Android string resources, shared by the two Android projects.

Firefox for Android (`android/`) and Focus (`focus_android/`) read the same
file format from the same repository, so what is peculiar to that format
lives here rather than being copied into each project's `tools/checks.py`.

**Escaping.** In an Android XML resource a bare apostrophe or double quote
is not merely ugly, it fails the build with "Unescaped apostrophe in
string". moz.l10n unescapes on parse, so the defect is invisible in the
model and has to be read from the file.
"""

from __future__ import annotations

import os
import re

from common_checks import _mk
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
                    f"(“Unescaped apostrophe in string”). Write \\{bad}, or "
                    "wrap the whole value in double quotes."
                ),
                impact=1,
            ))
    return out


CHECKS = {
    "escaping": lambda c: check_escaping(c.project, c.locale, c.l10n, c.trees),
}
