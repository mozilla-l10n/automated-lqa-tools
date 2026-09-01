# Android l10n QA — pl

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **Previous run** | 2026-08-24 @ `e8622a909368` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 2,717 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pl: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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

### 🗑 Retired — the string no longer exists upstream (7)

- `add_to_homescreen_continue` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Continue to website" is translated as "Wróć do strony" (Go back to the website).
    - Current: `Wróć do strony`
    - Suggest: `Przejdź do strony`
    - The source means to continue on to the website, not to go back to it.
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Round of 16" is rendered as "Druga runda" (second round) instead of the knockout stage name.
    - Current: `Druga runda`
    - Suggest: `1/8 finału`
    - The developer comment says this is the Round of 16 stage of the tournament; Polish uses "1/8 finału" for that knockout stage, not "druga runda", which names a generic second round.
- `sports_widget_round_of_32` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Round of 32" is rendered as "Pierwsza runda" (first round) instead of the knockout stage name.
    - Current: `Pierwsza runda`
    - Suggest: `1/16 finału`
    - The developer comment says this is the Round of 32 knockout stage; Polish names it "1/16 finału", not a generic "pierwsza runda".
- `sports_widget_team_to_be_determined` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Singular "Team to be determined" is translated with a plural subject.
    - Current: `Drużyny nie są jeszcze znane`
    - Suggest: `Drużyna nie jest jeszcze znana`
    - The source describes a single team slot that has not yet been determined; the Polish plural changes the meaning to multiple teams.
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — The translation drops "cookie banners" and mistranslates the sentence, saying Firefox rejects "annoying cookie requests" instead of rejecting cookie requests in order to dismiss annoying cookie banners.
    - Current: `%1$s próbuje odrzucać irytujące prośby o akceptację ciasteczek.  Zarządzaj preferencjami odrzucania w %2$s.`
    - Suggest: `%1$s próbuje odrzucać prośby o zgodę na ciasteczka, aby zamykać irytujące banery o ciasteczkach.  Zarządzaj preferencjami dotyczącymi banerów o ciasteczkach w %2$s.`
    - Source: "tries to reject cookie requests to dismiss annoying cookie banners" and "Manage cookie banner preferences"; the Polish omits the cookie banner concept entirely in both sentences.
- `menu_trackers_blocked_title` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — "Trackers blocked" is rendered as the generic "Blokowanie" (Blocking), losing the meaning.
    - Current: `Blokowanie`
    - Suggest: `Zablokowane elementy śledzące`
    - The source label names the count of blocked trackers; "Blokowanie" means merely "Blocking" and drops the tracker concept.
- `preference_autocomplete_custom_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — Misspelled/incorrectly formed verbal noun "zarządzenie" instead of "zarządzanie", and wrong case government.
    - Current: `Dodawanie i zarządzenie innymi adresami automatycznego uzupełniania.`
    - Suggest: `Dodawanie innych adresów automatycznego uzupełniania i zarządzanie nimi.`
    - "zarządzenie" is a different word (an ordinance/decree); the gerund of "zarządzać" is "zarządzanie". Also "Dodawanie ... adresami" is ungrammatical since "dodawanie" requires the genitive.

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 43 |
| Strings | 2,717 |
| Missing strings | 18 |
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

**18 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — 13
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-pl/strings.xml` — 5

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 84 | **polish-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2, `en` 3 | _mixed_ |
| nbsp | `total` 655, `before-punctuation` 14 | **total** |
| register | `informal` 9 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (86)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 62 |
| 3 | Degraded language (grammar, spelling, terminology) | 23 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pl/strings.xml` — "The connection was reset" is rendered identically to the "connection was interrupted" title, losing the distinction between the two error pages.
    - Current: `Przerwane połączenie`
    - Source: `The connection was reset`
    - Suggest: `Połączenie zostało zresetowane`
    - The source says the connection was reset, not interrupted; the same Polish text is already used for mozac_browser_errorpages_net_interrupt_title, making two distinct errors indistinguishable.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pl/strings.xml` — The third bullet mistranslates the firewall/proxy item, asking whether the program is allowed to connect instead of stating that incorrect settings can interfere with browsing.
    - Current: `Jeśli to urządzenie jest chronione przez zaporę sieciową lub serwer proxy, sprawdź, czy ten program jest uprawniony do łączenia się z Internetem.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Czy to urządzenie lub sieć są chronione przez zaporę sieciową lub serwer proxy? Nieprawidłowe ustawienia mogą zakłócać przeglądanie sieci.`
    - The source states that incorrect firewall/proxy settings can interfere with web browsing; the translation instead tells the user to check whether the program is permitted to connect, which is different content.
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pl/strings.xml` — Source says the port is normally used for purposes other than Web browsing; the Polish says it is normally not used for browsing, altering the meaning.
    - Current: `który zazwyczaj { <em> }nie jest{ </em> } wykorzystywany do przeglądania witryn WWW`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `który zazwyczaj jest wykorzystywany { <em> }do innych celów{ </em> } niż przeglądanie witryn WWW`
    - The emphasis in the source is on "other" purposes, i.e. the port serves a different function, not merely that it is unused for browsing.
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pl/strings.xml` — "host server" rendered as "adres serwera", duplicating "adres" and losing the meaning of host.
    - Current: `Przeglądarka nie mogła odnaleźć adresu serwera dla podanego adresu.`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `Przeglądarka nie mogła odnaleźć serwera dla podanego adresu.`
    - Source says the browser could not find the host server for the provided address; the Polish says it could not find the server's address for the provided address, which is redundant and inaccurate.
