# Android l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-09-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `ffd664766fe8` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `ffd664766fe8` |
| **Previous run** | 2026-09-17 @ `04999294f7f0` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 2,668 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hi-IN: [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (2)

- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नहींं" has a doubled anusvara/chandrabindu.
    - Current: `अभी सारांश नहींं बनाया जा सकता`
    - Source: `Can’t summarize right now`
    - Suggest: `अभी सारांश नहीं बनाया जा सकता`
    - The word for "not" is spelled नहीं; the target has an extra nasal mark producing "नहींं".
- `search_settings_menu_item` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Search settings" (the search settings screen) is rendered as an imperative "search the settings".
    - Current: `सेटिंग सर्च करें`
    - Source: `Search settings`
    - Suggest: `सर्च सेटिंग`
    - The developer comment says this menu option opens the search settings; the Hindi says "search the settings", reversing the noun phrase into a command.

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
| Files | 44 |
| Strings | 2,668 |
| Missing strings | 79 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**79 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — 79

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13 | **curly-double** |
| apostrophe | `straight` 6 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (26)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 6 |
| 3 | Degraded language (grammar, spelling, terminology) | 20 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `preference_autocomplete_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "custom URL" translated as "उपभोक्ता संशोधित URL" (consumer-modified URL), adding a meaning not in the source.
    - Current: `नया उपभोक्ता संशोधित URL जोड़ा गया।`
    - Source: `New custom URL added.`
    - Suggest: `नया कस्टम URL जोड़ा गया।`
    - The source says "New custom URL added."; "उपभोक्ता संशोधित" (consumer/user-modified) is not the meaning of "custom" here and is inconsistent with the add action string.
- `preference_autocomplete_add_error` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Double-check" rendered literally as "दोहरी जाँच" (a check that is double), losing the meaning "verify again".
    - Current: `आपके द्वारा दर्ज URL की दोहरी जाँच करें।`
    - Source: `Double-check the URL you entered.`
    - Suggest: `आपके द्वारा दर्ज किए गए URL की दोबारा जाँच करें।`
    - Source asks the user to re-verify the entered URL; "दोहरी जाँच" is a literal calque that does not convey "check again".
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Translation adds "उपभोक्ता" (consumer/user), which is not in the source "Remove custom URLs".
    - Current: `उपभोक्ता संशोधित URL हटाएँ`
    - Source: `Remove custom URLs`
    - Suggest: `मनपसंद URL हटाएँ`
    - The source says only "Remove custom URLs"; "उपभोक्ता संशोधित" (consumer-modified) introduces content not present and is inconsistent with preference_autocomplete_title_add.
- `preference_category_advanced` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Advanced" translated as "विस्तृत" (detailed/extensive) instead of the standard "उन्नत".
    - Current: `विस्तृत`
    - Source: `Advanced`
    - Suggest: `उन्नत`
    - The category is Advanced settings; "विस्तृत" means detailed/broad, not advanced. "उन्नत" is already used for Enhanced/Advanced elsewhere in the same file.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "provide and improve %1$s for everyone" is rendered as "make %1$s better and make it available to all", altering the meaning.
    - Current: `%1$s को बेहतर बनाने और सबको उपलब्ध कराने के लिए`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `सबके लिए %1$s को उपलब्ध कराने और बेहतर बनाने के लिए`
    - In the source, "for everyone" modifies both provide and improve; the translation splits it so that only availability applies to everyone, changing what Mozilla claims about data collection purpose.
- `preference_performance_block_webfonts` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Web fonts" translated as "वेब लिपियों" (web scripts), not fonts.
    - Current: `वेब लिपियों को अवरुद्ध करें`
    - Source: `Block web fonts`
    - Suggest: `वेब फ़ॉन्ट अवरुद्ध करें`
    - en-US "web fonts" refers to fonts; "लिपि" means script/writing system (and is commonly read as 'script' i.e. code), which names the wrong thing.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "potentially dangerous" rendered as plain "ख़तरनाक" and "deceptive" as "संदेहास्पद" (suspicious).
    - Current: `ख़तरनाक और संदेहास्पद साइटों को ब्लॉक करें`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `संभावित रूप से ख़तरनाक और भ्रामक साइटों को ब्लॉक करें`
    - Source hedges with "potentially" and uses "deceptive" (भ्रामक, as translated in the related summary string); the target asserts sites are dangerous and merely 'suspicious', dropping meaning and breaking consistency with preference_safe_browsing_summary.
- `search_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "added" is rendered as "संकलित" (compiled/collected), not "जोड़ा गया".
    - Current: `नया खोज इंजन संकलित।`
    - Source: `New search engine added.`
    - Suggest: `नया खोज इंजन जोड़ा गया।`
    - The source says a new search engine was added; "संकलित" means compiled/collected, which is a different action.

### C. Grammar, agreement & spelling

- `download_snackbar_open` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is misspelled/incorrect for the button label "Open".
    - Current: `खोले`
    - Source: `Open`
    - Suggest: `खोलें`
    - Hindi imperative should be खोलें; खोले is an incorrect form, inconsistent with other imperative labels in the file (जोड़ें, सहेजें).
- `firstrun_privacy_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is wrong/incomplete for "Make privacy a habit".
    - Current: `गोपनीयता एक आदत बनाये`
    - Source: `Make privacy a habit`
    - Suggest: `गोपनीयता को एक आदत बनाएँ`
    - "बनाये" is not the correct polite imperative; the correct form is "बनाएँ", and the object marker is missing.
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Gender agreement error: "खोज" is feminine, so the possessive should be "आपकी".
    - Current: `आपका खोज, आपका रास्ता`
    - Source: `Your search, your way`
    - Suggest: `आपकी खोज, आपका रास्ता`
    - "खोज" is a feminine noun in Hindi and requires "आपकी", not "आपका".
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb number: "स्वागत हैं" should be "स्वागत है".
    - Current: `%1$s में आपका स्वागत हैं`
    - Source: `Welcome to %1$s`
    - Suggest: `%1$s में आपका स्वागत है`
    - "स्वागत" is singular, so the copula must be "है", not the plural "हैं".
- `preference_advanced_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "डेवलपर".
    - Current: `डेवलेपर औज़ार`
    - Source: `Developer tools`
    - Suggest: `डेवलपर औज़ार`
    - "डेवलेपर" is a misspelling of the transliteration of "developer" (डेवलपर).
- `preference_mozilla_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Missing postposition/word order: "%1$s परिचय" is ungrammatical for "About %1$s".
    - Current: `%1$s परिचय, सहायता`
    - Source: `About %1$s, help`
    - Suggest: `%1$s के बारे में, सहायता`
    - Hindi requires "के बारे में" or "का परिचय"; a bare noun juxtaposition is grammatically incorrect.
- `preference_mozilla_telemetry2` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "उपयोगित" is not a valid Hindi word for "usage".
    - Current: `उपयोगित डेटा भेजें`
    - Source: `Send usage data`
    - Suggest: `उपयोग डेटा भेजें`
    - Source is "Send usage data"; "उपयोगित" is a malformed form, correct is "उपयोग" (or "उपयोग संबंधी").
- `preference_performance_block_webfonts_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Awkward/incorrect construction "के रूप में परिणाम हो सकता है" for "May result in".
    - Current: `अनुपस्थित प्रतीकों या छवियों के रूप में परिणाम हो सकता है`
    - Source: `May result in missing icons or images`
    - Suggest: `इससे प्रतीक या छवियाँ गायब हो सकती हैं`
    - Source means enabling this may cause icons or images to be missing; the literal "result in the form of" phrasing is ungrammatical in Hindi.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Case agreement error: "गतिविधियाँ" should be oblique "गतिविधियों को" as object of collect/analyze/measure.
    - Current: `टैपिंग और स्क्रॉलिंग जैसी गतिविधियाँ एकत्र, विश्लेषण और मापने के लिए उपयोग`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `टैपिंग और स्क्रॉलिंग जैसी गतिविधियों को एकत्र करने, उनका विश्लेषण करने और उन्हें मापने के लिए उपयोग किया जाता है`
    - The source is a passive clause with 'activities' as object; the Hindi leaves the noun in nominative plural and the verb chain incomplete.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling "दुसरे" (should be "दूसरे") and nonstandard "ऐप्प".
    - Current: `एक ऐप्प से दुसरे ऐप्प पर जाते समय`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `एक ऐप से दूसरे ऐप पर जाते समय`
    - "दुसरे" is a spelling error; the correct form is "दूसरे".
- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Case agreement error: the coordinated objects are in nominative (साइटें) instead of oblique before "को ब्लॉक करें".
    - Current: `रिपोर्ट किये हुए भ्रामक तथा अटैक करने वाली साइटें, मैलवेयर वाली साइटें, तथा अवांछित सॉफ्टवेयर वाली साइटों को ब्लॉक करें।`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `रिपोर्ट की गई भ्रामक तथा अटैक करने वाली साइटों, मैलवेयर वाली साइटों तथा अवांछित सॉफ़्टवेयर वाली साइटों को ब्लॉक करें।`
    - All three coordinated noun phrases share the postposition "को" and must be oblique (साइटों); the first two are left in the nominative plural, which is ungrammatical.
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Sentence structure garbles the meaning: "will send them to your search engine which you type in the address bar".
    - Current: `%1$s उन्हें आपके खोज इंजन में भेजेगा जिन्हें आप पता बार में टाइप करेंगे`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `%1$s आप पता बार में जो टाइप करेंगे उसे आपके खोज इंजन को भेजेगा`
    - The source says the app sends what you type in the address bar to your search engine; the Hindi puts the relative clause after the object pronoun, producing an ungrammatical/confusing sentence.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Missing participle inflection in "जोड़े साइटों".
    - Current: `आपके द्वारा जोड़े साइटों के लिए`
    - Source: `For sites you add`
    - Suggest: `आपके द्वारा जोड़ी गई साइटों के लिए`
    - "For sites you add" requires a proper relative participle; "जोड़े साइटों" is ungrammatical.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — The translation misrenders "never save and cannot restore" as "can never save and restore", breaking the verb agreement and the meaning of the first clause.
    - Current: `हम इस टैब को कभी भी सहेज तथा दुबारा प्राप्त नहीं कर सकते हैं।`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `हम इस टैब को कभी सहेजते नहीं हैं और इसे दुबारा प्राप्त नहीं कर सकते हैं।`
    - en-US states two facts: the browser never saves the tab, and it cannot restore it. The Hindi collapses them into "cannot ever save and restore", changing the first statement.
- `trackers_count_note` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "अवरूद्ध" should be "अवरुद्ध".
    - Current: `%s से ट्रैकर अवरूद्ध`
    - Source: `Trackers blocked since %s`
    - Suggest: `%s से ट्रैकर अवरुद्ध`
    - The correct Hindi spelling uses short u (ु) in अवरुद्ध.

### D. Terminology, register & consistency

- `insecure_connection` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Connection" rendered as "संपर्क" (contact) instead of the standard "कनेक्शन"/"संबंध".
    - Current: `संपर्क सुरक्षित नहीं है`
    - Source: `Connection is not secure`
    - Suggest: `कनेक्शन सुरक्षित नहीं है`
    - In browser security UI, "connection" is a network connection; "संपर्क" means contact and is the wrong term.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Block" rendered inconsistently across cookie settings (बाधित/प्रतिबंधित/ब्लॉक/अवरुद्ध).
    - Current: `कुकीज़ बाधित करें`
    - Source: `Block cookies`
    - Suggest: `कुकीज़ ब्लॉक करें`
    - On the same settings screen, "Block" appears as बाधित करें, प्रतिबंधित करें and ब्लॉक करें; "बाधित" means obstruct/interrupt and is the weakest match for blocking cookies.
- `secure_connection` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Connection" is translated as "संपर्क" (contact) instead of the standard "कनेक्शन"/"संबंध".
    - Current: `संपर्क सुरक्षित है`
    - Source: `Connection is secure`
    - Suggest: `कनेक्शन सुरक्षित है`
    - The label indicates a secure network connection; "संपर्क" means contact and is not the established term for a network connection.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (8)

- `browser_menu_webcompat_reporter_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Text is to incite user to help.
- `mozac_feature_applinks_link_from` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `mozac_feature_prompts_save_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `preference_doh_exceptions_add_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `search_widget_content_description` — `mozilla-mobile/android-components/components/feature/search/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.
- `webcompat_reporter_problem_description_placeholder_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — MT linguist review.

_One line each in `locales/hi-IN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (213)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `mozac_browser_awesomebar_stock_suggestion_increase` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `mozac_feature_prompts_update_address_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `my_longest_fox_is` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `addons_permissions_heading_required_data_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `addresses_village_township` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `likert_scale_option_6` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preference_option_phone_feature_ask_to_allow` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preferences_category_about` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preferences_delete_browsing_data_tabs_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preferences_passwords_save_logins_ask_to_save` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `preferences_sync_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `private_tab_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `review_prompt_rate_header` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `search_settings_google_lens_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `search_settings_menu_item` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `sent_from_firefox_template` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `sent_from_firefox_template_short` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `sync_connect_device` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `sync_send_tab_error_auth_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `sync_sign_in` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `tracking_protection_off` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `webcompat_reporter_screen_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-17
- `mozac_browser_errorpages_archive_retry` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_archive_unreachable` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_toolbar_content_description_autoplay_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
