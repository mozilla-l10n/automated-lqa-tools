# Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **Previous run** | 2026-08-21 @ `7134a6c77a67` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (1)

- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — `onboarding_first_screen_title` has placeholders %s where the source has %1$s
    - Current: `Dobrodošli v %su`
    - Source: `Welcome to %1$s`
    - Suggest: `Dobrodošli v %1$su`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

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
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**3 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — 3

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 15, `curly-double` 4 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1, `en` 5 | **en** |
| register | `informal` 4, `formal` 97 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (129)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 71 |
| 3 | Degraded language (grammar, spelling, terminology) | 45 |
| 4 | Cosmetic (typography, spacing) | 12 |

### A. Functional, markup, variables & plurals

- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — `onboarding_first_screen_title` has placeholders %s where the source has %1$s
    - Current: `Dobrodošli v %su`
    - Source: `Welcome to %1$s`
    - Suggest: `Dobrodošli v %1$su`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — Second bullet limits the spelling check to the file name instead of the address as in the source.
    - Current: `Je njeno ime napačno črkovano`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `Je v naslovu napaka v črkovanju`
    - Source asks about a typographical error in the address, not in the item's name.
- `mozac_browser_errorpages_harmful_addon_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — "credit card numbers" mistranslated as "podatki o bančnem računu" (bank account details).
    - Current: `podatki o bančnem računu`
    - Source: `{ <p> }This web page at %1$s has been blocked because one of your add-ons tried to open it. This site could be used to steal your info — like passwords or credit card numbers.{ </p> }`
    - Suggest: `številke kreditnih kartic`
    - The source says credit card numbers, not bank account information.
- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — Translation adds "varna" (secure) not present in the source when describing the HTTPS version.
    - Current: `varna različica HTTPS strani`
    - Source: `You’ve enabled HTTPS-Only Mode for enhanced security, and a HTTPS version of { <em> }%1$s{ </em> } is not available.`
    - Suggest: `različica HTTPS strani`
    - Source states only that an HTTPS version of the site is not available; "varna" is added content.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — "The network link was interrupted" rendered as "Povezava s stranjo je bila nepričakovano prekinjena", changing network link to page connection and adding "nepričakovano".
    - Current: `Povezava s stranjo je bila nepričakovano prekinjena med pogajanjem za povezavo.`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `Omrežna povezava je bila prekinjena med vzpostavljanjem povezave.`
    - The source refers to the network link, and contains no "unexpectedly".
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — Third bullet drops the source's mention that incorrect firewall/proxy settings can interfere with web browsing and rewrites the question.
    - Current: `Če uporabljate posrednika ali požarni zid, se prepričajte, da so vaše nastavitve pravilne.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Ali je vaša naprava ali omrežje zaščiteno s požarnim zidom ali posredniškim strežnikom? Napačne nastavitve lahko ovirajo brskanje po spletu.`
    - The source sentence's content (device/network protected by firewall or proxy; incorrect settings can interfere with Web browsing) is not conveyed.
- `mozac_browser_errorpages_port_blocked_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — "Port restricted for security reasons" is rendered as "Vrata nesprejemljiva" (port unacceptable) instead of restricted/blocked.
    - Current: `Vrata nesprejemljiva iz varnostnih razlogov`
    - Source: `Port restricted for security reasons`
    - Suggest: `Vrata omejena iz varnostnih razlogov`
    - The source says the port is restricted (blocked), not that it is "unacceptable".
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — First sentence mistranslated: source says the browser could not find the host server for the provided address, translation says only "The page could not be found".
    - Current: `Strani ni bilo mogoče najti.`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `Brskalnik ni mogel najti gostiteljskega strežnika za navedeni naslov.`
    - The en-US text refers to the host server for the provided address; the translation drops that content and says something different.
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — "wants to collect" is rendered as a plain present tense "zbira" (collects), dropping the intent/request meaning.
    - Current: `Razvijalec pravi, da razširitev zbira: %1$s`
    - Source: `The developer says the extension wants to collect: %1$s`
    - Suggest: `Razvijalec pravi, da želi razširitev zbirati: %1$s`
    - The source states the extension *wants to* collect the listed data (a request for consent), not that it already collects it.
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — Translation drops "during navigation" from the webNavigation permission description.
    - Current: `dostop do dejavnosti brskalnika`
    - Source: `Access browser activity during navigation`
    - Suggest: `dostop do dejavnosti brskalnika med krmarjenjem`
    - Source is "Access browser activity during navigation"; the qualifier is omitted, and the paired _for_update string does include it, creating inconsistency.
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — The privacy policy and terms of service links are swapped relative to the source order and placeholders.
    - Current: `njihovi <a href="%4$s">pogoji uporabe{ </a> } in <a href="%3$s">pravilnik o zasebnosti{ </a> }`
    - Source: `Logging in to %1$s with a %2$s account is subject to their <a href="%3$s">Privacy Policy{ </a> } and <a href="%4$s">Terms of Service{ </a> }`
    - Suggest: `njihov <a href="%3$s">pravilnik o zasebnosti{ </a> } in <a href="%4$s">pogoji uporabe{ </a> }`
    - Source lists Privacy Policy (%3$s) first and Terms of Service (%4$s) second; the translation reverses them, though placeholders still track their labels, the order change alters the string relative to source and risks confusion.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — "Setting up summaries" is rendered as "Namestitev povzetkov" (installation of summaries) instead of setup/preparation.
    - Current: `Namestitev povzetkov`
    - Source: `Setting up summaries`
    - Suggest: `Nastavljanje povzetkov`
    - The source means the feature is being set up/prepared, not that summaries are being installed; "namestitev" means installation of software.
- `mozac_support_base_permissions_needed_negative_button` — `mozilla-mobile/android-components/components/support/base/src/main/res/values-sl/strings.xml` — "Dismiss" is translated as "Skrij" (Hide) instead of a dismiss/close term.
    - Current: `Skrij`
    - Source: `Dismiss`
    - Suggest: `Opusti`
    - The button dismisses the dialog; "Skrij" means "hide", which is a different action than dismissing.
