# Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **Previous run** | 2026-08-21 @ `0d02c6c9f0f6` |
| **Mode** | incremental |
| **Strings reviewed this run** | 3 of 2,911 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (3)

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — `mozac_feature_sitepermissions_storage_access_message` has placeholders %1$s where the source has %s
    - Current: `Möglicherweise möchten Sie den Zugriff blockieren, wenn nicht klar ist, warum %1$s diese Daten benötigt.`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — `mozac_feature_findindpage_dismiss` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - Suggest: `„Seite durchsuchen“ schließen`
    - The locale's quote convention is `german-double` (25 occurrences).
- `accessibility_dismiss_find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — `accessibility_dismiss_find_in_page` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).

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
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `german-double` 25, `straight-double` 2, `curly-double` 1 | **german-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 8 | **en** |
| register | `formal` 685 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (117)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 66 |
| 3 | Degraded language (grammar, spelling, terminology) | 37 |
| 4 | Cosmetic (typography, spacing) | 13 |

### A. Functional, markup, variables & plurals

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — `mozac_feature_sitepermissions_storage_access_message` has placeholders %1$s where the source has %s
    - Current: `Möglicherweise möchten Sie den Zugriff blockieren, wenn nicht klar ist, warum %1$s diese Daten benötigt.`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — "Is your device or network protected..." is translated as "Computer" instead of "Gerät".
    - Current: `Wird Ihr Computer oder Ihr Netzwerk von einer Firewall oder einem Proxy geschützt?`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Wird Ihr Gerät oder Ihr Netzwerk von einer Firewall oder einem Proxy geschützt?`
    - The source refers to "your device", not a computer.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — "device" is translated as "Computer" in a mobile-browser error page.
    - Current: `Ist der Computer mit einem aktiven Netzwerk verbunden?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Ist das Gerät mit einem aktiven Netzwerk verbunden?`
    - The source says "Is the device connected to an active network?"; "Computer" names the wrong thing on Android devices.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — "not your device" is translated as "Ihres Computers".
    - Current: `nicht um einen Fehler Ihres Computers`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `nicht um einen Fehler Ihres Geräts`
    - The source refers to the user's device; "Computer" is wrong on a mobile browser.
- `mozac_browser_errorpages_redirect_loop_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — The redirect-loop page title is rendered as a redundant "Fehler: Umleitungsfehler" instead of translating the source sentence.
    - Current: `Fehler: Umleitungsfehler`
    - Source: `The page isn’t redirecting properly`
    - Suggest: `Die Seite leitet nicht korrekt um`
    - Source is "The page isn’t redirecting properly"; the German adds a "Fehler:" prefix and duplicates the word "Fehler", conveying different content than the source heading.
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — "If you are unable to load any pages" is rendered as "Wenn Sie auch keine andere Website aufrufen können", changing the meaning.
    - Current: `Wenn Sie auch keine andere Website aufrufen können, überprüfen Sie bitte die Daten- oder WLAN-Verbindung.`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `Wenn Sie überhaupt keine Seiten laden können, überprüfen Sie bitte die Daten- oder WLAN-Verbindung Ihres Geräts.`
    - The source condition is being unable to load any page at all, and it refers to the device's data or Wi-Fi connection; the German narrows it to "any other website" and drops "your device’s".
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — "device" is translated as "Computer".
    - Current: `Ist der Computer mit einem aktiven Netzwerk verbunden?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Ist das Gerät mit einem aktiven Netzwerk verbunden?`
    - Source: "Is the device connected to an active network?" — "Computer" is the wrong term for a mobile device.
- `mozac_browser_errorpages_unknown_socket_type_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — Title adds "Fehler:" and drops "from server".
    - Current: `Fehler: Unerwartete Antwort`
    - Source: `Unexpected response from server`
    - Suggest: `Unerwartete Antwort vom Server`
    - Source is "Unexpected response from server"; the German inserts a prefix not in the source and omits the server reference.
- `mozac_clear_button_description` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-de/strings.xml` — "Clear" for the clear-URL-text button is rendered as "Leeren" (empty a container) instead of the established "Löschen".
    - Current: `Leeren`
    - Source: `Clear`
    - Suggest: `Löschen`
    - The developer comment says this is the content description of the button that clears the typed URL text; German Firefox uses "Löschen" for clearing input text, whereas "Leeren" means emptying a container and is misleading when read aloud.
- `mozac_compose_base_link_text_links_available` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-de/strings.xml` — "Links available" (a statement that links are present) is translated as the noun phrase "Verfügbare Links".
    - Current: `Verfügbare Links`
    - Source: `Links available`
    - Suggest: `Links verfügbar`
    - Per the developer comment this is an announcement that interactive links are present, not a label naming "available links".
- `mozac_feature_addons_permissions_browsing_data_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — "recent" is omitted from "Clear recent browsing history".
    - Current: `Browser-Chronik, Cookies und verwandte Daten löschen.`
    - Source: `Clear recent browsing history, cookies, and related data.`
    - Suggest: `Neuere Browser-Chronik, Cookies und verwandte Daten löschen.`
    - The source limits the scope to "recent browsing history"; the German suggests the entire history can be cleared.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — The translation drops "your data" from "access your data in open tabs".
    - Current: `Entwicklerwerkzeuge erweitern, sodass Zugriff auf offene Tabs besteht`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `Entwicklerwerkzeuge erweitern, sodass diese auf Ihre Daten in offenen Tabs zugreifen können`
    - The source grants access to the user's data in open tabs, not to the tabs themselves; omitting "Ihre Daten" understates the permission.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — The translation drops "your data" from "access your data in open tabs".
    - Current: `Entwicklerwerkzeuge erweitern, sodass Zugriff auf offene Tabs besteht.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Entwicklerwerkzeuge erweitern, sodass diese auf Ihre Daten in offenen Tabs zugreifen können.`
    - The source grants access to the user's data in open tabs, not to the tabs themselves; omitting "Ihre Daten" understates the permission.
- `mozac_feature_addons_permissions_find_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — "Read the text of all open tabs" is rendered as "access the texts", losing the "read" meaning.
    - Current: `Auf Texte aller offenen Tabs zugreifen.`
    - Source: `Read the text of all open tabs.`
    - Suggest: `Den Text aller offenen Tabs lesen.`
    - The source says "Read the text of all open tabs"; "zugreifen" (access) is used elsewhere for "access" permissions and blurs the distinction.
