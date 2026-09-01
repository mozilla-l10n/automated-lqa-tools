# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-09-01
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 2,513 raised, 50 fixed (1%), 2,158 open
- **Closed by a person:** 14 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (1)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`ru`** `mozac_summarize_paywalled_content_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values/strings.xml`
    - The error title no longer says summarization is impossible; it instead asserts that the full content is paid-only.
    - Current: `Полное содержимое доступно только платно`
    - Suggest: `Не удалось создать резюме содержимого за платной подпиской`

### Broken output — impact 1 (2)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`cs` 2

- **`cs`** `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - `create_collection_save_to_collection_tab_selected` has placeholders none where the source has %1$d
    - Current: `Vybrán jeden panel`
- **`cs`** `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - `recently_closed_tab` has placeholders none where the source has %1$d
    - Current: `Jeden panel`

### Wrong content — impact 2 (1213)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **132** | 78 | 0 | 0 | 0 |
| [de](de/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **106** | 61 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,717 | 18 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **121** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **123** | 55 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,691 | 44 | **155** | 83 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **78** | 56 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,717 | 18 | **165** | 59 | 0 | 0 | 0 |
| [hu](hu/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,724 | 11 | **149** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,586 | 149 | **160** | 91 | 1 | 0 | 0 |
| [it](it/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,717 | 18 | **144** | 112 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,717 | 18 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,717 | 18 | **86** | 62 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **117** | 70 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,724 | 11 | **157** | 89 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,719 | 16 | **116** | 65 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,735 | 0 | **140** | 77 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-09-01 | incremental | `f39118d7` | 2,713 | 22 | **145** | 100 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
