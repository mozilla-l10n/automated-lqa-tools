"""The baseline reviewer: a from-scratch pass when a locale is added.

The incremental path works on a delta someone else computed. A brand new
locale has no delta -- roughly 18,000 strings and no prior knowledge -- and
that is a different job: it wants to read whole files in context, notice
that a term drifts across a surface, and follow a developer comment into a
neighbouring string. That is what the manual reviews did well, so the
baseline reuses their shape: eight partitions of the tree, one headless
`claude` invocation each, run in parallel.

The agent is given **read-only tools only** -- no Write, no Edit, no Bash.
It cannot touch the locale tree, the reference tree, or this repository's
own scripts; it returns its findings as its final message and the driver
parses them. That is a structural guarantee rather than an instruction in a
prompt, which matters because this is the one path where a model has file
access at all. Changing the tooling is a commit someone makes and
`selftest.py` re-pins, never something a run does.

A partition that fails or times out does not lose the others, and
`--partitions` re-runs just that one.

This path reads the whole tree, so it is far heavier than a normal run.
It happens once per locale and never again; from then on the locale is on
the incremental path.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field

from findings import Finding
from llm_incremental import language_of

# A project declares its own split under `partitions:` in config.yaml. The
# point is thematic coherence: a reviewer spots terminology drift only
# within what it can see at once, so a partition should be one surface, not
# an arbitrary slice.
#
# This is the eight-way split the manual Firefox reviews used, kept as the
# default for a project that declares none.
DEFAULT_PARTITIONS = [
    ("preferences", ["browser/browser/preferences/"]),
    ("browser-a-l", ["browser/browser/*.ftl:a-l"]),
    ("browser-m-z", ["browser/browser/*.ftl:m-z"]),
    ("newtab-and-branding", [
        "browser/browser/newtab/", "browser/browser/touchbar/",
        "browser/browser/policies/", "browser/branding/", "browser/installer/",
    ]),
    ("toolkit-about", ["toolkit/toolkit/about/"]),
    ("toolkit-rest", ["toolkit/", "!toolkit/toolkit/about/"]),
    ("devtools", ["devtools/"]),
    ("platform", ["dom/", "security/", "netwerk/", "mobile/"]),
]

# Every file must land in exactly one partition. Anything the patterns above
# do not claim -- browser/chrome/*.properties, browser/browser/enterprise/,
# locale-only files -- goes here rather than being silently skipped.
CATCHALL = "other"

INSTRUCTIONS = """\
You are reviewing the {language} ({locale}) localization of Firefox.

Locale tree: {l10n}
en-US reference (same relative paths): {source}

Your partition is **{partition}**. Review exactly these files and no others:

{files}

For each file, read the localized file and the en-US file at the same
relative path under the reference tree. Use the `#` developer comments as
context.

{rules}

## Output

Your final message must be a single JSON object and nothing else -- no
report, no commentary, no code fence:

{{"findings": [{{"string_id": "...", "file": "...", "category": "A|B|C|D|E",
  "impact": 1, "summary": "...", "current": "...", "suggest": "...",
  "rationale": "...", "confidence": "high|medium",
  "reads_as_deliberate": false}}]}}

`file` is the path relative to the locale tree. `current` must be the exact
defective fragment, copied verbatim from the localized string, because a
later run uses it to verify whether the defect is gone.

Reply `{{"findings": []}}` if the partition is clean. That is a normal
result, not a failure.

You have read-only tools. Read the files, do not try to change anything.
"""


def _rules(project, locale: str) -> str:
    """Reuse the incremental prompt's rules so both paths judge alike."""
    name = "variant_review.md" if project.is_variant(locale) else "incremental_review.md"
    text = project.prompt(name)
    start = text.index("## What to report")
    end = text.index("## Categories")
    body = text[start:end]
    conventions = project.conventions(locale).strip() or (
        "_No conventions recorded yet for this locale. Infer them by counting "
        "what the tree does, and do not impose conventions from outside it._"
    )
    return body.format(
        language=language_of(locale),
        locale=locale,
        source_locale=project.variant_of(locale) or "en-US",
        conventions=conventions,
    )


