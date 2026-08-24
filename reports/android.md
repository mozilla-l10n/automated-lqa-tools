# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-08-24
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 2,492 raised, 48 fixed (1%), 2,422 open
- **Closed by a person:** 11 dismissed, 4 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (3)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`cs` 2 · `ja` 1

- **`cs`** `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `create_collection_save_to_collection_tab_selected` has placeholders none where the source has %1$d
  - Current: `Vybrán jeden panel`
- **`cs`** `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `recently_closed_tab` has placeholders none where the source has %1$d
  - Current: `Jeden panel`
- **`ja`** `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
  - Markup tags are misplaced: text falls outside the { <li> } elements and the second bullet drops the "forward slashes" instruction.
  - Current: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> }{ </li> } のようなものになります。 { <li> }スラッシュ ({ <strong> }/{ </strong> }) { </li> }が使われているか確認してください。`
  - Suggest: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> } のようなものになります。{ </li> } { <li> }スラッシュ ({ <strong> }/{ </strong> }) が使われているか確認してください。{ </li> }`

### Wrong content — impact 2 (1321)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **147** | 85 | 0 | 0 | 0 |
| [de](de/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **116** | 66 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,894 | 17 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **68** | 7 | 0 | 0 | 0 |
| [es-AR](es-AR/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **138** | 47 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,834 | 77 | **133** | 62 | 0 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,886 | 25 | **177** | 95 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **80** | 57 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **175** | 60 | 0 | 0 | 0 |
| [hu](hu/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,897 | 14 | **165** | 87 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,592 | 319 | **165** | 96 | 1 | 0 | 0 |
| [it](it/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **161** | 124 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **68** | 36 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **93** | 67 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **125** | 75 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,908 | 3 | **169** | 100 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,908 | 3 | **128** | 71 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,911 | 0 | **155** | 83 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-08-24 | incremental | `e8622a90` | 2,873 | 38 | **159** | 106 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
