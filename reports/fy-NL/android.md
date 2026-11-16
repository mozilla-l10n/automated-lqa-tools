# Firefox for Android l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-11-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `cde0e6bfbfd2` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `cde0e6bfbfd2` |
| **Previous run** | 2026-11-09 @ `3c577835f1fc` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 2,606 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,606 |
| Missing strings | 14 |
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

**14 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — 14

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 16 | **curly-single** |
| apostrophe | `typographic` 104 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `addresses_street_address` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Street Address" is translated as just "Adres", losing the street distinction and colliding with the generic address label.
    - Current: `Adres`
    - Source: `Street Address`
    - Suggest: `Strjitte en hûsnûmer`
    - The source specifically labels the street address line; rendering it as the generic "Adres" makes it indistinguishable from other address labels in the same form.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Custom tab menu sheet" rendered as "Menublêd Ljepblêd oanpasse", turning the noun phrase into an imperative "customize tab".
    - Current: `Menublêd Ljepblêd oanpasse slute`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublêd fan oanpast ljepblêd slute`
    - The source describes closing the menu sheet of a custom tab; the translation reads as "Customize tab menu sheet close", changing the meaning.
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Translating" (in-progress state) is translated as the infinitive "Oersette", identical to the "Translate" button, losing the progress meaning.
    - Current: `Oersette`
    - Source: `Translating`
    - Suggest: `Oersette…`
    - The developer comment states this is the inactive button text indicating a translation is currently in progress; rendering it identically to translations_bottom_sheet_positive_button ("Translate" = "Oersette") removes the distinction between the two states.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "browsing history" is rendered as "browserskiednis" here but as "sneupskiednis" in the parallel _for_update string.
    - Current: `Resinte browserskiednis, cookies en relatearre gegevens wiskje`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Resinte sneupskiednis, cookies en relatearre gegevens wiskje`
    - The same source sentence ("Clear recent browsing history, cookies, and related data") is translated with two different terms on the same surface; fy-NL uses "sneup-" for browsing (cf. sneupaktiviteit for "browsing activity").

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (7)

- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The reviewer also rejected the same change in ref 2, and both strings use "Firefox Suggestjes", so this looks like a deliberate local rendering of the feature name, not a mistake.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `mozac_feature_addons_permissions_dialog_heading_required_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `mozac_feature_addons_permissions_privacy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The reviewer also rejected the same change in ref 0, and both strings use "Firefox Suggestjes", so this looks like a deliberate local rendering of the feature name, not a mistake.
- `preferences_passwords_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The finding contradicts itself: the spelling it says is correct is the original exactly, so the reviewer probably didn't accept that there was an error.
- `webcompat_reporter_label_mandatory_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The original ("so that we can investigate it") already gets the meaning across correctly, so the more literal rewording was probably seen as an unnecessary style change.

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (37)