def partition_files(l10n_root: str, extensions=(".ftl", ".properties", ".ini"),
                    files=None, partitions=None) -> dict[str, list[str]]:
    """Assign every file in the tree to exactly one partition.

    Coverage is the point: a baseline that quietly skips a directory looks
    like a clean locale. Each file goes to the first partition that claims
    it, and whatever is left over goes to ``other``.
    """
    if files is not None:
        everything = sorted(files)
    else:
        everything = []
        for dirpath, dirnames, filenames in os.walk(l10n_root):
            dirnames[:] = [d for d in dirnames if d != ".git"]
            for fn in filenames:
                if fn.endswith(tuple(extensions)):
                    everything.append(os.path.relpath(os.path.join(dirpath, fn), l10n_root))
        everything.sort()

    partitions = partitions or DEFAULT_PARTITIONS
    buckets: dict[str, list[str]] = {name: [] for name, _ in partitions}
    buckets[CATCHALL] = []

    def claims(patterns: list[str], rel: str) -> bool:
        include = [x for x in patterns if not x.startswith("!")]
        exclude = [x[1:] for x in patterns if x.startswith("!")]
        if any(rel.startswith(e) for e in exclude):
            return False
        for pattern in include:
            if "*.ftl:" in pattern:
                prefix, _, span = pattern.partition("*.ftl:")
                if not rel.startswith(prefix) or "/" in rel[len(prefix):]:
                    continue
                if not rel.endswith(".ftl"):
                    continue
                first = os.path.basename(rel)[0].lower()
                if (span == "a-l") == (first <= "l"):
                    return True
            elif rel.startswith(pattern):
                return True
        return False

    for rel in everything:
        for name, patterns in partitions:
            if claims(patterns, rel):
                buckets[name].append(rel)
                break
        else:
            buckets[CATCHALL].append(rel)

    assigned = sum(len(v) for v in buckets.values())
    if assigned != len(everything):  # pragma: no cover - defensive
        raise AssertionError(
            f"partitioning lost files: {len(everything)} in tree, {assigned} assigned"
        )
    return {name: files for name, files in buckets.items() if files}


# Everything the agent is allowed to do. No Write, no Edit, no Bash: the
# baseline reads and reports, and cannot alter the trees it is reviewing or
# the scripts reviewing them.
READ_ONLY_TOOLS = "Read,Grep,Glob"

_FENCE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$")


def _parse_result(text: str):
    """Pull the findings object out of the agent's final message."""
    text = _FENCE.sub("", (text or "").strip())
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        pass
    # Tolerate a stray sentence around the object.
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        try:
            return json.loads(text[start : end + 1]), None
        except json.JSONDecodeError as exc:
            return None, str(exc)
    return None, "no JSON object in the reply"


@dataclass
class Baseline:
    """The result of a whole baseline pass.

    ``clean`` and ``failed`` are kept apart because they mean opposite
    things: a clean partition is evidence, a failed one is the absence of it.
    They used to share one list called ``empty``.
    """

    findings: list = field(default_factory=list)
    clean: list = field(default_factory=list)
    covered: set = field(default_factory=set)
    failed: list = field(default_factory=list)
    attempted: int = 0


@dataclass
class Outcome:
    """What one partition did.

    ``ok`` is the whole point. ``_run_partition`` used to return ``[]`` for a
    clean partition *and* for a timeout, a non-zero exit, unreadable CLI
    output, an agent error and an unparseable reply -- so the caller could not
    tell "this surface is fine" from "nobody looked". It counted the files
    either way, advanced their snapshot hashes, and the strings were never
    offered to a reviewer again. A transient timeout permanently skipped a
    ninth of the locale.
    """

    name: str
    ok: bool
    findings: list = field(default_factory=list)
    reason: str = ""


