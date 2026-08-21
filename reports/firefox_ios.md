# Firefox for iOS — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 20 (19 with recorded state)
- **Findings:** 1,239 raised, 16 resolved (1%), 1,207 open
- **Closed by a person:** 14 dismissed, 2 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,910 | 0 | **65** | 42 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,910 | 0 | **76** | 33 | 0 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,847 | 63 | **16** | 9 | 0 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,910 | 0 | **53** | 13 | 0 | 0 | 0 |
| [es-AR](es-AR/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,910 | 0 | **85** | 36 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,815 | 95 | **48** | 26 | 0 | 0 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,883 | 27 | **115** | 65 | 0 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,909 | 1 | **44** | 29 | 0 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,906 | 4 | **80** | 40 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,891 | 19 | **91** | 40 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-08-21 | incremental | `7e1ae616` | 1,910 | 0 | **0** | 0 | 16 | 14 | 2 |
| [ja](ja/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,910 | 0 | **116** | 77 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,906 | 4 | **43** | 25 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,910 | 0 | **45** | 32 | 0 | 0 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,906 | 4 | **46** | 31 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,906 | 4 | **76** | 47 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,910 | 0 | **74** | 40 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,910 | 0 | **77** | 45 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-08-21 | baseline | `7e1ae616` | 1,835 | 75 | **57** | 36 | 0 | 0 | 0 |
| fy-NL | — | — | — | — | — | — | — | — | — | _not yet checked_ |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
