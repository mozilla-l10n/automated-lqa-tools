# Adding a locale

Add the code to the `locales:` list in `firefox/config.yaml`:

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

## Cost, and how to bound it

A full Firefox locale is roughly 18,000 strings across ~370 files. A
measured 13-file partition cost **$2.30**, which puts a whole locale at
roughly **$50–70**. It happens once per locale; every run afterwards is
incremental and cheap.

To spread it out, run a few partitions at a time with `--partitions`. To see
the shape of the work before spending anything:

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

## If the locale is only partly translated

Nothing special is needed. Untranslated strings are dropped before the model
sees them — paying to have it rediscover that a string is still English on
every run is waste — and completeness is reported in the health check rather
than raised as findings. A locale that is 4,000 strings behind produces a
missing count, not 4,000 defects.

## Removing a locale

Take it out of `config.yaml`. Its `state/` and `reports/` files stay where
they are; delete them by hand if you want them gone. Nothing will run
against it again.
