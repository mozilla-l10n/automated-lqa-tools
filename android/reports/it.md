# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `2ecee41489f8` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `2ecee41489f8` |
| **Previous run** | 2026-08-20 @ `2ecee41489f8` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,896 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (46)

- `recent_tabs_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Jump back in" is a section header for resuming recent tabs, but the Italian says "Torna a questa scheda" ("Go back to this tab"), naming a single specific tab.
  - Current: `Torna a questa scheda`
  - Source: `Jump back in`
  - Suggest: `Riprendi da dove eri rimasto`
  - The source is a generic header for the "Jump back in" section on the home screen; the Italian refers to one specific tab ("this tab"), which does not match the header's meaning.
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
- `nova_onboarding_customize_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Title adds a final period not present in the source.
  - Current: `Facile da personalizzare, più privacy a ogni tocco.`
  - Source: `Easy to customize and more private with every tap`
  - Suggest: `Facile da personalizzare, più privacy a ogni tocco`
  - The en-US onboarding title "Easy to customize and more private with every tap" has no terminating period; other onboarding titles in the batch also omit it.
- `preferences_tab_strip` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Tab bar display" is rendered as "Visualizzazione barra delle schede" which reverses the word order/meaning of the preference title.
  - Current: `Visualizzazione barra delle schede`
  - Source: `Tab bar display`
  - Suggest: `Mostra barra delle schede`
  - The developer comment says the preference is for showing the tab strip; the Italian noun phrase is acceptable but ambiguous. Low value.
- `link_shared_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Word order makes the snackbar read as an imperative-ish fragment instead of the past-participle status message "Link shared".
  - Current: `Condiviso link`
  - Source: `Link shared`
  - Suggest: `Link condiviso`
  - Source is a confirmation message "Link shared"; Italian requires "Link condiviso" (noun + participle), not the inverted "Condiviso link".
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "removed" is translated as "eliminato" (deleted), conflicting with the paired option that uses "eliminato" for actual deletion.
  - Current: `Il file viene eliminato dalla cronologia dei download`
  - Source: `File is removed from your download history, but is still saved on your device`
  - Suggest: `Il file viene rimosso dalla cronologia dei download`
  - Source says "is removed from your download history"; the sibling string preferences_downloads_delete_from_device_description uses "eliminato" for "deleted", so using "eliminato" here blurs the distinction between Delete (elimina) and Remove (rimuovi).
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The descriptive summary "Allows Mozilla to install and run studies" is rendered as an imperative addressed to the user.
  - Current: `Consenti a Mozilla di installare e condurre studi`
  - Source: `Allows Mozilla to install and run studies`
  - Suggest: `Consente a Mozilla di installare e condurre studi`
  - The source is a third-person description of what the setting does ("Allows Mozilla…"), not a command to the user; compare preferences_daily_usage_ping_description translated as "Questo consente a Mozilla…".
- `opening_screen_last_tab_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Open on last tab" is rendered as "Apri scheda più recente" (most recent tab) instead of the last open tab, inconsistent with opening_screen_last_tab "Ultima scheda".
  - Current: `Apri scheda più recente`
  - Source: `Open on last tab`
  - Suggest: `Apri ultima scheda`
  - The source says "Open on last tab", matching the option label "Last tab" translated as "Ultima scheda"; "scheda più recente" changes the wording and breaks consistency on the same preference surface.
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "pending" (in attesa) is translated as "in corso" (in progress), conflicting with the distinct in-progress state.
  - Current: `%1$s / %2$s • in corso`
  - Source: `%1$s / %2$s • pending`
  - Suggest: `%1$s / %2$s • in attesa`
  - The source says "pending", meaning the estimated remaining time is still being calculated; "in corso" means "in progress" and duplicates the wording used for download_header_in_progress.
- `download_rename_error_invalid_name_error` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation reverses the meaning: the source says file names cannot contain "/", the target says "/" cannot be used for a file name.
  - Current: `Non è possibile utilizzare “/” per il nome di un file.`
  - Source: `File names can’t use “/”`
  - Suggest: `I nomi dei file non possono contenere “/”.`
  - en-US "File names can’t use “/”" means the character is forbidden inside a file name, not that a name may not consist of it.
- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "URL" is rendered in all caps as "INDIRIZZO", inconsistent with the sibling field label "Nome" and with the term used elsewhere.
  - Current: `INDIRIZZO`
  - Source: `URL`
  - Suggest: `Indirizzo`
  - The source is the field label "URL"; the adjacent label "Name" is translated "Nome" in normal case, so the all-caps form is an unjustified deviation in the same screen.
- `browser_feature_desktop_site_on` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Gender/form inconsistency: "On" toggle state rendered as imperative/feminine "Attiva" while the matching "Off" string uses "Disattivata".
  - Current: `Attiva`
  - Source: `On`
  - Suggest: `Attivata`
  - The pair browser_feature_desktop_site_on/off describes the toggle state; "Attiva" reads as an imperative or adjective mismatching "Disattivata" used for the off state.
- `sync_offline` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Offline" is rendered as "Non in linea" instead of the standard Italian Mozilla term "Non connesso"/"Offline".
  - Current: `Non in linea`
  - Source: `Offline`
  - Suggest: `Non connesso`
  - The sync status label indicates the device/service is offline; Italian Mozilla localization uses "Non connesso" (or keeps "Offline"), not the literal "Non in linea".
- `sync_connect_device_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Translation adds "account" not present in the source ("sign in to Firefox" becomes "accedi all’account Firefox").
  - Current: `accedi all’account Firefox`
  - Source: `To send a tab, sign in to Firefox on at least one other device.`
  - Suggest: `accedi a Firefox`
  - The source says "sign in to Firefox on at least one other device", referring to signing in to the browser, not to an "account Firefox".
- `snackbar_added_to_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Exclamation mark of the source replaced with a full stop.
  - Current: `Aggiunto alle scorciatoie.`
  - Source: `Added to shortcuts!`
  - Source "Added to shortcuts!" ends with an exclamation mark; the Italian ends with a period, altering the punctuation of the source.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "manage font size here" is translated as "gestire la dimensione dei caratteri separatamente" (separately), and the imperative uses formal/infinitive form inconsistent with the informal register.
  - Current: `Disattivare per gestire la dimensione dei caratteri separatamente.`
  - Source: `Font size will match your Android settings. Disable to manage font size here.`
  - Suggest: `Disattiva per gestire la dimensione dei caratteri qui.`
  - The source says to disable the option in order to manage font size "here" (in this screen), not "separately"; the locale also uses the informal imperative.
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "%d addresses" is translated as "%d indirizzi" but the developer comment says it is the number of history items; however the literal source word is "addresses".
  - Current: `%d indirizzi`
  - Source: `%d addresses`
  - Placeholder-level check: source says "addresses" and target says "indirizzi", which matches; no defect.