- `mozac_protections_dashboard_empty_subtitle` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-de/strings.xml` — "You'll see them here" is rendered with "Sie" as the subject, reversing the sentence's meaning.
    - Current: `Sie werden sie hier sehen.`
    - Source: `You’ll see them here.`
    - Suggest: `Sie sehen sie hier.`
    - The source addresses the user ("You'll see them here"), i.e. the blocked trackers will appear here. The German is ambiguous/awkward; more importantly the future construction misreads. A clearer rendering is "Sie sehen sie hier." or "Hier werden sie angezeigt."
- `mozac_tab_counter_content_description` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-de/strings.xml` — The compound is mis-parsed: the source describes the tab counter button in the toolbar, not a button of a "tab counter toolbar".
    - Current: `Die Schaltfläche der Tab-Zähler-Symbolleiste.`
    - Source: `The tab counter toolbar button.`
    - Suggest: `Die Tab-Zähler-Schaltfläche in der Symbolleiste.`
    - "The tab counter toolbar button" = the toolbar button that counts tabs; the German says "button of the tab-counter toolbar", which names a nonexistent toolbar.
- `add_to_tab_group_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Add to" is expanded to "Zur Tab-Gruppe hinzufügen", adding content not in the source title.
    - Current: `Zur Tab-Gruppe hinzufügen`
    - Source: `Add to`
    - Suggest: `Hinzufügen zu`
    - The source title is simply "Add to" (followed by a group picker); the German invents a specific target that contradicts the list of choices.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Department" is rendered with the Spanish word "Departamento" instead of German.
    - Current: `Departamento`
    - Source: `Department`
    - Suggest: `Departamento (Verwaltungsbezirk)`
    - The source is English "Department" (administrative division in Nicaragua/Colombia); the German label should be a German term such as "Departement"/"Verwaltungsbezirk", not the Spanish form.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The address field label "Post town" is left in English rather than translated into German.
    - Current: `Post Town`
    - Source: `Post town`
    - Suggest: `Poststadt`
    - "Post town" is a normal address-field label, not a brand or do-not-translate term; every other field label in this batch is localized (Präfektur, Postleitzahl, Land). The English wording is also re-capitalized in a way that is neither English nor German usage.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Unblock specific features below" is translated as "Blockieren" (block) instead of "Freigeben/Entsperren" (unblock), reversing the meaning.
    - Current: `Blockieren Sie im Folgenden bestimmte Funktionen.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Entsperren Sie im Folgenden bestimmte Funktionen.`
    - The source instructs the user to unblock specific features; the German says to block them, the opposite.
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The artist's handle is misspelled, dropping "he" from @heyheymomodraws.
    - Current: `@heyheymomoraws`
    - Source: `Created by @heyheymomodraws`
    - Suggest: `@heyheymomodraws`
    - The source and developer comment give the handle as @heyheymomodraws; a social media handle is a name that must be reproduced exactly.
- `bookmark_sort_menu_custom` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Sort by custom order" is rendered only as "Benutzerdefiniert", dropping the sorting verb present in all sibling sort options.
    - Current: `Benutzerdefiniert`
    - Source: `Sort by custom order`
    - Suggest: `Nach benutzerdefinierter Reihenfolge sortieren`
    - The source and all other items in the same sorting menu ("Nach Neuesten sortieren", "Nach A bis Z sortieren") express the sort action; this entry omits it and is inconsistent within the same menu.
- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The label "URL" is translated as "ADRESSE" and additionally uppercased without reason.
    - Current: `ADRESSE`
    - Source: `URL`
    - Suggest: `URL`
    - The source is the technical term "URL", which is used unchanged in German; the all-caps form also does not match the source casing.
- `certificate_warning_homepage_card_hcr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Future conditional "will ... stop working" is rendered as a present-tense statement, and "nicht mehr richtig" loses the causal link.
    - Current: `Ein Stammzertifikat läuft ab, und Ihre Firefox-Version funktioniert nicht mehr richtig.`
    - Source: `A root certificate will expire, causing your version of Firefox to stop working properly.`
    - Suggest: `Ein Stammzertifikat läuft ab, weshalb Ihre Firefox-Version nicht mehr richtig funktionieren wird.`
    - The source says the expiry will cause Firefox to stop working properly; the German coordinates two independent statements in present tense, losing the causal/future meaning that the parallel string hca1_message preserves with "weshalb".
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "stop working properly" is translated as "funktioniert nicht mehr" (stops working entirely), dropping "properly".
    - Current: `Ihre Firefox-Version funktioniert ab 14. März nicht mehr, da ein Stammzertifikat abläuft.`
    - Source: `Your version of Firefox will stop working properly on March 14 because a root certificate is expiring.`
    - Suggest: `Ihre Firefox-Version funktioniert ab 14. März nicht mehr richtig, da ein Stammzertifikat abläuft.`
    - The source states the version will stop working *properly*; omitting "richtig" overstates the consequence.
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The hedged "might ... be risky" is rendered as a definite statement "ist ... riskant".
    - Current: `und ist für Ihr Gerät riskant`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `und für Ihr Gerät riskant sein`
    - The source says "This might open the file in a different app and be risky for your device" — both clauses are under "might"; the German asserts the risk as a fact.
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Regulation" (EU) 2024/1183 is a Verordnung, not a Richtlinie (directive).
    - Current: `Qualifiziert im Sinne der Richtlinie (EU) 2024/1183.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Qualifiziert im Sinne der Verordnung (EU) 2024/1183.`
    - EU legal terminology: "Regulation" = "Verordnung"; "Richtlinie" means "Directive", naming the wrong type of legal act.
