# Firefox for Android l10n QA — vi

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 2,551 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for vi: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,551 |
| Missing strings | 2 |
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
| Typography deviations from this locale's own norm | 2 |

### Completeness

**2 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 2 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (52)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "help Firefox win" is rendered as "so that Firefox can continue", which suggests Firefox's survival depends on the user's consent.
    - Current: `để Firefox có thể tiếp tục`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `để giúp Firefox chiến thắng`
    - The source asks the user to allow this to help Firefox win. The Vietnamese says it is needed for Firefox to be able to keep going, a claim about the product the source never makes.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "many of the most common trackers" loses "many of", so the text claims protection from the most common trackers without limit.
    - Current: `khỏi các trình theo dõi phổ biến nhất`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `khỏi nhiều trình theo dõi phổ biến nhất`
    - The source limits the claim to "many of" the most common trackers. Without that limit, the translation promises wider protection than the product offers.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 28 |
| 3 | Degraded language (grammar, spelling, terminology) | 18 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — "The connection was reset" is rendered as "the connection has been re-established", which reverses the error's meaning.
    - Current: `Kết nối đã được thiết lập lại`
    - Source: `The connection was reset`
    - Suggest: `Kết nối đã bị đặt lại`
    - "Reset" here means the network dropped the connection (an error). "đã được thiết lập lại" sounds positive and reads as the connection having been successfully set up again.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — "Is your device or network" is rendered with "Máy tính" (computer) instead of device.
    - Current: `Máy tính hoặc mạng của bạn`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Thiết bị hoặc mạng của bạn`
    - The source says "device". On Android, "computer" is wrong and doesn't match the rest of the file.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — "device's network connection" is rendered as "computer network connection".
    - Current: `Kiểm tra kết nối mạng máy tính`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Kiểm tra kết nối mạng của thiết bị`
    - The source says "device". These are mobile apps, and the other error messages in this file use "thiết bị".
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — 'device' is translated as 'Máy tính' (computer) in a mobile app.
    - Current: `Máy tính có được kết nối với mạng đang hoạt động không?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Thiết bị có được kết nối với mạng đang hoạt động không?`
    - The source says 'Is the device connected…'. On Android the device is a phone or tablet, not a computer.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — 'device' is translated as 'máy tính' (computer).
    - Current: `máy tính của bạn`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `thiết bị của bạn`
    - The source says 'your device'. On Android it is not a computer.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — The translation says both the server configuration and the user's computer have a problem, but the source says the problem is the server and not the device.
    - Current: `có thể cấu hình máy chủ và máy tính của bạn có vấn đề .`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `có thể đó là vấn đề về cấu hình máy chủ chứ không phải do thiết bị của bạn.`
    - Source: 'it is likely a server configuration issue and not your device'. The Vietnamese drops the 'not' and blames the user's device instead of clearing it. It also has a stray space before the full stop.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — 'device' is translated as 'Máy tính' (computer) in a mobile app.
    - Current: `Máy tính có được kết nối với mạng đang hoạt động không?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Thiết bị có được kết nối với mạng đang hoạt động không?`
    - The source says 'Is the device connected to an active network?'. The device is a phone or tablet, not a computer.
- `mozac_feature_addons_permissions_downloads_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-vi/strings.xml` — The translation drops "read" from "read and modify the browser's download history".
    - Current: `Tải về các tập tin và chỉnh sửa lịch sử tải về của trình duyệt`
    - Source: `Download files and read and modify the browser’s download history`
    - Suggest: `Tải về các tập tin, đọc và chỉnh sửa lịch sử tải về của trình duyệt`
    - The source says the permission lets the add-on both read and modify the download history. The Vietnamese only mentions modifying, so the permission description is incomplete.
- `mozac_feature_addons_permissions_downloads_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-vi/strings.xml` — The translation drops "read" from "read and modify the browser's download history".
    - Current: `Tải về các tập tin và chỉnh sửa lịch sử tải về của trình duyệt.`
    - Source: `Download files and read and modify the browser’s download history.`
    - Suggest: `Tải về các tập tin, đọc và chỉnh sửa lịch sử tải về của trình duyệt.`
    - The source says the permission lets the add-on both read and modify the download history. The Vietnamese only mentions modifying, so the permission description is incomplete.