- `sync_sent_tabs_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Plural "Tabs sent" is rendered in the singular, identical to the singular string sync_sent_tab_snackbar_2.
  - Current: `Scheda inviata`
  - Source: `Tabs sent`
  - Suggest: `Schede inviate`
  - The source is the multi-tab variant ("Tabs sent", shown when multiple tabs have been sent), so the Italian must be plural.
- `delete_history_prompt_button_today_and_yesterday` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Today and yesterday" is rendered with the order reversed as "Ieri e oggi".
  - Current: `Ieri e oggi`
  - Source: `Today and yesterday`
  - Suggest: `Oggi e ieri`
  - The source order is "Today and yesterday"; the Italian inverts the two terms.
- `sign_in_with_email` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Use email instead" is translated as "Accedi con l’email", losing the "instead" contrast.
  - Current: `Accedi con l’email`
  - Source: `Use email instead`
  - Suggest: `Usa invece l’email`
  - The source offers an alternative to camera pairing ("instead"); the Italian drops that meaning.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Help catch trackers" is rendered as an imperative "catch trackers" losing the "help" (contribute to catching) meaning.
  - Current: `Cattura i traccianti`
  - Source: `Help catch trackers`
  - Suggest: `Aiuta a catturare gli elementi traccianti`
  - The source asks the user to help catch trackers; the Italian tells the user to catch them, dropping "help". It also uses "traccianti" instead of the "elementi traccianti" used consistently in the surrounding strings.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "will cause websites to break" weakened to "alcuni siti non funzioneranno" (some sites), mirroring the previous string's "may".
  - Current: `Tutti i cookie (alcuni siti non funzioneranno correttamente)`
  - Source: `All cookies (will cause websites to break)`
  - Suggest: `Tutti i cookie (i siti web non funzioneranno correttamente)`
  - The source distinguishes cookies_3 ("may cause websites to break") from cookies_4 ("will cause websites to break"); the Italian for _4 adds "alcuni", weakening the certainty of the warning.
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Missing adversative conjunction "ma" for the source's "but", leaving two clauses joined only by a comma.
  - Current: `prestazioni più veloci, alcuni siti potrebbero non funzionare correttamente`
  - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
  - Suggest: `prestazioni più veloci, ma alcuni siti potrebbero non funzionare correttamente`
  - The source contrasts the benefit with the drawback via "but"; the Italian drops the conjunction, degrading grammar and losing the contrast.
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The Italian reverses the meaning: it says cookies set to redirect to tracking sites, whereas the source says cookies set by redirects to known tracking sites.
  - Current: `Elimina i cookie impostati per reindirizzare a siti web noti per il tracciamento.`
  - Source: `Clears cookies set by redirects to known tracking websites.`
  - Suggest: `Elimina i cookie impostati dai reindirizzamenti a siti web noti per il tracciamento.`
  - "cookies set by redirects to known tracking websites" means the cookies are set by the redirect process, not that the cookies cause redirection.
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation replaces "make your browsing more private" with "protect your privacy while browsing", changing the wording of the source.
  - Current: `Attiva la VPN per proteggere la tua privacy durante la navigazione e rendere più difficile il tracciamento.`
  - Source: `Turn VPN on to make your browsing more private and harder to trace.`
  - Suggest: `Attiva la VPN per rendere la tua navigazione più privata e difficile da tracciare.`
  - The source says "make your browsing more private and harder to trace"; the same sentence is correctly rendered in ip_protection_onboarding_body_promo as "rendere la tua navigazione più privata e difficile da tracciare", so this variant is both inaccurate and inconsistent.
- `preferences_credit_cards_save_and_autofill_cards_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "critta" is not the correct Italian verb form for "encrypts".
  - Current: `%s critta tutti i metodi di pagamento salvati`
  - Source: `%s encrypts all payment methods you save`
  - Suggest: `%s cripta tutti i metodi di pagamento salvati`
  - The source says "%s encrypts all payment methods you save"; the Italian verb is "criptare" (cripta) or "cifrare" (cifra); "critta" is a misspelling.
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Sync cards" rendered as "carte di credito" while the parallel string uses just "carte".
  - Current: `Sincronizza carte di credito`
  - Source: `Sync cards`
  - Suggest: `Sincronizza carte`
  - Source is "Sync cards" and the sibling string preferences_credit_cards_sync_cards_across_devices uses "le carte"; adding "di credito" is inconsistent with the other card strings (Aggiungi carta, Gestisci carte).
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
- `action_bar_up_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Navigate up" (the action bar back/up navigation) is rendered as "Vai su", which reads as "go up" (or even "go on") rather than navigating back up the hierarchy.
  - Current: `Vai su`
  - Source: `Navigate up`
  - Suggest: `Torna indietro`
  - The developer comment states this is the content description for the action bar "up" button, i.e. navigate back to the parent screen; the sibling string stories_back_button_content_description correctly uses "Torna indietro". "Vai su" is misleading for screen-reader users.
- `radio_preference_info_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Formal/impersonal infinitive "Fare clic" breaks the locale's informal address convention.
  - Current: `Fare clic per ulteriori dettagli`
  - Source: `Click for more details`
  - Suggest: `Tocca per ulteriori dettagli`
  - The it locale uses the informal register; also this is a touch device, where "clic" is inappropriate.
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Translating" (action in progress) is translated as the noun "Traduzione", losing the in-progress meaning.
  - Current: `Traduzione`
  - Source: `Translating`
  - Suggest: `Traduzione in corso`
  - The developer comment says the button text indicates a translation is currently in progress; the accompanying content description uses "Traduzione in corso".
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The quoted preference names are capitalized differently from the source, breaking the match with the actual UI labels.
  - Current: `“Traduci sempre” e “Non tradurre mai”`
  - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
  - Minor: source uses lowercase quoted labels; the Italian labels match the UI strings, so this is acceptable.
