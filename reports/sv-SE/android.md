# Android l10n QA — sv-SE

| | |
|---|---|
| **Generated** | 2026-10-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-19 @ `ea17dbc84971` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 2,803 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sv-SE: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,803 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 9, `curly-double` 6 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (78)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 30 |
| 3 | Degraded language (grammar, spelling, terminology) | 48 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — "device" is translated as "datorn" (the computer) on a mobile error page.
    - Current: `Är datorn ansluten till ett aktivt nätverk?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Är enheten ansluten till ett aktivt nätverk?`
    - The source says "device". This page shows on Android phones and tablets, and other strings in the batch use "enhet".
- `mozac_browser_errorpages_safe_browsing_unwanted_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — "serving unwanted software" is rendered as "betjäna", a word-for-word copy meaning to serve people, not to distribute software.
    - Current: `har rapporterats betjäna oönskad programvara`
    - Source: `{ <p> }The site at %1$s has been reported as serving unwanted software and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `har rapporterats sprida oönskad programvara`
    - In the source, "serving" means supplying or distributing software. In Swedish "betjäna" means waiting on or serving people, such as customers, so the sentence comes out wrong.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — "device" is translated as "datorn" (the computer) on a mobile error page.
    - Current: `Är datorn ansluten till ett aktivt nätverk?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Är enheten ansluten till ett aktivt nätverk?`
    - The source says "device". This page shows on Android devices, and other strings in the batch use "enhet".
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sv-rSE/strings.xml` — The adjective "Stödd" modifies "kontroll", so the channel name reads as "a supported add-on check" rather than "checker for supported add-ons".
    - Current: `Stödd tilläggskontroll`
    - Source: `Supported add-ons checker`
    - Suggest: `Kontroll av stödda tillägg`
    - The source means a checker that looks for add-ons that are now supported. In Swedish the compound attaches "stödd" to "kontroll", which changes what is described as supported.
- `mozac_feature_autofill_search_suggestions` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-sv-rSE/strings.xml` — "Sök efter %1$s" means "search for Firefox", but the item actually opens a search of logins inside the app.
    - Current: `Sök efter %1$s`
    - Source: `Search %1$s`
    - Suggest: `Sök i %1$s`
    - The developer comment says %1$s is the app name (e.g. Firefox) and that the item opens a screen for searching logins. So "Search Firefox" means searching within the app. "Sök efter" means "search for", which turns the app into the thing being searched for.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-sv-rSE/strings.xml` — Progress notification uses the imperative "Skicka" (Send) instead of the present tense "Skickar" (Sending).
    - Current: `Skicka kraschrapport till %1$s`
    - Source: `Sending crash report to %1$s`
    - Suggest: `Skickar kraschrapport till %1$s`
    - The comment says this label shows that the crash report service is running, so it describes something in progress, like "Samlar in kraschdata". The imperative reads as a command or action label, the same as the checkbox string.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — 'Department' as an administrative division is rendered as 'Avdelning' (organisational department) instead of 'Departement'.
    - Current: `Avdelning`
    - Source: `Department`
    - Suggest: `Departement`
    - The developer comment says this is the administrative division used in Colombia and Nicaragua. The Swedish term for that is 'departement'. 'Avdelning' means a department in a company or organisation.
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The artist's handle is misspelled with an extra "mo".
    - Current: `@heyheymomomodraws`
    - Source: `Created by @heyheymomodraws`
    - Suggest: `@heyheymomodraws`
    - The source and the developer comment give the handle as @heyheymomodraws. The translation adds a syllable, so it names an account that doesn't exist.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "till detta språk" means translating into this language, but the source means sites written in this language.
    - Current: `webbplatser till detta språk`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `webbplatser på detta språk`
    - The source says "sites in this language", meaning the language the sites are written in. "till" makes it the target language instead. The matching never-translate string correctly uses "på".
- `browser_menu_add_to_homescreen` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Home screen" is translated as "startsidan", which in this app means the browser homepage, not the device home screen.
    - Current: `Lägg till på startsidan`
    - Source: `Add to Home screen`
    - Suggest: `Lägg till på startskärmen`
    - The developer comment says this adds a shortcut to the device home screen. "Startsida" is the term this locale uses for the browser homepage (browser_menu_homepage = "Startsida"). The neighbouring string browser_menu_add_app_to_homescreen uses "startskärmen" for the same idea.
- `certificate_warning_homepage_card_hcr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "stop working properly" is rendered as "slutar fungera" (stops working), dropping "properly".
    - Current: `slutar fungera.`
    - Source: `A root certificate will expire, causing your version of Firefox to stop working properly.`
    - Suggest: `slutar fungera korrekt.`
    - The source says Firefox will stop working properly, not stop working entirely; the Swedish states a total failure.
