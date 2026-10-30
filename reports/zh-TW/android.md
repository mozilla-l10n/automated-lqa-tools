# Firefox for Android l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 2,553 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for zh-TW: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Strings | 2,553 |
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

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1071 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (63)

> **Reads as a deliberate edit (10).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "and that you use it" is rendered as "how you use it", which describes a much wider data share.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source shares only the fact that the user uses Firefox. The translation says Mozilla shares how the user uses Firefox, which is a much wider disclosure of usage data.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "and that you use it" is rendered as "how you use it", which describes a much wider data share.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source shares only the fact that the user uses Firefox, not how they use it. The translation describes sharing usage details with marketing partners.
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns where the user came from, but the source says Mozilla tells that platform the user uses Firefox.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla informs the external platform (the referring app, site, store or campaign, per the developer comment). The translation hides that information is sent to a third party.
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation says only that Mozilla learns the source, so a third party receiving data is hidden.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation hides that data goes to a third party.
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation hides that data goes to a third party.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "that you use it" is translated as "how you use it", which claims usage details are shared with marketing partners.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source says users share how they discovered Firefox and the fact that they use it. The translation says they share how they use it, which describes wider data sharing than the product does.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "that you use it" is translated as "how you use it", which claims usage details are shared with marketing partners.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source only shares the fact that the user uses Firefox. The developer comment stresses that this setting does not increase data collection, but the translation says the user's usage details are shared.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "many of the most common trackers" becomes "common trackers", which reads as protection against all common trackers.
    - Current: `%s 不讓常見的追蹤器記錄您的上網行為。`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `%s 可保護您免於被許多最常見的追蹤器記錄您的上網行為。`
    - The source limits the claim to "many of" the most common trackers. The translation drops that limit and promises wider protection than the source makes.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The text says the user shares how they use Firefox, but the source means only that they use it.
    - Current: `以及是如何使用`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The developer comment says 'that you use it' means only that the user keeps using Firefox after installing it, and does not mean Firefox tracks their usage. The translation turns this into sharing how the user uses Firefox, which describes a wider data collection than the product performs.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 31 |
| 3 | Degraded language (grammar, spelling, terminology) | 17 |
| 4 | Cosmetic (typography, spacing) | 15 |

### A. Functional, markup, variables & plurals

- `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `downloads_delete_dialog_title` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 要刪除檔案嗎？ [other] 要刪除 %d 個檔案嗎？`
    - Source: `{$quantity ->} [one] Delete file? [other] Delete %d files?`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `nova_onboarding_customize_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `nova_onboarding_customize_prompt_body` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。 [other] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。`
    - Source: `{$quantity ->} [one] %1$s blocked %2$,d tracker while you roamed the web. [other] %1$s blocked %2$,d trackers while you roamed the web.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rTW/strings.xml` — The translation tells the user to connect to another device, not to try connecting from another device.
    - Current: `試著連線到其他裝置`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `試著改用其他裝置連線`
    - The source "Try connecting on a different device" suggests going online with a different device. 「連線到其他裝置」 means connecting to a different device, which changes the troubleshooting step.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-zh-rTW/strings.xml` — "your location may be visible" is rendered as "your actual location may be tracked by someone".
    - Current: `您實際的所在位置可能會被人追蹤`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `您的所在位置可能會被看見`
    - The source only warns that your location may be visible (exposed) while the VPN is down. The translation claims someone may actively track your location, which is not what the source says.
- `browser_menu_remove_from_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The menu button is translated as a past-tense status message ("Removed from shortcuts") instead of an action.
    - Current: `已從捷徑刪除`
    - Source: `Remove from shortcuts`
    - Suggest: `從捷徑移除`
    - The source is an imperative button label, "Remove from shortcuts", that removes a shortcut from the home screen. 已從捷徑刪除 reads as a message that the action has already happened, so it's wrong as a label.
