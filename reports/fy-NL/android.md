# Android l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **Previous run** | 2026-08-20 @ `afd16223d876` |
| **Mode** | baseline |
| **Strings reviewed this run** | 2,908 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (167)

- `mozac_browser_errorpages_archive_check_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "argivearre" — Frisian for archived is "argivearre"? actually the root is "argyf", so the participle should be "argivearre" spelled consistently with the noun.
    - Current: `Argivearre ferzje kontrolearje`
    - Source: `Check Archived Version`
    - Suggest: `Argyfferzje kontrolearje`
    - Elsewhere in the same file the archive is rendered "argyf"/"argyftsjinst"; "Argivearre" is an inconsistent, non-standard derivation.
- `mozac_browser_errorpages_malformed_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Unjildich".
    - Current: `Unjildich adres`
    - Source: `Invalid Address`
    - Suggest: `Ûnjildich adres`
    - The Frisian word is "ûnjildich" with a circumflex; the same prefix is written "ûnjildige" in mozac_browser_errorpages_invalid_content_encoding_message.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "temporary outage" is rendered as "stroomûnderbrekking" (power cut), changing the meaning.
    - Current: `in tydlike stroomûnderbrekking`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `in tydlike steuring`
    - The source refers to a temporary service outage of the server, not an electrical power interruption.
- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Predicative adjective wrongly inflected: "oerbelêste" should be "oerbelêst".
    - Current: `of oerbelêste`
    - Source: `{ <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If you are unable to load any pages, check your device’s data or Wi-Fi connection.{ </li> } { </ul> }`
    - Suggest: `of oerbelêst`
    - In predicative position after "is ... net beskikber of" the adjective takes no -e ending.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "potentially harmful site" is rendered as "fertochte side" (suspicious site), duplicating the malware string instead of translating "potentially harmful".
    - Current: `is rapportearre as in fertochte side`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `is rapportearre as in mooglik skealike website`
    - The source says the site has been reported as a potentially harmful site; the target says "suspicious site", the same wording used for the malware/attack-site string, losing the source meaning. The corresponding title correctly uses "skealike website".
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "in oarder" should be "yn oarder" (typo for the preposition).
    - Current: `Is de proxykonfiguraasje fan de browser in oarder?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `Is de proxykonfiguraasje fan de browser yn oarder?`
    - Spelling error: the preposition is "yn", as correctly used in the parallel string mozac_browser_errorpages_unknown_proxy_host_message.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Wrong article gender: "It website" should be "De website".
    - Current: `It website ferwiist de oanfraach troch`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `De website ferwiist de oanfraach troch`
    - "website" takes the common-gender article "de" in Frisian, as used elsewhere in this same file ("De website op %1$s …").
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "net werkend" is a misspelling of "net werkent" (does not recognize).
    - Current: `dat de browser net werkend`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `dat de browser net werkent`
    - The verb form for "the browser does not recognize" is "werkent"; "werkend" is a participle/adjective form and is ungrammatical here.
- `mozac_cfr_dismiss_button_content_description` — `mozilla-mobile/android-components/components/compose/cfr/src/main/res/values-fy-rNL/strings.xml` — "Slute" is a misspelling of the Frisian verb "Slute" → correct form is "Slúte".
    - Current: `Slute`
    - Source: `Dismiss`
    - Suggest: `Slúte`
    - Frisian for 'close' is 'slúte' (with ú); the same string elsewhere in the tree uses 'Slúte'.
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Missing preposition "fan" before the placeholder, unlike the parallel enable/remove/uninstall strings.
    - Current: `Utskeakeljen %1$s mislearre`
    - Source: `Failed to disable %1$s`
    - Suggest: `Utskeakeljen fan %1$s mislearre`
    - The corresponding strings use 'Ynskeakeljen fan %1$s mislearre', 'Fuortsmiten fan %1$s mislearre'; omitting 'fan' is ungrammatical.
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Compound noun misspelled: "útwreidingûntwikkeler" is missing the linking -s- used in all sibling strings ("útwreidingsûntwikkeler").
    - Current: `útwreidingûntwikkeler`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `útwreidingsûntwikkeler`
    - All other data-collection long descriptions in the same file render "extension developer" as "útwreidingsûntwikkeler"; this one drops the linking s, which is a spelling/consistency error.
- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "browsing history" is rendered as "browserskiednis" here but as "sneupskiednis" in the parallel _for_update string.
    - Current: `Resinte browserskiednis, cookies en relatearre gegevens wiskje`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Resinte sneupskiednis, cookies en relatearre gegevens wiskje`
    - The same source sentence ("Clear recent browsing history, cookies, and related data") is translated with two different terms on the same surface; fy-NL uses "sneup-" for browsing (cf. sneupaktiviteit for "browsing activity").
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — The update variant uses an imperative form and different wording/terminology than the non-update variant of the same permission description.
    - Current: `Wreidzje jo ûntwikkelark út foar tagong ta gegevens yn jo iepen ljepblêden.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen.`
    - mozac_feature_addons_permissions_devtools_description translates the identical source as ‘Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen’; the update string must match in style (infinitive) and term (ûntwikkelersark vs ûntwikkelark) since these appear on the same surface.
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Misspelling of ‘útwreidingsgebrûk’ and missing diacritic on the initial U.
    - Current: `Utwreidigsgebrûk kontrolearje en tema’s beheare`
    - Source: `Monitor extension usage and manage themes`
    - Suggest: `Utwreidingsgebrûk kontrolearje en tema’s beheare`
    - ‘Utwreidigsgebrûk’ drops the ‘n’ from ‘útwreiding’ (extension); the compound should be ‘útwreidingsgebrûk’.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Misspelling of ‘útwreidingsgebrûk’.
    - Current: `Utwreidigsgebrûk kontrolearje en tema’s beheare.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `Utwreidingsgebrûk kontrolearje en tema’s beheare.`
    - ‘Utwreidigs-’ drops the ‘n’ from ‘útwreiding’ (extension); the compound should be ‘útwreidingsgebrûk’.
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Compound ‘útwreidingûntwikkeler’ is missing the linking -s- used elsewhere (‘útwreidingsûntwikkeler’).
    - Current: `útwreidingûntwikkeler`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `útwreidingsûntwikkeler`
    - The parallel string mozac_feature_addons_permissions_data_collection_websiteContent_long_description uses ‘útwreidingsûntwikkeler’ for the same source term ‘extension developer’.
- `mozac_feature_addons_permissions_dialog_heading_required_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — ‘permissions’ is rendered as ‘machtigingen’ here but as ‘tastimmingen’ in the parallel optional-permissions heading.
    - Current: `Fereaske machtigingen:`
    - Source: `Required permissions:`
    - Suggest: `Fereaske tastimmingen:`
    - mozac_feature_addons_permissions_dialog_heading_optional_permissions translates ‘New permissions:’ as ‘Nije tastimmingen:’; both headings appear in the same add-on permissions dialog and must use one term.
- `mozac_feature_addons_permissions_user_scripts_extra_warning` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Doubled apostrophe in "dy’'t" (typographic apostrophe followed by a straight one).
    - Current: `dy’'t`
    - Source: `Unverified scripts can pose security and privacy risks. Only run scripts from extensions or sources you trust.`
    - Suggest: `dy’t`
    - The relative pronoun should be "dy’t"; the extra straight apostrophe is a stray character and breaks the locale's typographic apostrophe convention.
- `mozac_feature_addons_permissions_privacy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "modify" rendered as "oanpasse" here but as "bewurkje" in the identical non-update string.
    - Current: `Privacyynstellingen lêze en oanpasse.`
    - Source: `Read and modify privacy settings.`
    - Suggest: `Privacyynstellingen lêze en bewurkje.`
    - mozac_feature_addons_permissions_privacy_description translates the same source sentence as "Privacyynstellingen lêze en bewurkje"; the paired update string must match.
- `mozac_feature_contextmenu_snackbar_link_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fy-rNL/strings.xml` — "Link" is rendered as "Koppeling" (Dutch) here while the rest of the file consistently uses the Frisian "Keppeling".
    - Current: `Koppeling nei klamboerd kopiearre`
    - Source: `Link copied to clipboard`
    - Suggest: `Keppeling nei klamboerd kopiearre`
    - Sibling strings (mozac_feature_contextmenu_share_link, mozac_feature_contextmenu_snackbar_link_text_copied) use "Keppeling"; "Koppeling" is the Dutch spelling and is inconsistent on the same surface.
- `mozac_feature_downloads_file_failure_no_connection` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — The Frisian says the file "is not downloading" instead of the past "wasn’t downloaded".
    - Current: `%1$s is net downloaden.`
    - Source: `%1$s wasn’t downloaded.`
    - Suggest: `%1$s is net download.`
    - Source is past tense/perfect: the download failed. "is net downloaden" reads as an infinitive construction, not the completed-action past participle.
- `mozac_feature_downloads_open_existing_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — Adjective inflection missing before neuter noun 'bestân'.
    - Current: `Besteande bestân iepenje`
    - Source: `Open existing file`
    - Suggest: `Besteand bestân iepenje`
    - 'bestân' is a neuter noun; in an indefinite neuter noun phrase the attributive adjective takes the uninflected form ('besteand bestân').
