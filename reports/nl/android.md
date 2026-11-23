# Firefox for Android l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **Previous run** | 2026-11-16 @ `cde0e6bfbfd2` |
| **Mode** | incremental |
| **Strings reviewed this run** | 44 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (1)

- `nova_onboarding_sync_pairing_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The verb used as a noun, 'koppelen', needs the article 'het' as the object of 'voltooien'.
    - Current: `Scan om koppelen met uw computer te voltooien`
    - Source: `Scan to finish pairing with your computer`
    - Suggest: `Scan om het koppelen met uw computer te voltooien`
    - In Dutch, a verb used as a noun as the object of 'om … te voltooien' needs the article 'het'. Without it the sentence is ungrammatical.

### ✅ Fixed since the last run (1)

- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "custom tab" is mistranslated as "Tabblad aanpassen" (customize tab) instead of the noun "aangepast tabblad".
    - Current: `Menublad Tabblad aanpassen sluiten`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublad van aangepast tabblad sluiten`
    - The source refers to the menu sheet of a custom tab (aangepast tabblad), not to an action of customizing a tab.

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
| Missing strings | 24 |
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

**24 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — 23
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-nl/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 20 | **curly-single** |
| apostrophe | `typographic` 50 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |
| register | `formal` 429 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `nova_onboarding_sync_pairing_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The verb used as a noun, 'koppelen', needs the article 'het' as the object of 'voltooien'.
    - Current: `Scan om koppelen met uw computer te voltooien`
    - Source: `Scan to finish pairing with your computer`
    - Suggest: `Scan om het koppelen met uw computer te voltooien`
    - In Dutch, a verb used as a noun as the object of 'om … te voltooien' needs the article 'het'. Without it the sentence is ungrammatical.

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (4)

- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — pontoon-rejected (2026-11-13): rejected in Pontoon without comment; reason unclear
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — pontoon-rejected (2026-11-13): rejected in Pontoon without comment; likely reason (inferred): Likely rejected because "Firefox Suggesties" is used the same way in both related strings, which suggests a deliberate Dutch name for the feature rather than a mistranslated brand.
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — pontoon-rejected (2026-11-13): rejected in Pontoon without comment; likely reason (inferred): Likely rejected because "Firefox Suggesties" is used the same way in both related strings, which suggests a deliberate Dutch name for the feature rather than a mistranslated brand.
- `translation_option_bottom_sheet_switch_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — pontoon-rejected (2026-11-13): rejected in Pontoon without comment; reason unclear

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (26)

- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate; 'bladeren' is the standard nl verb for browsing.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate; it is an understandable way to say 'go back'.
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 7b175ac5): unreliable finding: Dutch commonly uses the present tense for future events, and 'werken niet meer op 14 maart' acceptably says they stop working on that date; the suggested wording is a style preference.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 1b25438a): unreliable finding: 'Toestemming' is a common and correct Dutch rendering of 'permission'; nothing confirms that 'machtiging' is the required term here.
- `content_description_settings_search_navigate_back` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent, understandable nl rendering used for every Navigate back control; changing it is a terminology preference.
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string a8e8d8c8): unreliable finding: The meaning (a mask was picked to reuse) is fully conveyed; adding "voor u" is stylistic.
- `etp_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent, understandable nl rendering used across back buttons; the change is preference.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string cd436654): unreliable finding: "Doorleiding" is a valid Dutch noun and the claimed wording of the description string cannot be verified here.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 6de0e127): unreliable finding: Whether nl keeps Firefox Suggest untranslated in this header cannot be confirmed; the descriptive rendering is plausible.
- `ip_protection_locations_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent nl wording for back controls and is understandable; the change is preference.
- `ip_protection_mozilla_vpn_upsell_button` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 378950f8): unreliable finding: Rendering "Get" as "downloaden" is a common, acceptable choice for app/product CTAs.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent nl wording for back controls and is understandable; the change is preference.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 43f8856f): unreliable finding: "ontvang tot %1$s onbeperkte bandbreedte" naturally reads as "until <date>" in Dutch; "tot en met" is a nuance.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is an understandable label for a back control, so replacing it is a matter of style.
- `mozac_feature_sitepermissions_local_network_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 1e41d011): unreliable finding: The word order is somewhat loose but most readers will understand that access is to apps and services on those devices; a rewrite would be stylistic and would require moving text across the placeholder.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string cab6f8dc): unreliable finding: In Dutch, 'trots' can modify an adjective adverbially ('trots onafhankelijk'), and the phrase is idiomatic.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string d5b26c23): unreliable finding: In Fenix 'past explorations' are search-based history groups, so 'eerdere zoekopdrachten' is a plausible deliberate rendering.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string f6c6455c): unreliable finding: The source is itself ambiguous and the Dutch is an acceptable content description for the sort menu control.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 130d77d2): unreliable finding: 'Google doorzoeken' style phrasing is common, acceptable Dutch for searching with an engine.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 18dc2611): unreliable finding: 'essentials' may be an intentional loanword in this feature title; the proposed Dutch term is a guess.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is idiomatic for going back in a stories carousel and is not a mistranslation.
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string be64e7e2): unreliable finding: The sibling strings can't be checked, and the current word order is correct Dutch.
- `terms_of_use_prompt_body_line_two_alternative` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string ca395ba5): With %1$s being the link text 'hier', the sentence reads 'U vindt hier meer info.', which is grammatical, natural Dutch matching the source.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/nl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (31)

- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-23
- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_menu_customize_reset_to_default` — `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_feature_addons_author` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `microsurvey_homepage_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `search_bar_with_lens_widget_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `sent_from_firefox_template_short` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `uninstall_survey_error_failed` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-16
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-09
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-09
- `tab_tray_close_tabs_banner_positive_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-08
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-05