- `mozac_feature_addons_addons_manager` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — Noun phrase "Add-ons Manager" translated as an imperative verb phrase "Zarządzaj dodatkami".
    - Current: `Zarządzaj dodatkami`
    - Source: `Add-ons Manager`
    - Suggest: `Menedżer dodatków`
    - The developer comment identifies it as a label for the add-ons manager, a noun label, not an action.
- `mozac_feature_addons_admin_install_only` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — "enterprise policies" is rendered as "zasad organizacji", duplicating "organizacja" and losing the term; also the relative clause implies the policies are unsupported rather than the mechanism.
    - Current: `wyłącznie organizacja korzystająca z zasad organizacji, które nie są obsługiwane na tej platformie`
    - Source: `%1$s could not be installed because it can only be installed by an organization using enterprise policies, which isn‘t supported on this platform.`
    - Suggest: `wyłącznie organizacja korzystająca z zasad firmowych, które nie są obsługiwane na tej platformie`
    - The source term is "enterprise policies"; repeating "organizacja" twice is a terminology error in Polish Mozilla builds, where "zasady firmowe" is used.
- `mozac_feature_addons_extension_failed_to_install_network_error` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — Source says the extension could not be downloaded, but the translation says it could not be installed.
    - Current: `Nie udało się zainstalować tego rozszerzenia z powodu błędu połączenia.`
    - Source: `This extension could not be downloaded because of a connection failure.`
    - Suggest: `Nie udało się pobrać tego rozszerzenia z powodu błędu połączenia.`
    - en-US: "This extension could not be downloaded because of a connection failure." — "downloaded" (pobrane), not "installed".
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — "additional settings" is rendered as "nowe ustawienia" (new settings) instead of "dodatkowe ustawienia".
    - Current: `prosi o nowe ustawienia`
    - Source: `%1$s requests additional settings`
    - Suggest: `prosi o dodatkowe ustawienia`
    - The source says "additional settings"; the parallel string uses "dodatkowe" for "additional", so "nowe" (new) changes the meaning and is inconsistent.
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — "The developer says the extension wants to collect" is mistranslated as the extension "asking for" collection rather than wanting to collect.
    - Current: `Autorzy rozszerzenia twierdzą, że prosi ono o zbieranie: %1$s`
    - Source: `The developer says the extension wants to collect: %1$s`
    - Suggest: `Autorzy rozszerzenia twierdzą, że chce ono zbierać: %1$s`
    - The source states the extension wants to collect the listed data; "prosi o zbieranie" (asks for collection) alters the statement.
- `mozac_feature_addons_permissions_top_sites_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pl/strings.xml` — "topSites" permission description translated as access to browsing history instead of top sites.
    - Current: `Dostęp do historii przeglądania`
    - Source: `Access browsing history`
    - Suggest: `Dostęp do najczęściej odwiedzanych stron`
    - Source is "Access browsing history"… actually the source says browsing history; mirrors source.
