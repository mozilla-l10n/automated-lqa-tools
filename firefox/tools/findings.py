"""The finding record, its identity, and its lifecycle across runs.

A finding is raised once and then tracked. The hard part is recognising the
*same* finding on a later run so the backlog does not reset every time, and
deciding honestly whether it was fixed.

Identity is a hash of (locale, file, string id, category, normalized
summary). That is stable across runs for a deterministic check, and stable
enough for an LLM finding as long as it describes the same defect in
roughly the same words -- and when it does not, the fallback in
:func:`merge` matches on (string id, category) so the model rephrasing
itself does not create a duplicate.

Whether something is *fixed* is deliberately stricter than the ad-hoc
tooling that preceded this system, which counted any change to the string
as a fix. A Pontoon sync routinely rewrites a string for unrelated reasons.
Here a finding closes only when the string changed **and** the text the
finding complained about is no longer present. If the string changed but
the defective text survives, the finding stays open; if the finding never
quoted anything checkable, it goes to ``needs-recheck`` and is put back in
front of the reviewer rather than being silently closed.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass, field

# Report categories, shared with the legacy reports so imported findings
# land in the same buckets.
CATEGORIES = {
    "A": "Functional, markup, variables & plurals",
    "B": "Mistranslation, reversed meaning, wrong names & brand",
    "C": "Grammar, agreement & spelling",
    "D": "Terminology, register & consistency",
    "E": "Typography, punctuation & spacing",
}

# User-visible impact, the axis that should drive fixing order.
IMPACT = {
    1: "Broken output (blank value, broken markup, wrong variable)",
    2: "Wrong content (says something other than the English)",
    3: "Degraded language (grammar, spelling, terminology)",
    4: "Cosmetic (typography, spacing)",
}

DEFAULT_IMPACT = {"A": 1, "B": 2, "C": 3, "D": 3, "E": 4}

OPEN_STATUSES = {"open", "needs-recheck"}


@dataclass
class Finding:
    locale: str
    file: str
    string_id: str
    category: str
    summary: str
    check: str = "llm"  # which check raised it, or "llm" / "legacy"
    impact: int = 0
    current: str = ""
    suggest: str = ""
    rationale: str = ""
    status: str = "open"
    fid: str = ""
    first_seen: str = ""
    last_seen: str = ""
    resolved_on: str = ""
    suppressed_by: str = ""
    # Hash of the message when the finding was raised; drives fix detection.
    string_hash: str = ""
    # Free-form provenance, e.g. the legacy report and section it came from.
    origin: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.impact:
            self.impact = DEFAULT_IMPACT.get(self.category, 3)
        if not self.fid:
            self.fid = self.identity()

    def identity(self) -> str:
        h = hashlib.sha1()
        for part in (
            self.locale,
            self.file,
            self.string_id,
            self.category,
            normalize(self.summary),
        ):
            h.update(part.encode())
            h.update(b"\x00")
        return h.hexdigest()[:12]

    @property
    def key(self) -> tuple[str, str]:
        return (self.file, self.string_id)

    @property
    def is_open(self) -> bool:
        return self.status in OPEN_STATUSES


_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)


def normalize(text: str) -> str:
    """Lowercase, strip punctuation and collapse whitespace.

    Used for identity and for checking whether quoted defective text is
    still present, so that a difference in quoting style or trailing
    punctuation does not read as a different finding.
    """
    return _WS.sub(" ", _PUNCT.sub(" ", (text or "").lower())).strip()


def still_present(fragment: str, text: str) -> bool:
    """Is the defective fragment still in the string?"""
    frag = normalize(fragment)
    if not frag or len(frag) < 3:
        return False
    return frag in normalize(text)


def merge(existing: list[Finding], fresh: list[Finding], today: str) -> tuple[list[Finding], list[Finding]]:
    """Fold this run's findings into the stored backlog.

    Returns ``(all_findings, newly_raised)``. A fresh finding that matches a
    stored one -- by identity, or failing that by (string id, category) --
    refreshes it instead of duplicating it. Re-raising something that had
    been marked fixed reopens it.
    """
    by_fid = {f.fid: f for f in existing}
    by_loose: dict[tuple[str, str, str], Finding] = {}
    for f in existing:
        by_loose.setdefault((f.file, f.string_id, f.category), f)

    raised: list[Finding] = []
    for f in fresh:
        match = by_fid.get(f.fid) or by_loose.get((f.file, f.string_id, f.category))
        if match is None:
            f.first_seen = f.first_seen or today
            f.last_seen = today
            existing.append(f)
            by_fid[f.fid] = f
            by_loose.setdefault((f.file, f.string_id, f.category), f)
            raised.append(f)
            continue
        match.last_seen = today
        # Refresh the mutable description; keep identity and history.
        match.summary = f.summary or match.summary
        match.current = f.current or match.current
        match.suggest = f.suggest or match.suggest
        match.rationale = f.rationale or match.rationale
        match.string_hash = f.string_hash or match.string_hash
        if match.status in ("fixed", "obsolete", "needs-recheck"):
            match.status = "open"
            match.resolved_on = ""
            raised.append(match)
    return existing, raised


def resolve(findings: list[Finding], messages: dict, delta_keys: set, today: str) -> dict[str, list[Finding]]:
    """Update the status of stored findings against the current tree.

    ``delta_keys`` is the set of ``(file, id)`` whose content changed this
    run; only those can possibly have been fixed, which keeps this cheap and
    stops an unchanged string from flapping.
    """
    buckets: dict[str, list[Finding]] = {"fixed": [], "obsolete": [], "recheck": []}
    for f in findings:
        if not f.is_open:
            continue
        msg = messages.get(f.key)
        if msg is None:
            f.status = "obsolete"
            f.resolved_on = today
            buckets["obsolete"].append(f)
            continue
        if f.key not in delta_keys:
            continue  # string untouched: nothing can have changed
        if f.current and still_present(f.current, msg.text()):
            # Text moved but the exact defect survives: keep it open and say so.
            f.status = "open"
            f.string_hash = msg.hash()
            continue
        if f.current:
            f.status = "fixed"
            f.resolved_on = today
            buckets["fixed"].append(f)
        else:
            # Nothing quotable to verify against -- do not guess.
            f.status = "needs-recheck"
            f.string_hash = msg.hash()
            buckets["recheck"].append(f)
    return buckets


# --- persistence ---------------------------------------------------------

def path(project, locale: str) -> str:
    return os.path.join(project.state_dir(locale), "findings.json")


def load(project, locale: str) -> list[Finding]:
    p = path(project, locale)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        return [Finding(**row) for row in json.load(fh)]


def save(project, locale: str, findings: list[Finding]) -> None:
    p = path(project, locale)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    rows = sorted(
        (asdict(f) for f in findings),
        key=lambda r: (r["file"], r["string_id"], r["category"], r["fid"]),
    )
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
