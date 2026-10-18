# Android l10n QA — ro

| | |
|---|---|
| **Generated** | 2026-10-18 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **Previous run** | 2026-10-16 @ `4d7697d1b89b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 2,798 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ro: [firefox_ios](firefox_ios.md)

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
| Files | 45 |
| Strings | 2,798 |
| Missing strings | 4 |
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

**4 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 18 | **polish-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (91)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — The translation says entered data "will not be saved" where the source says it "may not be saved".
    - Current: `nu vor fi salvate`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `s-ar putea să nu fie salvate`
    - The en-US "may not be saved" only warns of a possible data loss. The ro states it as certain, which overstates what happens to the user's data.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 30 |
| 3 | Degraded language (grammar, spelling, terminology) | 53 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_feature_addons_permissions_dialog_heading_required_data_collection` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — The heading reads as "collection of the required data" rather than "data collection that is required".
    - Current: `Colectarea datelor necesare:`
    - Source: `Required data collection:`
    - Suggest: `Colectare de date necesară:`
    - In the source, "Required" describes the data collection (it is mandatory for the add-on). In the Romanian, "necesare" attaches to "datelor", so it says the data is required. The parallel heading for optional collection is rendered "Colectare nouă de date".
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — 'utilizarea extensiei' (use of the extension, singular) narrows 'extension usage', which refers to extensions generally.
    - Current: `utilizarea extensiei`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `utilizarea extensiilor`
    - The management permission covers monitoring the usage of all extensions, and the non-update string says 'utilizarea de extensii'. The singular suggests a single extension.
- `switch_to_tab_description` — `mozilla-mobile/android-components/components/feature/awesomebar/src/main/res/values-ro/strings.xml` — "Switch to tab" is rendered as "Switch to another tab", which is vague for a suggestion that stands for one particular open tab.
    - Current: `Treci la o altă filă`
    - Source: `Switch to tab`
    - Suggest: `Treci la filă`
    - The comment says this text describes a suggestion for one specific open tab. "o altă filă" (another tab) adds an indefinite "other" that the source doesn't have.
- `mozac_feature_downloads_time_remaining_unknown` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ro/strings.xml` — "oră necunoscută" means "unknown hour" (a time of day), but the string needs to say the remaining duration is unknown.
    - Current: `oră necunoscută`
    - Source: `unknown time`
    - Suggest: `timp necunoscut`
    - The developer comment says this replaces the estimated time remaining on an in-progress download, so it means an unknown duration. "Oră" refers to an hour or a time on the clock, not an amount of time; "timp" is the right word.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — The translation says entered data "will not be saved" where the source says it "may not be saved".
    - Current: `nu vor fi salvate`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `s-ar putea să nu fie salvate`
    - The en-US "may not be saved" only warns of a possible data loss. The ro states it as certain, which overstates what happens to the user's data.
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — 'crearea' (creating) misrenders 'entering'; the label is for typing text into a field, not for creating one.
    - Current: `crearea unui câmp de introducere text`
    - Source: `Label for entering a text input field`
    - Suggest: `introducerea textului într-un câmp de text`
    - The source and the developer comment describe a label for the field where the user enters text in a prompt. The translation says the label is for creating a field.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ro/strings.xml` — The relative clause says the user controls the pages rather than the summaries.
    - Current: `să rezume pagini pe care le controlezi tu`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `să creeze rezumate ale paginilor care rămân sub controlul tău`
    - The source says the generated summaries stay in the user's control. In the ro, 'pe care le controlezi tu' attaches to 'pagini', so it reads as summarizing pages that the user controls.
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ro/strings.xml` — "crash" is translated as "accidente" (physical accidents) instead of a software crash term.
    - Current: `datelor despre accidente`
    - Source: `Gathering crash data`
    - Suggest: `datelor despre defecțiuni`
    - In Romanian, "accidente" means road or physical accidents, not an app crash. The neighbouring strings in the same component use "defecțiune".
- `a11y_completed_task_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The singular "Completed task" is rendered in the plural.
    - Current: `Sarcini finalizate`
    - Source: `Completed task`
    - Suggest: `Sarcină finalizată`
    - The comment says this describes a check mark on a single completed task, but "Sarcini finalizate" means "completed tasks".
