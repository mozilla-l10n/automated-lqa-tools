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

There is also a difference between a defect being *fixed* and this system
deciding it was never a defect. When a check stops raising a finding but
the string never changed, the check changed its mind -- a false positive
being corrected -- and the finding is ``withdrawn``, not ``fixed``.
Crediting the locale team with work they did not do would make the fixed
count meaningless.

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

# Checks whose finding is about a *relation* between strings rather than one
# string's content. When such a check stops firing it is because the
# relation was repaired -- possibly by editing the other string -- so the
# finding is fixed, not withdrawn, even though its own string never moved.
CROSS_STRING_CHECKS = {"ui_references"}


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


def loose(text: str) -> str:
    """Collapse whitespace and case, but keep punctuation.

    Fix detection must **not** use :func:`normalize`: that strips
    punctuation, so a repaired ``</a >`` compares equal to ``</a>`` and a
    markup or typography fix looks like no change at all. Identity hashing
    still uses the aggressive form, where punctuation noise is unwanted.
    """
    return _WS.sub(" ", (text or "")).strip().casefold()


def still_present(fragment: str, text: str) -> bool:
    """Is the defective fragment still in the string?"""
    frag = loose(fragment)
    if not frag or len(frag) < 3:
        return False
    return frag in loose(text)


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


def drop_noop(findings: list[Finding], today: str) -> list[Finding]:
    """Retire stored findings that propose no change.

    A reviewer whose suggestion equals the current text has concluded there
    is nothing wrong. Such an item should never have been raised; retiring
    it as ``withdrawn`` says that plainly, rather than deleting it and
    leaving no trace of the judgement.
    """
    out = []
    for f in findings:
        if not f.is_open or not f.suggest or not f.current:
            continue
        if f.suggest.strip() != f.current.strip():
            continue
        f.status = "withdrawn"
        f.resolved_on = today
        f.rationale = (
            f.rationale + " " if f.rationale else ""
        ) + "(Retired: the suggested text is identical to the current text.)"
        out.append(f)
    return out


def resolve(
    findings: list[Finding],
    messages: dict,
    delta_keys: set,
    today: str,
    rerunnable: set[str] | None = None,
    still_raised: set[str] | None = None,
) -> dict[str, list[Finding]]:
    """Update the status of stored findings against the current tree.

    There are two kinds of finding and they are resolved differently.

    A finding from a **deterministic check** is authoritative, because that
    check just ran again over the whole tree: if it did not re-raise the
    finding and the string still exists, the defect is genuinely gone. No
    text matching, no guessing.

    A finding from the **model** or from an **imported report** cannot be
    re-derived, so it is judged on whether the fragment it quoted survives.
    ``delta_keys`` limits that to strings whose content actually changed,
    which keeps the work small and stops an untouched string from flapping. A
    finding that quoted nothing checkable is moved to ``needs-recheck``
    rather than being silently closed -- the honest answer is "a human or
    the model has to look again", not "fixed".
    """
    rerunnable = rerunnable or set()
    still_raised = still_raised or set()
    buckets: dict[str, list[Finding]] = {
        "fixed": [], "obsolete": [], "recheck": [], "withdrawn": [],
    }

    for f in findings:
        if not f.is_open:
            continue
        msg = messages.get(f.key)
        if msg is None:
            f.status = "obsolete"
            f.resolved_on = today
            buckets["obsolete"].append(f)
            continue

        if f.check in rerunnable:
            if f.fid in still_raised:
                f.status = "open"
                f.string_hash = msg.hash()
            elif (
                f.string_hash
                and f.string_hash == msg.hash()
                and f.check not in CROSS_STRING_CHECKS
            ):
                # The check stopped raising it while the string never moved,
                # so the check changed its mind -- most likely a false
                # positive that has since been corrected. Reporting that as
                # "fixed" would credit the locale team with work they did
                # not do and quietly inflate the fixed count.
                f.status = "withdrawn"
                f.resolved_on = today
                buckets["withdrawn"].append(f)
            else:
                f.status = "fixed"
                f.resolved_on = today
                buckets["fixed"].append(f)
            continue

        if f.key not in delta_keys:
            continue  # string untouched: nothing can have changed
        if f.current and still_present(f.current, msg.text()):
            f.status = "open"
            f.string_hash = msg.hash()
            continue
        if f.current:
            f.status = "fixed"
            f.resolved_on = today
            buckets["fixed"].append(f)
        else:
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
