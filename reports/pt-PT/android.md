# Android l10n QA — pt-PT

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7ee8e61a4a7d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7ee8e61a4a7d` |
| **Previous run** | 2026-10-18 @ `dd8ca757b7dd` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,552 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-PT: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,552 |
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
| Typography deviations from this locale's own norm | 3 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 3 | **curly-double** |
| apostrophe | `typographic` 1 | **typographic** |
| ellipsis | `char` 19 | **char** |
| dash | `em` 1, `en` 1 | _mixed_ |
| nbsp | `total` 7 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (74)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The hedged "might… be risky" becomes the certain "é perigoso" (is dangerous).
    - Current: `e é perigoso para o seu dispositivo`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `e ser arriscado para o seu dispositivo`
    - The source says changing the file type might be risky. The translation says it is dangerous, so the product now makes a stronger warning than the source does.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 24 |
| 3 | Degraded language (grammar, spelling, terminology) | 40 |
| 4 | Cosmetic (typography, spacing) | 10 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — “Device” is translated as “computador” (computer) in a mobile app.
    - Current: `Verifique a ligação do computador à rede`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Verifique a ligação do dispositivo à rede`
    - The source says “the device’s network connection” and “Is your device or network protected”. This is an Android app, so “computador” is wrong. The same error appears in “O seu computador ou rede estão protegidos”, which should be “O seu dispositivo ou rede estão protegidos”.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — "device" is rendered as "computador" (computer) on a mobile error page.
    - Current: `O computador está ligado a uma rede ativa?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `O dispositivo está ligado a uma rede ativa?`
    - The source says "Is the device connected…". This is an Android app, and other strings on the same surface use "dispositivo".
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — "your device" is rendered as "do seu computador".
    - Current: `e não do seu computador`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `e não do seu dispositivo`
    - The source says "not your device". This is an Android app, so "computador" is wrong.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — "device" is rendered as "computador" (computer).
    - Current: `O computador está ligado a uma rede ativa?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `O dispositivo está ligado a uma rede ativa?`
    - The source says "Is the device connected to an active network?". On a mobile browser "computador" is wrong and inconsistent with "dispositivo" used elsewhere.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — "manage themes" is rendered as the noun "gestão de temas", so the sentence says the extension monitors theme management rather than manages themes.
    - Current: `e gestão de temas`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `e gerir temas`
    - The source has two separate abilities: monitor extension usage, and manage themes. Using the noun "gestão" makes it the object of "Monitorizar", so the permission changes from managing themes to monitoring theme management. The version without the period correctly says "gerir temas".
- `mozac_feature_downloads_cancel_active_private_downloads_warning_content_body` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-pt-rPT/strings.xml` — The singular source (one download) is translated as plural, which doesn't work with a file-name placeholder.
    - Current: `%1$s transferências serão canceladas`
    - Source: `If you close all Private tabs now, %1$s download will be canceled. Are you sure you want to leave Private Browsing?`
    - Suggest: `a transferência de %1$s será cancelada`
    - The source says '%1$s download will be canceled' (singular), and the developer comment says %1$s is the file name. The translation says '%1$s transferências serão canceladas' (plural), which then reads as '[file name] downloads will be cancelled'.
- `likes_cookies` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-pt-rPT/strings.xml` — The cookie emojis were replaced with unrelated emojis (wave and boxing glove).
    - Current: `🌊 gosta de cookies 🥊`
    - Source: `🍪 likes cookies 🍪`
    - Suggest: `🍪 gosta de cookies 🍪`
    - The source puts 🍪 at both ends to illustrate cookies; 🌊 and 🥊 change the displayed content and make no sense here.
- `addresses_county` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "County" is translated as "País" (country) instead of "Condado".
    - Current: `País`
    - Source: `County`
    - Suggest: `Condado`
    - The source and the developer comment refer to a county, an administrative division below the region level. "País" means country, and it also duplicates the label of the addresses_country_only field.
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Townland", an Irish rural land division, is translated as "Cidade" (city).
    - Current: `Cidade`
    - Source: `Townland`
    - Suggest: `Townland`
    - The developer comment says a townland is a land division used in rural Ireland, not a city. "Cidade" is wrong and also duplicates the addresses_city label.