- `default_locale_text` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Follow device language" rendered as "Gerätesprache beachten" (observe/note the device language) rather than following it.
    - Current: `Gerätesprache beachten`
    - Source: `Follow device language`
    - Suggest: `Gerätesprache folgen`
    - The setting means the app follows the device's language; "beachten" means "take note of" and does not convey the setting's behavior.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Help catch trackers" is mistranslated as an appeal to the user to catch trackers.
    - Current: `Helfen Sie, Tracker zu fangen`
    - Source: `Help catch trackers`
    - Suggest: `Hilft, Tracker abzufangen`
    - The string is shown below the trackers-blocked card describing the app's protection, not a call for the user to catch trackers; "fangen" is also the wrong verb for blocking trackers.
- `ip_protection_onboarding_body_link` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Link text translated as an imperative sentence instead of the source's noun-like phrase, and it must fit inside the surrounding body sentence.
    - Current: `Surfen Sie mit zusätzlichem Schutz`
    - Source: `Browse with extra protection`
    - Suggest: `Mit zusätzlichem Schutz surfen`
    - The source "Browse with extra protection" is link text embedded in ip_protection_onboarding_body; the German formal-imperative "Surfen Sie …" reads as a standalone command and breaks the host sentence.
- `lens_opt_out_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "an image" is rendered as "eine Grafik" (a graphic) instead of "ein Bild".
    - Current: `Wählen Sie eine Grafik aus`
    - Source: `Choose an image or use your camera to get results with Google Lens.`
    - Suggest: `Wählen Sie ein Bild aus`
    - In the Google Lens context the user picks a photo/image from the device; "Grafik" means graphic/illustration and is the wrong term for "image" here.
- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "on WhatsApp shares" is mistranslated as "beim Teilen per WhatsApp" plus "hinzufügen" instead of "include"; acceptable, but "Download-Link für %1$s" reverses the sense of "%1$s download link".
    - Current: `Download-Link für %1$s beim Teilen per WhatsApp hinzufügen`
    - Source: `Include %1$s download link on WhatsApp shares`
    - Suggest: `%1$s-Download-Link beim Teilen über WhatsApp einfügen`
    - Source: "Include %1$s download link on WhatsApp shares".
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The German sentence reverses the meaning: it asks whether the user "may" help someone succeed instead of asking them to grant permission to help Firefox win.
    - Current: `Bitte überlegen Sie, ob Sie mit dieser Erlaubnis zum Erfolg verhelfen dürfen.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Bitte erwägen Sie, die Erlaubnis zu erteilen, um Firefox zum Erfolg zu verhelfen.`
    - Source: "Please consider allowing to help Firefox win." The developer comment explains that "allowing" refers to the "Allow and Continue" button; the German says "whether you are allowed to help to success" and drops Firefox entirely.
- `nova_onboarding_notifications_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The German reverses the subject: the source says notifications help the user stay safer with Firefox, not that the user makes Firefox safer.
    - Current: `Benachrichtigungen helfen Ihnen, Firefox noch sicherer zu machen`
    - Source: `Notifications help you stay safer with Firefox`
    - Suggest: `Benachrichtigungen helfen Ihnen, mit Firefox sicherer zu surfen`
    - Source: "Notifications help you stay safer with Firefox" — the user stays safer using Firefox; the target claims the user makes Firefox safer.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Content description for a button that opens the tabs menu is translated as a noun label instead of an action.
    - Current: `Offene-Tabs-Menü`
    - Source: `Open tabs menu`
    - Suggest: `Menü für offene Tabs öffnen`
    - The developer comment says the control "Opens the open tabs menu when pressed"; the German renders only the menu name, dropping the action that the screen reader must convey.
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Leave private tabs" (exit private browsing) is rendered as "Private Tabs belassen" (leave them as they are).
    - Current: `Private Tabs belassen`
    - Source: `Leave private tabs`
    - Suggest: `Private Tabs verlassen`
    - Per the developer comment this is the secondary action to exit private browsing mode; "belassen" means "to leave something unchanged", reversing the intended action.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "pinch and zoom" is mistranslated as "das Kneifen und Zoomen" (pinching someone).
    - Current: `das Kneifen und Zoomen`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `Zusammen- und Auseinanderziehen zum Zoomen`
    - "Kneifen" means pinching a person and is not the German term for the pinch gesture; the source refers to the pinch-to-zoom gesture.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "which website you're about to access" (a site you are about to visit) is rendered as "welche Website Sie gerade besuchen" (currently visiting).
    - Current: `welche Website Sie gerade besuchen`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `welche Website Sie als Nächstes aufrufen`
    - The source refers to a future action ("about to access"), while the German says the user is currently visiting the site, changing the meaning.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Cross-site and social media trackers" is translated without the noun "trackers", leaving a fragment.
    - Current: `Zur seitenübergreifenden Aktivitätenverfolgung und von sozialen Netzwerken`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Seitenübergreifende Elemente zur Aktivitätenverfolgung und solche von sozialen Netzwerken`
    - The source names a tracker category; the German fragment lacks the head noun and does not convey "trackers".
- `preference_enhanced_tracking_protection_custom_cookies_5` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Isolate cross-site cookies" is rendered only as "Seitenübergreifende Cookies", dropping the verb "isolate".
    - Current: `Seitenübergreifende Cookies`
    - Source: `Isolate cross-site cookies`
    - Suggest: `Seitenübergreifende Cookies isolieren`
    - The source is an action option ("Isolate cross-site cookies"); the German omits the key verb, changing the meaning to a mere category label.
- `preference_enhanced_tracking_protection_custom_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Translation says "which kind of scripts and other content" instead of "which trackers and scripts".
    - Current: `Wählen Sie, welche Art von Skripten zur Aktivitätenverfolgung und sonstige Inhalte blockiert werden.`
    - Source: `Choose which trackers and scripts to block.`
    - Suggest: `Wählen Sie, welche Elemente zur Aktivitätenverfolgung und welche Skripte blockiert werden.`
    - The source lists two blockable categories: trackers and scripts. The German renders it as "scripts for activity tracking and other content", which is different content and also grammatically inconsistent.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "trackers" is rendered as "Skripte" (scripts) instead of "Tracker".
    - Current: `vielen der gängigsten Skripte, die Ihre Online-Aktivitäten verfolgen`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `vielen der gängigsten Tracker, die Ihre Online-Aktivitäten verfolgen`
    - The source says "trackers"; "Skripte" names a different thing and is inconsistent with the "Tracker" terminology used in neighbouring strings.
