# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-20
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,772 raised, 1,395 resolved (24%), 4,345 open

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|
| [ru](ru/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,161 | 2 | **593** | 315 | 172 | 0 |
| [id](id/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 15,475 | 2,688 | **328** | 256 | 0 | 0 |
| [es-AR](es-AR/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,128 | 35 | **420** | 239 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,127 | 36 | **570** | 207 | 131 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,131 | 32 | **593** | 177 | 244 | 0 |
| [cs](cs/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,131 | 32 | **257** | 174 | 0 | 0 |
| [hu](hu/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,116 | 47 | **273** | 153 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,156 | 7 | **377** | 149 | 115 | 0 |
| [tr](tr/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,001 | 162 | **199** | 71 | 91 | 0 |
| [ja](ja/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,127 | 36 | **177** | 69 | 191 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 17,843 | 320 | **136** | 53 | 89 | 0 |
| [pl](pl/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 17,836 | 327 | **84** | 49 | 125 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 17,184 | 979 | **101** | 43 | 39 | 0 |
| [de](de/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,161 | 2 | **47** | 23 | 35 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,161 | 2 | **33** | 21 | 4 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 17,969 | 194 | **72** | 18 | 26 | 0 |
| [fr](fr/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,348 | 2 | **37** | 9 | 31 | 0 |
| [sl](sl/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 17,533 | 630 | **35** | 5 | 42 | 1 |
| [it](it/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,350 | 0 | **9** | 4 | 51 | 2 |
| [en-CA](en-CA/firefox.md) | 2026-08-20 | incremental | `fef20cd7` | 18,115 | 48 | **4** | 2 | 9 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
