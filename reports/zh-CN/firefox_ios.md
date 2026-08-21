# Firefox iOS l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 1,835 of 1,835 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-CN: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (57)

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `zh-CN/firefox-ios.xliff` — The translation reverses the direction of the sync: the source says signing in fetches bookmarks from other devices, not that bookmarks become usable on other devices.
    - Current: `登录后还可在其他同步的设备上使用这些书签。`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `登录后即可获取其他同步设备上的书签。`
    - en-US: "Sign in to grab bookmarks from other synced devices" — bookmarks are pulled from other devices to this one; the parallel signed-in string is correctly translated as 从其他同步的设备上接收书签.
- `ContextualHints.FeltDeletion.Body.v122` — `zh-CN/firefox-ios.xliff` — The translation reverses the timing/meaning: the source says tapping deletes history and cookies now to start a fresh private session, not that data is deleted after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `点按此处开始全新的隐私浏览会话，删除您的历史记录、Cookie，一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The deletion happens on tap, not "after you finish browsing" (浏览完毕后), which misstates the fire button's behavior.
- `Addresses.EditAddress.AutofillAddressName.v129` — `zh-CN/firefox-ios.xliff` — "Name" in an address form refers to the person's full name, but the translation means "name/title" of a thing.
    - Current: `名称`
    - Source: `Name`
    - Suggest: `姓名`
    - The developer comment says the field is where the user inputs their full name; Chinese uses 姓名 for a person's name, while 名称 refers to the name of an object or organization.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `zh-CN/firefox-ios.xliff` — "Townland" (a rural land division) is rendered as 镇 (town), losing the specific meaning and colliding with other town-related fields.
    - Current: `镇`
    - Source: `Townland`
    - Suggest: `乡村地区（Townland）`
    - The comment explains a townland is a specific type of rural land division, not a town; 镇 means "town" and duplicates the Village or Township field.
- `Engagement.Notification.Treatment.B.Body.v114` — `zh-CN/firefox-ios.xliff` — Missing sentence-ending period present in the source.
    - Current: `%@ 将不会保存浏览期间的 Cookie 和历史记录`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `%@ 将不会保存浏览期间的 Cookie 和历史记录。`
    - The en-US body ends with a period; the Chinese sentence has no terminating punctuation, unlike the other notification body strings in the same file.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `zh-CN/firefox-ios.xliff` — "Reader View" is rendered as 阅读模式 (Reader Mode) instead of Firefox's standard 阅读视图.
    - Current: `关闭阅读模式`
    - Source: `Turn off Reader View`
    - Suggest: `关闭阅读视图`
    - en-US "Reader View" is consistently 阅读视图 in Firefox zh-CN; 阅读模式 corresponds to "Reader Mode".
- `MainMenu.ToolsSection.AccessibilityLabels.LibraryOptions.v142` — `zh-CN/firefox-ios.xliff` — "Library" is translated as 我的足迹 ("my footprints"), which does not mean Library.
    - Current: `我的足迹`
    - Source: `Library`
    - Suggest: `资料库`
    - The source term "Library" names the collection of Downloads, History, Passwords; Firefox zh-CN uses 资料库. 我的足迹 is a different, invented label.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `zh-CN/firefox-ios.xliff` — Inconsistent register: the polite 您 switches to 你们 within the same sentence.
    - Current: `若您使用的是企业网络，那么你们的支持团队可能了解更多信息。`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `若您使用的是企业网络，您的支持团队可能了解更多信息。`
    - The source uses "your" consistently; mixing 您 and 你们 in one sentence breaks the honorific register used throughout the file.
- `NativeErrorPage.GenericError.Description.v134` — `zh-CN/firefox-ios.xliff` — "owner" is rendered as 管理员 (administrator) instead of 所有者/拥有者.
    - Current: `%@ 的管理员未正确配置此网站`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `%@ 的所有者未正确配置此网站`
    - The en-US source says "The owner of %@", not the administrator.
- `DefaultBrowserPopup.ThirdLabel.v114` — `zh-CN/firefox-ios.xliff` — Missing space after the list number, inconsistent with the first and second labels.
    - Current: `3.选择 *%@*`
    - Source: `3. Select *%@*`
    - Suggest: `3. 选择 *%@*`
    - Sibling strings use "1. " and "2. " with a space after the numeral; this one omits it.
- `Onboarding.Customization.Theme.Dark.Action.v123` — `zh-CN/firefox-ios.xliff` — Theme name "Dark" translated as 深邃 instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - iOS/Firefox zh-CN uses 深色/浅色 for Dark/Light themes; 深邃 ("profound") is not the established term.
- `Onboarding.Customization.Theme.Light.Action.v123` — `zh-CN/firefox-ios.xliff` — Theme name "Light" translated as 明亮 instead of the standard 浅色.
    - Current: `明亮`
    - Source: `Light`
    - Suggest: `浅色`
    - iOS/Firefox zh-CN uses 浅色 for the Light theme, paired with 深色 for Dark.
- `Onboarding.Customization.Toolbar.Description.v123` — `zh-CN/firefox-ios.xliff` — "Keep searches within reach" is mistranslated as being about holding/gripping the phone.
    - Current: `轻松握持就可唤起搜索。`
    - Source: `Keep searches within reach.`
    - Suggest: `让搜索触手可及。`
    - The source means keeping search easily accessible (toolbar placement), not "easy gripping summons search"; 握持 (gripping) introduces meaning not in the source.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `zh-CN/firefox-ios.xliff` — "and that you use it" is mistranslated as "使用方式" (how you use it).
    - Current: `您发现 %1$@ 的途径及使用方式`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `您发现 %1$@ 的途径以及您正在使用它这一事实`
    - The source only shares the fact that you use the app, not how you use it; the translation overstates the data shared.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `zh-CN/firefox-ios.xliff` — "Browsing just got better" rendered with a spurious "纯粹".
    - Current: `纯粹带来更好的浏览体验。`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `浏览体验就此更上一层楼。`
    - The source has no notion of "purely/simply"; 纯粹 adds meaning not present in en-US.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `zh-CN/firefox-ios.xliff` — "companies" is rendered as "大公司" (big companies), adding a qualifier not in the source.
    - Current: `自动阻止大公司窥探您的浏览活动`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `自动阻止各公司窥探您的点击行为`
    - The en-US says "companies", not "big companies"; also "your clicks" is generalized to "浏览活动".
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `zh-CN/firefox-ios.xliff` — "bookmarks, history" is translated as "书签、历史记录" but "history" list item order/content drops nothing—actually "your top sites" fine; issue is "history" omitted? No—see rationale.
    - Current: `键入即可获取搜索建议、常用网站、书签、历史记录、搜索引擎，尽在一处。`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `键入即可获取搜索建议、常用网站、书签、历史记录和搜索引擎，尽在一处。`
    - Enumeration in Chinese should join the final item with 和/以及 rather than another 顿号; minor grammar issue.
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148.v2` — `zh-CN/firefox-ios.xliff` — Translation adds "的浏览器" (browser), which is not in the source.
    - Current: `通过内置隐私保护的浏览器打开链接`
    - Source: `Open your links with built-in privacy`
    - Suggest: `打开链接，即享内置隐私保护`
    - The en-US "Open your links with built-in privacy" does not mention a browser; the added noun changes the statement.