- `about_crashes` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 790b91f0): fy-NL Firefox uses 'ungelok' for crashes (e.g. Ungelokrapporten), and per locale rules a capitalised initial never carries a diacritic.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 31958d5b): unreliable finding: 'AI troch %1$s brûke' (use AI via Firefox) conveys essentially the same meaning as AI provided by Firefox.
- `customize_addon_collection_user_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 799077e1): unreliable finding: Juxtaposed nouns are an acceptable compact label style; the change is a preference.
- `likert_scale_option_i_plan_to_keep_using` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string bba02ae6): Frisian verb clusters are ordered 'brûke te bliuwen'; the current construction is grammatical and the suggestion is not.
- `mozac_browser_errorpages_archive_check_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 949ffe5f): "argivearre" is the regular past participle of the Frisian verb "argivearje" (to archive); the finding itself proposes the identical spelling.
- `mozac_cfr_dismiss_button_content_description` — `mozilla-mobile/android-components/components/compose/cfr/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string c91e7f78): The Frisian verb "slute" (to close) is spelled without an accent; "slúte" is not the standard form.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 632b537e): unreliable finding: The translation is correct on its own and mirrors the English imperative; aligning it with the other variant would be a stylistic rewrite of the whole sentence.
- `mozac_feature_downloads_open_not_supported1` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string fbfd0f66): 'om … mei te iepenjen' refers back to the app (an app to open the files with), a normal grammatical Frisian construction, like Dutch 'mee te openen'.
- `mozac_feature_listentopage_dropdown_expanded` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 91a64667): Frisian orthography drops the accent on a capitalised sentence-initial 'út', giving 'Ut'.
- `mozac_feature_listentopage_notification_playback_speed_0_25` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 2e0e0701): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'; lowercase 'ôf' elsewhere is consistent.
- `mozac_feature_listentopage_notification_playback_speed_0_5` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 55a35ca8): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'.
- `mozac_feature_listentopage_notification_playback_speed_0_75` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 619c8299): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string bfbb08d4): unreliable finding: The English source is itself elliptical; the translation is a reasonable rendering of it.
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 01395599): unreliable finding: Blocking companies that spy on your clicks is functionally the same message; not a reversal of meaning.
- `phone_feature_blocked_intro` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 5f2eba85): unreliable finding: An infinitive heading like "Tastean:" is a normal Frisian/Dutch way to introduce steps; the suggestion is stylistic.
- `phone_feature_blocked_step_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 9b1fcd65): Frisian nouns in -ing form their plural in -ingen (cf. ynstellingen), so 'Machtigingen' is correct Frisian.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 22fd6508): In Frisian subordinate clauses the infinitive precedes the finite verb, so 'hokker website jo besykje gean' is grammatical.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string cab4b936): Swapping the order of the two joined verbs does not change the meaning; both share and sell are translated.
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 25b54c77): Frisian (like Dutch) writes compounds closed; 'Cross-sitecookies' is the regular compound form.
- `preferences_category_sync_controls` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 3e048046): Frisian spells this word with g (syngronisaasje, syngronisearje); 'ch' is the Dutch spelling.
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string e8f06056): 'efterlitte' is the standard Frisian verb; 'achterlitte' is Dutch.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string b4ccdd22): unreliable finding: The source is itself ambiguous, and "Wachtwurdmenu sortearje" is a plausible rendering for an icon content description.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string f580ec2b): "%s trochsykje" follows the standard Dutch/Frisian Mozilla pattern (cf. nl "%s doorzoeken") for searching with a named engine.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 18dc2611): unreliable finding: Keeping the feature label 'essentials' may be deliberate (as in Dutch builds), and the suggested 'essinsjes' is not an established Frisian word.
- `setup_checklist_group_helpful_tools` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 855ddf29): 'ark' is a neuter mass noun; without an article the adjective stays uninflected ('nuttich ark'), like Dutch 'nuttig gereedschap'.
- `setup_checklist_subtitle_5_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 96aced89): unreliable finding: "ynstallaasjestappen" mirrors the common Dutch "installatiestappen" for setup steps; the change is a terminology preference that can't be confirmed as an error.
- `setup_checklist_subtitle_6_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string c62c8120): unreliable finding: "ynstallaasjestappen" mirrors the common Dutch "installatiestappen" for setup steps; the change is a terminology preference that can't be confirmed as an error.
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string c91e7f78): "Slute" (close) is an accepted rendering of "Dismiss" for a banner button, as in Dutch "Sluiten".
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string 0a11c8c9): "Syngronisearre iepen ljepblêden" correctly means synced open tabs; word order is only a stylistic difference.
- `terms_of_use_prompt_title_option_a` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-13, string 4df8c1bf): unreliable finding: "Gebrûksbetingsten" is the standard rendering of Terms of Use (cf. Dutch "Gebruiksvoorwaarden"); any inconsistency should be resolved in the other string, not here.
- `tracking_protection_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 1c0d693a): Frisian orthography omits the accent on capital U (Út → Ut, cf. 'Utein', 'Ut' used throughout fy-NL Firefox); 'Ut' is the standard capitalized form.
- `translation_error_language_not_supported_warning_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 1806eba0): 'fan it [taal] út' is the idiomatic Frisian circumposition for 'from (a language)' (like Dutch 'vanuit het Engels'); language names take the article 'it' in Frisian.
- `translation_in_progress_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string 9bea963f): Infinitive plus ellipsis ("Oersette…") is the standard Dutch/Frisian way to express an in-progress action.
- `ungroup_tab_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 7ea51dae): 'degroepearje' follows the regular Frisian -earje verb form (groepearje); it is the other string ('Degroeperje') that deviates, so this one is correct.
- `webcompat_reporter_reason_content2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 364665d0): Frisian orthography drops the circumflex on capital U (û → U), so 'Untbrekkende' is the standard capitalized spelling.
- `wrex_widget_match_postponed` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 03a8011a): Frisian orthography drops accents on capital U, so 'Utsteld' is the correct capitalized form of 'útsteld'.
- `wrex_widget_match_suspended` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 42f56527): Frisian orthography drops the circumflex on capital U, so 'Underbrutsen' is the correct capitalized form of 'ûnderbrutsen'.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/fy-NL/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (87)

- `mozac_feature_downloads_file_failure_no_connection` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `mozac_feature_prompts_expand_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_settings_label` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `firefox_labs_no_labs_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `preferences_show_search_optimization_cards` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `startup_crash_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `tab_indicator_media_playing` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `wrex_widget_error_try_refreshing` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-09
- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_downloads_open_existing_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `addresses_eircode` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `bookmark_menu_open_all_in_private_tabs_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `bookmark_save_in_label` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `close_tab_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `create_collection_deselect_all` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