- `download_languages_default_system_language_require_preference` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "required" is rendered as 必填 (a must-fill form field), not as "necessary" for a language package.
    - Current: `必填`
    - Source: `required`
    - Suggest: `必要`
    - The developer comment says this label marks a language package the translation feature needs in order to work. 必填 is only used for form fields that must be filled in, so it makes no sense next to a language name and file size.
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The translation drops "tracking": it says cookies set by known websites during redirects, not cookies set by redirects to known tracking websites.
    - Current: `清除已知網站在重新導向時所設定的 Cookie。`
    - Source: `Clears cookies set by redirects to known tracking websites.`
    - Suggest: `清除重新導向至已知追蹤網站時所設定的 Cookie。`
    - The source limits the feature to redirects to known tracking websites. The translation drops 追蹤 (tracking), so it now refers to known websites in general and misdescribes what the feature clears.
- `home_bookmarks_menu_item_remove` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "Remove" (from the home screen section) is rendered as 刪除 "delete", implying the bookmark itself is deleted.
    - Current: `刪除`
    - Source: `Remove`
    - Suggest: `移除`
    - The developer comment says the action removes a recently saved bookmark from the home screen. It does not delete the bookmark, but 刪除 tells the user it does.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "and that you use it" is rendered as "how you use it", which describes a much wider data share.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source shares only the fact that the user uses Firefox. The translation says Mozilla shares how the user uses Firefox, which is a much wider disclosure of usage data.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "and that you use it" is rendered as "how you use it", which describes a much wider data share.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source shares only the fact that the user uses Firefox, not how they use it. The translation describes sharing usage details with marketing partners.
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns where the user came from, but the source says Mozilla tells that platform the user uses Firefox.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla informs the external platform (the referring app, site, store or campaign, per the developer comment). The translation hides that information is sent to a third party.
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation says only that Mozilla learns the source, so a third party receiving data is hidden.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation hides that data goes to a third party.
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The data flow is reversed: the Chinese says Mozilla learns the download platform, but the source says Mozilla informs that platform.
    - Current: `讓 Mozilla 知道您是從哪個平台下載 Firefox 的`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `讓 Mozilla 告知引導您來到 Firefox 的平台您正在使用 Firefox`
    - In the source, Mozilla tells the referring platform that the user uses Firefox. The translation hides that data goes to a third party.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "that you use it" is translated as "how you use it", which claims usage details are shared with marketing partners.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source says users share how they discovered Firefox and the fact that they use it. The translation says they share how they use it, which describes wider data sharing than the product does.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "that you use it" is translated as "how you use it", which claims usage details are shared with marketing partners.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The source only shares the fact that the user uses Firefox. The developer comment stresses that this setting does not increase data collection, but the translation says the user's usage details are shared.
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Translation says Firefox opens links found inside apps, instead of Firefox opening links in (other) apps.
    - Current: `您可以設定使用 %1$s 自動開啟各應用程式當中的鏈結。`
    - Source: `You can set %1$s to automatically open links in apps.`
    - Suggest: `您可以設定讓 %1$s 自動於應用程式中開啟鏈結。`
    - Source means Firefox can be set to hand links off to external apps automatically; target reads as Firefox automatically opening the links contained within apps, a different feature.
- `preference_doh_increased_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Translation drops the part about the user controlling when secure DNS is used and only covers choosing a provider.
    - Current: `由您自行決定要使用哪個提供者的安全 DNS。`
    - Source: `You control when to use secure DNS and choose your provider.`
    - Suggest: `由您決定何時使用安全 DNS，並選擇提供者。`
    - The source says 'You control when to use secure DNS and choose your provider': two things, timing and provider. The translation only says the user picks which provider's secure DNS to use. That loses the 'when', which is what separates this option from Default Protection.
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "many of the most common trackers" becomes "common trackers", which reads as protection against all common trackers.
    - Current: `%s 不讓常見的追蹤器記錄您的上網行為。`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `%s 可保護您免於被許多最常見的追蹤器記錄您的上網行為。`
    - The source limits the claim to "many of" the most common trackers. The translation drops that limit and promises wider protection than the source makes.
- `preferences_android_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The translation says "other apps on other devices" where the source says "other apps on your device".
    - Current: `使用其他裝置中的其他應用程式時也自動填寫使用者名稱與密碼。`
    - Source: `Fill usernames and passwords in other apps on your device.`
    - Suggest: `在您裝置上的其他應用程式中也自動填寫使用者名稱與密碼。`
    - The source says "other apps on your device" (the same device), but 其他裝置中 means "on other devices". That changes where autofill works.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The text says the user shares how they use Firefox, but the source means only that they use it.
    - Current: `以及是如何使用`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `以及您正在使用 Firefox 的事實`
    - The developer comment says 'that you use it' means only that the user keeps using Firefox after installing it, and does not mean Firefox tracks their usage. The translation turns this into sharing how the user uses Firefox, which describes a wider data collection than the product performs.
