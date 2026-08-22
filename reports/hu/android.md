# Android l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **Previous run** | 2026-08-21 @ `d368c9040c12` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,897 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hu: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,897 |
| Missing strings | 14 |
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
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**14 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — 14

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 17 | **polish-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (165)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 87 |
| 3 | Degraded language (grammar, spelling, terminology) | 71 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "your device’s" is narrowed to "mobileszköz" (mobile device) unlike the parallel strings using "eszköz".
    - Current: `ellenőrizze a mobileszköz adat- vagy Wi-Fi kapcsolatát`
    - Source: `{ <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If you are unable to load any pages, check your device’s data or Wi-Fi connection.{ </li> } { </ul> }`
    - Suggest: `ellenőrizze az eszköz adat- vagy Wi-Fi kapcsolatát`
    - The source says "your device’s data or Wi-Fi connection"; the same sentence elsewhere in this file is translated "az eszköz", so "mobileszköz" adds content and is inconsistent.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "Is your device or network protected by a firewall or proxy?" is translated as "számítógépe" (your computer).
    - Current: `Lehetséges, hogy tűzfal vagy proxy mögött van a számítógépe vagy a helyi hálózata?`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Lehetséges, hogy tűzfal vagy proxy mögött van az eszköze vagy a hálózata?`
    - The source refers to the device, not a computer; this is a mobile browser error page.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "device" is translated as "számítógép" (computer) in a mobile browser string.
    - Current: `Csatlakoztatva van a számítógép a hálózathoz?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Csatlakoztatva van az eszköz a hálózathoz?`
    - The source says "Is the device connected to an active network?"; "számítógép" means computer, which is wrong on Android and diverges from the source term "device".
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "The browser has canceled the request" is rendered as "a böngésző nem engedélyezi ezt a lekérést" (does not allow), changing the meaning/tense.
    - Current: `A böngésző nem engedélyezi ezt a lekérést az Ön védelme és biztonsága érdekében.`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `A böngésző megszakította a kérést az Ön védelme és biztonsága érdekében.`
    - Source states the browser has canceled the request (past, completed action), not that it disallows it.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "disabled or blocked cookies" is reduced to only "letiltotta", dropping one alternative.
    - Current: `Letiltotta a webhely által megkövetelt sütiket?`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `Kikapcsolta vagy letiltotta a webhely által megkövetelt sütiket?`
    - Source lists two actions ("disabled or blocked"); the translation conveys only one.
- `mozac_browser_errorpages_redirect_loop_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Active "isn’t redirecting properly" turned into passive "nem megfelelően van átirányítva" (is not redirected properly).
    - Current: `Az oldal nem megfelelően van átirányítva`
    - Source: `The page isn’t redirecting properly`
    - Suggest: `Az oldal nem megfelelően irányít át`
    - The source says the page is doing the redirecting incorrectly; the Hungarian passive says the page is being redirected, which reverses the actor.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "device" is rendered as "számítógép" (computer).
    - Current: `Csatlakoztatva van a számítógép a hálózathoz?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Csatlakoztatva van az eszköz a hálózathoz?`
    - Source: "Is the device connected to an active network?" — "eszköz" (device) is meant, not computer.
- `mozac_browser_errorpages_unknown_socket_type_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Translation adds "a párbeszédet" (the dialogue), which is not in the source.
    - Current: `a böngésző nem tudja folytatni a párbeszédet`
    - Source: `{ <p> }The site responded to the network request in an unexpected way and the browser cannot continue.{ </p> }`
    - Suggest: `a böngésző nem tudja folytatni`
    - Source is simply "the browser cannot continue"; the added object changes the meaning.
- `mozac_feature_addons_permissions_data_collection_browsingActivity_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "browsing activity" is translated as "Böngészési információk" (browsing information) instead of "böngészési tevékenység".
    - Current: `Böngészési információk megosztása a kiegészítő fejlesztőjével`
    - Source: `Share browsing activity with extension developer`
    - Suggest: `Böngészési tevékenység megosztása a kiegészítő fejlesztőjével`
    - Source says "Share browsing activity"; the corresponding short description uses "böngészési tevékenység", so the long form is inconsistent and imprecise.
- `mozac_feature_addons_permissions_data_collection_financialAndPaymentInfo_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — The long description drops "and payment" from "financial and payment information".
    - Current: `Pénzügyi információk megosztása a kiegészítő fejlesztőjével`
    - Source: `Share financial and payment information with extension developer`
    - Suggest: `Pénzügyi és fizetési információk megosztása a kiegészítő fejlesztőjével`
    - Source is "Share financial and payment information with extension developer"; the short description correctly uses "pénzügyi és fizetési információk", so the long form is missing part of the meaning and inconsistent.
- `mozac_feature_addons_permissions_data_collection_personalCommunications_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "personal communications" is rendered as "személyes információk" (personal information) instead of "személyes kommunikáció".
    - Current: `Személyes információk megosztása a kiegészítő fejlesztőjével`
    - Source: `Share personal communications with extension developer`
    - Suggest: `Személyes kommunikáció megosztása a kiegészítő fejlesztőjével`
    - Source says "Share personal communications"; the matching short description correctly uses "személyes kommunikáció", so this states a different data category.
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — Singular "extension developer" is rendered as plural "kiegészítőfejlesztőkkel", inconsistent with all sibling strings.
    - Current: `Műszaki és interakciós adatok megosztása a kiegészítőfejlesztőkkel`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `Műszaki és interakciós adatok megosztása a kiegészítő fejlesztőjével`
    - Source is "with extension developer" (singular); every other data collection long description uses "a kiegészítő fejlesztőjével".
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "Extend developer tools" is mistranslated as "opening" the developer tools.
    - Current: `Fejlesztőeszközök kinyitása, hogy elérje a nyitott lapokon lévő adatokat`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `Fejlesztőeszközök kiterjesztése, hogy elérjék a nyitott lapokon lévő adatokat`
    - The source means extending (adding to) the developer tools, not opening them; "kinyitása" says the extension opens the devtools.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "Extend developer tools" is mistranslated as "opening" the developer tools.
    - Current: `Fejlesztőeszközök kinyitása, hogy elérje a nyitott lapokon lévő adatokat.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Fejlesztőeszközök kiterjesztése, hogy elérjék a nyitott lapokon lévő adatokat.`
    - The source means extending (adding to) the developer tools, not opening them.
- `mozac_feature_addons_permissions_sites_in_domain_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "sites" is translated as "lapok" (tabs) instead of "oldalak" (sites).
    - Current: `Az adatai elérése a(z) %1$s tartományban lévő lapokhoz`
    - Source: `Access your data for sites in the %1$s domain`
    - Suggest: `Az adatai elérése a(z) %1$s tartományban lévő oldalakhoz`
    - The source refers to web sites in a domain; "lap" means browser tab in Firefox terminology, and other strings in this batch use "oldal"/"weboldal" for site.
- `mozac_feature_addons_permissions_sites_in_domain_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "sites" is translated as "lapokhoz" (tabs) instead of "oldalakhoz" (sites).
    - Current: `Az adatai elérése a(z) %1$s tartományban lévő lapokhoz.`
    - Source: `Access your data for sites in the %1$s domain.`
    - Suggest: `Az adatai elérése a(z) %1$s tartományban lévő oldalakhoz.`
    - The source refers to web sites in a domain; "lap" is the Firefox term for tab, inconsistent with the other site strings that use "oldal".