- `mozac_feature_downloads_open_not_supported1` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — Superfluous preposition 'mei' inserted, changing 'to open %1$s files' into 'to open with %1$s files'.
    - Current: `Gjin app fûn om %1$s-bestannen mei te iepenjen`
    - Source: `No app found to open %1$s files`
    - Suggest: `Gjin app fûn om %1$s-bestannen te iepenjen`
    - The source says no app was found to open the files; 'mei' adds an instrumental sense that is not in the source and is ungrammatical here.
- `mozac_feature_media_notification_action_play` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fy-rNL/strings.xml` — Missing accent on the initial 'Ô' in 'Ofspylje'.
    - Current: `Ofspylje`
    - Source: `Play`
    - Suggest: `Ôfspylje`
    - Frisian spelling is 'ôfspylje'; capitalised it is 'Ôfspylje', not 'Ofspylje'.
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Plural "files" rendered as singular "Bestân".
    - Current: `Bestân oplade?`
    - Source: `Upload files?`
    - Suggest: `Bestannen oplade?`
    - Source is "Upload files?" (plural); the Frisian says "Upload file?" (singular).
- `mozac_feature_prompts_expand_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre kaarten te útklappe`
    - Source: `Expand saved cards`
    - Suggest: `Bewarre kaarten útklappe`
    - The parallel strings (expand saved addresses, collapse saved passwords) use the bare infinitive "Bewarre adressen útklappe" / "Bewarre wachtwurden ynklappe"; the added "te" is ungrammatical here and inconsistent.
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre wachtwurden te útklappe`
    - Source: `Expand saved passwords`
    - Suggest: `Bewarre wachtwurden útklappe`
    - Parallel string mozac_feature_prompts_collapse_logins_content_description_2 uses "Bewarre wachtwurden ynklappe" without "te"; the "te" is ungrammatical and inconsistent.
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fy-rNL/strings.xml` — "Font size increase" is rendered as "Lettertype fergrutsje" (enlarge font/typeface) instead of font size, inconsistent with the decrease counterpart.
    - Current: `Lettertype fergrutsje`
    - Source: `Font size increase`
    - Suggest: `Lettergrutte fergrutsje`
    - Source is "Font size increase"; the parallel string mozac_feature_readerview_font_size_decrease_desc correctly uses "Lettergrutte ferlytsje". "Lettertype" means typeface, not font size.
- `mozac_feature_sitepermissions_notification_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — "notifications" is rendered as "meldingen" here but as "notifikaasjes" in the sibling notification-permission string on the same surface.
    - Current: `%1$s tastean om meldingen te ferstjoeren?`
    - Source: `Allow %1$s to send notifications?`
    - Suggest: `%1$s tastean om notifikaasjes te ferstjoeren?`
    - mozac_feature_sitepermissions_notification_permission_rationale_dialog_message translates "notifications" as "notifikaasjes"; the same term in the same notification-permission dialog flow should be consistent.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_settings_label` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — Unnecessary capitalisation of "Ynstellingen" mid-sentence in the button label.
    - Current: `Nei Ynstellingen`
    - Source: `Go to settings`
    - Suggest: `Nei ynstellingen`
    - Source is sentence case ("Go to settings"); Frisian does not capitalise common nouns.
- `mozac_lib_crash_activity_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Ûngelokrapporten".
    - Current: `Ungelokrapporten`
    - Source: `Crash Reports`
    - Suggest: `Ûngelokrapporten`
    - Frisian spells the word with a circumflex: ûngelok. The initial capital must keep the diacritic (Û).
- `about_crashes` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Crashes" (browser crashes, about:crashes) is rendered as "Ungelokken" (accidents), the wrong term, and it is also missing its diacritic.
    - Current: `Ungelokken`
    - Source: `Crashes`
    - Suggest: `Ûnderbrekkingen`
    - The developer comment says this links to a list of past crashes (about:crashes). "Ungelokken" means "accidents"; also the initial U should be Û ("Ûngelokken") in Frisian.
- `addon_ga_message_button_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial U of "Utwreidingen".
    - Current: `Utwreidingen ferkenne`
    - Source: `Explore extensions`
    - Suggest: `Ûtwreidingen ferkenne`
    - Elsewhere the same word is spelled "útwreidingen" with a diacritic; capitalised it must be "Ú/Û" rather than plain "U".
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic: "Ofdieling" should be "Ôfdieling".
    - Current: `Ofdieling`
    - Source: `Department`
    - Suggest: `Ôfdieling`
    - In Frisian the word is spelled "ôfdieling"; capitalised it keeps the circumflex: "Ôfdieling". The current form drops the required diacritic.
- `addresses_eircode` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Eircode" is a proper Irish postal-code system name and should not be translated as "Eirkoade".
    - Current: `Eirkoade`
    - Source: `Eircode`
    - Suggest: `Eircode`
    - The developer comment states this is the Eircode field, a specific Irish postal code system name; it is a proper name and stays untranslated.
- `addresses_street_address` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Street Address" is translated as just "Adres", losing the street distinction and colliding with the generic address label.
    - Current: `Adres`
    - Source: `Street Address`
    - Suggest: `Strjitte en hûsnûmer`
    - The source specifically labels the street address line; rendering it as the generic "Adres" makes it indistinguishable from other address labels in the same form.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Plural "specific features" rendered as singular "spesifike funksje".
    - Current: `Deblokkearje hjirûnder spesifike funksje.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Deblokkearje hjirûnder spesifike funksjes.`
    - The source says "Unblock specific features below" (plural); the Frisian noun is singular, a grammatical/number error.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "extensions that use AI provided by %1$s" is rendered as "utwreidingen dy't AI troch %1$s brûke", which misconstrues the relation.
    - Current: `útwreidingen dy’t AI troch %1$s brûke`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `útwreidingen dy’t troch %1$s levere AI brûke`
    - The source means extensions using AI that Firefox provides; the current word order reads as "extensions that use AI by means of Firefox", changing the meaning.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The "never translate" summary omits the negation and duplicates the "offer to translate" text.
    - Current: `%1$s sil oanbiede om websites yn dizze taal oer te setten.`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `%1$s sil nea oanbiede om websites yn dizze taal oer te setten.`
    - Source reads "%1$s will never offer to translate sites in this language." The translation drops "never", reversing the meaning and making it identical to the offer-to-translate option.
- `bookmark_menu_open_all_in_private_tabs_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "priveeljepblêden" as "proveeljepblêden".
    - Current: `Alles yn proveeljepblêden iepenje`
    - Source: `Open all in private tabs`
    - Suggest: `Alles yn priveeljepblêden iepenje`
    - "private tabs" is rendered elsewhere as "priveeljepblêd"; "proveeljepblêden" is a typo.
- `bookmark_save_in_label` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Save in" translated as "Besparje yn" (to economize/save money) instead of the storage sense used elsewhere.
    - Current: `Besparje yn`
    - Source: `Save in`
    - Suggest: `Bewarje yn`
    - The source refers to saving a bookmark in a folder; the related snackbar uses "Bewarre yn". "Besparje" means to economize, not to store.
- `bookmark_import_bookmarks_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_import_menu_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_invalid_url_error` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Unjildige".
    - Current: `Unjildige URL`
    - Source: `Invalid URL`
    - Suggest: `Ûnjildige URL`
    - The Frisian word is "ûnjildich"; capitalized it is "Ûnjildige".
- `browser_feature_desktop_site_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ut"; Frisian for "Off" is "Ût".
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Ût`
    - The Frisian word for "off" is spelled "út/Ût" with a circumflex/accent; the toggle label drops the diacritic.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Custom tab menu sheet" rendered as "Menublêd Ljepblêd oanpasse", turning the noun phrase into an imperative "customize tab".
    - Current: `Menublêd Ljepblêd oanpasse slute`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublêd fan oanpast ljepblêd slute`
    - The source describes closing the menu sheet of a custom tab; the translation reads as "Customize tab menu sheet close", changing the meaning.
- `close_tab_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Singular "Close tab %s" is rendered as plural "Ljepblêden" (tabs).
    - Current: `Ljepblêden %s slute`
    - Source: `Close tab %s`
    - Suggest: `Ljepblêd %s slute`
    - The source refers to closing one tab whose title is %s; the Frisian uses the plural form.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Singular "this permission" is rendered as "alle tastimmingen" (all permissions), duplicating the other, plural dialog.
    - Current: `Binne jo wis dat jo alle tastimmingen foar dizze website wiskje wolle?`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `Binne jo wis dat jo dizze tastimming foar dizze website wiskje wolle?`
    - The source asks about clearing one specific permission for a site; the developer comment says it sets a default value for a single permission. The translation says all permissions.
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Default collection name is pluralized: "Kolleksjes %d" instead of singular "Kolleksje %d".
    - Current: `Kolleksjes %d`
    - Source: `Collection %d`
    - Suggest: `Kolleksje %d`
    - Source "Collection %d" is the name of one new collection, not a plural.
- `connection_security_panel_verified_by` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — A colon was added that is not in the source, unlike the parallel string "Utjûn oan %s".
    - Current: `Ferifiearre troch: %s`
    - Source: `Verified by %s`
    - Suggest: `Ferifiearre troch %s`
    - Source "Verified by %s" has no colon; the sibling string "Issued to %s" is translated without one.
