# Firefox l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `4f181c236f19` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `aadbf7c9bb44` |
| **Previous run** | 2026-11-16 @ `d1d139c060cf` |
| **Mode** | incremental |
| **Strings reviewed this run** | 327 of 17,120 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (7)

- `smartwindow-onboarding-model-label` — `browser/browser/aiWindow.ftl` — Uses informal 你 instead of the polite 您 used throughout the surrounding onboarding strings.
    - Current: `挑選你的 AI 模型`
    - Source: `Pick your AI model`
    - Suggest: `挑選您的 AI 模型`
    - All sibling strings in the Smart Window onboarding flow (e.g. 依照您的喜好設定, 選擇…要如何了解您) address the user with 您; this label breaks the established form of address.
- `ipprotection-message-default-browser-confirmation` — `browser/browser/ipProtection.ftl` — The heading leaves out "more", so the additional locations read as the total number of locations.
    - Current: `您已獲得 { $additionalLocationsCount } 個 VPN 連線位置`
    - Source: `heading: {$additionalLocationsCount ->} [one] You’ve got { $additionalLocationsCount } more VPN location [other] You’ve got { $additionalLocationsCount } more VPN locations message: Thanks for making { -brand-short-name…`
    - Suggest: `您已額外獲得 { $additionalLocationsCount } 個 VPN 連線位置`
    - The en-US says "You've got N more VPN locations", and the developer comment describes the variable as the number of additional locations. The translation says the user has N locations, which gets the count wrong.
- `ipprotection-unlimited-bandwidth-promo` — `browser/browser/ipProtection.ftl` — There is a space after the date placeholder, but the zh-TW date ends in a Chinese character.
    - Current: `{ $endDate } 前`
    - Source: `Unlimited bandwidth until { $endDate }`
    - Suggest: `{ $endDate }前`
    - $endDate is a month-day date, which renders as something like 1月31日 in zh-TW and ends in 日. The locale's convention is to space a placeholder by what it expands to, so no space should come before 前.
- `mui-text-welcome-info-text` — `browser/installer/mui.ftl` — The translation says updating system files may require a reboot, but the source says closing other apps lets setup update them without rebooting.
    - Current: `為了更新相關的系統檔案可能必須重新啟動電腦。`
    - Source: `This wizard will guide you through the installation of { $BrandFullNameDA }.  It is recommended that you close all other applications before starting Setup. This will make it possible to update relevant system files wit…`
    - Suggest: `如此一來，更新相關系統檔案時就不必重新啟動電腦。`
    - The en-US gives the reason for closing other applications: it makes it possible to update system files without rebooting. The zh-TW drops that reason and says a reboot may be needed to update system files. That is the opposite of what the en-US says.
- `stub-blurb-first` — `browser/installer/nsisstrings.ftl` — "open web" is left in English as "Open Web", while the matching Developer Edition string translates it as 開放的網路環境.
    - Current: `準備好在 Open Web 中漫遊`
    - Source: `Get ready to roam on the open web`
    - Suggest: `準備好在開放的網路環境中漫遊`
    - "open web" is an ordinary phrase, not a brand. The same installer surface translates it in stub-blurb-first-devedition (開放的網路環境), so leaving it in English here is inconsistent.
- `nsis-dir-browse-text` — `browser/installer/override.ftl` — Sentence lacks the object 'folder', leaving 「選擇要將…安裝到：」 grammatically incomplete.
    - Current: `選擇要將 { $BrandFullNameDA } 安裝到：`
    - Source: `Select the folder to install { $BrandFullNameDA } in:`
    - Suggest: `選擇要將 { $BrandFullNameDA } 安裝到的資料夾：`
    - en-US 'Select the folder to install X in:' asks the user to select a folder; the translation reads 'Select to install X to:' with no object for 選擇.
- `nsis-dir-text` — `browser/installer/override.ftl` — Extra space after the full-width period before the placeable.
    - Current: `選擇其他資料夾。 { $ClickInstructions }`
    - Source: `Setup will install { $BrandFullNameDA } in the following folder. To install in a different folder, click Browse and select another folder. { $ClickInstructions }`
    - Suggest: `選擇其他資料夾。{ $ClickInstructions }`
    - Locale convention forbids spaces adjacent to full-width punctuation; sibling strings (e.g. nsis-license-text-rb) have no space here.

### ✅ Fixed since the last run (1)

