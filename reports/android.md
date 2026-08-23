# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-08-23
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 2,490 raised, 47 fixed (1%), 2,426 open
- **Closed by a person:** 11 dismissed, 4 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (9)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`cs` 2 · `de` 1 · `fy-NL` 1 · `id` 1 · `ja` 1 · `pl` 1 · `sl` 1 · `zh-CN` 1

- **`cs`** `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `create_collection_save_to_collection_tab_selected` has placeholders none where the source has %d
  - Current: `Vybrán jeden panel`
- **`cs`** `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `recently_closed_tab` has placeholders none where the source has %d
  - Current: `Jeden panel`
- **`de`** `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values/strings.xml`
  - `mozac_feature_sitepermissions_storage_access_message` has placeholders %1$s where the source has %s
  - Current: `Möglicherweise möchten Sie den Zugriff blockieren, wenn nicht klar ist, warum %1$s diese Daten benötigt.`
- **`fy-NL`** `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `search_suggestions_onboarding_text` has placeholders %1$s where the source has %s
  - Current: `%1$s sil alles wat jo yn de adresbalke yntype mei jo standert sykmasine diele.`
- **`id`** `preferences_delete_browsing_data_cookies_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - Stray escaped backslash-space after "Anda" in the translation.
  - Current: `Anda\ akan keluar`
  - Suggest: `Anda akan keluar`
- **`ja`** `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
  - Markup tags are misplaced: text falls outside the { <li> } elements and the second bullet drops the "forward slashes" instruction.
  - Current: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> }{ </li> } のようなものになります。 { <li> }スラッシュ ({ <strong> }/{ </strong> }) { </li> }が使われているか確認してください。`
  - Suggest: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> } のようなものになります。{ </li> } { <li> }スラッシュ ({ <strong> }/{ </strong> }) が使われているか確認してください。{ </li> }`
- **`pl`** `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
  - `firstrun_shortcut_text` has placeholders %1$s where the source has %1$s, %1$s
  - Current: `Szybko wracaj do ulubionych stron w %1$s. Po prostu wybierz „Dodaj do ekranu głównego” z menu.`
- **`sl`** `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
  - `onboarding_first_screen_title` has placeholders %s where the source has %1$s
  - Current: `Dobrodošli v %su`
  - Suggest: `Dobrodošli v %1$su`
- **`zh-CN`** `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
  - `downloads_delete_dialog_title` has placeholders %d where the source has none
  - Current: `{$quantity ->} [other] 删除 %d 个文件？`

### Wrong content — impact 2 (1321)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **147** | 85 | 0 | 0 | 0 |
| [de](de/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **117** | 67 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,894 | 17 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **68** | 7 | 0 | 0 | 0 |
| [es-AR](es-AR/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **138** | 47 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,834 | 77 | **133** | 62 | 0 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,886 | 25 | **177** | 95 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **80** | 57 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **176** | 61 | 0 | 0 | 0 |
| [hu](hu/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,897 | 14 | **165** | 87 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,592 | 319 | **166** | 97 | 0 | 0 | 0 |
| [it](it/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **161** | 124 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **68** | 36 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **94** | 68 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,897 | 14 | **123** | 75 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **169** | 100 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,908 | 3 | **129** | 72 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,911 | 0 | **155** | 83 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-08-22 | incremental | `eda9938a` | 2,873 | 38 | **160** | 107 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
