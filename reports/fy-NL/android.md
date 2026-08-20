# Android l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for fy-NL: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (9)

- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `search_suggestions_onboarding_text` has placeholders %1$s where the source has %s
  - Current: `%1$s sil alles wat jo yn de adresbalke yntype mei jo standert sykmasine diele.`
  - Source: `%s will share everything you type in the address bar with your default search engine.`
  - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `tab_tray_inactive_auto_close_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `tab_tray_inactive_auto_close_body_2` uses a straight apostrophe
  - Current: `%1$s kin ljepblêden dy't jo de ôfrûne moanne net besjoen hawwe slute.`
  - Source: `%1$s can close tabs you haven’t viewed over the past month.`
  - The tree uses ’ 101 times against 8 straight.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `onboarding_marketing_redesign_opt_out_checkbox` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `onboarding_marketing_body_1` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `nova_onboarding_marketing_body_2` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `preferences_marketing_data_description_4` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke.`
  - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
  - The tree uses ’ 101 times against 8 straight.
- `download_content_type_filter_video` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `download_content_type_filter_video` uses a straight apostrophe
  - Current: `Fideo's`
  - Source: `Videos`
  - The tree uses ’ 101 times against 8 straight.
- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `etp_known_fingerprinters_description` uses a straight apostrophe
  - Current: `Foarkomt dat unyk identifisearbere gegevens oer jo apparaat sammele wurde dy't brûkt wurde kinne foar folchdoeleinen.`
  - Source: `Stops uniquely identifiable data from being collected about your device that can be used for tracking purposes.`
  - The tree uses ’ 101 times against 8 straight.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `uninstall_survey_option_4_v2` uses a straight apostrophe
  - Current: `Fideo's, downloads of media wurken net`
  - Source: `Videos, downloads, or media didn’t work`
  - The tree uses ’ 101 times against 8 straight.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 43 |
| Strings | 2,908 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 8 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 17 | **curly-single** |
| apostrophe | `typographic` 101, `straight` 8 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 7 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `search_suggestions_onboarding_text` has placeholders %1$s where the source has %s
  - Current: `%1$s sil alles wat jo yn de adresbalke yntype mei jo standert sykmasine diele.`
  - Source: `%s will share everything you type in the address bar with your default search engine.`
  - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `download_content_type_filter_video` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `download_content_type_filter_video` uses a straight apostrophe
  - Current: `Fideo's`
  - Source: `Videos`
  - The tree uses ’ 101 times against 8 straight.
- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `etp_known_fingerprinters_description` uses a straight apostrophe
  - Current: `Foarkomt dat unyk identifisearbere gegevens oer jo apparaat sammele wurde dy't brûkt wurde kinne foar folchdoeleinen.`
  - Source: `Stops uniquely identifiable data from being collected about your device that can be used for tracking purposes.`
  - The tree uses ’ 101 times against 8 straight.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `nova_onboarding_marketing_body_2` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `onboarding_marketing_body_1` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `onboarding_marketing_redesign_opt_out_checkbox` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
  - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
  - The tree uses ’ 101 times against 8 straight.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `preferences_marketing_data_description_4` uses a straight apostrophe
  - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke.`
  - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
  - The tree uses ’ 101 times against 8 straight.
- `tab_tray_inactive_auto_close_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `tab_tray_inactive_auto_close_body_2` uses a straight apostrophe
  - Current: `%1$s kin ljepblêden dy't jo de ôfrûne moanne net besjoen hawwe slute.`
  - Source: `%1$s can close tabs you haven’t viewed over the past month.`
  - The tree uses ’ 101 times against 8 straight.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `uninstall_survey_option_4_v2` uses a straight apostrophe
  - Current: `Fideo's, downloads of media wurken net`
  - Source: `Videos, downloads, or media didn’t work`
  - The tree uses ’ 101 times against 8 straight.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