- `add_to_exiting_tab_group_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The few variant makes the group and the color plural, but the count is the number of tabs.
    - Current: `Adaugă la %1$s grupuri de file, %2$d file, culorile %3$s`
    - Source: `{$quantity ->} [one] Add to %1$s tab group, %2$d tab, color %3$s [other] Add to %1$s tab group, %2$d tabs, color %3$s`
    - Suggest: `Adaugă la grupul de file %1$s, %2$d file, culoarea %3$s`
    - In the source, the quantity only controls "tab/tabs". There is still one group (%1$s) with one color (%3$s), so "grupuri" and "culorile" are wrong.
- `add_to_exiting_tab_group_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The other variant makes the group and the color plural, but the count is the number of tabs.
    - Current: `Adaugă la %1$s de grupuri de file, %2$d de file, culorile %3$s`
    - Source: `{$quantity ->} [one] Add to %1$s tab group, %2$d tab, color %3$s [other] Add to %1$s tab group, %2$d tabs, color %3$s`
    - Suggest: `Adaugă la grupul de file %1$s, %2$d de file, culoarea %3$s`
    - In the source, the quantity only controls "tabs". The group name and its color are singular, and "de" after the group name is wrong.
- `addons_permissions_heading_required_data_collection` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The heading reads "collection of the required data" instead of "required data collection". In English, "required" describes the collection, not the data.
    - Current: `Colectarea datelor necesare:`
    - Source: `Required data collection:`
    - Suggest: `Colectare de date necesară:`
    - The section lists data collection that is required (as opposed to the optional section). In the Romanian, "necesare" agrees with "datelor", so it says the data are what is required.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Post town" is translated as "Oficiu poștal", which means "post office", not the town used for postal addressing.
    - Current: `Oficiu poștal`
    - Source: `Post town`
    - Suggest: `Localitate poștală`
    - A UK/Norway/Sweden post town is a town or locality name in the address, not a post office. The label would make users enter the wrong information.
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The artist handle is misspelled as @heyheymodraws instead of @heyheymomodraws.
    - Current: `@heyheymodraws`
    - Source: `Created by @heyheymomodraws`
    - Suggest: `@heyheymomodraws`
    - The source and the developer comment both give the handle as @heyheymomodraws. The translation drops a 'mo', so the credit points to the wrong account.
- `automatic_translation_option_offer_to_translate_title_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The option label is rendered as the noun 'Translation offer' instead of the action 'Offer to translate'.
    - Current: `Ofertă de traducere`
    - Source: `Offer to translate (default)`
    - Suggest: `Oferă traducerea`
    - This radio option describes the browser's behaviour ('offer to translate'), and its siblings use verbs ('Tradu întotdeauna', 'Nu tradu niciodată'). 'Ofertă de traducere' reads like a commercial offer.
- `browser_menu_signed_in_caption` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Translation adds "files" (fișierele), which the source doesn't mention, and the phrasing makes "sync" read as a separate command.
    - Current: `Gestionează fișierele pentru care faci backup și sincronizează`
    - Source: `Manage what you back up and sync`
    - Suggest: `Gestionează ce salvezi și sincronizezi`
    - Source means 'Manage what you back up and sync' (data such as passwords and bookmarks); the ro speaks of 'files for which you make backup' and 'sincronizează' reads ambiguously as a separate command.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Debug" is translated as an imperative verb, so the header reads "Debug the locales for activation" instead of "Debug locales to enable".
    - Current: `Depanează setările regionale pentru activare`
    - Source: `Debug locales to enable`
    - Suggest: `Setări regionale de depanare de activat`
    - The comment says this is a header over a list of debug locales that can be enabled or disabled. "Debug" describes the locales; it is not a command.
- `download_item_in_progress_description_unknown_total_size` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "unknown time" (unknown remaining duration) is rendered as "oră necunoscută", which means an unknown clock time.
    - Current: `oră necunoscută`
    - Source: `%1$s • unknown time`
    - Suggest: `timp necunoscut`
    - The developer comment says the estimated time remaining for the download is unknown. "Oră" refers to a clock time or an hour, not a duration, so the Romanian text says something different; "timp" is the word for an amount of time.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The category title reads as "The redirection of trackers" instead of naming a type of tracker.
    - Current: `Redirecționarea elementelor de urmărire`
    - Source: `Redirect Trackers`
    - Suggest: `Elemente de urmărire prin redirecționare`
    - The comment says this is a category of trackers (redirect trackers). The translation describes an action instead.
- `expanded_tab_group_header_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The [few] and [other] variants make the group plural ("groups"), but the count applies only to tabs.
    - Current: `[few] %1$s grupuri de file cu %2$d file, culoarea %3$s [other] %1$s de grupuri de file cu %2$d de file, culoarea %3$s`
    - Source: `{$quantity ->} [one] %1$s tab group with %2$d tab, color %3$s [other] %1$s tab group with %2$d tabs, color %3$s`
    - Suggest: `[few] %1$s grup de file cu %2$d file, culoarea %3$s [other] %1$s grup de file cu %2$d de file, culoarea %3$s`
    - The source describes one tab group containing N tabs. The translation says multiple groups and puts "de" wrongly after the group name.
