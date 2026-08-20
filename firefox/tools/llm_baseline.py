"""The baseline reviewer: a from-scratch pass when a locale is added.

The incremental path works on a delta someone else computed. A brand new
locale has no delta -- roughly 18,000 strings and no prior knowledge -- and
that is a different job: it wants to read whole files in context, notice
that a term drifts across a surface, and follow a developer comment into a
neighbouring string. That is what the manual reviews did well, so the
baseline reuses their shape: eight partitions of the tree, one headless
`claude` invocation each, run in parallel.

Each partition writes its own JSON. A partition that fails or times out
does not lose the others, and `--partitions` re-runs just that one.

This path is expensive -- on the order of 2.5-3M input tokens for a full
Firefox locale -- so it runs once per locale and never again; from then on
the locale is on the cheap incremental path.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import shutil
import subprocess
import tempfile

from findings import Finding
from llm_incremental import language_of

# The eight-way split the manual reviews used. It balances file counts and
# keeps each partition thematically coherent, which matters because a
# reviewer spots terminology drift only within what it can see at once.
PARTITIONS = [
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

Write your findings as JSON to `{outfile}` -- nothing else, no report, no
commentary. The file must contain a single JSON object:

{{"findings": [{{"string_id": "...", "file": "...", "category": "A|B|C|D|E",
  "impact": 1, "summary": "...", "current": "...", "suggest": "...",
  "rationale": "...", "confidence": "high|medium"}}]}}

`file` is the path relative to the locale tree. `current` must be the exact
defective fragment, copied verbatim from the localized string, because a
later run uses it to verify whether the defect is gone.

Write `{{"findings": []}}` if the partition is clean. Do not modify any file
in the locale tree or the reference tree.
"""


def _rules(project, locale: str) -> str:
    """Reuse the incremental prompt's rules so both paths judge alike."""
    text = project.prompt("incremental_review.md")
    start = text.index("## What to report")
    end = text.index("## Categories")
    body = text[start:end]
    conventions = project.conventions(locale).strip() or (
        "_No conventions recorded yet for this locale. Infer them by counting "
        "what the tree does, and do not impose conventions from outside it._"
    )
    return body.format(language=language_of(locale), locale=locale, conventions=conventions)


def partition_files(l10n_root: str, extensions=(".ftl", ".properties", ".ini")) -> dict[str, list[str]]:
    """Assign every file in the tree to exactly one partition.

    Coverage is the point: a baseline that quietly skips a directory looks
    like a clean locale. Each file goes to the first partition that claims
    it, and whatever is left over goes to ``other``.
    """
    everything = []
    for dirpath, dirnames, filenames in os.walk(l10n_root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            if fn.endswith(tuple(extensions)):
                everything.append(os.path.relpath(os.path.join(dirpath, fn), l10n_root))
    everything.sort()

    buckets: dict[str, list[str]] = {name: [] for name, _ in PARTITIONS}
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
        for name, patterns in PARTITIONS:
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


def _run_partition(project, locale, l10n_root, source_root, name, files, outdir, log):
    outfile = os.path.join(outdir, f"{name}.json")
    if not files:
        log(f"    partition {name}: no files, skipped")
        return []

    listing = "\n".join(f"- {f}" for f in files)
    if len(files) > 400:
        listing = "\n".join(f"- {f}" for f in files[:400]) + (
            f"\n- …and {len(files) - 400} more matching the same patterns; "
            "review all of them."
        )
    prompt = INSTRUCTIONS.format(
        language=language_of(locale), locale=locale,
        l10n=l10n_root, source=source_root, partition=name,
        files=listing, rules=_rules(project, locale), outfile=outfile,
    )

    cmd = [
        _claude_bin(),
        "-p", prompt,
        "--output-format", "json",
        "--permission-mode", "acceptEdits",
        "--allowedTools", "Read,Grep,Glob,Write",
        "--add-dir", l10n_root,
        "--add-dir", source_root,
        "--add-dir", outdir,
    ]
    model = project.llm.get("baseline_model")
    if model:
        cmd += ["--model", model]

    log(f"    partition {name}: {len(files)} files")
    proc = subprocess.run(
        cmd,
        cwd=outdir,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=int(project.llm.get("baseline_timeout_seconds", 3600)),
    )
    if not os.path.exists(outfile):
        log(f"    partition {name}: produced no output (exit {proc.returncode})")
        log(f"      stderr: {proc.stderr[-500:]}")
        return []
    with open(outfile, encoding="utf-8") as fh:
        try:
            data = json.load(fh)
        except json.JSONDecodeError as exc:
            log(f"    partition {name}: unreadable JSON ({exc})")
            return []
    return data.get("findings", [])


def _claude_bin() -> str:
    found = shutil.which("claude")
    if not found:
        raise RuntimeError(
            "the `claude` CLI is required for baseline reviews but is not on PATH"
        )
    return found


def review(project, locale, l10n_root, source_root, l10n, only=None, log=print):
    """Run every partition and return the findings, plus the partitions that
    produced nothing so a caller can tell 'clean' from 'failed'."""
    from llm_incremental import _to_finding

    buckets = partition_files(l10n_root, tuple(project.extensions))
    partitions = [(n, f) for n, f in buckets.items() if not only or n in only]
    outdir = tempfile.mkdtemp(prefix=f"l10nqa-{locale}-")
    results: list[Finding] = []
    empty: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {
            pool.submit(
                _run_partition, project, locale, l10n_root, source_root,
                name, files, outdir, log,
            ): name
            for name, files in partitions
        }
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                raw_findings = future.result()
            except Exception as exc:  # noqa: BLE001
                log(f"    partition {name} failed: {exc}")
                empty.append(name)
                continue
            if not raw_findings:
                empty.append(name)
            for raw in raw_findings:
                finding = _to_finding(locale, raw, l10n)
                if finding is not None:
                    results.append(finding)
    log(f"    baseline produced {len(results)} findings from {len(partitions)} partitions")
    return results, empty