- `certificate_warning_homepage_card_hcr1_title` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Update" is rendered as a noun although the developer comment says it is a verb.
    - Current: `Uppdatering före den 14 mars`
    - Source: `Update before March 14`
    - Suggest: `Uppdatera före den 14 mars`
    - Developer comment explicitly states "Update" is a verb; "Uppdatering" is a noun, turning the call to action into a label.
- `clear_permission` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Singular "Clear permission" is translated with the plural "behörigheter", which makes it the same as the clear_permissions label.
    - Current: `Rensa behörigheter`
    - Source: `Clear permission`
    - Suggest: `Rensa behörighet`
    - The source and the developer comment both refer to clearing one site permission. The Swedish plural means all permissions and duplicates clear_permissions ("Clear permissions"), so users can't tell the two actions apart.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Singular "this permission" is rendered with an ungrammatical mix of a singular neuter determiner and a plural definite noun.
    - Current: `det här behörigheterna`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `den här behörigheten`
    - The source says "this permission" (singular), and the dialog is about clearing one permission. "det här behörigheterna" is ungrammatical: "det här" is neuter singular, but "behörigheterna" is common gender and plural definite. It also suggests more than one permission. The correct form is "den här behörigheten".
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Debug" is translated as the command "Felsök" instead of describing the debug locales.
    - Current: `Felsök språkversioner för att aktivera`
    - Source: `Debug locales to enable`
    - Suggest: `Felsökningsspråk att aktivera`
    - The header lists debug locales that can be turned on and off. The Swedish reads "Debug locales in order to enable", which is an odd instruction.
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Överskrider" means "exceeds", not "overrides".
    - Current: `Överskrider tillfälligt`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `Åsidosätter tillfälligt`
    - Source says the tool temporarily overrides region values. "Överskrida" means "exceed". The other override strings in this tool use "Åsidosätt".
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "isolerar kakor från webbplatsen" says cookies are isolated from the current site, the opposite of isolating them to it.
    - Current: `isolerar kakor från webbplatsen du är på`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `isolerar kakor till den webbplats du är på`
    - The source says Total Cookie Protection isolates cookies *to* the site you're on, so each site's cookies stay with that site. "från" (from) describes the wrong separation.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The category name is translated as an imperative verb phrase ("Redirect trackers!") instead of a noun.
    - Current: `Omdirigera spårare`
    - Source: `Redirect Trackers`
    - Suggest: `Omdirigeringsspårare`
    - The developer comment says this names a category of trackers. "Omdirigera spårare" reads as a command to redirect trackers.
