# Focus for Android l10n QA

Localization quality review for **Firefox Focus for Android**, the private
browser (shipped as Firefox Klar in some regions).

| | |
|---|---|
| Repository | [`mozilla-l10n/android-l10n`](https://github.com/mozilla-l10n/android-l10n), shared with [Firefox for Android](../android/) |
| Source and locales | one repository — `res/values/` is the source, `res/values-<code>/` each locale |
| Path mapping | `focus.toml`, read with `moz.l10n.paths`; `firefox.toml` is read for context only |
| Locales checked | 33 — Firefox for Android's list minus pt-PT, which Focus does not ship (from [`config.yaml`](config.yaml)) |
| Format | Android XML string resources (`strings.xml`) |
| Workflow | **Actions → Focus for Android l10n QA** |

Results arrive as a pull request on `l10n-qa/focus_android`, separate from
Firefox for Android's because Focus is its own Pontoon project.

Start at [`../reports/focus_android.md`](../reports/focus_android.md), then
the per-locale report at `../reports/<locale>/focus_android.md`.

## How this differs from Firefox for Android

The file format and the checks are the same; see
[`../android/README.md`](../android/README.md) for placeholders and
escaping. What differs is that Focus is small — one `strings.xml` of about
250 strings — and that it reads part of its neighbour.

**Conventions are counted with Firefox for Android.** Measured on Focus
alone, 25 of its locales inferred a different convention from the rest of
their tree, from as few as one occurrence: a single curly single quote made
en-GB "curly-single" against thousands of double quotes elsewhere, and
en-GB and en-CA learned no spelling rules at all. The same team translates
both apps, so both projects count the two trees together and always agree.

**A quoted label may name an Android Components string.** Focus is built on
Android Components, not on Fenix, so `ui_references` may resolve a label
Focus quotes to a string in `mozilla-mobile/android-components/`, and
nothing else.

Neither kind of context is ever checked, reviewed or reported here: those
strings belong to Firefox for Android. The `context:` block in
[`config.yaml`](config.yaml) declares both.

**No plural checks.** Focus has no `<plurals>` element, so `plurals` and
`selectors` could never fire and are not run. The self-test fails if that
changes.

## Running it

```bash
# deterministic checks only, writes nothing
.venv/bin/python lib/run.py --project focus_android --locale it --no-llm --dry-run \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n

# the real thing
.venv/bin/python lib/run.py --project focus_android --locale it \
    --l10n-dir ~/github/android-l10n --source-dir ~/github/android-l10n
```

## Verifying a change

```bash
.venv/bin/python focus_android/tools/selftest.py --l10n-dir ~/github/android-l10n
```

Focus has no deterministic defect in any covered locale today, so there is
nothing real to pin as a must-find. The suite pins what the split has to
keep true instead: only Focus files are checked, the context is Android
Components and nothing in Fenix, conventions match Firefox for Android's
for every locale tested, variants learn spelling rules from the shared
corpus, and the checks stay silent where Focus alone would have inferred a
convention from one character.