- `alternative_app_icon_option_cool` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — 'Cool' is translated as 'Simpático' (friendly/nice), not the stylish, modern sense the comment describes.
    - Current: `Simpático`
    - Source: `Cool`
    - Suggest: `Fixe`
    - The developer comment says the icon is a sleek, modern twist that looks fresh and stylish. 'Simpático' describes a person's friendliness and does not carry that meaning.
- `alternative_app_icon_option_momo_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The artist's handle is wrong: "@heyheymoshots" instead of "@heyheymomodraws".
    - Current: `@heyheymoshots`
    - Source: `Created by @heyheymomodraws`
    - Suggest: `@heyheymomodraws`
    - The source and the developer comment both name the artist as @heyheymomodraws. The translation credits a different handle, so the icon is attributed to the wrong account.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Item de Menu" means "menu item", reversing the source's "item menu" (the overflow menu of a bookmark item).
    - Current: `Item de Menu para %s`
    - Source: `Item Menu for %s`
    - Suggest: `Menu do item %s`
    - The developer comment says this describes the overflow menu for a bookmark item. The pt-PT text reads as "menu item for %s", so screen-reader users hear the wrong control described.
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The hedged "might… be risky" becomes the certain "é perigoso" (is dangerous).
    - Current: `e é perigoso para o seu dispositivo`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `e ser arriscado para o seu dispositivo`
    - The source says changing the file type might be risky. The translation says it is dangerous, so the product now makes a stronger warning than the source does.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — In this heading, "Debug" describes the locales, but the translation uses it as a verb ("Debug languages to activate").
    - Current: `Depurar idiomas para ativar`
    - Source: `Debug locales to enable`
    - Suggest: `Idiomas de depuração a ativar`
    - The developer comment says this heading sits above a list of debug locales that can be turned on and off. So "debug" describes the locales; it is not an instruction. "Depurar idiomas" tells the user to debug the languages.
- `email_masks_error_retrieving_masks` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "aren’t available right now" rendered as "not yet available", turning a temporary error into a not-yet-launched feature.
    - Current: `ainda não estão disponíveis`
    - Source: `Email masks aren’t available right now. Try again in a few minutes.`
    - Suggest: `não estão disponíveis neste momento`
    - The source and comment describe a temporary service error; "ainda não" means "not yet".
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The product name "Firefox Suggest" was translated as "Sugestões Firefox".
    - Current: `Sugestões Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - Firefox Suggest is a Mozilla product name, and Mozilla's convention is to keep it in English. Here it is used as the header that labels this source of suggestions.
- `preference_bottom_toolbar` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Bottom" toolbar position is translated as "Fim" (end), which doesn't match the sibling tab-strip string "Fundo".
    - Current: `Fim`
    - Source: `Bottom`
    - Suggest: `Fundo`
    - The source means the bottom position on screen. "Fim" means end or finish. The bottom tab-strip setting on the same screen uses "Fundo", so the two are inconsistent.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "DNS resolver" is translated as "tradutor de DNS" (DNS translator).
    - Current: `tradutor de DNS`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `resolvedor de DNS`
    - A DNS resolver resolves names. "Tradutor" means translator, which is the wrong technical term.
- `preferences_customize_extension_collection` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The adjective "personalizadas" agrees with "extensões", so the Portuguese means a collection of customised extensions instead of a custom collection.
    - Current: `Coleção de extensões personalizadas`
    - Source: `Custom extension collection`
    - Suggest: `Coleção personalizada de extensões`
    - The source "Custom extension collection" means a custom AMO collection the user configures. The extensions themselves are not customised. The feminine plural agreement in pt-PT attaches "custom" to the extensions.