- `PrimaryButton.Label.v112` — `zh-CN/firefox-ios.xliff` — "Take Survey" (an action button) is rendered as the noun phrase "问卷调查" instead of a call to action.
    - Current: `问卷调查`
    - Source: `Take Survey`
    - Suggest: `参与调查`
    - The source is a button that takes the user to a survey; the translation is just the noun "survey/questionnaire", losing the imperative action meaning.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatus.v151` — `zh-CN/firefox-ios.xliff` — "Available" as a feature status is rendered as the verb "提供" instead of the adjective "可用".
    - Current: `提供`
    - Source: `Available`
    - Suggest: `可用`
    - The source is a status label meaning the feature is turned on/usable; the companion description string already uses "**可用**", so "提供" is both wrong in part of speech and inconsistent on the same screen.
- `Settings.Notifications.TipsAndFeaturesNotificationsTitle.v112` — `zh-CN/firefox-ios.xliff` — "Tips and Features" is translated as only "使用技巧", dropping "Features".
    - Current: `使用技巧`
    - Source: `Tips and Features`
    - Suggest: `使用技巧与功能`
    - The source lists two items, tips and features; the target omits "Features", which the accompanying description string also references.
- `Settings.Notifications.TurnOnNotificationsMessage.v112` — `zh-CN/firefox-ios.xliff` — Translation says go to the device setting item named %@ instead of going to device Settings to turn on notifications for %@.
    - Current: `前往设备设置中的“%@”开启通知`
    - Source: `Go to your device Settings to turn on notifications in %@`
    - Suggest: `前往设备的“设置”，开启 %@ 的通知`
    - In en-US %@ is the app name and the user should open the device Settings to enable notifications for the app; the Chinese reads as if %@ were a section of device settings.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `zh-CN/firefox-ios.xliff` — "suggestions" is rendered as "结果" (results) instead of "建议".
    - Current: `在隐私浏览中显示来自 Firefox 建议的结果`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `在隐私浏览中显示来自 Firefox 建议的建议`
    - The source says "Show suggestions from Firefox Suggest in private sessions"; the translation says "results" rather than "suggestions", inconsistent with the parallel string Settings.Search.PrivateSession.Description.v125 which uses 建议.
- `Settings.Translation.AutoTranslate.Footer.v151` — `zh-CN/firefox-ios.xliff` — "top preferred language" is rendered as "最熟悉的语言" (most familiar language) instead of the top item in the preferred-languages list.
    - Current: `自动将页面翻译成您最熟悉的语言。`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `自动将页面翻译成您的首选语言（列表中的第一种语言）。`
    - The source refers to the user's top-ranked preferred language configured in the Preferred Languages list (translated elsewhere as 首选语言), not to which language the user knows best.
- `Settings.Translation.PreferredLanguages.Footer.v151` — `zh-CN/firefox-ios.xliff` — The footer reverses the agent: the app chooses from these languages when translating, but the translation implies a passive/unspecified selection process.
    - Current: `翻译时将从这些语言中选择。`
    - Source: `Choose from these languages when translating.`
    - Suggest: `翻译时可从这些语言中选择。`
    - "Choose from these languages when translating" instructs the user that these languages will be available as choices; "将从这些语言中选择" states the system will pick one automatically.
- `SendTo.NoDevicesFound.Message.v119` — `zh-CN/firefox-ios.xliff` — The translation drops "connected to this account" nuance and says devices are not in the account rather than no other devices are connected.
    - Current: `您的账户中没有其他设备可供同步。`
    - Source: `You don’t have any other devices connected to this account available to sync.`
    - Suggest: `您没有其他连接到此账户的设备可供同步。`
    - en-US: "You don’t have any other devices connected to this account available to sync."
- `TabsButton.Accessibility.LargeContentTitle.v122` — `zh-CN/firefox-ios.xliff` — "Show Tabs: %@" is rendered as "显示的标签页" (the tabs that are shown) instead of the imperative action "显示标签页".
    - Current: `显示的标签页：%@`
    - Source: `Show Tabs: %@`
    - Suggest: `显示标签页：%@`
    - The source is a button action title "Show Tabs"; adding 的 turns it into a noun phrase meaning "the displayed tabs", changing the meaning.
- `TabTrayCloseTabsOlderThanTitle.v140` — `zh-CN/firefox-ios.xliff` — The ellipsis at the end of "Close tabs older than…" is dropped in the translation.
    - Current: `关闭早于特定时间的标签页`
    - Source: `Close tabs older than…`
    - Suggest: `关闭早于以下时间的标签页…`
    - The source ends with an ellipsis indicating a submenu/further choice; the translation omits it, unlike the sibling string TabTrayCloseOldTabsTitle which keeps it.
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `zh-CN/firefox-ios.xliff` — "放大缩放比例" is an incorrect collocation and inconsistent with the paired "减小缩放比例".
    - Current: `放大缩放比例`
    - Source: `Increase Zoom Level`
    - Suggest: `增大缩放比例`
    - The source pair is Increase/Decrease Zoom Level; the decrease string uses 减小缩放比例, so the increase string should use 增大缩放比例. 放大…比例 is not a valid verb-object pairing.
- `ContextualHints.TabTray.InactiveTabs` — `zh-CN/firefox-ios.xliff` — Translation reverses the meaning: source says tabs not viewed for two weeks, target says tabs not viewed within two weeks (which reads as under two weeks).
    - Current: `两周内未查看的标签页将移至此处。`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `超过两周未查看的标签页将移至此处。`
    - en-US "Tabs you haven’t viewed for two weeks" means tabs untouched for two weeks or longer; "两周内未查看" states the opposite timeframe.
- `CoverSheet.v24.ETP.Description` — `zh-CN/firefox-ios.xliff` — The item "ads" is dropped from the list of blocked content.
    - Current: `则可拦截更多跟踪器和弹窗`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `则可拦截更多跟踪器、广告和弹窗`
    - Source lists "trackers, ads, and popups"; the translation omits "ads".
- `Closing tab` — `zh-CN/firefox-ios.xliff` — Progressive "Closing tab" rendered as the imperative/label "关闭标签页".
    - Current: `关闭标签页`
    - Source: `Closing tab`
    - Suggest: `正在关闭标签页`
    - The developer comment says this notifies the user that the tab is being closed; the Chinese lacks the in-progress aspect and reads as the action label "Close tab".
- `Dark` — `zh-CN/firefox-ios.xliff` — Reading View dark theme setting is rendered as "深邃" instead of the standard "深色".
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - "Dark" as a theme setting is consistently "深色" in Firefox zh-CN; "深邃" means "profound/deep" and is not a theme name.
- `Downloads.CancelDialog.Resume` — `zh-CN/firefox-ios.xliff` — "Resume" is translated as "继续" which loses the resume-download meaning in this cancel dialog.
    - Current: `继续`
    - Source: `Resume`
    - Suggest: `继续下载`
    - The button declines cancellation and resumes the download; "继续" alone is ambiguous next to "取消", the source is "Resume".
- `FirefoxHome.Stories.Minutes.v140` — `zh-CN/firefox-ios.xliff` — The abbreviation required by the developer comment is not used; "分钟" is the full form and the source's "min:" label pattern is dropped.
    - Current: `%d 分钟`
    - Source: `min: %d`
    - Suggest: `%d 分钟阅读`
    - Developer comment states minutes should be abbreviated due to space constraints; the source is "min: %d". Chinese has no shorter form, but the label meaning "minutes to read" is lost — at minimum the reading context should be preserved compactly.
- `FirefoxHomepage.ContextualMenu.SponsoredContent.v101` — `zh-CN/firefox-ios.xliff` — Full-width ampersand "＆" used instead of the conventional Chinese connector.
    - Current: `我们的赞助商＆您的隐私`
    - Source: `Our Sponsors & Your Privacy`
    - Suggest: `我们的赞助商与您的隐私`
    - zh-CN typography does not use a full-width ampersand as a conjunction; compare FxA.ManageAccount which renders "&" as "和".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `zh-CN/firefox-ios.xliff` — "Tab pickup" is rendered as "接收标签页" (receive tabs), which misses the feature name meaning of resuming a tab from another device.
    - Current: `接收标签页`
    - Source: `Tab pickup`
    - Suggest: `标签页接力`
    - "Tab pickup" is the feature that lets you pick up a synced tab from another device; "接收标签页" reads as an action of receiving tabs rather than the section label.
- `Menu.RemovedFromShortcuts.v99` — `zh-CN/firefox-ios.xliff` — "Remove from Shortcuts" is translated as "移除快捷方式" (remove the shortcut) rather than removing the site from the Shortcuts list.
    - Current: `移除快捷方式`
    - Source: `Remove from Shortcuts`
    - Suggest: `从快捷方式中移除`
    - The source means removing the current website from the Shortcuts section on the home page; the related toast Menu.RemovePin.Confirm2.v99 correctly uses "已从快捷方式移除". "移除快捷方式" reads as deleting a shortcut object and is inconsistent.
- `OpenURL.Error.Message` — `zh-CN/firefox-ios.xliff` — Missing space between the Chinese text and the Latin brand name "Firefox".
    - Current: `地址无效，因此Firefox 无法打开该页面。`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `地址无效，因此 Firefox 无法打开该页面。`
    - zh-CN convention (and the rest of this file, e.g. "啊哦！Firefox 崩溃了") inserts a space between CJK characters and Latin words; here "因此Firefox" lacks it while the following space is present.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `zh-CN/firefox-ios.xliff` — "Fingerprinters" is rendered as 数字指纹跟踪程序 here but 数字指纹追踪程序 in the description string on the same feature screen.
    - Current: `数字指纹跟踪程序`
    - Source: `Fingerprinters`
    - Suggest: `数字指纹追踪程序`
    - Menu.TrackingProtectionDescription.Fingerprinters uses 数字指纹追踪程序 for the same source term; the two should match within the same tracking-protection screen.
- `SentTab_TabArrivingNotification_WithDevice_title` — `zh-CN/firefox-ios.xliff` — Translation reverses the direction: source says the tab was received from the named device, but the Chinese says the device received the tab.
    - Current: `%@ 收到新的标签页`
    - Source: `Tab received from %@`
    - Suggest: `收到来自 %@ 的标签页`
    - en-US "Tab received from %@" where %@ is the sending device name; the target makes %@ the receiver.
- `SentTab_TabArrivingNotification_WithDevice_body` — `zh-CN/firefox-ios.xliff` — Body string mis-renders "arrived in %@" (the app name) as the app receiving nothing meaningful/ambiguous direction.
    - Current: `%@ 收到了新的标签页`
    - Source: `New tab arrived in %@`
    - Suggest: `新标签页已送达 %@`
    - The comment says %@ is the app name; "New tab arrived in %@" means the tab arrived in the app, not that the app name device received it — combined with the title string the direction is confusing/wrong.
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `zh-CN/firefox-ios.xliff` — "Sponsored Shortcuts" is rendered as "赞助商网站" (sponsored websites) instead of sponsored shortcuts.
    - Current: `赞助商网站`
    - Source: `Sponsored Shortcuts`
    - Suggest: `赞助商快捷方式`
    - The source term is "Shortcuts", translated elsewhere in the same screen as "快捷方式"; "网站" (websites) is a different term and breaks consistency with the other shortcuts strings.
- `Settings.OfferClipboardBar.Status.v128` — `zh-CN/firefox-ios.xliff` — Translation adds "询问" (ask/offer), which is not in the source "When opening %@".
    - Current: `打开 %@ 时询问`
    - Source: `When opening %@`
    - Suggest: `打开 %@ 时`
    - The source is only "When opening %@", matching the earlier variant "当打开 Firefox 时"; adding "询问" introduces content not present in the source.
- `Settings.Passwords.OnboardingMessage.v103` — `zh-CN/firefox-ios.xliff` — Missing space between "触控 ID" and "或" pattern — actually missing space in "触控 ID或设备密码".
    - Current: `触控 ID或设备密码`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `触控 ID 或设备密码`
    - Latin text "ID" must be separated from the following Chinese character with a space, as done elsewhere in the same string ("面容 ID、").
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `zh-CN/firefox-ios.xliff` — The translation drops "ads" from the list of blocked items.
    - Current: `拦截更多跟踪器和弹窗。`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `拦截更多跟踪器、广告和弹窗。`
    - The source says "Blocks more trackers, ads, and popups." — "ads" (广告) is missing in the Chinese text.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `zh-CN/firefox-ios.xliff` — The translation reverses the time condition: source says tabs not viewed FOR two weeks, translation says tabs not viewed WITHIN two weeks.
    - Current: `两周内未查看的标签页将进入休眠状态。`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `超过两周未查看的标签页将移至休眠标签页区域。`
    - "Tabs you haven’t viewed for two weeks" means tabs untouched for at least two weeks; 两周内未查看 literally reads as "not viewed within two weeks" which is ambiguous/reversed, and the mention of moving to the inactive section is lost.
- `TranslationToastHandler.PromptTranslate.Title` — `zh-CN/firefox-ios.xliff` — "This page appears to be in %1$@" is mistranslated as "此页面以 %1$@ 显示" (this page is displayed in %1$@), losing the "appears to be" hedge and the language sense.
    - Current: `此页面以 %1$@ 显示`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `此页面似乎使用 %1$@ 撰写`
    - The source says the page appears to be in a given language; the translation states it is displayed in it, dropping the uncertainty.
- `You don’t have any tabs open in Firefox on your other devices.` — `zh-CN/firefox-ios.xliff` — Awkward/ungrammatical rendering with redundant 已经 makes the sentence read incorrectly.
    - Current: `您没有在其他设备的 Firefox 上已经打开的标签页。`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `您的其他设备上的 Firefox 没有打开任何标签页。`
    - The source states no tabs are open in Firefox on the user's other devices; the Chinese word order with 已经 is ungrammatical.
- `Use stage servers` — `zh-CN/firefox-ios.xliff` — Half-width parentheses used without spacing around Latin text in Chinese sentence.
    - Current: `使用预发布(Stage)服务器`
    - Source: `Use stage servers`
    - Suggest: `使用预发布（Stage）服务器`
    - zh-CN typography requires full-width parentheses within Chinese text.
- `TopSites.RemovePage.Button` — `zh-CN/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `移除页面 - %@`
    - Source: `Remove page — %@`
    - Suggest: `移除页面 — %@`
    - Source uses an em dash separator; the translation uses a plain hyphen.
