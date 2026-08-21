# Android l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **Previous run** | 2026-08-21 @ `7134a6c77a67` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [firefox](firefox.md)

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
| Strings | 2,908 |
| Missing strings | 3 |
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

**3 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — 3

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 16 | **curly-single** |
| apostrophe | `typographic` 51 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 7 | **en** |
| register | `formal` 445 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (68)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 36 |
| 3 | Degraded language (grammar, spelling, terminology) | 32 |
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
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren", which means "browse back" rather than navigating back.
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - The content description describes a back navigation button; "bladeren" means browsing/leafing through, not navigating. Standard Dutch Mozilla wording is "Terugnavigeren" or "Teruggaan".
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "custom tab" is mistranslated as "Tabblad aanpassen" (customize tab) instead of the noun "aangepast tabblad".
    - Current: `Menublad Tabblad aanpassen sluiten`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublad van aangepast tabblad sluiten`
    - The source refers to the menu sheet of a custom tab (aangepast tabblad), not to an action of customizing a tab.
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The Dutch says features stop working "on 14 March" as a completed statement but places the time adverbial ambiguously, changing "will stop working on March 14" into "work no longer on 14 March".
    - Current: `Add-ons en sommige functies werken niet meer op 14 maart.`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `Add-ons en sommige functies werken vanaf 14 maart niet meer.`
    - Source is a future warning: they will stop working on March 14. "werken niet meer op 14 maart" reads as a present-tense statement and misplaces the date; "vanaf 14 maart niet meer" conveys the intended meaning.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Never" is translated as "Handmatig" (Manually) instead of "Nooit".
    - Current: `Handmatig`
    - Source: `Never`
    - Suggest: `Nooit`
    - The source option label is "Never"; the summary string separately renders "Close manually". Rendering the option itself as "Handmatig" changes the displayed content.
- `content_description_settings_search_navigate_back` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate Back" is rendered as "Terug bladeren" (page through backwards) instead of "Terug"/"Terug navigeren".
    - Current: `Terug bladeren`
    - Source: `Navigate Back`
    - Suggest: `Terug navigeren`
    - The button navigates back to the Settings page; "bladeren" means browsing/leafing through, not navigating back. Mozilla nl uses "Terug" / "Terug navigeren".
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren" (browse back / leaf through), which is not the meaning of navigating back.
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terug navigeren`
    - The content description describes a back button; Dutch Firefox uses ‘Terug navigeren’ / ‘Terug’. ‘Terug bladeren’ means paging/leafing backwards and misdescribes the control for screen-reader users.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren" (browse back) instead of the standard "Terugnavigeren"/"Terug".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - The source means navigating back within the debug drawer; "bladeren" means browsing/leafing through and is not the term used for navigation elsewhere in the product.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren" (browse back) instead of the standard "Terug"/"Terugnavigeren".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terug navigeren`
    - The source is a content description for the back button; "bladeren" means browsing/leafing, not navigating back, and is inconsistent with "Naar Downloadinstellingen navigeren" used for the sibling button.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren" (page/leaf through backwards) instead of "Terugnavigeren"/"Terug".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - The source means navigating back (going back a screen); "bladeren" means browsing/leafing through and misdescribes the control for screen-reader users.
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "we picked one for you to reuse" is translated as "we hebben er één uitgekozen om opnieuw te gebruiken", dropping the "for you".
    - Current: `dus we hebben er één uitgekozen om opnieuw te gebruiken`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `dus we hebben er één voor u uitgekozen om opnieuw te gebruiken`
    - The source says the app picked a mask for the user to reuse; the omission of "voor u" loses part of the meaning.
- `etp_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren" instead of "Terugnavigeren"/"Terug".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - The source means navigating back from the ETP detail screen; "bladeren" (leaf through/browse) is not the meaning of "navigate".
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The product name "Firefox Suggest" is translated instead of kept as a brand name.
    - Current: `Firefox Suggesties`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a Mozilla feature/product name that stays untranslated per brand conventions.
