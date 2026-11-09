# Firefox for Android l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `f7a886b5b048` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| quotes | `curly-single` 15 | **curly-single** |
| apostrophe | `typographic` 46 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |
| register | `formal` 435 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (31)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 20 |
| 3 | Degraded language (grammar, spelling, terminology) | 11 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `sent_from_firefox_template_short` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The blank line separating the shared link from the footer is missing in the translation.
    - Current: `%1$s Verzonden vanuit %2$s 🦊 %3$s`
    - Source: `%1$s  Sent from %2$s 🦊 %3$s`
    - Suggest: `%1$s  Verzonden vanuit %2$s 🦊 %3$s`
    - The source has an empty line between %1$s and the footer, matching the long template; the Dutch short template drops it, changing the shared message layout.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — "Try again in a few moments" is rendered as "over een paar seconden" (a few seconds).
    - Current: `Probeer het over een paar seconden opnieuw.`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `Probeer het over enkele ogenblikken opnieuw.`
    - The source says "in a few moments", not "in a few seconds"; other strings in the same file use "enkele ogenblikken".
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — "Is your device or network protected..." is translated as "uw computer".
    - Current: `Wordt uw computer of netwerk beschermd door een firewall of proxy?`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Wordt uw apparaat of netwerk beschermd door een firewall of proxy?`
    - Source says "Is your device or network protected by a firewall or proxy?" — device, not computer.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — “Press” rendered as “Klik” (click) on a touch device.
    - Current: `Klik op ‘Opnieuw proberen’`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Tik op ‘Opnieuw proberen’`
    - Source says “Press “Try Again””; on a mobile browser the action is tapping/pressing, not clicking.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — “your device” translated as “uw computer”.
    - Current: `niet met uw computer`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `niet met uw apparaat`
    - Source: “not your device”; the Dutch names a computer instead of the device.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — “device” translated as “computer”.
    - Current: `Is de computer verbonden met een actief netwerk?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Is het apparaat verbonden met een actief netwerk?`
    - Source: “Is the device connected to an active network?”; “computer” is the wrong referent on Android.
- `mozac_menu_customize_reset_to_default` — `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-nl/strings.xml` — Button label drops the action 'reset' and reads only as 'Default values'.
    - Current: `Standaardwaarden`
    - Source: `Reset to default`
    - Suggest: `Standaardwaarden herstellen`
    - Source 'Reset to default' is a button that resets the menu configuration; 'Standaardwaarden' is just a noun ('default values') and does not convey the reset action.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "custom tab" is mistranslated as "Tabblad aanpassen" (customize tab) instead of the noun "aangepast tabblad".
    - Current: `Menublad Tabblad aanpassen sluiten`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublad van aangepast tabblad sluiten`
    - The source refers to the menu sheet of a custom tab (aangepast tabblad), not to an action of customizing a tab.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Never" is translated as "Handmatig" (Manually) instead of "Nooit".
    - Current: `Handmatig`
    - Source: `Never`
    - Suggest: `Nooit`
    - The source option label is "Never"; the summary string separately renders "Close manually". Rendering the option itself as "Handmatig" changes the displayed content.
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Neutral" is rendered as "Gemiddeld" (average) instead of the neutral midpoint term.
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
    - The likert midpoint "Neutral" means neither satisfied nor dissatisfied; "Gemiddeld" means "average", a different concept.
- `microsurvey_homepage_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Translation adds "ervaring" (experience), which is not in the source.
    - Current: `Hoe tevreden bent u met uw Firefox Startpagina-ervaring?`
    - Source: `How satisfied are you with your Firefox homepage?`
    - Suggest: `Hoe tevreden bent u met uw Firefox-startpagina?`
    - Source: "How satisfied are you with your Firefox homepage?" — no "experience"; also "Startpagina" is wrongly capitalised mid-compound.
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The translation drops "search", making the string about Firefox in general rather than search in Firefox.
    - Current: `Help Firefox te verbeteren. Het duurt maar een minuutje`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `Help zoeken in Firefox te verbeteren. Het duurt maar een minuutje`
    - Source is "Help make search in Firefox better"; the parallel sync/printing strings do keep the feature name.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "marketing partners" is rendered as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `Mozilla’s marketingtechnologiepartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "technology" is not mentioned.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "marketing partners" is rendered as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `Mozilla’s marketingtechnologiepartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - The source says "Mozilla’s marketing partners"; "technology" is not mentioned.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "marketing partners" is rendered as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `Mozilla’s marketingtechnologiepartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - Source says "Mozilla’s marketing partners", not "marketing technology partners".
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "marketing partners" is rendered as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `Mozilla’s marketingtechnologiepartners`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Mozilla’s marketingpartners`
    - Source says "Mozilla’s marketing partners", not "marketing technology partners".
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Brand name "Firefox Suggest" translated as "Firefox Suggesties".
    - Current: `Firefox Suggesties`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must not be translated.
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Brand name "Firefox Suggest" translated as "Firefox Suggesties".
    - Current: `Firefox Suggesties`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must not be translated.
