"""Checks specific to Fluent and the legacy `.properties` files.

Everything that reasons about messages in the abstract is in `lib/checks.py`.
What is left here needs Fluent itself: terms and their parameters, access
keys paired with a label attribute, and HTML markup embedded in values.
"""

from __future__ import annotations

import re

from moz.l10n.model import Expression, PatternMessage, SelectMessage

import common_checks as common
from common_checks import Health, _mk, _message_vars, _selectors, _vars  # noqa: F401
from findings import Finding

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




CHECKS = {
    **common.CHECKS,
    "term_params": lambda c: check_term_params(c.locale, c.l10n, c.source),
    "accesskey": lambda c: check_accesskeys(c.locale, c.l10n, c.source),
    "markup": lambda c: check_markup(c.locale, c.l10n, c.source),
}


def run_all(project, locale, l10n_root, source_root, l10n, source, counts):
    return common.run_all(
        project, locale, l10n_root, source_root, l10n, source, counts, CHECKS
    )