def _run_partition(project, locale, l10n_root, source_root, name, files, log,
                   locale_paths=None):
    if not files:
        log(f"    partition {name}: no files, skipped")
        return Outcome(name, True)

    # Partitioning works in *reference* paths, because that is what a message
    # key is made of and so what the caller can turn back into reviewed
    # strings. The agent has to be handed a path that exists on disk, which
    # for a layout where the two differ is the localized one.
    locale_paths = locale_paths or {}
    listing = "\n".join(f"- {locale_paths.get(f, f)}" for f in files)
    prompt = INSTRUCTIONS.format(
        language=language_of(locale), locale=locale,
        l10n=l10n_root, source=source_root, partition=name,
        files=listing, rules=_rules(project, locale),
    )

    cmd = [
        _claude_bin(),
        "-p", prompt,
        "--output-format", "json",
        "--permission-mode", "default",
        "--allowedTools", READ_ONLY_TOOLS,
        "--disallowedTools", "Write,Edit,NotebookEdit,Bash,WebFetch,WebSearch,Task",
        "--add-dir", l10n_root,
        "--add-dir", source_root,
    ]
    model = project.llm.get("baseline_model")
    if model:
        cmd += ["--model", model]

    log(f"    partition {name}: {len(files)} files")
    try:
        proc = subprocess.run(
            cmd,
            cwd=tempfile.gettempdir(),
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=int(project.llm.get("baseline_timeout_seconds", 3600)),
        )
    except subprocess.TimeoutExpired:
        log(f"    partition {name}: timed out; re-run it with --partitions {name}")
        return Outcome(name, False, reason="timed out")

    if proc.returncode != 0:
        log(f"    partition {name}: exit {proc.returncode}: {proc.stderr[-400:]}")
        return Outcome(name, False, reason=f"exit {proc.returncode}")

    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        log(f"    partition {name}: unreadable CLI output: {proc.stdout[:300]}")
        return Outcome(name, False, reason="unreadable CLI output")

    if envelope.get("is_error"):
        log(f"    partition {name}: agent reported an error: "
            f"{str(envelope.get('result'))[:300]}")
        return Outcome(name, False, reason="the agent reported an error")

    denials = envelope.get("permission_denials") or []
    if denials:
        # The agent tried to use a tool it does not have. Worth surfacing:
        # it means the prompt is steering it somewhere it should not go.
        log(f"    partition {name}: {len(denials)} tool denials (expected none)")

    data, error = _parse_result(envelope.get("result"))
    if data is None:
        log(f"    partition {name}: reply was not JSON ({error}); "
            f"re-run it with --partitions {name}")
        return Outcome(name, False, reason=f"reply was not JSON ({error})")
    return Outcome(name, True, findings=data.get("findings", []))


def _claude_bin() -> str:
    found = shutil.which("claude")
    if not found:
        raise RuntimeError(
            "the `claude` CLI is required for baseline reviews but is not on PATH"
        )
    return found


def review(project, locale, l10n_root, source_root, l10n, trees=None, only=None, log=print):
    """Run every partition and return the findings.

    Also returns the partitions that produced nothing, so a caller can tell
    "clean" from "failed".

    ``l10n_root`` is the **locale tree**, not the localization repository:
    the partition patterns are written against the paths a message key uses
    (``browser/browser/preferences/``), and rooting this at the repository
    instead prefixes every path with a locale code, so nothing matches, every
    file falls into ``other``, and the split silently stops existing. It did:
    45,440 files from 230 locales in one bucket.
    """
    from llm_incremental import _to_finding

    configured = project.data.get("partitions")
    locale_paths = dict(trees.locale_paths) if trees else {}
    buckets = partition_files(
        l10n_root, tuple(project.extensions),
        files=sorted(trees.l10n_files) if trees and trees.l10n_files else None,
        partitions=[(p["name"], p["paths"]) for p in configured] if configured else None,
    )
    if only:
        unknown = [name for name in only if name not in buckets]
        if unknown:
            raise RuntimeError(
                f"unknown partition(s): {', '.join(unknown)}; "
                f"available: {', '.join(buckets)}"
            )
    partitions = [(n, f) for n, f in buckets.items() if not only or n in only]

    results: list[Finding] = []
    clean: list[str] = []
    failed: list[tuple[str, str]] = []
    covered: set[str] = set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {
            pool.submit(
                _run_partition, project, locale, l10n_root, source_root,
                name, files, log, locale_paths,
            ): (name, files)
            for name, files in partitions
        }
        for future in concurrent.futures.as_completed(futures):
            name, files = futures[future]
            try:
                outcome = future.result()
            except Exception as exc:  # noqa: BLE001 - one partition, not the run
                log(f"    partition {name} failed: {exc}")
                failed.append((name, str(exc)))
                continue
            if not outcome.ok:
                failed.append((name, outcome.reason))
                continue
            # Only now are these files reviewed. A partition that failed
            # leaves its files out of `covered`, so their snapshot hashes do
            # not advance and the next run offers them again.
            covered.update(files)
            if not outcome.findings:
                clean.append(name)
            for raw in outcome.findings:
                finding = _to_finding(locale, raw, l10n)
                if finding is not None:
                    results.append(finding)

    log(f"    baseline: {len(results)} findings from "
        f"{len(partitions) - len(failed)} of {len(partitions)} partitions")
    if failed:
        log("    did NOT review: "
            + "; ".join(f"{n} ({why})" for n, why in sorted(failed)))
    return Baseline(results, clean, covered, failed, len(partitions))