- `Revert` — `toolkit/chrome/global/commonDialogs.properties` — The 'Revert' dialog button is translated as 'invert selection'
    - Current: `反向選擇(&R)`
    - Source: `&Revert`
    - Suggest: `還原(&R)`
    - 反向選擇 means 'invert selection', a different command from 'revert' (go back to the previous state).

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
| Files | 336 |
| Strings | 17,120 |
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
| quotes | `corner` 931, `straight-double` 25, `curly-single` 9, `curly-double` 6 | **corner** |
| apostrophe | `typographic` 9, `straight` 9 | _mixed_ |
| ellipsis | `char` 414 | **char** |
| dash | `em` 54, `en` 1 | **em** |
| nbsp | `total` 1, `space-before-punctuation` 5 | **space-before-punctuation** |
| fullwidth | `punctuation` 8778 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (39)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 10 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 10 |

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
- `KillAddonScriptMessage` — `dom/chrome/dom/dom.properties` — The second paragraph refers to the browser and a 'plugin' (外掛程式) instead of the extension script.
    - Current: `瀏覽器可能還在忙碌中，或是已經無法回應。您可以現在就中斷該指令碼，或是繼續等待外掛程式完成工作。`
    - Source: `A script from the extension “%1$S” is running on this page, and making %2$S unresponsive.  It may be busy, or it may have stopped responding permanently. You can stop the script now, or you can continue to see if it wil…`
    - Suggest: `該指令碼可能還在忙碌中，或是已經永久停止回應。您可以現在就中斷該指令碼，或是繼續等待它完成工作。`
    - In en-US, 'It may be busy … see if it will complete' refers to the extension's script. Plugins are a different and obsolete concept.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — The code literal 'events' was changed to 'event', and the sentence no longer says the default is a ping
    - Current: `否則預設的 <code>event</code> 指標是 <code>event</code>`
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
    - Suggest: `否則 <code>event</code> 指標的預設值為 <code>events</code> ping`
    - en-US: 'the default for event metrics is the events ping'. Text inside <code> must not be translated, and the ping is named 'events', not 'event'. The zh-TW also reads as 'the default event metric is event'. A developer following this would pick a ping that doesn't exist.
- `about-networking-ssl-tokens-summary-count` — `toolkit/toolkit/about/aboutNetworking.ftl` — `about-networking-ssl-tokens-summary-count` has plural variant ['one'], which zh-TW does not have
    - Current: `{$count ->} [one] { $count } 個 token [other] { $count } 個 token`
    - Source: `{$count ->} [one] { $count } token [other] { $count } tokens`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

### B. Mistranslation, reversed meaning, wrong names & brand

- `confirmation-hint-tab-group-button-removed` — `browser/browser/confirmationHints.ftl` — "Find" (locate) is rendered as 搜尋 (search), wrongly suggesting the menu lets you search tab groups.
    - Current: `可在此選單搜尋分頁群組`
    - Source: `Find tab groups in this menu`
    - Suggest: `可在此選單找到分頁群組`
    - Per the developer comment, this hint points to the app menu where tab groups can still be found after the toolbar button is removed. 'Find' means 'locate', not 'search'; 搜尋 implies a search function in the menu.
- `ipprotection-message-default-browser-confirmation` — `browser/browser/ipProtection.ftl` — The heading leaves out "more", so the additional locations read as the total number of locations.
    - Current: `您已獲得 { $additionalLocationsCount } 個 VPN 連線位置`
    - Source: `heading: {$additionalLocationsCount ->} [one] You’ve got { $additionalLocationsCount } more VPN location [other] You’ve got { $additionalLocationsCount } more VPN locations message: Thanks for making { -brand-short-name…`
    - Suggest: `您已額外獲得 { $additionalLocationsCount } 個 VPN 連線位置`
    - The en-US says "You've got N more VPN locations", and the developer comment describes the variable as the number of additional locations. The translation says the user has N locations, which gets the count wrong.
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
- `mui-text-welcome-info-text` — `browser/installer/mui.ftl` — The translation says updating system files may require a reboot, but the source says closing other apps lets setup update them without rebooting.
    - Current: `為了更新相關的系統檔案可能必須重新啟動電腦。`
    - Source: `This wizard will guide you through the installation of { $BrandFullNameDA }.  It is recommended that you close all other applications before starting Setup. This will make it possible to update relevant system files wit…`
    - Suggest: `如此一來，更新相關系統檔案時就不必重新啟動電腦。`
    - The en-US gives the reason for closing other applications: it makes it possible to update system files without rebooting. The zh-TW drops that reason and says a reboot may be needed to update system files. That is the opposite of what the en-US says.
- `download-ui-confirm-private-browsing-message` — `toolkit/toolkit/downloads/downloadUI.ftl` — The singular variant uses the plural 「這些檔案」 (these files) for a single download.
    - Current: `[1] 將無法繼續下載這些檔案。`
    - Source: `{$downloadsCount ->} [1] You won’t be able to resume this download. [other] You won’t be able to resume these downloads.`
    - Suggest: `[1] 將無法繼續下載此檔案。`
    - The en-US [1] variant says "this download", but the translation copies the plural wording 「這些」 (these), so it no longer matches the source.

