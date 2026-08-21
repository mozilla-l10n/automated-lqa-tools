# Android l10n QA — cs

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **Previous run** | 2026-08-21 @ `0d02c6c9f0f6` |
| **Mode** | incremental |
| **Strings reviewed this run** | 11 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for cs: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (3)

- `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — `recently_closed_tab` has placeholders none where the source has %d
    - Current: `Jeden panel`
    - Source: `%d tab`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — `create_collection_save_to_collection_tab_selected` has placeholders none where the source has %d
    - Current: `Vybrán jeden panel`
    - Source: `%d tab selected`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — `firstrun_shortcut_text` quotes “Přidat na plochu” but the string it names, `menu_add_to_home_screen`, reads “Přidat na domovskou obrazovku”
    - Current: `S aplikací %1$s se můžete rychle vrátit ke svým oblíbeným stránkám. Použijte „Přidat na plochu“ z nabídky aplikace %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Přidat na domovskou obrazovku`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

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
| Missing strings | 3 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 2 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**3 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — 3

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `german-double` 15, `curly-double` 5 | **german-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2, `en` 4 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (147)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 2 |
| 2 | Wrong content (says something other than the English) | 83 |
| 3 | Degraded language (grammar, spelling, terminology) | 51 |
| 4 | Cosmetic (typography, spacing) | 11 |

### A. Functional, markup, variables & plurals

- `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — `create_collection_save_to_collection_tab_selected` has placeholders none where the source has %d
    - Current: `Vybrán jeden panel`
    - Source: `%d tab selected`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — `recently_closed_tab` has placeholders none where the source has %d
    - Current: `Jeden panel`
    - Source: `%d tab`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-cs/strings.xml` — Third bullet says something entirely different from the source about access permissions.
    - Current: `Jste-li autorem tohoto souboru, ověřte, že daný soubor na serveru existuje a že má příslušná práva na zobrazení.`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `Máte k požadované položce dostatečná přístupová oprávnění?`
    - The source asks whether the user has sufficient access permissions to the requested item; the translation instead addresses the file's author and server-side existence.
- `mozac_browser_errorpages_invalid_content_encoding_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-cs/strings.xml` — "Content Encoding Error" (data compression/encoding) is rendered as "chyba znakové sady" (character set error).
    - Current: `Chyba znakové sady obsahu`
    - Source: `Content Encoding Error`
    - Suggest: `Chyba kódování obsahu`
    - The message body concerns an invalid or unsupported compression form, not a character set; "znaková sada" means charset and names the wrong thing.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-cs/strings.xml` — "potentially harmful site" is rendered as "útočná" (attack site), duplicating the malware string instead of translating "harmful".
    - Current: `byla nahlášena jako útočná`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `byla nahlášena jako potenciálně škodlivá`
    - The source says the site was reported as a potentially harmful site; "útočná" means "attack site", which is the wording of the separate malware error page (mozac_browser_errorpages_safe_browsing_malware_uri_message). The title of this same page already uses "škodlivou stránkou".
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-cs/strings.xml` — Subject and object are reversed: the Czech says "the protocol specifies the address" instead of "the address specifies a protocol".
    - Current: `Adresu (URL) určuje protokol (např. { <q> }wxyz://{ </q> }), který nebyl prohlížečem rozpoznán, a proto se k ní nemůže korektně připojit.`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `Adresa (URL) určuje protokol (např. { <q> }wxyz://{ </q> }), který prohlížeč nezná, a proto se k danému serveru nemůže správně připojit.`
    - Source: "The address specifies a protocol … the browser does not recognize". The Czech accusative "Adresu" reverses the roles.
- `mozac_feature_addons_failed_to_translate` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "locale" is translated as "region" instead of "národní prostředí"/"jazyk".
    - Current: `Překlad pro region %1$s`
    - Source: `Translation not found, for locale %1$s neither default language %2$s`
    - Suggest: `Překlad pro národní prostředí %1$s`
    - The developer comment says %1$s is the user's locale, not a region; "region" names the wrong concept.
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — The translation states the extension collects data, dropping the "wants to" (intent) from the source.
    - Current: `Vývojář říká, že toto rozšíření shromažďuje: %1$s`
    - Source: `The developer says the extension wants to collect: %1$s`
    - Suggest: `Vývojář říká, že toto rozšíření chce shromažďovat: %1$s`
    - Source: "the extension wants to collect" — a request for permission, not a statement of current behavior.
- `mozac_feature_addons_permissions_data_collection_personalCommunications_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "personal communications" is mistranslated as "osobní údaje" (personal data), inconsistent with the short description "osobní komunikace".
    - Current: `Sdílet osobní údaje s vývojářem rozšíření`
    - Source: `Share personal communications with extension developer`
    - Suggest: `Sdílet osobní komunikaci s vývojářem rozšíření`
    - The source says "personal communications"; the matching short description string correctly uses "osobní komunikace". "Osobní údaje" means personal data, a different permission category.
- `mozac_feature_addons_permissions_proxy_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "Control browser proxy settings" is rendered as "Změnit nastavení proxy", dropping "browser" and changing the aspect/meaning from ongoing control to a one-off change.
    - Current: `Změnit nastavení proxy`
    - Source: `Control browser proxy settings`
    - Suggest: `Ovládat nastavení proxy prohlížeče`
    - The source says the extension controls the browser's proxy settings; the other permission descriptions in this set consistently use imperfective verbs (Číst a upravovat, Přistupovat) and keep "prohlížeče".
- `mozac_feature_addons_permissions_proxy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "Control browser proxy settings." is rendered as "Změnit nastavení proxy.", dropping "browser" and altering the meaning.
    - Current: `Změnit nastavení proxy.`
    - Source: `Control browser proxy settings.`
    - Suggest: `Ovládat nastavení proxy prohlížeče.`
    - The source refers to controlling the browser's proxy settings; the translation omits "prohlížeče" and uses a perfective one-off verb inconsistent with the rest of the permission list.
- `mozac_feature_addons_settings_on` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "On" (toggle state) is translated as "Povoleno" while the neighbouring "Run in private browsing" label is also translated as "Povoleno v režimu...", conflating label and state.
    - Current: `Povoleno`
    - Source: `On`
    - Suggest: `Zapnuto`
    - The developer comment says this indicates the add-on is enabled — a toggle state; the same word is reused for the separate setting label, causing inconsistency on the same surface.
- `mozac_feature_addons_settings_run_in_private_browsing` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — The setting label "Run in private browsing" is translated as a state ("Povoleno v režimu anonymního prohlížení") instead of the action label.
    - Current: `Povoleno v režimu anonymního prohlížení`
    - Source: `Run in private browsing`
    - Suggest: `Spouštět v režimu anonymního prohlížení`
    - The source is a settings label describing running the add-on in private browsing, not a status saying it is already allowed.
- `mozac_feature_addons_updater_notification_title_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — "%1$s has an update" is rendered as the add-on requiring an update rather than an update being available for it.
    - Current: `Doplněk %1$s vyžaduje aktualizaci`
    - Source: `%1$s has an update`
    - Suggest: `Pro doplněk %1$s je dostupná aktualizace`
    - The source says an update is available for the add-on; the Czech says the add-on requires/demands an update, which reverses who needs what.
- `mozac_feature_applinks_normal_confirm_dialog_message` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-cs/strings.xml` — The message says "allow the app to show this content" instead of asking whether the user wants to leave the browser to view the content.
    - Current: `Chcete aplikaci %1$s dovolit zobrazit tento obsah?`
    - Source: `Would you like to leave %s to view this content?`
    - Suggest: `Chcete opustit aplikaci %s a zobrazit tento obsah?`
    - Source: "Would you like to leave %s to view this content?" — %s is the browser app being left, not an app being granted permission.
- `mozac_feature_autofill_confirmation_authenticity` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-cs/strings.xml` — Translation says the app could not be verified rather than that its authenticity could not be verified, dropping the key notion.
    - Current: `nemohla ověřit cílovou aplikaci`
    - Source: `%1$s could not verify the authenticity of the application. Do you want to proceed with autofilling the selected credentials?`
    - Suggest: `nemohla ověřit pravost aplikace`
    - Source: "%1$s could not verify the authenticity of the application."
- `mozac_feature_contextmenu_add_to_contact` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-cs/strings.xml` — "Add to contact" is rendered as "Add contact", changing the meaning.
    - Current: `Přidat kontakt`
    - Source: `Add to contact`
    - Suggest: `Přidat ke kontaktu`
    - Source adds the email address to an existing contact, not creates a new contact.
- `mozac_feature_contextmenu_download_link` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-cs/strings.xml` — "Download link" is translated as just "Stáhnout", dropping the object.
    - Current: `Stáhnout`
    - Source: `Download link`
    - Suggest: `Stáhnout odkaz`
    - Source: "Download link" — the context menu item explicitly names the link target.
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-cs/strings.xml` — Plural "Upload files?" rendered as singular "Nahrát soubor?".
    - Current: `Nahrát soubor?`
    - Source: `Upload files?`
    - Suggest: `Nahrát soubory?`
    - The source refers to multiple files being uploaded from a folder; the Czech says a single file.
- `mozac_feature_pwa_default_shortcut_label` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-cs/strings.xml` — "Website" is translated as "Server" instead of a web page/site.
    - Current: `Server`
    - Source: `Website`
    - Suggest: `Webová stránka`
    - The source is the default shortcut label for a website when it has no title; "Server" means a server machine, not a website.
- `mozac_feature_pwa_site_controls_notification_channel` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-cs/strings.xml` — Translation drops "site" and says "full screen mode controls" instead of "full screen site controls".
    - Current: `Ovládací prvky režimu celé obrazovky`
    - Source: `Full screen site controls`
    - Suggest: `Ovládací prvky serveru v režimu celé obrazovky`
    - The source refers to controls for the site shown in full screen; the Czech omits the site aspect.
- `mozac_feature_summarize_summary_model` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-cs/strings.xml` — Translation adds "stránky" (of the page), which is not in the source "Summary by %1$s".
    - Current: `Souhrn stránky od %1$s`
    - Source: `Summary by %1$s`
    - Suggest: `Souhrn od %1$s`
    - The source is just "Summary by %1$s" where %1$s is the model name; "Souhrn stránky" adds content not present in the source.
- `addresses_name` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Name" here means a person's full name, but the Czech "Název" means the name/title of a thing.
    - Current: `Název`
    - Source: `Name`
    - Suggest: `Jméno`
    - The developer comment states Name represents a person's full name (e.g. John Joe Doe); Czech uses "Jméno" for a person's name, while "Název" is used for objects/titles.
- `addresses_neighborhood` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Neighborhood" as an address field is translated as "Sousedství" (the abstract state of being neighbors), not a city district.
    - Current: `Sousedství`
    - Source: `Neighborhood`
    - Suggest: `Čtvrť`
    - In an address form the field denotes a neighborhood/quarter of a city (Iran, Mexico); Czech "Sousedství" does not denote a place name and is wrong here.
- `addresses_organization` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Organization" is rendered as "Společnost" (company), narrowing the meaning.
    - Current: `Společnost`
    - Source: `Organization`
    - Suggest: `Organizace`
    - The source field is the generic organization name; "Společnost" means specifically a business company, which excludes non-business organizations.
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Townland" (an Irish rural land division) is translated as "Město" (city/town), which names the wrong concept.
    - Current: `Město`
    - Source: `Townland`
    - Suggest: `Townland`
    - The developer comment states the Townland field is a specific type of rural land division in Ireland; "Město" means "city/town" and conflicts with the separate city field.
- `addresses_village_township` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Township" is rendered as "okres" (district), which is a different administrative level.
    - Current: `Obec nebo okres`
    - Source: `Village or Township`
    - Suggest: `Vesnice nebo obec`
    - The source refers to a village or township (a rural settlement unit in Malaysia), not a district (okres), which is a higher-level administrative division.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "sites in this language" was rendered as translating "into this language", reversing the direction.
    - Current: `%1$s nabídne překlad stránek do tohoto jazyka.`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `%1$s nabídne překlad stránek v tomto jazyce.`
    - The source says the app will offer to translate sites written in this language (source language), matching the parallel never-translate string which correctly uses "v tomto jazyce".
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Item Menu" (menu for one item) translated as plural "Nabídka položek" (menu of items).
    - Current: `Nabídka položek pro %s`
    - Source: `Item Menu for %s`
    - Suggest: `Nabídka položky pro %s`
    - The developer comment says %s is a single folder name or bookmark title, so the menu belongs to one item, not to multiple items.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "sheet" (bottom sheet) is mistranslated as "seznam" (list).
    - Current: `Zavřít seznam s nabídkou pro vlastní panel`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Zavřít nabídku vlastního panelu`
    - The source refers to closing the bottom-sheet custom tab menu; "seznam" means "list", which is not what the source says.
- `browser_menu_customize_homepage` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Customize homepage" is rendered as just "Přizpůsobit", dropping the object.
    - Current: `Přizpůsobit`
    - Source: `Customize homepage`
    - Suggest: `Přizpůsobit domovskou stránku`
    - The menu item opens the customize homepage settings; the Czech omits "homepage", making the label ambiguous compared to the source.
- `browser_menu_stop` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Stop" is rendered as a descriptive sentence in third person instead of the action label.
    - Current: `Zastaví načítání stránky`
    - Source: `Stop`
    - Suggest: `Zastavit načítání stránky`
    - The source is the imperative control label "Stop"; other content descriptions in the same set use the infinitive (e.g. "Obnovit" for Refresh). "Zastaví" is third-person indicative and inconsistent.
- `browser_menu_summarize_page` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Menu action "Summarize page" translated as a noun phrase instead of a verb.
    - Current: `Shrnutí stránky`
    - Source: `Summarize page`
    - Suggest: `Shrnout stránku`
    - The developer comment says it is a menu label for navigating to the summarization feature; the source is a verb phrase, as with "Translate page" → "Přeložit stránku" in the same menu.
- `customize_toggle_world_cup` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "World Cup" is rendered as the generic "Světový šampionát" instead of the established Czech name.
    - Current: `Světový šampionát`
    - Source: `World Cup`
    - Suggest: `Mistrovství světa`
    - The source names the World Cup event; the standard Czech equivalent is "Mistrovství světa".
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Debug locales to enable" is mistranslated as a list of languages for which debugging can be enabled.
    - Current: `Seznam jazyků, pro které je možné zapnout ladění`
    - Source: `Debug locales to enable`
    - Suggest: `Ladicí jazyky (locale) k zapnutí`
    - The source is a header for a list of debug locales that can be toggled on/off, not about enabling debugging for languages.
- `debug_drawer_region_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Region Tools" translated as "Nastavení regionu" (Region settings), inconsistent with other *Tools titles.
    - Current: `Nastavení regionu`
    - Source: `Region Tools`
    - Suggest: `Nástroje pro region`
    - Source says "Tools"; other debug drawer tool titles use "Nástroje" (e.g. Nástroje CFR, Nástroje pro doplňky).
- `default_browser_experiment_card_text` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation says links, e-mails and messages open in Firefox, but the source means links from websites, e-mails and messages.
    - Current: `Nastavte si automatické otevírání odkazů, e-mailů a zpráv ve Firefoxu.`
    - Source: `Set links from websites, emails, and messages to open automatically in Firefox.`
    - Suggest: `Nastavte si, aby se odkazy z webových stránek, e-mailů a zpráv automaticky otevíraly ve Firefoxu.`
    - The source is "links from websites, emails, and messages" — the three nouns are sources of the links, not things being opened. The Czech makes e-mails and messages themselves open in Firefox.
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The word "pending" (and its bullet separator) is dropped from the translation.
    - Current: `%1$s / %2$s`
    - Source: `%1$s / %2$s • pending`
    - Suggest: `%1$s / %2$s • čeká`
    - The source shows the download state "pending" after the sizes; the Czech omits this status information entirely.
- `download_rename_error_case_only_error` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The Czech says the entered name "contains only uppercase or lowercase letters" instead of that it only changes letter casing.
    - Current: `Zadaný název obsahuje pouze velká nebo malá písmena.`
    - Source: `The name you entered only changes uppercase or lowercase letters. Try a different file name.`
    - Suggest: `Zadaný název mění pouze velikost písmen.`
    - Source: "The name you entered only changes uppercase or lowercase letters" — the difference is only in casing, not that the name consists solely of letters.
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation drops "analytics companies" and "your browsing data", saying only "reklamní sítě a firmy ke sběru informací".
    - Current: `které používají reklamní sítě a firmy ke sběru informací z mnoha serverů na internetu`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `které používají reklamní sítě a analytické firmy ke shromažďování údajů o vašem prohlížení na mnoha serverech`
    - Source says "ad networks and analytics companies use to compile your browsing data"; the Czech omits "analytics" and the notion of browsing data.
- `felt_privacy_desc_card_title` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The translation drops "on this device" from the title.
    - Current: `Nezanechá stopy`
    - Source: `Leave no traces on this device`
    - Suggest: `Nezanechá stopy v tomto zařízení`
    - Source is "Leave no traces on this device"; the qualifier "on this device" is essential to the meaning and is missing.
- `inactive_tabs_auto_close_message_header` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The header asks about auto-closing tabs after one month of inactivity, not about tabs that are already one month old.
    - Current: `Chcete automaticky zavírat měsíc staré neaktivní panely?`
    - Source: `Auto-close after one month?`
    - Suggest: `Zavírat automaticky po jednom měsíci?`
    - Source "Auto-close after one month?" refers to closing inactive tabs after one month; the Czech reads "tabs that are one month old", shifting the meaning.
- `nimbus_notification_default_browser_text` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Adds a possessive "můj" (my) not present in the source, mismatching the second-person address.
    - Current: `Nastavit Firefox jako můj výchozí prohlížeč`
    - Source: `Make Firefox your default browser`
    - Suggest: `Nastavte si Firefox jako výchozí prohlížeč`
    - Source "Make Firefox your default browser" addresses the user in second person; "můj" (my) is a first-person possessive and does not match.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The translation drops the "allowing" (i.e. granting permission) sense and turns the sentence into a generic "consider whether you could help".
    - Current: `Zvažte prosím, zda byste mohli pomoci Firefoxu zvítězit.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Zvažte prosím udělení souhlasu a pomozte Firefoxu zvítězit.`
    - The developer comment says "Allowing" refers to the main "Allow and Continue" button — the user is asked to allow the data sharing; the Czech omits that and only asks them to consider being able to help.
- `open_all_warning_message` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The clause "while the pages are loading" is dropped from the translation.
    - Current: `Otevření tolika panelů může aplikaci %s zpomalit.`
    - Source: `Opening this many tabs may slow down %s while the pages are loading. Are you sure you want to continue?`
    - Suggest: `Otevření tolika panelů může aplikaci %s během načítání stránek zpomalit.`
    - Source states the slowdown occurs while the pages are loading; that qualification is missing in Czech.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation says "recent browsing history" instead of "all past explorations".
    - Current: `Zobrazit nedávnou historii prohlížení`
    - Source: `Show all past explorations`
    - Suggest: `Zobrazit celou historii prohlížení`
    - Source is "Show all past explorations" and the comment says the button navigates to show all of the user's history; "nedávnou" (recent) reverses the "all" meaning.
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Leave private tabs" translated as "Leave private browsing".
    - Current: `Opustit anonymní prohlížení`
    - Source: `Leave private tabs`
    - Suggest: `Opustit anonymní panely`
    - Source refers to private tabs, consistent with the other pbm_authentication_* strings that use "anonymní panely".
- `preference_doh_default_protection_info_5` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — %1$s is the application name (e.g. Firefox), not a server, but the Czech renders it as "serveru" (the server).
    - Current: `když síť sdělí serveru %1$s`
    - Source: `Turn off when a network tells %1$s it shouldn’t use secure DNS. %2$s`
    - Suggest: `když síť aplikaci %1$s sdělí`
    - Developer comment states %1$s is the name of the application; calling it a server misstates the source meaning.
- `preference_doh_max_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Adds "vždy" (always) that is not in the source and changes the meaning of the warning sentence.
    - Current: `Před použitím systémového překladače DNS vždy uvidíte bezpečnostní varování.`
    - Source: `%1$s will always use secure DNS. You’ll see a security risk warning before we use your system DNS.`
    - Suggest: `Před použitím systémového překladače DNS uvidíte bezpečnostní varování.`
    - Source says "You’ll see a security risk warning before we use your system DNS" — no "always" in this second sentence.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Cross-site and social media trackers" rendered as "sledovací cookies, např. sociálních sítí", losing the cross-site category.
    - Current: `Sledovací cookies, např. sociálních sítí`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Sledovací cookies mezi weby a ze sociálních sítí`
    - The source lists two tracker types (cross-site and social media); the target drops cross-site and turns social media into a mere example.
- `preference_enhanced_tracking_protection_standard_description_5` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The Czech text loses the meaning "but block fewer trackers" and instead says pages load normally "except for some trackers".
    - Current: `Stránky se načítají normálně s výjimkou některých sledovacích prvků.`
    - Source: `Pages will load normally, but block fewer trackers.`
    - Suggest: `Stránky se načítají normálně, blokuje se ale méně sledovacích prvků.`
    - Source states pages load normally but fewer trackers are blocked; the translation implies pages load normally except for some trackers, which changes the meaning.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "browsing data" was rendered as "soukromých dat" (private data) instead of "dat o prohlížení".
    - Current: `dojde ke smazání soukromých dat`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `dojde ke smazání dat o prohlížení`
    - The source says "browsing data"; "soukromá data" (private data) is a different concept and inconsistent with the Delete browsing data feature naming.
- `preferences_android_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation adds "ukládání" (saving), which is not in the source.
    - Current: `Vyplňování a ukládání uživatelských jmen a hesel v dalších aplikacích na vašem zařízení.`
    - Source: `Fill usernames and passwords in other apps on your device.`
    - Suggest: `Vyplňování uživatelských jmen a hesel v dalších aplikacích na vašem zařízení.`
    - Source only mentions filling usernames and passwords in other apps, not saving them.
- `preferences_downloads_ask_when_to_delete_files` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Ask when I delete files" mistranslated as a passive "when a file is deleted", losing the first-person subject and the plural.
    - Current: `Při smazání souboru se ptát`
    - Source: `Ask when I delete files`
    - Suggest: `Zeptat se, když mažu soubory`
    - Source is "Ask when I delete files" — the user deleting files; the Czech reads as an impersonal "upon deletion of a file".
- `preferences_inactive_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation says "Moving inactive tabs" instead of "Move old tabs to inactive".
    - Current: `Přesun neaktivních panelů`
    - Source: `Move old tabs to inactive`
    - Suggest: `Přesouvat staré panely mezi neaktivní`
    - The source describes moving old (unused) tabs into the inactive section; the Czech reverses it to moving tabs that are already inactive.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "haven’t viewed" rendered as "neotevřeli" (haven't opened).
    - Current: `které jste dva týdny neotevřeli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `které jste dva týdny nezobrazili`
    - Source says tabs not viewed for two weeks; "neotevřeli" means not opened, which is a different condition.
- `preferences_passwords_exceptions_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation adds "nikdy" (never), which is not in the source.
    - Current: `Aplikace %s nebude nikdy ukládat hesla pro tyto stránky.`
    - Source: `%s won’t save passwords for these sites.`
    - Suggest: `Aplikace %s nebude ukládat hesla pro tyto stránky.`
    - Source is "%s won’t save passwords for these sites." — there is no "never".
- `preferences_passwords_exceptions_description_empty_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Translation adds "nikdy" (never), which is not in the source.
    - Current: `Aplikace %s nebude nikdy ukládat hesla pro stránky uvedené v tomto seznamu.`
    - Source: `%s won’t save passwords for sites listed here.`
    - Suggest: `Aplikace %s nebude ukládat hesla pro stránky uvedené v tomto seznamu.`
    - Source is "%s won’t save passwords for sites listed here." — no "never" in the source.
- `preferences_passwords_saved_logins_site` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Site" is rendered as "Server" instead of "Stránka"/"Server (stránka)".
    - Current: `Server`
    - Source: `Site`
    - Suggest: `Stránka`
    - The header labels the website a login belongs to; elsewhere in this batch "sites" is translated as "stránky", so "Server" is inconsistent and inaccurate.
- `preferences_screenshots_in_private_mode_disclaimer` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "private tabs" is translated as generic "obsah panelů", dropping the private-browsing qualifier.
    - Current: `obsah panelů bude viditelný`
    - Source: `If allowed, private tabs will also be visible when multiple apps are open`
    - Suggest: `obsah anonymních panelů bude viditelný`
    - The source says "private tabs will also be visible"; the Czech omits that it concerns private tabs specifically.
- `preferences_search_bookmarks` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Search bookmarks" rendered as "Našeptávat ze záložek" (suggest from bookmarks).
    - Current: `Našeptávat ze záložek`
    - Source: `Search bookmarks`
    - Suggest: `Hledat v záložkách`
    - Source is "Search bookmarks"; "našeptávat" means to suggest, which corresponds to a different term used for suggestions strings.
- `preferences_tracking_protection_exceptions_turn_on_for_all` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "all sites" is rendered as "všechny servery" (all servers) instead of "všechny stránky/weby".
    - Current: `Zapnout pro všechny servery`
    - Source: `Turn on for all sites`
    - Suggest: `Zapnout pro všechny stránky`
    - The source refers to sites (web pages), and the rest of the batch consistently translates "site" as "stránka"; "server" names a different thing.
- _…and 28 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_addons_permissions_one_extra_domain_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — Wrong preposition: "z další domény" (from another domain) instead of "na další doméně", inconsistent with the related domain string.
    - Current: `Přistupovat k vašim datům z další domény`
    - Source: `Access your data on another domain`
    - Suggest: `Přistupovat k vašim datům na další doméně`
    - The source is "Access your data on another domain"; the sibling string mozac_feature_addons_permissions_sites_in_domain_description uses "na doméně %1$s".
- `mozac_feature_addons_permissions_one_extra_domain_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — Wrong preposition: "z další domény" instead of "na další doméně".
    - Current: `Přistupovat k vašim datům z další domény.`
    - Source: `Access your data on another domain.`
    - Suggest: `Přistupovat k vašim datům na další doméně.`
    - The source is "Access your data on another domain."; the sibling domain string uses "na doméně %1$s".
- `mozac_feature_addons_updater_notification_heading_data_collection_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-cs/strings.xml` — Tense mismatch: "The developer says" rendered in past tense "Vývojář řekl".
    - Current: `Vývojář řekl, že rozšíření bude shromažďovat %1$s.`
    - Source: `New required data collection: The developer says the extension will collect %1$s.`
    - Suggest: `Vývojář uvádí, že rozšíření bude shromažďovat %1$s.`
    - The source uses the present tense "says"; the Czech past tense changes the statement's timeframe.
- `mozac_feature_sitepermissions_storage_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-cs/strings.xml` — Wrong possessive pronoun: "své cookies" should be "jeho cookies" and the source has no "také".
    - Current: `Povolit serveru %1$s používat své cookies také na serveru %2$s?`
    - Source: `Allow %1$s to use its cookies on %2$s?`
    - Suggest: `Chcete serveru %1$s povolit používat jeho cookies na serveru %2$s?`
    - Source: "Allow %1$s to use its cookies on %2$s?" — the reflexive "své" refers to the subject of the clause; and "také" (also) is not in the source. Other dialogs in the same file use the "Chcete … povolit" pattern.
- `crash_reporting_never` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-cs/strings.xml` — "Never send" is rendered with an ungrammatical double-negative verb form.
    - Current: `Nikdy neodeslat`
    - Source: `Never send`
    - Suggest: `Nikdy neodesílat`
    - The radio-button option means "never send"; Czech requires the imperfective infinitive "neodesílat" for a repeated/ongoing setting, matching "Odeslat automaticky"/"Zeptat se před odesláním". "Nikdy neodeslat" (perfective) is not idiomatic Czech.
- `addon_ga_message_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Plural agreement error: "Nové rozšíření jsou" mixes singular noun form with plural verb.
    - Current: `Nové rozšíření jsou nyní k dispozici`
    - Source: `New extensions now available`
    - Suggest: `Nová rozšíření jsou nyní k dispozici`
    - Source is plural "New extensions now available"; Czech nominative plural of "rozšíření" requires the neuter plural adjective "Nová".
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "EÚ" is the Slovak abbreviation; Czech uses "EU".
    - Current: `(EÚ) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `(EU) 2024/1183`
    - The source says "Regulation (EU) 2024/1183"; in Czech the European Union abbreviation is "EU", while "EÚ" is Slovak.
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Wrong case/valency: "Zabraňuje skriptům přístup" should be "Zabraňuje škodlivým skriptům v přístupu".
    - Current: `Zabraňuje skriptům přístup k vašemu zařízení`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `Zabraňuje škodlivým skriptům v přístupu k vašemu zařízení`
    - "zabraňovat" requires the preposition "v" + locative; also "malicious" is untranslated.
- `extension_process_crash_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Gender agreement error: "Rozšíření" (neuter) takes "restartována", not "restartovány".
    - Current: `Rozšíření nebudou restartovány během vaší aktuální relace.`
    - Source: `One or more extensions stopped working, making your system unstable. %1$s unsuccessfully tried to restart the extension(s).  Extensions won’t be restarted during your current session.  Removing or disabling extensions m…`
    - Suggest: `Rozšíření nebudou během vaší aktuální relace restartována.`
    - Czech neuter plural noun "rozšíření" requires the neuter participle ending -a; the same string already uses "zakázána" correctly in the title string.
- `microsurvey_close_handle_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Content description for the close action uses a 3rd-person verb form instead of an infinitive label.
    - Current: `Zavře průzkum`
    - Source: `Close survey`
    - Suggest: `Zavřít průzkum`
    - The source "Close survey" is an action label; Czech convention (and the sibling string "Zavřít") uses the infinitive, not "Zavře" ("it closes").
- `nova_onboarding_theme_selection_automatic_label` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Gender of the theme option label is inconsistent with the sibling options ("Tmavý", "Světlý").
    - Current: `Automatická`
    - Source: `Automatic`
    - Suggest: `Automatický`
    - The three theme options must agree with the same noun; dark/light use masculine (vzhled), so "Automatická" (feminine) does not agree.
- `preference_enhanced_tracking_protection_custom_tracking_content_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Sentence-initial lowercase where the parallel option string uses uppercase.
    - Current: `jen v anonymních panelech`
    - Source: `Only in Private tabs`
    - Suggest: `Jen v anonymních panelech`
    - Source "Only in Private tabs" is capitalized, and the sibling option "Ve všech panelech" starts with a capital letter.
- `preference_enhanced_tracking_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Case agreement error: apposition should be in instrumental to agree with "s funkcí".
    - Current: `dosud nejsilnější bariéry proti cross-site sledovacím prvkům`
    - Source: `Now featuring Total Cookie Protection, our most powerful barrier yet against cross-site trackers.`
    - Suggest: `dosud nejsilnější bariérou proti cross-site sledovacím prvkům`
    - "Nyní s funkcí … , naší dosud nejsilnější bariérou…" – the appositive must be instrumental to agree with "s funkcí", not genitive.
- `preferences_show_nonsponsored_suggestions_summary` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Grammatical agreement error: "z webu souvisejícím" should agree with the plural "návrhy".
    - Current: `Získat návrhy z webu souvisejícím s vaším vyhledáváním`
    - Source: `Get suggestions from the web related to your search`
    - Suggest: `Získat návrhy z webu související s vaším vyhledáváním`
    - The source means suggestions related to your search; the participle must agree with "návrhy" (accusative plural), not with "webu".
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Wrong case: "Zanechat" requires the accusative "zpětnou vazbu", not the genitive "zpětné vazby".
    - Current: `Zanechat zpětné vazby`
    - Source: `Leave feedback`
    - Suggest: `Zanechat zpětnou vazbu`
    - "Leave feedback" — the verb zanechat takes the accusative; "zpětné vazby" is genitive/plural and ungrammatical here.
- `shortcut_max_limit_content` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Wrong form "na ní" instead of accusative "na ni", and the instruction to select "remove" is dropped.
    - Current: `Stačí na ní podržet prst.`
    - Source: `To add a new shortcut, remove one. Touch and hold the site and select remove.`
    - Suggest: `Podržte na ní prst a zvolte Odebrat.`
    - The preposition "na" with a verb of location here requires "na ni" (accusative) — "na ní podržet prst" is incorrect; also the source's "select remove" step is missing.
- `sports_widget_penalties` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Penalties" (the shoot-out phase) rendered with the singular/ambiguous "Penalty".
    - Current: `Penalty`
    - Source: `Penalties`
    - Suggest: `Penaltový rozstřel`
    - The source is a match status label for the penalty shoot-out; Czech "Penalty" reads as a single penalty kick (and looks like the untranslated English word), whereas the established term is "penaltový rozstřel".
- `startup_crash_body` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The sentence is broken by a stray line break inserted in the middle of it, splitting "Při otevírání %s." from "došlo k problému."
    - Current: `Při otevírání %s. došlo k problému.`
    - Source: `There was a problem opening %s.  Sending a crash report helps us diagnose and fix problems with the browser. Reports may include personal or sensitive data.`
    - Suggest: `Při otevírání %s došlo k problému.`
    - The source has one sentence "There was a problem opening %s." followed by a blank line; the Czech puts a period after the placeholder and then continues the sentence on a new line, producing ungrammatical, broken output.
- `sync_no_devices_available` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Gender agreement error: "žádné zařízení" (neuter plural) requires "nejsou k dispozici žádná zařízení".
    - Current: `K dispozici nejsou žádné zařízení`
    - Source: `No devices available`
    - Suggest: `K dispozici nejsou žádná zařízení`
    - "zařízení" is neuter; the plural determiner must be "žádná", not the feminine/masculine-inanimate "žádné".
- `tabs_header_normal_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Normální otevřené panely: %1$s" misparses the source and is inconsistent with the sibling strings' pattern.
    - Current: `Normální otevřené panely: %1$s.`
    - Source: `Normal Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Počet otevřených normálních panelů: %1$s.`
    - The source "Normal Tabs Open: %1$s" gives the count of open normal tabs; the parallel private/synced strings use "Počet otevřených … panelů: %1$s", while this one reads as "normal open tabs" with the count appended.
- `webcompat_reporter_description_3` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Gender/agreement error: "byl" refers to "aplikace" (feminine), should be "byla".
    - Current: `aby byl pro všechny co nejlepší`
    - Source: `Your report helps us understand and fix issues in %1$s to make it better for everyone. %2$s`
    - Suggest: `aby byla pro všechny co nejlepší`
    - The subject is "aplikace %1$s", which is feminine in Czech, so the past participle must be "byla" and the adjective agreement follows.
- `add_custom_autocomplete_label` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Wrong preposition/case: "Přidat odkaz na našeptávání" means "add a link to (pointing at) autocomplete".
    - Current: `Přidat odkaz na našeptávání`
    - Source: `Add link to autocomplete`
    - Suggest: `Přidat odkaz do našeptávání`
    - The source means adding the URL into the custom autocomplete list; Czech requires "do" (into) rather than "na".
- `biometric_auth_image_description` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Content description uses accusative case instead of nominative for "Fingerprint icon".
    - Current: `Ikonu otisku prstu`
    - Source: `Fingerprint icon`
    - Suggest: `Ikona otisku prstu`
    - The source is a noun phrase label "Fingerprint icon"; Czech should use nominative "Ikona otisku prstu", not accusative "Ikonu".
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Repetition of "odmítnout/odmítl" mistranslates "to dismiss" and duplicates the verb.
    - Current: `se pokouší odmítnout požadavky na soubory cookie, aby odmítl otravné bannery cookie`
    - Source: `%1$s tries to reject cookie requests to dismiss annoying cookie banners.  Manage cookie banner preferences in %2$s.`
    - Suggest: `se pokouší odmítat požadavky na soubory cookie, aby odstranil otravné cookie lišty`
    - Source "to dismiss annoying cookie banners" means to get rid of the banners; using "odmítl" twice is wrong and inconsistent with "cookie lišty" used elsewhere.
- `cookie_banner_exception_panel_description_site_is_not_supported` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Stray conjunction "a" makes the sentence ungrammatical.
    - Current: `Chcete náš tým požádat o kontrolu této stránky a za účelem budoucího přidání podpory?`
    - Source: `This site is currently not supported by Cookie Banner Reduction. Would you like to request our team review this website and add support in the future?`
    - Suggest: `Chcete náš tým požádat o kontrolu této stránky za účelem budoucího přidání podpory?`
    - The extra "a" before "za účelem" is a leftover that breaks the sentence structure; the source reads "review this website and add support in the future".
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Misspelling "pokračovaní" and missing reflexive/preposition in "vydávat za zmiňovaný server"; source also says "site", not "server".
    - Current: `Někdo se může snažit vydávat za zmiňovaný server a pokračovaní může být riskantní.`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `Někdo se může snažit vydávat za tento server a pokračování může být riskantní.`
    - "pokračovaní" is a spelling error (correct: "pokračování"); "zmiňovaný" has no counterpart in the source.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Misspelling "shromážďování" and missing comma before "jako".
    - Current: `Slouží k shromážďování, analýze a měření aktivit jako je klepnutí nebo posouvání`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `Slouží ke shromažďování, analýze a měření aktivit, jako je klepnutí nebo posouvání`
    - Correct Czech spelling is "shromažďování"; a comma is required before the comparative clause "jako je…".
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Wrong abbreviation for the European Union: "EÚ" is Slovak, Czech uses "EU".
    - Current: `(EÚ)`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `(EU)`
    - The source reads "Regulation (EU) 2024/1183"; the Czech abbreviation of Evropská unie is "EU", not the Slovak "EÚ".

### D. Terminology, register & consistency

- `mozac_feature_media_sharing_camera_and_microphone_text` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-cs/strings.xml` — "camera" is rendered as "fotoaparát" here while the related notification title string uses "kamera", an inconsistency on the same surface.
    - Current: `váš mikrofon a fotoaparát`
    - Source: `Tap to open the tab that’s using your microphone and camera.`
    - Suggest: `váš mikrofon a kameru`
    - mozac_feature_media_sharing_camera and mozac_feature_media_sharing_camera_and_microphone translate "camera" as "kamera", and the reminder string mozac_feature_media_sharing_camera_and_microphone_reminder_text_2 also uses "kameru"; using "fotoaparát" for the same WebRTC camera is inconsistent.
- `mozac_feature_prompts_manage_logins_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-cs/strings.xml` — "Manage passwords" is rendered as "Správa přihlašovacích údajů" (manage logins/credentials), inconsistent with the other password strings in the same prompt.
    - Current: `Správa přihlašovacích údajů`
    - Source: `Manage passwords`
    - Suggest: `Správa hesel`
    - The source term is "passwords", translated as "hesla" in the sibling strings (mozac_feature_prompts_saved_logins_2 "Uložená hesla", expand/collapse "uložená hesla"). Using "přihlašovací údaje" here is the legacy "logins" term and is inconsistent on the same surface.
- `mozac_feature_prompts_redirect_dialog_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-cs/strings.xml` — "this site" is translated as "tento server" while the parallel dialog title translates "this site" as "této stránky".
    - Current: `Povolit přesměrování na tento server?`
    - Source: `Allow redirect to this site?`
    - Suggest: `Povolit přesměrování na tuto stránku?`
    - Both mozac_feature_prompts_popup_dialog_title and this string use "site" in the source; rendering one as "stránka" and the other as "server" is inconsistent terminology on the same surface.
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-cs/strings.xml` — "shake" is translated as "protřepáním" (shaking a liquid/bottle), inconsistent with "zatřesením" used in the other shake strings.
    - Current: `Shrnout protřepáním?`
    - Source: `Summarize with a shake?`
    - Suggest: `Vytvořit souhrn zatřesením?`
    - All other strings in the same feature render the shake gesture as "zatřást/zatřesením" (e.g. mozac_summarize_settings_shake_to_summarize "Vytvořit souhrn zatřesením"); "protřepání" means shaking a container of liquid and is wrong for a device gesture.
- `browser_menu_add_to_homescreen` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Home screen" is translated inconsistently as "plocha" here but "domovská obrazovka" in the neighboring strings.
    - Current: `Přidat na plochu`
    - Source: `Add to Home screen`
    - Suggest: `Přidat na domovskou obrazovku`
    - browser_menu_add_app_to_homescreen and browser_menu_add_to_homescreen_xiaomi use "domovská obrazovka" for the same source term on the same surface.
- `clear_permissions_on_all_sites` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "sites" is rendered as "servery" (servers) instead of the standard "stránky/weby" used elsewhere in the same surface.
    - Current: `Vymazat oprávnění pro všechny servery`
    - Source: `Clear permissions on all sites`
    - Suggest: `Vymazat oprávnění pro všechny stránky`
    - Source says "all sites"; other strings in this batch translate "site(s)"/"websites" as "stránky"/"weby" (e.g. clear_site_data_dialog_description). "Servery" means servers and is inconsistent terminology.
- `ip_protection_location_unavailable` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Location" is rendered inconsistently within one string as "Poloha" and "umístění".
    - Current: `Poloha není dostupná. Zvolte jiné umístění.`
    - Source: `Location unavailable. Choose another location.`
    - Suggest: `Umístění není dostupné. Zvolte jiné umístění.`
    - All other VPN location strings use "umístění"; using "Poloha" here is inconsistent with the same term in the same sentence and screen.
- `preference_doh_exceptions_add_site` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Site" is translated as "Server" while the neighbouring DoH exception strings use "web"/"servery" inconsistently.
    - Current: `Server`
    - Source: `Site`
    - Suggest: `Web`
    - The related buttons preference_doh_exceptions_add and preference_doh_add_site_description translate "Add site" as "Přidat web"; the input field label for the same concept should use the same term.
- `preferences_site_settings` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Site settings" rendered as "Nastavení serveru" instead of the established "Nastavení stránky/webu".
    - Current: `Nastavení serveru`
    - Source: `Site settings`
    - Suggest: `Nastavení stránky`
    - "Site" in Firefox refers to a website, not a server; "server" is a wrong/legacy term inconsistent with other site-related strings.
- `quick_setting_option_autoplay_allowed` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Autoplay option label omits "automatické přehrávání" while the sibling options include it, making the set inconsistent.
    - Current: `Povolit zvuk i video`
    - Source: `Allow audio and video`
    - Suggest: `Povolit automatické přehrávání zvuků i videí`
    - The two related autoplay options are translated as "Blokovat automatické přehrávání zvuků"/"...zvuků i videí"; this one drops the autoplay notion, so the same setting group uses inconsistent terminology.
- `sports_widget_get_custom_wallpaper` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Menu item translated as an imperative sentence instead of an infinitive action label.
    - Current: `Získejte vlastní tapetu`
    - Source: `Get custom wallpaper`
    - Suggest: `Získat vlastní tapetu`
    - Menu items in the Czech Firefox UI use the infinitive (cf. "Odebrat", "Přeskočit", "Zobrazit výsledky" in this same widget); "Získejte" is an imperative addressing the user, inconsistent with the surrounding menu labels.
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Round of 16" is rendered as "Nejlepších 16" instead of the standard Czech football term "Osmifinále".
    - Current: `Nejlepších 16`
    - Source: `Round of 16`
    - Suggest: `Osmifinále`
    - In Czech football terminology the round of 16 is "osmifinále"; "Nejlepších 16" is a literal, non-standard rendering, inconsistent with the neighbouring "Čtvrtfinále"/"Semifinále".
- `sports_widget_round_of_32` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — "Round of 32" is rendered as "Nejlepších 32" instead of the standard Czech term "Šestnáctifinále".
    - Current: `Nejlepších 32`
    - Source: `Round of 32`
    - Suggest: `Šestnáctifinále`
    - Czech football terminology uses "šestnáctifinále" for the round of 32, consistent with "osmifinále", "čtvrtfinále", "semifinále" used elsewhere in the widget.
- `sports_widget_upcoming_match_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The English word "versus" is left untranslated in a Czech accessibility string.
    - Current: `%1$s versus %2$s`
    - Source: `Upcoming: %1$s versus %2$s, %3$s at %4$s`
    - Suggest: `%1$s proti %2$s`
    - This content description is read aloud; "versus" should be rendered in Czech (e.g. "proti") as the rest of the string is translated.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — `firstrun_shortcut_text` quotes “Přidat na plochu” but the string it names, `menu_add_to_home_screen`, reads “Přidat na domovskou obrazovku”
    - Current: `S aplikací %1$s se můžete rychle vrátit ke svým oblíbeným stránkám. Použijte „Přidat na plochu“ z nabídky aplikace %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Přidat na domovskou obrazovku`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_category_search` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Preference category title "Search" rendered as a verb ("Hledat") instead of a noun heading.
    - Current: `Hledat`
    - Source: `Search`
    - Suggest: `Vyhledávání`
    - This is a settings category heading alongside nouns like "Výkon", "Soukromí", "Zabezpečení"; the imperative verb form is inconsistent and wrong for a category label.
- `preference_privacy_block_analytics` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "analytic trackers" translated as "analytické prvky", dropping the "tracker" term used consistently in sibling strings.
    - Current: `Blokovat analytické prvky`
    - Source: `Block analytic trackers`
    - Suggest: `Blokovat analytické sledovací prvky`
    - Neighbouring settings render "trackers" as "sledovací prvky"; here the tracking notion is lost.
- `preference_site_permissions` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Site permissions" rendered as "Oprávnění serverů" instead of the site terminology used elsewhere.
    - Current: `Oprávnění serverů`
    - Source: `Site permissions`
    - Suggest: `Oprávnění stránek`
    - Elsewhere in this file "sites" is consistently translated as "stránky" (e.g. "Blokovat potenciálně nebezpečné a podvodné stránky"); "servery" means servers.

### E. Typography, punctuation & spacing

- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-cs/strings.xml` — Straight/English-style double quotes used instead of Czech german-double quotes.
    - Current: `z “%1$s” nahrajete`
    - Source: `Make sure you trust this site before you upload from “%1$s”.`
    - Suggest: `z „%1$s“ nahrajete`
    - The locale convention is german-double quotes („…“); the string uses “…” taken from the source.
- `bookmark_saved_in_folder_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Straight/English-style quotes used instead of Czech German-double quotes.
    - Current: `Uloženo do “%s”`
    - Source: `Saved in “%s”`
    - Suggest: `Uloženo do „%s“`
    - The locale convention is german-double quotes („…“); the target keeps the English curly opening/closing pair.
- `delete_all_history_group_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — The quotation marks around the group name placeholder were dropped.
    - Current: `Smazat všechny stránky v %s`
    - Source: `Delete all sites in “%s”`
    - Suggest: `Smazat všechny stránky v „%s“`
    - The source wraps the group name in typographic quotes; cs convention is german-double quotes, which should be preserved.
- `download_delete_single_item_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Uses straight/English-style curly quotes instead of the Czech german-double quotes.
    - Current: `Smazáno “%1$s”`
    - Source: `Deleted “%1$s”`
    - Suggest: `Smazáno „%1$s“`
    - The cs convention is german-double quotes („…“); the target keeps the English opening/closing curly quotes.
- `preference_doh_provider_custom_dialog_error_https` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Quotation marks use English-style opening curly quotes instead of Czech german-double quotes.
    - Current: `URL musí začínat “https://”`
    - Source: `URL must start with “https://”`
    - Suggest: `URL musí začínat „https://“`
    - The cs locale convention is german-double quotes („…“); the target keeps the source's English curly quotes.
- `search_add_custom_engine_suggest_string_example_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Straight/English double quotes used instead of Czech low-high quotes as in the parallel string.
    - Current: `výrazem “%s”`
    - Source: `Replace query with “%s”. Example: https://suggestqueries.google.com/complete/search?client=firefox&q=%s`
    - Suggest: `výrazem „%s“`
    - The locale convention is german-double quotes („ “), used correctly in search_add_custom_engine_search_string_example.
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-cs/strings.xml` — Straight/English double quotes used instead of Czech german-double quotes.
    - Current: `Záložky uloženy do složky “%s”`
    - Source: `Bookmarks saved in “%s”`
    - Suggest: `Záložky uloženy do složky „%s“`
    - The locale convention is german-double quotes („…“); the target keeps the English-style “…” pair.
- `contextmenu_erased_images_note2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Missing comma before the subordinate clause "když".
    - Current: `nebudou{ </b> } smazány když smažete historii`
    - Source: `Saved and shared images { <b> }will not be{ </b> } deleted when you erase %1$s history`
    - Suggest: `nebudou{ </b> } smazány, když smažete historii`
    - Czech requires a comma before the subordinating conjunction "když".
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Path separator inconsistently rendered as "->" instead of ">" in the settings path.
    - Current: `v části Nastavení -> Soukromí a zabezpečení > Zabezpečení`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `v části Nastavení > Soukromí a zabezpečení > Zabezpečení`
    - Source uses "Settings > Privacy & Security > Security" with ">" throughout; the Czech text mixes "->" and ">".
- `preference_remote_debugging` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Double slash typo between USB and Wi-Fi.
    - Current: `USB//Wi-Fi`
    - Source: `Remote debugging via USB/Wi-Fi`
    - Suggest: `USB/Wi-Fi`
    - Source is "USB/Wi-Fi" with a single slash; the duplicated slash is a typo.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Missing comma before the relative clause "které přidáte".
    - Current: `Pro stránky které přidáte`
    - Source: `For sites you add`
    - Suggest: `Pro stránky, které přidáte`
    - Czech requires a comma before a subordinate clause introduced by "které".

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/cs/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
