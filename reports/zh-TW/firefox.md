# Firefox l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `db2cfca9d18c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `af4e7312bee1` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 16,456 of 16,456 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




---

## Changes in this run

### 🆕 New findings (232)

- `fxa-menu-device-view-all-synced-tabs` — `browser/browser/appmenu.ftl` — `fxa-menu-device-view-all-synced-tabs` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$tabCount ->} [one] 檢視 { $tabCount } 個同步的分頁 [other] 檢視全部 { $tabCount } 個同步的分頁`
    - Source: `label: {$tabCount ->} [one] View { $tabCount } Synced Tab [other] View All { $tabCount } Synced Tabs`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-countdown` — `browser/browser/browser.ftl` — `urlbar-result-dates-countdown` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilStart ->} [one] { $name } · 明天 [other] { $name } · { $daysUntilStart } 天後`
    - Source: `{$daysUntilStart ->} [one] { $name } · In { $daysUntilStart } day [other] { $name } · In { $daysUntilStart } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-countdown-range` — `browser/browser/browser.ftl` — `urlbar-result-dates-countdown-range` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilStart ->} [one] { $name } · 明天開始 [other] { $name } · { $daysUntilStart } 天後開始`
    - Source: `{$daysUntilStart ->} [one] { $name } · Starts in { $daysUntilStart } day [other] { $name } · Starts in { $daysUntilStart } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-ongoing` — `browser/browser/browser.ftl` — `urlbar-result-dates-ongoing` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilEnd ->} [one] { $name } · 明天結束 [other] { $name } · { $daysUntilEnd } 天後結束`
    - Source: `{$daysUntilEnd ->} [one] { $name } · Ends in { $daysUntilEnd } day [other] { $name } · Ends in { $daysUntilEnd } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `menu-share-copy-links` — `browser/browser/browser.ftl` — `menu-share-copy-links` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] 複製鏈結 [other] 複製 { $count } 個鏈結`
    - Source: `accesskey: L label: {$count ->} [one] Copy Link [other] Copy { $count } Links`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — `downloads-files-not-downloaded` has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [other] 未下載 { $num } 個檔案。 [one] 未下載檔案。`
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-history` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-history` has plural variant ['one'], which zh-TW does not have
    - Current: `{$maxAgeInDays ->} [one] 昨天以來 [other] 過去 { $maxAgeInDays } 天以來的資料`
    - Source: `{$maxAgeInDays ->} [one] From the last day [other] From the last { $maxAgeInDays } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `security-visits-number` — `browser/browser/pageInfo.ftl` — `security-visits-number` has plural variant ['one'], which zh-TW does not have
    - Current: `{$visits ->} [0] 沒有 [one] 有，1 次 [other] 有，{ $visits } 次`
    - Source: `{$visits ->} [0] No [one] Yes, once [other] Yes, { $visits } times`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `site-permissions-open-blocked-popups` — `browser/browser/sitePermissions.ftl` — `site-permissions-open-blocked-popups` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] 開啟被封鎖的彈出型視窗… [other] 開啟 { $count } 個被封鎖的彈出型視窗…`
    - Source: `{$count ->} [one] Open { $count } blocked pop-up… [other] Open { $count } blocked pop-ups…`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `home-prefs-sections-rows-option` — `browser/browser/preferences/preferences.ftl` — `home-prefs-sections-rows-option` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `home-prefs-sections-rows-option-srd` — `browser/browser/newtab/newtab.ftl` — `home-prefs-sections-rows-option-srd` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `newtab-custom-row-selector2` — `browser/browser/newtab/newtab.ftl` — `newtab-custom-row-selector2` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-networking-ssl-tokens-summary-count` — `toolkit/toolkit/about/aboutNetworking.ftl` — `about-networking-ssl-tokens-summary-count` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] { $count } 個 token [other] { $count } 個 token`
    - Source: `{$count ->} [one] { $count } token [other] { $count } tokens`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — `preventedConsoleClear` quotes “保存紀錄” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “保留紀錄”
    - Current: `由於開啟「保存紀錄」功能，已防止執行 console.clear()`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `保留紀錄`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — `ImageMapRectBoundsError` uses straight double quotes
    - Current: `<area shape="rect">的"coords" 屬性不是 "left,top,right,bottom" 格式。`
    - Source: `The “coords” attribute of the <area shape="rect"> tag is not in the “left,top,right,bottom” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapCircleWrongNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapCircleWrongNumberOfCoords` uses straight double quotes
    - Current: `<area shape="circle"> 標籤中的 "coords" 屬性並不是 "center-x,center-y,radius" 的格式。`
    - Source: `The “coords” attribute of the <area shape="circle"> tag is not in the “center-x,center-y,radius” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapCircleNegativeRadius` — `dom/chrome/layout/layout_errors.properties` — `ImageMapCircleNegativeRadius` uses straight double quotes
    - Current: `<area shape="circle"> 標籤中的 "coords" 屬性不能有負的半徑。`
    - Source: `The “coords” attribute of the <area shape="circle"> tag has a negative radius.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapPolyWrongNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapPolyWrongNumberOfCoords` uses straight double quotes
    - Current: `<area shape="poly"> 標籤中的 "coords" 屬性並不是 "x1,y1,x2,y2,…" 的格式。`
    - Source: `The “coords” attribute of the <area shape="poly"> tag is not in the “x1,y1,x2,y2 …” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapPolyOddNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapPolyOddNumberOfCoords` uses straight double quotes
    - Current: `<area shape="poly"> 標籤中的 "coords" 屬性少了最後的 y 座標 (正確格式是 "x1,y1,x2,y2,…")。`
    - Source: `The “coords” attribute of the <area shape="poly"> tag is missing the last “y” coordinate (the correct format is “x1,y1,x2,y2 …”).`
    - The locale's quote convention is `corner` (890 occurrences).
- `appearance-browser-icon-entry-group` — `browser/browser/preferences/browserIcon.ftl` — The en-US says "taskbar", but the translation says 工具列, which means "toolbar".
    - Current: `選擇要在工具列、桌面與開始選單顯示的自訂圖示。`
    - Source: `description: Choose a custom icon for your taskbar, desktop and start menu. label: Browser icon`
    - Suggest: `選擇要在工作列、桌面與開始選單顯示的自訂圖示。`
    - The developer comment says the icon appears on the desktop, taskbar and Start Menu. The same file already uses 工作列 for taskbar in appearance-browser-icon-pin-button (釘選到工作列). 工具列 is the browser toolbar, which is a different thing.
- `preferences-ai-controls-pdfjs-control` — `browser/browser/preferences/preferences.ftl` — "Accessible" (usable with assistive technology) is translated as 親和力, which means friendly or approachable.
    - Current: `讓圖片更有親和力`
    - Source: `description: When you add images to PDFs, this adds descriptions to make them accessible. label: Image alt text in { -brand-short-name } PDF viewer`
    - Suggest: `讓圖片更容易使用輔助技術存取`
    - This feature generates alt text so images can be read by assistive technology. 更有親和力 says the images become more approachable, which loses the accessibility meaning completely.
- `connection-dns-over-https-url-item` — `browser/browser/preferences/preferences.ftl` — Typo: 使用者 ("user") is written where 使用 ("use") is meant.
    - Current: `使用者此提供者進行 DNS over HTTPS 解析`
    - Source: `label: { $name } tooltiptext: Use this provider for resolving DNS over HTTPS`
    - Suggest: `使用此提供者進行 DNS over HTTPS 解析`
    - The en-US is "Use this provider…". As written, the tooltip reads "user this provider…", which is ungrammatical. Compare the matching string in connection.ftl: 使用預設網址來解析 DNS over HTTPS.
- `permissions-site-speaker-desc` — `browser/browser/preferences/permissions.ftl` — 允許 ("allow") appears twice, which makes the sentence ungrammatical.
    - Current: `您可指定要允許哪些網站允許選擇音訊輸出裝置。`
    - Source: `The following websites have requested to select an audio output device. You can specify which websites are allowed to select an audio output device.`
    - Suggest: `您可指定要允許哪些網站選擇音訊輸出裝置。`
    - The en-US is "You can specify which websites are allowed to select an audio output device." The second 允許 is redundant and garbles the sentence.
- `preferences-ai-controls-description` — `browser/browser/preferences/preferences.ftl` — "Features enhanced with AI" is rendered as AI 擴充功能 ("AI extension features"), while the rest of the page uses AI 強化功能.
    - Current: `是否使用 AI 擴充功能`
    - Source: `You always have a choice in { -brand-short-name }, including whether to use features enhanced with AI. More controls coming soon.`
    - Suggest: `是否使用 AI 強化功能`
    - Every other string on the AI controls page uses 強化功能 for "enhancements" (for example 封鎖 AI 強化功能). In zh-TW, 擴充 suggests add-ons or extensions, which is a different concept in Firefox settings.
- `preferences-ai-controls-tab-group-suggestions-control` — `browser/browser/preferences/preferences.ftl` — The translation says the feature manages the user's tabs, but the source only says it suggests names and organization.
    - Current: `管理您的分頁，並提供名稱建議。`
    - Source: `description: Get suggestions to name and organize your tabs. label: Tab group suggestions`
    - Suggest: `取得為分頁命名與整理分頁的建議。`
    - The en-US is "Get suggestions to name and organize your tabs." Both naming and organizing are suggestions. The translation instead states that the feature itself manages your tabs.
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — The menu path starts with the old name 選項 ("Options"), but the page is now called 設定 ("Settings").
    - Current: `您可以到「選項 > 隱私權與安全性 > Cookie 與網站資料」清除目前儲存的網站資料。`
    - Source: `<strong>{ -brand-short-name } is running out of disk space.</strong> Website contents may not display properly. You can clear stored data in Settings > Privacy & Security > Cookies and Site Data.`
    - Suggest: `您可以到「設定 > 隱私權與安全性 > Cookie 與網站資料」清除目前儲存的網站資料。`
    - The en-US path is Settings > Privacy & Security, and this locale names the page 設定 (settings-page-title, category-nav-heading). A user following 選項 would look for a menu entry that does not exist.