- `create_collection_deselect_all` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Alle deselektearje" is inconsistent with the parallel "Alles selektearje".
    - Current: `Alle deselektearje`
    - Source: `Deselect all`
    - Suggest: `Alles deselektearje`
    - Source pair "Select all"/"Deselect all" should use the same pronoun form; "Alles selektearje" is used for the counterpart.
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Word order is ungrammatical: the imperative with object should be "Untskoattelje jo apparaat" reversed to "Ûntskoattelje jo apparaat" — actual defect is the missing circumflex/accent on Û and wrong construction.
    - Current: `Untskoattelje jo apparaat`
    - Source: `Unlock your device`
    - Suggest: `Ûntskoattelje jo apparaat`
    - Frisian "ûntskoattelje" is written with û; the initial capital must be Û. The same error appears in the neighbouring credit_cards_biometric_prompt_* strings.
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om jo bewarre kaarten te besjen`
    - Source: `Unlock to view your saved cards`
    - Suggest: `Ûntskoattelje om jo bewarre kaarten te besjen`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje", not "Untskoattelje".
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om bewarre betellingsmetoaden te brûken`
    - Source: `Unlock to use saved payment methods`
    - Suggest: `Ûntskoattelje om bewarre betellingsmetoaden te brûken`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje".
- `credit_cards_warning_dialog_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "payment methods" is rendered "betelmetoaden" here but "betellingsmetoaden" in the neighbouring credit card strings.
    - Current: `betelmetoaden`
    - Source: `Secure your saved payment methods`
    - Suggest: `betellingsmetoaden`
    - Inconsistent terminology for the same source term on the same surface (see credit_cards_warning_dialog_message_3 and credit_cards_biometric_prompt_unlock_message_2).
- `customize_addon_collection_user_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Adjective/noun agreement error: "Eigener kolleksje" instead of "Eigener fan de kolleksje"/"Kolleksje-eigener".
    - Current: `Eigener kolleksje (brûkers-ID)`
    - Source: `Collection owner (User ID)`
    - Suggest: `Kolleksje-eigener (brûkers-ID)`
    - The source is "Collection owner" (owner of the collection); "Eigener kolleksje" is two juxtaposed nouns without a valid Frisian compound or genitive, giving ungrammatical text.
- `debug_drawer_region_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Tools" rendered as "helpmiddelen" here while the same debug-drawer surface uses "ark" elsewhere (CFR-ark, Add-ons-ark, Ark foar automatysk ynfoljen).
    - Current: `Regiohelpmiddelen`
    - Source: `Region Tools`
    - Suggest: `Regio-ark`
    - Terminology inconsistency for "Tools" on the same Debug Drawer surface, where "ark" is the established rendering.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Navigate back" translated as "Tebek blêdzje" (browse back) rather than navigating back within the drawer.
    - Current: `Tebek blêdzje`
    - Source: `Navigate back`
    - Suggest: `Tebek navigearje`
    - The developer comment says the control navigates back within the debug drawer, not page browsing; "blêdzje" implies web page navigation.
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Út" (Frisian for "Off").
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Út`
    - The Frisian word for "Off" is "Út" with an acute accent on the capital U; "Ut" is a spelling error.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "If you delete all languages" rendered as "As jo dizze talen fuortsmite" (if you delete these languages).
    - Current: `As jo dizze talen fuortsmite`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `As jo alle talen fuortsmite`
    - Source says "all languages", not "these languages"; the demonstrative changes the meaning.
- _…and 107 more._

### ✅ Fixed since the last run (9)

- `download_content_type_filter_video` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `download_content_type_filter_video` uses a straight apostrophe
    - Current: `Fideo's`
    - Source: `Videos`
    - The tree uses ’ 101 times against 8 straight.
- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Straight apostrophe used instead of the typographic apostrophe required by the locale convention.
    - Current: `dy't brûkt wurde kinne`
    - Source: `Stops uniquely identifiable data from being collected about your device that can be used for tracking purposes.`
    - Suggest: `dy’t brûkt wurde kinne`
    - fy-NL convention is the typographic apostrophe (’), as used in neighbouring strings such as etp_cookies_description.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `nova_onboarding_marketing_body_2` uses a straight apostrophe
    - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke. Dizze gegevens wurde nea ferkocht.`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - The tree uses ’ 101 times against 8 straight.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Straight apostrophe used in "Mozilla's" instead of the locale's typographic apostrophe.
    - Current: `Mozilla's`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s`
    - fy-NL convention is the typographic apostrophe (’), used elsewhere in the same string ("hoe’t").
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Straight apostrophe used in "Mozilla's" instead of the locale's typographic apostrophe.
    - Current: `Mozilla's`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s`
    - fy-NL convention is the typographic apostrophe (’), used elsewhere in the same string ("hoe’t").
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `preferences_marketing_data_description_4` uses a straight apostrophe
    - Current: `Diel mei Mozilla's marketingtechnologypartners hoe’t jo Firefox ûntdutsen hawwe en dat jo it brûke.`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - The tree uses ’ 101 times against 8 straight.
- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `search_suggestions_onboarding_text` has placeholders %1$s where the source has %s
    - Current: `%1$s sil alles wat jo yn de adresbalke yntype mei jo standert sykmasine diele.`
    - Source: `%s will share everything you type in the address bar with your default search engine.`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `tab_tray_inactive_auto_close_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `tab_tray_inactive_auto_close_body_2` uses a straight apostrophe
    - Current: `%1$s kin ljepblêden dy't jo de ôfrûne moanne net besjoen hawwe slute.`
    - Source: `%1$s can close tabs you haven’t viewed over the past month.`
    - The tree uses ’ 101 times against 8 straight.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — `uninstall_survey_option_4_v2` uses a straight apostrophe
    - Current: `Fideo's, downloads of media wurken net`
    - Source: `Videos, downloads, or media didn’t work`
    - The tree uses ’ 101 times against 8 straight.

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
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 8 |

### Completeness

**3 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — 3

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 17 | **curly-single** |
| apostrophe | `typographic` 101, `straight` 8 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 7 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (167)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 60 |
| 3 | Degraded language (grammar, spelling, terminology) | 103 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "temporary outage" is rendered as "stroomûnderbrekking" (power cut), changing the meaning.
    - Current: `in tydlike stroomûnderbrekking`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `in tydlike steuring`
    - The source refers to a temporary service outage of the server, not an electrical power interruption.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "potentially harmful site" is rendered as "fertochte side" (suspicious site), duplicating the malware string instead of translating "potentially harmful".
    - Current: `is rapportearre as in fertochte side`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `is rapportearre as in mooglik skealike website`
    - The source says the site has been reported as a potentially harmful site; the target says "suspicious site", the same wording used for the malware/attack-site string, losing the source meaning. The corresponding title correctly uses "skealike website".
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Plural "files" rendered as singular "Bestân".
    - Current: `Bestân oplade?`
    - Source: `Upload files?`
    - Suggest: `Bestannen oplade?`
    - Source is "Upload files?" (plural); the Frisian says "Upload file?" (singular).
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fy-rNL/strings.xml` — "Font size increase" is rendered as "Lettertype fergrutsje" (enlarge font/typeface) instead of font size, inconsistent with the decrease counterpart.
    - Current: `Lettertype fergrutsje`
    - Source: `Font size increase`
    - Suggest: `Lettergrutte fergrutsje`
    - Source is "Font size increase"; the parallel string mozac_feature_readerview_font_size_decrease_desc correctly uses "Lettergrutte ferlytsje". "Lettertype" means typeface, not font size.
- `about_crashes` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Crashes" (browser crashes, about:crashes) is rendered as "Ungelokken" (accidents), the wrong term, and it is also missing its diacritic.
    - Current: `Ungelokken`
    - Source: `Crashes`
    - Suggest: `Ûnderbrekkingen`
    - The developer comment says this links to a list of past crashes (about:crashes). "Ungelokken" means "accidents"; also the initial U should be Û ("Ûngelokken") in Frisian.
- `addresses_eircode` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Eircode" is a proper Irish postal-code system name and should not be translated as "Eirkoade".
    - Current: `Eirkoade`
    - Source: `Eircode`
    - Suggest: `Eircode`
    - The developer comment states this is the Eircode field, a specific Irish postal code system name; it is a proper name and stays untranslated.
- `addresses_street_address` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Street Address" is translated as just "Adres", losing the street distinction and colliding with the generic address label.
    - Current: `Adres`
    - Source: `Street Address`
    - Suggest: `Strjitte en hûsnûmer`
    - The source specifically labels the street address line; rendering it as the generic "Adres" makes it indistinguishable from other address labels in the same form.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "extensions that use AI provided by %1$s" is rendered as "utwreidingen dy't AI troch %1$s brûke", which misconstrues the relation.
    - Current: `útwreidingen dy’t AI troch %1$s brûke`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `útwreidingen dy’t troch %1$s levere AI brûke`
    - The source means extensions using AI that Firefox provides; the current word order reads as "extensions that use AI by means of Firefox", changing the meaning.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The "never translate" summary omits the negation and duplicates the "offer to translate" text.
    - Current: `%1$s sil oanbiede om websites yn dizze taal oer te setten.`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `%1$s sil nea oanbiede om websites yn dizze taal oer te setten.`
    - Source reads "%1$s will never offer to translate sites in this language." The translation drops "never", reversing the meaning and making it identical to the offer-to-translate option.
- `bookmark_save_in_label` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Save in" translated as "Besparje yn" (to economize/save money) instead of the storage sense used elsewhere.
    - Current: `Besparje yn`
    - Source: `Save in`
    - Suggest: `Bewarje yn`
    - The source refers to saving a bookmark in a folder; the related snackbar uses "Bewarre yn". "Besparje" means to economize, not to store.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Custom tab menu sheet" rendered as "Menublêd Ljepblêd oanpasse", turning the noun phrase into an imperative "customize tab".
    - Current: `Menublêd Ljepblêd oanpasse slute`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublêd fan oanpast ljepblêd slute`
    - The source describes closing the menu sheet of a custom tab; the translation reads as "Customize tab menu sheet close", changing the meaning.
