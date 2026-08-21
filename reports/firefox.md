# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-21
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,780 raised, 1,411 fixed (24%), 4,321 open
- **Closed by a person:** 15 dismissed, 3 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,161 | 19 | **258** | 174 | 0 | 0 | 0 |
| [de](de/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,161 | 19 | **48** | 23 | 35 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,131 | 49 | **1** | 0 | 13 | 0 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,161 | 19 | **32** | 19 | 6 | 0 | 0 |
| [es-AR](es-AR/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,129 | 51 | **420** | 239 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 17,184 | 996 | **101** | 43 | 39 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 17,843 | 337 | **132** | 53 | 93 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,348 | 19 | **37** | 9 | 31 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,131 | 49 | **588** | 177 | 245 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,116 | 64 | **273** | 153 | 0 | 0 | 0 |
| [id](id/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 15,488 | 2,692 | **329** | 257 | 0 | 0 | 0 |
| [it](it/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,360 | 7 | **0** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,127 | 53 | **178** | 69 | 189 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,156 | 24 | **377** | 149 | 115 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 17,866 | 314 | **83** | 50 | 127 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,127 | 53 | **565** | 207 | 131 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,161 | 19 | **593** | 315 | 172 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 17,533 | 647 | **35** | 5 | 42 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 18,001 | 179 | **199** | 71 | 91 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-21 | incremental | `bd0ff4b2` | 17,969 | 211 | **72** | 18 | 26 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