- `felt_privacy_info_card_subtitle_3` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "private tabs" is translated as "private windows".
    - Current: `toate ferestrele private`
    - Source: `%1$s deletes your cookies, history, and site data when you close all your private tabs.`
    - Suggest: `toate filele private`
    - The source says private tabs. Elsewhere in the batch, tabs are "file" and "ferestre" means windows.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "through %1$s" (until the date) is rendered as "prin %1$s" (by means of), so the end date of the promotion is lost.
    - Current: `prin %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `până pe %1$s`
    - Per the developer comment, %1$s is the end date of the promotional period, so "through" here means "until". "Prin" means "through/via", which makes no sense with a date and doesn't say when the promotion ends.
- `logins_warning_dialog_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Translation adds "login data" to what is protected; source only mentions saved passwords.
    - Current: `datele de autentificare și parolele salvate`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved passwords from being accessed if someone else has your device.`
    - Suggest: `parolele salvate`
    - en-US says 'to protect your saved passwords'; the Romanian extends this to 'your login data and saved passwords', content not in the source.
- `onboarding_redesign_tou_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The Romanian says 'the latest version of the Android browser' where the source says 'the ultimate Android browser'.
    - Current: `Lansează ultima versiune a browserului Android`
    - Source: `Launch the ultimate Android browser`
    - Suggest: `Lansează browserul Android suprem`
    - 'Ultimate' here means the best possible browser. 'Ultima versiune' means the latest release, which is a different claim.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — This confirm button reads as the noun phrase 'opened tabs' instead of the action 'open tabs'.
    - Current: `File deschise`
    - Source: `Open tabs`
    - Suggest: `Deschide filele`
    - The developer comment says this button confirms opening all tabs, so it needs a verb. 'File deschise' means 'open (opened) tabs'.
- `open_all_warning_message` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The app name is in the wrong place, so the sentence says the tabs slow down 'the time' instead of the app, and 'în ce' is ungrammatical.
    - Current: `Deschiderea atâtor %s file poate încetini timpul în ce paginile se încarcă.`
    - Source: `Opening this many tabs may slow down %s while the pages are loading. Are you sure you want to continue?`
    - Suggest: `Deschiderea atâtor file poate încetini %s în timp ce paginile se încarcă.`
    - In the source, %s (the app name) is what gets slowed down. Here the app name describes the tabs ('so many Firefox tabs'), the thing slowed is 'timpul' (the time), and 'în ce' should be 'în timp ce' (while).
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Allows" is translated as "Ajută" (helps) instead of "Permite" (allows).
    - Current: `Ajută Mozilla să instaleze`
    - Source: `Allows Mozilla to install and run studies`
    - Suggest: `Permite Mozilla să instaleze`
    - The source describes a toggle that grants Mozilla permission to install and run studies. "Ajută" means "helps", which loses the permission meaning.
- `preferences_customize_extension_collection` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The adjective "personalizate" agrees with "extensii", so the string says the extensions are custom instead of the collection.
    - Current: `Colecție de extensii personalizate`
    - Source: `Custom extension collection`
    - Suggest: `Colecție personalizată de extensii`
    - The source means a custom (user-configured) AMO collection. The plural feminine "personalizate" modifies "extensii" and gives "collection of customized extensions". The singular "personalizată" has to follow "Colecție".
- `preferences_downloads_ask_when_to_delete_files` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Translation means 'Ask when the files should be deleted' instead of 'Ask when I delete files'.
    - Current: `Întreabă când să se șteargă fișierele`
    - Source: `Ask when I delete files`
    - Suggest: `Întreabă când șterg fișiere`
    - The source option means the app asks the user something at the moment they delete a file. It does not ask the user when deletion should happen, which is what the Romanian says.
- `recent_tabs_synced_device_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Singular "Synced device" rendered in the plural as "devices".
    - Current: `Dispozitive sincronizate`
    - Source: `Synced device`
    - Suggest: `Dispozitiv sincronizat`
    - The source and comment describe the icon for a single synced device; the translation says "synced devices", so screen readers announce the wrong number.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Search settings" (verb) is translated as a noun phrase meaning "settings for search".
    - Current: `Setări de căutare`
    - Source: `Search settings`
    - Suggest: `Caută în setări`
    - The developer comment says "Search" is a verb here: the title of a screen for searching through the settings. "Setări de căutare" means "search settings", i.e. settings for the search engine.
- `setup_checklist_subtitle_3_steps_second_step` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Finished" is dropped, so the sentence says "two steps and one more" instead of "two steps finished and one to go".
    - Current: `Doi pași și mai e unul.`
    - Source: `Almost there! Two steps finished and 1 to go.`
    - Suggest: `Doi pași finalizați și mai e unul.`
    - The source says two steps are finished. Without that word the Romanian doesn't say the steps are done.
- `wallpaper_artist_series_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Seria artistului" names a single artist's series, while the source names a collection made with several artists.
    - Current: `Seria artistului`
    - Source: `Artist series`
    - Suggest: `Seria artiștilor`
    - The developer comment says "Artist series" is a collection of wallpapers made in collaboration with artists. The singular genitive "artistului" makes it one artist's series.
