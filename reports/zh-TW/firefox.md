# Firefox l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f278b81a68aa` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-08 @ `f300f0e83cb6` |
| **Mode** | incremental |
| **Strings reviewed this run** | 188 of 16,875 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (2)

- `protections-panel-shim-allowed-indicator` — `browser/browser/protectionsPanel.ftl` — The tooltip says some trackers were unblocked; the source says this one tracker was partly unblocked.
    - Current: `已解除封鎖部分追蹤器`
    - Source: `tooltiptext: Tracker partially unblocked`
    - Suggest: `已部分解除封鎖追蹤器`
    - en-US "Tracker partially unblocked" means the blocking of this tracker was partly lifted. The zh-TW reads as "unblocked some of the trackers", which moves "partially" from the unblocking to the number of trackers.
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — "Risk-free" is translated as "free trial", which is a different offer.
    - Current: `免費試用`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `零風險試用`
    - "Try risk-free" refers to a money-back guarantee on a paid subscription. It is not a free trial. "免費試用" ("try for free") tells users the VPN can be used at no cost.

### ✅ Fixed since the last run (185)

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
- `smart-window-model-custom-info` — `browser/browser/aiFeatures.ftl` — 'Custom model' is rendered as 'custom mode' (模式 instead of 模型).
    - Current: `使用自訂模式時`
    - Source: `message: When you use a custom model, { -smart-window-brand-name } may not work as expected.`
    - Suggest: `使用自訂模型時`
    - en-US: 'When you use a custom model'. The surrounding strings consistently use 自訂模型.
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — The pronoun 他們 (used for people) refers to the memories.
    - Current: `久而久之，他們可讓回覆結果對您更有幫助。`
    - Source: `{ -smart-window-brand-name } can learn from your chats, browsing, or both to create memories. They make answers more helpful over time.`
    - Suggest: `久而久之，記憶可讓回覆結果對您更有幫助。`
    - 'They' refers to memories, which are inanimate. Standard written Chinese uses 它們 for things, or repeats the noun.
- `aiwindow-firstrun-model-subtitle-v2` — `browser/browser/aiWindow.ftl` — 'Across your tabs' is rendered as 'across different devices'.
    - Current: `在不同裝置間進行摘要、比對、探索`
    - Source: `Each model can help you to summarize, compare, and explore across your tabs. Switch anytime.`
    - Suggest: `在您的分頁間進行摘要、比對、探索`
    - en-US: 'Each model can help you to summarize, compare, and explore across your tabs.' The translation claims the models work across devices, which is a capability the source does not mention.
- `contextual-manager-passwords-update-label` — `browser/browser/contextual-manager.ftl` — The edit-form label 'Update password' is rendered as the past-tense confirmation 'Password updated'.
    - Current: `已更新密碼`
    - Source: `label: Update password`
    - Suggest: `更新密碼`
    - This is the label of the login form in edit mode, paired with 新增密碼 ('Add password'). The translation tells the user an update has already happened before they have saved anything.
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
- `downloads-blocked-potentially-insecure` — `browser/browser/downloads.ftl` — Half-width colon followed by a space is used instead of the locale's full-width colon.
    - Current: `未下載檔案: 有`
    - Source: `File not downloaded: Potential security risk.`
    - Suggest: `未下載檔案：有`
    - zh-TW consistently uses full-width punctuation; a half-width colon plus space deviates from the established convention.
- `bookmark-properties-title-add-folder` — `browser/browser/editBookmarkOverlay.ftl` — "Add bookmark folder" is translated as "Add bookmarks toolbar".
    - Current: `新增書籤工具列`
    - Source: `Add bookmark folder`
    - Suggest: `新增書籤資料夾`
    - In this locale 書籤工具列 means the Bookmarks Toolbar. The source says "bookmark folder", which elsewhere in this file is 資料夾.
