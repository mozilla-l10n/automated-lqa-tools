# Android l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **Previous run** | 2026-08-21 @ `d368c9040c12` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ru: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Typography deviations from this locale's own norm | 2 |

### Completeness

**3 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — 3

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 46, `straight-double` 2 | **guillemet** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 7 | **em** |
| register | `informal` 150, `formal` 491 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (169)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 100 |
| 3 | Degraded language (grammar, spelling, terminology) | 65 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_content_crashed_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "Content crashed" is translated as "content is corrupted", duplicating the corrupted-content title and losing the crash meaning.
    - Current: `Загружаемое содержимое повреждено`
    - Source: `Content crashed`
    - Suggest: `Сбой содержимого`
    - The source says the content process crashed, not that the content is corrupted; the same Russian text is also used for mozac_browser_errorpages_corrupted_content_title, making the two error pages indistinguishable.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "the requested item" is rendered as "сайтом" (site) instead of the generic requested resource.
    - Current: `не может установить соединение с запрашиваемым сайтом`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `не может установить соединение с запрашиваемым ресурсом`
    - The source says "the requested item", a generic resource, not specifically a website.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "network administrator" is translated as "системному администратору" (system administrator).
    - Current: `Обратитесь к своему системному администратору или Интернет-провайдеру`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `Обратитесь к своему сетевому администратору или Интернет-провайдеру`
    - The source says "network administrator", not "system administrator".
- `mozac_browser_errorpages_security_bad_cert_back` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "(Recommended)" is translated as "(желательно)" (desirable) instead of "(рекомендуется)".
    - Current: `Назад (желательно)`
    - Source: `Go Back (Recommended)`
    - Suggest: `Назад (рекомендуется)`
    - The source qualifier is "Recommended", the standard Mozilla rendering of which is "рекомендуется"; "желательно" weakens/changes the meaning.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "self-signed" certificate is rendered as "подписан самим сайтом" (signed by the site itself) — inaccurate technical term.
    - Current: `сертификат подписан самим сайтом`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `сертификат является самоподписанным`
    - "Self-signed certificate" is a standard term (самоподписанный сертификат); the current wording changes the technical meaning.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — "network administrator" is translated as "системному администратору" (system administrator).
    - Current: `Обратитесь к своему системному администратору или Интернет-провайдеру`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Обратитесь к своему сетевому администратору или Интернет-провайдеру`
    - The source says "network administrator", not "system administrator".
- `mozac_browser_errorpages_unknown_socket_type_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ru/strings.xml` — Title mistranslates "Unexpected response" and leaves an untranslated alternative slash-variant in the UI.
    - Current: `Неизвестный/неопознанный ответ сервера`
    - Source: `Unexpected response from server`
    - Suggest: `Неожиданный ответ сервера`
    - Source is "Unexpected response from server"; the target says "unknown/unidentified" and additionally exposes two unresolved translation variants separated by a slash in a page heading.
- `mozac_feature_addons_failed_to_load_extensions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "Try again later" is expanded into "Подождите некоторое время и попробуйте снова", adding content not in the source.
    - Current: `Не удалось загрузить расширения. Подождите некоторое время и попробуйте снова.`
    - Source: `Couldn’t load extensions. Try again later.`
    - Suggest: `Не удалось загрузить расширения. Попробуйте позже.`
    - The source simply says "Try again later"; the translation adds an instruction to wait.
- `mozac_feature_addons_not_yet_supported_caption2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "building support for an initial selection of Recommended Extensions" is mistranslated as building a "selection system".
    - Current: `В данное время мы подготавливаем первоначальную систему выбора предлагаемых расширений.`
    - Source: `We‘re currently building support for an initial selection of Recommended Extensions.`
    - Suggest: `В настоящее время мы работаем над поддержкой первоначальной подборки рекомендуемых расширений.`
    - The source says support is being built for an initial selection of Recommended Extensions, not that a "selection system" is being prepared.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Meaning shifted: source says extend developer tools so they can access your data, not "extend the access of developer tools".
    - Current: `Расширение доступа инструментов разработчика к вашим данным в открытых вкладках`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `Расширение инструментов разработчика для доступа к вашим данным в открытых вкладках`
    - "Extend developer tools to access your data" means extending the devtools themselves; the translation reverses the object of extension.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Meaning shifted: source says extend developer tools so they can access your data, not "extend the access of developer tools".
    - Current: `Расширение доступа инструментов разработчика к вашим данным в открытых вкладках.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Расширение инструментов разработчика для доступа к вашим данным в открытых вкладках.`
    - "Extend developer tools to access your data" means extending the devtools themselves; the translation reverses the object of extension.
- `mozac_feature_customtabs_menu_button` — `mozilla-mobile/android-components/components/feature/customtabs/src/main/res/values-ru/strings.xml` — "More options" is rendered as "Другие настройки" ("Other settings"), naming settings rather than options of the menu button.
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Дополнительные опции`
    - The content description describes the menu button; the source says "More options", not "settings". Elsewhere in Firefox this is "Дополнительные опции"/"Ещё".
- `mozac_feature_relay_chip_text` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ru/strings.xml` — Singular "email mask" rendered as plural and as an imperative sentence in a chip label.
    - Current: `Используйте псевдонимы эл. почты`
    - Source: `Use email mask`
    - Suggest: `Использовать псевдоним эл. почты`
    - The source is a chip action label "Use email mask" (singular); the translation pluralizes it and uses a suggestive imperative instead of an action label.
- `mozac_feature_qr_scanner` — `mozilla-mobile/android-components/components/feature/qr/src/main/res/values-ru/strings.xml` — "QR scanner" is rendered as "barcode reader", naming a different technology.
    - Current: `Считыватель штрих-кодов`
    - Source: `QR scanner`
    - Suggest: `Сканер QR-кодов`
    - The source says QR scanner; штрих-код is a barcode, not a QR code.
- `mozac_feature_sitepermissions_media_key_system_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ru/strings.xml` — "DRM-controlled content" is rendered as "защищённое авторским правом содержимое" (copyright-protected), losing the DRM term.
    - Current: `Разрешить %1$s воспроизводить защищённое авторским правом содержимое?`
    - Source: `Allow %1$s to play DRM-controlled content?`
    - Suggest: `Разрешить %1$s воспроизводить содержимое, защищённое DRM?`
    - The source specifies content controlled by DRM, not merely copyrighted content; DRM is a technical term that should be kept.
- `mozac_summarize_settings_shake_to_summarize` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ru/strings.xml` — Toggle label translated as an imperative command instead of a feature name.
    - Current: `Встряхните, чтобы резюмировать`
    - Source: `Shake to summarize`
    - Suggest: `Встряхивание для резюмирования`
    - This is the label of a settings toggle naming the feature ("Shake to summarize"), not an instruction to the user; the imperative reads as a command and is inconsistent with the neighbouring noun-style labels.