- `protection_panel_banner_not_secure_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Your connection" is rendered as "Questa connessione" (this connection).
  - Current: `Questa connessione non è sicura.`
  - Source: `Your connection is not secure.`
  - Suggest: `La tua connessione non è sicura.`
  - The source says "Your connection is not secure."; the possessive was changed to a demonstrative.
- `download_languages_item_content_description_downloaded_state` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Delete" is rendered as "Rimuovi" here while the same source term is translated "Elimina" in the neighbouring delete strings.
  - Current: `Rimuovi`
  - Source: `Delete`
  - Suggest: `Elimina`
  - Inconsistent with download_language_all_languages_item_preference_to_delete ("Elimina tutte le lingue") and delete_language_file_dialog_positive_button_text ("Elimina") on the same screen.
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation says "disconnetterti dal sito" (singular, this site) while the source says it might log you out of websites in general.
  - Current: `potrebbe disconnetterti dal sito o svuotare eventuali carrelli in sospeso`
  - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
  - Suggest: `potrebbe disconnetterti dai siti web e svuotare eventuali carrelli della spesa`
  - en-US: "might log you out of websites and clear shopping carts" — plural "websites" and coordinating "and", not "or" with a singular site.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Debug locales to enable" is rendered as a generic "choice of languages", dropping the "debug" qualifier and mistranslating "locales".
  - Current: `Scelta delle lingue da attivare`
  - Source: `Debug locales to enable`
  - Suggest: `Locale di debug da attivare`
  - The source names the list of debug locales; the translation says "choice of languages" and loses the debug qualifier.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "selected locale" translated as "lingua selezionata" (selected language), inconsistent with the locale terminology in this feature.
  - Current: `per la lingua selezionata`
  - Source: `Add new address for selected locale`
  - Suggest: `per il locale selezionato`
  - The debug feature works with locales (region/format), not languages; source says "locale".
- `debug_drawer_cfr_tools_reset_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Reset CFRs" translated as "Ripristina CFR" where elsewhere reset/override wording differs; "Ripristina" means restore, acceptable, but the plural marker is lost — see rationale.
  - Current: `Ripristina CFR`
  - Source: `Reset CFRs`
  - Suggest: `Reimposta CFR`
  - "Reset" in this debug context means reimpostare/azzerare the CFR state, not restoring a previous state.
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Override" is translated as "Sostituisci" here but as "Sovrascrivi" in the sibling override strings.
  - Current: `Sostituisci regione home in modo permanente`
  - Source: `Override home region permanently`
  - Suggest: `Sovrascrivi regione home in modo permanente`
  - Inconsistent rendering of the same source term "Override" within the same Region Tools surface.
- `certificate_warning_push_notification_pnw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "tomorrow" is rendered as "da domani" (from tomorrow on), altering the meaning slightly but more importantly the source says features will stop working tomorrow.
  - Current: `Alcune funzioni smetteranno di funzionare da domani.`
  - Source: `Some features will stop working tomorrow.`
  - Suggest: `Alcune funzioni smetteranno di funzionare domani.`
  - The source states the features stop working tomorrow; "da domani" adds "starting from", which is not in the source.
- `sports_widget_final_results_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "World Cup" is rendered as "Mondiali" here but as "Coppa del mondo" in the sibling strings, an inconsistency on the same surface.
  - Current: `Risultati finali dei Mondiali`
  - Source: `World Cup final results`
  - Suggest: `Risultati finali della Coppa del mondo`
  - sports_widget_final_results_page_content_description translates the same source phrase "World Cup final results" as "Risultati finali della Coppa del mondo"; the two accessibility strings for the same page must match.
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation drops "above" and renders "active search engine" as "motore di ricerca predefinito" (default search engine).
  - Current: `Disponibile solo se Google è attivo ed è impostato come motore di ricerca predefinito durante la navigazione.`
  - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
  - Suggest: `Disponibile solo se Google è attivo qui sopra ed è il motore di ricerca attivo durante la navigazione.`
  - The source says "enabled above" (referring to the setting above) and "your active search engine", not the default search engine; the Italian changes the meaning.