- `search_bar_with_lens_widget_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The translation says "com imagem" (with an image) instead of naming image search as one of the widget's search types.
    - Current: `Barra de pesquisa com imagem, pesquisa privada e pesquisa por voz`
    - Source: `Search bar with image, private and voice search`
    - Suggest: `Barra de pesquisa com pesquisa por imagem, privada e por voz`
    - The source and developer comment describe buttons for image search, private search and voice search. "com imagem" reads as a search bar that contains a picture, not one that offers image search.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The title says 'search settings' as a noun (settings about search), but the source uses 'Search' as a verb.
    - Current: `Definições de pesquisa`
    - Source: `Search settings`
    - Suggest: `Pesquisar definições`
    - The developer comment says 'Search' is a verb here, because this screen is for searching through the settings. 'Definições de pesquisa' reads as the settings for the search engine, which is a different screen.
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Synced Tabs Open" (tabs that are open) is rendered as the imperative "Abrir" ("Open synced tabs").
    - Current: `Abrir separadores sincronizados:`
    - Source: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Separadores sincronizados abertos:`
    - The source is a counter label for open synced tabs, like the normal and private versions, which use "… abertos". "Abrir" turns it into a command.
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The sentence is garbled: it says we introduced Firefox "to the Terms of Use" rather than introducing Firefox Terms of Use.
    - Current: `Introduzimos o %1$s, aos %2$s e atualizámos a nossa %3$s.`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `Introduzimos os %2$s do %1$s e atualizámos a nossa %3$s.`
    - The source means "We've introduced Firefox Terms of Use and updated our Privacy Notice". The translation's "o %1$s, aos %2$s" makes no sense and gets the object wrong.
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Translating" (in-progress state) is rendered as the noun "Tradução" ("Translation"), losing the progressive meaning.
    - Current: `Tradução`
    - Source: `Translating`
    - Suggest: `A traduzir`
    - The developer comment says this inactive button text indicates a translation is currently in progress; pt-PT expresses that with "A traduzir", whereas "Tradução" is just the noun.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — The English possessive “’s” was left in the Portuguese sentence, which makes it ungrammatical.
    - Current: `no Internet Archive’s %2$s`
    - Source: `%1$s can look for an earlier version of this page from the Internet Archive’s %2$s.`
    - Suggest: `na %2$s do Internet Archive`
    - Portuguese has no “’s” possessive. The archive service (%2$s) belongs to the Internet Archive, so it should read “na %2$s do Internet Archive”.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — "cookies" takes feminine agreement here but masculine ("os cookies") later in the same string.
    - Current: `cookies que são necessárias`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `cookies que são necessários`
    - The same string later uses "os cookies do site" (masculine), so the agreement in "necessárias" is wrong and inconsistent.
- `mozac_feature_addons_installed_dialog_description_3` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — The preposition "no" (masculine singular) does not agree with the substituted link text "definições da extensão" (feminine plural).
    - Current: `no %1$s`
    - Source: `Update permissions and data preferences any time in the %1$s.`
    - Suggest: `nas %1$s`
    - Per the developer comment, %1$s is replaced by the link text from mozac_feature_addons_installed_dialog_description_link_text, which is "definições da extensão". So the user sees "no definições da extensão", which is ungrammatical. It should be "nas definições da extensão".
- `mozac_feature_addons_permissions_downloads_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — A stray "e," makes the sentence ungrammatical.
    - Current: `Transferir ficheiros e, ler e modificar`
    - Source: `Download files and read and modify the browser’s download history.`
    - Suggest: `Transferir ficheiros, ler e modificar`
    - "e, ler e modificar" has an extra conjunction and comma, which breaks the sentence. The install version of this string has the correct form: "Transferir ficheiros, ler e modificar…".
- `mozac_feature_addons_permissions_extra_domains_description_plural_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — This uses "em outros" without the contraction, unlike the install version and the related sites strings, which all use "noutros".
    - Current: `em outros domínios`
    - Source: `Access your data on other domains.`
    - Suggest: `noutros domínios`
    - European Portuguese normally contracts "em outros" to "noutros". The install version of this string and both sites strings already say "noutros".