- `bookmark-properties-title-edit-folder` — `browser/browser/editBookmarkOverlay.ftl` — "Edit bookmark folder" is translated as "Edit bookmarks toolbar".
    - Current: `編輯書籤工具列`
    - Source: `Edit bookmark folder`
    - Suggest: `編輯書籤資料夾`
    - 書籤工具列 means the Bookmarks Toolbar, not a bookmark folder.
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
- `genai-menu-new-badge` — `browser/browser/genai.ftl` — The 'New' feature badge is rendered as 新增 ('Add').
    - Current: `新增`
    - Source: `New`
    - Suggest: `新功能`
    - This badge marks a new menu item. 新增 is the verb 'add', which makes the badge read like an action. The locale uses 新功能 for the same badge elsewhere (main-context-menu-new-feature-badge, ipprotection-recommended-location-badge).
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — The settings section name "Tabs and browsing" is translated as an action phrase ("tabs, and browse"), so the path to the setting is wrong.
    - Current: `分頁並瀏覽`
    - Source: `You won’t see this menu when you select text. Visit Settings <span data-l10n-name="chevron"></span> Tabs and browsing to show it again.`
    - Suggest: `分頁與瀏覽`
    - "Tabs and browsing" is the name of a Settings section, shown after a chevron. 並 turns it into a sequence of actions ("tabs and browse"), so it no longer names the section.
- `genai-selection-callout-text` — `browser/browser/genai.ftl` — This string uses the informal 你, while the surrounding strings use 您.
    - Current: `你可以透過`
    - Source: `Search or copy when you select text. Choose which actions appear with the <span data-l10n-name="more-actions">•••</span> menu.`
    - Suggest: `您可以透過`
    - The neighbouring strings in this batch use the polite 您 (e.g. downloads, sanitize), so 你 here is inconsistent with the locale's form of address.
- `fxa-adoption-addresses-backup-title` — `browser/browser/newtab/asrouter.ftl` — Saved (postal) addresses are rendered as 網址 (web addresses/URLs)
    - Current: `一起備份儲存的網址吧！`
    - Source: `Let’s back up your saved addresses`
    - Suggest: `一起備份儲存的地址吧！`
    - This message is about saved autofill addresses. Its subtitle uses 地址, but the title says 網址, which means URLs.
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
- `root-certificate-succession-infobar-january-message` — `browser/browser/newtab/asrouter.ftl` — 'Problems' is narrowed to 'startup problems', and the date is missing 日
    - Current: `可能會在 2025 年 1 月 14 起遇到啟動問題`
    - Source: `<strong>Older versions of { -brand-short-name } may start to have problems on January 14, 2025.</strong>`
    - Suggest: `可能會在 2025 年 1 月 14 日起開始遇到問題`
    - The en-US says only 'may start to have problems'; it does not say the problems are at startup. The sibling March message writes the date with 日.
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
- `newtab-privacy-message-info-10` — `browser/browser/newtab/newtab.ftl` — A preposition is missing before 任何網站
    - Current: `即可任何網站都使用`
    - Source: `Save passwords in { -brand-short-name } to use strong, unique logins everywhere.`
    - Suggest: `即可在任何網站都使用`
    - Without 在 the clause is ungrammatical.
- `newtab-wallpaper-error-upload-file-type` — `browser/browser/newtab/newtab.ftl` — This file-type error tells the user to retry later instead of telling them to use an image file
    - Current: `請稍後再重新上傳圖片。`
    - Source: `We couldn’t upload your file. Please try again with an image file.`
    - Suggest: `請改用圖片檔案再試一次。`
    - The en-US says 'Please try again with an image file.' The error is about the file type, so 'try again later' sends the user the wrong way.
