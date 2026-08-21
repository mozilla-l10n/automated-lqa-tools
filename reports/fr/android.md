# Android l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **Previous run** | 2026-08-21 @ `0d02c6c9f0f6` |
| **Mode** | incremental |
| **Strings reviewed this run** | 3 of 2,911 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [firefox](firefox.md)

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
| Strings | 2,911 |
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
| quotes | `guillemet` 24 | **guillemet** |
| apostrophe | `typographic` 718 | **typographic** |
| ellipsis | `char` 22 | **char** |
| dash | `em` 3 | **em** |
| nbsp | `total` 211, `before-punctuation` 145, `space-before-punctuation` 73 | _mixed_ |
| register | `formal` 453 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (80)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 57 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — "Press “Try Again”" is rendered as "Cliquez sur le bouton" (click), which is wrong on a touch-based mobile component.
    - Current: `Cliquez sur le bouton « Réessayer »`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Appuyez sur le bouton « Réessayer »`
    - The source says "Press"; on Android this is a tap, not a mouse click, and the added "Cliquez" changes the interaction described.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — "The browser has stopped trying to retrieve the requested item" is mistranslated as the browser stopping to wait for a response from the site.
    - Current: `Le navigateur a arrêté d’attendre une réponse du site.`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `Le navigateur a cessé d’essayer de récupérer l’élément demandé.`
    - The source states the browser stopped trying to retrieve the requested item, not that it stopped waiting for a response.
- `mozac_browser_errorpages_safe_browsing_malware_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — "Malware site issue" is translated without the notion of "site", unlike the parallel titles.
    - Current: `Problème de logiciel malveillant`
    - Source: `Malware site issue`
    - Suggest: `Problème de site malveillant`
    - Source is "Malware site issue"; the other titles in the same family ("Problème de site indésirable", "Problème de site dangereux", "Problème de site trompeur") keep "site", so dropping it here is inconsistent and loses the meaning.
