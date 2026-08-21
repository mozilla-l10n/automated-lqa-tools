# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,778 raised, 1,408 resolved (24%), 4,322 open
- **Closed by a person:** 15 dismissed, 3 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,141 | 32 | **257** | 174 | 0 | 0 | 0 |
| [de](de/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,161 | 12 | **48** | 23 | 35 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,115 | 58 | **4** | 2 | 10 | 0 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,161 | 12 | **32** | 19 | 6 | 0 | 0 |
| [es-AR](es-AR/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,129 | 44 | **420** | 239 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 17,184 | 989 | **101** | 43 | 39 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 17,843 | 330 | **132** | 53 | 93 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,348 | 12 | **37** | 9 | 31 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,131 | 42 | **588** | 177 | 245 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,116 | 57 | **273** | 153 | 0 | 0 | 0 |
| [id](id/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 15,485 | 2,688 | **328** | 256 | 0 | 0 | 0 |
| [it](it/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,360 | 0 | **0** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,127 | 46 | **178** | 69 | 189 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,156 | 17 | **377** | 149 | 115 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 17,866 | 307 | **83** | 50 | 127 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,127 | 46 | **565** | 207 | 131 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,161 | 12 | **593** | 315 | 172 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 17,533 | 640 | **35** | 5 | 42 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 18,001 | 172 | **199** | 71 | 91 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-21 | incremental | `f2e9b7fc` | 17,969 | 204 | **72** | 18 | 26 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