- `firefox_labs_banner_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The exclamation mark of the source is replaced by a full stop.
  - Current: `Prova le nostre funzioni sperimentali.`
  - Source: `Try our experimental features!`
  - Suggest: `Prova le nostre funzioni sperimentali!`
  - Source ends with "!"; the punctuation of the banner title was changed without reason.
- `content_description_gallery` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Choose from gallery" is rendered as "Seleziona una foto dalla galleria", adding "foto" (photo) which the source does not specify.
  - Current: `Seleziona una foto dalla galleria da inviare a Google Lens`
  - Source: `Choose from gallery to send to Google Lens`
  - Suggest: `Seleziona dalla galleria un’immagine da inviare a Google Lens`
  - The source refers generically to choosing from the gallery (images), not specifically a photo.

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
| apostrophe | `typographic` 173 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 2 | **em** |
| register | `informal` 89, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (47)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 28 |
| 3 | Degraded language (grammar, spelling, terminology) | 15 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `action_bar_up_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Navigate up" (the action bar back/up navigation) is rendered as "Vai su", which reads as "go up" (or even "go on") rather than navigating back up the hierarchy.
  - Current: `Vai su`
  - Source: `Navigate up`
  - Suggest: `Torna indietro`
  - The developer comment states this is the content description for the action bar "up" button, i.e. navigate back to the parent screen; the sibling string stories_back_button_content_description correctly uses "Torna indietro". "Vai su" is misleading for screen-reader users.
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The quoted preference names are capitalized differently from the source, breaking the match with the actual UI labels.
  - Current: `“Traduci sempre” e “Non tradurre mai”`
  - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
  - Minor: source uses lowercase quoted labels; the Italian labels match the UI strings, so this is acceptable.
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
- `certificate_warning_push_notification_pnw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "tomorrow" is rendered as "da domani" (from tomorrow on), altering the meaning slightly but more importantly the source says features will stop working tomorrow.
  - Current: `Alcune funzioni smetteranno di funzionare da domani.`
  - Source: `Some features will stop working tomorrow.`
  - Suggest: `Alcune funzioni smetteranno di funzionare domani.`
  - The source states the features stop working tomorrow; "da domani" adds "starting from", which is not in the source.
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation says "disconnetterti dal sito" (singular, this site) while the source says it might log you out of websites in general.
  - Current: `potrebbe disconnetterti dal sito o svuotare eventuali carrelli in sospeso`
  - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
  - Suggest: `potrebbe disconnetterti dai siti web e svuotare eventuali carrelli della spesa`
  - en-US: "might log you out of websites and clear shopping carts" — plural "websites" and coordinating "and", not "or" with a singular site.
- `content_description_gallery` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Choose from gallery" is rendered as "Seleziona una foto dalla galleria", adding "foto" (photo) which the source does not specify.
  - Current: `Seleziona una foto dalla galleria da inviare a Google Lens`
  - Source: `Choose from gallery to send to Google Lens`
  - Suggest: `Seleziona dalla galleria un’immagine da inviare a Google Lens`
  - The source refers generically to choosing from the gallery (images), not specifically a photo.
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
- `delete_history_prompt_button_today_and_yesterday` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Today and yesterday" is rendered with the order reversed as "Ieri e oggi".
  - Current: `Ieri e oggi`
  - Source: `Today and yesterday`
  - Suggest: `Oggi e ieri`
  - The source order is "Today and yesterday"; the Italian inverts the two terms.
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "pending" (in attesa) is translated as "in corso" (in progress), conflicting with the distinct in-progress state.
  - Current: `%1$s / %2$s • in corso`
  - Source: `%1$s / %2$s • pending`
  - Suggest: `%1$s / %2$s • in attesa`
  - The source says "pending", meaning the estimated remaining time is still being calculated; "in corso" means "in progress" and duplicates the wording used for download_header_in_progress.
- `download_rename_error_invalid_name_error` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation reverses the meaning: the source says file names cannot contain "/", the target says "/" cannot be used for a file name.
  - Current: `Non è possibile utilizzare “/” per il nome di un file.`
  - Source: `File names can’t use “/”`
  - Suggest: `I nomi dei file non possono contenere “/”.`
  - en-US "File names can’t use “/”" means the character is forbidden inside a file name, not that a name may not consist of it.
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The Italian reverses the meaning: it says cookies set to redirect to tracking sites, whereas the source says cookies set by redirects to known tracking sites.
  - Current: `Elimina i cookie impostati per reindirizzare a siti web noti per il tracciamento.`
  - Source: `Clears cookies set by redirects to known tracking websites.`
  - Suggest: `Elimina i cookie impostati dai reindirizzamenti a siti web noti per il tracciamento.`
  - "cookies set by redirects to known tracking websites" means the cookies are set by the redirect process, not that the cookies cause redirection.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Help catch trackers" is rendered as an imperative "catch trackers" losing the "help" (contribute to catching) meaning.
  - Current: `Cattura i traccianti`
  - Source: `Help catch trackers`
  - Suggest: `Aiuta a catturare gli elementi traccianti`
  - The source asks the user to help catch trackers; the Italian tells the user to catch them, dropping "help". It also uses "traccianti" instead of the "elementi traccianti" used consistently in the surrounding strings.
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation replaces "make your browsing more private" with "protect your privacy while browsing", changing the wording of the source.
  - Current: `Attiva la VPN per proteggere la tua privacy durante la navigazione e rendere più difficile il tracciamento.`
  - Source: `Turn VPN on to make your browsing more private and harder to trace.`
  - Suggest: `Attiva la VPN per rendere la tua navigazione più privata e difficile da tracciare.`
  - The source says "make your browsing more private and harder to trace"; the same sentence is correctly rendered in ip_protection_onboarding_body_promo as "rendere la tua navigazione più privata e difficile da tracciare", so this variant is both inaccurate and inconsistent.
- `opening_screen_last_tab_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Open on last tab" is rendered as "Apri scheda più recente" (most recent tab) instead of the last open tab, inconsistent with opening_screen_last_tab "Ultima scheda".
  - Current: `Apri scheda più recente`
  - Source: `Open on last tab`
  - Suggest: `Apri ultima scheda`
  - The source says "Open on last tab", matching the option label "Last tab" translated as "Ultima scheda"; "scheda più recente" changes the wording and breaks consistency on the same preference surface.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "manage font size here" is translated as "gestire la dimensione dei caratteri separatamente" (separately), and the imperative uses formal/infinitive form inconsistent with the informal register.
  - Current: `Disattivare per gestire la dimensione dei caratteri separatamente.`
  - Source: `Font size will match your Android settings. Disable to manage font size here.`
  - Suggest: `Disattiva per gestire la dimensione dei caratteri qui.`
  - The source says to disable the option in order to manage font size "here" (in this screen), not "separately"; the locale also uses the informal imperative.
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
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "%d addresses" is translated as "%d indirizzi" but the developer comment says it is the number of history items; however the literal source word is "addresses".
  - Current: `%d indirizzi`
  - Source: `%d addresses`
  - Placeholder-level check: source says "addresses" and target says "indirizzi", which matches; no defect.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "removed" is translated as "eliminato" (deleted), conflicting with the paired option that uses "eliminato" for actual deletion.
  - Current: `Il file viene eliminato dalla cronologia dei download`
  - Source: `File is removed from your download history, but is still saved on your device`
  - Suggest: `Il file viene rimosso dalla cronologia dei download`
  - Source says "is removed from your download history"; the sibling string preferences_downloads_delete_from_device_description uses "eliminato" for "deleted", so using "eliminato" here blurs the distinction between Delete (elimina) and Remove (rimuovi).
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The translation drops "above" and renders "active search engine" as "motore di ricerca predefinito" (default search engine).
  - Current: `Disponibile solo se Google è attivo ed è impostato come motore di ricerca predefinito durante la navigazione.`
  - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
  - Suggest: `Disponibile solo se Google è attivo qui sopra ed è il motore di ricerca attivo durante la navigazione.`
  - The source says "enabled above" (referring to the setting above) and "your active search engine", not the default search engine; the Italian changes the meaning.
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
- `sync_sent_tabs_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Plural "Tabs sent" is rendered in the singular, identical to the singular string sync_sent_tab_snackbar_2.
  - Current: `Scheda inviata`
  - Source: `Tabs sent`
  - Suggest: `Schede inviate`
  - The source is the multi-tab variant ("Tabs sent", shown when multiple tabs have been sent), so the Italian must be plural.
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
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Missing adversative conjunction "ma" for the source's "but", leaving two clauses joined only by a comma.
  - Current: `prestazioni più veloci, alcuni siti potrebbero non funzionare correttamente`
  - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
  - Suggest: `prestazioni più veloci, ma alcuni siti potrebbero non funzionare correttamente`
  - The source contrasts the benefit with the drawback via "but"; the Italian drops the conjunction, degrading grammar and losing the contrast.
- `preferences_credit_cards_save_and_autofill_cards_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "critta" is not the correct Italian verb form for "encrypts".
  - Current: `%s critta tutti i metodi di pagamento salvati`
  - Source: `%s encrypts all payment methods you save`
  - Suggest: `%s cripta tutti i metodi di pagamento salvati`
  - The source says "%s encrypts all payment methods you save"; the Italian verb is "criptare" (cripta) or "cifrare" (cifra); "critta" is a misspelling.

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
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Override" is translated as "Sostituisci" here but as "Sovrascrivi" in the sibling override strings.
  - Current: `Sostituisci regione home in modo permanente`
  - Source: `Override home region permanently`
  - Suggest: `Sovrascrivi regione home in modo permanente`
  - Inconsistent rendering of the same source term "Override" within the same Region Tools surface.
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
- `radio_preference_info_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Formal/impersonal infinitive "Fare clic" breaks the locale's informal address convention.
  - Current: `Fare clic per ulteriori dettagli`
  - Source: `Click for more details`
  - Suggest: `Tocca per ulteriori dettagli`
  - The it locale uses the informal register; also this is a touch device, where "clic" is inappropriate.
- `sports_widget_final_results_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "World Cup" is rendered as "Mondiali" here but as "Coppa del mondo" in the sibling strings, an inconsistency on the same surface.
  - Current: `Risultati finali dei Mondiali`
  - Source: `World Cup final results`
  - Suggest: `Risultati finali della Coppa del mondo`
  - sports_widget_final_results_page_content_description translates the same source phrase "World Cup final results" as "Risultati finali della Coppa del mondo"; the two accessibility strings for the same page must match.