- `mozac_feature_customtabs_menu_button` — `mozilla-mobile/android-components/components/feature/customtabs/src/main/res/values-hu/strings.xml` — "More options" is rendered as "További beállítások" (more settings) instead of "További lehetőségek".
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The source is "More options" for the overflow menu button; "beállítások" means "settings", which names a different concept.
- `mozac_feature_passwords_importer_dialog_description` — `mozilla-mobile/android-components/components/feature/password-importer/src/main/res/values-hu/strings.xml` — "It should only take a few seconds" translated without the hedging "should only" and misses the sense of duration limit.
    - Current: `Csak néhány másodpercig tart.`
    - Source: `Keep this screen open. It should only take a few seconds.`
    - Suggest: `Ez várhatóan csak néhány másodpercig tart.`
    - Source expresses expectation ("should only take"), the target states it as fact.
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — Plural "files" rendered as singular "Fájl".
    - Current: `Fájl feltöltése?`
    - Source: `Upload files?`
    - Suggest: `Feltölti a fájlokat?`
    - Source is "Upload files?" (plural); the Hungarian says a single file.
- `mozac_feature_prompts_identity_credentials_choose_account_for_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — "Sign in with a %1$s account" is rendered as "sign in to your %1$s account", changing the meaning.
    - Current: `Jelentkezzen be a %1$s-fiókjába`
    - Source: `Sign in with a %1$s account`
    - Suggest: `Jelentkezzen be egy %1$s-fiókkal`
    - The source says to sign in *with* a provider account (the provider is the means of login), not to sign in *into* that account; the Hungarian also drops the required a(z) article handling for a placeholder.
- `mozac_feature_prompts_suggest_strong_password_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — "Use strong password?" translated as a second-person question "Erős jelszót használ?" which asks whether the user uses one, rather than offering the action.
    - Current: `Erős jelszót használ?`
    - Source: `Use strong password?`
    - Suggest: `Használ erős jelszót?`
    - The dialog offers to use the generated strong password; the Hungarian word order states rather than asks the offer, and is inconsistent with the sibling string "Erős jelszó használata".
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — The word "Relay" is duplicated because the placeholder already contains "Firefox Relay".
    - Current: `A %s Relay e-mail-maszkok`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `A %s e-mail-maszkok`
    - The developer comment states %s is the service name "Firefox Relay", so adding "Relay" after the placeholder yields "Firefox Relay Relay".
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The translated example scheme is „https:” instead of „https://”.
    - Current: `„https:” vagy „http://”`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `„https://” vagy „http://”`
    - Source says the web address must contain “https://” or “http://”; the Hungarian drops the slashes from the first variant, giving incorrect guidance.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Department" as an administrative division (Nicaragua, Colombia) is rendered as "Részleg" (department of an organization).
    - Current: `Részleg`
    - Source: `Department`
    - Suggest: `Megye`
    - The developer comment states this is an address field for the administrative division "departamento"; "Részleg" means a section/unit of an organization, not a territorial division.
- `addresses_neighborhood` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Neighborhood" as an address subdivision is translated as "Szomszédság" (the abstract state of being neighbors).
    - Current: `Szomszédság`
    - Source: `Neighborhood`
    - Suggest: `Városrész`
    - In an address form the field designates a district/quarter (colonia, mahalle); "Szomszédság" does not name a place in Hungarian.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Post town" is translated as "Postaállomás" (post station/office), not the town name used in postal addresses.
    - Current: `Postaállomás`
    - Source: `Post town`
    - Suggest: `Postaváros`
    - The source refers to the postal town component of an address (UK/Norway/Sweden), not a post office facility.
- `ai_controls_block_ai_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The translation drops "AI" from "AI enhancements", saying only "the app's new or current enhancements".
    - Current: `nem fogja látni a %s új vagy jelenlegi fejlesztéseit`
    - Source: `Blocking means you won’t see new or current AI enhancements in %s, or pop-ups about them.`
    - Suggest: `nem fogja látni a %s új vagy jelenlegi MI funkcióbővítéseit`
    - Source is "you won’t see new or current AI enhancements in %s"; the Hungarian omits "AI" and uses "fejlesztéseit" instead of the established "MI funkcióbővítések" used in the sibling strings.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Unblock specific features below" is rendered as an instruction to use the controls below, adding content not in the source.
    - Current: `Egy adott funkció blokkolásának feloldásához használja az alábbi vezérlőket.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Az egyes funkciók blokkolását alább oldhatja fel.`
    - The source sentence is an imperative "Unblock specific features below."; the translation invents "use the controls below".
- `bookmark_save_in_label` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Save in" label is translated as "Mentés máshová…" (Save elsewhere…), which says something different from the source.
    - Current: `Mentés máshová…`
    - Source: `Save in`
    - Suggest: `Mentés ide:`
    - The source is a label indicating which folder the bookmark will be saved in; "Mentés máshová…" means "Save somewhere else…" and adds an ellipsis not in the source.
- `browser_menu_bookmark_this_page_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Bookmark page" is translated as "Lap könyvjelzőzése" (bookmark tab) instead of referring to the page.
    - Current: `Lap könyvjelzőzése`
    - Source: `Bookmark page`
    - Suggest: `Oldal könyvjelzőzése`
    - The source refers to the currently visited page ("page"), which in Hungarian Firefox is "oldal"; "lap" is the term used for "tab".
- `browser_menu_powered_by2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Powered by %1$s" is rendered as a literal idiom about being "under the hood", losing the source meaning.
    - Current: `A motorháztető alatt: %1$s`
    - Source: `Powered by %1$s`
    - Suggest: `Működteti: %1$s`
    - The source states the tab is powered by the app; "A motorháztető alatt" ("under the hood") says something different.
- `certificate_warning_homepage_card_hcw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The Hungarian says "less than 7 days ago" instead of "less than 7 days left to update".
    - Current: `Kevesebb mint 7 napja van a frissítésre`
    - Source: `Less than 7 days to left to update`
    - Suggest: `Kevesebb mint 7 nap van hátra a frissítésre`
    - "7 napja van" reads as "it has been 7 days"/ambiguous; the source means there are fewer than 7 days remaining to update.
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "will stop working" rendered as "will not work properly", weakening the meaning, and "some features" expanded to "some other features".
    - Current: `A kiegészítők és egyes egyéb funkciók március 14-től nem fognak megfelelően működni.`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `A kiegészítők és egyes funkciók március 14-én leállnak.`
    - The source says add-ons and some features will stop working, not that they will work improperly; "egyéb" (other) is also not in the source.