- `mozac_feature_downloads_cancel_active_downloads_warning_content_title` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-pl/strings.xml` — The word "private" is dropped from the dialog title about cancelling private downloads.
    - Current: `Czy anulować pobieranie plików?`
    - Source: `Cancel private downloads?`
    - Suggest: `Czy anulować prywatne pobieranie?`
    - Source is "Cancel private downloads?"; the Polish omits "private", losing the distinction that only private-mode downloads are affected.
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — "Label for entering a text input field" is rendered as "label for navigating to the field", changing the meaning.
    - Current: `Etykieta przechodzenia do pola wprowadzania tekstu`
    - Source: `Label for entering a text input field`
    - Suggest: `Etykieta pola wprowadzania tekstu`
    - The source is a label for a text input field (where the user types text), not a label about "going to"/navigating to it.
- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — "for future use" is mistranslated as "aby zawsze mieć do niego dostęp" (so you always have access to it).
    - Current: `aby zawsze mieć do niego dostęp`
    - Source: `Protect your account by using a strong, randomly generated password. It’ll be saved into your account for future use.`
    - Suggest: `do użycia w przyszłości`
    - The source states the password will be saved into the account for future use; the Polish invents a claim about always having access.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — "on mobile" is rendered as "na telefonie" (on the phone), narrowing the meaning to phones only.
    - Current: `są teraz dostępne na telefonie`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `są teraz dostępne na urządzeniach mobilnych`
    - The source says the masks are available on mobile (mobile devices generally, including tablets), not specifically "on the phone".
- `mozac_feature_sitepermissions_do_not_ask_again_on_this_site2` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-pl/strings.xml` — "Remember decision for this site" is rendered as "Nie pytaj ponownie na tej witrynie" ("Don't ask again on this site").
    - Current: `Nie pytaj ponownie na tej witrynie`
    - Source: `Remember decision for this site`
    - Suggest: `Zapamiętaj decyzję dla tej witryny`
    - The source says to remember the decision, not to stop asking; the parallel string ...site4 correctly uses "Zapamiętaj dla tej witryny".
- `mozac_summarize_settings_summarize_pages_cloud` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-pl/strings.xml` — "stay private" was rendered as "są zawsze prywatne" (are always private), adding a claim not in the source.
    - Current: `Strony i ich streszczenia są zawsze prywatne i nigdy nie są nigdzie przechowywane.`
    - Source: `Create page summaries with AI. Pages and summaries stay private and are never stored.`
    - Suggest: `Strony i ich streszczenia pozostają prywatne i nigdy nie są przechowywane.`
    - The source says pages and summaries stay private and are never stored; the Polish adds "zawsze" and "nigdzie", changing the strength of the privacy claim.
- `ai_controls_block_ai_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "or pop-ups about them" is rendered as "czy nawet informacji o nich", adding "nawet" and dropping the pop-up notion.
    - Current: `czy nawet informacji o nich`
    - Source: `Blocking means you won’t see new or current AI enhancements in %s, or pop-ups about them.`
    - Suggest: `ani wyskakujących okien na ich temat`
    - The source says the user won't see pop-ups about the AI enhancements; the Polish says "or even information about them", changing the meaning and omitting "pop-ups".
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "or pop-ups about them" mistranslated as "czy nawet informacji o nich".
    - Current: `czy nawet informacji o nich`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `ani wyskakujących okien na ich temat`
    - Source refers to pop-ups about the AI enhancements, not to "even information about them".
- `alternative_app_icon_option_minimal` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Minimal" is rendered as the non-existent word "Minimalis".
    - Current: `Minimalis`
    - Source: `Minimal`
    - Suggest: `Minimalistyczna`
    - The source "Minimal" describes a simplified icon style; "Minimalis" is not a Polish word and does not convey the meaning.
- `alternative_app_icon_option_pixelated` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Pixelated" is rendered as the non-existent word "Pikselis".
    - Current: `Pikselis`
    - Source: `Pixelated`
    - Suggest: `Pikselowa`
    - The source describes a pixel-art icon; "Pikselis" is not a Polish word.
- `alternative_app_icon_option_retro_2004` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Retro 2004" is rendered as the non-existent word "Retrolis 2004".
    - Current: `Retrolis 2004`
    - Source: `Retro 2004`
    - Suggest: `Retro 2004`
    - "Retro" is used in Polish as-is; "Retrolis" is not a Polish word and misrepresents the source.
- `app_name_private_5` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Translation adds parentheses not present in the source "Private %s".
    - Current: `%s (tryb prywatny)`
    - Source: `Private %s`
    - Suggest: `%s — tryb prywatny`
    - app_name_private_5 is a distinct variant without parentheses; rendering it identically to app_name_private_4 loses the intended distinction.
- `application_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Enter search terms" is translated merely as "Szukaj" (Search).
    - Current: `Szukaj`
    - Source: `Enter search terms`
    - Suggest: `Wpisz wyszukiwane słowa`
    - The source is an instruction to enter search terms, not the label "Search".
- `bookmark_sort_menu_custom` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "custom order" (user-defined order) translated as "innej kolejności" (another/different order).
    - Current: `Sortuj według innej kolejności`
    - Source: `Sort by custom order`
    - Suggest: `Sortuj według własnej kolejności`
    - The developer comment says sorting is by user-defined sort order; "inna kolejność" means simply a different order, losing the meaning of a user-defined/custom order.
- `browser_menu_powered_by2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Powered by %1$s" is rendered as "Funkcja przeglądarki %1$s" ("A feature of browser %1$s"), which changes the meaning.
    - Current: `Funkcja przeglądarki %1$s`
    - Source: `Powered by %1$s`
    - Suggest: `Obsługiwane przez %1$s`
    - The source indicates the custom tab is powered by the app; the Polish says it is a feature of the browser, a different statement.
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "log you out of websites and clear shopping carts" (plural, general) is rendered as singular "ze strony" and "koszyka w sklepie", and "and" becomes "lub".
    - Current: `może spowodować wylogowanie ze strony lub opróżnienie koszyka w sklepie`
    - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
    - Suggest: `może spowodować wylogowanie z witryn i opróżnienie koszyków w sklepach`
    - Source says removing data may log the user out of websites and clear shopping carts (plural, conjunction "and"); the Polish narrows it to one page/one cart and changes the conjunction to "or".
