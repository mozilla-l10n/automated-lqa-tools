"""Deterministic checks shared by every project, whatever the file format.

`moz.l10n` parses Fluent, `.properties` and Android XML into the same model,
so everything that reasons about *messages* rather than *syntax* lives here:
completeness, variables, plural selectors, plural categories, typography
against the locale's own conventions, and the source-language variant check.

Format-specific checks live with their project -- Fluent terms and access
keys in `firefox/tools/checks.py`, Android escaping and `translatable` in
`android/tools/checks.py`. Each project declares which checks it runs, and
in what order, under `checks:` in its config.

These are ports of phase 1 of the manual runbook, plus the three checks the
per-locale reviews proved were missing:

``selectors``
    ``vars_of()`` subtracts ``msg.declarations``, which hides the case where
    the source selects on ``$linkCount`` and the locale selects on
    ``$tabCount``. That is a blank number on screen, and it is how the
    Slovenian ``tab-group-editor-action-copy-links`` bug was found by hand.

``term_params``
    en-US passes a parameter to a term (``{ -brand-short-name(plural-form:
    "true") }``) that the locale's term does not select on, or vice versa.
    Two Turkish strings and one Slovenian one hit this.

``markup``
    Malformed closing tags (``</a >``), unbalanced tags and dropped
    ``data-l10n-name`` attributes -- all real defects found in Dutch.

Completeness is computed but deliberately never raised as a finding: a
missing string needs translating, not fixing, and the manual reviews always
reported it separately.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

from moz.l10n.model import (
    Expression,
    Markup,
    PatternMessage,
    SelectMessage,
    VariableRef,
)
from moz.l10n.resource import parse_resource

import conventions
import variants
from findings import Finding
from plurals import (
    categories_for,
    covered_categories,
    is_numeric_key,
    plural_selectors,
)
from parse import is_excluded  # noqa: F401


@dataclass
class Health:
    """The numbers that go in the report's health-check table."""

    files: int = 0
    strings: int = 0
    missing: int = 0
    obsolete: int = 0
    missing_files: list[str] = field(default_factory=list)
    locale_only_files: list[str] = field(default_factory=list)
    untranslated_files: list[str] = field(default_factory=list)
    syntax_errors: list[str] = field(default_factory=list)
    missing_by_file: dict[str, int] = field(default_factory=dict)
    counts: dict[str, int] = field(default_factory=dict)
    skipped: list[str] = field(default_factory=list)


# --- helpers -------------------------------------------------------------

# moz.l10n names an anonymous selector -- { PLATFORM() -> } and friends --
# `sel_1`, `sel_2`. Those are not variables the code passes, so comparing
# them locale-to-source is meaningless.
_SYNTHETIC = re.compile(r"^sel_\d+$")


def _vars(msg) -> set[str]:
    """External variables a message consumes, excluding local declarations."""
    found: set[str] = set()

    def walk(pattern):
        for part in pattern:
            if isinstance(part, Expression):
                if isinstance(part.arg, VariableRef):
                    found.add(part.arg.name)
                for opt in part.options.values():
                    if isinstance(opt, VariableRef):
                        found.add(opt.name)
            elif isinstance(part, Markup):
                for opt in list(part.options.values()) + list(part.attributes.values()):
                    if isinstance(opt, VariableRef):
                        found.add(opt.name)

    declared: set[str] = set()
    selectors: set[str] = set()
    if isinstance(msg, PatternMessage):
        declared |= set(msg.declarations)
        walk(msg.pattern)
    elif isinstance(msg, SelectMessage):
        declared |= set(msg.declarations)
        for sel in msg.selectors:
            if isinstance(sel, VariableRef):
                selectors.add(sel.name)
        for variant in msg.variants.values():
            walk(variant)
    # A selector is an *external* variable even though moz.l10n also records
    # it as a declaration ({ $count -> } declares `count` locally). Subtracting
    # declarations first and adding selectors back is what makes a plural
    # message compare equal to a flattened one that interpolates the same
    # variable -- the bug that made the hand-written checks report ~46
    # phantom mismatches in a locale with none.
    return {v for v in (found - declared) | selectors if not _SYNTHETIC.match(v)}


