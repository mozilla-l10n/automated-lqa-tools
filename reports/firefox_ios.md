# Firefox for iOS — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 1 (1 with recorded state)
- **Findings:** 32 raised, 16 resolved (50%), 0 open
- **Closed by a person:** 14 dismissed, 2 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [it](it/firefox_ios.md) | 2026-08-21 | incremental | `8ec9ec78` | 1,910 | 0 | **0** | 0 | 16 | 14 | 2 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
