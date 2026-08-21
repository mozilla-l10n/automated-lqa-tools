# Android l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `d368c9040c12` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `d368c9040c12` |
| **Previous run** | 2026-08-21 @ `ac24476c7ff2` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,871 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-CN: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,871 |
| Missing strings | 40 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**40 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — 36
- `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 78 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |
| fullwidth | `punctuation` 1061 | **punctuation** |
| register | `informal` 3, `formal` 278 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (160)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 106 |
| 3 | Degraded language (grammar, spelling, terminology) | 42 |
| 4 | Cosmetic (typography, spacing) | 11 |

### A. Functional, markup, variables & plurals

- `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — `downloads_delete_dialog_title` has placeholders %d where the source has none
    - Current: `{$quantity ->} [other] 删除 %d 个文件？`
    - Source: `{$quantity ->} [one] Delete file? [other] Delete %d files?`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_engine_system_alert_title` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-zh-rCN/strings.xml` — Placeholder holds a URL, but the translation calls it a domain name (域名).
    - Current: `域名为 %1$s 的页面提示：`
    - Source: `The page at %1$s says:`
    - Suggest: `网址为 %1$s 的页面提示：`
    - The developer comment states %1$s is replaced with the URL of the current page, not the domain name.
- `mozac_browser_errorpages_file_access_denied_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — The verbs "removed, moved" are rendered in swapped/incorrect order ("移走、移除" for "removed, moved").
    - Current: `文件可能已被移走、移除，或者没有访问该文件的权限。`
    - Source: `{ <ul> } { <li> }It may have been removed, moved, or file permissions may be preventing access.{ </li> } { </ul> }`
    - Suggest: `文件可能已被移除、移动，或者文件权限阻止了访问。`
    - Source says "removed, moved, or file permissions may be preventing access"; the translation reverses the order of removed/moved and renders "file permissions may be preventing access" as simply lacking permission.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "Internet provider" mistranslated as "电信运营商" (telecom carrier).
    - Current: `请联系您的网络管理员或者电信运营商以寻求协助。`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `请联系您的网络管理员或互联网服务提供商以寻求协助。`
    - Source says "Internet provider" (ISP), which is not necessarily a telecom carrier.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "the device" is translated as "计算机" (computer) instead of "设备".
    - Current: `计算机是否连接了可用的网络？`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `设备是否连接了可用的网络？`
    - Source reads "Is the device connected to an active network?"; on Android the term is device (设备), not computer, and other strings in the same file use 设备.
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — The port-blocked message reverses the source meaning: the source says the port is normally used for purposes other than Web browsing, while the target says the port is "normally not used for web browsing".
    - Current: `通常{ <em> }不是{ </em> }用于网络浏览`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `通常用于网络浏览{ <em> }以外{ </em> }的用途`
    - Source: "normally used for purposes other than Web browsing" — the port does have a normal use, just not browsing; the translation states it is normally not used for browsing, losing/altering the meaning conveyed by <em>other</em>.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "Internet provider" is translated as "电信运营商" (telecom carrier) instead of internet service provider, inconsistent with the parallel string which uses 互联网服务提供商.
    - Current: `请联系您的网络管理员或者电信运营商以寻求协助。`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `请联系您的网络管理员或者互联网服务提供商以寻求协助。`
    - The same source sentence in mozac_browser_errorpages_unknown_proxy_host_message is rendered 互联网服务提供商; 电信运营商 names a different entity.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "your device" is translated as "您计算机" (your computer) in a mobile browser string.
    - Current: `而不是您计算机的问题`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `而不是您设备的问题`
    - Source says "not your device"; the target says computer, which is wrong on Android.
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "potentially harmful site" is rendered as "可能有攻击行为" (attack site), duplicating the malware string's wording instead of "有害".
    - Current: `可能有攻击行为`
    - Source: `{ <p> }The site at %1$s has been reported as a potentially harmful site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `可能是有害网站`
    - The source distinguishes "attack site" (malware string) from "potentially harmful site"; using 攻击行为 for both mistranslates and conflicts with the title 有恶意网站问题.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — The reason clause drops "because", turning the alternative causes into a statement of fact instead of an explanation.
    - Current: `不信任 { <b> }%2$s{ </b> }，其证书颁发者未知`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `不信任 { <b> }%2$s{ </b> }，因为其证书颁发者未知`
    - Source says "does not trust X because its certificate issuer is unknown, the certificate is self-signed, or..."; without 因为 the Chinese asserts these as facts rather than possible reasons.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — "Is the device connected to an active network?" is translated as "计算机" (computer) instead of device.
    - Current: `计算机是否连接了可用的网络？`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `设备是否连接了可用的网络？`
    - Source says "the device", not "the computer".
- `mozac_cfr_dismiss_button_content_description` — `mozilla-mobile/android-components/components/compose/cfr/src/main/res/values-zh-rCN/strings.xml` — "Dismiss" (close button content description) is rendered as "知道了" ("Got it"), which describes a different control.
    - Current: `知道了`
    - Source: `Dismiss`
    - Suggest: `关闭`
    - The developer comment says this is the content description for the close button of a CFR popup; screen readers should announce "Dismiss/Close", not an acknowledgement label. Other strings in the batch translate Dismiss as 关闭.