- `mozac_feature_addons_status_incompatible` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — The possessive is missing its definite article, which is a Brazilian construction and not correct pt-PT.
    - Current: `com sua versão`
    - Source: `%1$s is not compatible with your version of %2$s (version %3$s).`
    - Suggest: `com a sua versão`
    - In European Portuguese a possessive takes the definite article ("a sua versão"). Other strings in this batch already do this, for example "a sua versão e definições atuais".
- `mozac_feature_prompts_manage_logins_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rPT/strings.xml` — Incorrect plural of the compound noun "palavra-passe".
    - Current: `palavras-passes`
    - Source: `Manage passwords`
    - Suggest: `palavras-passe`
    - The plural of "palavra-passe" is "palavras-passe" (only the first element is pluralised), as used correctly elsewhere in this batch ("Palavras-passe guardadas").
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rPT/strings.xml` — The service name is placed before the noun in English order, which leaves the Portuguese sentence ungrammatical.
    - Current: `Novo! %s máscaras de e-mail estão agora disponíveis`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `Novo! As máscaras de e-mail do %s estão agora disponíveis`
    - %s is "Firefox Relay". The text then reads "Firefox Relay máscaras de e-mail estão…", which copies English word order. Portuguese needs an article and a possessive construction ("As máscaras de e-mail do Firefox Relay").
- `addresses_oblast` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Oblasto" is not a Portuguese word; the loanword "Oblast" is used unchanged.
    - Current: `Oblasto`
    - Source: `Oblast`
    - Suggest: `Oblast`
    - Portuguese uses the term "oblast" without adaptation for Russian and Ukrainian administrative divisions. "Oblasto" is an invented form.
- `alternative_app_icon_option_gradient_midnight` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — 'Meia-noite' is spelled with a hyphen in pt-PT.
    - Current: `Meia noite`
    - Source: `Midnight`
    - Suggest: `Meia-noite`
    - The compound noun for 'midnight' is always written 'meia-noite'. 'Meia noite' is a spelling error.
- `browser_menu_add_to_homescreen` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Inicial" has a stray capital letter in the middle of the phrase, unlike the sibling string "ecrã inicial".
    - Current: `ecrã Inicial`
    - Source: `Add to Home screen`
    - Suggest: `ecrã inicial`
    - Portuguese doesn't capitalise a common noun phrase in the middle of a sentence. The sibling string browser_menu_add_app_to_homescreen uses "ecrã inicial" in lowercase, so this capital looks like an English carry-over from "Home screen".
- `close_tabs_after_one_month_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The preposition "de" is missing after "depois".
    - Current: `Fechar depois um mês`
    - Source: `Close after one month`
    - Suggest: `Fechar depois de um mês`
    - Correct Portuguese is "depois de". The sibling strings (one day, one week) all use "depois de".
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Uses the Brazilian construction "Tem certeza que" instead of European Portuguese "Tem a certeza de que".
    - Current: `Tem certeza que deseja`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `Tem a certeza de que deseja`
    - European Portuguese needs the article and preposition: "ter a certeza de que". "Tem certeza que" is Brazilian usage.
- `confirm_clear_permissions_on_all_sites` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Uses the Brazilian construction "Tem certeza que" instead of European Portuguese "Tem a certeza de que".
    - Current: `Tem certeza que deseja`
    - Source: `Are you sure that you want to clear all the permissions on all sites?`
    - Suggest: `Tem a certeza de que deseja`
    - European Portuguese needs the article and preposition: "ter a certeza de que". "Tem certeza que" is Brazilian usage.
- `confirm_clear_permissions_site` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Uses the Brazilian construction "Tem certeza que" instead of European Portuguese "Tem a certeza de que".
    - Current: `Tem certeza que deseja`
    - Source: `Are you sure that you want to clear all the permissions for this site?`
    - Suggest: `Tem a certeza de que deseja`
    - European Portuguese needs the article and preposition: "ter a certeza de que". "Tem certeza que" is Brazilian usage.
