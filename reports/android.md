# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-09-10
- **Locales tracked:** 21 (21 with recorded state)
- **Findings:** 2,744 raised, 53 fixed (1%), 2,383 open
- **Closed by a person:** 17 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (7)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`de`** `sync_send_tab_error_auth_remove_account` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "Remove account" is rendered as "Konto löschen" (delete account), which suggests deleting the account rather than disconnecting it.
    - Current: `Konto löschen`
    - Suggest: `Konto entfernen`
- **`hi-IN`** `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values/strings.xml`
    - "additional data collection" is rendered as "collect even more data", changing the meaning.
    - Current: `%1$s और भी डेटा को इकट्ठा करने का अनुरोध करता है`
    - Suggest: `%1$s अतिरिक्त डेटा संग्रह का अनुरोध करता है`
- **`hi-IN`** `download_language_file_dialog_message_all_languages` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "partial languages" is rendered as "आधी-अधूरी भाषाएं" (half-baked/incomplete languages), a pejorative claim about the product's language files.
    - Current: `कुछ आधी-अधूरी भाषाओं को आपके कैशे में डाउनलोड करते हैं`
    - Suggest: `भाषाओं के कुछ हिस्सों को आपके कैशे में डाउनलोड करते हैं`
- **`hi-IN`** `likert_scale_option_slow_or_buggy` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "It’s slow or buggy" translated as "It is very slow and has some bugs", changing "or" to "and" and adding intensifiers.
    - Current: `बहुत धीमा है और इसमें कुछ बग हैं`
    - Suggest: `यह धीमा है या इसमें बग हैं`
- **`hi-IN`** `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - Second sentence mistranslated: "Disable to manage font size here" became "unable to manage font size here".
    - Current: `यहां फ़ॉन्ट आकार प्रबंधित करने में अक्षम।`
    - Suggest: `यहां फ़ॉन्ट आकार प्रबंधित करने के लिए इसे बंद करें।`
- **`hi-IN`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - Translation adds a claim that the data is never sold, which the source does not contain, and mistranslates "that you use it" as "how you use it".
    - Current: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल कैसे करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें। इस डेटा को कभी बेचा नहीं जाता है।`
    - Suggest: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें।`
- **`sl`** `sync_send_tab_error_auth_remove_account` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "Remove account" is rendered as "Delete account", which implies destroying the Firefox account rather than disconnecting it from the device.
    - Current: `Izbriši račun`
    - Suggest: `Odstrani račun`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1305)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **130** | 76 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **107** | 62 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,717 | 29 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **121** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **123** | 55 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,691 | 55 | **155** | 83 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **78** | 56 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,717 | 29 | **165** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-09-10 | incremental | `72345b32` | 2,668 | 81 | **216** | 85 | 0 | 1 | 0 |
| [hu](hu/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,724 | 22 | **149** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,738 | 8 | **163** | 91 | 3 | 0 | 0 |
| [it](it/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **147** | 115 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,735 | 11 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **87** | 63 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,735 | 11 | **117** | 70 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **156** | 88 | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,738 | 8 | **118** | 66 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,746 | 0 | **142** | 79 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-09-07 | incremental | `b172b90d` | 2,718 | 28 | **145** | 100 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