- `fx100-thank-you-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 釘選到工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `將 { -brand-short-name } 釘選到工作列`
    - The source is 'Pin … to taskbar'.
- `hnt-card-taskbar-tabs-primary-button` — `browser/browser/newtab/onboarding.ftl` — The button translates "taskbar" as 工具列 ("toolbar") instead of 工作列.
    - Current: `將網站新增至工具列`
    - Source: `Add sites to taskbar`
    - Suggest: `將網站新增至工作列`
    - The en-US says "Add sites to taskbar", meaning the Windows taskbar. The card's header (hnt-card-taskbar-tabs-header) and hnt-card-pin-body both use 工作列 for taskbar, while 工具列 means a browser toolbar. As written, the button names a different place than the header does.
- `mr1-return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — Typo: a stray 斯 after 隱私
    - Current: `又快又有隱私斯的瀏覽器`
    - Source: `You’ve got a fast, private browser at your fingertips. Now you can add <b>{ $addon-name }</b> and do even more with { -brand-short-name }.`
    - Suggest: `又快又有隱私的瀏覽器`
    - 斯 is a stray character that makes the phrase ungrammatical.
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
- `onboarding-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — The particle 的 is duplicated
    - Current: `最完整的的上網體驗`
    - Source: `Complete these steps to get the most out of your browsing experience.`
    - Suggest: `最完整的上網體驗`
    - Repeated particle.
- `onboarding-refresh-tou-pin` — `browser/browser/newtab/onboarding.ftl` — 'Taskbar' is rendered 工具列 (toolbar)
    - Current: `將 { -brand-short-name } 新增到您的工具列`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Add { -brand-short-name } to your taskbar`
    - Suggest: `將 { -brand-short-name } 新增到您的工作列`
    - The source is 'Add … to your taskbar'.
- `appearance-browser-icon-entry-group` — `browser/browser/preferences/browserIcon.ftl` — The en-US says "taskbar", but the translation says 工具列, which means "toolbar".
    - Current: `選擇要在工具列、桌面與開始選單顯示的自訂圖示。`
    - Source: `description: Choose a custom icon for your taskbar, desktop and start menu. label: Browser icon`
    - Suggest: `選擇要在工作列、桌面與開始選單顯示的自訂圖示。`
    - The developer comment says the icon appears on the desktop, taskbar and Start Menu. The same file already uses 工作列 for taskbar in appearance-browser-icon-pin-button (釘選到工作列). 工具列 is the browser toolbar, which is a different thing.
- `more-from-moz-firefox-enterprise-card` — `browser/browser/preferences/moreFromMozilla.ftl` — "regulated" is translated as 受管理 (managed), and a stray 對 makes the sentence ungrammatical.
    - Current: `為受管理或對注重安全性的組織進行瀏覽器治理。`
    - Source: `description: Browser governance for regulated and security-sensitive organizations. label: { -firefox-enterprise-brand-name }`
    - Suggest: `為受法規監管及注重安全性的組織提供瀏覽器治理。`
    - "Regulated organizations" are ones under regulatory oversight, not organizations that are "managed". Also, 或對注重安全性的組織 has a dangling 對 that breaks the sentence.
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
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — The personal pronoun 他 is used for a product.
    - Current: `他的速度`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `它的速度`
    - The quote refers to the VPN product ('its speed'). 他 is the pronoun for a person; a thing takes 它.
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
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — 'Harmful programs' in the unwanted-software title is translated as 惡意軟體 ('malware'), so it reads the same as the malware title.
    - Current: `此網站可能含有惡意軟體`
    - Source: `The site ahead may contain harmful programs`
    - Suggest: `此網站可能含有有害程式`
    - en-US uses different titles for the unwanted-software page ('harmful programs') and the harmful page ('malware'). The locale renders both as 惡意軟體, even though the unwanted-software descriptions in this file use 有害軟體.
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
- `speech-dispatcher-lib-missing` — `browser/browser/speechDispatcher.ftl` — The product name Speech Dispatcher is translated.
    - Current: `語音分配器`
    - Source: `You can’t use speech synthesis because the Speech Dispatcher library is missing.`
    - Suggest: `Speech Dispatcher`
    - The file comment says Speech Dispatcher is the name of a speech synthesis tool and shouldn't be localized. The same translated name appears in all five speech-dispatcher-* messages.
- _…and 125 more._

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
| Files | 331 |
| Strings | 16,875 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 13 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**Files present but identical to en-US:**

