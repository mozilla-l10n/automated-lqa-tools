# Android l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,897 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for tr: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (9)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Yeniden dene” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Tekrar dene”
    - Current: `{ <p> }Tarayıcı şu an çevrimdışı kipte çalışıyor ve istenen öğeye bağlanamaz.{ </p> }{ <ul> }{ <li> }Cihazınız etkin bir ağa bağlı mı?{ </li> }{ <li> }Çevrimiçi kipe geçerek sayfayı tazelemek için “Yeniden dene” düğmesi…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Tekrar dene`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-tr/strings.xml` — `mozac_lib_send_crash_report_in_progress` uses a straight apostrophe
    - Current: `Çökme raporu %1$s'ya gönderiliyor`
    - Source: `Sending crash report to %1$s`
    - The tree uses ’ 156 times against 5 straight.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Ana menüden "Çık"ı seçtiğinizde gezinti verilerini otomatik olarak siler`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `ip_protection_onboarding_body_promo` uses a straight apostrophe
    - Current: `Gezintinizi daha gizli ve izlemesi zor hale getirmek için VPN'i açın. %1$s tarihine kadar sınırsız bant genişliğine sahip olmak için hemen deneyin. %2$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - The tree uses ’ 156 times against 5 straight.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `Web adresi "https://" veya "http://" içermelidir`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `external_app_prompt` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt` uses a straight apostrophe
    - Current: `Bu bağlantıyı %2$s ile açmak için %1$s'tan çıkabilirsiniz.`
    - Source: `You can leave %1$s to open this link in %2$s.`
    - The tree uses ’ 156 times against 5 straight.
- `external_app_prompt_no_app` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt_no_app` uses a straight apostrophe
    - Current: `Cihazınızdaki uygulamalar bu bağlantıyı açamıyor. %2$s mağazasında uygun bir uygulama aramak için %1$s'tan çıkabilirsiniz.`
    - Source: `None of the apps on your device are able to open this link. You can leave %1$s to search %2$s for an app that can.`
    - The tree uses ’ 156 times against 5 straight.
- `external_multiple_apps_matched_exit` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_multiple_apps_matched_exit` uses a straight apostrophe
    - Current: `Gizli Gezinti'den çıkılsın mı?`
    - Source: `Exit Private Browsing?`
    - The tree uses ’ 156 times against 5 straight.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `%1$s’ta sevdiğiniz sitelere çabucak ulaşabilirsiniz. %1$s menüsünden "Ana ekrana ekle"yi seçmeniz yeterli.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - The locale's quote convention is `curly-double` (14 occurrences).

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
| Strings | 2,897 |
| Missing strings | 11 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 8 |

### Completeness

**11 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — 11

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 14, `straight-double` 3 | **curly-double** |
| apostrophe | `typographic` 156, `straight` 5 | **typographic** |
| ellipsis | `char` 21 | **char** |
| register | `informal` 2, `formal` 16 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Yeniden dene” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Tekrar dene”
    - Current: `{ <p> }Tarayıcı şu an çevrimdışı kipte çalışıyor ve istenen öğeye bağlanamaz.{ </p> }{ <ul> }{ <li> }Cihazınız etkin bir ağa bağlı mı?{ </li> }{ <li> }Çevrimiçi kipe geçerek sayfayı tazelemek için “Yeniden dene” düğmesi…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Tekrar dene`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-tr/strings.xml` — `mozac_lib_send_crash_report_in_progress` uses a straight apostrophe
    - Current: `Çökme raporu %1$s'ya gönderiliyor`
    - Source: `Sending crash report to %1$s`
    - The tree uses ’ 156 times against 5 straight.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `Web adresi "https://" veya "http://" içermelidir`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `ip_protection_onboarding_body_promo` uses a straight apostrophe
    - Current: `Gezintinizi daha gizli ve izlemesi zor hale getirmek için VPN'i açın. %1$s tarihine kadar sınırsız bant genişliğine sahip olmak için hemen deneyin. %2$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - The tree uses ’ 156 times against 5 straight.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Ana menüden "Çık"ı seçtiğinizde gezinti verilerini otomatik olarak siler`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `external_app_prompt` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt` uses a straight apostrophe
    - Current: `Bu bağlantıyı %2$s ile açmak için %1$s'tan çıkabilirsiniz.`
    - Source: `You can leave %1$s to open this link in %2$s.`
    - The tree uses ’ 156 times against 5 straight.
- `external_app_prompt_no_app` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt_no_app` uses a straight apostrophe
    - Current: `Cihazınızdaki uygulamalar bu bağlantıyı açamıyor. %2$s mağazasında uygun bir uygulama aramak için %1$s'tan çıkabilirsiniz.`
    - Source: `None of the apps on your device are able to open this link. You can leave %1$s to search %2$s for an app that can.`
    - The tree uses ’ 156 times against 5 straight.
- `external_multiple_apps_matched_exit` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_multiple_apps_matched_exit` uses a straight apostrophe
    - Current: `Gizli Gezinti'den çıkılsın mı?`
    - Source: `Exit Private Browsing?`
    - The tree uses ’ 156 times against 5 straight.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `%1$s’ta sevdiğiniz sitelere çabucak ulaşabilirsiniz. %1$s menüsünden "Ana ekrana ekle"yi seçmeniz yeterli.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - The locale's quote convention is `curly-double` (14 occurrences).

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
