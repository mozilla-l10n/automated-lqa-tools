# Firefox for Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **Previous run** | 2026-11-16 @ `cde0e6bfbfd2` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,534 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,534 |
| Missing strings | 91 |
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

**91 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — 46
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — 18
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-sl/strings.xml` — 11
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — 5
- `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — 5
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-sl/strings.xml` — 5
- `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-sl/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 16, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 5 | **en** |
| register | `informal` 4, `formal` 81 | **formal** |

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

- `certificate_details_panel_issued_to_label` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The preposition "to" is missing, so the label reads "Certificate issued:" instead of "Certificate issued to:".
    - Current: `Potrdilo izdano:`
    - Source: `Certificate issued to:`
    - Suggest: `Potrdilo izdano za:`
    - The label introduces the organisation the certificate was issued to. Without "za", the Slovenian reads like an issue date or status. It no longer introduces the recipient.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (6)

- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Glede na kontekst je prav, da je v rodilniku.</p>
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Razumem, zakaj je bot reagiral na ta niz, ampak če se prebere kot "ohranjevalnik baterije nastavi to nastavitev", je pravilen in slogovno boljši.</p>
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Glede na kontekst je v redu, da je mala začetnica. Slovenski pravopis ima malo drugačna pravila za alinejno naštevanje kot angleški. Bodisi morajo biti male začetnice, bodisi mora biti na koncu vsake alineje končno ločilo.</p>
- `tab_manager_empty_tab_groups_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-15): rejected in Pontoon without comment; reason unclear
- `webcompat_reporter_clear_reason_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (48)

