# Firefox for iOS — l10n QA

- **Generated:** 2026-08-24
- **Locales tracked:** 19 (19 with recorded state)
- **Findings:** 1,239 raised, 17 fixed (1%), 1,177 open
- **Closed by a person:** 14 dismissed, 31 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (662)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **65** | 42 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **76** | 33 | 0 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-08-24 | incremental | `21033d5f` | 1,847 | 63 | **16** | 9 | 0 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-08-24 | incremental | `21033d5f` | 1,910 | 0 | **24** | 10 | 0 | 0 | 29 |
| [es-AR](es-AR/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **85** | 36 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,815 | 95 | **48** | 26 | 0 | 0 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,883 | 27 | **114** | 64 | 1 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **44** | 29 | 0 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,906 | 4 | **80** | 40 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,891 | 19 | **91** | 40 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **0** | 0 | 16 | 14 | 2 |
| [ja](ja/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **116** | 77 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **43** | 25 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **45** | 32 | 0 | 0 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **46** | 31 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,906 | 4 | **76** | 47 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **74** | 40 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,910 | 0 | **77** | 45 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-08-24 | incremental | `a2ecb0a8` | 1,835 | 75 | **57** | 36 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