- `MUI_UNTEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — The uninstall wizard tells the user to close Firefox 'before installing' instead of before uninstalling
    - Current: `安裝前請確定 $BrandFullNameDA 已經關閉。`
    - Source: `This wizard will guide you through the uninstallation of $BrandFullNameDA.  Before starting the uninstallation, make sure $BrandFullNameDA is not running.  $_CLICK`
    - Suggest: `開始移除前請確定 $BrandFullNameDA 已經關閉。`
    - The en-US says 'Before starting the uninstallation, make sure … is not running.' This page belongs to the uninstall wizard, but the Chinese says 安裝前 (before installing).
- `MUI_TEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — The meaning is reversed: the en-US says closing other apps lets Setup avoid a reboot, but the Chinese says a reboot may be needed
    - Current: `安裝前建議您關閉其他的常駐程式，為了更新相關的系統檔案可能必須重新啟動電腦。`
    - Source: `This wizard will guide you through the installation of $BrandFullNameDA.  It is recommended that you close all other applications before starting Setup. This will make it possible to update relevant system files without…`
    - Suggest: `安裝前建議您關閉其他所有程式，這樣就可以更新相關的系統檔案而不需要重新啟動電腦。`
    - The en-US says 'This will make it possible to update relevant system files without having to reboot your computer.' The Chinese says the computer may have to be restarted to update system files, which is the opposite.
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — The policy's purpose is misdescribed: the Chinese says the page is blocked in order to block third-party modules
    - Current: `防止使用者開啟第三方模組資訊（about:third-party）頁面，以封鎖第三方模組注入 { -brand-short-name } 程序。`
    - Source: `Prevent the user from using Third-party Module Information (about:third-party) to block third-party modules injected into the { -brand-short-name } process.`
    - Suggest: `防止使用者透過第三方模組資訊（about:third-party）頁面封鎖注入 { -brand-short-name } 程序的第三方模組。`
    - The en-US says the policy stops the user from using about:third-party to block injected modules. The Chinese 以封鎖… turns module blocking into the purpose of the policy, which is the reverse of what it does.
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — 'Set the default value for' is dropped, so this reads like an enforcing policy rather than a default
    - Current: `允許 { -brand-short-name } 提供記住儲存登入帳號與密碼的功能。`
    - Source: `Set the default value for allowing { -brand-short-name } to offer to remember saved logins and passwords. Both true and false values are accepted.`
    - Suggest: `設定是否允許 { -brand-short-name } 提供記住登入資訊與密碼的預設值。`
    - The en-US is 'Set the default value for allowing …'. Its sibling policy-OfferToSaveLogins enforces the setting. Without the word 'default', administrators cannot tell the two policies apart.
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — The legal representation is turned into an obligation to obtain authorization from every user
    - Current: `您必須獲得您提供使用此瀏覽器的所有使用者授權，並代表他們同意使用條款。`
    - Source: `Do not display the Terms of Use and Privacy Notice upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.`
    - Suggest: `您聲明您接受，並有權代表所有您提供此瀏覽器使用權限的人員接受使用條款。`
    - The en-US says 'You represent that you accept and have the authority to accept…'. The developer comment says this means 'you confirm/declare'. The Chinese instead says you 'must obtain authorization from all users', which is a different legal statement.
- `onboarding-easy-setup-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — 'Helps stop companies' becomes 'automatically blocks the programs that let big companies follow you', which is an unhedged promise
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `可幫助防止企業在網路上偷偷跟蹤您`
    - The en-US says the browser 'helps stop companies from secretly following you'. The Chinese drops the hedge and claims the browser automatically blocks this tracking. It also narrows 'companies' to 大企業 (big companies).
- `newtab-wallpaper-error-upload-file-type` — `browser/browser/newtab/newtab.ftl` — This file-type error tells the user to retry later instead of telling them to use an image file
    - Current: `請稍後再重新上傳圖片。`
    - Source: `We couldn’t upload your file. Please try again with an image file.`
    - Suggest: `請改用圖片檔案再試一次。`
    - The en-US says 'Please try again with an image file.' The error is about the file type, so 'try again later' sends the user the wrong way.
- `fxa-adoption-addresses-backup-title` — `browser/browser/newtab/asrouter.ftl` — Saved (postal) addresses are rendered as 網址 (web addresses/URLs)
    - Current: `一起備份儲存的網址吧！`
    - Source: `Let’s back up your saved addresses`
    - Suggest: `一起備份儲存的地址吧！`
    - This message is about saved autofill addresses. Its subtitle uses 地址, but the title says 網址, which means URLs.
- `home-custom-homepage-delete-address-button` — `browser/browser/newtab/newtab.ftl` — A website address is called 地址 (postal address), while the neighbouring strings use 網址
    - Current: `刪除地址`
    - Source: `aria-label: Delete address title: Delete address`
    - Suggest: `刪除網址`
    - In the same subpage, 'Enter address' and 'Add address' are rendered 請輸入網址 and 新增網址. The delete button should match them.
- `WARN_RESTART_REQUIRED_UNINSTALL` — `browser/installer/custom.properties` — 'A previous uninstall' is dropped, so it sounds like the current operation needs a reboot
    - Current: `必須重新啟動電腦才能完成 $BrandShortName 的解除安裝程序。`
    - Source: `Your computer must be restarted to complete a previous uninstall of $BrandShortName. Do you want to reboot now?`
    - Suggest: `必須重新啟動電腦才能完成先前的 $BrandShortName 解除安裝程序。`
    - The en-US says 'to complete a previous uninstall'. This dialog appears when an earlier operation is still pending.
- `WARN_RESTART_REQUIRED_UPGRADE` — `browser/installer/custom.properties` — 'A previous upgrade' is dropped
    - Current: `您的電腦必須重新啟動以完成升級 $BrandShortName。`
    - Source: `Your computer must be restarted to complete a previous upgrade of $BrandShortName. Do you want to reboot now?`
    - Suggest: `您的電腦必須重新啟動以完成先前的 $BrandShortName 升級。`
    - The en-US says 'to complete a previous upgrade'. Without 'previous', the dialog seems to refer to the current upgrade.
- `REG_APP_DESC` — `browser/installer/custom.properties` — 'Protection from online identity theft' becomes a 'new online scam-site detection feature'
    - Current: `（包含新的線上辨識詐騙網站功能）`
    - Source: `$BrandShortName delivers safe, easy web browsing. A familiar user interface, enhanced security features including protection from online identity theft, and integrated search let you get the most out of the web.`
    - Suggest: `（包含線上身分盜用防護）`
    - The en-US names protection from identity theft. The Chinese describes a different feature and adds 'new'.
- `STUB_BLURB_FIRST3` — `browser/installer/nsisstrings.properties` — 'open web' is left in English, although the sibling string translates it
    - Current: `準備好在 Open Web 中漫遊`
    - Source: `Get ready to roam on the open web`
    - Suggest: `準備好在開放的網路中漫遊`
    - The sibling STUB_BLURB_FIRST2_DEVEDITION renders 'the open web' as 開放的網路環境. 'Open web' is a common phrase, not a brand.
- `root-certificate-succession-infobar-january-message` — `browser/browser/newtab/asrouter.ftl` — 'Problems' is narrowed to 'startup problems', and the date is missing 日
    - Current: `可能會在 2025 年 1 月 14 起遇到啟動問題`
    - Source: `<strong>Older versions of { -brand-short-name } may start to have problems on January 14, 2025.</strong>`
    - Suggest: `可能會在 2025 年 1 月 14 日起開始遇到問題`
    - The en-US says only 'may start to have problems'; it does not say the problems are at startup. The sibling March message writes the date with 日.
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — 'Backed by the Mozilla Foundation' becomes 'developed by the Mozilla Foundation'
    - Current: `由 Mozilla 基金會開發的`
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet more open, accessible, and better for everyone.`
    - Suggest: `由 Mozilla 基金會支持的`
    - The en-US says Firefox is backed by the Foundation, not developed by it. The same change appears in onboarding-gratitude-security-and-privacy-subtitle.
- `mr1-return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — Typo: a stray 斯 after 隱私
    - Current: `又快又有隱私斯的瀏覽器`
    - Source: `You’ve got a fast, private browser at your fingertips. Now you can add <b>{ $addon-name }</b> and do even more with { -brand-short-name }.`
    - Suggest: `又快又有隱私的瀏覽器`
    - 斯 is a stray character that makes the phrase ungrammatical.
- `onboarding-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — The particle 的 is duplicated
    - Current: `最完整的的上網體驗`
    - Source: `Complete these steps to get the most out of your browsing experience.`
    - Suggest: `最完整的上網體驗`
    - Repeated particle.
- `newtab-sports-widget-message-survey-widget-body` — `browser/browser/newtab/newtab.ftl` — A stray 在 makes the sentence ungrammatical
    - Current: `幫助我們在改善未來的小工具功能`
    - Source: `Share your feedback to help us improve future widgets. Then, try the new one in your lineup.`
    - Suggest: `幫助我們改善未來的小工具功能`
    - The 在 has no role here and breaks the verb phrase.
- `newtab-privacy-message-info-10` — `browser/browser/newtab/newtab.ftl` — A preposition is missing before 任何網站
    - Current: `即可任何網站都使用`
    - Source: `Save passwords in { -brand-short-name } to use strong, unique logins everywhere.`
    - Suggest: `即可在任何網站都使用`
    - Without 在 the clause is ungrammatical.
- `onboarding-checklist-pin` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar) instead of 工作列
    - Current: `釘選到工具列`
    - Source: `Pin { -brand-short-name } to taskbar`
    - Suggest: `釘選到工作列`
    - In zh-TW Windows the taskbar is 工作列. In Firefox, 工具列 is the browser toolbar, which is a different thing. Other strings that mean pinning to the taskbar already use 工作列: launch-on-login-spotlight-pin-taskbar-checkbox, spotlight-pin-primary-button, mr2022-upgrade-onboarding-pin-private-window-primary-button-label and ICONS_TASKBAR.
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — 'Pin to taskbar' is rendered with 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar' (the Windows taskbar, 工作列). 工具列 means the browser toolbar.
- `mr2022-onboarding-pin-primary-button-label-msix` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `釘選到工具列與開始選單`
    - Source: `Pin { -brand-short-name } to taskbar and start menu`
    - Suggest: `釘選到工作列與開始選單`
    - Windows taskbar is 工作列.
- `fx100-thank-you-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar'.
- `onboarding-refresh-tou-pin` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 新增到您的工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Add { -brand-short-name } to your taskbar`
    - Suggest: `將 { -brand-short-name } 新增到您的工作列`
    - The source is 'Add … to your taskbar'.
- `multi-cta-fox-doodle-pin-checkbox` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar'. The same file uses 工作列 in spotlight-pin-primary-button.
- `multi-cta-fox-doodle-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `並釘選至工具列。`
    - Source: `{$sel_1 ->} [macos] Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and keep it in your Dock. [other] Keep your favorite privacy-focuse…`
    - Suggest: `並釘選至工作列。`
    - The source is 'pin it to your taskbar'.
- `multi-cta-fox-doodle-msix-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `並釘選至工具列與開始選單。`
    - Source: `Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and pin it to your taskbar and Start menu.`
    - Suggest: `並釘選至工作列與開始選單。`
    - The source is 'pin it to your taskbar and Start menu'.
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `釘選到工具列，`
    - Source: `Pin { -brand-shorter-name } to your taskbar so the browser you chose is always there when you need it.`
    - Suggest: `釘選到工作列，`
    - The source is 'Pin … to your taskbar'.