- `sync_offline` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Offline" is rendered as "Non in linea" instead of the standard Italian Mozilla term "Non connesso"/"Offline".
  - Current: `Non in linea`
  - Source: `Offline`
  - Suggest: `Non connesso`
  - The sync status label indicates the device/service is offline; Italian Mozilla localization uses "Non connesso" (or keeps "Offline"), not the literal "Non in linea".

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — Message quotes a button label that does not match the actual button text
  - Current: `Selezionare “Riprova” per passare alla modalità in linea e ricaricare la pagina.`
  - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
  - Suggest: `Selezionare “Riprovare” per passare alla modalità in linea e ricaricare la pagina.`
  - The button on the error page (mozac_browser_errorpages_page_refresh) is labelled "Riprovare"; the message tells the user to press "Riprova", so the quoted label does not exist on screen.
- `firefox_labs_banner_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — The exclamation mark of the source is replaced by a full stop.
  - Current: `Prova le nostre funzioni sperimentali.`
  - Source: `Try our experimental features!`
  - Suggest: `Prova le nostre funzioni sperimentali!`
  - Source ends with "!"; the punctuation of the banner title was changed without reason.
- `nova_onboarding_customize_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Title adds a final period not present in the source.
  - Current: `Facile da personalizzare, più privacy a ogni tocco.`
  - Source: `Easy to customize and more private with every tap`
  - Suggest: `Facile da personalizzare, più privacy a ogni tocco`
  - The en-US onboarding title "Easy to customize and more private with every tap" has no terminating period; other onboarding titles in the batch also omit it.
- `snackbar_added_to_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Exclamation mark of the source replaced with a full stop.
  - Current: `Aggiunto alle scorciatoie.`
  - Source: `Added to shortcuts!`
  - Source "Added to shortcuts!" ends with an exclamation mark; the Italian ends with a period, altering the punctuation of the source.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (12)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_contextmenu_open_image_in_new_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tab_manager_empty_private_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `content_description_trackers_blocked` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `external_app_prompt_no_app_title` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