- `webcompat_reporter_preview_report` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Button label for previewing the report is rendered as a noun phrase meaning 'a preview-type report' instead of an action.
    - Current: `Raport de previzualizare`
    - Source: `Preview Report`
    - Suggest: `Previzualizează raportul`
    - The developer comment says this is a button to view a preview of the report; 'Raport de previzualizare' means 'report of preview', not the action 'Preview the report'.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ro/strings.xml` — The genitive after the %2$s placeholder (the archive service's name) has no possessive article, so the phrase is ungrammatical.
    - Current: `din %2$s Arhivei Internet`
    - Source: `%1$s can look for an earlier version of this page from the Internet Archive’s %2$s.`
    - Suggest: `din %2$s al Arhivei Internet`
    - %2$s is a proper name with no article (the archive service's name), so the genitive that follows it needs the possessive article "al". As written, "din %2$s Arhivei Internet" is broken Romanian for "from the Internet Archive's %2$s".
- `mozac_feature_addons_migrated_from_a_previous_version_label` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — The genitive article is missing before the app name, so "o versiune anterioară %1$s" is ungrammatical.
    - Current: `de la o versiune anterioară %1$s`
    - Source: `This add-on was migrated from a previous version of %1$s`
    - Suggest: `de la o versiune anterioară a %1$s`
    - The source says "a previous version of %1$s". In Romanian, a genitive after an indefinite noun phrase needs the possessive article "a". Without it the app name just hangs after the noun.
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — The adjective 'acceptat' agrees with 'verificator' instead of 'suplimente', so the phrase reads as 'accepted checker' rather than 'checker for supported add-ons'.
    - Current: `Verificator de suplimente acceptat`
    - Source: `Supported add-ons checker`
    - Suggest: `Verificator de suplimente acceptate`
    - In the source, 'supported' describes the add-ons. In Romanian the adjective must be feminine plural ('acceptate') to agree with 'suplimente'. The masculine singular 'acceptat' attaches it to 'verificator'.
- `mozac_feature_prompts_clear` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Uses the cedilla letter 'Ş' instead of the correct Romanian comma-below 'Ș'.
    - Current: `Şterge`
    - Source: `Clear`
    - Suggest: `Șterge`
    - Correct Romanian spelling uses ș (comma below). The rest of the batch uses the comma form.
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Misspelled verb with 'â' instead of 'ă', and the wording doesn't match the sibling strings, which use 'Extinde'.
    - Current: `Expandeazâ`
    - Source: `Expand saved passwords`
    - Suggest: `Extinde`
    - 'Expandeazâ' is misspelled (the ending should be 'ă'). The other expand content descriptions in this prompt use 'Extinde'.
- `mozac_feature_prompts_manage_logins_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Misspelling: "â" used instead of "ă" in the verb ending.
    - Current: `Gestioneazâ`
    - Source: `Manage passwords`
    - Suggest: `Gestionează`
    - The correct Romanian imperative is "Gestionează". "â" is a different letter, so the word is misspelled.
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Misspelled demonstrative: "acestă" should be "această".
    - Current: `acestă pagină`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `această pagină`
    - The feminine demonstrative in Romanian is spelled "această". "acestă" is not a word.
- `mozac_feature_prompts_save_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Command-form verb used in a yes/no question; it should be the question form, as in the sibling titles.
    - Current: `Salvează securizat acest card?`
    - Source: `Securely save this card?`
    - Suggest: `Salvezi securizat acest card?`
    - The source is a question ("Securely save this card?"). "Salvează" is a command, which doesn't fit a question mark. The sibling title "Salvezi adresa?" uses the question form.
- `mozac_feature_prompts_set_time` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Misspelling: "â" used instead of "ă" in the verb ending.
    - Current: `Seteazâ`
    - Source: `Set time`
    - Suggest: `Setează`
    - The correct Romanian imperative is "Setează". "â" is a different letter, so the word is misspelled.
- `mozac_feature_prompts_update_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — Command-form verb used in a yes/no question; it should be the question form, as in the sibling titles.
    - Current: `Actualizează data de expirare a cardului?`
    - Source: `Update card expiration date?`
    - Suggest: `Actualizezi data de expirare a cardului?`
    - The source is a question ("Update card expiration date?"). "Actualizează" is a command, which doesn't fit a question mark. The sibling title "Actualizezi adresa?" uses the question form.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ro/strings.xml` — The placeholder holds the service name "Firefox Relay", but the translation treats it as a count, adding the numeral connector "(de)" and making the sentence ungrammatical.
    - Current: `Acum sunt disponibile %s (de) măști de e-mail pe mobil.`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `Măștile de e-mail %s sunt acum disponibile pe mobil.`
    - The developer comment says %s is "Firefox Relay". On screen this reads "disponibile Firefox Relay (de) măști de e-mail": "(de)" goes only between a number and a noun, so the result is broken Romanian.