- `toolkit/toolkit/about/aboutMozilla.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 906, `straight-double` 25, `curly-single` 9, `curly-double` 6 | **corner** |
| apostrophe | `typographic` 9, `straight` 9 | _mixed_ |
| ellipsis | `char` 405 | **char** |
| dash | `em` 54, `en` 1 | **em** |
| nbsp | `total` 1, `space-before-punctuation` 5 | **space-before-punctuation** |
| fullwidth | `punctuation` 8577 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (55)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 21 |
| 2 | Wrong content (says something other than the English) | 18 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 13 |

### A. Functional, markup, variables & plurals

- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — The word 'tabs' is missing, so the notification reads 'Closed N Firefox(es)'.
    - Current: `已關閉 { $closedCount } 個 { -brand-short-name }`
    - Source: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab closed [other] { $closedCount } { -brand-short-name } tabs closed`
    - Suggest: `已關閉 { $closedCount } 個 { -brand-short-name } 分頁`
    - en-US: '{ $closedCount } { -brand-short-name } tabs closed'. The noun 分頁 was dropped, which changes what was closed.
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
- `customkeys-description` — `browser/browser/customkeys.ftl` — 'Control how you move around and interact with Firefox' is rendered as 'control how you move the cursor'.
    - Current: `控制您如何移動游標以及與 { -brand-short-name } 互動。`
    - Source: `Control how you move around and interact with { -brand-short-name }.`
    - Suggest: `控制您如何在 { -brand-short-name } 中瀏覽與互動。`
    - In this context 'move around' means navigating the browser with shortcuts, not moving a cursor. The translation narrows the meaning of the keyboard-shortcuts page.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — `downloads-files-not-downloaded` has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [other] 未下載 { $num } 個檔案。 [one] 未下載檔案。`
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `genai-settings-chat-localhost-links` — `browser/browser/genai.ftl` — The sentence is reversed: it tells the user to bring their chatbot's llamafile to Mozilla's Innovation group.
    - Current: `將您本機端的私人聊天機器人的 <a data-l10n-name="link1">llamafile</a> 帶到 { -vendor-short-name } 的創新群組使用。`
    - Source: `Bring your own private local chatbot such as <a data-l10n-name="link1">llamafile</a> from { -vendor-short-name }’s Innovation group.`
    - Suggest: `使用您自己的本機私人聊天機器人，例如 { -vendor-short-name } 創新團隊推出的 <a data-l10n-name="link1">llamafile</a>。`
    - en-US: 'Bring your own private local chatbot such as llamafile from Mozilla's Innovation group.' llamafile comes from the Innovation group and is only an example. The translation gets the relationship backwards.
- `migration-wizard-progress-success-history` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-history` has plural variant ['one'], which zh-TW does not have
    - Current: `{$maxAgeInDays ->} [one] 昨天以來 [other] 過去 { $maxAgeInDays } 天以來的資料`
    - Source: `{$maxAgeInDays ->} [one] From the last day [other] From the last { $maxAgeInDays } days`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `home-prefs-sections-rows-option-srd` — `browser/browser/newtab/newtab.ftl` — `home-prefs-sections-rows-option-srd` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `newtab-custom-row-selector2` — `browser/browser/newtab/newtab.ftl` — `newtab-custom-row-selector2` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
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
- `home-prefs-sections-rows-option` — `browser/browser/preferences/preferences.ftl` — `home-prefs-sections-rows-option` (`.label`) has plural variant ['one'], which zh-TW does not have
    - Current: `{$num ->} [one] { $num } 行 [other] { $num } 行`
    - Source: `label: {$num ->} [one] { $num } row [other] { $num } rows`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `preferences-ai-controls-pdfjs-control` — `browser/browser/preferences/preferences.ftl` — "Accessible" (usable with assistive technology) is translated as 親和力, which means friendly or approachable.
    - Current: `讓圖片更有親和力`
    - Source: `description: When you add images to PDFs, this adds descriptions to make them accessible. label: Image alt text in { -brand-short-name } PDF viewer`
    - Suggest: `讓圖片更容易使用輔助技術存取`
    - This feature generates alt text so images can be read by assistive technology. 更有親和力 says the images become more approachable, which loses the accessibility meaning completely.