- `set-default-menu-message-row-layout-subtitle-variant` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `保留在您的工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your Dock. [other] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your taskbar.`
    - Suggest: `保留在您的工作列`
    - The source is 'keep it in your taskbar'.
- `taskbar-tab-urlbar-button-open` — `browser/browser/taskbartabs.ftl` — 'Taskbar' is translated as 'toolbar' (工具列).
    - Current: `將分頁新增到工具列`
    - Source: `tooltiptext: Add tab to taskbar`
    - Suggest: `將分頁新增到工作列`
    - en-US is 'Add tab to taskbar'. This feature pins a site to the Windows taskbar (工作列). 工具列 is the browser's own toolbar, so the tooltip describes a different action.
- `taskbar-tab-urlbar-button-close` — `browser/browser/taskbartabs.ftl` — 'Taskbar' is translated as 'sidebar' (側邊欄).
    - Current: `從側邊欄移除分頁`
    - Source: `tooltiptext: Remove tab from taskbar`
    - Suggest: `從工作列移除分頁`
    - en-US is 'Remove tab from taskbar'. The translation says the tab is removed from the sidebar, which is a different UI element.
- `delete-profile-page-title-2` — `browser/browser/profiles.ftl` — 'Profile' is rendered as 原則 ('policy') in the delete page title.
    - Current: `刪除「{ $profilename }」原則`
    - Source: `Delete “{ $profilename }” profile`
    - Suggest: `刪除「{ $profilename }」設定檔`
    - en-US is 'Delete “{ $profilename }” profile'. 原則 means policy. Every other string in this file uses 設定檔 for profile, including delete-profile-header-2 right next to it.
- `webrtc-allow-share-camera-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — The camera-only delegation prompt also asks about the microphone.
    - Current: `使用您的攝影機與麥克風嗎`
    - Source: `Allow { $origin } to give { $thirdParty } access to your camera?`
    - Suggest: `使用您的攝影機嗎`
    - en-US is 'Allow { $origin } to give { $thirdParty } access to your camera?'. Adding 與麥克風 makes the user think they are also granting microphone access. A separate string exists for camera plus microphone.
- `report-broken-site-panel-reason-adblocker-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — 'Ad blocker' is translated as 'ad trackers' (廣告追蹤器).
    - Current: `網站要求關閉廣告追蹤器`
    - Source: `label: Site asked to turn off ad blocker`
    - Suggest: `網站要求關閉廣告封鎖器`
    - en-US is 'Site asked to turn off ad blocker'. 廣告追蹤器 means ad trackers, which is close to the opposite thing, so the report reason no longer makes sense.
- _…and 172 more._

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
| Files | 327 |
| Strings | 16,456 |
| Missing strings | 61 |
| Obsolete strings | 1 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 13 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 5 |

### Completeness

**61 strings** are not translated yet, concentrated in:

- `toolkit/toolkit/global/viewSource.ftl` — 10
- `browser/browser/editBookmarkOverlay.ftl` — 9
- `browser/browser/ipProtection.ftl` — 9
- `browser/browser/browser.ftl` — 8
- `browser/browser/newtab/newtab.ftl` — 4
- `browser/browser/sanitize.ftl` — 3
- `browser/browser/sidebar.ftl` — 2
- `browser/browser/preferences/permissions.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/newtab/asrouter.ftl` — 2
- `toolkit/toolkit/about/aboutGlean.ftl` — 2
- `browser/browser/confirmationHints.ftl` — 1

**Files absent from the locale:**

- `toolkit/toolkit/global/viewSource.ftl`

**Files present but identical to en-US:**

- `toolkit/toolkit/about/aboutMozilla.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 890, `straight-double` 34, `curly-single` 9, `curly-double` 6 | **corner** |
| apostrophe | `typographic` 9, `straight` 9 | _mixed_ |
| ellipsis | `char` 400 | **char** |
| dash | `em` 52, `en` 1 | **em** |
| nbsp | `total` 1, `space-before-punctuation` 5 | **space-before-punctuation** |
| fullwidth | `punctuation` 8324 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (232)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 141 |
| 2 | Wrong content (says something other than the English) | 73 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 18 |

### A. Functional, markup, variables & plurals

- `about-logins-add-password-tooltip` — `browser/browser/aboutLogins.ftl` — The Add-password tooltip says 'make sure you've changed this site's password, then modify it here'. The en-US says to make sure you are saving your current password.
    - Current: `請確認您更改過此網站的密碼，再於此處修改。`
    - Source: `Make sure you’re saving your current password for this site.`
    - Suggest: `請確認您儲存的是此網站目前使用的密碼。`
    - en-US: 'Make sure you're saving your current password for this site.' This tooltip is shown when adding a new password. Telling the user to have changed the password first and then 'modify' it does not fit that context.
- `about-logins-confirm-export-dialog-message2` — `browser/browser/aboutLogins.ftl` — The translation tells the user to delete their passwords after export. The en-US says to delete the exported file.
    - Current: `建議您在使用完檔案後立即刪除密碼`
    - Source: `When you export, your passwords are saved to a file with readable text. When you’re done using the file, we recommend deleting it so others who use this device can’t see your passwords.`
    - Suggest: `建議您在使用完檔案後立即刪除該檔案`
    - en-US: 'When you're done using the file, we recommend deleting it'. Here 'it' is the exported file. The zh-TW says 刪除密碼 (delete the passwords), which could lead a user to remove their saved passwords.
- `about-logins-login-list-empty-search-title2` — `browser/browser/aboutLogins.ftl` — The empty-search title says 'No passwords saved' instead of 'No passwords found'.
    - Current: `未儲存密碼`
    - Source: `No passwords found`
    - Suggest: `找不到密碼`
    - en-US: 'No passwords found'. It appears when a search has no matches. It reuses the no-saved-passwords text, which wrongly tells the user they have no saved passwords.
- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — The word 'tabs' is missing, so the notification reads 'Closed N Firefox(es)'.
    - Current: `已關閉 { $closedCount } 個 { -brand-short-name }`
    - Source: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab closed [other] { $closedCount } { -brand-short-name } tabs closed`
    - Suggest: `已關閉 { $closedCount } 個 { -brand-short-name } 分頁`
    - en-US: '{ $closedCount } { -brand-short-name } tabs closed'. The noun 分頁 was dropped, which changes what was closed.
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — The memory-learning checkbox is rendered as 'Learn the differences between classic browsing and Smart Windows'.
    - Current: `了解傳統上網方式與{ -smart-window-brand-name(plural-form: "true") }的差異`
    - Source: `label: Learn from browsing in Classic and { -smart-window-brand-name }`
    - Suggest: `從傳統視窗與{ -smart-window-brand-name(plural-form: "true") }的上網活動學習`
    - en-US: 'Learn from browsing in Classic and Smart Windows'. This is a setting that lets the assistant learn from browsing activity. The translation turns it into an informational phrase, so the user cannot tell what the checkbox enables.
- `smart-window-model-custom-info` — `browser/browser/aiFeatures.ftl` — 'Custom model' is rendered as 'custom mode' (模式 instead of 模型).
    - Current: `使用自訂模式時`
    - Source: `message: When you use a custom model, { -smart-window-brand-name } may not work as expected.`
    - Suggest: `使用自訂模型時`
    - en-US: 'When you use a custom model'. The surrounding strings consistently use 自訂模型.
- `aiwindow-firstrun-model-subtitle-v2` — `browser/browser/aiWindow.ftl` — 'Across your tabs' is rendered as 'across different devices'.
    - Current: `在不同裝置間進行摘要、比對、探索`
    - Source: `Each model can help you to summarize, compare, and explore across your tabs. Switch anytime.`
    - Suggest: `在您的分頁間進行摘要、比對、探索`
    - en-US: 'Each model can help you to summarize, compare, and explore across your tabs.' The translation claims the models work across devices, which is a capability the source does not mention.
- `aiwindow-starter-scroll-start` — `browser/browser/aiWindow.ftl` — 'Scroll back' for the conversation-starter pill row is rendered as 'scroll up'. The matching 'Scroll forward' is rendered as 'scroll down'.
    - Current: `向上捲動`
    - Source: `aria-label: Scroll back tooltiptext: Scroll back`
    - Suggest: `向前捲動`
    - The comment says these buttons scroll the pill row toward its start or end. That row is horizontal, so up and down give the wrong direction.
- `smartwindow-search-loader-text` — `browser/browser/aiWindowContent.ftl` — 'Loaded search results in this tab' is rendered as 'in this window'.
    - Current: `已於此視窗載入搜尋結果。`
    - Source: `Loaded search results in this tab. Analyzing…`
    - Suggest: `已於此分頁載入搜尋結果。`
    - The developer comment says the results were loaded into the current tab and that the tab's content changed. 視窗 (window) points the user to the wrong place.
- `appmenu-update-other-instance-message` — `browser/browser/appMenuNotifications.ftl` — 'A new Firefox update is available' is rendered as 'Firefox has been released'.
    - Current: `{ -brand-shorter-name } 已經推出，但由於`
    - Source: `A new { -brand-shorter-name } update is available, but it can’t be installed because another copy of { -brand-shorter-name } is running. Close it to continue the update, or choose to update anyway (the other copy may no…`
    - Suggest: `已推出新的 { -brand-shorter-name } 更新，但由於`
    - The en-US is about a new update being available. The translation drops 'update' and 'new', so the message is about the product being released.
