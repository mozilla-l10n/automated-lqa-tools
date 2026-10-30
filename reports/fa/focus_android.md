# Focus for Android l10n QA — fa

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 250 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for fa: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

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
| Files | 1 |
| Strings | 250 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 16 | **guillemet** |
| ellipsis | `char` 21 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (12)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Erase to delete cookies as well as search and browsing history" is mistranslated as "clear or delete cookies like search and browsing history".
    - Current: `کوکی‌ها را مانند جست‌وجو و تاریخچه مرور پاک یا حذف کنید`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `برای حذف کوکی‌ها و همچنین تاریخچهٔ جست‌وجو و مرور، پاک‌سازی کنید`
    - The source instructs the user to use Erase to delete cookies as well as search and browsing history; the target turns "as well as" into "like/such as" and "erase to delete" into "erase or delete", changing the meaning.
- `notification_erase_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Browsing history" rendered as "browser history" (تاریخچهٔ مرورگر) inconsistently with feedback_erase2.
    - Current: `پاک کردن تاریخچهٔ مرورگر`
    - Source: `Erase browsing history`
    - Suggest: `پاک کردن تاریخچهٔ مرور`
    - The source says browsing history; مرورگر means "browser". feedback_erase2 correctly uses تاریخچهٔ مرور.
- `preference_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Site Data" translated as "داده‌های پایگاه" (database/base data) instead of site data.
    - Current: `کوکی‌ها و داده‌های پایگاه`
    - Source: `Cookies and Site Data`
    - Suggest: `کوکی‌ها و داده‌های پایگاه‌وب`
    - "Site" is rendered elsewhere in this file as «سایت»; «پایگاه» alone means base/database, not website.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "potentially dangerous ... sites" rendered as "potential dangers", losing the noun "sites".
    - Current: `مسدود سازی خطرات بالقوه و سایت‌های فریبنده`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `مسدود کردن سایت‌های بالقوه خطرناک و فریبنده`
    - Source blocks sites that are potentially dangerous and deceptive, not "potential dangers".
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Shortcuts" (the feature, plural) is rendered as "this shortcut".
    - Current: `اگر این میانبر را اضافه کرده‌ اید`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `اگر میانبرهایی اضافه کرده‌اید`
    - The developer comment explains Shortcuts is a feature for pinning favorite websites; the source says "if you've added Shortcuts", not a specific single shortcut.
- `shortcut_erase_long_label` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "browsing history" rendered as "تاریخچهٔ مرورگر" (browser's history) instead of "تاریخچهٔ مرور".
    - Current: `پاک کردن تاریخچهٔ مرورگر`
    - Source: `Erase browsing history`
    - Suggest: `پاک کردن تاریخچهٔ مرور`
    - The source says browsing history, not the browser's history; "مرورگر" means browser.
- `text_selection_search_action_focus` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Brand name "Focus" transliterated as «فوکوس» despite the developer comment forbidding translation or transliteration.
    - Current: `جست‌و‌جو در فوکوس`
    - Source: `Search in Focus`
    - Suggest: `جست‌و‌جو در Focus`
    - Developer comment states: "Do not translate or transliterate Focus." The sibling strings keep "Focus Beta"/"Focus Nightly" in Latin script.

### C. Grammar, agreement & spelling

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "ماموریت ما تا رواج یک اینترنت سالم و باز است" is ungrammatical: "تا" should be a verbal noun construction.
    - Current: `ماموریت ما تا رواج یک اینترنت سالم و باز است`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `مأموریت ما ترویج اینترنتی سالم و باز است`
    - "تا" is not grammatical here; the sentence "Our mission is to foster a healthy, open Internet" needs a noun/infinitive phrase.
- `notification_action_erase_and_open` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Imperative verb form mixed with noun form: "حذف و باز کن" is inconsistent and ungrammatical as a notification action label.
    - Current: `حذف و باز کن`
    - Source: `Erase and Open`
    - Suggest: `پاک کردن و باز کردن`
    - The parallel action notification_action_open uses the verbal noun باز کردن; this string mixes a noun (حذف) with an imperative (باز کن).
- `onboarding_second_screen_subtitle_one` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Missing zero-width non-joiner in verb forms: "می بندید" and "می کنیم".
    - Current: `وقتی برنامه را می بندید، سابقه شما را پاک می کنیم`
    - Source: `We clear your history when you close the app for extra privacy.`
    - Suggest: `وقتی برنامه را می‌بندید، سابقهٔ شما را پاک می‌کنیم`
    - Persian prefix می must be joined with ZWNJ (می‌بندید, می‌کنیم), as done elsewhere in the batch.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Plural "these websites" rendered as singular "this site".
    - Current: `برای این سایت`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `برای این سایت‌ها`
    - Source says "for these websites" (plural); the translation uses the singular "این سایت".

### D. Terminology, register & consistency

- `onboarding_first_screen_privacy_notice_link_2` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Privacy Notice" is rendered as "privacy tips/points" instead of the legal document name.
    - Current: `نکات حفظ حریم خصوصی`
    - Source: `Privacy Notice`
    - Suggest: `اعلامیهٔ حریم خصوصی`
    - The link points to Mozilla's Privacy Notice, a legal notice; «نکات» means tips/points and misnames the document.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fa/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (18)

- `content_description_reload` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `content_description_stop` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `firstrun_shortcut_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `preference_autocomplete_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-12
- `download_firefox` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `notification_browsing_session_channel_name` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `preference_privacy_notice` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-07
- `custom_tab_copy_url_action` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-05
- `preference_exceptions` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-05
- `preference_remote_debugging` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-05
- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-05
- `text_selection_search_action_focus_beta` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — fixed 2026-10-05