- `preferences_passwords_autofill2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The translation means 'autofill %1$s fields' instead of 'autofill inside %1$s'.
    - Current: `自動填入 %1$s 欄位`
    - Source: `Autofill in %1$s`
    - Suggest: `在 %1$s 中自動填入`
    - The source means autofilling saved logins in web content inside the app (%1$s is the app name). The translation reads as filling in fields that belong to the app.
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "face unlock" is rendered as 表情 (facial expression), and "View tabs" is dropped.
    - Current: `使用您的指紋、PIN 碼或表情來解鎖`
    - Source: `View tabs with your fingerprint, PIN, or face unlock. Turning this on also prevents screen capture and sharing.`
    - Suggest: `使用您的指紋、PIN 碼或臉部解鎖來檢視分頁`
    - The source says tabs are viewed via fingerprint, PIN, or face unlock. 表情 means facial expression, not face recognition, and the translation leaves out that this is for viewing tabs.
- `preferences_search_engines_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Adds 其他 ("other"), which makes it say the suggestions come from other search engines.
    - Current: `來自其他搜尋引擎的建議`
    - Source: `Suggestions from search engines`
    - Suggest: `來自搜尋引擎的建議`
    - The source says "Suggestions from search engines" with no "other". Adding 其他 changes which engines the setting is about.
- `preferences_usage_data_description_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Translation adds "for all users" (為所有使用者), which is not in the source.
    - Current: `可幫助我們為所有使用者改進 Firefox 功能`
    - Source: `Data about your device, hardware configuration, and usage helps us improve Firefox features, performance, and stability.`
    - Suggest: `可幫助我們改進 Firefox 功能`
    - The en-US says the data helps improve Firefox features, performance, and stability; it says nothing about doing so for all users. The added phrase widens what the description claims.
- `protection_panel_banner_protected_no_blocked_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The status message "You’re protected." is translated as "Let us protect you."
    - Current: `讓我們保護您。`
    - Source: `You’re protected.`
    - Suggest: `您已受到保護。`
    - The source tells the user that protection is already active; this banner appears when protection is on and no trackers were blocked. "讓我們保護您" reads as an offer or invitation, not a statement of the current status.