- `sound_off` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-sl/strings.xml` — The muted-sound emoji 🔇 was replaced with the speaker emoji 🔈, making "sound off" and "sound on" visually identical.
    - Current: `🔈 zvok izključen`
    - Source: `🔇 sound off`
    - Suggest: `🔇 zvok izključen`
    - The source uses 🔇 (muted) for sound off and 🔈 for sound on; the translation uses 🔈 for both, losing the distinction.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "you can unblock anything you want to keep using" is rendered as "you can enable individual features", losing the unblock/keep-using meaning and using inconsistent terminology.
    - Current: `Naknadno lahko omogočite posamezne možnosti, ki bi jih radi uporabljali.`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `Pozneje lahko odblokirate karkoli, kar želite še naprej uporabljati.`
    - The source states the user can unblock anything they want to keep using; the translation changes it to enabling individual options, and elsewhere the same concept uses prepovedati/omogočiti inconsistently.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Custom tab menu" is mistranslated as "menu of custom tabs", changing the meaning.
    - Current: `Zapri meni zavihkov po meri`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Zapri list menija prilagojenega zavihka`
    - Source is "Close custom tab menu sheet" — the menu of the custom tab (singular), and the word "sheet" (bottom sheet) is dropped; the Slovenian genitive plural "zavihkov po meri" says "tabs made to order".
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Unlock to use saved payment methods" is translated as "unlock to view saved payment methods".
    - Current: `Odklenite za ogled shranjenih plačilnih sredstev`
    - Source: `Unlock to use saved payment methods`
    - Suggest: `Odklenite za uporabo shranjenih plačilnih sredstev`
    - The source says "use" (uporabo), not "view" (ogled); the developer comment states it is shown before allowing users to use their stored payment method information.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Debug locales to enable" is rendered as "Jeziki" (languages), losing both "debug" and the locale concept.
    - Current: `Jeziki, ki naj bodo omogočeni`
    - Source: `Debug locales to enable`
    - Suggest: `Razhroščevalne območne nastavitve, ki naj bodo omogočene`
    - The source refers to debug locales, not languages; elsewhere in the same feature (debug_drawer_add_new_address) "locale" is translated as "območna nastavitev".
- `etp_cookies_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Cross-Site Tracking Cookies" rendered as "Spletni sledilni piškotki", dropping the cross-site meaning.
    - Current: `Spletni sledilni piškotki`
    - Source: `Cross-Site Tracking Cookies`
    - Suggest: `Medspletni sledilni piškotki`
    - The source specifies cookies that track across sites; "Spletni" only means "web/online" and loses the cross-site distinction, which the sibling string etp_cookies_title_2 renders as "Medspletni".
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Redirect Trackers" is rendered as "Preusmeritve sledilcev" ("redirects of trackers"), reversing the head of the phrase.
    - Current: `Preusmeritve sledilcev`
    - Source: `Redirect Trackers`
    - Suggest: `Preusmeritveni sledilci`
    - The source names a category of trackers (trackers that use redirects), not redirects belonging to trackers; the head noun must be "sledilci", as in the sibling titles "Sledilci družbenih omrežij".
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Placeholder for the app name is used as a modifier of "zavihkov", producing "Zaprtih Firefox zavihkov" instead of naming the app as subject/prefix.
    - Current: `Zaprtih %1$s zavihkov: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s – zaprtih zavihkov: %2$d`
    - %1$s is the app name (Firefox). "Zaprtih Firefox zavihkov: 3" is ungrammatical in Slovenian (unmarked noun-noun modification) and misreads the placeholder role described in the developer comment.
- `link_shared_snackbar_action` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Manage settings" is shortened to just "Nastavitve", dropping the verb "Manage".
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljaj nastavitve`
    - The source action label instructs the user to manage settings; the translation only says "Settings".