- `fxa-menu-device-view-all-synced-tabs` — `browser/browser/appmenu.ftl` — `fxa-menu-device-view-all-synced-tabs` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$tabCount ->} [one] 檢視 { $tabCount } 個同步的分頁 [other] 檢視全部 { $tabCount } 個同步的分頁`
    - Source: `label: {$tabCount ->} [one] View { $tabCount } Synced Tab [other] View All { $tabCount } Synced Tabs`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — The praise message 'Nice work organizing your tabs' is rendered as an instruction, 'Organize your tabs well'.
    - Current: `好好整理您的分頁`
    - Source: `Nice work organizing your tabs`
    - Suggest: `分頁整理得真好`
    - The comment says this is shown when every suggested group has already been created. The translation tells the user to organize their tabs instead of acknowledging that they already did.
- `menu-share-copy-links` — `browser/browser/browser.ftl` — `menu-share-copy-links` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] 複製鏈結 [other] 複製 { $count } 個鏈結`
    - Source: `accesskey: L label: {$count ->} [one] Copy Link [other] Copy { $count } Links`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-countdown` — `browser/browser/browser.ftl` — `urlbar-result-dates-countdown` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilStart ->} [one] { $name } · 明天 [other] { $name } · { $daysUntilStart } 天後`
    - Source: `{$daysUntilStart ->} [one] { $name } · In { $daysUntilStart } day [other] { $name } · In { $daysUntilStart } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-countdown-range` — `browser/browser/browser.ftl` — `urlbar-result-dates-countdown-range` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilStart ->} [one] { $name } · 明天開始 [other] { $name } · { $daysUntilStart } 天後開始`
    - Source: `{$daysUntilStart ->} [one] { $name } · Starts in { $daysUntilStart } day [other] { $name } · Starts in { $daysUntilStart } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `urlbar-result-dates-ongoing` — `browser/browser/browser.ftl` — `urlbar-result-dates-ongoing` has plural variant ['one'], which zh-TW does not have
    - Current: `{$daysUntilEnd ->} [one] { $name } · 明天結束 [other] { $name } · { $daysUntilEnd } 天後結束`
    - Source: `{$daysUntilEnd ->} [one] { $name } · Ends in { $daysUntilEnd } day [other] { $name } · Ends in { $daysUntilEnd } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `contextual-manager-passwords-update-label` — `browser/browser/contextual-manager.ftl` — The edit-form label 'Update password' is rendered as the past-tense confirmation 'Password updated'.
    - Current: `已更新密碼`
    - Source: `label: Update password`
    - Suggest: `更新密碼`
    - This is the label of the login form in edit mode, paired with 新增密碼 ('Add password'). The translation tells the user an update has already happened before they have saved anything.
- `customkeys-description` — `browser/browser/customkeys.ftl` — 'Control how you move around and interact with Firefox' is rendered as 'control how you move the cursor'.
    - Current: `控制您如何移動游標以及與 { -brand-short-name } 互動。`
    - Source: `Control how you move around and interact with { -brand-short-name }.`
    - Suggest: `控制您如何在 { -brand-short-name } 中瀏覽與互動。`
    - In this context 'move around' means navigating the browser with shortcuts, not moving a cursor. The translation narrows the meaning of the keyboard-shortcuts page.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — `downloads-files-not-downloaded` has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [other] 未下載 { $num } 個檔案。 [one] 未下載檔案。`
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `genai-menu-new-badge` — `browser/browser/genai.ftl` — The 'New' feature badge is rendered as 新增 ('Add').
    - Current: `新增`
    - Source: `New`
    - Suggest: `新功能`
    - This badge marks a new menu item. 新增 is the verb 'add', which makes the badge read like an action. The locale uses 新功能 for the same badge elsewhere (main-context-menu-new-feature-badge, ipprotection-recommended-location-badge).
- `genai-settings-chat-localhost-links` — `browser/browser/genai.ftl` — The sentence is reversed: it tells the user to bring their chatbot's llamafile to Mozilla's Innovation group.
    - Current: `將您本機端的私人聊天機器人的 <a data-l10n-name="link1">llamafile</a> 帶到 { -vendor-short-name } 的創新群組使用。`
    - Source: `Bring your own private local chatbot such as <a data-l10n-name="link1">llamafile</a> from { -vendor-short-name }’s Innovation group.`
    - Suggest: `使用您自己的本機私人聊天機器人，例如 { -vendor-short-name } 創新團隊推出的 <a data-l10n-name="link1">llamafile</a>。`
    - en-US: 'Bring your own private local chatbot such as llamafile from Mozilla's Innovation group.' llamafile comes from the Innovation group and is only an example. The translation gets the relationship backwards.
- `migration-wizard-progress-success-history` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-history` has plural variant ['one'], which zh-TW does not have
    - Current: `{$maxAgeInDays ->} [one] 昨天以來 [other] 過去 { $maxAgeInDays } 天以來的資料`
    - Source: `{$maxAgeInDays ->} [one] From the last day [other] From the last { $maxAgeInDays } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `fxa-adoption-addresses-backup-title` — `browser/browser/newtab/asrouter.ftl` — Saved (postal) addresses are rendered as 網址 (web addresses/URLs)
    - Current: `一起備份儲存的網址吧！`
    - Source: `Let’s back up your saved addresses`
    - Suggest: `一起備份儲存的地址吧！`
    - This message is about saved autofill addresses. Its subtitle uses 地址, but the title says 網址, which means URLs.
- `root-certificate-succession-infobar-january-message` — `browser/browser/newtab/asrouter.ftl` — 'Problems' is narrowed to 'startup problems', and the date is missing 日
    - Current: `可能會在 2025 年 1 月 14 起遇到啟動問題`
    - Source: `<strong>Older versions of { -brand-short-name } may start to have problems on January 14, 2025.</strong>`
    - Suggest: `可能會在 2025 年 1 月 14 日起開始遇到問題`
    - The en-US says only 'may start to have problems'; it does not say the problems are at startup. The sibling March message writes the date with 日.
- `home-prefs-sections-rows-option-srd` — `browser/browser/newtab/newtab.ftl` — `home-prefs-sections-rows-option-srd` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `newtab-custom-row-selector2` — `browser/browser/newtab/newtab.ftl` — `newtab-custom-row-selector2` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `newtab-wallpaper-error-upload-file-type` — `browser/browser/newtab/newtab.ftl` — This file-type error tells the user to retry later instead of telling them to use an image file
    - Current: `請稍後再重新上傳圖片。`
    - Source: `We couldn’t upload your file. Please try again with an image file.`
    - Suggest: `請改用圖片檔案再試一次。`
    - The en-US says 'Please try again with an image file.' The error is about the file type, so 'try again later' sends the user the wrong way.
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — 'Backed by the Mozilla Foundation' becomes 'developed by the Mozilla Foundation'
    - Current: `由 Mozilla 基金會開發的`
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet more open, accessible, and better for everyone.`
    - Suggest: `由 Mozilla 基金會支持的`
    - The en-US says Firefox is backed by the Foundation, not developed by it. The same change appears in onboarding-gratitude-security-and-privacy-subtitle.
- `onboarding-easy-setup-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — 'Helps stop companies' becomes 'automatically blocks the programs that let big companies follow you', which is an unhedged promise
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `可幫助防止企業在網路上偷偷跟蹤您`
    - The en-US says the browser 'helps stop companies from secretly following you'. The Chinese drops the hedge and claims the browser automatically blocks this tracking. It also narrows 'companies' to 大企業 (big companies).
- `security-visits-number` — `browser/browser/pageInfo.ftl` — `security-visits-number` has plural variant ['one'], which zh-TW does not have
    - Current: `{$visits ->} [0] 沒有 [one] 有，1 次 [other] 有，{ $visits } 次`
    - Source: `{$visits ->} [0] No [one] Yes, once [other] Yes, { $visits } times`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — The policy's purpose is misdescribed: the Chinese says the page is blocked in order to block third-party modules
    - Current: `防止使用者開啟第三方模組資訊（about:third-party）頁面，以封鎖第三方模組注入 { -brand-short-name } 程序。`
    - Source: `Prevent the user from using Third-party Module Information (about:third-party) to block third-party modules injected into the { -brand-short-name } process.`
    - Suggest: `防止使用者透過第三方模組資訊（about:third-party）頁面封鎖注入 { -brand-short-name } 程序的第三方模組。`
    - The en-US says the policy stops the user from using about:third-party to block injected modules. The Chinese 以封鎖… turns module blocking into the purpose of the policy, which is the reverse of what it does.
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — 'Set the default value for' is dropped, so this reads like an enforcing policy rather than a default
    - Current: `允許 { -brand-short-name } 提供記住儲存登入帳號與密碼的功能。`
    - Source: `Set the default value for allowing { -brand-short-name } to offer to remember saved logins and passwords. Both true and false values are accepted.`
    - Suggest: `設定是否允許 { -brand-short-name } 提供記住登入資訊與密碼的預設值。`
    - The en-US is 'Set the default value for allowing …'. Its sibling policy-OfferToSaveLogins enforces the setting. Without the word 'default', administrators cannot tell the two policies apart.
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — The legal representation is turned into an obligation to obtain authorization from every user
    - Current: `您必須獲得您提供使用此瀏覽器的所有使用者授權，並代表他們同意使用條款。`
    - Source: `Do not display the Terms of Use and Privacy Notice upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.`
    - Suggest: `您聲明您接受，並有權代表所有您提供此瀏覽器使用權限的人員接受使用條款。`
    - The en-US says 'You represent that you accept and have the authority to accept…'. The developer comment says this means 'you confirm/declare'. The Chinese instead says you 'must obtain authorization from all users', which is a different legal statement.
- `appearance-browser-icon-entry-group` — `browser/browser/preferences/browserIcon.ftl` — The en-US says "taskbar", but the translation says 工具列, which means "toolbar".
    - Current: `選擇要在工具列、桌面與開始選單顯示的自訂圖示。`
    - Source: `description: Choose a custom icon for your taskbar, desktop and start menu. label: Browser icon`
    - Suggest: `選擇要在工作列、桌面與開始選單顯示的自訂圖示。`
    - The developer comment says the icon appears on the desktop, taskbar and Start Menu. The same file already uses 工作列 for taskbar in appearance-browser-icon-pin-button (釘選到工作列). 工具列 is the browser toolbar, which is a different thing.
- `home-prefs-sections-rows-option` — `browser/browser/preferences/preferences.ftl` — `home-prefs-sections-rows-option` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `preferences-ai-controls-pdfjs-control` — `browser/browser/preferences/preferences.ftl` — "Accessible" (usable with assistive technology) is translated as 親和力, which means friendly or approachable.
    - Current: `讓圖片更有親和力`
    - Source: `description: When you add images to PDFs, this adds descriptions to make them accessible. label: Image alt text in { -brand-short-name } PDF viewer`
    - Suggest: `讓圖片更容易使用輔助技術存取`
    - This feature generates alt text so images can be read by assistive technology. 更有親和力 says the images become more approachable, which loses the accessibility meaning completely.
- `preferences-ai-controls-tab-group-suggestions-control` — `browser/browser/preferences/preferences.ftl` — The translation says the feature manages the user's tabs, but the source only says it suggests names and organization.
    - Current: `管理您的分頁，並提供名稱建議。`
    - Source: `description: Get suggestions to name and organize your tabs. label: Tab group suggestions`
    - Suggest: `取得為分頁命名與整理分頁的建議。`
    - The en-US is "Get suggestions to name and organize your tabs." Both naming and organizing are suggestions. The translation instead states that the feature itself manages your tabs.