- `Menu.SharePageAction.Title` — `zh-CN/firefox-ios.xliff` — "Share Page With…" is rendered without the "With" sense; it should indicate sharing with someone/an app.
    - Current: `分享页面…`
    - Source: `Share Page With…`
    - Suggest: `分享页面给…`
    - The en-US source is "Share Page With…", indicating sharing with a recipient/app; the translation drops "With".
- `Menu.ViewDekstopSiteAction.Title` — `zh-CN/firefox-ios.xliff` — "Request Desktop Site" is translated as 要求 while the parallel mobile string uses 请求, an inconsistency on the same menu.
    - Current: `要求桌面版网站`
    - Source: `Request Desktop Site`
    - Suggest: `请求桌面版网站`
    - Menu.ViewMobileSiteAction.Title renders the identical source verb "Request" as 请求; the same term should be consistent within the same menu.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `zh-CN/firefox-ios.xliff` — "any of your history or cookies" is translated as 历史记录和 Cookie, weakening the negation coverage.
    - Current: `不会记住您的历史记录和 Cookie`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `不会记住您的任何历史记录或 Cookie`
    - The source negates both items individually ("any … or …"); 和 in Chinese negation can be read as excluding only the combination.
- `When Leaving Private Browsing` — `zh-CN/firefox-ios.xliff` — Translation adds "关闭" (close), which is not in the source label.
    - Current: `离开隐私浏览时关闭`
    - Source: `When Leaving Private Browsing`
    - Suggest: `离开隐私浏览时`
    - The source is only "When Leaving Private Browsing"; it is an option value under the 'Close Private Tabs' setting, so appending 关闭 duplicates the setting title and changes the string's content.