- `search_add_custom_engine_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Label drops 'URL', so the field no longer says it expects a URL.
    - Current: `搜尋字串`
    - Source: `Search string URL`
    - Suggest: `搜尋字串網址`
    - Source is 'Search string URL'; the field takes a URL template, and sibling strings render URL as 網址.
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The noun order is reversed, so the hint reads "URL shortcut" instead of "the shortcut's URL".
    - Current: `網址捷徑`
    - Source: `Shortcut URL`
    - Suggest: `捷徑網址`
    - The source "Shortcut URL" is the hint for the field where the shortcut's URL is edited. 網址捷徑 means a shortcut to a URL, not the shortcut's URL. It is also inconsistent with the sibling hint 捷徑名稱 ("shortcut name").
- `tab_tray_close_tabs_banner_message` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — 'the past day, week, or month' is rendered as 'several days, weeks or months', which doesn't match the actual auto-close options.
    - Current: `超過幾天、幾週或幾個月`
    - Source: `Set open tabs to close automatically that haven’t been viewed in the past day, week, or month.`
    - Suggest: `超過一天、一週或一個月`
    - The source means the fixed options of one day, one week or one month. 幾天/幾週/幾個月 means 'several' of each, which suggests different thresholds.
- `trackers_blocked_empty` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "You’re protected" is rendered as "Let us protect you", which turns a statement that protection is already active into an offer.
    - Current: `讓我們保護您`
    - Source: `You’re protected`
    - Suggest: `您已受到保護`
    - The source states that the user is already protected (the card shows when no trackers have been blocked yet). 讓我們保護您 means "let us protect you", which suggests protection is not yet in effect.
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The translation says websites are slow or unreliable, but the source means the browser itself.
    - Current: `網站速度很慢或不穩定`
    - Source: `It’s slow or unreliable`
    - Suggest: `速度很慢或不穩定`
    - In this uninstall survey, "It's slow or unreliable" is about the app. Option 2 is the one that covers websites, so adding 網站 here moves the complaint to the wrong thing.
- `webcompat_reporter_edit_url_dialog_dismiss` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The dismiss button in the Edit URL dialog is rendered as "Got it!" instead of a cancel/close action.
    - Current: `知道了！`
    - Source: `Dismiss`
    - Suggest: `取消`
    - This button sits next to "Save" in an edit confirmation dialog, so "Dismiss" means close without saving. 知道了！ ("Got it!") reads as an acknowledgement, not as discarding the edit.
- `webcompat_reporter_reason_turn_off_adblocker` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — "ad blocker" is translated as 廣告追蹤器 ("ad tracker"), which is a different thing.
    - Current: `廣告追蹤器`
    - Source: `Site asked to turn off ad blocker`
    - Suggest: `廣告封鎖器`
    - The source refers to an ad blocker. 廣告追蹤器 means ad tracker, close to the opposite concept.

### C. Grammar, agreement & spelling

- `mozac_feature_addons_failed_to_load_extensions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — 「稍候」is misused for「稍後」in "try again later".
    - Current: `請稍候再試`
    - Source: `Couldn’t load extensions. Try again later.`
    - Suggest: `請稍後再試`
    - Source says "Try again later"; 稍後 means 'later', while 稍候 means 'wait a moment'. Standard wording is 請稍後再試.
- `mozac_feature_addons_permissions_content_description_item` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — The counting word 組 ("set/group") is wrong for a single permission's position in a list.
    - Current: `（第 %2$d 組，共 %3$d 組）`
    - Source: `%1$s, %2$d of %3$d`
    - Suggest: `（第 %2$d 項，共 %3$d 項）`
    - The comment says this gives the item's position in the permissions list ("2 of 6"). Each entry is one permission, not a group, so 項 is the right counting word.
- `browser_menu_add_to_homescreen_xiaomi` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The verb is missing: 「才能捷徑到主畫面」 treats the noun 捷徑 (shortcut) as if it were a verb.
    - Current: `才能捷徑到主畫面`
    - Source: `Xiaomi devices may need extra permissions to add shortcuts to the home screen. Please check your settings.`
    - Suggest: `才能新增捷徑到主畫面`
    - The source says 'to add shortcuts to the home screen'. The translation drops the verb 'add' (新增), so the sentence is ungrammatical.
- `lens_camera_loading_status` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The phrase 這張 is accidentally written twice.
    - Current: `這張這張圖片`
    - Source: `Looking this up`
    - Suggest: `這張圖片`
    - The repeated 這張 is a typo. The status should read 正在搜尋這張圖片 ('Looking this up').
- `nimbus_survey_message_text` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The character 變 is missing, so 「讓 Firefox 得更好」 is ungrammatical.
    - Current: `讓 Firefox 得更好`
    - Source: `Please help make Firefox better by taking a short survey.`
    - Suggest: `讓 Firefox 變得更好`
    - The source says "make Firefox better". Chinese needs 變得更好 here, and the other survey prompts in this batch already use 「讓 Firefox 變得更好」.
- `setup_checklist_subtitle_3_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Duplicated particle "的的".
    - Current: `最完整的的上網體驗`
    - Source: `Complete these 3 steps to set up %1$s for the best browsing experience.`
    - Suggest: `最完整的上網體驗`
    - The particle 的 is accidentally repeated; this is a typo.
- `setup_checklist_subtitle_5_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Duplicated particle "的的".
    - Current: `最完整的的上網體驗`
    - Source: `Complete all 5 steps to set up %1$s for the best browsing experience.`
    - Suggest: `最完整的上網體驗`
    - The particle 的 is accidentally repeated; this is a typo.