- `add_to_exiting_tab_group_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Misspelling "coloarea" instead of "culoarea".
    - Current: `coloarea %3$s`
    - Source: `{$quantity ->} [one] Add to %1$s tab group, %2$d tab, color %3$s [other] Add to %1$s tab group, %2$d tabs, color %3$s`
    - Suggest: `culoarea %3$s`
    - The Romanian word for "color" is "culoare", so with the article it is "culoarea". "coloarea" is not a word.
- `bookmark_add_folder` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The screen title uses the definite form 'dosarul' ('the folder') for the generic 'Add folder'.
    - Current: `Adaugă dosarul`
    - Source: `Add folder`
    - Suggest: `Adaugă dosar`
    - The source is a generic screen title for creating a new folder. The definite article makes it read as adding a specific, already-known folder.
- `browser_menu_translated` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The adjective is plural ("Traduse") but it refers to the single current page (feminine singular).
    - Current: `Traduse`
    - Source: `Translated`
    - Suggest: `Tradusă`
    - The label indicates the current page (pagina, feminine singular) has been translated; the plural form does not agree.
- `debug_drawer_addons_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Two nouns are placed side by side with no genitive or preposition, which is ungrammatical and can be read as "supplementary tools".
    - Current: `Instrumente suplimente`
    - Source: `Add-ons Tools`
    - Suggest: `Instrumente pentru suplimente`
    - "Add-ons Tools" means tools for add-ons. Romanian needs a preposition or genitive to link the two nouns.
- `inactive_tabs_auto_close_message_action` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The direct object of the imperative is missing its definite article.
    - Current: `PORNEȘTE ÎNCHIDERE AUTOMATĂ`
    - Source: `TURN ON AUTO CLOSE`
    - Suggest: `PORNEȘTE ÎNCHIDEREA AUTOMATĂ`
    - In Romanian, a specific noun used as the object of "pornește" needs the definite article ("închiderea"). Without it the phrase is ungrammatical.
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The verb needs the reflexive form; "Resetează" without "se" reads as an order or as a verb acting on an object.
    - Current: `Resetează la`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `Se resetează la`
    - In the source, "Resets" means the allowance resets by itself. Romanian needs the reflexive "se resetează" for that meaning.
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The plural "Recomandate" labels a single location option.
    - Current: `Recomandate`
    - Source: `Recommended`
    - Suggest: `Recomandată`
    - The label marks one automatic location option, so the adjective should be singular and agree with "locație".
- `library_item_selected_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The screen-reader label for a single selected item uses the plural feminine "Selectate" instead of the singular.
    - Current: `Selectate`
    - Source: `Selected`
    - Suggest: `Selectat`
    - The comment says this describes the check mark on one selected item. A singular form ("Selectat") is needed, not a plural.
- `likert_scale_option_4` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Uses cedilla ţ instead of the correct comma-below ț, inconsistent with sibling options.
    - Current: `Nemulţumit(ă)`
    - Source: `Dissatisfied`
    - Suggest: `Nemulțumit(ă)`
    - Romanian orthography uses ț (comma below); the other likert options use ț correctly.
- `onboarding_redesign_tou_body_one_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Link text lacks the definite article, so the composed sentence reads "ești de acord cu Condiții de utilizare Firefox" and differs from the parallel nova string.
    - Current: `Condiții de utilizare Firefox`
    - Source: `Firefox Terms of Use`
    - Suggest: `Condițiile de utilizare Firefox`
    - The text is inserted into "Prin continuare, ești de acord cu %1$s.", where Romanian needs the article ("the Firefox Terms of Use"). The equivalent nova_onboarding_tou_body_line_1_link_text already uses "Condițiile de utilizare Firefox".