- `preference_enhanced_tracking_protection_standard_default_1` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The "(default)" qualifier from the source is missing.
    - Current: `Standard`
    - Source: `Standard (default)`
    - Suggest: `Standard (Standardeinstellung)`
    - Source is "Standard (default)"; the translation drops the information that this is the default setting.
- `preferences_android_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Translation wrongly says "on websites" instead of "in other apps on your device".
    - Current: `Benutzernamen und Passwörter auf Webseite bei Nutzung von anderen Apps auf Ihrem Gerät automatisch ausfüllen.`
    - Source: `Fill usernames and passwords in other apps on your device.`
    - Suggest: `Benutzernamen und Passwörter in anderen Apps auf Ihrem Gerät ausfüllen.`
    - Source is "Fill usernames and passwords in other apps on your device." The German inserts "auf Webseite bei Nutzung von", which changes the meaning to filling on websites and is also ungrammatical.
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Present-tense description of what the option does is rendered as past tense in German.
    - Current: `Die Datei wurde von Ihrem Gerät gelöscht und aus der Download-Chronik entfernt`
    - Source: `File is deleted from your device and removed from download history`
    - Suggest: `Die Datei wird von Ihrem Gerät gelöscht und aus der Download-Chronik entfernt`
    - The source "File is deleted from your device and removed from download history" describes the behaviour of the setting (present/future), not a completed action; "wurde ... gelöscht" states it already happened.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Present-tense description of the option is rendered as past tense in German.
    - Current: `Die Datei wurde aus Ihrer Download-Chronik entfernt, ist aber noch auf Ihrem Gerät gespeichert`
    - Source: `File is removed from your download history, but is still saved on your device`
    - Suggest: `Die Datei wird aus Ihrer Download-Chronik entfernt, ist aber noch auf Ihrem Gerät gespeichert`
    - The source "File is removed from your download history, but is still saved on your device" describes what the setting does, not a completed past action.
- `preferences_marketing_data_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Campaign measurement data" is rendered as "Messdaten für die Kampagne", introducing a definite specific campaign instead of the general term.
    - Current: `Messdaten für die Kampagne`
    - Source: `Campaign measurement data`
    - Suggest: `Daten zur Kampagnenmessung`
    - The source is the generic data category matching the section title "Campaign measurement" (translated "Kampagnenmessung"); "für die Kampagne" implies one specific campaign and breaks consistency with the section title.
- `protection_panel_etp_toggle_enabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "looks broken" is mistranslated as "beschädigt aussieht" and the imperative drops the "try" hedge.
    - Current: `Wenn etwas auf dieser Website beschädigt aussieht, deaktivieren Sie ihn.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Wenn etwas auf dieser Website nicht richtig funktioniert, versuchen Sie, ihn zu deaktivieren.`
    - The source says the site may appear broken (not working correctly) and suggests trying to turn protection off; "beschädigt aussieht" means physically damaged and the German loses "try".
- `recent_tabs_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Content description misplaces the quotation so it names a button labelled "Alle zuletzt geöffneten Tabs" instead of describing the "Show all recent tabs" button.
    - Current: `Schaltfläche „Alle zuletzt geöffneten Tabs“ anzeigen`
    - Source: `Show all recent tabs button`
    - Suggest: `Schaltfläche „Alle zuletzt geöffneten Tabs anzeigen“`
    - The source is "Show all recent tabs button", i.e. the button whose action is showing all recent tabs; the German quotes only part of the label and leaves "anzeigen" outside, changing the meaning to "show the button".
- `saved_logins_clear_password` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Clear password" (clear the input field) is translated as "Passwort löschen", which is identical to deleting the password.
    - Current: `Passwort löschen`
    - Source: `Clear password`
    - Suggest: `Passwortfeld leeren`
    - The developer comment says this button clears the password field while editing a login, not deletes the stored password; German should use "leeren" to distinguish it from delete.
- `settings_search_recent_searches_section_header` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Recent search results" is rendered as "Neueste Suchergebnisse" (newest/latest), losing the "recent searches" sense used consistently in this screen.
    - Current: `Neueste Suchergebnisse`
    - Source: `Recent search results`
    - Suggest: `Letzte Suchergebnisse`
    - The sibling string uses "Keine letzten Suchanfragen" for "No recent searches"; "recent" should stay "letzte" for consistency on the same surface.
- `share_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Cannot share to this app" rendered with "freigegeben", inconsistent with "Teilen" used for Share elsewhere.
    - Current: `Kann nicht für diese App freigegeben werden`
    - Source: `Cannot share to this app`
    - Suggest: `Teilen mit dieser App nicht möglich`
    - All other share strings in this surface use "teilen" for Share; "freigeben" is a different term and the passive phrasing changes the meaning (sharing the link with an app, not releasing something for the app).
- `sports_widget_error_load_failed_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Translation adds "die Seite" (the page), which is not in the source and misdescribes refreshing the widget's match data.
    - Current: `Aktualisieren Sie die Seite in ein paar Minuten.`
    - Source: `Try refreshing in a few minutes.`
    - Suggest: `Versuchen Sie es in ein paar Minuten erneut zu aktualisieren.`
    - Source "Try refreshing in a few minutes." refers to refreshing the sports widget data, not a page; the German invents an object.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Navigate back" rendered as "Rückwärts navigieren" instead of the established "Zurück" navigation wording.
    - Current: `Rückwärts navigieren`
    - Source: `Navigate back`
    - Suggest: `Zurück navigieren`
    - The source means going back to the previous screen; "rückwärts" means moving backwards in a directional sense and is not the term used for back navigation in German UI.
