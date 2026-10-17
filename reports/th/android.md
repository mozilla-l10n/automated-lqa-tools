# Android l10n QA — th

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **Previous run** | 2026-10-16 @ `4d7697d1b89b` |
| **Mode** | baseline |
| **Strings reviewed this run** | 2,685 of 2,685 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for th: [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (49)

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The source's "device's network connection" is translated as the computer's network connection.
    - Current: `ตรวจสอบการเชื่อมต่อเครือข่ายของคอมพิวเตอร์`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `ตรวจสอบการเชื่อมต่อเครือข่ายของอุปกรณ์`
    - The source says "device", and the other error pages in this file use อุปกรณ์. On Android, "computer" is the wrong thing to name.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The source's "your device or network" is translated as "your computer or network".
    - Current: `คอมพิวเตอร์หรือเครือข่ายของคุณ`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `อุปกรณ์หรือเครือข่ายของคุณ`
    - The source says "device", not "computer". This is a mobile browser, and the other error pages here use อุปกรณ์.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The clause "but the proxy refused a connection" is missing, so the error page never states what went wrong.
    - Current: `เบราว์เซอร์ถูกกำหนดค่าให้ใช้เซิร์ฟเวอร์พร็อกซี{ </p> }`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `เบราว์เซอร์ถูกกำหนดค่าให้ใช้เซิร์ฟเวอร์พร็อกซี แต่พร็อกซีปฏิเสธการเชื่อมต่อ{ </p> }`
    - The source says the browser is set up to use a proxy but the proxy refused the connection. The Thai keeps only the first half, which removes the actual error.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "device" is translated as "computer" (คอมพิวเตอร์) in a mobile app.
    - Current: `คอมพิวเตอร์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `อุปกรณ์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - The source says "device". This is an Android app, and other strings in this batch translate it as อุปกรณ์.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "device" is translated as "computer" (คอมพิวเตอร์) in a mobile app.
    - Current: `คอมพิวเตอร์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `อุปกรณ์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - The source says "device". Other strings in this batch translate it as อุปกรณ์.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "your device" is translated as "your computer" (คอมพิวเตอร์ของคุณ).
    - Current: `ไม่ใช่คอมพิวเตอร์ของคุณ`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `ไม่ใช่อุปกรณ์ของคุณ`
    - The source says "not your device". The app runs on mobile devices, and the batch elsewhere uses อุปกรณ์.
- `mozac_compose_base_link_text_links_available` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-th/strings.xml` — "Link" is spelled ลิงค์ here but ลิงก์ in the title string next to it in the same LinkText component.
    - Current: `ลิงค์`
    - Source: `Links available`
    - Suggest: `ลิงก์`
    - Two strings in the same LinkText component spell "link" differently. ลิงก์ is the standard spelling (Royal Institute) and is the one the links dialog title uses, so ลิงค์ should be changed to match.
- `mozac_feature_addons_permissions_all_domain_count_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-th/strings.xml` — Number placed after โดเมน reads as 'domain number N' rather than 'N domains'.
    - Current: `ไซต์ในโดเมน %1$d`
    - Source: `{$quantity ->} [other] Access your data for sites in %1$d domains`
    - Suggest: `ไซต์ใน %1$d โดเมน`
    - Source says sites in %1$d domains (a count); in Thai 'โดเมน %1$d' reads as a domain identified by number, while a count needs number + classifier 'ใน %1$d โดเมน'.
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-th/strings.xml` — The channel name is translated as a verb phrase meaning "Supports the add-on checker tool", not as the name "Supported add-ons checker".
    - Current: `รองรับเครื่องมือตรวจสอบส่วนเสริม`
    - Source: `Supported add-ons checker`
    - Suggest: `เครื่องมือตรวจสอบส่วนเสริมที่รองรับ`
    - In the source, "Supported" describes the add-ons, and the whole string names a notification channel. The Thai puts รองรับ ("supports") first, so it reads as a statement that something supports a checker tool. It is not the name of a checker for supported add-ons.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-th/strings.xml` — "VPN isn't working right now" is translated as "the VPN is not in use right now", which loses the fact that there is an error.
    - Current: `ขณะนี้ไม่ได้ใช้งาน VPN อยู่`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `ขณะนี้ VPN ไม่ทำงาน`
    - The source and developer comment describe an internal VPN error, meaning the VPN isn't working. The Thai says the VPN is simply not being used, which misstates why the user's location may be visible.
- `mozac_feature_importer_dialog_title` — `mozilla-mobile/android-components/components/feature/importer/src/main/res/values-th/strings.xml` — The loading dialog title reads as the command "Import bookmarks" rather than the in-progress "Importing bookmarks".
    - Current: `นำเข้าที่คั่นหน้า`
    - Source: `Importing bookmarks`
    - Suggest: `กำลังนำเข้าที่คั่นหน้า`
    - The comment says this is the title of a loading dialog, so it needs the progressive marker กำลัง to show the action is in progress.
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-th/strings.xml` — "Upload" is spelled อัพโหลด here, but the Upload button in the same dialog uses the standard spelling อัปโหลด.
    - Current: `อัพโหลดไฟล์?`
    - Source: `Upload files?`
    - Suggest: `อัปโหลดไฟล์?`
    - The Royal Institute spelling is อัปโหลด, and that is the spelling the positive button in this same folder-upload dialog uses. The title and the button should match.
- `mozac_feature_sitepermissions_do_not_ask_again_on_this_site4` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-th/strings.xml` — "Remember for this site" is rendered as "Remember this site", so the checkbox seems to save the site rather than the permission decision.
    - Current: `จดจำไซต์นี้`
    - Source: `Remember for this site`
    - Suggest: `จดจำสำหรับไซต์นี้`
    - The checkbox remembers the permission decision for this site (developer comment: it stops the prompt from showing again). The Thai drops "for" (สำหรับ) and makes the site the thing remembered, which reads like bookmarking it.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-th/strings.xml` — The in-progress title "Setting up summaries" was translated as the plain phrase "Set up summaries", so it no longer says the setup is happening now.
    - Current: `ตั้งค่าสรุป`
    - Source: `Setting up summaries`
    - Suggest: `กำลังตั้งค่าสรุป`
    - According to the developer comment, this is the title of the download-in-progress screen. Without "กำลัง", the Thai reads like the setup action or a settings label instead of saying that setup is underway.
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "clicks left" (remaining) is translated as คลิกซ้าย, which means "left-click" (the mouse button), not the number of clicks remaining.
    - Current: `คลิกซ้าย %1$d ทีเพื่อเปิดใช้งาน`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `เหลือการคลิกอีก %1$d ครั้งเพื่อเปิดใช้งาน`
    - The developer comment says %1$d is the number of long clicks left to enable the menu. The Thai tells the user to left-click %1$d times, which is a different instruction.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Straight double quotes are used where the locale convention and the source use curly quotes.
    - Current: `"https://" หรือ "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” หรือ “http://”`
    - The th convention is curly double quotes, and the en-US uses curly quotes.
- `addresses_pin` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Pin" is translated as the verb "to pin (a location)" when it should be India's postal code.
    - Current: `ปักหมุด`
    - Source: `Pin`
    - Suggest: `รหัส PIN`
    - The developer comment says this is the PIN (Postal Index Number), India's postal code. "ปักหมุด" means pinning something, like a map pin or pinned item, so the field label is wrong.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Department" is translated as a department in an organisation when it should be an administrative region.
    - Current: `แผนก`
    - Source: `Department`
    - Suggest: `จังหวัด`
    - The comment says this is the administrative division used in Colombia and Nicaragua. "แผนก" means a section of a company or organisation, not a region in an address.
- `addresses_prefecture` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Prefecture is rendered as "อำเภอ" (district), which is the wrong level of administrative division.
    - Current: `อำเภอ`
    - Source: `Prefecture`
    - Suggest: `จังหวัด`
    - The comment says a prefecture is a major top-level division, as in Japan. Thai normally calls these จังหวัด (e.g. จังหวัดโตเกียว). อำเภอ is a district, the level below the province, so the label names the wrong field.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Unblock" is rendered as "ปลดล็อก" (unlock), which clashes with "เลิกปิดกั้น" used for the same action in the block dialog.
    - Current: `ปลดล็อกคุณลักษณะ`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `เลิกปิดกั้นคุณลักษณะ`
    - This surface uses ปิดกั้น for 'block' and เลิกปิดกั้น for 'unblock' (ai_controls_block_dialog_body). ปลดล็อก means 'unlock', a different concept, so the term is inconsistent on the same screen.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says Firefox will never offer to translate sites "into" this language, but the source means sites written "in" this language.
    - Current: `แปลไซต์เป็นภาษานี้`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `แปลไซต์ที่เป็นภาษานี้`
    - The source "never offer to translate sites in this language" is about the language the page is written in. "แปลไซต์เป็นภาษานี้" means translating into this language, which turns the setting around.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says Firefox will offer to translate sites "into" this language, but the source means sites written "in" this language.
    - Current: `แปลไซต์เป็นภาษานี้`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `แปลไซต์ที่เป็นภาษานี้`
    - The source "offer to translate sites in this language" is about the page's own language. "เป็นภาษานี้" makes it the target language of the translation instead.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Never" (never auto-close tabs) is translated as "กำหนดเอง" (custom/set by yourself).
    - Current: `กำหนดเอง`
    - Source: `Never`
    - Suggest: `ไม่ปิดอัตโนมัติ`
    - The option means tabs are never closed automatically. "กำหนดเอง" means "custom", which reads like a settings choice that should open more options. It doesn't say "never".
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The button that opens a collection's tabs is translated as a noun phrase, "tabs that are open", not an action.
    - Current: `แท็บที่เปิด`
    - Source: `Open tabs`
    - Suggest: `เปิดแท็บ`
    - The developer comment says this is a button to open the tabs of the selected collection, so it needs the verb "open". "แท็บที่เปิด" means "open tabs" as in tabs that are currently open.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "locale" is rendered as ตำแหน่ง (position/location) instead of the locale term รูปแบบภาษา used on the same debug addresses surface.
    - Current: `สำหรับตำแหน่งที่เลือก`
    - Source: `Add new address for selected locale`
    - Suggest: `สำหรับรูปแบบภาษาที่เลือก`
    - The source means a language/region locale, not a location. The adjacent header debug_drawer_addresses_debug_locales_header translates 'locales' as รูปแบบภาษา, so this string is both inconsistent with it and misleading.
- `ip_protection_connection_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "อีก" (again) is misspelled as "อี่ก", with a stray tone mark (mai ek).
    - Current: `อี่กครั้ง`
    - Source: `Couldn’t connect to VPN. Try again in a few minutes.`
    - Suggest: `อีกครั้ง`
    - The source says "Try again". The Thai word for "again" is spelled อีก, and อี่ก is not a valid spelling.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'Share how you discovered Firefox, and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That implies usage details go to marketing partners, which is more data than the product says it shares.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That claims a wider data share with marketing partners than the source states.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai says how you use it is shared, so it describes sharing usage details with marketing partners.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai claims usage details are shared. The developer comment stresses that data practices stay the same, so this broader claim misleads on a consent checkbox.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "won't sell you out" (betray you) is translated as "won't abandon you".
    - Current: `ไม่ทอดทิ้งคุณ`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `ไม่ทรยศคุณ`
    - "Sell you out" means to betray, and it also hints at not selling your data. "ทอดทิ้ง" means to abandon, which is a different idea.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The confirm button says "tabs that are open" (a noun phrase) instead of telling the user to open the tabs.
    - Current: `แท็บที่เปิด`
    - Source: `Open tabs`
    - Suggest: `เปิดแท็บ`
    - The developer comment says this is the dialog button that confirms opening all the tabs, so "Open tabs" is an instruction (open the tabs). "แท็บที่เปิด" means "tabs that are open", which doesn't work as a confirm action.
- `pbm_authentication_unlock_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Unlock" is spelled ปลดล็อค here but ปลดล็อก on the Unlock button on the same screen.
    - Current: `ปลดล็อคแท็บส่วนตัว`
    - Source: `Unlock private tabs`
    - Suggest: `ปลดล็อกแท็บส่วนตัว`
    - The Unlock button on the same private-tabs screen (pbm_authentication_unlock) uses ปลดล็อก, and the screen-lock strings use ล็อก. ล็อก is the standard Royal Institute spelling, so ล็อค is the odd one out on this surface.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "secure DNS" is left in English here, but every other DNS over HTTPS string translates it as "DNS ที่เชื่อถือได้".
    - Current: `ผู้ให้บริการ secure DNS`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `ผู้ให้บริการ DNS ที่เชื่อถือได้`
    - These strings all appear on the same DNS over HTTPS settings screens. The term is translated as "DNS ที่เชื่อถือได้" in the other strings, including increased_protection_info_2, the summaries and the max protection bullets, so leaving it untranslated in this one bullet is inconsistent.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The quantifier "many of" is dropped, so the Thai says Firefox protects against the most common trackers as a whole rather than many of them.
    - Current: `ปกป้องคุณจากตัวติดตามที่พบบ่อยที่สุดซึ่งติดตาม`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `ปกป้องคุณจากตัวติดตามจำนวนมากที่พบบ่อยที่สุดซึ่งติดตาม`
    - The source says the app protects from 'many of the most common trackers', which is deliberately limited. The Thai drops the limit and implies protection from all of the most common trackers, which is a broader claim about the product.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Straight double quotes are used where the locale convention and the source use curly quotes.
    - Current: `"ออก"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“ออก”`
    - The th convention is curly double quotes, and the en-US source uses “Quit” with curly quotes.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "That you use it" is rendered as "how you use it" (อย่างไร), so the setting now describes sharing usage details.
    - Current: `และคุณใช้มันอย่างไร`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `และการที่คุณใช้งาน Firefox อยู่`
    - The developer comment says explicitly that "that you use it" means the user still uses Firefox after installing it, not what they use it for. The Thai says Firefox shares how the user uses it with marketing partners, which is a wider data-sharing claim than the source makes.
- `preferences_passwords_autofill2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The word "in" (ใน) is missing, so the label reads "autofill Firefox" instead of "autofill in Firefox".
    - Current: `กรอกอัตโนมัติ %1$s`
    - Source: `Autofill in %1$s`
    - Suggest: `กรอกอัตโนมัติใน %1$s`
    - The source is "Autofill in %1$s". Without ใน, the app name becomes the object of the autofill.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The title is translated as a noun phrase meaning "settings for search" instead of the verb phrase "search the settings".
    - Current: `การตั้งค่าการค้นหา`
    - Source: `Search settings`
    - Suggest: `ค้นหาการตั้งค่า`
    - The developer comment says "Search" is a verb here: the screen is for searching through settings. "การตั้งค่าการค้นหา" reads as "search settings" in the sense of search preferences, which is a different screen. The related content description already uses ค้นหาการตั้งค่า.
- `setup_checklist_task_search_widget_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Search widget" is rendered as เครื่องมือค้นหา, the standard Thai term for "search engine".
    - Current: `สำรวจเครื่องมือค้นหา`
    - Source: `Explore search widget`
    - Suggest: `สำรวจวิดเจ็ตการค้นหา`
    - The task is about the home-screen search widget. In Thai UI, เครื่องมือค้นหา means "search engine", which points users to a different feature. Widget is normally rendered as วิดเจ็ต.
- `synced_tabs_reauth` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "รับรอบ" is misspelled; it should be "รับรอง" (authenticate).
    - Current: `รับรอบความถูกต้อง`
    - Source: `Please re-authenticate.`
    - Suggest: `รับรองความถูกต้อง`
    - In Thai, "authenticate" is "รับรองความถูกต้อง". "รับรอบ" is a typo and means nothing here, so the message reads wrong.
- `unsubmitted_crash_dialog_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Crash report" is rendered as "รายงานข้อผิดพลาด" (error report), unlike "รายงานข้อขัดข้อง" in the same dialog's body.
    - Current: `ส่งรายงานข้อผิดพลาด`
    - Source: `Send crash report`
    - Suggest: `ส่งรายงานข้อขัดข้อง`
    - The dialog body (unsubmitted_crash_dialog_body) and the other crash strings use ข้อขัดข้อง for 'crash'. ข้อผิดพลาด means 'error', so the button label is inconsistent with the body on the same surface.
- `unsubmitted_crash_dialog_checkbox_label` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Crash reports" is rendered as "รายงานความผิดพลาด" (error reports), unlike "รายงานข้อขัดข้อง" in the same dialog.
    - Current: `รายงานความผิดพลาด`
    - Source: `Automatically send crash reports`
    - Suggest: `รายงานข้อขัดข้อง`
    - The same dialog's body text calls a crash report รายงานข้อขัดข้อง. ความผิดพลาด means 'error/mistake', so the checkbox label uses a different term on the same surface.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "check out" (complete a purchase) is translated as "ดำเนินการต่อ" (continue/proceed).
    - Current: `ดำเนินการต่อ`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `ทำรายการสั่งซื้อ`
    - In 'Can’t pay, check out or shop', 'check out' means completing an online purchase at checkout. "ดำเนินการต่อ" just means 'continue', so this option no longer clearly describes a checkout failure.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Continuing could be risky" is rendered as "you should not continue".
    - Current: `และคุณไม่ควรดำเนินการต่อ`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `และการดำเนินการต่ออาจมีความเสี่ยง`
    - The source says continuing could be risky. The translation tells the user not to continue, which is an instruction and stronger than the original statement of possible risk.
- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Shortcuts" is rendered as "คำสั่งลัด", but the matching Add item uses "ทางลัด".
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Remove from Shortcuts`
    - Suggest: `ลบออกจากทางลัด`
    - menu_add_to_shortcuts and firstrun_shortcut_title both use ทางลัด for the same home-screen shortcuts feature. The Add and Remove menu items should match.
- `notification_erase_text_android_14_1` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Erase browsing history" is rendered as "ลบประวัติการเรียกดู", while the title of the same notification and the rest of the app use "ล้างประวัติการท่องเว็บ".
    - Current: `ลบประวัติการเรียกดูของคุณ`
    - Source: `Tap or swipe this notification to securely erase your browsing history.`
    - Suggest: `ล้างประวัติการท่องเว็บของคุณ`
    - The notification title (notification_erase_title_android_14) and the other erase strings use ล้างประวัติการท่องเว็บ. Using a different term in the body of the same notification is inconsistent.
- `onboarding_second_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Browser" is misspelled as บราวเซอร์ instead of the standard เบราว์เซอร์.
    - Current: `บราวเซอร์อื่นๆ`
    - Source: `%1$s isn’t like other browsers`
    - Suggest: `เบราว์เซอร์อื่นๆ`
    - The standard Thai spelling of "browser", which Mozilla's Thai products also use, is เบราว์เซอร์. บราวเซอร์ is a common misspelling.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — 'Unlock' is spelled ปลดล็อค here, but the summary on the same preference uses the standard spelling ปลดล็อก.
    - Current: `ปลดล็อค`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `ปลดล็อก`
    - The standard Thai spelling of 'lock' is ล็อก, and preference_security_biometric_summary2 already uses ปลดล็อก. The title and its summary appear together, so they should match.

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
| Strings | 2,685 |
| Missing strings | 113 |
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

**113 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — 82
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-th/strings.xml` — 19
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-th/strings.xml` — 8
- `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — 2
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values-th/strings.xml` — 1
- `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 2 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (51)

> **Reads as a deliberate edit (6).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'Share how you discovered Firefox, and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That implies usage details go to marketing partners, which is more data than the product says it shares.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That claims a wider data share with marketing partners than the source states.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai says how you use it is shared, so it describes sharing usage details with marketing partners.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai claims usage details are shared. The developer comment stresses that data practices stay the same, so this broader claim misleads on a consent checkbox.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The quantifier "many of" is dropped, so the Thai says Firefox protects against the most common trackers as a whole rather than many of them.
    - Current: `ปกป้องคุณจากตัวติดตามที่พบบ่อยที่สุดซึ่งติดตาม`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `ปกป้องคุณจากตัวติดตามจำนวนมากที่พบบ่อยที่สุดซึ่งติดตาม`
    - The source says the app protects from 'many of the most common trackers', which is deliberately limited. The Thai drops the limit and implies protection from all of the most common trackers, which is a broader claim about the product.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "That you use it" is rendered as "how you use it" (อย่างไร), so the setting now describes sharing usage details.
    - Current: `และคุณใช้มันอย่างไร`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `และการที่คุณใช้งาน Firefox อยู่`
    - The developer comment says explicitly that "that you use it" means the user still uses Firefox after installing it, not what they use it for. The Thai says Firefox shares how the user uses it with marketing partners, which is a wider data-sharing claim than the source makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 27 |
| 3 | Degraded language (grammar, spelling, terminology) | 20 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The source's "device's network connection" is translated as the computer's network connection.
    - Current: `ตรวจสอบการเชื่อมต่อเครือข่ายของคอมพิวเตอร์`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `ตรวจสอบการเชื่อมต่อเครือข่ายของอุปกรณ์`
    - The source says "device", and the other error pages in this file use อุปกรณ์. On Android, "computer" is the wrong thing to name.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The source's "your device or network" is translated as "your computer or network".
    - Current: `คอมพิวเตอร์หรือเครือข่ายของคุณ`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `อุปกรณ์หรือเครือข่ายของคุณ`
    - The source says "device", not "computer". This is a mobile browser, and the other error pages here use อุปกรณ์.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — The clause "but the proxy refused a connection" is missing, so the error page never states what went wrong.
    - Current: `เบราว์เซอร์ถูกกำหนดค่าให้ใช้เซิร์ฟเวอร์พร็อกซี{ </p> }`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `เบราว์เซอร์ถูกกำหนดค่าให้ใช้เซิร์ฟเวอร์พร็อกซี แต่พร็อกซีปฏิเสธการเชื่อมต่อ{ </p> }`
    - The source says the browser is set up to use a proxy but the proxy refused the connection. The Thai keeps only the first half, which removes the actual error.
- `mozac_feature_addons_permissions_all_domain_count_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-th/strings.xml` — Number placed after โดเมน reads as 'domain number N' rather than 'N domains'.
    - Current: `ไซต์ในโดเมน %1$d`
    - Source: `{$quantity ->} [other] Access your data for sites in %1$d domains`
    - Suggest: `ไซต์ใน %1$d โดเมน`
    - Source says sites in %1$d domains (a count); in Thai 'โดเมน %1$d' reads as a domain identified by number, while a count needs number + classifier 'ใน %1$d โดเมน'.
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-th/strings.xml` — The channel name is translated as a verb phrase meaning "Supports the add-on checker tool", not as the name "Supported add-ons checker".
    - Current: `รองรับเครื่องมือตรวจสอบส่วนเสริม`
    - Source: `Supported add-ons checker`
    - Suggest: `เครื่องมือตรวจสอบส่วนเสริมที่รองรับ`
    - In the source, "Supported" describes the add-ons, and the whole string names a notification channel. The Thai puts รองรับ ("supports") first, so it reads as a statement that something supports a checker tool. It is not the name of a checker for supported add-ons.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-th/strings.xml` — "VPN isn't working right now" is translated as "the VPN is not in use right now", which loses the fact that there is an error.
    - Current: `ขณะนี้ไม่ได้ใช้งาน VPN อยู่`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `ขณะนี้ VPN ไม่ทำงาน`
    - The source and developer comment describe an internal VPN error, meaning the VPN isn't working. The Thai says the VPN is simply not being used, which misstates why the user's location may be visible.
- `mozac_feature_sitepermissions_do_not_ask_again_on_this_site4` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-th/strings.xml` — "Remember for this site" is rendered as "Remember this site", so the checkbox seems to save the site rather than the permission decision.
    - Current: `จดจำไซต์นี้`
    - Source: `Remember for this site`
    - Suggest: `จดจำสำหรับไซต์นี้`
    - The checkbox remembers the permission decision for this site (developer comment: it stops the prompt from showing again). The Thai drops "for" (สำหรับ) and makes the site the thing remembered, which reads like bookmarking it.
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "clicks left" (remaining) is translated as คลิกซ้าย, which means "left-click" (the mouse button), not the number of clicks remaining.
    - Current: `คลิกซ้าย %1$d ทีเพื่อเปิดใช้งาน`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `เหลือการคลิกอีก %1$d ครั้งเพื่อเปิดใช้งาน`
    - The developer comment says %1$d is the number of long clicks left to enable the menu. The Thai tells the user to left-click %1$d times, which is a different instruction.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Department" is translated as a department in an organisation when it should be an administrative region.
    - Current: `แผนก`
    - Source: `Department`
    - Suggest: `จังหวัด`
    - The comment says this is the administrative division used in Colombia and Nicaragua. "แผนก" means a section of a company or organisation, not a region in an address.
- `addresses_pin` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Pin" is translated as the verb "to pin (a location)" when it should be India's postal code.
    - Current: `ปักหมุด`
    - Source: `Pin`
    - Suggest: `รหัส PIN`
    - The developer comment says this is the PIN (Postal Index Number), India's postal code. "ปักหมุด" means pinning something, like a map pin or pinned item, so the field label is wrong.
- `addresses_prefecture` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Prefecture is rendered as "อำเภอ" (district), which is the wrong level of administrative division.
    - Current: `อำเภอ`
    - Source: `Prefecture`
    - Suggest: `จังหวัด`
    - The comment says a prefecture is a major top-level division, as in Japan. Thai normally calls these จังหวัด (e.g. จังหวัดโตเกียว). อำเภอ is a district, the level below the province, so the label names the wrong field.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says Firefox will never offer to translate sites "into" this language, but the source means sites written "in" this language.
    - Current: `แปลไซต์เป็นภาษานี้`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `แปลไซต์ที่เป็นภาษานี้`
    - The source "never offer to translate sites in this language" is about the language the page is written in. "แปลไซต์เป็นภาษานี้" means translating into this language, which turns the setting around.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says Firefox will offer to translate sites "into" this language, but the source means sites written "in" this language.
    - Current: `แปลไซต์เป็นภาษานี้`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `แปลไซต์ที่เป็นภาษานี้`
    - The source "offer to translate sites in this language" is about the page's own language. "เป็นภาษานี้" makes it the target language of the translation instead.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Never" (never auto-close tabs) is translated as "กำหนดเอง" (custom/set by yourself).
    - Current: `กำหนดเอง`
    - Source: `Never`
    - Suggest: `ไม่ปิดอัตโนมัติ`
    - The option means tabs are never closed automatically. "กำหนดเอง" means "custom", which reads like a settings choice that should open more options. It doesn't say "never".
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The button that opens a collection's tabs is translated as a noun phrase, "tabs that are open", not an action.
    - Current: `แท็บที่เปิด`
    - Source: `Open tabs`
    - Suggest: `เปิดแท็บ`
    - The developer comment says this is a button to open the tabs of the selected collection, so it needs the verb "open". "แท็บที่เปิด" means "open tabs" as in tabs that are currently open.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'Share how you discovered Firefox, and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That implies usage details go to marketing partners, which is more data than the product says it shares.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says 'and that you use it'. 'คุณใช้มันอย่างไร' means 'how you use it'. That claims a wider data share with marketing partners than the source states.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "won't sell you out" (betray you) is translated as "won't abandon you".
    - Current: `ไม่ทอดทิ้งคุณ`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `ไม่ทรยศคุณ`
    - "Sell you out" means to betray, and it also hints at not selling your data. "ทอดทิ้ง" means to abandon, which is a different idea.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai says how you use it is shared, so it describes sharing usage details with marketing partners.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
    - The source says only the fact that you use Firefox is shared. The Thai claims usage details are shared. The developer comment stresses that data practices stay the same, so this broader claim misleads on a consent checkbox.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The confirm button says "tabs that are open" (a noun phrase) instead of telling the user to open the tabs.
    - Current: `แท็บที่เปิด`
    - Source: `Open tabs`
    - Suggest: `เปิดแท็บ`
    - The developer comment says this is the dialog button that confirms opening all the tabs, so "Open tabs" is an instruction (open the tabs). "แท็บที่เปิด" means "tabs that are open", which doesn't work as a confirm action.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The quantifier "many of" is dropped, so the Thai says Firefox protects against the most common trackers as a whole rather than many of them.
    - Current: `ปกป้องคุณจากตัวติดตามที่พบบ่อยที่สุดซึ่งติดตาม`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `ปกป้องคุณจากตัวติดตามจำนวนมากที่พบบ่อยที่สุดซึ่งติดตาม`
    - The source says the app protects from 'many of the most common trackers', which is deliberately limited. The Thai drops the limit and implies protection from all of the most common trackers, which is a broader claim about the product.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "That you use it" is rendered as "how you use it" (อย่างไร), so the setting now describes sharing usage details.
    - Current: `และคุณใช้มันอย่างไร`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `และการที่คุณใช้งาน Firefox อยู่`
    - The developer comment says explicitly that "that you use it" means the user still uses Firefox after installing it, not what they use it for. The Thai says Firefox shares how the user uses it with marketing partners, which is a wider data-sharing claim than the source makes.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The title is translated as a noun phrase meaning "settings for search" instead of the verb phrase "search the settings".
    - Current: `การตั้งค่าการค้นหา`
    - Source: `Search settings`
    - Suggest: `ค้นหาการตั้งค่า`
    - The developer comment says "Search" is a verb here: the screen is for searching through settings. "การตั้งค่าการค้นหา" reads as "search settings" in the sense of search preferences, which is a different screen. The related content description already uses ค้นหาการตั้งค่า.
- `setup_checklist_task_search_widget_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Search widget" is rendered as เครื่องมือค้นหา, the standard Thai term for "search engine".
    - Current: `สำรวจเครื่องมือค้นหา`
    - Source: `Explore search widget`
    - Suggest: `สำรวจวิดเจ็ตการค้นหา`
    - The task is about the home-screen search widget. In Thai UI, เครื่องมือค้นหา means "search engine", which points users to a different feature. Widget is normally rendered as วิดเจ็ต.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "check out" (complete a purchase) is translated as "ดำเนินการต่อ" (continue/proceed).
    - Current: `ดำเนินการต่อ`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `ทำรายการสั่งซื้อ`
    - In 'Can’t pay, check out or shop', 'check out' means completing an online purchase at checkout. "ดำเนินการต่อ" just means 'continue', so this option no longer clearly describes a checkout failure.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Continuing could be risky" is rendered as "you should not continue".
    - Current: `และคุณไม่ควรดำเนินการต่อ`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `และการดำเนินการต่ออาจมีความเสี่ยง`
    - The source says continuing could be risky. The translation tells the user not to continue, which is an instruction and stronger than the original statement of possible risk.

### C. Grammar, agreement & spelling

- `mozac_feature_importer_dialog_title` — `mozilla-mobile/android-components/components/feature/importer/src/main/res/values-th/strings.xml` — The loading dialog title reads as the command "Import bookmarks" rather than the in-progress "Importing bookmarks".
    - Current: `นำเข้าที่คั่นหน้า`
    - Source: `Importing bookmarks`
    - Suggest: `กำลังนำเข้าที่คั่นหน้า`
    - The comment says this is the title of a loading dialog, so it needs the progressive marker กำลัง to show the action is in progress.
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-th/strings.xml` — "Upload" is spelled อัพโหลด here, but the Upload button in the same dialog uses the standard spelling อัปโหลด.
    - Current: `อัพโหลดไฟล์?`
    - Source: `Upload files?`
    - Suggest: `อัปโหลดไฟล์?`
    - The Royal Institute spelling is อัปโหลด, and that is the spelling the positive button in this same folder-upload dialog uses. The title and the button should match.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-th/strings.xml` — The in-progress title "Setting up summaries" was translated as the plain phrase "Set up summaries", so it no longer says the setup is happening now.
    - Current: `ตั้งค่าสรุป`
    - Source: `Setting up summaries`
    - Suggest: `กำลังตั้งค่าสรุป`
    - According to the developer comment, this is the title of the download-in-progress screen. Without "กำลัง", the Thai reads like the setup action or a settings label instead of saying that setup is underway.
- `ip_protection_connection_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "อีก" (again) is misspelled as "อี่ก", with a stray tone mark (mai ek).
    - Current: `อี่กครั้ง`
    - Source: `Couldn’t connect to VPN. Try again in a few minutes.`
    - Suggest: `อีกครั้ง`
    - The source says "Try again". The Thai word for "again" is spelled อีก, and อี่ก is not a valid spelling.
- `pbm_authentication_unlock_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Unlock" is spelled ปลดล็อค here but ปลดล็อก on the Unlock button on the same screen.
    - Current: `ปลดล็อคแท็บส่วนตัว`
    - Source: `Unlock private tabs`
    - Suggest: `ปลดล็อกแท็บส่วนตัว`
    - The Unlock button on the same private-tabs screen (pbm_authentication_unlock) uses ปลดล็อก, and the screen-lock strings use ล็อก. ล็อก is the standard Royal Institute spelling, so ล็อค is the odd one out on this surface.
- `preferences_passwords_autofill2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — The word "in" (ใน) is missing, so the label reads "autofill Firefox" instead of "autofill in Firefox".
    - Current: `กรอกอัตโนมัติ %1$s`
    - Source: `Autofill in %1$s`
    - Suggest: `กรอกอัตโนมัติใน %1$s`
    - The source is "Autofill in %1$s". Without ใน, the app name becomes the object of the autofill.
- `synced_tabs_reauth` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "รับรอบ" is misspelled; it should be "รับรอง" (authenticate).
    - Current: `รับรอบความถูกต้อง`
    - Source: `Please re-authenticate.`
    - Suggest: `รับรองความถูกต้อง`
    - In Thai, "authenticate" is "รับรองความถูกต้อง". "รับรอบ" is a typo and means nothing here, so the message reads wrong.
- `onboarding_second_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Browser" is misspelled as บราวเซอร์ instead of the standard เบราว์เซอร์.
    - Current: `บราวเซอร์อื่นๆ`
    - Source: `%1$s isn’t like other browsers`
    - Suggest: `เบราว์เซอร์อื่นๆ`
    - The standard Thai spelling of "browser", which Mozilla's Thai products also use, is เบราว์เซอร์. บราวเซอร์ is a common misspelling.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — 'Unlock' is spelled ปลดล็อค here, but the summary on the same preference uses the standard spelling ปลดล็อก.
    - Current: `ปลดล็อค`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `ปลดล็อก`
    - The standard Thai spelling of 'lock' is ล็อก, and preference_security_biometric_summary2 already uses ปลดล็อก. The title and its summary appear together, so they should match.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "device" is translated as "computer" (คอมพิวเตอร์) in a mobile app.
    - Current: `คอมพิวเตอร์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `อุปกรณ์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - The source says "device". This is an Android app, and other strings in this batch translate it as อุปกรณ์.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "your device" is translated as "your computer" (คอมพิวเตอร์ของคุณ).
    - Current: `ไม่ใช่คอมพิวเตอร์ของคุณ`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `ไม่ใช่อุปกรณ์ของคุณ`
    - The source says "not your device". The app runs on mobile devices, and the batch elsewhere uses อุปกรณ์.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-th/strings.xml` — "device" is translated as "computer" (คอมพิวเตอร์) in a mobile app.
    - Current: `คอมพิวเตอร์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `อุปกรณ์เชื่อมต่อกับเครือข่ายที่ใช้งานได้หรือไม่?`
    - The source says "device". Other strings in this batch translate it as อุปกรณ์.
- `mozac_compose_base_link_text_links_available` — `mozilla-mobile/android-components/components/compose/base/src/main/res/values-th/strings.xml` — "Link" is spelled ลิงค์ here but ลิงก์ in the title string next to it in the same LinkText component.
    - Current: `ลิงค์`
    - Source: `Links available`
    - Suggest: `ลิงก์`
    - Two strings in the same LinkText component spell "link" differently. ลิงก์ is the standard spelling (Royal Institute) and is the one the links dialog title uses, so ลิงค์ should be changed to match.
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Unblock" is rendered as "ปลดล็อก" (unlock), which clashes with "เลิกปิดกั้น" used for the same action in the block dialog.
    - Current: `ปลดล็อกคุณลักษณะ`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `เลิกปิดกั้นคุณลักษณะ`
    - This surface uses ปิดกั้น for 'block' and เลิกปิดกั้น for 'unblock' (ai_controls_block_dialog_body). ปลดล็อก means 'unlock', a different concept, so the term is inconsistent on the same screen.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "locale" is rendered as ตำแหน่ง (position/location) instead of the locale term รูปแบบภาษา used on the same debug addresses surface.
    - Current: `สำหรับตำแหน่งที่เลือก`
    - Source: `Add new address for selected locale`
    - Suggest: `สำหรับรูปแบบภาษาที่เลือก`
    - The source means a language/region locale, not a location. The adjacent header debug_drawer_addresses_debug_locales_header translates 'locales' as รูปแบบภาษา, so this string is both inconsistent with it and misleading.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "secure DNS" is left in English here, but every other DNS over HTTPS string translates it as "DNS ที่เชื่อถือได้".
    - Current: `ผู้ให้บริการ secure DNS`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `ผู้ให้บริการ DNS ที่เชื่อถือได้`
    - These strings all appear on the same DNS over HTTPS settings screens. The term is translated as "DNS ที่เชื่อถือได้" in the other strings, including increased_protection_info_2, the summaries and the max protection bullets, so leaving it untranslated in this one bullet is inconsistent.
- `unsubmitted_crash_dialog_checkbox_label` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Crash reports" is rendered as "รายงานความผิดพลาด" (error reports), unlike "รายงานข้อขัดข้อง" in the same dialog.
    - Current: `รายงานความผิดพลาด`
    - Source: `Automatically send crash reports`
    - Suggest: `รายงานข้อขัดข้อง`
    - The same dialog's body text calls a crash report รายงานข้อขัดข้อง. ความผิดพลาด means 'error/mistake', so the checkbox label uses a different term on the same surface.
- `unsubmitted_crash_dialog_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — "Crash report" is rendered as "รายงานข้อผิดพลาด" (error report), unlike "รายงานข้อขัดข้อง" in the same dialog's body.
    - Current: `ส่งรายงานข้อผิดพลาด`
    - Source: `Send crash report`
    - Suggest: `ส่งรายงานข้อขัดข้อง`
    - The dialog body (unsubmitted_crash_dialog_body) and the other crash strings use ข้อขัดข้อง for 'crash'. ข้อผิดพลาด means 'error', so the button label is inconsistent with the body on the same surface.
- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Shortcuts" is rendered as "คำสั่งลัด", but the matching Add item uses "ทางลัด".
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Remove from Shortcuts`
    - Suggest: `ลบออกจากทางลัด`
    - menu_add_to_shortcuts and firstrun_shortcut_title both use ทางลัด for the same home-screen shortcuts feature. The Add and Remove menu items should match.
- `notification_erase_text_android_14_1` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Erase browsing history" is rendered as "ลบประวัติการเรียกดู", while the title of the same notification and the rest of the app use "ล้างประวัติการท่องเว็บ".
    - Current: `ลบประวัติการเรียกดูของคุณ`
    - Source: `Tap or swipe this notification to securely erase your browsing history.`
    - Suggest: `ล้างประวัติการท่องเว็บของคุณ`
    - The notification title (notification_erase_title_android_14) and the other erase strings use ล้างประวัติการท่องเว็บ. Using a different term in the body of the same notification is inconsistent.

### E. Typography, punctuation & spacing

- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `ที่อยู่เว็บต้องมี "https://" หรือ "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Straight double quotes are used where the locale convention and the source use curly quotes.
    - Current: `"https://" หรือ "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” หรือ “http://”`
    - The th convention is curly double quotes, and the en-US uses curly quotes.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `ลบข้อมูลการเรียกดูโดยอัตโนมัติเมื่อคุณเลือก "ออก" จากเมนูหลัก`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-th/strings.xml` — Straight double quotes are used where the locale convention and the source use curly quotes.
    - Current: `"ออก"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“ออก”`
    - The th convention is curly double quotes, and the en-US source uses “Quit” with curly quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/th/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
