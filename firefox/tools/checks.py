"""Deterministic checks. No model involved, so they run over the whole tree
on every run and cost nothing.

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
from findings import Finding
from parse import is_excluded, list_files


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


def _term_calls(msg) -> dict[str, frozenset]:
    """Term references and the parameter names each is called with."""
    calls: dict[str, frozenset] = {}

    def walk(pattern):
        for part in pattern:
            if isinstance(part, Expression) and isinstance(part.arg, str):
                if part.arg.startswith("-"):
                    calls[part.arg] = frozenset(part.options)

    if isinstance(msg, PatternMessage):
        walk(msg.pattern)
    elif isinstance(msg, SelectMessage):
        for variant in msg.variants.values():
            walk(variant)
    return calls


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

def check_completeness(project, l10n_root, source_root, l10n, source) -> Health:
    """Missing / obsolete strings and whole files, plus a syntax pass."""
    h = Health()
    h.strings = len(l10n)

    l_files = list_files(l10n_root, project.extensions, project.exclude)
    s_files = list_files(source_root, project.extensions, project.exclude)
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
    for file, flags in by_file.items():
        if len(flags) >= 3 and all(flags):
            if project.check_skips_path("untranslated", file):
                continue
            h.untranslated_files.append(file)
    h.untranslated_files.sort()

    for rel in sorted(l_files):
        path = os.path.join(l10n_root, rel)
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
            undefined = sorted(got - want)
            # Only a variable the source actually renders can be "dropped".
            dropped = sorted((want - got) & _interpolated(src.raw[prop]))
            if undefined:
                out.append(_mk(
                    locale, msg, "A", "variables",
                    f"{label} references {undefined}, which en-US does not pass",
                    current=msg.props.get(prop, ""),
                    suggest=src.props.get(prop, ""),
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
                    suggest=src.props.get(prop, ""),
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
            available = _vars(src.raw[prop])
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
                    suggest=src.props.get(prop, ""),
                    rationale=(
                        "Selecting on a variable the code does not pass makes every "
                        "variant unreachable and the number render blank."
                    ),
                    impact=1,
                )
            )
    return out


def check_term_params(locale, l10n, source) -> list[Finding]:
    """A term called with parameters its definition does not select on."""
    out = []
    term_selectors: dict[str, set[str]] = {}
    for (file, mid), msg in l10n.items():
        if not mid.startswith("-"):
            continue
        names: set[str] = set()
        for raw in msg.raw.values():
            names.update(_selectors(raw))
        term_selectors.setdefault(mid, set()).update(names)

    for key, msg in l10n.items():
        for prop, raw in msg.raw.items():
            for term, params in _term_calls(raw).items():
                if not params:
                    continue
                known = term_selectors.get(term)
                if known is None:
                    continue  # term defined elsewhere/not parsed: do not guess
                unused = set(params) - known
                if not unused or not known:
                    # A parameter a flat term ignores is harmless in Fluent
                    # (confirmed in the Dutch review), so only flag it when
                    # the term *does* select, on something else.
                    continue
                label = f"`{msg.id}`" + (f" (`.{prop}`)" if prop else "")
                out.append(
                    _mk(
                        locale,
                        msg,
                        "A",
                        "term_params",
                        f"{label} calls `{term}` with {sorted(unused)}, but that term "
                        f"selects on {sorted(known)}",
                        current=msg.props.get(prop, ""),
                        rationale=(
                            "The term falls back to its catch-all variant, so the "
                            "intended form is never selected."
                        ),
                        impact=1,
                    )
                )
    return out


_ACCESSKEY_PARTNERS = (
    "label", "value", "title", "aria-label", "placeholder", "tooltiptext", "toolbarname",
)


def check_accesskeys(locale, l10n, source) -> list[Finding]:
    """An access key that does not occur in the label it belongs to."""
    out = []
    flat: dict[str, str] = {}
    for (file, mid), msg in l10n.items():
        flat[mid] = msg.value or next(iter(msg.props.values()), "")

    ref = re.compile(r"\{\s*(-[^}\s]+)\s*\}")

    def expand(text: str, depth: int = 0) -> str:
        if depth > 3:
            return text
        return ref.sub(lambda m: expand(flat.get(m.group(1), ""), depth + 1), text)

    for key, msg in l10n.items():
        for prop, value in msg.props.items():
            if not prop.endswith("accesskey"):
                continue
            akey = value.strip()
            if len(akey) != 1:
                continue
            base = prop[: -len("accesskey")]
            label = None
            candidate = None
            for candidate in [base + p for p in _ACCESSKEY_PARTNERS] + ["", *_ACCESSKEY_PARTNERS]:
                if candidate in msg.props and candidate != prop:
                    label = msg.props[candidate]
                    break
            if label is None:
                continue
            if akey.lower() in expand(label).lower():
                continue
            # en-US carries a handful of access keys that are not in their own
            # label (`inspect` -> Q). The locale inherited those; they are not
            # its defect, and the runbook says so explicitly.
            src = source.get(key)
            if src is not None:
                src_key = src.props.get(prop, "").strip()
                src_label = src.props.get(candidate)
                if src_label is not None and len(src_key) == 1:
                    if src_key.lower() not in src_label.lower():
                        continue
            out.append(
                _mk(
                    locale,
                    msg,
                    "A",
                    "accesskey",
                    f"Access key `{akey}` of `{msg.id}` is not present in its label",
                    current=akey,
                    rationale=(
                        f"The label is “{expand(label)}”. An access key not in "
                        "the label cannot be underlined and is unreachable by keyboard."
                    ),
                    impact=2,
                )
            )
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
                    current=value, suggest=source_text,
                    rationale="Whitespace inside a closing tag makes it render as literal text.",
                    impact=1,
                ))

            if _unbalanced(value) and not _unbalanced(source_text):
                out.append(_mk(
                    locale, msg, "A", "markup",
                    f"Unbalanced markup in `{msg.id}`" + (f" (`.{prop}`)" if prop else ""),
                    current=value, suggest=source_text,
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
                    current=value, suggest=source_text,
                    rationale=(
                        "The element is matched by its data-l10n-name; a missing or "
                        "renamed one drops the link, icon or button entirely."
                    ),
                    impact=1,
                ))
    return out


def check_typography(project, locale, l10n, counts) -> list[Finding]:
    """Deviations from the locale's *own* majority convention.

    Nothing here is language knowledge -- every rule is "the locale does X
    almost everywhere, and these strings do Y instead". Groups that came out
    mixed produce no findings at all.
    """
    out = []
    ellipsis = conventions.preferred(counts, "ellipsis")
    quotes = conventions.preferred(counts, "quotes")
    apostrophe = conventions.preferred(counts, "apostrophe")

    ascii_ellipsis = re.compile(r"(?<!\.)\.\.\.(?!\.)")
    straight_apostrophe = re.compile(r"(?<=\w)'(?=\w)")
    straight_pair = re.compile(r'"[^"]{1,200}?"')

    for key, msg in l10n.items():
        if project.check_skips_path("typography", msg.file):
            continue
        for prop, value in msg.props.items():
            if prop in ("style", "accesskey") or not value:
                continue
            text = conventions.clean(value)
            if ellipsis == "char" and ascii_ellipsis.search(text):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses three dots where this locale uses …",
                    current=value,
                    rationale=f"The tree uses … {counts['ellipsis']['char']} times "
                              f"against {counts['ellipsis']['ascii']} ASCII runs.",
                    impact=4,
                ))
            elif ellipsis == "ascii" and "…" in text:
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses … where this locale uses three dots",
                    current=value,
                    rationale=f"The tree uses ASCII dots {counts['ellipsis']['ascii']} times "
                              f"against {counts['ellipsis']['char']} ….",
                    impact=4,
                ))
            if quotes and quotes != "straight-double" and straight_pair.search(text):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses straight double quotes",
                    current=value,
                    rationale=f"The locale's quote convention is `{quotes}` "
                              f"({counts['quotes'].get(quotes)} occurrences).",
                    impact=4,
                ))
            if apostrophe == "typographic" and straight_apostrophe.search(text):
                out.append(_mk(
                    locale, msg, "E", "typography",
                    f"`{msg.id}` uses a straight apostrophe",
                    current=value,
                    rationale=f"The tree uses ’ {counts['apostrophe']['typographic']} times "
                              f"against {counts['apostrophe']['straight']} straight.",
                    impact=4,
                ))
    return out


# --- entry point ---------------------------------------------------------

ALL_CHECKS = ("variables", "selectors", "term_params", "accesskey", "markup", "typography")


def run_all(project, locale, l10n_root, source_root, l10n, source, counts) -> tuple[Health, list[Finding]]:
    health = check_completeness(project, l10n_root, source_root, l10n, source)
    out: list[Finding] = []
    for name in ALL_CHECKS:
        if project.check_skipped(name, locale):
            health.skipped.append(name)
            health.counts[name] = 0
            continue
        if name == "variables":
            found = check_variables(locale, l10n, source)
        elif name == "selectors":
            found = check_selectors(locale, l10n, source)
        elif name == "term_params":
            found = check_term_params(locale, l10n, source)
        elif name == "accesskey":
            found = check_accesskeys(locale, l10n, source)
        elif name == "markup":
            found = check_markup(locale, l10n, source)
        else:
            found = check_typography(project, locale, l10n, counts)
        health.counts[name] = len(found)
        out.extend(found)
    return health, out