- `mozac_lib_crash_dialog_checkbox` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ru/strings.xml` — Singular one-time action "Send crash report" rendered as an imperfective plural "Отправлять сообщения о падениях".
    - Current: `Отправлять сообщения о падениях в %1$s`
    - Source: `Send crash report to %1$s`
    - Suggest: `Отправить сообщение о падении в %1$s`
    - The source is a one-off checkbox "Send crash report to %1$s" (singular, perfective), not a recurring setting to send reports repeatedly.
- `mozac_lib_crash_share` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ru/strings.xml` — "Share" is translated as "Сообщить" (Report) instead of "Поделиться".
    - Current: `Сообщить`
    - Source: `Share`
    - Suggest: `Поделиться`
    - The source is "Share" — a link that opens an app chooser to share the crash report; "Сообщить" means "Report" and duplicates mozac_lib_crash_notification_action_report.
- `a11y_selected_locale_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Selected language" is rendered as "Current language".
    - Current: `Текущий язык`
    - Source: `Selected language`
    - Suggest: `Выбранный язык`
    - The content description marks the tick on the selected language; "Текущий" means "current", not "selected".
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — The English conjunction "or" was left untranslated and the typographic quotes were replaced with straight double quotes.
    - Current: `Сетевой адрес должен содержать "https://" or "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `Сетевой адрес должен содержать «https://» или «http://»`
    - The source reads “https://” or “http://”; the Russian keeps the English word "or" and uses straight quotes instead of the locale's guillemets.
- `add_tab` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Add tab" is translated as "Open tab", inconsistent with add_private_tab which uses "Добавить".
    - Current: `Открыть вкладку`
    - Source: `Add tab`
    - Suggest: `Добавить вкладку`
    - Source is "Add tab"; the sibling string add_private_tab is correctly rendered "Добавить приватную вкладку".
- `add_to_homescreen_continue` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Continue to website" is translated as "Return to the site".
    - Current: `Вернуться к сайту`
    - Source: `Continue to website`
    - Suggest: `Перейти на сайт`
    - The source means continuing on to the website, not returning to it.
- `addresses_name` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Name" here is a person's full name, but the translation means "title/designation".
    - Current: `Название`
    - Source: `Name`
    - Suggest: `Имя`
    - The developer comment states Name represents a person's full name (e.g. John Joe Doe); "Название" refers to the name of a thing, not a person.
- `addresses_province` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Province" is rendered as the generic "Регион", identical to the State label, losing the distinction.
    - Current: `Регион`
    - Source: `Province`
    - Suggest: `Провинция`
    - The source distinguishes Province from State (addresses_state), and "Регион" also duplicates the wording used for "Country or region"; Province should be "Провинция".
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Townland" (an Irish rural land division) is rendered as "Городская земля" ("urban/town land"), which means the opposite.
    - Current: `Городская земля`
    - Source: `Townland`
    - Suggest: `Таунленд`
    - The developer comment states the Townland field is specific to Ireland and denotes a land division used in rural areas; "Городская земля" says "city land", the wrong concept.
- `ai_controls_voice_search_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — The service name is mistyped as "Google Speech Service" instead of the source's "Google Speech Services".
    - Current: `службами Google Speech Service`
    - Source: `Audio is converted to text by Google Speech Services.`
    - Suggest: `службами Google Speech Services`
    - The source names the product "Google Speech Services"; product names must be reproduced exactly.
- `automatic_translation_option_always_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "translate this language" (i.e. translate pages in this language) is rendered as "translate into this language", reversing the translation direction.
    - Current: `%1$s будет переводить на этот язык автоматически при загрузке страницы.`
    - Source: `%1$s will translate this language automatically when the page loads.`
    - Suggest: `%1$s будет автоматически переводить страницы на этом языке при их загрузке.`
    - The source means Firefox will translate content written in this language; the Russian says it will translate into this language, the opposite direction, and is inconsistent with the sibling strings that use «сайтов на этом языке».
- `bookmark_empty_list_guest_cta` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Sign in to sync" is translated as "Войти в синхронизацию", which is not the intended meaning.
    - Current: `Войти в синхронизацию`
    - Source: `Sign in to sync`
    - Suggest: `Войдите для синхронизации`
    - The button navigates to sync authentication: the user signs in so that syncing can happen; "войти в синхронизацию" (log in to synchronization) is a nonsensical rendering in Russian.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Item Menu for %s" is rendered as "Элемент меню" (menu item), reversing the meaning.
    - Current: `Элемент меню для %s`
    - Source: `Item Menu for %s`
    - Suggest: `Меню элемента «%s»`
    - The source means the overflow menu belonging to an item (a bookmark or folder); the translation says "menu item", which is the opposite relationship and misleads screen-reader users.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "sheet" (bottom sheet) is mistranslated as "страницу" (page), producing a confusing screen-reader description.
    - Current: `Закрыть страницу меню пользовательских вкладок`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Закрыть панель меню пользовательской вкладки`
    - The source refers to closing the bottom-sheet of the custom tab menu, not a "page"; the developer comment says it is a bottom sheet handlebar.
- `browser_menu_default_banner_dismiss_promotion` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Dismiss promotion" is rendered as "Скрыть рекламу" (hide advertisement), which misstates the banner as an ad.
    - Current: `Скрыть рекламу`
    - Source: `Dismiss promotion`
    - Suggest: `Закрыть предложение`
    - The banner promotes making the app default; "реклама" (advertisement) is not what the source means by "promotion".
- `browser_menu_summarize_page_badge` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "New" (a badge marking a new feature) is translated as "Создать" ("Create").
    - Current: `Создать`
    - Source: `New`
    - Suggest: `Новое`
    - The source is a badge label meaning "new feature", not the verb "create"; "Создать" says something entirely different.
- `browser_toolbar_summarize_cfr_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Translation adds "просмотреть и" and rewords, saying "view and retell this page" instead of "summarize this page in seconds".
    - Current: `чтобы просмотреть и пересказать эту страницу, займёт всего несколько секунд`
    - Source: `Shake your device to summarize this page in seconds. ⚡️`
    - Suggest: `чтобы за несколько секунд получить краткое содержание этой страницы`
    - The source only says "summarize this page in seconds"; the added "просмотреть" (view) is not in the source and the clause structure is broken.
