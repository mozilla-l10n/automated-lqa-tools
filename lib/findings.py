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

A finding can also be closed by a person: ``dismissed`` means a reviewer
read it and judged the string acceptable, recorded one line in the locale's
``dismissed.txt``. That is distinct from ``suppressed``, which is a rule
about a whole class, and from ``fixed``, which is a claim about the string
having changed.

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

# `check` values that name no check of their own. When a deterministic check
# turns out to be re-deriving one of these -- word for word, see
# `unique_by_wording` -- it takes the record over, so the next run can resolve
# it authoritatively instead of guessing from the text.
UNATTRIBUTED_CHECKS = {"legacy"}


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
    dismissed_because: str = ""
    # The translation asserts something the source does not, in a way a
    # reader could take as intentional rather than as a slip. Set by the
    # reviewer, never by a deterministic check, and deliberately outside
    # ``identity`` so flagging an existing finding does not fork it.
    reads_as_deliberate: bool = False
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
    def rekey(self) -> tuple[str, str, str, str]:
        """What the finding is about, with the wording left out.

        ``identity`` folds in the summary, so rephrasing a check's message
        gives the same defect a new ``fid``. That is wanted for dedup -- two
        different complaints about one string are two findings -- but it
        must not let a stored finding look abandoned when the check did
        re-raise it. Same string, same category, same check is the same
        complaint however it is worded this month.
        """
        return (self.file, self.string_id, self.category, self.check)

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
    """Collapse whitespace, and nothing else.

    Fix detection must **not** use :func:`normalize`: that strips
    punctuation, so a repaired ``</a >`` compares equal to ``</a>``. It must
    not fold case either -- "INDIRIZZO" corrected to "Indirizzo" is a real
    fix, and casefolding makes it invisible. Identity hashing keeps the
    aggressive form, where that noise is unwanted; comparison here has to be
    literal.
    """
    return _WS.sub(" ", (text or "")).strip()


def still_present(fragment: str, text: str) -> bool:
    """Is the defective fragment still in the string?"""
    frag = loose(fragment)
    if not frag or len(frag) < 3:
        return False
    return frag in loose(text)


def verdict(fragment: str, text: str) -> str:
    """What the current text says about a finding: gone, unchanged, or unclear.

    Three outcomes, because substring matching alone gives wrong answers in
    both directions.

    ``gone``      the quoted text is no longer there; the defect is fixed.
    ``unchanged`` the string is still exactly what was flagged.
    ``unclear``   the string has changed but the quoted text survives inside
                  it. That is *not* evidence the defect survived: a fragment
                  stays a substring when the fix was to add words around it.
                  "Traduzione", flagged for losing the in-progress sense, is
                  still inside the corrected "Traduzione in corso".
    """
    if not fragment:
        return "unclear"
    if loose(text).strip() == loose(fragment).strip():
        return "unchanged"
    if not still_present(fragment, text):
        return "gone"
    return "unclear"