- `customize_toggle_privacy_report` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Privacy report" translated as "Informacja o prywatności" (privacy notice) instead of a report.
    - Current: `Informacja o prywatności`
    - Source: `Privacy report`
    - Suggest: `Raport prywatności`
    - A privacy report is a summary of blocked trackers, not a privacy notice/information statement; "Informacja o prywatności" corresponds to a different feature.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "for selected locale" mistranslated as "do wybranych ustawień regionalnych" (adding an address to the settings).
    - Current: `Dodaj nowy adres do wybranych ustawień regionalnych`
    - Source: `Add new address for selected locale`
    - Suggest: `Dodaj nowy adres dla wybranych ustawień regionalnych`
    - The source means adding an address formatted for the selected locale, not adding an address into the locale settings; the preposition "do" reverses the relationship.
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "home and current region values" rendered as "wartości lokalne i regionalne", losing the home/current region distinction.
    - Current: `Tymczasowo zastępuje wartości lokalne i regionalne do celów testowych.`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `Tymczasowo zastępuje wartości regionu lokalnego i obecnego do celów testowych.`
    - The source refers to two region values (home region and current region); the translation says "local and regional values", which is a different meaning and inconsistent with the neighbouring strings that use "region lokalny" and "obecny region".
- `default_browser_experiment_card_text` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "messages" is narrowed to "SMS-ów" (text messages only).
    - Current: `wiadomości e-mail i SMS-ów`
    - Source: `Set links from websites, emails, and messages to open automatically in Firefox.`
    - Suggest: `wiadomości e-mail i wiadomości`
    - The source says "emails, and messages" generically, not specifically SMS.