- `expanded_tab_group_header_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The group name comes before the noun, so the sentence reads ungrammatically in Portuguese.
    - Current: `%1$s grupo de separadores`
    - Source: `{$quantity ->} [one] %1$s tab group with %2$d tab, color %3$s [other] %1$s tab group with %2$d tabs, color %3$s`
    - Suggest: `Grupo de separadores %1$s`
    - %1$s is the group name. Placing it before "grupo de separadores" gives readings like "Trabalho grupo de separadores", which is not grammatical Portuguese. The name should follow the noun. The same fix applies to both plural variants.
- `history_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The singular/plural marker is malformed: the plural form gets an extra "(s)", producing "selecionados(s)".
    - Current: `selecionados(s)`
    - Source: `%1$d selected`
    - Suggest: `selecionado(s)`
    - The usual Portuguese way to cover one or many is "selecionado(s)". "selecionados(s)" is a spelling error.
- `inactive_tabs_auto_close_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The preposition "a" is missing: in this sense "aceder" takes "a", so it should read "separadores a que não acedeu".
    - Current: `separadores que não acedeu`
    - Source: `Firefox can close tabs you haven’t viewed over the past month.`
    - Suggest: `separadores a que não acedeu`
    - When "aceder" means accessing something, it takes the preposition "a" ("aceder a algo"). Without it, the relative clause is ungrammatical in pt-PT.
- `ip_protection_mozilla_vpn_upsell_body` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Missing preposition before "até 5 dispositivos", so the sentence says to protect apps "up to 5 devices" rather than "on up to 5 devices".
    - Current: `proteja todas as suas aplicações até 5 dispositivos`
    - Source: `Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `proteja todas as suas aplicações em até 5 dispositivos`
    - Source says "on up to 5 devices"; without "em" the Portuguese is ungrammatical and the meaning is unclear.
- `nimbus_notification_default_browser_text` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Ungrammatical construction "Torne o Firefox no seu navegador predefinido".
    - Current: `Torne o Firefox no seu navegador predefinido`
    - Source: `Make Firefox your default browser`
    - Suggest: `Torne o Firefox o seu navegador predefinido`
    - "Tornar X Y" (make X your default) takes a direct predicative in Portuguese. "Torne … no seu navegador" is not correct standard pt-PT.
- `onboarding_term_of_service_line_two_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The masculine "no nosso" does not agree with the feminine link text "Informação de privacidade" that replaces %1$s.
    - Current: `Saiba mais no nosso %1$s.`
    - Source: `Firefox cares about your privacy. Learn more in our %1$s.`
    - Suggest: `Saiba mais na nossa %1$s.`
    - %1$s is replaced by onboarding_term_of_service_line_two_link_text, "Informação de privacidade", which is feminine. The parallel string onboarding_redesign_tou_body_two correctly uses "na nossa".
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The phrase is missing the preposition that "aceder" requires, so the relative clause is ungrammatical.
    - Current: `qual o site que está prestes a aceder`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `qual o site a que está prestes a aceder`
    - In pt-PT, "aceder" takes the preposition "a" ("aceder a um site"), so the relative clause has to be "a que". Without it the clause is a grammar error.
- `preferences_marketing_data_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The preposition "sobre" is misspelled as "sobres".
    - Current: `Saber mais sobres`
    - Source: `Learn more about marketing data`
    - Suggest: `Saber mais sobre`
    - The correct preposition is "sobre". "Sobres" is wrong here.
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Site" is singular where the plural is needed.
    - Current: `em site ao utilizar`
    - Source: `Fill and save usernames and passwords in websites while using %1$s.`
    - Suggest: `em sites ao utilizar`
    - The source says "in websites" (plural), and in Portuguese the bare singular "em site" is ungrammatical here.
- `tab_group_color_grey` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Cinza" is the Brazilian colour name; European Portuguese uses "Cinzento".
    - Current: `Cinza`
    - Source: `Grey`
    - Suggest: `Cinzento`
    - In European Portuguese the adjective/colour name for grey is "cinzento"; "cinza" as a colour label is a Brazilian usage, out of place in a pt-PT locale.
- `tab_tray_inactive_onboarding_message` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The relative clause is missing the preposition that "aceder" requires.
    - Current: `Os separadores que não acede`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `Os separadores aos quais não acede`
    - "Aceder" takes the preposition "a", so standard pt-PT needs "aos quais" (or "a que") here.
