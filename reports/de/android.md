# Firefox for Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-08 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `c1a76afc1b60` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `c1a76afc1b60` |
| **Previous run** | 2026-11-05 @ `66b4c732bf9d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Plural variants (dead or missing forms) | 0 |
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
| quotes | `german-double` 23, `curly-double` 1 | **german-double** |
| ellipsis | `char` 22 | **char** |
| dash | `en` 7 | **en** |
| register | `formal` 658 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (53)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 34 |
| 3 | Degraded language (grammar, spelling, terminology) | 18 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

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
- `mozac_feature_addons_permissions_find_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — "Read the text of all open tabs" is rendered as "access the texts", losing the "read" meaning.
    - Current: `Auf Texte aller offenen Tabs zugreifen.`
    - Source: `Read the text of all open tabs.`
    - Suggest: `Den Text aller offenen Tabs lesen.`
    - The source says "Read the text of all open tabs"; "zugreifen" (access) is used elsewhere for "access" permissions and blurs the distinction.
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
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The German sentence reverses the meaning: it asks whether the user "may" help someone succeed instead of asking them to grant permission to help Firefox win.
    - Current: `Bitte überlegen Sie, ob Sie mit dieser Erlaubnis zum Erfolg verhelfen dürfen.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Bitte erwägen Sie, die Erlaubnis zu erteilen, um Firefox zum Erfolg zu verhelfen.`
    - Source: "Please consider allowing to help Firefox win." The developer comment explains that "allowing" refers to the "Allow and Continue" button; the German says "whether you are allowed to help to success" and drops Firefox entirely.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Content description for a button that opens the tabs menu is translated as a noun label instead of an action.
    - Current: `Offene-Tabs-Menü`
    - Source: `Open tabs menu`
    - Suggest: `Menü für offene Tabs öffnen`
    - The developer comment says the control "Opens the open tabs menu when pressed"; the German renders only the menu name, dropping the action that the screen reader must convey.
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
- `preferences_marketing_data_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Campaign measurement data" is rendered as "Messdaten für die Kampagne", introducing a definite specific campaign instead of the general term.
    - Current: `Messdaten für die Kampagne`
    - Source: `Campaign measurement data`
    - Suggest: `Daten zur Kampagnenmessung`
    - The source is the generic data category matching the section title "Campaign measurement" (translated "Kampagnenmessung"); "für die Kampagne" implies one specific campaign and breaks consistency with the section title.
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The translation drops "save" and only describes filling in usernames and passwords.
    - Current: `Benutzernamen und Passwörter auf Webseiten bei Nutzung von %1$s automatisch ausfüllen.`
    - Source: `Fill and save usernames and passwords in websites while using %1$s.`
    - Suggest: `Benutzernamen und Passwörter auf Websites bei Nutzung von %1$s ausfüllen und speichern.`
    - The source says "Fill and save usernames and passwords", so the preference covers both filling and saving. The German only mentions filling.
- `protection_panel_etp_toggle_enabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "looks broken" is mistranslated as "beschädigt aussieht" and the imperative drops the "try" hedge.
    - Current: `Wenn etwas auf dieser Website beschädigt aussieht, deaktivieren Sie ihn.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Wenn etwas auf dieser Website nicht richtig funktioniert, versuchen Sie, ihn zu deaktivieren.`
    - The source says the site may appear broken (not working correctly) and suggests trying to turn protection off; "beschädigt aussieht" means physically damaged and the German loses "try".
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

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — Faulty parallel construction: "ein Problem … sein oder jemand, der vorgibt, der Server zu sein".
    - Current: `Dies könnte ein Problem mit der Konfiguration des Servers sein oder jemand, der vorgibt, der Server zu sein.`
    - Source: `{ <ul> } { <li> }This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server.{ </li> } { <li> }If you have connected to this server successfully in the past, the erro…`
    - Suggest: `Dies könnte ein Problem mit der Konfiguration des Servers sein, oder es versucht jemand, sich als der Server auszugeben.`
    - The source has two parallel clauses ("it could be someone trying to impersonate the server"); the German coordination is ungrammatical.
- `notification_erase_text_android_14` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Wrong verb government: "tippen ... auf diese Benachrichtigung" combined with "wischen" is ungrammatical.
    - Current: `Tippen oder wischen Sie auf diese Benachrichtigung`
    - Source: `Tap or swipe this notification to close private tabs.`
    - Suggest: `Tippen Sie auf diese Benachrichtigung oder wischen Sie sie weg`
    - "wischen auf" is not correct German for swiping a notification away; the coordinated construction forces the wrong preposition for one of the verbs.