- `mozac_feature_addons_not_yet_supported_caption2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — Translation adds "请稍后再来" ("check back later"), which is not in the source.
    - Current: `我们目前着重构建对部分“推荐扩展”的支持，请稍后再来。`
    - Source: `We‘re currently building support for an initial selection of Recommended Extensions.`
    - Suggest: `我们目前正在构建对首批“推荐扩展”的支持。`
    - The source only says support for an initial selection of Recommended Extensions is being built; there is no invitation to come back later.
- `mozac_feature_addons_permissions_all_domain_count_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "Access your data for sites in %1$d domains" is rendered as accessing data "you use for" the domains, losing the "sites in domains" meaning.
    - Current: `访问您用于 %1$d 个域名的数据`
    - Source: `{$quantity ->} [other] Access your data for sites in %1$d domains`
    - Suggest: `访问您在 %1$d 个域名下网站中的数据`
    - The source refers to data for sites within the listed domains, not data the user uses for the domains.
- `mozac_feature_addons_permissions_extra_domains_description_plural_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "other domains" is translated as "other sites" (网站) instead of domains (域名).
    - Current: `访问您在其他网站的数据`
    - Source: `Access your data on other domains`
    - Suggest: `访问您在其他域名下的数据`
    - The source distinguishes domains from sites; the parallel _for_update string correctly uses 域名, and this string is identical to the "other sites" string, erasing the distinction.
- `mozac_feature_addons_permissions_extra_sites_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "Access your data on other sites" is mistranslated as "data you use for other sites".
    - Current: `访问您用于其他网站的数据。`
    - Source: `Access your data on other sites.`
    - Suggest: `访问您在其他网站的数据。`
    - The source means data located on other sites, not data used for other sites; the parallel string mozac_feature_addons_permissions_extra_sites_description_2 correctly uses 访问您在其他网站的数据.
- `mozac_feature_addons_permissions_show_fewer_sites` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "Show fewer sites" is rendered as a generic "折叠" (collapse), dropping the "sites" content and mismatching the paired "显示所有网站" button.
    - Current: `折叠`
    - Source: `Show fewer sites`
    - Suggest: `显示较少网站`
    - The source reads "Show fewer sites" and the counterpart string is translated as "显示所有网站"; "折叠" omits the object and is inconsistent with the paired label.
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "Supported add-ons checker" is rendered as "新支持附加组件检查器", adding "新" which is not in the source.
    - Current: `新支持附加组件检查器`
    - Source: `Supported add-ons checker`
    - Suggest: `受支持的附加组件检查器`
    - The source names the channel "Supported add-ons checker"; "新" (new) is not present in the source string.
- `mozac_feature_addons_updater_notification_heading_data_collection_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "New required data collection" is translated as "新必要权限" (new required permissions), losing the data-collection meaning and duplicating the adjacent permissions string.
    - Current: `新必要权限：开发者称此扩展将收集%1$s。`
    - Source: `New required data collection: The developer says the extension will collect %1$s.`
    - Suggest: `新增必要数据收集：开发者称此扩展将收集%1$s。`
    - Source distinguishes data collection from permissions; the sibling string mozac_feature_addons_updater_notification_heading_permissions already uses 新必要权限, so this rendering is both wrong and ambiguous.
- `mozac_feature_autofill_search_suggestions` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-zh-rCN/strings.xml` — "Search %1$s" is expanded to "搜索保存于 %1$s 的登录信息", adding content not in the source.
    - Current: `搜索保存于 %1$s 的登录信息`
    - Source: `Search %1$s`
    - Suggest: `搜索 %1$s`
    - The source is simply "Search %1$s" where %1$s is the app name; the target adds "saved logins in" which is not in the source string.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-zh-rCN/strings.xml` — "choose tabs to close" is mistranslated as "select tabs to close (them/the dialog)" with wrong structure.
    - Current: `或者选择标签页以关闭`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `或者选择要关闭的标签页`
    - The source means the user picks which tabs to close; the Chinese reads as "select a tab in order to close", which is ambiguous/incorrect.
- `mozac_feature_passwords_importer_dialog_title` — `mozilla-mobile/android-components/components/feature/password-importer/src/main/res/values-zh-rCN/strings.xml` — Progress title "Importing passwords" rendered as an imperative/action label instead of ongoing state.
    - Current: `导入密码`
    - Source: `Importing passwords`
    - Suggest: `正在导入密码`
    - The comment says it is the title of a loading dialog showing progress; the parallel bookmarks string uses 正在导入书签.
- `mozac_feature_prompts_collapse_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-zh-rCN/strings.xml` — "Collapse saved cards" is rendered as "信用卡" (credit cards) instead of the generic "卡"/"银行卡".
    - Current: `折叠保存的信用卡`
    - Source: `Collapse saved cards`
    - Suggest: `折叠已保存的卡片`
    - The source deliberately says "cards", not "credit cards"; narrowing it to 信用卡 changes the meaning.
- `mozac_feature_prompts_identity_credentials_choose_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-zh-rCN/strings.xml` — "login provider" is rendered as "登录方式" (login method) instead of a provider.
    - Current: `选择一个登录方式`
    - Source: `Choose a login provider`
    - Suggest: `选择登录提供商`
    - The source refers to an identity/login provider (a service), not a login method; the related string uses %1$s as the provider name.
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-zh-rCN/strings.xml` — "as a login provider" is dropped from the translation.
    - Current: `使用 %1$s 登录`
    - Source: `Use %1$s as a login provider`
    - Suggest: `使用 %1$s 作为登录提供商`
    - Source "Use %1$s as a login provider" states the provider role; the translation only says "log in with %1$s", losing the meaning.