- `translation_option_bottom_sheet_close_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Seite" wrongly renders "sheet" (bottom sheet dialog) as "page".
    - Current: `Seite „Übersetzungen“ schließen`
    - Source: `Close Translations sheet`
    - Suggest: `Dialog „Übersetzungen“ schließen`
    - The developer comment says this closes the translations bottom sheet; "Seite" means page, which conflicts with the page/site terminology used elsewhere in this feature.
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The adverb placement changes the meaning: the source says languages are always downloaded even in data saving mode, not that they should be downloaded in data saving mode.
    - Current: `Sprachen immer im Datensparmodus herunterladen`
    - Source: `Always download languages in data saving mode`
    - Suggest: `Sprachen im Datensparmodus immer herunterladen`
    - Source: "Always download languages in data saving mode" — the toggle permits downloading while in data saver mode. "Sprachen immer im Datensparmodus herunterladen" reads as "always download languages in (i.e. using) data saving mode".
- `translation_toolbar_expand_action` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Open translation sheet" is rendered as opening a page named „Übersetzungen“ instead of the translation sheet/dialog.
    - Current: `Seite „Übersetzungen“ öffnen`
    - Source: `Open translation sheet`
    - Suggest: `Übersetzungsdialog öffnen`
    - The developer comment says this action opens the translations dialog (a bottom sheet), not a page called "Übersetzungen"; "Seite" also collides with "page" terminology used elsewhere in the translation UI.
- `uninstall_survey_option_2_v2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Past tense of the source is rendered as present tense.
    - Current: `Websites funktionieren nicht richtig`
    - Source: `Websites didn’t work properly`
    - Suggest: `Websites funktionierten nicht richtig`
    - Source "Websites didn’t work properly" is past tense, describing the user's past experience; the German present tense changes the meaning.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Past tense of the source is rendered as present tense.
    - Current: `Videos, Downloads oder Medien funktionieren nicht`
    - Source: `Videos, downloads, or media didn’t work`
    - Suggest: `Videos, Downloads oder Medien funktionierten nicht`
    - Source "Videos, downloads, or media didn’t work" is past tense; the German present tense changes the meaning.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "check out" (Kaufabschluss/Bezahlvorgang) was mistranslated as "den Warenkorb leeren" (empty the shopping cart).
    - Current: `Ich kann nicht bezahlen, den Warenkorb leeren oder einkaufen`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `Ich kann nicht bezahlen, den Kauf abschließen oder einkaufen`
    - The source "Can’t pay, check out or shop" refers to completing the checkout process, not emptying the cart.
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Search and browse right in the app" is translated as "Suchen und blättern Sie in der App", where "blättern" means paging/leafing rather than web browsing.
    - Current: `Suchen und blättern Sie in der App`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Suchen und surfen Sie direkt in der App`
    - "browse" here means browsing the web; "blättern" is the wrong sense and "right in the app" (direkt) is dropped.
- _…and 8 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — Missing case agreement in "Ihr Modem oder Router" after "Überprüfen Sie".
    - Current: `Überprüfen Sie Ihr Modem oder Router.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Überprüfen Sie Ihr Modem oder Ihren Router.`
    - Accusative object requires "Ihren Router"; the shared determiner "Ihr" does not work for the masculine noun.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — Faulty parallel construction: "ein Problem … sein oder jemand, der vorgibt, der Server zu sein".
    - Current: `Dies könnte ein Problem mit der Konfiguration des Servers sein oder jemand, der vorgibt, der Server zu sein.`
    - Source: `{ <ul> } { <li> }This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server.{ </li> } { <li> }If you have connected to this server successfully in the past, the erro…`
    - Suggest: `Dies könnte ein Problem mit der Konfiguration des Servers sein, oder es versucht jemand, sich als der Server auszugeben.`
    - The source has two parallel clauses ("it could be someone trying to impersonate the server"); the German coordination is ungrammatical.
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Wrong gender agreement: "Ein" should be "Eine" with feminine "Erweiterung(en)".
    - Current: `Ein oder mehrere Erweiterungen`
    - Source: `One or more extensions stopped working, making your system unstable.`
    - Suggest: `Eine oder mehrere Erweiterungen`
    - "Erweiterung" is feminine, so the singular article must be "Eine".
- `notification_erase_text_android_14` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Wrong verb government: "tippen ... auf diese Benachrichtigung" combined with "wischen" is ungrammatical.
    - Current: `Tippen oder wischen Sie auf diese Benachrichtigung`
    - Source: `Tap or swipe this notification to close private tabs.`
    - Suggest: `Tippen Sie auf diese Benachrichtigung oder wischen Sie sie weg`
    - "wischen auf" is not correct German for swiping a notification away; the coordinated construction forces the wrong preposition for one of the verbs.
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Wrong case/structure: "die Kanäle … mitzuteilen" should be dative "den Kanälen".
    - Current: `die Kanäle, in denen wir Firefox bewerben, mitzuteilen`
    - Source: `You can help us reach more people by allowing Mozilla to inform the channels where we promote Firefox that you’re a Firefox user.`
    - Suggest: `den Kanälen, in denen wir Firefox bewerben, mitzuteilen`
    - "mitteilen" takes a dative object for the recipient; the accusative "die Kanäle" is ungrammatical.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Broken coordination: "ist stolz darauf, unabhängig und verteidigt …" is ungrammatical.
    - Current: `Firefox ist stolz darauf, unabhängig und verteidigt das offene Web gegen Technologie-Monopole.`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox ist stolz darauf, unabhängig zu sein und das offene Web gegen Technologie-Monopole zu verteidigen.`
    - The source "Firefox is proudly independent and dedicated to defending the open web" requires two parallel complements; the German mixes an adjective and a finite verb after "stolz darauf," producing an incomplete clause.
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "DNS over HTTPS" is a fixed technical term and must keep lowercase "over", not "Over".
    - Current: `DNS Over HTTPS`
    - Source: `DNS over HTTPS`
    - Suggest: `DNS over HTTPS`
    - The source and the developer comment both write "DNS over HTTPS"; capitalizing "Over" misspells the established protocol name.
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "auf Webseite" lacks the plural/article required for "in websites".
    - Current: `auf Webseite bei Nutzung von %1$s`
    - Source: `Fill and save usernames and passwords in websites while using %1$s.`
    - Suggest: `auf Websites bei Nutzung von %1$s`
    - Source says "in websites" (plural); the German singular without article is grammatically wrong.