- `close_tab_and_delete_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Singular "tab" translated as plural "lapokat".
    - Current: `Bezárja a lapokat és törli a csoportot?`
    - Source: `Close tab and delete group?`
    - Suggest: `Bezárja a lapot és törli a csoportot?`
    - Source is "Close tab and delete group?" — singular tab (the last tab), but the target uses the plural "lapokat".
- `content_description_menu` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "More options" translated as "További beállítások" (More settings).
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The source says "More options" (the three-dot menu), not settings; "beállítások" means settings and is the established translation of "Settings".
- `create_collection_view` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Snackbar action "View" (a verb/action) is translated as the noun "Nézet" (a view/layout).
    - Current: `Nézet`
    - Source: `View`
    - Suggest: `Megtekintés`
    - The developer comment says this is a snackbar action to view the collection just created; Hungarian "Nézet" means "view" as in a display mode, not the action of viewing.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The clause "from being accessed if someone else has your device" is rendered as "hogy megvédje ... ha valaki hozzáfér az eszközéhez", losing the negation/protection sense.
    - Current: `hogy megvédje a mentett fizetési módjait, ha valaki hozzáfér az eszközéhez`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `hogy megvédje a mentett fizetési módjait az illetéktelen hozzáféréstől, ha valaki más kezébe kerül az eszköze`
    - The source means protecting the data from being accessed by someone who has the device; the Hungarian reads as protecting the payment methods in case someone accesses the device, dropping what they are protected from.
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The Hungarian adds "is" ("also"), which is not in the source.
    - Current: `hogy megakadályozza a feltételezett ujjlenyomat-készítőket is.`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `hogy megakadályozza a feltételezett ujjlenyomat-készítőket.`
    - Source: "to stop suspected fingerprinters." There is no "also" in the English text; the added "is" changes the meaning.
- `history_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Search history" (imperative: search the history) is rendered as "Keresés előzményei" ("search history" as in history of searches).
    - Current: `Keresés előzményei`
    - Source: `Search history`
    - Suggest: `Keresés az előzményekben`
    - The developer comment says this is placeholder text in the search bar for searching history; the Hungarian genitive construction means "history of searches", the opposite content.
- `ip_protection_get_started` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Button label "Get started" is rendered as a noun phrase "Kezdő lépések" ("First steps") instead of an action label.
    - Current: `Kezdő lépések`
    - Source: `Get started`
    - Suggest: `Kezdés`
    - The developer comment says this is the label for the button that starts the VPN authentication flow; "Kezdő lépések" means "getting-started steps", not the call to action "Get started".
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "more private" is translated as "biztonságosabb" (more secure) instead of "privátabb".
    - Current: `hogy a böngészés biztonságosabb legyen`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `hogy a böngészése privátabb legyen`
    - The source says "make your browsing more private"; the parallel string ip_protection_settings_description correctly uses "privátabb". "Biztonságosabb" means "safer/more secure", a different claim.
- `likert_scale_option_7` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "I don't use search on Firefox" is rendered as "I don't use a search engine in Firefox", changing the meaning.
    - Current: `Nem használok keresőt a Firefoxban`
    - Source: `I don’t use search on Firefox`
    - Suggest: `Nem használok keresést a Firefoxban`
    - The source refers to not using the search feature, not to a "kereső" (search engine).
- `logins_warning_dialog_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The translation drops "from being accessed", turning the condition into simply "if someone accesses your device" and losing the protection sense.
    - Current: `hogy megvédje a mentett jelszavait, ha valaki hozzáfér az eszközéhez`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved passwords from being accessed if someone else has your device.`
    - Suggest: `hogy megvédje a mentett jelszavait az illetéktelen hozzáféréstől, ha valaki más kezébe kerül az eszköze`
    - Source: protect saved passwords from being accessed if someone else has your device; the Hungarian omits what is being protected against.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "that you use it" is mistranslated as "how you use it", changing the meaning of what data is shared.
    - Current: `hogy miként fedezte fel, és hogyan használja a Firefoxot`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `hogy miként fedezte fel a Firefoxot, és hogy használja azt`
    - The source says the shared data is the fact that the user uses Firefox, not how they use it; "hogyan használja" implies usage details are shared.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "that you use it" is mistranslated as "how you use it", changing the meaning of what data is shared.
    - Current: `hogy miként fedezte fel, és hogyan használja a Firefoxot`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a Firefoxot, és hogy használja azt`
    - The source shares the fact of usage, not the manner of usage.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "won't sell you out" is rendered as "nem adja el" ("doesn't sell it"), losing the object/meaning of not betraying the user.
    - Current: `Gyors, biztonságos, és nem adja el.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Gyors, biztonságos, és nem árulja el Önt.`
    - The source means the browser will not betray/sell out the user; the Hungarian says only "does not sell (it)" with a missing object, which reads as incomplete and different in meaning.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "and that you use it" is mistranslated as "and how you use it".
    - Current: `hogy miként fedezte fel, és hogyan használja a Firefoxot`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a Firefoxot, és hogy használja azt`
    - The source shares the fact that the user uses Firefox, not how they use it; "hogyan használja" claims usage-behaviour data is shared.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "and that you use it" is mistranslated as "and how you use it".
    - Current: `hogy miként fedezte fel, és hogyan használja a Firefoxot`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a Firefoxot, és hogy használja azt`
    - The source shares only the fact of usage, not how the user uses Firefox; the Hungarian misstates what data is shared.
- `onboarding_preferences_dialog_usage_data_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "hardware configuration" is translated as "hardverbeállítások" (hardware settings).
    - Current: `a hardverbeállításokra`
    - Source: `Data about your device, hardware configuration, and how you use Firefox helps improve features, performance, and stability for everyone.`
    - Suggest: `a hardverkonfigurációra`
    - "Hardware configuration" refers to the device's hardware makeup, not user-adjustable hardware settings.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The confirm button "Open tabs" (imperative action) is translated as the noun phrase "Nyitott lapok" ("open tabs" as in currently open tabs).
    - Current: `Nyitott lapok`
    - Source: `Open tabs`
    - Suggest: `Lapok megnyitása`
    - The developer comment says this is the dialog button for confirming opening all tabs, so it is a verb phrase; "Nyitott lapok" means "tabs that are open".
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Battery Saver" is rendered as "Energiagazdálkodás" (power management) instead of the Android "Akkumulátorkímélő mód" feature name.
    - Current: `Energiagazdálkodás által beállítva`
    - Source: `Set by Battery Saver`
    - Suggest: `Akkumulátorkímélő mód által beállítva`
    - The source refers to Android's Battery Saver mode, not general power management; the theme follows the Battery Saver setting.