- `ip_protection_mozilla_vpn_upsell_button` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Get Mozilla VPN" is translated as "Mozilla VPN downloaden" (download), adding a meaning not in the source.
    - Current: `Mozilla VPN downloaden`
    - Source: `Get Mozilla VPN`
    - Suggest: `Mozilla VPN aanschaffen`
    - The button takes the user to get the standalone paid product; "downloaden" states a specific action (download) not implied by "Get".
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren", which means "browse back" rather than "go back".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terug`
    - The back button content description should say "Terug" (or "Teruggaan"); "bladeren" means to browse/leaf through and is the wrong verb for navigation in Mozilla nl, which uses "Terug" for back buttons.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "unlimited bandwidth through %1$s" (a date) is translated as "tot %1$s onbeperkte bandbreedte" with the amount phrasing reversed/ambiguous.
    - Current: `Probeer het nu en ontvang tot %1$s onbeperkte bandbreedte.`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `Probeer het nu en ontvang onbeperkte bandbreedte tot en met %1$s.`
    - %1$s is an end date; "tot %1$s onbeperkte bandbreedte" reads as a quantity limit rather than "through <date>", and "tot en met" correctly renders "through".
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Neutral" is rendered as "Gemiddeld" (average) instead of the neutral midpoint term.
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
    - The likert midpoint "Neutral" means neither satisfied nor dissatisfied; "Gemiddeld" means "average", a different concept.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is translated as "Terug bladeren" (page/scroll back) instead of navigating back.
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - "Bladeren" means browsing/leafing through; the control returns to the previous screen, and the parallel string logins_navigate_back_button_content_description uses "Terug".
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
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "past explorations" (browsing history) is rendered as "zoekopdrachten" (search queries).
    - Current: `Alle eerdere zoekopdrachten tonen`
    - Source: `Show all past explorations`
    - Suggest: `Alle eerdere verkenningen tonen`
    - The developer comment says the button navigates the user to their history; the source says "explorations", not searches.
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
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Sort passwords menu" is rendered as "Wachtwoordmenu sorteren" (sort the password menu), reversing the meaning.
    - Current: `Wachtwoordmenu sorteren`
    - Source: `Sort passwords menu`
    - Suggest: `Menu Wachtwoorden sorteren`
    - The source names a menu for sorting passwords; the Dutch reads as a command to sort a password menu.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Search %s" (search using engine %s) is rendered as "%s doorzoeken" (search through %s).
    - Current: `%s doorzoeken`
    - Source: `Search %s`
    - Suggest: `Zoeken met %s`
    - The developer comment says %s is the name of the suggested search engine; the string means to search using that engine, not to search inside it.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "essentials" is left untranslated in the Dutch group title.
    - Current: `%1$s-essentials`
    - Source: `%1$s essentials`
    - Suggest: `%1$s-basisinstellingen`
    - Only the app name %1$s is a brand; the common noun "essentials" should be translated into Dutch.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is translated as "Terug bladeren" (page/browse back) instead of "Terug"/"Terugnavigeren".
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terug`
    - 'Bladeren' means browsing/paging; the control is a back navigation button, and elsewhere Mozilla nl uses 'Terug' or 'Terugnavigeren'.
- `tab_tray_close_tabs_banner_positive_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "View options" (view the settings/options) is translated as "Beeldopties" (display options).
    - Current: `Beeldopties`
    - Source: `View options`
    - Suggest: `Opties bekijken`
    - Per the developer comment the button goes to Settings for auto close tabs; "View" is a verb here, not "display/beeld".
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Word order makes "Gesynchroniseerde open tabbladen" inconsistent with the parallel normal/private strings.
    - Current: `Gesynchroniseerde open tabbladen: %1$s.`
    - Source: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Open gesynchroniseerde tabbladen: %1$s.`
    - The sibling strings render "Tabs Open" as "Open ... tabbladen"; here the modifiers are swapped, breaking consistency on the same surface.
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
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — The order of "blocked" and "unsupported" is swapped relative to the source.
    - Current: `Browser wordt niet ondersteund of geblokkeerd`
    - Source: `Browser is blocked or unsupported`
    - Suggest: `Browser is geblokkeerd of wordt niet ondersteund`
    - Source is "Browser is blocked or unsupported"; the Dutch reverses the order of the two conditions.
- `add_custom_autocomplete_label` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — "Add link to autocomplete" is rendered as if adding a link pointing to autocomplete.
    - Current: `Koppeling naar automatisch aanvullen toevoegen`
    - Source: `Add link to autocomplete`
    - Suggest: `Koppeling aan automatisch aanvullen toevoegen`
    - The button adds the current URL to the custom autocomplete list; "naar" reads as direction (a link to autocomplete) rather than adding it to the list.
- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — "Dismiss" (close/return to browser) is translated as "Verwijderen" (delete).
    - Current: `Verwijderen`
    - Source: `Dismiss`
    - Suggest: `Sluiten`
    - Per the developer comment, tapping the overlay dismisses typing mode and returns to the browser; "Verwijderen" means "delete", which describes a destructive action, not dismissing.
- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — "Dismiss" is translated as "Verwijderen" (delete), which means something different.
    - Current: `Verwijderen`
    - Source: `Dismiss`
    - Suggest: `Sluiten`
    - The button dismisses/closes a message; "Verwijderen" means "Delete", implying data removal rather than dismissing the prompt.
- `firstrun_shortcut_title` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — ‘Shortcuts’ is translated as ‘koppelingen’ (links) instead of ‘snelkoppelingen’ (shortcuts).
    - Current: `Voeg koppelingen toe aan uw startscherm`
    - Source: `Add shortcuts to your home screen`
    - Suggest: `Voeg snelkoppelingen toe aan uw startscherm`
    - The source says 'Add shortcuts to your home screen'; 'koppelingen' means links, and elsewhere in this batch 'Shortcuts' is rendered as 'snelkoppelingen' (menu_add_to_shortcuts).

### C. Grammar, agreement & spelling

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
- `mozac_feature_sitepermissions_local_network_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-nl/strings.xml` — Misplaced prepositional phrase makes the sentence say permission is granted "on devices" rather than access to apps/services on those devices.
    - Current: `Toegang tot apps en services door %1$s toestaan op apparaten die zijn verbonden met uw lokale netwerk?`
    - Source: `Allow %1$s to access apps and services on devices connected to your local network?`
    - Suggest: `%1$s toegang geven tot apps en services op apparaten die zijn verbonden met uw lokale netwerk?`
    - The source is "access to apps and services on devices connected to your local network"; in the Dutch the phrase "op apparaten…" is detached from "apps en services" and attaches to "toestaan", changing the meaning.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Inconsistent/incorrect spelling of "doorleidings-" vs "doorgeleidingen" used in the matching description string.
    - Current: `Doorleidingstrackers`
    - Source: `Redirect Trackers`
    - Suggest: `Doorgeleidingstrackers`
    - The description string etp_redirect_trackers_description renders "redirects" as "doorgeleidingen"; the title uses the malformed "Doorleidings-", inconsistent with the same term on the same surface.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "trots onafhankelijk" is ungrammatical as an adverbial modifier in Dutch.
    - Current: `Firefox is trots onafhankelijk`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox is trots op zijn onafhankelijkheid`
    - "proudly independent" requires an adverb construction; "trots onafhankelijk" is not idiomatic/grammatical Dutch.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Sentence is ungrammatical: missing subject/verb agreement for "One tap helps stop…".
    - Current: `Met één tik voorkomen dat bedrijven uw tikken bespioneren.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Met één tik voorkomt u dat bedrijven uw klikken bespioneren.`
    - The Dutch clause has no subject; "Met één tik voorkomen dat…" is not a well-formed sentence, unlike the source "One tap helps stop companies spying on your clicks."
