# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | 2026-08-20 @ `8c439c8dbd76` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (6)

- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation says "disconnetterti dal sito" (singular, this site) while the source says it might log you out of websites in general.
  - Current: `potrebbe disconnetterti dal sito o svuotare eventuali carrelli in sospeso`
  - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
  - Suggest: `potrebbe disconnetterti dai siti web e svuotare eventuali carrelli della spesa`
  - en-US: "might log you out of websites and clear shopping carts" — plural "websites" and coordinating "and", not "or" with a singular site.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "selected locale" translated as "lingua selezionata" (selected language), inconsistent with the locale terminology in this feature.
  - Current: `per la lingua selezionata`
  - Source: `Add new address for selected locale`
  - Suggest: `per il locale selezionato`
  - The debug feature works with locales (region/format), not languages; source says "locale".
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Debug locales to enable" is rendered as a generic "choice of languages", dropping the "debug" qualifier and mistranslating "locales".
  - Current: `Scelta delle lingue da attivare`
  - Source: `Debug locales to enable`
  - Suggest: `Locale di debug da attivare`
  - The source names the list of debug locales; the translation says "choice of languages" and loses the debug qualifier.
- `debug_drawer_cfr_tools_reset_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Reset CFRs" translated as "Ripristina CFR" where elsewhere reset/override wording differs; "Ripristina" means restore, acceptable, but the plural marker is lost — see rationale.
  - Current: `Ripristina CFR`
  - Source: `Reset CFRs`
  - Suggest: `Reimposta CFR`
  - "Reset" in this debug context means reimpostare/azzerare the CFR state, not restoring a previous state.
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation replaces "make your browsing more private" with "protect your privacy while browsing", changing the wording of the source.
  - Current: `Attiva la VPN per proteggere la tua privacy durante la navigazione e rendere più difficile il tracciamento.`
  - Source: `Turn VPN on to make your browsing more private and harder to trace.`
  - Suggest: `Attiva la VPN per rendere la tua navigazione più privata e difficile da tracciare.`
  - The source says "make your browsing more private and harder to trace"; the same sentence is correctly rendered in ip_protection_onboarding_body_promo as "rendere la tua navigazione più privata e difficile da tracciare", so this variant is both inaccurate and inconsistent.
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation drops "above" and renders "active search engine" as "motore di ricerca predefinito" (default search engine).
  - Current: `Disponibile solo se Google è attivo ed è impostato come motore di ricerca predefinito durante la navigazione.`
  - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
  - Suggest: `Disponibile solo se Google è attivo qui sopra ed è il motore di ricerca attivo durante la navigazione.`
  - The source says "enabled above" (referring to the setting above) and "your active search engine", not the default search engine; the Italian changes the meaning.

### ↩︎ Withdrawn — no longer considered a defect (2)

- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The quoted preference names are capitalized differently from the source, breaking the match with the actual UI labels.
  - Current: `“Traduci sempre” e “Non tradurre mai”`
  - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
  - Minor: source uses lowercase quoted labels; the Italian labels match the UI strings, so this is acceptable. (Retired: the suggested text is identical to the current text.)
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "%d addresses" is translated as "%d indirizzi" but the developer comment says it is the number of history items; however the literal source word is "addresses".
  - Current: `%d indirizzi`
  - Source: `%d addresses`
  - Placeholder-level check: source says "addresses" and target says "indirizzi", which matches; no defect. (Retired: the suggested text is identical to the current text.)

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

## 3. Open findings (21)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 12 |
| 3 | Degraded language (grammar, spelling, terminology) | 8 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Custom tab menu sheet" is mistranslated as a menu for customizing tabs.
  - Current: `Chiudi il menu per la personalizzazione schede`
  - Source: `Close custom tab menu sheet`
  - Suggest: `Chiudi il pannello del menu della scheda personalizzata`
  - "Custom tab" is a specific Android feature (scheda personalizzata); the Italian says "menu for customizing tabs", which is a different thing.
- `browser_menu_summarize_page_badge` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Badge text "New" rendered as "Novità" (news) instead of "Novità"/"Nuovo" label meaning new feature.
  - Current: `Novità`
  - Source: `New`
  - Suggest: `Nuovo`
  - The source is the adjective "New" used as a badge on a new feature; "Novità" means "news/novelty".
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Help catch trackers" is rendered as an imperative "catch trackers" losing the "help" (contribute to catching) meaning.
  - Current: `Cattura i traccianti`
  - Source: `Help catch trackers`
  - Suggest: `Aiuta a catturare gli elementi traccianti`
  - The source asks the user to help catch trackers; the Italian tells the user to catch them, dropping "help". It also uses "traccianti" instead of the "elementi traccianti" used consistently in the surrounding strings.
- `opening_screen_last_tab_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Open on last tab" is rendered as "Apri scheda più recente" (most recent tab) instead of the last open tab, inconsistent with opening_screen_last_tab "Ultima scheda".
  - Current: `Apri scheda più recente`
  - Source: `Open on last tab`
  - Suggest: `Apri ultima scheda`
  - The source says "Open on last tab", matching the option label "Last tab" translated as "Ultima scheda"; "scheda più recente" changes the wording and breaks consistency on the same preference surface.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "will cause websites to break" weakened to "alcuni siti non funzioneranno" (some sites), mirroring the previous string's "may".
  - Current: `Tutti i cookie (alcuni siti non funzioneranno correttamente)`
  - Source: `All cookies (will cause websites to break)`
  - Suggest: `Tutti i cookie (i siti web non funzioneranno correttamente)`
  - The source distinguishes cookies_3 ("may cause websites to break") from cookies_4 ("will cause websites to break"); the Italian for _4 adds "alcuni", weakening the certainty of the warning.
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The descriptive summary "Allows Mozilla to install and run studies" is rendered as an imperative addressed to the user.
  - Current: `Consenti a Mozilla di installare e condurre studi`
  - Source: `Allows Mozilla to install and run studies`
  - Suggest: `Consente a Mozilla di installare e condurre studi`
  - The source is a third-person description of what the setting does ("Allows Mozilla…"), not a command to the user; compare preferences_daily_usage_ping_description translated as "Questo consente a Mozilla…".
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
- `recent_tabs_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Jump back in" is a section header for resuming recent tabs, but the Italian says "Torna a questa scheda" ("Go back to this tab"), naming a single specific tab.
  - Current: `Torna a questa scheda`
  - Source: `Jump back in`
  - Suggest: `Riprendi da dove eri rimasto`
  - The source is a generic header for the "Jump back in" section on the home screen; the Italian refers to one specific tab ("this tab"), which does not match the header's meaning.
- `sign_in_with_email` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Use email instead" is translated as "Accedi con l’email", losing the "instead" contrast.
  - Current: `Accedi con l’email`
  - Source: `Use email instead`
  - Suggest: `Usa invece l’email`
  - The source offers an alternative to camera pairing ("instead"); the Italian drops that meaning.
- `sync_connect_device_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Translation adds "account" not present in the source ("sign in to Firefox" becomes "accedi all’account Firefox").
  - Current: `accedi all’account Firefox`
  - Source: `To send a tab, sign in to Firefox on at least one other device.`
  - Suggest: `accedi a Firefox`
  - The source says "sign in to Firefox on at least one other device", referring to signing in to the browser, not to an "account Firefox".
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Translating" (action in progress) is translated as the noun "Traduzione", losing the in-progress meaning.
  - Current: `Traduzione`
  - Source: `Translating`
  - Suggest: `Traduzione in corso`
  - The developer comment says the button text indicates a translation is currently in progress; the accompanying content description uses "Traduzione in corso".