- `preference_downloads_folder_permission_lost` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "this folder" rendered as "a mappa" instead of "ez a mappa".
    - Current: `Nincs jogosultsága a mappa használatára.`
    - Source: `You don’t have permission to use this folder. Try choosing a different one.`
    - Suggest: `Nincs jogosultsága ennek a mappának a használatára.`
    - The source specifies "this folder" (the previously selected custom folder); the translation loses the demonstrative.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "will cause websites to break" translated with an added "egyes" (some), weakening the statement inconsistently with option 3.
    - Current: `Összes süti (egyes weboldalakon hibát fog okozni)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `Összes süti (a weboldalak el fognak törni)`
    - Source states unconditionally that websites will break; the added "egyes" (some) changes the meaning and duplicates the hedging used for the "may cause" option.
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "faster performance" is rendered as "jobb teljesítmény" (better performance).
    - Current: `jobb teljesítmény`
    - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
    - Suggest: `gyorsabb teljesítmény`
    - The source says "faster performance", not "better performance".
- `preferences_addresses_save_and_autofill_addresses_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Includes phone numbers and email addresses" is rendered as "Telefonszámok és e-mail-címek belevétele" (an action "including ...") instead of a statement that it includes them.
    - Current: `Telefonszámok és e-mail-címek belevétele`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Tartalmazza a telefonszámokat és az e-mail-címeket`
    - The source is a descriptive summary stating that the feature covers phone numbers and email addresses; the Hungarian nominalized form reads as a command/action label, changing the meaning.
- `preferences_link_sharing` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Link sharing" is rendered as "Megosztási hivatkozás" (sharing link), reversing the head noun.
    - Current: `Megosztási hivatkozás`
    - Source: `Link sharing`
    - Suggest: `Hivatkozásmegosztás`
    - The source names the feature of sharing links; the translation says "sharing link", i.e. a link used for sharing, which is a different concept.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "that you use it" is mistranslated as "hogyan használja" (how you use it), which the developer comment explicitly warns against.
    - Current: `hogy miként fedezte fel, és hogyan használja a Firefoxot`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `hogy miként fedezte fel a Firefoxot, és hogy használja azt`
    - The comment states “That you use it” means the user shares the fact that they continue to use Firefox, not usage details; "hogyan használja" says the opposite.
- `preferences_show_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The verb "Show" is dropped, making the label inconsistent with the neighbouring "… megjelenítése" preference titles.
    - Current: `Keresési javaslatok`
    - Source: `Show search suggestions`
    - Suggest: `Keresési javaslatok megjelenítése`
    - Source is "Show search suggestions"; sibling strings (Show clipboard suggestions, Show recent searches, Show trending suggestions, Show voice search) all keep "megjelenítése". Here the action word is missing.
- `preferences_show_sponsored_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Suggestions from sponsors" is translated as "Szponzorált javaslatok" (sponsored suggestions), losing the "from sponsors" source meaning and duplicating the summary's wording.
    - Current: `Szponzorált javaslatok`
    - Source: `Suggestions from sponsors`
    - Suggest: `Javaslatok szponzoroktól`
    - The source names the source of the suggestions (sponsors), parallel to "Suggestions from %1$s" which is correctly rendered as "Javaslatok a következőtől: %1$s".
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Source says Firefox will improve features, performance and stability; the target says it will install modifications affecting them.
    - Current: `A Firefox funkciókat, teljesítményt és stabilitást érintő módosításokat fog telepíteni a frissítések között.`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `A Firefox javítja a funkciókat, a teljesítményt és a stabilitást a frissítések között.`
    - "improve features, performance, and stability" is not "install modifications affecting …"; the meaning is altered.
- _…and 28 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_file_access_denied_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Missing comma in "Lehet hogy".
    - Current: `Lehet hogy törölve lett`
    - Source: `{ <ul> } { <li> }It may have been removed, moved, or file permissions may be preventing access.{ </li> } { </ul> }`
    - Suggest: `Lehet, hogy törölve lett`
    - Hungarian requires a comma before the subordinating "hogy".
- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Adverb missing suffix: "ideiglenes" should be "ideiglenesen".
    - Current: `Az oldal ideiglenes nem érhető el`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `Az oldal ideiglenesen nem érhető el`
    - "temporarily unavailable" requires the adverb "ideiglenesen"; the adjective form is ungrammatical here.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Adverb missing suffix: "ideiglenes" should be "ideiglenesen".
    - Current: `Az oldal ideiglenes nem érhető el`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `Az oldal ideiglenesen nem érhető el`
    - "temporarily unavailable" requires the adverb "ideiglenesen".
- `mozac_browser_errorpages_safe_browsing_malware_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Missing linking element in the compound noun phrase.
    - Current: `Kártékony szoftvert terjesztő webhely probléma`
    - Source: `Malware site issue`
    - Suggest: `Kártékony szoftvert terjesztő webhely miatti probléma`
    - "webhely probléma" is ungrammatical juxtaposition in Hungarian; compare the correctly formed sibling string "Nem kívánt webhely miatti probléma".
- `mozac_browser_errorpages_safe_harmful_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Missing linking element in the compound noun phrase.
    - Current: `Káros webhely probléma`
    - Source: `Harmful site issue`
    - Suggest: `Káros webhely miatti probléma`
    - "webhely probléma" is an ungrammatical noun juxtaposition; the parallel string uses "webhely miatti probléma".
- `mozac_browser_errorpages_safe_phishing_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — Missing linking element in the compound noun phrase.
    - Current: `Félrevezető oldal probléma`
    - Source: `Deceptive site issue`
    - Suggest: `Félrevezető oldal miatti probléma`
    - "oldal probléma" is an ungrammatical juxtaposition; the parallel string uses "... miatti probléma".
- `mozac_browser_awesomebar_stock_suggestion_decrease` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-hu/strings.xml` — Case mismatch: "%s százalékot csökkent" should be "%s százalékkal csökkent".
    - Current: `%s százalékot csökkent`
    - Source: `Dropped %s percent`
    - Suggest: `%s százalékkal csökkent`
    - "Dropped %s percent" expresses a decrease by a percentage; the Hungarian verb "csökkent" requires "-kal/-kel" ("százalékkal"), not the accusative.
- `mozac_browser_awesomebar_stock_suggestion_increase` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-hu/strings.xml` — Case mismatch: "%s százalékot nőtt" uses the accusative with an intransitive verb; should be "%s százalékkal nőtt".
    - Current: `%s százalékot nőtt`
    - Source: `Gained %s percent`
    - Suggest: `%s százalékkal nőtt`
    - "Gained %s percent" means the value rose by that percentage; Hungarian requires the instrumental-comitative case ("százalékkal") with "nőtt". The parallel string uses "csökkent", which likewise takes "-kal/-kel".
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — Plural "kiegészítőfejlesztőkkel" does not match the singular "extension developer" used in the source and in the parallel websiteContent string.
    - Current: `a kiegészítőfejlesztőkkel`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `a kiegészítő fejlesztőjével`
    - Source is singular "extension developer"; the sibling string mozac_feature_addons_permissions_data_collection_websiteContent_long_description uses "a kiegészítő fejlesztőjével".
- `mozac_feature_addons_permissions_proxy_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — Compound noun written as separate words, inconsistent with the _for_update variant.
    - Current: `Böngésző proxy beállítások vezérlése`
    - Source: `Control browser proxy settings`
    - Suggest: `Böngésző proxybeállításainak vezérlése`
    - Hungarian orthography requires "proxybeállítások" as one word; the parallel string mozac_feature_addons_permissions_proxy_description_for_update already uses that form.
- `mozac_feature_autofill_search_suggestions` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-hu/strings.xml` — Missing case ending/hyphen: "%1$s keresés" is ungrammatical for "Search %1$s".
    - Current: `%1$s keresés`
    - Source: `Search %1$s`
    - Suggest: `Keresés a(z) %1$s alkalmazásban`
    - The source is an imperative list item "Search Firefox"; the Hungarian noun phrase "%1$s keresés" reads as "Firefox search" and lacks any case marking, unlike the parallel strings which use "… keresése" or a prepositional construction.
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — Possessive suffix mismatch: "Adatvédelmi irányelvek" and "Szolgáltatási feltételei" are inconsistent, and the possessive form is ungrammatical here.
    - Current: `Szolgáltatási feltételei`
    - Source: `Logging in to %1$s with a %2$s account is subject to their <a href="%3$s">Privacy Policy{ </a> } and <a href="%4$s">Terms of Service{ </a> }`
    - Suggest: `Szolgáltatási feltételek`
    - The sentence subject is "az Adatvédelmi irányelvek és a Szolgáltatási feltételek ... vonatkoznak"; the third-person possessive -i on "feltételei" does not agree with the coordinated non-possessive "Adatvédelmi irányelvek".
