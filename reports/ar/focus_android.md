# Focus for Android l10n QA — ar

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 249 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for ar: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Strings | 249 |
| Missing strings | 1 |
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

**1 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 14, `curly-double` 3, `guillemet` 2 | **straight-double** |
| ellipsis | `char` 20 | **char** |
| dash | `em` 1 | **em** |
| nbsp | `total` 1 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (17)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 6 |
| 3 | Degraded language (grammar, spelling, terminology) | 8 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `cfr_for_toolbar_delete_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "start fresh" is translated literally as "start with a refreshment".
    - Current: `وابدأ بانتعاشة`
    - Source: `Tap here to trash it all — history, cookies, everything — and start fresh on a new tab.`
    - Suggest: `وابدأ من جديد`
    - "Start fresh" is an idiom for starting over. "بانتعاشة" (with a refreshment/freshness) does not convey that meaning.
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "press back" is translated as pressing the delete button.
    - Current: `زر الحذف`
    - Source: `Drag from top & press back to exit`
    - Suggest: `زر الرجوع`
    - The source tells the user to press the back button to exit fullscreen. "زر الحذف" means "delete button", so the instruction is wrong.
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "Your favorite URLs" is rendered as "URLs in Favorites", which suggests bookmarks rather than the user-defined autocomplete list.
    - Current: `المسارات في المفضّلة`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `مساراتك المفضّلة`
    - The source means the user's own custom list of preferred URLs. "في المفضّلة" names the Favorites/bookmarks feature, which is a different data source.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — Brand name Mozilla is transliterated into Arabic script.
    - Current: `تحاول موزيلا`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `تحاول Mozilla`
    - Mozilla is a brand that stays untranslated; other strings in the same file keep it in Latin script.
- `preference_privacy_and_security_header` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "Security" is rendered as "السريّة" (confidentiality) instead of "الأمان".
    - Current: `الخصوصية والسريّة`
    - Source: `Privacy & Security`
    - Suggest: `الخصوصية والأمان`
    - السريّة means secrecy/confidentiality; security is الأمان, as used elsewhere in this batch (preference_https_only_summary3).
- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "Deceptive" is translated as "ضارة" (harmful), so deceptive sites are no longer mentioned.
    - Current: `بأنها ضارة أو هجومية`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `بأنها خدّاعة أو هجومية`
    - The source lists "deceptive and attack sites". The title string uses "خدّاعة" for "deceptive", but the summary uses "ضارة" (harmful), which is a different idea and repeats the later "ما هو ضار".
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "الذي فضّله" (that he preferred) uses the wrong person and changes "your search engine" into the engine Focus preferred.
    - Current: `الذي فضّله`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `الذي فضّلته`
    - The source says "your search engine", meaning the one the user picked. The masculine third-person verb points back to %1$s (the app), so the sentence says the app picked the engine.

### C. Grammar, agreement & spelling

- `notification_action_erase_and_open` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — The conjunction و is written as a separate word.
    - Current: `امسح و افتح`
    - Source: `Erase and Open`
    - Suggest: `امسح وافتح`
    - In Arabic orthography the conjunction و attaches to the following word.
- `notification_browsing_session_channel_name` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — The phrase breaks noun–adjective agreement: "تصفح" has no article but the adjective "الخاص" does.
    - Current: `جلسة تصفح الخاص`
    - Source: `Private browsing session`
    - Suggest: `جلسة التصفح الخاص`
    - "Private browsing" needs the definite noun to match the definite adjective; "تصفح الخاص" is ungrammatical.
- `onboarding_second_screen_subtitle_two` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — Imperative verb misspelled with hamzat qat', turning "Make" into "I make".
    - Current: `أجعل`
    - Source: `Make %1$s your default to protect your data with every link you open.`
    - Suggest: `اجعل`
    - The source is an imperative ("Make %1$s your default"); the imperative of جعل takes hamzat wasl (اجعل), while أجعل is first-person present.
- `preference_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — The conjunction و is written as a separate word instead of attached to the following word.
    - Current: `الكعكات و بيانات المواقع`
    - Source: `Cookies and Site Data`
    - Suggest: `الكعكات وبيانات المواقع`
    - In Arabic orthography the conjunction و must be joined to the next word; a space after it is a spelling error.
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "تتحمّل" means "endure/bear", not "load".
    - Current: `قد تتحمّل الصفحات`
    - Source: `Pages may load faster, but may also behave unexpectedly`
    - Suggest: `قد تُحمَّل الصفحات`
    - Source says pages may load faster; the verb for loading is the passive تُحمَّل, while تتحمّل means to bear or withstand.

### D. Terminology, register & consistency

- `cfr_for_toolbar_delete_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "history" is rendered as "التاريخ" (usually "date"), unlike "تأريخ" in the other strings.
    - Current: `التاريخ وملفات`
    - Source: `Tap here to trash it all — history, cookies, everything — and start fresh on a new tab.`
    - Suggest: `التأريخ وملفات`
    - Elsewhere in this batch, browsing history is "تأريخ التصفح". "التاريخ" is ambiguous and commonly read as "date".
- `promote_search_widget_dialog_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — "Widget" is spelled "ودجت" here but "ويدجت" in the button and picture description of the same dialog.
    - Current: `ودجت %1$s`
    - Source: `We’ll leave you to your private browsing, but get a quicker start next time with the %1$s widget on your Home screen.`
    - Suggest: `ويدجت %1$s`
    - The same term should be spelled the same way on one dialog. promote_search_widget_button_text and promote_search_widget_dialog_picture_content_description both use "ويدجت".

### E. Typography, punctuation & spacing

- `cfr_for_toolbar_delete_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — Hyphens are used where the source and the locale convention use em dashes.
    - Current: `كل شيء - التاريخ`
    - Source: `Tap here to trash it all — history, cookies, everything — and start fresh on a new tab.`
    - Suggest: `كل شيء — التاريخ`
    - The source uses em dashes, and the locale's convention is the em dash.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — Conjunction و is written apart from the next word.
    - Current: `و تحسينه`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `وتحسينه`
    - In Arabic orthography the conjunction و attaches to the following word.
- `preference_privacy_and_security_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ar/strings.xml` — Conjunction و is written apart from the following words.
    - Current: `التّعقّب، و الكعكات، و اختيار البيانات`
    - Source: `Tracking, cookies, data choices`
    - Suggest: `التّعقّب، والكعكات، واختيار البيانات`
    - In Arabic orthography the conjunction و attaches to the following word.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ar/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
