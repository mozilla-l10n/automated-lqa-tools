# Android l10n QA — uk

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **Previous run** | 2026-10-16 @ `4d7697d1b89b` |
| **Mode** | baseline |
| **Strings reviewed this run** | 2,798 of 2,798 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for uk: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (54)

- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступним, або перевантаженим`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `недоступним або перевантаженим`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступним, або перевантаженим`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `недоступним або перевантаженим`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступний, або перевантажений`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `недоступний або перевантажений`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Не слід" needs the dative "вам", but the translation uses the accusative "вас".
    - Current: `тому вас не слід продовжувати`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `тому вам не слід продовжувати`
    - The impersonal construction «не слід» takes a dative experiencer, so «вас не слід» is ungrammatical.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — The second sentence has no full stop at the end, while the source has one.
    - Current: `посередницькі сертифікати{ </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `посередницькі сертифікати.{ </label> }`
    - The source sentence ends with a period; the translation drops it.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Device" is translated as "computer" in a mobile app.
    - Current: `ваш комп’ютер підключений`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `ваш пристрій підключений`
    - The source says "device". On Android the user is on a phone or tablet, so «комп’ютер» names the wrong thing.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Device" is translated as "computer" in a mobile app.
    - Current: `чи комп’ютер підключений`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `чи пристрій підключений`
    - The source says "Is the device connected". «Комп’ютер» is wrong for the Android apps.
- `mozac_feature_addons_installed_dialog_description_link_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-uk/strings.xml` — The link text is in the nominative case, so the dialog sentence reads "в налаштування розширення", which is the wrong case after «в».
    - Current: `налаштування розширення`
    - Source: `extension settings`
    - Suggest: `налаштуваннях розширення`
    - According to the developer comment, this text is inserted only into mozac_feature_addons_installed_dialog_description_3, where it follows «в» ("in the %1$s"). That position needs the locative case, «налаштуваннях», but the nominative used here gives the ungrammatical «в налаштування розширення».
- `mozac_feature_contextmenu_snackbar_email_address_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-uk/strings.xml` — Wrong genitive form "буферу"; the technical noun "буфер" takes "-а" in the genitive.
    - Current: `до буферу обміну`
    - Source: `Email address copied to clipboard`
    - Suggest: `до буфера обміну`
    - The genitive of "буфер" (a technical device) is "буфера". The sibling string mozac_feature_contextmenu_snackbar_link_copied already uses "до буфера", so this one is inconsistent with it.
- `mozac_feature_prompts_suggest_strong_password_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-uk/strings.xml` — The header is translated as a general instruction to the user ("Використовуйте") instead of the action label ("Використати") used by the related strong-password strings.
    - Current: `Використовуйте надійний пароль`
    - Source: `Use strong password`
    - Suggest: `Використати надійний пароль`
    - The comment says this is the header of a prompt that fills the form with a suggested strong password, so it labels an action. The related strings render the same English as "Використати надійний пароль?" and "Використати пароль". The imperative "Використовуйте" reads as general advice.
- `mozac_feature_qr_scanner_no_camera` — `mozilla-mobile/android-components/components/feature/qr/src/main/res/values-uk/strings.xml` — The translation says there is no access to the camera rather than that no camera is available on the device.
    - Current: `Немає доступу до камери пристрою`
    - Source: `No camera available on device`
    - Suggest: `На пристрої немає доступної камери`
    - The source and the developer comment describe a device with no camera, so the QR scanner cannot be shown. 'Немає доступу' (no access) reads as a permission problem, which points users toward the wrong cause.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-uk/strings.xml` — In Ukrainian, the relative clause "які ви можете контролювати" now describes the pages, not the summaries, so the string says the pages are under the user's control.
    - Current: `підсумовувати вміст сторінок, які ви можете контролювати`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `створювати підсумки сторінок, які залишаються під вашим контролем`
    - The source says the page summaries stay in the user's control. The translation has no noun for "summaries", so "які" can only refer back to "сторінок". It then reads as "pages that you can control", which is a different claim, and the point about privacy is lost.
- `a11y_action_label_wallpaper_collection_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Imperative "відкрийте" is used where TalkBack's appended construction needs an infinitive.
    - Current: `відкрийте посилання`
    - Source: `open link to learn more about this collection`
    - Suggest: `відкрити посилання`
    - TalkBack adds this label after "Double tap to…" (Ukrainian "Двічі торкніться, щоб…"), which needs an infinitive. The sibling labels already use one ("згорнути", "розгорнути"), so the imperative here makes the spoken sentence ungrammatical.
- `ai_controls_block_ai_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "AI enhancements" is rendered as "покращень ШІ" here, while every other string on the AI controls surface uses "вдосконалення ШІ".
    - Current: `покращень ШІ`
    - Source: `Blocking means you won’t see new or current AI enhancements in %s, or pop-ups about them.`
    - Suggest: `вдосконалень ШІ`
    - The same source term "AI enhancements" appears in the toggle title, dialog title, dialog body and banner as "вдосконалення ШІ"; using a different noun in the toggle description on the same screen is inconsistent.
- `ai_controls_banner_supporting_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "whether to use" AI features is rendered as "the possibility of using" them, losing the sense of choice.
    - Current: `Це передбачає можливість використання функцій, вдосконалених ШІ.`
    - Source: `That includes whether to use features enhanced with AI. %s`
    - Suggest: `Зокрема, чи використовувати функції, вдосконалені ШІ.`
    - The source continues the headline about always having a choice: the choice includes whether to use AI features. The Ukrainian says the choice includes the ability to use them, which drops the option not to use them.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Item Menu for %s" is rendered as "menu item for %s" instead of "the menu of item %s".
    - Current: `Елемент меню для %s`
    - Source: `Item Menu for %s`
    - Suggest: `Меню елемента %s`
    - The source and developer comment describe the overflow menu belonging to a bookmark/folder item; the Ukrainian "Елемент меню" means "a menu item", so screen readers announce the wrong control.
- `collections_migration_homepage_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Collections" is rendered as "Колекції" here, while the established term on the same home surface is "Збірки".
    - Current: `Колекції`
    - Source: `Collections are now groups`
    - Suggest: `Збірки`
    - Every other collection string in this batch uses "Збірки"/"збірку", including the home fragment header (collections_header). Using "Колекції" on the home banner gives users two different words for one feature.
- `credit_cards_name_on_card_validation_error_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Cardholder name is rendered as "назву" (name of an object) instead of "ім’я", which doesn't match the field header "Ім’я на картці".
    - Current: `Додайте назву`
    - Source: `Add a name`
    - Suggest: `Додайте ім’я`
    - This error belongs to the "Name on Card" field, which is the cardholder's personal name. "назва" is used for the names of things, and the field header in credit_cards_name_on_card uses "Ім’я".
- `debug_drawer_tab_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Tab Tools" is rendered with singular "вкладки" (of one tab) instead of plural "вкладок".
    - Current: `Інструменти вкладки`
    - Source: `Tab Tools`
    - Suggest: `Інструменти вкладок`
    - The feature provides tools for tabs in general (count, bulk creation); sibling strings use the plural "вкладок" (e.g. "Інструмент створення вкладок"), so the singular genitive is a number error.
- `download_languages_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Two separate benefits (faster translations; translating offline) are merged into one ('faster offline translation'), and 'complete' is dropped.
    - Current: `Завантажте мови для швидшого перекладу офлайн.`
    - Source: `Download complete languages for faster translations and to translate offline. %1$s`
    - Suggest: `Завантажте повні мовні пакети для швидшого перекладу та перекладу офлайн.`
    - Source lists two benefits: faster translations and the ability to translate offline. The Ukrainian says only 'for faster offline translation', which changes the claim and omits 'complete'.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "through %1$s" (until an end date) is rendered as "протягом %1$s" ("during"), which does not fit a single date.
    - Current: `протягом %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `до %1$s`
    - The developer comment says %1$s is a localized date such as "Jun 9" that marks when the promotion ends. So "through" here means "until" that date. "протягом" means "during" and needs a span of time, not a date, so "протягом 9 черв." does not say when the promotion ends.
- `nova_onboarding_app_icon_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Home screen" is rendered as "домівка", which means a dwelling or, in uk Firefox, the Firefox Home page, not the device home screen.
    - Current: `Надайте своїй домівці індивідуальності.`
    - Source: `Give your home screen a personal touch.`
    - Suggest: `Надайте своєму головному екрану індивідуальності.`
    - This string belongs to the custom app icon prompt, and the icon appears on the phone's home screen. In uk Firefox, "Домівка" is the term for the Firefox Home page, so a user would think the setting changes that page or would read it as their literal home.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "So you're always up to date on how to stay protected" became "so you're always protected", a guarantee of protection the source doesn't make.
    - Current: `щоб завжди бути захищеними`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `щоб завжди знати, як залишатися захищеними`
    - The source only promises information about how to stay protected. The Ukrainian promises the user will always be protected.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Is proudly independent" became "is known for its independence", which states Firefox's reputation instead of a plain fact about it.
    - Current: `Firefox відомий своєю незалежністю та відданістю`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox гордо зберігає незалежність і відданий`
    - The source says Firefox is independent and dedicated, with pride. The Ukrainian instead says Firefox is known for these qualities, which is a different claim.
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — A comma is missing before "що" after the participle "знаючи".
    - Current: `знаючи що вас`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `знаючи, що вас`
    - The subordinate clause introduced by "що" after "знаючи" must be set off with a comma in Ukrainian punctuation.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The hedge "helps stop" became the absolute "Forbid companies from tracking", and "one tap" was dropped.
    - Current: `Забороніть компаніям стежити за вашими діями онлайн.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Один дотик допомагає завадити компаніям стежити за вашими діями онлайн.`
    - The en-US only says one tap helps stop companies spying on clicks. The Ukrainian tells users they can forbid tracking outright, which promises more protection than the product claims.
- `pbm_authentication_unlock_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Typo in the genitive plural of "вкладка": "вкладкок" instead of "вкладок".
    - Current: `вкладкок`
    - Source: `Unlock private tabs`
    - Suggest: `вкладок`
    - The correct genitive plural of "вкладка" is "вкладок", which the other private-tabs strings in this batch use.
- `open_all_warning_message` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — A comma is missing before the subordinate clause introduced by "поки".
    - Current: `сповільнити %s поки`
    - Source: `Opening this many tabs may slow down %s while the pages are loading. Are you sure you want to continue?`
    - Suggest: `сповільнити %s, поки`
    - Ukrainian punctuation rules require a comma to set off a subordinate clause beginning with "поки".
- `preference_doh_default_protection_info_4` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says "VPN policies" are active, but the source means a VPN itself is active.
    - Current: `якщо є активні політики VPN, батьківський контроль або корпоративні політики`
    - Source: `Turn off when VPN, parental control, or enterprise policies are active`
    - Suggest: `якщо активні VPN, батьківський контроль або корпоративні політики`
    - The en-US lists three separate conditions: an active VPN, parental control, or enterprise policies. The Ukrainian attaches "політики" to VPN, which is a condition the source never states.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Social media trackers" is rendered as "соціальні мережі" (social networks), so the option reads as blocking social networks rather than social media trackers.
    - Current: `Елементи стеження між сайтами та соціальні мережі`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Елементи стеження між сайтами та соціальних мереж`
    - In the source, "cross-site" and "social media" both describe "trackers". In the translation, "соціальні мережі" is in the nominative and stands as a second item on the list, so it names the social networks themselves as what is blocked.
- `preferences_customize_extension_collection` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation calls the extensions custom, when it is the collection that is custom.
    - Current: `Збірка користувацьких розширень`
    - Source: `Custom extension collection`
    - Suggest: `Власна збірка розширень`
    - Per the developer comment, this setting lets the user customize the configured AMO collection, i.e. use a custom collection of extensions. The Ukrainian says 'a collection of user-made extensions', which describes the extensions instead of the collection.
- `preferences_https_only_on_all` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Status summary "On in all tabs" is translated as an imperative action ("Enable in all tabs") instead of a state.
    - Current: `Увімкнути в усіх вкладках`
    - Source: `On in all tabs`
    - Suggest: `Увімкнено в усіх вкладках`
    - The developer comment says this is the summary shown when HTTPS-Only is set to on in all tabs, so it should state the current setting. It should match the sibling "Off" summary, which is "Вимкнено".
- `preferences_https_only_on_private` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Status summary "On in private tabs" is translated as an imperative action ("Enable in private tabs") instead of a state.
    - Current: `Увімкнути у приватних вкладках`
    - Source: `On in private tabs`
    - Suggest: `Увімкнено у приватних вкладках`
    - The developer comment says this is the summary shown when HTTPS-Only is on in private tabs only, so it should state the setting. It should match the "Off" summary, which is "Вимкнено".
- `preferences_sync_category` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Missing comma before the subordinate clause introduced by «що».
    - Current: `Оберіть що синхронізувати`
    - Source: `Choose what to sync`
    - Suggest: `Оберіть, що синхронізувати`
    - Ukrainian punctuation requires a comma before a subordinate clause starting with «що». The locale's own string preferences_sync_category_no_engine_selected_summary writes «Виберіть, що потрібно синхронізувати» with the comma.
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Off-duty" is rendered as "не працює" (is not working/broken) instead of conveying that protection is inactive.
    - Current: `%s не працює.`
    - Source: `%s is off-duty. We suggest turning protections back on.`
    - Suggest: `%s не на чергуванні.`
    - The source means the app's protections are switched off ("off-duty"). "не працює" reads as the app malfunctioning or not working at all.
- `protection_panel_etp_toggle_disabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Tracking protection" is rendered as "захист від відстеження", while the toggle label on the same panel uses "захист від стеження".
    - Current: `захист від відстеження`
    - Source: `Turning on tracking protection is recommended.`
    - Suggest: `захист від стеження`
    - The same feature name appears on the same protection panel (protection_panel_etp_toggle_label: "Розширений захист від стеження"), so the term should be consistent.
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "between updates" is rendered as "with each update", which reverses the point that changes arrive outside regular updates.
    - Current: `з кожним оновленням`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `між оновленнями`
    - The source says Firefox improves features between updates, through remotely applied changes. "З кожним оновленням" means "with each update", which contradicts the remote-rollout meaning of the string.
- `search_header_menu_item_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation drops "This time", so the header no longer says the engine choice applies only to the current search.
    - Current: `Шукати в:`
    - Source: `This time search in:`
    - Suggest: `Цього разу шукати в:`
    - The en-US "This time search in:" makes clear that the engine chosen in this menu is used once and does not change the default. "Шукати в:" leaves that out.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Search" is translated as a noun, so the title reads as "settings of search" instead of "search through settings".
    - Current: `Налаштування пошуку`
    - Source: `Search settings`
    - Suggest: `Пошук у налаштуваннях`
    - The developer comment says "Search" is a verb here: this is the title of the Settings Search screen. "Налаштування пошуку" means the settings of the search engine, which is a different screen.
- `sync_send_tab_empty_state_link` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `під'єднати`
    - Source: `Learn how to connect a device`
    - Suggest: `під’єднати`
    - The uk convention is the typographic apostrophe (111 vs 3), and other strings on this surface use it (e.g. sync_connect_device).
- `sync_send_tab_empty_state_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `під'єднаних`
    - Source: `No devices connected`
    - Suggest: `під’єднаних`
    - The uk convention is the typographic apostrophe, and the matching string sync_add_new_device_message already uses "під’єднаних".
- `sync_send_tab_error_connection_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `з'єднання`
    - Source: `Check your internet connection`
    - Suggest: `з’єднання`
    - The uk convention is the typographic apostrophe (111 vs 3 straight).
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Data saving mode" is rendered as «режим збереження даних» here but as «режим заощадження даних» in the related download dialog.
    - Current: `режимі збереження даних`
    - Source: `Always download languages in data saving mode`
    - Suggest: `режимі заощадження даних`
    - Both strings refer to the same Android data saver mode on the translations surface. 'Збереження даних' can also be read as 'storing data', so the dialog's 'заощадження даних' is clearer and should be used in both places.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The adverbial participle 'Закривши' has no matching subject because the main clause is impersonal ('звіт буде проігноровано').
    - Current: `Закривши це сповіщення, звіт буде проігноровано.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Якщо закрити це сповіщення, звіт буде проігноровано.`
    - In Ukrainian an adverbial participle needs the same subject as the main clause. Here the participle would grammatically attach to 'звіт', so the phrase reads as if the report closes the notification.
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The adverbial participle 'Закривши' has no matching subject because the main clause is impersonal ('звіти буде проігноровано').
    - Current: `Закривши це сповіщення, звіти буде проігноровано.`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `Якщо закрити це сповіщення, звіти буде проігноровано.`
    - In Ukrainian an adverbial participle needs the same subject as the main clause. Here it would grammatically attach to 'звіти', so the phrase reads as if the reports close the notification.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says the unsent report itself is being investigated, but the source says the report relates to crashes that are being investigated.
    - Current: `який наразі досліджується`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `пов’язаний зі збоями, які наразі досліджуються`
    - Source: 'related to crashes being investigated'. It is the crashes that are under investigation. The report has not been sent, so it cannot itself be under investigation.
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says the unsent reports themselves are being investigated, but the source says they relate to crashes that are being investigated.
    - Current: `які наразі досліджуються`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `пов’язані зі збоями, які наразі досліджуються`
    - Source: 'related to crashes being investigated'. It is the crashes that are under investigation, not the reports, which have not been sent.
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Missing comma before the participial phrase "перейшовши до…".
    - Current: `Змініть це налаштування перейшовши`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `Змініть це налаштування, перейшовши`
    - Ukrainian punctuation requires a comma to set off a дієприслівниковий зворот; without it the sentence is grammatically mis-punctuated.
- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Forward-navigation content description uses a noun ("Перехід уперед") while its paired back-navigation string uses an imperative verb ("Перейти назад").
    - Current: `Перехід уперед`
    - Source: `Navigate forward`
    - Suggest: `Перейти вперед`
    - The two buttons are paired screen-reader labels on the same toolbar ("Navigate back"/"Navigate forward"); they should share the same verbal form for consistency.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The final sentence has lost the full stop that ends the source sentence.
    - Current: `посередницькі сертифікати{ </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `посередницькі сертифікати.{ </label> }`
    - The en-US sentence ends with a period before </label>. The Ukrainian leaves it out, although the first sentence in the same string keeps its period.
- `menu_about` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The menu item is the bare preposition "Про" with no object, so it reads as unfinished.
    - Current: `Про`
    - Source: `About`
    - Suggest: `Про програму`
    - In English, "About" works on its own as a menu label. In Ukrainian, "Про" needs an object (for example "Про програму"). On its own it is ungrammatical.
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "Your favorite URLs" (the list the user builds) is translated as "URLs of popular sites".
    - Current: `URL-адреси популярних сайтів`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `ваші улюблені URL-адреси`
    - The source and the developer comment both refer to the user's own list of URLs. "Популярних сайтів" mixes this up with the separate built-in list of 450 popular URLs (preference_autocomplete_topsite_summary2), so it misdescribes what the toggle does.
- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "HTTPS-Only Mode" is rendered as "HTTPS-режим", which drops the "only" meaning.
    - Current: `HTTPS-режим`
    - Source: `HTTPS-Only Mode`
    - Suggest: `Режим лише HTTPS`
    - The source names a mode that allows only HTTPS connections. "HTTPS-режим" just means "HTTPS mode" and loses the restriction. Firefox uses "Режим лише HTTPS" for this.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The example nouns are in the nominative case but should agree with the genitive "активності".
    - Current: `наприклад, дотики і прокручування`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `наприклад, дотиків і прокручування`
    - "Дотики і прокручування" are examples of the activity being measured ("вимірювання активності"), so they need the same genitive case.

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
| Strings | 2,798 |
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
| quotes | `curly-double` 13, `straight-double` 10 | _mixed_ |
| apostrophe | `typographic` 111, `straight` 3 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 9 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (57)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "So you're always up to date on how to stay protected" became "so you're always protected", a guarantee of protection the source doesn't make.
    - Current: `щоб завжди бути захищеними`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `щоб завжди знати, як залишатися захищеними`
    - The source only promises information about how to stay protected. The Ukrainian promises the user will always be protected.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The hedge "helps stop" became the absolute "Forbid companies from tracking", and "one tap" was dropped.
    - Current: `Забороніть компаніям стежити за вашими діями онлайн.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Один дотик допомагає завадити компаніям стежити за вашими діями онлайн.`
    - The en-US only says one tap helps stop companies spying on clicks. The Ukrainian tells users they can forbid tracking outright, which promises more protection than the product claims.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 25 |
| 3 | Degraded language (grammar, spelling, terminology) | 17 |
| 4 | Cosmetic (typography, spacing) | 15 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Device" is translated as "computer" in a mobile app.
    - Current: `ваш комп’ютер підключений`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `ваш пристрій підключений`
    - The source says "device". On Android the user is on a phone or tablet, so «комп’ютер» names the wrong thing.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Device" is translated as "computer" in a mobile app.
    - Current: `чи комп’ютер підключений`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `чи пристрій підключений`
    - The source says "Is the device connected". «Комп’ютер» is wrong for the Android apps.
- `mozac_feature_qr_scanner_no_camera` — `mozilla-mobile/android-components/components/feature/qr/src/main/res/values-uk/strings.xml` — The translation says there is no access to the camera rather than that no camera is available on the device.
    - Current: `Немає доступу до камери пристрою`
    - Source: `No camera available on device`
    - Suggest: `На пристрої немає доступної камери`
    - The source and the developer comment describe a device with no camera, so the QR scanner cannot be shown. 'Немає доступу' (no access) reads as a permission problem, which points users toward the wrong cause.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-uk/strings.xml` — In Ukrainian, the relative clause "які ви можете контролювати" now describes the pages, not the summaries, so the string says the pages are under the user's control.
    - Current: `підсумовувати вміст сторінок, які ви можете контролювати`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `створювати підсумки сторінок, які залишаються під вашим контролем`
    - The source says the page summaries stay in the user's control. The translation has no noun for "summaries", so "які" can only refer back to "сторінок". It then reads as "pages that you can control", which is a different claim, and the point about privacy is lost.
- `ai_controls_banner_supporting_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "whether to use" AI features is rendered as "the possibility of using" them, losing the sense of choice.
    - Current: `Це передбачає можливість використання функцій, вдосконалених ШІ.`
    - Source: `That includes whether to use features enhanced with AI. %s`
    - Suggest: `Зокрема, чи використовувати функції, вдосконалені ШІ.`
    - The source continues the headline about always having a choice: the choice includes whether to use AI features. The Ukrainian says the choice includes the ability to use them, which drops the option not to use them.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Item Menu for %s" is rendered as "menu item for %s" instead of "the menu of item %s".
    - Current: `Елемент меню для %s`
    - Source: `Item Menu for %s`
    - Suggest: `Меню елемента %s`
    - The source and developer comment describe the overflow menu belonging to a bookmark/folder item; the Ukrainian "Елемент меню" means "a menu item", so screen readers announce the wrong control.
- `download_languages_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Two separate benefits (faster translations; translating offline) are merged into one ('faster offline translation'), and 'complete' is dropped.
    - Current: `Завантажте мови для швидшого перекладу офлайн.`
    - Source: `Download complete languages for faster translations and to translate offline. %1$s`
    - Suggest: `Завантажте повні мовні пакети для швидшого перекладу та перекладу офлайн.`
    - Source lists two benefits: faster translations and the ability to translate offline. The Ukrainian says only 'for faster offline translation', which changes the claim and omits 'complete'.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "through %1$s" (until an end date) is rendered as "протягом %1$s" ("during"), which does not fit a single date.
    - Current: `протягом %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `до %1$s`
    - The developer comment says %1$s is a localized date such as "Jun 9" that marks when the promotion ends. So "through" here means "until" that date. "протягом" means "during" and needs a span of time, not a date, so "протягом 9 черв." does not say when the promotion ends.
- `nova_onboarding_app_icon_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Home screen" is rendered as "домівка", which means a dwelling or, in uk Firefox, the Firefox Home page, not the device home screen.
    - Current: `Надайте своїй домівці індивідуальності.`
    - Source: `Give your home screen a personal touch.`
    - Suggest: `Надайте своєму головному екрану індивідуальності.`
    - This string belongs to the custom app icon prompt, and the icon appears on the phone's home screen. In uk Firefox, "Домівка" is the term for the Firefox Home page, so a user would think the setting changes that page or would read it as their literal home.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Is proudly independent" became "is known for its independence", which states Firefox's reputation instead of a plain fact about it.
    - Current: `Firefox відомий своєю незалежністю та відданістю`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox гордо зберігає незалежність і відданий`
    - The source says Firefox is independent and dedicated, with pride. The Ukrainian instead says Firefox is known for these qualities, which is a different claim.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "So you're always up to date on how to stay protected" became "so you're always protected", a guarantee of protection the source doesn't make.
    - Current: `щоб завжди бути захищеними`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `щоб завжди знати, як залишатися захищеними`
    - The source only promises information about how to stay protected. The Ukrainian promises the user will always be protected.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The hedge "helps stop" became the absolute "Forbid companies from tracking", and "one tap" was dropped.
    - Current: `Забороніть компаніям стежити за вашими діями онлайн.`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `Один дотик допомагає завадити компаніям стежити за вашими діями онлайн.`
    - The en-US only says one tap helps stop companies spying on clicks. The Ukrainian tells users they can forbid tracking outright, which promises more protection than the product claims.
- `preference_doh_default_protection_info_4` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says "VPN policies" are active, but the source means a VPN itself is active.
    - Current: `якщо є активні політики VPN, батьківський контроль або корпоративні політики`
    - Source: `Turn off when VPN, parental control, or enterprise policies are active`
    - Suggest: `якщо активні VPN, батьківський контроль або корпоративні політики`
    - The en-US lists three separate conditions: an active VPN, parental control, or enterprise policies. The Ukrainian attaches "політики" to VPN, which is a condition the source never states.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Social media trackers" is rendered as "соціальні мережі" (social networks), so the option reads as blocking social networks rather than social media trackers.
    - Current: `Елементи стеження між сайтами та соціальні мережі`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Елементи стеження між сайтами та соціальних мереж`
    - In the source, "cross-site" and "social media" both describe "trackers". In the translation, "соціальні мережі" is in the nominative and stands as a second item on the list, so it names the social networks themselves as what is blocked.
- `preferences_customize_extension_collection` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation calls the extensions custom, when it is the collection that is custom.
    - Current: `Збірка користувацьких розширень`
    - Source: `Custom extension collection`
    - Suggest: `Власна збірка розширень`
    - Per the developer comment, this setting lets the user customize the configured AMO collection, i.e. use a custom collection of extensions. The Ukrainian says 'a collection of user-made extensions', which describes the extensions instead of the collection.
- `preferences_https_only_on_all` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Status summary "On in all tabs" is translated as an imperative action ("Enable in all tabs") instead of a state.
    - Current: `Увімкнути в усіх вкладках`
    - Source: `On in all tabs`
    - Suggest: `Увімкнено в усіх вкладках`
    - The developer comment says this is the summary shown when HTTPS-Only is set to on in all tabs, so it should state the current setting. It should match the sibling "Off" summary, which is "Вимкнено".
- `preferences_https_only_on_private` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Status summary "On in private tabs" is translated as an imperative action ("Enable in private tabs") instead of a state.
    - Current: `Увімкнути у приватних вкладках`
    - Source: `On in private tabs`
    - Suggest: `Увімкнено у приватних вкладках`
    - The developer comment says this is the summary shown when HTTPS-Only is on in private tabs only, so it should state the setting. It should match the "Off" summary, which is "Вимкнено".
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Off-duty" is rendered as "не працює" (is not working/broken) instead of conveying that protection is inactive.
    - Current: `%s не працює.`
    - Source: `%s is off-duty. We suggest turning protections back on.`
    - Suggest: `%s не на чергуванні.`
    - The source means the app's protections are switched off ("off-duty"). "не працює" reads as the app malfunctioning or not working at all.
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "between updates" is rendered as "with each update", which reverses the point that changes arrive outside regular updates.
    - Current: `з кожним оновленням`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `між оновленнями`
    - The source says Firefox improves features between updates, through remotely applied changes. "З кожним оновленням" means "with each update", which contradicts the remote-rollout meaning of the string.
- `search_header_menu_item_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation drops "This time", so the header no longer says the engine choice applies only to the current search.
    - Current: `Шукати в:`
    - Source: `This time search in:`
    - Suggest: `Цього разу шукати в:`
    - The en-US "This time search in:" makes clear that the engine chosen in this menu is used once and does not change the default. "Шукати в:" leaves that out.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Search" is translated as a noun, so the title reads as "settings of search" instead of "search through settings".
    - Current: `Налаштування пошуку`
    - Source: `Search settings`
    - Suggest: `Пошук у налаштуваннях`
    - The developer comment says "Search" is a verb here: this is the title of the Settings Search screen. "Налаштування пошуку" means the settings of the search engine, which is a different screen.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says the unsent report itself is being investigated, but the source says the report relates to crashes that are being investigated.
    - Current: `який наразі досліджується`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `пов’язаний зі збоями, які наразі досліджуються`
    - Source: 'related to crashes being investigated'. It is the crashes that are under investigation. The report has not been sent, so it cannot itself be under investigation.
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The translation says the unsent reports themselves are being investigated, but the source says they relate to crashes that are being investigated.
    - Current: `які наразі досліджуються`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `пов’язані зі збоями, які наразі досліджуються`
    - Source: 'related to crashes being investigated'. It is the crashes that are under investigation, not the reports, which have not been sent.
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "Your favorite URLs" (the list the user builds) is translated as "URLs of popular sites".
    - Current: `URL-адреси популярних сайтів`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `ваші улюблені URL-адреси`
    - The source and the developer comment both refer to the user's own list of URLs. "Популярних сайтів" mixes this up with the separate built-in list of 450 popular URLs (preference_autocomplete_topsite_summary2), so it misdescribes what the toggle does.
- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "HTTPS-Only Mode" is rendered as "HTTPS-режим", which drops the "only" meaning.
    - Current: `HTTPS-режим`
    - Source: `HTTPS-Only Mode`
    - Suggest: `Режим лише HTTPS`
    - The source names a mode that allows only HTTPS connections. "HTTPS-режим" just means "HTTPS mode" and loses the restriction. Firefox uses "Режим лише HTTPS" for this.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — "Не слід" needs the dative "вам", but the translation uses the accusative "вас".
    - Current: `тому вас не слід продовжувати`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `тому вам не слід продовжувати`
    - The impersonal construction «не слід» takes a dative experiencer, so «вас не слід» is ungrammatical.
- `mozac_feature_addons_installed_dialog_description_link_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-uk/strings.xml` — The link text is in the nominative case, so the dialog sentence reads "в налаштування розширення", which is the wrong case after «в».
    - Current: `налаштування розширення`
    - Source: `extension settings`
    - Suggest: `налаштуваннях розширення`
    - According to the developer comment, this text is inserted only into mozac_feature_addons_installed_dialog_description_3, where it follows «в» ("in the %1$s"). That position needs the locative case, «налаштуваннях», but the nominative used here gives the ungrammatical «в налаштування розширення».
- `mozac_feature_contextmenu_snackbar_email_address_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-uk/strings.xml` — Wrong genitive form "буферу"; the technical noun "буфер" takes "-а" in the genitive.
    - Current: `до буферу обміну`
    - Source: `Email address copied to clipboard`
    - Suggest: `до буфера обміну`
    - The genitive of "буфер" (a technical device) is "буфера". The sibling string mozac_feature_contextmenu_snackbar_link_copied already uses "до буфера", so this one is inconsistent with it.
- `a11y_action_label_wallpaper_collection_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Imperative "відкрийте" is used where TalkBack's appended construction needs an infinitive.
    - Current: `відкрийте посилання`
    - Source: `open link to learn more about this collection`
    - Suggest: `відкрити посилання`
    - TalkBack adds this label after "Double tap to…" (Ukrainian "Двічі торкніться, щоб…"), which needs an infinitive. The sibling labels already use one ("згорнути", "розгорнути"), so the imperative here makes the spoken sentence ungrammatical.
- `debug_drawer_tab_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Tab Tools" is rendered with singular "вкладки" (of one tab) instead of plural "вкладок".
    - Current: `Інструменти вкладки`
    - Source: `Tab Tools`
    - Suggest: `Інструменти вкладок`
    - The feature provides tools for tabs in general (count, bulk creation); sibling strings use the plural "вкладок" (e.g. "Інструмент створення вкладок"), so the singular genitive is a number error.
- `pbm_authentication_unlock_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Typo in the genitive plural of "вкладка": "вкладкок" instead of "вкладок".
    - Current: `вкладкок`
    - Source: `Unlock private tabs`
    - Suggest: `вкладок`
    - The correct genitive plural of "вкладка" is "вкладок", which the other private-tabs strings in this batch use.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The adverbial participle 'Закривши' has no matching subject because the main clause is impersonal ('звіт буде проігноровано').
    - Current: `Закривши це сповіщення, звіт буде проігноровано.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Якщо закрити це сповіщення, звіт буде проігноровано.`
    - In Ukrainian an adverbial participle needs the same subject as the main clause. Here the participle would grammatically attach to 'звіт', so the phrase reads as if the report closes the notification.
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — The adverbial participle 'Закривши' has no matching subject because the main clause is impersonal ('звіти буде проігноровано').
    - Current: `Закривши це сповіщення, звіти буде проігноровано.`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `Якщо закрити це сповіщення, звіти буде проігноровано.`
    - In Ukrainian an adverbial participle needs the same subject as the main clause. Here it would grammatically attach to 'звіти', so the phrase reads as if the reports close the notification.
- `menu_about` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The menu item is the bare preposition "Про" with no object, so it reads as unfinished.
    - Current: `Про`
    - Source: `About`
    - Suggest: `Про програму`
    - In English, "About" works on its own as a menu label. In Ukrainian, "Про" needs an object (for example "Про програму"). On its own it is ungrammatical.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The example nouns are in the nominative case but should agree with the genitive "активності".
    - Current: `наприклад, дотики і прокручування`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `наприклад, дотиків і прокручування`
    - "Дотики і прокручування" are examples of the activity being measured ("вимірювання активності"), so they need the same genitive case.

### D. Terminology, register & consistency

- `mozac_feature_prompts_suggest_strong_password_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-uk/strings.xml` — The header is translated as a general instruction to the user ("Використовуйте") instead of the action label ("Використати") used by the related strong-password strings.
    - Current: `Використовуйте надійний пароль`
    - Source: `Use strong password`
    - Suggest: `Використати надійний пароль`
    - The comment says this is the header of a prompt that fills the form with a suggested strong password, so it labels an action. The related strings render the same English as "Використати надійний пароль?" and "Використати пароль". The imperative "Використовуйте" reads as general advice.
- `ai_controls_block_ai_description` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "AI enhancements" is rendered as "покращень ШІ" here, while every other string on the AI controls surface uses "вдосконалення ШІ".
    - Current: `покращень ШІ`
    - Source: `Blocking means you won’t see new or current AI enhancements in %s, or pop-ups about them.`
    - Suggest: `вдосконалень ШІ`
    - The same source term "AI enhancements" appears in the toggle title, dialog title, dialog body and banner as "вдосконалення ШІ"; using a different noun in the toggle description on the same screen is inconsistent.
- `collections_migration_homepage_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Collections" is rendered as "Колекції" here, while the established term on the same home surface is "Збірки".
    - Current: `Колекції`
    - Source: `Collections are now groups`
    - Suggest: `Збірки`
    - Every other collection string in this batch uses "Збірки"/"збірку", including the home fragment header (collections_header). Using "Колекції" on the home banner gives users two different words for one feature.
- `credit_cards_name_on_card_validation_error_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Cardholder name is rendered as "назву" (name of an object) instead of "ім’я", which doesn't match the field header "Ім’я на картці".
    - Current: `Додайте назву`
    - Source: `Add a name`
    - Suggest: `Додайте ім’я`
    - This error belongs to the "Name on Card" field, which is the cardholder's personal name. "назва" is used for the names of things, and the field header in credit_cards_name_on_card uses "Ім’я".
- `protection_panel_etp_toggle_disabled_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Tracking protection" is rendered as "захист від відстеження", while the toggle label on the same panel uses "захист від стеження".
    - Current: `захист від відстеження`
    - Source: `Turning on tracking protection is recommended.`
    - Suggest: `захист від стеження`
    - The same feature name appears on the same protection panel (protection_panel_etp_toggle_label: "Розширений захист від стеження"), so the term should be consistent.
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — "Data saving mode" is rendered as «режим збереження даних» here but as «режим заощадження даних» in the related download dialog.
    - Current: `режимі збереження даних`
    - Source: `Always download languages in data saving mode`
    - Suggest: `режимі заощадження даних`
    - Both strings refer to the same Android data saver mode on the translations surface. 'Збереження даних' can also be read as 'storing data', so the dialog's 'заощадження даних' is clearer and should be used in both places.
- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Forward-navigation content description uses a noun ("Перехід уперед") while its paired back-navigation string uses an imperative verb ("Перейти назад").
    - Current: `Перехід уперед`
    - Source: `Navigate forward`
    - Suggest: `Перейти вперед`
    - The two buttons are paired screen-reader labels on the same toolbar ("Navigate back"/"Navigate forward"); they should share the same verbal form for consistency.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступним, або перевантаженим`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `недоступним або перевантаженим`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступним, або перевантаженим`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `недоступним або перевантаженим`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — Superfluous comma before the single conjunction «або» joining homogeneous predicates.
    - Current: `недоступний, або перевантажений`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `недоступний або перевантажений`
    - Ukrainian punctuation rules do not put a comma before a single «або» linking homogeneous parts of a sentence.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-uk/strings.xml` — The second sentence has no full stop at the end, while the source has one.
    - Current: `посередницькі сертифікати{ </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `посередницькі сертифікати.{ </label> }`
    - The source sentence ends with a period; the translation drops it.
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — A comma is missing before "що" after the participle "знаючи".
    - Current: `знаючи що вас`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `знаючи, що вас`
    - The subordinate clause introduced by "що" after "знаючи" must be set off with a comma in Ukrainian punctuation.
- `open_all_warning_message` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — A comma is missing before the subordinate clause introduced by "поки".
    - Current: `сповільнити %s поки`
    - Source: `Opening this many tabs may slow down %s while the pages are loading. Are you sure you want to continue?`
    - Suggest: `сповільнити %s, поки`
    - Ukrainian punctuation rules require a comma to set off a subordinate clause beginning with "поки".
- `preferences_sync_category` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Missing comma before the subordinate clause introduced by «що».
    - Current: `Оберіть що синхронізувати`
    - Source: `Choose what to sync`
    - Suggest: `Оберіть, що синхронізувати`
    - Ukrainian punctuation requires a comma before a subordinate clause starting with «що». The locale's own string preferences_sync_category_no_engine_selected_summary writes «Виберіть, що потрібно синхронізувати» with the comma.
- `sync_send_tab_empty_state_link` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — `sync_send_tab_empty_state_link` uses a straight apostrophe
    - Current: `Дізнатися, як під'єднати пристрій`
    - Source: `Learn how to connect a device`
    - The tree uses ’ 111 times against 3 straight.
- `sync_send_tab_empty_state_link` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `під'єднати`
    - Source: `Learn how to connect a device`
    - Suggest: `під’єднати`
    - The uk convention is the typographic apostrophe (111 vs 3), and other strings on this surface use it (e.g. sync_connect_device).
- `sync_send_tab_empty_state_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — `sync_send_tab_empty_state_title` uses a straight apostrophe
    - Current: `Немає під'єднаних пристроїв`
    - Source: `No devices connected`
    - The tree uses ’ 111 times against 3 straight.
- `sync_send_tab_empty_state_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `під'єднаних`
    - Source: `No devices connected`
    - Suggest: `під’єднаних`
    - The uk convention is the typographic apostrophe, and the matching string sync_add_new_device_message already uses "під’єднаних".
- `sync_send_tab_error_connection_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — `sync_send_tab_error_connection_title` uses a straight apostrophe
    - Current: `Перевірте своє з'єднання з інтернетом`
    - Source: `Check your internet connection`
    - The tree uses ’ 111 times against 3 straight.
- `sync_send_tab_error_connection_title` — `mozilla-mobile/fenix/app/src/main/res/values-uk/strings.xml` — Straight apostrophe used instead of the locale's typographic apostrophe.
    - Current: `з'єднання`
    - Source: `Check your internet connection`
    - Suggest: `з’єднання`
    - The uk convention is the typographic apostrophe (111 vs 3 straight).
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Missing comma before the participial phrase "перейшовши до…".
    - Current: `Змініть це налаштування перейшовши`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `Змініть це налаштування, перейшовши`
    - Ukrainian punctuation requires a comma to set off a дієприслівниковий зворот; without it the sentence is grammatically mis-punctuated.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The final sentence has lost the full stop that ends the source sentence.
    - Current: `посередницькі сертифікати{ </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `посередницькі сертифікати.{ </label> }`
    - The en-US sentence ends with a period before </label>. The Ukrainian leaves it out, although the first sentence in the same string keeps its period.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/uk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
