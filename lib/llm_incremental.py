"""The incremental reviewer: an Anthropic SDK batch pass over changed strings.

This is the path that runs on almost every execution. It is deliberately
*not* agentic: the strings to review are already known, so there is nothing
to explore. A plain batched Messages call with a forced tool schema is
leaner, reproducible, and testable with recorded fixtures.

Structured output is enforced by ``tool_choice``, so a malformed response is
a retryable API-level error rather than something to parse out of prose.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field

import anthropic

from findings import CATEGORIES, IMPACT, Finding

LANGUAGE_NAMES = {
    "de": "German", "es-ES": "Spanish (Spain)", "es-MX": "Spanish (Mexico)",
    "fr": "French", "fy-NL": "Frisian", "it": "Italian", "ja": "Japanese",
    "nl": "Dutch", "pl": "Polish", "pt-BR": "Portuguese (Brazil)",
    "pt-PT": "Portuguese (Portugal)", "ru": "Russian", "sl": "Slovenian",
    "tr": "Turkish", "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)", "cs": "Czech", "sv-SE": "Swedish",
    "ko": "Korean", "hu": "Hungarian", "fi": "Finnish", "da": "Danish",
    "el": "Greek", "uk": "Ukrainian", "vi": "Vietnamese", "id": "Indonesian",
}


class Usage:
    def __init__(self) -> None:
        self.input = 0
        self.output = 0
        self.calls = 0

    def add(self, response) -> None:
        self.calls += 1
        self.input += response.usage.input_tokens
        self.output += response.usage.output_tokens

    def __str__(self) -> str:
        return f"{self.calls} calls, {self.input:,} in / {self.output:,} out"


def language_of(locale: str) -> str:
    return LANGUAGE_NAMES.get(locale, locale)


def render_batch(keys, l10n, source, keep_identical: bool = False) -> str:
    """Format one batch of strings for review.

    Strings identical to the source are normally dropped here rather than in
    the prompt: an identical value is a completeness gap, and having the
    model rediscover that on every run is pointless.

    A string with **no** source is dropped too, and unconditionally. There is
    nothing to review it against, and saying so in the block did not stop the
    model reviewing it anyway -- it reconstructed the English from the string
    id and criticised the translation against that. `review` filters these
    out before batching; this is the guard for any other caller.

    For a variant of the source language that rule inverts. Most of en-GB is
    identical to en-US and correct, and the defect worth finding is a string
    that should have diverged and did not -- so ``keep_identical`` keeps
    them in.
    """
    blocks = []
    for key in keys:
        msg = l10n.get(key)
        if msg is None:
            continue
        src = source.get(key)
        if src is None:
            continue
        identical = msg.text().strip() == src.text().strip()
        if identical and not keep_identical:
            continue
        block = [f"### {msg.id}", f"file: {msg.file}"]
        if msg.comment:
            comment = "\n".join(f"  {line}" for line in msg.comment.splitlines())
            block.append(f"developer comment:\n{comment}")
        block.append(f"source: {src.text()}")
        block.append(f"target: {msg.text()}")
        if identical:
            block.append("note: identical to the source string")
        blocks.append("\n".join(block))
    return "\n\n".join(blocks)


def _schema(project) -> dict:
    with open(
        os.path.join(project.root, "prompts", "finding_schema.json"), encoding="utf-8"
    ) as fh:
        return json.load(fh)


def _call(client, model, system, batch, tool, max_tokens, attempts=4):
    last = None
    for attempt in range(attempts):
        try:
            return client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                tools=[tool],
                tool_choice={"type": "tool", "name": tool["name"]},
                messages=[{"role": "user", "content": batch}],
            )
        except (anthropic.RateLimitError, anthropic.APIStatusError, anthropic.APIConnectionError) as exc:
            last = exc
            status = getattr(exc, "status_code", None)
            if status is not None and 400 <= status < 500 and status != 429:
                raise
            if attempt < attempts - 1:
                # No point sleeping after the last one: the loop is over and
                # the only thing the wait delays is the error report.
                time.sleep(min(2 ** attempt * 5, 60))
    raise RuntimeError(f"LLM call failed after {attempts} attempts: {last}")


def system_prompt(project, locale: str, filename: str | None = None) -> str:
    """The review instructions for a locale, variant-aware."""
    source_locale = project.variant_of(locale)
    name = filename or (
        "variant_review.md" if source_locale else "incremental_review.md"
    )
    return project.prompt(name).format(
        language=language_of(locale),
        locale=locale,
        source_locale=source_locale or "en-US",
        conventions=project.conventions(locale).strip()
        or "_No conventions recorded yet for this locale._",
    )


@dataclass
class Progress:
    """What a review actually got through.

    ``reviewed`` is the set of keys a batch returned an answer for, not the
    set it was asked about, and it is what the snapshot is advanced by.

    ``trusted`` is the subset whose answer was *well formed*, and it is what
    may be read as reviewer silence. The two came apart after a malformed
    response -- no tool call, or a findings list with an unparseable item --
    was counted as a clean review, closing an open finding on the strength of
    an answer nobody could read. Discarding a malformed item is right;
    treating the same answer as evidence of absence is not.

    ``stopped`` holds the reason the pass ended early, or "" if it ran to the
    end.
    """

    reviewed: set = field(default_factory=set)
    trusted: set = field(default_factory=set)
    stopped: str = ""


def review(project, locale, keys, l10n, source, log=print) -> tuple[list[Finding], Usage, Progress]:
    """Review the given strings.

    Returns the findings, the usage, and how far it got. A batch that fails
    after its retries ends the pass, but everything already reviewed is
    returned and kept: 2,900 strings is dozens of batches, and throwing away
    an hour of completed review because the last call timed out is both
    wasteful and, since the snapshot only advances for strings actually
    read, unnecessary. The next run resumes at the first unread string.
    """
    usage = Usage()
    progress = Progress()
    if not keys:
        return [], usage, progress

    # Filtered here, not in `render_batch`: a batch that renders empty is
    # counted as reviewed, and that shortcut means "every string in it is
    # identical to its source", which is a reviewed answer. A string with no
    # en-US counterpart has not been reviewed and never can be, so it must
    # not be marked as read -- it is out of scope, not clean. The batched
    # baseline reaches this with `sorted(l10n)`, so the whole locale-only
    # part of a tree arrives here in one go.
    unreviewable = [k for k in keys if k not in source]
    if unreviewable:
        log(f"    skipping {len(unreviewable)} string(s) with no en-US counterpart")
        keys = [k for k in keys if k in source]
        if not keys:
            return [], usage, progress

    cfg = project.llm
    tool = _schema(project)
    system = system_prompt(project, locale)
    keep_identical = project.is_variant(locale)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        ways_out = ["export it", "use --no-llm for the deterministic checks only"]
        if project.supports_agent_baseline:
            ways_out.append(
                "or run a from-scratch review with --baseline-strategy agent, "
                "which drives the `claude` CLI and uses its credentials instead"
            )
        raise RuntimeError(
            "reviewing through the API needs ANTHROPIC_API_KEY: "
            + ", ".join(ways_out)
            + "."
        )
    client = anthropic.Anthropic()
    batch_size = int(cfg.get("batch_size", 40))
    model = cfg["model"]
    max_tokens = int(cfg.get("max_output_tokens", 16000))

    keys = list(keys)
    batches = [keys[i : i + batch_size] for i in range(0, len(keys), batch_size)]
    out: list[Finding] = []
    for index, batch_keys in enumerate(batches, 1):
        body = render_batch(batch_keys, l10n, source, keep_identical)
        if not body.strip():
            # Nothing in the batch needed the model -- every string in it is
            # identical to its source. Seen, as it always was.
            progress.reviewed.update(batch_keys)
            progress.trusted.update(batch_keys)
            continue
        log(f"    batch {index}/{len(batches)} ({len(batch_keys)} strings)")
        try:
            response = _call(client, model, system, body, tool, max_tokens)
        except Exception as exc:  # noqa: BLE001 - keep what has been reviewed
            progress.stopped = f"stopped at batch {index} of {len(batches)}: {exc}"
            log(f"    {progress.stopped}")
            log(f"    keeping {len(progress.reviewed):,} string(s) already reviewed")
            break
        usage.add(response)
        found, malformed, ok = collect(response.content, locale, l10n)
        out.extend(found)
        if ok:
            progress.reviewed.update(batch_keys)
            if not malformed:
                progress.trusted.update(batch_keys)
        if malformed:
            log(f"      discarded {malformed} malformed item(s) in this batch; "
                "these strings are not counted as cleanly reviewed")
        if not ok:
            log("      the reply carried no readable findings list; "
                "this batch is not counted as reviewed and will be retried")
    return out, usage, progress


def collect(content, locale, l10n) -> tuple[list[Finding], int, bool]:
    """Findings from one response, what was not one, and whether it parsed.

    Returns ``(findings, malformed, ok)``. ``ok`` is False when the response
    carried no tool call at all, or a ``findings`` field that is not a list --
    there is no answer there to read, so the caller must not treat the batch
    as reviewed.

    Everything else is per item. The tool schema says each finding is an
    object with an integer impact, and the model mostly obliges, but nothing
    enforces it: a bare string in the list used to raise on ``.get``, and
    ``"impact": "high"`` still raised on ``int()`` -- from outside the batch
    loop, so a single bad item discarded every completed batch for the
    locale. One malformed item is a dropped item, counted and logged.
    """
    out: list[Finding] = []
    malformed = 0
    saw_tool_use = False
    ok = True
    for block in content:
        if getattr(block, "type", "") != "tool_use":
            continue
        saw_tool_use = True
        payload = block.input if isinstance(block.input, dict) else {}
        items = payload.get("findings")
        if not isinstance(items, list):
            malformed += 1
            ok = False
            continue
        for raw in items:
            if not isinstance(raw, dict):
                malformed += 1
                continue
            try:
                finding = _to_finding(locale, raw, l10n)
            except Exception:  # noqa: BLE001 - one bad item, not the batch
                malformed += 1
                continue
            if finding is not None:
                out.append(finding)
    return out, malformed, ok and saw_tool_use


def _deliberate(raw: dict) -> bool:
    """Honour the reviewer's flag, but only where it can mean anything.

    The flag is about the localized text saying something the source does
    not, so it only applies to a finding that is already about content:
    category B at impact 1 or 2. Set anywhere else it is the model reaching
    for an emphasis marker -- a typography finding cannot put words in the
    product's mouth -- and it is dropped rather than escalated.
    """
    if raw.get("reads_as_deliberate") is not True:
        return False
    return (raw.get("category") or "").strip().upper()[:1] == "B" and \
        int(raw.get("impact") or 0) in (1, 2)


def _category(raw: dict) -> str:
    """The finding's category, forced into A-E.

    Anything else is dropped rather than kept: the report groups open
    findings by category, so a `Z` appears in no section at all while still
    counting as open. Falling back to B matches the schema's own default and
    at least puts it in front of somebody.
    """
    got = (raw.get("category") or "").strip().upper()[:1]
    return got if got in CATEGORIES else "B"


def _impact(raw: dict) -> int:
    """The finding's impact, forced into 1-4.

    ``int()`` on whatever arrived used to raise -- ``"impact": "high"`` is a
    plausible thing for a model to say -- and an out-of-range number appeared
    in no row of the impact table. 0 means "unset", which ``Finding`` fills
    in from the category.
    """
    try:
        got = int(raw.get("impact") or 0)
    except (TypeError, ValueError):
        return 0
    return got if got in IMPACT else 0


def _to_finding(locale, raw: dict, l10n) -> Finding | None:
    """Convert one model finding, dropping anything that is not one.

    Two things get discarded here. A hallucinated string id, because the
    backlog must only contain strings that exist. And a finding whose
    suggested text is identical to the current text, because a reviewer who
    proposes no change has concluded there is no defect -- their own
    rationale usually says so outright ("no defect", "this is acceptable")
    while the tool call still reports it. About one model finding in twenty
    was of that kind.
    """
    string_id = (raw.get("string_id") or "").strip().strip("`")
    file = (raw.get("file") or "").strip().strip("`")
    if not string_id:
        return None
    key = (file, string_id)
    msg = l10n.get(key)
    if msg is None:
        # Tolerate an attribute suffix the model appended, and a wrong path.
        base = string_id.rsplit(".", 1)[0]
        msg = l10n.get((file, base))
        if msg is None:
            candidates = [k for k in l10n if k[1] in (string_id, base)]
            if len(candidates) != 1:
                return None
            key = candidates[0]
            msg = l10n[key]
        else:
            key = (file, base)
    current = (raw.get("current") or "").strip()
    suggest = (raw.get("suggest") or "").strip()
    if suggest and current and suggest == current:
        return None
    if not (raw.get("summary") or "").strip():
        # A finding with nothing to say cannot be triaged or reported.
        return None

    return Finding(
        locale=locale,
        file=key[0],
        string_id=key[1],
        category=_category(raw),
        check="llm",
        impact=_impact(raw),
        summary=(raw.get("summary") or "").strip(),
        current=current,
        suggest=suggest,
        rationale=(raw.get("rationale") or "").strip(),
        reads_as_deliberate=_deliberate(raw),
        string_hash=msg.hash(),
        origin={"confidence": raw.get("confidence", "")},
    )
