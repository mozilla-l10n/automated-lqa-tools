# Adding a locale

Add the code to the `locales:` list in [`../config.yaml`](../config.yaml):

```yaml
locales:
  - de
  ...
  - cs        # new
```

That is the whole configuration change. The next run sees no
`state/cs/meta.json`, concludes the locale has never been checked, and takes
the **baseline** path instead of the incremental one.

## What the baseline does

It is a different job from an incremental run. There is no delta to work
from and no accumulated knowledge, so it reads the tree the way the manual
reviews did: nine thematic partitions, one headless `claude` invocation
each, running in parallel, each reading the localized file and its en-US
counterpart together and returning findings as JSON.

The agent has **read-only tools** — `Read`, `Grep`, `Glob`, with `Write`,
`Edit` and `Bash` explicitly denied. It reports its findings as its final
message rather than writing them anywhere, so it cannot alter the locale
tree, the reference tree, or this repository.

Partitioning is verified to be total — every file lands in exactly one
partition, and anything the patterns do not claim goes to `other`. A
baseline that silently skips a directory would look like a clean locale.

A partition that fails or times out does not lose the others. Re-run just
that one:

```bash
python firefox/tools/run.py --locale cs --mode baseline --partitions devtools
```

## Scale, and how to bound it

A full Firefox locale is roughly 18,000 strings across ~370 files, reviewed
in nine parallel partitions. It is far heavier than an incremental run, and
it happens once per locale; every run afterwards works on the delta only.

To spread it over several runs, take a few partitions at a time with
`--partitions`. To see the shape of the work before involving the model at
all:

```bash
python firefox/tools/run.py --locale cs --no-llm --dry-run
```

That runs the deterministic checks over the whole tree, prints the health
numbers, and writes nothing.

## Afterwards: check the inferred conventions

The first run writes `firefox/locales/cs/conventions.md` with a table of
conventions counted over the tree — quote family, apostrophe, ellipsis,
dash, no-break space, register. **Read it.** Everything the checks flag as a
typography deviation is measured against these, so a wrong inference
produces a wave of false positives, and a locale whose usage is genuinely
split shows `_mixed_` and is not flagged at all.

Then add the standing instructions the counting cannot know: deliberate
legacy terminology, files intentionally left in English, house rules the
team has settled on. See [suppressions.md](suppressions.md).

It also writes an empty `firefox/locales/cs/suppressions.yaml` for you to
fill in as false positives turn up.

## If the locale is a variant of English

`en-GB` and `en-CA` are not translations, and the pipeline treats them
differently. Declare that in `config.yaml`:

```yaml
variants:
  en-GB: en-US
  en-CA: en-US
```

93% of `en-GB` and 97% of `en-CA` are byte-identical to en-US **and
correct**, so three things change:

- **Identical strings are reviewed, not skipped.** For a translation an
  identical string is untranslated and worth no tokens. For a variant it is
  the interesting population: the defect to find is a string that should
  have diverged and did not.
- **"File is identical to en-US" stops being reported.** It would fire on
  145 of `en-GB`'s 360 files and mean nothing.
- **The reviewer gets a different prompt** (`prompts/variant_review.md`),
  aimed at spelling, vocabulary, date and unit conventions, and at
  over-correction — a variant must not touch `background-color`, `Firefox
  Color`, or MathML's `color` attribute.

A deterministic `variant_spelling` check runs too. It **learns** the
substitution map from the locale rather than using a word list: every string
that does differ from en-US is a worked example, and aligning the two word
by word yields `color → colour`, `organization → organisation`,
`syncing → synchronising`. Only near-universal substitutions are kept —
`forward → forwards` appears in the alignment but the locale keeps
`forward` far more often, so it is a contextual choice, not a rule. The
rules are then applied to the identical strings to find the ones that were
missed.

Nothing about British or American English is encoded anywhere, so the same
mechanism would work for `pt-PT` against `pt-BR`.

## If the locale is only partly translated

Nothing special is needed. Untranslated strings are dropped before the model
sees them — having it rediscover that a string is still English on every run
is pointless — and completeness is reported in the health check rather than
raised as findings. A locale that is 4,000 strings behind produces a
missing count, not 4,000 defects.

## Removing a locale

Take it out of `config.yaml`. Its `state/` and `reports/` files stay where
they are; delete them by hand if you want them gone. Nothing will run
against it again.