- `site-permissions-open-blocked-popups` — `browser/browser/sitePermissions.ftl` — `site-permissions-open-blocked-popups` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] 開啟被封鎖的彈出型視窗… [other] 開啟 { $count } 個被封鎖的彈出型視窗…`
    - Source: `{$count ->} [one] Open { $count } blocked pop-up… [other] Open { $count } blocked pop-ups…`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `taskbar-tab-title-default` — `browser/browser/taskbartabs.ftl` — The window title '{ $name } in Firefox' reads as the instruction 'Open { $name } with Firefox'.
    - Current: `用 { -brand-full-name } 開啟 { $name }`
    - Source: `{ $name } in { -brand-full-name }`
    - Suggest: `{ $name } — { -brand-full-name }`
    - This is part of the web app's window title. The translation turns a label into a command. taskbar-tab-title-container has the same wording.
- `MUI_TEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — The meaning is reversed: the en-US says closing other apps lets Setup avoid a reboot, but the Chinese says a reboot may be needed
    - Current: `安裝前建議您關閉其他的常駐程式，為了更新相關的系統檔案可能必須重新啟動電腦。`
    - Source: `This wizard will guide you through the installation of $BrandFullNameDA.  It is recommended that you close all other applications before starting Setup. This will make it possible to update relevant system files without…`
    - Suggest: `安裝前建議您關閉其他所有程式，這樣就可以更新相關的系統檔案而不需要重新啟動電腦。`
    - The en-US says 'This will make it possible to update relevant system files without having to reboot your computer.' The Chinese says the computer may have to be restarted to update system files, which is the opposite.
- `MUI_UNTEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — The uninstall wizard tells the user to close Firefox 'before installing' instead of before uninstalling
    - Current: `安裝前請確定 $BrandFullNameDA 已經關閉。`
    - Source: `This wizard will guide you through the uninstallation of $BrandFullNameDA.  Before starting the uninstallation, make sure $BrandFullNameDA is not running.  $_CLICK`
    - Suggest: `開始移除前請確定 $BrandFullNameDA 已經關閉。`
    - The en-US says 'Before starting the uninstallation, make sure … is not running.' This page belongs to the uninstall wizard, but the Chinese says 安裝前 (before installing).
- `inspector-emulation-panel-reduced-motion-no-preference` — `devtools/client/inspector.ftl` — The aria-label reads as 'do not prefer the reduced-motion emulation' instead of 'enable no-preference reduced-motion emulation'.
    - Current: `不偏好減少動畫模擬功能`
    - Source: `(value): No preference aria-label: Enable no preference for reduced motion emulation`
    - Suggest: `啟用「無偏好」減少動畫模擬功能`
    - en-US: 'Enable no preference for reduced motion emulation'. The sibling labels start with 啟用 or 停用. This one drops the action, and its wording suggests declining the emulation.
- `styleeditor-new-button` — `devtools/client/styleeditor.ftl` — 'append' is translated 擴充 ('expand / extend') instead of 附加.
    - Current: `建立並將新的樣式表擴充至文件尾端`
    - Source: `accesskey: N tooltiptext: Create and append a new style sheet to the document`
    - Suggest: `建立並將新的樣式表附加到文件尾端`
    - en-US: 'Create and append a new style sheet to the document'. The import button right next to it correctly uses 附加到文件尾端. 擴充 doesn't mean 'append'.
- `comboboxlist` — `dom/chrome/accessibility/AccessFu.properties` — 'combo box list' is translated as 'multi-select drop-down list' (複選下拉清單).
    - Current: `複選下拉清單`
    - Source: `combo box list`
    - Suggest: `下拉選單清單`
    - Combo boxes are not multi-select. 複選 adds a property the role does not have. comboboxoption (複選下拉清單項目) has the same problem.
- `KillAddonScriptMessage` — `dom/chrome/dom/dom.properties` — The second paragraph refers to the browser and a 'plugin' (外掛程式) instead of the extension script.
    - Current: `瀏覽器可能還在忙碌中，或是已經無法回應。您可以現在就中斷該指令碼，或是繼續等待外掛程式完成工作。`
    - Source: `A script from the extension “%1$S” is running on this page, and making %2$S unresponsive.  It may be busy, or it may have stopped responding permanently. You can stop the script now, or you can continue to see if it wil…`
    - Suggest: `該指令碼可能還在忙碌中，或是已經永久停止回應。您可以現在就中斷該指令碼，或是繼續等待它完成工作。`
    - In en-US, 'It may be busy … see if it will complete' refers to the extension's script. Plugins are a different and obsolete concept.
- `Revert` — `toolkit/chrome/global/commonDialogs.properties` — The 'Revert' dialog button is translated as 'invert selection'
    - Current: `反向選擇(&R)`
    - Source: `&Revert`
    - Suggest: `還原(&R)`
    - 反向選擇 means 'invert selection', a different command from 'revert' (go back to the previous state).
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — The code literal 'events' was changed to 'event', and the sentence no longer says the default is a ping
    - Current: `否則預設的 <code>event</code> 指標是 <code>event</code>`
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
    - Suggest: `否則 <code>event</code> 指標的預設值為 <code>events</code> ping`
    - en-US: 'the default for event metrics is the events ping'. Text inside <code> must not be translated, and the ping is named 'events', not 'event'. The zh-TW also reads as 'the default event metric is event'. A developer following this would pick a ping that doesn't exist.
- `about-networking-ssl-tokens-summary-count` — `toolkit/toolkit/about/aboutNetworking.ftl` — `about-networking-ssl-tokens-summary-count` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] { $count } 個 token [other] { $count } 個 token`
    - Source: `{$count ->} [one] { $count } token [other] { $count } tokens`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `password-manager-update-password-button-delete` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — The button label says it deletes ALL saved passwords, but the action removes only the one saved password
    - Current: `刪除所有已儲存的密碼`
    - Source: `accesskey: R label: Remove saved password`
    - Suggest: `移除已儲存的密碼`
    - en-US 'Remove saved password' acts on the single login in the update doorhanger. The Chinese tells the user the button wipes every stored password, so it claims a much wider deletion than the product performs.