- `content_description_menu` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "More options" is rendered as "Другие настройки" (other settings), which names the wrong concept for the three-dot menu.
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Дополнительные опции`
    - The source is "More options" for the three-dot menu; "настройки" means settings, not options/menu items.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Debug locales" is translated as "Языки отладки" (debug languages) instead of locales.
    - Current: `Языки отладки для включения`
    - Source: `Debug locales to enable`
    - Suggest: `Локали отладки для включения`
    - The source refers to locales (used elsewhere in this batch as "локаль": debug_drawer_add_new_address uses "для выбранной локали"), not languages.
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "home and current region values" is mistranslated as "значения дома и текущего региона" (values of the home and the current region).
    - Current: `значения дома и текущего региона`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `значения домашнего и текущего региона`
    - "home" modifies "region" (домашний регион, as translated in debug_drawer_home_region_label), not a separate noun meaning "house".
- `edit_tab_group_bottom_sheet_grabber_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "New group" is rendered as an imperative "Создать группу" instead of the noun phrase.
    - Current: `Создать группу, свернуть маркер перетаскивания`
    - Source: `New group, collapse drag handle`
    - Suggest: `Новая группа, свернуть маркер перетаскивания`
    - The source "New group" is a label naming the sheet, not an action command; the Russian turns it into "Create a group".
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Button label translated as an imperative addressed to the user ("Try restarting…") rather than the action label; wording implies advice instead of a button action.
    - Current: `Попробуйте перезапустить расширения`
    - Source: `Try restarting extensions`
    - Suggest: `Попробовать перезапустить расширения`
    - It is a button the user presses; Russian button labels use the infinitive. "Попробуйте" reads as an instruction, inconsistent with other buttons like "Перезапустить", "Продолжить с отключенными расширениями".
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Placeholders reordered so the app name reads as a count of closed tabs.
    - Current: `Закрыто %1$s вкладок: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s: закрыто вкладок: %2$d`
    - %1$s is the app name and %2$d the number of tabs; the Russian reads "Closed <app name> tabs: N", turning the app name into a quantity modifier and producing a nonsensical phrase.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Shortcuts" (home screen site tiles) is mistranslated as "горячие клавиши" (keyboard shortcuts).
    - Current: `Показать все горячие клавиши`
    - Source: `Show all shortcuts`
    - Suggest: `Показать все ярлыки`
    - The developer comment says this button shows all the shortcuts in the home screen shortcuts section; related strings translate "shortcut" as "ярлык" (homepage_shortcuts_add_shortcut = "Добавить ярлык"). "Горячие клавиши" means keyboard shortcuts, a different thing.
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Resets to X GB" rendered with the wrong preposition, changing the meaning.
    - Current: `Сбрасывается на %1$.0f ГБ`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `Сбрасывается до %1$.0f ГБ`
    - The source means the allowance is reset back to the full X GB; "на X ГБ" reads as "by X GB", a different meaning.