def _interpolated(msg) -> set[str]:
    """Variables actually rendered into the text, ignoring pure selectors.

    en-US often selects on a variable only to pick a word form -- ``{ $count
    -> [one] Comment [other] Comments }`` never prints the number. A language
    without that plural distinction correctly writes one flat string, and
    reporting the variable as "dropped" is noise. Ten such strings appear in
    both Japanese and Chinese.
    """
    return _vars(msg) - set(_selectors(msg))


def _message_vars(msg) -> set[str]:
    """Every variable the message uses, across its value and attributes."""
    out: set[str] = set()
    for raw in msg.raw.values():
        out |= _vars(raw)
    return out


def _selectors(msg) -> tuple[str, ...]:
    """Names the message switches on. Empty for a non-select message."""
    if not isinstance(msg, SelectMessage):
        return ()
    out = []
    for sel in msg.selectors:
        if isinstance(sel, VariableRef):
            name = sel.name
        elif isinstance(sel, Expression) and isinstance(sel.arg, VariableRef):
            name = sel.arg.name
        else:
            name = str(sel)
        if not _SYNTHETIC.match(name):
            out.append(name)
    return tuple(out)


_TAG = re.compile(r"<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)\s*>")
_MALFORMED = re.compile(r"<\s*/\s*([a-zA-Z][a-zA-Z0-9]*)\s+>")
_DLN = re.compile(r"data-l10n-name\s*=\s*[\"']([^\"']+)[\"']")

# Elements that never carry a closing tag.
VOID_TAGS = {"img", "br", "hr", "input", "wbr"}

# Only these are treated as markup. Firefox strings are full of angle-bracket
# *text* that is not markup at all -- `<anonymous>`, `<inline style sheet>`,
# `<unavailable>` in the legacy .properties files, all of which a bare
# ``<\w+>`` regex reads as an unclosed tag. moz.l10n does not help here: it
# parses Fluent HTML as plain text, so there is no node type to key off.
KNOWN_TAGS = {
    "a", "abbr", "b", "br", "button", "code", "div", "em", "h1", "h2", "h3",
    "h4", "h5", "h6", "hr", "i", "img", "input", "label", "li", "ol", "p",
    "small", "span", "strong", "sub", "sup", "u", "ul", "wbr",
}


def _tags(text: str) -> list[tuple[str, str]]:
    """(closing?, name) for every real tag, skipping self-closing and void."""
    out = []
    for m in _TAG.finditer(text):
        closing, name, _attrs, self_closing = m.groups()
        name = name.lower()
        if name not in KNOWN_TAGS:
            continue
        if self_closing or (not closing and name in VOID_TAGS):
            continue
        out.append((closing, name))
    return out


def _has_markup(text: str) -> bool:
    return any(m.group(2).lower() in KNOWN_TAGS for m in _TAG.finditer(text))


def _unbalanced(text: str) -> bool:
    opened: list[str] = []
    for closing, name in _tags(text):
        if closing:
            if not opened or opened.pop() != name:
                return True
        else:
            opened.append(name)
    return bool(opened)


def _mk(locale, msg, category, check, summary, current="", suggest="", rationale="", impact=0):
    return Finding(
        locale=locale,
        file=msg.file,
        string_id=msg.id,
        category=category,
        check=check,
        summary=summary,
        current=current,
        suggest=suggest,
        rationale=rationale,
        impact=impact,
        string_hash=msg.hash(),
    )


# --- individual checks ---------------------------------------------------

