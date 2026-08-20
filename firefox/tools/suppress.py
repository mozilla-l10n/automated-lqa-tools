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

MATCH_FIELDS = ("check", "category", "file", "string_id", "text")


class Rule:
    """One suppression rule.

    All conditions present must match (AND). ``string_id`` and ``file``
    accept a trailing ``*`` glob or a ``re:`` prefix for a full regex;
    ``text`` is a case-insensitive substring test against the finding's
    summary, rationale and current value.
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
        text = self.match.get("text")
        if text is not None:
            haystack = " ".join(
                (finding.summary, finding.rationale, finding.current)
            ).lower()
            if text.lower() not in haystack:
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

    The second half matters: deleting a rule must bring its findings back,
    otherwise the file stops being the single source of truth.
    """
    by_id = {r.id: r for r in rules}
    counts: dict[str, int] = {}
    for finding in findings:
        if finding.status in ("fixed", "obsolete"):
            continue
        hit = next((r for r in rules if r.applies(finding)), None)
        if hit is not None:
            if finding.status != "suppressed":
                finding.status = "suppressed"
            finding.suppressed_by = hit.id
            hit.hits += 1
            counts[hit.id] = counts.get(hit.id, 0) + 1
        elif finding.status == "suppressed" and finding.suppressed_by not in by_id:
            # The rule that retired this was removed: put it back in view.
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