- `translation_option_bottom_sheet_switch_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Overrides offers to translate" is rendered as "Negeert" (ignores) instead of "overschrijft" (overrides), inconsistent with the sibling string.
    - Current: `Negeert vertaalaanbiedingen`
    - Source: `Overrides offers to translate`
    - Suggest: `Overschrijft aanbiedingen om te vertalen`
    - The source means the setting takes precedence over the offer-to-translate setting; the parallel string translation_option_bottom_sheet_switch_never_translate_site_description uses "Overschrijft". "Negeert" means "ignores", a different meaning.
- `uninstall_survey_error_failed` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "system uninstall prompt" mistranslated as prompt for uninstalling the system.
    - Current: `Het openen van de prompt voor het de-installeren van het systeem is mislukt`
    - Source: `Failed to open the system uninstall prompt, please use the system uninstall action directly.`
    - Suggest: `Het openen van de de-installatieprompt van het systeem is mislukt`
    - The source means the system's uninstall prompt (for the app), not a prompt to uninstall the system.
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "or" translated as "en", changing the meaning of the survey option.
    - Current: `De browser is traag en onbetrouwbaar`
    - Source: `It’s slow or unreliable`
    - Suggest: `De browser is traag of onbetrouwbaar`
    - Source is "It’s slow or unreliable" — a disjunction, not a conjunction.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — Untranslated English article "the" left in the Dutch sentence before "Internet Archive".
    - Current: `vanuit %2$s van the Internet Archive`
    - Source: `%1$s can look for an earlier version of this page from the Internet Archive’s %2$s.`
    - Suggest: `vanuit %2$s van het Internet Archive`
    - The source reads "the Internet Archive’s %2$s"; the Dutch keeps the English article "the" instead of the Dutch "het", which is a grammar/spelling error.
- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — Missing hyphen makes "de gegevens of Wi-Fi-verbinding" ungrammatical compared with the parallel strings.
    - Current: `controleer dan de gegevens of Wi-Fi-verbinding van uw apparaat`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `controleer dan de gegevens- of Wi-Fi-verbinding van uw apparaat`
    - Source "check your device’s data or Wi-Fi connection" requires the elided compound hyphen ("gegevens-"), as done correctly in mozac_browser_errorpages_net_reset_message.
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — Missing subject pronoun 'u' in the relative clause.
    - Current: `De pagina die probeert te bekijken kan niet worden getoond`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `De pagina die u probeert te bekijken kan niet worden getoond`
    - Source: “The page you are trying to view”. The Dutch omits “u”, making the sentence ungrammatical; the parallel string mozac_browser_errorpages_security_ssl_message correctly has “De pagina die u wilt bekijken”.
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-nl/strings.xml` — Missing preposition "om" makes the sentence ungrammatical and inconsistent with the parallel string.
    - Current: `%1$s vraagt aanvullende instellingen`
    - Source: `%1$s requests additional settings`
    - Suggest: `%1$s vraagt om aanvullende instellingen`
    - Dutch "vragen" requires "om" here; the parallel string mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title correctly uses "vraagt om aanvullende gegevensverzameling".
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Sentence is ungrammatical: missing subject/verb agreement for "One tap helps stop…".
    - Current: `Met één tik voorkomen dat bedrijven uw tikken bespioneren.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Met één tik voorkomt u dat bedrijven uw klikken bespioneren.`
    - The Dutch clause has no subject; "Met één tik voorkomen dat…" is not a well-formed sentence, unlike the source "One tap helps stop companies spying on your clicks."
- `search_bar_with_lens_widget_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Without hyphens marking the shared compound part, 'afbeelding' reads as a separate noun, so the text says 'search bar with an image' rather than 'with image search'.
    - Current: `met afbeelding, privé en gesproken zoekopdrachten`
    - Source: `Search bar with image, private and voice search`
    - Suggest: `met afbeeldings-, privé- en gesproken zoekopdrachten`
    - The source lists three search types (image, private, voice). In Dutch, compound parts that share a head noun need a hyphen ('afbeeldingszoekopdrachten' becomes 'afbeeldings-'). Without it, 'afbeelding' reads as a separate item in the list, so the description names an image rather than image search.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Subject mismatch: "Door dit te verzenden, helpt het ons" is ungrammatical and inconsistent with the plural variant.
    - Current: `Door dit te verzenden, helpt het ons %1$s te verbeteren.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Als u dit verzendt, helpt u ons %1$s te verbeteren.`
    - Source: "Sending it will help us improve %1$s." The Dutch mixes an implicit subject with "het"; the parallel plural string correctly uses "Als u deze verzendt, helpt u ons…".

### D. Terminology, register & consistency

- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-nl/strings.xml` — English word “issue” left untranslated where Dutch “probleem” is the established term.
    - Current: `Het issue ligt waarschijnlijk bij de website`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `Het probleem ligt waarschijnlijk bij de website`
    - Source “The issue is most likely with the website”; the same string translates “problem” as “probleem”, so “issue” is an inconsistent anglicism.