def check_completeness(project, locale, trees) -> Health:
    """Missing / obsolete strings and whole files, plus a syntax pass."""
    l10n, source = trees.l10n, trees.source
    h = Health()
    h.strings = len(l10n)

    l_files = trees.l10n_files
    s_files = trees.source_files
    h.files = len(l_files)
    h.missing_files = sorted(s_files - l_files)
    h.locale_only_files = sorted(l_files - s_files)

    for key in source:
        if key not in l10n:
            h.missing += 1
            h.missing_by_file[key[0]] = h.missing_by_file.get(key[0], 0) + 1
    for key in l10n:
        if key not in source and key[0] in s_files:
            h.obsolete += 1

    # A file that exists but whose every string is byte-identical to en-US
    # is untranslated in practice, which the manual reviews reported.
    by_file: dict[str, list[bool]] = {}
    for key, msg in l10n.items():
        src = source.get(key)
        if src is None:
            continue
        by_file.setdefault(key[0], []).append(msg.text().strip() == src.text().strip())
    # For a variant of the source language a file identical to en-US is the
    # normal case, not a signal, so the whole notion is skipped.
    if not project.is_variant(locale):
        for file, flags in by_file.items():
            if len(flags) >= 3 and all(flags):
                if project.check_skips_path("untranslated", file):
                    continue
                h.untranslated_files.append(file)
    h.untranslated_files.sort()

    for rel in sorted(l_files):
        path = os.path.join(trees.root, trees.locale_paths.get(rel, rel))
        try:
            parse_resource(path)
        except Exception as exc:  # noqa: BLE001 - we want the message verbatim
            h.syntax_errors.append(f"{rel}: {exc}")
    return h


def check_variables(locale, l10n, source) -> list[Finding]:
    out = []
    for key, msg in l10n.items():
        if key[1].startswith("-"):
            # A term *definition* is the locale's own business: Slovenian and
            # Polish legitimately add case parameters ({ -brand-short-name ->
            # [sklon] ... }) that en-US has no notion of. What matters is
            # whether call sites agree with the definition, which is
            # check_term_params' job.
            continue
        src = source.get(key)
        if src is None:
            continue
        for prop, raw in msg.raw.items():
            if prop not in src.raw:
                continue
            want = _vars(src.raw[prop])
            got = _vars(raw)
            if want == got:
                continue
            label = f"`{msg.id}`" + (f" (`.{prop}`)" if prop else "")
            # Fluent arguments are passed per *message*, not per attribute:
            # `l10n.setAttributes(el, id, {extensionsCount})` makes the
            # variable available to every attribute of that id. So a
            # variable is only undefined if the source message does not use
            # it *anywhere*. Comparing attribute-to-attribute reported
            # es-MX's `.message` as broken merely because en-US happened to
            # use the count in `.heading` instead.
            undefined = sorted(got - _message_vars(src))
            # Only a variable the source actually renders can be "dropped".
            dropped = sorted((want - got) & _interpolated(src.raw[prop]))
            if undefined:
                out.append(_mk(
                    locale, msg, "A", "variables",
                    f"{label} references {undefined}, which en-US does not pass",
                    current=msg.props.get(prop, ""),

                    rationale=(
                        "A variable the code does not pass renders as an empty string, "
                        "so the sentence loses the value it was built around."
                    ),
                    impact=1,
                ))
            if dropped:
                out.append(_mk(
                    locale, msg, "A", "variables",
                    f"{label} drops {dropped}, which en-US passes",
                    current=msg.props.get(prop, ""),

                    rationale=(
                        "The string renders, but the value en-US shows the user -- a "
                        "count, a name, a size -- never appears."
                    ),
                    impact=2,
                ))
    return out


