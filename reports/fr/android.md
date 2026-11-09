# Firefox for Android l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `f7a886b5b048` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,601 |
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
| quotes | `guillemet` 23 | **guillemet** |
| apostrophe | `typographic` 696 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| nbsp | `total` 214, `before-punctuation` 144, `space-before-punctuation` 62 | _mixed_ |
| register | `formal` 443 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (20)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 14 |
| 3 | Degraded language (grammar, spelling, terminology) | 6 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

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
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — "entering a text input field" (saisie dans un champ) is rendered as "création" (creating).
    - Current: `Libellé pour la création d’un champ de saisie de texte`
    - Source: `Label for entering a text input field`
    - Suggest: `Libellé pour la saisie dans un champ de texte`
    - The source labels the field where the user enters text; "création" says the label is for creating a field, which is a different meaning.
- `automatic_translation_option_always_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The translation reverses the meaning: the source says the app will translate this (source) language automatically, not translate the page into this language.
    - Current: `%1$s traduira automatiquement la page dans cette langue à son chargement.`
    - Source: `%1$s will translate this language automatically when the page loads.`
    - Suggest: `%1$s traduira automatiquement cette langue au chargement de la page.`
    - Source: "%1$s will translate this language automatically when the page loads." — the language is the one being translated from, matching the sibling strings ("ne proposera jamais de traduire les sites dans cette langue"). The current text says the page will be translated into that language.
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
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — "your active search engine" is translated as "moteur de recherche principal" (default/primary) instead of active/current.
    - Current: `défini comme moteur de recherche principal lors de la navigation`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `défini comme moteur de recherche actif lors de la navigation`
    - The source specifies the active search engine while browsing, not the primary/default one.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — The translation turns a data-sharing statement into an instruction to tell someone a story, and misattaches "with Mozilla's marketing partners".
    - Current: `Racontez votre découverte de Firefox et expliquez que vous l’utilisez avec les partenaires en technologies marketing de Mozilla.`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `Partagez avec les partenaires en technologies marketing de Mozilla la façon dont vous avez découvert Firefox et le fait que vous l’utilisez.`
    - The source means sharing, with Mozilla's marketing technology partners, how the user discovered Firefox and that they use it. The French reads as "Tell the story of your discovery... and explain that you use it with Mozilla's marketing partners", which changes the meaning (suggesting the user uses Firefox together with the partners) and loses the sharing/opt-in sense described in the developer co…
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

### C. Grammar, agreement & spelling

- `mozac_feature_addons_updater_permissions_dialog_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — The "or" between the two choices is missing, so the sentence is two orders joined by a comma.
    - Current: `actuels, mettez à jour`
    - Source: `Cancel to keep your current version and settings, or update to get the new version and approve the changes.`
    - Suggest: `actuels, ou mettez à jour`
    - The source offers a choice: "Cancel ... or update ...". Without "ou", the French reads as two instructions in a row.
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
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — Infinitive "Activer" used where the source is a descriptive third-person statement ("Enables").
    - Current: `Activer la protection`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `Active la protection`
    - The developer comment says this is a description of fingerprinters blocked by the protection; the source "Enables fingerprinting protection" is descriptive, not an imperative, matching the other description strings in the same group ("Efface…", "Limite…", "Empêche…").

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — The final period is missing, even though the developer comment says it matters because descriptions are concatenated.
    - Current: `dans les onglets ouverts`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `dans les onglets ouverts.`
    - The comment says multiple permissions are joined with a space, which is why the period is important. Without it, the sentences run together in the update notification.

---

## 4. Appendix

### Dismissed by hand (2)