- `delete-profile-page-title-2` — `browser/browser/profiles.ftl` — 'Profile' is rendered as 原則 ('policy') in the delete page title.
    - Current: `刪除「{ $profilename }」原則`
    - Source: `Delete “{ $profilename }” profile`
    - Suggest: `刪除「{ $profilename }」設定檔`
    - en-US is 'Delete “{ $profilename }” profile'. 原則 means policy. Every other string in this file uses 設定檔 for profile, including delete-profile-header-2 right next to it.
- `new-profile-page-header-description` — `browser/browser/profiles.ftl` — 'Privacy protections' is rendered as 'security protections' (安全性保護).
    - Current: `強大的安全性保護設定`
    - Source: `Each profile keeps its unique browsing history and settings separate from your other profiles. Plus, { -brand-short-name }’s strong privacy protections are on by default.`
    - Suggest: `強大的隱私保護設定`
    - en-US is 'Firefox’s strong privacy protections are on by default'. 安全性 means security, which is a different claim. restored-profile-page-header-description has the same wording.
- `restored-profile-page-header-description` — `browser/browser/profiles.ftl` — 'Privacy protections' is rendered as 'security protections' (安全性保護).
    - Current: `強大的安全性保護設定`
    - Source: `Each profile keeps its unique browsing history and settings separate from your other profiles. Plus, { -brand-short-name }’s strong privacy protections are on by default.`
    - Suggest: `強大的隱私保護設定`
    - Same issue as new-profile-page-header-description: the en-US says 'privacy protections'.
- `protection-report-page-summary-default` — `browser/browser/protections.ftl` — The assertive 'protects' variant keeps the hedged 'can protect' (可).
    - Current: `可在背景保護您的隱私`
    - Source: `{ -brand-short-name } protects your privacy behind the scenes while you browse. This is a personalized summary of those protections, including tools to take control of your online security.`
    - Suggest: `會在背景保護您的隱私`
    - The developer comments separate the two summaries: one says 'can' because protections are off, this one says Firefox is actively protecting you. The translation is identical to protection-report-page-summary, so the difference is lost.
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — 'Try risk-free' is rendered as 'try for free' (免費試用).
    - Current: `免費試用 { -mozilla-vpn-brand-name }`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `無風險試用 { -mozilla-vpn-brand-name }`
    - 'Risk-free' refers to a money-back guarantee on a paid subscription. 免費試用 promises a free trial, a pricing claim the source does not make.
- `cfr-protections-panel-body` — `browser/browser/protectionsPanel.ftl` — 'Protects you from many of the most common trackers' became a flat promise that common trackers can't record you.
    - Current: `{ -brand-short-name } 不讓常見的追蹤器記錄您的上網行為。`
    - Source: `Keep your data to yourself. { -brand-short-name } protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `{ -brand-short-name } 可保護您不受許多最常見的追蹤器記錄上網行為。`
    - The en-US limits the claim to 'many of' the common trackers. The translation drops that limit and says Firefox stops common trackers outright, a promise the product does not make.
- `protections-panel-description-shim-allowed` — `browser/browser/protectionsPanel.ftl` — 'Partially unblocked' is rendered as plainly 'unblocked'.
    - Current: `已解除封鎖下列標示的追蹤器`
    - Source: `Some trackers marked below have been partially unblocked on this page because you interacted with them.`
    - Suggest: `已部分解除封鎖下列標示的追蹤器`
    - en-US is 'Some trackers marked below have been partially unblocked on this page'. Dropping 'partially' tells the user the trackers were fully unblocked, which overstates what the browser did.
- `protections-panel-shim-allowed-indicator` — `browser/browser/protectionsPanel.ftl` — 'Tracker partially unblocked' became 'some trackers have been unblocked'.
    - Current: `部分追蹤器已解除封鎖`
    - Source: `tooltiptext: Tracker partially unblocked`
    - Suggest: `追蹤器已部分解除封鎖`
    - In the translation 部分 modifies the trackers ('some trackers'), not the unblocking. The en-US says each tracker is only partially unblocked.
- `report-broken-site-panel-reason-adblocker-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — 'Ad blocker' is translated as 'ad trackers' (廣告追蹤器).
    - Current: `網站要求關閉廣告追蹤器`
    - Source: `label: Site asked to turn off ad blocker`
    - Suggest: `網站要求關閉廣告封鎖器`
    - en-US is 'Site asked to turn off ad blocker'. 廣告追蹤器 means ad trackers, which is close to the opposite thing, so the report reason no longer makes sense.
- `menu-view-open-tabs` — `browser/browser/sidebar.ftl` — The noun phrase 'Open Tabs' reads as the command 'open a tab'.
    - Current: `開啟分頁`
    - Source: `label: Open Tabs`
    - Suggest: `已開啟的分頁`
    - The comment says 'Open Tabs' is a noun phrase for tabs currently open, not an instruction. 開啟分頁 reads as an imperative. delete-profile-tabs in profiles.ftl uses 開啟的分頁 for the same idea. sidebar-menu-open-tabs-header and sidebar-opentabs-title use the same wording.
- `sidebar-menu-open-tabs-label` — `browser/browser/sidebar.ftl` — The noun phrase 'Open tabs' reads as the command 'open a tab'.
    - Current: `開啟分頁`
    - Source: `label: Open tabs`
    - Suggest: `已開啟的分頁`
    - The comment says this is a noun phrase, not an instruction to open tabs.
- `site-permissions-open-blocked-popups` — `browser/browser/sitePermissions.ftl` — `site-permissions-open-blocked-popups` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] 開啟被封鎖的彈出型視窗… [other] 開啟 { $count } 個被封鎖的彈出型視窗…`
    - Source: `{$count ->} [one] Open { $count } blocked pop-up… [other] Open { $count } blocked pop-ups…`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-confirm-close-all-duplicate-tabs-text` — `browser/browser/tabbrowser.ftl` — 'Last active tab' is rendered as 'last opened tab'.
    - Current: `只保留最後一個開啟的分頁`
    - Source: `We’ll close duplicate tabs in this window. The last active tab will stay open.`
    - Suggest: `只保留最後使用的分頁`
    - en-US is 'The last active tab will stay open'. The most recently opened duplicate and the most recently used one can be different tabs, so the dialog misdescribes which tab survives.
- `tabbrowser-empty-private-tab-title` — `browser/browser/tabbrowser.ftl` — The tab title 'New Private Tab' reads as the command 'Open new private tab'.
    - Current: `開新隱私分頁`
    - Source: `New Private Tab`
    - Suggest: `新隱私分頁`
    - This is the title shown on an empty tab. The regular-tab equivalent is 新分頁 (tabbrowser-empty-tab-title). 開新… is the wording for the menu command.
- `taskbar-tab-title-default` — `browser/browser/taskbartabs.ftl` — The window title '{ $name } in Firefox' reads as the instruction 'Open { $name } with Firefox'.
    - Current: `用 { -brand-full-name } 開啟 { $name }`
    - Source: `{ $name } in { -brand-full-name }`
    - Suggest: `{ $name } — { -brand-full-name }`
    - This is part of the web app's window title. The translation turns a label into a command. taskbar-tab-title-container has the same wording.
- `taskbar-tab-urlbar-button-close` — `browser/browser/taskbartabs.ftl` — 'Taskbar' is translated as 'sidebar' (側邊欄).
    - Current: `從側邊欄移除分頁`
    - Source: `tooltiptext: Remove tab from taskbar`
    - Suggest: `從工作列移除分頁`
    - en-US is 'Remove tab from taskbar'. The translation says the tab is removed from the sidebar, which is a different UI element.
- `taskbar-tab-urlbar-button-open` — `browser/browser/taskbartabs.ftl` — 'Taskbar' is translated as 'toolbar' (工具列).
    - Current: `將分頁新增到工具列`
    - Source: `tooltiptext: Add tab to taskbar`
    - Suggest: `將分頁新增到工作列`
    - en-US is 'Add tab to taskbar'. This feature pins a site to the Windows taskbar (工作列). 工具列 is the browser's own toolbar, so the tooltip describes a different action.
- `webrtc-allow-share-camera-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — The camera-only delegation prompt also asks about the microphone.
    - Current: `使用您的攝影機與麥克風嗎`
    - Source: `Allow { $origin } to give { $thirdParty } access to your camera?`
    - Suggest: `使用您的攝影機嗎`
    - en-US is 'Allow { $origin } to give { $thirdParty } access to your camera?'. Adding 與麥克風 makes the user think they are also granting microphone access. A separate string exists for camera plus microphone.
- `safebrowsing.reportedAttackSite` — `browser/chrome/browser/browser.properties` — 'Reported Attack Site!' is translated as 'Known harmful site!', which turns a report into a confirmed fact.
    - Current: `已知的有害網站！`
    - Source: `Reported Attack Site!`
    - Suggest: `已檢舉為攻擊網站！`
    - The source says the site has been reported. 已知 ('known') states it as certain. The neighbouring strings use 已檢舉為… for 'Reported …'.
- `dialogTitleAddBookmarkFolder` — `browser/chrome/browser/places/bookmarkProperties.properties` — 'Add bookmark folder' is translated as 'Add bookmarks toolbar'.
    - Current: `新增書籤工具列`
    - Source: `Add bookmark folder`
    - Suggest: `新增書籤資料夾`
    - 書籤工具列 means 'bookmarks toolbar', but this dialog creates a bookmark folder. The same file already uses 資料夾 for 'folder' (newFolderDefault = 新資料夾).
- `dialogTitleEditBookmarkFolder` — `browser/chrome/browser/places/bookmarkProperties.properties` — 'Edit bookmark folder' is translated as 'Edit bookmarks toolbar'.
    - Current: `編輯書籤工具列`
    - Source: `Edit bookmark folder`
    - Suggest: `編輯書籤資料夾`
    - This is the same error as the add-folder title: 工具列 (toolbar) is used where the source means a folder.
- `permission.shortcuts.label` — `browser/chrome/browser/sitePermissions.properties` — 'Override keyboard shortcuts' is translated as 'Ignore keyboard shortcuts'.
    - Current: `忽略快速鍵`
    - Source: `Override keyboard shortcuts`
    - Suggest: `蓋過快速鍵`
    - This permission lets a site take over (override) the browser's shortcuts, not ignore them. Elsewhere the locale uses 蓋過 for 'override' with shortcuts (aboutAddons shortcuts-system: 無法蓋過 … 的快速鍵).
- `REG_APP_DESC` — `browser/installer/custom.properties` — 'Protection from online identity theft' becomes a 'new online scam-site detection feature'
    - Current: `（包含新的線上辨識詐騙網站功能）`
    - Source: `$BrandShortName delivers safe, easy web browsing. A familiar user interface, enhanced security features including protection from online identity theft, and integrated search let you get the most out of the web.`
    - Suggest: `（包含線上身分盜用防護）`
    - The en-US names protection from identity theft. The Chinese describes a different feature and adds 'new'.
- _…and 90 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `restart-required-single-instance-question` — `browser/browser/aboutRestartRequired.ftl` — The product name is hard-coded as 'Firefox' where en-US uses no brand at all.
    - Current: `安裝多種 Firefox`
    - Source: `I don’t use multiple profiles or instances. Why is this happening?`
    - Suggest: `安裝多種 { -brand-short-name }`
    - en-US: 'I don't use multiple profiles or instances.' The locale adds a literal 'Firefox', which will show in Nightly, Developer Edition and other branded builds. The sibling question uses { -brand-short-name }.
- `newtab-privacy-message-info-10` — `browser/browser/newtab/newtab.ftl` — A preposition is missing before 任何網站
    - Current: `即可任何網站都使用`
    - Source: `Save passwords in { -brand-short-name } to use strong, unique logins everywhere.`
    - Suggest: `即可在任何網站都使用`
    - Without 在 the clause is ungrammatical.
- `newtab-sports-widget-message-survey-widget-body` — `browser/browser/newtab/newtab.ftl` — A stray 在 makes the sentence ungrammatical
    - Current: `幫助我們在改善未來的小工具功能`
    - Source: `Share your feedback to help us improve future widgets. Then, try the new one in your lineup.`
    - Suggest: `幫助我們改善未來的小工具功能`
    - The 在 has no role here and breaks the verb phrase.
- `mr1-return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — Typo: a stray 斯 after 隱私
    - Current: `又快又有隱私斯的瀏覽器`
    - Source: `You’ve got a fast, private browser at your fingertips. Now you can add <b>{ $addon-name }</b> and do even more with { -brand-short-name }.`
    - Suggest: `又快又有隱私的瀏覽器`
    - 斯 is a stray character that makes the phrase ungrammatical.
