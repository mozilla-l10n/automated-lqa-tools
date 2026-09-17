# Android l10n QA — fa

| | |
|---|---|
| **Generated** | 2026-09-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `51a5854c742d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `51a5854c742d` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 2,594 of 2,594 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




---

## Changes in this run

### 🆕 New findings (139)

- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "The connection was reset" is rendered as "the connection was re-established", reversing the meaning of the error.
    - Current: `اتصال از نو برقرار شد`
    - Source: `The connection was reset`
    - Suggest: `اتصال بازنشانی شد`
    - The source reports a connection reset error (failure); the target says the connection was successfully re-established, the opposite of an error condition.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — First paragraph translates the net-interrupt message instead of "The network link was interrupted while negotiating a connection."
    - Current: `مرورگر با موفقیت متصل شد ، اما هنگام انتقال اطلاعات ، اتصال قطع شد. لطفا دوباره امتحان کنید.`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `پیوند شبکه در هنگام برقراری اتّصال قطع شد. لطفاً دوباره تلاش کنید.`
    - The source says the network link was interrupted while negotiating a connection; the target claims the browser connected successfully and the connection dropped while transferring information (text copied from the net_interrupt string).
- `mozac_browser_errorpages_file_access_denied_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Past-tense "was denied" rendered as present/habitual "is denied".
    - Current: `دسترسی به این پرونده رد می‌شود`
    - Source: `Access to the file was denied`
    - Suggest: `دسترسی به این پرونده رد شد`
    - The source states a completed event ("Access to the file was denied"); the Persian present tense describes an ongoing/general behaviour.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "device" translated as "رایانه" (computer) in a mobile component string.
    - Current: `آیا رایانه به یک شبکهٔ فعال متصل است؟`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `آیا افزاره به یک شبکهٔ فعال متصل است؟`
    - The source asks about the device; "رایانه" names a computer, which is wrong on an Android device and inconsistent with other strings that use دستگاه/افزاره.
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "invalid" form of compression rendered as "ناشناخته" (unknown).
    - Current: `از گونه‌ای ناشناخته یا پشتیبانی نشده از فشرده‌سازی استفاده می‌کند`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `از گونه‌ای نامعتبر یا پشتیبانی‌نشده از فشرده‌سازی استفاده می‌کند`
    - The source says the compression form is invalid or unsupported, not unknown.
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Third bullet asks about access permissions to the "address" instead of to the requested item.
    - Current: `آیا مجوزهای دسترسی کافی برای دست‌یابی به این نشانی را دارید؟`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `آیا مجوزهای دسترسی کافی برای دست‌یابی به مورد درخواستی را دارید؟`
    - The source asks about sufficient access permissions to the requested item, not to the address.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "Incorrect settings can interfere with Web browsing" rendered as a certainty ("prevents Web browsing").
    - Current: `تنظیمات نادرست آن مانع از مرور وب می‌شود.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `تنظیمات نادرست می‌تواند در مرور وب اختلال ایجاد کند.`
    - The source hedges with "can interfere"; the target asserts that incorrect settings do prevent Web browsing.
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing spaces around inline markup and after punctuation, plus broken spacing in several words.
    - Current: `نشانی درخواست مشخصا(به عنوان مثال{ <q> }mozilla.org:80{ </q> }برای درگاه ۸۰ بر روی mozilla.org) ازدرگاهی استفاده می کندکه`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `نشانی درخواست‌شده درگاهی را مشخص کرده است (به عنوان مثال { <q> }mozilla.org:80{ </q> } برای درگاه ۸۰ بر روی mozilla.org) که در حالت عادی`
    - Words are run together ("ازدرگاهی", "می کندکه", "لغوکرد") and spaces are missing before/after the inline <q> markup and after the sentence-ending period, which the user reads as broken text.
- `mozac_browser_errorpages_file_access_denied_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Comma misplaced/attached and mood mismatch in the second clause ("may be preventing" rendered as a plain assertion).
    - Current: `ممکن است حذف،‌منتقل شده باشد یا مجوز‌های آن از دسترسی جلوگیری‌ می‌کند.`
    - Source: `{ <ul> } { <li> }It may have been removed, moved, or file permissions may be preventing access.{ </li> } { </ul> }`
    - Suggest: `ممکن است حذف یا منتقل شده باشد، یا مجوزهای آن مانع دسترسی شوند.`
    - The source says permissions "may be preventing" access; the target states it as fact, and the punctuation/spacing ("حذف،‌منتقل", "جلوگیری‌ می‌کند") is broken.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "potentially harmful site" is rendered as "attack site" (تهاجمی), duplicating the malware string instead of translating this one.
    - Current: `پایگاه%1$s به عنوان یک وب‌گاه تهاجمی گزارش شده و بر اساس ترجیحات امنیتی شما مسدود شده است.`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `پایگاه %1$s به عنوان یک وب‌گاه بالقوه زیان‌آور گزارش شده و بر اساس ترجیحات امنیتی شما مسدود شده است.`
    - The source says "reported as a potentially harmful site", not "attack site"; the title of this same error page correctly uses زیان‌آور.
