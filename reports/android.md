# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-09-15
- **Locales tracked:** 21 (21 with recorded state)
- **Findings:** 2,774 raised, 235 fixed (8%), 2,218 open
- **Closed by a person:** 17 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1245)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **130** | 76 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **105** | 60 | 1 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **121** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,687 | 59 | **152** | 82 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **77** | 55 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,713 | 33 | **165** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-09-15 | incremental | `655dd75b` | 2,665 | 82 | **65** | 35 | 179 | 1 | 0 |
| [hu](hu/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,738 | 8 | **161** | 90 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **148** | 116 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,732 | 14 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,742 | 4 | **87** | 63 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **117** | 70 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **156** | 88 | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,737 | 9 | **117** | 65 | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,746 | 0 | **140** | 77 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-09-14 | incremental | `6e23dc94` | 2,742 | 4 | **145** | 100 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
