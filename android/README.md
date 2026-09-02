# Android l10n QA

Localization quality review for Mozilla's Android applications: **Firefox
for Android** (fenix), **Focus**, and the shared **Android Components**
library they are built on.

| | |
|---|---|
| Repository | [`mozilla-l10n/android-l10n`](https://github.com/mozilla-l10n/android-l10n) |
| Source and locales | one repository — `res/values/` is the source, `res/values-<code>/` each locale |
| Path mapping | `firefox.toml` and `focus.toml`, read with `moz.l10n.paths` |
| Locales checked | listed in [`config.yaml`](config.yaml) |
| Format | Android XML string resources (`strings.xml`) |
| Workflow | **Actions → Android l10n QA** |

Results arrive as a pull request on `l10n-qa/android`, separate from the
Firefox one so the two teams do not have to read each other's findings.

Start at [`../reports/android.md`](../reports/android.md), then the
per-locale report at `../reports/<locale>/android.md`, which sits beside
that locale's Firefox report.

## How this differs from the Firefox project

Everything format-agnostic is shared, in [`../lib/`](../lib/). Three things
here are genuinely different.

**One repository, TOML-mapped paths.** There is no separate reference
repository and no mirrored tree: `res/values/strings.xml` sits beside
`res/values-it/strings.xml`, and the mapping — including Android's own
locale codes, where `pt-BR` becomes `pt-rBR` — comes from the compare-locales
configs. `lib/layout.py` delegates that to `moz.l10n.paths`.

Findings are keyed by the **reference** path, which is the one identifier
every locale shares, so stored state survives. Reports show the localized
path, because that is the file you would edit.

**printf placeholders, not Fluent variables.** Android formats through
`String.format`, so a placeholder carries a type as well as a position.
`%1$s` where the source says `%1$d` throws at runtime rather than rendering
wrong, and mixing `%s` with `%1$s` in one string throws too. The shared
variable check compares argument *names* and cannot see a retyped
placeholder, so `tools/checks.py` adds one that compares the literal specs.
The shared `variables` check is switched off here: it reports the same
defects in terms of moz.l10n's derived `arg1` names rather than the `%1$s`
actually in the file, and it was verified to catch nothing extra across
fourteen locales.

**Escaping.** A bare apostrophe or double quote in a string body fails the
Android build. moz.l10n unescapes on parse, so the check reads the file
rather than the model.

There is no access-key or Fluent-term check here, and no
`translatable="false"` check — the repository exports only translatable
strings, so that attribute never appears.

## Running it

From the repository root:

```bash
# deterministic checks only, writes nothing
.venv/bin/python lib/run.py --project android --locale it --no-llm --dry-run \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n

# the real thing
export ANTHROPIC_API_KEY=...
.venv/bin/python lib/run.py --project android --locale it \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n
```

`--l10n-dir` and `--source-dir` are the same path: the repository is its own
reference. Both are used exactly as they are on disk, so pull first.

A from-scratch review **batches strings through the API** rather than handing
whole files to an agent, because Fenix keeps thousands of strings in one
large `strings.xml` — source and target together are more than one agent can
read. Unlike Fluent, an Android string carries its context in its own
developer comment rather than in neighbouring entries, so little is lost.

`--baseline-strategy agent` forces the file-reading agent instead, which
works well for `android-components` and `focus` and needs no API key, only
an authenticated `claude` CLI:

```bash
.venv/bin/python lib/run.py --project android --locale it \
    --mode baseline --baseline-strategy agent \
    --partitions android-components --partitions focus \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n
```

## Verifying a change

```bash
.venv/bin/python android/tools/selftest.py --l10n-dir ~/github/android-l10n
```

23 assertions: the layout resolves, placeholders survive parsing verbatim,
the checks catch real defects that exist in other locales today (`cs` and
`ar` drop a placeholder, `de` swapped `%s` for `%1$s`, `zh-CN` invented one,
`ja` has an unreachable `one` plural), and they stay silent on the locales
that are correct.
