"""Declarative false-positive suppression.

Two layers, because there are two moments at which a false positive can be
stopped:

1. ``locales/<code>/conventions.md`` is prose, injected verbatim into every
   review prompt. It stops the model raising the finding in the first place
   -- the cleanest outcome, and where locale knowledge like "access keys
   are deliberately English" belongs.
2. ``locales/<code>/suppressions.yaml`` is structured and applied *after*
   the fact, to deterministic checks (which have no prompt) and to anything
   the model raises anyway.

Layer 2 is re-applied to the **entire** backlog on every run, not just to
this run's new findings. That is what makes the mechanism usable: write a
rule today and every matching finding ever raised is retired, without
re-reviewing anything or calling the model.

Suppressed findings are never deleted. They keep their rule id in
``findings.json`` and are listed in the report appendix, so a wrong rule is
visible and reversible.
"""

from __future__ import annotations

import os
import re

import yaml

MATCH_FIELDS = ("check", "category", "file", "string_id", "text", "suggest")


class Rule:
    """One suppression rule.

    All conditions present must match (AND). ``string_id`` and ``file``
    accept a trailing ``*`` glob or a ``re:`` prefix for a full regex.
    ``text`` tests the finding's summary, rationale and current value;
    ``suggest`` tests the proposed replacement, which is what you want when
    the rule is about a correction that should never be accepted rather than
    about the string being corrected. Both are case-insensitive substrings,
    or a full regex with a ``re:`` prefix -- needed when a substring would
    over-match, as "attivat" does inside "disattivato".
    """

    def __init__(self, raw: dict, index: int):
        self.id = raw.get("id") or f"rule-{index + 1}"
        self.reason = (raw.get("reason") or "").strip()
        self.match = dict(raw.get("match") or {})
        if "one_off" in raw:
            one = dict(raw["one_off"])
            self.reason = self.reason or (one.pop("reason", "") or "").strip()
            self.match.update(one)
        unknown = set(self.match) - set(MATCH_FIELDS)
        if unknown:
            raise ValueError(
                f"suppression rule {self.id!r} has unknown match fields: "
                f"{sorted(unknown)} (allowed: {list(MATCH_FIELDS)})"
            )
        if not self.match:
            raise ValueError(f"suppression rule {self.id!r} matches nothing")
        if not self.reason:
            raise ValueError(f"suppression rule {self.id!r} needs a reason")
        self.hits = 0

    @staticmethod
    def _matches(pattern: str, value: str) -> bool:
        if pattern.startswith("re:"):
            return re.search(pattern[3:], value or "") is not None
        if pattern.endswith("*"):
            return (value or "").startswith(pattern[:-1])
        return (value or "") == pattern

    def applies(self, finding) -> bool:
        for field in ("check", "category"):
            want = self.match.get(field)
            if want is not None and getattr(finding, field) != want:
                return False
        for field in ("file", "string_id"):
            want = self.match.get(field)
            if want is not None and not self._matches(want, getattr(finding, field)):
                return False
        for field, haystack in (
            ("text", " ".join((finding.summary, finding.rationale, finding.current))),
            ("suggest", finding.suggest or ""),
        ):
            want = self.match.get(field)
            if want is None:
                continue
            if want.startswith("re:"):
                if re.search(want[3:], haystack, re.IGNORECASE) is None:
                    return False
            elif want.lower() not in haystack.lower():
                return False
        return True


def path(project, locale: str) -> str:
    return os.path.join(project.locale_dir(locale), "suppressions.yaml")


def load(project, locale: str) -> list[Rule]:
    p = path(project, locale)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return [Rule(raw, i) for i, raw in enumerate(data.get("rules") or [])]


def apply(rules: list[Rule], findings: list) -> dict[str, int]:
    """Suppress matching findings and un-suppress ones no longer covered.

    The second half matters: the file has to be the single source of truth,
    so what brings a finding back is *no rule matching it now* -- not the
    narrower question of whether the rule that retired it still exists.
    Keying on the id meant narrowing a rule's ``match`` while keeping its id
    left every finding it had ever matched suppressed for ever, which is the
    one thing the retroactive-and-reversible promise rules out.

    ``dismissed`` is left alone. A dismissal is a person saying they read
    *this* string and it is fine; a class rule must not overwrite that, or
    the reason they recorded disappears from the report behind a rule id.
    """
    counts: dict[str, int] = {}
    for finding in findings:
        if finding.status in ("fixed", "obsolete", "dismissed"):
            continue
        hit = next((r for r in rules if r.applies(finding)), None)
        if hit is not None:
            finding.status = "suppressed"
            finding.suppressed_by = hit.id
            hit.hits += 1
            counts[hit.id] = counts.get(hit.id, 0) + 1
        elif finding.status == "suppressed":
            # Nothing covers it any more: put it back in view.
            finding.status = "open"
            finding.suppressed_by = ""
    return counts


TEMPLATE = """# Suppressions for {locale}
#
# Every rule needs an `id` and a `reason`. Conditions inside `match` are
# ANDed. `string_id` and `file` accept a trailing `*` or a `re:` prefix;
# `text` is a case-insensitive substring of the finding.
#
# Rules are re-applied to the whole backlog on every run, so adding one here
# retires matching findings that were raised in the past too. Nothing is
# deleted -- suppressed findings move to the report appendix with the rule id
# next to them.
#
# Prefer writing locale knowledge as prose in conventions.md when you can:
# that stops the finding being raised at all, instead of filtering it after.

rules: []
"""