### B. Mistranslation, reversed meaning, wrong names & brand

- `main-context-menu-use-mini-window` — `browser/browser/miniWindow.ftl` — "Section" is translated as 段落 (paragraph), but the feature selects an area of the page.
    - Current: `將段落移動到迷你視窗`
    - Source: `accesskey: w label: Move Section to Mini Window`
    - Suggest: `將區域移動到迷你視窗`
    - The tool selects a rectangular region of the page, and the overlay header already calls it 區域. 段落 means a text paragraph.
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — The tooltip turns the noun phrase 'open tabs from your other devices' into the command 'open the tabs on your other devices'.
    - Current: `開啟您其他裝置上的分頁`
    - Source: `accesskey: t label: Open tabs tooltiptext: Open tabs from your other devices`
    - Suggest: `您其他裝置上開啟的分頁`
    - The developer comment says 'Open' modifies the noun (tabs that are open). This tooltip describes what gets synced; it is not an action, but the zh-TW text reads as an instruction to open tabs.
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — "Risk-free" is translated as "free trial", which is a different offer.
    - Current: `免費試用`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `零風險試用`
    - "Try risk-free" refers to a money-back guarantee on a paid subscription. It is not a free trial. "免費試用" ("try for free") tells users the VPN can be used at no cost.
- `protections-panel-shim-allowed-indicator` — `browser/browser/protectionsPanel.ftl` — The tooltip says some trackers were unblocked; the source says this one tracker was partly unblocked.
    - Current: `已解除封鎖部分追蹤器`
    - Source: `tooltiptext: Tracker partially unblocked`
    - Suggest: `已部分解除封鎖追蹤器`
    - en-US "Tracker partially unblocked" means the blocking of this tracker was partly lifted. The zh-TW reads as "unblocked some of the trackers", which moves "partially" from the unblocking to the number of trackers.
- `permission.register-protocol-handler.label` — `browser/chrome/browser/sitePermissions.properties` — The permission label says "ask me before opening app links" instead of "may the site ask to open app links".
    - Current: `開啟應用程式鏈結前先問我`
    - Source: `Ask to open app links`
    - Suggest: `詢問是否可開啟應用程式鏈結`
    - The developer comment says this permission controls whether the site may ask to open app links. The translation describes the browser asking the user before it opens app links, which is a different setting.