- `sports_widget_penalties` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Elfmeterschließen" is a misspelling of "Elfmeterschießen".
    - Current: `Elfmeterschließen`
    - Source: `Penalties`
    - Suggest: `Elfmeterschießen`
    - The German term for a penalty shoot-out is "Elfmeterschießen"; "Elfmeterschließen" is not a word.
- `sync_no_devices_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "mit ihnen synchronisieren" uses lowercase "ihnen" and mistranslates "syncing to this account".
    - Current: `Alle Geräte, die mit diesem Konto angemeldet sind und mit ihnen synchronisieren, werden hier angezeigt.`
    - Source: `Any devices signed in and syncing to this account will appear here.`
    - Suggest: `Alle Geräte, die bei diesem Konto angemeldet sind und damit synchronisieren, werden hier angezeigt.`
    - The source says devices signed in and syncing to this account; "mit ihnen" (plural pronoun, lowercase) refers to nothing and is grammatically wrong — it should refer back to the account (singular).
- `terms_of_use_prompt_body_line_two_alternative_link` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Inline link text "here" is capitalized as "Hier" although it appears mid-sentence in "Weitere Informationen %1$s."
    - Current: `Hier`
    - Source: `here`
    - Suggest: `hier`
    - The link is embedded in the sentence terms_of_use_prompt_body_line_two_alternative, so German requires lowercase "hier"; the source is lowercase too.
- `terms_of_use_prompt_postpone` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Remind me later" is translated as "Später erinnern", which lacks the object and reads as a fragment.
    - Current: `Später erinnern`
    - Source: `Remind me later`
    - Suggest: `Später erinnern lassen`
    - German requires a reflexive/object construction; the standard Mozilla wording is "Später erinnern lassen" or "Mich später erinnern".
- `trackers_blocked_panel_num_trackers_blocked_this_week_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The singular variant uses a plural verb form ("wurden") with a singular subject.
    - Current: `[one] %1$d Tracker wurden in dieser Woche blockiert`
    - Source: `{$quantity ->} [one] %1$d tracker blocked this week [other] %1$d trackers blocked this week`
    - Suggest: `[one] %1$d Tracker wurde in dieser Woche blockiert`
    - In the [one] case the subject is a single tracker, so the verb must be "wurde", not "wurden".
- `translations_bottom_sheet_info_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Grammatical error: "Zu Sicherstellung" should be "Zur Sicherstellung".
    - Current: `Zu Sicherstellung Ihrer Privatsphäre`
    - Source: `For your privacy, translations never leave your device. New languages and improvements coming soon! %1$s`
    - Suggest: `Zur Sicherstellung Ihrer Privatsphäre`
    - "Sicherstellung" is feminine dative, requiring "zur", not "zu".
- `uninstall_survey_button_label` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The verb "deinstallieren" is incorrectly capitalized.
    - Current: `Feedback übermitteln und Deinstallieren`
    - Source: `Submit feedback and uninstall`
    - Suggest: `Feedback übermitteln und deinstallieren`
    - "deinstallieren" here is an infinitive verb parallel to "übermitteln", not a noun, so it must be lowercase.
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Superfluous article "den" before the link placeholder produces "in den Einstellungen" grammar mismatch with the link text.
    - Current: `Verwalten Sie die Cookie-Banner-Einstellungen in den %2$s.`
    - Source: `%1$s tries to reject cookie requests to dismiss annoying cookie banners.  Manage cookie banner preferences in %2$s.`
    - Suggest: `Verwalten Sie die Cookie-Banner-Einstellungen in den Einstellungen.`
    - %2$s is replaced by the link text "Einstellungen"; the sentence is fine only if the article agrees, but as written the source has no article and the link string itself is capitalized — the article "den" plus the linked word yields correct German only by coincidence; the risk is that the article is outside the link. Recommend restructuring so the article is part of the link phrase.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Misspelling of "Aussteller" as "Austeller".
    - Current: `das Zertifikat vom Austeller selbst signiert wurde`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `das Zertifikat vom Aussteller selbst signiert wurde`
    - "Austeller" is a typo; the correct German spelling is "Aussteller", as used earlier in the same string ("der Aussteller des Zertifikats").

### D. Terminology, register & consistency

- `mozac_browser_toolbar_content_description_tracking_protection_on_no_trackers_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-de/strings.xml` — "Tracking Protection" is translated as "Schutz vor Aktivitätenverfolgung" here but as "Tracking-Schutz" in the two neighbouring toolbar strings.
    - Current: `Schutz vor Aktivitätenverfolgung ist an`
    - Source: `Tracking Protection is on`
    - Suggest: `Der Tracking-Schutz ist an`
    - The same source term on the same surface (tracking protection toolbar icon content descriptions) is rendered two different ways; the adjacent strings use "Tracking-Schutz".
- `mozac_feature_addons_permissions_data_collection_browsingActivity_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — "browsing activity" is rendered as "Surfaktivität" in the short description but as "Surf-Aktivität" in the corresponding long description.
    - Current: `Surfaktivität`
    - Source: `browsing activity`
    - Suggest: `Surf-Aktivität`
    - The same source term must use the same German term across the short/long description pair for the same permission (mozac_feature_addons_permissions_data_collection_browsingActivity_long_description uses "Surf-Aktivität").