- `etp_tracking_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Content that contains tracking code" is rendered as "content, because they may contain tracking code".
    - Current: `från laddning eftersom de kan innehålla spårningskod`
    - Source: `Stops outside ads, videos, and other content from loading that contains tracking code. May affect some website functionality.`
    - Suggest: `som innehåller spårningskod från att laddas`
    - The source only blocks content that contains tracking code. The Swedish says all external ads, videos and other content are blocked because they might contain tracking code, which is a broader claim.
- `extension_process_crash_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "unsuccessfully tried to restart" is rendered as "did not try to restart", which reverses the meaning.
    - Current: `%1$s försökte inte starta om tillägget.`
    - Source: `One or more extensions stopped working, making your system unstable. %1$s unsuccessfully tried to restart the extension(s).  Extensions won’t be restarted during your current session.  Removing or disabling extensions m…`
    - Suggest: `%1$s försökte utan framgång starta om tillägget/tilläggen.`
    - The source says the app tried to restart the extensions and failed. The Swedish says the app made no attempt at all, which is a different claim about what the app did.
- `history_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Sökhistorik" means the history of searches, not the instruction to search the history.
    - Current: `Sökhistorik`
    - Source: `Search history`
    - Suggest: `Sök i historik`
    - The source text is placeholder text in the history search bar, inviting the user to search their browsing history ("Search history" as an instruction). The Swedish compound "Sökhistorik" is a noun meaning "history of searches", which is something else.
- `ip_protection_location_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Unavailable" is translated as "Upptagen" (busy/occupied) instead of "Otillgänglig".
    - Current: `Upptagen`
    - Source: `Unavailable`
    - Suggest: `Otillgänglig`
    - The source says the VPN location is unavailable. "Upptagen" means busy or occupied, which suggests the location is only busy for now. The related strings (ip_protection_location_unavailable, the snackbars) use "otillgänglig", so the terminology is also inconsistent on the same surface.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Temporal "through <date>" is rendered as "genom", which means "by means of" rather than "until".
    - Current: `genom %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `till och med %1$s`
    - %1$s is the end date of the promotion. In English, "through" means up to and including that date. In Swedish, "genom" means "via" or "by means of", so the end date of the promotion is lost. Use "till och med".
- `never_translate_site_dialog_title_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Dialog title uses past tense "Tog bort" ("Removed") instead of the imperative question "Delete …?".
    - Current: `Tog bort %1$s?`
    - Source: `Delete %1$s?`
    - Suggest: `Ta bort %1$s?`
    - Source "Delete %1$s?" asks the user to confirm a deletion; "Tog bort" means "removed", so the title is wrong. It also doesn't match the "Ta bort" confirm button.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The idiom "won't sell you out" (won't betray you) is rendered as "won't expose/reveal you".
    - Current: `kommer inte att avslöja dig`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `kommer inte att svika dig`
    - "Sell you out" means betray (here, selling your data). "Avslöja dig" means unmask or expose you, which is a different statement. "Svika dig" (or "sälja ut dig") keeps the source meaning.
- `preference_enhanced_tracking_protection_custom_cookies_5` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — 'Cross-site cookies' is rendered as 'cross-site tracking cookies', which narrows the option's scope.
    - Current: `Isolera globala spårningskakor`
    - Source: `Isolate cross-site cookies`
    - Suggest: `Isolera globala kakor`
    - The source says 'Isolate cross-site cookies', meaning all cross-site cookies, not only tracking cookies. Adding 'spårnings' changes what the option says it does.
- `preference_enhanced_tracking_protection_standard_default_1` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The '(default)' marker from the source is dropped.
    - Current: `Standard`
    - Source: `Standard (default)`
    - Suggest: `Standard (standard)`
    - The source tells users this option is the default ('Standard (default)'). The translation leaves that out. A wording such as 'Standard (förvald)' would keep it.
- `preferences_site_settings` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Site settings" is rendered as "Platsinställningar", which reads as location settings rather than website settings.
    - Current: `Platsinställningar`
    - Source: `Site settings`
    - Suggest: `Webbplatsinställningar`
    - The source and comment refer to settings for websites ("advanced site settings"); in Swedish "plats" alone means place/location, and the established Firefox term for a site is "webbplats".