- `link_shared_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Link shared" is translated as "Povezava poslana" (link sent) instead of "shared".
    - Current: `Povezava poslana`
    - Source: `Link shared`
    - Suggest: `Povezava deljena`
    - The source says the link was shared, not sent; other strings in this feature use "deliti/deljeno" for share.
- `microsurvey_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "search experience" translated as "možnost iskanja" (search option).
    - Current: `Kako zadovoljni ste z možnostjo iskanja v Firefoxu?`
    - Source: `How satisfied are you with the search experience in Firefox?`
    - Suggest: `Kako zadovoljni ste z izkušnjo iskanja v Firefoxu?`
    - The source asks about the search experience, not about a search option; the parallel string microsurvey_sync_title also drops "experience" but this one changes the meaning to a feature/option.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "translation menu" rendered as "meni prevajalnika" (translator's menu).
    - Current: `v meniju prevajalnika`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `v meniju za prevajanje`
    - The source says "the translation menu"; "prevajalnik" names a translator tool rather than the translation menu.
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "home screen" of the phone is translated as "domača stran" (web homepage) instead of "domači zaslon".
    - Current: `Začnite vsako iskanje z domače strani svojega telefona`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `Začnite vsako iskanje z domačega zaslona svojega telefona`
    - The source refers to the phone's home screen; Slovenian uses "domači zaslon" for that (as correctly used in nova_onboarding_app_icon_prompt_body), while "domača stran" means a website homepage.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "marketing partners" is rendered as "tehnološkim partnerjem za trženje", adding "tehnološkim" (technology) which is not in the source.
    - Current: `Mozillinim tehnološkim partnerjem za trženje`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Mozillinim tržnim partnerjem`
    - The source says only "Mozilla’s marketing partners"; "tehnološkim" (technological) is invented content.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "marketing partners" is rendered as "tehnološkim partnerjem za trženje", adding "tehnološkim" (technology) which is not in the source.
    - Current: `Mozillinim tehnološkim partnerjem za trženje`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozillinim tržnim partnerjem`
    - The source says only "Mozilla’s marketing partners"; "tehnološkim" (technological) is invented content.
- `nova_onboarding_tou_body_line_3_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Link text "Manage settings" is rendered only as "Nastavitve", dropping the verb.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - Source is "Manage settings"; the parallel string onboarding_redesign_tou_body_three_link_text correctly uses "Upravljanje nastavitev". "Nastavitve" means just "Settings".
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "marketing partners" is translated as "tehnološkim partnerjem za trženje", adding "technology" which is not in the source.
    - Current: `Mozillinim tehnološkim partnerjem za trženje`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozillinim partnerjem za trženje`
    - The source says only "Mozilla’s marketing partners"; "tehnološkim" (technology) is an addition not present in the English.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "marketing partners" is translated as "tehnološkim partnerjem za trženje", adding "technology" which is not in the source.
    - Current: `Mozillinim tehnološkim partnerjem za trženje`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozillinim partnerjem za trženje`
    - The source says only "Mozilla’s marketing partners"; "tehnološkim" (technology) is an addition not present in the English.
- `open_all_warning_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Translation says "Open several tabs" instead of "Open %d tabs?", losing the exact count wording.
    - Current: `Odprem več zavihkov (%d)?`
    - Source: `Open %d tabs?`
    - Suggest: `Odprem toliko zavihkov (%d)?`
    - The source asks whether to open the specific number of tabs; "več" (several/more) changes the meaning.
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Set by Battery Saver" is rendered as an imperative "Nastavi ohranjevalnik baterije" ("Set the battery saver"), reversing the meaning.
    - Current: `Nastavi ohranjevalnik baterije`
    - Source: `Set by Battery Saver`
    - Suggest: `Nastavi ohranjevalnik baterije → "Nastavi ohranjevalnik baterije" naj bo "Nastavi ohranjevalnik porabe" – pravilno: "Določi ohranjevalnik baterije"`
    - The source means the theme is determined by the Battery Saver setting; the Slovenian reads as a command to set/configure the battery saver, with the wrong subject-object relation.
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Translation is truncated: the word "DNS" is missing at the end of the phrase "z zavarovanim".
    - Current: `privzeti razreševalnik DNS uporabi samo, če pride do težav z zavarovanim`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `privzeti razreševalnik DNS uporabi samo, če pride do težav z zavarovanim DNS`
    - Source reads "...if there is a problem with secure DNS"; the Slovenian ends with the adjective "zavarovanim" with no noun, leaving the sentence incomplete.
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Cross-site cookies" is translated as "Spletni piškotki" (web cookies), losing the cross-site meaning.
    - Current: `Spletni piškotki`
    - Source: `Cross-site cookies`
    - Suggest: `Piškotki drugih strani`
    - The source refers specifically to cross-site cookies; the translation says merely "web cookies", which is a different, broader concept.
- `preferences_enable_gecko_logs` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Adds "izrisovalnika" (renderer), which is not in the source and mischaracterizes Gecko.
    - Current: `Omogoči dnevnike izrisovalnika Gecko`
    - Source: `Enable Gecko logs`
    - Suggest: `Omogoči dnevnike Gecko`
    - Source is "Enable Gecko logs"; the translation invents the qualifier "renderer" not present in the English string.
- `preferences_https_only_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The object "sites" is dropped, so the sentence says it connects to the protocol rather than to sites using HTTPS.
    - Current: `Za večjo varnost poskuša samodejno vzpostaviti povezavo s šifrirnim protokolom HTTPS.`
    - Source: `Automatically attempts to connect to sites using HTTPS encryption protocol for increased security.`
    - Suggest: `Za večjo varnost poskuša samodejno vzpostaviti povezavo s spletnimi mesti prek šifrirnega protokola HTTPS.`
    - Source: "Automatically attempts to connect to sites using HTTPS encryption protocol" — the connection target (sites) is omitted.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "haven’t viewed" rendered as "niste odprli" (haven't opened).
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - Source says tabs you haven't viewed for two weeks; opening and viewing are different actions.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The translation drops "marketing" from "Mozilla's marketing technology partners".
    - Current: `z Mozillinimi tehnološkimi partnerji`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `z Mozillinimi trženjskimi tehnološkimi partnerji`
    - Source says "Mozilla’s marketing technology partners"; the Slovenian omits "marketing", changing who the data is shared with.
- `preferences_search_browsing_history` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Search browsing history" is rendered as "search history" instead of "browsing history".
    - Current: `Išči po zgodovini iskanja`
    - Source: `Search browsing history`
    - Suggest: `Iskanje po zgodovini brskanja`
    - The source refers to browsing history (zgodovina brskanja), not search history; also inconsistent with the parallel items "Iskanje po zaznamkih"/"Iskanje po sinhroniziranih zavihkih".
- `restart_warning_dialog_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The placeholder (brand name) was moved to the first sentence, so the translation says "Firefox may close" instead of "The app may close … to reopen Firefox".
    - Current: `%1$s se bo morda zaprl. Ponovno ga odprite z dotikom čudovite nove ikone.`
    - Source: `The app may close. Just tap your shiny new icon to reopen %1$s.`
    - Suggest: `Aplikacija se bo morda zaprla. Za ponovno odprtje %1$s se dotaknite čudovite nove ikone.`
    - Source: "The app may close. Just tap your shiny new icon to reopen %1$s." The brand name belongs to the second sentence; the first sentence should refer to the app generically.
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Leave feedback" is rendered as "Send feedback" instead of leaving/giving feedback.
    - Current: `Pošlji povratne informacije`
    - Source: `Leave feedback`
    - Suggest: `Pustite povratne informacije`
    - The source asks the user to leave feedback in a forum, not to send it; also the imperative form differs from the formal register used elsewhere in this prompt group.
- `saved_login_clear_hostname` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "hostname" is translated as "domeno" (domain) rather than host/site name.
    - Current: `Počisti domeno`
    - Source: `Clear hostname`
    - Suggest: `Počisti ime gostitelja`
    - The field is the hostname field; a domain is not the same as a hostname, and this content description misnames the control.
- `saved_login_hostname_required` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Hostname required" translated as "domain name required".
    - Current: `Zahtevano je ime domene`
    - Source: `Hostname required`
    - Suggest: `Zahtevano je ime gostitelja`
    - The error refers to the hostname field, not a domain name.
- `search_add_custom_engine_error_missing_template` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Example format" is rendered as "the format of the example" losing the reference to the shown example format placeholder.
    - Current: `Prepričajte se, da se iskalni niz ujema z obliko primera`
    - Source: `Check that search string matches Example format`
    - Suggest: `Preverite, ali se iskalni niz ujema z obliko primera`
    - The source instructs the user to check that the string matches the example format; "Prepričajte se" (make sure) plus wording shifts the meaning slightly, but more importantly the check-verb should be used.
- `search_suggestions_onboarding_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "private sessions" is translated as "zasebnih oknih" (private windows).
    - Current: `zasebnih oknih`
    - Source: `Allow search suggestions in private sessions?`
    - Suggest: `zasebnih sejah`
    - The source says sessions, not windows; Android has no windows.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Search settings" as a verb phrase (search through settings) is rendered as the noun phrase "Nastavitve iskanja" (settings of search).
    - Current: `Nastavitve iskanja`
    - Source: `Search settings`
    - Suggest: `Preišči nastavitve`
    - The developer comment explicitly says "Search" is a verb here — this is the title of the Settings Search screen, not the search settings page (which is search_settings_menu_item).
- `setup_checklist_subtitle_5_steps_third_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Ste preko polovice" (you are past halfway) differs from the source "You’re halfway there".
    - Current: `Ste preko polovice!`
    - Source: `You’re halfway there! Three steps finished and 2 to go.`
    - Suggest: `Ste na pol poti!`
    - Source says "halfway there"; the parallel 6-step string correctly uses "Ste na pol poti!", making this both a mistranslation and an inconsistency.
- `sports_widget_error_load_failed_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Try refreshing" is rendered as "Poskusite znova" (try again), dropping the refresh action present in the sibling strings.
    - Current: `Poskusite znova čez nekaj minut.`
    - Source: `Try refreshing in a few minutes.`
    - Suggest: `Poskusite osvežiti čez nekaj minut.`
    - The source says "Try refreshing in a few minutes"; the identical clause in sports_widget_error_load_failed is translated "Poskusite osvežiti čez nekaj minut", so this rendering is both inaccurate and inconsistent.
- `sports_widget_still_want_to_follow` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Still want to follow along?" is reduced to "Vas še zanima?", losing the meaning of continuing to follow the tournament.
    - Current: `Vas še zanima?`
    - Source: `Still want to follow along?`
    - Suggest: `Želite še naprej spremljati dogajanje?`
    - The card asks whether the user wants to keep following the tournament after their team was eliminated; the translation only asks whether they are still interested.
- `sports_widget_team_followed_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Check back" is mistranslated as "Spremljajte nas" (follow us).
    - Current: `Spremljajte nas za informacije o tekmah, ko se bo turnir približal.`
    - Source: `Check back for match info as the tournament approaches.`
    - Suggest: `Znova preverite informacije o tekmah, ko se bo turnir približal.`
    - The source tells the user to return later to see match info, not to follow the provider.
- `sports_widget_team_followed_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Following: %s" is translated as "Sledim" (I am following) instead of a neutral/user-oriented form.
    - Current: `Sledim: %s`
    - Source: `Following:  %s`
    - Suggest: `Sledite: %s`
    - The source label states which team the user follows; first-person singular "Sledim" makes the app speak for itself and breaks the established formal address to the user.
- `sync_failed_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Last success" is rendered as "Nazadnje sinhronizirano", losing the distinction from the never-synced/last-synced strings.
    - Current: `Sinhronizacija ni uspela. Nazadnje sinhronizirano: %s`
    - Source: `Sync failed. Last success: %s`
    - Suggest: `Sinhronizacija ni uspela. Zadnja uspešna: %s`
    - The source specifically says "Last success" (last successful sync), not simply "last synced".
- `synced_tabs_no_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Translation adds "drugih" ("other tabs"), changing the meaning of the source.
    - Current: `V Firefoxu na drugih napravah nimate odprtih drugih zavihkov.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `V Firefoxu na drugih napravah nimate odprtih zavihkov.`
    - Source says the user has no tabs open in Firefox on other devices; "odprtih drugih zavihkov" implies "no other tabs open", which is not the source meaning.
- `tab_group_color_purple` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Purple" is translated as "Lila" (lilac) instead of "Vijolična".
    - Current: `Lila`
    - Source: `Purple`
    - Suggest: `Vijolična`
    - The standard Slovenian term for the color purple is "vijolična"; "lila" denotes a different, lighter shade (lilac).
- `tab_group_sheet_dismiss_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "View tab group" is rendered as an imperative command to the app rather than the accessibility action label, and the string is a content description for a handle.
    - Current: `Prikaži skupino zavihkov, strni ročico za vlečenje`
    - Source: `View tab group, collapse drag handle`
    - Suggest: `Ogled skupine zavihkov, ročica za strnjenje`
    - The source describes the drag handle state (view tab group / collapse drag handle) for screen readers; the Slovenian imperative "Prikaži ... strni ..." reads as commands rather than a description.
- `tab_manager_empty_tab_groups_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "They're saved here" is mistranslated as "Vanjo bodo shranjeni" (saved into the group) and expanded with content not in the source.
    - Current: `Vanjo bodo shranjeni in pripravljeni na trenutek, ko jih boste potrebovali.`
    - Source: `Select tabs to create a group. They’re saved here, ready when you are.`
    - Suggest: `Shranjene bodo tukaj, pripravljene, ko boste vi.`
    - The source says the groups are saved here (on this page), ready when you are; the translation says the tabs will be saved into the group and ready when you need them.
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Dismiss" (dismiss the banner) is translated as "Zapri" which in this tab-tray context reads as "Close [tabs]".
    - Current: `Zapri`
    - Source: `Dismiss`
    - Suggest: `Opusti`
    - The button dismisses the Close Tabs Banner; "Zapri" is the same word used elsewhere for closing tabs (tab_tray_menu_item_close) and is ambiguous/wrong here.
- `tab_tray_inactive_onboarding_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "haven’t viewed" is rendered as "niste odprli" (haven't opened) instead of "si niste ogledali".
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - Source says tabs not viewed for two weeks; opening and viewing are different actions, and the parallel string tab_tray_inactive_auto_close_body_2 uses "si jih niste ogledali".
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Content description drops "sheet", saying "Close Translations" instead of "Close Translations sheet".
    - Current: `Zaprite Prevode`
    - Source: `Close Translations sheet`
    - Suggest: `Zaprite list Prevajanje`
    - The source describes closing the translations bottom sheet; the target omits the "sheet" element and reads as closing the translations themselves.
- `translations_bottom_sheet_info_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "your device" is translated as "računalnika" (computer) in a mobile app.
    - Current: `nikoli ne zapustijo vašega računalnika`
    - Source: `For your privacy, translations never leave your device. New languages and improvements coming soon! %1$s`
    - Suggest: `nikoli ne zapustijo vaše naprave`
    - The source says "never leave your device"; other strings in the same feature use "naprava" (translation_settings_control_description). "Računalnik" means computer and is wrong on Android.
- _…and 12 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — Agreement error: "svoje račun" should be "svoj račun".
    - Current: `Zaščitite svoje račun`
    - Source: `Protect your account by using a strong, randomly generated password. It’ll be saved into your account for future use.`
    - Suggest: `Zaščitite svoj račun`
    - "račun" is masculine singular accusative, so the possessive pronoun must be "svoj", not the neuter/plural "svoje".
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Verb gender agreement error: "Dodatki in nekatere možnosti" (masculine + feminine subjects) requires masculine plural "nehali", not feminine "nehale".
    - Current: `Dodatki in nekatere možnosti bodo 14. marca nehale delovati.`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `Dodatki in nekatere možnosti bodo 14. marca nehali delovati.`
    - In Slovenian, with mixed-gender coordinated subjects the participle takes masculine plural form; "nehale" agrees only with the feminine noun.
- `content_description_take_photo` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Missing preposition in "pošlji Google Lens"; the source says "send to Google Lens".
    - Current: `Fotografiraj in pošlji Google Lens`
    - Source: `Take photo and send to Google Lens`
    - Suggest: `Fotografiraj in pošlji v Google Lens`
    - "pošlji Google Lens" lacks the preposition "v"; the parallel string content_description_gallery correctly uses "za pošiljanje v Google Lens".
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Active" tab-count category uses singular masculine "Dejaven" while the sibling categories use plural forms.
    - Current: `Dejaven`
    - Source: `Active`
    - Suggest: `Dejavni`
    - Parallel strings debug_drawer_tab_tools_tab_count_inactive ("Nedejavni") and _private ("Zasebni") use the plural form for the same tab-count category list; "Dejaven" is inconsistent and grammatically mismatched.
- `download_delete_single_item_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Adjective agreement is wrong: the placeholder holds a file name ("datoteka" is not in the string), so "izbrisana" should be neuter/masculine-neutral form.
    - Current: `"%1$s" izbrisana`
    - Source: `Deleted “%1$s”`
    - Suggest: `"%1$s" izbrisano`
    - The source is "Deleted “%1$s”"; %1$s is the download item name, which has no fixed gender, so the feminine form "izbrisana" is unwarranted agreement.
- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Category header is in accusative case instead of nominative.
    - Current: `Znane sledilce prstnih odtisov`
    - Source: `Known Fingerprinters`
    - Suggest: `Znani sledilci prstnih odtisov`
    - "Known Fingerprinters" is a category heading, so it should be nominative plural ("Znani sledilci prstnih odtisov"), not accusative "Znane sledilce".
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Category title uses the accusative case "Morebitne sledilce" instead of the nominative required for a standalone preference title.
    - Current: `Morebitne sledilce prstnih odtisov`
    - Source: `Suspected Fingerprinters`
    - Suggest: `Morebitni sledilci prstnih odtisov`
    - The source "Suspected Fingerprinters" is a heading/preference label; other category titles in the same list use the nominative (e.g. "Sledilci družbenih omrežij").
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Verb agreement error: "da ... obvestimo" should be third person "obvesti", since the subject of the subordinate clause is Mozilla.
    - Current: `da Mozilli dovolite, da kanale, na katerih promoviramo Firefox, obvestimo, da ste vi njegov uporabnik`
    - Source: `You can help us reach more people by allowing Mozilla to inform the channels where we promote Firefox that you’re a Firefox user.`
    - Suggest: `da Mozilli dovolite, da kanale, na katerih promoviramo Firefox, obvesti, da ste njegov uporabnik`
    - Source: "allowing Mozilla to inform the channels ... that you’re a Firefox user" — Mozilla informs, not "we inform"; parallel strings correctly use "obvesti".
- `preference_option_autoplay_allowed_wifi_subtext` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Video" is incorrectly capitalized mid-sentence in Slovenian.
    - Current: `Zvok in Video se bosta predvajala na Wi-Fi`
    - Source: `Audio and video will play on Wi-Fi`
    - Suggest: `Zvok in video se bosta predvajala na Wi-Fi`
    - Slovenian does not capitalize common nouns mid-sentence; the source is "Audio and video" and other strings use lowercase "video".
- `preferences_delete_browsing_data_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Checkbox item in "Delete browsing data" list uses nominative instead of the accusative used by the sibling items.
    - Current: `Prenosi`
    - Source: `Downloads`
    - Suggest: `Prenose`
    - The other items in the same list ("Zgodovino brskanja", "Piškotke in podatke strani", "Dovoljenja strani") are in accusative agreeing with "Izbriši ..."; this one breaks that pattern.
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Verb agrees with feminine gender although %s is the app name (Firefox), which is masculine in Slovenian.
    - Current: `%s je izključena.`
    - Source: `%s is off-duty. We suggest turning protections back on.`
    - Suggest: `%s je izključen.`
    - The developer comment says %s is the app name (e.g. "Firefox"); "izključena" is feminine and wrongly agrees, as if referring to protection rather than the app.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Missing preposition: "Ste samo 1 korak od ciljne črte" lacks the required preposition/case for "1 step away".
    - Current: `Ste samo 1 korak od ciljne črte.`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Ste le še 1 korak od ciljne črte.`
    - The Slovenian sentence as written is ungrammatical/awkward; the source says "You're just 1 step away from the finish line".
- `sports_widget_semi_final` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Semi-finals" is rendered as "Polfinala", the genitive/dual form rather than the plural nominative.
    - Current: `Polfinala`
    - Source: `Semi-finals`
    - Suggest: `Polfinale`
    - The round name label should be nominative; Slovenian standard term for the stage is "Polfinale" (cf. "Osmina finala", "Tretje mesto" which are nominative). "Polfinala" reads as genitive singular/dual.
- `translation_option_bottom_sheet_about_translations` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The placeholder holding the app name is given an inflectional suffix '-u' that produces wrong forms for many app names.
    - Current: `O prevodih v %1$su`
    - Source: `About translations in %1$s`
    - Suggest: `O prevodih v brskalniku %1$s`
    - %1$s is the app name (e.g. Firefox); appending the locative ending directly to the placeholder yields incorrect and unnatural output.
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "ni potrebno" should be "ni treba" in standard Slovenian.
    - Current: `Aplikacije vam ni potrebno niti odpreti`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Aplikacije vam ni treba niti odpreti`
    - With an infinitive the correct impersonal construction is "ni treba"; "ni potrebno" is a well-known non-standard usage.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Plural "custom URLs" translated as singular.
    - Current: `Odstrani URL po meri`
    - Source: `Remove custom URLs`
    - Suggest: `Odstrani URL-je po meri`
    - Source is "Remove custom URLs" (plural, screen for removing multiple URLs); the target is singular.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Adjective agreement error: "Zavrni morebitne nevarne" should be "morebiti nevarne", and the verb form is inconsistent with the other block-preference titles.
    - Current: `Zavrni morebitne nevarne in zavajajoče strani`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `Zavračaj morebitno nevarne in zavajajoče strani`
    - "morebitne nevarne" stacks two adjectives ungrammatically; the intended sense is "potentially dangerous" ("morebiti/morebitno nevarne"). Other Block* titles use the imperfective "Zavračaj".
- `share_dialog_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "preko" with genitive is a non-standard preposition use; standard Slovene is "prek".
    - Current: `Deli preko`
    - Source: `Share via`
    - Suggest: `Deli prek`
    - Slovene style guides prefer "prek"; "Deli preko" is a colloquialism.

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — Imperative "Deli" breaks the noun-phrase pattern used by all other long descriptions in the same list.
    - Current: `Deli tehnične in interakcijske podatke z razvijalcem razširitve`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `deljenje tehničnih podatkov in podatkov o interakcijah z razvijalcem razširitve`
    - Every sibling *_long_description string uses the lowercase gerund form ("deljenje ... z razvijalcem razširitve"); this one uses a capitalized imperative verb, an inconsistency on the same surface.
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — Checkbox label uses imperative "Deli" while the parallel data-collection string uses the nominalized "deljenje", breaking consistency in the same dialog.
    - Current: `Deli tehnične in interakcijske podatke z razvijalcem razširitve`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `Deljenje tehničnih in interakcijskih podatkov z razvijalcem razširitve`
    - The parallel string mozac_feature_addons_permissions_data_collection_websiteContent_long_description ("Share website content with extension developer") is rendered as "deljenje vsebine spletnih strani z razvijalcem razširitve"; the same source pattern in the same dialog should not switch to an imperative verb form.
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — Permission description uses an imperative verb form instead of the nominalized lowercase pattern used by all other permission descriptions.
    - Current: `Prenesite in uporabljajte modele z umetno inteligenco na svoji napravi`
    - Source: `Download and run AI models on your device`
    - Suggest: `prenos in uporaba modelov umetne inteligence na napravi`
    - All sibling permission descriptions (e.g. "dostop do zavihkov brskalnika", "branje in spreminjanje nastavitev zasebnosti") are lowercase nominal phrases describing what the add-on may do; here it is rendered as a command to the user, which also changes the meaning (the extension downloads the models, not the user). The _for_update variant already uses the correct nominal form.
- `mozac_feature_prompts_redirect_dialog_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — "this site" is rendered as "to stran" (page) while the parallel string uses "spletno mesto" for site.
    - Current: `Dovolite preusmeritev na to stran?`
    - Source: `Allow redirect to this site?`
    - Suggest: `Dovolite preusmeritev na to spletno mesto?`
    - The neighbouring string mozac_feature_prompts_popup_dialog_title translates "site" as "spletno mesto"; here "site" is rendered "stran" (page), an inconsistent term on the same surface.
- `mozac_feature_prompts_update_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — Dialog title question uses imperative/1st-person form inconsistent with the parallel address dialog and the formal register.
    - Current: `Posodobi datum poteka veljavnosti kartice?`
    - Source: `Update card expiration date?`
    - Suggest: `Želite posodobiti datum poteka veljavnosti kartice?`
    - Source "Update card expiration date?" is a confirmation question; the sibling strings use "Posodobim naslov?" / "Želite uporabiti močno geslo?". "Posodobi ...?" is an imperative and reads as a command, not a question.
- `mozac_feature_summarize_disclaimer_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — "AI" is rendered as "UI", which in Slovenian means user interface, not artificial intelligence.
    - Current: `UI lahko dela napake`
    - Source: `AI can make mistakes`
    - Suggest: `UI (umetna inteligenca) lahko dela napake`
    - The source "AI" means artificial intelligence; the Slovenian abbreviation "UI" is ambiguous with "uporabniški vmesnik" and elsewhere Mozilla sl uses "UI"/"umetna inteligenca" spelled out; as written it can be read as "user interface can make mistakes".
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — Title is rendered in first person ("Povzamem vsebino") instead of the impersonal/imperative form used in the parallel on-device title.
    - Current: `Povzamem vsebino s tresenjem?`
    - Source: `Summarize with a shake?`
    - Suggest: `Povzetek s stresanjem?`
    - The source "Summarize with a shake?" is impersonal; the sibling string uses "Povzemi to stran" and the feature term elsewhere is "stresanje" (Občutljivost na stresanje), so "tresenjem" is also inconsistent.
- `ai_controls_ai_powered_features` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — AI is abbreviated as "UI" here while other strings in the same surface spell it out as "umetna inteligenca", creating inconsistency.
    - Current: `Funkcije, ki jih poganja UI`
    - Source: `AI-powered features`
    - Suggest: `Funkcije, ki jih poganja umetna inteligenca`
    - Within the same AI controls screen, ai_controls_banner_supporting_text_2 and ai_controls_block_ai_description use "umetna inteligenca" while this and other strings use the abbreviation "UI"; the same source term should be rendered consistently.
- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Imperative "priloži" uses informal command form in a setting title where the formal/neutral register is used elsewhere.
    - Current: `priloži povezavo za prenos %1$sa`
    - Source: `Include %1$s download link on WhatsApp shares`
    - Suggest: `priložite povezavo za prenos %1$sa`
    - The locale convention is the formal register; other user-directed strings in this batch use the formal form (e.g. "Povabite prijatelje…").
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Informal/incorrect "Prosim" plus an inconsistent imperative construction instead of the formal polite request.
    - Current: `Prosim, razmislite o tem, da dovolite in pomagajte Firefoxu, da zmaga.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Prosimo, razmislite o tem, da to dovolite in pomagate Firefoxu do zmage.`
    - Formal register requires "Prosimo"; also "pomagajte" breaks the subordinate clause introduced by "da", which needs "pomagate".
- `nova_onboarding_marketing_primary_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Button uses informal singular imperative "Pomagaj" while the locale convention and neighbouring marketing strings use the formal plural.
    - Current: `Pomagaj Firefoxu`
    - Source: `Help Firefox`
    - Suggest: `Pomagajte Firefoxu`
    - sl convention is formal address; the related title uses "Pomagajte nam ...".
- `onboarding_term_of_service_line_three_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Informal imperative "Upravljaj" breaks the locale's formal register used elsewhere in the same onboarding flow.
    - Current: `Upravljaj`
    - Source: `Manage`
    - Suggest: `Upravljanje`
    - The sl locale uses the formal register (e.g. "Nastavite", "Preberite več", "Zaženite") on this very onboarding screen; a second-person singular informal imperative is inconsistent.
- `preference_doh_exceptions_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "secure DNS" is rendered "varnega DNS" here but "zavarovanega DNS" in the sibling DoH strings.
    - Current: `varnega DNS`
    - Source: `%1$s won’t use secure DNS on these sites and their subdomains.`
    - Suggest: `zavarovanega DNS`
    - The same source term "secure DNS" is translated as "zavarovanega DNS" in preference_doh_default_protection_info_2/_5 and _summary on the same DNS over HTTPS surface; this one is inconsistent.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Imperative form uses informal/second-person singular "sporočaj" instead of the established formal register used elsewhere.
    - Current: `Spletnim mestom sporočaj, naj ne prodajajo ali delijo podatkov`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `Spletnim mestom sporoči, naj ne prodajajo ali delijo podatkov`
    - The locale convention is formal address; "sporočaj" is an informal singular imperative, inconsistent with strings like "Izberite" and "Izolirajte".
- `preferences_ai_controls` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "AI" is rendered as "UI" instead of the Slovenian abbreviation "UI"... reversed word order gives wrong term.
    - Current: `Nadzor UI`
    - Source: `AI controls`
    - Suggest: `Nadzor umetne inteligence`
    - "Nadzor UI" is ambiguous/incorrect in Slovenian (UI also reads as user interface); the settings screen title for AI controls should spell out "umetne inteligence".
- `protection_panel_num_trackers_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Trackers blocked" rendered as "Zavrnjeni sledilci" instead of the consistent "blokirani" used in neighbouring protection-panel strings.
    - Current: `Zavrnjeni sledilci: %d`
    - Source: `Trackers blocked: %d`
    - Suggest: `Blokirani sledilci: %d`
    - Other strings on the same panel translate "blocked" as "blokiran" (e.g. "Sledilci niso blokirani", "je bil blokiran %1$d sledilec"); "zavrnjeni" (rejected) is inconsistent terminology on the same surface.
- `quick_setting_option_autoplay_block_audio` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Block" is rendered as "Zavrni" (deny/reject) instead of "Blokiraj"/"Zavračaj", inconsistent with the "Allow" counterpart and the standard blocking terminology.
    - Current: `Zavrni samo zvok`
    - Source: `Block audio only`
    - Suggest: `Blokiraj samo zvok`
    - Source "Block audio only" refers to blocking autoplay; "zavrni" means to deny/reject a request, not block content.
- `quick_setting_option_autoplay_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Block audio and video" translated as "Zavrni zvok in video" instead of using the blocking term.
    - Current: `Zavrni zvok in video`
    - Source: `Block audio and video`
    - Suggest: `Blokiraj zvok in video`
    - Source uses "Block"; Slovenian "zavrni" means deny/reject, not block.
- `setup_checklist_task_explore_extensions` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Imperative form is inconsistent with the other setup checklist task titles, which use the formal plural.
    - Current: `Razišči razširitve`
    - Source: `Explore extensions`
    - Suggest: `Raziščite razširitve`
    - Sibling task titles use the formal address ("Raziščite pripomoček za iskanje", "Izberite temo", "Prijavite se v račun"); the sl convention is formal.
- `sports_widget_follow_another_team` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Button label uses the informal imperative singular instead of the established formal address.
    - Current: `Spremljaj drugo ekipo`
    - Source: `Follow another team`
    - Suggest: `Spremljajte drugo ekipo`
    - The locale convention is formal address (e.g. "Pridobite ozadje po meri", "Poskusite osvežiti"); "Spremljaj" is the informal second-person singular imperative.
- `sports_widget_go_to_world_cup_site_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Content description uses the informal imperative singular instead of the established formal address.
    - Current: `Obišči spletno stran svetovnega prvenstva`
    - Source: `Go to World Cup site`
    - Suggest: `Obiščite spletno stran svetovnega prvenstva`
    - The locale convention is formal address; "Obišči" is the informal second-person singular imperative, inconsistent with other formal strings in this batch.
- `studies_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "feature studies" is translated as "raziskave značilnosti" instead of the established term for features (funkcije).
    - Current: `Dovoli raziskave značilnosti`
    - Source: `Allow feature studies`
    - Suggest: `Dovoli raziskave funkcij`
    - "Features" in Mozilla sl is rendered as "funkcije"; "značilnosti" is a different concept (characteristics).
- `external_multiple_apps_matched_exit` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — First-person verb form used instead of the neutral/impersonal question typical for dialog prompts in the formal register.
    - Current: `Končam zasebno brskanje?`
    - Source: `Exit Private Browsing?`
    - Suggest: `Želite končati zasebno brskanje?`
    - The locale uses the formal register; "Končam" is a first-person informal-style rendering, inconsistent with the source's neutral "Exit Private Browsing?".
- `preference_privacy_secure_mode` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Stealth" is translated as "Skrivni način" (secret mode) rather than a stealth/hidden-mode term matching the feature name.
    - Current: `Skrivni način`
    - Source: `Stealth`
    - Suggest: `Prikrit način`
    - The developer comment describes Stealth mode as hiding app content; "skrivni" (secret) suggests private browsing, which is a different Focus concept.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Top sites" is translated as "glavne strani", inconsistent with the top-site strings elsewhere in the file.
    - Current: `Za glavne strani`
    - Source: `For top sites`
    - Suggest: `Za glavne strani (priljubljene strani)`
    - Terminology for "top sites" should be consistent across the Top Sites section (remove_top_site/rename_top_site context).
- `social` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Tracker category "Social" is rendered with the masculine adjective "Družbeni" instead of the established category noun.
    - Current: `Družbeni`
    - Source: `Social`
    - Suggest: `Družbena omrežja`
    - This is a tracker category label; "Družbeni" alone is an incomplete adjective with no noun and does not name the category the way other categories do.

### E. Typography, punctuation & spacing

- `mozac_browser_engine_system_auth_message` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-sl/strings.xml` — Curly typographic quotes used instead of the locale's straight double quotes.
    - Current: `“%1$s”`
    - Source: `%2$s is requesting your username and password. The site says: “%1$s”`
    - Suggest: `"%1$s"`
    - The sl convention is straight-double quotes; the string keeps the English curly quotes.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — Curly/typographic double quotes used where the locale convention is straight double quotes.
    - Current: `Pritisnite “Poskusi znova” za preklop`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Pritisnite "Poskusi znova" za preklop`
    - The sl convention is straight-double quotes; the source uses “Try Again” but the locale's house style is straight doubles.
- `mozac_feature_applinks_open_in` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-sl/strings.xml` — Space inserted before the ellipsis character.
    - Current: `Odpri v …`
    - Source: `Open in…`
    - Suggest: `Odpri v…`
    - The source "Open in…" has no space before the ellipsis; Slovenian localization convention here uses the ellipsis character attached directly to the preceding word.
- `mozac_summarize_settings_shake_sensitivity_description` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — Superfluous comma before the prepositional phrase "za povzetek".
    - Current: `Prilagodite, kako močno morate stresati, za povzetek.`
    - Source: `Adjust how hard you need to shake to trigger summarization.`
    - Suggest: `Prilagodite, kako močno morate stresati za povzetek.`
    - In Slovenian no comma separates the verb from its purpose phrase; the comma breaks the sentence incorrectly.
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Quotation marks are reversed/incorrect; the locale convention is straight double quotes.
    - Current: `”vedno prevedi“ in ”nikoli ne prevajaj“`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `"vedno prevedi" in "nikoli ne prevajaj"`
    - The translation uses closing curly quote before and opening-style low quote after, which is neither correct Slovenian quoting nor the established straight-double convention.
- `delete_all_history_group_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Slovenian quotation marks are wrong; straight double quotes used where Slovenian typographic quotes (or at least the source's curly quotes) are expected.
    - Current: `"%s"`
    - Source: `Delete all sites in “%s”`
    - Suggest: `„%s“`
    - The source uses typographic quotes “%s”; the sl target uses straight ASCII quotes, deviating from Slovenian quoting conventions.
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — English-style opening quotation mark used instead of the locale's straight double quotes.
    - Current: `Zaznamki shranjeni v “%s”`
    - Source: `Bookmarks saved in “%s”`
    - Suggest: `Zaznamki shranjeni v "%s"`
    - The sl convention is straight double quotes; the target uses English curly quotes “ ” with the opening mark in the English position.
- `sports_widget_error_connection_interrupted` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Em dash used where the locale's house dash is the en dash.
    - Current: `Povezava prekinjena — posodobitve`
    - Source: `Connection interrupted — live updates paused.`
    - Suggest: `Povezava prekinjena – posodobitve`
    - The sl convention for dashes is the en dash; the source em dash should be adapted.
- `toast_customize_extension_collection_done` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Space before ellipsis is inconsistent with the other translated strings in this batch that use a normal space-free ellipsis placement.
    - Current: `Zapiranje aplikacije za uveljavitev sprememb …`
    - Source: `Extension collection modified. Quitting the application to apply changes…`
    - Suggest: `Zapiranje aplikacije za uveljavitev sprememb…`
    - Source ends with '…' directly attached; other strings such as 'Prevajanje …' show the locale style, but a stray space before the ellipsis after a full clause deviates from the source typography.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Curly quotes in the source are rendered as straight double quotes but the app name placeholder is also declined with an appended suffix; the quoting style should match the house straight-double convention consistently.
    - Current: `"Dodaj na domač zaslon"`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `"Dodaj na domači zaslon"`
    - The quoted menu item must match the actual menu string menu_add_to_home_screen; also, the adjective form should be consistent with that item's wording.
- `menu_share` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Space inserted before the ellipsis character.
    - Current: `Deli …`
    - Source: `Share…`
    - Suggest: `Deli…`
    - The source "Share…" has no space before the ellipsis; Slovenian typography also attaches the ellipsis directly to the word.
- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Uses straight double quotes where the source has none and Slovenian typography would use „ “ or none at all.
    - Current: `Način "samo HTTPS"`
    - Source: `HTTPS-Only Mode`
    - Suggest: `Način samo HTTPS`
    - The source title "HTTPS-Only Mode" contains no quotation marks; the added quotes are gratuitous.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
