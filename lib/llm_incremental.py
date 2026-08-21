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

from findings import Finding

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
        identical = src is not None and msg.text().strip() == src.text().strip()
        if identical and not keep_identical:
            continue
        block = [f"### {msg.id}", f"file: {msg.file}"]
        if msg.comment:
            comment = "\n".join(f"  {line}" for line in msg.comment.splitlines())
            block.append(f"developer comment:\n{comment}")
        if src is not None:
            block.append(f"source: {src.text()}")
        else:
            block.append("source: (no source string; locale-only)")
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
    set it was asked about, and it is what the snapshot and the
    did-the-reviewer-stay-silent logic are advanced by. ``stopped`` holds the
    reason the pass ended early, or "" if it ran to the end.
    """

    reviewed: set = field(default_factory=set)
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
        found, malformed = collect(response.content, locale, l10n)
        out.extend(found)
        progress.reviewed.update(batch_keys)
        if malformed:
            log(f"      discarded {malformed} malformed item(s) in this batch")
    return out, usage, progress


def collect(content, locale, l10n) -> tuple[list[Finding], int]:
    """Findings from one response, plus a count of what was not one.

    The tool schema says each finding is an object, and the model mostly
    obliges -- but nothing enforces it, and a batch that answered with a
    bare string in the list used to reach ``_to_finding`` and raise on
    ``.get``. That killed the locale from inside the batch loop, discarding
    twenty-seven batches of completed review over one item. A response that
    is the wrong shape is a dropped item, counted and logged; it is not a
    reason to throw away the work that was done.
    """
    out: list[Finding] = []
    malformed = 0
    for block in content:
        if getattr(block, "type", "") != "tool_use":
            continue
        payload = block.input if isinstance(block.input, dict) else {}
        items = payload.get("findings")
        if not isinstance(items, list):
            malformed += 1
            continue
        for raw in items:
            if not isinstance(raw, dict):
                malformed += 1
                continue
            finding = _to_finding(locale, raw, l10n)
            if finding is not None:
                out.append(finding)
    return out, malformed


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

    return Finding(
        locale=locale,
        file=key[0],
        string_id=key[1],
        category=(raw.get("category") or "B").strip().upper()[:1],
        check="llm",
        impact=int(raw.get("impact") or 0),
        summary=(raw.get("summary") or "").strip(),
        current=current,
        suggest=suggest,
        rationale=(raw.get("rationale") or "").strip(),
        string_hash=msg.hash(),
        origin={"confidence": raw.get("confidence", "")},
    )