- `mozac_feature_addons_author` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-nl/strings.xml` — "Author" of an add-on is rendered as "Schrijver" (writer of texts) instead of the established "Auteur"/"Ontwikkelaar".
    - Current: `Schrijver`
    - Source: `Author`
    - Suggest: `Auteur`
    - The developer comment says this is the author (developer) of an add-on; Dutch "Schrijver" refers to a writer of text and is the wrong term in a software context.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Shortcuts" (home screen tiles) is translated as "sneltoetsen" (keyboard shortcuts) instead of "snelkoppelingen".
    - Current: `Alle sneltoetsen tonen`
    - Source: `Show all shortcuts`
    - Suggest: `Alle snelkoppelingen tonen`
    - The related string homepage_shortcuts_add_shortcut uses "Snelkoppeling"; "sneltoetsen" means keyboard shortcuts, which is the wrong concept for home screen shortcut tiles.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (26)

- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate; 'bladeren' is the standard nl verb for browsing.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate; it is an understandable way to say 'go back'.
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 7b175ac5): unreliable finding: Dutch commonly uses the present tense for future events, and 'werken niet meer op 14 maart' acceptably says they stop working on that date; the suggested wording is a style preference.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 1b25438a): unreliable finding: 'Toestemming' is a common and correct Dutch rendering of 'permission'; nothing confirms that 'machtiging' is the required term here.
- `content_description_settings_search_navigate_back` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is used consistently across all the back-button strings in this locale, so it looks deliberate rather than wrong.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent, understandable nl rendering used for every Navigate back control; changing it is a terminology preference.
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string a8e8d8c8): unreliable finding: The meaning (a mask was picked to reuse) is fully conveyed; adding "voor u" is stylistic.
- `etp_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent, understandable nl rendering used across back buttons; the change is preference.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string cd436654): unreliable finding: "Doorleiding" is a valid Dutch noun and the claimed wording of the description string cannot be verified here.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 6de0e127): unreliable finding: Whether nl keeps Firefox Suggest untranslated in this header cannot be confirmed; the descriptive rendering is plausible.
- `ip_protection_locations_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent nl wording for back controls and is understandable; the change is preference.
- `ip_protection_mozilla_vpn_upsell_button` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 378950f8): unreliable finding: Rendering "Get" as "downloaden" is a common, acceptable choice for app/product CTAs.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: "Terug bladeren" is the consistent nl wording for back controls and is understandable; the change is preference.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 43f8856f): unreliable finding: "ontvang tot %1$s onbeperkte bandbreedte" naturally reads as "until <date>" in Dutch; "tot en met" is a nuance.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is an understandable label for a back control, so replacing it is a matter of style.
- `mozac_feature_sitepermissions_local_network_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 1e41d011): unreliable finding: The word order is somewhat loose but most readers will understand that access is to apps and services on those devices; a rewrite would be stylistic and would require moving text across the placeholder.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string cab6f8dc): unreliable finding: In Dutch, 'trots' can modify an adjective adverbially ('trots onafhankelijk'), and the phrase is idiomatic.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string d5b26c23): unreliable finding: In Fenix 'past explorations' are search-based history groups, so 'eerdere zoekopdrachten' is a plausible deliberate rendering.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string f6c6455c): unreliable finding: The source is itself ambiguous and the Dutch is an acceptable content description for the sort menu control.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 130d77d2): unreliable finding: 'Google doorzoeken' style phrasing is common, acceptable Dutch for searching with an engine.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string 18dc2611): unreliable finding: 'essentials' may be an intentional loanword in this feature title; the proposed Dutch term is a guess.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string e6ea73b4): unreliable finding: 'Terug bladeren' is idiomatic for going back in a stories carousel and is not a mistranslation.
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string be64e7e2): unreliable finding: The sibling strings can't be checked, and the current word order is correct Dutch.
- `terms_of_use_prompt_body_line_two_alternative` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — auto-suggest (2026-11-09, string ca395ba5): With %1$s being the link text 'hier', the sentence reads 'U vindt hier meer info.', which is grammatical, natural Dutch matching the source.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/nl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (4)

- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-09
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-09
- `tab_tray_close_tabs_banner_positive_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-08
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — fixed 2026-11-05