- `ip_protection_mozilla_vpn_upsell_body` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "up to 5 devices" is rendered as "on 5 devices", dropping "up to".
    - Current: `на 5 устройствах`
    - Source: `Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `не более чем на 5 устройствах`
    - The source says "up to 5 devices"; the translation states a fixed 5 devices, changing the meaning.
- `likert_scale_option_features_hard_to_find_or_missing` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — The translation turns the sentence "Features are hard to find or missing" into a noun phrase "Features that are hard to find or absent".
    - Current: `Возможности, которые трудно найти или отсутствуют`
    - Source: `Features are hard to find or missing`
    - Suggest: `Функции трудно найти, или они отсутствуют`
    - Source is a full statement (features are hard to find or missing); the Russian relative-clause noun phrase changes the meaning and is ungrammatical as a coordinated clause.
- `link_sharing_toggle_body` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Invite your friends to try..." is rendered as "Invite your friends in order to try...", changing who tries the browsing.
    - Current: `Пригласите своих друзей, чтобы попробовать`
    - Source: `Invite your friends to try faster, safer browsing with %1$s every time you share a link on WhatsApp.`
    - Suggest: `Предложите своим друзьям попробовать`
    - In the source the friends are the ones trying faster, safer browsing; the Russian «чтобы попробовать» attaches the trying to the reader.
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "No site exceptions" is rendered as "No exceptions for this site", changing the meaning.
    - Current: `Нет исключений для этого сайта`
    - Source: `No site exceptions`
    - Suggest: `Нет исключений для сайтов`
    - The source is a label shown when the site-exceptions list is empty; it means there are no site exceptions at all, not that a particular site has none.
- `onboarding_firefox_account_sync_is_on` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Sync is on" is rendered as "Sync has started", changing the meaning from a state to an event.
    - Current: `Началась синхронизация`
    - Source: `Sync is on`
    - Suggest: `Синхронизация включена`
    - The source states that sync is enabled (a state after sign-in), not that a sync run has begun.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "past explorations" (browsing history entries) rendered as "поиски" (searches).
    - Current: `Показать все прошлые поиски`
    - Source: `Show all past explorations`
    - Suggest: `Показать все прошлые посещения`
    - The comment says the button navigates the user to their history; "поиски" means searches, not past browsing/explorations.
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Leave private tabs" translated as "Покинуть приватные вкладки", which is not idiomatic and loses the sense of exiting private browsing.
    - Current: `Покинуть приватные вкладки`
    - Source: `Leave private tabs`
    - Suggest: `Выйти из приватных вкладок`
    - The comment states this is the action to exit private browsing mode; "покинуть вкладки" does not convey exiting.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "your default DNS resolver" is mistranslated as "разрешение DNS по умолчанию" (the act of resolving) instead of the resolver service.
    - Current: `Использовать разрешение DNS по умолчанию`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `Использовать ваш DNS-преобразователь по умолчанию`
    - The source refers to the DNS resolver (a server/service), not to "DNS resolution"; "разрешение" also reads as "permission" here, which is misleading.
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "DNS resolver" is rendered as "разрешение DNS" (DNS resolution) instead of the DNS resolver service.
    - Current: `Использовать разрешение DNS по умолчанию только в том случае, если есть проблема с безопасным DNS`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `Использовать DNS-резолвер по умолчанию только в том случае, если есть проблема с безопасным DNS`
    - The source refers to "your default DNS resolver" — a server/service, not the act of resolving; "разрешение DNS" mistranslates the noun.
- `preference_doh_off_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "DNS resolver" mistranslated as "разрешение DNS" (DNS resolution).
    - Current: `Использовать разрешение DNS по умолчанию`
    - Source: `Use your default DNS resolver`
    - Suggest: `Использовать DNS-резолвер по умолчанию`
    - The source "Use your default DNS resolver" refers to a resolver service, not to resolution as a process.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Tell websites not to share & sell data" is rendered as a hard prohibition rather than a request/signal to websites.
    - Current: `Запретить веб-сайтам делиться и продавать данные`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `Просить веб-сайты не передавать и не продавать данные`
    - The source asks (tells) sites not to share or sell data — a signal, not an enforced block; also "делиться и продавать" reverses the negation, saying to share and sell.
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — The contrastive "but" is dropped and "Stronger" is rendered as "Строгая", duplicating the mode name.
    - Current: `Строгая защита от отслеживания с увеличенной производительностью, некоторые сайты могут работать неправильно.`
    - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
    - Suggest: `Более сильная защита от отслеживания и более высокая производительность, но некоторые сайты могут работать неправильно.`
    - The source contrasts the benefits with the drawback using "but"; the translation loses this and mistranslates "Stronger".
- `preference_gestures_dynamic_toolbar` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Scroll to hide toolbar" is translated as an imperative one-time action instead of the setting description.
    - Current: `Прокрутить для скрытия панели инструментов`
    - Source: `Scroll to hide toolbar`
    - Suggest: `Прокрутка для скрытия панели инструментов`
    - The preference describes a gesture setting; the perfective imperative "Прокрутить" misreads the source and is inconsistent with other gesture preferences.
- `preference_option_phone_feature_allowed` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — State label "Allowed" translated as the action "Разрешить" (to allow).
    - Current: `Разрешить`
    - Source: `Allowed`
    - Suggest: `Разрешено`
    - The developer comment says this label indicates a permission state (allowed), not an action.
- `preference_option_phone_feature_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — State label "Blocked" translated as the action "Блокировать" (to block).
    - Current: `Блокировать`
    - Source: `Blocked`
    - Suggest: `Заблокировано`
    - The developer comment says this label indicates a permission state (blocked), not an action.
- `preference_phone_feature_media_key_system_access` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "DRM-controlled content" rendered as "copyright-protected content", losing the DRM term.
    - Current: `Защищённое авторским правом содержимое`
    - Source: `DRM-controlled content`
    - Suggest: `Содержимое, защищённое DRM`
    - The source and developer comment refer to DRM/EME-controlled content, not copyright protection generally.
- `preferences_category_delete_or_remove_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Delete or remove downloads" is rendered as "Удаление или уничтожение загрузки", using "уничтожение" (destruction) and a singular noun.
    - Current: `Удаление или уничтожение загрузки`
    - Source: `Delete or remove downloads`
    - Suggest: `Удаление или удаление загрузок с устройства`
    - The source distinguishes deleting the download record from removing the file; "уничтожение" (destruction) is not the meaning, and "загрузки" singular contradicts the plural "downloads".
- `preferences_downloads_default_location_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Default download location" is rendered as "Адрес для загрузок" (address) instead of a folder/save location.
    - Current: `Адрес для загрузок по умолчанию`
    - Source: `Default download location`
    - Suggest: `Папка для загрузок по умолчанию`
    - The preference sets the default folder on the device where downloads are saved; "адрес" suggests a URL, which is the wrong content.
- `preferences_remote_improvements` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Remote improvements" is rendered as "Удалённые улучшения", which reads as "deleted improvements".
    - Current: `Удалённые улучшения`
    - Source: `Remote improvements`
    - Suggest: `Дистанционные улучшения`
    - "Удалённые" is ambiguous and most naturally reads as "deleted/removed" here (unlike "Удалённая отладка" where the context disambiguates), so it conveys the wrong meaning of "remote".
- _…and 45 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_addons_permissions_declarative_net_request_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Accusative "Блокировку" used where the nominative list item form is required.
    - Current: `Блокировку содержимого на любой странице`
    - Source: `Block content on any page`
    - Suggest: `Блокировка содержимого на любой странице`
    - All other permission descriptions in this list use the nominative noun (e.g. the _for_update variant uses "Блокировка"); the accusative case is ungrammatical as a standalone list entry.
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "разработчиком расширений" is plural where the source refers to the single extension's developer.
    - Current: `с разработчиком расширений`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `с разработчиком расширения`
    - Source is "extension developer" (singular, the developer of this extension), matching the websiteContent string which uses "разработчику расширения".
- `mozac_feature_addons_permissions_extra_domains_description_plural_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Wrong case ending: "вашим данных" instead of "вашим данным".
    - Current: `Доступ к вашим данных на других доменах`
    - Source: `Access your data on other domains`
    - Suggest: `Доступ к вашим данным на других доменах`
    - Dative plural after "к" requires "данным"; "данных" is genitive and does not agree with "вашим".
