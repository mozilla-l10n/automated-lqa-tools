"""Plural-category facts, kept in one place.

Two independent sources of truth, and the plural check needs both:

``moz.l10n`` tells us whether a select is a *plural* at all. It annotates
the selector it parsed -- ``function="number"`` for ``{ $count -> [one] … }``
and ``function="string"`` for a custom select like Slovenian's grammatical
case parameter. Guessing from the variant keys instead would misread
``[one]`` used as an ordinary string key, and would miss a plural whose
categories are all unfamiliar.

``babel`` supplies the CLDR categories a language actually has, which is
what makes "this variant can never match" a fact rather than an opinion.

CLDR is deliberately **not** used to decide that a variant is *missing*.
The categories a language possesses and the categories a UI string needs
are different questions: CLDR gives Mexican Spanish a ``many`` category for
compact notation, yet no Firefox Spanish string uses it, so requiring the
full CLDR set would flag every plural in the locale. Completeness is
measured from the locale's own tree instead; see ``check_plurals``.
"""

from __future__ import annotations

import re

from moz.l10n.model import CatchallKey, Expression, SelectMessage, VariableRef

try:
    from babel import Locale
    from babel.core import UnknownLocaleError
except ImportError:  # pragma: no cover - babel is a hard requirement
    Locale = None
    UnknownLocaleError = Exception

# CLDR always allows `other`; babel's `tags` omits it when the rule set is
# trivial, so it is added back explicitly.
_ALWAYS = {"other"}

_NUMERIC = re.compile(r"^-?\d+(\.\d+)?$")

_cache: dict[str, frozenset[str] | None] = {}


def categories_for(locale: str) -> frozenset[str] | None:
    """CLDR plural categories for a locale, or None if it cannot be resolved.

    Returning None rather than guessing matters: an unrecognized locale code
    must disable the check, not produce findings against the wrong
    language's rules.
    """
    if locale in _cache:
        return _cache[locale]
    result: frozenset[str] | None = None
    if Locale is not None:
        # Mozilla codes are BCP-47-ish (`es-MX`, `fy-NL`, `ja-JP-mac`);
        # babel wants underscores and knows nothing of the `-mac` variant.
        candidates = [locale.replace("-", "_")]
        if locale.count("-") >= 2:
            candidates.append("_".join(locale.split("-")[:2]))
        candidates.append(locale.split("-")[0])
        for candidate in candidates:
            try:
                parsed = Locale.parse(candidate)
            except (UnknownLocaleError, ValueError, TypeError):
                continue
            result = frozenset(set(parsed.plural_form.tags) | _ALWAYS)
            break
    _cache[locale] = result
    return result


def is_numeric_key(key: str) -> bool:
    """`[0]` and `[1]` are exact-match keys, not plural categories."""
    return bool(_NUMERIC.match(key))


_rule_cache: dict[str, object] = {}


def _rule(locale: str):
    if locale not in _rule_cache:
        rule = None
        if Locale is not None:
            for candidate in (locale.replace("-", "_"), locale.split("-")[0]):
                try:
                    rule = Locale.parse(candidate).plural_form
                    break
                except (UnknownLocaleError, ValueError, TypeError):
                    continue
        _rule_cache[locale] = rule
    return _rule_cache[locale]


def covered_categories(locale: str, keys) -> frozenset[str]:
    """Which plural categories a set of variant keys actually handles.

    Fluent matches an exact number before it matches a category, so
    ``[1]`` already covers whatever category the number 1 falls into --
    ``one`` in Spanish, ``one`` in Polish, ``other`` in Japanese. Treating
    a numeric key as "not a category" makes ``[1] … *[other]`` look like it
    is missing the singular, which is how en-US writes many of these and
    how locales correctly mirror them.
    """
    rule = _rule(locale)
    out: set[str] = set()
    for key in keys:
        if is_numeric_key(key):
            if rule is not None:
                try:
                    out.add(rule(float(key) if "." in key else int(key)))
                except Exception:  # noqa: BLE001 - a weird key is just not a category
                    continue
        else:
            out.add(key)
    return frozenset(out)


def variant_categories(msg) -> list[frozenset[str]]:
    """The variant keys of a SelectMessage, one set per selector position."""
    if not isinstance(msg, SelectMessage) or not msg.variants:
        return []
    width = max(len(k) for k in msg.variants)
    columns: list[set[str]] = [set() for _ in range(width)]
    for key in msg.variants:
        for index, part in enumerate(key):
            columns[index].add(part.value if isinstance(part, CatchallKey) else str(part))
    return [frozenset(c) for c in columns]


def plural_selectors(msg) -> list[frozenset[str]]:
    """Variant keys for each selector that moz.l10n parsed as a *number*.

    A message can select on several things at once, only some of which are
    plurals, so this returns one set of categories per numeric selector and
    skips the rest.
    """
    if not isinstance(msg, SelectMessage):
        return []
    columns = variant_categories(msg)
    if not columns:
        return []
    out: list[frozenset[str]] = []
    for index, selector in enumerate(msg.selectors):
        if index >= len(columns):
            break
        name = selector.name if isinstance(selector, VariableRef) else None
        declaration = msg.declarations.get(name) if name else None
        function = (
            declaration.function
            if isinstance(declaration, Expression)
            else None
        )
        if function == "number":
            out.append(columns[index])
    return out