def check_selectors(locale, l10n, source) -> list[Finding]:
    """Plural/select selector mismatches -- invisible to the variable check.

    Only two things are functional defects, and neither is "the locale did
    not pluralize":

    * both sides select, on *different* variables -- the locale switches on
      something the code never passes, so every variant is unreachable and
      the number renders blank (Slovenian
      ``tab-group-editor-action-copy-links`` selects ``$tabCount`` while the
      source passes ``$linkCount``);
    * the locale selects on a variable the source does not pass at all.

    Collapsing a source select into one flat variant, or splitting a flat
    source into variants, is a legitimate language decision. The Dutch
    review confirmed the first explicitly, and flagging it produced dozens
    of false positives.
    """
    out = []
    for key, msg in l10n.items():
        if key[1].startswith("-"):
            # A term *definition* is the locale's own business: Slovenian and
            # Polish legitimately add case parameters ({ -brand-short-name ->
            # [sklon] ... }) that en-US has no notion of. What matters is
            # whether call sites agree with the definition, which is
            # check_term_params' job.
            continue
        src = source.get(key)
        if src is None:
            continue
        for prop, raw in msg.raw.items():
            if prop not in src.raw:
                continue
            want = _selectors(src.raw[prop])
            got = _selectors(raw)
            if not got or set(want) == set(got):
                continue
            available = _message_vars(src)
            undefined = set(got) - available
            if want and not undefined:
                continue  # both select, and the locale's selector is passed
            if not undefined:
                continue
            label = f"`{msg.id}`" + (f" (`.{prop}`)" if prop else "")
            out.append(
                _mk(
                    locale,
                    msg,
                    "A",
                    "selectors",
                    f"{label} switches on {sorted(undefined)}, which en-US does not "
                    f"pass (it provides {sorted(available) or 'nothing'})",
                    current=msg.props.get(prop, ""),

                    rationale=(
                        "Selecting on a variable the code does not pass makes every "
                        "variant unreachable and the number render blank."
                    ),
                    impact=1,
                )
            )
    return out


# Quote characters a locale might use to set off a UI label. Single curly
# quotes are deliberately excluded: U+2019 is also the apostrophe in French,
# Italian and English, so treating it as a delimiter cuts "Ajouter à
# l\u2019écran d\u2019accueil" down to "Ajouter à l".
_OPEN = "\u201c\u201e\u00ab\u300c\""
_CLOSE = "\u201d\u201c\u00bb\u300d\""
_QUOTED = re.compile(f"[{_OPEN}]([^{_OPEN}{_CLOSE}]{{2,40}})[{_CLOSE}]")


def _is_label(value: str) -> bool:
    """Could this plausibly be a piece of UI being named?

    A multi-word run of letters. The space matters: without it the check
    matches technical tokens that merely coincide with some other string --
    `SameSite`, `secure`, `count` -- and produced over a hundred false
    positives per Firefox locale.
    """
    if not value or "%" in value or "{" in value or "<" in value:
        return False
    return " " in value.strip() and any(c.isalpha() for c in value)


def _nearest(key, candidates):
    """Which of several identically-worded strings this one is naming.

    A label is often reused: five Android strings read "Try Again". Text
    quoting one of them almost always means the control defined beside it,
    so candidates in the same file win, and among those the one sharing the
    longest id prefix. Returning None when that still does not single one
    out is deliberate -- an ambiguous reference supports no conclusion.
    """
    file, ident = key
    same_file = [k for k in candidates if k[0] == file]
    pool = same_file or candidates
    if len(pool) == 1:
        return pool[0]

    def shared(other: str) -> int:
        n = 0
        for a, b in zip(ident, other):
            if a != b:
                break
            n += 1
        return n

    ranked = sorted(pool, key=lambda k: -shared(k[1]))
    if len(ranked) > 1 and shared(ranked[0][1]) == shared(ranked[1][1]):
        return None
    if not same_file and shared(ranked[0][1]) < 6:
        # A different file and no meaningful shared prefix is a guess, not a
        # reference: "Web browser" happens to be some desktop entry's
        # generic name, which says nothing about the notification quoting it.
        return None
    return ranked[0]