- `webcompat_reporter_reason_turn_off_adblocker` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The Swedish says the site is being asked to turn off the ad blocker, when the site actually asked the user to do it.
    - Current: `Webbplatsen ombeds att stänga av annonsblockeraren`
    - Source: `Site asked to turn off ad blocker`
    - Suggest: `Webbplatsen bad mig stänga av annonsblockeraren`
    - Source: 'Site asked to turn off ad blocker' means the site made the request. 'ombeds' is passive ('is asked'), so it reverses who is asking whom.
- `preference_privacy_should_block_cookies_cross_site_option` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — "Cross-site cookies" is rendered as "globala kakor" (global cookies), which names the wrong thing.
    - Current: `globala kakor`
    - Source: `Block cross-site cookies`
    - Suggest: `kakor mellan webbplatser`
    - The source says cross-site, meaning cookies shared between different sites, not 'global' cookies. Firefox sv-SE elsewhere uses 'mellan webbplatser'.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — The last verb in the list uses the active "flyttat" instead of the passive "flyttats", so it no longer matches "tagits bort" or the source's meaning ("relocated").
    - Current: `tagits bort eller flyttat?`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `tagits bort eller flyttats?`
    - The source asks whether the item was renamed, removed or relocated, meaning someone moved it. The verb before it, "tagits bort", is passive, so the list should end with the passive "flyttats". The sibling string file_access_denied_message already says "flyttats" for the same idea.
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — The possessive "ditt" does not agree with the common-gender noun "router".
    - Current: `Kontrollera ditt modem eller router.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Kontrollera ditt modem eller din router.`
    - "router" is an en-word, so it needs its own possessive "din". "ditt" only agrees with "modem".
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sv-rSE/strings.xml` — "ladda om sidan igen" says "again" twice.
    - Current: `ladda om sidan igen`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `ladda om sidan`
    - "Ladda om" already means reload, so "igen" repeats it. The source says only "reload the page".
- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sv-rSE/strings.xml` — The pronoun "Den" doesn't agree with the neuter noun "lösenord" it refers to.
    - Current: `Den kommer att sparas`
    - Source: `Protect your account by using a strong, randomly generated password. It’ll be saved into your account for future use.`
    - Suggest: `Det kommer att sparas`
    - "It'll be saved" refers to the password; "lösenord" is neuter (ett lösenord), so the pronoun must be "det".
- `mozac_feature_readerview_sans_serif_font_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-sv-rSE/strings.xml` — Compound is incorrectly split (särskrivning); it should be joined with a hyphen.
    - Current: `Sans Serif typsnitt`
    - Source: `Sans Serif font`
    - Suggest: `Sans serif-typsnitt`
    - Swedish writes compounds as one word. When the first part is a multi-word name, it is joined with a hyphen, so it should be 'sans serif-typsnitt'.
- `mozac_feature_readerview_sepia_color_scheme_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-sv-rSE/strings.xml` — Compound is incorrectly split (särskrivning).
    - Current: `Sepia färgschema`
    - Source: `Sepia color scheme`
    - Suggest: `Sepiafärgschema`
    - Swedish compounds must be written as one word; 'Sepia färgschema' is a split compound.
- `mozac_feature_readerview_serif_font_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-sv-rSE/strings.xml` — Compound is incorrectly split (särskrivning).
    - Current: `Serif typsnitt`
    - Source: `Serif font`
    - Suggest: `Serif-typsnitt`
    - Swedish compounds must be written together or hyphenated; 'Serif typsnitt' is a split compound.
- `mozac_feature_sitepermissions_persistent_storage_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-sv-rSE/strings.xml` — Infinitive "Tillåta" is used instead of the imperative "Tillåt" that every other permission dialog title uses.
    - Current: `Tillåta %1$s`
    - Source: `Allow %1$s to store data in persistent storage?`
    - Suggest: `Tillåt %1$s`
    - The source "Allow %1$s to…?" is rendered with the imperative "Tillåt" in all sibling permission titles. The infinitive here is inconsistent and reads as a slip.
