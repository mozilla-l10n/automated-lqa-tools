# Android l10n QA — sk

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `ea17dbc84971` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `ea17dbc84971` |
| **Previous run** | 2026-10-19 @ `7ee8e61a4a7d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 2,802 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for sk: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,802 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 2 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 8, `german-double` 7, `straight-double` 4 | _mixed_ |
| apostrophe | `straight` 2 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 4 | **en** |
| nbsp | `total` 8 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (57)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 30 |
| 3 | Degraded language (grammar, spelling, terminology) | 24 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

- `mozac_feature_listentopage_notification_skip_back` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-sk/strings.xml` — `mozac_feature_listentopage_notification_skip_back` is missing the ['many'] plural form
    - Current: `{$quantity ->} [one] Späť o %1$d sekundu [few] Späť o %1$d sekundy [other] Späť o %1$d sekúnd`
    - Source: `{$quantity ->} [one] Back %1$d second [other] Back %1$d seconds`
    - This locale uses ['few', 'many', 'one', 'other'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `mozac_feature_listentopage_notification_skip_forward` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-sk/strings.xml` — `mozac_feature_listentopage_notification_skip_forward` is missing the ['many'] plural form
    - Current: `{$quantity ->} [one] Dopredu o %1$d sekundu [few] Dopredu o %1$d sekundy [other] Dopredu o %1$d sekúnd`
    - Source: `{$quantity ->} [one] Forward %1$d second [other] Forward %1$d seconds`
    - This locale uses ['few', 'many', 'one', 'other'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — "Compression" is rendered as "formátovanie" (formatting).
    - Current: `neplatné alebo nepodporované formátovanie`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `neplatnú alebo nepodporovanú formu kompresie`
    - The source says the page uses an invalid or unsupported form of compression, but "formátovanie" means formatting, which gives the wrong cause.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — The second bullet replaces the source's "check your network connection" advice with different advice about waiting.
    - Current: `Ak sa dá predpokladať, že server je preťažený, skúste pred ďalším pokusom o pripojenie chvíľu počkať.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Nedajú sa načítať ani iné stránky? Skontrolujte pripojenie zariadenia k sieti.`
    - The source bullet asks whether other sites can be browsed and tells the user to check the device's network connection. The translation instead tells the user to wait if the server is overloaded, so that guidance is lost.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — The verb for 'trust' is missing, so the sentence is incomplete and doesn't say the app distrusts the site.
    - Current: `Aplikácia %1$s nemôže stránku`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `Aplikácia %1$s nedôveruje stránke`
    - Source: '%1$s does not trust %2$s because…'. The Slovak reads 'App %1$s cannot the page %2$s', with no verb, so the statement about trust is lost.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — The translation says the proxy refused the connection, but the source says the proxy could not be found.
    - Current: `no tento odmietol pripojenie.`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `no proxy server sa nepodarilo nájsť.`
    - Source: 'but the proxy could not be found'. The text was copied from the proxy-connection-refused message and describes a different error.
- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sk/strings.xml` — "Clear" is translated as "Čítať" (read), so the permission description is wrong.
    - Current: `Čítať nedávnu históriu prehliadania`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Vymazať nedávnu históriu prehliadania`
    - The browsingData permission lets an extension clear recent history, cookies and related data. The sk text says the extension reads them instead.
- `mozac_feature_addons_permissions_browsing_data_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sk/strings.xml` — "Clear" is translated as "Čítať" (read) in the update-notification version of the browsingData permission.
    - Current: `Čítať nedávnu históriu prehliadania`
    - Source: `Clear recent browsing history, cookies, and related data.`
    - Suggest: `Vymazať nedávnu históriu prehliadania`
    - The source says the extension can clear recent browsing history, cookies and related data. The sk text says it reads them.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sk/strings.xml` — The question is reversed: the source asks "Do you want to leave this site?" but the Slovak asks "Do you want to stay on this site?"
    - Current: `Chcete zostať na tejto stránke?`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `Chcete opustiť túto stránku?`
    - The source and the developer comment both say this dialog appears when the user is leaving a site. "zostať" means "stay", so the question is the opposite of the source. Users who answer it against the dialog's leave/stay buttons could do the opposite of what they intend and lose the data they entered.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-sk/strings.xml` — The translation adds "Relay" after the placeholder, which already holds "Firefox Relay", so users see "Firefox Relay Relay".
    - Current: `služby %s Relay`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `služby %s`
    - The developer comment says %s is the full service name "Firefox Relay", so the extra "Relay" in the target repeats the brand name.
- `mozac_summarize_shake_consent_on_device_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-sk/strings.xml` — The translation says the one-time download is of "content" and ties it to the shake, but the source means a one-time download of the feature that then lets the app summarize pages.
    - Current: `Keď zatrasiete zariadením, %s po rýchlom jednorazovom stiahnutí obsahu vytvorí súhrn stránky.`
    - Source: `After a quick one-time download, %s can summarize pages when you shake your device.`
    - Suggest: `Po rýchlom jednorazovom stiahnutí dokáže %s vytvárať súhrny stránok, keď zatrasiete zariadením.`
    - The en-US says that after a one-time download (of the on-device model), the app can summarize pages on shake. The added "obsahu" (of content) makes it a download of page content, and the word order blurs the fact that the download happens once, before the feature is used.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Item Menu" is translated with the plural "menu of items" instead of the menu of one item.
    - Current: `Ponuka položiek pre %s`
    - Source: `Item Menu for %s`
    - Suggest: `Ponuka položky pre %s`
    - Here %s is a single bookmark or folder, and the menu belongs to that one item. The plural "položiek" means a menu listing items.
- `collections_migration_homepage_card_message` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Tabs" is translated as "záložkách" (bookmarks) instead of "kartách" (tabs).
    - Current: `poriadok v záložkách`
    - Source: `There’s a simpler way to keep your tabs organized`
    - Suggest: `poriadok v kartách`
    - In the sk Firefox localization, "záložky" means bookmarks and "karty" means tabs, as the neighbouring strings show (Otvoriť karty, skupiny kariet). The message is about keeping tabs organized, so it currently refers to the wrong feature.
- `debug_drawer_cfr_tools_reset_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Reset CFRs" is rendered as "Reset CFR tools" instead of resetting the recommendations themselves.
    - Current: `Obnoviť nástroje CFR`
    - Source: `Reset CFRs`
    - Suggest: `Obnoviť CFR`
    - The source resets the contextual feature recommendations (CFRs); the translation says the CFR tools are reset, which names a different object.
- `default_browser_experiment_card_text` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The translation drops "links from", so it says websites, emails and messages themselves will open in Firefox rather than the links in them.
    - Current: `Nastavte si automatické otváranie webových stránok, e‑mailov a správ vo Firefoxe.`
    - Source: `Set links from websites, emails, and messages to open automatically in Firefox.`
    - Suggest: `Nastavte si automatické otváranie odkazov z webových stránok, e‑mailov a správ vo Firefoxe.`
    - The source is about links from websites, emails and messages opening in Firefox. The Slovak says emails and messages open in Firefox, which is a different and inaccurate claim.
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Browsing data" is translated as "private data" (súkromné údaje).
    - Current: `súkromné údaje`
    - Source: `Deleting browsing data…`
    - Suggest: `údaje prehliadania`
    - The source and the developer comment both refer to browsing data. "Súkromné údaje" names a different category of data.
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The "• pending" status is missing from the translation.
    - Current: `%1$s / %2$s`
    - Source: `%1$s / %2$s • pending`
    - Suggest: `%1$s / %2$s • čaká sa`
    - The source adds a "pending" status after the sizes to show that the remaining time is still being calculated. The translation shows only the sizes.
- `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "private" is translated as "bezpečný" (secure), so the product calls itself secure rather than private.
    - Current: `rýchly a bezpečný`
    - Source: `Firefox is fast and private`
    - Suggest: `rýchly a súkromný`
    - The source says Firefox is fast and private. The Slovak claims a different property, security, which the source never claimed.
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "in apps" (generic) is rendered as "in this app", changing the scope of the feature.
    - Current: `v tejto aplikácii`
    - Source: `You can set %1$s to automatically open links in apps.`
    - Suggest: `v aplikáciách`
    - The source says the user can make Firefox open links in apps in general. The Slovak says "in this app", which points to one specific app that the message never names.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The second sentence leaves out the instruction to turn off this toggle and the word "here", and tells users to adjust their settings instead.
    - Current: `Ak chcete spravovať veľkosť písma, upravte svoje nastavenia.`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `Ak chcete spravovať veľkosť písma tu, túto možnosť vypnite.`
    - The source says 'Disable to manage font size here', meaning turn off this toggle to set font size in the app. The translation says 'If you want to manage font size, adjust your settings', which sends the user somewhere else and drops 'disable'.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Prevent this gesture" is translated as "do not support this gesture".
    - Current: `ktoré toto gesto nepodporujú`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `ktoré toto gesto blokujú`
    - The source says websites 'prevent' (block) pinch-zoom, and that is the reason this setting exists. 'Nepodporujú' means the sites don't support the gesture, which is a different statement.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The translation leaves out cross-site trackers and mentions only social media trackers.
    - Current: `Sledovacie prvky sociálnych sietí`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Sledovacie prvky sociálnych sietí a sledovanie medzi stránkami`
    - The source option covers both cross-site trackers and social media trackers. The Slovak names only social media trackers, so it misstates what this cookie option blocks.
- `preference_enhanced_tracking_protection_standard_description_5` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The translation says pages will contain fewer trackers, but the source says Standard mode blocks fewer trackers.
    - Current: `no budú obsahovať menej sledovacích prvkov`
    - Source: `Pages will load normally, but block fewer trackers.`
    - Suggest: `no bude blokovaných menej sledovacích prvkov`
    - The source describes a trade-off: pages load normally, but fewer trackers are blocked, so more trackers remain. The Slovak says the opposite, that pages will contain fewer trackers.
- `search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The 'or enter address' part of the placeholder is missing.
    - Current: `Hľadať`
    - Source: `Search or enter address`
    - Suggest: `Hľadať alebo zadať adresu`
    - Source is 'Search or enter address'. The target only says 'Search', which is the same as search_hint_short and leaves out the address-entry hint.
- `search_settings_menu_item` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Search settings" (settings for search) is translated as the action "Search in settings".
    - Current: `Hľadať v nastaveniach`
    - Source: `Search settings`
    - Suggest: `Nastavenia vyhľadávania`
    - The menu item opens the search settings; the target instead means 'search within settings'.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Search" is translated as a noun, so the title reads "Settings for search" instead of "Search through settings".
    - Current: `Nastavenia vyhľadávania`
    - Source: `Search settings`
    - Suggest: `Hľadať v nastaveniach`
    - The developer comment says "Search" is a verb here, because the screen searches through settings. "Nastavenia vyhľadávania" means "search settings" as a noun phrase, which suggests the search engine preferences page.
- `tab_manager_empty_tab_groups_page_header` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The translation renders "more doing" as "more having fun", which changes the meaning.
    - Current: `viac sa zabávať`
    - Source: `Try tab groups for less scrolling, more doing`
    - Suggest: `viac stihnúť`
    - The en-US "less scrolling, more doing" is about getting more done. "Zabávať sa" means entertaining oneself or having fun, which is a different idea.
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The translation counts open tabs instead of open tab groups.
    - Current: `%1$d otvorená karta.`
    - Source: `{$quantity ->} [one] %1$d tab group open. Tap to switch tabs. [other] %1$d tab groups open. Tap to switch tabs.`
    - Suggest: `%1$d otvorená skupina kariet.`
    - The source and the developer comment both say this is the number of open tab groups. The Slovak drops "group" in every plural form (karta/karty/kariet), so screen readers announce a tab count. The other forms need the same fix: few "%1$d otvorené skupiny kariet", many/other "%1$d otvorených skupín kariet".
- `translation_option_bottom_sheet_switch_description` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — 'Nebude ponúkať preklad' means 'will not offer translation', but the source says these settings take priority over the offer-to-translate setting.
    - Current: `Nebude ponúkať preklad`
    - Source: `Overrides offers to translate`
    - Suggest: `Má prednosť pred ponukami na preklad`
    - The developer comment says this text explains how the Never/Always translate switches interact with other settings: they override the 'offer to translate' setting. Under 'Always translate', the Slovak text misleadingly says no translation will be offered.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "check out" is rendered as "view the cart" instead of completing the purchase.
    - Current: `zobraziť košík`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `dokončiť objednávku`
    - In the source, "check out" means completing the order or payment. It does not mean viewing the cart, which "zobraziť košík" says.
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — "Your search, your way" is translated as "Browsing your way", replacing search with browsing.
    - Current: `Prehliadanie podľa vás`
    - Source: `Your search, your way`
    - Suggest: `Vyhľadávanie podľa vás`
    - The source title refers to search (this is the Search page of the first-run tour), but "Prehliadanie" means browsing, so the title is about the wrong feature.
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The Slovak drops the clause "or see what's running in your browser" and changes "session" to "history".
    - Current: `Nemusíte ani otvárať aplikáciu.`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Nemusíte otvárať aplikáciu ani vidieť, čo je spustené vo vašom prehliadači.`
    - The source says the user does not need to open the app or see what is running in the browser. The translation keeps only the first part, so content that conveys the discreet-erase benefit is missing.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The translation leaves out "measure" and the "tapping" example from the source.
    - Current: `na zbieranie a analýzu údajov o aktivitách, napríklad o posúvaní sa na stránke`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `na zbieranie, analýzu a meranie aktivít, ako je ťukanie a posúvanie`
    - The source says "collect, analyze and measure activities like tapping and scrolling"; the Slovak keeps only collecting/analysis and only scrolling.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_safe_browsing_unwanted_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — Spelling error: standard Slovak is 'nežiaduca' (short u), not 'nežiadúca'.
    - Current: `Nežiadúca`
    - Source: `Unwanted site issue`
    - Suggest: `Nežiaduca`
    - Standard Slovak spelling is 'žiaduci/nežiaduci'. The form with a long 'ú' is a common misspelling.
- `mozac_extension_install_progress_caption` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-sk/strings.xml` — The reflexive particle "sa" is duplicated in the caption.
    - Current: `Rozšírenie sa sťahuje sa a overuje…`
    - Source: `Downloading and verifying extension…`
    - Suggest: `Rozšírenie sa sťahuje a overuje…`
    - The two verbs share one reflexive "sa". The second "sa" is a grammatical error that makes the sentence read as broken.
- `bookmark_add_folder` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Wrong genitive form of "priečinok": standard Slovak is "priečinka", not "priečinku".
    - Current: `Pridanie priečinku`
    - Source: `Add folder`
    - Suggest: `Pridanie priečinka`
    - Standard Slovak dictionaries give the genitive singular of "priečinok" as "priečinka". The "-u" ending is a common non-standard form.
- `bookmark_select_folder_fragment_label` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Wrong genitive form of "priečinok".
    - Current: `Výber priečinku`
    - Source: `Select folder`
    - Suggest: `Výber priečinka`
    - The standard genitive singular of "priečinok" is "priečinka", not "priečinku".
- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Typo: the conditional particle "by" is written as "my".
    - Current: `ktoré my mohli byť použité`
    - Source: `Stops uniquely identifiable data from being collected about your device that can be used for tracking purposes.`
    - Suggest: `ktoré by mohli byť použité`
    - The Slovak conditional needs "by" ("which could be used"). "my" means "we", so the sentence is ungrammatical.
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Wrong case: "každý mesiac" must be genitive after "v prvý deň".
    - Current: `v prvý deň každý mesiac`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `v prvý deň každého mesiaca`
    - "On the first of every month" requires genitive "každého mesiaca"; the nominative/accusative form is ungrammatical here.
- `preference_enhanced_tracking_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Typo: 'sledovaciu' should be the dative noun 'sledovaniu'.
    - Current: `proti sledovaciu medzi stránkami`
    - Source: `Now featuring Total Cookie Protection, our most powerful barrier yet against cross-site trackers.`
    - Suggest: `proti sledovaniu medzi stránkami`
    - 'Proti' takes the dative, so the noun has to be 'sledovaniu'. 'Sledovaciu' is a misspelling, and it is the form of a different word (the adjective).
- `preference_option_autoplay_allowed_wifi_subtext` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The verb is singular even though its subject, "Zvuk a video", is a compound subject that comes before it.
    - Current: `Zvuk a video sa bude`
    - Source: `Audio and video will play on Wi-Fi`
    - Suggest: `Zvuk a video sa budú`
    - In Slovak, a compound subject placed before the verb takes a plural verb, so it should be "Zvuk a video sa budú automaticky prehrávať".
- `preferences_https_only_off` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The 'Off' summary uses the masculine form while the matching 'On' summaries of the same preference use the neuter form.
    - Current: `Vypnutý`
    - Source: `Off`
    - Suggest: `Vypnuté`
    - The sibling summaries for the HTTPS-Only preference (preferences_https_only_on_all and preferences_https_only_on_private) use the neuter 'Zapnuté'. The 'Off' state of the same setting should use the same gender.
- `preferences_passwords_saved_logins_description_empty_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The relative clause is missing its closing comma before the main verb.
    - Current: `do %su budú zobrazené tu`
    - Source: `The passwords you save or sync to %s will be listed here. All passwords you save are encrypted.`
    - Suggest: `do %su, budú zobrazené tu`
    - Slovak punctuation rules require a comma after the relative clause "ktoré uložíte alebo synchronizujete do %su" and before the main clause continues.
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "nahraďte výraz s" is an incorrect construction; nahradiť takes the instrumental case without a preposition.
    - Current: `Nahraďte výraz s „%s“`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `Nahraďte výraz výrazom „%s“`
    - In standard Slovak it is 'nahradiť niečo niečím'. Using 's' here is a grammatical error.
- `sign_out_confirmation_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — 'z toho zariadenia' means 'from that device'; the source says 'this device', which is 'z tohto zariadenia'.
    - Current: `z toho zariadenia`
    - Source: `%s will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `z tohto zariadenia`
    - The source says 'on this device'. The standard Slovak demonstrative for 'this' is 'tento/tohto', while 'toho' is the form of 'ten' ('that').
- `sign_out_confirmation_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Wrong instrumental form of the possessive pronoun: 'vašim' instead of 'vaším'.
    - Current: `s vašim účtom`
    - Source: `%s will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `s vaším účtom`
    - The instrumental singular masculine of 'váš' is 'vaším' (long í). 'vašim' is the dative plural form.
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Possessive pronoun in instrumental singular is misspelled as "Našim" instead of "Naším".
    - Current: `Našim poslaním`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Naším poslaním`
    - Instrumental singular of "náš" is "naším" (long í); "našim" is the dative plural form.
- `preference_privacy_block_ads_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Missing comma before the subordinate clause "aj keď".
    - Current: `Niektoré reklamy vás sledujú aj keď na ne nekliknete`
    - Source: `Some ads track site visits, even if you don’t click the ads`
    - Suggest: `Niektoré reklamy vás sledujú, aj keď na ne nekliknete`
    - Slovak punctuation rules require a comma before the conjunction "aj keď" that introduces a subordinate clause.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Genitive plural 'aplikácii' is misspelled; it should be 'aplikácií'.
    - Current: `nedávnych aplikácii`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `nedávnych aplikácií`
    - The genitive plural after 'nedávnych' needs the long í ending, so it is 'aplikácií'.
- `promote_search_widget_button_text` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The button label uses the third-person 'Pridá' ('it adds') instead of the infinitive used for actions.
    - Current: `Pridá miniaplikáciu`
    - Source: `Add widget to home screen`
    - Suggest: `Pridať miniaplikáciu`
    - This is a button label for an action. Slovak UI uses the infinitive for actions, as in other strings here ('Pridať ďalší vyhľadávací modul').

### D. Terminology, register & consistency

- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Location" rendered as "miesto" while all other VPN location strings use "lokalita".
    - Current: `Prepnuté na odporúčané miesto.`
    - Source: `Switched to the recommended location.`
    - Suggest: `Prepnuté na odporúčanú lokalitu.`
    - The same phrase "Switched to the recommended location" is translated "Prepnuté na odporúčanú lokalitu" in ip_protection_location_selection_reset_snackbar; the VPN surface consistently uses "lokalita".
- `preferences_privacy_report` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — "Privacy report" is translated as "ochrane osobných údajov" in the category header but as "ochrane súkromia" in the toggle directly under it.
    - Current: `Správa o ochrane osobných údajov`
    - Source: `Privacy report`
    - Suggest: `Správa o ochrane súkromia`
    - The header and the toggle (preferences_privacy_report_title) name the same feature on the same screen. "Ochrana osobných údajov" means personal data protection, not privacy, so the two labels don't match.
- `trackers_blocked_panel_num_trackers_blocked_this_week_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The 'many' and 'other' forms say 'sledovacích zariadení' (tracking devices), not 'sledovacích prvkov' (trackers).
    - Current: `bolo zablokovaných %1$d sledovacích zariadení`
    - Source: `{$quantity ->} [one] %1$d tracker blocked this week [other] %1$d trackers blocked this week`
    - Suggest: `bolo zablokovaných %1$d sledovacích prvkov`
    - This uses the wrong term. It does not match the 'few' form of the same message or the other tracker-count strings, which use 'sledovacích prvkov'.
- `trackers_blocked_panel_num_trackers_blocked_this_week_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — The 'one' form says 'sledovacie zariadenie' (tracking device), not 'sledovací prvok' (tracker) as in the 'few' form and the other tracker strings.
    - Current: `bolo zablokované %1$d sledovacie zariadenie`
    - Source: `{$quantity ->} [one] %1$d tracker blocked this week [other] %1$d trackers blocked this week`
    - Suggest: `bol zablokovaný %1$d sledovací prvok`
    - The source means a tracker. 'Zariadenie' means a hardware device. Within this one message, the 'few' form uses 'sledovacie prvky', and the rest of the tracker panel uses 'sledovací prvok'.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-sk/strings.xml` — The first paragraph has no full stop at the end.
    - Current: `Skúste to znova{ </p> }`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `Skúste to znova.{ </p> }`
    - The source sentence "Please try again." ends with a full stop, and the translation leaves it out.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — A spaced hyphen is used as a dash where the locale's house style is the en dash.
    - Current: `Pošta - mesto`
    - Source: `Post town`
    - Suggest: `Pošta – mesto`
    - The sk conventions use the en dash. A hyphen with a space on each side is standing in for a dash here.
- `search_add_custom_engine_suggest_string_example_2` — `mozilla-mobile/fenix/app/src/main/res/values-sk/strings.xml` — Uses English-style curly quotes instead of the Slovak „“ used in the sibling string.
    - Current: `“%s”`
    - Source: `Replace query with “%s”. Example: https://suggestqueries.google.com/complete/search?client=firefox&q=%s`
    - Suggest: `„%s“`
    - Slovak uses low-high quotes, and the matching search-string example string already uses „%s“.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