- `preference_doh_default_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The verb is in the second person, so the sentence says the user protects their privacy instead of the app protecting it.
    - Current: `ca să-ți protejezi confidențialitatea`
    - Source: `%1$s decides when to use secure DNS to protect your privacy.`
    - Suggest: `ca să-ți protejeze confidențialitatea`
    - In the source, %1$s (the app) decides when to use secure DNS to protect your privacy. "să-ți protejezi" is second person and changes who does the protecting. The verb should be third person to agree with %1$s.
- `preference_doh_max_protection` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "max" is a cut-off English-style abbreviation and doesn't agree in Romanian.
    - Current: `Protecție max`
    - Source: `Max Protection`
    - Suggest: `Protecție maximă`
    - The English "Max" is short for "Maximum". In Romanian the adjective has to agree with the feminine noun: "maximă". This also matches "Protecție sporită" on the same screen.
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Misspelling: "urmării" (genitive of "urmare", consequence) is used instead of "urmăririi" (tracking).
    - Current: `împotriva urmării`
    - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
    - Suggest: `împotriva urmăririi`
    - "Tracking protection" needs the genitive of "urmărire", which is "urmăririi", as the sibling strings use. "urmării" is a different word.
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The modifier "inter-site" has wrongly been given a plural ending, producing the ungrammatical "inter-site-uri".
    - Current: `Cookie-uri inter-site-uri`
    - Source: `Cross-site cookies`
    - Suggest: `Cookie-uri inter-site`
    - "Cross-site" is an invariable modifier. Adding the plural noun ending "-uri" to it is a grammar error in Romanian; it should read "Cookie-uri inter-site" (or "între site-uri").
- `preferences_https_only_in_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Misspelled verb: "Activeză" instead of "Activează".
    - Current: `Activeză`
    - Source: `Enable only in private tabs`
    - Suggest: `Activează`
    - Spelling error; the sibling string uses the correct form "Activează".
- `preferences_tab_groups_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The imperative of "a organiza" is misspelled as "Organiză-ți" instead of "Organizează-ți".
    - Current: `Organiză-ți`
    - Source: `Organize your tabs into groups you can name and save.`
    - Suggest: `Organizează-ți`
    - The verb "a organiza" uses the -ează ending in the 2nd person singular imperative ("organizează"). "Organiză" is not a valid form.
- `saved_login_reveal_password` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Misspelled verb "Afișeză" instead of "Afișează".
    - Current: `Afișeză`
    - Source: `Show password`
    - Suggest: `Afișează`
    - The correct imperative form of "a afișa" is "Afișează", which is the spelling used elsewhere in this batch (e.g. "Afișează toate").
- `send_to_devices_device_selected_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Feminine plural "Selectate" is used for a single selected device.
    - Current: `Selectate`
    - Source: `Selected`
    - Suggest: `Selectat`
    - Screen readers announce this when one device is selected. "Dispozitiv" is neuter singular, so it takes the masculine singular form "Selectat".
- `sync_scan_code` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The verb is misspelled "Scananează"; the correct form is "Scanează".
    - Current: `Scananează`
    - Source: `Scan the code`
    - Suggest: `Scanează`
    - The Romanian verb "a scana" conjugates to "scanează" in the 2nd person imperative. The extra syllable "na" is a typo.
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Article and suffix agreement break when the placeholders expand to the feminine/plural link texts.
    - Current: `Am introdus un %1$s %2$s și am actualizat %3$s-ul nostru.`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `Am introdus Condițiile de utilizare %1$s și am actualizat %3$s.`
    - %2$s is "Condiții de utilizare" (feminine plural) and %3$s is "Politică de confidențialitate" (feminine). The output reads "un Firefox Condiții de utilizare" and "Politică de confidențialitate-ul nostru", which are both ungrammatical.
- `terms_of_use_prompt_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The reflexive pronoun is missing in the idiom for "take a moment".
    - Current: `Acordă un moment`
    - Source: `Please take a moment to review and accept. %1$s.`
    - Suggest: `Acordă-ți un moment`
    - "Take a moment" is idiomatically "Acordă-ți un moment". Without the pronoun, "Acordă un moment" is an incomplete phrase.
- `trackers_blocked_panel_num_social_media_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — The singular form uses the plural genitive article "ale" after the singular noun "element".
    - Current: `%1$d element de urmărire ale rețelelor de socializare`
    - Source: `{$quantity ->} [one] %1$d social media tracker [other] %1$d social media trackers`
    - Suggest: `%1$d element de urmărire al rețelelor de socializare`
    - The masculine/neuter singular "element" needs the singular genitive article "al". "Ale" is plural, which only fits the few/other forms.
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "foaia traduceri" is ungrammatical because nothing links "traduceri" to "foaia".
    - Current: `Închide foaia traduceri`
    - Source: `Close Translations sheet`
    - Suggest: `Închide foaia de traduceri`
    - Romanian needs either a preposition ("foaia de traduceri") or a genitive ("foaia traducerilor") here. A bare indefinite plural cannot modify the noun directly.