- `sports_widget_team_followed_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Following:" is translated as the present participle "Volgend:" which means "next" rather than "you are following".
    - Current: `Volgend:`
    - Source: `Following:  %s`
    - Suggest: `Volgt:`
    - The source labels the team the user follows; Dutch 'volgend' means 'next/following (in sequence)' and is misleading here.
- `sync_no_devices_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Wrong article gender with ‘account’ (het account) and ‘Alle’ instead of ‘Alle apparaten die … ’ mismatch.
    - Current: `met deze account`
    - Source: `Any devices signed in and syncing to this account will appear here.`
    - Suggest: `met dit account`
    - In Dutch (and in Mozilla nl terminology) ‘account’ is a het-woord: ‘dit account’, not ‘deze account’.
- `terms_of_use_prompt_body_line_two_alternative` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Sentence reads awkwardly/ungrammatically with the link placeholder inserted mid-sentence.
    - Current: `U vindt %1$s meer info.`
    - Source: `You can learn more %1$s.`
    - Suggest: `U kunt %1$s meer info vinden.`
    - %1$s is the link text "hier"; "U vindt hier meer info" splits oddly and the source is "You can learn more here."
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — Subject mismatch: "Door dit te verzenden, helpt het ons" is ungrammatical and inconsistent with the plural variant.
    - Current: `Door dit te verzenden, helpt het ons %1$s te verbeteren.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Als u dit verzendt, helpt u ons %1$s te verbeteren.`
    - Source: "Sending it will help us improve %1$s." The Dutch mixes an implicit subject with "het"; the parallel plural string correctly uses "Als u deze verzendt, helpt u ons…".
