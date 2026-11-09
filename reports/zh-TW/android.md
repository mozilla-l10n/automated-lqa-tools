# Firefox for Android l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `eb5867992b38` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,601 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1111 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `webcompat_reporter_edit_url_dialog_dismiss` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The dismiss button in the Edit URL dialog is rendered as "Got it!" instead of a cancel/close action.
    - Current: `知道了！`
    - Source: `Dismiss`
    - Suggest: `取消`
    - This button sits next to "Save" in an edit confirmation dialog, so "Dismiss" means close without saving. 知道了！ ("Got it!") reads as an acknowledgement, not as discarding the edit.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (13)

- `download_item_paused_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>correct but original approved translation provides more context</p>
- `home_bookmarks_menu_item_remove` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangeable; not better from original translation</p>
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>the suggested translation is less accurate from the original approved translation</p>
- `mozac_feature_addons_enabled` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>chinese does not have a past perfect tense, simply use 啟用 for indicators</p>
- `mozac_feature_addons_failed_to_load_extensions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon without comment; reason unclear
- `mozac_feature_addons_permissions_browser_settings_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
- `mozac_feature_addons_permissions_content_description_item` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable for quantifiers for permission items</p>
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>correct but doesn't sound natural</p>
- `protection_panel_banner_protected_no_blocked_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
- `startup_crash_positive` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>
- `trackers_blocked_empty` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
- `unsubmitted_crash_dialog_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-04): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/zh-TW/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (48)

- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_updater_dialog_last_attempt` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_updater_dialog_status` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_user_rating_count_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `automotive_authentication_setup_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `browser_menu_add_to_homescreen_xiaomi` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `browser_menu_remove_from_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `download_languages_default_system_language_require_preference` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `login_deletion_confirmation_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nimbus_survey_message_text` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `phone_feature_blocked_intro` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preference_doh_increased_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_android_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_passwords_autofill2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_search_engines_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `preferences_usage_data_description_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `search_add_custom_engine_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `search_header_menu_item_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `setup_checklist_subtitle_3_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `setup_checklist_subtitle_5_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `setup_checklist_subtitle_6_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `sync_failed_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `sync_failed_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
- `sync_last_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-05