### C. Grammar, agreement & spelling

- `restart-required-single-instance-question` — `browser/browser/aboutRestartRequired.ftl` — The product name is hard-coded as 'Firefox' where en-US uses no brand at all.
    - Current: `安裝多種 Firefox`
    - Source: `I don’t use multiple profiles or instances. Why is this happening?`
    - Suggest: `安裝多種 { -brand-short-name }`
    - en-US: 'I don't use multiple profiles or instances.' The locale adds a literal 'Firefox', which will show in Nightly, Developer Edition and other branded builds. The sibling question uses { -brand-short-name }.
- `tab-context-add-tab-to-group` — `browser/browser/tabbrowser.ftl` — The plural variant uses the possessive 的 where it needs the measure word 個, so it reads 'add the tabs of N to group'.
    - Current: `將 { $tabCount } 的分頁加入至群組`
    - Source: `accesskey: G label: {$tabCount ->} [1] Add to Group [other] Add { $tabCount } Tabs to Group`
    - Suggest: `將 { $tabCount } 個分頁加入至群組`
    - The en-US is 'Add N Tabs to Group'. A number in Chinese needs the classifier 個, as in the sibling string 移動 { $tabCount } 個分頁到. With 的 the phrase is ungrammatical.
- `nsis-dir-browse-text` — `browser/installer/override.ftl` — Sentence lacks the object 'folder', leaving 「選擇要將…安裝到：」 grammatically incomplete.
    - Current: `選擇要將 { $BrandFullNameDA } 安裝到：`
    - Source: `Select the folder to install { $BrandFullNameDA } in:`
    - Suggest: `選擇要將 { $BrandFullNameDA } 安裝到的資料夾：`
    - en-US 'Select the folder to install X in:' asks the user to select a folder; the translation reads 'Select to install X to:' with no object for 選擇.

### D. Terminology, register & consistency

- `about-logins-import-report-row-index` — `browser/browser/aboutLogins.ftl` — 'Row N' is rendered as 'N 行', which reads as 'N rows' rather than 'row number N'.
    - Current: `{ $number } 行`
    - Source: `Row { $number }`
    - Suggest: `第 { $number } 行`
    - This labels a single row index in the import report. Chinese needs the ordinal 第 here. Without it the text reads as a count.
- `smartwindow-onboarding-model-label` — `browser/browser/aiWindow.ftl` — Uses informal 你 instead of the polite 您 used throughout the surrounding onboarding strings.
    - Current: `挑選你的 AI 模型`
    - Source: `Pick your AI model`
    - Suggest: `挑選您的 AI 模型`
    - All sibling strings in the Smart Window onboarding flow (e.g. 依照您的喜好設定, 選擇…要如何了解您) address the user with 您; this label breaks the established form of address.
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — The phrase 關閉分頁起來 is ungrammatical.
    - Current: `若您還是想要關閉分頁起來`
    - Source: `If you still want to close tabs, choose <strong>Retry</strong> and make your selection in the card that opens.`
    - Suggest: `若您還是想要關閉分頁`
    - The complement 起來 does not combine with 關閉. It looks copied from the group-tabs sibling string (將分頁群組起來).
- `stub-blurb-first` — `browser/installer/nsisstrings.ftl` — "open web" is left in English as "Open Web", while the matching Developer Edition string translates it as 開放的網路環境.
    - Current: `準備好在 Open Web 中漫遊`
    - Source: `Get ready to roam on the open web`
    - Suggest: `準備好在開放的網路環境中漫遊`
    - "open web" is an ordinary phrase, not a brand. The same installer surface translates it in stub-blurb-first-devedition (開放的網路環境), so leaving it in English here is inconsistent.

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
- `ipprotection-unlimited-bandwidth-promo` — `browser/browser/ipProtection.ftl` — There is a space after the date placeholder, but the zh-TW date ends in a Chinese character.
    - Current: `{ $endDate } 前`
    - Source: `Unlimited bandwidth until { $endDate }`
    - Suggest: `{ $endDate }前`
    - $endDate is a month-day date, which renders as something like 1月31日 in zh-TW and ends in 日. The locale's convention is to space a placeholder by what it expands to, so no space should come before 前.
- `nsis-dir-text` — `browser/installer/override.ftl` — Extra space after the full-width period before the placeable.
    - Current: `選擇其他資料夾。 { $ClickInstructions }`
    - Source: `Setup will install { $BrandFullNameDA } in the following folder. To install in a different folder, click Browse and select another folder. { $ClickInstructions }`
    - Suggest: `選擇其他資料夾。{ $ClickInstructions }`
    - Locale convention forbids spaces adjacent to full-width punctuation; sibling strings (e.g. nsis-license-text-rb) have no space here.