- `onboarding-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — The particle 的 is duplicated
    - Current: `最完整的的上網體驗`
    - Source: `Complete these steps to get the most out of your browsing experience.`
    - Suggest: `最完整的上網體驗`
    - Repeated particle.
- `speech-dispatcher-lib-missing` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because the Speech Dispatcher library is missing.`
    - Suggest: `Speech Dispatcher`
    - The file comment says Speech Dispatcher is the name of a speech synthesis tool and shouldn't be localized. The same translated name appears in all five speech-dispatcher-* messages.
- `speech-dispatcher-lib-too-old` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because Speech Dispatcher needs to be updated.`
    - Suggest: `Speech Dispatcher`
    - The file comment says the name must not be localized.
- `speech-dispatcher-missing-symbol` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because the Speech Dispatcher library is broken.`
    - Suggest: `Speech Dispatcher`
    - The file comment says the name must not be localized.
- `speech-dispatcher-no-voices` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because voices aren’t available in Speech Dispatcher.`
    - Suggest: `Speech Dispatcher`
    - The file comment says the name must not be localized.
- `speech-dispatcher-open-fail` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because Speech Dispatcher won’t open.`
    - Suggest: `Speech Dispatcher`
    - The file comment says the name must not be localized.
- `addProtocolHandlerMessage` — `browser/chrome/browser/feeds/subscribe.properties` — Typo: 鍵結 should be 鏈結 ('link').
    - Current: `鍵結`
    - Source: `Add “%1$S” as an application for %2$S links?`
    - Suggest: `鏈結`
    - The locale's word for 'links' is 鏈結, as in openProtocolHandlerPermissionEntryLabel '%S:// 鏈結' and externalProtocolChkMsg. 鍵結 is a different word that means 'chemical bond'.
- `STUB_BLURB_FIRST3` — `browser/installer/nsisstrings.properties` — 'open web' is left in English, although the sibling string translates it
    - Current: `準備好在 Open Web 中漫遊`
    - Source: `Get ready to roam on the open web`
    - Suggest: `準備好在開放的網路中漫遊`
    - The sibling STUB_BLURB_FIRST2_DEVEDITION renders 'the open web' as 開放的網路環境. 'Open web' is a common phrase, not a brand.
- `netmonitor.emptyBrowserToolbox` — `devtools/client/netmonitor.properties` — Typo: 請出請求 should be 送出請求.
    - Current: `請出請求`
    - Source: `Perform a request to see detailed information about network activity.`
    - Suggest: `送出請求`
    - en-US: 'Perform a request to see detailed information about network activity.' 請出 is not a word in this context. The intended word is clearly 送出 ('send').
- `toolbox-mode-parent-process-container` — `devtools/client/toolbox.ftl` — Typo: 謹 ('careful') is used instead of 僅 ('only').
    - Current: `謹聚焦於來自父處理程序的資源。`
    - Source: `title: Only focus on resources from the parent process.`
    - Suggest: `僅聚焦於來自父處理程序的資源。`
    - en-US: 'Only focus on resources from the parent process.' 謹 is a homophone typo for 僅.
- `toolbox.meatballMenu.button.tooltip` — `devtools/client/toolbox.properties` — Uses the variant character 説 instead of the standard Traditional Chinese 說.
    - Current: `取得説明`
    - Source: `Customize Developer Tools and Get Help`
    - Suggest: `取得說明`
    - The rest of the zh-TW tree writes 說明 (for example 輔助說明圖示 and 說明 in accessibility.ftl). 説 is the Japanese / variant form.
- `SelectOptionsLengthAssignmentWarning` — `dom/chrome/dom/dom.properties` — The API name HTMLOptionsCollection.length, marked do-not-translate, is truncated to 'HTMLOptionsCollection.lengt'.
    - Current: `HTMLOptionsCollection.lengt（`
    - Source: `Refused to expand <select> option list via assignment to HTMLOptionsCollection.length (value %1$S). The maximum supported size is %2$S.`
    - Suggest: `HTMLOptionsCollection.length（`
    - The localization note says not to translate HTMLOptionsCollection.length. The final 'h' is missing, so developers see an identifier that does not exist.
- `BlockTopLevelDataURINavigation` — `dom/chrome/security/security.properties` — 'data: URI', marked do-not-translate, is split and translated as '資料: … URI', which breaks the meaning.
    - Current: `不允許瀏覽頂層資料: 不允許的 URI`
    - Source: `Navigation to toplevel data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `不允許瀏覽頂層 data: URI`
    - The note says not to translate 'data: URI'. The result reads as 'Navigating to top-level data not allowed: disallowed URI'.
- `addon-badge-verified4` — `toolkit/toolkit/about/aboutAddons.ftl` — Adds 'we' to the badge tooltip, which the developer comment explicitly forbids
    - Current: `我們審查過此擴充套件，確認符合安全性與運作效能標準`
    - Source: `title: This extension has been reviewed to meet standards for security and performance`
    - Suggest: `此擴充套件已經過審查，符合安全性與運作效能標準`
    - The comment says this string must work in forks and must avoid personalising words like 'our' or 'we', so it doesn't imply some organisation other than Mozilla did the review. The zh-TW opens with 我們 ('we reviewed'), which is exactly what the comment rules out.
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — 'Important' was translated although the comment says not to
    - Current: `重要`
    - Source: `Important`
    - Suggest: `Important`
    - The comment says 'Important' refers to the filter-syntax option and should not be translated, because it is technical syntax.
- `experimental-features-media-jxl` — `toolkit/toolkit/firefoxlabs/features.ftl` — The experiment title is translated although the developer comment says to keep it in English
    - Current: `媒體：JPEG XL 格式`
    - Source: `label: Media: JPEG XL`
    - Suggest: `Media: JPEG XL`
    - The comment reads: 'The title of the experiment should be kept in English as it may be referenced by various online articles'.

### D. Terminology, register & consistency

- `about-logins-import-report-row-index` — `browser/browser/aboutLogins.ftl` — 'Row N' is rendered as 'N 行', which reads as 'N rows' rather than 'row number N'.
    - Current: `{ $number } 行`
    - Source: `Row { $number }`
    - Suggest: `第 { $number } 行`
    - This labels a single row index in the import report. Chinese needs the ordinal 第 here. Without it the text reads as a count.
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — The pronoun 他們 (used for people) refers to the memories.
    - Current: `久而久之，他們可讓回覆結果對您更有幫助。`
    - Source: `{ -smart-window-brand-name } can learn from your chats, browsing, or both to create memories. They make answers more helpful over time.`
    - Suggest: `久而久之，記憶可讓回覆結果對您更有幫助。`
    - 'They' refers to memories, which are inanimate. Standard written Chinese uses 它們 for things, or repeats the noun.
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — The phrase 關閉分頁起來 is ungrammatical.
    - Current: `若您還是想要關閉分頁起來`
    - Source: `If you still want to close tabs, choose <strong>Retry</strong> and make your selection in the card that opens.`
    - Suggest: `若您還是想要關閉分頁`
    - The complement 起來 does not combine with 關閉. It looks copied from the group-tabs sibling string (將分頁群組起來).
- `identity-https-only-info-turn-on3` — `browser/browser/browser.ftl` — The verb 'turn on' is missing: 請對此網站 HTTPS 升級.
    - Current: `請對此網站 HTTPS 升級`
    - Source: `Turn on HTTPS upgrades for this site if you want { -brand-short-name } to upgrade the connection when possible.`
    - Suggest: `請對此網站開啟 HTTPS 升級`
    - en-US: 'Turn on HTTPS upgrades for this site...'. Without 開啟 the sentence has no action verb. The sibling turn-off string correctly says 關閉 HTTPS 升級.
- `customkeys-dev-profiler-capture` — `browser/browser/customkeys.ftl` — Typo: 補捉 should be 捕捉.
    - Current: `補捉效能檢測檔`
    - Source: `Capture a Performance Profile`
    - Suggest: `捕捉效能檢測檔`
    - The correct word for 'capture' is 捕捉, as in profiler-popup-capture-button in appmenu.ftl.
- `downloads-blocked-download-detailed-info` — `browser/browser/downloads.ftl` — Typo: 擋案 should be 檔案.
    - Current: `無用擋案`
    - Source: `{ $url } attempted to automatically download multiple files. The site could be broken or trying to store spam files on your device.`
    - Suggest: `無用檔案`
    - 擋 means 'block'. 'File' is 檔案, which is used everywhere else in the tree.
- `multi-cta-fox-doodle-msix-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `並釘選至工具列與開始選單。`
    - Source: `Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and pin it to your taskbar and Start menu.`
    - Suggest: `並釘選至工作列與開始選單。`
    - The source is 'pin it to your taskbar and Start menu'.