- `mozac_feature_prompts_save_credit_card_prompt_body_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-zh-rCN/strings.xml` — Translation adds "保存" (save) that is not in the source, which says the app encrypts the card number.
    - Current: `%s 会将卡号加密保存。`
    - Source: `%s encrypts your card number. Your security code won’t be saved.`
    - Suggest: `%s 会加密您的卡号。`
    - Source: "%s encrypts your card number." — no mention of saving in that clause; the next sentence contrasts that the security code won't be saved.
- `mozac_feature_sitepermissions_do_not_ask_again_on_this_site4` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-zh-rCN/strings.xml` — New shorter source "Remember for this site" is translated with the older, longer wording including "decision".
    - Current: `记住对此网站的决定`
    - Source: `Remember for this site`
    - Suggest: `记住此网站的选择`
    - The source was deliberately shortened from "Remember decision for this site" (v2 string) to "Remember for this site"; the target duplicates the v2 translation verbatim.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-zh-rCN/strings.xml` — Translation says the website must be allowed to show notifications in the app, while the source says the user must allow notifications for the app itself.
    - Current: `您需要允许其在 %1$s 中显示通知`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `您需要允许 %1$s 发送通知`
    - Source: "You'll need to allow notifications in %1$s" — the Android app-level notification permission for the app (%1$s is the app name), not a per-site permission.
- `mozac_summarize_error_dissmiss` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-zh-rCN/strings.xml` — "Dismiss" is translated as "知道了" (Got it), which is a different action label.
    - Current: `知道了`
    - Source: `Dismiss`
    - Suggest: `关闭`
    - The source is a dismiss button; "知道了" means "Got it/OK", an acknowledgement rather than dismissal.
- `mozac_summarize_fxa_sign_in_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-zh-rCN/strings.xml` — "create one to get started" is rendered as "注册账户开始使用" but the sentence structure loses the meaning that the user can create a new account; more importantly "Use your Mozilla account to continue" is fine while the second clause omits "新".
    - Current: `或注册账户开始使用`
    - Source: `Use your Mozilla account to continue or create one to get started.`
    - Suggest: `或注册新账户开始使用`
    - The source offers creating a new account as the alternative to using an existing one; without "新" the contrast between the two options is lost.
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-zh-rCN/strings.xml` — "Summarize with a shake?" is rendered as "启用“摇动生成摘要”？" (Enable "Shake to summarize"?), adding "enable" not present in the source.
    - Current: `启用“摇动生成摘要”？`
    - Source: `Summarize with a shake?`
    - Suggest: `摇一摇即可生成摘要？`
    - The source asks whether the user wants to summarize with a shake; the translation converts it into a feature-enablement prompt wording that differs from the source.
- `mozac_lib_crash_notification_action_report` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-zh-rCN/strings.xml` — "Report" (send the crash report) is rendered as "反馈" (feedback) rather than reporting/sending the report.
    - Current: `反馈`
    - Source: `Report`
    - Suggest: `报告`
    - Per the developer comment the button sends the crash report to Mozilla; other strings in the same file use 崩溃报告 for "crash report", so 报告/发送报告 is the consistent term.
- `mozac_support_base_permissions_needed_negative_button` — `mozilla-mobile/android-components/components/support/base/src/main/res/values-zh-rCN/strings.xml` — "Dismiss" is translated as "隐藏" (hide) instead of dismissing/closing the dialog.
    - Current: `隐藏`
    - Source: `Dismiss`
    - Suggest: `忽略`
    - The developer comment says this button dismisses the dialog; 隐藏 means "hide", which is a different action.
- `automatic_translation_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Couldn't load languages" is rendered as "无法加载语言包" (language packs), changing the meaning.
    - Current: `无法加载语言包，请稍后再试。`
    - Source: `Couldn’t load languages. Please check back later.`
    - Suggest: `无法加载语言列表，请稍后再试。`
    - The source refers to loading the list of languages in translation settings, not downloadable language packs.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "will never offer to translate" translated as "将永不翻译", dropping "offer to".
    - Current: `%1$s 将永不翻译使用此语言的网站。`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `%1$s 将永不询问是否翻译使用此语言的网站。`
    - Source states the app will never offer (prompt) to translate, not that it will never translate; the parallel "offer to translate" string is rendered 询问是否翻译.