- `mozac_protections_dashboard_trackers_blocked_this_week_title` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-hu/strings.xml` — Plural "Trackers blocked" rendered as singular subject without plural marking, reading oddly as a header.
    - Current: `Nyomkövető blokkolva a héten`
    - Source: `Trackers blocked this week`
    - Suggest: `Blokkolt nyomkövetők a héten`
    - The source is a plural noun phrase title "Trackers blocked this week"; the Hungarian reads like a fragment of a count sentence with the number missing.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hu/strings.xml` — Missing hyphen before the suffix attached to the app-name placeholder.
    - Current: `a %1$sban`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `a %1$s-ban`
    - In Hungarian, a case suffix appended to a placeholder holding a proper/brand name (Firefox, Focus) must be joined with a hyphen: "a Firefox-ban"/"a %1$s-ban". Written solid as "%1$sban" it renders as "Firefoxban" without the required separator used elsewhere for placeholder-based names.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hu/strings.xml` — Relative pronoun does not agree in number with its plural antecedent.
    - Current: `oldalösszegzéseket tud készíteni, amelyet továbbra is Ön irányít`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `oldalösszegzéseket tud készíteni, amelyeket továbbra is Ön irányít`
    - The antecedent "oldalösszegzéseket" is plural (source: "page summaries that stay in your control"), so the pronoun must be "amelyeket", not the singular "amelyet".
- `mozac_summarize_shake_consent_off_device_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hu/strings.xml` — Missing hyphen before the suffix attached to the app-name placeholder.
    - Current: `a %1$stól`
    - Source: `Shake your device, get a page summary from %1$s in seconds.`
    - Suggest: `a %1$s-tól`
    - In Hungarian a suffix appended to a placeholder standing for a proper name (Firefox) must be joined with a hyphen; other strings would render "Firefoxtól" incorrectly glued. Standard Mozilla hu practice is "%1$s-tól".
- `alternative_app_icon_group_solid_colors` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Egyszínű színek" is a redundant/incorrect rendering of "Solid colors".
    - Current: `Egyszínű színek`
    - Source: `Solid colors`
    - Suggest: `Egyszínű háttér`
    - "Egyszínű" already means "solid-colored", so "Egyszínű színek" reads as "solid-colored colors"; a natural rendering is needed for this group title.
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Misspelled "rendeleteben" instead of "rendeletben".
    - Current: `Az (EU) 2024/1183 rendeleteben meghatározottak szerint.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Az (EU) 2024/1183 rendeletben meghatározottak szerint.`
    - The Hungarian inessive form of "rendelet" is "rendeletben"; "rendeleteben" is a spelling error.
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Misspelled/mis-suffixed word "megtekintéshez" written as "megtekintéshez" with missing possessive: "megtekintéshez" should be "megtekintéséhez".
    - Current: `Feloldás a mentett kártyák megtekintéshez`
    - Source: `Unlock to view your saved cards`
    - Suggest: `Feloldás a mentett kártyák megtekintéséhez`
    - Hungarian requires the possessive form "kártyák megtekintéséhez" (viewing of the cards); the current form is ungrammatical.
- `debug_drawer_addons_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Add-ons Tools" is rendered with a possessive suffix, producing "the add-on's tools" instead of "add-on tools".
    - Current: `Kiegészítői eszközök`
    - Source: `Add-ons Tools`
    - Suggest: `Kiegészítőeszközök`
    - The source is a compound noun "Add-ons Tools" (tools for add-ons); "Kiegészítői" is a possessive/adjectival form that is ungrammatical here. Compare the sibling strings "Régióeszközök" and "Automatikus kitöltési eszközök".
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Register inconsistency: formal "Próbálja ki" is followed by informal verb form "kapj".
    - Current: `Próbálja ki most, hogy korlátlan sávszélességet kapj %1$s-ig.`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `Próbálja ki most, hogy korlátlan sávszélességet kapjon %1$s-ig.`
    - The string uses the formal address ("Kapcsolja be", "Próbálja ki") but switches to the informal second-person "kapj", which is both a register violation and a grammatical mismatch.
- `likert_scale_option_i_plan_to_keep_using` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Word order gives a contrastive focus reading ("It's Firefox I plan to keep using") instead of the neutral source meaning.
    - Current: `Továbbra is a Firefoxot tervezem használni`
    - Source: `I plan to keep using Firefox`
    - Suggest: `Tervezem, hogy továbbra is a Firefoxot használom`
    - The source is a plain statement of intent to keep using Firefox; the Hungarian focus structure distorts it.
- `logins_biometric_prompt_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Missing possessive suffix: "megtekintéshez" should be "megtekintéséhez".
    - Current: `Feloldás a mentett jelszavak megtekintéshez`
    - Source: `Unlock to view your saved passwords`
    - Suggest: `Feloldás a mentett jelszavak megtekintéséhez`
    - The noun phrase "a mentett jelszavak megtekintése" requires the possessive form; "megtekintéshez" is ungrammatical here.
- `microsurvey_app_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Compound spelled as two words; Hungarian requires "Firefox logó" to be hyphenated as "Firefox-logó".
    - Current: `Firefox logó`
    - Source: `Firefox logo`
    - Suggest: `Firefox-logó`
    - Hungarian orthography joins a proper-name attribute to the noun with a hyphen (cf. "WhatsApp-megosztásokhoz" used in this same batch).
