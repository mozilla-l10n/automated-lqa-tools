# Firefox for Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **Previous run** | 2026-11-08 @ `c1a76afc1b60` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,542 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,542 |
| Missing strings | 59 |
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

**59 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — 42
- `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — 7
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — 5
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-sl/strings.xml` — 4
- `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-sl/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 17, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 5 | **en** |
| register | `informal` 4, `formal` 90 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (43)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 27 |
| 3 | Degraded language (grammar, spelling, terminology) | 14 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — Second bullet limits the spelling check to the file name instead of the address as in the source.
    - Current: `Je njeno ime napačno črkovano`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `Je v naslovu napaka v črkovanju`
    - Source asks about a typographical error in the address, not in the item's name.
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
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Debug locales to enable" is rendered as "Jeziki" (languages), losing both "debug" and the locale concept.
    - Current: `Jeziki, ki naj bodo omogočeni`
    - Source: `Debug locales to enable`
    - Suggest: `Razhroščevalne območne nastavitve, ki naj bodo omogočene`
    - The source refers to debug locales, not languages; elsewhere in the same feature (debug_drawer_add_new_address) "locale" is translated as "območna nastavitev".
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
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "translation menu" rendered as "meni prevajalnika" (translator's menu).
    - Current: `v meniju prevajalnika`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `v meniju za prevajanje`
    - The source says "the translation menu"; "prevajalnik" names a translator tool rather than the translation menu.
- `notification_privacy_report_body_has_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Translation adds "sledilce" (trackers), a specific object the source does not state.
    - Current: `Brskajte dalje, %1$s pa bo še naprej blokiral sledilce.`
    - Source: `Keep browsing. %1$s will keep blocking.`
    - Suggest: `Brskajte dalje, %1$s pa bo še naprej blokiral.`
    - Source is "Keep browsing. %1$s will keep blocking." with no explicit object; the sentence structure and content were changed.
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "Cross-site cookies" is translated as "Spletni piškotki" (web cookies), losing the cross-site meaning.
    - Current: `Spletni piškotki`
    - Source: `Cross-site cookies`
    - Suggest: `Piškotki drugih strani`
    - The source refers specifically to cross-site cookies; the translation says merely "web cookies", which is a different, broader concept.
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
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Content description drops "sheet", saying "Close Translations" instead of "Close Translations sheet".
    - Current: `Zaprite Prevode`
    - Source: `Close Translations sheet`
    - Suggest: `Zaprite list Prevajanje`
    - The source describes closing the translations bottom sheet; the target omits the "sheet" element and reads as closing the translations themselves.

### C. Grammar, agreement & spelling

- `download_delete_single_item_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Adjective agreement is wrong: the placeholder holds a file name ("datoteka" is not in the string), so "izbrisana" should be neuter/masculine-neutral form.
    - Current: `"%1$s" izbrisana`
    - Source: `Deleted “%1$s”`
    - Suggest: `"%1$s" izbrisano`
    - The source is "Deleted “%1$s”"; %1$s is the download item name, which has no fixed gender, so the feminine form "izbrisana" is unwarranted agreement.
- `preferences_delete_browsing_data_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Checkbox item in "Delete browsing data" list uses nominative instead of the accusative used by the sibling items.
    - Current: `Prenosi`
    - Source: `Downloads`
    - Suggest: `Prenose`
    - The other items in the same list ("Zgodovino brskanja", "Piškotke in podatke strani", "Dovoljenja strani") are in accusative agreeing with "Izbriši ..."; this one breaks that pattern.
- `translation_option_bottom_sheet_about_translations` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — The placeholder holding the app name is given an inflectional suffix '-u' that produces wrong forms for many app names.
    - Current: `O prevodih v %1$su`
    - Source: `About translations in %1$s`
    - Suggest: `O prevodih v brskalniku %1$s`
    - %1$s is the app name (e.g. Firefox); appending the locative ending directly to the placeholder yields incorrect and unnatural output.

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
- `nova_onboarding_marketing_primary_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — Button uses informal singular imperative "Pomagaj" while the locale convention and neighbouring marketing strings use the formal plural.
    - Current: `Pomagaj Firefoxu`
    - Source: `Help Firefox`
    - Suggest: `Pomagajte Firefoxu`
    - sl convention is formal address; the related title uses "Pomagajte nam ...".
- `preferences_ai_controls` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "AI" is rendered as "UI" instead of the Slovenian abbreviation "UI"... reversed word order gives wrong term.
    - Current: `Nadzor UI`
    - Source: `AI controls`
    - Suggest: `Nadzor umetne inteligence`
    - "Nadzor UI" is ambiguous/incorrect in Slovenian (UI also reads as user interface); the settings screen title for AI controls should spell out "umetne inteligence".
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
- `studies_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — "feature studies" is translated as "raziskave značilnosti" instead of the established term for features (funkcije).
    - Current: `Dovoli raziskave značilnosti`
    - Source: `Allow feature studies`
    - Suggest: `Dovoli raziskave funkcij`
    - "Features" in Mozilla sl is rendered as "funkcije"; "značilnosti" is a different concept (characteristics).

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