- `mozac_feature_addons_permissions_declarative_net_request_feedback_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Permission description rendered as an imperative sentence addressed to the user instead of an infinitive permission label.
    - Current: `Lesen Sie Ihre Surf-Chronik`
    - Source: `Read your browsing history`
    - Suggest: `Ihre Surf-Chronik lesen`
    - The source "Read your browsing history" is a permission description in a list; all sibling permission strings use the infinitive form ("Datenschutzeinstellungen lesen und ändern", "Auf Browsertabs zugreifen"). The current text reads as a command to the user ("You read your browsing history"), which reverses who performs the action.
- `mozac_feature_addons_permissions_history_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Same source string "Access browsing history" is translated inconsistently with its _for_update counterpart ("Auf die Surf-Chronik zugreifen").
    - Current: `Auf Chronik zugreifen`
    - Source: `Access browsing history`
    - Suggest: `Auf die Surf-Chronik zugreifen`
    - mozac_feature_addons_permissions_history_description_for_update uses "Auf die Surf-Chronik zugreifen" for the identical source text; the bare "Auf Chronik zugreifen" also lacks the article.
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Permission description uses an imperative sentence addressed to the user instead of the infinitive style used by all sibling permission strings.
    - Current: `Laden Sie KI-Modelle herunter und führen Sie diese auf Ihrem Gerät aus`
    - Source: `Download and run AI models on your device`
    - Suggest: `KI-Modelle herunterladen und auf Ihrem Gerät ausführen`
    - The source is a permission description listing what the extension may do ("Download and run AI models on your device"), and every other description in this file, including the _for_update variant of the same string, uses the infinitive form. Here it reads as an instruction to the user.
- `mozac_feature_addons_soft_blocked_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Inconsistent preposition for installation in the app: "auf %2$s installiert" vs. "in %2$s installiert" in the parallel blocklist string.
    - Current: `kann nicht auf %2$s installiert werden`
    - Source: `%1$s is restricted and can’t be installed on %2$s.`
    - Suggest: `kann nicht in %2$s installiert werden`
    - mozac_feature_addons_blocklisted_2 uses "kann nicht in %2$s installiert werden" for the same "can't be installed on <app>" construction; the app name requires "in", not "auf", in German.
- `mozac_ui_tabcounter_duplicate_tab` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-de/strings.xml` — "Duplicate tab" is rendered as "Tab klonen" instead of the established "Tab duplizieren".
    - Current: `Tab klonen`
    - Source: `Duplicate tab`
    - Suggest: `Tab duplizieren`
    - Source is "Duplicate tab"; German Firefox uses "duplizieren", not "klonen".
- `debug_drawer_logins_add_login_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Button label translated as an imperative sentence instead of an infinitive label.
    - Current: `Fügen Sie gefälschte Zugangsdaten für diese Domain hinzu`
    - Source: `Add a fake login for this domain`
    - Suggest: `Gefälschte Zugangsdaten für diese Domain hinzufügen`
    - Per the developer comment this is a button label; German UI convention (and the sibling debug drawer buttons) use the infinitive form.
- `download_clear_search_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Clear" for the search-field clear button is rendered as "Leeren" instead of the established "Löschen"/"Eingabe löschen".
    - Current: `Leeren`
    - Source: `Clear`
    - Suggest: `Löschen`
    - The string is the content description for the search bar clear-text button; German Firefox uses "Löschen" for clearing a search field, while "Leeren" (to empty) is not used for this control.
- `download_item_paused_description_unknown_total_size` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "paused" is translated as "pausiert" here but as "angehalten" in the parallel string download_item_paused_description on the same downloads list surface.
    - Current: `%1$s • pausiert`
    - Source: `%1$s • paused`
    - Suggest: `%1$s • angehalten`
    - The same source term "paused" in the same downloads-list context must be rendered consistently; download_item_paused_description uses "angehalten".
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "the site" is rendered as "Webseite" although the same string and surrounding strings use "Website" for site.
    - Current: `vorübergehend für die Webseite deaktiviert`
    - Source: `However, it’s also possible that an attacker is involved. If you continue to the website, you should not enter any sensitive info. If you continue, HTTPS-Only mode will be turned off temporarily for the site.`
    - Suggest: `vorübergehend für die Website deaktiviert`
    - The source uses "website"/"site" consistently; earlier in the same string it is translated as "Website". "Webseite" means a single page and is inconsistent.
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Fingerprinters" is rendered inconsistently: "Identifizierer (Fingerprinter)" in the titles but plain "Fingerprinter" in the description on the same settings surface.
    - Current: `Vermutete Identifizierer (Fingerprinter)`
    - Source: `Suspected Fingerprinters`
    - Suggest: `Vermutete Fingerprinter`
    - The related description string uses "Fingerprinter" alone; the same term should be rendered consistently on the same screen.
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Button label rendered as a full sentence addressed to the user instead of an action label.
    - Current: `Versuchen Sie, die Erweiterungen neu zu starten`
    - Source: `Try restarting extensions`
    - Suggest: `Erweiterungen neu zu starten versuchen`
    - The developer comment says this is button text; the source "Try restarting extensions" is an imperative action label, and the parallel button uses infinitive style ("Mit deaktivierten Erweiterungen fortfahren"). The current wording is also far longer than the source for a button.
- `firefox_labs_share_feedback` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Share feedback" is translated inconsistently with the matching content description, which uses "Feedback geben".
    - Current: `Sagen Sie Ihre Meinung`
    - Source: `Share feedback`
    - Suggest: `Feedback geben`
    - The link label and its own content description (firefox_labs_share_feedback_content_description, "Geben Sie Feedback für %s.") describe the same control but use different terminology for "share feedback".
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Shortcuts" (home screen shortcuts) is rendered as "Tastenkombinationen" (keyboard shortcuts), inconsistent with "Verknüpfungen" used elsewhere.
    - Current: `Alle Tastenkombinationen anzeigen`
    - Source: `Show all shortcuts`
    - Suggest: `Alle Verknüpfungen anzeigen`
    - The same feature is called "Verknüpfungen" in homepage_shortcuts_title, browser_menu_add_to_shortcuts etc.; "Tastenkombinationen" means keyboard shortcuts and is wrong for the shortcuts home screen section.
