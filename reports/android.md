# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-08-20
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 114 raised, 33 resolved (28%), 75 open

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|
| [it](it/android.md) | 2026-08-20 | incremental | `afd16223` | 2,908 | 0 | **20** | 13 | 33 | 4 |
| [es-MX](es-MX/android.md) | 2026-08-20 | baseline | `afd16223` | 2,886 | 22 | **7** | 3 | 0 | 0 |
| [cs](cs/android.md) | 2026-08-20 | baseline | `afd16223` | 2,897 | 11 | **3** | 3 | 0 | 0 |
| [hu](hu/android.md) | 2026-08-20 | baseline | `afd16223` | 2,897 | 11 | **2** | 2 | 0 | 0 |
| [id](id/android.md) | 2026-08-20 | baseline | `afd16223` | 2,592 | 316 | **2** | 2 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **9** | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-08-20 | baseline | `afd16223` | 2,897 | 11 | **9** | 1 | 0 | 0 |
| [es-AR](es-AR/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **5** | 1 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-08-20 | baseline | `afd16223` | 2,834 | 74 | **5** | 1 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-08-20 | baseline | `afd16223` | 2,897 | 11 | **4** | 1 | 0 | 0 |
| [de](de/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **3** | 1 | 0 | 0 |
| [pl](pl/android.md) | 2026-08-20 | baseline | `afd16223` | 2,897 | 11 | **1** | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **1** | 1 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-08-20 | baseline | `afd16223` | 2,871 | 37 | **1** | 1 | 0 | 0 |
| [ru](ru/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **2** | 0 | 0 | 0 |
| [ja](ja/android.md) | 2026-08-20 | baseline | `afd16223` | 2,892 | 16 | **1** | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-08-20 | baseline | `afd16223` | 2,894 | 14 | **0** | 0 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **0** | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **0** | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-08-20 | baseline | `afd16223` | 2,908 | 0 | **0** | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