- `webcompat_reporter_edit_url_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — 'siteului' is misspelled; the inflected form of the loanword needs a hyphen ('site-ului'), as used elsewhere ('Site-ul').
    - Current: `siteului`
    - Source: `Edit website URL`
    - Suggest: `site-ului`
    - Romanian norms (DOOM) write inflected forms of 'site' with a hyphen; the same batch uses 'Site-ul'.
- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-ro/strings.xml` — "protecţia" uses the cedilla letter ţ (U+0163) instead of the correct comma-below ț (U+021B).
    - Current: `protecţia`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `protecția`
    - Romanian spelling uses comma-below ț, and the rest of the locale spells it that way (e.g. "Protecție îmbunătățită" in enhanced_tracking_protection). The cedilla form is a legacy encoding error.
- `preference_block_autoplay_audio_only_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ro/strings.xml` — The summary for a single option uses the feminine plural "Recomandate" instead of the singular.
    - Current: `Recomandate`
    - Source: `Recommended`
    - Suggest: `Recomandat`
    - "Recommended" is the summary of one option ("Block audio only"). The plural form does not agree with a single option.

### D. Terminology, register & consistency

- `mozac_feature_addons_addons_manager` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — "Add-ons" is rendered as "extensii" here but as "Suplimente" on the add-ons page title on the same surface.
    - Current: `Manager de extensii`
    - Source: `Add-ons Manager`
    - Suggest: `Manager de suplimente`
    - en-US uses the same term, "Add-ons", in both strings. mozac_feature_addons_addons translates it as "Suplimente", and the usual Romanian Firefox term for the manager is "Manager de suplimente". Using "extensii" here is inconsistent.
- `mozac_feature_addons_permissions_trial_ml_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — Breaks the 'Să ...' subjunctive pattern used by all other permission descriptions and reads as a command or a statement of fact.
    - Current: `Descarcă și rulează modele de inteligență artificială`
    - Source: `Download and run AI models on your device.`
    - Suggest: `Să descarce și să ruleze modele de inteligență artificială`
    - Every other permission description, including the non-update version of this one, uses 'Să ...' to describe what the add-on may do. 'Descarcă și rulează' is inconsistent when these descriptions are appended together.
- `mozac_feature_sitepermissions_media_key_system_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ro/strings.xml` — Uses the formal/plural 'Permiteți', but the other permission dialog titles use the informal 'Permiți'.
    - Current: `Permiteți`
    - Source: `Allow %1$s to play DRM-controlled content?`
    - Suggest: `Permiți`
    - Sibling permission titles (location, microphone, notifications, local network) address the user informally. This mixes forms of address on the same surface.
- `mozac_feature_sitepermissions_persistent_storage_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ro/strings.xml` — Uses the formal/plural 'Permiteți', but the other permission dialog titles use the informal 'Permiți'.
    - Current: `Permiteți`
    - Source: `Allow %1$s to store data in persistent storage?`
    - Suggest: `Permiți`
    - Mixes forms of address with the sibling permission dialog titles, which use the informal form.
- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ro/strings.xml` — Uses the formal 'doriți să blocați', which doesn't match the informal address used in the rest of the permission dialogs.
    - Current: `Poate doriți să blocați accesul`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - Suggest: `Poate vrei să blochezi accesul`
    - The other site-permission strings address the user with informal 'tu' forms. This is inconsistent with them.
- `mozac_feature_sitepermissions_storage_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ro/strings.xml` — Uses the formal/plural 'Permiteți', but the other permission dialog titles use the informal 'Permiți'.
    - Current: `Permiteți`
    - Source: `Allow %1$s to use its cookies on %2$s?`
    - Suggest: `Permiți`
    - Mixes forms of address with the sibling permission dialog titles, which use the informal form.
- `bookmark_add_new_folder_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — 'folder' is used here, while the other bookmark strings use 'dosar'.
    - Current: `Adaugă un folder nou`
    - Source: `Add a new folder`
    - Suggest: `Adaugă un dosar nou`
    - The bookmark strings in this batch translate 'folder' as 'dosar' ('Șterge dosarul', 'Dosarele implicite', 'Adaugă dosarul'). This one string switches to 'folder'.
- `debug_drawer_fab_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Uses the formal/plural imperative "Deschideți", while the other action labels nearby use the singular imperative.
    - Current: `Deschideți`
    - Source: `Open debug drawer`
    - Suggest: `Deschide`
    - The other debug drawer actions use the singular imperative ("Adaugă", "Șterge", "Navighează"), so this label switches the form of address.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Tabs" is rendered as "tab-uri" here, while the same surface consistently uses "file".
    - Current: `tab-uri închise`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `file închise`
    - Every other tab string in the batch, including the sibling notification strings, translates "tab" as "filă/file". The anglicism "tab-uri" breaks that terminology.
