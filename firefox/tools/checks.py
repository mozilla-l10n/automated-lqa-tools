"""Checks specific to Fluent and the legacy `.properties` files.

Everything that reasons about messages in the abstract is in `lib/checks.py`.
What is left here needs Fluent itself: terms and their parameters, access
keys paired with a label attribute, and HTML markup embedded in values.

Not run, and why -- checked against the repository rather than assumed:

``selectors``
    Subsumed by ``variables`` here. ``_vars()`` folds a message's selectors
    back into the variable set precisely so a plural message compares equal
    to a flattened one, and both checks then measure the same thing against
    the same ``_message_vars(src)``. Across all twenty locales `selectors`
    raised 7 findings and `variables` had already raised every one of them,
    on the same string. Two findings for one defect is a false positive with
    extra steps, and this one was invisible until `merge` stopped letting
    them overwrite each other. Android runs `selectors` and not `variables`,
    which is the same trade made the other way round.
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




CHECKS = {
    **common.CHECKS,
    "term_params": lambda c: check_term_params(c.locale, c.l10n, c.source),
    "accesskey": lambda c: check_accesskeys(c.locale, c.l10n, c.source),
}


def run_all(project, locale, trees, counts):
    return common.run_all(project, locale, trees, counts, CHECKS)