- `delete_language_file_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Placeholder %1$s is the language name, but the Polish text renders it as an unnamed "this language" plus size, losing the language name reference.
    - Current: `Czy usunąć ten język (%1$s – %2$s)?`
    - Source: `Delete %1$s (%2$s)?`
    - Suggest: `Czy usunąć język %1$s (%2$s)?`
    - Per the developer comment %1$s is the language name (e.g. "Spanish") and %2$s the file size; the translation says "delete this language (Spanish – 5 MB)", changing the sentence structure and implying the placeholders are of the same kind.
- `download_language_file_dialog_checkbox_text` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Always download" is rendered as "Pobieraj także" ("Download also"), losing the meaning of the checkbox.
    - Current: `Pobieraj także w trybie oszczędzania danych`
    - Source: `Always download in data saving mode`
    - Suggest: `Zawsze pobieraj w trybie oszczędzania danych`
    - The source says the download should always happen in data saving mode; "także" means "also/too", which is a different statement.
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "You've used your 5 free email masks" is rendered as "5 masks have already been created", losing the meaning of having used up the free allowance.
    - Current: `5 bezpłatnych masek dla adresu e-mail zostało już utworzonych`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `Wszystkie 5 bezpłatnych masek dla adresu e-mail zostało już wykorzystanych`
    - The source says the user has used up all their free masks; the translation says they were created, which does not convey the exhausted quota.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "%1$s tabs closed" is rendered as "tabs of the %1$s browser closed", altering the meaning.
    - Current: `Zamknięto karty przeglądarki %1$s: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s — zamknięto karty: %2$d`
    - The developer comment says %1$s is the app name and the notification reports the number of closed tabs; "karty przeglądarki Firefox" implies the tabs belong to a specific browser rather than being an app-name prefix, but the meaning shift is minor.
- `history_search_group_site_1` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Singular form "%d page" is rendered with a plural-style label identical to the plural string.
    - Current: `Strony: %d`
    - Source: `%d page`
    - Suggest: `Strona: %d`
    - The source distinguishes singular (%d page) from plural (%d pages); the Polish singular string uses the same plural wording as history_search_group_sites_1, losing the distinction.
- `ip_protection_mozilla_vpn_upsell_button` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Get Mozilla VPN" is translated as "Wypróbuj Mozilla VPN" (Try Mozilla VPN).
    - Current: `Wypróbuj Mozilla VPN`
    - Source: `Get Mozilla VPN`
    - Suggest: `Pobierz Mozilla VPN`
    - The button takes the user to get the standalone product; "Wypróbuj" means "Try", which is a different call to action and duplicates the wording used for "Try it now" elsewhere.
- `ip_protection_navigate_settings` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The content description drops the action verb "Open", describing the target as a label rather than the control's action.
    - Current: `Ustawienia VPN`
    - Source: `Open VPN settings`
    - Suggest: `Otwórz ustawienia VPN`
    - Source is "Open VPN settings" and the developer comment says it is a content description for a chevron button that opens the settings screen; the Polish only says "VPN settings".
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "the platform you came from" mistranslated as "the platform Firefox was downloaded from".
    - Current: `platformę, z której pobrano Firefoksa`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `platformę, z której trafiono do Firefoksa`
    - Per the developer comment, the platform is the external app, website, store or campaign that directed the user to Firefox, not necessarily where it was downloaded from.
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "the platform you came from" mistranslated as "the platform Firefox was downloaded from".
    - Current: `platformę, z której pobrano Firefoksa`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `platformę, z której trafiono do Firefoksa`
    - Per the developer comment, the platform is the source that directed the user to Firefox, not the download source.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "the platform you came from" mistranslated as "the platform Firefox was downloaded from".
    - Current: `platformę, z której pobrano Firefoksa`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `platformę, z której trafiono do Firefoksa`
    - Per the developer comment, the platform is the source that directed the user to Firefox, not the download source.
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "the platform you came from" mistranslated as "the platform Firefox was downloaded from".
    - Current: `platformę, z której pobrano Firefoksa`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `platformę, z której trafiono do Firefoksa`
    - Per the developer comment, the platform is the source that directed the user to Firefox, not the download source.
- `onboarding_redesign_sync_body` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "tabs" was translated as "historii" (history) instead of "kart" (tabs).
    - Current: `Korzystaj z zakładek, historii i haseł na każdym urządzeniu.`
    - Source: `Get bookmarks, tabs, and passwords on any device. All protected with encryption.`
    - Suggest: `Korzystaj z zakładek, kart i haseł na każdym urządzeniu.`
    - Source says "bookmarks, tabs, and passwords"; "historii" means history, which is a different item.
- `preferences_enable_gecko_logs` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The translation drops "Enable", rendering the preference as just "Gecko logs".
    - Current: `Dzienniki Gecko`
    - Source: `Enable Gecko logs`
    - Suggest: `Włącz dzienniki Gecko`
    - Source is "Enable Gecko logs"; the verb "Enable" is missing in the Polish string, changing the meaning of the preference.
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The clarification "enabled above" and "while browsing" is dropped/altered.
    - Current: `Dostępne tylko wtedy, gdy wyszukiwarka Google jest włączona i w danej chwili aktywna.`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Dostępne tylko wtedy, gdy wyszukiwarka Google jest włączona powyżej i jest aktywną wyszukiwarką podczas przeglądania.`
    - Source specifies Google must be enabled in the setting above and be the active search engine while browsing; the Polish omits both qualifiers.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The phrase "with Mozilla’s marketing technology partners" is attached to "that you use it", making it read "that you use it with Mozilla's partners".
    - Current: `Podziel się informacją, skąd wiesz o Firefoksie i że go używasz z partnerami technologii marketingowych Mozilli.`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `Podziel się z partnerami technologii marketingowych Mozilli informacją, skąd wiesz o Firefoksie i że go używasz.`
    - In the source the sharing is done with Mozilla's marketing technology partners; the Polish word order makes it say the user uses Firefox together with those partners.
- `preferences_marketing_data_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Section title "Campaign measurement" is translated identically to "Campaign measurement data", adding "Dane".
    - Current: `Dane pomiarowe kampanii`
    - Source: `Campaign measurement`
    - Suggest: `Pomiary kampanii`
    - The source distinguishes the section title "Campaign measurement" from the switch label "Campaign measurement data"; the Polish collapses both into the same string.
- `preferences_privacy_report` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Privacy report" is rendered as "Inne funkcje" ("Other features"), which is unrelated to the source.
    - Current: `Inne funkcje`
    - Source: `Privacy report`
    - Suggest: `Raport prywatności`
    - The source is the category header "Privacy report"; the Polish says "Other features", a completely different meaning.
- `preferences_privacy_report_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Enable privacy report" is translated as "Informacja o prywatności" ("Privacy information"), dropping the enable action and mistranslating "report".
    - Current: `Informacja o prywatności`
    - Source: `Enable privacy report`
    - Suggest: `Włączenie raportu prywatności`
    - The developer comment says this is the title of a preference to enable/disable the privacy report feature; the target neither mentions enabling nor the report.