- `mozac_feature_addons_permissions_extra_sites_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Wrong case ending: "вашим данных" instead of "вашим данным".
    - Current: `Доступ к вашим данных на других сайтах.`
    - Source: `Access your data on other sites.`
    - Suggest: `Доступ к вашим данным на других сайтах.`
    - Dative plural after "к" requires "данным"; the parallel string mozac_feature_addons_permissions_extra_sites_description_2 uses the correct form.
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Mixed verb forms: "Скачайте и запускайте" is imperative while the rest of the permission descriptions use nominal/infinitive form, and the two verbs disagree in aspect.
    - Current: `Скачайте и запускайте ИИ-модели на вашем устройстве`
    - Source: `Download and run AI models on your device`
    - Suggest: `Скачивание и запуск ИИ-моделей на вашем устройстве`
    - Source "Download and run AI models on your device" is a permission description, rendered elsewhere in this file with nominal forms ("Скрытие и отображение…", "Предоставление услуг…"); the current text is an imperative with inconsistent aspect.
- `mozac_feature_addons_permissions_trial_ml_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Imperative with mismatched aspect instead of the nominal permission-description form.
    - Current: `Скачайте и запускайте ИИ-модели на вашем устройстве.`
    - Source: `Download and run AI models on your device.`
    - Suggest: `Скачивание и запуск ИИ-моделей на вашем устройстве.`
    - Source "Download and run AI models on your device." is a permission description; other update descriptions in this file use nominal forms, and "Скачайте и запускайте" mixes perfective and imperfective imperatives.
- `mozac_feature_addons_unavailable_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "Ещё не доступно" should be written as one word "недоступно".
    - Current: `Ещё не доступно`
    - Source: `Not yet available`
    - Suggest: `Ещё недоступно`
    - In Russian the predicative adverb is spelled together as «недоступно» when there is no contrast/negation particle; «не доступно» here is a spelling error.
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ru/strings.xml` — Extraneous comma before "как" in "перед тем, как загружать" combined with dangling verb without object.
    - Current: `перед тем, как загружать на «%1$s»`
    - Source: `Make sure you trust this site before you upload from “%1$s”.`
    - Suggest: `перед тем как загружать файлы из папки «%1$s»`
    - The source means uploading from the folder "%1$s"; the Russian says uploading onto "%1$s", reversing the direction.
- `mozac_protections_dashboard_trackers_blocked_this_week_title` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-ru/strings.xml` — Header reads as a sentence "Trackers were blocked this week" instead of the noun phrase heading.
    - Current: `На этой неделе заблокированы трекеры`
    - Source: `Trackers blocked this week`
    - Suggest: `Заблокировано трекеров за эту неделю`
    - Source is a dashboard header noun phrase "Trackers blocked this week" that labels a count; the Russian predicate form changes it into a statement.
- `mozac_open_tab_counter_tab_tray` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-ru/strings.xml` — "не приватных" should be written as one word "неприватных".
    - Current: `Открытых не приватных вкладок`
    - Source: `Non-private Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Открытых неприватных вкладок`
    - In Russian, the negative prefix не- with an adjective without contrast is written together: «неприватных».
- `score` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-ru/strings.xml` — "Счет" is missing the ё (should be "Счёт"), inconsistent with «счётчика» elsewhere.
    - Current: `Счет: %1$d`
    - Source: `Score: %1$d`
    - Suggest: `Счёт: %1$d`
    - The word for score is «счёт»; the tree uses ё consistently (e.g. «счётчика вкладок», «включён»).
- `alternative_app_icon_option_purple_dark` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Missing "ё" in "Тёмно-фиолетовый", inconsistent with "Зелёный" in the same set.
    - Current: `Темно-фиолетовый`
    - Source: `Dark Purple`
    - Suggest: `Тёмно-фиолетовый`
    - The same batch uses ё ("Зелёный"), so the ё-spelling is the convention here.
- `bookmark_moved_single_item` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Snackbar message uses a neuter short participle with a name placeholder, producing incorrect agreement.
    - Current: `Перемещено %1$s в %2$s`
    - Source: `Moved %1$s to %2$s`
    - Suggest: `«%1$s» перемещено в «%2$s»`
    - The source "Moved %1$s to %2$s" places the item name as object; the Russian word order "Перемещено %1$s в %2$s" reads as broken grammar without quoting the item title.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Пин-код" is misspelled; Russian orthography requires "PIN-код" or "ПИН-код".
    - Current: `Пин-код`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `PIN-код`
    - The source "PIN" is an abbreviation; the mixed-case "Пин-код" is a spelling error in Russian.
- `debug_drawer_tab_tools_tab_count_inactive` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Genitive plural "Неактивных" is inconsistent with the nominative "Активные" used for the parallel category label.
    - Current: `Неактивных`
    - Source: `Inactive`
    - Suggest: `Неактивные`
    - The sibling strings are category labels; debug_drawer_tab_tools_tab_count_active uses nominative "Активные", so the same form is required here.
- `debug_drawer_tab_tools_tab_count_private` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Genitive plural "Приватных" is inconsistent with the nominative "Активные" used for the parallel category label.
    - Current: `Приватных`
    - Source: `Private`
    - Suggest: `Приватные`
    - Parallel tab-count category labels should share grammatical form; "Активные" is nominative plural.
- `download_empty_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Verb form error: "будут находится" should be "будут находиться" (infinitive).
    - Current: `Скачанные вами файлы будут находится здесь.`
    - Source: `Files you download will appear here.`
    - Suggest: `Скачанные вами файлы будут находиться здесь.`
    - After «будут» the infinitive «находиться» (with soft sign) is required; «находится» is 3rd person singular.
- `history_older` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Старее" is a non-standard comparative form used as a history group header.
    - Current: `Старее`
    - Source: `Older`
    - Suggest: `Ранее`
    - Source "Older" heads history entries older than the last month; "Старее" is colloquial/incorrect Russian for this heading.
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Plural adjective used for a singular option label "Recommended".
    - Current: `Рекомендуемые`
    - Source: `Recommended`
    - Suggest: `Рекомендуемое`
    - The label refers to a single recommended automatic location option; the plural form does not agree with the singular item it labels (cf. "Подключено к рекомендуемому местоположению").