- `awesomebar_clipboard_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Fill link from clipboard" translated as "打开剪贴板中的链接" (open the link), but the action fills the link into the search bar.
    - Current: `打开剪贴板中的链接`
    - Source: `Fill link from clipboard`
    - Suggest: `填入剪贴板中的链接`
    - Source says "Fill link from clipboard"; filling the URL bar differs from opening the link.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" (go back in the bookmarks navigation bar) is rendered as "browse the previous page".
    - Current: `浏览上一页`
    - Source: `Navigate back`
    - Suggest: `返回`
    - The developer comment says this is the content description for the bookmark navigation bar back button, i.e. navigating back to the previous bookmarks screen, not browsing a previous web page.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "sheet" (bottom sheet) is mistranslated as "表单" (form).
    - Current: `关闭定制标签页菜单表单`
    - Source: `Close custom tab menu sheet`
    - Suggest: `关闭自定义标签页菜单面板`
    - The developer comment says this is a bottom sheet handlebar; "表单" means "form", not a bottom sheet panel (面板/底部弹出面板).
- `browser_menu_remove_from_shortcuts` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Remove from shortcuts" is rendered as "移除快捷方式" (remove the shortcut) instead of removing the item from the shortcuts list.
    - Current: `移除快捷方式`
    - Source: `Remove from shortcuts`
    - Suggest: `从快捷方式中移除`
    - The source means removing the current site from the shortcuts section on the home page; the current wording reads as deleting a shortcut object and loses the "from shortcuts" relation.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Never" is translated as 手动 ("manually") instead of "从不".
    - Current: `手动`
    - Source: `Never`
    - Suggest: `从不`
    - The source option label is "Never"; the separate summary string already conveys "Close manually".
- `content_description_settings_search_navigate_back` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate Back" (return to Settings screen) is rendered as "浏览上一页" (browse to previous page).
    - Current: `浏览上一页`
    - Source: `Navigate Back`
    - Suggest: `返回`
    - The developer comment says the button navigates back to the Settings page from the Settings Search screen; "浏览上一页" describes browsing a previous web page, not returning to the previous screen.
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" (back button content description) is rendered as "浏览上一页" (browse the previous page), which describes page navigation rather than going back.
    - Current: `浏览上一页`
    - Source: `Navigate back`
    - Suggest: `返回`
    - The comment says this is the content description for the top bar back button in the credit card feature; it should say "go back", not "browse the previous page".
- `customize_toggle_contile` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Sponsored shortcuts" is translated as "赞助商网站" (sponsor websites), losing the "shortcuts" concept.
    - Current: `赞助商网站`
    - Source: `Sponsored shortcuts`
    - Suggest: `赞助商快捷方式`
    - The source refers to sponsored shortcuts on the home screen, not sponsor websites.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Debug locales to enable" is translated as "选择要启用的调试区域设置", adding "选择" (choose) which is not in the source header.
    - Current: `选择要启用的调试区域设置`
    - Source: `Debug locales to enable`
    - Suggest: `要启用的调试区域设置`
    - The source is a section header listing debug locales; it contains no verb "select".
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" (go back within the debug drawer) is rendered as "浏览上一页" (browse the previous page), which describes page navigation rather than returning in the drawer.
    - Current: `浏览上一页`
    - Source: `Navigate back`
    - Suggest: `返回`
    - The developer comment says this content description is for navigating back within the debug drawer, not browsing a previous web page.
- `default_locale_text` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation adds a spurious "(ISO 3166/639)" not present in the source.
    - Current: `依照设备语言显示 (ISO 3166/639)`
    - Source: `Follow device language`
    - Suggest: `跟随设备语言`
    - Source is simply "Follow device language"; the standards reference is invented content shown to users.
- `delete_from_history` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Delete from history" is rendered as "delete history", losing the "from history" meaning.
    - Current: `删除历史记录`
    - Source: `Delete from history`
    - Suggest: `从历史记录中删除`
    - The menu item deletes a top site from history, not the history itself.
- `download_languages_fetch_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Couldn’t load languages" is rendered as "cannot load language packs", changing the object of the action.
    - Current: `无法加载语言包`
    - Source: `Couldn’t load languages. Please check back later.`
    - Suggest: `无法加载语言列表`
    - The developer comment says the error occurs when fetching the list of languages, not language packages.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" is translated as "browse the previous page" instead of a generic back-navigation label.
    - Current: `浏览上一页`
    - Source: `Navigate back`
    - Suggest: `返回`
    - The source is the content description of the toolbar back button, meaning navigate back in the app UI, not browsing to the previous web page.
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation drops "ad networks" from the list of parties that use tracking cookies.
    - Current: `拦截网络分析公司用于跨网站收集浏览数据的 Cookie。`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `拦截广告联盟和分析公司用于跨网站收集您浏览数据的 Cookie。`
    - The source says "cookies that ad networks and analytics companies use"; the Chinese mentions only 网络分析公司 (analytics companies), omitting ad networks.
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation adds "完全" (completely) not present in the source and misstates the isolation scope.
    - Current: `能够完全隔离每个网站的 Cookie`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `会将 Cookie 隔离到您当前所在的网站`
    - The source says Total Cookie Protection isolates cookies to the site you're on; the added "完全" (completely) is an unsupported intensifier.
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation says "helps block suspicious programs" instead of "stop suspected fingerprinters".
    - Current: `启用数字指纹跟踪程序防护，有助于阻止可疑程序。`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `启用数字指纹跟踪防护，以阻止存疑的数字指纹跟踪程序。`
    - The source states it stops suspected fingerprinters; "有助于" (helps) is not in the source and "可疑程序" is a vaguer term than the established 存疑的数字指纹跟踪程序 used in the paired title string.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation says tabs were closed "in" the app, but the source means the app closed N tabs (notification title "Firefox tabs closed: 3").
    - Current: `已关闭 %1$s 中的 %2$d 个标签页`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s 已关闭标签页：%2$d`
    - Source "%1$s tabs closed: %2$d" is a notification title where %1$s is the app name; the Chinese reformulation "已关闭 [app] 中的 N 个标签页" changes the meaning to tabs located inside the app being closed, and the tabs were actually closed from another device.
- `history_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Translation adds "条历史记录" (history items) not present in the source "%1$d selected".
    - Current: `已选择 %1$d 条历史记录`
    - Source: `%1$d selected`
    - Suggest: `已选择 %1$d 项`
    - Source is a generic "%1$d selected" count for the multi-select app bar; the target invents a noun ("history items") not in the source.