### C. Grammar, agreement & spelling

- `browser_feature_desktop_site_on` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Gender/form inconsistency: "On" toggle state rendered as imperative/feminine "Attiva" while the matching "Off" string uses "Disattivata".
  - Current: `Attiva`
  - Source: `On`
  - Suggest: `Attivata`
  - The pair browser_feature_desktop_site_on/off describes the toggle state; "Attiva" reads as an imperative or adjective mismatching "Disattivata" used for the off state.
- `link_shared_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Word order makes the snackbar read as an imperative-ish fragment instead of the past-participle status message "Link shared".
  - Current: `Condiviso link`
  - Source: `Link shared`
  - Suggest: `Link condiviso`
  - Source is a confirmation message "Link shared"; Italian requires "Link condiviso" (noun + participle), not the inverted "Condiviso link".

### D. Terminology, register & consistency

- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "URL" is rendered in all caps as "INDIRIZZO", inconsistent with the sibling field label "Nome" and with the term used elsewhere.
  - Current: `INDIRIZZO`
  - Source: `URL`
  - Suggest: `Indirizzo`
  - The source is the field label "URL"; the adjacent label "Name" is translated "Nome" in normal case, so the all-caps form is an unjustified deviation in the same screen.
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "saved cards" translated as "carte di credito salvate", inconsistent with "Carte salvate" elsewhere.
  - Current: `Sblocca per visualizzare le carte di credito salvate`
  - Source: `Unlock to view your saved cards`
  - Suggest: `Sblocca per visualizzare le carte salvate`
  - Source is "Unlock to view your saved cards"; the app consistently uses "carte" (see credit_cards_saved_cards "Carte salvate").
- `dialog_delete_positive` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Delete" is rendered as "Rimuovi" (Remove) while the identical source elsewhere in the same surface uses "Elimina".
  - Current: `Rimuovi`
  - Source: `Delete`
  - Suggest: `Elimina`
  - Source is "Delete"; search_engine_delete and other delete actions in this batch use "Elimina", and "Rimuovi" is the standard rendering of "Remove" (see browser_menu_remove_from_shortcuts), creating an inconsistency.
- `download_languages_item_content_description_downloaded_state` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Delete" is rendered as "Rimuovi" here while the same source term is translated "Elimina" in the neighbouring delete strings.
  - Current: `Rimuovi`
  - Source: `Delete`
  - Suggest: `Elimina`
  - Inconsistent with download_language_all_languages_item_preference_to_delete ("Elimina tutte le lingue") and delete_language_file_dialog_positive_button_text ("Elimina") on the same screen.
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Sync cards" rendered as "carte di credito" while the parallel string uses just "carte".
  - Current: `Sincronizza carte di credito`
  - Source: `Sync cards`
  - Suggest: `Sincronizza carte`
  - Source is "Sync cards" and the sibling string preferences_credit_cards_sync_cards_across_devices uses "le carte"; adding "di credito" is inconsistent with the other card strings (Aggiungi carta, Gestisci carte).
- `sports_widget_final_results_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "World Cup" is rendered as "Mondiali" here but as "Coppa del mondo" in the sibling strings, an inconsistency on the same surface.
  - Current: `Risultati finali dei Mondiali`
  - Source: `World Cup final results`
  - Suggest: `Risultati finali della Coppa del mondo`
  - sports_widget_final_results_page_content_description translates the same source phrase "World Cup final results" as "Risultati finali della Coppa del mondo"; the two accessibility strings for the same page must match.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — Message quotes a button label that does not match the actual button text
  - Current: `Selezionare “Riprova” per passare alla modalità in linea e ricaricare la pagina.`
  - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
  - Suggest: `Selezionare “Riprovare” per passare alla modalità in linea e ricaricare la pagina.`
  - The button on the error page (mozac_browser_errorpages_page_refresh) is labelled "Riprovare"; the message tells the user to press "Riprova", so the quoted label does not exist on screen.