- `mozac_browser_errorpages_unknown_protocol_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "Unknown Protocol" is translated as "the address was not understandable" instead of referring to the protocol.
    - Current: `نشانی قابل فهم نبود`
    - Source: `Unknown Protocol`
    - Suggest: `قرارداد ناشناخته`
    - The source names an unknown protocol; the translation says the address was unintelligible, and the body text of the same page uses قرارداد for protocol.
- `mozac_browser_errorpages_safe_browsing_malware_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing space between پایگاه and the %1$s placeholder, so the URL runs into the preceding word.
    - Current: `پایگاه%1$s`
    - Source: `{ <p> }The site at %1$s has been reported as an attack site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `پایگاه %1$s`
    - The rendered sentence needs a space between the word and the inserted URL.
- `mozac_browser_errorpages_safe_browsing_unwanted_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Misspelled relative construction "وبگاه‌ی" instead of "وبگاهی".
    - Current: `وبگاه‌ی که`
    - Source: `{ <p> }The site at %1$s has been reported as serving unwanted software and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `وبگاهی که`
    - The indefinite/relative ی attaches directly to the noun; a ZWNJ before ی here is a spelling error.
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing ZWNJ in "نمیتواند" and incorrect space in "نمی توانید".
    - Current: `نمیتواند نمایش داده شود`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `نمی‌تواند نمایش داده شود`
    - Persian negation prefix نمی requires a ZWNJ, not zero or a full space.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — The untranslated English abbreviation "e.g." is left inside the parentheses in addition to the Persian "مثلا", duplicating it.
    - Current: `قراردادی مثلا (e.g. { <q> }wxyz://{ </q> })`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `قراردادی (مثلاً { <q> }wxyz://{ </q> })`
    - The source has "(e.g., wxyz://)"; the translation both translates it as مثلا and keeps the English "e.g.", and misplaces the parenthesis.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "cookies required by this site" is rendered as "possible cookies" (کلوچک‌های احتمالی), and "not your device" as "not your computer".
    - Current: `آیا کلوچک‌های احتمالی مورد نیاز این وبگاه را غیرفعال ساخته‌اید؟`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `آیا کلوچک‌های مورد نیاز این وبگاه را غیرفعال ساخته‌اید؟`
    - The source says "cookies required by this site"; the added احتمالی ("possible") is not in the source.
- `mozac_compose_base_close_button_content_description` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-fa/strings.xml` — Trailing zero-width non-joiner after "بستن".
    - Current: `بستن‌`
    - Source: `Close`
    - Suggest: `بستن`
    - The Persian text ends with a stray ZWNJ character that has no function at the end of a word.
- `mozac_tab_counter_open_tab_tray_single` — `mozilla-mobile/android-components/components/compose/tabstray/src/main/res/values-fa/strings.xml` — Missing ZWNJ in "زبانه ها" (should be "زبانه‌ها"), inconsistent with the plural string.
    - Current: `زبانه ها`
    - Source: `1 open tab. Tap to switch tabs.`
    - Suggest: `زبانه‌ها`
    - Persian plural suffix -ها attaches with a zero-width non-joiner; the parallel string mozac_tab_counter_open_tab_tray_plural correctly uses "زبانه‌ها".
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "Failed to disable" is translated as "failed to enable", identical to the enable string.
    - Current: `شکست در فعالسازی %1$s`
    - Source: `Failed to disable %1$s`
    - Suggest: `شکست در غیرفعال‌سازی %1$s`
    - Source says "Failed to disable %1$s" but the target says failed to enable, reversing the action.
- `mozac_feature_addons_failed_to_remove` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the word and the placeholder.
    - Current: `شکست در حذف%1$s`
    - Source: `Failed to remove %1$s`
    - Suggest: `شکست در حذف %1$s`
    - The add-on name would be glued to the preceding word in the rendered text.
- `mozac_feature_addons_failed_to_enable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "فعالسازی" is missing the required ZWNJ (should be فعال‌سازی).
    - Current: `شکست در فعالسازی %1$s`
    - Source: `Failed to enable %1$s`
    - Suggest: `شکست در فعال‌سازی %1$s`
    - Persian orthography requires a zero-width non-joiner in the compound فعال‌سازی.
- `mozac_feature_addons_failed_to_translate` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Spelling error: "همچینین" should be "همچنین".
    - Current: `همچینین`
    - Source: `Translation not found, for locale %1$s neither default language %2$s`
    - Suggest: `همچنین`
    - Misspelling of the Persian word همچنین.
- `mozac_feature_addons_permissions_all_urls_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Adds "all" to the data being accessed, which the source does not say.
    - Current: `دسترسی به تمامی اطلاعات شما برای تمامی پایگاه های اینترنتی`
    - Source: `Access your data for all websites`
    - Suggest: `دسترسی به داده‌های شما برای همهٔ وب‌گاه‌ها`
    - Source is "Access your data for all websites"; "all" modifies websites, not the user's data, so the translation claims a broader permission scope.
- `mozac_feature_addons_enabled` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — State label "Enabled" rendered as a past-tense event "was enabled".
    - Current: `فعال شد`
    - Source: `Enabled`
    - Suggest: `فعال`
    - Developer comment says this indicates the add-on is enabled (a state), not that an action just occurred.
- `mozac_feature_addons_installed_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Section heading "Installed" rendered as the past-tense event "was installed".
    - Current: `نصب شد`
    - Source: `Installed`
    - Suggest: `نصب‌شده`
    - Per the developer comment this is a section label listing installed add-ons, not a completion message.
- `mozac_feature_addons_permissions_data_collection_searchTerms_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "search terms" is rendered as "شرایط جستجو" (search conditions/circumstances) instead of search keywords.
    - Current: `شرایط جستجو`
    - Source: `search terms`
    - Suggest: `عبارت‌های جست‌وجو`
    - In this context "terms" means the words/phrases the user searches for (عبارت‌ها/واژه‌های جست‌وجو), not "conditions" (شرایط).
- `mozac_feature_addons_permissions_data_collection_searchTerms_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "search terms" mistranslated as "شرایط جستجو" (search conditions).
    - Current: `هم‌رسانی شرایط جستجو با توسعه‌دهنده افزونه`
    - Source: `Share search terms with extension developer`
    - Suggest: `هم‌رسانی عبارت‌های جست‌وجو با توسعه‌دهنده افزونه`
    - "Search terms" refers to the queries the user types, not conditions/criteria; شرایط means conditions.
- `mozac_feature_addons_permissions_downloads_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Translation garbles the source: "Download files and read and modify the browser's download history" becomes "downloading the files of download history and setting and reading them".
    - Current: `دریافت پرونده‌های تاریخچه دریافت ها و تنظیم و خواندن آن ها`
    - Source: `Download files and read and modify the browser’s download history`
    - Suggest: `پرونده‌ها را دریافت کنید و تاریخچه دریافت مرورگر را بخوانید و تغییر دهید`
    - The source describes two separate capabilities (downloading files; reading and modifying the browser's download history); the target merges them into a different meaning and omits "browser's".
- `mozac_feature_addons_permissions_downloads_open_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "your device" is translated as "کامپیوتر شما" (your computer) and the phrase is ungrammatical.
    - Current: `بازکردن پرونده‌های دریافت ها بر روی کامپیوتر شما`
    - Source: `Open files downloaded to your device`
    - Suggest: `باز کردن پرونده‌های دریافت‌شده در دستگاه شما`
    - Source says "device" (دستگاه), not computer; this is an Android string. Also "پرونده‌های دریافت ها" is malformed compared with the parallel string which uses "پرونده‌های دریافت‌شده".
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space in "ابزارتوسعه‌دهندگان".
    - Current: `گسترش ابزارتوسعه‌دهندگان`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `گسترش ابزارهای توسعه‌دهندگان`
    - "ابزار" and "توسعه‌دهندگان" are run together without a space, producing a malformed word.
- `mozac_feature_addons_permissions_declarative_net_request_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Permission description rendered as an imperative command to the browser instead of a noun/gerund phrase like the parallel strings.
    - Current: `محتوا را در هر صفحه‌ای مسدود کن`
    - Source: `Block content on any page`
    - Suggest: `مسدود کردن محتوا در هر صفحه`
    - Other permission descriptions in the same dialog use the gerund form (e.g. "مسدود کردن محتوا در هر صفحه."); the informal imperative "مسدود کن" also breaks the locale's register.
- `mozac_feature_addons_rating_content_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Leftover English word "of" in the translation produces "از of 5".
    - Current: `رتبه‌بندی: %1$.02f از of 5`
    - Source: `Rating: %1$.02f out of 5`
    - Suggest: `رتبه‌بندی: %1$.02f از ۵`
    - Source is "Rating: %1$.02f out of 5"; the target duplicates the preposition, leaving an untranslated "of" that a screen reader will read aloud.
- `mozac_feature_addons_permissions_sites_in_domain_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — The possessive "your data" is lost: translation says "data of the sites" instead of "your data for sites in the %1$s domain".
    - Current: `دسترسی به داده‌های پایگاه‌ها در دامنهٔ %1$s`
    - Source: `Access your data for sites in the %1$s domain`
    - Suggest: `دسترسی به داده‌های شما در پایگاه‌های دامنهٔ %1$s`
    - Source grants access to the user's own data on sites in that domain; the target describes access to the sites' data, a different object.
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "browser activity" is rendered as just "activity", dropping "browser"; also missing ZWNJ in "فعالیت ها".
    - Current: `دسترسی به فعالیت ها در طی گشتن`
    - Source: `Access browser activity during navigation`
    - Suggest: `دسترسی به فعالیت مرورگر هنگام پیمایش`
    - Source says "Access browser activity during navigation"; the parallel _for_update string correctly uses "فعالیت مرورگر هنگام پیمایش".
- `mozac_feature_addons_permissions_sessions_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Ungrammatical relative clause and missing ezafe: "زبانه‌های که اخیرا بسته‌شده".
    - Current: `دسترسی به زبانه‌های که اخیرا بسته‌شده.`
    - Source: `Access recently closed tabs.`
    - Suggest: `دسترسی به زبانه‌هایی که اخیراً بسته شده‌اند.`
    - Persian requires the indefinite -yi marker (زبانه‌هایی) before the relative clause, and plural agreement; "اخیرا" also lacks the tanvin.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "themes" translated as "پوسته‌ها" here but as "زمینه‌ها" in the parallel non-update string.
    - Current: `پایش بر استفاده از افزونه و مدیریت پوسته‌ها.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `پایش استفادهٔ افزونه‌ها و مدیریت زمینه‌ها.`
    - mozac_feature_addons_permissions_management_description renders the same source "manage themes" as "مدیریت زمینه‌ها"; the two variants of the same permission text should be consistent.
- `mozac_feature_addons_status_incompatible` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — The translation drops the add-on name meaning and turns %1$s into a version, saying "%1$s is not compatible with your version %2$s" instead of "%1$s is not compatible with your version of %2$s".
    - Current: `%1$s با نگارش %2$s شما (نگارش %3$s) سازگار نیست.`
    - Source: `%1$s is not compatible with your version of %2$s (version %3$s).`
    - Suggest: `%1$s با نگارش شما از %2$s (نگارش %3$s) سازگار نیست.`
    - Per the comment, %2$s is the app name, not a version; the current word order reads "your version %2$s" and mislabels the app name as a version.
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "Updater Information" is rendered as "Updating information", reversing the head noun.
    - Current: `به‌روزرسانی اطلاعات`
    - Source: `Updater Information`
    - Suggest: `اطلاعات به‌روزرسان`
    - The source is a dialog title meaning information about the updater; the target reads as the action of updating the information.
- `mozac_feature_addons_updater_dialog_last_attempt` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing colon after the label, which is followed by the date per the developer comment.
    - Current: `آخرین تلاش`
    - Source: `Last attempt:`
    - Suggest: `آخرین تلاش:`
    - Source is "Last attempt:" and the comment states it is followed by the date; the colon was dropped, unlike the parallel "وضعیت:" string.
- `mozac_feature_addons_user_rating_count_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space after the colon before the placeholder.
    - Current: `بررسی‌های:%1$s`
    - Source: `Reviews: %1$s`
    - Suggest: `بررسی‌ها: %1$s`
    - Source "Reviews: %1$s" has a space after the colon; the target also uses an incorrect ezafe form "بررسی‌های".
- `mozac_feature_addons_successfully_installed` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the placeholder and the following word.
    - Current: `%1$sبا موفقیت نصب شد`
    - Source: `Successfully installed %1$s`
    - Suggest: `%1$s با موفقیت نصب شد`
    - The add-on name will run into the next word with no separating space.
- `mozac_feature_addons_successfully_removed` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the placeholder and the following word.
    - Current: `%1$sبا موفقیت حذف شد`
    - Source: `Successfully removed %1$s`
    - Suggest: `%1$s با موفقیت حذف شد`
    - The add-on name will run into the next word with no separating space.
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Present tense "cannot be verified" used where the source states it could not be verified (past).
    - Current: `%1$s نمی‌تواند به عنوان امن تأیید شود و غیرفعال شده است.`
    - Source: `%1$s could not be verified as secure and has been disabled.`
    - Suggest: `امنیت %1$s قابل تأیید نبود و غیرفعال شده است.`
    - Source is "could not be verified as secure and has been disabled"; the Persian present tense mismatches the completed action.
- `mozac_feature_autofill_search_hint` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-fa/strings.xml` — "Search logins" is rendered with a nonsensical term and a spacing error instead of the established Persian term for logins (ورودها/اطلاعات ورود).
    - Current: `جست‌وجو در واردشده ها`
    - Source: `Search logins`
    - Suggest: `جست‌وجوی ورودها`
    - "واردشده ها" ("imported/entered ones") is not the term for saved logins, and the detached "ها" should be joined (واردشده‌ها); the source means searching saved logins.
- `mozac_feature_contextmenu_open_link_in_external_app` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — "external app" rendered as "کاره‌ای دیگر", inconsistent with "برنامه" used for app elsewhere in the same surface.
    - Current: `گشودن پیوند در کاره‌ای دیگر`
    - Source: `Open link in external app`
    - Suggest: `گشودن پیوند در برنامهٔ بیرونی`
    - The same term "app" is translated "برنامه" in neighbouring strings (e.g. mozac_feature_applinks_normal_confirm_dialog_title, mozac_feature_customtabs_exit_button); "کاره" is an obscure coinage and inconsistent.
- `mozac_selection_context_menu_search_privately_2` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — "Private Search" rendered as "جست‌وجوی ناشناس" (anonymous search) instead of the established term for private (خصوصی).
    - Current: `جست‌وجوی ناشناس`
    - Source: `Private Search`
    - Suggest: `جست‌وجوی خصوصی`
    - Elsewhere in the same file "private tab" is translated "زبانهٔ خصوصی"; using "ناشناس" here is inconsistent terminology for the Private browsing feature.
- `mozac_feature_downloads_again_dialog_title_with_unknown_size` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — The confirmation title is rendered in first person ("Shall I download the file again?") instead of the neutral "Download file again?" used in the sibling string.
    - Current: `دوباره پرونده را بارگیری کنم؟`
    - Source: `Download file again?`
    - Suggest: `دریافت دوبارهٔ پرونده؟`
    - The source is an impersonal dialog title; the parallel string mozac_feature_downloads_again_dialog_title uses "دریافت دوبارهٔ پرونده؟". The first-person verb also breaks consistency with the other download dialog titles.
- `mozac_feature_downloads_write_external_storage_permissions_needed_message` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — Spelling error: "تنطیمات" should be "تنظیمات".
    - Current: `تنطیمات اندروید`
    - Source: `Files and media permission access needed to download files. Go to Android settings, tap permissions, and tap allow.`
    - Suggest: `تنظیمات اندروید`
    - "تنظیمات" (settings) is misspelled with ط instead of ظ.
- `mozac_feature_downloads_unable_to_open_third_party_app` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — "نتوانست %1$s را باز کند" adds a third-person past subject not present in the impersonal source "Unable to open %1$s".
    - Current: `نتوانست %1$s را باز کند`
    - Source: `Unable to open %1$s`
    - Suggest: `امکان باز کردن %1$s نبود`
    - The source is impersonal; the Persian implies an unnamed third party failed to open it, which is ungrammatical without a subject.
- `mozac_feature_media_sharing_camera_and_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fa/strings.xml` — "Camera and microphone are on" is rendered with "وصل هستند" (are connected) and "صدابَر" instead of the consistent "میکروفون"/"روشن است" used elsewhere.
    - Current: `دوربین و صدابَر وصل هستند`
    - Source: `Camera and microphone are on`
    - Suggest: `دوربین و میکروفون روشن هستند`
    - The source says "are on", and the sibling string mozac_feature_media_sharing_camera correctly uses "روشن است"; also all other media-sharing strings use "میکروفون" for microphone, making "صدابَر" inconsistent on the same surface.
- `mozac_feature_media_sharing_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fa/strings.xml` — "Microphone is on" rendered as "صدابَر وصل است" (the sound device is connected), inconsistent with "میکروفون" and "روشن است" used in the neighbouring strings.
    - Current: `صدابَر وصل است`
    - Source: `Microphone is on`
    - Suggest: `میکروفون روشن است`
    - The related notification texts all use "میکروفون", and the parallel camera title uses "روشن است" for "is on"; "وصل است" means "is connected", not "is on".
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "می خواهید" is missing the required zero-width non-joiner (should be "می‌خواهید").
    - Current: `می خواهید این پایگاه را ترک کنید؟`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `می‌خواهید این پایگاه را ترک کنید؟`
    - Persian orthography requires the prefix "می" to be joined with ZWNJ, as done consistently elsewhere in this file (e.g. "استفاده می‌کند").
- `mozac_feature_prompt_repost_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — The source's "twice" / duplication of recent actions such as "sending a payment or posting a comment" is rendered so that the payment/comment itself is repeated, and "دوباره تکرار کند" is redundant.
    - Current: `می‌تواند کنش‌های اخیر مانند پرداخت یا ارسال نظر را دوباره تکرار کند`
    - Source: `Refreshing this page could duplicate recent actions, such as sending a payment or posting a comment twice.`
    - Suggest: `می‌تواند کنش‌های اخیر، مانند فرستادن یک پرداخت یا ارسال یک نظر، را دو بار تکرار کند`
    - The English warns the action could be duplicated (done twice); the translation's "دوباره تکرار کند" is a pleonasm and loses "twice".
- `mozac_feature_prompt_update_confirmation` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — Trailing stray zero-width non-joiner after "به‌روزرسانی".
    - Current: `به‌روزرسانی‌`
    - Source: `Update`
    - Suggest: `به‌روزرسانی`
    - The button label ends with an extraneous ZWNJ character not present in the equivalent strings (e.g. mozac_feature_prompt_login_update_headline_2).
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "additional dialogs" is rendered as "new windows" (پنجره‌های جدید) instead of dialogs.
    - Current: `از ایجاد پنجره‌های جدید توسط این صفحه جلوگیری شود.`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `از ایجاد محاوره‌های بیشتر توسط این صفحه جلوگیری شود`
    - The source refers to additional dialogs, not new windows; the neighbouring strings use separate wording for windows. Also a trailing period was added that the source lacks.
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "login provider" is rendered as just "provider", dropping "login".
    - Current: `استفاده از %1$s به عنوان یک فراهم‌کننده`
    - Source: `Use %1$s as a login provider`
    - Suggest: `استفاده از %1$s به عنوان یک فراهم‌کنندهٔ ورود`
    - The source says "as a login provider"; the qualifier "login" is dropped, unlike the sibling string mozac_feature_prompts_identity_credentials_choose_provider which keeps فراهم‌کنندهٔ ورود.
- `mozac_feature_prompts_sep` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — The abbreviated month name "Sep" is rendered with the full month name, contrary to the comment requesting a short description.
    - Current: `سپتامبر`
    - Source: `Sep`
    - Suggest: `سپتا`
    - Developer comment specifies "September month of the year (short description)" used in a compact month chooser; the target uses the full form.
- `mozac_feature_readerview_sephia` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fa/strings.xml` — "Sepia" is misspelled in Persian as سوبیایی instead of سپیا/سپیایی.
    - Current: `سوبیایی`
    - Source: `Sepia`
    - Suggest: `سپیا`
    - The color Sepia is rendered سپیا in Persian; سوبیایی is not a word and appears to be a transliteration error.
- `mozac_feature_readerview_sepia_color_scheme_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fa/strings.xml` — "Sepia" is misspelled in Persian as سوبیایی instead of سپیا.
    - Current: `طرح رنگی سوبیایی`
    - Source: `Sepia color scheme`
    - Suggest: `طرح رنگی سپیا`
    - Same misspelling of the color name Sepia as in mozac_feature_readerview_sephia.
- `mozac_feature_sitepermissions_notification_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fa/strings.xml` — Typo: «اجاره» (rent) instead of «اجازه» (permission).
    - Current: `اجاره می‌دهید`
    - Source: `Allow %1$s to send notifications?`
    - Suggest: `اجازه می‌دهید`
    - The source says "Allow %1$s to send notifications?"; «اجاره دادن» means "to rent", a spelling error for «اجازه».
- _…and 79 more._

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
| Files | 39 |
| Strings | 2,594 |
| Missing strings | 152 |
| Obsolete strings | 0 |
| Files absent from the locale | 5 |
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

**152 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — 61
- `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — 31
- `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-fa/strings.xml` — 11
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — 7
- `mozilla-mobile/android-components/components/compose/base/src/main/res/values-fa/strings.xml` — 6
- `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — 6
- `mozilla-mobile/fenix/app/longfox/src/main/res/values-fa/strings.xml` — 6
- `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-fa/strings.xml` — 4
- `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values/strings.xml` — 4
- `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values/strings.xml` — 4
- `mozilla-mobile/android-components/components/feature/importer/src/main/res/values/strings.xml` — 3
- `mozilla-mobile/android-components/components/feature/password-importer/src/main/res/values/strings.xml` — 3

**Files absent from the locale:**

- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values/strings.xml`
- `mozilla-mobile/android-components/components/feature/importer/src/main/res/values/strings.xml`
- `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values/strings.xml`
- `mozilla-mobile/android-components/components/feature/password-importer/src/main/res/values/strings.xml`
- `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values/strings.xml`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 16 | **guillemet** |
| ellipsis | `char` 21 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (139)

> **Reads as a deliberate edit (8).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — First paragraph translates the net-interrupt message instead of "The network link was interrupted while negotiating a connection."
    - Current: `مرورگر با موفقیت متصل شد ، اما هنگام انتقال اطلاعات ، اتصال قطع شد. لطفا دوباره امتحان کنید.`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `پیوند شبکه در هنگام برقراری اتّصال قطع شد. لطفاً دوباره تلاش کنید.`
    - The source says the network link was interrupted while negotiating a connection; the target claims the browser connected successfully and the connection dropped while transferring information (text copied from the net_interrupt string).
- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "The connection was reset" is rendered as "the connection was re-established", reversing the meaning of the error.
    - Current: `اتصال از نو برقرار شد`
    - Source: `The connection was reset`
    - Suggest: `اتصال بازنشانی شد`
    - The source reports a connection reset error (failure); the target says the connection was successfully re-established, the opposite of an error condition.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "Incorrect settings can interfere with Web browsing" rendered as a certainty ("prevents Web browsing").
    - Current: `تنظیمات نادرست آن مانع از مرور وب می‌شود.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `تنظیمات نادرست می‌تواند در مرور وب اختلال ایجاد کند.`
    - The source hedges with "can interfere"; the target asserts that incorrect settings do prevent Web browsing.
- `mozac_feature_addons_permissions_all_urls_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Adds "all" to the data being accessed, which the source does not say.
    - Current: `دسترسی به تمامی اطلاعات شما برای تمامی پایگاه های اینترنتی`
    - Source: `Access your data for all websites`
    - Suggest: `دسترسی به داده‌های شما برای همهٔ وب‌گاه‌ها`
    - Source is "Access your data for all websites"; "all" modifies websites, not the user's data, so the translation claims a broader permission scope.
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The translation adds "at random" which the source does not say.
    - Current: `یکی از آن‌ها را به‌صورت تصادفی برای استفادهٔ مجدد انتخاب کردیم`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `یکی از آن‌ها را برای استفادهٔ مجدد برایتان انتخاب کردیم`
    - Source: "so we picked one for you to reuse" — there is no statement that the pick was random; the translation asserts a random selection behaviour of the product.
- `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "private" is rendered as "امن" (secure/safe) instead of "خصوصی" (private).
    - Current: `‏Firefox سریع و امن است`
    - Source: `Firefox is fast and private`
    - Suggest: `‏Firefox سریع و خصوصی است`
    - The source says Firefox is fast and private; the translation claims it is fast and secure, a different property claim about the product.
- `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Singular "Tab's browsing history" rendered as plural "tabs of the browser".
    - Current: `تاریخچه زبانه‌های مرورگر پاک شده است.`
    - Source: `Tab’s browsing history has been erased.`
    - Suggest: `تاریخچهٔ مرور زبانه پاک شده است.`
    - The source refers to a single custom tab's browsing history; the translation says the history of the browser's tabs (plural), widening the scope of what was erased.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "we never save and cannot restore this tab" rendered as "we cannot save and restore this tab", losing the "never save" assertion.
    - Current: `به عنوان یک مرورگر خصوصی نمی توانیم این زبانه را ذخیره و بازیابی کنیم.`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `به عنوان یک مرورگر خصوصی، ما هرگز این زبانه را ذخیره نمی‌کنیم و نمی‌توانیم آن را بازیابی کنیم.`
    - The source distinguishes a deliberate policy (never save) from an inability (cannot restore); the translation states only inability, changing what the product says about its own behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 62 |
| 3 | Degraded language (grammar, spelling, terminology) | 64 |
| 4 | Cosmetic (typography, spacing) | 13 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Third bullet asks about access permissions to the "address" instead of to the requested item.
    - Current: `آیا مجوزهای دسترسی کافی برای دست‌یابی به این نشانی را دارید؟`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `آیا مجوزهای دسترسی کافی برای دست‌یابی به مورد درخواستی را دارید؟`
    - The source asks about sufficient access permissions to the requested item, not to the address.
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "invalid" form of compression rendered as "ناشناخته" (unknown).
    - Current: `از گونه‌ای ناشناخته یا پشتیبانی نشده از فشرده‌سازی استفاده می‌کند`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `از گونه‌ای نامعتبر یا پشتیبانی‌نشده از فشرده‌سازی استفاده می‌کند`
    - The source says the compression form is invalid or unsupported, not unknown.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — First paragraph translates the net-interrupt message instead of "The network link was interrupted while negotiating a connection."
    - Current: `مرورگر با موفقیت متصل شد ، اما هنگام انتقال اطلاعات ، اتصال قطع شد. لطفا دوباره امتحان کنید.`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `پیوند شبکه در هنگام برقراری اتّصال قطع شد. لطفاً دوباره تلاش کنید.`
    - The source says the network link was interrupted while negotiating a connection; the target claims the browser connected successfully and the connection dropped while transferring information (text copied from the net_interrupt string).
- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "The connection was reset" is rendered as "the connection was re-established", reversing the meaning of the error.
    - Current: `اتصال از نو برقرار شد`
    - Source: `The connection was reset`
    - Suggest: `اتصال بازنشانی شد`
    - The source reports a connection reset error (failure); the target says the connection was successfully re-established, the opposite of an error condition.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "Incorrect settings can interfere with Web browsing" rendered as a certainty ("prevents Web browsing").
    - Current: `تنظیمات نادرست آن مانع از مرور وب می‌شود.`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `تنظیمات نادرست می‌تواند در مرور وب اختلال ایجاد کند.`
    - The source hedges with "can interfere"; the target asserts that incorrect settings do prevent Web browsing.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "device" translated as "رایانه" (computer) in a mobile component string.
    - Current: `آیا رایانه به یک شبکهٔ فعال متصل است؟`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `آیا افزاره به یک شبکهٔ فعال متصل است؟`
    - The source asks about the device; "رایانه" names a computer, which is wrong on an Android device and inconsistent with other strings that use دستگاه/افزاره.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "cookies required by this site" is rendered as "possible cookies" (کلوچک‌های احتمالی), and "not your device" as "not your computer".
    - Current: `آیا کلوچک‌های احتمالی مورد نیاز این وبگاه را غیرفعال ساخته‌اید؟`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `آیا کلوچک‌های مورد نیاز این وبگاه را غیرفعال ساخته‌اید؟`
    - The source says "cookies required by this site"; the added احتمالی ("possible") is not in the source.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "potentially harmful site" is rendered as "attack site" (تهاجمی), duplicating the malware string instead of translating this one.
    - Current: `پایگاه%1$s به عنوان یک وب‌گاه تهاجمی گزارش شده و بر اساس ترجیحات امنیتی شما مسدود شده است.`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `پایگاه %1$s به عنوان یک وب‌گاه بالقوه زیان‌آور گزارش شده و بر اساس ترجیحات امنیتی شما مسدود شده است.`
    - The source says "reported as a potentially harmful site", not "attack site"; the title of this same error page correctly uses زیان‌آور.
- `mozac_browser_errorpages_unknown_protocol_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — "Unknown Protocol" is translated as "the address was not understandable" instead of referring to the protocol.
    - Current: `نشانی قابل فهم نبود`
    - Source: `Unknown Protocol`
    - Suggest: `قرارداد ناشناخته`
    - The source names an unknown protocol; the translation says the address was unintelligible, and the body text of the same page uses قرارداد for protocol.
- `mozac_feature_addons_enabled` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — State label "Enabled" rendered as a past-tense event "was enabled".
    - Current: `فعال شد`
    - Source: `Enabled`
    - Suggest: `فعال`
    - Developer comment says this indicates the add-on is enabled (a state), not that an action just occurred.
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "Failed to disable" is translated as "failed to enable", identical to the enable string.
    - Current: `شکست در فعالسازی %1$s`
    - Source: `Failed to disable %1$s`
    - Suggest: `شکست در غیرفعال‌سازی %1$s`
    - Source says "Failed to disable %1$s" but the target says failed to enable, reversing the action.
- `mozac_feature_addons_installed_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Section heading "Installed" rendered as the past-tense event "was installed".
    - Current: `نصب شد`
    - Source: `Installed`
    - Suggest: `نصب‌شده`
    - Per the developer comment this is a section label listing installed add-ons, not a completion message.
- `mozac_feature_addons_permissions_all_urls_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Adds "all" to the data being accessed, which the source does not say.
    - Current: `دسترسی به تمامی اطلاعات شما برای تمامی پایگاه های اینترنتی`
    - Source: `Access your data for all websites`
    - Suggest: `دسترسی به داده‌های شما برای همهٔ وب‌گاه‌ها`
    - Source is "Access your data for all websites"; "all" modifies websites, not the user's data, so the translation claims a broader permission scope.
- `mozac_feature_addons_permissions_data_collection_searchTerms_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "search terms" mistranslated as "شرایط جستجو" (search conditions).
    - Current: `هم‌رسانی شرایط جستجو با توسعه‌دهنده افزونه`
    - Source: `Share search terms with extension developer`
    - Suggest: `هم‌رسانی عبارت‌های جست‌وجو با توسعه‌دهنده افزونه`
    - "Search terms" refers to the queries the user types, not conditions/criteria; شرایط means conditions.
- `mozac_feature_addons_permissions_data_collection_searchTerms_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "search terms" is rendered as "شرایط جستجو" (search conditions/circumstances) instead of search keywords.
    - Current: `شرایط جستجو`
    - Source: `search terms`
    - Suggest: `عبارت‌های جست‌وجو`
    - In this context "terms" means the words/phrases the user searches for (عبارت‌ها/واژه‌های جست‌وجو), not "conditions" (شرایط).
- `mozac_feature_addons_permissions_downloads_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Translation garbles the source: "Download files and read and modify the browser's download history" becomes "downloading the files of download history and setting and reading them".
    - Current: `دریافت پرونده‌های تاریخچه دریافت ها و تنظیم و خواندن آن ها`
    - Source: `Download files and read and modify the browser’s download history`
    - Suggest: `پرونده‌ها را دریافت کنید و تاریخچه دریافت مرورگر را بخوانید و تغییر دهید`
    - The source describes two separate capabilities (downloading files; reading and modifying the browser's download history); the target merges them into a different meaning and omits "browser's".
- `mozac_feature_addons_permissions_downloads_open_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "your device" is translated as "کامپیوتر شما" (your computer) and the phrase is ungrammatical.
    - Current: `بازکردن پرونده‌های دریافت ها بر روی کامپیوتر شما`
    - Source: `Open files downloaded to your device`
    - Suggest: `باز کردن پرونده‌های دریافت‌شده در دستگاه شما`
    - Source says "device" (دستگاه), not computer; this is an Android string. Also "پرونده‌های دریافت ها" is malformed compared with the parallel string which uses "پرونده‌های دریافت‌شده".
- `mozac_feature_addons_permissions_sites_in_domain_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — The possessive "your data" is lost: translation says "data of the sites" instead of "your data for sites in the %1$s domain".
    - Current: `دسترسی به داده‌های پایگاه‌ها در دامنهٔ %1$s`
    - Source: `Access your data for sites in the %1$s domain`
    - Suggest: `دسترسی به داده‌های شما در پایگاه‌های دامنهٔ %1$s`
    - Source grants access to the user's own data on sites in that domain; the target describes access to the sites' data, a different object.
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "browser activity" is rendered as just "activity", dropping "browser"; also missing ZWNJ in "فعالیت ها".
    - Current: `دسترسی به فعالیت ها در طی گشتن`
    - Source: `Access browser activity during navigation`
    - Suggest: `دسترسی به فعالیت مرورگر هنگام پیمایش`
    - Source says "Access browser activity during navigation"; the parallel _for_update string correctly uses "فعالیت مرورگر هنگام پیمایش".
- `mozac_feature_addons_status_incompatible` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — The translation drops the add-on name meaning and turns %1$s into a version, saying "%1$s is not compatible with your version %2$s" instead of "%1$s is not compatible with your version of %2$s".
    - Current: `%1$s با نگارش %2$s شما (نگارش %3$s) سازگار نیست.`
    - Source: `%1$s is not compatible with your version of %2$s (version %3$s).`
    - Suggest: `%1$s با نگارش شما از %2$s (نگارش %3$s) سازگار نیست.`
    - Per the comment, %2$s is the app name, not a version; the current word order reads "your version %2$s" and mislabels the app name as a version.
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "Updater Information" is rendered as "Updating information", reversing the head noun.
    - Current: `به‌روزرسانی اطلاعات`
    - Source: `Updater Information`
    - Suggest: `اطلاعات به‌روزرسان`
    - The source is a dialog title meaning information about the updater; the target reads as the action of updating the information.
- `mozac_feature_downloads_again_dialog_title_with_unknown_size` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — The confirmation title is rendered in first person ("Shall I download the file again?") instead of the neutral "Download file again?" used in the sibling string.
    - Current: `دوباره پرونده را بارگیری کنم؟`
    - Source: `Download file again?`
    - Suggest: `دریافت دوبارهٔ پرونده؟`
    - The source is an impersonal dialog title; the parallel string mozac_feature_downloads_again_dialog_title uses "دریافت دوبارهٔ پرونده؟". The first-person verb also breaks consistency with the other download dialog titles.
- `mozac_feature_media_sharing_camera_and_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fa/strings.xml` — "Camera and microphone are on" is rendered with "وصل هستند" (are connected) and "صدابَر" instead of the consistent "میکروفون"/"روشن است" used elsewhere.
    - Current: `دوربین و صدابَر وصل هستند`
    - Source: `Camera and microphone are on`
    - Suggest: `دوربین و میکروفون روشن هستند`
    - The source says "are on", and the sibling string mozac_feature_media_sharing_camera correctly uses "روشن است"; also all other media-sharing strings use "میکروفون" for microphone, making "صدابَر" inconsistent on the same surface.
- `mozac_feature_prompt_repost_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — The source's "twice" / duplication of recent actions such as "sending a payment or posting a comment" is rendered so that the payment/comment itself is repeated, and "دوباره تکرار کند" is redundant.
    - Current: `می‌تواند کنش‌های اخیر مانند پرداخت یا ارسال نظر را دوباره تکرار کند`
    - Source: `Refreshing this page could duplicate recent actions, such as sending a payment or posting a comment twice.`
    - Suggest: `می‌تواند کنش‌های اخیر، مانند فرستادن یک پرداخت یا ارسال یک نظر، را دو بار تکرار کند`
    - The English warns the action could be duplicated (done twice); the translation's "دوباره تکرار کند" is a pleonasm and loses "twice".
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "login provider" is rendered as just "provider", dropping "login".
    - Current: `استفاده از %1$s به عنوان یک فراهم‌کننده`
    - Source: `Use %1$s as a login provider`
    - Suggest: `استفاده از %1$s به عنوان یک فراهم‌کنندهٔ ورود`
    - The source says "as a login provider"; the qualifier "login" is dropped, unlike the sibling string mozac_feature_prompts_identity_credentials_choose_provider which keeps فراهم‌کنندهٔ ورود.
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "additional dialogs" is rendered as "new windows" (پنجره‌های جدید) instead of dialogs.
    - Current: `از ایجاد پنجره‌های جدید توسط این صفحه جلوگیری شود.`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `از ایجاد محاوره‌های بیشتر توسط این صفحه جلوگیری شود`
    - The source refers to additional dialogs, not new windows; the neighbouring strings use separate wording for windows. Also a trailing period was added that the source lacks.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fa/strings.xml` — Mistranslation: the source asks the user to allow notifications in the app, not to let the app receive them.
    - Current: `باید به %1$s اجازه دهید آنها را دریافت کند`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `باید آگاه‌سازی‌ها را در %1$s مجاز کنید`
    - en-US: "You’ll need to allow notifications in %1$s" — %1$s is the app where notifications must be enabled, not an entity granted permission to receive them.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-fa/strings.xml` — Adds "کاملاً" (completely), an intensifier absent from the source claim about user control.
    - Current: `کاملاً در کنترل خودتان باقی می‌مانند`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `در کنترل خودتان باقی می‌مانند`
    - The en-US says summaries "stay in your control"; "کاملاً" asserts complete control, which the source does not claim.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-fa/strings.xml` — "Setting up summaries" is rendered as "preparing the summarizer" instead of "summaries".
    - Current: `در حال آماده‌سازی خلاصه‌ساز`
    - Source: `Setting up summaries`
    - Suggest: `در حال آماده‌سازی خلاصه‌ها`
    - The source refers to setting up summaries (plural noun), not a tool called a "summarizer"; the sibling title string mozac_summarize_download_consent_title uses خلاصه‌های خصوصی.
- `alternative_app_icon_option_cuddling` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Cuddling" is rendered as the verbal action "embracing/hugging" rather than an adjectival icon-style name.
    - Current: `در آغوش کشیدن`
    - Source: `Cuddling`
    - Suggest: `بغلی`
    - The string is an icon variant name describing a cute, cuddly design; the Persian infinitive phrase "در آغوش کشیدن" (the act of hugging someone) reads as an action label, not a style name, and is inconsistent with the other adjective-style icon names in this group.
- `alternative_app_icon_option_pride` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Pride" (LGBTQ+ Pride) is transliterated as «پراید», which in Persian denotes the Kia Pride car, not the concept of pride.
    - Current: `پراید`
    - Source: `Pride`
    - Suggest: `افتخار`
    - The developer comment states the icon supports the LGBTQ+ community; «پراید» is universally read in Persian as the car brand Pride, conveying the wrong meaning.
- `automatic_translation_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Please check back later" is rendered as "please try again later".
    - Current: `لطفاً بعداً دوباره امتحان کنید.`
    - Source: `Couldn’t load languages. Please check back later.`
    - Suggest: `لطفاً بعداً دوباره سر بزنید.`
    - The source asks the user to check back later, not to retry the action.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "translate sites in this language" is rendered as translating sites *into* this language, reversing the direction.
    - Current: `هرگز ترجمهٔ سایت‌ها به این زبان را پیشنهاد نخواهد داد`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `هرگز ترجمهٔ سایت‌های این زبان را پیشنهاد نخواهد داد`
    - The source means sites written in this language; «به این زبان» means translating into this language, the opposite direction.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "translate sites in this language" is rendered as translating sites *into* this language, reversing the direction.
    - Current: `ترجمهٔ سایت‌ها به این زبان را پیشنهاد خواهد داد`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `ترجمهٔ سایت‌های این زبان را پیشنهاد خواهد داد`
    - The source refers to sites written in this language; «به این زبان» states the target language of translation instead.
- `awesomebar_clipboard_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Fill link from clipboard" translated as "Paste link from clipboard".
    - Current: `جای‌گذاری پیوند از کلیپ‌بورد`
    - Source: `Fill link from clipboard`
    - Suggest: `پر کردن پیوند از کلیپ‌بورد`
    - The button fills the search field with the clipboard link; «جای‌گذاری» is "paste", a different action term.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Close custom tab menu sheet" is rendered with the modifiers reordered, yielding "sheet of the custom tab's menu" instead of "custom tab menu sheet".
    - Current: `بستن برگهٔ منوی زبانهٔ سفارشی`
    - Source: `Close custom tab menu sheet`
    - Suggest: `بستن برگهٔ منوی زبانهٔ سفارشی (بستن صفحهٔ منوی زبانهٔ سفارشی)`
    - The term برگه duplicates the word used for "tab" elsewhere, making the description ambiguous for screen-reader users.
- `browser_menu_no_extensions_installed_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Translation adds "yet" (هنوز), which the source does not say.
    - Current: `هنوز هیچ افزونه‌ای فعال نیست`
    - Source: `No extensions enabled`
    - Suggest: `هیچ افزونه‌ای فعال نیست`
    - Source is simply "No extensions enabled"; "هنوز" (yet) is an addition not present in the English.
- `close_tab_and_delete_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Close tab" rendered as "close the last tab", adding "last" which the visible source does not say.
    - Current: `آخرین زبانه بسته شده و گروه حذف شود؟`
    - Source: `Close tab and delete group?`
    - Suggest: `زبانه بسته شده و گروه حذف شود؟`
    - Source title is "Close tab and delete group?"; the translation adds "آخرین" (the last), which appears only in the internal developer description, not in the user-facing text.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The conditional clause is reversed: the source says protect payment methods from being accessed if someone else has your device, but the target says they stay safe "in case others access the device".
    - Current: `تا در صورت دسترسی دیگران به دستگاه، ایمن بمانند`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `تا اگر دستگاهتان دست شخص دیگری افتاد، کسی به آن‌ها دسترسی نداشته باشد`
    - en-US: "to protect your saved payment methods from being accessed if someone else has your device." The Persian rendering says the methods "remain safe in the event others access the device", which confuses the condition (someone else having the device) with the outcome being prevented (access to the payment data).
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "locale" rendered as "زبان" (language) instead of locale/regional setting.
    - Current: `افزودن نشانی جدید برای زبان انتخابی`
    - Source: `Add new address for selected locale`
    - Suggest: `افزودن نشانی جدید برای محلی انتخابی`
    - The developer comment and the Addresses debug tool refer to a locale (language+region combination used for address formats), not just a language.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Debug locales" translated as "زبان‌های اشکال‌زدایی" (debug languages).
    - Current: `زبان‌های اشکال‌زدایی برای فعال‌سازی`
    - Source: `Debug locales to enable`
    - Suggest: `محلی‌های اشکال‌زدایی برای فعال‌سازی`
    - The source says locales, not languages; the comment describes a list of debug locales that can be enabled/disabled.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "all languages" is translated as "all tabs" (زبانه‌ها) instead of "all languages" (زبان‌ها).
    - Current: `در صورت حذف تمام زبانه‌ها`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `در صورت حذف تمام زبان‌ها`
    - The source says "If you delete all languages"; زبانه means tab, not language. The sibling title string correctly uses زبان‌ها.
- `download_languages_item_content_description_delete_in_progress_state` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Generic "In progress" rendered as "deleting" specific wording.
    - Current: `در حال حذف`
    - Source: `In progress`
    - Suggest: `در حال انجام`
    - The source string is simply "In progress"; the translation states "deleting in progress", adding content not in the source (though the comment mentions deletion context).
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The translation adds "at random" which the source does not say.
    - Current: `یکی از آن‌ها را به‌صورت تصادفی برای استفادهٔ مجدد انتخاب کردیم`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `یکی از آن‌ها را برای استفادهٔ مجدد برایتان انتخاب کردیم`
    - Source: "so we picked one for you to reuse" — there is no statement that the pick was random; the translation asserts a random selection behaviour of the product.
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Suspected Fingerprinters" (the actors/trackers) is rendered as "suspected fingerprintings" (the activity).
    - Current: `انگشت‌نگاری‌های مشکوک`
    - Source: `Suspected Fingerprinters`
    - Suggest: `انگشت‌نگارهای مشکوک`
    - The category names the trackers themselves, as the description string correctly renders with «ابزارهای مشکوک به انگشت‌نگاری»; the title names an activity instead.
- `exit_fullscreen_with_gesture_short` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The gesture-navigation instruction is rendered as pressing back rather than using the back gesture, making it identical to the button-navigation string.
    - Current: `برای خروج، از بالا به پایین بکشید و بازگشت بزنید`
    - Source: `Drag from top & use back gesture to exit`
    - Suggest: `برای خروج، از بالا به پایین بکشید و از اشارهٔ بازگشت استفاده کنید`
    - Source says "use back gesture to exit" (gesture navigation), while the fa says press back, duplicating exit_fullscreen_with_back_button_short and giving the wrong instruction.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The notification title renders "%1$s tabs closed" as "tabs closed in %1$s", turning the app name into a location instead of the subject of the count.
    - Current: `زبانه‌های بسته‌شده در %1$s: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `زبانه‌های بسته‌شدهٔ %1$s: %2$d`
    - Per the comment, %1$s is the app name and %2$d is the number of tabs closed; the source reads "%1$s tabs closed: %2$d", not "tabs closed in %1$s".
- `ip_protection_data_limit_reached_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Access resets next month" translated as "دسترسی ... مجدداً شارژ می‌شود" (access is recharged), and "دیتا" used instead of the consistent term "داده".
    - Current: `سهمیهٔ دیتای VPN خود را استفاده کرده‌اید. دسترسی ماه آینده مجدداً شارژ می‌شود.`
    - Source: `You’ve used all %1$d GB of your VPN data. Access resets next month.`
    - Suggest: `سهمیهٔ دادهٔ VPN خود را استفاده کرده‌اید. دسترسی ماه آینده بازنشانی می‌شود.`
    - Other strings render "data" as "داده" and "reset" as "بازنشانی"; "دیتا" and "شارژ" are inconsistent loanwords and "شارژ" implies a top-up/payment not in the source.
- `ip_protection_menu_limit_reached` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "limit reached" rendered as "سقف ... به پایان رسید" (the limit has ended/expired) instead of the limit being reached.
    - Current: `سقف %1$d گیگابایت به پایان رسید`
    - Source: `%1$d GB limit reached`
    - Suggest: `به سقف %1$d گیگابایت رسیدید`
    - The source says the user has reached the %1$d GB limit; "سقف ... به پایان رسید" says the limit itself ended, which is not the source meaning.
- `microsurvey_describe_your_experience_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Which best describes your experience" is rendered as "describes your experience better", losing the superlative selection sense.
    - Current: `کدام گزینه تجربهٔ شما را تا کنون بهتر توصیف می‌کند؟`
    - Source: `Help us improve Firefox. Which best describes your experience so far?`
    - Suggest: `کدام گزینه تجربهٔ شما را تا کنون بهترین توصیف می‌کند؟`
    - The source asks which option best describes the experience; the Persian comparative «بهتر» changes it to a comparison with something unspecified.
- `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "private" is rendered as "امن" (secure/safe) instead of "خصوصی" (private).
    - Current: `‏Firefox سریع و امن است`
    - Source: `Firefox is fast and private`
    - Suggest: `‏Firefox سریع و خصوصی است`
    - The source says Firefox is fast and private; the translation claims it is fast and secure, a different property claim about the product.
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "the channels where we promote Firefox" is rendered as "our advertising channels", dropping the relation to promoting Firefox.
    - Current: `کانال‌های تبلیغاتی ما`
    - Source: `You can help us reach more people by allowing Mozilla to inform the channels where we promote Firefox that you’re a Firefox user.`
    - Suggest: `کانال‌هایی که در آن‌ها Firefox را تبلیغ می‌کنیم`
    - The source specifies the channels where Mozilla promotes Firefox; the translation says generically "our advertising channels".
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "automatically block" is mistranslated so that "automatically" modifies the companies' spying rather than the blocking.
    - Current: `مانع از جاسوسی خودکار شرکت‌ها روی کلیک‌هایتان می‌شویم`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `به‌طور خودکار مانع از جاسوسی شرکت‌ها روی کلیک‌هایتان می‌شویم`
    - The source says the browser automatically blocks companies from spying; the Persian reads "we prevent companies' automatic spying on your clicks", moving "automatically" to the spying.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The imperative "Enable to allow..." is rendered as a noun phrase "فعال‌سازی امکان...", losing the instruction to enable the setting.
    - Current: `فعال‌سازی امکان نیشگون گرفتن و بزرگ‌نمایی`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `برای مجاز کردن نیشگون گرفتن و بزرگ‌نمایی، فعال کنید`
    - Source tells the user to enable the option in order to allow pinch-and-zoom; the target instead states "enabling the ability of pinch and zoom", dropping the conditional instruction.
- `preference_auto_battery_theme` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Battery Saver" is rendered as "بهینه‌ساز باتری" (battery optimizer) instead of the Android feature name "ذخیره‌ساز/صرفه‌جویی باتری".
    - Current: `تنظیم‌شده بر اساس بهینه‌ساز باتری`
    - Source: `Set by Battery Saver`
    - Suggest: `تنظیم‌شده بر اساس بهینه‌سازی مصرف باتری`
    - Android's "Battery Saver" mode has an established Persian name; "بهینه‌ساز باتری" names a different concept.
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "studies" is rendered twice as "آزمایش‌ها و مطالعات" (experiments and studies), adding a term the source does not have and conflicting with the title string which uses only "مطالعات".
    - Current: `اجازه به Mozilla برای نصب و اجرای آزمایش‌ها و مطالعات`
    - Source: `Allows Mozilla to install and run studies`
    - Suggest: `اجازه به Mozilla برای نصب و اجرای مطالعات`
    - Source: "Allows Mozilla to install and run studies"; the related title preference_experiments_2 translates "Studies" as "مطالعات" only.
- `preference_option_autoplay_allowed_wifi_only2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The translation drops "only" applying to cellular data and misplaces it, saying "block audio and video only on mobile internet" vs. source "Block audio and video on cellular data only".
    - Current: `مسدود کردن صدا و تصویر فقط روی اینترنت همراه`
    - Source: `Block audio and video on cellular data only`
    - Suggest: `مسدود کردن صدا و تصویر فقط روی داده‌های تلفن همراه`
    - Minor: source means blocking occurs only on cellular data; the Persian ordering is acceptable, but "اینترنت همراه" vs "داده تلفن همراه" terminology.
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "sharing" is rendered as "screen sharing", narrowing/changing what the feature blocks.
    - Current: `اشتراک‌گذاری صفحه`
    - Source: `View tabs with your fingerprint, PIN, or face unlock. Turning this on also prevents screen capture and sharing.`
    - Suggest: `اشتراک‌گذاری`
    - The source says "prevents screen capture and sharing"; the target adds "صفحه" (screen) to sharing, asserting it blocks screen sharing specifically.
- `restart_and_shortcuts_removal_warning_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Translation adds "تمام" (all), claiming removal of all sites/shortcuts where the source says "any sites and shortcuts you've saved".
    - Current: `تغییر آیکون باعث حذف تمام سایت‌ها و میان‌برهایی می‌شود که در صفحهٔ اصلی خود ذخیره کرده‌اید.`
    - Source: `Changing the icon will remove any sites and shortcuts you’ve saved to your Home screen.   %1$s may close. Tap your new icon to reopen.`
    - Suggest: `تغییر آیکون باعث حذف سایت‌ها و میان‌برهایی می‌شود که در صفحهٔ اصلی خود ذخیره کرده‌اید.`
    - The source is "any sites and shortcuts you’ve saved to your Home screen"; adding "تمام" (all) is not a material change... actually it broadens the claim about what is deleted.
- `saved_login_duplicate` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "A login" rendered as "ورودی" (an entry/input), not the login/account credential meaning.
    - Current: `ورودی با این نام کاربری از قبل وجود دارد`
    - Source: `A login with that username already exists`
    - Suggest: `ورودی با این نام کاربری از قبل وجود دارد ← «گذرواژه‌ای با این نام کاربری از قبل وجود دارد»`
    - "ورودی" means "entry/input" in Persian and does not convey a saved login credential; other strings in this surface use "ورود"/"گذرواژه".
- _…and 24 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_file_access_denied_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Comma misplaced/attached and mood mismatch in the second clause ("may be preventing" rendered as a plain assertion).
    - Current: `ممکن است حذف،‌منتقل شده باشد یا مجوز‌های آن از دسترسی جلوگیری‌ می‌کند.`
    - Source: `{ <ul> } { <li> }It may have been removed, moved, or file permissions may be preventing access.{ </li> } { </ul> }`
    - Suggest: `ممکن است حذف یا منتقل شده باشد، یا مجوزهای آن مانع دسترسی شوند.`
    - The source says permissions "may be preventing" access; the target states it as fact, and the punctuation/spacing ("حذف،‌منتقل", "جلوگیری‌ می‌کند") is broken.
- `mozac_browser_errorpages_file_access_denied_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Past-tense "was denied" rendered as present/habitual "is denied".
    - Current: `دسترسی به این پرونده رد می‌شود`
    - Source: `Access to the file was denied`
    - Suggest: `دسترسی به این پرونده رد شد`
    - The source states a completed event ("Access to the file was denied"); the Persian present tense describes an ongoing/general behaviour.
- `mozac_browser_errorpages_safe_browsing_unwanted_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Misspelled relative construction "وبگاه‌ی" instead of "وبگاهی".
    - Current: `وبگاه‌ی که`
    - Source: `{ <p> }The site at %1$s has been reported as serving unwanted software and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `وبگاهی که`
    - The indefinite/relative ی attaches directly to the noun; a ZWNJ before ی here is a spelling error.
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing ZWNJ in "نمیتواند" and incorrect space in "نمی توانید".
    - Current: `نمیتواند نمایش داده شود`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `نمی‌تواند نمایش داده شود`
    - Persian negation prefix نمی requires a ZWNJ, not zero or a full space.
- `mozac_tab_counter_open_tab_tray_single` — `mozilla-mobile/android-components/components/compose/tabstray/src/main/res/values-fa/strings.xml` — Missing ZWNJ in "زبانه ها" (should be "زبانه‌ها"), inconsistent with the plural string.
    - Current: `زبانه ها`
    - Source: `1 open tab. Tap to switch tabs.`
    - Suggest: `زبانه‌ها`
    - Persian plural suffix -ها attaches with a zero-width non-joiner; the parallel string mozac_tab_counter_open_tab_tray_plural correctly uses "زبانه‌ها".
- `mozac_feature_addons_failed_to_enable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "فعالسازی" is missing the required ZWNJ (should be فعال‌سازی).
    - Current: `شکست در فعالسازی %1$s`
    - Source: `Failed to enable %1$s`
    - Suggest: `شکست در فعال‌سازی %1$s`
    - Persian orthography requires a zero-width non-joiner in the compound فعال‌سازی.
- `mozac_feature_addons_failed_to_translate` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Spelling error: "همچینین" should be "همچنین".
    - Current: `همچینین`
    - Source: `Translation not found, for locale %1$s neither default language %2$s`
    - Suggest: `همچنین`
    - Misspelling of the Persian word همچنین.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space in "ابزارتوسعه‌دهندگان".
    - Current: `گسترش ابزارتوسعه‌دهندگان`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `گسترش ابزارهای توسعه‌دهندگان`
    - "ابزار" and "توسعه‌دهندگان" are run together without a space, producing a malformed word.
- `mozac_feature_addons_permissions_sessions_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Ungrammatical relative clause and missing ezafe: "زبانه‌های که اخیرا بسته‌شده".
    - Current: `دسترسی به زبانه‌های که اخیرا بسته‌شده.`
    - Source: `Access recently closed tabs.`
    - Suggest: `دسترسی به زبانه‌هایی که اخیراً بسته شده‌اند.`
    - Persian requires the indefinite -yi marker (زبانه‌هایی) before the relative clause, and plural agreement; "اخیرا" also lacks the tanvin.
- `mozac_feature_addons_rating_content_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Leftover English word "of" in the translation produces "از of 5".
    - Current: `رتبه‌بندی: %1$.02f از of 5`
    - Source: `Rating: %1$.02f out of 5`
    - Suggest: `رتبه‌بندی: %1$.02f از ۵`
    - Source is "Rating: %1$.02f out of 5"; the target duplicates the preposition, leaving an untranslated "of" that a screen reader will read aloud.
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Present tense "cannot be verified" used where the source states it could not be verified (past).
    - Current: `%1$s نمی‌تواند به عنوان امن تأیید شود و غیرفعال شده است.`
    - Source: `%1$s could not be verified as secure and has been disabled.`
    - Suggest: `امنیت %1$s قابل تأیید نبود و غیرفعال شده است.`
    - Source is "could not be verified as secure and has been disabled"; the Persian present tense mismatches the completed action.
- `mozac_feature_downloads_unable_to_open_third_party_app` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — "نتوانست %1$s را باز کند" adds a third-person past subject not present in the impersonal source "Unable to open %1$s".
    - Current: `نتوانست %1$s را باز کند`
    - Source: `Unable to open %1$s`
    - Suggest: `امکان باز کردن %1$s نبود`
    - The source is impersonal; the Persian implies an unnamed third party failed to open it, which is ungrammatical without a subject.
- `mozac_feature_downloads_write_external_storage_permissions_needed_message` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fa/strings.xml` — Spelling error: "تنطیمات" should be "تنظیمات".
    - Current: `تنطیمات اندروید`
    - Source: `Files and media permission access needed to download files. Go to Android settings, tap permissions, and tap allow.`
    - Suggest: `تنظیمات اندروید`
    - "تنظیمات" (settings) is misspelled with ط instead of ظ.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — "می خواهید" is missing the required zero-width non-joiner (should be "می‌خواهید").
    - Current: `می خواهید این پایگاه را ترک کنید؟`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `می‌خواهید این پایگاه را ترک کنید؟`
    - Persian orthography requires the prefix "می" to be joined with ZWNJ, as done consistently elsewhere in this file (e.g. "استفاده می‌کند").
- `mozac_feature_readerview_sephia` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fa/strings.xml` — "Sepia" is misspelled in Persian as سوبیایی instead of سپیا/سپیایی.
    - Current: `سوبیایی`
    - Source: `Sepia`
    - Suggest: `سپیا`
    - The color Sepia is rendered سپیا in Persian; سوبیایی is not a word and appears to be a transliteration error.
- `mozac_feature_readerview_sepia_color_scheme_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fa/strings.xml` — "Sepia" is misspelled in Persian as سوبیایی instead of سپیا.
    - Current: `طرح رنگی سوبیایی`
    - Source: `Sepia color scheme`
    - Suggest: `طرح رنگی سپیا`
    - Same misspelling of the color name Sepia as in mozac_feature_readerview_sephia.
- `mozac_feature_sitepermissions_notification_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fa/strings.xml` — Typo: «اجاره» (rent) instead of «اجازه» (permission).
    - Current: `اجاره می‌دهید`
    - Source: `Allow %1$s to send notifications?`
    - Suggest: `اجازه می‌دهید`
    - The source says "Allow %1$s to send notifications?"; «اجاره دادن» means "to rent", a spelling error for «اجازه».
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Duplicated word "تا تا" in the translated sentence.
    - Current: `اکنون امتحان کنید تا تا تاریخ %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `اکنون امتحان کنید تا تا تاریخ %1$s را اصلاح کرده: «اکنون امتحان کنید تا تاریخ %1$s»`
    - The Persian text repeats «تا» twice consecutively, a typing error.
- `preference_accessibility_auto_size_2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Persian rendering reads "automatic font size" with the adjective misplaced, saying "automatic font size" as "font size automatic" — it should modify the sizing, not read as a noun phrase with dangling adjective.
    - Current: `اندازهٔ قلم خودکار`
    - Source: `Automatic font sizing`
    - Suggest: `اندازه‌گیری خودکار قلم`
    - Source "Automatic font sizing" describes automatic sizing; "اندازهٔ قلم خودکار" attaches "خودکار" to قلم, reading as "automatic font's size".
- `preference_doh_default_protection_info_4` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Imperative/behaviour bullet "Turn off when..." rendered as the state "خاموش بودن" (being off), inconsistent with the parallel bullet info_5.
    - Current: `خاموش بودن در زمان فعال بودن VPN`
    - Source: `Turn off when VPN, parental control, or enterprise policies are active`
    - Suggest: `خاموش شدن در زمان فعال بودن VPN`
    - The bullet describes the feature turning itself off; "خاموش بودن" describes a static state rather than the action, and diverges from info_5's "خاموش می‌شود".
- `setup_checklist_subtitle_6_steps_fifth_step` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Mixed subject agreement: sentence starts impersonal but ends with a second-person verb, unlike the parallel 5-step string.
    - Current: `تنها ۱ مرحله با خط پایان فاصله دارید`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `تنها ۱ مرحله تا خط پایان مانده است`
    - The source is the same as setup_checklist_subtitle_5_steps_fourth_step; the Persian here reads ungrammatically ("۱ مرحله ... فاصله دارید") and is inconsistent with the parallel string.
- `terms_of_use_prompt_link_terms_of_use` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Link label ends with a dangling preposition "از", leaving an incomplete phrase.
    - Current: `شرایط استفاده از`
    - Source: `Terms of Use`
    - Suggest: `شرایط استفاده`
    - The source is the standalone link text "Terms of Use"; "شرایط استفاده از" ends with the preposition "از" ("of/from") which requires a following noun, so the link reads as truncated. The parallel string terms_of_use_prompt_title_option_a correctly uses "شرایط استفاده".
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "ماموریت ما تا رواج یک اینترنت سالم و باز است" is ungrammatical: "تا" should be a verbal noun construction.
    - Current: `ماموریت ما تا رواج یک اینترنت سالم و باز است`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `مأموریت ما ترویج اینترنتی سالم و باز است`
    - "تا" is not grammatical here; the sentence "Our mission is to foster a healthy, open Internet" needs a noun/infinitive phrase.
- `notification_action_erase_and_open` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Imperative verb form mixed with noun form: "حذف و باز کن" is inconsistent and ungrammatical as a notification action label.
    - Current: `حذف و باز کن`
    - Source: `Erase and Open`
    - Suggest: `پاک کردن و باز کردن`
    - The parallel action notification_action_open uses the verbal noun باز کردن; this string mixes a noun (حذف) with an imperative (باز کن).
- `onboarding_second_screen_subtitle_one` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Missing zero-width non-joiner in verb forms: "می بندید" and "می کنیم".
    - Current: `وقتی برنامه را می بندید، سابقه شما را پاک می کنیم`
    - Source: `We clear your history when you close the app for extra privacy.`
    - Suggest: `وقتی برنامه را می‌بندید، سابقهٔ شما را پاک می‌کنیم`
    - Persian prefix می must be joined with ZWNJ (می‌بندید, می‌کنیم), as done elsewhere in the batch.
- `preference_exceptions` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Misspelled Persian plural of "exception".
    - Current: `استثناعات`
    - Source: `Exceptions`
    - Suggest: `استثناها`
    - The correct Persian form is «استثناها» (or «استثناءات»); «استثناعات» is a misspelling.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Plural "these websites" rendered as singular "this site".
    - Current: `برای این سایت`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `برای این سایت‌ها`
    - Source says "for these websites" (plural); the translation uses the singular "این سایت".
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Spelling error: "غیر متنظره" should be "غیرمنتظره".
    - Current: `غیر متنظره`
    - Source: `Pages may load faster, but may also behave unexpectedly`
    - Suggest: `غیرمنتظره`
    - Typo — letters transposed in منتظره ("unexpected").
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Missing zero-width non-joiner in "نمی توانیم" (space instead of ZWNJ).
    - Current: `نمی توانیم`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `نمی‌توانیم`
    - Persian prefix "نمی" must join the verb with a ZWNJ, as done elsewhere in this batch (e.g. "می‌کنید").

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_declarative_net_request_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Permission description rendered as an imperative command to the browser instead of a noun/gerund phrase like the parallel strings.
    - Current: `محتوا را در هر صفحه‌ای مسدود کن`
    - Source: `Block content on any page`
    - Suggest: `مسدود کردن محتوا در هر صفحه`
    - Other permission descriptions in the same dialog use the gerund form (e.g. "مسدود کردن محتوا در هر صفحه."); the informal imperative "مسدود کن" also breaks the locale's register.
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — "themes" translated as "پوسته‌ها" here but as "زمینه‌ها" in the parallel non-update string.
    - Current: `پایش بر استفاده از افزونه و مدیریت پوسته‌ها.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `پایش استفادهٔ افزونه‌ها و مدیریت زمینه‌ها.`
    - mozac_feature_addons_permissions_management_description renders the same source "manage themes" as "مدیریت زمینه‌ها"; the two variants of the same permission text should be consistent.
- `mozac_feature_autofill_search_hint` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-fa/strings.xml` — "Search logins" is rendered with a nonsensical term and a spacing error instead of the established Persian term for logins (ورودها/اطلاعات ورود).
    - Current: `جست‌وجو در واردشده ها`
    - Source: `Search logins`
    - Suggest: `جست‌وجوی ورودها`
    - "واردشده ها" ("imported/entered ones") is not the term for saved logins, and the detached "ها" should be joined (واردشده‌ها); the source means searching saved logins.
- `mozac_feature_contextmenu_open_link_in_external_app` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — "external app" rendered as "کاره‌ای دیگر", inconsistent with "برنامه" used for app elsewhere in the same surface.
    - Current: `گشودن پیوند در کاره‌ای دیگر`
    - Source: `Open link in external app`
    - Suggest: `گشودن پیوند در برنامهٔ بیرونی`
    - The same term "app" is translated "برنامه" in neighbouring strings (e.g. mozac_feature_applinks_normal_confirm_dialog_title, mozac_feature_customtabs_exit_button); "کاره" is an obscure coinage and inconsistent.
- `mozac_selection_context_menu_search_privately_2` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — "Private Search" rendered as "جست‌وجوی ناشناس" (anonymous search) instead of the established term for private (خصوصی).
    - Current: `جست‌وجوی ناشناس`
    - Source: `Private Search`
    - Suggest: `جست‌وجوی خصوصی`
    - Elsewhere in the same file "private tab" is translated "زبانهٔ خصوصی"; using "ناشناس" here is inconsistent terminology for the Private browsing feature.
- `mozac_feature_media_sharing_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fa/strings.xml` — "Microphone is on" rendered as "صدابَر وصل است" (the sound device is connected), inconsistent with "میکروفون" and "روشن است" used in the neighbouring strings.
    - Current: `صدابَر وصل است`
    - Source: `Microphone is on`
    - Suggest: `میکروفون روشن است`
    - The related notification texts all use "میکروفون", and the parallel camera title uses "روشن است" for "is on"; "وصل است" means "is connected", not "is on".
- `mozac_feature_prompts_sep` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — The abbreviated month name "Sep" is rendered with the full month name, contrary to the comment requesting a short description.
    - Current: `سپتامبر`
    - Source: `Sep`
    - Suggest: `سپتا`
    - Developer comment specifies "September month of the year (short description)" used in a compact month chooser; the target uses the full form.
- `certificate_warning_homepage_card_update_now_button` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Button label "Update now" rendered with the unidiomatic and much longer "به‌روزرسانی در همین لحظه".
    - Current: `به‌روزرسانی در همین لحظه`
    - Source: `Update now`
    - Suggest: `همین حالا به‌روزرسانی کنید`
    - "در همین لحظه" (at this very moment) is not the idiomatic Persian for "now" in a button label and makes the button text drastically longer than the source.
- `credit_cards_warning_dialog_set_up_now` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Set up now" rendered as "راه‌اندازی در همین لحظه", an unnatural and overly long button label.
    - Current: `راه‌اندازی در همین لحظه`
    - Source: `Set up now`
    - Suggest: `راه‌اندازی هم‌اکنون`
    - The button label "Set up now" should be a short imperative; "در همین لحظه" ("at this very moment") is verbose and non-idiomatic for a dialog button.
- `enhanced_tracking_protection_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Enhanced" is dropped from the feature name "Enhanced Tracking Protection".
    - Current: `محافظت در برابر ردیابی برای این وب‌سایت‌ها خاموش است`
    - Source: `Enhanced Tracking Protection is off for these websites`
    - Suggest: `محافظت پیشرفته در برابر ردیابی برای این وب‌سایت‌ها خاموش است`
    - The source names the feature "Enhanced Tracking Protection"; the translation renders it as plain "Tracking Protection", inconsistent with the feature name.
- `logins_warning_dialog_set_up_now` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Set up now" is rendered with an unnatural, overly long phrase for a dialog button.
    - Current: `راه‌اندازی در همین لحظه`
    - Source: `Set up now`
    - Suggest: `هم‌اکنون راه‌اندازی شود`
    - The source is a short positive dialog button; "در همین لحظه" ("in this very moment") is awkward and drastically longer than needed for a button label.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "font" is rendered "فونت" here but "قلم" in the related title string, an inconsistency on the same settings surface.
    - Current: `اندازهٔ فونت با تنظیمات اندروید شما مطابقت خواهد داشت.`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `اندازهٔ قلم با تنظیمات اندروید شما مطابقت خواهد داشت.`
    - preference_accessibility_auto_size_2 uses "قلم" for font while this summary uses "فونت" for the same term on the same screen.
- `private_browsing_common_myths` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "private browsing" is rendered as «مرور خصوصی» here but as «مرور ناشناس» in the neighbouring private-browsing string, an inconsistent term on the same surface.
    - Current: `باورهای نادرست و رایج دربارهٔ مرور خصوصی`
    - Source: `Common myths about private browsing`
    - Suggest: `باورهای نادرست و رایج دربارهٔ مرور ناشناس`
    - private_browsing_a11y_session_announcement translates "Private browsing session" as «نشست مرور ناشناس»; the same feature name should be consistent.
- `notification_browsing_session_channel_name` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — "Private browsing" rendered as "anonymous browsing" (ناشناس) instead of the standard خصوصی.
    - Current: `نشستِ مرور ناشناس`
    - Source: `Private browsing session`
    - Suggest: `نشستِ مرور خصوصی`
    - Elsewhere in the batch "private" is translated as خصوصی (e.g. onboarding_first_screen_subtitle); ناشناس means "anonymous/unknown" and is inconsistent terminology for Private browsing.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing spaces around inline markup and after punctuation, plus broken spacing in several words.
    - Current: `نشانی درخواست مشخصا(به عنوان مثال{ <q> }mozilla.org:80{ </q> }برای درگاه ۸۰ بر روی mozilla.org) ازدرگاهی استفاده می کندکه`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `نشانی درخواست‌شده درگاهی را مشخص کرده است (به عنوان مثال { <q> }mozilla.org:80{ </q> } برای درگاه ۸۰ بر روی mozilla.org) که در حالت عادی`
    - Words are run together ("ازدرگاهی", "می کندکه", "لغوکرد") and spaces are missing before/after the inline <q> markup and after the sentence-ending period, which the user reads as broken text.
- `mozac_browser_errorpages_safe_browsing_malware_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — Missing space between پایگاه and the %1$s placeholder, so the URL runs into the preceding word.
    - Current: `پایگاه%1$s`
    - Source: `{ <p> }The site at %1$s has been reported as an attack site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `پایگاه %1$s`
    - The rendered sentence needs a space between the word and the inserted URL.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — The untranslated English abbreviation "e.g." is left inside the parentheses in addition to the Persian "مثلا", duplicating it.
    - Current: `قراردادی مثلا (e.g. { <q> }wxyz://{ </q> })`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `قراردادی (مثلاً { <q> }wxyz://{ </q> })`
    - The source has "(e.g., wxyz://)"; the translation both translates it as مثلا and keeps the English "e.g.", and misplaces the parenthesis.
- `mozac_compose_base_close_button_content_description` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-fa/strings.xml` — Trailing zero-width non-joiner after "بستن".
    - Current: `بستن‌`
    - Source: `Close`
    - Suggest: `بستن`
    - The Persian text ends with a stray ZWNJ character that has no function at the end of a word.
- `mozac_feature_addons_failed_to_remove` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the word and the placeholder.
    - Current: `شکست در حذف%1$s`
    - Source: `Failed to remove %1$s`
    - Suggest: `شکست در حذف %1$s`
    - The add-on name would be glued to the preceding word in the rendered text.
- `mozac_feature_addons_successfully_installed` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the placeholder and the following word.
    - Current: `%1$sبا موفقیت نصب شد`
    - Source: `Successfully installed %1$s`
    - Suggest: `%1$s با موفقیت نصب شد`
    - The add-on name will run into the next word with no separating space.
- `mozac_feature_addons_successfully_removed` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space between the placeholder and the following word.
    - Current: `%1$sبا موفقیت حذف شد`
    - Source: `Successfully removed %1$s`
    - Suggest: `%1$s با موفقیت حذف شد`
    - The add-on name will run into the next word with no separating space.
- `mozac_feature_addons_updater_dialog_last_attempt` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing colon after the label, which is followed by the date per the developer comment.
    - Current: `آخرین تلاش`
    - Source: `Last attempt:`
    - Suggest: `آخرین تلاش:`
    - Source is "Last attempt:" and the comment states it is followed by the date; the colon was dropped, unlike the parallel "وضعیت:" string.
- `mozac_feature_addons_user_rating_count_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — Missing space after the colon before the placeholder.
    - Current: `بررسی‌های:%1$s`
    - Source: `Reviews: %1$s`
    - Suggest: `بررسی‌ها: %1$s`
    - Source "Reviews: %1$s" has a space after the colon; the target also uses an incorrect ezafe form "بررسی‌های".
- `mozac_feature_prompt_update_confirmation` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fa/strings.xml` — Trailing stray zero-width non-joiner after "به‌روزرسانی".
    - Current: `به‌روزرسانی‌`
    - Source: `Update`
    - Suggest: `به‌روزرسانی`
    - The button label ends with an extraneous ZWNJ character not present in the equivalent strings (e.g. mozac_feature_prompt_login_update_headline_2).
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Stray space after the ZWNJ in "خوش‌ آمدید".
    - Current: `به %1$s خوش‌ آمدید`
    - Source: `Welcome to %1$s`
    - Suggest: `به %1$s خوش آمدید`
    - The word contains both a ZWNJ and a space, producing incorrect spacing.
- `preference_autocomplete_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-fa/strings.xml` — Missing sentence-final period present in the source.
    - Current: `نشانی سفارشی جدید اضافه شد`
    - Source: `New custom URL added.`
    - Suggest: `نشانی سفارشی جدید اضافه شد.`
    - Source ends with a full stop; other translated sentences in this batch keep it.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fa/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