- `home_screen_shortcut_uninstall_survey` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Uninstall, why?" is rendered as "卸载并询问原因" (uninstall and ask the reason), changing the meaning.
    - Current: `卸载并询问原因`
    - Source: `Uninstall, why?`
    - Suggest: `卸载？告诉我们原因`
    - The source is a prompt asking the user why they are uninstalling, not an action that uninstalls the app.
- `inactive_tabs_auto_close_message_action` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Call-to-action "TURN ON AUTO CLOSE" is expanded to "启用自动关闭标签页功能", adding content and length to a button label.
    - Current: `启用自动关闭标签页功能`
    - Source: `TURN ON AUTO CLOSE`
    - Suggest: `启用自动关闭`
    - The source is a short button label; "标签页功能" is not in the source and makes the label drastically longer.
- `inactive_tabs_auto_close_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "tabs you haven’t viewed over the past month" is mistranslated as "您一个月内未查看的标签页".
    - Current: `Firefox 可自动关闭您一个月内未查看的标签页。`
    - Source: `Firefox can close tabs you haven’t viewed over the past month.`
    - Suggest: `Firefox 可关闭您过去一个月未曾查看的标签页。`
    - "一个月内" reads as "within one month"; the source means tabs not viewed during the past month (i.e. unused for over a month). Also "自动" is not in the source.
- `inactive_tabs_num_items` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Items: %d" label format is changed to "%d 个项目".
    - Current: `%d 个项目`
    - Source: `Items: %d`
    - Suggest: `项目：%d`
    - The source is a label-colon-value format; the translation restructures it, losing the label form.
- `ip_protection_data_limit_reached_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Access will reset next month" is mistranslated as "使用权限将于下个月重置" — acceptable — but "已用完" states data is exhausted while source says "used"; actually the snackbar signals the limit is reached, so retain, however "流量已用完" drops the amount semantics.
    - Current: `%1$d GB VPN 流量已用完，使用权限将于下个月重置。`
    - Source: `%1$d GB of VPN data used. Access will reset next month.`
    - Suggest: `已用完 %1$d GB VPN 流量，使用权限将于下个月重置。`
    - The source reads "%1$d GB of VPN data used"; the Chinese word order makes "%1$d GB VPN 流量" the subject of "已用完" awkwardly and reads as a fragment. Reordering keeps the meaning and grammar.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" is rendered as "浏览上一页" (browse the previous page), which describes page navigation rather than the back button of the settings screen.
    - Current: `浏览上一页`
    - Source: `Navigate back`
    - Suggest: `返回`
    - The developer comment says this is the content description for the settings screen top bar back button; "浏览上一页" wrongly implies browsing to a previous web page.
- `lens_camera_permission_denied` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Permission denied" is translated as "拒绝访问" (access denied/refuse access) instead of indicating the permission was denied.
    - Current: `拒绝访问`
    - Source: `Permission denied`
    - Suggest: `权限被拒绝`
    - The toast appears when the user denies the camera permission; "拒绝访问" loses the notion of a permission and reads as an imperative/ambiguous phrase.
- _…and 53 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — Missing measure word/particle in "请检查您网络连接".
    - Current: `请检查您网络连接。`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `请检查您的网络连接。`
    - Grammatically incomplete: 您 requires 的 before 网络连接 (source: "Check the device's network connection.").