- `close_tab_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Singular "Close tab %s" is rendered as plural "Ljepblêden" (tabs).
    - Current: `Ljepblêden %s slute`
    - Source: `Close tab %s`
    - Suggest: `Ljepblêd %s slute`
    - The source refers to closing one tab whose title is %s; the Frisian uses the plural form.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Singular "this permission" is rendered as "alle tastimmingen" (all permissions), duplicating the other, plural dialog.
    - Current: `Binne jo wis dat jo alle tastimmingen foar dizze website wiskje wolle?`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `Binne jo wis dat jo dizze tastimming foar dizze website wiskje wolle?`
    - The source asks about clearing one specific permission for a site; the developer comment says it sets a default value for a single permission. The translation says all permissions.
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Default collection name is pluralized: "Kolleksjes %d" instead of singular "Kolleksje %d".
    - Current: `Kolleksjes %d`
    - Source: `Collection %d`
    - Suggest: `Kolleksje %d`
    - Source "Collection %d" is the name of one new collection, not a plural.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Navigate back" translated as "Tebek blêdzje" (browse back) rather than navigating back within the drawer.
    - Current: `Tebek blêdzje`
    - Source: `Navigate back`
    - Suggest: `Tebek navigearje`
    - The developer comment says the control navigates back within the debug drawer, not page browsing; "blêdzje" implies web page navigation.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "If you delete all languages" rendered as "As jo dizze talen fuortsmite" (if you delete these languages).
    - Current: `As jo dizze talen fuortsmite`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `As jo alle talen fuortsmite`
    - Source says "all languages", not "these languages"; the demonstrative changes the meaning.
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The back-button variant was translated as if it were the gesture variant ("press back" rendered as "press the back gesture").
    - Current: `druk it gebear werom`
    - Source: `Drag from top & press back to exit`
    - Suggest: `druk op werom`
    - Source says "press back" (hardware/software back button); the gesture wording belongs to exit_fullscreen_with_gesture_short. As translated both strings say essentially the same thing.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The brand name "Firefox Suggest" has been altered with a Frisian plural suffix.
    - Current: `Firefox Suggestjes`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must remain unchanged; adding "-jes" turns it into a non-brand plural word.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "shortcuts" (fluchkeppelingen) rendered as "fluchtoetsen" (keyboard shortcuts).
    - Current: `Alle fluchtoetsen toane`
    - Source: `Show all shortcuts`
    - Suggest: `Alle fluchkeppelingen toane`
    - The source refers to home screen shortcuts, translated elsewhere in this batch as "Fluchkeppeling"; "fluchtoetsen" means keyboard shortcut keys.
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Neutral" is rendered as "Gemiddeld" (average), not the neutral midpoint label.
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
    - Source "Neutral" is the middle likert option; "Gemiddeld" means "average", a different concept.
- `microsurvey_homepage_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The translation adds "ûnderfining fan" (experience of), which is not in the source.
    - Current: `mei jo ûnderfining fan de Firefox-Startside?`
    - Source: `How satisfied are you with your Firefox homepage?`
    - Suggest: `mei jo Firefox-startside?`
    - Source is "How satisfied are you with your Firefox homepage?" with no mention of experience; also "Startside" is capitalized mid-compound without reason.
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The translation drops "search", making the prompt about Firefox in general instead of search in Firefox.
    - Current: `Help Firefox te ferbetterjen. It duorret mar in minút`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `Help it sykjen yn Firefox better te meitsjen. It duorret mar in minút`
    - Source is "Help make search in Firefox better"; the sibling strings for printing and sync keep the feature name, but here it is omitted.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "marketing partners" is rendered as "marketingtechnologypartners", adding a word not in the source.
    - Current: `Mozilla’s marketingtechnologypartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "technology" is not present and the compound is also an untranslated English string.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "marketing partners" is rendered as "marketingtechnologypartners", adding a word not in the source.
    - Current: `Mozilla's marketingtechnologypartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "technology" is not in the source. The straight apostrophe also deviates from the typographic-apostrophe convention.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Please consider allowing" is rendered as "think about permission", losing the request to grant permission.
    - Current: `Tink asjebleaft oer tastimming om Firefox te helpen winnen.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Oerwaach asjebleaft om tastimming te jaan om Firefox winne te litten.`
    - The developer comment explains that "allowing" refers to granting permission via the "Allow and Continue" button; the current wording only says to think about permission and drops the act of allowing.
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Translation states companies do spy on your clicks instead of blocking them from spying.
    - Current: `blokkearje automatysk bedriuwen dy’t jo klikken bespionearje`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `foarkomme automatysk dat bedriuwen jo klikken bespionearje`
    - The source is "automatically block companies from spying on your clicks"; the relative clause presupposes the spying instead of preventing it.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "marketing partners" is rendered as "marketingtechnologypartners", adding a term not in the source.
    - Current: `Mozilla's marketingtechnologypartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "marketingtechnologypartners" invents "technology" and is also an untranslated English compound element.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "marketing partners" is rendered as "marketingtechnologypartners", adding a term not in the source.
    - Current: `Mozilla's marketingtechnologypartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "marketingtechnologypartners" invents "technology" and mixes untranslated English.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The translation drops "helps", turning "One tap helps stop…" into "With one tap you prevent…" and losing the subject.
    - Current: `Mei ien tik foarkomme dat bedriuwen jo tikken bespionearje.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Ien tik helpt foar te kommen dat bedriuwen jo klikken bespionearje.`
    - The source is "One tap helps stop companies spying on your clicks"; the Frisian sentence lacks a subject and omits "helps", and "clicks" is rendered as "tikken" (taps), duplicating "tik".
- `phone_feature_blocked_intro` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "To allow it:" is rendered as the bare verb "Tastean:" losing the introductory meaning.
    - Current: `Tastean:`
    - Source: `To allow it:`
    - Suggest: `Om dit ta te stean:`
    - The source is a heading introducing the steps to allow the permission ("To allow it:"), not a command "Allow:".
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Order of "share & sell" is reversed in the translation.
    - Current: `gegevens net te ferkeapjen en te dielen`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `gegevens net te dielen en te ferkeapjen`
    - Source says "not to share & sell data" (share first, then sell); the target swaps the verbs.
- `preference_gestures_swipe_toolbar_switch_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "address bar" translated as "arkbalke" (toolbar) instead of "adresbalke".
    - Current: `De arkbalke op side feie om fan ljepblêd te wikseljen`
    - Source: `Swipe address bar sideways to switch tabs`
    - Suggest: `De adresbalke op side feie om fan ljepblêd te wikseljen`
    - The source and developer comment refer to the address bar, not the toolbar; the neighbouring string uses "wurkbalke" for toolbar, so this is also inconsistent.
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Firefox Suggest" brand name is translated as "Firefox Suggestjes".
    - Current: `Firefox Suggestjes`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product feature brand name that must remain untranslated; the neighbouring string uses yet another form.
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Firefox Suggest" brand name is translated and inconsistently rendered.
    - Current: `Firefox Suggestes`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and should not be translated; it is also rendered differently ("Firefox Suggestjes") in preference_search_address_bar_fx_suggest.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Sort passwords menu" (a menu for sorting passwords) is rendered as an imperative "sort the password menu".
    - Current: `Wachtwurdmenu sortearje`
    - Source: `Sort passwords menu`
    - Suggest: `Menu Wachtwurden sortearje`
    - The source is a noun phrase naming the menu used to sort passwords, not an instruction to sort a 'password menu'.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Search %s" (search using engine %s) is translated as "%s trochsykje", meaning "search through %s".
    - Current: `%s trochsykje`
    - Source: `Search %s`
    - Suggest: `Sykje mei %s`
    - %s is the suggested search engine name; the source means to search with that engine, not to search inside it.
- `search_suggestions_onboarding_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "private sessions" is translated as "priveefinsters" (private windows).
    - Current: `priveefinsters`
    - Source: `Allow search suggestions in private sessions?`
    - Suggest: `priveesesjes`
    - The source says "private sessions", not private windows.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "essentials" is left untranslated in the compound "%1$s-essentials".
    - Current: `%1$s-essentials`
    - Source: `%1$s essentials`
    - Suggest: `%1$s-essinsjes`
    - "essentials" is an ordinary English noun, not a brand name, and should be rendered in Frisian (e.g. "basisynstellingen" / "essinsjes").
- `sports_widget_team_followed_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Following:" (the user follows the team) is rendered as "Folgjend:" which means "next/following" in the ordinal sense.
    - Current: `Folgjend:`
    - Source: `Following:  %s`
    - Suggest: `Folget:`
    - Source means the user is now following the given team; "Folgjend" is the adjective "next", not the state of following.
- `tab_manager_close_all_tabs_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Dropped "open" from "all open tabs".
    - Current: `Dit slút alle ljepblêden.`
    - Source: `This will close all open tabs.`
    - Suggest: `Dit slút alle iepen ljepblêden.`
    - Source says "This will close all open tabs."; the translation omits "open".
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Dismiss" (dismiss the banner) is translated as "Slute" (Close), the same word used elsewhere for closing tabs.
    - Current: `Slute`
    - Source: `Dismiss`
    - Suggest: `Ferbergje`
    - The source is "Dismiss", meaning dismiss/hide the banner; "Slute" means "Close" and duplicates the translation of the separate "Close" strings.
