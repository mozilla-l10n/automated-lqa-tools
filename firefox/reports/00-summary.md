# Firefox l10n QA — all locales

- **Generated:** 2026-08-20
- **Locales tracked:** 14 (14 with recorded state)
- **Findings:** 4,408 raised, 1,382 resolved (31%), 3,023 open

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|
| [ru](ru.md) | 2026-08-20 | incremental | `d411ef04` | 18,161 | 2 | **591** | 313 | 172 | 0 |
| [pt-BR](pt-BR.md) | 2026-08-20 | incremental | `d411ef04` | 18,127 | 36 | **570** | 206 | 131 | 0 |
| [fy-NL](fy-NL.md) | 2026-08-20 | incremental | `d411ef04` | 18,131 | 32 | **594** | 178 | 244 | 0 |
| [nl](nl.md) | 2026-08-20 | incremental | `d411ef04` | 18,148 | 15 | **400** | 160 | 115 | 0 |
| [ja](ja.md) | 2026-08-20 | incremental | `d411ef04` | 18,127 | 36 | **176** | 68 | 191 | 0 |
| [tr](tr.md) | 2026-08-20 | incremental | `d411ef04` | 18,001 | 162 | **194** | 66 | 91 | 0 |
| [es-MX](es-MX.md) | 2026-08-20 | incremental | `d411ef04` | 17,843 | 320 | **132** | 49 | 89 | 0 |
| [pl](pl.md) | 2026-08-20 | incremental | `d411ef04` | 17,836 | 327 | **82** | 46 | 125 | 0 |
| [es-ES](es-ES.md) | 2026-08-20 | incremental | `d411ef04` | 17,184 | 979 | **98** | 40 | 39 | 0 |
| [zh-CN](zh-CN.md) | 2026-08-20 | incremental | `d411ef04` | 17,969 | 194 | **72** | 18 | 26 | 0 |
| [de](de.md) | 2026-08-20 | incremental | `d411ef04` | 18,131 | 32 | **40** | 16 | 35 | 0 |
| [fr](fr.md) | 2026-08-20 | incremental | `d411ef04` | 18,348 | 2 | **37** | 9 | 31 | 0 |
| [sl](sl.md) | 2026-08-20 | incremental | `d411ef04` | 17,521 | 642 | **32** | 2 | 42 | 1 |
| [it](it.md) | 2026-08-20 | incremental | `d411ef04` | 18,350 | 0 | **5** | 0 | 51 | 2 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