- `mozac_feature_prompts_manage_credit_cards_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-vi/strings.xml` — Translation still says "credit cards" although the revised source says just "cards".
    - Current: `Quản lý thẻ tín dụng`
    - Source: `Manage cards`
    - Suggest: `Quản lý thẻ`
    - The _2 revision changed the source from "Manage credit cards" to "Manage cards" to cover all saved cards. The Vietnamese keeps the old, narrower wording, and it doesn't match sibling strings like "Sử dụng thẻ đã lưu".
- `mozac_lib_crash_activity_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-vi/strings.xml` — "Trình báo cáo lỗi" means "error reporter" (a tool), not "Crash Reports" (the list of past crash reports).
    - Current: `Trình báo cáo lỗi`
    - Source: `Crash Reports`
    - Suggest: `Báo cáo sự cố`
    - The developer comment says this is the title of the screen listing past crashes (like about:crashes). "Trình …" names a program or tool, so the title describes the wrong thing. The same file also uses "sự cố" for crash (mozac_lib_crash_channel), so "Báo cáo sự cố" is the consistent term.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Department" is translated as an organizational department instead of an administrative division.
    - Current: `Bộ phận`
    - Source: `Department`
    - Suggest: `Tỉnh (Department)`
    - The comment says this is the administrative division used in Nicaragua and Colombia. "Bộ phận" means a section or department of an organisation, not a geographic region.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Post town" is rendered as "town post office" rather than the postal town name.
    - Current: `Bưu điện thị trấn`
    - Source: `Post town`
    - Suggest: `Thị trấn bưu chính`
    - A post town is the town name used in postal addresses in the UK, Norway and Sweden. "Bưu điện thị trấn" means a town's post office, which is a different thing.
- `addresses_townland` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Townland" is translated as "town", but it is a small rural land division in Ireland.
    - Current: `Thị trấn`
    - Source: `Townland`
    - Suggest: `Khu đất (Townland)`
    - The comment describes a townland as a type of land division used in rural Ireland. "Thị trấn" means a town, which is the opposite kind of place, and the same word is also used for the Township field.
- `alternative_app_icon_group_solid_colors` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Solid colors" is rendered as just "Màu" ("Colors"), dropping the "solid/flat" meaning that sets this group apart from the gradient group.
    - Current: `Màu`
    - Source: `Solid colors`
    - Suggest: `Màu trơn`
    - The developer comment says this group holds icons with flat, uniform color backgrounds, as opposed to the "Gradients" group. "Màu" alone just means "Colors", and gradient icons are colored too, so the label no longer names what is in the group.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Item Menu" (the menu belonging to an item) is translated as "Mục menu", which means "menu item".
    - Current: `Mục menu cho %s`
    - Source: `Item Menu for %s`
    - Suggest: `Menu mục cho %s`
    - Per the developer comment, this describes the overflow-menu button for a bookmark or folder: the menu of that item. In Vietnamese, "Mục menu" means an entry inside a menu, so a screen-reader user hears that this is a menu item, not the button that opens the item's menu.
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Button label meaning 'open the tabs' is translated as a noun phrase 'the currently open tabs'.
    - Current: `Các thẻ đang mở`
    - Source: `Open tabs`
    - Suggest: `Mở các thẻ`
    - The developer comment says this is a button that opens the tabs of the selected collection; 'Các thẻ đang mở' means 'open (currently opened) tabs', not the action.
- `compact_search_bar_widget_description` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The widget name "Compact search bar" is translated as the command "Collapse the search bar".
    - Current: `Thu gọn thanh tìm kiếm`
    - Source: `Compact search bar`
    - Suggest: `Thanh tìm kiếm thu gọn`
    - The source is a noun phrase that names a widget in the widget picker. "Thu gọn thanh tìm kiếm" is verb first, so it reads as an instruction to collapse the search bar. Putting the modifier after the noun ("Thanh tìm kiếm thu gọn") makes it a name again.