- `tab_tray_close_tabs_banner_positive_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "View options" is rendered as "Byldopsjes" (display/image options), not "view the options".
    - Current: `Byldopsjes`
    - Source: `View options`
    - Suggest: `Opsjes besjen`
    - Per the developer comment the button opens Settings for auto-close tabs; "View" is a verb here, not "display". "Byldopsjes" means "image/display options".
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Word order makes "Syngronisearre" modify the wrong element compared to "Synced Tabs Open".
    - Current: `Syngronisearre iepen ljepblêden: %1$s.`
    - Source: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Iepen syngronisearre ljepblêden: %1$s.`
    - The source means open synced tabs; the sibling strings use "Iepen normale ljepblêden" and "Iepen priveeljepblêden", so this one is inconsistent and reads as "synchronised open tabs".
- `translation_in_progress_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Translating…" (ongoing action) rendered as the infinitive "Oersette…".
    - Current: `Oersette…`
    - Source: `Translating…`
    - Suggest: `Dwaande mei oersetten…`
    - The snackbar reports a translation in progress, not a command/infinitive; the same word is also used for the Translate shortcut label, losing the progress meaning.
- `translation_option_bottom_sheet_switch_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Overrides offers to translate" is rendered as "Ignores translation offers" instead of "overrides".
    - Current: `Negearret oersetoanbiedingen`
    - Source: `Overrides offers to translate`
    - Suggest: `Oerskriuwt oersetoanbiedingen`
    - The source says the setting overrides (takes precedence over) offers to translate; "negearret" means "ignores". The parallel string translation_option_bottom_sheet_switch_never_translate_site_description correctly uses "Oerskriuwt" for "Overrides".
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Translating" (in-progress state) is translated as the infinitive "Oersette", identical to the "Translate" button, losing the progress meaning.
    - Current: `Oersette`
    - Source: `Translating`
    - Suggest: `Oersette…`
    - The developer comment states this is the inactive button text indicating a translation is currently in progress; rendering it identically to translations_bottom_sheet_positive_button ("Translate" = "Oersette") removes the distinction between the two states.
- `uninstall_survey_error_failed` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "system uninstall prompt" mistranslated as "prompt for uninstalling the system".
    - Current: `It iepenjen fan de prompt foar it de-ynstallearjen fan it systeem is mislearre`
    - Source: `Failed to open the system uninstall prompt, please use the system uninstall action directly.`
    - Suggest: `It iepenjen fan de systeemprompt foar de-ynstallaasje is mislearre`
    - The source means the prompt provided by the system to uninstall the app, not a prompt to uninstall the system.
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Disjunction "or" translated as conjunction "en".
    - Current: `De browser is stadich en ûnbetrouber`
    - Source: `It’s slow or unreliable`
    - Suggest: `De browser is stadich of ûnbetrouber`
    - Source is "It’s slow or unreliable" — an either/or option, not both.
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Plural "these reports" rendered as singular "dit rapport".
    - Current: `wurdt dit rapport negearre`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `wurde dizze rapporten negearre`
    - Source says "Closing this notification will ignore these reports" (plural), matching the multiple-crash-reports context of this string.
- `webcompat_reporter_label_mandatory_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — “to help us investigate the issue” rendered as “so that we can investigate it”, dropping the help sense; inconsistent with the optional variant.
    - Current: `Beskriuw it probleem yn detail, sadat wy it ûndersykje kinne`
    - Source: `Describe the problem in detail to help us investigate the issue`
    - Suggest: `Beskriuw it probleem yn detail om ús te helpen it te ûndersykjen`
    - The identical source phrase is translated as “om ús te helpen it te ûndersykjen” in webcompat_reporter_label_optional_description; the mandatory variant changes the meaning and breaks consistency on the same screen.
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The order of the two conditions is swapped relative to the source.
    - Current: `Browser wurdt net stipe of blokkearre`
    - Source: `Browser is blocked or unsupported`
    - Suggest: `Browser wurdt blokkearre of net stipe`
    - Source is “Browser is blocked or unsupported”; the translation reverses the order and reads as “not supported or blocked”, where “net” no longer applies to “blokkearre”.
- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Dismiss" is translated as "Fuortsmite" (delete/throw away) instead of dismissing/closing the overlay.
    - Current: `Fuortsmite`
    - Source: `Dismiss`
    - Suggest: `Slute`
    - Per the developer comment the action dismisses the overlay and returns to the browser; ‘Fuortsmite’ means to discard/delete, which suggests data removal.
- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Dismiss" (close/hide the message) is translated as "Fuortsmite" (delete).
    - Current: `Fuortsmite`
    - Source: `Dismiss`
    - Suggest: `Slute`
    - The developer comment says the button dismisses a message; "Fuortsmite" means delete/remove, which conveys a destructive action not present in the source.
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Back-button instruction wrongly says "press the back gesture" instead of pressing the back button, duplicating the gesture string.
    - Current: `druk it gebear werom`
    - Source: `Drag from top & press back to exit`
    - Suggest: `druk op de weromknop`
    - Source is "press back to exit" (hardware/back button), not a gesture; the gesture wording belongs to exit_fullscreen_with_gesture_short.
- `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Singular "Tab's browsing history" rendered as plural "of the tabs".
    - Current: `Jo sneupskiednis fan de ljepblêden is wiske.`
    - Source: `Tab’s browsing history has been erased.`
    - Suggest: `De sneupskiednis fan it ljepblêd is wiske.`
    - Source refers to a single tab's browsing history; the translation says the history of the tabs (plural) and adds "Jo" (your).
- `firstrun_shortcut_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "shortcuts" translated as "keppelingen" (links) instead of "fluchkeppelingen" (shortcuts).
    - Current: `Foegje keppelingen ta oan jo startskerm`
    - Source: `Add shortcuts to your home screen`
    - Suggest: `Foegje fluchkeppelingen ta oan jo startskerm`
    - Source says "Add shortcuts to your home screen"; elsewhere (menu_add_to_shortcuts) "Shortcuts" is "fluchkeppelingen", while "keppelingen" means links.
- `preference_advanced_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Developer tools" is rendered as "Untwikkelersark" (singular/odd form) — should be the plural "Untwikkeldersark"/"Ark foar ûntwikkelers", and the word is misspelled without the initial circumflex.
    - Current: `Untwikkelersark`
    - Source: `Developer tools`
    - Suggest: `Ûntwikkelersark`
    - Frisian "ûntwikkelder/ûntwikkeler" starts with û (circumflex); "Untwikkelersark" is a spelling error.
- `preference_crashes` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Crashes" (app crash reports) is translated as "Ungelokken" (accidents), the wrong sense, and also lacks the Frisian accented initial letter.
    - Current: `Ungelokken`
    - Source: `Crashes`
    - Suggest: `Fêstrinnen`
    - The developer comment says this links to Focus crash reports; "ûngelokken" means real-world accidents, not software crashes. Also the initial U should be Û.
- `preference_privacy_should_block_cookies_third_party_only_option` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — The verb "blokkearje" (block) is missing, so the option reads "Only third-party cookies" instead of "Block 3rd-party cookies only".
    - Current: `Allinnich cookies fan tredden`
    - Source: `Block 3rd-party cookies only`
    - Suggest: `Allinnich cookies fan tredden blokkearje`
    - Source is "Block 3rd-party cookies only"; the parallel option string for tracker cookies correctly ends in "blokkearje".
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Coordination makes "apps" and "taking screenshots" both objects of switching, distorting the meaning.
    - Current: `Websiden ferstopje by wikseljen fan apps en meitsjen fan skermôfdrukken blokkearje.`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `Websiden ferstopje by it wikseljen fan apps en it meitsjen fan skermôfdrukken blokkearje.`
    - Source: hide webpages when switching apps AND block taking screenshots; current wording reads as "switching apps and taking screenshots".
- _…and 1 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_check_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "argivearre" — Frisian for archived is "argivearre"? actually the root is "argyf", so the participle should be "argivearre" spelled consistently with the noun.
    - Current: `Argivearre ferzje kontrolearje`
    - Source: `Check Archived Version`
    - Suggest: `Argyfferzje kontrolearje`
    - Elsewhere in the same file the archive is rendered "argyf"/"argyftsjinst"; "Argivearre" is an inconsistent, non-standard derivation.
- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Predicative adjective wrongly inflected: "oerbelêste" should be "oerbelêst".
    - Current: `of oerbelêste`
    - Source: `{ <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If you are unable to load any pages, check your device’s data or Wi-Fi connection.{ </li> } { </ul> }`
    - Suggest: `of oerbelêst`
    - In predicative position after "is ... net beskikber of" the adjective takes no -e ending.