- `TodayWidget.TopSitesGalleryDescription` — `zh-CN/firefox-ios.xliff` — Translation drops "recently visited" and turns the description into a quoted widget name.
    - Current: `添加“常用网站”快捷方式。`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `为常用及最近访问的网站添加快捷方式。`
    - en-US says "Add shortcuts to frequently and recently visited sites." — the "recently visited" part is missing.
- `TodayWidget.MoreTabsLabel` — `zh-CN/firefox-ios.xliff` — Redundant wording "还有另" in the more-tabs label.
    - Current: `+还有另 %d 个…`
    - Source: `+%d More…`
    - Suggest: `+另有 %d 个…`
    - "还有" and "另" duplicate the same meaning; source is simply "+%d More…".

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
| Files | 93 |
| Strings | 1,835 |
| Missing strings | 75 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**75 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — 49
- `zh-CN/firefox-ios.xliff` — 11
- `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — 7
- `zh-CN/firefox-ios.xliff` — 3
- `zh-CN/firefox-ios.xliff` — 2
- `zh-CN/firefox-ios.xliff` — 2
- `zh-CN/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings`
- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 40 | **curly-double** |
| ellipsis | `char` 15 | **char** |
| fullwidth | `punctuation` 545 | **punctuation** |
| register | `informal` 1, `formal` 133 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (57)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 36 |
| 3 | Degraded language (grammar, spelling, terminology) | 12 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `zh-CN/firefox-ios.xliff` — The translation reverses the direction of the sync: the source says signing in fetches bookmarks from other devices, not that bookmarks become usable on other devices.
    - Current: `登录后还可在其他同步的设备上使用这些书签。`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `登录后即可获取其他同步设备上的书签。`
    - en-US: "Sign in to grab bookmarks from other synced devices" — bookmarks are pulled from other devices to this one; the parallel signed-in string is correctly translated as 从其他同步的设备上接收书签.
- `ContextualHints.FeltDeletion.Body.v122` — `zh-CN/firefox-ios.xliff` — The translation reverses the timing/meaning: the source says tapping deletes history and cookies now to start a fresh private session, not that data is deleted after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `点按此处开始全新的隐私浏览会话，删除您的历史记录、Cookie，一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The deletion happens on tap, not "after you finish browsing" (浏览完毕后), which misstates the fire button's behavior.
- `Addresses.EditAddress.AutofillAddressName.v129` — `zh-CN/firefox-ios.xliff` — "Name" in an address form refers to the person's full name, but the translation means "name/title" of a thing.
    - Current: `名称`
    - Source: `Name`
    - Suggest: `姓名`
    - The developer comment says the field is where the user inputs their full name; Chinese uses 姓名 for a person's name, while 名称 refers to the name of an object or organization.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `zh-CN/firefox-ios.xliff` — "Townland" (a rural land division) is rendered as 镇 (town), losing the specific meaning and colliding with other town-related fields.
    - Current: `镇`
    - Source: `Townland`
    - Suggest: `乡村地区（Townland）`
    - The comment explains a townland is a specific type of rural land division, not a town; 镇 means "town" and duplicates the Village or Township field.