def merge(existing: list[Finding], fresh: list[Finding], today: str) -> tuple[list[Finding], list[Finding]]:
    """Fold this run's findings into the stored backlog.

    Returns ``(all_findings, newly_raised)``. A fresh finding that matches a
    stored one refreshes it instead of duplicating it; re-raising something
    that had been marked fixed reopens it.

    Matching is by ``fid`` first. The fallback exists for one case only: a
    check or the model rewording the *same* complaint, which changes the
    ``fid`` because the summary is folded into it. So the fallback is
    ``rekey`` -- file, string id, category **and check** -- and it is used
    only when exactly one stored finding and exactly one fresh finding share
    it. Anything else is two complaints, and two complaints are two findings.

    Both halves of that were wrong before. The key left ``check`` out, so a
    model finding could silently overwrite a typography one on the same
    string; and it applied however many findings shared it, so the second of
    two genuine defects on one string simply replaced the first. That is not
    a hypothetical: an es-MX message with two different broken access keys,
    en-GB strings carrying both a straight quote and a straight apostrophe,
    and Czech strings flagged by both `variables` and `selectors` came to
    thirteen real findings that never reached the backlog.
    """
    by_fid = {f.fid: f for f in existing}

    def unique_by_rekey(items):
        """Findings whose rekey belongs to exactly one of them."""
        seen: dict[tuple, list] = {}
        for f in items:
            seen.setdefault(f.rekey, []).append(f)
        return {k: v[0] for k, v in seen.items() if len(v) == 1}

    stored_unique = unique_by_rekey(existing)
    fresh_unique = unique_by_rekey(fresh)

    def unique_by_wording(items):
        """Stored findings indexed by what they actually say.

        ``fid`` is assigned once and kept, but ``merge`` refreshes a
        finding's summary without recomputing it, so a record that has ever
        been reworded no longer hashes to its own text -- and an import
        carries a ``fid`` from a scheme that no longer exists at all. Two
        findings that say the identical thing about the identical string are
        the same complaint whoever raised it, and this is what lets the
        deterministic check that now derives a defect adopt the imported or
        model-raised record instead of forking it.

        Requiring the wording to match exactly is what makes this safe: it
        cannot merge two *different* complaints, which is the whole point of
        keeping them apart.
        """
        seen: dict[tuple, list] = {}
        for f in items:
            seen.setdefault(
                (f.file, f.string_id, f.category, normalize(f.summary)), []
            ).append(f)
        return {k: v[0] for k, v in seen.items() if len(v) == 1}

    by_wording = unique_by_wording(existing)

    claimed = {g.fid for g in fresh}
    raised: list[Finding] = []
    for f in fresh:
        match = by_fid.get(f.fid)
        if match is None and f.rekey in fresh_unique and fresh_unique[f.rekey] is f:
            wording = (f.file, f.string_id, f.category, normalize(f.summary))
            candidate = stored_unique.get(f.rekey) or by_wording.get(wording)
            # Do not let the loose match steal a stored finding that some
            # other fresh finding already claims by fid.
            if candidate is not None and candidate.fid not in claimed:
                match = candidate
                if candidate.check in UNATTRIBUTED_CHECKS and f.check != "llm":
                    # The check that derived it now owns it, so the next run
                    # can resolve it authoritatively instead of guessing from
                    # the text. Only for an import, which names no check: a
                    # model finding keeps `llm`, because the model cannot
                    # re-derive it and text matching must stay in charge.
                    candidate.check = f.check
                by_wording.pop(wording, None)
        if match is None:
            f.first_seen = f.first_seen or today
            f.last_seen = today
            existing.append(f)
            by_fid[f.fid] = f
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


def close_reviewed(
    findings: list[Finding],
    reviewed: set,
    raised: set,
    changed: set,
    today: str,
    rerunnable: set[str] | None = None,
) -> list[Finding]:
    """Close findings the reviewer looked at again and did not repeat.

    A model finding cannot be re-derived the way a check can, so without
    this a `needs-recheck` item would stay open for ever: nothing would ever
    say the defect had gone. If the reviewer read the string this run and
    did not raise it again, it is resolved.

    Limited to strings whose content actually changed. The reviewer is not
    deterministic, and staying quiet about an unchanged string is not
    evidence of anything -- it may simply not have spotted the defect this
    time. No flag may relax this: ``--recheck`` once passed every reviewed
    string as trusted and closed thirteen Italian findings whose text was
    byte-identical to what had been flagged.

    ``rerunnable`` is the set of checks that ran over the whole tree this
    run, and their findings are excluded outright. ``raised`` holds what the
    *model* raised, so a check finding is never in it -- which meant a
    typography or ui_references defect the check had just re-raised was
    closed as fixed on the sole evidence that the model had not also
    mentioned it. A check answers for itself, in :func:`resolve`; silence
    from the reviewer says nothing about it either way.
    """
    rerunnable = rerunnable or set()
    out = []
    for f in findings:
        if not f.is_open or f.key not in reviewed or f.key not in changed:
            continue
        if f.check in rerunnable or f.fid in raised:
            continue
        f.status = "fixed"
        f.resolved_on = today
        out.append(f)
    return out