- `terms_of_use_prompt_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Despender" takes a direct object, so the "de" in "despenda de um momento" is wrong.
    - Current: `despenda de um momento`
    - Source: `Please take a moment to review and accept. %1$s.`
    - Suggest: `despenda um momento`
    - The correct construction is "despender um momento". The "de" looks like a mix-up with "dispor de".
- `uninstall_survey_option_3_v2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The relative clause leaves out the preposition that "precisar" requires.
    - Current: `Funcionalidades em falta que preciso`
    - Source: `Missing features I need`
    - Suggest: `Funcionalidades em falta de que preciso`
    - In standard pt-PT the verb "precisar" takes "de", so the relative clause must be "de que preciso".
- `wallpaper_artist_series_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Artist series" names one wallpaper collection but is translated as a plural.
    - Current: `Séries de artista`
    - Source: `Artist series`
    - Suggest: `Série de artista`
    - The developer comment says "Artist series" is one collection of artist wallpapers. The English "series" is singular here, so the plural "Séries" is wrong.

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rPT/strings.xml` — "developer tools" is translated as "ferramentas de programação" here but as "ferramentas de programador" in the install version of the same permission.
    - Current: `ferramentas de programação`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `ferramentas de programador`
    - The same source term should be translated the same way in both versions of this permission description. The install version uses "ferramentas de programador".
- `certificate_warning_homepage_card_hcr1_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Imperative uses informal 'tu' form (Atualiza) instead of the formal 'você' form used throughout the locale.
    - Current: `Atualiza antes`
    - Source: `Update before March 14`
    - Suggest: `Atualize antes`
    - pt-PT strings address the user with the formal imperative (e.g. 'Atualize o seu Firefox', 'Experimente', 'Abane o seu dispositivo'); 'Atualiza' breaks this register.
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Somente HTTPS" is Brazilian Portuguese; the pt-PT name for the mode is "Apenas HTTPS".
    - Current: `modo Somente HTTPS`
    - Source: `However, it’s also possible that an attacker is involved. If you continue to the website, you should not enter any sensitive info. If you continue, HTTPS-Only mode will be turned off temporarily for the site.`
    - Suggest: `modo Apenas HTTPS`
    - "Somente" is a pt-BR form; pt-PT Firefox calls the mode "Apenas HTTPS".
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Uses "rastreadores" for trackers, while the surrounding tracking-protection strings use "monitorização" terms.
    - Current: `rastreadores (como redes de anúncios)`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `elementos de monitorização (como redes de anúncios)`
    - Inconsistent with the "monitorização" terminology used elsewhere on the same ETP surface.
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Uses "rastreamento" for tracking, while the surrounding tracking-protection strings use "monitorização".
    - Current: `sites de rastreamento conhecidos`
    - Source: `Clears cookies set by redirects to known tracking websites.`
    - Suggest: `sites de monitorização conhecidos`
    - Inconsistent with the established pt-PT term "monitorização" used in the other strings on this screen.
- `ip_protection_mozilla_vpn_upsell_button` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Product name "Mozilla VPN" is rendered as "a VPN da Mozilla", which doesn't match the headline on the same card.
    - Current: `Obtenha a VPN da Mozilla`
    - Source: `Get Mozilla VPN`
    - Suggest: `Obtenha a Mozilla VPN`
    - Mozilla VPN is a standalone product name (per the comment), and the headline on the same card keeps "a Mozilla VPN"; the button should keep the brand name too.
- `ip_protection_toolbar_pill_label_off` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — The off-state pill label uses "desligada" while its on-state counterpart uses "ativada" and the matching accessibility text uses "desativada".
    - Current: `VPN desligada`
    - Source: `VPN off`
    - Suggest: `VPN desativada`
    - The two toolbar pill labels (VPN on / VPN off) are shown in the same place and should form a consistent pair; "ativada" pairs with "desativada", as already used in ip_protection_toolbar_pill_description_off.
- `microsurvey_close_handle_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Survey" is rendered as "inquérito" here, while every other microsurvey string uses "questionário".
    - Current: `Fechar inquérito`
    - Source: `Close survey`
    - Suggest: `Fechar questionário`
    - The same microsurvey surface uses "questionário" in the header, completion, icon and Nimbus survey strings. This screen-reader label should use the same term.