- `promote_search_widget_dialog_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — Comma splice and misplaced/duplicated adverb make the sentence ungrammatical and awkward.
    - Current: `We laten u nu verdergaan met uw privénavigatie, u kunt de volgende keer sneller van start gaan nu met de %1$s-widget op uw startscherm.`
    - Source: `We’ll leave you to your private browsing, but get a quicker start next time with the %1$s widget on your Home screen.`
    - Suggest: `We laten u verdergaan met uw privénavigatie, maar u kunt de volgende keer sneller van start gaan met de %1$s-widget op uw startscherm.`
    - The source uses ‘but’ to join the clauses; the Dutch joins two main clauses with only a comma and repeats ‘nu’ in an ungrammatical position (‘van start gaan nu met’).

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
- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren", which means "browse back" rather than navigating back/going back.
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terug navigeren`
    - The source is a content description for a back button; Dutch "bladeren" means to browse/leaf through, not to navigate back. Compare action_bar_up_description usage of navigation wording.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "permission" is translated as "toestemming" here while the sibling strings use "machtigingen", creating inconsistency on the same surface.
    - Current: `deze toestemming`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `deze machtiging`
    - confirm_clear_permissions_site and confirm_clear_permissions_on_all_sites use "machtigingen" for the same source term "permissions" in the same dialog family.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Shortcuts" (home screen tiles) is translated as "sneltoetsen" (keyboard shortcuts) instead of "snelkoppelingen".
    - Current: `Alle sneltoetsen tonen`
    - Source: `Show all shortcuts`
    - Suggest: `Alle snelkoppelingen tonen`
    - The related string homepage_shortcuts_add_shortcut uses "Snelkoppeling"; "sneltoetsen" means keyboard shortcuts, which is the wrong concept for home screen shortcut tiles.
- `ip_protection_locations_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Navigate back" is rendered as "Terug bladeren", which is not the standard Dutch back-navigation wording.
    - Current: `Terug bladeren`
    - Source: `Navigate back`
    - Suggest: `Terugnavigeren`
    - The source is a back button content description; "bladeren" means "to browse/leaf through" and misdescribes the control for screen-reader users. Mozilla nl uses "Terug"/"Terugnavigeren".
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "more private" is translated as "persoonlijker" (more personal) instead of "meer privé".
    - Current: `uw navigatie persoonlijker en moeilijker te volgen te maken`
    - Source: `Turn VPN on to make your browsing more private and harder to trace.`
    - Suggest: `uw navigatie meer privé en moeilijker te volgen te maken`
    - "persoonlijker" means "more personal", the opposite emphasis of "more private"; the parallel string ip_protection_onboarding_body_promo correctly uses "meer privé".
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Round of 16" is rendered literally as "Ronde van 16" instead of the Dutch football term "Achtste finales".
    - Current: `Ronde van 16`
    - Source: `Round of 16`
    - Suggest: `Achtste finales`
    - In Dutch soccer terminology the Round of 16 is called 'achtste finales'; 'Ronde van 16' is a literal, incorrect rendering (and inconsistent with 'Halve finales' used elsewhere).
- `sports_widget_round_of_32` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "Round of 32" is rendered literally as "Ronde van 32" instead of the Dutch term "Zestiende finales".
    - Current: `Ronde van 32`
    - Source: `Round of 32`
    - Suggest: `Zestiende finales`
    - Dutch soccer terminology for the Round of 32 is 'zestiende finales'; the literal 'Ronde van 32' is not the established term and is inconsistent with 'Halve finales'.
- `sports_widget_view_schedule` — `mozilla-mobile/fenix/app/src/main/res/values-nl/strings.xml` — "View schedule" (tournament match schedule) is translated as "Tijdschema bekijken" instead of "Speelschema bekijken".
    - Current: `Tijdschema bekijken`
    - Source: `View schedule`
    - Suggest: `Speelschema bekijken`
    - The developer comment specifies the full soccer tournament match schedule, which in Dutch is 'speelschema'; 'tijdschema' means timetable in a generic sense.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