def resolve(
    findings: list[Finding],
    messages: dict,
    delta_keys: set,
    today: str,
    rerunnable: set[str] | None = None,
    still_raised: set[str] | None = None,
    recheck: bool = False,
    still_raised_loose: set[tuple] | None = None,
) -> dict[str, list[Finding]]:
    """Update the status of stored findings against the current tree.

    There are two kinds of finding and they are resolved differently.

    A finding from a **deterministic check** is authoritative, because that
    check just ran again over the whole tree: if it did not re-raise the
    finding and the string still exists, the defect is genuinely gone. No
    text matching, no guessing.

    A finding from the **model** or from an **imported report** cannot be
    re-derived, so it is judged on whether the fragment it quoted survives.
    Whether the string moved is judged against the hash stored on the
    finding when it was raised, so it holds however long ago that was and
    whatever the snapshot has done since. A finding that quoted nothing
    checkable is moved to ``needs-recheck`` rather than being silently
    closed -- the honest answer is "somebody has to look again", not
    "fixed".
    """
    rerunnable = rerunnable or set()
    still_raised = still_raised or set()
    # Wording is not identity. A check that renames its own message must not
    # thereby withdraw every finding it has ever raised -- and, because
    # `merge` then matches the re-raised one loosely and refreshes it in
    # place, the defect would leave the backlog without anyone deciding it
    # had. Two Czech placeholder defects went this way in a dry run.
    still_raised_loose = still_raised_loose or set()
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
            if f.fid in still_raised or f.rekey in still_raised_loose:
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

        # Has the string moved since this finding was raised? Answered from
        # the hash recorded on the finding itself, not from this run's
        # delta. The delta only says what changed since the last *snapshot*,
        # and the snapshot advances when the reviewer reads a string --
        # which meant a finding raised before an edit could have its
        # evidence quietly absorbed and never be looked at again.
        moved = bool(f.string_hash) and f.string_hash != msg.hash()
        if recheck:
            # Re-read every open finding against the tree as it stands,
            # whatever the delta says.
            call = verdict(f.current, msg.text())
            if call == "gone":
                f.status = "fixed"
                f.resolved_on = today
                buckets["fixed"].append(f)
            elif call == "unclear" and moved:
                # Only re-queue where the string demonstrably moved. Most
                # findings quote a fragment rather than a whole value, so
                # "unclear" is the common case and re-queueing all of them
                # would have sent 534 of fy-NL's 593 back for a re-read on
                # no evidence at all.
                f.status = "needs-recheck"
                f.string_hash = msg.hash()
                buckets["recheck"].append(f)
            continue
        if not moved and f.key not in delta_keys:
            continue  # string untouched since the finding was raised
        call = verdict(f.current, msg.text())
        if call == "gone":
            f.status = "fixed"
            f.resolved_on = today
            buckets["fixed"].append(f)
            continue
        if call == "unchanged":
            continue  # the string is still exactly what was flagged
        f.status = "needs-recheck"
        f.string_hash = msg.hash()
        buckets["recheck"].append(f)
    return buckets


# --- escalation ----------------------------------------------------------

def deliberate(findings: list[Finding]) -> list[Finding]:
    """Open findings the reviewer marked as reading like a deliberate edit.

    A separate axis from impact. "AI can make mistakes" rendered as "AI can
    tell lies" is impact 2 like any other wrong content, but it puts words
    in the product's mouth, so it needs a person today rather than a place
    in the queue.
    """
    return [f for f in findings if f.is_open and f.reads_as_deliberate]


def broken(findings: list[Finding]) -> list[Finding]:
    """Open impact-1 findings: the string does not render as intended."""
    return [f for f in findings if f.is_open and f.impact == 1]


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