- `mozac_browser_errorpages_malformed_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Unjildich".
    - Current: `Unjildich adres`
    - Source: `Invalid Address`
    - Suggest: `Ûnjildich adres`
    - The Frisian word is "ûnjildich" with a circumflex; the same prefix is written "ûnjildige" in mozac_browser_errorpages_invalid_content_encoding_message.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "in oarder" should be "yn oarder" (typo for the preposition).
    - Current: `Is de proxykonfiguraasje fan de browser in oarder?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `Is de proxykonfiguraasje fan de browser yn oarder?`
    - Spelling error: the preposition is "yn", as correctly used in the parallel string mozac_browser_errorpages_unknown_proxy_host_message.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Wrong article gender: "It website" should be "De website".
    - Current: `It website ferwiist de oanfraach troch`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `De website ferwiist de oanfraach troch`
    - "website" takes the common-gender article "de" in Frisian, as used elsewhere in this same file ("De website op %1$s …").
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — "net werkend" is a misspelling of "net werkent" (does not recognize).
    - Current: `dat de browser net werkend`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `dat de browser net werkent`
    - The verb form for "the browser does not recognize" is "werkent"; "werkend" is a participle/adjective form and is ungrammatical here.
- `mozac_cfr_dismiss_button_content_description` — `mozilla-mobile/android-components/components/compose/cfr/src/main/res/values-fy-rNL/strings.xml` — "Slute" is a misspelling of the Frisian verb "Slute" → correct form is "Slúte".
    - Current: `Slute`
    - Source: `Dismiss`
    - Suggest: `Slúte`
    - Frisian for 'close' is 'slúte' (with ú); the same string elsewhere in the tree uses 'Slúte'.
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Missing preposition "fan" before the placeholder, unlike the parallel enable/remove/uninstall strings.
    - Current: `Utskeakeljen %1$s mislearre`
    - Source: `Failed to disable %1$s`
    - Suggest: `Utskeakeljen fan %1$s mislearre`
    - The corresponding strings use 'Ynskeakeljen fan %1$s mislearre', 'Fuortsmiten fan %1$s mislearre'; omitting 'fan' is ungrammatical.
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Compound noun misspelled: "útwreidingûntwikkeler" is missing the linking -s- used in all sibling strings ("útwreidingsûntwikkeler").
    - Current: `útwreidingûntwikkeler`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `útwreidingsûntwikkeler`
    - All other data-collection long descriptions in the same file render "extension developer" as "útwreidingsûntwikkeler"; this one drops the linking s, which is a spelling/consistency error.
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Compound ‘útwreidingûntwikkeler’ is missing the linking -s- used elsewhere (‘útwreidingsûntwikkeler’).
    - Current: `útwreidingûntwikkeler`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `útwreidingsûntwikkeler`
    - The parallel string mozac_feature_addons_permissions_data_collection_websiteContent_long_description uses ‘útwreidingsûntwikkeler’ for the same source term ‘extension developer’.
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Misspelling of ‘útwreidingsgebrûk’ and missing diacritic on the initial U.
    - Current: `Utwreidigsgebrûk kontrolearje en tema’s beheare`
    - Source: `Monitor extension usage and manage themes`
    - Suggest: `Utwreidingsgebrûk kontrolearje en tema’s beheare`
    - ‘Utwreidigsgebrûk’ drops the ‘n’ from ‘útwreiding’ (extension); the compound should be ‘útwreidingsgebrûk’.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Misspelling of ‘útwreidingsgebrûk’.
    - Current: `Utwreidigsgebrûk kontrolearje en tema’s beheare.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `Utwreidingsgebrûk kontrolearje en tema’s beheare.`
    - ‘Utwreidigs-’ drops the ‘n’ from ‘útwreiding’ (extension); the compound should be ‘útwreidingsgebrûk’.
- `mozac_feature_downloads_file_failure_no_connection` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — The Frisian says the file "is not downloading" instead of the past "wasn’t downloaded".
    - Current: `%1$s is net downloaden.`
    - Source: `%1$s wasn’t downloaded.`
    - Suggest: `%1$s is net download.`
    - Source is past tense/perfect: the download failed. "is net downloaden" reads as an infinitive construction, not the completed-action past participle.
- `mozac_feature_downloads_open_existing_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — Adjective inflection missing before neuter noun 'bestân'.
    - Current: `Besteande bestân iepenje`
    - Source: `Open existing file`
    - Suggest: `Besteand bestân iepenje`
    - 'bestân' is a neuter noun; in an indefinite neuter noun phrase the attributive adjective takes the uninflected form ('besteand bestân').
- `mozac_feature_downloads_open_not_supported1` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — Superfluous preposition 'mei' inserted, changing 'to open %1$s files' into 'to open with %1$s files'.
    - Current: `Gjin app fûn om %1$s-bestannen mei te iepenjen`
    - Source: `No app found to open %1$s files`
    - Suggest: `Gjin app fûn om %1$s-bestannen te iepenjen`
    - The source says no app was found to open the files; 'mei' adds an instrumental sense that is not in the source and is ungrammatical here.
- `mozac_feature_media_notification_action_play` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fy-rNL/strings.xml` — Missing accent on the initial 'Ô' in 'Ofspylje'.
    - Current: `Ofspylje`
    - Source: `Play`
    - Suggest: `Ôfspylje`
    - Frisian spelling is 'ôfspylje'; capitalised it is 'Ôfspylje', not 'Ofspylje'.
- `mozac_feature_prompts_expand_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre kaarten te útklappe`
    - Source: `Expand saved cards`
    - Suggest: `Bewarre kaarten útklappe`
    - The parallel strings (expand saved addresses, collapse saved passwords) use the bare infinitive "Bewarre adressen útklappe" / "Bewarre wachtwurden ynklappe"; the added "te" is ungrammatical here and inconsistent.
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre wachtwurden te útklappe`
    - Source: `Expand saved passwords`
    - Suggest: `Bewarre wachtwurden útklappe`
    - Parallel string mozac_feature_prompts_collapse_logins_content_description_2 uses "Bewarre wachtwurden ynklappe" without "te"; the "te" is ungrammatical and inconsistent.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_settings_label` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — Unnecessary capitalisation of "Ynstellingen" mid-sentence in the button label.
    - Current: `Nei Ynstellingen`
    - Source: `Go to settings`
    - Suggest: `Nei ynstellingen`
    - Source is sentence case ("Go to settings"); Frisian does not capitalise common nouns.
- `mozac_lib_crash_activity_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Ûngelokrapporten".
    - Current: `Ungelokrapporten`
    - Source: `Crash Reports`
    - Suggest: `Ûngelokrapporten`
    - Frisian spells the word with a circumflex: ûngelok. The initial capital must keep the diacritic (Û).
- `addon_ga_message_button_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial U of "Utwreidingen".
    - Current: `Utwreidingen ferkenne`
    - Source: `Explore extensions`
    - Suggest: `Ûtwreidingen ferkenne`
    - Elsewhere the same word is spelled "útwreidingen" with a diacritic; capitalised it must be "Ú/Û" rather than plain "U".
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic: "Ofdieling" should be "Ôfdieling".
    - Current: `Ofdieling`
    - Source: `Department`
    - Suggest: `Ôfdieling`
    - In Frisian the word is spelled "ôfdieling"; capitalised it keeps the circumflex: "Ôfdieling". The current form drops the required diacritic.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Plural "specific features" rendered as singular "spesifike funksje".
    - Current: `Deblokkearje hjirûnder spesifike funksje.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Deblokkearje hjirûnder spesifike funksjes.`
    - The source says "Unblock specific features below" (plural); the Frisian noun is singular, a grammatical/number error.
- `bookmark_import_bookmarks_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_import_menu_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_invalid_url_error` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Unjildige".
    - Current: `Unjildige URL`
    - Source: `Invalid URL`
    - Suggest: `Ûnjildige URL`
    - The Frisian word is "ûnjildich"; capitalized it is "Ûnjildige".
- `bookmark_menu_open_all_in_private_tabs_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "priveeljepblêden" as "proveeljepblêden".
    - Current: `Alles yn proveeljepblêden iepenje`
    - Source: `Open all in private tabs`
    - Suggest: `Alles yn priveeljepblêden iepenje`
    - "private tabs" is rendered elsewhere as "priveeljepblêd"; "proveeljepblêden" is a typo.
- `browser_feature_desktop_site_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ut"; Frisian for "Off" is "Ût".
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Ût`
    - The Frisian word for "off" is spelled "út/Ût" with a circumflex/accent; the toggle label drops the diacritic.
- `create_collection_deselect_all` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Alle deselektearje" is inconsistent with the parallel "Alles selektearje".
    - Current: `Alle deselektearje`
    - Source: `Deselect all`
    - Suggest: `Alles deselektearje`
    - Source pair "Select all"/"Deselect all" should use the same pronoun form; "Alles selektearje" is used for the counterpart.
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om jo bewarre kaarten te besjen`
    - Source: `Unlock to view your saved cards`
    - Suggest: `Ûntskoattelje om jo bewarre kaarten te besjen`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje", not "Untskoattelje".
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Word order is ungrammatical: the imperative with object should be "Untskoattelje jo apparaat" reversed to "Ûntskoattelje jo apparaat" — actual defect is the missing circumflex/accent on Û and wrong construction.
    - Current: `Untskoattelje jo apparaat`
    - Source: `Unlock your device`
    - Suggest: `Ûntskoattelje jo apparaat`
    - Frisian "ûntskoattelje" is written with û; the initial capital must be Û. The same error appears in the neighbouring credit_cards_biometric_prompt_* strings.
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om bewarre betellingsmetoaden te brûken`
    - Source: `Unlock to use saved payment methods`
    - Suggest: `Ûntskoattelje om bewarre betellingsmetoaden te brûken`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje".
