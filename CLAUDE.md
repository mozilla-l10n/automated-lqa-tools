# Working in this repository

LLM-assisted localization QA. `lib/` is the pipeline; each project directory
(`firefox/`, `android/`, `firefox_ios/`) holds only what differs. Read
`README.md` first for the shape of a run, then the project's own README.

## Commands

```bash
# setup
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# deterministic checks only, writes nothing — always safe, always start here
.venv/bin/python lib/run.py --project firefox --locale it --no-llm --dry-run \
    --l10n-dir ~/mozilla/git/firefox-l10n --source-dir ~/mozilla/git/firefox-quarantine

# a real run
export ANTHROPIC_API_KEY=...
.venv/bin/python lib/run.py --project android --locale it \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n

# the tests — run all three after touching anything in lib/
.venv/bin/python firefox/tools/selftest.py
.venv/bin/python android/tools/selftest.py
.venv/bin/python firefox_ios/tools/selftest.py
```

Local clones are used exactly as they are on disk; nothing is fetched. Pull
them yourself. Android and iOS pass the same path twice: the repository is
its own reference.

## The rule that matters most

**A false positive costs more than a missed defect.** This output is a
backlog a localization team works through by hand. Every check here was
tightened at least once after producing noise, and several were deleted or
disabled outright when they turned out to be redundant.

Concretely, when adding or changing a check:

1. **Count, never assume.** No check may encode an opinion about what a
   language *should* do. `conventions.py` measures what the tree actually
   does and checks flag deviations from its own majority; where usage is
   genuinely split, nothing is reported. This is what keeps Japanese ASCII
   ellipsis, Dutch en dashes and Polish case-parameterized brands out.
2. **Run it across every locale before believing it.** The first version of
   `ui_references` produced 123–264 false positives per Firefox locale; the
   first plural check flagged most of Polish and Russian. Both looked fine
   on one locale.
3. **Never blame a locale for its source.** If en-US has the same straight
   quote, the same typo, the same odd wording, it is not the locale's
   defect.
4. **Add the case to `selftest.py`.** Each suite pins real defects that
   exist in the repositories today and real conventions that must stay
   silent. A defect fixed upstream moves to `FIXED_UPSTREAM` rather than
   being deleted — "the check broke" and "the defect is gone" must stay
   distinguishable.

## Reporting honestly

The finding lifecycle is the fiddliest part of the system and every rule in
it was written after getting it wrong:

- **fixed** — the string changed *and* the defect went with it.
- **withdrawn** — a check stopped firing while the string never moved. The
  check changed its mind; do not call that fixed and credit the team with
  work they did not do.
- **needs-recheck** — the string moved but text matching cannot tell whether
  the defect survived. Say so; do not guess. A quoted fragment stays a
  substring when the fix was to add words around it.
- **dismissed / suppressed** — a person said it is fine. Kept with the
  reason, never deleted.

Two invariants that were violated once each and must not be again:

- Comparison for fix detection is **literal**. It must not fold case or
  strip punctuation — `INDIRIZZO` → `Indirizzo` and `</a >` → `</a>` are
  real fixes.
- **Silence from the reviewer closes nothing about an unchanged string.**
  The model is not deterministic; not spotting a defect twice is not
  evidence it is gone. No flag may relax this.

## Cost and scope

Do not write dollar figures or token estimates anywhere in the repository —
that was a deliberate decision. Describe paths by what they do: a baseline
reads the whole tree, an incremental reads a delta, deterministic checks
involve no model.

`--recheck` is for repairing state after the *checking logic* changes. It
is not scheduled hygiene and must stay out of the workflows.

## Saying a finding is fine

Three mechanisms, narrowest first — see `<project>/docs/suppressions.md`:

| Scope | Where |
|---|---|
| one string you have read | `locales/<code>/dismissed.txt`, one line |
| a class that will recur | `locales/<code>/suppressions.yaml` |
| never raise it at all | `locales/<code>/conventions.md` (prose, injected into the prompt) |

All three are re-applied to the whole backlog every run, so they are
retroactive and reversible. Prefer `conventions.md` when it fits: nothing is
raised and no review work is spent.

## What the automation may touch

A run writes its project's `state/`, its own files under `reports/`, and on
first sight of a locale a draft under `locales/`. It never edits the content
it reviews and never edits itself. The incremental reviewer is a plain API
request with no tools; the from-scratch reviewer runs with `Read,Grep,Glob`
and an explicit deny-list. Keep it that way — changing the checks is a human
commit that `selftest.py` re-pins.

## Adding a project

Sibling directory with `config.yaml`, `prompts/`, `tools/checks.py`,
`docs/`. Things that vary in config: `layout` (how localized files map to
source files — `mirrored`, `android`, `xliff`; add a loader in
`lib/layout.py` for a new shape), `checks` (ordered; an unknown name fails
loudly), `baseline` (`agent` hands whole files to a subagent, `batched`
sends strings through the API — use `batched` when one file is too large for
an agent to read), and `display_name` where the directory name would render
badly in a heading.

**Delete a check that cannot fire.** Android's `translatable` and iOS's
`plurals`/`markup` were dropped after checking the repository, not assumed
away. A check that never fires reads as coverage and is only noise waiting
to happen — record the absence and the evidence in the project's
`tools/checks.py` docstring.

Give it its own workflow and its own PR branch: different projects have
different reviewers, and neither team should have to read the other's
findings.