- `nova_onboarding_tou_body_line_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The definite article does not agree with the link text inserted at %1$s ("Adatvédelmi nyilatkozat" begins with a consonant).
    - Current: `További információk az %1$sunkban.`
    - Source: `Firefox cares about your privacy. Learn more in our %1$s.`
    - Suggest: `További információk a %1$sunkban.`
    - The placeholder is replaced by "Adatvédelmi nyilatkozat", which starts with a consonant, so the article must be "a", not "az".
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Bullet point is translated as an imperative/3rd-person verb form, inconsistent with the parallel bullet in preference_doh_default_protection_info_2 which uses the noun form.
    - Current: `Csak akkor használja az alapértelmezett DNS-feloldót, ha probléma van a biztonságos DNS-sel`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `Az alapértelmezett DNS-feloldó használata csak akkor, ha probléma van a biztonságos DNS-sel`
    - The equivalent bullet lists use nominal constructions ("Alapértelmezett DNS-feloldó használata, ha…"); here the sentence reads as an instruction to the user, changing who performs the action.
- `preference_doh_max_protection_info_3` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Negation not distributed correctly: "nem fognak betöltődni és működni" reads awkwardly; source means sites will not load or will not work properly.
    - Current: `akkor a webhelyek nem fognak betöltődni és működni`
    - Source: `If secure DNS is not available sites will not load or function properly`
    - Suggest: `akkor a webhelyek nem fognak betöltődni, vagy nem fognak megfelelően működni`
    - The source "sites will not load or function properly" negates both alternatives; the Hungarian also drops "properly" (megfelelően).
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Spelling/agreement error: "lássak" should be "lássák", and the object phrase is mismatched in number/person.
    - Current: `hogy lássak, hogy melyik weboldalakat éri el`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `hogy lássák, melyik weboldalt készül elérni`
    - The source says "making it harder for others to see which website you’re about to access"; "lássak" (I see) is a misspelling of "lássák" (they see), and "melyik weboldalakat" mixes singular "melyik" with plural noun.
- `preference_option_autoplay_allowed_wifi_only2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "mobil-adatkapcsolaton" is misspelled with a hyphen.
    - Current: `mobil-adatkapcsolaton`
    - Source: `Block audio and video on cellular data only`
    - Suggest: `mobiladat-kapcsolaton`
    - Hungarian orthography: the compound is "mobiladat-kapcsolat"; "mobil-adatkapcsolaton" is not a correct hyphenation.
- `preferences_ai_controls` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "MI vezérlők" should be a compound written as one word or hyphenated per Hungarian orthography.
    - Current: `MI vezérlők`
    - Source: `AI controls`
    - Suggest: `MI-vezérlők`
    - An abbreviation modifying a noun forms a compound requiring a hyphen in Hungarian (cf. "Mozilla-fiók" in the same batch).
- `preferences_crashes_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Wrong definite article before a vowel-initial word.
    - Current: `a összeomlás-jelentésekről`
    - Source: `Learn more about crash reports`
    - Suggest: `az összeomlás-jelentésekről`
    - Hungarian requires "az" before words beginning with a vowel ("összeomlás").
- `preferences_delete_browsing_data_site_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Compound noun written as two words instead of one.
    - Current: `Webhely engedélyek`
    - Source: `Site permissions`
    - Suggest: `Webhelyengedélyek`
    - "Site permissions" is a compound; Hungarian orthography requires it written as one word (or hyphenated), not as two separate words.
- `preferences_enable_gecko_logs` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Gecko naplók" should be hyphenated as a compound with a proper name.
    - Current: `Gecko naplók engedélyezése`
    - Source: `Enable Gecko logs`
    - Suggest: `Gecko-naplók engedélyezése`
    - Hungarian orthography requires a hyphen when a proper name is combined with a common noun (Gecko-naplók).
- `preferences_marketing_data_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Kampány mérési adatai" is incorrectly spaced/compounded for "Campaign measurement data".
    - Current: `Kampány mérési adatai`
    - Source: `Campaign measurement data`
    - Suggest: `Kampánymérési adatok`
    - The compound "kampánymérési" should be written as one word (cf. "Kampánymérés" in preferences_marketing_data_title), and the source is a plain noun phrase, not a possessive.
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Typo: "íz" instead of "az" in the lock screen summary.
    - Current: `Lapok megtekintése íz ujjlenyomatával`
    - Source: `View tabs with your fingerprint, PIN, or face unlock. Turning this on also prevents screen capture and sharing.`
    - Suggest: `Lapok megtekintése az ujjlenyomatával`
    - The source says "View tabs with your fingerprint"; "íz" is a misspelling of the definite article "az".
- `recent_tabs_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Typo: "Öösszes" instead of "Összes".
    - Current: `Öösszes legutóbbi lap megjelenítése gomb`
    - Source: `Show all recent tabs button`
    - Suggest: `Összes legutóbbi lap megjelenítése gomb`
    - Misspelling of "Összes" with a doubled initial vowel.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "%s keresés" is ungrammatical for "Search %s" where %s is the engine name.
    - Current: `%s keresés`
    - Source: `Search %s`
    - Suggest: `Keresés ezzel: %s`
    - The source means to search using the named engine; "%s keresés" reads as a noun phrase ("%s search") and is not a correct Hungarian rendering of the action.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Missing second-person address: "You’re just 1 step away" rendered as third person "van" instead of "van".
    - Current: `Csak 1 lépésre van a célvonaltól.`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Csak 1 lépésre van a célvonaltól!`
    - Placeholder finding
- `setup_checklist_subtitle_6_steps_fifth_step` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Register/person inconsistency: first sentence uses first person plural while the second uses formal third person, and "1 lépésre van a célvonaltól" lacks the subject agreement of the source.
    - Current: `Mindjárt megvagyunk! Csak 1 lépésre van a célvonaltól.`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Mindjárt kész! Csak 1 lépésre van a célvonaltól.`
    - The source "Almost there! You're just 1 step away" addresses the user; mixing "megvagyunk" (we) with the formal "van" (you) is inconsistent within one string.
- `sports_widget_page_position_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The page-position phrasing "%2$d. / %3$d oldal" is garbled Hungarian for "page %2$d of %3$d".
    - Current: `%1$s, %2$d. / %3$d oldal`
    - Source: `%1$s, page %2$d of %3$d`
    - Suggest: `%1$s, %2$d. oldal, összesen %3$d`
    - Source reads "page %2$d of %3$d"; the target mixes an ordinal and a slash so a screen reader announces something unintelligible rather than the current page out of the total.
- `tab_crash_send_report` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Typo: "Összeomlási jelentése elküldése" contains a duplicated/incorrect possessive suffix.
    - Current: `Összeomlási jelentése elküldése a Mozillának`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Összeomlási jelentés elküldése a Mozillának`
    - The source is "Send crash report to Mozilla"; the Hungarian noun phrase should be "Összeomlási jelentés elküldése" — "jelentése" is an erroneous possessive form.
- `terms_of_use_prompt_body_line_two_alternative_link` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Link text is capitalized although it is inserted mid-sentence into the surrounding string.
    - Current: `Itt`
    - Source: `here`
    - Suggest: `itt`
    - The source "here" is lowercase and the placeholder is embedded in a sentence ("You can learn more %1$s."), so a capital letter is wrong.
- `trackers_blocked_panel_num_cross_site_cookies` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — The compound modifier is in plural ("webhelyek közötti") but should agree as "webhelyek közötti" is acceptable; the singular counted noun phrase reads awkwardly with the number.
    - Current: `%1$d webhelyek közötti nyomkövető süti`
    - Source: `{$quantity ->} [one] %1$d cross-site tracking cookie [other] %1$d cross-site tracking cookies`
    - Suggest: `%1$d webhelyközi nyomkövető süti`
    - In Hungarian a numeral is followed by a singular noun phrase; "webhelyek közötti" after a numeral is grammatically inconsistent.