- `ip_protection_recommended_location` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Plural form used for a single server-location option label.
    - Current: `Рекомендуемые`
    - Source: `Recommended`
    - Suggest: `Рекомендуемое`
    - Per the developer comment this labels one "Recommended" server location option; the plural adjective does not agree with the singular option (местоположение).
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "партнерам" is spelled without ё while the parallel string nova_onboarding_marketing_body_2 uses "партнёрам".
    - Current: `маркетинговым партнерам Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `маркетинговым партнёрам Mozilla`
    - Inconsistent with the identical sibling string (_2) which uses «партнёрам»; the ru tree uses ё here.
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "блокируем компании от отслеживания" is an ungrammatical calque of the English "block companies from".
    - Current: `автоматически блокируем компании от отслеживания ваших кликов`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `автоматически не даём компаниям отслеживать ваши клики`
    - Russian «блокировать кого-то от чего-то» is not a valid construction; the source means preventing companies from spying on your clicks.
- `onboarding_redesign_tou_body_one` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "соглашаетесь с" requires instrumental case but the link text is nominative "Условия использования Firefox".
    - Current: `Продолжая, вы соглашаетесь с %1$s.`
    - Source: `By continuing, you agree to the %1$s.`
    - Suggest: `Продолжая, вы принимаете %1$s.`
    - The associated link string onboarding_redesign_tou_body_one_link_text is in the nominative, producing an ungrammatical composed sentence "соглашаетесь с Условия использования Firefox".
- `onboarding_redesign_tou_body_two` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Possessive pronoun does not agree with the feminine link text "Уведомление о конфиденциальности" inserted at %1$s.
    - Current: `Узнайте больше в нашем %1$s.`
    - Source: `Firefox cares about your privacy. Learn more in our %1$s.`
    - Suggest: `Узнайте больше в нашем Уведомлении о конфиденциальности.`
    - The link text for this string is "Уведомление о конфиденциальности" in the nominative, so the composed sentence reads "в нашем Уведомление о конфиденциальности" — case/agreement mismatch.
- `setup_checklist_subtitle_3_steps_second_step` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Numeral–noun agreement error: "Выполнено 2 шага" is fine but the parallel structure is inconsistent; actual error is missing comma-free clause—see rationale.
    - Current: `Почти готово! Выполнено 2 шага, остался 1.`
    - Source: `Almost there! Two steps finished and 1 to go.`
    - Suggest: `Почти готово! Выполнено 2 шага, остался 1 шаг.`
    - "остался 1" without the noun is elliptical and reads awkwardly in Russian; the source "1 to go" refers to a remaining step.
- `shortcuts_update_error` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Imperative instruction rendered as infinitives instead of imperatives.
    - Current: `Удалить существующие ярлыки и попробовать снова.`
    - Source: `Failed to update the app icon. Remove existing shortcuts and try again.`
    - Suggest: `Удалите существующие ярлыки и попробуйте снова.`
    - The source "Remove existing shortcuts and try again." is an imperative directed at the user; the Russian infinitive form reads as a menu action, not an instruction, and clashes with the formal register used elsewhere (e.g. "Проверьте подключение… и повторите попытку").
- `sports_widget_group_a` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Group A uses the Cyrillic letter А while all other groups keep Latin letters, breaking consistency.
    - Current: `Группа А`
    - Source: `Group A`
    - Suggest: `Группа A`
    - Groups B–L are rendered with Latin letters; the mixed Cyrillic "А" is inconsistent and may sort/match incorrectly.
- `sports_widget_upcoming_match_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Upcoming:" announcing a single match is translated in the plural form "Предстоящие:".
    - Current: `Предстоящие: %1$s против %2$s`
    - Source: `Upcoming: %1$s versus %2$s, %3$s at %4$s`
    - Suggest: `Предстоящий матч: %1$s против %2$s`
    - This content description announces one upcoming match, so the plural/section-header form used for sports_widget_upcoming is grammatically wrong here.
- `studies_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "feature studies" is translated in the singular "исследование функций" instead of plural.
    - Current: `Разрешить исследование функций`
    - Source: `Allow feature studies`
    - Suggest: `Разрешить исследования функций`
    - The source is plural "studies", and the feature is consistently called "Исследования" elsewhere (studies_data_category).
- `tab_group_onboarding_item_dismiss_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Ungrammatical genitive chain "обучение группы вкладок" implies teaching the group, not onboarding about tab groups.
    - Current: `Скрыть обучение группы вкладок`
    - Source: `Dismiss tab group onboarding`
    - Suggest: `Скрыть обучение работе с группами вкладок`
    - The source is "Dismiss tab group onboarding": the onboarding is about tab groups, not belonging to a group; the current genitive reads as "training of the tab group".
- `tabs_header_normal_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Misspelling of "вкладок" as "вкладкок".
    - Current: `Обычных открытых вкладкок: %1$s.`
    - Source: `Normal Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Обычных открытых вкладок: %1$s.`
    - "вкладкок" is not a Russian word; the genitive plural of "вкладка" is "вкладок", as used in the sibling strings.
- `trackers_blocked_panel_num_cross_site_cookies` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Wrong genitive plural form of "кука" in the [other] variant.
    - Current: `%1$d межсайтовых отслеживающих куков`
    - Source: `{$quantity ->} [one] %1$d cross-site tracking cookie [other] %1$d cross-site tracking cookies`
    - Suggest: `%1$d межсайтовых отслеживающих кук`
    - "кука" is a feminine noun; its genitive plural is "кук", not "куков".
- `translation_option_bottom_sheet_switch_description` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Wrong preposition/case: "предложения на перевод" instead of "предложения перевода".
    - Current: `Переопределяет предложения на перевод`
    - Source: `Overrides offers to translate`
    - Suggest: `Переопределяет предложения перевода`
    - "Offers to translate" is rendered elsewhere as "предлагать перевод"; "предложения на перевод" is ungrammatical in Russian.
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — Placeholder for the app name is left ungoverned, producing "автодополнение Firefox Focus URL ваших любимых сайтов", which garbles the sentence.
    - Current: `Включить автодополнение %s URL ваших любимых сайтов.`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `Включите, чтобы %s автоматически дополнял URL ваших любимых сайтов.`
    - The source says "Enable to have %s autocomplete your favorite URLs"; the Russian juxtaposes the app name and "URL" without any grammatical link, unlike the parallel string preference_autocomplete_topsite_summary2 which uses "в %s".

### D. Terminology, register & consistency

- `mozac_browser_awesomebar_remove_suggestion` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-ru/strings.xml` — "suggestion" is rendered as «подсказку» in the adjacent string but as «предложение» here, an inconsistent and incorrect term for a search suggestion.
    - Current: `Удалить предложение`
    - Source: `Remove suggestion`
    - Suggest: `Удалить подсказку`
    - The sibling string mozac_browser_awesomebar_edit_suggestion translates "suggestion" as «подсказка»; «предложение» on the same surface is inconsistent and misleading (it reads as "offer/sentence").