- `MainMenu.ToolsSection.AccessibilityLabels.LibraryOptions.v142` — `zh-CN/firefox-ios.xliff` — "Library" is translated as 我的足迹 ("my footprints"), which does not mean Library.
    - Current: `我的足迹`
    - Source: `Library`
    - Suggest: `资料库`
    - The source term "Library" names the collection of Downloads, History, Passwords; Firefox zh-CN uses 资料库. 我的足迹 is a different, invented label.
- `NativeErrorPage.GenericError.Description.v134` — `zh-CN/firefox-ios.xliff` — "owner" is rendered as 管理员 (administrator) instead of 所有者/拥有者.
    - Current: `%@ 的管理员未正确配置此网站`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `%@ 的所有者未正确配置此网站`
    - The en-US source says "The owner of %@", not the administrator.
- `Onboarding.Customization.Toolbar.Description.v123` — `zh-CN/firefox-ios.xliff` — "Keep searches within reach" is mistranslated as being about holding/gripping the phone.
    - Current: `轻松握持就可唤起搜索。`
    - Source: `Keep searches within reach.`
    - Suggest: `让搜索触手可及。`
    - The source means keeping search easily accessible (toolbar placement), not "easy gripping summons search"; 握持 (gripping) introduces meaning not in the source.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `zh-CN/firefox-ios.xliff` — "and that you use it" is mistranslated as "使用方式" (how you use it).
    - Current: `您发现 %1$@ 的途径及使用方式`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `您发现 %1$@ 的途径以及您正在使用它这一事实`
    - The source only shares the fact that you use the app, not how you use it; the translation overstates the data shared.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `zh-CN/firefox-ios.xliff` — "Browsing just got better" rendered with a spurious "纯粹".
    - Current: `纯粹带来更好的浏览体验。`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `浏览体验就此更上一层楼。`
    - The source has no notion of "purely/simply"; 纯粹 adds meaning not present in en-US.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `zh-CN/firefox-ios.xliff` — "companies" is rendered as "大公司" (big companies), adding a qualifier not in the source.
    - Current: `自动阻止大公司窥探您的浏览活动`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `自动阻止各公司窥探您的点击行为`
    - The en-US says "companies", not "big companies"; also "your clicks" is generalized to "浏览活动".
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148.v2` — `zh-CN/firefox-ios.xliff` — Translation adds "的浏览器" (browser), which is not in the source.
    - Current: `通过内置隐私保护的浏览器打开链接`
    - Source: `Open your links with built-in privacy`
    - Suggest: `打开链接，即享内置隐私保护`
    - The en-US "Open your links with built-in privacy" does not mention a browser; the added noun changes the statement.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `zh-CN/firefox-ios.xliff` — "bookmarks, history" is translated as "书签、历史记录" but "history" list item order/content drops nothing—actually "your top sites" fine; issue is "history" omitted? No—see rationale.
    - Current: `键入即可获取搜索建议、常用网站、书签、历史记录、搜索引擎，尽在一处。`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `键入即可获取搜索建议、常用网站、书签、历史记录和搜索引擎，尽在一处。`
    - Enumeration in Chinese should join the final item with 和/以及 rather than another 顿号; minor grammar issue.
- `PrimaryButton.Label.v112` — `zh-CN/firefox-ios.xliff` — "Take Survey" (an action button) is rendered as the noun phrase "问卷调查" instead of a call to action.
    - Current: `问卷调查`
    - Source: `Take Survey`
    - Suggest: `参与调查`
    - The source is a button that takes the user to a survey; the translation is just the noun "survey/questionnaire", losing the imperative action meaning.
- `Settings.Notifications.TipsAndFeaturesNotificationsTitle.v112` — `zh-CN/firefox-ios.xliff` — "Tips and Features" is translated as only "使用技巧", dropping "Features".
    - Current: `使用技巧`
    - Source: `Tips and Features`
    - Suggest: `使用技巧与功能`
    - The source lists two items, tips and features; the target omits "Features", which the accompanying description string also references.
- `Settings.Notifications.TurnOnNotificationsMessage.v112` — `zh-CN/firefox-ios.xliff` — Translation says go to the device setting item named %@ instead of going to device Settings to turn on notifications for %@.
    - Current: `前往设备设置中的“%@”开启通知`
    - Source: `Go to your device Settings to turn on notifications in %@`
    - Suggest: `前往设备的“设置”，开启 %@ 的通知`
    - In en-US %@ is the app name and the user should open the device Settings to enable notifications for the app; the Chinese reads as if %@ were a section of device settings.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `zh-CN/firefox-ios.xliff` — "suggestions" is rendered as "结果" (results) instead of "建议".
    - Current: `在隐私浏览中显示来自 Firefox 建议的结果`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `在隐私浏览中显示来自 Firefox 建议的建议`
    - The source says "Show suggestions from Firefox Suggest in private sessions"; the translation says "results" rather than "suggestions", inconsistent with the parallel string Settings.Search.PrivateSession.Description.v125 which uses 建议.
- `Settings.Translation.AutoTranslate.Footer.v151` — `zh-CN/firefox-ios.xliff` — "top preferred language" is rendered as "最熟悉的语言" (most familiar language) instead of the top item in the preferred-languages list.
    - Current: `自动将页面翻译成您最熟悉的语言。`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `自动将页面翻译成您的首选语言（列表中的第一种语言）。`
    - The source refers to the user's top-ranked preferred language configured in the Preferred Languages list (translated elsewhere as 首选语言), not to which language the user knows best.
- `Settings.Translation.PreferredLanguages.Footer.v151` — `zh-CN/firefox-ios.xliff` — The footer reverses the agent: the app chooses from these languages when translating, but the translation implies a passive/unspecified selection process.
    - Current: `翻译时将从这些语言中选择。`
    - Source: `Choose from these languages when translating.`
    - Suggest: `翻译时可从这些语言中选择。`
    - "Choose from these languages when translating" instructs the user that these languages will be available as choices; "将从这些语言中选择" states the system will pick one automatically.
- `SendTo.NoDevicesFound.Message.v119` — `zh-CN/firefox-ios.xliff` — The translation drops "connected to this account" nuance and says devices are not in the account rather than no other devices are connected.
    - Current: `您的账户中没有其他设备可供同步。`
    - Source: `You don’t have any other devices connected to this account available to sync.`
    - Suggest: `您没有其他连接到此账户的设备可供同步。`
    - en-US: "You don’t have any other devices connected to this account available to sync."
- `TabsButton.Accessibility.LargeContentTitle.v122` — `zh-CN/firefox-ios.xliff` — "Show Tabs: %@" is rendered as "显示的标签页" (the tabs that are shown) instead of the imperative action "显示标签页".
    - Current: `显示的标签页：%@`
    - Source: `Show Tabs: %@`
    - Suggest: `显示标签页：%@`
    - The source is a button action title "Show Tabs"; adding 的 turns it into a noun phrase meaning "the displayed tabs", changing the meaning.
- `Closing tab` — `zh-CN/firefox-ios.xliff` — Progressive "Closing tab" rendered as the imperative/label "关闭标签页".
    - Current: `关闭标签页`
    - Source: `Closing tab`
    - Suggest: `正在关闭标签页`
    - The developer comment says this notifies the user that the tab is being closed; the Chinese lacks the in-progress aspect and reads as the action label "Close tab".
- `ContextualHints.TabTray.InactiveTabs` — `zh-CN/firefox-ios.xliff` — Translation reverses the meaning: source says tabs not viewed for two weeks, target says tabs not viewed within two weeks (which reads as under two weeks).
    - Current: `两周内未查看的标签页将移至此处。`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `超过两周未查看的标签页将移至此处。`
    - en-US "Tabs you haven’t viewed for two weeks" means tabs untouched for two weeks or longer; "两周内未查看" states the opposite timeframe.
- `CoverSheet.v24.ETP.Description` — `zh-CN/firefox-ios.xliff` — The item "ads" is dropped from the list of blocked content.
    - Current: `则可拦截更多跟踪器和弹窗`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `则可拦截更多跟踪器、广告和弹窗`
    - Source lists "trackers, ads, and popups"; the translation omits "ads".
- `Downloads.CancelDialog.Resume` — `zh-CN/firefox-ios.xliff` — "Resume" is translated as "继续" which loses the resume-download meaning in this cancel dialog.
    - Current: `继续`
    - Source: `Resume`
    - Suggest: `继续下载`
    - The button declines cancellation and resumes the download; "继续" alone is ambiguous next to "取消", the source is "Resume".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `zh-CN/firefox-ios.xliff` — "Tab pickup" is rendered as "接收标签页" (receive tabs), which misses the feature name meaning of resuming a tab from another device.
    - Current: `接收标签页`
    - Source: `Tab pickup`
    - Suggest: `标签页接力`
    - "Tab pickup" is the feature that lets you pick up a synced tab from another device; "接收标签页" reads as an action of receiving tabs rather than the section label.
- `Menu.RemovedFromShortcuts.v99` — `zh-CN/firefox-ios.xliff` — "Remove from Shortcuts" is translated as "移除快捷方式" (remove the shortcut) rather than removing the site from the Shortcuts list.
    - Current: `移除快捷方式`
    - Source: `Remove from Shortcuts`
    - Suggest: `从快捷方式中移除`
    - The source means removing the current website from the Shortcuts section on the home page; the related toast Menu.RemovePin.Confirm2.v99 correctly uses "已从快捷方式移除". "移除快捷方式" reads as deleting a shortcut object and is inconsistent.
- `SentTab_TabArrivingNotification_WithDevice_body` — `zh-CN/firefox-ios.xliff` — Body string mis-renders "arrived in %@" (the app name) as the app receiving nothing meaningful/ambiguous direction.
    - Current: `%@ 收到了新的标签页`
    - Source: `New tab arrived in %@`
    - Suggest: `新标签页已送达 %@`
    - The comment says %@ is the app name; "New tab arrived in %@" means the tab arrived in the app, not that the app name device received it — combined with the title string the direction is confusing/wrong.
- `SentTab_TabArrivingNotification_WithDevice_title` — `zh-CN/firefox-ios.xliff` — Translation reverses the direction: source says the tab was received from the named device, but the Chinese says the device received the tab.
    - Current: `%@ 收到新的标签页`
    - Source: `Tab received from %@`
    - Suggest: `收到来自 %@ 的标签页`
    - en-US "Tab received from %@" where %@ is the sending device name; the target makes %@ the receiver.
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `zh-CN/firefox-ios.xliff` — "Sponsored Shortcuts" is rendered as "赞助商网站" (sponsored websites) instead of sponsored shortcuts.
    - Current: `赞助商网站`
    - Source: `Sponsored Shortcuts`
    - Suggest: `赞助商快捷方式`
    - The source term is "Shortcuts", translated elsewhere in the same screen as "快捷方式"; "网站" (websites) is a different term and breaks consistency with the other shortcuts strings.
- `Settings.OfferClipboardBar.Status.v128` — `zh-CN/firefox-ios.xliff` — Translation adds "询问" (ask/offer), which is not in the source "When opening %@".
    - Current: `打开 %@ 时询问`
    - Source: `When opening %@`
    - Suggest: `打开 %@ 时`
    - The source is only "When opening %@", matching the earlier variant "当打开 Firefox 时"; adding "询问" introduces content not present in the source.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `zh-CN/firefox-ios.xliff` — The translation reverses the time condition: source says tabs not viewed FOR two weeks, translation says tabs not viewed WITHIN two weeks.
    - Current: `两周内未查看的标签页将进入休眠状态。`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `超过两周未查看的标签页将移至休眠标签页区域。`
    - "Tabs you haven’t viewed for two weeks" means tabs untouched for at least two weeks; 两周内未查看 literally reads as "not viewed within two weeks" which is ambiguous/reversed, and the mention of moving to the inactive section is lost.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `zh-CN/firefox-ios.xliff` — The translation drops "ads" from the list of blocked items.
    - Current: `拦截更多跟踪器和弹窗。`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `拦截更多跟踪器、广告和弹窗。`
    - The source says "Blocks more trackers, ads, and popups." — "ads" (广告) is missing in the Chinese text.
- `TranslationToastHandler.PromptTranslate.Title` — `zh-CN/firefox-ios.xliff` — "This page appears to be in %1$@" is mistranslated as "此页面以 %1$@ 显示" (this page is displayed in %1$@), losing the "appears to be" hedge and the language sense.
    - Current: `此页面以 %1$@ 显示`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `此页面似乎使用 %1$@ 撰写`
    - The source says the page appears to be in a given language; the translation states it is displayed in it, dropping the uncertainty.
- `Menu.SharePageAction.Title` — `zh-CN/firefox-ios.xliff` — "Share Page With…" is rendered without the "With" sense; it should indicate sharing with someone/an app.
    - Current: `分享页面…`
    - Source: `Share Page With…`
    - Suggest: `分享页面给…`
    - The en-US source is "Share Page With…", indicating sharing with a recipient/app; the translation drops "With".
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `zh-CN/firefox-ios.xliff` — "any of your history or cookies" is translated as 历史记录和 Cookie, weakening the negation coverage.
    - Current: `不会记住您的历史记录和 Cookie`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `不会记住您的任何历史记录或 Cookie`
    - The source negates both items individually ("any … or …"); 和 in Chinese negation can be read as excluding only the combination.
- `When Leaving Private Browsing` — `zh-CN/firefox-ios.xliff` — Translation adds "关闭" (close), which is not in the source label.
    - Current: `离开隐私浏览时关闭`
    - Source: `When Leaving Private Browsing`
    - Suggest: `离开隐私浏览时`
    - The source is only "When Leaving Private Browsing"; it is an option value under the 'Close Private Tabs' setting, so appending 关闭 duplicates the setting title and changes the string's content.
- `TodayWidget.TopSitesGalleryDescription` — `zh-CN/firefox-ios.xliff` — Translation drops "recently visited" and turns the description into a quoted widget name.
    - Current: `添加“常用网站”快捷方式。`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `为常用及最近访问的网站添加快捷方式。`
    - en-US says "Add shortcuts to frequently and recently visited sites." — the "recently visited" part is missing.

### C. Grammar, agreement & spelling

- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `zh-CN/firefox-ios.xliff` — Inconsistent register: the polite 您 switches to 你们 within the same sentence.
    - Current: `若您使用的是企业网络，那么你们的支持团队可能了解更多信息。`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `若您使用的是企业网络，您的支持团队可能了解更多信息。`
    - The source uses "your" consistently; mixing 您 and 你们 in one sentence breaks the honorific register used throughout the file.
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `zh-CN/firefox-ios.xliff` — "放大缩放比例" is an incorrect collocation and inconsistent with the paired "减小缩放比例".
    - Current: `放大缩放比例`
    - Source: `Increase Zoom Level`
    - Suggest: `增大缩放比例`
    - The source pair is Increase/Decrease Zoom Level; the decrease string uses 减小缩放比例, so the increase string should use 增大缩放比例. 放大…比例 is not a valid verb-object pairing.
- `You don’t have any tabs open in Firefox on your other devices.` — `zh-CN/firefox-ios.xliff` — Awkward/ungrammatical rendering with redundant 已经 makes the sentence read incorrectly.
    - Current: `您没有在其他设备的 Firefox 上已经打开的标签页。`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `您的其他设备上的 Firefox 没有打开任何标签页。`
    - The source states no tabs are open in Firefox on the user's other devices; the Chinese word order with 已经 is ungrammatical.
- `TodayWidget.MoreTabsLabel` — `zh-CN/firefox-ios.xliff` — Redundant wording "还有另" in the more-tabs label.
    - Current: `+还有另 %d 个…`
    - Source: `+%d More…`
    - Suggest: `+另有 %d 个…`
    - "还有" and "另" duplicate the same meaning; source is simply "+%d More…".

### D. Terminology, register & consistency

- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `zh-CN/firefox-ios.xliff` — "Reader View" is rendered as 阅读模式 (Reader Mode) instead of Firefox's standard 阅读视图.
    - Current: `关闭阅读模式`
    - Source: `Turn off Reader View`
    - Suggest: `关闭阅读视图`
    - en-US "Reader View" is consistently 阅读视图 in Firefox zh-CN; 阅读模式 corresponds to "Reader Mode".
- `Onboarding.Customization.Theme.Dark.Action.v123` — `zh-CN/firefox-ios.xliff` — Theme name "Dark" translated as 深邃 instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - iOS/Firefox zh-CN uses 深色/浅色 for Dark/Light themes; 深邃 ("profound") is not the established term.
- `Onboarding.Customization.Theme.Light.Action.v123` — `zh-CN/firefox-ios.xliff` — Theme name "Light" translated as 明亮 instead of the standard 浅色.
    - Current: `明亮`
    - Source: `Light`
    - Suggest: `浅色`
    - iOS/Firefox zh-CN uses 浅色 for the Light theme, paired with 深色 for Dark.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatus.v151` — `zh-CN/firefox-ios.xliff` — "Available" as a feature status is rendered as the verb "提供" instead of the adjective "可用".
    - Current: `提供`
    - Source: `Available`
    - Suggest: `可用`
    - The source is a status label meaning the feature is turned on/usable; the companion description string already uses "**可用**", so "提供" is both wrong in part of speech and inconsistent on the same screen.