- `mozac_feature_prompts_suggest_strong_password_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `tab_tray_close_tabs_banner_message` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (32)

- `add_private_tab` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 0bb53af7): unreliable finding: « Ouvrir un nouvel onglet privé » is an idiomatic label for the action; the difference is stylistic.
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string f8651f61): unreliable finding: There is no French equivalent for townland; choosing « Commune » is a localization decision, not a confirmed error.
- `browser_menu_webcompat_reporter_2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 7e2ede7e): unreliable finding: « Signaler des problèmes avec ce site » is a natural French label for reporting a broken site.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 5e8ed611): unreliable finding: The French conveys protecting saved payment methods in case someone accesses the device, which preserves the source intent.
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string fbcbce37): unreliable finding: Sibling strings are not visible to confirm plural usage; « Actif » is a plausible label.
- `download_time_period_older` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 17921018): unreliable finding: The groups precede it with last 30 days, so « Avant le mois dernier » is a reasonable adaptation; change would be stylistic.
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02, string 715c7d68): "Si + imparfait, conditionnel" ("Si vous poursuiviez…, vous ne devriez…") is the standard, grammatical French hypothetical construction.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string ea7063b0): unreliable finding: French Firefox localizations have used « Firefox suggère » for this feature label, so this may be an established locale choice.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02, string 0e45ab51): "Aidez-nous à" is the idiomatic French rendering of an object-less "Help (to) do X"; "Aidez à attraper" would be unnatural.
- `ip_protection_location_selection_reset_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 14d5968c): unreliable finding: « Connexion à l’emplacement recommandé » is an acceptable snackbar rendering; change would be stylistic.
- `mozac_browser_awesomebar_stock_suggestion_decrease` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02, string a7d7c9fe): A capital "A" without an accent is the correct verb form in "A perdu"; the finding itself admits it is correct and suggests the identical text.
- `mozac_compose_base_snackbar_dismiss_content_description` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 3c9cd745): unreliable finding: 'Masquer ce message' is a natural, correct rendering for dismissing a snackbar; preferring 'Ignorer' is stylistic.
- `mozac_feature_downloads_third_party_app_chooser_dialog_title` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 3c7cc219): unreliable finding: 'Continuer avec' is a common French rendering for Android app-chooser titles and conveys the intended action.
- `mozac_feature_downloads_time_remaining` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02, string b237052a): « dans %1$s » is a literal, faithful rendering of the source "in %1$s".
- `mozac_feature_listentopage_playback_speed_option` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string b97ca809): unreliable finding: Placing the multiplication sign before the number appears to be a deliberate display choice and is understandable as a speed factor.
- `mozac_feature_listentopage_playback_speed_option_default` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 84d30124): unreliable finding: « × 1 » is a common French typographic rendering of a speed multiplier and remains understandable as playback speed.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string c3bd6465): unreliable finding: In context, data not saved when leaving is data lost; the wording is an acceptable idiomatic equivalent.
- `mozac_feature_prompt_not_now` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 369eb2f9): unreliable finding: « Pas pour cette fois » is a valid rendering of "Not now"; aligning with « Plus tard » is a stylistic preference.
- `mozac_feature_prompt_repost_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 342f64e3): unreliable finding: « répéter des actions récentes » already conveys the duplication, so "twice" is implicitly covered.
- `mozac_feature_prompts_account_picture` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 3d1dcd15): unreliable finding: « Photo du profil » is a plausible, commonly used label for an account picture; the change is preferential.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string e2438e60): unreliable finding: The polite request rendering conveys the same appeal for permission; the suggested change is stylistic.
- `preference_doh_off_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02, string d5b6aabc): French naturally uses the definite article here; "le serveur … par défaut" conveys the same meaning as "your default".
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 7f15bc0c): unreliable finding: French Firefox localization deliberately renders the feature name Firefox Suggest as « Firefox suggère », so this is a team choice, not a clear error.
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 95d0a9b0): unreliable finding: French Firefox localization deliberately renders Firefox Suggest as « Firefox suggère »; consistent with string 1.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string f5d1b1b2): unreliable finding: « Recherche %s » works fine as a heading for search engine suggestions; the change would be stylistic.
- `setup_checklist_subtitle_6_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 34b78c78): unreliable finding: « Vous en êtes à quatre étapes » is idiomatic enough to show progress; the change is a matter of preference.
- `sign_out_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 45a5659a): unreliable finding: An infinitive question with « se » plus « votre » is a widespread, accepted pattern in French UI strings.
- `studies_active` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 7d94f015): unreliable finding: « Activées » agrees with « études » and is a valid label for active studies.
- `tab_group_onboarding_item_dismiss_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 3b2108db): unreliable finding: « accueil » is a common French Mozilla rendering of onboarding; the change would be stylistic.
- `webcompat_reporter_label_url` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 8c2d136e): unreliable finding: « Adresse web » is a standard French Mozilla rendering of URL for a field label; the change would be a preference.
- `webcompat_reporter_reason_media2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 878c5b54): unreliable finding: "Impossible de lire une vidéo ou de la charger" correctly conveys the problem; the change of subject is a stylistic preference, not an error.
- `webcompat_reporter_screen_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-09, string 7e2ede7e): unreliable finding: "Signaler des problèmes avec ce site" is an acceptable idiomatic rendering of the reporting action; the suggested wording is a preference.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/fr/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (27)

- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `browser_menu_extensions_review_update_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `share_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `translations_bottom_sheet_positive_button_error` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `wrex_widget_error_results_load_failed_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `wrex_widget_error_results_load_failed_title` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_browser_menu_highlighted` — `mozilla-mobile/android-components/components/browser/menu/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_browser_menu2_highlighted` — `mozilla-mobile/android-components/components/browser/menu2/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_feature_addons_permissions_extra_domains_description_plural_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_feature_prompts_suggest_strong_password_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_feature_readerview_serif_font` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `alternative_app_icon_option_gradient_sunrise` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `setup_checklist_task_search_widget_2` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `sync_failed_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `webcompat_reporter_send_report` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fr/strings.xml` — fixed 2026-10-12
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-10-12
- `firefox_labs_feature_conflict` — `mozilla-mobile/fenix/app/src/main/res/values-fr/strings.xml` — fixed 2026-10-12
- `mozac_feature_listentopage_notification_playback_speed_0_25` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — fixed 2026-10-05
- `mozac_feature_listentopage_notification_playback_speed_0_75` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — fixed 2026-10-05
- `mozac_feature_listentopage_notification_playback_speed_1_25` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — fixed 2026-10-05
- `mozac_feature_listentopage_notification_playback_speed_1_5` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — fixed 2026-10-05
- `mozac_feature_listentopage_notification_playback_speed_1_75` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fr/strings.xml` — fixed 2026-10-05
