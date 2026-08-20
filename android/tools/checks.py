"""Checks specific to Android string resources.

Everything that reasons about messages in the abstract -- completeness,
variables, plural categories, markup, typography -- is shared, in
`lib/common_checks.py`. Two things are peculiar to Android and can break an
app rather than merely read badly.

**printf placeholders.** Android formats through `String.format`, so a
placeholder carries a *type* as well as a position. `%1$s` where the source
says `%1$d` throws `IllegalFormatConversionException` at runtime rather than
rendering wrong, and mixing `%s` with `%1$s` in one string throws too. The
shared variable check compares argument *names*, which moz.l10n derives from
the position, so it catches a dropped or invented argument but not a
retyped one. This closes that gap.

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

from moz.l10n.model import Expression, PatternMessage, SelectMessage

import common_checks as common
from common_checks import Health, _mk  # noqa: F401
from findings import Finding

# %[argument_index$][flags][width][.precision]conversion
PRINTF = re.compile(
    r"%(?:(\d+)\$)?([-#+ 0,(]*)(\d+)?(?:\.(\d+))?([a-zA-Z%])"
)


def _specs(msg) -> list[tuple[str, str]]:
    """The printf placeholders of a message, as (index, conversion).

    Read from the `source` attribute moz.l10n keeps on each expression, so
    this is the literal text from the file rather than a reconstruction.
    Index is "" for a non-positional `%s`.
    """
    out: list[tuple[str, str]] = []

    def walk(pattern):
        for part in pattern:
            if not isinstance(part, Expression):
                continue
            literal = (part.attributes or {}).get("source")
            if not isinstance(literal, str):
                continue
            for index, _flags, _width, _prec, conv in PRINTF.findall(literal):
                if conv == "%":
                    continue
                out.append((index or "", conv.lower()))

    if isinstance(msg, PatternMessage):
        walk(msg.pattern)
    elif isinstance(msg, SelectMessage):
        # Every variant should carry the same placeholders; the first is
        # representative, and a variant that disagrees is caught by the
        # shared variable check.
        for variant in msg.variants.values():
            walk(variant)
            break
    return out


def _describe(specs) -> str:
    return ", ".join(f"%{i}${c}" if i else f"%{c}" for i, c in specs) or "none"


def check_placeholders(locale, l10n, source) -> list[Finding]:
    out = []
    for key, msg in l10n.items():
        src = source.get(key)
        if src is None:
            continue
        for prop, raw in msg.raw.items():
            if prop not in src.raw:
                continue
            want = _specs(src.raw[prop])
            got = _specs(raw)
            if not want and not got:
                continue

            label = f"`{msg.id}`" + (f" (`.{prop}`)" if prop else "")

            # A retyped argument is a runtime crash, not a rendering bug.
            by_index_src = {i: c for i, c in want if i}
            by_index_loc = {i: c for i, c in got if i}
            retyped = sorted(
                i for i, c in by_index_loc.items()
                if i in by_index_src and by_index_src[i] != c
            )
            if retyped:
                detail = ", ".join(
                    f"%{i}${by_index_src[i]} became %{i}${by_index_loc[i]}" for i in retyped
                )
                out.append(_mk(
                    locale, msg, "A", "placeholders",
                    f"{label} changes a placeholder's type: {detail}",
                    current=msg.props.get(prop, ""), suggest=src.props.get(prop, ""),
                    rationale=(
                        "Android formats these through String.format, which throws "
                        "IllegalFormatConversionException when the conversion does not "
                        "match the argument. The string crashes rather than rendering."
                    ),
                    impact=1,
                ))

            # Mixing %s and %1$s in one string is also a runtime failure.
            positional = {i for i, _ in got if i}
            bare = sum(1 for i, _ in got if not i)
            if positional and bare:
                out.append(_mk(
                    locale, msg, "A", "placeholders",
                    f"{label} mixes numbered and unnumbered placeholders",
                    current=msg.props.get(prop, ""), suggest=src.props.get(prop, ""),
                    rationale=(
                        "String.format rejects a format string that mixes `%s` with "
                        "`%1$s`. Number every placeholder or none of them."
                    ),
                    impact=1,
                ))

            if sorted(want) != sorted(got) and not retyped:
                out.append(_mk(
                    locale, msg, "A", "placeholders",
                    f"{label} has placeholders {_describe(sorted(got))} where the "
                    f"source has {_describe(sorted(want))}",
                    current=msg.props.get(prop, ""), suggest=src.props.get(prop, ""),
                    rationale=(
                        "The set of placeholders must match the source: a missing one "
                        "drops a value the user should see, an extra one throws."
                    ),
                    impact=1,
                ))
    return out


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
    "placeholders": lambda c: check_placeholders(c.locale, c.l10n, c.source),
    "escaping": lambda c: check_escaping(c.project, c.locale, c.l10n, c.trees),
}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