- `customize_addon_collection_user_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Adjective/noun agreement error: "Eigener kolleksje" instead of "Eigener fan de kolleksje"/"Kolleksje-eigener".
    - Current: `Eigener kolleksje (brûkers-ID)`
    - Source: `Collection owner (User ID)`
    - Suggest: `Kolleksje-eigener (brûkers-ID)`
    - The source is "Collection owner" (owner of the collection); "Eigener kolleksje" is two juxtaposed nouns without a valid Frisian compound or genitive, giving ungrammatical text.
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Út" (Frisian for "Off").
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Út`
    - The Frisian word for "Off" is "Út" with an acute accent on the capital U; "Ut" is a spelling error.
- `download_content_type_filter_image` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing accent on "Ôfbyldingen".
    - Current: `Ofbyldingen`
    - Source: `Images`
    - Suggest: `Ôfbyldingen`
    - Frisian spells the word with a circumflex: Ôfbylding(en). The initial capital should keep the diacritic.
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Spelling error: "betân" should be "bestân".
    - Current: `Kin betân net omneame`
    - Source: `Can’t rename file`
    - Suggest: `Kin bestân net omneame`
    - The Frisian word for "file" is "bestân" (as used in the related strings); "betân" is a typo.
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Stray preposition 'yn' makes the sentence ungrammatical.
    - Current: `isolearret cookies yn op de website`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `isolearret cookies op de website`
    - The source says cookies are isolated to the site you are on; 'isolearret cookies yn op de website' contains a superfluous 'yn' that breaks the sentence.
- `extension_process_crash_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Ungrammatical verb form and incomplete clause in the second paragraph.
    - Current: `Utwreidingen sille net opnij starte wurden wylst jo aktuele sesje.`
    - Source: `One or more extensions stopped working, making your system unstable. %1$s unsuccessfully tried to restart the extension(s).  Extensions won’t be restarted during your current session.  Removing or disabling extensions m…`
    - Suggest: `Utwreidingen wurde net opnij start yn jo aktuele sesje.`
    - "starte wurden" is not a valid passive construction and "wylst jo aktuele sesje" misuses "wylst" (a conjunction) as a preposition.
- `firefox_labs_no_labs_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "No" appears misplaced/incorrect rendering of "right now".
    - Current: `No gjin eksperimintele funksjes om te probearjen`
    - Source: `No experimental features to try right now`
    - Suggest: `Op dit stuit gjin eksperimintele funksjes om te probearjen`
    - Source is "No experimental features to try right now"; the sentence-initial "No" reads as the English word and does not convey "right now" idiomatically.
- `ip_protection_onboarding_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Untfang" is missing the diacritic; should be "Ûntfang".
    - Current: `Untfang elke moanne fergees %2$d GB.`
    - Source: `%1$s by hiding your location, even on public Wi-Fi. Get %2$d GB free every month.`
    - Suggest: `Ûntfang elke moanne fergees %2$d GB.`
    - Frisian "ûntfange" requires the circumflex; the string elsewhere (ip_protection_onboarding_body_promo) correctly uses "ûntfang".
- `likert_scale_option_i_plan_to_keep_using` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Ungrammatical verb order/construction "om Firefox brûke te bliuwen".
    - Current: `Ik bin fan plan om Firefox brûke te bliuwen`
    - Source: `I plan to keep using Firefox`
    - Suggest: `Ik bin fan plan om Firefox te bliuwen brûken`
    - The source "I plan to keep using Firefox" requires a correct Frisian infinitive construction; "om Firefox brûke te bliuwen" is not grammatical.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untdek".
    - Current: `Untdek`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `Ûntdek`
    - The Frisian imperative of "ûntdekke" is "Ûntdek"; the capital U must carry the circumflex.
- `onboarding_redesign_set_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untfang" (should be "Ûntfang").
    - Current: `Untfang standert automatyske beskerming tsjin folgjen`
    - Source: `Get automatic tracking protection by default`
    - Suggest: `Ûntfang standert automatyske beskerming tsjin folgjen`
    - Frisian "ûntfange" requires the circumflex on the initial u; the capitalised form is "Û".
- `onboarding_redesign_sync_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untfang" (should be "Ûntfang").
    - Current: `Untfang blêdwizers, ljepblêden en wachtwurden op elk apparaat.`
    - Source: `Get bookmarks, tabs, and passwords on any device. All protected with encryption.`
    - Suggest: `Ûntfang blêdwizers, ljepblêden en wachtwurden op elk apparaat.`
    - Frisian "ûntfange" requires the circumflex on the initial u; the capitalised form is "Û".
- `phone_feature_blocked_step_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Machtigingen" is Dutch spelling; Frisian uses "Machtigingen"→"Tastimmingen"/"Machtigings".
    - Current: `Machtigingen`
    - Source: `2. Tap { <b> }Permissions{ </b> }`
    - Suggest: `Machtigings`
    - Frisian plural of "machtiging" is "machtigings"; "machtigingen" is the Dutch form.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Word order error in "hokker website jo besykje gean".
    - Current: `hokker website jo besykje gean`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `hokker website jo besykje sille`
    - The source says "which website you're about to access"; the Frisian clause is ungrammatical/garbled word order.
- `preference_enhanced_tracking_protection_allow_list_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "funksje" as "funskje".
    - Current: `As jo de funskje útskeakelje`
    - Source: `This setting helps fix the most common site problems. If you turn it off, some sites may not work, and %1$s won’t be able to help troubleshoot those issues.`
    - Suggest: `As jo de funksje útskeakelje`
    - "funskje" is a typo; the correct Frisian word is "funksje".
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing space between words in "Cross-sitecookies".
    - Current: `Cross-sitecookies`
    - Source: `Cross-site cookies`
    - Suggest: `Cross-site-cookies`
    - The source is "Cross-site cookies"; the target has the two words run together without a space or hyphen.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Ofslute" is missing the accent on the initial O.
    - Current: `‘Ofslute’`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `‘Ôfslute’`
    - Frisian spelling requires "Ôfslute" with a circumflex on the initial vowel.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "downloadskiednis" as "downloadskeiednis".
    - Current: `downloadskeiednis`
    - Source: `File is removed from your download history, but is still saved on your device`
    - Suggest: `downloadskiednis`
    - The word for history is "skiednis"; other strings in the same group use "downloadskiednis".
- `preferences_passwords_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Utsûnderingen"; should be "Utsûnderingen" with Ú.
    - Current: `Utsûnderingen`
    - Source: `Exceptions`
    - Suggest: `Útsûnderingen`
    - Frisian "útsûnderingen" begins with ú; capitalized it is Ú, as used in the same file's string preferences_passwords_exceptions_remove_all ("Alle útsûnderingen fuortsmite").
- `preferences_show_search_optimization_cards` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Verb form "type" should be the plural/polite form "type" → "typt" agreeing with "jo".
    - Current: `wylst jo type`
    - Source: `Retrieve suggestions from Mozilla as you type`
    - Suggest: `wylst jo type `
    - In Frisian the polite pronoun "jo" takes the -e/-je form depending on verb class; "typen" is a weak verb class II, so the correct form is "jo type" — however the standard form after "jo" for this verb is "typje".
- `preferences_show_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "suggestjes" as "suggesjes".
    - Current: `Syksuggesjes toane`
    - Source: `Show search suggestions`
    - Suggest: `Syksuggestjes toane`
    - Elsewhere the term is spelled "suggestjes" (e.g. "Klamboerdsuggestjes toane"); "suggesjes" drops the t.
- `preferences_sync_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "ljepblêden" as "ljeplêden".
    - Current: `Iepen ljeplêden`
    - Source: `Open tabs`
    - Suggest: `Iepen ljepblêden`
    - The Frisian word for tabs is "ljepblêden" (used consistently elsewhere in this batch); "ljeplêden" is missing the b.
- `privacy_notice_updated_homepage_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Duplicated/garbled verb phrase "yn Firefox te wer te jaan".
    - Current: `om de nijste funksjes yn Firefox te wer te jaan`
    - Source: `We’ve updated our %1$s to reflect the latest features in Firefox. %2$s`
    - Suggest: `om de nijste funksjes yn Firefox wer te jaan`
    - The infinitive marker "te" is duplicated, producing ungrammatical Frisian; source is "to reflect the latest features in Firefox".
- `protection_panel_etp_disabled_no_trackers_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelled verb "wirde" instead of "wurde".
    - Current: `Trackers wirde net blokkearre`
    - Source: `Trackers aren’t blocked`
    - Suggest: `Trackers wurde net blokkearre`
    - The Frisian plural present of "wurde" is "wurde"; "wirde" is a spelling error.
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Misspelled verb "efterlitte"; correct Frisian is "efterlitte" written as "achterlitte"/"efterlitte" — here the spelling is wrong.
    - Current: `Kommentaar efterlitte`
    - Source: `Leave feedback`
    - Suggest: `Kommentaar achterlitte`
    - The standard Frisian verb for 'leave (behind)' is 'achterlitte'; 'efterlitte' is not the standard spelling.