- `mozac_browser_errorpages_security_ssl_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-zh-rCN/strings.xml` — Ungrammatical phrase "建议联系向这个网站的拥有者反馈此问题" contains a stray 联系 before 向.
    - Current: `建议联系向这个网站的拥有者反馈此问题。`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because the authenticity of the received data could not be verified.{ </li> } { <li> }Please contact the website owners to inform them of this problem.{ <…`
    - Suggest: `请向这个网站的拥有者反馈此问题。`
    - "联系向" is not valid Chinese; the source is "Please contact the website owners to inform them of this problem."
- `mozac_feature_applinks_normal_confirm_dialog_title` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-zh-rCN/strings.xml` — Translation is missing the preposition/verb structure, reading as a fragment instead of "Open in another app".
    - Current: `其他应用打开`
    - Source: `Open in another app`
    - Suggest: `在其他应用中打开`
    - The source "Open in another app" requires "在……中打开" or at least "用其他应用打开"; the current text lacks any preposition and reads ungrammatically, inconsistent with the sibling string "用其他应用打开链接？".
- `mozac_feature_summarize_summary_model` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-zh-rCN/strings.xml` — "由 %1$s 摘要" is ungrammatical; "Summary by X" means the summary was generated by model X.
    - Current: `由 %1$s 摘要`
    - Source: `Summary by %1$s`
    - Suggest: `由 %1$s 生成的摘要`
    - In Chinese 摘要 as a verb after 由…is not idiomatic; the source is a noun phrase attributing the summary to the model.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Missing noun/measure word makes the content description ungrammatical.
    - Current: `显示所有过去探索`
    - Source: `Show all past explorations`
    - Suggest: `显示所有过去的探索记录`
    - "显示所有过去探索" lacks a proper noun phrase in Chinese; screen readers will read an incomplete phrase.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Missing preposition/word makes "%s 上搜索" ungrammatical for "Search %s".
    - Current: `%s 上搜索`
    - Source: `Search %s`
    - Suggest: `在 %s 上搜索`
    - Source "Search %s" means search using/at the named engine; Chinese needs 在…上搜索 or 使用 %s 搜索; "%s 上搜索" lacks the required preposition.
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Wrong word: "制订" should be "制定" (or 推出) for introducing terms of use.
    - Current: `我们制订了`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `我们推出了`
    - The source says "We’ve introduced a ... Terms of Use"; 制订 is a misuse here and the standard form is 制定/推出.
- `tip_autocomplete_url` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Misplaced particle "的" makes the phrase ungrammatical.
    - Current: `长按地址栏的中任一链接`
    - Source: `Autocomplete URLs for sites you use most  Long-press any URL in the address bar`
    - Suggest: `长按地址栏中的任一网址`
    - "地址栏的中任一链接" is ungrammatical; should be "地址栏中的", and the source refers to URLs, not links.

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_declarative_net_request_feedback_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — Inconsistent verb for "Read" vs. the paired _for_update string is fine, but "Access browsing history" and "Access browsing history." are rendered with two different verbs (获取 vs 访问).
    - Current: `获取浏览历史`
    - Source: `Read your browsing history`
    - Suggest: `访问浏览历史`
    - mozac_feature_addons_permissions_history_description ("Access browsing history") is translated as 获取浏览历史 while its _for_update twin with identical source wording uses 访问浏览历史; the same term must be rendered consistently on the same surface.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — "access" rendered as 存取 (Traditional Chinese/Taiwan usage) instead of the zh-CN term used in the twin string.
    - Current: `让开发者工具可以存取您打开的标签页中的数据`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `让开发者工具可以获取您打开的标签页中的数据`
    - 存取 is not standard zh-CN terminology here; the paired _for_update string uses 获取 for the same source wording.
- `mozac_feature_addons_permissions_pkcs11_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-zh-rCN/strings.xml` — The pkcs11 permission is translated as "密码认证服务" (password authentication) here while the non-update variant uses "密码学身份认证服务" (cryptographic authentication).
    - Current: `提供密码认证服务。`
    - Source: `Provide cryptographic authentication services.`
    - Suggest: `提供密码学身份认证服务。`
    - Source is "Provide cryptographic authentication services."; "密码认证" means password authentication, which is a different concept and inconsistent with mozac_feature_addons_permissions_pkcs11_description.
- `mozac_ui_tabcounter_duplicate_tab` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-zh-rCN/strings.xml` — "Duplicate tab" is translated as "克隆标签页" (clone) instead of the standard 复制标签页.
    - Current: `克隆标签页`
    - Source: `Duplicate tab`
    - Suggest: `复制标签页`
    - The established zh-CN term for the Duplicate tab menu option is 复制标签页; 克隆 is inconsistent terminology.
- `browser_menu_read` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Reader view" rendered as 阅读模式 while browser_menu_customize_reader_view_2 uses 阅读器视图 on the same menu.
    - Current: `阅读模式`
    - Source: `Reader view`
    - Suggest: `阅读器视图`
    - The same source term "Reader View" is translated inconsistently within the same browser menu surface (see "定制阅读器视图").
- `close_tab_and_delete_group_confirmation_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Tab "group" is rendered as 群组 (a social group), the wrong term for a tab group.
    - Current: `将永久删除此群组。`
    - Source: `This deletes the group permanently.`
    - Suggest: `将永久删除此标签页分组。`
    - Source refers to a tab group; 群组 in Firefox zh-CN means a group of people/chat group, while tab groups are 分组.
- `close_tab_and_delete_group_confirmation_dialog_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Tab "group" is rendered as 群组 instead of the tab-group term 分组.
    - Current: `删除群组`
    - Source: `Delete group`
    - Suggest: `删除分组`
    - The dialog concerns a tab group; 群组 is the term for a group of people, not a tab group.
- `close_tab_and_delete_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Tab "group" is rendered as 群组 instead of the tab-group term 分组.
    - Current: `关闭标签页并删除群组？`
    - Source: `Close tab and delete group?`
    - Suggest: `关闭标签页并删除分组？`
    - The dialog concerns deleting a tab group; 群组 is the wrong term for tab groups in Firefox zh-CN.
- `delete_tab_group_confirmation_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "group" (tab group) is translated as 群组 while elsewhere history group uses 分组; 群组 means a group of people.
    - Current: `将永久删除此群组。`
    - Source: `This deletes the group permanently.`
    - Suggest: `将永久删除此分组。`
    - Tab group terminology should be consistent with 分组 used in delete_history_group_snackbar; 群组 denotes a social group.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Navigate back" is rendered as 后退 here but as 浏览上一页 in etp_back_button_content_description, an inconsistency for the same source string on the same surface.
    - Current: `后退`
    - Source: `Navigate back`
    - Suggest: `返回上一页`
    - Same source string "Navigate back" in content descriptions should use one consistent rendering; the two current variants differ.
- `lens_camera_mode_qr` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "QR scanner" is translated as "扫码器", dropping the QR qualifier used elsewhere (二维码).
    - Current: `扫码器`
    - Source: `QR scanner`
    - Suggest: `二维码扫描器`
    - Other strings in the same feature use "二维码" for QR (e.g. lens_camera_qr_no_code_found); "扫码器" is inconsistent and vaguer than the source.
- `nova_onboarding_theme_selection_dark_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Theme option "Dark" rendered as "深邃" instead of the standard Firefox term "深色".
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - Firefox zh-CN consistently uses 深色/浅色 for dark/light theme options; "深邃" (profound) is not the established term.
- `nova_onboarding_theme_selection_light_label` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Theme option "Light" rendered as "明亮" instead of the standard Firefox term "浅色".
    - Current: `明亮`
    - Source: `Light`
    - Suggest: `浅色`
    - Firefox zh-CN consistently uses 浅色 for the light theme; "明亮" is inconsistent with the paired dark option and product terminology.
- `preferences_credit_cards_manage_saved_cards_2` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Manage cards" is rendered as "管理信用卡" (manage credit cards), inconsistent with the surrounding "卡片" terminology used for the same source term.
    - Current: `管理信用卡`
    - Source: `Manage cards`
    - Suggest: `管理卡片`
    - Source says "cards", and sibling strings (Add card → 添加卡片, Sync cards → 同步卡片信息) use 卡片; the feature is "payment methods", not specifically credit cards.
- `preferences_credit_cards_sync_cards_across_devices` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Sync cards across devices" is translated as "跨设备同步信用卡信息", narrowing "cards" to credit cards and diverging from the sibling string's 卡片 wording.
    - Current: `跨设备同步信用卡信息`
    - Source: `Sync cards across devices`
    - Suggest: `跨设备同步卡片信息`
    - Source uses the generic term "cards"; the related string preferences_credit_cards_sync_cards uses 卡片信息.
- `preferences_https_only_on_private` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Summary state string "On in private tabs" is translated as an action ("启用") instead of a state, inconsistent with the parallel string 对所有标签页开启.
    - Current: `仅在隐私标签页启用`
    - Source: `On in private tabs`
    - Suggest: `仅在隐私标签页开启`
    - This is the summary showing the current state ("On in private tabs"), parallel to preferences_https_only_on_all which uses 开启; using 启用 duplicates the option label preferences_https_only_in_private_tabs and breaks consistency between state and option strings.
- `sports_widget_close_team_selection_sheet_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "sheet" (bottom sheet UI) mistranslated as 表单 (form).
    - Current: `关闭球队选择表单`
    - Source: `Close team selection sheet`
    - Suggest: `关闭球队选择面板`
    - The source refers to a bottom sheet UI element, not a form; 表单 means form/questionnaire.
- `sports_widget_countdown_hours` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Abbreviated hour label uses two characters 小时 instead of a single-character abbreviation.
    - Current: `小时`
    - Source: `H`
    - Suggest: `时`
    - The developer comment asks for a single character equivalent where one exists; Chinese has 时 as the standard single-character abbreviation for hour, and the string is truncated to 2 characters in a countdown pill.
- `sports_widget_countdown_minutes` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Abbreviated minute label uses two characters 分钟 instead of the single-character 分.
    - Current: `分钟`
    - Source: `M`
    - Suggest: `分`
    - The developer comment asks for a single-character equivalent if the language has one; 分 is the standard single-character abbreviation for minute.
- `sports_widget_final_results_page_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "World Cup final results" is rendered 世界杯最终结果 here but 世界杯决赛结果 in the sibling string.
    - Current: `世界杯最终结果`
    - Source: `World Cup final results, page %1$d of %2$d`
    - Suggest: `世界杯决赛结果`
    - The same source phrase "World Cup final results" is translated inconsistently on the same surface; sports_widget_final_results_content_description uses 决赛结果, matching sports_widget_final = 决赛.
- `synced_tabs_connect_another_device` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — "Connect another device" rendered as 绑定 here but 连接 elsewhere (sync_connect_device).
    - Current: `绑定其他设备`
    - Source: `Connect another device.`
    - Suggest: `连接其他设备。`
    - Same source phrase is translated inconsistently on the same sync surface; 连接 is the established rendering.
- `biometric_prompt_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Uses informal "你" while the locale convention is the formal "您".
    - Current: `你可以验证指纹以继续当前应用会话。`
    - Source: `You can use your fingerprint to continue your current app session.`
    - Suggest: `您可以验证指纹以继续当前应用会话。`
    - zh-CN register convention for this tree is formal (您); neighboring strings such as cfr_cookie_banner and cfr_for_start_browsing use 您.
- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Enhanced Tracking Protection" is translated as "跟踪保护", losing "Enhanced" and diverging from the established term 增强型跟踪保护.
    - Current: `将禁用跟踪保护功能`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `将禁用增强型跟踪保护功能`
    - The same term is rendered 增强型跟踪保护 in enhanced_tracking_protection; here "Enhanced" is dropped.
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Uses informal "你" while the locale convention is the formal "您".
    - Current: `用你的方式搜你所寻`
    - Source: `Your search, your way`
    - Suggest: `用您的方式搜您所寻`
    - The zh-CN tree is established as formal register (您); neighboring first-run strings such as firstrun_privacy_text and firstrun_shortcut_text use 您.
- `preference_performance_block_webfonts` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Block" is rendered as "拦截" here but as "阻止" in the neighboring Block JavaScript preference, an inconsistency on the same settings screen.
    - Current: `拦截网络字体`
    - Source: `Block web fonts`
    - Suggest: `阻止网络字体`
    - preference_performance_block_javascript translates "Block" as "阻止"; the same term on the same surface should be consistent.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Block" is translated as 阻止 here but as 拦截 in the neighbouring cookie-blocking option strings.
    - Current: `阻止 Cookie`
    - Source: `Block cookies`
    - Suggest: `拦截 Cookie`
    - On the same settings screen preference_privacy_should_block_cookies_cross_site_option uses 拦截跨站 Cookie, so the category title should use the same verb.

### E. Typography, punctuation & spacing

- `app_name_private_4` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Halfwidth parentheses used instead of the locale's fullwidth punctuation convention.
    - Current: `%s (隐私模式)`
    - Source: `%s (Private)`
    - Suggest: `%s（隐私模式）`
    - zh-CN convention is fullwidth punctuation, as used in e.g. 询问是否翻译（默认）.
- `change_file_extension_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Halfwidth question mark used instead of the fullwidth question mark required by zh-CN punctuation convention.
    - Current: `将文件类型更改为 %s?`
    - Source: `Change file type to %s?`
    - Suggest: `将文件类型更改为 %s？`
    - The zh-CN convention is fullwidth punctuation; other dialog titles in this batch use “？” (e.g. 关闭标签页并删除群组？).
- `create_tab_group_form_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Default tab group name adds quotation marks around the number placeholder that are not in the source.
    - Current: `群组“%d”`
    - Source: `Group %d`
    - Suggest: `群组 %d`
    - Source is "Group %d", a plain default name (compare create_collection_default_name "收藏集 %d"); the added curly quotes are spurious and inconsistent.
- `other_default_search_engine_suggestion_header` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — An interpunct separator was added that does not exist in the source "%s search".
    - Current: `%s · 搜索`
    - Source: `%s search`
    - Suggest: `%s 搜索`
    - The source is a simple "<engine> search" header; inserting "·" changes the typography without basis in the source.
- `preferences_manage_account_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Extra enumeration comma before the final coordinated item in a Chinese list.
    - Current: `更改密码、管理数据收集、或删除账户`
    - Source: `Change your password, manage data collection, or delete your account`
    - Suggest: `更改密码、管理数据收集或删除账户`
    - Chinese punctuation convention does not use 、 immediately before 或 in a coordinated list; the source has "or" without a preceding separator in this position for zh-CN style.
- `sports_widget_error_connection_interrupted` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Halfwidth em dash surrounded by spaces instead of the fullwidth punctuation convention.
    - Current: `连接中断 — 实时更新已暂停。`
    - Source: `Connection interrupted — live updates paused.`
    - Suggest: `连接中断——实时更新已暂停。`
    - zh-CN uses fullwidth punctuation without surrounding spaces; the spaced dash copies English spacing conventions.
- `sports_widget_upcoming_match_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Extra space after the fullwidth colon in the content description.
    - Current: `即将进行： %1$s`
    - Source: `Upcoming: %1$s versus %2$s, %3$s at %4$s`
    - Suggest: `即将进行：%1$s`
    - A fullwidth colon already includes trailing space in zh-CN typography; the additional ASCII space is a spacing defect.
- `sync_last_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Halfwidth colon used instead of fullwidth colon, inconsistent with other sync summary strings.
    - Current: `上次同步: %s`
    - Source: `Last synced: %s`
    - Suggest: `上次同步：%s`
    - The zh-CN convention is fullwidth punctuation, and sibling strings (sync_failed_summary) use “：”.
- `sync_never_synced_summary` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Halfwidth colon used instead of fullwidth colon.
    - Current: `上次同步: 从未`
    - Source: `Last synced: never`
    - Suggest: `上次同步：从未`
    - zh-CN uses fullwidth punctuation; sync_failed_never_synced_summary uses “：”.
- `synced_tabs_connect_another_device` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Missing sentence-final period present in the source.
    - Current: `绑定其他设备`
    - Source: `Connect another device.`
    - Suggest: `绑定其他设备。`
    - Source "Connect another device." ends with a period; parallel strings (synced_tabs_enable_tab_syncing, synced_tabs_reauth) keep the fullwidth period.
- `top_sites_menu_sponsor_privacy` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rCN/strings.xml` — Uses a fullwidth ampersand "＆" without spacing where the source uses a regular ampersand.
    - Current: `我们的赞助商＆您的隐私`
    - Source: `Our sponsors & your privacy`
    - Suggest: `我们的赞助商与您的隐私`
    - The developer comment says '&' is the ampersand symbol; the fullwidth ＆ is not standard zh-CN typography, and the conjunction is normally rendered as 与/和 in Chinese.
- `tip_disable_tracking_protection` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Duplicated question mark.
    - Current: `网站表现异常？？`
    - Source: `Site behaving unexpectedly?  Try turning off Tracking Protection`
    - Suggest: `网站表现异常？`
    - The source has a single question mark; the translation repeats it.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/zh-CN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