- `setup_checklist_subtitle_6_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Duplicated particle "的的".
    - Current: `最完整的的上網體驗`
    - Source: `Complete all 6 steps to set up %1$s for the best browsing experience.`
    - Suggest: `最完整的上網體驗`
    - The particle 的 is accidentally repeated; this is a typo.
- `tab_manager_empty_tab_groups_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Human pronoun 他們 is used to refer to tabs (non-human).
    - Current: `他們儲存在此處`
    - Source: `Select tabs to create a group. They’re saved here, ready when you are.`
    - Suggest: `它們儲存在此處`
    - 'They' refers to the tabs/groups. In Chinese the pronoun for non-human things is 它們, not 他們.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The sentence has no verb before 影片 ("videos"), so it is ungrammatical.
    - Current: `無法影片、下載檔案或播放媒體內容`
    - Source: `Videos, downloads, or media didn’t work`
    - Suggest: `影片、下載檔案或媒體內容無法正常運作`
    - 無法 ("cannot") needs a verb after it. As written, 無法影片 reads as "cannot videos". The source says videos, downloads or media didn't work.

### D. Terminology, register & consistency

- `mozac_feature_addons_enabled` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — Status label "Enabled" rendered as bare 啟用, which reads as the action "Enable" and is inconsistent with 已停用 for Disabled.
    - Current: `啟用`
    - Source: `Enabled`
    - Suggest: `已啟用`
    - The comment says it indicates the add-on is enabled (a state); the paired Disabled string uses 已停用, so 已啟用 is the consistent state form.
- `mozac_feature_addons_permissions_browser_settings_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — "browser settings" is rendered as 瀏覽器選項 here, but as 瀏覽器設定 in the same permission's non-update description.
    - Current: `讀取或修改瀏覽器選項。`
    - Source: `Read and modify browser settings.`
    - Suggest: `讀取或修改瀏覽器設定。`
    - Both strings describe the same browserSettings permission. They should use the same term, and the sibling string uses 設定.
- `download_item_paused_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The "paused" status is translated as "暫停下載", which reads like a command to pause the download and doesn't match the "已暫停" used in the matching string.
    - Current: `暫停下載`
    - Source: `%1$s / %2$s • paused`
    - Suggest: `已暫停`
    - The source "paused" describes the state of a download in the list. The sibling string download_item_paused_description_unknown_total_size renders the same status as "已暫停". "暫停下載" is inconsistent with it and can be misread as an action label.
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The "Recommended" location option is labeled 推薦, but the snackbars and cards on the same VPN screens call it 建議位置.
    - Current: `推薦`
    - Source: `Recommended`
    - Suggest: `建議`
    - The snackbars and cards (ip_protection_location_selection_reset_snackbar, ip_protection_location_unavailable_recommended_snackbar, ip_protection_locations_unavailable_description) all say 建議位置 for the recommended location. Using 推薦 for the option label means one option has two different names on the same screen.
- `login_deletion_confirmation_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The informal 你 is used here, while the other login and password strings address the user with the formal 您.
    - Current: `你確定要刪除這筆密碼嗎？`
    - Source: `Are you sure you want to delete this password?`
    - Suggest: `您確定要刪除這筆密碼嗎？`
    - The surrounding login and password strings (logins_warning_dialog_message_2, logins_warning_dialog_title_2, micro_survey_feedback_confirmation) consistently use the formal 您. This dialog switches to 你, so the form of address is inconsistent on the same surface.
- `startup_crash_positive` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — 'Crash report' is rendered 錯誤報表 on the button but 錯誤報告 in the body text of the same crash page.
    - Current: `傳送錯誤報表`
    - Source: `Send crash report`
    - Suggest: `傳送錯誤報告`
    - The same source term is used twice on one screen (startup_crash_body uses 錯誤報告), so the two should match.
- `unsubmitted_crash_dialog_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — This button calls a crash report 錯誤報表, while the rest of the same dialog uses 錯誤報告.
    - Current: `傳送錯誤報表`
    - Source: `Send crash report`
    - Suggest: `傳送錯誤報告`
    - The body text, the checkbox label and the other crash dialog strings all translate "crash report" as 錯誤報告. The button should use the same term.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rTW/strings.xml` — Half-width colon followed by a space used inside Chinese text instead of a full-width colon.
    - Current: `例:`
    - Source: `{ <ul> } { <li> }Web addresses are usually written like { <strong> }http://www.example.com/{ </strong> }{ </li> } { <li> }Make sure that you’re using forward slashes (i.e. { <strong> }/{ </strong> }).{ </li> } { </ul> }`
    - Suggest: `例：`
    - zh-TW convention is full-width punctuation; the rest of the string uses full-width parentheses and period.