- `protection_panel_etp_toggle_enabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "try turning it off" refers to tracking protection, but the Polish "spróbuj ją wyłączyć" grammatically refers to the site (witryna).
    - Current: `Jeśli coś na tej witrynie nie działa, spróbuj ją wyłączyć.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Jeśli coś na tej witrynie nie działa, spróbuj wyłączyć ochronę.`
    - The pronoun "ją" agrees with "witryna" (the site), suggesting the user turn off the site rather than the tracking protection toggle described in the developer comment.
- `recently_closed_tab` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Singular string "%d tab" rendered with plural noun "Karty: %d", identical to the plural string.
    - Current: `Karty: %d`
    - Source: `%d tab`
    - Suggest: `Karta: %d`
    - The developer comment marks this as the one-tab case; the plural form is used for recently_closed_tabs.
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The example URL domain was changed from google.com to google.pl, altering the source example.
    - Current: `https://www.google.pl/search?q=%s`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `https://www.google.com/search?q=%s`
    - The source example URL is https://www.google.com/search?q=%s; the example URL should not be localized to a different domain, especially as the parallel suggestion-string example keeps google.com.
- `search_settings_google_lens_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Toggle title drops "Enable".
    - Current: `Wyszukiwanie w Google Lens`
    - Source: `Enable Google Lens search`
    - Suggest: `Włącz wyszukiwanie w Google Lens`
    - Source "Enable Google Lens search" includes the action "Enable", omitted in Polish.
- `search_suggestions_delete_history_item_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Adds "witrynę" (website), but the placeholder may be a search term, not a site.
    - Current: `Usunięto witrynę %1$s z historii`
    - Source: `Deleted %1$s from history`
    - Suggest: `Usunięto %1$s z historii`
    - The comment says %1$s is either a shortened URL or the actual deleted search term, so calling it a website is wrong in half the cases.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Search settings" (verb, i.e. search through settings) is rendered as "Ustawienia wyszukiwania" (search settings as a noun phrase), the wrong meaning.
    - Current: `Ustawienia wyszukiwania`
    - Source: `Search settings`
    - Suggest: `Przeszukaj ustawienia`
    - The developer comment explicitly states "Search" is a verb here — the screen lets users search through settings, not configure search. The current text duplicates search_settings_menu_item ("Ustawienia wyszukiwania").
- `sync_offline` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Offline" is rendered as "Rozłączono" ("Disconnected"), a status of a different meaning.
    - Current: `Rozłączono`
    - Source: `Offline`
    - Suggest: `Offline`
    - The source states the sync service is offline/unreachable; "Rozłączono" says the user was disconnected, which is a different state. Polish Mozilla products use "Offline"/"Tryb offline".
- `tab_group_color_purple` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Purple" is translated as "Purpurowy" instead of "Fioletowy".
    - Current: `Purpurowy`
    - Source: `Purple`
    - Suggest: `Fioletowy`
    - Polish "purpurowy" denotes a crimson/dark red hue; the standard equivalent of English "purple" is "fioletowy". Colour labels are used for accessibility, so naming the wrong colour is misleading.
- `tab_manager_multiselect_menu_item_bookmark_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Bookmark selected tabs" is rendered as "add bookmarks to the selected tabs", reversing the relationship.
    - Current: `Dodaj zakładki do zaznaczonych kart`
    - Source: `Bookmark selected tabs`
    - Suggest: `Dodaj zaznaczone karty do zakładek`
    - The source means to create bookmarks for the selected tabs; the Polish says to add bookmarks to the tabs, which is not the intended action.
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Dismiss" (dismiss the banner) is translated as "Zamknij", which in the tab-tray context reads as "Close (tabs)" and collides with the close-tabs terminology.
    - Current: `Zamknij`
    - Source: `Dismiss`
    - Suggest: `Odrzuć`
    - The button dismisses the Close Tabs Banner; "Zamknij" is the translation used elsewhere in this batch for "Close" and is ambiguous with closing tabs, misrepresenting the negative action.
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The translation says the Terms of Use come "from the Firefox browser" instead of "a Firefox Terms of Use" being newly introduced.
    - Current: `Wprowadziliśmy %2$s z przeglądarki %1$s`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `Wprowadziliśmy %2$s przeglądarki %1$s`
    - Source: "We’ve introduced a %1$s %2$s" — %1$s modifies the Terms of Use (Firefox Terms of Use); "z przeglądarki" (from the browser) changes the meaning.
- `ungroup_tab_group_confirmation_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — The source says the tabs will remain open; the Polish rephrases it as a negation of closing, changing the statement.
    - Current: `Karty na tym urządzeniu nie zostaną zamknięte, ale grupa zostanie usunięta.`
    - Source: `The tabs will remain open on this device, but the group will be deleted.`
    - Suggest: `Karty pozostaną otwarte na tym urządzeniu, ale grupa zostanie usunięta.`
    - en-US: "The tabs will remain open on this device" — an affirmative statement about tabs remaining open, not a negative statement about closing.
