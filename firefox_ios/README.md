# Firefox for iOS l10n QA

Localization quality review for **Firefox for iOS**.

| | |
|---|---|
| Repository | [`mozilla-l10n/firefoxios-l10n`](https://github.com/mozilla-l10n/firefoxios-l10n) |
| Format | XLIFF 1.2 — one `<locale>/firefox-ios.xliff` per locale |
| Source | `en-US/firefox-ios.xliff` (the reference locale) |
| Locales checked | listed in [`config.yaml`](config.yaml) |
| Workflow | **Actions → Firefox iOS l10n QA** |

Results arrive as a pull request on `l10n-qa/firefox_ios`, separate from the
Firefox desktop and Android ones so no team reads another's findings.

Start at [`../reports/firefox_ios.md`](../reports/firefox_ios.md), then the
per-locale report at `../reports/<locale>/firefox_ios.md`, which sits beside
that locale's reports for the other projects.

## How this differs from the other projects

Everything format-agnostic is shared, in [`../lib/`](../lib/).

**Source and translation live in the same element.** An XLIFF trans-unit
carries `<source>` and `<target>` together, so there is no second tree to
walk — one parse fills both sides of the comparison. `lib/layout.py` has an
`xliff` loader for this.

Two details that matter and are easy to get wrong:

- The reference is `en-US/firefox-ios.xliff`, **not** the `<source>` sitting
  next to each target. Upstream only rewrites a locale's `<source>` in one
  of its three matching modes, so it can lag behind the English; taking the
  reference from its own file is what lets the pipeline notice that the
  source moved under a translation nobody updated.
- An untranslated unit is **present but empty** — `<target>` absent, so
  moz.l10n returns an empty pattern rather than no entry. The loader drops
  those so completeness counts them. `bo` is 47 translated of 1,894, and the
  self-test pins that number.

**Strings are keyed by their originating `.strings` file.** A trans-unit id
is only unique within its `<file original="...">` group, so the group is part
of the key — and it is the most useful thing to show a reviewer, since a
group is roughly one screen.

**A from-scratch review batches through the API.** A locale is a single
684 KB file holding all 1,894 units; source and target together are more
than one agent can read, and no partition helps because every group is in
that same file. `--baseline-strategy agent` is refused for this project
rather than silently handing an agent something it cannot read.

## What is deliberately not checked

Each decision was taken against the repository, not assumed:

| Not run | Why |
|---|---|
| `plurals`, `selectors`, `variables` | there is no plural mechanism at all — no `.stringsdict`, no plural trans-units, not one `SelectMessage` in 1,894 units |
| `markup` | zero HTML-ish tags in those same 1,894 strings |
| `escaping`, `term_params`, `accesskey` | Android and Fluent concepts; XLIFF escaping is XML escaping and the parser owns it |

A check that cannot fire reads as coverage and is only noise waiting to
happen.

What is left is `placeholders`, `ui_references`, `typography` and
`variant_spelling`. Placeholders are the main mechanical risk here: iOS
formats through printf, `%@` is unnumbered and cannot be reordered, and a
type mismatch is a crash rather than a rendering bug.

## Running it

From the repository root:

```bash
# deterministic checks only, writes nothing
.venv/bin/python lib/run.py --project firefox_ios --locale it --no-llm --dry-run \
    --l10n-dir ~/github/firefoxios-l10n --source-dir ~/github/firefoxios-l10n

# the real thing
export ANTHROPIC_API_KEY=...
.venv/bin/python lib/run.py --project firefox_ios --locale it \
    --l10n-dir ~/github/firefoxios-l10n --source-dir ~/github/firefoxios-l10n
```

Both `--dir` flags are the same path: the repository is its own reference.
They are used exactly as they are on disk, so pull first.

## Verifying a change

```bash
.venv/bin/python firefox_ios/tools/selftest.py --l10n-dir ~/github/firefoxios-l10n
```

28 assertions: the XLIFF layout resolves both sides from one file, the
source really is the reference rather than the target's own copy, an empty
target counts as untranslated, `%@` parses, and the checks catch placeholder
defects that exist in the repository today — `dsb` has `%%3$@$s`, where the
doubled percent escapes to a literal so the third link never renders, and
`oc` has `%S` where the source passes an integer.