# %[argument_index$][flags][width][.precision]conversion
#
# `@` is in the conversion set for iOS, where every placeholder that matters
# is `%@` or `%1$@`; Android never writes one, so including it costs nothing
# there.
PRINTF = re.compile(
    r"%(?:(\d+)\$)?([-#+ 0,(]*)(\d+)?(?:\.(\d+))?([a-zA-Z@%])"
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
    """Placeholder parity between a string and its source.

    Both Android and iOS format through printf-style substitution, so a
    placeholder carries a *type* and often a position as well. Getting
    either wrong is a runtime failure rather than a rendering one: Android
    throws `IllegalFormatConversionException` when `%1$s` meets an integer,
    and both platforms reject a format string that mixes `%s` with `%1$s`.

    The shared variable check compares the argument *names* moz.l10n derives
    from position, so it sees a dropped or invented argument but not a
    retyped one. This closes that gap, and reads the literal spec from the
    `source` attribute moz.l10n keeps on each expression rather than
    reconstructing it.
    """
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
                    current=msg.props.get(prop, ""),
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
                    current=msg.props.get(prop, ""),
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
                    current=msg.props.get(prop, ""),
                    rationale=(
                        "The set of placeholders must match the source: a missing one "
                        "drops a value the user should see, an extra one throws."
                    ),
                    impact=1,
                ))
    return out


def check_ui_references(locale, l10n, source) -> list[Finding]:
    """A string that quotes another string's text, where the two disagree.

    "Select \u201cTry Again\u201d to go back online" only works while the button
    really says "Try Again". Translate the two independently and they drift,
    and the message then tells the user to press something that is not on
    screen.

    The relation is discovered rather than declared: a source string that
    quotes the exact value of another source string is taken to be naming
    that piece of UI, and the same must then hold in the locale. Nothing is
    hardcoded, and the pairing is re-derived from the source every run --
    which is the point, because it means fixing *either* string closes the
    finding. A finding that named only one of them could never notice the
    other being fixed.

    Deliberately conservative: the quoted text must look like a label rather
    than a technical token, and must match exactly one other string, because
    an ambiguous match says nothing.
    """
    by_value: dict[str, list] = {}
    for key, msg in source.items():
        value = msg.text().strip()
        if _is_label(value) and len(value) <= 40:
            by_value.setdefault(value.casefold(), []).append(key)

    out = []
    seen: set = set()
    for key, src in source.items():
        msg = l10n.get(key)
        if msg is None:
            continue
        for fragment in _QUOTED.findall(conventions.clean(src.text())):
            if not _is_label(fragment):
                continue
            candidates = [k for k in by_value.get(fragment.strip().casefold(), []) if k != key]
            target = _nearest(key, candidates) if candidates else None
            if target is None:
                continue  # nothing to point at, or too ambiguous to judge
            targets = [target]
            referenced = l10n.get(target)
            if referenced is None:
                continue
            label = referenced.text().strip()
            if not label or label.casefold() == fragment.strip().casefold():
                continue  # untranslated on both sides; nothing to compare
            # Not filtered by _is_label: the whole point is that the locale
            # may have quoted a single word ("Riprova") where the source
            # quoted two ("Try Again"). Only placeholders are dropped.
            here = [
                q.strip() for q in _QUOTED.findall(conventions.clean(msg.text()))
                if "%" not in q and "{" not in q
            ]
            if not here or label in here:
                continue
            if (key, target) in seen:
                continue  # the same label quoted twice is one defect
            seen.add((key, target))
            out.append(_mk(
                locale, msg, "D", "ui_references",
                f"`{msg.id}` quotes \u201c{here[0]}\u201d but the string it names, "
                f"`{targets[0][1]}`, reads \u201c{label}\u201d",
                current=msg.text(),
                suggest=label,
                rationale=(
                    f"In the source this string quotes \u201c{fragment.strip()}\u201d, which is "
                    f"exactly the value of `{targets[0][1]}` -- it is naming a piece of "
                    "UI. The two have been translated differently, so the message "
                    "points at a label the user cannot see. Fixing either string "
                    "resolves this, and the check is re-derived every run."
                ),
                impact=2,
            ))
    return out