- `opening_screen_after_four_hours_of_inactivity_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — 'Homepage' is translated as 'pagina principală' here but as 'pagina de start' in the other options on the same settings screen.
    - Current: `Deschide pe pagina principală după patru ore`
    - Source: `Open on homepage after four hours`
    - Suggest: `Deschide pe pagina de start după patru ore`
    - The neighbouring strings opening_screen_homepage, opening_screen_homepage_summary and opening_screen_after_four_hours_of_inactivity all use 'pagina de start'.
- `preference_doh_off_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "default DNS resolver" is rendered as "rezolvitorul" here but as "rezolverul" in preference_doh_increased_protection_info_2 on the same screen.
    - Current: `rezolvitorul DNS implicit`
    - Source: `Use your default DNS resolver`
    - Suggest: `rezolverul DNS implicit`
    - The same source term appears in the same DNS over HTTPS settings in two different forms. It should be one consistent term.
- `preference_enhanced_tracking_protection_allow_list_dialog_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "fixes" is rendered as "remediile" (remedies), unlike "remedierile" used for the Cancel button of the same dialog and in the related strings.
    - Current: `Dezactivează remediile`
    - Source: `Turn fixes off`
    - Suggest: `Dezactivează remedierile`
    - The Cancel button of the same dialog says "Menține activate remedierile", and the description uses "remedieri". "remediile" means remedies or cures, so it is inconsistent and the wrong term.
- `snackbar_added_to_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Shortcuts" is rendered as "scurtături", while every other shortcut string uses "comenzi rapide".
    - Current: `Adăugat la scurtături!`
    - Source: `Added to shortcuts!`
    - Suggest: `Adăugat la comenzile rapide!`
    - The same shortcuts feature uses "comandă rapidă/comenzi rapide" in shortcut_max_limit_title, shortcut_name_hint, shortcut_url_hint and shortcut_max_limit_content. "scurtături" is inconsistent with all of them.
- `snackbar_num_tabs_closed` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — "Tabs" is rendered as "Taburi", while the sibling snackbars use "filă/file".
    - Current: `Taburi închise`
    - Source: `Tabs closed: %1$s`
    - Suggest: `File închise`
    - snackbar_tab_closed and snackbar_private_tab_closed use "Filă" for tab, which is the locale's established term. "Taburi" is inconsistent on the same snackbar surface.

### E. Typography, punctuation & spacing

- `mozac_feature_addons_permissions_data_collection_locationInfo_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — Uses the cedilla ţ instead of the comma-below ț.
    - Current: `locaţie`
    - Source: `location`
    - Suggest: `locație`
    - Standard Romanian spelling uses the comma-below ț, and the rest of the batch does too (e.g. "îți"). The cedilla form is inconsistent with that.
- `mozac_feature_addons_permissions_tab_hide_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ro/strings.xml` — Uses cedilla 'ş' instead of the correct Romanian comma-below 'ș'.
    - Current: `şi`
    - Source: `Hide and show browser tabs.`
    - Suggest: `și`
    - Standard Romanian orthography uses ș (comma below); the rest of the batch uses ș, including the sibling string.
- `my_longest_fox_is` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-ro/strings.xml` — There is a double space before the score placeholder.
    - Current: `este de  %1$d`
    - Source: `My longest fox is %1$d! #longfox %2$s`
    - Suggest: `este de %1$d`
    - Users see the extra space in the shared text.
- `ai_controls_banner_headline` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — There are two spaces before the app name placeholder, where there should be one.
    - Current: `în  %s`
    - Source: `You always have a choice in %s`
    - Suggest: `în %s`
    - The source has one space before %s. The extra space appears in the banner headline that users see.
- `change_file_extension_confirm_button` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — Button label has a trailing full stop not present in the source.
    - Current: `Da, schimbă-l.`
    - Source: `Yes, change it`
    - Suggest: `Da, schimbă-l`
    - The source button label "Yes, change it" has no terminal punctuation; button labels should not end with a period.
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-ro/strings.xml` — A spaced hyphen is used as a dash instead of the locale's em dash.
    - Current: `aplicație - ceea ce`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `aplicație — ceea ce`
    - The ro convention is the em dash; a hyphen between spaces is used here as a sentence dash.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ro/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