- `mozac_feature_summarize_feedback_bad_click_label` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sv-rSE/strings.xml` — Imperative "betygssätt" is used where the interpolated accessibility phrase needs the infinitive.
    - Current: `betygssätt sammanfattningen som dålig`
    - Source: `rate summary as bad`
    - Suggest: `betygsätta sammanfattningen som dålig`
    - The comment says this text is placed into "Double tap to [...]" and recommends the infinitive. In Swedish that becomes "för att …", which needs "betygsätta", so the imperative is ungrammatical there.
- `mozac_feature_summarize_feedback_good_click_label` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sv-rSE/strings.xml` — Imperative "betygssätt" is used where the interpolated accessibility phrase needs the infinitive.
    - Current: `betygssätt sammanfattningen som bra`
    - Source: `rate summary as good`
    - Suggest: `betygsätta sammanfattningen som bra`
    - The comment says this text is placed into "Double tap to [...]" and recommends the infinitive. In Swedish that becomes "för att …", which needs "betygsätta", so the imperative is ungrammatical there.
- `accessibility_text_size_sample_text_1` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The compound "textstorleken" is split into two words.
    - Current: `text storleken`
    - Source: `This is sample text. It is here to show how text will appear when you increase or decrease the size with this setting.`
    - Suggest: `textstorleken`
    - Swedish compounds are written as one word. Splitting this one is a spelling error.
- `add_to_tab_group_bottom_sheet_grabber_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "drahandtaget" is misspelled. It should be "draghandtaget".
    - Current: `drahandtaget`
    - Source: `Add to a tab group, collapse drag handle`
    - Suggest: `draghandtaget`
    - The Swedish word for drag handle is "draghandtag", but the g is missing here. Screen readers read this string aloud.
- `automatic_translation_option_offer_to_translate_title_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The radio label uses the infinitive "Erbjuda" where the imperative "Erbjud" is needed.
    - Current: `Erbjuda att översätta`
    - Source: `Offer to translate (default)`
    - Suggest: `Erbjud att översätta`
    - The other radio-button labels use the imperative ("Översätt alltid", "Översätt aldrig"). The infinitive is grammatically off for this label and inconsistent with them.
- `certificate_warning_homepage_card_hca1_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "upphöra" alone does not mean "expire" for a certificate; the idiom is "upphöra att gälla".
    - Current: `kommer att upphöra,`
    - Source: `A root certificate will expire, causing some features to stop working on March 14.`
    - Suggest: `kommer att upphöra att gälla,`
    - "Upphöra" alone means "cease"; a certificate expiring is "upphöra att gälla", as already used in certificate_warning_homepage_card_hcr1_message.
- `certificate_warning_homepage_card_hcw2_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "upphöra" alone does not mean "expire" for a certificate; the idiom is "upphöra att gälla".
    - Current: `håller på att upphöra.`
    - Source: `On March 14, add-ons and other Firefox features will stop working because a root certificate is expiring.`
    - Suggest: `håller på att upphöra att gälla.`
    - "Upphöra" alone means "cease"; certificate expiry is "upphöra att gälla", consistent with hcr1_message.
- `debug_drawer_override_region` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The shortened compound "hem" needs a hyphen before "och".
    - Current: `Åsidosätt hem och aktuell region`
    - Source: `Override home and current region`
    - Suggest: `Åsidosätt hem- och aktuell region`
    - "Hemregion" is shortened before "och", so Swedish needs a hyphen: "hem- och aktuell region".
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The shortened compound "hem" needs a hyphen before "och".
    - Current: `för hem och aktuell region`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `för hem- och aktuell region`
    - Swedish uses a hyphen when the shared second part of a compound (hemregion) is left out.
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "surfsdata" is a non-standard compound; the established form is "surfdata".
    - Current: `surfsdata`
    - Source: `Deleting browsing data…`
    - Suggest: `surfdata`
    - Swedish forms this compound without the linking s ("surfdata"), and sv-SE Firefox uses "surfdata" for "browsing data".