- `webcompat_reporter_problem_description_placeholder_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Incorrect case/agreement: "Adjon meg a lépéseket" should be "Adja meg a lépéseket".
    - Current: `Adjon meg a lépéseket a probléma reprodukálásához.`
    - Source: `What happened? What did you expect to happen? Please provide steps to reproduce the issue.`
    - Suggest: `Adja meg a lépéseket a probléma reprodukálásához.`
    - With a definite object ("a lépéseket"), the verb must take the definite conjugation: "Adja meg", not the indefinite "Adjon meg".
- `cookie_banner_exception_panel_description_site_is_not_supported` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Grammatically broken sentence: reversed subject/object and wrong article agreement.
    - Current: `Ez az oldalt jelenleg nem támogatja a Sütibannerek számának csökkentését.`
    - Source: `This site is currently not supported by Cookie Banner Reduction. Would you like to request our team review this website and add support in the future?`
    - Suggest: `Ezt az oldalt jelenleg nem támogatja a Sütibannerek számának csökkentése.`
    - The source says the site is not supported by Cookie Banner Reduction; the Hungarian has "Ez az oldalt" (demonstrative not agreeing with the accusative noun) and makes the site the subject supporting the feature, reversing the meaning.
- `crash_report_send_crash_label` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Grammatical error: duplicated possessive suffix in "Összeomlási jelentése elküldése".
    - Current: `Összeomlási jelentése elküldése a Mozillának`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Összeomlási jelentés elküldése a Mozillának`
    - "jelentése elküldése" is ungrammatical; the source is "Send crash report to Mozilla".
- `preference_autocomplete_add_hint` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Wrong definite article before a consonant-initial word.
    - Current: `Illessze be, vagy adja meg az webcímet`
    - Source: `Paste or enter URL`
    - Suggest: `Illessze be, vagy adja meg a webcímet`
    - Hungarian uses "a" before consonant-initial words; "az webcímet" is ungrammatical.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Misspelled "rendeleteben" and the word "Qualified" (minősített) is dropped from the sentence.
    - Current: `Az (EU) 2024/1183 rendeleteben meghatározottak szerint.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Minősített az (EU) 2024/1183 rendeletben meghatározottak szerint.`
    - "rendeleteben" should be "rendeletben"; also the source states the certificate is "Qualified as specified in…", which the target omits.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Próbálja újra” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Újrapróbálkozás”
    - Current: `{ <p> }A böngésző kapcsolat nélküli módban van, ezért nem tud csatlakozni a kért elemhez.{ </p> } { <ul> } { <li> }Csatlakoztatva van a számítógép a hálózathoz?{ </li> } { <li> }Nyomja meg a „Próbálja újra” gombot az on…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Újrapróbálkozás`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mozac_browser_errorpages_security_bad_hsts_cert_back` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — "Go Back" is rendered inconsistently with the parallel bad_cert string.
    - Current: `Ugrás vissza`
    - Source: `Go Back`
    - Suggest: `Visszalépés`
    - The same source label "Go Back" is translated "Visszalépés" in mozac_browser_errorpages_security_bad_cert_back on the same error-page surface; the two buttons should match.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hu/strings.xml` — "extension" is rendered as "Bővítmény" here but as "Kiegészítő" in the non-update variant of the same permission.
    - Current: `Bővítményhasználat monitorozása és témák kezelése.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `Kiegészítőhasználat monitorozása és témák kezelése.`
    - mozac_feature_addons_permissions_management_description uses "Kiegészítőhasználat" for the identical source text; the two must be consistent.
- `webauthn_related_origin_create_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — "passkey" is rendered as "jelkód" (passcode) instead of the established Hungarian term "jelszó nélküli belépési kulcs"/"belépési kulcs".
    - Current: `jelkódot akar létrehozni`
    - Source: `%1$s wants to create a passkey for %2$s.`
    - Suggest: `belépési kulcsot akar létrehozni`
    - "jelkód" means passcode/PIN, not passkey; Mozilla Hungarian uses "belépési kulcs" for passkey.
- `webauthn_related_origin_use_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hu/strings.xml` — "passkey" is rendered as "jelkód" (passcode) instead of the established Hungarian term for passkey.
    - Current: `jelkódot akar használni`
    - Source: `%1$s wants to use a passkey for %2$s.`
    - Suggest: `belépési kulcsot akar használni`
    - "jelkód" means passcode/PIN, not passkey; Mozilla Hungarian uses "belépési kulcs" for passkey.
- `debug_drawer_fab_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "drawer" (UI panel) is translated as "fiók" (drawer of furniture/account), inconsistent with the other debug drawer strings.
    - Current: `Hibakereső fiók megnyitása`
    - Source: `Open debug drawer`
    - Suggest: `Hibakereső fiók megnyitása (egységesítendő a többi „debug drawer” fordítással)`
    - Other strings in the same feature avoid a translation of "drawer" entirely (e.g. "Navigálás visszafelé"); "fiók" is the term used for account/box and is misleading here.
- `download_item_paused_description_unknown_total_size` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "paused" is rendered as the noun "szünet" instead of "szüneteltetve", inconsistent with the parallel string.
    - Current: `%1$s • szünet`
    - Source: `%1$s • paused`
    - Suggest: `%1$s • szüneteltetve`
    - The sibling string download_item_paused_description translates the same source word "paused" as "szüneteltetve"; "szünet" (a break/pause noun) is inconsistent on the same downloads list surface.
- `download_navigate_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Content description rendered as an imperative command instead of a noun-style description of the control.
    - Current: `Navigáljon a Letöltési beállításokhoz`
    - Source: `Navigate to Downloads Settings`
    - Suggest: `Navigálás a letöltési beállításokhoz`
    - The source "Navigate to Downloads Settings" is a content description naming the button action; the parallel string download_navigate_back_description uses the noun form "Navigálás visszafelé", so the imperative here is inconsistent.
- `edit_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "login" as a stored credential entry is rendered as the action "Bejelentkezés" (signing in) instead of the saved credential.
    - Current: `Bejelentkezés szerkesztése`
    - Source: `Edit login`
    - Suggest: `Bejelentkezési adatok szerkesztése`
    - In the passwords/logins screen, "Edit login" refers to editing a saved login entry, not to the act of signing in; Hungarian Firefox uses "bejelentkezési adatok" for stored logins.
- `microsurvey_feature_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Survey" is rendered as "Felmérés" here while every other microsurvey string in the same surface uses "Kérdőív"/"felmérés" inconsistently.
    - Current: `Felmérés funkció ikonja`
    - Source: `Survey feature icon`
    - Suggest: `Kérdőív funkció ikonja`
    - microsurvey_close_handle_content_description translates "Close survey" as "Kérdőív bezárása"; the same term on the same surface should be consistent.
- `nova_onboarding_add_search_widget_button` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "widget" is translated as "modul" instead of the established Hungarian term "widget".
    - Current: `Firefox modul hozzáadása`
    - Source: `Add Firefox widget`
    - Suggest: `Firefox widget hozzáadása`
    - The Android home-screen "widget" is rendered "widget" in Hungarian Firefox/Android UI; "modul" means module and is misleading.
- `preferences_toolbar_select_shortcut` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "shortcut" is rendered as "indítóikon" (launcher icon), which is the wrong term for a toolbar shortcut.
    - Current: `Válasszon egy indítóikont`
    - Source: `Select a shortcut`
    - Suggest: `Válasszon egy parancsikont`
    - "Shortcut" here is a toolbar action shortcut, not a launcher/home-screen icon; "indítóikon" denotes an app launcher icon.
