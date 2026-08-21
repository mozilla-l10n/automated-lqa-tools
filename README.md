# llm-l10n-qa

Automation for localization quality: LLM-assisted review with per-project
state, so a run only looks at what changed since the last one.

[`lib/`](lib/) holds the pipeline. Each project is a directory beside it
holding only what differs: its configuration, prompts, docs, locale
instructions, state, and the checks its file format needs.

Reports are the exception: they live in [`reports/`](reports/) at the root,
grouped by **locale** rather than by project, because a locale usually has
one team and they want everything about their language together.

```
reports/firefox.md        every locale, one project
reports/android.md
reports/it/firefox.md     one locale, one project
reports/it/android.md
```

| Project | What it covers | |
|---|---|---|
| [`firefox/`](firefox/) | Firefox desktop, plus shared `toolkit` and `dom` strings | [README](firefox/README.md) · [reports](reports/firefox.md) |
| [`android/`](android/) | Firefox for Android, Focus, and Android Components | [README](android/README.md) · [reports](reports/android.md) |
| [`firefox_ios/`](firefox_ios/) | Firefox for iOS | [README](firefox_ios/README.md) · [reports](reports/firefox_ios.md) |

Each has its own workflow and opens its own pull request, so a reviewer only
sees the project they work on.

## Reading the reports

Published at
**<https://mozilla-l10n.github.io/automated-lqa-tools/>** — one page, two
dropdowns: pick a locale and a project. Choosing **All locales** shows that
project's cross-locale summary. Not every project covers every locale, so
the project list follows the locale you pick.

The same reports are plain markdown under [`reports/`](reports/) if you
would rather read them on GitHub.

To preview the site locally:

```bash
pip install markdown
python site/build.py
python -m http.server -d _site
node site/selftest.mjs      # exercises the dropdown logic
```

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

A run writes only its own project's `state/`, its own files under
`reports/`, and — on first sight of a locale — a draft under `locales/`. It never edits the content it
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

Create a sibling directory with `config.yaml`, `prompts/`, `tools/checks.py`
and `docs/`; the pipeline maintains `locales/` and `state/`, and writes
into the shared `reports/` tree at the root.
Give it its own workflow in `.github/workflows/` and its own README.

`config.yaml` declares the three things that vary:

- **`layout`** — how localized files relate to source files. `mirrored` is
  two repositories with identical relative paths (Firefox); `android` is one
  repository with compare-locales TOML mappings; `xliff` is one file per
  locale carrying source and target together (iOS). A new shape means a
  loader in [`lib/layout.py`](lib/layout.py), not changes to the pipeline.
- **`checks`** — which checks run, in report order. Shared ones come from
  `lib/common_checks.py`; the project's `tools/checks.py` composes them with
  its own and an unknown name fails loudly.
- **`baseline`** — `agent` hands whole files to a subagent, which catches
  drift across a surface; `batched` sends strings through the API, which is
  what you need when a single file is too large for one agent to read.

The library was extracted when the second project arrived rather than
designed up front, so its seams follow the differences that actually turned
up. Keep doing that: copy, then extract once duplication shows what is
genuinely common.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

The incremental reviewer needs an `ANTHROPIC_API_KEY`; in CI it comes from
the repository secrets. A from-scratch run does not, because it drives the
`claude` CLI, which carries its own credentials.

Every entry point is non-interactive — subprocesses get a closed stdin,
nothing prompts, and one failure does not stop the rest.
