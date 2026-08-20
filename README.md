# llm-l10n-qa

Automated localization quality review, driven by deterministic checks and an
LLM, with per-locale state so each run only looks at what changed.

Currently covers one project, **Firefox** (`firefox/`). The layout is
per-project so others can be added as sibling directories without touching
the shared machinery.

```
firefox/
  config.yaml          which repositories, which locales, which model
  RUNBOOK.md           the review method this automates
  docs/                how to add a locale, how to flag a false positive
  prompts/             the review prompts and the finding schema
  tools/               the pipeline
  locales/<code>/      conventions.md + suppressions.yaml  (you edit these)
  state/<code>/        snapshot, findings, metadata          (the pipeline owns these)
  reports/<code>.md    the generated report                  (read this)
```

## What a run does

1. **Refresh** the locale tree and the en-US source. `firefox-l10n` is
   cloned blobless, depth 1, sparse to the locales being checked — 16 MB
   instead of 2.1 GB.
2. **Diff** the tree against the stored snapshot. Every string carries a
   hash of its localized text *and* of its en-US text, so the run detects
   both "the translation changed" and "the English changed underneath a
   translation nobody updated". No repository history is needed.
3. **Check** the whole tree deterministically: completeness, syntax,
   variables, plural selectors, term parameters, access keys, markup, and
   typography against the locale's own measured conventions. Free, so it
   runs in full every time.
4. **Review** the changed strings with the model — only those, which is what
   makes daily runs affordable. A brand new locale has no snapshot, so it
   takes the from-scratch baseline path instead.
5. **Reconcile** against the stored backlog: what is new, what got fixed,
   what became obsolete, what needs another look.
6. **Suppress** anything matching the locale's false-positive rules, across
   the entire backlog, not just this run's findings.
7. **Write** the report — only if it actually changed — and the new state.

## Reading the output

Start at [`firefox/reports/00-summary.md`](firefox/reports/00-summary.md),
then the per-locale report. Each report opens with what changed in this run
(new / fixed / needs re-read / retired) before the full open backlog.

Findings carry two axes. **Category** A–E says what kind of defect it is;
**impact** 1–4 says what the user experiences. Impact 1–2 — broken output
and wrong content — is the queue worth working through first.

## Running it

Manual dispatch: **Actions → Firefox l10n QA → Run workflow**. Pick locales
(or `all`), and use `dry_run` the first time to see what it would do. The
daily schedule is present in the workflow but commented out.

Locally:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# deterministic checks only, writes nothing
.venv/bin/python firefox/tools/run.py --locale it --no-llm --dry-run

# the real thing, against clones you already have
export ANTHROPIC_API_KEY=...
.venv/bin/python firefox/tools/run.py --locale it \
    --l10n-dir ~/mozilla/git/firefox-l10n \
    --source-dir ~/mozilla/git/firefox-quarantine
```

Useful flags: `--limit N` caps how many changed strings go to the model,
`--mode baseline` forces a from-scratch pass, `--partitions devtools`
re-runs one slice of a baseline, `--no-llm` skips the API entirely.

Everything is non-interactive. Subprocesses get a closed stdin, nothing
prompts, and one locale failing does not stop the others.

## Two things you will want to do

**Add a locale** — put its code in `firefox/config.yaml`. Its first run has
no state, so it takes the baseline path over the whole tree, which is
expensive (~2.5–3M input tokens); every run after that is incremental. See
[`firefox/docs/adding-a-locale.md`](firefox/docs/adding-a-locale.md).

**Flag a false positive** — add a sentence to
`firefox/locales/<code>/conventions.md` so the model stops raising it, or a
rule to `firefox/locales/<code>/suppressions.yaml` to filter it after the
fact. Both are re-applied to the whole backlog on the next run, so a rule
written today retires findings raised months ago, and deleting a rule brings
them back. See
[`firefox/docs/suppressions.md`](firefox/docs/suppressions.md).

## Where the current state came from

Fourteen locales were reviewed by hand between July and August 2026. Those
reviews were imported rather than redone: `firefox/tools/import_legacy.py`
read the reports into `state/`, classified each finding against the current
tree as open or already fixed, and turned the maintainer decisions recorded
in them — Japanese ASCII ellipsis, Dutch en dashes, Polish and Slovenian
case-parameterized brand terms, CJK access keys — into the seeded
conventions and suppressions. That import runs once; it is kept in the tree
as the record of where the baseline came from.

## Cost

An incremental run costs roughly in proportion to how much changed. A quiet
day across all fourteen locales is a handful of batches; a large Pontoon
sync is more. `--limit` and `--no-llm` bound it, and a locale with an empty
delta makes no API call at all.
