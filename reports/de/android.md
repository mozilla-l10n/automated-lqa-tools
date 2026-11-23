# Firefox for Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `cfdda3ae820f` |
| **Previous run** | 2026-11-16 @ `cde0e6bfbfd2` |
| **Mode** | incremental |
| **Strings reviewed this run** | 54 of 2,625 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (2)

- `browser_toolbar_picture_in_picture_close` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Picture-in-picture is rendered "Bild-in-Bild" here but "Bild-im-Bild" in the companion toolbar string browser_toolbar_picture_in_picture.
    - Current: `Bild-in-Bild-Fenster schließen`
    - Source: `Close picture-in-picture`
    - Suggest: `Bild-im-Bild-Fenster schließen`
    - Both strings describe the same toolbar button, which opens or closes the same feature. German Firefox uses "Bild-im-Bild", as the open-PiP string in this batch does. The close string uses a different form, so screen readers announce two different names for the feature.
- `wrex_widget_match_canceled` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Abgebrochen" means a match that was started and stopped (abandoned), not one that was canceled.
    - Current: `Abgebrochen`
    - Source: `Canceled`
    - Suggest: `Abgesagt`
    - The comment says the badge shows that a match has been canceled. In German sports usage a canceled match is "abgesagt". "Abgebrochen" is a different status (a match stopped while in progress), and sports widgets often show both.

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
| Strings | 2,625 |
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
| quotes | `german-double` 27, `curly-double` 1 | **german-double** |
| ellipsis | `char` 22 | **char** |
| dash | `en` 7 | **en** |
| register | `formal` 653 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `wrex_widget_match_canceled` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Abgebrochen" means a match that was started and stopped (abandoned), not one that was canceled.
    - Current: `Abgebrochen`
    - Source: `Canceled`
    - Suggest: `Abgesagt`
    - The comment says the badge shows that a match has been canceled. In German sports usage a canceled match is "abgesagt". "Abgebrochen" is a different status (a match stopped while in progress), and sports widgets often show both.

### C. Grammar, agreement & spelling

- `notification_erase_text_android_14` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Wrong verb government: "tippen ... auf diese Benachrichtigung" combined with "wischen" is ungrammatical.
    - Current: `Tippen oder wischen Sie auf diese Benachrichtigung`
    - Source: `Tap or swipe this notification to close private tabs.`
    - Suggest: `Tippen Sie auf diese Benachrichtigung oder wischen Sie sie weg`
    - "wischen auf" is not correct German for swiping a notification away; the coordinated construction forces the wrong preposition for one of the verbs.