- `nova_onboarding_customize_prompt_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Button label rendered as a full sentence instead of a short imperative action label.
    - Current: `Beginnen Sie mit den Anpassungen`
    - Source: `Start customizing`
    - Suggest: `Anpassung starten`
    - "Start customizing" is a short button label; the German is a drastically longer sentence-style phrasing inconsistent with other button labels in this set (e.g. "Benachrichtigungen aktivieren").
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Sync cards" rendered as "Kreditkarten synchronisieren" while the parallel string uses "Karten".
    - Current: `Kreditkarten synchronisieren`
    - Source: `Sync cards`
    - Suggest: `Karten synchronisieren`
    - Source says "cards", and the sibling strings (preferences_credit_cards_sync_cards_across_devices, add card, manage cards) all use "Karten"; "Kreditkarten" is inconsistent and narrower than the source.
- `menu_trackers_blocked_title` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Trackers" is rendered as "Verfolger" here but as "Tracker" elsewhere in the same app (about_content).
    - Current: `Verfolger blockiert`
    - Source: `Trackers blocked`
    - Suggest: `Tracker blockiert`
    - The established German term in Mozilla products (and in about_content of this same file) is "Tracker"; "Verfolger" is inconsistent and misleading.

### E. Typography, punctuation & spacing

- `mozac_compose_base_progress_loading` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-de/strings.xml` — An ellipsis was added that is not in the source.
    - Current: `Wird geladen…`
    - Source: `Loading`
    - Suggest: `Wird geladen`
    - Source "Loading" has no ellipsis; this is a screen-reader announcement.
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Dialog title adds a trailing period not present in the source.
    - Current: `%1$s bittet um zusätzliche Einstellungen.`
    - Source: `%1$s requests additional settings`
    - Suggest: `%1$s bittet um zusätzliche Einstellungen`
    - Source "%1$s requests additional settings" is a dialog title without final punctuation.
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Dialog title adds a trailing period not present in the source.
    - Current: `%1$s bittet um zusätzliche Datenerfassung.`
    - Source: `%1$s requests additional data collection`
    - Suggest: `%1$s bittet um zusätzliche Datenerfassung`
    - Source "%1$s requests additional data collection" is a dialog title without final punctuation.
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — `mozac_feature_findindpage_dismiss` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - Suggest: `„Seite durchsuchen“ schließen`
    - The locale's quote convention is `german-double` (25 occurrences).
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — Stray straight double quote before the German opening quotation mark.
    - Current: `von "„%1$s“ hochladen`
    - Source: `Make sure you trust this site before you upload from “%1$s”.`
    - Suggest: `von „%1$s“ hochladen`
    - The source has only one pair of curly quotes around %1$s; the German adds an extra stray straight quote character.
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — Stray space before the closing link markup after "Nutzungsbedingungen".
    - Current: `Nutzungsbedingungen { </a> }`
    - Source: `Logging in to %1$s with a %2$s account is subject to their <a href="%3$s">Privacy Policy{ </a> } and <a href="%4$s">Terms of Service{ </a> }`
    - Suggest: `Nutzungsbedingungen{ </a> }`
    - The source has no space between the link text and the closing tag placeholder ("Terms of Service{ </a> }"); the added space breaks the link text/markup alignment.
- `certificate_warning_push_notification_pnw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — A final period was added to a notification title that has none in the source.
    - Current: `Sie verwenden eine veraltete Firefox-Version.`
    - Source: `You’re on an older version of Firefox`
    - Suggest: `Sie verwenden eine veraltete Firefox-Version`
    - The English title "You’re on an older version of Firefox" has no terminal punctuation; other titles in this batch also omit it.
- `debug_drawer_autofill_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Hyphen used as a separating dash instead of the house en dash.
    - Current: `Automatisches Ausfüllen - Werkzeuge`
    - Source: `Autofill tools`
    - Suggest: `Automatisches Ausfüllen – Werkzeuge`
    - The locale convention is the en dash for parenthetical/separating dashes; a hyphen with spaces is incorrect German typography.
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Straight/English quotes used instead of German quotation marks.
    - Current: `Lesezeichen in “%s” gespeichert`
    - Source: `Bookmarks saved in “%s”`
    - Suggest: `Lesezeichen in „%s“ gespeichert`
    - The de convention is german-double quotes („…“), as used elsewhere (e.g. preference_summary_delete_browsing_data_on_quit_2).
- `sync_syncing_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Missing space before ellipsis is fine, but the ellipsis follows a word without the locale's spacing convention—actually the issue is the missing space is correct; flagged for character use.
    - Current: `Synchronisation läuft…`
    - Source: `Syncing…`
    - Suggest: `Synchronisation läuft …`
    - German typography convention (Duden) requires a space before the ellipsis when it follows a complete word.
- `accessibility_dismiss_find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — `accessibility_dismiss_find_in_page` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).
- `menu_open_with_a_browser2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Missing space before the ellipsis, inconsistent with the German convention used in menu_share ("Teilen …").
    - Current: `Öffnen in…`
    - Source: `Open in…`
    - Suggest: `Öffnen in …`
    - German typography (and the sibling string menu_share) places a space before the ellipsis character.
- `tip_add_to_homescreen` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Menu path separator ">" was replaced with an arrow "→", deviating from the source's menu-path notation.
    - Current: `Menü → Zum Startbildschirm hinzufügen`
    - Source: `Get one-tap access to sites you use most%1$s Menu > Add to Home screen`
    - Suggest: `Menü > Zum Startbildschirm hinzufügen`
    - The source uses "Menu > Add to Home screen"; the German substitutes a different symbol not used elsewhere for menu paths.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