- `crash_reports_data_category` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Header 'Crash Reports' is translated as 'Crash reporter' (the tool) instead of the reports.
    - Current: `Trình báo cáo lỗi`
    - Source: `Crash Reports`
    - Suggest: `Báo cáo sự cố`
    - Source names the data category 'Crash Reports'; 'Trình báo cáo lỗi' denotes the reporting program, and is inconsistent with 'Báo cáo sự cố' used in crash_reporting_description.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The product name "Firefox Suggest" is translated as a generic phrase instead of being kept as a brand.
    - Current: `Đề xuất của Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - Firefox Suggest is a Mozilla product name for this feature and should stay untranslated. The rendering "Firefox's suggestions" turns the brand into a description.
- `lens_camera_upload_failed` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The Vietnamese says no results were found instead of saying the results couldn't be retrieved.
    - Current: `Không tìm thấy kết quả từ Google Ống kính`
    - Source: `Couldn’t get results from Google Lens`
    - Suggest: `Không thể nhận kết quả từ Google Ống kính`
    - The source "Couldn’t get results" and the developer comment describe a failure caused by a network problem or a Google Lens error, with a retry action. "Không tìm thấy kết quả" means "no results found", which tells the user the search worked but matched nothing.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "the platform you came from" is rendered as "the platform you are currently using".
    - Current: `nền tảng bạn đang sử dụng rằng`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `nền tảng bạn vừa sử dụng rằng`
    - The developer comment says the platform is the external source that sent the user to Firefox. "đang sử dụng" means the one in use right now. The sibling strings (_4, _5, _7) correctly use "vừa sử dụng".
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "help Firefox win" is rendered as "so that Firefox can continue", which suggests Firefox's survival depends on the user's consent.
    - Current: `để Firefox có thể tiếp tục`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `để giúp Firefox chiến thắng`
    - The source asks the user to allow this to help Firefox win. The Vietnamese says it is needed for Firefox to be able to keep going, a claim about the product the source never makes.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The translation adds "is a company": Firefox is a browser, and the source only says it is proudly independent.
    - Current: `Firefox tự hào là một công ty độc lập`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox tự hào là trình duyệt độc lập`
    - The source says "Firefox is proudly independent". Calling Firefox a company misstates what the product is.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "will cause websites to break" is softened to "may break websites".
    - Current: `(có thể làm hỏng các trang web)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `(sẽ làm hỏng các trang web)`
    - The source says blocking all cookies is certain to break sites. The translation copies the "may" wording from option 3, which plays down a definite warning.
- `preference_enhanced_tracking_protection_custom_known_fingerprinters` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Known Fingerprinters" is translated as "known traces", which does not name the trackers.
    - Current: `Dấu vết đã biết`
    - Source: `Known Fingerprinters`
    - Suggest: `Trình lấy dấu vân tay đã biết`
    - Fingerprinters are trackers that identify you by your device's fingerprint. "Dấu vết" just means "traces", which is a different thing.
- `preference_enhanced_tracking_protection_custom_tracking_content` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "Tracking content" is translated as "content trackers".
    - Current: `Trình theo dõi nội dung`
    - Source: `Tracking content`
    - Suggest: `Nội dung theo dõi`
    - The category is content that tracks you, not trackers that track content.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "many of the most common trackers" loses "many of", so the text claims protection from the most common trackers without limit.
    - Current: `khỏi các trình theo dõi phổ biến nhất`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `khỏi nhiều trình theo dõi phổ biến nhất`
    - The source limits the claim to "many of" the most common trackers. Without that limit, the translation promises wider protection than the product offers.
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The source's "and" became "khi" (when), so the two actions read as condition and result.
    - Current: `khi bị xoá khỏi lịch sử tải xuống`
    - Source: `File is deleted from your device and removed from download history`
    - Suggest: `và khỏi lịch sử tải xuống`
    - The en-US says the file is deleted from the device and removed from download history (both happen). The Vietnamese says the file will be deleted from the device when it is removed from download history, which describes a different relationship.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Without a nominalizer, "và bạn sử dụng nó với các đối tác…" reads as "and you use Firefox with Mozilla's marketing partners" instead of "share that you use it".
    - Current: `và bạn sử dụng nó với`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `và việc bạn sử dụng nó với`
    - The comment says "that you use it" is something the user shares: that they keep using Firefox. The Vietnamese leaves out "việc"/"rằng", so the clause reads as a separate statement that the user uses Firefox with the partners. That is not what the source means, and the Vietnamese is ungrammatical.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Title rendered as a noun phrase meaning 'settings for search' instead of the verb phrase 'search (through) settings'.
    - Current: `Cài đặt tìm kiếm`
    - Source: `Search settings`
    - Suggest: `Tìm kiếm cài đặt`
    - The developer comment states 'Search' is a verb here (the screen searches through settings). 'Cài đặt tìm kiếm' means 'search settings' as in configuration of search, a different screen.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_not_found` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — Misspelling: "lưu trũ" should be "lưu trữ".
    - Current: `lưu trũ`
    - Source: `No archived version found.`
    - Suggest: `lưu trữ`
    - "trũ" is a wrong-tone typo. The correct word for archive/storage is "lưu trữ", which the neighbouring archive strings spell correctly.
