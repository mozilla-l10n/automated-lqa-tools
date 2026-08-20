# llm-l10n-qa

Automation for localization quality: LLM-assisted review with per-project
state, so a run only looks at what changed since the last one.

Each automation lives in its own top-level directory and is self-contained —
its own configuration, prompts, tooling, state and reports.

| Project | What it covers | |
|---|---|---|
| [`firefox/`](firefox/) | Firefox desktop, plus shared `toolkit` and `dom` strings | [README](firefox/README.md) · [reports](firefox/reports/00-summary.md) |

## The shape of a run

The Firefox pipeline is the only one so far, but the approach is meant to
carry over.

1. **Refresh** the localized tree and the en-US reference. Clones are
   blobless, depth 1, and sparse to what is being checked.
2. **Diff** against a stored snapshot. Every string carries a content hash
   of its localized text *and* of its source text, so a run detects both
   "the translation changed" and "the English changed underneath a
   translation nobody updated" — without needing any repository history,
   which matters when the repository is gigabytes of sync commits.
3. **Check** deterministically over the whole tree: syntax, placeholders,
   plural selectors, markup, completeness, and typography measured against
   the locale's own conventions. No model is involved, so this always runs
   in full.
4. **Review** only the changed strings with the model. Reviewing the delta
   rather than the tree is what makes frequent runs practical; a project or
   locale with no stored state gets a one-off from-scratch pass instead.
5. **Reconcile** with the stored backlog — what is new, what got fixed, what
   became obsolete, what needs another look.
6. **Suppress** anything matching the project's false-positive rules, across
   the whole backlog rather than just this run's findings.
7. **Propose** the result as a pull request. Nothing lands unreviewed.

Two ideas do most of the work. **Conventions are counted, never assumed** —
a check flags deviations from what the tree itself overwhelmingly does, and
says nothing where usage is genuinely split. And **findings have a
lifecycle**: they are raised once and then tracked, so a report can say what
is new and what got fixed rather than restating everything every time.

## What the automation can and cannot touch

A run writes only its own project's `state/`, `reports/`, and — on first
sight of a locale — a draft under `locales/`. It never edits the content it
reviews, and it never edits itself.

That holds structurally, not by convention. The incremental reviewer is a
plain API request: the model returns findings and has no tools at all. The
from-scratch reviewer is the only path where a model sees a filesystem, and
it runs with `Read,Grep,Glob` and an explicit deny-list covering `Write`,
`Edit` and `Bash`, returning its findings as its final message rather than
writing them anywhere.

So changing the checks is a human job: edit the tooling, re-run the
project's self-test, commit. A run never improvises its own logic.

## Adding another automation

Create a sibling directory and keep it self-contained, the way `firefox/`
is: `config.yaml`, `prompts/`, `tools/`, `docs/`, plus the `locales/`,
`state/` and `reports/` trees the pipeline maintains. Give it its own
workflow in `.github/workflows/`, and its own README describing what it
covers and how to run it.

There is deliberately **no shared library yet**. Everything currently lives
under `firefox/`, because factoring a framework out of a single example
tends to produce the wrong abstraction. The parts most likely to be worth
extracting when a second project arrives are the snapshot and delta engine,
the finding lifecycle, the suppression layer, and the report renderer —
`config.py` already takes the project directory as a parameter, so that is
the natural seam. Copy first; extract once the duplication shows what is
actually common.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

The incremental reviewer needs an `ANTHROPIC_API_KEY`; in CI it comes from
the repository secrets. A from-scratch run does not, because it drives the
`claude` CLI, which carries its own credentials.

Every entry point is non-interactive — subprocesses get a closed stdin,
nothing prompts, and one failure does not stop the rest.