def check_typography(project, locale, l10n, counts, source=None) -> list[Finding]:
    """Deviations from the locale's *own* majority convention.

    Nothing here is language knowledge -- every rule is "the locale does X
    almost everywhere, and these strings do Y instead". Groups that came out
    mixed produce no findings at all.

    A deviation the en-US string shares is never reported. Developer console
    messages in `dom/chrome/*.properties` are full of straight quotes and
    apostrophes that the locale inherited verbatim, and blaming the locale
    for its source's typography is exactly the mistake the manual runbook
    warns about. It matters most for a variant of the source language, where
    almost every string is inherited.
    """
    out = []
    ellipsis = conventions.preferred(counts, "ellipsis")
    quotes = conventions.preferred(counts, "quotes")
    apostrophe = conventions.preferred(counts, "apostrophe")

    ascii_ellipsis = re.compile(r"(?<!\.)\.\.\.(?!\.)")
    straight_apostrophe = re.compile(r"(?<=\w)'(?=\w)")
    straight_pair = re.compile(r'"[^"]{1,200}?"')

    source = source or {}
    for key, msg in l10n.items():
        if project.check_skips_path("typography", msg.file):
            continue
        src = source.get(key)
        for prop, value in msg.props.items():
            if prop in ("style", "accesskey") or not value:
                continue
            text = conventions.clean(value)
            src_text = conventions.clean((src.props.get(prop, "") if src else ""))
            if ellipsis == "char" and ascii_ellipsis.search(text) and not ascii_ellipsis.search(src_text):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses three dots where this locale uses …",
                    current=value,
                    rationale=f"The tree uses … {counts['ellipsis']['char']} times "
                              f"against {counts['ellipsis']['ascii']} ASCII runs.",
                    impact=4,
                ))
            elif ellipsis == "ascii" and "…" in text and "…" not in src_text:
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses … where this locale uses three dots",
                    current=value,
                    rationale=f"The tree uses ASCII dots {counts['ellipsis']['ascii']} times "
                              f"against {counts['ellipsis']['char']} ….",
                    impact=4,
                ))
            if (quotes and quotes != "straight-double" and straight_pair.search(text)
                    and not straight_pair.search(src_text)):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses straight double quotes",
                    current=value,
                    rationale=f"The locale's quote convention is `{quotes}` "
                              f"({counts['quotes'].get(quotes)} occurrences).",
                    impact=4,
                ))
            if (apostrophe == "typographic" and straight_apostrophe.search(text)
                    and not straight_apostrophe.search(src_text)):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses a straight apostrophe",
                    current=value,
                    rationale=f"The tree uses ’ {counts['apostrophe']['typographic']} times "
                              f"against {counts['apostrophe']['straight']} straight.",
                    impact=4,
                ))
    return out