- `opening_screen_homepage_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Homepage" is rendered as "página principal", while the sibling strings in this group use "página inicial".
    - Current: `Abrir na página principal`
    - Source: `Open on homepage`
    - Suggest: `Abrir na página inicial`
    - On the same settings surface, opening_screen_homepage and opening_screen_after_four_hours_of_inactivity(_summary) translate Homepage as "página inicial".
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Battery Saver" is rendered as the generic "gestão da bateria" (battery management) instead of the name of the Android feature.
    - Current: `gestão da bateria`
    - Source: `Set by Battery Saver`
    - Suggest: `poupança de bateria`
    - The source names the specific Android Battery Saver mode, which pt-PT Android calls "Poupança de bateria". "Gestão da bateria" describes something else.
- `preference_doh_default_protection_info_1` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "você" breaks the formal pt-PT register, which addresses the user without a pronoun.
    - Current: `que você selecionar`
    - Source: `Use the provider you select`
    - Suggest: `que selecionar`
    - pt-PT UI text avoids "você" and uses the third person without a pronoun, as the other strings in this batch do ("Ative", "Toque", "Aceda").
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — "Exclui" is the Brazilian Portuguese verb for delete; pt-PT uses "Elimina".
    - Current: `Exclui automaticamente`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `Elimina automaticamente`
    - In pt-PT, "excluir" means to exclude or leave something out, not to delete. pt-PT uses "eliminar" for deleting data.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — Extra spaces were added inside the <em> element, so a stray space shows before the full stop.
    - Current: `{ <em> } %1$s { </em> }.`
    - Source: `You’ve enabled HTTPS-Only Mode for enhanced security, and a HTTPS version of { <em> }%1$s{ </em> } is not available.`
    - Suggest: `{ <em> }%1$s{ </em> }.`
    - The source has no spaces around %1$s inside <em>. The added space before </em> shows up as “example.com .” on the page.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }O navegador está a operar no modo desligado e não consegue estabelecer ligação ao objeto solicitado.{ </p> } { <ul> } { <li> }O computador está ligado a uma rede ativa?{ </li> } { <li> }Pressione "Tentar novament…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — The quotes around the button name are straight, not the locale's curly double quotes.
    - Current: `"Tentar novamente"`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `“Tentar novamente”`
    - pt-PT uses curly double quotes, and the source uses curly quotes too.
- `mozac_feature_prompts_jan` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rPT/strings.xml` — January abbreviation is lowercase while the other months on the same month chooser are capitalised.
    - Current: `jan`
    - Source: `Jan`
    - Suggest: `Jan`
    - Other month abbreviations on the same dialog are rendered "Mai", "Set", "Out"; "jan" is inconsistent on the same surface.
- `mozac_support_ktx_menu_call_with` — `mozilla-mobile/android-components/components/support/ktx/src/main/res/values-pt-rPT/strings.xml` — There is a stray space before the ellipsis.
    - Current: `Chamar com …`
    - Source: `Call with…`
    - Suggest: `Chamar com…`
    - The source and the sibling strings ("Enviar e-mail com…", "Partilhar com…") attach the ellipsis directly to the word.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `O endereço web deve conter "https://" ou "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — This string uses straight double quotes, but the locale convention (and the source) uses curly double quotes.
    - Current: `"https://" ou "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” ou “http://”`
    - The locale convention is curly double quotes, and the en-US source also uses “ ”.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Exclui automaticamente os dados de navegação quando seleciona "Sair" no menu principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — Straight double quotes are used where the locale convention and the source use curly quotes.
    - Current: `"Sair"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Sair”`
    - The pt-PT convention is curly double quotes, and the source also uses curly quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pt-PT/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