- `Dark` — `zh-CN/firefox-ios.xliff` — Reading View dark theme setting is rendered as "深邃" instead of the standard "深色".
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - "Dark" as a theme setting is consistently "深色" in Firefox zh-CN; "深邃" means "profound/deep" and is not a theme name.
- `FirefoxHome.Stories.Minutes.v140` — `zh-CN/firefox-ios.xliff` — The abbreviation required by the developer comment is not used; "分钟" is the full form and the source's "min:" label pattern is dropped.
    - Current: `%d 分钟`
    - Source: `min: %d`
    - Suggest: `%d 分钟阅读`
    - Developer comment states minutes should be abbreviated due to space constraints; the source is "min: %d". Chinese has no shorter form, but the label meaning "minutes to read" is lost — at minimum the reading context should be preserved compactly.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `zh-CN/firefox-ios.xliff` — "Fingerprinters" is rendered as 数字指纹跟踪程序 here but 数字指纹追踪程序 in the description string on the same feature screen.
    - Current: `数字指纹跟踪程序`
    - Source: `Fingerprinters`
    - Suggest: `数字指纹追踪程序`
    - Menu.TrackingProtectionDescription.Fingerprinters uses 数字指纹追踪程序 for the same source term; the two should match within the same tracking-protection screen.
- `Menu.ViewDekstopSiteAction.Title` — `zh-CN/firefox-ios.xliff` — "Request Desktop Site" is translated as 要求 while the parallel mobile string uses 请求, an inconsistency on the same menu.
    - Current: `要求桌面版网站`
    - Source: `Request Desktop Site`
    - Suggest: `请求桌面版网站`
    - Menu.ViewMobileSiteAction.Title renders the identical source verb "Request" as 请求; the same term should be consistent within the same menu.