- _…and 6 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_prompt_repost_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — Ungrammatical clause: infinitives "wysłać"/"opublikować" do not agree with the sentence structure and the meaning is garbled.
    - Current: `może spowodować powtórzenie ostatnich działań, na przykład jeszcze raz wysłać płatność lub opublikować komentarz dwa razy`
    - Source: `Refreshing this page could duplicate recent actions, such as sending a payment or posting a comment twice.`
    - Suggest: `może spowodować powtórzenie ostatnich działań, na przykład ponowne wysłanie płatności lub opublikowanie komentarza dwa razy`
    - The source says refreshing could duplicate recent actions, such as sending a payment or posting a comment twice; the Polish mixes a noun phrase with bare infinitives, producing a broken sentence.
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — Wrong case after "jako" and added word "konta" not in source.
    - Current: `Używaj konta %1$s jako dostawcę logowania`
    - Source: `Use %1$s as a login provider`
    - Suggest: `Używaj %1$s jako dostawcy logowania`
    - Source is "Use %1$s as a login provider" (the provider itself, not an account); Polish "jako" here requires the nominative/genitive agreement "jako dostawcy logowania".
- `mozac_feature_prompts_mar` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pl/strings.xml` — Polish abbreviation for March is "mar" instead of the standard "mar."/"marz" — inconsistent with other months.
    - Current: `mar`
    - Source: `Mar`
    - Suggest: `mar.`
    - The standard Polish short form for marzec is "mar."; "mar" is not a recognized abbreviation.
- `mozac_lib_crash_dialog_checkbox` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-pl/strings.xml` — Wrong case: "Zgłoś awarię organizacji %1$s" reads as reporting the crash of the organization instead of to the organization.
    - Current: `Zgłoś awarię organizacji %1$s`
    - Source: `Send crash report to %1$s`
    - Suggest: `Zgłoś awarię organizacji %1$s (np. „Wyślij zgłoszenie awarii do organizacji %1$s”)`
    - Source is "Send crash report to %1$s"; the genitive "organizacji %1$s" attaches to "awarię", losing the "to Mozilla" recipient meaning.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-pl/strings.xml` — "Zgłaszanie awarii organizacji %1$s" implies reporting the organization's crash rather than sending the report to the organization.
    - Current: `Zgłaszanie awarii organizacji %1$s`
    - Source: `Sending crash report to %1$s`
    - Suggest: `Wysyłanie zgłoszenia awarii do organizacji %1$s`
    - Source is "Sending crash report to %1$s"; the recipient (dative/do + genitive) is required, otherwise the genitive attaches to "awarii".
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Singular "Item Menu" rendered as plural "Menu elementów" instead of "Menu elementu".
    - Current: `Menu elementów „%s”`
    - Source: `Item Menu for %s`
    - Suggest: `Menu elementu „%s”`
    - The source refers to the overflow menu of a single bookmark or folder item (%s is one item's name), so the genitive singular "elementu" is required.
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Wrong case after "uniemożliwia ... " — verb should be in infinitive complement with genitive noun, current "używania" is ungrammatical.
    - Current: `Uniemożliwia złośliwym skryptom używania Twojego urządzenia`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `Uniemożliwia złośliwym skryptom używanie Twojego urządzenia`
    - "Uniemożliwia komuś coś" requires the accusative/nominative verbal noun "używanie", not genitive "używania".
- `felt_privacy_info_card_subtitle_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Missing comma before the subordinate clause in "Kto może zobaczyć co robię?".
    - Current: `Kto może zobaczyć co robię?`
    - Source: `Who might be able to see my activity?`
    - Suggest: `Kto może zobaczyć, co robię?`
    - Polish punctuation requires a comma before the subordinate clause introduced by "co".
- `nova_onboarding_sync_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Idiom misspelled: "w mgnieniu okna" instead of "w mgnieniu oka".
    - Current: `w mgnieniu okna`
    - Source: `Grab bookmarks, passwords, and more on any device in a snap. Your personal data stays safe and secure with encryption.`
    - Suggest: `w mgnieniu oka`
    - The Polish idiom for "in a snap" is "w mgnieniu oka"; "okna" (of the window) is a typo producing nonsense.
- `onboarding_preferences_dialog_usage_data_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Case agreement error: "sposobu" should be "sposobie" to match the locative series after "o".
    - Current: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobu korzystania z Firefoksa`
    - Source: `Data about your device, hardware configuration, and how you use Firefox helps improve features, performance, and stability for everyone.`
    - Suggest: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobie korzystania z Firefoksa`
    - The enumeration after the preposition "o" requires the locative case (urządzeniu, konfiguracji, sposobie), not the genitive "sposobu".
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Missing comma closing the relative clause before the predicate.
    - Current: `Karty, których nie odwiedzono od dwóch tygodni są przenoszone`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `Karty, których nie odwiedzono od dwóch tygodni, są przenoszone`
    - Polish punctuation requires the subordinate clause to be closed with a comma before "są przenoszone".