- `mozac_feature_addons_updater_dialog_last_attempt` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — Halfwidth colon used instead of the fullwidth colon required by zh-TW convention.
    - Current: `上次嘗試:`
    - Source: `Last attempt:`
    - Suggest: `上次嘗試：`
    - zh-TW convention is fullwidth punctuation; other strings in this batch (e.g. 評分：, 新增的必要權限：) use the fullwidth colon.
- `mozac_feature_addons_updater_dialog_status` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — Halfwidth colon used instead of the fullwidth colon required by zh-TW convention.
    - Current: `狀態:`
    - Source: `Status:`
    - Suggest: `狀態：`
    - zh-TW convention is fullwidth punctuation; other strings in this batch use the fullwidth colon.
- `mozac_feature_addons_user_rating_count_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used where the locale uses the full-width colon (：).
    - Current: `評價:`
    - Source: `Reviews: %1$s`
    - Suggest: `評價：`
    - The zh-TW tree almost always uses full-width punctuation. A Latin colon followed by a space doesn't match that convention.
- `phone_feature_blocked_intro` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The colon is halfwidth, but zh-TW uses fullwidth punctuation.
    - Current: `若要允許:`
    - Source: `To allow it:`
    - Suggest: `若要允許：`
    - The locale's established convention is fullwidth punctuation (1071 occurrences). After Chinese text, a halfwidth ASCII colon is out of place.
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Protocol name is written 'DNS Over HTTPS' with a capital O, unlike the source and the other DoH strings.
    - Current: `DNS Over HTTPS`
    - Source: `DNS over HTTPS`
    - Suggest: `DNS over HTTPS`
    - The protocol name in the source is 'DNS over HTTPS', and the locale writes it that way in preference_doh_summary. The title should match.
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `例如:`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `例如：`
    - zh-TW uses full-width punctuation; the parallel suggest-string example already uses '例如：'.
- `search_header_menu_item_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `這次搜尋:`
    - Source: `This time search in:`
    - Suggest: `這次搜尋：`
    - zh-TW convention is full-width punctuation.
- `sync_failed_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `上次同步: 從未`
    - Source: `Sync failed. Last synced: never`
    - Suggest: `上次同步：從未`
    - zh-TW convention is full-width punctuation; a half-width colon followed by a space looks wrong next to the Chinese text.
- `sync_failed_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `上次成功: %s`
    - Source: `Sync failed. Last success: %s`
    - Suggest: `上次成功：%s`
    - zh-TW convention is full-width punctuation.
- `sync_last_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `上次同步: %s`
    - Source: `Last synced: %s`
    - Suggest: `上次同步：%s`
    - zh-TW convention is full-width punctuation.
- `sync_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width colon.
    - Current: `上次同步: 從未`
    - Source: `Last synced: never`
    - Suggest: `上次同步：從未`
    - zh-TW convention is full-width punctuation.
- `wallpapers_item_name_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — The string uses a half-width colon where the locale uses full-width punctuation.
    - Current: `背景圖項目: %1$s`
    - Source: `Wallpaper Item: %1$s`
    - Suggest: `背景圖項目：%1$s`
    - zh-TW uses full-width punctuation as its convention, so the colon should be ：.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