- `preferences_toolbar_shortcut` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Toolbar shortcut" is rendered with "indítóikon" (launcher icon), the wrong term.
    - Current: `Eszköztár indítóikonja`
    - Source: `Toolbar shortcut`
    - Suggest: `Eszköztár parancsikonja`
    - The shortcut is a toolbar action, not a launcher icon; "indítóikon" means app launcher icon.
- `protection_panel_num_trackers_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Trackers" is rendered as "követők" here while the surrounding protection panel strings use "nyomkövetők".
    - Current: `Blokkolt követők: %d`
    - Source: `Trackers blocked: %d`
    - Suggest: `Blokkolt nyomkövetők: %d`
    - The same source term "trackers" is translated "nyomkövető" in protection_panel_banner_protected_blocked_trackers_description and protection_panel_etp_disabled_no_trackers_blocked; "követők" (followers) is inconsistent and misleading on the same surface.
- `sports_widget_group_stage` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "Group Stage" is rendered as the redundant "Csoportkörök szakasza".
    - Current: `Csoportkörök szakasza`
    - Source: `Group Stage`
    - Suggest: `Csoportkör`
    - The established Hungarian football term for "Group Stage" is "csoportkör"; "Csoportkörök szakasza" ("the stage of the group rounds") is redundant and overly long for a widget label.
- `sports_widget_more_options_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "More options" is rendered as "További beállítások" (more settings) instead of the standard "További lehetőségek".
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The source is "More options" for an overflow menu button; "beállítások" means "settings", which is a different concept and inconsistent with the established Hungarian term for the overflow menu.
- `sports_widget_team_followed_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "tournament" is translated with the colloquial slang "vébé".
    - Current: `a vébé közeledtével`
    - Source: `Check back for match info as the tournament approaches.`
    - Suggest: `a torna közeledtével`
    - The source says "the tournament"; "vébé" is a colloquial abbreviation of "világbajnokság" that clashes with the neutral register of the UI and is not what the source says.
- `tab_group_three_dot_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — "More options" rendered as "További beállítások" (more settings) instead of "További lehetőségek".
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - "Options" here refers to menu options, not settings ("beállítások"); the established rendering for the three-dot menu content description is "További lehetőségek".
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — `firstrun_shortcut_text` quotes “Hozzáadás a kezdőképernyőre” but the string it names, `menu_add_to_home_screen`, reads “Kezdőképernyőhöz adás”
    - Current: `Térjen vissza gyorsan a kedvenc oldalaihoz a %1$sban. Csak válassza a „Hozzáadás a kezdőképernyőre” lehetőséget a %1$s menüből.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Kezdőképernyőhöz adás`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `snackbar_added_to_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "shortcuts" is rendered as "indítóikonokhoz" (launcher icons) instead of the consistent term for shortcuts.
    - Current: `Hozzáadva az indítóikonokhoz.`
    - Source: `Added to shortcuts!`
    - Suggest: `Hozzáadva a parancsikonokhoz.`
    - Other Focus strings use "parancsikon" for shortcuts; "indítóikon" is inconsistent terminology on the same surface.
- `tab_crash_report_headline` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Sorry." is translated in first person singular ("Sajnálom"), while the app speaks as "we" in the same string set.
    - Current: `Sajnálom. Probléma van ezzel a lapon.`
    - Source: `Sorry. We’re having a problem with this tab.`
    - Suggest: `Sajnáljuk. Probléma van ezzel a lappal.`
    - Source "We’re having a problem with this tab" uses first person plural; also "probléma van ezzel a lapon" should be "ezzel a lappal" (problem with the tab, not on the tab).
- `trackers_count_note` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Trackers" is rendered as "nyomkövetők" here while the neighbouring string uses "követők".
    - Current: `Blokkolt nyomkövetők %s óta`
    - Source: `Trackers blocked since %s`
    - Suggest: `Blokkolt követők %s óta`
    - The adjacent string trackers_and_scripts translates "Trackers" as "követők"; using "nyomkövetők" on the same tracking-protection surface is inconsistent terminology.

### E. Typography, punctuation & spacing

- `add_to_tab_group_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Ellipsis added that is not in the source title "Add to".
    - Current: `Hozzáadás…`
    - Source: `Add to`
    - Suggest: `Hozzáadás`
    - Source is a plain title "Add to" with no ellipsis; the added ellipsis suggests a further dialog.
- `bookmark_sort_menu_a_to_z` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Hyphen used instead of en dash / incorrect Hungarian suffix hyphenation in "A-tól Z-ig".
    - Current: `Rendezés A-tól Z-ig`
    - Source: `Sort by A to Z`
    - Suggest: `Rendezés A–Z szerint`
    - Hungarian orthography attaches suffixes to letters with a hyphen, which is used here, but the range convention in the locale uses an en dash; the string as written mixes conventions.
- `certificate_warning_push_notification_pnw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Period added to a notification title that has no final punctuation in the source.
    - Current: `A Firefox egy régebbi verzióját használja.`
    - Source: `You’re on an older version of Firefox`
    - Suggest: `A Firefox egy régebbi verzióját használja`
    - The source title "You’re on an older version of Firefox" has no terminal punctuation; titles in this set (e.g. "Frissítés javasolt") are unpunctuated.
- `micro_survey_feedback_confirmation` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Exclamation mark of the source replaced with a period.
    - Current: `Köszönjük visszajelzését.`
    - Source: `Thanks for your feedback!`
    - Suggest: `Köszönjük a visszajelzését!`
    - Source "Thanks for your feedback!" ends with an exclamation mark.
- `nova_onboarding_tou_body_line_3` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Superfluous comma between the adverbial phrase and the subject.
    - Current: `A böngésző fejlesztése érdekében, a Firefox`
    - Source: `To help improve the browser, Firefox sends diagnostic and interaction data to Mozilla. %1$s`
    - Suggest: `A böngésző fejlesztése érdekében a Firefox`
    - Hungarian punctuation does not place a comma after a sentence-initial adverbial phrase here; the comma is an anglicism.
- `onboarding_redesign_tou_body_three` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Superfluous comma between the adverbial clause and the subject.
    - Current: `A böngésző fejlesztése érdekében, a Firefox`
    - Source: `To help improve the browser, Firefox sends diagnostic and interaction data to Mozilla. %1$s`
    - Suggest: `A böngésző fejlesztése érdekében a Firefox`
    - Hungarian punctuation does not place a comma after a fronted purpose adverbial like "…érdekében" before the main clause subject.
- `onboarding_term_of_service_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — Superfluous comma between the adverbial phrase and the subject.
    - Current: `A böngésző fejlesztése érdekében, a Firefox`
    - Source: `To help improve the browser, Firefox sends diagnostic and interaction data to Mozilla. %1$s`
    - Suggest: `A böngésző fejlesztése érdekében a Firefox`
    - Hungarian punctuation does not place a comma after a fronted adverbial phrase like this; the source has a comma only because of English usage after an introductory phrase.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/hu/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