- `search_suggestions_delete_history_item_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Confirmation of a completed deletion is rendered as an infinitive/imperative instead of a past participle.
    - Current: `%1$s út skiednis fuortsmite`
    - Source: `Deleted %1$s from history`
    - Suggest: `%1$s út skiednis fuortsmiten`
    - Source "Deleted %1$s from history" is a snackbar confirming that the item has been deleted, not an action label.
- `setup_checklist_group_helpful_tools` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Plural "tools" rendered as singular "ark" without plural marking.
    - Current: `Nuttich ark`
    - Source: `Helpful tools`
    - Suggest: `Nuttige ark`
    - Source is "Helpful tools" (plural, collective); the Frisian adjective before the collective noun "ark" requires the inflected form "nuttige".
- `setup_checklist_subtitle_3_steps_first_step` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Goed j!" is a garbled/incomplete rendering of "Great start!".
    - Current: `Goed j!`
    - Source: `Great start! You’ve completed 1 out of 3 steps.`
    - Suggest: `Goed begjin!`
    - The source "Great start!" should read "Goed begjin!"; "Goed j" is not a Frisian word/phrase and appears to be a truncation.
- _…and 27 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "browsing history" is rendered as "browserskiednis" here but as "sneupskiednis" in the parallel _for_update string.
    - Current: `Resinte browserskiednis, cookies en relatearre gegevens wiskje`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Resinte sneupskiednis, cookies en relatearre gegevens wiskje`
    - The same source sentence ("Clear recent browsing history, cookies, and related data") is translated with two different terms on the same surface; fy-NL uses "sneup-" for browsing (cf. sneupaktiviteit for "browsing activity").
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — The update variant uses an imperative form and different wording/terminology than the non-update variant of the same permission description.
    - Current: `Wreidzje jo ûntwikkelark út foar tagong ta gegevens yn jo iepen ljepblêden.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen.`
    - mozac_feature_addons_permissions_devtools_description translates the identical source as ‘Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen’; the update string must match in style (infinitive) and term (ûntwikkelersark vs ûntwikkelark) since these appear on the same surface.
- `mozac_feature_addons_permissions_dialog_heading_required_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — ‘permissions’ is rendered as ‘machtigingen’ here but as ‘tastimmingen’ in the parallel optional-permissions heading.
    - Current: `Fereaske machtigingen:`
    - Source: `Required permissions:`
    - Suggest: `Fereaske tastimmingen:`
    - mozac_feature_addons_permissions_dialog_heading_optional_permissions translates ‘New permissions:’ as ‘Nije tastimmingen:’; both headings appear in the same add-on permissions dialog and must use one term.
- `mozac_feature_addons_permissions_privacy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "modify" rendered as "oanpasse" here but as "bewurkje" in the identical non-update string.
    - Current: `Privacyynstellingen lêze en oanpasse.`
    - Source: `Read and modify privacy settings.`
    - Suggest: `Privacyynstellingen lêze en bewurkje.`
    - mozac_feature_addons_permissions_privacy_description translates the same source sentence as "Privacyynstellingen lêze en bewurkje"; the paired update string must match.
- `mozac_feature_contextmenu_snackbar_link_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fy-rNL/strings.xml` — "Link" is rendered as "Koppeling" (Dutch) here while the rest of the file consistently uses the Frisian "Keppeling".
    - Current: `Koppeling nei klamboerd kopiearre`
    - Source: `Link copied to clipboard`
    - Suggest: `Keppeling nei klamboerd kopiearre`
    - Sibling strings (mozac_feature_contextmenu_share_link, mozac_feature_contextmenu_snackbar_link_text_copied) use "Keppeling"; "Koppeling" is the Dutch spelling and is inconsistent on the same surface.
- `mozac_feature_sitepermissions_notification_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — "notifications" is rendered as "meldingen" here but as "notifikaasjes" in the sibling notification-permission string on the same surface.
    - Current: `%1$s tastean om meldingen te ferstjoeren?`
    - Source: `Allow %1$s to send notifications?`
    - Suggest: `%1$s tastean om notifikaasjes te ferstjoeren?`
    - mozac_feature_sitepermissions_notification_permission_rationale_dialog_message translates "notifications" as "notifikaasjes"; the same term in the same notification-permission dialog flow should be consistent.
- `credit_cards_warning_dialog_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "payment methods" is rendered "betelmetoaden" here but "betellingsmetoaden" in the neighbouring credit card strings.
    - Current: `betelmetoaden`
    - Source: `Secure your saved payment methods`
    - Suggest: `betellingsmetoaden`
    - Inconsistent terminology for the same source term on the same surface (see credit_cards_warning_dialog_message_3 and credit_cards_biometric_prompt_unlock_message_2).
- `debug_drawer_region_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Tools" rendered as "helpmiddelen" here while the same debug-drawer surface uses "ark" elsewhere (CFR-ark, Add-ons-ark, Ark foar automatysk ynfoljen).
    - Current: `Regiohelpmiddelen`
    - Source: `Region Tools`
    - Suggest: `Regio-ark`
    - Terminology inconsistency for "Tools" on the same Debug Drawer surface, where "ark" is the established rendering.
- `extension_process_crash_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "extension(s)" rendered as "add-on(s)" while the rest of the string uses "útwreidingen" for extensions.
    - Current: `de add-on(s) opnij te starten`
    - Source: `One or more extensions stopped working, making your system unstable. %1$s unsuccessfully tried to restart the extension(s).  Extensions won’t be restarted during your current session.  Removing or disabling extensions m…`
    - Suggest: `de útwreiding(en) opnij te starten`
    - Source consistently says "extension(s)"; the surrounding sentences use útwreidingen, so add-on is an inconsistent term for the same source word.
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "more private" rendered as "persoanliker" (more personal) instead of the privacy term used in the parallel string.
    - Current: `persoanliker`
    - Source: `Turn VPN on to make your browsing more private and harder to trace.`
    - Suggest: `mear privee`
    - The source says "more private"; the parallel string ip_protection_onboarding_body_promo translates the same phrase as "mear privee", so "persoanliker" (more personal) is both a mistranslation and inconsistent.
- `search_engine_selector_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Search engine" is rendered as "sykmasjine" here but "sykmasine" everywhere else in the same surface.
    - Current: `%s: sykmasjineselektor`
    - Source: `%s: search engine selector`
    - Suggest: `%s: sykmasineselektor`
    - Neighbouring strings (search_engine_edit_custom_search_engine_title, search_engine_icon_content_description_1, search_engine_use_default) all use "sykmasine"; this spelling is inconsistent.
- `setup_checklist_subtitle_5_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "setup steps" translated as "ynstallaasjestappen" (installation steps) instead of setup/configuration steps.
    - Current: `ynstallaasjestappen`
    - Source: `You’ve completed all 5 setup steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `ynstelstappen`
    - The checklist concerns setting up the app (ynstelle), not installing it; other strings in the same feature use "ynstelle".
- `setup_checklist_subtitle_6_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "setup steps" translated as "ynstallaasjestappen" (installation steps) instead of setup/configuration steps.
    - Current: `ynstallaasjestappen`
    - Source: `You’ve completed all 6 setup steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `ynstelstappen`
    - The checklist concerns setting up the app (ynstelle), not installing it; other strings in the same feature use "ynstelle".
- `sports_widget_country_selector_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Informal address "dyn" used instead of the polite "jo" form used throughout the locale.
    - Current: `Folgje dyn team`
    - Source: `Follow your team`
    - Suggest: `Folgje jo team`
    - The rest of the batch consistently uses the formal "jo" (e.g. "Kontrolearje jo ynternetferbining", "Meld jo oan mei jo kamera"); "dyn" breaks the established register.
- `terms_of_use_prompt_title_option_a` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Terms of Use" is translated as "Gebrûksbetingsten" here but "Brûkersbetingsten" in terms_of_use_prompt_link_terms_of_use on the same prompt.
    - Current: `Gebrûksbetingsten`
    - Source: `Terms of Use`
    - Suggest: `Brûkersbetingsten`
    - The same source term on the same surface is rendered two different ways, creating terminology inconsistency.
- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "search string" rendered as "sykterm" here but "syksterm" in search_add_error_empty_search on the same screen.
    - Current: `sykterm`
    - Source: `Check that search string matches Example format`
    - Suggest: `syksterm`
    - The same source term "search string" is translated inconsistently within the same settings surface (search_add_error_empty_search uses "syksterm").

### E. Typography, punctuation & spacing

- `mozac_feature_addons_permissions_user_scripts_extra_warning` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — Doubled apostrophe in "dy’'t" (typographic apostrophe followed by a straight one).
    - Current: `dy’'t`
    - Source: `Unverified scripts can pose security and privacy risks. Only run scripts from extensions or sources you trust.`
    - Suggest: `dy’t`
    - The relative pronoun should be "dy’t"; the extra straight apostrophe is a stray character and breaks the locale's typographic apostrophe convention.
- `connection_security_panel_verified_by` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — A colon was added that is not in the source, unlike the parallel string "Utjûn oan %s".
    - Current: `Ferifiearre troch: %s`
    - Source: `Verified by %s`
    - Suggest: `Ferifiearre troch %s`
    - Source "Verified by %s" has no colon; the sibling string "Issued to %s" is translated without one.
- `sports_widget_error_connection_interrupted` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Em dash in source rendered as an en dash without matching house convention spacing/character check.
    - Current: `Ferbining ûnderbrutsen – live updates pauzearre.`
    - Source: `Connection interrupted — live updates paused.`
    - Suggest: `Ferbining ûnderbrutsen — live updates pauzearre.`
    - The source uses an em dash; the locale convention table lists the en dash as the house dash, but here the punctuation mark differs from the source separator. Low-impact cosmetic mismatch.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (9)

- `download_content_type_filter_video` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `tab_tray_inactive_auto_close_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-08-21
