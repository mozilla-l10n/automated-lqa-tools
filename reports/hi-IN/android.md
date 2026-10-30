# Firefox for Android l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 2,533 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for hi-IN: [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 44 |
| Strings | 2,533 |
| Missing strings | 20 |
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

**20 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — 14
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-hi-rIN/strings.xml` — 5
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-hi-rIN/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13 | **curly-double** |
| apostrophe | `straight` 5 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (0)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

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