---

## 4. Appendix

### Suppressed as false positives (3)

- **`it-crittare`** (1) — `crittare` and its forms (`critta`, `crittato`) are the correct Italian verb for "to encrypt" — not a typo for `criptare`. Confirmed by the maintainer. Scoped to spelling findings so a mistranslation in the same string still reports.
  - `preferences_credit_cards_save_and_autofill_cards_summary_2`
- **`it-final-exclamation`** (2) — Ending a sentence with `.` where the source ends with `!` is a deliberate register choice; Italian UI text uses the exclamation mark far more sparingly than English. Scoped to typography findings so a real punctuation defect in the same string still reports.
  - `firefox_labs_banner_title_2`, `snackbar_added_to_shortcuts`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (2)

- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — raised by `llm`, withdrawn 2026-08-20
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — raised by `llm`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (33)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_contextmenu_open_image_in_new_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `action_bar_up_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `certificate_warning_push_notification_pnw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `content_description_gallery` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_cfr_tools_reset_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `delete_history_prompt_button_today_and_yesterday` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `download_rename_error_invalid_name_error` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `nova_onboarding_customize_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `radio_preference_info_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `sync_offline` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `sync_sent_tabs_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tab_manager_empty_private_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `content_description_trackers_blocked` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `external_app_prompt_no_app_title` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