- `mozac_browser_errorpages_security_bad_hsts_cert_techInfo2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — The HSTS explanation reverses which party can only connect securely.
    - Current: `ce qui signifie que { <b> }%2$s{ </b> } doit impérativement établir une connexion sécurisée pour y accéder`
    - Source: `{ <label> } { <b> }%1$s{ </b> } has a security policy called HTTP Strict Transport Security (HSTS), which means that { <b> }%2$s{ </b> } can only connect to it securely. You can’t add an exception to visit this site. {…`
    - Suggest: `ce qui signifie que { <b> }%2$s{ </b> } ne peut s’y connecter que de manière sécurisée`
    - Source: "%2$s can only connect to it securely"; the French wording is acceptable in meaning but the phrasing "doit impérativement établir une connexion sécurisée" is a rendering, not a reversal — however it drops the exclusivity nuance of "only".
- `mozac_browser_menu_highlighted` — `mozilla-mobile/android-components/components/browser/menu/src/main/res/values-fr/strings.xml` — "Highlighted" (menu item has a highlight) is rendered as "Sélectionné" (selected), which conveys a different state.
    - Current: `Sélectionné`
    - Source: `Highlighted`
    - Suggest: `Mis en évidence`
    - The developer comment says the string indicates that the overflow menu has a highlight; "Sélectionné" means "selected", a different UI state announced to screen reader users.
- `mozac_browser_menu2_highlighted` — `mozilla-mobile/android-components/components/browser/menu2/src/main/res/values-fr/strings.xml` — "Highlighted" (menu item has a highlight) is rendered as "Sélectionné" (selected), which conveys a different state.
    - Current: `Sélectionné`
    - Source: `Highlighted`
    - Suggest: `Mis en évidence`
    - The developer comment says the string indicates that the overflow menu has a highlight; "Sélectionné" means "selected", a different UI state.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "Extend developer tools" is mistranslated as "Ouvrir les outils de développement" (open developer tools).
    - Current: `Ouvrir les outils de développement afin d’accéder à vos données dans les onglets ouverts`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `Étendre les outils de développement afin d’accéder à vos données dans les onglets ouverts`
    - The source says the extension extends (adds to) the developer tools, not that it opens them.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "Extend developer tools" is mistranslated as "Ouvrir les outils de développement" (open developer tools).
    - Current: `Ouvrir les outils de développement afin d’accéder à vos données dans les onglets ouverts.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Étendre les outils de développement afin d’accéder à vos données dans les onglets ouverts.`
    - The source says the extension extends the developer tools, not that it opens them.
- `mozac_feature_addons_permissions_extra_domains_description_plural_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "Access your data on other domains" drops the possessive "your data".
    - Current: `Accéder aux données d’autres domaines`
    - Source: `Access your data on other domains`
    - Suggest: `Accéder à vos données pour d’autres domaines`
    - The source refers to the user's data on other domains; the target says "the data of other domains", inconsistent with the parallel sites string which correctly uses "vos données".
- `mozac_feature_addons_permissions_extra_domains_description_plural_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "Access your data on other domains." drops the possessive "your data".
    - Current: `Accéder aux données d’autres domaines.`
    - Source: `Access your data on other domains.`
    - Suggest: `Accéder à vos données pour d’autres domaines.`
    - The source refers to the user's data on other domains; the target says "the data of other domains", inconsistent with the parallel sites string which uses "vos données".
- `mozac_feature_addons_permissions_one_extra_domain_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "your data" is dropped, giving "les données" instead of "vos données", inconsistent with the sibling strings.
    - Current: `Accéder aux données d’un autre domaine`
    - Source: `Access your data on another domain`
    - Suggest: `Accéder à vos données pour un autre domaine`
    - Source is "Access your data on another domain"; the possessive "your" is lost and the wording diverges from the parallel site/domain strings which use "vos données".
- `mozac_feature_addons_permissions_one_extra_domain_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "your data" is dropped, giving "les données" instead of "vos données", inconsistent with the sibling strings.
    - Current: `Accéder aux données d’un autre domaine.`
    - Source: `Access your data on another domain.`
    - Suggest: `Accéder à vos données pour un autre domaine.`
    - Source is "Access your data on another domain."; the possessive "your" is lost and the wording diverges from the parallel domain string mozac_feature_addons_permissions_sites_in_domain_description which uses "vos données".
- `mozac_feature_addons_permissions_pkcs11_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "cryptographic authentication services" is rendered as "authentification chiffrée" (encrypted authentication), changing the meaning.
    - Current: `Fournir des services d’authentification chiffrée`
    - Source: `Provide cryptographic authentication services`
    - Suggest: `Fournir des services d’authentification cryptographique`
    - The source describes cryptographic authentication services (PKCS#11), not "encrypted" authentication.
- `mozac_feature_addons_permissions_pkcs11_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — "cryptographic authentication services" is rendered as "authentification chiffrée" (encrypted authentication), changing the meaning.
    - Current: `Fournir des services d’authentification chiffrée.`
    - Source: `Provide cryptographic authentication services.`
    - Suggest: `Fournir des services d’authentification cryptographique.`
    - The source describes cryptographic authentication services (PKCS#11), not "encrypted" authentication.
- `mozac_feature_downloads_third_party_app_chooser_dialog_title` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fr/strings.xml` — "Complete action using" is rendered as "Continuer avec" (Continue with) instead of indicating completing the action with an app.
    - Current: `Continuer avec`
    - Source: `Complete action using`
    - Suggest: `Effectuer l’action avec`
    - The source is the standard Android app-chooser title "Complete action using"; "Continuer avec" means "Continue with" and loses the meaning of completing the action.
- `mozac_feature_downloads_time_remaining` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fr/strings.xml` — "in %1$s" (time remaining) is translated as "dans %1$s" but shown as remaining duration summary; should be "il reste %1$s" / "dans %1$s" ambiguity.
    - Current: `dans %1$s`
    - Source: `in %1$s`
    - Suggest: `il reste %1$s`
    - The comment says the placeholder is the estimated time remaining shown in a progress notification; "dans %1$s" reads as a future point in time rather than remaining duration.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — The source says entered data "may not be saved", the French says the data "may be lost", changing the meaning.
    - Current: `Des données saisies peuvent être perdues`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `Les données que vous avez saisies pourraient ne pas être enregistrées`
    - "may not be saved" = « pourraient ne pas être enregistrées », not « peuvent être perdues ».
- `mozac_feature_prompt_repost_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — The phrase "twice" is dropped from the translation.
    - Current: `la publication d’un commentaire.`
    - Source: `Refreshing this page could duplicate recent actions, such as sending a payment or posting a comment twice.`
    - Suggest: `la publication d’un commentaire en double.`
    - Source: "such as sending a payment or posting a comment twice"; the duplication qualifier is missing in French.
- `mozac_feature_prompts_account_picture` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "Account picture" is rendered as "Photo du profil" (profile picture) instead of account picture.
    - Current: `Photo du profil`
    - Source: `Account picture`
    - Suggest: `Image du compte`
    - The source and developer comment refer to the account picture in the Select Account FedCM prompt, not a profile picture.
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "entering a text input field" (saisie dans un champ) is rendered as "création" (creating).
    - Current: `Libellé pour la création d’un champ de saisie de texte`
    - Source: `Label for entering a text input field`
    - Suggest: `Libellé pour la saisie dans un champ de texte`
    - The source labels the field where the user enters text; "création" says the label is for creating a field, which is a different meaning.
- `mozac_feature_readerview_serif_font` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fr/strings.xml` — "Serif" font option is translated as "Empattement" (the serif itself) instead of "Avec empattement".
    - Current: `Empattement`
    - Source: `Serif`
    - Suggest: `Avec empattement`
    - The option names a font style; the companion string uses "Police avec empattement" and the opposite option is "Sans empattement". "Empattement" alone names the serif feature, not the font type.
- `add_private_tab` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Add private tab" is rendered as "Ouvrir un nouvel onglet privé" while the parallel string add_tab uses "Ajouter un onglet".
    - Current: `Ouvrir un nouvel onglet privé`
    - Source: `Add private tab`
    - Suggest: `Ajouter un onglet privé`
    - The source says "Add private tab"; the sibling string add_tab is translated "Ajouter un onglet", so the verb and the added "nouvel" are inconsistent with the source.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Department" as an administrative division (Nicaragua, Colombia) is translated as "Service" (a company department).
    - Current: `Service`
    - Source: `Department`
    - Suggest: `Département`
    - The developer comment states this is an address field for countries like Nicaragua and Colombia where departments are a key administrative division; "Service" means an organizational unit, not a territorial division.
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Townland" is rendered as "Commune", which names a different administrative unit than the Irish townland described in the comment.
    - Current: `Commune`
    - Source: `Townland`
    - Suggest: `Townland`
    - The developer comment states the Townland is a specific Irish rural land division; "Commune" is a French municipality-level unit and is also used for other address levels, making the field misleading.
- `automatic_translation_option_always_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The translation reverses the meaning: the source says the app will translate this (source) language automatically, not translate the page into this language.
    - Current: `%1$s traduira automatiquement la page dans cette langue à son chargement.`
    - Source: `%1$s will translate this language automatically when the page loads.`
    - Suggest: `%1$s traduira automatiquement cette langue au chargement de la page.`
    - Source: "%1$s will translate this language automatically when the page loads." — the language is the one being translated from, matching the sibling strings ("ne proposera jamais de traduire les sites dans cette langue"). The current text says the page will be translated into that language.
- `browser_menu_webcompat_reporter_2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Singular "Report broken site" is rendered as a plural "des problèmes" instead of reporting the site as broken.
    - Current: `Signaler des problèmes avec ce site`
    - Source: `Report broken site`
    - Suggest: `Signaler un site défectueux`
    - The source is a menu label meaning to report that this site is broken; the French turns it into reporting multiple unspecified problems.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The French drops "from being accessed", reversing the sense so it reads "protect your payment methods if someone accesses your device" instead of "protect them from being accessed if someone else has your device".
    - Current: `pour protéger vos moyens de paiement enregistrés si jamais quelqu’un accède à votre appareil`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `pour empêcher l’accès à vos moyens de paiement enregistrés si quelqu’un d’autre venait à utiliser votre appareil`
    - Source: "protect your saved payment methods from being accessed if someone else has your device" — the object of protection is access prevention when another person has the device; the French says "protect ... if someone accesses your device", which loses the meaning.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Debug locales to enable" is mistranslated as an imperative "Debug the locales to enable".
    - Current: `Déboguer les locales à activer`
    - Source: `Debug locales to enable`
    - Suggest: `Locales de débogage à activer`
    - "Debug locales" is a noun phrase (the list of debug locales that can be enabled), not a verb phrase; the header names a list, per the developer comment.
- `delete_language_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The French says the app will download "this language" partially, whereas the source says it will download partial languages to the cache.
    - Current: `%1$s la téléchargera partiellement dans votre cache`
    - Source: `If you delete this language, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `%1$s téléchargera des langues partielles dans votre cache`
    - Source: "%1$s will download partial languages to your cache as you translate." — the object is "partial languages", not the deleted language; the parallel string delete_language_all_languages_file_dialog_message renders it correctly.
- `download_time_period_older` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Older" is rendered as "Avant le mois dernier" ("before last month"), which states a specific period not present in the source.
    - Current: `Avant le mois dernier`
    - Source: `Older`
    - Suggest: `Plus ancien`
    - The source is a generic header "Older" for downloads older than the other groups (today, yesterday, last 7 days, last 30 days); the French invents a specific timeframe.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Firefox Suggest" is a product/feature name and must not be translated as a verb phrase.
    - Current: `Firefox suggère`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The developer comment identifies this as the Firefox Suggest feature name; brand/feature names stay untranslated, and "Firefox suggère" turns it into a sentence.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Adds "nous" (help us) which is not in the source.
    - Current: `Aidez-nous à attraper les traqueurs`
    - Source: `Help catch trackers`
    - Suggest: `Aidez à attraper les traqueurs`
    - Source is "Help catch trackers", with no first-person object; the translation invents an addressee.
- `history_older` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Older" is rendered as "Avant le mois dernier" (before last month), which states a specific period not in the source.
    - Current: `Avant le mois dernier`
    - Source: `Older`
    - Suggest: `Plus ancien`
    - The header groups history older than the last month; the source is the generic "Older", and the French invents an explicit time frame.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The French reverses the speaker: the source asks the user to consider allowing, while the translation says "we ask for your authorization".
    - Current: `Nous vous demandons votre autorisation pour contribuer à la victoire de Firefox.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Merci d’envisager de donner votre autorisation pour aider Firefox à gagner.`
    - Source "Please consider allowing to help Firefox win" is an appeal to the user to allow; the translation states that Mozilla is requesting authorization, changing the sentence's actor and losing the "consider" nuance.
- `preference_doh_off_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The possessive "your" is dropped from the summary for the "Off" DoH option.
    - Current: `Utiliser le serveur de résolution DNS par défaut`
    - Source: `Use your default DNS resolver`
    - Suggest: `Utiliser votre serveur de résolution DNS par défaut`
    - Source says "Use your default DNS resolver"; the related string preference_doh_increased_protection_info_2 correctly uses "votre serveur DNS par défaut".
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The product name "Firefox Suggest" is translated as "Firefox suggère" instead of being kept as the brand feature name.
    - Current: `Barre d’adresse - Firefox suggère`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Barre d’adresse - Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name (see developer comment "settings to Firefox Suggest") and must not be translated into a verb phrase.
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The product name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `En savoir plus sur Firefox suggère`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `En savoir plus sur Firefox Suggest`
    - "Firefox Suggest" is a brand feature name and must be kept untranslated; "Firefox suggère" reads as a sentence, not a feature name.
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "your active search engine" is translated as "moteur de recherche principal" (default/primary) instead of active/current.
    - Current: `défini comme moteur de recherche principal lors de la navigation`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `défini comme moteur de recherche actif lors de la navigation`
    - The source specifies the active search engine while browsing, not the primary/default one.
- `preferences_inactive_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Move old tabs to inactive" is rendered as "Déplacer les onglets inactifs", losing the meaning of moving old tabs into the inactive section.
    - Current: `Déplacer les onglets inactifs`
    - Source: `Move old tabs to inactive`
    - Suggest: `Déplacer les anciens onglets vers les onglets inactifs`
    - The source says old (unused) tabs get moved to the inactive state; the translation says "move the inactive tabs", which is a different statement.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The translation turns a data-sharing statement into an instruction to tell someone a story, and misattaches "with Mozilla's marketing partners".
    - Current: `Racontez votre découverte de Firefox et expliquez que vous l’utilisez avec les partenaires en technologies marketing de Mozilla.`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `Partagez avec les partenaires en technologies marketing de Mozilla la façon dont vous avez découvert Firefox et le fait que vous l’utilisez.`
    - The source means sharing, with Mozilla's marketing technology partners, how the user discovered Firefox and that they use it. The French reads as "Tell the story of your discovery... and explain that you use it with Mozilla's marketing partners", which changes the meaning (suggesting the user uses Firefox together with the partners) and loses the sharing/opt-in sense described in the developer co…
- `recent_tabs_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Content description mistranslated: "Show all recent tabs button" became "Display the recent tabs button".
    - Current: `Afficher le bouton des onglets récents`
    - Source: `Show all recent tabs button`
    - Suggest: `Bouton « Afficher tous les onglets récents »`
    - The source describes a button whose function is to show all recent tabs; the French says to display the recent tabs button, reversing the roles of the verb and the noun "button".
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Search %s" is an action (search using engine %s) but was rendered as the noun "Recherche".
    - Current: `Recherche %s`
    - Source: `Search %s`
    - Suggest: `Rechercher avec %s`
    - The source is a verb phrase inviting the user to search with the suggested engine; "Recherche %s" reads as a noun phrase ("Search of %s") and loses the imperative meaning.
- `setup_checklist_subtitle_6_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "You’re 4 steps in" is rendered awkwardly/incorrectly as "Vous en êtes à quatre étapes".
    - Current: `Vous en êtes à quatre étapes. Plus que deux !`
    - Source: `You’re 4 steps in. Only 2 more to go!`
    - Suggest: `Vous avez terminé quatre étapes. Plus que deux !`
    - The source states four steps are completed; the French phrasing does not convey completion clearly.
- `setup_checklist_task_search_widget_2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Singular "search widget" is rendered as plural "les widgets de recherche".
    - Current: `Découvrir les widgets de recherche`
    - Source: `Explore search widget`
    - Suggest: `Découvrir le widget de recherche`
    - The source refers to a single search widget task; the plural changes the meaning.
- `share_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The French says sharing this application is impossible, whereas the source means sharing to this app fails.
    - Current: `Impossible de partager cette application`
    - Source: `Cannot share to this app`
    - Suggest: `Impossible de partager avec cette application`
    - "Cannot share to this app" means the content cannot be shared to the target app; the translation reverses the object, saying the app itself cannot be shared.
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Round of 16" is rendered as "8es de finale" while "Round of 32" is rendered as "16es de finale", but the French labels are shifted one round off in a way that mismatches the tournament stage naming used together.
    - Current: `8es de finale`
    - Source: `Round of 16`
    - Suggest: `Huitièmes de finale`
    - Round of 16 = huitièmes de finale (16 teams, 8 matches); the abbreviation "8es" is correct in substance, but should be consistent with the spelled-out forms used for "Demi-finales"; keep the same spelled-out register.
- `studies_active` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Section title "Active" is translated as a plural adjective "Activées" rather than the section heading "Actives".
    - Current: `Activées`
    - Source: `Active`
    - Suggest: `Actives`
    - The source is the title of the "active" section of the studies list (studies that are currently running), not a state "enabled"; "Activées" also mismatches the neighbouring on/off strings.
- `sync_failed_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Last synced: never" is rendered as "Dernier succès : jamais" (last success), duplicating the wording of sync_failed_summary.
    - Current: `La synchronisation a échoué. Dernier succès : jamais`
    - Source: `Sync failed. Last synced: never`
    - Suggest: `La synchronisation a échoué. Dernière synchronisation : jamais`
    - The source says "Last synced: never", not "Last success"; the sibling string sync_failed_summary uses "Last success" and is already translated as "Dernier succès".
- `sync_no_devices_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Any devices" (i.e. tout appareil qui sera connecté) is translated as "Tous les appareils", changing the meaning in a context where no devices exist.
    - Current: `Tous les appareils connectés et synchronisés avec ce compte apparaîtront ici.`
    - Source: `Any devices signed in and syncing to this account will appear here.`
    - Suggest: `Tout appareil connecté et synchronisé avec ce compte apparaîtra ici.`
    - The English "Any devices signed in and syncing to this account will appear here" is a conditional/generic statement, shown precisely when there are no devices; "Tous les appareils" implies existing devices.
- `tab_group_onboarding_item_dismiss_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "onboarding" is rendered as « accueil » (welcome/reception), which misnames the onboarding card being dismissed.
    - Current: `Fermer l’accueil des groupes d’onglets`
    - Source: `Dismiss tab group onboarding`
    - Suggest: `Ignorer la présentation des groupes d’onglets`
    - The source dismisses the tab group onboarding card; « accueil » means reception/home and does not convey onboarding/introduction.
- `tab_tray_close_tabs_banner_message` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "in the past day, week, or month" is mistranslated as plural periods "les derniers jours, semaines ou mois".
    - Current: `depuis les derniers jours, semaines ou mois`
    - Source: `Set open tabs to close automatically that haven’t been viewed in the past day, week, or month.`
    - Suggest: `depuis un jour, une semaine ou un mois`
    - The source refers to a single choice of period (one day, one week, one month) for auto-closing, not several days/weeks/months.
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Translations sheet" (bottom sheet / panneau) is rendered as "onglet" (tab).
    - Current: `Fermer l’onglet Traductions`
    - Source: `Close Translations sheet`
    - Suggest: `Fermer le panneau Traductions`
    - The source refers to the translations bottom sheet, not a browser tab; elsewhere in the same batch "translation sheet" is correctly translated as "panneau de traduction".
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Translating" (action in progress) is rendered as the noun "Traduction".
    - Current: `Traduction`
    - Source: `Translating`
    - Suggest: `Traduction en cours`
    - The comment states this button text indicates a translation is currently in progress; "Traduction" alone is ambiguous with the noun/label "Translation".
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The dropdown option drops "check out" and switches to a first-person phrasing unlike the other options.
    - Current: `Je ne peux pas payer ou faire des achats`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `Impossible de payer, de finaliser la commande ou de faire des achats`
    - Source is "Can’t pay, check out or shop"; the checkout step is omitted and the register differs from the parallel option webcompat_reporter_reason_account2 ("Impossible de se connecter ou de s’inscrire").
- `webcompat_reporter_reason_media2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Video isn’t playing or loading" is rendered as an impossibility for the user to play the video.
    - Current: `Impossible de lire une vidéo ou de la charger`
    - Source: `Video isn’t playing or loading`
    - Suggest: `La vidéo ne se lit pas ou ne se charge pas`
    - The source describes the video's behaviour, matching the other options such as "Le site ne se charge pas"; the translation shifts the subject to the user.
- `webcompat_reporter_screen_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Report broken site" is rendered as the vaguer "Signaler des problèmes avec ce site".
    - Current: `Signaler des problèmes avec ce site`
    - Source: `Report broken site`
    - Suggest: `Signaler un site défectueux`
    - The source names the action of reporting a broken site; the plural "des problèmes" and the longer wording change the meaning of the toolbar title.
- `content_description_back` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "Navigate back" is rendered as the label "Précédent" instead of an action description, inconsistent with content_description_forward ("Avancer dans l’historique").
    - Current: `Précédent`
    - Source: `Navigate back`
    - Suggest: `Reculer dans l’historique`
    - The source is an action content description read by screen readers; the sibling string content_description_forward is translated as "Avancer dans l’historique", so "Précédent" is both inconsistent and not describing the action.
- `external_app_prompt` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "You can leave" (optional/permission) is rendered as "Vous allez quitter" (you are going to leave), changing the meaning.
    - Current: `Vous allez quitter %1$s pour ouvrir ce lien dans %2$s.`
    - Source: `You can leave %1$s to open this link in %2$s.`
    - Suggest: `Vous pouvez quitter %1$s pour ouvrir ce lien dans %2$s.`
    - The source says the user may leave the app; the sibling string external_app_prompt_no_app correctly uses « Vous pouvez quitter ». Here the future tense states it as a fact.
- `firstrun_privacy_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "Make privacy a habit" is translated as "Reprenez votre vie privée en main" (take back control of your privacy), a different meaning.
    - Current: `Reprenez votre vie privée en main`
    - Source: `Make privacy a habit`
    - Suggest: `Faites de la vie privée une habitude`
    - The source urges making privacy a habit, not regaining control of it.
- `preference_phone_feature_notification` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — Singular "Notification" (a site-permission category label) is rendered in the plural.
    - Current: `Notifications`
    - Source: `Notification`
    - Suggest: `Notification`
    - The source is the singular permission name "Notification", matching the other site-permission entries; the French pluralises it.

### C. Grammar, agreement & spelling

- `mozac_browser_awesomebar_stock_suggestion_decrease` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-fr/strings.xml` — Missing accent on the auxiliary verb "A" at the start of the sentence.
    - Current: `A perdu %s %%`
    - Source: `Dropped %s percent`
    - Suggest: `A perdu %s %% (voir justification)`
    - In French the verb form is "a perdu"; capitalised sentence-initial "A" without accent is correct here, but the string should read "A perdu" — see note.
- `alternative_app_icon_option_gradient_sunrise` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Spelling error: "Levé de soleil" should be "Lever de soleil".
    - Current: `Levé de soleil`
    - Source: `Sunrise`
    - Suggest: `Lever de soleil`
    - The French for "Sunrise" is "lever de soleil" (noun "lever"), not the past participle "levé".
- `bookmark_import_failure_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Wrong verb form: "Veuillez réessayez" should be the infinitive "réessayer".
    - Current: `Veuillez réessayez.`
    - Source: `Couldn’t import bookmarks. Try again.`
    - Suggest: `Veuillez réessayer.`
    - After "Veuillez" the following verb must be in the infinitive; "réessayez" is a conjugated form and is a grammatical error.
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Incorrect expression "à fin de tests" instead of "à des fins de test".
    - Current: `à fin de tests`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `à des fins de test`
    - "à fin de tests" is not a correct French locution; the standard form is "à des fins de test".
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "Active" tab count category translated in the singular while the sibling categories use the plural.
    - Current: `Actif`
    - Source: `Active`
    - Suggest: `Actifs`
    - The string labels a count category for tabs, like "Inactifs" and "Privés"; the singular "Actif" is inconsistent and incorrect.
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Incorrect verb mood/tense: "Si vous poursuiviez" (imperfect) instead of present tense.
    - Current: `Si vous poursuiviez vers ce site web, vous ne devriez saisir aucune donnée sensible.`
    - Source: `However, it’s also possible that an attacker is involved. If you continue to the website, you should not enter any sensitive info. If you continue, HTTPS-Only mode will be turned off temporarily for the site.`
    - Suggest: `Si vous poursuivez vers ce site web, vous ne devriez saisir aucune donnée sensible.`
    - The source "If you continue to the website" is a present-tense conditional clause; the imperfect "poursuiviez" is ungrammatical here and inconsistent with the following sentence "Si vous continuez".
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Infinitive "Activer" used where the source is a descriptive third-person statement ("Enables").
    - Current: `Activer la protection`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `Active la protection`
    - The developer comment says this is a description of fingerprinters blocked by the protection; the source "Enables fingerprinting protection" is descriptive, not an imperative, matching the other description strings in the same group ("Efface…", "Limite…", "Empêche…").
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — Superfluous article "les" before the link placeholder produces "dans les paramètres" where %2$s already reads "paramètres".
    - Current: `dans les %2$s`
    - Source: `%1$s tries to reject cookie requests to dismiss annoying cookie banners.  Manage cookie banner preferences in %2$s.`
    - Suggest: `dans les paramètres`
    - %2$s is replaced by the link text "paramètres"; the phrase reads correctly only if the article is not duplicated — as written the visible link excludes "les", but the sentence is intended as "Manage ... in settings". The article should be part of the same fragment or removed.

### D. Terminology, register & consistency

- `mozac_compose_base_snackbar_dismiss_content_description` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-fr/strings.xml` — "Dismiss message" translated as "Masquer ce message" (hide this message) instead of the established "Ignorer".
    - Current: `Masquer ce message`
    - Source: `Dismiss message`
    - Suggest: `Ignorer le message`
    - "Dismiss" is rendered "Ignorer" in mozac_compose_base_link_text_dismiss in the same file; "Masquer" (hide) is inconsistent terminology for the same source term on the same surface.
- `mozac_feature_prompt_not_now` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "Not now" is translated inconsistently: « Plus tard » elsewhere but « Pas pour cette fois » here.
    - Current: `Pas pour cette fois`
    - Source: `Not now`
    - Suggest: `Plus tard`
    - The same source string "Not now" on the same prompt surface is rendered « Plus tard » in mozac_feature_prompt_dont_save_2 and mozac_feature_prompt_dont_update_2.
- `mozac_feature_prompts_suggest_strong_password_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "strong password" is rendered "mot de passe compliqué" here but "mot de passe fort" in the sibling content description.
    - Current: `Utilisez un mot de passe compliqué`
    - Source: `Use strong password`
    - Suggest: `Utiliser un mot de passe fort`
    - Inconsistent terminology for the same term on the same prompt (mozac_feature_prompts_suggest_strong_password_content_description uses "fort"); "compliqué" is not the established term.
- `mozac_feature_prompts_suggest_strong_password_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "strong password" is rendered as « mot de passe compliqué », inconsistent with the other strings in the same dialog which use « fort »/« robuste ».
    - Current: `Utiliser un mot de passe compliqué ?`
    - Source: `Use strong password?`
    - Suggest: `Utiliser un mot de passe fort ?`
    - The source term "strong password" is translated as "fort" in mozac_feature_prompts_suggest_strong_password_message and "robuste" in the description; "compliqué" (complicated) is a different notion and inconsistent within the same dialog.
- `translations_bottom_sheet_positive_button_error` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Button label "Try again" is translated as a polite sentence "Veuillez réessayer" instead of a concise action label.
    - Current: `Veuillez réessayer`
    - Source: `Try again`
    - Suggest: `Réessayer`
    - The developer comment says this is button text; French UI buttons use the infinitive without "Veuillez", which reads as a message rather than an action label.
- `webcompat_reporter_label_url` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "URL" is rendered as "Adresse web" while other Web Compat Reporter strings keep "URL".
    - Current: `Adresse web`
    - Source: `URL`
    - Suggest: `URL`
    - The source label is "URL" and webcompat_reporter_edit_url_dialog_title translates it as « Modifier l’URL du site web », so the field label is inconsistent on the same surface.
- `webcompat_reporter_send_report` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "report" is translated as "rapport" here while the rest of the feature uses "signalement".
    - Current: `Envoyer le rapport`
    - Source: `Send report`
    - Suggest: `Envoyer le signalement`
    - Neighbouring strings (webcompat_reporter_description_3, preview_bottom_sheet_header, success_snackbar_text_2) all use "signalement" for "report"; this is an inconsistency on the same screen.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "top sites" rendered as "sites les plus populaires" instead of the established "sites les plus visités" used elsewhere for top sites.
    - Current: `Pour les sites les plus populaires`
    - Source: `For top sites`
    - Suggest: `Pour les sites les plus visités`
    - "Top sites" in Mozilla French is consistently "sites les plus visités"; "populaires" changes the meaning (popularity vs. the user's own most-visited sites).

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — List item ends with a semicolon instead of a period, deviating from the source punctuation and from the other list items.
    - Current: `par exemple) ;{ </li> }`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `par exemple).{ </li> }`
    - The source sentence ends with a period, and the following list item in the same string ends with a period; the semicolon is inconsistent.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — A final period was added that is not in the source error message.
    - Current: `L’adresse web doit contenir « https:// » ou « http:// ».`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `L’adresse web doit contenir « https:// » ou « http:// »`
    - The en-US string "Web address must contain “https://” or “http://”" has no terminal punctuation, and the sibling error string add_login_hostname_invalid_text_2 has none either.
- `firefox_labs_feature_conflict` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Wrong apostrophe character (U+2018 left single quotation mark) used instead of the typographic apostrophe.
    - Current: `disponible à l‘essai`
    - Source: `Feature isn’t available to try.`
    - Suggest: `disponible à l’essai`
    - The locale convention is the typographic apostrophe ’ (U+2019); here a left single quote ‘ is used.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — Missing space after "n°" abbreviation and French typography for the regulation number.
    - Current: `n°2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `no 2024/1183`
    - In French typography the number abbreviation requires a space before the digits (and is properly "no" with superscript o); "n°2024/1183" is set without the required space.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