- `mozac_feature_addons_failed_to_uninstall` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Inconsistent formatting compared with the parallel "Failed to …" strings, which use "Ошибка при … %1$s" without a colon.
    - Current: `Ошибка при удалении: %1$s`
    - Source: `Failed to uninstall %1$s`
    - Suggest: `Ошибка при удалении %1$s`
    - mozac_feature_addons_failed_to_remove uses "Ошибка при удалении %1$s" for the same pattern; the colon here is an inconsistent rendering of the same construction on the same surface.
- `mozac_feature_addons_permissions_declarative_net_request_feedback_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Renders "your browsing history" differently from the non-update variant of the same source string.
    - Current: `Чтение истории просмотра.`
    - Source: `Read your browsing history.`
    - Suggest: `Чтение истории браузера.`
    - mozac_feature_addons_permissions_declarative_net_request_feedback_description translates the identical source as "истории браузера"; the two variants must be consistent.
- `mozac_feature_addons_permissions_history_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Renders "browsing history" differently from the non-update variant of the same source string.
    - Current: `Доступ к истории просмотра.`
    - Source: `Access browsing history.`
    - Suggest: `Доступ к истории браузера.`
    - mozac_feature_addons_permissions_history_description translates the identical source as "истории браузера"; the two variants of the same permission must match.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Uses "Мониторинг" where the non-update variant of the same source uses "Отслеживание".
    - Current: `Мониторинг использования расширений и управление темами.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `Отслеживание использования расширений и управление темами.`
    - The identical source "Monitor extension usage and manage themes" is translated inconsistently between the two variants of the same permission.
- `mozac_feature_addons_permissions_native_messaging_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Inconsistent with the non-update variant and drops "other than this one" nuance.
    - Current: `Обмен сообщениями с другими приложениями.`
    - Source: `Exchange messages with apps other than this one.`
    - Suggest: `Обмен сообщениями с приложениями, помимо этого.`
    - The same source phrase "Exchange messages with apps other than this one" is rendered differently from mozac_feature_addons_permissions_native_messaging_description; the update variant loses the "other than this one" qualifier.
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Inconsistent rendering of the same source string compared with mozac_feature_addons_permissions_one_site_description ("на %1$s" vs "для %1$s").
    - Current: `Доступ к вашим данным для %1$s.`
    - Source: `Access your data for %1$s.`
    - Suggest: `Доступ к вашим данным на %1$s.`
    - The identical source "Access your data for %1$s" is translated two different ways in the same permission list surface.
- `mozac_feature_addons_permissions_privacy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "параметров приватности" is inconsistent with the non-update variant's "настроек приватности" for the same source term "privacy settings".
    - Current: `Чтение и изменение параметров приватности.`
    - Source: `Read and modify privacy settings.`
    - Suggest: `Чтение и изменение настроек приватности.`
    - Same permission, same source wording, translated with two different terms on the same surface.
- `mozac_feature_addons_permissions_proxy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Wording diverges from the non-update variant of the same "proxy" permission ("Контроль настроек прокси в браузере").
    - Current: `Управление настройками прокси браузера.`
    - Source: `Control browser proxy settings.`
    - Suggest: `Контроль настроек прокси в браузере.`
    - The identical source "Control browser proxy settings" is rendered two different ways for the same permission on the same surface.
- `mozac_feature_addons_permissions_top_sites_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — "Доступ к истории просмотра" differs from the non-update variant of the same permission, which uses "Доступ к истории браузера".
    - Current: `Доступ к истории просмотра.`
    - Source: `Access browsing history.`
    - Suggest: `Доступ к истории браузера.`
    - Same source string "Access browsing history" is rendered two different ways on the same permission surface (mozac_feature_addons_permissions_top_sites_description).
- `mozac_feature_addons_permissions_user_scripts_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ru/strings.xml` — Word order and phrasing diverge from the non-update variant of the same permission.
    - Current: `Разрешение на доступ непроверенным сторонним скриптам к вашим данным.`
    - Source: `Allow unverified third-party scripts to access your data.`
    - Suggest: `Разрешение непроверенным сторонним скриптам доступа к вашим данным.`
    - The same source "Allow unverified third-party scripts to access your data" is rendered differently, and the current split of "доступ … к вашим данным" around the dative phrase is awkward/ungrammatical.
- `mozac_feature_prompt_folder_upload_confirm_positive_button_text` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ru/strings.xml` — "Upload" is rendered as "Закачать", inconsistent with the dialog title/message which use "Загрузить".
    - Current: `Закачать`
    - Source: `Upload`
    - Suggest: `Загрузить`
    - The related strings mozac_feature_prompt_folder_upload_confirm_title ("Загрузить файлы?") and _message ("загружать") use "загрузить"; "Закачать" is colloquial and inconsistent on the same dialog.
- `mozac_feature_summarize_loading_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ru/strings.xml` — "Summarizing…" is translated with a first-person verb "Резюмирую…" instead of an impersonal progress label.
    - Current: `Резюмирую…`
    - Source: `Summarizing…`
    - Suggest: `Резюмирование…`
    - UI progress labels in ru use impersonal noun forms; the first-person singular verb makes the app speak as "I", which conflicts with the locale's register.
- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ru/strings.xml` — First-person "Не могу" breaks the impersonal/formal register used for app messages.
    - Current: `Не могу резюмировать прямо сейчас`
    - Source: `Can’t summarize right now`
    - Suggest: `Не удалось резюмировать прямо сейчас`
    - The English "Can’t summarize right now" is impersonal; the Russian rendering makes the app speak in the first person singular, which conflicts with the locale's formal, impersonal register.
- `collections_migration_homepage_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Collections" is translated as "Подборки" here, while all other collection strings in the same feature use "Сборники".
    - Current: `Подборки теперь группы`
    - Source: `Collections are now groups`
    - Suggest: `Сборники теперь группы`
    - Terminology inconsistency: collections_header and all create_collection_* strings render "Collection(s)" as "Сборник/Сборники".
- `customize_toggle_pocket_sponsored` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Sponsored stories" is rendered as "Статьи спонсоров" while the related "Stories" section uses "Истории", creating inconsistent terminology on the same screen.
    - Current: `Статьи спонсоров`
    - Source: `Sponsored stories`
    - Suggest: `Спонсируемые истории`
    - customize_toggle_pocket_3 translates "Stories" as "Истории" and customize_toggle_contile translates "Sponsored" as "Спонсируемые"; the same surface should use the same terms.
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — First-person "Не могу" is used where the source is an impersonal "Can't rename file".
    - Current: `Не могу переименовать файл`
    - Source: `Can’t rename file`
    - Suggest: `Не удалось переименовать файл`
    - The dialog title states that the file cannot be renamed; Russian UI convention (and the accompanying description string) uses an impersonal form, not the app speaking in first person.
- `ip_protection_get_started` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Button label translated as a noun phrase instead of a call to action.
    - Current: `Начало работы`
    - Source: `Get started`
    - Suggest: `Начать`
    - The developer comment says this is a button that starts the VPN authentication flow; "Начало работы" is a heading-style noun phrase, not a button action.
- `likert_scale_option_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Likert scale options mix impersonal ("Полностью удовлетворяет") and personal masculine forms ("Доволен"), which is inconsistent and gendered.
    - Current: `Доволен`
    - Source: `Satisfied`
    - Suggest: `Удовлетворяет`
    - Options 1 and 5 use the impersonal "удовлетворяет" form; options 2–4 switch to masculine adjectives, breaking consistency on the same surface and assuming the user's gender.
- `preference_doh_provider_custom_dialog_textfield` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Provider" is translated as "Провайдер" while the neighbouring DoH strings use "поставщик".
    - Current: `Провайдер`
    - Source: `Provider`
    - Suggest: `Поставщик`
    - Inconsistent terminology on the same surface: preference_doh_provider_custom_dialog_title and the protection summaries render "provider" as "поставщик".
- `preferences_privacy_report_title` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "Privacy report" is rendered inconsistently: "Отчёт о конфиденциальности" in the category header but "отчёт о приватности" in the title.
    - Current: `Включить отчёт о приватности`
    - Source: `Enable privacy report`
    - Suggest: `Включить отчёт о конфиденциальности`
    - The adjacent string preferences_privacy_report translates the same feature name "Privacy report" as "Отчёт о конфиденциальности"; the same feature on the same settings screen must use one term.
- `preferences_shake_to_summarize` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Preference title translated as an imperative instruction rather than a setting label.
    - Current: `Встряхните, чтобы резюмировать`
    - Source: `Shake to summarize`
    - Suggest: `Встряхнуть, чтобы резюмировать`
    - The source is a toggle preference title "Shake to summarize"; Russian preference titles use the infinitive, not a command addressed to the user.
- `preferences_show_recent_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Toggle preference title uses perfective imperative "Показать" instead of the imperfective used in the sibling toggles.
    - Current: `Показать недавние запросы`
    - Source: `Show recent searches`
    - Suggest: `Показывать недавние запросы`
    - Neighbouring switch preferences use "Показывать" (Show voice search, Show trending suggestions); "Показать" implies a one-off action rather than a persistent setting.
- `tab_tray_add_new_collection` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — "collection" is translated as "сборник" here while the sibling string uses "подборка".
    - Current: `Создать новый сборник`
    - Source: `Add new collection`
    - Suggest: `Создать новую подборку`
    - tab_manager_multiselect_menu_item_add_to_collection renders "collection" as "подборка"; using "сборник" on the same surface is inconsistent terminology.
- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Navigate forward" translated as bare "Вперёд", inconsistent with "Перейти назад" used for the paired back button.
    - Current: `Вперёд`
    - Source: `Navigate forward`
    - Suggest: `Перейти вперёд`
    - The paired string content_description_back uses "Перейти назад" for "Navigate back"; the forward counterpart drops the verb, breaking consistency on the same surface.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "top sites" translated as colloquial "топ сайтов" instead of the established term.
    - Current: `Для топа сайтов`
    - Source: `For top sites`
    - Suggest: `Для топ сайтов`
    - "Top sites" is a UI feature name; "топа сайтов" is colloquial and inconsistent with the term used elsewhere (top site strings).

### E. Typography, punctuation & spacing

- `mozac_feature_downloads_third_party_app_chooser_dialog_title` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ru/strings.xml` — Missing comma before the adverbial participle «используя».
    - Current: `Завершить действие используя`
    - Source: `Complete action using`
    - Suggest: `Завершить действие с помощью`
    - In Russian a деепричастный оборот requires a comma («Завершить действие, используя»); the usual chooser-dialog wording is «Завершить действие с помощью».
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `Сетевой адрес должен содержать "https://" or "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `guillemet` (46 occurrences).
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — Hyphen used instead of an em dash as separator.
    - Current: `Адресная строка - Firefox Suggest`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Адресная строка — Firefox Suggest`
    - Russian typography uses an em dash as a separator; the locale's house dash is the em dash.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-ru/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Автоматически удаляет данные просмотра сети, когда вы выбираете "Выйти" в главном меню`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `«Выйти»`
    - The locale's quote convention is `guillemet` (46 occurrences).

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ru/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