def check_plurals(locale, l10n, source) -> list[Finding]:
    """Plural variants, judged against CLDR and the locale's own habits.

    Two different questions, and conflating them is what makes naive plural
    checks useless:

    *Is a variant reachable?* Answered by CLDR. A category that does not
    exist in the language can never match, so the variant is dead text --
    `[two]` in Spanish, or a typo like `[ony]`.

    *Is a variant missing?* **Not** answered by CLDR, which is why this is
    measured instead. CLDR says Mexican Spanish has a `many` category, but
    no Firefox Spanish string uses it, so requiring the CLDR set would flag
    every plural in the locale. The expectation comes from what this locale
    actually does across its own tree, and only applies where en-US treats
    the string as a real plural in the first place -- en-US often writes a
    single `*[other]` for a count that is always greater than one, and a
    locale is free to follow suit or to add forms.

    Adding categories en-US does not have is never a defect: that is
    precisely what localizing a plural means.
    """
    valid = categories_for(locale)
    if valid is None:
        return []

    # What this locale habitually does: categories present in most of its
    # own number-selects.
    seen: dict[str, int] = {}
    total = 0
    for msg in l10n.values():
        for raw in msg.raw.values():
            for cats in plural_selectors(raw):
                total += 1
                for cat in covered_categories(locale, cats):
                    seen[cat] = seen.get(cat, 0) + 1
    norm = {c for c, n in seen.items() if total >= 5 and n >= total * 0.5}

    out = []
    for key, msg in l10n.items():
        src = source.get(key)
        for prop, raw in msg.raw.items():
            for cats in plural_selectors(raw):
                label = f"`{msg.id}`" + (f" (`.{prop}`)" if prop else "")

                dead = sorted(c for c in cats if c not in valid and not is_numeric_key(c))
                if dead:
                    out.append(_mk(
                        locale, msg, "A", "plurals",
                        f"{label} has plural {'variants' if len(dead) > 1 else 'variant'} "
                        f"{dead}, which {locale} does not have",
                        current=msg.props.get(prop, ""),
                        rationale=(
                            f"{locale} has the categories {sorted(valid)}. A variant whose "
                            "category the language never produces is never selected, so "
                            "the text written there never appears. Nothing is broken -- "
                            "the catch-all is shown -- but the variant is dead."
                        ),
                        impact=4,
                    ))

                if src is None or not norm:
                    continue
                src_raw = src.raw.get(prop)
                if src_raw is None:
                    continue
                src_columns = plural_selectors(src_raw)
                src_keys = set().union(*src_columns) if src_columns else set()
                if not src_keys:
                    continue
                # en-US keying on an exact number (`[1] Remove [other] Remove
                # All`) is a one-versus-many *choice*, not grammatical
                # agreement, and a locale that mirrors it is right to. Only a
                # source that selects on a category (`[one]`) is really
                # pluralizing, and only then should the locale supply its own
                # full set of forms.
                if not any(
                    not is_numeric_key(k) and k != "other" for k in src_keys
                ):
                    continue
                if len(covered_categories(locale, src_keys)) < 2:
                    continue
                missing = sorted(norm - covered_categories(locale, cats))
                if missing:
                    out.append(_mk(
                        locale, msg, "A", "plurals",
                        f"{label} is missing the {missing} plural "
                        f"{'forms' if len(missing) > 1 else 'form'}",
                        current=msg.props.get(prop, ""),

                        rationale=(
                            f"This locale uses {sorted(norm)} in most of its plurals, and "
                            "en-US pluralizes this string. The catch-all variant will be "
                            "shown instead, giving the wrong grammatical form."
                        ),
                        impact=3,
                    ))
    return out


def check_variant_spelling(project, locale, l10n, source) -> list[Finding]:
    """Strings a language variant left identical when they should not be.

    Only meaningful for a variant of the source language, and silent for
    every other locale. The substitutions are learned from the locale's own
    divergences rather than from a word list, so nothing here encodes an
    opinion about British versus American English -- it reports only where
    the locale contradicts itself.
    """
    if not project.is_variant(locale):
        return []
    rules = variants.learn(l10n, source)
    if not rules:
        return []
    out = []
    for key, word, replacement in variants.unapplied(l10n, source, rules):
        msg = l10n[key]
        _, applied, retained = rules[word]
        out.append(_mk(
            locale, msg, "C", "variant_spelling",
            f"`{msg.id}` still uses the en-US form \u201c{word}\u201d",
            current=msg.text(),
            suggest=replacement,
            rationale=(
                f"This locale writes \u201c{replacement}\u201d for \u201c{word}\u201d in "
                f"{applied} other strings and keeps \u201c{word}\u201d in {retained}. "
                "This string is byte-identical to en-US, so the substitution looks "
                "simply to have been missed."
            ),
            impact=3,
        ))
    return out