- `ai_controls_ai_powered_features` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string e74456d0): unreliable finding: UI is the standard Slovenian abbreviation for umetna inteligenca, and the tree uses both forms; using the abbreviation in a short label is not clearly an error.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 628a415c): unreliable finding: The paraphrase "enable the individual options you want to use" keeps the meaning of unblocking the features you want to keep using; the change would be stylistic.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 4fb0ff62): unreliable finding: "zavihek po meri" is the established term for custom tab, and dropping "sheet" in an accessibility label for closing the menu does not clearly change the meaning.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 902ab77d): unreliable finding: This is a header in a debug-only drawer, and "Jeziki" for locales is a plausible simplification; this is not a confirmed defect.
- `delete_all_history_group_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string ec247628): Straight double quotes are the measured majority convention in the sl tree (14–15 straight vs 4 curly).
- `download_delete_single_item_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 92443a02): unreliable finding: The feminine form implies the unstated noun "datoteka" (file), which is a common, acceptable pattern; the neuter form is also possible, so this is a preference.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 51a1c1cb): unreliable finding: "Preusmeritve sledilcev" is an established rendering of this ETP category name, and the suggested wording is not clearly more correct.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 9eb1757e): unreliable finding: Using the brand name as an uninflected modifier ("Firefox zavihki") is common practice in Slovenian Mozilla localization, so the wording is acceptable.
- `link_shared_snackbar_action` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 6e5f433a): unreliable finding: A short snackbar action label "Nastavitve" still conveys opening the settings; adding the verb would be a stylistic change.
- `link_shared_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 20a0910a): unreliable finding: "poslana" (sent) is an acceptable Slovenian rendering of a shared link, and "deljena" is not clearly better.
- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 2b275a17): Slovenian UI labels and toggles conventionally use the 2nd-person singular imperative (e.g. "Shrani", "Prikaži"), which is not a register violation.
- `mozac_browser_engine_system_auth_message` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 9a0defd0): The en-US source uses the same curly quotes around %1$s, and the locale also uses curly quotes in some strings.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 4035b9c4): unreliable finding: The paraphrase still tells the user to check their proxy/firewall settings, so the meaning comes across; a closer rendering would be a stylistic rewrite.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string dc4fa37f): The en-US source uses the same curly quotes around “Try Again”, and the locale also uses curly quotes in some strings.
- `mozac_browser_errorpages_port_blocked_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 11822b86): unreliable finding: "nesprejemljiva" is a plausible established rendering for a restricted port; the change is a matter of preference.
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 917b156a): This is a checkbox/setting label, and the locale conventions say such labels use the informal imperative (e.g. "Deli").
- `mozac_feature_applinks_open_in` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string bd7c47c0): Slovenian orthography (SP) separates the ellipsis by a space after a complete word indicating omission, e.g. "Odpri v …", a standard Slovenian Mozilla convention.
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 54371095): Each link keeps its correct placeholder (%3$s privacy policy, %4$s terms), so reordering the two items is a valid stylistic choice with no functional or semantic change.
- `mozac_feature_summarize_disclaimer_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string c1d201a3): "UI" is the standard Slovenian abbreviation for "umetna inteligenca"; user interface is not abbreviated UI in Slovenian.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 03d3b2c6): unreliable finding: "Namestitev" (setup/installation) is a reasonable rendering for a step that downloads and installs models.
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string b32d4183): unreliable finding: A first-person offer ("Povzamem…?") is a natural Slovenian way to phrase this kind of question; the change is stylistic.
- `mozac_support_base_permissions_needed_negative_button` — `mozilla-mobile/android-components/components/support/base/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string f440d86d): unreliable finding: "Skrij" is a common, acceptable Slovenian rendering of a "Dismiss" button that closes a prompt; the suggestion is a preference.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 904a3e60): unreliable finding: "meni prevajalnika" naturally refers to the translation feature's menu; the suggestion is a stylistic alternative.
- `notification_privacy_report_body_has_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 375428c4): unreliable finding: Making the implied object (trackers) explicit is a legitimate clarification for a transitive Slovenian verb, not a meaning change.
- `nova_onboarding_marketing_primary_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 39b6a8ff): Locale instructions specify that button labels use the informal singular imperative, so "Pomagaj Firefoxu" is correct.
- `onboarding_term_of_service_line_three_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 1018b662): Slovenian UI command labels (buttons/links) normally use the singular imperative (e.g. 'Shrani', 'Prekliči'), independent of the formal register used in prose.
- `open_all_warning_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 51d91efc): 'več zavihkov (%d)' is a standard way to avoid plural forms; here 'več' means 'multiple' and the exact count still shows through %d.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 2f1015ff): Setting labels in sl use this imperative form (cf. "Omogoči"), and the suggested "sporoči" is the same 2nd-person singular, so there is no register mismatch.
- `preferences_ai_controls` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 1bd5a4ac): unreliable finding: "UI" is the standard Slovenian abbreviation for umetna inteligenca; the label is acceptable.
- `preferences_enable_gecko_logs` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 8a2caa37): Gecko is Mozilla's rendering engine, so "izrisovalnika Gecko" is an accurate descriptor that also allows correct declension of the brand name.
- `preferences_https_only_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string d6b1c3b4): unreliable finding: The sentence reads as connecting using the HTTPS protocol, which is understandable; adding sites is a rewording.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 6ef4e42a): unreliable finding: "odprli" for viewed tabs is a natural, acceptable rendering; the difference is stylistic.
- `quick_setting_option_autoplay_block_audio` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 16e4d639): unreliable finding: "Zavrni" is used consistently in the autoplay options and appears to be the locale's chosen term.
- `quick_setting_option_autoplay_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string c4cbbb6d): unreliable finding: "Zavrni" is used consistently across the autoplay options; changing it would be a terminology preference.
- `restart_warning_dialog_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string ee34a357): unreliable finding: The app is %1$s itself, so "%1$s may close… reopen it" means the same as the source; this is a legitimate restructuring.
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 0b669242): unreliable finding: "Pošlji povratne informacije" is the idiomatic Slovenian button label for leaving feedback, and the imperative is the house style for buttons.
- `saved_login_clear_hostname` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 0b8ba364): unreliable finding: Calling this login field "domena" is a plausible established term choice; changing it would be terminology preference.
- `saved_login_hostname_required` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 20b55f9a): unreliable finding: This matches the "domena" term the sibling strings use for the same field; changing it would be terminology preference.
- `search_add_custom_engine_error_missing_template` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string c77183cc): 'Prepričajte se, da se iskalni niz ujema z obliko primera' accurately conveys 'Check that search string matches Example format'.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string eecc6405): "Ste samo 1 korak od ciljne črte" is grammatical Slovenian; no preposition is missing, the suggestion is only stylistic.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (45)

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `preferences_delete_browsing_data_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `search_suggestions_onboarding_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_harmful_addon_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_redirect_dialog_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_update_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_summarize_settings_shake_sensitivity_description` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `sound_off` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `content_description_take_photo` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `etp_cookies_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `microsurvey_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_tou_body_line_3_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_doh_exceptions_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_option_autoplay_allowed_wifi_subtext` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preferences_search_browsing_history` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `setup_checklist_subtitle_5_steps_third_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `setup_checklist_task_explore_extensions` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