- `download-ui-confirm-private-browsing-message` — `toolkit/toolkit/downloads/downloadUI.ftl` — The singular variant uses the plural 「這些檔案」 (these files) for a single download.
    - Current: `[1] 將無法繼續下載這些檔案。`
    - Source: `{$downloadsCount ->} [1] You won’t be able to resume this download. [other] You won’t be able to resume these downloads.`
    - Suggest: `[1] 將無法繼續下載此檔案。`
    - The en-US [1] variant says "this download", but the translation copies the plural wording 「這些」 (these), so it no longer matches the source.
- `credit-card-label-with-security-code-2` — `toolkit/toolkit/payments/payments.ftl` — The aria-label says the card is saved, instead of saying the security code is saved.
    - Current: `已儲存 { $ariaLabel }，{ $securityCode }`
    - Source: `(value): { $label } \| { $securityCode } ••• aria-label: { $ariaLabel }, { $securityCode } saved`
    - Suggest: `{ $ariaLabel }，已儲存 { $securityCode }`
    - The source reads '{ $ariaLabel }, { $securityCode } saved', so 'saved' applies to the security code. The translation puts 已儲存 in front of the card description, so it says the card was saved.

### C. Grammar, agreement & spelling

- `restart-required-single-instance-question` — `browser/browser/aboutRestartRequired.ftl` — The product name is hard-coded as 'Firefox' where en-US uses no brand at all.
    - Current: `安裝多種 Firefox`
    - Source: `I don’t use multiple profiles or instances. Why is this happening?`
    - Suggest: `安裝多種 { -brand-short-name }`
    - en-US: 'I don't use multiple profiles or instances.' The locale adds a literal 'Firefox', which will show in Nightly, Developer Edition and other branded builds. The sibling question uses { -brand-short-name }.
- `decoder-doctor-no-codecs-linux-message` — `browser/browser/browser.ftl` — 必須的 is used where 必需的 is meant ("required").
    - Current: `必須的視訊解碼器`
    - Source: `To play video, you may need to install the required video codecs.`
    - Suggest: `必需的視訊解碼器`
    - en-US says "required video codecs". The adjective for "needed" is 必需; 必須 is an adverb meaning "must", so 必須的 is wrong here.
- `ip-protection-not-opted-in-inclusions-enabled` — `browser/browser/ipProtection.ftl` — "免費" ("free") appears twice in the same sentence.
    - Current: `每月免費獲得 { $maxUsage } GB 的免費流量`
    - Source: `heading: Ready to try it? message: Get { $maxUsage } GB free each month and choose which sites use VPN.`
    - Suggest: `每月免費獲得 { $maxUsage } GB 流量`
    - Saying "free" twice ("get free … of free data") is redundant and reads awkwardly. The source says "free" only once.
- `tab-context-add-tab-to-group` — `browser/browser/tabbrowser.ftl` — The plural variant uses the possessive 的 where it needs the measure word 個, so it reads 'add the tabs of N to group'.
    - Current: `將 { $tabCount } 的分頁加入至群組`
    - Source: `accesskey: G label: {$tabCount ->} [1] Add to Group [other] Add { $tabCount } Tabs to Group`
    - Suggest: `將 { $tabCount } 個分頁加入至群組`
    - The en-US is 'Add N Tabs to Group'. A number in Chinese needs the classifier 個, as in the sibling string 移動 { $tabCount } 個分頁到. With 的 the phrase is ungrammatical.
- `STUB_BLURB_FIRST3` — `browser/installer/nsisstrings.properties` — 'open web' is left in English, although the sibling string translates it
    - Current: `準備好在 Open Web 中漫遊`
    - Source: `Get ready to roam on the open web`
    - Suggest: `準備好在開放的網路中漫遊`
    - The sibling STUB_BLURB_FIRST2_DEVEDITION renders 'the open web' as 開放的網路環境. 'Open web' is a common phrase, not a brand.
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
- `connection-dns-over-https-url-item` — `browser/browser/preferences/preferences.ftl` — Typo: 使用者 ("user") is written where 使用 ("use") is meant.
    - Current: `使用者此提供者進行 DNS over HTTPS 解析`
    - Source: `label: { $name } tooltiptext: Use this provider for resolving DNS over HTTPS`
    - Suggest: `使用此提供者進行 DNS over HTTPS 解析`
    - The en-US is "Use this provider…". As written, the tooltip reads "user this provider…", which is ungrammatical. Compare the matching string in connection.ftl: 使用預設網址來解析 DNS over HTTPS.

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
- `underscript` — `dom/chrome/accessibility/AccessFu.properties` — 'underscript' is announced as 下標, the same word as 'subscript'.
    - Current: `underscript = 下標`
    - Source: `underscript`
    - Suggest: `底標`
    - overscript is rendered 頂標. Using 下標 for both subscript and underscript makes two different MathML roles sound identical.

