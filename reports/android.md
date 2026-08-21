# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 2,487 raised, 75 resolved (3%), 2,395 open
- **Closed by a person:** 11 dismissed, 4 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,908 | 3 | **147** | 85 | 0 | 0 | 0 |
| [de](de/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,911 | 0 | **117** | 67 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,894 | 17 | **1** | 0 | 0 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **68** | 7 | 0 | 0 | 0 |
| [es-AR](es-AR/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,911 | 0 | **138** | 47 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,834 | 77 | **133** | 62 | 0 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,886 | 25 | **177** | 95 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,911 | 0 | **80** | 57 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **167** | 60 | 9 | 0 | 0 |
| [hu](hu/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,897 | 14 | **163** | 85 | 2 | 0 | 0 |
| [id](id/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,592 | 319 | **164** | 95 | 2 | 0 | 0 |
| [it](it/android.md) | 2026-08-21 | incremental | `7134a6c7` | 2,911 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **160** | 124 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **68** | 36 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **93** | 67 | 1 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,897 | 14 | **119** | 74 | 4 | 0 | 0 |
| [ru](ru/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **167** | 100 | 2 | 0 | 0 |
| [sl](sl/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,908 | 3 | **128** | 71 | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,897 | 14 | **146** | 83 | 9 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-08-21 | baseline | `7134a6c7` | 2,871 | 40 | **159** | 106 | 1 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