---

## 4. Appendix

### Dismissed by hand (18)

- `delete_all_history_group_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Straight double quotes are the measured majority convention in the sl tree (14–15 straight vs 4 curly).
- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Glede na kontekst je prav, da je v rodilniku.</p>
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear
- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Slovenian UI labels and toggles conventionally use the 2nd-person singular imperative (e.g. "Shrani", "Prikaži"), which is not a register violation.
- `mozac_feature_applinks_open_in` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Slovenian orthography (SP) separates the ellipsis by a space after a complete word indicating omission, e.g. "Odpri v …", a standard Slovenian Mozilla convention.
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Each link keeps its correct placeholder (%3$s privacy policy, %4$s terms), so reordering the two items is a valid stylistic choice with no functional or semantic change.
- `mozac_feature_summarize_disclaimer_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): "UI" is the standard Slovenian abbreviation for "umetna inteligenca"; user interface is not abbreviated UI in Slovenian.
- `onboarding_term_of_service_line_three_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Slovenian UI command labels (buttons/links) normally use the singular imperative (e.g. 'Shrani', 'Prekliči'), independent of the formal register used in prose.
- `open_all_warning_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): 'več zavihkov (%d)' is a standard way to avoid plural forms; here 'več' means 'multiple' and the exact count still shows through %d.
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Razumem, zakaj je bot reagiral na ta niz, ampak če se prebere kot "ohranjevalnik baterije nastavi to nastavitev", je pravilen in slogovno boljši.</p>
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Glede na kontekst je v redu, da je mala začetnica. Slovenski pravopis ima malo drugačna pravila za alinejno naštevanje kot angleški. Bodisi morajo biti male začetnice, bodisi mora biti na koncu vsake alineje končno ločilo.</p>
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Setting labels in sl use this imperative form (cf. "Omogoči"), and the suggested "sporoči" is the same 2nd-person singular, so there is no register mismatch.
- `preferences_enable_gecko_logs` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Gecko is Mozilla's rendering engine, so "izrisovalnika Gecko" is an accurate descriptor that also allows correct declension of the brand name.
- `search_add_custom_engine_error_missing_template` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): 'Prepričajte se, da se iskalni niz ujema z obliko primera' accurately conveys 'Check that search string matches Example format'.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): "Ste samo 1 korak od ciljne črte" is grammatical Slovenian; no preposition is missing, the suggestion is only stylistic.
- `sync_failed_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): "Nazadnje sinhronizirano" after a failure message conveys the last successful sync, equivalent to the source.
- `toast_customize_extension_collection_done` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03): Slovenian orthography puts a space before an ellipsis following a complete word, as the tree does elsewhere ("Prevajanje …").
- `webcompat_reporter_clear_reason_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (38)

- `mozac_browser_errorpages_harmful_addon_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_redirect_dialog_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_feature_prompts_update_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `mozac_summarize_settings_shake_sensitivity_description` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `sound_off` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `content_description_take_photo` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `etp_cookies_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `microsurvey_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `nova_onboarding_tou_body_line_3_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_doh_exceptions_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_option_autoplay_allowed_wifi_subtext` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preferences_search_browsing_history` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `setup_checklist_subtitle_5_steps_third_step` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `setup_checklist_task_explore_extensions` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `synced_tabs_no_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `tab_tray_inactive_onboarding_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `translations_bottom_sheet_info_message` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `sync_send_tab_error_auth_remove_account` — `mozilla-mobile/fenix/app/src/main/res/values-sl/strings.xml` — fixed 2026-09-10
