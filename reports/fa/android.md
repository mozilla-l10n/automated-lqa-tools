# Firefox for Android l10n QA — fa

| | |
|---|---|
| **Generated** | 2026-11-02 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `bc6fbd15dac8` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `bc6fbd15dac8` |
| **Previous run** | 2026-11-02 @ `a2d8921e4c16` |
| **Mode** | incremental |
| **Strings reviewed this run** | 42 of 2,548 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fa: [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (1)

- `saved_login_duplicate` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "A login" rendered as "ورودی" (an entry/input), not the login/account credential meaning.
    - Current: `ورودی با این نام کاربری از قبل وجود دارد`
    - Source: `A login with that username already exists`
    - Suggest: `ورودی با این نام کاربری از قبل وجود دارد ← «گذرواژه‌ای با این نام کاربری از قبل وجود دارد»`
    - "ورودی" means "entry/input" in Persian and does not convey a saved login credential; other strings in this surface use "ورود"/"گذرواژه".

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
| Strings | 2,548 |
| Missing strings | 56 |
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

**56 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — 30
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fa/strings.xml` — 12
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-fa/strings.xml` — 7
- `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fa/strings.xml` — 7

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 21 | **guillemet** |
| ellipsis | `char` 21 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (63)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 25 |
| 3 | Degraded language (grammar, spelling, terminology) | 38 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

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
- `mozac_feature_contextmenu_snackbar_link_text_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — "Link text copied to clipboard" is rendered as an ungrammatical noun phrase that swaps the words and loses the verb.
    - Current: `پیوند متن رونوشت شده در تخته‌گیره`
    - Source: `Link text copied to clipboard`
    - Suggest: `متن پیوند در تخته‌گیره رونوشت شد`
    - Source is a confirmation sentence: the link text was copied to the clipboard. The target reverses «متن پیوند» into «پیوند متن» (text's link) and uses a participial fragment instead of a completed action.
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
- `alternative_app_icon_option_pride` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Pride" (LGBTQ+ Pride) is transliterated as «پراید», which in Persian denotes the Kia Pride car, not the concept of pride.
    - Current: `پراید`
    - Source: `Pride`
    - Suggest: `افتخار`
    - The developer comment states the icon supports the LGBTQ+ community; «پراید» is universally read in Persian as the car brand Pride, conveying the wrong meaning.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Close custom tab menu sheet" is rendered with the modifiers reordered, yielding "sheet of the custom tab's menu" instead of "custom tab menu sheet".
    - Current: `بستن برگهٔ منوی زبانهٔ سفارشی`
    - Source: `Close custom tab menu sheet`
    - Suggest: `بستن برگهٔ منوی زبانهٔ سفارشی (بستن صفحهٔ منوی زبانهٔ سفارشی)`
    - The term برگه duplicates the word used for "tab" elsewhere, making the description ambiguous for screen-reader users.
- `debug_drawer_tab_tools_tab_count_inactive` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Inactive" (a tab-count category) is rendered as the verbal noun "disabling" instead of an adjective.
    - Current: `ازکار انداختن`
    - Source: `Inactive`
    - Suggest: `ازکار افتاده`
    - The comment says this labels the inactive-tab count category. «ازکار انداختن» means "to disable" (an action), not the state "inactive". The sibling string already uses «ازکار افتاده».
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Title says "the file name does not change" instead of expressing inability to rename the file.
    - Current: `نام پرونده تغییر نمی‌کند`
    - Source: `Can’t rename file`
    - Suggest: `نمی‌توان نام پرونده را تغییر داد`
    - Source "Can’t rename file" states an inability/failure; the fa reads as a plain statement that the name doesn't change, which misstates the error.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The notification title renders "%1$s tabs closed" as "tabs closed in %1$s", turning the app name into a location instead of the subject of the count.
    - Current: `زبانه‌های بسته‌شده در %1$s: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `زبانه‌های بسته‌شدهٔ %1$s: %2$d`
    - Per the comment, %1$s is the app name and %2$d is the number of tabs closed; the source reads "%1$s tabs closed: %2$d", not "tabs closed in %1$s".
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Translation drops both "default" (resolver) and "secure" (DNS provider), losing the meaning of falling back to the default resolver when the secure provider fails.
    - Current: `استفاده از مبدل ساناد در صورتی که مشکلی برای کار با ارائه‌دهندهٔ ساناد وجود داشته باشد`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `استفاده از مبدل پیش‌گزیده ساناد در صورتی که مشکلی برای کار با ارائه‌دهندهٔ ساناد امن وجود داشته باشد`
    - Source: "Use your default DNS resolver if there is a problem with the secure DNS provider". The fa reads "use a DNS resolver if there is a problem with the DNS provider", omitting the key qualifiers; sibling strings (increased_protection_info_2, off_summary) do render "default" as پیش‌گزیده.
- `preferences_email_masks_suggest_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The toggle title drops "Suggest" and is identical to the section title "Email masks", so it no longer says what the toggle does.
    - Current: `پنهان‌کننده رایانامه`
    - Source: `Suggest email masks`
    - Suggest: `پیشنهاد پنهان‌کننده‌های رایانامه`
    - The source is "Suggest email masks", the label of a toggle that controls whether masks are suggested. The translation only says "email mask", repeats the parent settings title, and leaves out the action.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Inactive section" is rendered as «بخش ازکار افتاده», which means a broken or out-of-order section, not an inactive one.
    - Current: `بخش ازکار افتاده`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `بخش زبانه‌های غیرفعال`
    - The source refers to the inactive-tabs section, meaning tabs not viewed recently. «ازکار افتاده» means "broken down" or "defunct", which gives the wrong idea of the feature; «غیرفعال» is the usual term for inactive.
- `preferences_inactive_tabs_toggle_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — "Inactive tabs" is translated as "broken/out-of-order tabs".
    - Current: `زبانه‌های ازکار افتاده`
    - Source: `Inactive tabs`
    - Suggest: `زبانه‌های غیرفعال`
    - «از کار افتاده» means broken down/defunct, not inactive; the feature refers to tabs the user has not used recently.
- `tab_group_sheet_dismiss_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Content description reverses the relationship: "collapse drag handle" rendered as "drag handle to collapse".
    - Current: `دستگیرهٔ کشیدن برای جمع کردن`
    - Source: `View tab group, collapse drag handle`
    - Suggest: `دستگیرهٔ کشیدن برای جمع کردن را ببندید`
    - Source lists two elements: viewing the tab group and a collapse drag handle; the Persian restructures it, but the main issue is minor wording.
- `wallpaper_artist_series_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The collection name "Independent Voices" is rendered as «آوای مشترک», which means "shared/common voice".
    - Current: `آوای مشترک`
    - Source: `The Independent Voices collection.`
    - Suggest: `آواهای مستقل`
    - The source and the developer comment name the collection "Independent Voices". «مشترک» means shared or common, so it does not mean "independent" («مستقل»).
- `wallpaper_artist_series_description_with_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — The collection name "Independent Voices" is rendered as «آوای مشترک», which means "shared/common voice".
    - Current: `آوای مشترک`
    - Source: `The Independent Voices collection. %s`
    - Suggest: `آواهای مستقل`
    - The source and the developer comment name the collection "Independent Voices". «مشترک» means shared or common, so it does not mean "independent" («مستقل»), and «آوا» is singular where the source is plural.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — The sentence mixes the object marker «را» with a passive verb, which is ungrammatical, and it drops the subject "you".
    - Current: `را برای امنیت بیشتر به‌کار انداخته شده است`
    - Source: `You’ve enabled HTTPS-Only Mode for enhanced security, and a HTTPS version of { <em> }%1$s{ </em> } is not available.`
    - Suggest: `را برای امنیت بیشتر به‌کار انداخته‌اید`
    - The source says "You've enabled HTTPS-Only Mode". The fa uses «را», which needs an active verb with a subject, but ends in the passive «به‌کار انداخته شده است», so the sentence is broken. The active form «به‌کار انداخته‌اید» fixes the grammar and restores the subject.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — «وبگاهٔ» is misspelled: the hamza linking mark doesn't belong after the pronounced final «ه».
    - Current: `وبگاهٔ بالقوه`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `وبگاه بالقوه`
    - The final «ه» in «وبگاه» is a pronounced consonant, so the linking vowel is not written with «ٔ». The sibling strings correctly write «وبگاه مهاجم» and «وبگاه گمراه‌کننده».
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
- `addons_permissions_allow_for_all_sites_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — A stray ezafe (ٔ) is attached to «وبگاه» directly before the object marker «را», which is ungrammatical.
    - Current: `هر وبگاهٔ را`
    - Source: `If you trust this extension, you can give it permission on every website.`
    - Suggest: `هر وبگاه را`
    - The ezafe means a modifier follows, but here the noun is followed directly by «را». The correct form is «در هر وبگاه».
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Missing ezafe on «وبگاه‌ها» breaks the link to «این زبان».
    - Current: `ترجمهٔ وبگاه‌ها این زبان`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `ترجمهٔ وبگاه‌های این زبان`
    - The source says 'sites in this language', which needs the ezafe form «وبگاه‌های این زبان». Without it the phrase is ungrammatical. The parallel 'never translate' summary uses the correct form.
- `preference_accessibility_auto_size_2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Persian rendering reads "automatic font size" with the adjective misplaced, saying "automatic font size" as "font size automatic" — it should modify the sizing, not read as a noun phrase with dangling adjective.
    - Current: `اندازهٔ قلم خودکار`
    - Source: `Automatic font sizing`
    - Suggest: `اندازه‌گیری خودکار قلم`
    - Source "Automatic font sizing" describes automatic sizing; "اندازهٔ قلم خودکار" attaches "خودکار" to قلم, reading as "automatic font's size".
- `preferences_category_select_default_search_engine_2` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Missing ezafe marker (هٔ) on «پیش‌گزیده» before «مرور».
    - Current: `پیش‌گزیده مرور عادی`
    - Source: `Normal browsing default search engine`
    - Suggest: `پیش‌گزیدهٔ مرور عادی`
    - The locale consistently writes the ezafe on final ه as هٔ (صفحهٔ، زبانهٔ، همهٔ); here the ezafe linking «پیش‌گزیده» to «مرور عادی» is omitted.
- `preferences_category_select_private_search_engine` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Missing ezafe marker (هٔ) on «پیش‌گزیده» before «مرور».
    - Current: `پیش‌گزیده مرور خصوصی`
    - Source: `Private browsing default search engine`
    - Suggest: `پیش‌گزیدهٔ مرور خصوصی`
    - The locale consistently writes the ezafe on final ه as هٔ (صفحهٔ، زبانهٔ، همهٔ); here the ezafe linking «پیش‌گزیده» to «مرور خصوصی» is omitted.

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
- `mozac_feature_contextmenu_copy_link_text` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-fa/strings.xml` — Context menu item label is rendered as an imperative sentence instead of a noun-phrase action label.
    - Current: `متن پیوند را رونوشت کنید`
    - Source: `Copy link text`
    - Suggest: `رونوشت از متن پیوند`
    - Other context menu items are nominal labels; the source "Copy link text" is a menu action label, not an instruction addressed to the user.
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
- `etp_cookies_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Here "cross-site" is translated as «میان‌مبدأ» (cross-origin), while the other tracking protection strings use «بین‌وبگاهی» or «میان‌وبگاهی», and "Cookies" is left singular.
    - Current: `کلوچک ردیاب میان‌مبدأ`
    - Source: `Cross-Site Tracking Cookies`
    - Suggest: `کلوچک‌های ردیاب بین‌وبگاهی`
    - The source says "Cross-Site Tracking Cookies". «مبدأ» (origin) is a different technical term from "site". The sibling strings on the same screen (etp_cookies_title_2, preference_enhanced_tracking_protection_custom_cookies_1/_5) use «وبگاهی». The plural "Cookies" also became the singular «کلوچک».
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — `never_translate_site_header_preference` quotes “این وبگاه‌ هرگز ترجمه نشود” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “این وبگاه هرگز ترجمه نشود”
    - Current: `برای افزودن وبگاه‌ جدید: به آن وبگاه‌ بروید و از منوی ترجمه «این وبگاه‌ هرگز ترجمه نشود» را انتخاب کنید.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `این وبگاه هرگز ترجمه نشود`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `phone_feature_go_to_settings` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — Button label uses the informal singular imperative «برو», which clashes with the formal address and infinitive button labels used elsewhere.
    - Current: `برو به تنظیمات`
    - Source: `Go to Settings`
    - Suggest: `رفتن به تنظیمات`
    - The locale addresses users formally (e.g. «دوباره تلاش کنید») and labels buttons with infinitives (e.g. «گشودن در زبانهٔ جدید»). «برو» is an informal second-person singular command, so this label breaks the established register.

### E. Typography, punctuation & spacing

_Nothing in this category._

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

### Fixed to date (78)

- `mozac_browser_errorpages_file_access_denied_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_file_access_denied_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_safe_browsing_unwanted_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `mozac_browser_errorpages_unknown_protocol_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `alternative_app_icon_option_cuddling` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `automatic_translation_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `awesomebar_clipboard_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `browser_menu_no_extensions_installed_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `certificate_warning_homepage_card_update_now_button` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `close_tab_and_delete_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `credit_cards_warning_dialog_set_up_now` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `download_languages_item_content_description_delete_in_progress_state` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `enhanced_tracking_protection_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `exit_fullscreen_with_gesture_short` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `ip_protection_data_limit_reached_description` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `ip_protection_menu_limit_reached` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `lens_camera_loading_status` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `lens_camera_upload_failed` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `logins_password_copied` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `logins_warning_dialog_set_up_now` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `microsurvey_describe_your_experience_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
- `nova_onboarding_marketing_body_3` — `mozilla-mobile/fenix/app/src/main/res/values-fa/strings.xml` — fixed 2026-11-02