- `mozac_feature_addons_permissions_content_description_item` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-vi/strings.xml` — The position phrase "X of Y" is translated word for word as "của" (possessive), which is not idiomatic Vietnamese for a position in a list.
    - Current: `%2$d của %3$d`
    - Source: `%1$s, %2$d of %3$d`
    - Suggest: `%2$d trên %3$d`
    - The comment says this reads like "2 of 6". "2 của 6" means "2 belonging to 6". Vietnamese uses "trên" for this kind of count.
- `mozac_feature_addons_permissions_tab_hide_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-vi/strings.xml` — "hiển thị" is misspelled as "hiển thỉ" (wrong tone mark).
    - Current: `hiển thỉ`
    - Source: `Hide and show browser tabs.`
    - Suggest: `hiển thị`
    - The correct Vietnamese word for "show/display" is "hiển thị". "thỉ" is a misspelling, and the version of this string without the period uses a different, correctly spelled word.
- `mozac_feature_media_sharing_camera_and_microphone_reminder_text_2` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-vi/strings.xml` — The word "Nhắc" is misspelled as "Nhăc" because its tone mark (dấu sắc) is missing.
    - Current: `Nhăc nhở`
    - Source: `Reminder: %1$s is still using your microphone and camera. Tap to open the tab.`
    - Suggest: `Nhắc nhở`
    - "Reminder" is "Nhắc nhở" in Vietnamese, as in the sibling microphone string. "Nhăc" without the tone mark is not a real word.
- `browser_menu_discover_more_extensions` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "tiện tích" is a misspelling of "tiện ích" (extensions).
    - Current: `tiện tích`
    - Source: `Discover more extensions`
    - Suggest: `tiện ích`
    - Elsewhere on the same menu, Extensions is rendered as "Tiện ích" (browser_menu_extensions, browser_menu_manage_extensions). "tiện tích" is not a Vietnamese word; it is a typo.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Misspelling: "đuọc" should be "được".
    - Current: `lấy đuọc`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `lấy được`
    - "đuọc" is not a Vietnamese word; the intended word is "được" (someone else gets hold of your device).
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — "khu vục" is misspelled; it should be "khu vực" (region).
    - Current: `khu vục chính`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `khu vực chính`
    - The word for region is "khu vực", and the same sentence spells it correctly a few words earlier. "vục" is a wrong-accent typo.
- `delete_language_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The word "xuống" appears twice: "tải xuống một phần ngôn ngữ xuống bộ nhớ đệm".
    - Current: `tải xuống một phần ngôn ngữ xuống bộ nhớ đệm`
    - Source: `If you delete this language, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `tải một phần ngôn ngữ xuống bộ nhớ đệm`
    - Using "xuống" twice in the same verb phrase is ungrammatical. The related string delete_language_all_languages_file_dialog_message already uses the correct wording "tải một phần ngôn ngữ xuống bộ nhớ đệm".
- `nova_onboarding_add_search_widget_button` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — English word order: the modifier "Firefox" comes before the head noun "widget", which is ungrammatical in Vietnamese.
    - Current: `Thêm Firefox widget`
    - Source: `Add Firefox widget`
    - Suggest: `Thêm widget Firefox`
    - In Vietnamese the modifier follows the noun it describes (compare "Logo Firefox" in the same batch). "Firefox widget" copies the English order.
