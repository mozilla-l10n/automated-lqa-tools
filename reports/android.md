# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-09-10
- **Locales tracked:** 21 (21 with recorded state)
- **Findings:** 2,759 raised, 107 fixed (3%), 2,344 open
- **Closed by a person:** 17 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (3)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`hi-IN`** `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values/strings.xml`
    - "additional data collection" is rendered as "collect even more data", changing the meaning.
    - Current: `%1$s और भी डेटा को इकट्ठा करने का अनुरोध करता है`
    - Suggest: `%1$s अतिरिक्त डेटा संग्रह का अनुरोध करता है`
- **`hi-IN`** `likert_scale_option_slow_or_buggy` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "It’s slow or buggy" translated as "It is very slow and has some bugs", changing "or" to "and" and adding intensifiers.
    - Current: `बहुत धीमा है और इसमें कुछ बग हैं`
    - Suggest: `यह धीमा है या इसमें बग हैं`
- **`hi-IN`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - Translation adds a claim that the data is never sold, which the source does not contain, and mistranslates "that you use it" as "how you use it".
    - Current: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल कैसे करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें। इस डेटा को कभी बेचा नहीं जाता है।`
    - Suggest: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें।`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1292)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **130** | 76 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **106** | 61 | 1 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,717 | 32 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **121** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **123** | 55 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,691 | 58 | **155** | 83 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **78** | 56 | 0 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,717 | 32 | **165** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,668 | 81 | **179** | 74 | 52 | 1 | 0 |
| [hu](hu/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **149** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,741 | 8 | **163** | 91 | 3 | 0 | 0 |
| [it](it/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **0** | 0 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **147** | 115 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,735 | 14 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **87** | 63 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,749 | 0 | **117** | 70 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **156** | 88 | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,738 | 11 | **117** | 65 | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **142** | 79 | 3 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-09-10 | incremental | `6bf5ed95` | 2,746 | 3 | **145** | 100 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