- `etp_social_media_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The genitive -s is missing on "nätverk".
    - Current: `sociala nätverk förmåga`
    - Source: `Limits the ability of social networks to track your browsing activity around the web.`
    - Suggest: `sociala nätverks förmåga`
    - A possessive construction is needed here: "the social networks' ability".
- `inactive_tabs_auto_close_message_header` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The object pronoun is wrongly written as "de" when it should be "dem".
    - Current: `Stäng de automatiskt`
    - Source: `Auto-close after one month?`
    - Suggest: `Stäng dem automatiskt`
    - The pronoun is the object of "Stäng", so Swedish requires the object form "dem".
- `lens_camera_permission_denied` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The participle does not agree with the neuter noun "tillstånd".
    - Current: `Tillstånd nekad`
    - Source: `Permission denied`
    - Suggest: `Tillstånd nekat`
    - "Tillstånd" is a neuter noun (ett tillstånd), so the predicative participle must be "nekat".
- `microsurvey_app_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Split compound: "Firefox logotyp" should be hyphenated as a compound.
    - Current: `Firefox logotyp`
    - Source: `Firefox logo`
    - Suggest: `Firefox-logotyp`
    - Swedish compounds with a proper name need a hyphen ("Firefox-logotyp"); writing it as two words is a spelling error.
- `notifications_allowed_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Gender doesn't match the paired summary "Inte tillåtet": common-gender "Tillåten" vs neuter.
    - Current: `Tillåten`
    - Source: `Allowed`
    - Suggest: `Tillåtet`
    - The two summaries describe the same preference state and should agree in form; the not-allowed variant uses neuter "tillåtet".
- `nova_onboarding_add_search_widget_button` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Split compound: "Firefox widget" should be hyphenated as a compound.
    - Current: `Lägg till Firefox widget`
    - Source: `Add Firefox widget`
    - Suggest: `Lägg till Firefox-widget`
    - Swedish compounds with a proper name need a hyphen; writing it as two words is a spelling error.
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The clause 'känn att Firefox automatiska skydd dig' has no verb, so the sentence is ungrammatical and doesn't render 'have your back'.
    - Current: `känn att Firefox automatiska skydd dig`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `vet att Firefox automatiska skydd har din rygg`
    - The source says Firefox's automatic protections 'have your back'. The Swedish leaves out the verb, so the sentence doesn't parse and that meaning is lost.
- `nova_onboarding_theme_selection_automatic_label` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The theme option 'Automatisk' uses the common-gender form, while its sibling options 'Mörkt' and 'Ljust' use the neuter form that agrees with 'tema'.
    - Current: `Automatisk`
    - Source: `Automatic`
    - Suggest: `Automatiskt`
    - All three labels describe a theme ('tema', a neuter noun). The dark and light options are neuter, so the automatic option should be 'Automatiskt' to agree with them.
- `onboarding_term_of_service_line_two_2` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Plural possessive "våra" does not agree with the singular common-gender link text "Sekretesspolicy".
    - Current: `Läs mer i våra %1$s.`
    - Source: `Firefox cares about your privacy. Learn more in our %1$s.`
    - Suggest: `Läs mer i vår %1$s.`
    - The placeholder is replaced by "Sekretesspolicy" (singular, common gender), so the possessive must be "vår"; "våra" is plural and ungrammatical here.
- `open_source_licenses_title` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Split compound "OSS bibliotek" should be hyphenated as "OSS-bibliotek".
    - Current: `OSS bibliotek`
    - Source: `%s \| OSS Libraries`
    - Suggest: `OSS-bibliotek`
    - Swedish compounds formed with an abbreviation are joined with a hyphen; writing them apart is a spelling error (särskrivning).
- `phone_feature_blocked_step_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Tryck" needs the preposition "på" before the item being tapped.
    - Current: `2. Tryck { <b> }`
    - Source: `2. Tap { <b> }Permissions{ </b> }`
    - Suggest: `2. Tryck på { <b> }`
    - 'Tap X' is 'Tryck på X' in Swedish. Without 'på' it reads as 'press/print Permissions'.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "Inaktivera att hantera" is missing "för", so it is not grammatical.
    - Current: `Inaktivera att hantera`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `Inaktivera för att hantera`
    - Source: 'Disable to manage font size here'. In Swedish a purpose clause needs 'för att'.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — "standard DNS-resolver" is written as two words when Swedish requires one compound.
    - Current: `standard DNS-resolver`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `standard-DNS-resolver`
    - Swedish compounds have to be joined. A compound containing an abbreviation is joined with hyphens.