- `preference_doh_default_protection_info_5` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The phrase "yêu cầu %1$s nó không nên" is ungrammatical: "yêu cầu" (request) can't take this clause, and the pronoun "nó" is left dangling.
    - Current: `mạng yêu cầu %1$s nó không nên sử dụng`
    - Source: `Turn off when a network tells %1$s it shouldn’t use secure DNS. %2$s`
    - Suggest: `mạng báo cho %1$s rằng nó không nên sử dụng`
    - The source means a network *tells* the app that it shouldn't use secure DNS. In Vietnamese, "yêu cầu X nó không nên" doesn't parse; it needs a reporting verb plus "rằng", e.g. "báo cho %1$s rằng".
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The word “của” appears twice in a row.
    - Current: `%3$s của của chúng tôi`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `%3$s của chúng tôi`
    - “của của” is a typo. The source says “our %3$s”, so “của” should appear once.
- `webcompat_reporter_etp_checkbox_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Two nouns are stacked in a way Vietnamese grammar doesn't allow: "tính năng trình chống theo dõi".
    - Current: `tính năng trình chống theo dõi`
    - Source: `Send list of items blocked by tracking protection`
    - Suggest: `tính năng chống theo dõi`
    - "tính năng" (feature) and "trình chống theo dõi" (tracking protector) both name the same thing. Putting them together reads like an unfinished edit and is ungrammatical. The source simply says "tracking protection".

### D. Terminology, register & consistency

- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — The same sentence translates 'port' as 'cổng' and then leaves it as the English 'port'.
    - Current: `cho port 80`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `cho cổng 80`
    - Earlier in the same sentence 'a port' is 'một cổng'. Switching to the English 'port' for the same term is inconsistent.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-vi/strings.xml` — The English abbreviation 'e.g.,' is left untranslated inside a Vietnamese sentence.
    - Current: `(e.g.,`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `(ví dụ:`
    - The rest of the sentence is in Vietnamese. The port blocked message translates 'e.g.' as 'ví dụ:'.
- `mozac_feature_addons_permissions_bookmarks_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-vi/strings.xml` — "Bookmarks" is rendered as "trang đánh dấu" here but as "dấu trang" in the matching update string and all the other bookmark strings.
    - Current: `trang đánh dấu`
    - Source: `Read and modify bookmarks`
    - Suggest: `dấu trang`
    - This string and its _for_update twin describe the same permission. Every other string in the batch uses "dấu trang", so this term is the inconsistent one.

### E. Typography, punctuation & spacing

- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — This string uses straight double quotes, but the locale convention (and the source) uses curly double quotes.
    - Current: `"https://" hoặc "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” hoặc “http://”`
    - The en-US string uses curly quotes “…”, and the vi tree's established convention is curly double quotes.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `Địa chỉ trang web phải chứa "https://" hoặc "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `microsurvey_uninstall_survey_title` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — There appear to be stray zero-width characters between "kiến" and "phản hồi".
    - Current: `Ý kiến ​​phản hồi`
    - Source: `Your feedback matters. Why are you uninstalling?`
    - Suggest: `Ý kiến phản hồi`
    - Invisible zero-width characters seem to sit next to the space, probably left over from a paste. They can affect line wrapping and screen readers. A single normal space is enough.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Tự động xóa dữ liệu duyệt khi bạn chọn "Thoát" từ menu chính`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — Straight double quotes used around “Thoát” instead of the locale's curly double quotes.
    - Current: `"Thoát"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Thoát”`
    - The vi convention is curly double quotes, and the en-US source also uses curly quotes around “Quit”.
- `preferences_show_nonsponsored_suggestions_summary` — `mozilla-mobile/fenix/app/src/main/res/values-vi/strings.xml` — The translation has two invisible zero-width spaces (U+200B) between "từ" and "web".
    - Current: `từ ​​web`
    - Source: `Get suggestions from the web related to your search`
    - Suggest: `từ web`
    - The source has no zero-width characters. These look like stray characters left by copy-pasting, and they can affect searching and line breaking. Only a normal space should be there.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/vi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
