# Android l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `81c3d1941037` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `81c3d1941037` |
| **Previous run** | 2026-08-20 @ `81c3d1941037` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for it: [firefox](firefox.md)

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
| Files | 43 |
| Strings | 2,908 |
| Missing strings | 0 |
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
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 25 | **curly-double** |
| apostrophe | `typographic` 174 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 2 | **em** |
| register | `informal` 89, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (11)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 10 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "custom tab" (a browser feature: a tab opened by another app) is mistranslated as "personalizzazione schede" (tab customization).
  - Current: `Chiudi il menu per la personalizzazione schede`
  - Source: `Close custom tab menu sheet`
  - Suggest: `Chiudi il pannello del menu della scheda personalizzata`
  - The source refers to the bottom sheet menu of a Custom Tab, not to a menu for customizing tabs; the meaning is reversed/altered.
- `browser_menu_summarize_page_badge` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Badge text "New" rendered as "Novità" (news) instead of "Novità"/"Nuovo" label meaning new feature.
  - Current: `Novità`
  - Source: `New`
  - Suggest: `Nuovo`
  - The source is the adjective "New" used as a badge on a new feature; "Novità" means "news/novelty".
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Help catch trackers" is translated as "Cattura i traccianti", dropping the "help" sense.
  - Current: `Cattura i traccianti`
  - Source: `Help catch trackers`
  - Suggest: `Aiuta a individuare i traccianti`
  - The source invites the user to help catch trackers; the Italian turns it into a direct command to catch them.
- `opening_screen_last_tab_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Open on last tab" is rendered as "Apri scheda più recente" (most recent tab) instead of the last open tab, inconsistent with opening_screen_last_tab "Ultima scheda".
  - Current: `Apri scheda più recente`
  - Source: `Open on last tab`
  - Suggest: `Apri ultima scheda`
  - The source says "Open on last tab", matching the option label "Last tab" translated as "Ultima scheda"; "scheda più recente" changes the wording and breaks consistency on the same preference surface.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation adds "alcuni" (some) and softens the source's "will cause websites to break".
  - Current: `Tutti i cookie (alcuni siti non funzioneranno correttamente)`
  - Source: `All cookies (will cause websites to break)`
  - Suggest: `Tutti i cookie (i siti web non funzioneranno correttamente)`
  - The source states websites will break, without limiting it to some sites.
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Descriptive summary "Allows Mozilla to…" rendered as an imperative "Consenti a Mozilla…".
  - Current: `Consenti a Mozilla di installare e condurre studi`
  - Source: `Allows Mozilla to install and run studies`
  - Suggest: `Consente a Mozilla di installare e condurre studi`
  - The developer comment marks this as a summary describing what the preference does, not a command to the user.
- `preferences_tab_strip` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Tab bar display" is rendered as "Visualizzazione barra delle schede" which reverses the word order/meaning of the preference title.
  - Current: `Visualizzazione barra delle schede`
  - Source: `Tab bar display`
  - Suggest: `Mostra barra delle schede`
  - The developer comment says the preference is for showing the tab strip; the Italian noun phrase is acceptable but ambiguous. Low value.
- `protection_panel_banner_not_secure_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Your connection" is rendered as "Questa connessione" (this connection).
  - Current: `Questa connessione non è sicura.`
  - Source: `Your connection is not secure.`
  - Suggest: `La tua connessione non è sicura.`
  - The source says "Your connection is not secure."; the possessive was changed to a demonstrative.
- `recent_tabs_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Section header "Jump back in" is rendered as a singular call to action "Torna a questa scheda" (Go back to this tab).
  - Current: `Torna a questa scheda`
  - Source: `Jump back in`
  - Suggest: `Riprendi da dove eri`
  - This is a home-screen section header for recent tabs, not a per-tab action label referring to "this tab".
- `sign_in_with_email` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Use email instead" is translated without the contrastive "instead", losing the alternative-method meaning.
  - Current: `Accedi con l’email`
  - Source: `Use email instead`
  - Suggest: `Usa invece l’email`
  - The source offers an alternative sign-in method ("instead"); the Italian drops that contrast.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `sports_widget_final_results_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "World Cup" is rendered as "Mondiali" here but as "Coppa del mondo" in the sibling strings, an inconsistency on the same surface.
  - Current: `Risultati finali dei Mondiali`
  - Source: `World Cup final results`
  - Suggest: `Risultati finali della Coppa del mondo`
  - sports_widget_final_results_page_content_description translates the same source phrase "World Cup final results" as "Risultati finali della Coppa del mondo"; the two accessibility strings for the same page must match.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Suppressed as false positives (4)

- **`it-attiva-not-attivata`** (1) — The expected pair is `Attiva`/`Attivo`/`Attivi` with `Disattivata`/`Disattivato`/`Disattivati`. The asymmetry is deliberate and borne out by the tree, which uses `attiva` 279 times against 35 for the participle forms. A suggestion to "restore symmetry" with `Attivata`/`Attivato`/`Attivi` is wrong. The regex is word-anchored because a plain substring would also match `disattivato`.
  - `browser_feature_desktop_site_on`
- **`it-crittare`** (1) — `crittare` and its forms (`critta`, `crittato`) are the correct Italian verb for "to encrypt" — not a typo for `criptare`. Confirmed by the maintainer. Scoped to spelling findings so a mistranslation in the same string still reports.
  - `preferences_credit_cards_save_and_autofill_cards_summary_2`
- **`it-final-exclamation`** (2) — Ending a sentence with `.` where the source ends with `!` is a deliberate register choice; Italian UI text uses the exclamation mark far more sparingly than English. Scoped to typography findings so a real punctuation defect in the same string still reports.
  - `firefox_labs_banner_title_2`, `snackbar_added_to_shortcuts`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (2)

- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — raised by `llm`, withdrawn 2026-08-20
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — raised by `llm`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (42)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_contextmenu_open_image_in_new_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `action_bar_up_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `certificate_warning_push_notification_pnw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `content_description_gallery` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_cfr_tools_reset_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `delete_history_prompt_button_today_and_yesterday` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `dialog_delete_positive` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `download_languages_item_content_description_downloaded_state` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `download_rename_error_invalid_name_error` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `link_shared_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `nova_onboarding_customize_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `radio_preference_info_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `sync_connect_device_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `sync_offline` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `sync_sent_tabs_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tab_manager_empty_private_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