- `qr_scanner_confirmation_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Ungrammatical verb complement: "Zezwól aplikacji ... otworzyć" should use the noun phrase "na otwarcie".
    - Current: `Zezwól aplikacji %1$s otworzyć %2$s`
    - Source: `Allow %1$s to open %2$s`
    - Suggest: `Zezwól aplikacji %1$s na otwarcie %2$s`
    - In Polish, "zezwolić" requires "na + accusative" (na otwarcie), not a bare infinitive.
- `uninstall_survey_option_2_v2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Past tense "didn’t work" rendered as present tense.
    - Current: `Strony nie działają poprawnie`
    - Source: `Websites didn’t work properly`
    - Suggest: `Strony nie działały poprawnie`
    - en-US uses the past tense "Websites didn’t work properly"; the Polish uses present tense.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Past tense "didn’t work" rendered as present tense.
    - Current: `Filmy, pobieranie lub multimedia nie działają`
    - Source: `Videos, downloads, or media didn’t work`
    - Suggest: `Filmy, pobieranie lub multimedia nie działały`
    - en-US uses the past tense "Videos, downloads, or media didn’t work"; the Polish uses present tense.
- `wallpapers_onboarding_dialog_title_text` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Wrong case after "Wypróbuj": should be genitive singular "odrobinę koloru" (accusative) rather than plural/genitive "odrobiny".
    - Current: `Wypróbuj odrobiny koloru`
    - Source: `Try a splash of color`
    - Suggest: `Wypróbuj odrobinę koloru`
    - "Wypróbuj" takes the accusative: "odrobinę koloru". "odrobiny" is ungrammatical here.
- `webcompat_reporter_problem_description_placeholder_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — "Co powinno się było stać?" is an awkward/incorrect rendering of "What did you expect to happen?".
    - Current: `Co powinno się było stać?`
    - Source: `What happened? What did you expect to happen? Please provide steps to reproduce the issue.`
    - Suggest: `Czego oczekiwano? / Co powinno się stać?`
    - The source asks what the user expected; the Polish double past construction "powinno się było stać" is grammatically clumsy and shifts meaning.

### D. Terminology, register & consistency

- `ai_controls_block_ai_title` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — AI is rendered inconsistently as "SI" here but as "sztuczna inteligencja" in neighbouring strings on the same screen.
    - Current: `Blokuj ulepszenia SI`
    - Source: `Block AI enhancements`
    - Suggest: `Blokuj ulepszenia sztucznej inteligencji`
    - ai_controls_ai_powered_features and ai_controls_block_dialog_body use "sztuczna inteligencja" while these toggles use the abbreviation "SI", creating inconsistent terminology on the same settings surface.
- `review_prompt_rate_header` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Literal, unidiomatic rendering of "Thanks for loving Firefox... spread the love".
    - Current: `Dziękujemy za pokochanie przeglądarki %1$s. Masz sekundę, aby podzielić się miłością, wystawiając ocenę?`
    - Source: `Thanks for loving %1$s. Got a second to spread the love with a rating?`
    - Suggest: `Cieszymy się, że lubisz przeglądarkę %1$s. Masz chwilę, aby wystawić ocenę i podzielić się swoją opinią?`
    - "Dziękujemy za pokochanie" is not grammatical/idiomatic Polish; the source is a friendly thank-you for liking the app, not a thank-you for an act of "loving".
- `setup_checklist_subtitle_6_steps_fifth_step` — `mozilla-mobile/fenix/app/src/main/res/values-pl/strings.xml` — Informal register uses capitalized "Cię" inconsistently with other strings addressing the user.
    - Current: `Od mety dzieli Cię tylko jeden krok.`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Od mety dzieli cię tylko jeden krok.`
    - The locale uses the informal register; capitalized honorific "Cię" belongs to the formal/polite style used elsewhere in Mozilla pl.

### E. Typography, punctuation & spacing

- `mozac_feature_pwa_copy_success` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-pl/strings.xml` — The final period of the source sentence is missing in the translation.
    - Current: `Skopiowano adres`
    - Source: `URL copied.`
    - Suggest: `Skopiowano adres.`
    - Source "URL copied." ends with a period; the toast text drops it.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