---

## 4. Appendix

### Dismissed by hand (20)

- `PENeverMatchingHostSelector` — `dom/chrome/layout/css.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The suggestion left the English word 'featureless' untranslated in the Chinese text, which is a new error.
- `PostMessageSharedMemoryObjectToCrossOriginWarning` — `dom/chrome/dom/dom.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>post is an action verb, not postmessage.</p>
- `about-webauthn-auth-info-certifications` — `toolkit/toolkit/about/aboutWebauthn.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>learn = 了解 is more accurate for this string</p>
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>no difference from approved string?</p>
- `comboboxlist` — `dom/chrome/accessibility/AccessFu.properties` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `contentanalysis-error-message-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `credit-card-label-with-security-code-2` — `toolkit/toolkit/payments/payments.ftl` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; likely reason (inferred): The suggestion was exactly the same as the original and fixed nothing; the translation has no aria-label for the finding to apply to, so there was nothing new to accept.
- `customize-mode-toolbarspring` — `browser/browser/customizeMode.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `experimental-features-media-jxl` — `toolkit/toolkit/firefoxlabs/features.ftl` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `finduri-AgeInMonths-isgreater` — `toolkit/chrome/places/places.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The suggestion didn't fix the finding: 個月以前 still means '%S months ago', just like the original, so the 'older than' meaning is still missing.
- `menu-application-settings` — `browser/browser/menubar.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `permission-dialog-remember-file` — `toolkit/toolkit/global/handlerDialog.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `support-remote-settings-status-broken` — `toolkit/toolkit/about/aboutSupport.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `tab` — `dom/chrome/accessibility/mac/accessible.properties` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `underscript` — `dom/chrome/accessibility/AccessFu.properties` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>should keep Passkey intact, as per glossary.</p>

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (7)

- `STUB_BLURB_FIRST3` — `browser/installer/nsisstrings.properties` — auto-suggest (2026-11-09, string 56cf369f): unreliable finding: Keeping 'Open Web' as a concept term is a plausible stylistic choice, not a clear error.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — auto-suggest (2026-11-09, string ed64d941): unreliable finding: Dead [one] variant is harmless; the [other] output is correct, and removal requires changing select markup.
- `main-context-menu-use-mini-window` — `browser/browser/miniWindow.ftl` — auto-suggest (2026-11-09, string bb628b99): unreliable finding: 段落 is a plausible rendering of Section and the claimed 區域 usage in the overlay header cannot be verified here.
- `menu-share-copy-links` — `browser/browser/browser.ftl` — auto-suggest (2026-11-09, string 8bf28060): unreliable finding: The unused [one] variant is harmless; the [other] output is correct and removing it would require changing select markup.
- `urlbar-result-dates-countdown` — `browser/browser/browser.ftl` — auto-suggest (2026-11-09, string 95ae0c86): unreliable finding: Dead [one] variant is harmless; the [other] output is correct for all counts, and removal requires changing select markup.
- `urlbar-result-dates-countdown-range` — `browser/browser/browser.ftl` — auto-suggest (2026-11-09, string 71397184): unreliable finding: Dead [one] variant is harmless; the [other] output is correct for all counts, and removal requires changing select markup.
- `urlbar-result-dates-ongoing` — `browser/browser/browser.ftl` — auto-suggest (2026-11-09, string 2ed1f40d): unreliable finding: Dead [one] variant is harmless; the [other] output is correct for all counts, and removal requires changing select markup.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/zh-TW/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (197)

- `Revert` — `toolkit/chrome/global/commonDialogs.properties` — fixed 2026-11-23
- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — fixed 2026-11-16
- `decoder-doctor-no-codecs-linux-message` — `browser/browser/browser.ftl` — fixed 2026-11-16
- `identity-https-only-info-turn-on3` — `browser/browser/browser.ftl` — fixed 2026-11-16
- `customkeys-description` — `browser/browser/customkeys.ftl` — fixed 2026-11-16
- `ip-protection-not-opted-in-inclusions-enabled` — `browser/browser/ipProtection.ftl` — fixed 2026-11-16
- `connection-dns-over-https-url-item` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-16
- `inspector-emulation-panel-reduced-motion-no-preference` — `devtools/client/inspector.ftl` — fixed 2026-11-16
- `styleeditor-new-button` — `devtools/client/styleeditor.ftl` — fixed 2026-11-16
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-11-16
- `password-manager-update-password-button-delete` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — fixed 2026-11-16
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