- `multi-cta-fox-doodle-pin-checkbox` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar'. The same file uses 工作列 in spotlight-pin-primary-button.
- `multi-cta-fox-doodle-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `並釘選至工具列。`
    - Source: `{$sel_1 ->} [macos] Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and keep it in your Dock. [other] Keep your favorite privacy-focuse…`
    - Suggest: `並釘選至工作列。`
    - The source is 'pin it to your taskbar'.
- `set-default-menu-message-row-layout-subtitle-variant` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `保留在您的工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your Dock. [other] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your taskbar.`
    - Suggest: `保留在您的工作列`
    - The source is 'keep it in your taskbar'.
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `釘選到工具列，`
    - Source: `Pin { -brand-shorter-name } to your taskbar so the browser you chose is always there when you need it.`
    - Suggest: `釘選到工作列，`
    - The source is 'Pin … to your taskbar'.
- `home-custom-homepage-delete-address-button` — `browser/browser/newtab/newtab.ftl` — A website address is called 地址 (postal address), while the neighbouring strings use 網址
    - Current: `刪除地址`
    - Source: `aria-label: Delete address title: Delete address`
    - Suggest: `刪除網址`
    - In the same subpage, 'Enter address' and 'Add address' are rendered 請輸入網址 and 新增網址. The delete button should match them.
- `fx100-thank-you-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar'.
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — 'Pin to taskbar' is rendered with 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar' (the Windows taskbar, 工作列). 工具列 means the browser toolbar.
- `mr2022-onboarding-pin-primary-button-label-msix` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `釘選到工具列與開始選單`
    - Source: `Pin { -brand-short-name } to taskbar and start menu`
    - Suggest: `釘選到工作列與開始選單`
    - Windows taskbar is 工作列.
- `onboarding-checklist-pin` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar) instead of 工作列
    - Current: `釘選到工具列`
    - Source: `Pin { -brand-short-name } to taskbar`
    - Suggest: `釘選到工作列`
    - In zh-TW Windows the taskbar is 工作列. In Firefox, 工具列 is the browser toolbar, which is a different thing. Other strings that mean pinning to the taskbar already use 工作列: launch-on-login-spotlight-pin-taskbar-checkbox, spotlight-pin-primary-button, mr2022-upgrade-onboarding-pin-private-window-primary-button-label and ICONS_TASKBAR.
- `onboarding-refresh-tou-pin` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 新增到您的工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Add { -brand-short-name } to your taskbar`
    - Suggest: `將 { -brand-short-name } 新增到您的工作列`
    - The source is 'Add … to your taskbar'.
- `permissions-site-speaker-desc` — `browser/browser/preferences/permissions.ftl` — 允許 ("allow") appears twice, which makes the sentence ungrammatical.
    - Current: `您可指定要允許哪些網站允許選擇音訊輸出裝置。`
    - Source: `The following websites have requested to select an audio output device. You can specify which websites are allowed to select an audio output device.`
    - Suggest: `您可指定要允許哪些網站選擇音訊輸出裝置。`
    - The en-US is "You can specify which websites are allowed to select an audio output device." The second 允許 is redundant and garbles the sentence.
- `connection-dns-over-https-url-item` — `browser/browser/preferences/preferences.ftl` — Typo: 使用者 ("user") is written where 使用 ("use") is meant.
    - Current: `使用者此提供者進行 DNS over HTTPS 解析`
    - Source: `label: { $name } tooltiptext: Use this provider for resolving DNS over HTTPS`
    - Suggest: `使用此提供者進行 DNS over HTTPS 解析`
    - The en-US is "Use this provider…". As written, the tooltip reads "user this provider…", which is ungrammatical. Compare the matching string in connection.ftl: 使用預設網址來解析 DNS over HTTPS.
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — The personal pronoun 他 is used for a product.
    - Current: `他的速度`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `它的速度`
    - The quote refers to the VPN product ('its speed'). 他 is the pronoun for a person; a thing takes 它.
- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — The possessive 的 is used where the measure word 個 belongs.
    - Current: `複製群組中的 { $linkCount } 的鏈結`
    - Source: `label: {$linkCount ->} [1] Copy link in group [other] Copy { $linkCount } links in group`
    - Suggest: `複製群組中的 { $linkCount } 個鏈結`
    - 'Copy { $linkCount } links in group' needs the classifier 個 after the number. As written, the phrase is ungrammatical.
- `sourceTabs.closeTabsToEnd` — `devtools/client/debugger.properties` — 'Tabs' is translated 標籤 here, while every neighboring source-tab menu item uses 分頁.
    - Current: `關閉右方標籤`
    - Source: `Close tabs to the right`
    - Suggest: `關閉右方分頁`
    - The sibling items in the same context menu are 關閉分頁, 關閉其他分頁 and 關閉所有分頁. 標籤 usually means 'label' or 'tag' in this tree.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — `preventedConsoleClear` quotes “保存紀錄” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “保留紀錄”
    - Current: `由於開啟「保存紀錄」功能，已防止執行 console.clear()`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `保留紀錄`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — The quoted option name 保存紀錄 does not match the actual setting label 保留紀錄.
    - Current: `「保存紀錄」`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `「保留紀錄」`
    - The developer comment says 'Persist Logs' must stay in sync with webconsole.console.settings.menu.item.enablePersistentLogs.label. That label is translated 保留紀錄, so the message names a setting the user can't find.
- `EncMetaUserDefined` — `dom/chrome/layout/htmlparser.properties` — The encoding identifier windows-1252 is misspelled as 'windown-1252'.
    - Current: `windown-1252`
    - Source: `A meta tag was used to declare the character encoding as x-user-defined. This was interpreted as a windows-1252 declaration instead for compatibility with intentionally mis-encoded legacy fonts. This site should migrate…`
    - Suggest: `windows-1252`
    - This is a literal encoding label and must match exactly.
- `CookieBlockedForeignByETP` — `netwerk/necko.properties` — 開啟 is duplicated: 'turned on Enhanced Tracking Protection turn-on feature'.
    - Current: `且開啟加強型追蹤保護開啟功能`
    - Source: `Request to access cookie or storage on “%1$S” was blocked because we are blocking all third-party storage access requests and Enhanced Tracking Protection is enabled.`
    - Suggest: `且已開啟加強型追蹤保護功能`
    - The duplicated word is a grammatical error.
- `TrackerUriBlockedByETP` — `netwerk/necko.properties` — Typo: 開用了 is not a word; it should be 開啟了 or 啟用了.
    - Current: `開用了`
    - Source: `The resource at “%1$S” was blocked because Enhanced Tracking Protection is enabled.`
    - Suggest: `開啟了`
    - This is a spelling error. The rest of the file uses 開啟.
- `disabled-unsigned-description` — `toolkit/toolkit/about/aboutAddons.ftl` — Typo: 原件 should be 元件
    - Current: `以下原件尚未經過驗證`
    - Source: `The following add-ons have not been verified for use in { -brand-short-name }. You can <label data-l10n-name="find-addons">find replacements</label> or ask the developer to get them verified.`
    - Suggest: `以下元件尚未經過驗證`
    - 原件 means 'original document'. The intended word is 元件 (add-on component), as used throughout the file.
- `shortcuts-remove-button` — `toolkit/toolkit/about/aboutAddons.ftl` — Keyboard 'shortcut' is rendered as 捷徑 (file/desktop shortcut) instead of 快速鍵
    - Current: `移除捷徑`
    - Source: `aria-label: Remove shortcut`
    - Suggest: `移除快速鍵`
    - This button removes an extension keyboard shortcut. Every other string in the shortcut-management screen uses 快速鍵, and the tree uses 捷徑 for desktop shortcuts and new-tab shortcuts.
- `about-httpsonly-suggestion-box-www-text` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — Grammar: extra 的 in 目前的開啟的
    - Current: `目前的開啟的`
    - Source: `There is a secure version of <em>www.{ $websiteUrl }</em>. You can visit this page instead of <em>{ $websiteUrl }</em>.`
    - Suggest: `目前開啟的`
    - The doubled 的 is ungrammatical.
- `about-webauthn-credential-list-subsection-title` — `toolkit/toolkit/about/aboutWebauthn.ftl` — 'Credentials' is rendered as 'account and password', unlike every other string in the file
    - Current: `帳號密碼：`
    - Source: `Credentials:`
    - Suggest: `登入資訊：`
    - Everywhere else in this file 'credentials' is 登入資訊 (e.g. 管理登入資訊, 列出登入資訊, 裝置上未儲存登入資訊). Security-token credentials aren't passwords, so 帳號密碼 is also wrong in substance.
- `experimental-features-link-previews-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — Typo: 可會 should be 可能會 ('may')
    - Current: `預覽內容可會包含`
    - Source: `{$sel_1 ->} [macos] To learn more about a webpage before you click, hover over a link and press Shift (⇧) plus Option (⌥) or Alt. Previews can include details like title and reading time. For some webpages, AI can also…`
    - Suggest: `預覽內容可能會包含`
    - 可會 is not a valid word. The fragment appears in both platform variants.
- `cookie-banner-handled-webconsole` — `toolkit/toolkit/global/cookieBannerHandling.ftl` — Garbled sentence: 'on behalf of' is missing, so it reads as '…has user replied to the cookie banner'
    - Current: `已使用者回覆了 Cookie 橫幅`
    - Source: `{ -brand-shorter-name } handled a cookie banner on behalf of the user.`
    - Suggest: `已代替使用者回覆了 Cookie 橫幅`
    - Without 代替 (on behalf of) the sentence is ungrammatical.
- `webext-site-perms-description-gated-perms-webserial` — `toolkit/toolkit/global/extensions.ftl` — Typo: 損畫 should be 損壞 ('damage')
    - Current: `可能會造成損畫`
    - Source: `These are devices like microcontrollers, 3D printers, and other devices that connect via USB, serial ports, or Bluetooth.  You will be able to choose which devices the website can access.  Websites are normally not allo…`
    - Suggest: `可能會造成損壞`
    - 損畫 is not a word. The parallel MIDI string correctly uses 損壞.
- `wallet-custom-scheme-warning-heading` — `toolkit/toolkit/global/handlerDialog.ftl` — The question particle is duplicated (嗎嗎)
    - Current: `開啟您的數位錢包嗎嗎？`
    - Source: `heading: Allow this site to open your digital wallet?`
    - Suggest: `開啟您的數位錢包嗎？`
    - There is a stray repeated 嗎.
- `fp-certerror-bad-domain-what-can-you-do-body` — `toolkit/toolkit/neterror/certError.ftl` — Typo: 已支 should be 已知 ('known issues')
    - Current: `有已支的問題`
    - Source: `Probably nothing, since it’s likely there’s a problem with the site itself. Sites use certificates issued by a certificate authority to prove they’re really who they say they are. But if you’re on a corporate network, y…`
    - Suggest: `有已知的問題`
    - 已支 is a misspelling of 已知.