### E. Typography, punctuation & spacing

- `Engagement.Notification.Treatment.B.Body.v114` — `zh-CN/firefox-ios.xliff` — Missing sentence-ending period present in the source.
    - Current: `%@ 将不会保存浏览期间的 Cookie 和历史记录`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `%@ 将不会保存浏览期间的 Cookie 和历史记录。`
    - The en-US body ends with a period; the Chinese sentence has no terminating punctuation, unlike the other notification body strings in the same file.
- `DefaultBrowserPopup.ThirdLabel.v114` — `zh-CN/firefox-ios.xliff` — Missing space after the list number, inconsistent with the first and second labels.
    - Current: `3.选择 *%@*`
    - Source: `3. Select *%@*`
    - Suggest: `3. 选择 *%@*`
    - Sibling strings use "1. " and "2. " with a space after the numeral; this one omits it.
- `TabTrayCloseTabsOlderThanTitle.v140` — `zh-CN/firefox-ios.xliff` — The ellipsis at the end of "Close tabs older than…" is dropped in the translation.
    - Current: `关闭早于特定时间的标签页`
    - Source: `Close tabs older than…`
    - Suggest: `关闭早于以下时间的标签页…`
    - The source ends with an ellipsis indicating a submenu/further choice; the translation omits it, unlike the sibling string TabTrayCloseOldTabsTitle which keeps it.