- `trackers_blocked_panel_num_trackers_blocked_this_week_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — The singular variant uses a plural verb form ("wurden") with a singular subject.
    - Current: `[one] %1$d Tracker wurden in dieser Woche blockiert`
    - Source: `{$quantity ->} [one] %1$d tracker blocked this week [other] %1$d trackers blocked this week`
    - Suggest: `[one] %1$d Tracker wurde in dieser Woche blockiert`
    - In the [one] case the subject is a single tracker, so the verb must be "wurde", not "wurden".
- `wrex_widget_match_penalties` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Typo: "Elfmeterschließen" should be "Elfmeterschießen".
    - Current: `Elfmeterschließen`
    - Source: `Penalties`
    - Suggest: `Elfmeterschießen`
    - The German term for a penalty shootout is "Elfmeterschießen" (from "schießen", to shoot). "Elfmeterschließen" (from "schließen", to close) is a misspelling.

### D. Terminology, register & consistency

- `mozac_browser_toolbar_content_description_tracking_protection_on_no_trackers_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-de/strings.xml` — "Tracking Protection" is translated as "Schutz vor Aktivitätenverfolgung" here but as "Tracking-Schutz" in the two neighbouring toolbar strings.
    - Current: `Schutz vor Aktivitätenverfolgung ist an`
    - Source: `Tracking Protection is on`
    - Suggest: `Der Tracking-Schutz ist an`
    - The same source term on the same surface (tracking protection toolbar icon content descriptions) is rendered two different ways; the adjacent strings use "Tracking-Schutz".
- `mozac_feature_addons_permissions_history_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — Same source string "Access browsing history" is translated inconsistently with its _for_update counterpart ("Auf die Surf-Chronik zugreifen").
    - Current: `Auf Chronik zugreifen`
    - Source: `Access browsing history`
    - Suggest: `Auf die Surf-Chronik zugreifen`
    - mozac_feature_addons_permissions_history_description_for_update uses "Auf die Surf-Chronik zugreifen" for the identical source text; the bare "Auf Chronik zugreifen" also lacks the article.
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
- `nova_onboarding_customize_prompt_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Button label rendered as a full sentence instead of a short imperative action label.
    - Current: `Beginnen Sie mit den Anpassungen`
    - Source: `Start customizing`
    - Suggest: `Anpassung starten`
    - "Start customizing" is a short button label; the German is a drastically longer sentence-style phrasing inconsistent with other button labels in this set (e.g. "Benachrichtigungen aktivieren").
- `preferences_category_sync_controls` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — Category heading "Sync" rendered as a verb ("Synchronisieren") instead of the noun used elsewhere ("Synchronisation").
    - Current: `Synchronisieren`
    - Source: `Sync`
    - Suggest: `Synchronisation`
    - The comment says it is a preference category title, short for "Synchronization"; the noun form is used in the neighbouring strings ("Konto und Synchronisation"), so the imperative verb is inconsistent terminology.
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — "Sync cards" rendered as "Kreditkarten synchronisieren" while the parallel string uses "Karten".
    - Current: `Kreditkarten synchronisieren`
    - Source: `Sync cards`
    - Suggest: `Karten synchronisieren`
    - Source says "cards", and the sibling strings (preferences_credit_cards_sync_cards_across_devices, add card, manage cards) all use "Karten"; "Kreditkarten" is inconsistent and narrower than the source.

### E. Typography, punctuation & spacing

- `mozac_compose_base_progress_loading` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-de/strings.xml` — An ellipsis was added that is not in the source.
    - Current: `Wird geladen…`
    - Source: `Loading`
    - Suggest: `Wird geladen`
    - Source "Loading" has no ellipsis; this is a screen-reader announcement.

---

## 4. Appendix

### Dismissed by hand (8)

- `link_sharing_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02): "Download-Link für %1$s" correctly means the download link for the app; the meaning is not reversed.
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `mozac_protections_dashboard_empty_subtitle` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02): 'Sie werden sie hier sehen.' correctly means 'You will see them here' with formal 'Sie' as subject; the meaning is not reversed.
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>Sounds to me as if this is a deletion process that has been coompleted.</p>
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>Sounds to me as if this is a deletion process that has been coompleted.</p>
- `snackbar_message_bookmarks_saved_in_2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `terms_of_use_prompt_body_line_two_alternative_link` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `terms_of_use_prompt_postpone` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-02): "Später erinnern" is a standard, idiomatic German button label (infinitive style used throughout German UI); no object is required.

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (42)

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_browsing_data_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_data_collection_browsingActivity_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_declarative_net_request_feedback_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_listentopage_error_could_not_finish_playing_audio` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `certificate_warning_push_notification_pnw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `debug_drawer_autofill_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `debug_drawer_logins_add_login_button` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `lens_camera_image_load_failed_v2` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `nova_onboarding_notifications_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `pdf_tools_signature_adding_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `preference_enhanced_tracking_protection_custom_cookies_5` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `preferences_android_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `translations_bottom_sheet_info_message` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `uninstall_survey_button_label` — `mozilla-mobile/fenix/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