- `preference_enhanced_tracking_protection_allow_list_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Pronoun 'det' does not agree with the common-gender antecedent 'inställningen'.
    - Current: `Om du stänger av det`
    - Source: `This setting helps fix the most common site problems. If you turn it off, some sites may not work, and %1$s won’t be able to help troubleshoot those issues.`
    - Suggest: `Om du stänger av den`
    - 'Inställning' is common gender (en inställning), so the referring pronoun must be 'den'.
- `preferences_install_local_extension` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Definite form "tillägget" makes the generic menu action refer to a specific extension.
    - Current: `Installera tillägget från fil`
    - Source: `Install extension from file`
    - Suggest: `Installera tillägg från fil`
    - The source "Install extension from file" is a generic preference/action label; the definite "tillägget" (the extension) implies a particular, already-identified extension.
- `preferences_passwords_save_logins_ask_to_save` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Wrong preposition: "Fråga för att spara" means "ask in order to save" rather than "ask whether to save".
    - Current: `Fråga för att spara`
    - Source: `Ask to save`
    - Suggest: `Fråga om att spara`
    - The option makes the browser ask the user whether to save a password. In Swedish that needs "fråga om att spara"; "för att" expresses purpose, so the current text is unidiomatic and misleading.
- `protection_panel_etp_toggle_disabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The bare imperative "Aktivera" can't be the subject of "rekommenderas", so the sentence is ungrammatical.
    - Current: `Aktivera spårningsskydd rekommenderas.`
    - Source: `Turning on tracking protection is recommended.`
    - Suggest: `Att aktivera spårningsskydd rekommenderas.`
    - The source "Turning on tracking protection is recommended" uses a gerund as the subject. In Swedish that needs an infinitive phrase with "Att". As written it reads as an order ("Activate tracking protection") followed by "is recommended".
- `search_suggestions_onboarding_title` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The title uses the present tense "Tillåter" where the imperative "Tillåt" is needed.
    - Current: `Tillåter sökförslag`
    - Source: `Allow search suggestions in private sessions?`
    - Suggest: `Tillåt sökförslag`
    - The source "Allow search suggestions in private sessions?" asks the user for permission, so Swedish needs the imperative "Tillåt". "Tillåter" turns it into a statement-like question ("Allows search suggestions…?") with no subject.
- `sign_in_create_account_text` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The verb "Har" is misspelled as "Ha" in the question "Har du inget konto?".
    - Current: `Ha du inget konto?`
    - Source: `No account? { <u> }Create one{ </u> } to sync Firefox between devices.`
    - Suggest: `Har du inget konto?`
    - "Ha" is the infinitive. A question in the present tense needs the finite form "Har" ("Do you have no account?").
- `sync_last_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The adjective form "Senaste" is used where the adverb "Senast" is needed before the participle "synkroniserad".
    - Current: `Senaste synkroniserad`
    - Source: `Last synced: %s`
    - Suggest: `Senast synkroniserad`
    - "Last synced" calls for the adverb "Senast" in Swedish. The sibling string sync_never_synced_summary correctly uses "Senast synkroniserad".
- `tab_collection_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — The preposition "på" is missing from "säker att"; standard Swedish is "säker på att".
    - Current: `Är du säker att du vill`
    - Source: `Are you sure you want to delete %1$s?`
    - Suggest: `Är du säker på att du vill`
    - In standard Swedish, the adjective "säker" (sure) takes the preposition "på" before an att-clause. Without it, the confirmation dialog reads as colloquial or ungrammatical.
