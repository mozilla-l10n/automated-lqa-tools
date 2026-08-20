# Firefox l10n QA

Localization quality review for **Firefox desktop**, plus the shared
`toolkit` and `dom` strings other Mozilla projects consume.

| | |
|---|---|
| Localized strings | [`mozilla-l10n/firefox-l10n`](https://github.com/mozilla-l10n/firefox-l10n) — one directory per locale |
| en-US reference | [`mozilla-l10n/firefox-l10n-source`](https://github.com/mozilla-l10n/firefox-l10n-source) — same relative paths |
| Locales checked | 14, listed in [`config.yaml`](config.yaml) |
| Formats | `.ftl`, `.properties`, `.ini` (no `.dtd` — that migration is done) |
| Workflow | **Actions → Firefox l10n QA** |

```
config.yaml          which repositories, which locales, which model
RUNBOOK.md           the manual review method this automates
docs/                how to add a locale, how to flag a false positive
prompts/             the review prompts and the finding schema
tools/               the pipeline
locales/<code>/      conventions.md + suppressions.yaml  (you edit these)
state/<code>/        snapshot, findings, metadata          (the pipeline owns these)
reports/<code>.md    the generated report                  (read this)
```

## Reading the output

Start at [`reports/00-summary.md`](reports/00-summary.md), then the
per-locale report. Each one opens with what changed in this run — new,
fixed, needs re-read, retired — before the full open backlog.

Findings carry two axes. **Category** A–E says what kind of defect it is;
**impact** 1–4 says what the user experiences. Impact 1–2 — broken output
and wrong content — is the queue worth working through first.

## Running it

Manual dispatch: **Actions → Firefox l10n QA → Run workflow**. Pick locales
(or `all`), and use `dry_run` the first time to see what it would do. The
daily schedule is present in the workflow but commented out.

Results arrive as a pull request on the branch `l10n-qa/firefox`. The branch
is reused, so successive runs add commits to the same open PR rather than
piling up one per run; merge it whenever you have read the diffs. If a run
finds nothing new, it pushes nothing.

Locally, from the repository root:

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

`--l10n-dir` and `--source-dir` point at checkouts you already have, which
is the usual way to run this locally. They are used **exactly as they are on
disk** — nothing is fetched or checked out for you, so pull them first:

```bash
git -C ~/mozilla/git/firefox-l10n       pull --ff-only
git -C ~/mozilla/git/firefox-quarantine pull --ff-only
```

The run prints the sha, branch and commit date of both trees before it
starts, so a stale or off-branch checkout is visible rather than silently
producing an empty delta. Getting this wrong is not destructive: the delta
is computed from content hashes, so anything missed by a stale run simply
shows up as changed on the next one.

Omit both flags and the run makes its own clones under `work/` instead:
blobless, depth 1, and sparse to the locales being checked, which is 16 MB
rather than the repository's full 2.1 GB.

Useful flags: `--limit N` caps how many changed strings go to the model,
`--mode baseline` forces a from-scratch pass, `--partitions devtools`
re-runs one slice of a baseline, `--no-llm` skips the API entirely.

## The checks

Deterministic, so they run over the whole tree every time and cost nothing:
completeness, Fluent and `.properties` syntax, variable and placeholder
mismatches, plural and select selector mismatches, term-parameter
mismatches, plural variants, access keys against their labels, markup and
`data-l10n-name` parity, and typography measured against the locale's own
conventions.

Two subtleties are worth knowing, because getting them wrong is what makes
most l10n checkers noisy.

**Fluent arguments are scoped to the message, not the attribute.**
`l10n.setAttributes(el, id, { count })` makes `count` available to every
attribute of that id, so a locale using it in `.message` where en-US used it
in `.heading` is perfectly fine. Comparing attribute-to-attribute reports
that as an undefined variable.

**Plural completeness is not a CLDR question.** CLDR is used only to decide
whether a variant is *reachable* — Japanese has no `one` category, so a
`[one]` variant there is dead text. It is deliberately not used to decide a
variant is missing: CLDR gives Mexican Spanish a `many` category that no
Firefox Spanish string uses, so requiring the full set would flag every
plural in the locale. Expected forms are measured from what the locale does
across its own tree, and only where en-US selects on a *category*
(`[one]`) rather than an exact number (`[1] Remove / [other] Remove All`,
which is a one-versus-many choice that locales are right to mirror). A
locale adding forms en-US lacks is never flagged — that is what localizing a
plural means.

Several of those exist because the hand-written reviews found defects
nothing was checking for: a selector switching on a variable the code never
passes (the number renders blank), a term called with a parameter its
definition does not select on, and malformed closing tags like `</a >`. The
plural check found one they missed — Polish
`pdfjs-editor-comments-sidebar-title` has only `one`/`other`, so five
comments render the *few* form.

Nothing here assumes what is correct for a language. Conventions — quote
family, apostrophe, ellipsis, dash, no-break space, register — are counted
over the whole tree first, and only deviations from the locale's *own* clear
majority are flagged. Where the tree is genuinely split the report says
`_mixed_` and nothing is raised. That is what keeps Japanese ASCII ellipsis,
Dutch en dashes, and Polish case-parameterized brand terms out of the
results.

## Two things you will want to do

**Add a locale** — put its code in [`config.yaml`](config.yaml). Its first
run has no state, so it takes the baseline path over the whole tree. That is
the expensive one: **roughly $50–70** for a full Firefox locale, measured
from a real partition run. Every run after that is incremental. See
[`docs/adding-a-locale.md`](docs/adding-a-locale.md).

**Flag a false positive** — add a sentence to
`locales/<code>/conventions.md` so the model stops raising it, or a rule to
`locales/<code>/suppressions.yaml` to filter it after the fact. Both are
re-applied to the whole backlog on the next run, so a rule written today
retires findings raised months ago, and deleting a rule brings them back.
See [`docs/suppressions.md`](docs/suppressions.md).

## Where the state came from

Fourteen locales were reviewed by hand between July and August 2026, driven
by [`RUNBOOK.md`](RUNBOOK.md). Those reviews were imported rather than
redone: `tools/import_legacy.py` read the reports into `state/`, classified
each finding against the current tree as open or already fixed, and turned
the maintainer decisions they recorded into the seeded conventions and
suppressions.

`tools/selftest.py` pins the result as 35 assertions — the defects those
reviews found must still be caught, and the conventions they established
must stay silent. Run it after touching `tools/checks.py`:

```bash
.venv/bin/python firefox/tools/selftest.py \
    --l10n-dir ~/mozilla/git/firefox-l10n \
    --source-dir ~/mozilla/git/firefox-quarantine
```