- `trackers_blocked_panel_num_trackers_blocked_this_week_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The singular variant uses a plural verb form ("wurden") with a singular subject.
    - Current: `[one] %1$d Tracker wurden in dieser Woche blockiert`
    - Source: `{$quantity ->} [one] %1$d tracker blocked this week [other] %1$d trackers blocked this week`
    - Suggest: `[one] %1$d Tracker wurde in dieser Woche blockiert`
    - In the [one] case the subject is a single tracker, so the verb must be "wurde", not "wurden".

### D. Terminology, register & consistency

- `browser_toolbar_picture_in_picture_close` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Picture-in-picture is rendered "Bild-in-Bild" here but "Bild-im-Bild" in the companion toolbar string browser_toolbar_picture_in_picture.
    - Current: `Bild-in-Bild-Fenster schließen`
    - Source: `Close picture-in-picture`
    - Suggest: `Bild-im-Bild-Fenster schließen`
    - Both strings describe the same toolbar button, which opens or closes the same feature. German Firefox uses "Bild-im-Bild", as the open-PiP string in this batch does. The close string uses a different form, so screen readers announce two different names for the feature.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (6)

- `bookmark_sort_menu_custom` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-09): rejected in Pontoon without comment; reason unclear
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>Sounds to me as if this is a deletion process that has been coompleted.</p>
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>Sounds to me as if this is a deletion process that has been coompleted.</p>
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `terms_of_use_prompt_body_line_two_alternative_link` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (43)

- `add_to_tab_group_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string e148a9ea): unreliable finding: The title introduces a tab-group picker; "Zur Tab-Gruppe hinzufügen" is an idiomatic rendering and "Hinzufügen zu" would be awkward German.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 78a45008): unreliable finding: "Departamento" is the established name of these administrative divisions also in German usage; the choice is plausibly deliberate.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 31b2b7d6): unreliable finding: "Post town" is a UK-specific address concept with no German equivalent; keeping the term is defensible.
- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 83223c73): unreliable finding: "Adresse" is a common German UI rendering of URL and the uppercase likely matches sibling field labels; not demonstrably wrong.
- `default_locale_text` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 438de7cd): unreliable finding: "beachten" conveys respecting the device language acceptably; the suggested "Gerätesprache folgen" would itself need a dative article, so this is a stylistic matter.
- `download_clear_search_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string abd77503): unreliable finding: "Leeren" is an acceptable rendering for clearing a search field; the change is a preference.
- `download_item_paused_description_unknown_total_size` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 4604c5de): unreliable finding: "pausiert" is correct and the claimed inconsistency with another string cannot be verified here.
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 064c7aff): unreliable finding: "Identifizierer (Fingerprinter)" is the established Firefox German title term; a plain description using the short form is not clearly a defect.
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 51a67fa8): unreliable finding: The formal sentence is correct German in the locale's formal register; shortening is stylistic.
- `firefox_labs_share_feedback` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 9d450938): unreliable finding: "Sagen Sie Ihre Meinung" is an idiomatic rendering of the link; aligning with the content description is a preference.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 0c006ec2): unreliable finding: The source can be read as a call to action to the user, so the imperative translation is plausibly correct.
- `ip_protection_onboarding_body_link` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 3d02013c): unreliable finding: It is not shown that the link is grammatically embedded in the body sentence; the imperative works as standalone link text.
- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02, string ffe7de12): "Download-Link für %1$s" correctly means the download link for the app; the meaning is not reversed.
- `mozac_browser_errorpages_redirect_loop_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 97dc38aa): unreliable finding: "Fehler: Umleitungsfehler" matches the established German Firefox error-page title wording and appears intentional.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 3060e2ea): unreliable finding: The elliptical coordination "Dies könnte ein Problem … sein oder jemand, der …" is acceptable German, sharing the verb "sein".
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 33538ece): unreliable finding: "auch keine andere Website aufrufen können" conveys essentially the same condition; the change is stylistic.
- `mozac_browser_errorpages_unknown_socket_type_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 4a435447): unreliable finding: The "Fehler: …" title pattern follows established German Firefox error-page conventions; omission of "from server" is minor.
- `mozac_clear_button_description` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string abd77503): unreliable finding: "Leeren" is an acceptable label for clearing a text field; the change is preferential.
- `mozac_compose_base_link_text_links_available` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 328dee21): unreliable finding: "Verfügbare Links" works fine as an announcement; the difference is stylistic.
- `mozac_compose_base_progress_loading` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 155fa1c2): unreliable finding: "Wird geladen…" is the common German loading phrasing; the ellipsis is harmless.
- `mozac_feature_addons_soft_blocked_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 449de91f): unreliable finding: "auf <App> installieren" is acceptable German and the parallel string cannot be verified here; this is a stylistic preference.
- `mozac_protections_dashboard_empty_subtitle` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02, string 44a6f360): 'Sie werden sie hier sehen.' correctly means 'You will see them here' with formal 'Sie' as subject; the meaning is not reversed.
- `mozac_ui_tabcounter_duplicate_tab` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string b20831ae): unreliable finding: German Firefox commonly uses "Tab klonen" for Duplicate Tab, so the claimed established term is doubtful.
- `nova_onboarding_customize_prompt_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string e0051e57): unreliable finding: The sentence-style label is correct in formal register; shortening is a stylistic preference.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string f5837233): unreliable finding: The source 'Open tabs menu' can be read as a noun label (menu of open tabs), which the German renders faithfully.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 31fb1423): unreliable finding: 'Kneifen' is used in German UI texts for the pinch gesture; replacing it would be a stylistic rewording.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 1f8de495): unreliable finding: 'gerade' can mean 'just about to' as well as 'currently', so the meaning is plausibly preserved.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 0ec9727a): unreliable finding: This is an option under the cookie settings, so the phrase reads as describing cookies ('[Cookies] zur seitenübergreifenden Aktivitätenverfolgung…') and is not a broken fragment.
- `preference_enhanced_tracking_protection_custom_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 588cb853): unreliable finding: The wording reflects the established German tracking-protection phrasing; changing it would be a rewrite rather than a clear error fix.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 882da875): unreliable finding: The German localization appears to deliberately describe trackers as 'Skripte, die Ihre Online-Aktivitäten verfolgen'; it cannot be confirmed as a defect.
- `preference_enhanced_tracking_protection_standard_default_1` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 43563939): In German 'Standard' already means 'default', so adding '(Standard)' or '(Standardeinstellung)' would be redundant.
- `preferences_category_sync_controls` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 57b08c62): unreliable finding: 'Synchronisieren' is an acceptable German category heading; the noun form is a stylistic preference.
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string fcb149b0): unreliable finding: 'Kreditkarten' accurately describes the cards in this credit-card section; the claimed sibling inconsistency cannot be verified.
- `preferences_marketing_data_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 43b1e225): unreliable finding: "Messdaten für die Kampagne" is an understandable rendering of the data category; the suggested wording is a stylistic preference.
- `saved_logins_clear_password` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 0e35b760): unreliable finding: "Passwort löschen" is commonly used for clearing a field in German UI; whether it is ambiguous here cannot be confirmed from the string alone.
- `settings_search_recent_searches_section_header` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 7a0b6f7e): unreliable finding: "Neueste" is an acceptable rendering of "recent"; changing it to "Letzte" is a stylistic consistency preference.
- `share_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string b84508bc): unreliable finding: "freigeben" has been used for share in German Mozilla UI; the inconsistency cannot be confirmed from what is visible.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 264b97a4): unreliable finding: "Rückwärts navigieren" is understandable as an accessibility description; preferring "Zurück" is stylistic.
- `terms_of_use_prompt_postpone` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02, string 009aca5e): "Später erinnern" is a standard, idiomatic German button label (infinitive style used throughout German UI); no object is required.
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 3ba958b8): unreliable finding: "Seite" for a sheet is used consistently across the translation strings and is plausibly a deliberate term choice.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/de/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (52)

- `mozac_browser_toolbar_content_description_tracking_protection_on_no_trackers_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `mozac_feature_addons_permissions_find_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `mozac_feature_addons_permissions_history_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `mozac_tab_counter_content_description` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `certificate_warning_homepage_card_hcr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `lens_opt_out_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `protection_panel_etp_toggle_enabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `wrex_widget_match_penalties` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-09
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_browsing_data_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_data_collection_browsingActivity_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_declarative_net_request_feedback_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_listentopage_error_could_not_finish_playing_audio` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `certificate_warning_push_notification_pnw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `debug_drawer_autofill_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `debug_drawer_logins_add_login_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `lens_camera_image_load_failed_v2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