- `uninstall_survey_option_6_v2` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Missing hyphen after "Sekretess" in a coordinated compound, so the phrase reads as "Privacy or security problems" rather than "privacy or security concerns".
    - Current: `Sekretess eller säkerhetsproblem`
    - Source: `Privacy or security concerns`
    - Suggest: `Sekretess- eller säkerhetsproblem`
    - In Swedish, when two compounds share the same final part ("sekretessproblem" and "säkerhetsproblem"), the first must end in a hyphen. Without it, "Sekretess" stands on its own as a separate noun, which is a spelling error and changes the reading of the source "Privacy or security concerns".
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — Ungrammatical phrase: "för" is missing before "att" in the purpose clause.
    - Current: `uppdatera inställningar att tillåta trackers`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `uppdatera inställningar för att tillåta spårare`
    - 'update settings to allow trackers' needs 'för att' in Swedish. 'uppdatera inställningar att tillåta' is ungrammatical.
- `onboarding_first_screen_terms_of_use_link_2` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The link text is in the indefinite form but is inserted into a sentence that needs the definite form.
    - Current: `användarvillkor för Firefox`
    - Source: `Firefox Terms of Use`
    - Suggest: `användarvillkoren för Firefox`
    - This link is substituted into 'Genom att fortsätta godkänner du %1$s.', which gives 'godkänner du användarvillkor för Firefox'. The source refers to the specific Firefox Terms of Use ('agree to the Firefox Terms of Use'), so Swedish needs the definite form 'användarvillkoren'.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The imperative 'Dölj' is paired with the present-tense 'blockerar', so the two verbs don't match.
    - Current: `och blockerar skärmdumpar`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `och blockera skärmdumpar`
    - The source uses two parallel imperatives ('Hide ... and block ...'), so the second verb should also be in the imperative.

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_notifications_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sv-rSE/strings.xml` — "Notifications" is rendered as "meddelanden" here but as "aviseringar" in the update variant of the same permission.
    - Current: `Visa meddelanden till dig`
    - Source: `Display notifications to you`
    - Suggest: `Visa aviseringar till dig`
    - These are the same notifications permission on the same permission surface. The _for_update string uses the standard term "aviseringar". "Meddelanden" means messages and is also used for the nativeMessaging permission ("Utbyta meddelanden"), so the two permissions could be confused.
- `browser_menu_read_close` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Reader view is "läsarvy" here but "Läsvy" in the matching menu item browser_menu_read.
    - Current: `Stäng läsarvy`
    - Source: `Close reader view`
    - Suggest: `Stäng läsvy`
    - Same feature on the same menu surface is named inconsistently between the open and close entries.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — `never_translate_site_header_preference` quotes “Översätt aldrig den här webbplatsen” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Översätt aldrig denna sida”
    - Current: `För att lägga till en ny webbplats: Besök den och välj "Översätt aldrig den här webbplatsen" från översättningsmenyn.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Översätt aldrig denna sida`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sv-rSE/strings.xml` — Font size is called "Teckensnittstorlek" here (also missing the joining s), but "teckenstorlek" later in the same string and in the title.
    - Current: `Teckensnittstorlek matchar`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `Teckenstorlek matchar`
    - The same term should be rendered the same way on one surface. The title preference_accessibility_font_size_title uses 'Teckenstorlek', and the compound as written is misspelled (it would be 'teckensnittsstorlek').
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The English word 'trackers' is used, but the same app uses 'spårare' elsewhere.
    - Current: `Blockera trackers`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Blockera spårare`
    - cfr_for_start_browsing in Focus renders trackers as 'spårare'. The About text keeps the English loanword, so the term is inconsistent within the same app.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sv-SE/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