def check_markup(locale, l10n, source) -> list[Finding]:
    """Broken tags, unbalanced tags, and dropped ``data-l10n-name`` hooks.

    Everything is judged against the en-US string: a locale is only expected
    to carry markup where the source has it, and only the same
    ``data-l10n-name`` hooks, because those are what the code matches on.
    """
    out = []
    for key, msg in l10n.items():
        src = source.get(key)
        if src is None:
            continue
        for prop, value in msg.props.items():
            if prop in ("style", "accesskey") or not value:
                continue
            source_text = src.props.get(prop)
            if source_text is None or not _has_markup(source_text):
                continue

            bad = _MALFORMED.search(value)
            if bad and bad.group(1).lower() in KNOWN_TAGS:
                out.append(_mk(
                    locale, msg, "A", "markup",
                    f"Malformed closing tag `{bad.group(0)}` in `{msg.id}`"
                    + (f" (`.{prop}`)" if prop else ""),
                    current=value,
                    rationale="Whitespace inside a closing tag makes it render as literal text.",
                    impact=1,
                ))

            if _unbalanced(value) and not _unbalanced(source_text):
                out.append(_mk(
                    locale, msg, "A", "markup",
                    f"Unbalanced markup in `{msg.id}`" + (f" (`.{prop}`)" if prop else ""),
                    current=value,
                    rationale="Tags must open and close in the same order as en-US.",
                    impact=1,
                ))

            want = set(_DLN.findall(source_text))
            got = set(_DLN.findall(value))
            if want and want != got:
                out.append(_mk(
                    locale, msg, "A", "markup",
                    f"`data-l10n-name` mismatch in `{msg.id}`: en-US has "
                    f"{sorted(want)}, the locale has {sorted(got) or 'none'}",
                    current=value,
                    rationale=(
                        "The element is matched by its data-l10n-name; a missing or "
                        "renamed one drops the link, icon or button entirely."
                    ),
                    impact=1,
                ))
    return out


# --- registry ------------------------------------------------------------

# Every check has the same shape: it takes a Context and returns findings.
# That is what lets a project compose the shared set with its own.

@dataclass
class Context:
    project: object
    locale: str
    l10n: dict
    source: dict
    counts: dict
    health: "Health"
    trees: object = None


CHECKS = {
    "variables": lambda c: check_variables(c.locale, c.l10n, c.source),
    "selectors": lambda c: check_selectors(c.locale, c.l10n, c.source),
    "plurals": lambda c: check_plurals(c.locale, c.l10n, c.source),
    "markup": lambda c: check_markup(c.locale, c.l10n, c.source),
    "placeholders": lambda c: check_placeholders(c.locale, c.l10n, c.source),
    "ui_references": lambda c: check_ui_references(c.locale, c.l10n, c.source),
    "typography": lambda c: check_typography(
        c.project, c.locale, c.l10n, c.counts, c.source
    ),
    "variant_spelling": lambda c: check_variant_spelling(
        c.project, c.locale, c.l10n, c.source
    ),
}


def run_all(project, locale, trees, counts, registry=None):
    """Run the checks this project declares, in the order it declares them."""
    registry = registry or CHECKS
    health = check_completeness(project, locale, trees)
    ctx = Context(project, locale, trees.l10n, trees.source, counts, health, trees)

    names = project.checks or list(registry)
    unknown = [n for n in names if n not in registry]
    if unknown:
        raise RuntimeError(
            f"{project.name}/config.yaml lists unknown checks: {unknown}; "
            f"available: {sorted(registry)}"
        )

    out: list[Finding] = []
    for name in names:
        if project.check_skipped(name, locale):
            health.skipped.append(name)
            health.counts[name] = 0
            continue
        found = registry[name](ctx)
        health.counts[name] = len(found)
        out.extend(found)
    return health, out