- `FirefoxHomepage.ContextualMenu.SponsoredContent.v101` — `zh-CN/firefox-ios.xliff` — Full-width ampersand "＆" used instead of the conventional Chinese connector.
    - Current: `我们的赞助商＆您的隐私`
    - Source: `Our Sponsors & Your Privacy`
    - Suggest: `我们的赞助商与您的隐私`
    - zh-CN typography does not use a full-width ampersand as a conjunction; compare FxA.ManageAccount which renders "&" as "和".
- `OpenURL.Error.Message` — `zh-CN/firefox-ios.xliff` — Missing space between the Chinese text and the Latin brand name "Firefox".
    - Current: `地址无效，因此Firefox 无法打开该页面。`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `地址无效，因此 Firefox 无法打开该页面。`
    - zh-CN convention (and the rest of this file, e.g. "啊哦！Firefox 崩溃了") inserts a space between CJK characters and Latin words; here "因此Firefox" lacks it while the following space is present.
- `Settings.Passwords.OnboardingMessage.v103` — `zh-CN/firefox-ios.xliff` — Missing space between "触控 ID" and "或" pattern — actually missing space in "触控 ID或设备密码".
    - Current: `触控 ID或设备密码`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `触控 ID 或设备密码`
    - Latin text "ID" must be separated from the following Chinese character with a space, as done elsewhere in the same string ("面容 ID、").
- `TopSites.RemovePage.Button` — `zh-CN/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `移除页面 - %@`
    - Source: `Remove page — %@`
    - Suggest: `移除页面 — %@`
    - Source uses an em dash separator; the translation uses a plain hyphen.
- `Use stage servers` — `zh-CN/firefox-ios.xliff` — Half-width parentheses used without spacing around Latin text in Chinese sentence.
    - Current: `使用预发布(Stage)服务器`
    - Source: `Use stage servers`
    - Suggest: `使用预发布（Stage）服务器`
    - zh-CN typography requires full-width parentheses within Chinese text.

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

### Resolved to date (0)

_Nothing resolved yet._