---

## 4. Appendix

### Dismissed by hand (14)

- `PENeverMatchingHostSelector` — `dom/chrome/layout/css.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The suggestion left the English word 'featureless' untranslated in the Chinese text, which is a new error.
- `PostMessageSharedMemoryObjectToCrossOriginWarning` — `dom/chrome/dom/dom.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>post is an action verb, not postmessage.</p>
- `about-webauthn-auth-info-certifications` — `toolkit/toolkit/about/aboutWebauthn.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>learn = 了解 is more accurate for this string</p>
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>no difference from approved string?</p>
- `contentanalysis-error-message-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `customize-mode-toolbarspring` — `browser/browser/customizeMode.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `finduri-AgeInMonths-isgreater` — `toolkit/chrome/places/places.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The suggestion didn't fix the finding: 個月以前 still means '%S months ago', just like the original, so the 'older than' meaning is still missing.
- `menu-application-settings` — `browser/browser/menubar.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `permission-dialog-remember-file` — `toolkit/toolkit/global/handlerDialog.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `support-remote-settings-status-broken` — `toolkit/toolkit/about/aboutSupport.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `tab` — `dom/chrome/accessibility/mac/accessible.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>should keep Passkey intact, as per glossary.</p>

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (186)

- `about-logins-add-password-tooltip` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-09
- `about-logins-confirm-export-dialog-message2` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-09
- `about-logins-login-list-empty-search-title2` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-09
- `smart-window-model-custom-info` — `browser/browser/aiFeatures.ftl` — fixed 2026-11-09
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — fixed 2026-11-09
- `aiwindow-firstrun-model-subtitle-v2` — `browser/browser/aiWindow.ftl` — fixed 2026-11-09
- `contextual-manager-passwords-update-label` — `browser/browser/contextual-manager.ftl` — fixed 2026-11-09
- `customkeys-dev-profiler-capture` — `browser/browser/customkeys.ftl` — fixed 2026-11-09
- `downloads-blocked-download-detailed-info` — `browser/browser/downloads.ftl` — fixed 2026-11-09
- `downloads-blocked-potentially-insecure` — `browser/browser/downloads.ftl` — fixed 2026-11-09
- `bookmark-properties-title-add-folder` — `browser/browser/editBookmarkOverlay.ftl` — fixed 2026-11-09
- `bookmark-properties-title-edit-folder` — `browser/browser/editBookmarkOverlay.ftl` — fixed 2026-11-09
- `taskbar-tabs-chat-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-chat-callout-title-v3` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-email-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-email-callout-title-v3` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-media-callout-title-v3` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-social-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-value-prop-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `taskbar-tabs-value-prop-callout-title-v3` — `browser/browser/featureCallout.ftl` — fixed 2026-11-09
- `genai-menu-new-badge` — `browser/browser/genai.ftl` — fixed 2026-11-09
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — fixed 2026-11-09
- `genai-selection-callout-text` — `browser/browser/genai.ftl` — fixed 2026-11-09
- `fxa-adoption-addresses-backup-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `multi-cta-fox-doodle-msix-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `multi-cta-fox-doodle-pin-checkbox` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `multi-cta-fox-doodle-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `root-certificate-succession-infobar-january-message` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `set-default-menu-message-row-layout-subtitle-variant` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-09
- `home-custom-homepage-delete-address-button` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-09
- `newtab-privacy-message-info-10` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-09
- `newtab-wallpaper-error-upload-file-type` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-09
- `fx100-thank-you-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `hnt-card-taskbar-tabs-primary-button` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `mr1-return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `mr2022-onboarding-pin-primary-button-label-msix` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `onboarding-checklist-pin` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `onboarding-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
