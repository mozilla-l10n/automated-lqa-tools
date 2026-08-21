# Firefox for iOS — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 1 (1 with recorded state)
- **Findings:** 0 raised, 0 resolved (—), 0 open

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|
| [it](it/firefox_ios.md) | 2026-08-21 | baseline | `6b4ba8b9` | 1,894 | 0 | **0** | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