- `neterror-load-osx-permission` — `toolkit/toolkit/neterror/netError.ftl` — Ungrammatical conditional clause: 是 is missing
    - Current: `若您要開啟的本地區域網路頁面`
    - Source: `If you are trying to load a local network page, please check that { -brand-short-name } has been granted Local Network permissions in the macOS Privacy & Security settings.`
    - Suggest: `若您要開啟的是本地區域網路頁面`
    - Without 是 the clause has no predicate and does not read as a sentence.
- `sec-error-crl-expired` — `toolkit/toolkit/neterror/nsserrors.ftl` — The subject noun (CRL) is missing: 'the certificate issuer's ___ has expired'
    - Current: `憑證簽發者的已過期`
    - Source: `The CRL for the certificate’s issuer has expired. Update it or check your system date and time.`
    - Suggest: `憑證簽發者的憑證廢止清冊已過期`
    - The sentence has no head noun after 的, so it does not say what expired.

### E. Typography, punctuation & spacing

- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — 'Classic Window' is rendered as 經典視窗 here, while the rest of the Smart Window UI uses 傳統視窗.
    - Current: `切換智慧視窗與經典視窗`
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic Windows`
    - Suggest: `切換智慧視窗與傳統視窗`
    - The same file uses 傳統視窗 throughout, including the v1 tooltip of this string and the switcher labels. Users would see two different names for the same window type.
- `appmenu-remote-tabs-opensettings` — `browser/browser/appmenu.ftl` — 'Settings' is rendered as 選項 (Options). The same menu uses 設定.
    - Current: `選項`
    - Source: `label: Settings`
    - Suggest: `設定`
    - en-US now says 'Settings'. The appmenu comment says Settings is used on all platforms, and appmenuitem-settings in the same file is 設定.
- `taskbar-tabs-chat-callout-title` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `從工具列直接聊天`
    - Source: `Chat from your taskbar`
    - Suggest: `從工作列直接聊天`
    - Same issue as the other taskbar-tabs callouts.
- `taskbar-tabs-chat-callout-title-v3` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `從工具列保持連線`
    - Source: `Stay connected from your taskbar`
    - Suggest: `從工作列保持連線`
    - Same issue as the other taskbar-tabs callouts.
- `taskbar-tabs-email-callout-title` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `在工具列收發信件`
    - Source: `Keep your email in your taskbar`
    - Suggest: `在工作列收發信件`
    - Same issue as the other taskbar-tabs callouts.
- `taskbar-tabs-email-callout-title-v3` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `從工具列直接開啟收件匣`
    - Source: `Keep your inbox in your taskbar`
    - Suggest: `從工作列直接開啟收件匣`
    - Same issue as the other taskbar-tabs callouts.
- `taskbar-tabs-media-callout-title-v3` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `將您的影片網站放在工具列`
    - Source: `Keep your streaming in your taskbar`
    - Suggest: `將您的影片網站放在工作列`
    - Same issue as the other taskbar-tabs callouts. The non-v3 media title correctly uses 工作列.
- `taskbar-tabs-social-callout-title` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar).
    - Current: `放置於工具列`
    - Source: `Keep your favorite feeds in your taskbar`
    - Suggest: `放置於工作列`
    - Same issue as the other taskbar-tabs callouts. 工作列 is the locale's term for the OS taskbar.
- `taskbar-tabs-value-prop-callout-title` — `browser/browser/featureCallout.ftl` — The Windows taskbar is rendered as 工具列 (toolbar) instead of 工作列.
    - Current: `將此網站新增至工具列`
    - Source: `Add this site to your taskbar`
    - Suggest: `將此網站新增至工作列`
    - Taskbar tabs pin a site to the OS taskbar. zh-TW uses 工作列 for the taskbar, including in this same file (taskbar-tabs-callout-primary-button-v3 釘選到工作列, the media and gaming titles) and in aboutPrivateBrowsing. 工具列 is the browser toolbar.
- `taskbar-tabs-value-prop-callout-title-v3` — `browser/browser/featureCallout.ftl` — 'Taskbar' is rendered as 工具列 (toolbar), right next to a button that says 釘選到工作列.
    - Current: `將您最愛的網站釘選至工具列`
    - Source: `Pin your favorite sites to your taskbar`
    - Suggest: `將您最愛的網站釘選至工作列`
    - The callout title says toolbar and its primary button says taskbar, for the same action.
- `menu-application-settings` — `browser/browser/menubar.ftl` — The macOS 'Settings…' item is rendered as 選項 ('Options').
    - Current: `選項…`
    - Source: `label: Settings…`
    - Suggest: `設定…`
    - The comment says this item replaces 'Preferences' with 'Settings' on macOS Ventura and later. zh-TW macOS uses 設定, and the same file translates menu-settings as 設定.
- `preferences-ai-controls-description` — `browser/browser/preferences/preferences.ftl` — "Features enhanced with AI" is rendered as AI 擴充功能 ("AI extension features"), while the rest of the page uses AI 強化功能.
    - Current: `是否使用 AI 擴充功能`
    - Source: `You always have a choice in { -brand-short-name }, including whether to use features enhanced with AI. More controls coming soon.`
    - Suggest: `是否使用 AI 強化功能`
    - Every other string on the AI controls page uses 強化功能 for "enhancements" (for example 封鎖 AI 強化功能). In zh-TW, 擴充 suggests add-ons or extensions, which is a different concept in Firefox settings.
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — The menu path starts with the old name 選項 ("Options"), but the page is now called 設定 ("Settings").
    - Current: `您可以到「選項 > 隱私權與安全性 > Cookie 與網站資料」清除目前儲存的網站資料。`
    - Source: `<strong>{ -brand-short-name } is running out of disk space.</strong> Website contents may not display properly. You can clear stored data in Settings > Privacy & Security > Cookies and Site Data.`
    - Suggest: `您可以到「設定 > 隱私權與安全性 > Cookie 與網站資料」清除目前儲存的網站資料。`
    - The en-US path is Settings > Privacy & Security, and this locale names the page 設定 (settings-page-title, category-nav-heading). A user following 選項 would look for a menu entry that does not exist.
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — 'Harmful programs' in the unwanted-software title is translated as 惡意軟體 ('malware'), so it reads the same as the malware title.
    - Current: `此網站可能含有惡意軟體`
    - Source: `The site ahead may contain harmful programs`
    - Suggest: `此網站可能含有有害程式`
    - en-US uses different titles for the unwanted-software page ('harmful programs') and the harmful page ('malware'). The locale renders both as 惡意軟體, even though the unwanted-software descriptions in this file use 有害軟體.
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — An invisible zero-width space (U+200B) sits between 透 and 明 in 透明度.
    - Current: `透​明度`
    - Source: `Opacity`
    - Suggest: `透明度`
    - The stray U+200B is part of the displayed or spoken title text. It can break screen-reader pronunciation and text search, and it appears nowhere else in the tree.
- `underscript` — `dom/chrome/accessibility/AccessFu.properties` — 'underscript' is announced as 下標, the same word as 'subscript'.
    - Current: `underscript = 下標`
    - Source: `underscript`
    - Suggest: `底標`
    - overscript is rendered 頂標. Using 下標 for both subscript and underscript makes two different MathML roles sound identical.
- `ImageMapCircleNegativeRadius` — `dom/chrome/layout/layout_errors.properties` — `ImageMapCircleNegativeRadius` uses straight double quotes
    - Current: `<area shape="circle"> 標籤中的 "coords" 屬性不能有負的半徑。`
    - Source: `The “coords” attribute of the <area shape="circle"> tag has a negative radius.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapCircleWrongNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapCircleWrongNumberOfCoords` uses straight double quotes
    - Current: `<area shape="circle"> 標籤中的 "coords" 屬性並不是 "center-x,center-y,radius" 的格式。`
    - Source: `The “coords” attribute of the <area shape="circle"> tag is not in the “center-x,center-y,radius” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapPolyOddNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapPolyOddNumberOfCoords` uses straight double quotes
    - Current: `<area shape="poly"> 標籤中的 "coords" 屬性少了最後的 y 座標 (正確格式是 "x1,y1,x2,y2,…")。`
    - Source: `The “coords” attribute of the <area shape="poly"> tag is missing the last “y” coordinate (the correct format is “x1,y1,x2,y2 …”).`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapPolyWrongNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapPolyWrongNumberOfCoords` uses straight double quotes
    - Current: `<area shape="poly"> 標籤中的 "coords" 屬性並不是 "x1,y1,x2,y2,…" 的格式。`
    - Source: `The “coords” attribute of the <area shape="poly"> tag is not in the “x1,y1,x2,y2 …” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — `ImageMapRectBoundsError` uses straight double quotes
    - Current: `<area shape="rect">的"coords" 屬性不是 "left,top,right,bottom" 格式。`
    - Source: `The “coords” attribute of the <area shape="rect"> tag is not in the “left,top,right,bottom” format.`
    - The locale's quote convention is `corner` (890 occurrences).
- `BlockMixedDisplayContent` — `dom/chrome/security/security.properties` — 'mixed content' is written 混和 here but 混合 elsewhere in the same file.
    - Current: `已封鎖載入混和的顯示內容`
    - Source: `Blocked loading mixed display content “%1$S”`
    - Suggest: `已封鎖載入混合的顯示內容`
    - LoadingMixedActiveContent2 and LoadingMixedDisplayContent2 in the same file use 混合, the standard term for mixed content. BlockMixedActiveContent and csp.properties obsoleteBlockAllMixedContent also use 混和.
- `xpath-bad-extension-function` — `dom/dom/xslt.ftl` — The sentence ends with a full-width comma instead of a full stop.
    - Current: `呼叫了未知的 XPath 擴充功能，`
    - Source: `An unknown XPath extension function was called.`
    - Suggest: `呼叫了未知的 XPath 擴充函式。`
    - en-US ends with a period and nothing follows. A trailing comma looks truncated. 'function' is also rendered 功能 (feature) here but 函式 elsewhere in the file.
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — 'passkey' is left in English here, but the same dialog translates it as 密碼金鑰
    - Current: `建立一把 Passkey`
    - Source: `{ $origin } wants to create a passkey for { $rpId }.`
    - Suggest: `建立一把密碼金鑰`
    - webauthn-a-passkey-label, webauthn-another-passkey-label and webauthn-specific-passkey-label all use 密碼金鑰, so the same prompt shows two terms. webauthn-related-origin-use-header has the same issue.

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
