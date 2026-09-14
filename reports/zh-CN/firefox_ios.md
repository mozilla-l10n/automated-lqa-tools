# Firefox iOS l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-CN: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (70)

- `Use your fingerprint to access Logins now.` — `zh-CN/firefox-ios.xliff` — "Use your fingerprint" mistranslated as "验证您的指纹" is fine, but "Enter passcode" string uses 密码 for passcode — see separate finding.
    - Current: `验证您的指纹以访问登录信息。`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `请使用您的指纹访问登录信息。`
    - Minor, but the source asks the user to use their fingerprint now; the rendering is acceptable. (skip)
- `Closing tab` — `zh-CN/firefox-ios.xliff` — Progressive "Closing tab" notification rendered as the imperative/plain "关闭标签页" (Close tab), losing the in-progress meaning.
    - Current: `关闭标签页`
    - Source: `Closing tab`
    - Suggest: `正在关闭标签页`
    - The developer comment says it notifies the user that the tab is being closed; the target reads as the action label "Close tab" rather than an ongoing process.
- `ContextualHints.TabTray.InactiveTabs` — `zh-CN/firefox-ios.xliff` — Reversed meaning: source says tabs not viewed FOR two weeks, target says tabs not viewed WITHIN two weeks get moved.
    - Current: `两周内未查看的标签页将移至此处。`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `超过两周未查看的标签页将移至此处。`
    - "Tabs you haven’t viewed for two weeks" means tabs untouched for at least two weeks; "两周内未查看" states a different (shorter/inverted) condition.
- `CoverSheet.v24.ETP.Description` — `zh-CN/firefox-ios.xliff` — The item "ads" is dropped from the list of things Strict mode blocks.
    - Current: `开启“严格”模式则可拦截更多跟踪器和弹窗。`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `开启“严格”模式则可拦截更多跟踪器、广告和弹窗。`
    - Source lists "more trackers, ads, and popups"; the translation omits "ads".
- `Dark` — `zh-CN/firefox-ios.xliff` — "Dark" theme rendered as 深邃 ("profound/deep") instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - This is the dark theme setting in reader mode; the established term is 深色.
- `ErrorPages.CertWarning.Description` — `zh-CN/firefox-ios.xliff` — "The owner of %@" is rendered as "管理员" (administrator) instead of "所有者/拥有者".
    - Current: `%@ 的管理员未正确配置网站。`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `%@ 的所有者未正确配置网站。`
    - en-US says "The owner of %@"; 管理员 means administrator, a different party.
- `FirefoxHomepage.ContextualMenu.SponsoredContent.v101` — `zh-CN/firefox-ios.xliff` — Uses fullwidth ampersand "＆" instead of the Chinese conjunction/standard punctuation.
    - Current: `我们的赞助商＆您的隐私`
    - Source: `Our Sponsors & Your Privacy`
    - Suggest: `我们的赞助商与您的隐私`
    - zh-CN convention renders "&" as 与/和; the fullwidth ampersand is not used elsewhere (e.g. FxA.ManageAccount uses 和).
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `zh-CN/firefox-ios.xliff` — Translation drops the notion of disconnecting "from" Firefox Sync, reading as "a device has disconnected Firefox Sync".
    - Current: `一台设备已断开 Firefox 同步`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `一台设备已断开与 Firefox 同步的连接`
    - Source is "A device has disconnected from Firefox Sync"; the Chinese omits 与…的连接, making 同步 the object of 断开 rather than the service disconnected from.
- `Increase text size` — `zh-CN/firefox-ios.xliff` — "Increase text size" is rendered as "增大文字", dropping "size".
    - Current: `增大文字`
    - Source: `Increase text size`
    - Suggest: `增大文字大小`
    - The source refers to increasing the font size in reader mode display settings; 增大文字 alone omits 大小/字号.
- `Menu.AddPin.Confirm2` — `zh-CN/firefox-ios.xliff` — Toast says the shortcut itself was added rather than the item was added to Shortcuts.
    - Current: `快捷方式已添加`
    - Source: `Added to Shortcuts`
    - Suggest: `已添加到快捷方式`
    - en-US "Added to Shortcuts" and the comment state the item was added to the Shortcuts list; the translation reverses the relationship, matching neither the source nor the parallel string Menu.AddToReadingList.Confirm (已添加到阅读列表).
- `Menu.RemovedFromShortcuts.v99` — `zh-CN/firefox-ios.xliff` — "Remove from Shortcuts" is rendered as "移除快捷方式" (remove the shortcut(s)) instead of "从快捷方式移除".
    - Current: `移除快捷方式`
    - Source: `Remove from Shortcuts`
    - Suggest: `从快捷方式移除`
    - The source means removing the current site from the Shortcuts section; the related toast Menu.RemovePin.Confirm2.v99 correctly uses "已从快捷方式移除". "移除快捷方式" reads as deleting the Shortcuts feature/entry itself.
- `OpenURL.Error.Message` — `zh-CN/firefox-ios.xliff` — Missing space between the Chinese text and the Latin brand name "Firefox".
    - Current: `地址无效，因此Firefox 无法打开该页面。`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `地址无效，因此 Firefox 无法打开该页面。`
    - The locale inserts a space between CJK text and Latin words, as done elsewhere in the same string ("Firefox 无法").
- `Menu.TrackingProtectionDescription.Fingerprinters` — `zh-CN/firefox-ios.xliff` — Fingerprinters is rendered "数字指纹追踪程序" here but "数字指纹跟踪程序" in the related title string.
    - Current: `数字指纹追踪程序`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `数字指纹跟踪程序`
    - Menu.TrackingProtectionFingerprintersBlocked.Title on the same screen uses "数字指纹跟踪程序"; the term should be consistent.
- `SentTab_TabArrivingNotification_WithDevice_body` — `zh-CN/firefox-ios.xliff` — The placeholder is the app name where the tab arrived, but the translation makes it the subject that received the tab.
    - Current: `%@ 收到了新的标签页`
    - Source: `New tab arrived in %@`
    - Suggest: `新标签页已送达 %@`
    - Source: "New tab arrived in %@" with %@ = app name; the tab arrives in the app, it is not the app/device receiving as an agent in a title sense. Also it duplicates the title string wording.
- `SentTab_TabArrivingNotification_WithDevice_title` — `zh-CN/firefox-ios.xliff` — "Tab received from %@" is rendered as "%@ received a new tab", reversing the direction of the transfer.
    - Current: `%@ 收到新的标签页`
    - Source: `Tab received from %@`
    - Suggest: `收到来自 %@ 的标签页`
    - The source says the tab was received FROM the named device; the translation says the named device received the tab.
- `Settings.DisplayTheme.OptionDark` — `zh-CN/firefox-ios.xliff` — "Dark" theme option translated as 深邃 ("deep/profound") instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - The source is the dark theme option; zh-CN uses 深色 consistently elsewhere in this file (e.g. 网站深色模式, 使用系统浅/深色模式). 深邃 means "profound/deep" and is not a theme term.
- `Settings.DisplayTheme.OptionLight` — `zh-CN/firefox-ios.xliff` — "Light" theme option translated as 明亮 instead of the standard 浅色.
    - Current: `明亮`
    - Source: `Light`
    - Suggest: `浅色`
    - Paired with the dark option; the file elsewhere uses 浅/深色模式. 明亮 ("bright") is inconsistent with the established theme terminology.
- `Settings.DataManagement.SearchLabel` — `zh-CN/firefox-ios.xliff` — "Filter Sites" (an imperative placeholder in a search bar) rendered as the noun phrase 网站过滤.
    - Current: `网站过滤`
    - Source: `Filter Sites`
    - Suggest: `过滤网站`
    - The source is a verb phrase prompting the user to filter sites; 网站过滤 reads as the noun "site filtering".
- `Settings.Home.Option.Wallpaper.LimitedEdition.IndependentVoices.Description.v106` — `zh-CN/firefox-ios.xliff` — "Independent Voices" collection name mistranslated as "凡人之声" (voices of mortals).
    - Current: `全新“凡人之声”壁纸集。`
    - Source: `The new Independent Voices collection.`
    - Suggest: `全新“独立之声”壁纸集。`
    - The en-US collection name is "Independent Voices"; 凡人 means "mortals/ordinary people", not "independent".
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `zh-CN/firefox-ios.xliff` — "Sponsored Shortcuts" rendered as "赞助商网站" (sponsor websites), dropping the Shortcuts term used consistently elsewhere on the same screen.
    - Current: `赞助商网站`
    - Source: `Sponsored Shortcuts`
    - Suggest: `赞助商快捷方式`
    - Source is "Sponsored Shortcuts"; other strings on the same screen translate Shortcuts as 快捷方式, so 网站 (websites) is both a mistranslation and inconsistent.
- `Settings.OfferClipboardBar.Status.v128` — `zh-CN/firefox-ios.xliff` — Translation adds "询问" (ask/prompt) which is not in the source "When opening %@".
    - Current: `打开 %@ 时询问`
    - Source: `When opening %@`
    - Suggest: `打开 %@ 时`
    - The source is just the status description "When opening %@"; the older variant Settings.OfferClipboardBar.Status is correctly rendered as "当打开 Firefox 时" without the added verb.
- `Settings.Passwords.OnboardingMessage.v103` — `zh-CN/firefox-ios.xliff` — Missing space/separator between "触控 ID" and "或设备密码".
    - Current: `面容 ID、触控 ID或设备密码保护`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `面容 ID、触控 ID 或设备密码保护`
    - Latin text "ID" abutting the following Chinese character without the spacing used elsewhere in the same sentence ("面容 ID、").
- `Settings.NoImageModeBlockImages.Label.v99` — `zh-CN/firefox-ios.xliff` — "Block Images" rendered as "无图模式" (no-image mode) instead of the action label.
    - Current: `无图模式`
    - Source: `Block Images`
    - Suggest: `屏蔽图片`
    - The source label is "Block Images", the toggle action; "无图模式" names a mode not present in the source.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `zh-CN/firefox-ios.xliff` — The description reverses the timing condition and mistranslates "inactive section" as a sleep state.
    - Current: `两周内未查看的标签页将进入休眠状态。`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `超过两周未查看的标签页将被移至“不活跃”版块。`
    - en-US says tabs you haven't viewed FOR two weeks (i.e. for longer than two weeks) get moved to the inactive section; "两周内未查看" means "not viewed within two weeks" which is ambiguous/reversed, and "进入休眠状态" claims the tabs are suspended rather than moved to a separate section of the tab tray.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `zh-CN/firefox-ios.xliff` — "ads" is dropped from the list of blocked items.
    - Current: `拦截更多跟踪器和弹窗。`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `拦截更多跟踪器、广告和弹窗。`
    - The source lists "more trackers, ads, and popups"; the translation omits ads.
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-CN/firefox-ios.xliff` — "helps stop" is rendered as an absolute "阻止", overstating the protection.
    - Current: `减少定向广告，并阻止广告商跟踪您的浏览。`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `减少定向广告，并帮助阻止广告商跟踪您的浏览。`
    - en-US says "helps stop advertisers from tracking"; the Chinese asserts the product stops tracking outright, a claim the source does not make.
- `You don’t have any tabs open in Firefox on your other devices.` — `zh-CN/firefox-ios.xliff` — Awkward/ungrammatical rendering of "You don't have any tabs open in Firefox on your other devices."
    - Current: `您没有在其他设备的 Firefox 上已经打开的标签页。`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `您的其他设备上的 Firefox 未打开任何标签页。`
    - The Chinese sentence structure "没有…已经打开的标签页" is ungrammatical/garbled; the source simply states no tabs are open in Firefox on other devices.
- `fxa.signin.qr-link-instruction` — `zh-CN/firefox-ios.xliff` — Instruction mistranslated: source says open Firefox and go to firefox.com/pair, translation says use Firefox to open firefox.com/pair, dropping the two-step meaning is acceptable but "在计算机上" omits "your" — main issue is the merged instruction
    - Current: `在计算机上使用 Firefox 打开 firefox.com/pair`
    - Source: `On your computer open Firefox and go to firefox.com/pair`
    - Suggest: `在您的计算机上打开 Firefox 并访问 firefox.com/pair`
    - The en-US instructs the user to open Firefox and then navigate to firefox.com/pair; the translation collapses this into using Firefox to open a URL, losing the explicit step of opening the browser.
- `Menu.ViewDekstopSiteAction.Title` — `zh-CN/firefox-ios.xliff` — "Request Desktop Site" is rendered as 要求桌面版网站 while the parallel "Request Mobile Site" uses 请求移动版网站, an inconsistent rendering of the same verb on the same menu.
    - Current: `要求桌面版网站`
    - Source: `Request Desktop Site`
    - Suggest: `请求桌面版网站`
    - Same source verb "Request" in two adjacent menu items translated differently; 请求 is the established term used in the sibling string.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `zh-CN/firefox-ios.xliff` — "any of your history or cookies" is rendered as "历史记录和 Cookie" (and), weakening the negation to "won't remember both".
    - Current: `Firefox 不会记住您的历史记录和 Cookie`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox 不会记住您的任何历史记录或 Cookie`
    - The en-US negates each item individually ("any of ... or ..."); "和" under negation in Chinese can be read as negating the combination rather than each item.
- `TodayWidget.MoreTabsLabel` — `zh-CN/firefox-ios.xliff` — "+还有另 %d 个…" is redundant/ungrammatical for "+%d More…".
    - Current: `+还有另 %d 个…`
    - Source: `+%d More…`
    - Suggest: `+另 %d 个…`
    - "还有" and "另" duplicate the same meaning; source is a compact widget label "+%d More…" and space is tight.
- `TodayWidget.TopSitesGalleryDescription` — `zh-CN/firefox-ios.xliff` — Translation drops "and recently visited" from "frequently and recently visited sites".
    - Current: `添加“常用网站”快捷方式。`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `添加常用和最近访问网站的快捷方式。`
    - The source describes shortcuts to frequently AND recently visited sites; the target only mentions frequently visited sites.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `zh-CN/firefox-ios.xliff` — Reversed direction: source says signing in grabs bookmarks FROM other synced devices, translation says the bookmarks can be used ON other devices.
    - Current: `登录后还可在其他同步的设备上使用这些书签。`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `登录后即可获取其他同步设备上的书签。`
    - en-US: "Sign in to grab bookmarks from other synced devices." The Chinese states the opposite data direction (using these bookmarks on other devices), inconsistent with the sibling string Root.Body which correctly says 从其他同步的设备上接收书签.
- `Biometry.Screen.UniversalAuthenticationReason.v122` — `zh-CN/firefox-ios.xliff` — Imperative prompt rendered as a restrictive statement ("only after authenticating can you access") instead of a request to authenticate.
    - Current: `进行身份验证后才能访问保存的密码和付款方式。`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `请验证身份后访问保存的密码和付款方式。`
    - The source "Authenticate to access your saved passwords and payment methods." is an instruction to the user, matching the sibling v115 string translated as 请验证身份后访问密码。; the current wording changes register and phrasing inconsistently within the same file.
- `ContextualHints.FeltDeletion.Body.v122` — `zh-CN/firefox-ios.xliff` — The translation reverses the sequence/meaning: the source says tapping starts a fresh private session by deleting history and cookies, while the Chinese says to delete data after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `点按此处开始全新的隐私浏览会话。删除您的历史记录、Cookie 等一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The added "浏览完毕后" (after you finish browsing) is not in the source and changes when deletion happens.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `zh-CN/firefox-ios.xliff` — "Townland" (a rural land division, chiefly Irish) is rendered as 镇 (town), which is the term used for "Town"/"Township" elsewhere in the same file.
    - Current: `镇`
    - Source: `Townland`
    - Suggest: `乡村地区`
    - The developer comment specifies a townland is "a specific type of land division used in rural areas", distinct from 镇/乡镇 already used for Village or Township in Addresses.EditAddress.AutofillAddressVillageTownship.v129; using 镇 both mistranslates and creates a within-screen terminology clash.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `zh-CN/firefox-ios.xliff` — "Tracking content" is translated but the developer comment/label concerns analytics trackers; more importantly the unit counter is fine — the issue is the string renders "Tracking content" consistently, but count suffix ok
    - Current: `跟踪性内容：%@ 项`
    - Source: `Tracking content: %@`
    - Suggest: `跟踪性内容：%@`
    - The source has no measure word/unit after the number; adding 项 is acceptable style, however here it mismatches other entries — low value.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `zh-CN/firefox-ios.xliff` — The Pocket footer title reverses the meaning: the source says Pocket powers the section and is part of the Firefox family, but the target says the Firefox family product line provides Pocket in an odd merged sentence.
    - Current: `由 %2$@ 系列产品 - %1$@ 提供。`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `由 %1$@ 提供支持。%1$@ 是 %2$@ 产品家族的一员。`
    - en-US is two statements: "Powered by Pocket." and "Part of the Firefox family." The translation collapses them and mis-assigns the roles.
- `MainMenu.ToolsSection.AccessibilityLabels.LibraryOptions.v142` — `zh-CN/firefox-ios.xliff` — "Library" is rendered as 我的足迹 ("my footprints/trail") instead of the standard term 资料库.
    - Current: `我的足迹`
    - Source: `Library`
    - Suggest: `资料库`
    - The source is "Library", the accessibility label for the group containing Downloads, History, Passwords. 我的足迹 is not the Firefox term for Library and conveys a different concept (browsing traces).
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `zh-CN/firefox-ios.xliff` — Register inconsistency: the informal 你们 is used in the same sentence that begins with the formal 您.
    - Current: `若您使用的是企业网络，那么你们的支持团队可能了解更多信息。`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `若您使用的是企业网络，贵单位的支持团队可能了解更多信息。`
    - zh-CN convention is the formal 您; mixing 您 and 你们 within one sentence violates the established form of address.
- `NativeErrorPage.GenericError.Description.v134` — `zh-CN/firefox-ios.xliff` — "The owner of %@" is rendered as 管理员 (administrator) and the sentence attributes misconfiguration in a different way than the source.
    - Current: `%@ 的管理员未正确配置此网站`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `%@ 的所有者未正确设置此网站`
    - The en-US says "owner", not "administrator".
- `DefaultBrowserPopup.ThirdLabel.v114` — `zh-CN/firefox-ios.xliff` — Missing space after the list number, inconsistent with the first and second labels.
    - Current: `3.选择 *%@*`
    - Source: `3. Select *%@*`
    - Suggest: `3. 选择 *%@*`
    - Sibling strings use "1. 前往" and "2. 轻点" with a space after the numeral; this one omits it.
- `Onboarding.Customization.Toolbar.Description.v123` — `zh-CN/firefox-ios.xliff` — "Keep searches within reach" is rendered as "holding the phone lightly can invoke search", which is not what the source says.
    - Current: `轻松握持就可唤起搜索。`
    - Source: `Keep searches within reach.`
    - Suggest: `让搜索始终触手可及。`
    - The en-US means the search bar stays easy to reach; the Chinese asserts that merely holding the device invokes search, which is a different (and false) behaviour claim.
- `Onboarding.Customization.Intro.Title.v123` — `zh-CN/firefox-ios.xliff` — Adds "线上生活" (online life), which the source does not mention.
    - Current: `%@ 让您掌控线上生活`
    - Source: `%@ puts you in control`
    - Suggest: `%@ 让您掌控一切`
    - Source is simply "%@ puts you in control"; the translation narrows/expands it to controlling one's online life.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `zh-CN/firefox-ios.xliff` — "companies" rendered as "大公司" (big companies), adding a qualifier the source does not have.
    - Current: `自动阻止大公司窥探您的浏览活动`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `自动阻止各公司窥探您的点击行为`
    - The en-US says "companies", not "big companies"; the translation narrows/changes the claim about who is blocked.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `zh-CN/firefox-ios.xliff` — "Browsing just got better" mistranslated as "纯粹带来更好的浏览体验", introducing "纯粹" which is not in the source.
    - Current: `纯粹带来更好的浏览体验。`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `浏览体验更上一层楼。`
    - The source simply states browsing just got better; "纯粹" (purely/simply) is an added and unsupported qualifier.
- `Onboarding.Welcome.Description.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", adding a claim the source never makes.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US says the browser "helps stop companies"; the Chinese asserts it "automatically blocks" them, and narrows "companies" to "big companies".
- `Onboarding.Welcome.Description.TreatementA.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", overstating the product's behaviour.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US only says the browser "helps stop companies" from tracking; the translation claims automatic blocking and restricts the subject to large companies.
- `PasswordGenerator.PasswordReadoutPrefaceA11y.v132` — `zh-CN/firefox-ios.xliff` — "Generated password: %@" is rendered as a sentence "Password has been generated" instead of a noun label.
    - Current: `已生成密码：%@`
    - Source: `Generated password: %@`
    - Suggest: `生成的密码：%@`
    - The source is a noun-phrase prefix labelling the password that follows ("Generated password"), not a statement that a password was generated.
- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `zh-CN/firefox-ios.xliff` — Missing measure word/unit after the count placeholder in the footer text.
    - Current: `已拦截 %1$@ 跟踪器`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `已拦截 %1$@ 个跟踪器`
    - %1$@ is a number; Chinese requires a measure word (个/项) between the number and 跟踪器, as done in HeaderLabelAccessibilityLabel.
- `PrimaryButton.Label.v112` — `zh-CN/firefox-ios.xliff` — Action button "Take Survey" translated as the noun "Survey" instead of an action.
    - Current: `问卷调查`
    - Source: `Take Survey`
    - Suggest: `填写问卷`
    - The source is a call-to-action button label meaning the user will be taken to a survey; 问卷调查 is just the noun "survey" and loses the action.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `zh-CN/firefox-ios.xliff` — Translation adds "此链接" (this link), which the source does not state.
    - Current: `要允许 %@ 打开此链接吗？`
    - Source: `Allow %@ to open?`
    - Suggest: `要允许打开 %@ 吗？`
    - In the source, %@ is the app name and the prompt asks whether to allow the app to open; the added object "此链接" is not in the source.
- `CreditCard.RememberCard.Header.v122` — `zh-CN/firefox-ios.xliff` — Adds "保存" (save) to "encrypts your card number", asserting behaviour the source does not state.
    - Current: `%@ 会将卡号加密保存。`
    - Source: `%@ encrypts your card number. Your security code won’t be saved.`
    - Suggest: `%@ 会加密您的卡号。`
    - The source only says the app encrypts the card number, not that it encrypts and saves it.
- `Settings.Browsing.BackgroundAudio.Title.v156` — `zh-CN/firefox-ios.xliff` — "Background Audio" is translated as "背景音乐" (background music), which misstates the feature.
    - Current: `背景音乐`
    - Source: `Background Audio`
    - Suggest: `后台音频`
    - The comment says audio from web pages continues playing when the app is backgrounded; "背景音乐" means background music (a soundtrack), not audio playing in the background.
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Message.v154` — `zh-CN/firefox-ios.xliff` — "Your voice" rendered as "您的声音" reads as the sound itself rather than voice input/recordings.
    - Current: `您的声音、问题和答案永远不会被存储。`
    - Source: `Your voice, questions, and answers are never stored.`
    - Suggest: `您的语音、问题和答案永远不会被存储。`
    - In the context of a Quick Answers voice feature, "voice" means voice input (语音); 声音 is generic sound.
- `Settings.Notifications.TipsAndFeaturesNotificationsTitle.v112` — `zh-CN/firefox-ios.xliff` — "Tips and Features" is rendered only as "使用技巧", dropping "Features".
    - Current: `使用技巧`
    - Source: `Tips and Features`
    - Suggest: `使用技巧与功能`
    - The source title is "Tips and Features"; the translation omits "Features", and the accompanying description does mention features.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `zh-CN/firefox-ios.xliff` — "suggestions" is translated as "结果" (results) instead of "建议", inconsistent with the parallel string.
    - Current: `在隐私浏览中显示来自 Firefox 建议的结果`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `在隐私浏览中显示来自 Firefox 建议的建议`
    - Source says "Show suggestions from Firefox Suggest in private sessions"; the parallel string Settings.Search.PrivateSession.Description uses "建议" for suggestions.
- `Settings.Translation.AutoTranslate.Footer.v151` — `zh-CN/firefox-ios.xliff` — "your top preferred language" is mistranslated as "the language you know best".
    - Current: `自动将页面翻译成您最熟悉的语言。`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `自动将页面翻译成您的首选语言。`
    - The source refers to the top entry in the user's Preferred Languages list (see Settings.Translation.PreferredLanguages.SectionTitle 首选语言), not the language the user is most familiar with.
- `Settings.Studies.Message.v136` — `zh-CN/firefox-ios.xliff` — "before they're released to everyone" is rendered as "not yet fully rolled out", losing the meaning of trying features early.
    - Current: `抢先体验尚未全面推出的功能和概念。`
    - Source: `Try out features and ideas before they’re released to everyone.`
    - Suggest: `在功能和想法向所有人推出之前抢先体验。`
    - The source says users try features and ideas before general release; the translation states the features have not been fully rolled out, a different assertion.
- `ContextualHints.Summarize.Description.v142` — `zh-CN/firefox-ios.xliff` — "Touch and hold for Reader View" is rendered as "按住可进入阅读模式" which drops the standard Firefox term 阅读器视图; more importantly the sentence structure is fine but the term is wrong.
    - Current: `按住可进入阅读模式`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `长按可进入阅读器视图`
    - Firefox's established zh-CN term for "Reader View" is 阅读器视图, not 阅读模式.
- _…and 10 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (58)

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — The translation reverses the direction of the sync: the source says signing in fetches bookmarks from other devices, not that bookmarks become usable on other devices.
    - Current: `登录后还可在其他同步的设备上使用这些书签。`
    - Suggest: `登录后即可获取其他同步设备上的书签。`
    - en-US: "Sign in to grab bookmarks from other synced devices" — bookmarks are pulled from other devices to this one; the parallel signed-in string is correctly translated as 从其他同步的设备上接收书签.
- `ContextualHints.FeltDeletion.Body.v122` — `Shared/Supporting Files/en.lproj/ContextualHints.strings` — The translation reverses the timing/meaning: the source says tapping deletes history and cookies now to start a fresh private session, not that data is deleted after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Suggest: `点按此处开始全新的隐私浏览会话，删除您的历史记录、Cookie，一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The deletion happens on tap, not "after you finish browsing" (浏览完毕后), which misstates the fire button's behavior.
- `Addresses.EditAddress.AutofillAddressName.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Name" in an address form refers to the person's full name, but the translation means "name/title" of a thing.
    - Current: `名称`
    - Suggest: `姓名`
    - The developer comment says the field is where the user inputs their full name; Chinese uses 姓名 for a person's name, while 名称 refers to the name of an object or organization.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Townland" (a rural land division) is rendered as 镇 (town), losing the specific meaning and colliding with other town-related fields.
    - Current: `镇`
    - Suggest: `乡村地区（Townland）`
    - The comment explains a townland is a specific type of rural land division, not a town; 镇 means "town" and duplicates the Village or Township field.
- `Engagement.Notification.Treatment.B.Body.v114` — `Shared/Supporting Files/en.lproj/EngagementNotification.strings` — Missing sentence-ending period present in the source.
    - Current: `%@ 将不会保存浏览期间的 Cookie 和历史记录`
    - Suggest: `%@ 将不会保存浏览期间的 Cookie 和历史记录。`
    - The en-US body ends with a period; the Chinese sentence has no terminating punctuation, unlike the other notification body strings in the same file.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reader View" is rendered as 阅读模式 (Reader Mode) instead of Firefox's standard 阅读视图.
    - Current: `关闭阅读模式`
    - Suggest: `关闭阅读视图`
    - en-US "Reader View" is consistently 阅读视图 in Firefox zh-CN; 阅读模式 corresponds to "Reader Mode".
- `MainMenu.ToolsSection.AccessibilityLabels.LibraryOptions.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Library" is translated as 我的足迹 ("my footprints"), which does not mean Library.
    - Current: `我的足迹`
    - Suggest: `资料库`
    - The source term "Library" names the collection of Downloads, History, Passwords; Firefox zh-CN uses 资料库. 我的足迹 is a different, invented label.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Inconsistent register: the polite 您 switches to 你们 within the same sentence.
    - Current: `若您使用的是企业网络，那么你们的支持团队可能了解更多信息。`
    - Suggest: `若您使用的是企业网络，您的支持团队可能了解更多信息。`
    - The source uses "your" consistently; mixing 您 and 你们 in one sentence breaks the honorific register used throughout the file.
- `NativeErrorPage.GenericError.Description.v134` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — "owner" is rendered as 管理员 (administrator) instead of 所有者/拥有者.
    - Current: `%@ 的管理员未正确配置此网站`
    - Suggest: `%@ 的所有者未正确配置此网站`
    - The en-US source says "The owner of %@", not the administrator.
- `DefaultBrowserPopup.ThirdLabel.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Missing space after the list number, inconsistent with the first and second labels.
    - Current: `3.选择 *%@*`
    - Suggest: `3. 选择 *%@*`
    - Sibling strings use "1. " and "2. " with a space after the numeral; this one omits it.
- `Onboarding.Customization.Theme.Dark.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Theme name "Dark" translated as 深邃 instead of the standard 深色.
    - Current: `深邃`
    - Suggest: `深色`
    - iOS/Firefox zh-CN uses 深色/浅色 for Dark/Light themes; 深邃 ("profound") is not the established term.
- `Onboarding.Customization.Theme.Light.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Theme name "Light" translated as 明亮 instead of the standard 浅色.
    - Current: `明亮`
    - Suggest: `浅色`
    - iOS/Firefox zh-CN uses 浅色 for the Light theme, paired with 深色 for Dark.
- `Onboarding.Customization.Toolbar.Description.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Keep searches within reach" is mistranslated as being about holding/gripping the phone.
    - Current: `轻松握持就可唤起搜索。`
    - Suggest: `让搜索触手可及。`
    - The source means keeping search easily accessible (toolbar placement), not "easy gripping summons search"; 握持 (gripping) introduces meaning not in the source.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "and that you use it" is mistranslated as "使用方式" (how you use it).
    - Current: `您发现 %1$@ 的途径及使用方式`
    - Suggest: `您发现 %1$@ 的途径以及您正在使用它这一事实`
    - The source only shares the fact that you use the app, not how you use it; the translation overstates the data shared.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Browsing just got better" rendered with a spurious "纯粹".
    - Current: `纯粹带来更好的浏览体验。`
    - Suggest: `浏览体验就此更上一层楼。`
    - The source has no notion of "purely/simply"; 纯粹 adds meaning not present in en-US.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "companies" is rendered as "大公司" (big companies), adding a qualifier not in the source.
    - Current: `自动阻止大公司窥探您的浏览活动`
    - Suggest: `自动阻止各公司窥探您的点击行为`
    - The en-US says "companies", not "big companies"; also "your clicks" is generalized to "浏览活动".
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148.v2` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Translation adds "的浏览器" (browser), which is not in the source.
    - Current: `通过内置隐私保护的浏览器打开链接`
    - Suggest: `打开链接，即享内置隐私保护`
    - The en-US "Open your links with built-in privacy" does not mention a browser; the added noun changes the statement.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "bookmarks, history" is translated as "书签、历史记录" but "history" list item order/content drops nothing—actually "your top sites" fine; issue is "history" omitted? No—see rationale.
    - Current: `键入即可获取搜索建议、常用网站、书签、历史记录、搜索引擎，尽在一处。`
    - Suggest: `键入即可获取搜索建议、常用网站、书签、历史记录和搜索引擎，尽在一处。`
    - Enumeration in Chinese should join the final item with 和/以及 rather than another 顿号; minor grammar issue.
- `PrimaryButton.Label.v112` — `Shared/Supporting Files/en.lproj/ResearchSurface.strings` — "Take Survey" (an action button) is rendered as the noun phrase "问卷调查" instead of a call to action.
    - Current: `问卷调查`
    - Suggest: `参与调查`
    - The source is a button that takes the user to a survey; the translation is just the noun "survey/questionnaire", losing the imperative action meaning.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatus.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Available" as a feature status is rendered as the verb "提供" instead of the adjective "可用".
    - Current: `提供`
    - Suggest: `可用`
    - The source is a status label meaning the feature is turned on/usable; the companion description string already uses "**可用**", so "提供" is both wrong in part of speech and inconsistent on the same screen.
- `Settings.Browsing.BackgroundAudio.Title.v156` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Background Audio" is rendered as "背景音乐" (background music), which names the wrong feature.
    - Current: `背景音乐`
    - Suggest: `后台音频`
    - The setting keeps web page audio playing when the app is backgrounded; "背景音乐" means background music, not audio playback in the background.
- `Settings.Notifications.TipsAndFeaturesNotificationsTitle.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Tips and Features" is translated as only "使用技巧", dropping "Features".
    - Current: `使用技巧`
    - Suggest: `使用技巧与功能`
    - The source lists two items, tips and features; the target omits "Features", which the accompanying description string also references.
- `Settings.Notifications.TurnOnNotificationsMessage.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — Translation says go to the device setting item named %@ instead of going to device Settings to turn on notifications for %@.
    - Current: `前往设备设置中的“%@”开启通知`
    - Suggest: `前往设备的“设置”，开启 %@ 的通知`
    - In en-US %@ is the app name and the user should open the device Settings to enable notifications for the app; the Chinese reads as if %@ were a section of device settings.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `Shared/Supporting Files/en.lproj/Settings.strings` — "suggestions" is rendered as "结果" (results) instead of "建议".
    - Current: `在隐私浏览中显示来自 Firefox 建议的结果`
    - Suggest: `在隐私浏览中显示来自 Firefox 建议的建议`
    - The source says "Show suggestions from Firefox Suggest in private sessions"; the translation says "results" rather than "suggestions", inconsistent with the parallel string Settings.Search.PrivateSession.Description.v125 which uses 建议.
- `Settings.Translation.AutoTranslate.Footer.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "top preferred language" is rendered as "最熟悉的语言" (most familiar language) instead of the top item in the preferred-languages list.
    - Current: `自动将页面翻译成您最熟悉的语言。`
    - Suggest: `自动将页面翻译成您的首选语言（列表中的第一种语言）。`
    - The source refers to the user's top-ranked preferred language configured in the Preferred Languages list (translated elsewhere as 首选语言), not to which language the user knows best.
- `Settings.Translation.PreferredLanguages.Footer.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — The footer reverses the agent: the app chooses from these languages when translating, but the translation implies a passive/unspecified selection process.
    - Current: `翻译时将从这些语言中选择。`
    - Suggest: `翻译时可从这些语言中选择。`
    - "Choose from these languages when translating" instructs the user that these languages will be available as choices; "将从这些语言中选择" states the system will pick one automatically.
- `SendTo.NoDevicesFound.Message.v119` — `Shared/Supporting Files/en.lproj/Share.strings` — The translation drops "connected to this account" nuance and says devices are not in the account rather than no other devices are connected.
    - Current: `您的账户中没有其他设备可供同步。`
    - Suggest: `您没有其他连接到此账户的设备可供同步。`
    - en-US: "You don’t have any other devices connected to this account available to sync."
- `TabsButton.Accessibility.LargeContentTitle.v122` — `Shared/Supporting Files/en.lproj/TabLocation.strings` — "Show Tabs: %@" is rendered as "显示的标签页" (the tabs that are shown) instead of the imperative action "显示标签页".
    - Current: `显示的标签页：%@`
    - Suggest: `显示标签页：%@`
    - The source is a button action title "Show Tabs"; adding 的 turns it into a noun phrase meaning "the displayed tabs", changing the meaning.
- `TabTrayCloseTabsOlderThanTitle.v140` — `Shared/Supporting Files/en.lproj/TabsTray.strings` — The ellipsis at the end of "Close tabs older than…" is dropped in the translation.
    - Current: `关闭早于特定时间的标签页`
    - Suggest: `关闭早于以下时间的标签页…`
    - The source ends with an ellipsis indicating a submenu/further choice; the translation omits it, unlike the sibling string TabTrayCloseOldTabsTitle which keeps it.
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `Shared/Supporting Files/en.lproj/ZoomPageBar.strings` — "放大缩放比例" is an incorrect collocation and inconsistent with the paired "减小缩放比例".
    - Current: `放大缩放比例`
    - Suggest: `增大缩放比例`
    - The source pair is Increase/Decrease Zoom Level; the decrease string uses 减小缩放比例, so the increase string should use 增大缩放比例. 放大…比例 is not a valid verb-object pairing.
- `Closing tab` — `Shared/en.lproj/Localizable.strings` — Progressive "Closing tab" rendered as the imperative/label "关闭标签页".
    - Current: `关闭标签页`
    - Suggest: `正在关闭标签页`
    - The developer comment says this notifies the user that the tab is being closed; the Chinese lacks the in-progress aspect and reads as the action label "Close tab".
- `ContextualHints.TabTray.InactiveTabs` — `Shared/en.lproj/Localizable.strings` — Translation reverses the meaning: source says tabs not viewed for two weeks, target says tabs not viewed within two weeks (which reads as under two weeks).
    - Current: `两周内未查看的标签页将移至此处。`
    - Suggest: `超过两周未查看的标签页将移至此处。`
    - en-US "Tabs you haven’t viewed for two weeks" means tabs untouched for two weeks or longer; "两周内未查看" states the opposite timeframe.
- `CoverSheet.v24.ETP.Description` — `Shared/en.lproj/Localizable.strings` — The item "ads" is dropped from the list of blocked content.
    - Current: `则可拦截更多跟踪器和弹窗`
    - Suggest: `则可拦截更多跟踪器、广告和弹窗`
    - Source lists "trackers, ads, and popups"; the translation omits "ads".
- `Dark` — `Shared/en.lproj/Localizable.strings` — Reading View dark theme setting is rendered as "深邃" instead of the standard "深色".
    - Current: `深邃`
    - Suggest: `深色`
    - "Dark" as a theme setting is consistently "深色" in Firefox zh-CN; "深邃" means "profound/deep" and is not a theme name.
- `Downloads.CancelDialog.Resume` — `Shared/en.lproj/Localizable.strings` — "Resume" is translated as "继续" which loses the resume-download meaning in this cancel dialog.
    - Current: `继续`
    - Suggest: `继续下载`
    - The button declines cancellation and resumes the download; "继续" alone is ambiguous next to "取消", the source is "Resume".
- `FirefoxHome.Stories.Minutes.v140` — `Shared/en.lproj/Localizable.strings` — The abbreviation required by the developer comment is not used; "分钟" is the full form and the source's "min:" label pattern is dropped.
    - Current: `%d 分钟`
    - Suggest: `%d 分钟阅读`
    - Developer comment states minutes should be abbreviated due to space constraints; the source is "min: %d". Chinese has no shorter form, but the label meaning "minutes to read" is lost — at minimum the reading context should be preserved compactly.
- `FirefoxHomepage.ContextualMenu.SponsoredContent.v101` — `Shared/en.lproj/Localizable.strings` — Full-width ampersand "＆" used instead of the conventional Chinese connector.
    - Current: `我们的赞助商＆您的隐私`
    - Suggest: `我们的赞助商与您的隐私`
    - zh-CN typography does not use a full-width ampersand as a conjunction; compare FxA.ManageAccount which renders "&" as "和".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `Shared/en.lproj/Localizable.strings` — "Tab pickup" is rendered as "接收标签页" (receive tabs), which misses the feature name meaning of resuming a tab from another device.
    - Current: `接收标签页`
    - Suggest: `标签页接力`
    - "Tab pickup" is the feature that lets you pick up a synced tab from another device; "接收标签页" reads as an action of receiving tabs rather than the section label.
- `Menu.RemovedFromShortcuts.v99` — `Shared/en.lproj/Localizable.strings` — "Remove from Shortcuts" is translated as "移除快捷方式" (remove the shortcut) rather than removing the site from the Shortcuts list.
    - Current: `移除快捷方式`
    - Suggest: `从快捷方式中移除`
    - The source means removing the current website from the Shortcuts section on the home page; the related toast Menu.RemovePin.Confirm2.v99 correctly uses "已从快捷方式移除". "移除快捷方式" reads as deleting a shortcut object and is inconsistent.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `Shared/en.lproj/Localizable.strings` — "Fingerprinters" is rendered as 数字指纹跟踪程序 here but 数字指纹追踪程序 in the description string on the same feature screen.
    - Current: `数字指纹跟踪程序`
    - Suggest: `数字指纹追踪程序`
    - Menu.TrackingProtectionDescription.Fingerprinters uses 数字指纹追踪程序 for the same source term; the two should match within the same tracking-protection screen.
- `OpenURL.Error.Message` — `Shared/en.lproj/Localizable.strings` — Missing space between the Chinese text and the Latin brand name "Firefox".
    - Current: `地址无效，因此Firefox 无法打开该页面。`
    - Suggest: `地址无效，因此 Firefox 无法打开该页面。`
    - zh-CN convention (and the rest of this file, e.g. "啊哦！Firefox 崩溃了") inserts a space between CJK characters and Latin words; here "因此Firefox" lacks it while the following space is present.
- `SentTab_TabArrivingNotification_WithDevice_body` — `Shared/en.lproj/Localizable.strings` — Body string mis-renders "arrived in %@" (the app name) as the app receiving nothing meaningful/ambiguous direction.
    - Current: `%@ 收到了新的标签页`
    - Suggest: `新标签页已送达 %@`
    - The comment says %@ is the app name; "New tab arrived in %@" means the tab arrived in the app, not that the app name device received it — combined with the title string the direction is confusing/wrong.
- `SentTab_TabArrivingNotification_WithDevice_title` — `Shared/en.lproj/Localizable.strings` — Translation reverses the direction: source says the tab was received from the named device, but the Chinese says the device received the tab.
    - Current: `%@ 收到新的标签页`
    - Suggest: `收到来自 %@ 的标签页`
    - en-US "Tab received from %@" where %@ is the sending device name; the target makes %@ the receiver.
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `Shared/en.lproj/Localizable.strings` — "Sponsored Shortcuts" is rendered as "赞助商网站" (sponsored websites) instead of sponsored shortcuts.
    - Current: `赞助商网站`
    - Suggest: `赞助商快捷方式`
    - The source term is "Shortcuts", translated elsewhere in the same screen as "快捷方式"; "网站" (websites) is a different term and breaks consistency with the other shortcuts strings.
- `Settings.OfferClipboardBar.Status.v128` — `Shared/en.lproj/Localizable.strings` — Translation adds "询问" (ask/offer), which is not in the source "When opening %@".
    - Current: `打开 %@ 时询问`
    - Suggest: `打开 %@ 时`
    - The source is only "When opening %@", matching the earlier variant "当打开 Firefox 时"; adding "询问" introduces content not present in the source.
- `Settings.Passwords.OnboardingMessage.v103` — `Shared/en.lproj/Localizable.strings` — Missing space between "触控 ID" and "或" pattern — actually missing space in "触控 ID或设备密码".
    - Current: `触控 ID或设备密码`
    - Suggest: `触控 ID 或设备密码`
    - Latin text "ID" must be separated from the following Chinese character with a space, as done elsewhere in the same string ("面容 ID、").
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `Shared/en.lproj/Localizable.strings` — The translation reverses the time condition: source says tabs not viewed FOR two weeks, translation says tabs not viewed WITHIN two weeks.
    - Current: `两周内未查看的标签页将进入休眠状态。`
    - Suggest: `超过两周未查看的标签页将移至休眠标签页区域。`
    - "Tabs you haven’t viewed for two weeks" means tabs untouched for at least two weeks; 两周内未查看 literally reads as "not viewed within two weeks" which is ambiguous/reversed, and the mention of moving to the inactive section is lost.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `Shared/en.lproj/Localizable.strings` — The translation drops "ads" from the list of blocked items.
    - Current: `拦截更多跟踪器和弹窗。`
    - Suggest: `拦截更多跟踪器、广告和弹窗。`
    - The source says "Blocks more trackers, ads, and popups." — "ads" (广告) is missing in the Chinese text.
- `TopSites.RemovePage.Button` — `Shared/en.lproj/Localizable.strings` — Em dash from the source replaced with a hyphen.
    - Current: `移除页面 - %@`
    - Suggest: `移除页面 — %@`
    - Source uses an em dash separator; the translation uses a plain hyphen.
- `TranslationToastHandler.PromptTranslate.Title` — `Shared/en.lproj/Localizable.strings` — "This page appears to be in %1$@" is mistranslated as "此页面以 %1$@ 显示" (this page is displayed in %1$@), losing the "appears to be" hedge and the language sense.
    - Current: `此页面以 %1$@ 显示`
    - Suggest: `此页面似乎使用 %1$@ 撰写`
    - The source says the page appears to be in a given language; the translation states it is displayed in it, dropping the uncertainty.
- `Use stage servers` — `Shared/en.lproj/Localizable.strings` — Half-width parentheses used without spacing around Latin text in Chinese sentence.
    - Current: `使用预发布(Stage)服务器`
    - Suggest: `使用预发布（Stage）服务器`
    - zh-CN typography requires full-width parentheses within Chinese text.
- `You don’t have any tabs open in Firefox on your other devices.` — `Shared/en.lproj/Localizable.strings` — Awkward/ungrammatical rendering with redundant 已经 makes the sentence read incorrectly.
    - Current: `您没有在其他设备的 Firefox 上已经打开的标签页。`
    - Suggest: `您的其他设备上的 Firefox 没有打开任何标签页。`
    - The source states no tabs are open in Firefox on the user's other devices; the Chinese word order with 已经 is ungrammatical.
- `Menu.SharePageAction.Title` — `Shared/en.lproj/Menu.strings` — "Share Page With…" is rendered without the "With" sense; it should indicate sharing with someone/an app.
    - Current: `分享页面…`
    - Suggest: `分享页面给…`
    - The en-US source is "Share Page With…", indicating sharing with a recipient/app; the translation drops "With".
- `Menu.ViewDekstopSiteAction.Title` — `Shared/en.lproj/Menu.strings` — "Request Desktop Site" is translated as 要求 while the parallel mobile string uses 请求, an inconsistency on the same menu.
    - Current: `要求桌面版网站`
    - Suggest: `请求桌面版网站`
    - Menu.ViewMobileSiteAction.Title renders the identical source verb "Request" as 请求; the same term should be consistent within the same menu.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en.lproj/PrivateBrowsing.strings` — "any of your history or cookies" is translated as 历史记录和 Cookie, weakening the negation coverage.
    - Current: `不会记住您的历史记录和 Cookie`
    - Suggest: `不会记住您的任何历史记录或 Cookie`
    - The source negates both items individually ("any … or …"); 和 in Chinese negation can be read as excluding only the combination.
- `When Leaving Private Browsing` — `Shared/en.lproj/PrivateBrowsing.strings` — Translation adds "关闭" (close), which is not in the source label.
    - Current: `离开隐私浏览时关闭`
    - Suggest: `离开隐私浏览时`
    - The source is only "When Leaving Private Browsing"; it is an option value under the 'Close Private Tabs' setting, so appending 关闭 duplicates the setting title and changes the string's content.
- `TodayWidget.MoreTabsLabel` — `Shared/en.lproj/Today.strings` — Redundant wording "还有另" in the more-tabs label.
    - Current: `+还有另 %d 个…`
    - Suggest: `+另有 %d 个…`
    - "还有" and "另" duplicate the same meaning; source is simply "+%d More…".
- `TodayWidget.TopSitesGalleryDescription` — `Shared/en.lproj/Today.strings` — Translation drops "recently visited" and turns the description into a quoted widget name.
    - Current: `添加“常用网站”快捷方式。`
    - Suggest: `为常用及最近访问的网站添加快捷方式。`
    - en-US says "Add shortcuts to frequently and recently visited sites." — the "recently visited" part is missing.

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,922 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 44 | **curly-double** |
| ellipsis | `char` 20 | **char** |
| fullwidth | `punctuation` 567 | **punctuation** |
| register | `informal` 1, `formal` 138 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (70)

> **Reads as a deliberate edit (6).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `ContextualHints.FeltDeletion.Body.v122` — `zh-CN/firefox-ios.xliff` — The translation reverses the sequence/meaning: the source says tapping starts a fresh private session by deleting history and cookies, while the Chinese says to delete data after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `点按此处开始全新的隐私浏览会话。删除您的历史记录、Cookie 等一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The added "浏览完毕后" (after you finish browsing) is not in the source and changes when deletion happens.
- `Onboarding.Customization.Toolbar.Description.v123` — `zh-CN/firefox-ios.xliff` — "Keep searches within reach" is rendered as "holding the phone lightly can invoke search", which is not what the source says.
    - Current: `轻松握持就可唤起搜索。`
    - Source: `Keep searches within reach.`
    - Suggest: `让搜索始终触手可及。`
    - The en-US means the search bar stays easy to reach; the Chinese asserts that merely holding the device invokes search, which is a different (and false) behaviour claim.
- `Onboarding.Welcome.Description.TreatementA.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", overstating the product's behaviour.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US only says the browser "helps stop companies" from tracking; the translation claims automatic blocking and restricts the subject to large companies.
- `Onboarding.Welcome.Description.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", adding a claim the source never makes.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US says the browser "helps stop companies"; the Chinese asserts it "automatically blocks" them, and narrows "companies" to "big companies".
- `Summarizer.Footnote.Label.v144` — `zh-CN/firefox-ios.xliff` — "Summarization can make errors" is rendered as "摘要内容可能存在错误", changing the claim from the process making errors to the content containing errors — acceptable in meaning but the label is a disclaimer about the summarizer.
    - Current: `请注意：摘要内容可能存在错误。`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `请注意：摘要功能可能出错。`
    - The source disclaims that the summarization process can make mistakes; the translation asserts the produced content contains errors.
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-CN/firefox-ios.xliff` — "helps stop" is rendered as an absolute "阻止", overstating the protection.
    - Current: `减少定向广告，并阻止广告商跟踪您的浏览。`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `减少定向广告，并帮助阻止广告商跟踪您的浏览。`
    - en-US says "helps stop advertisers from tracking"; the Chinese asserts the product stops tracking outright, a claim the source does not make.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 42 |
| 3 | Degraded language (grammar, spelling, terminology) | 23 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `zh-CN/firefox-ios.xliff` — Reversed direction: source says signing in grabs bookmarks FROM other synced devices, translation says the bookmarks can be used ON other devices.
    - Current: `登录后还可在其他同步的设备上使用这些书签。`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `登录后即可获取其他同步设备上的书签。`
    - en-US: "Sign in to grab bookmarks from other synced devices." The Chinese states the opposite data direction (using these bookmarks on other devices), inconsistent with the sibling string Root.Body which correctly says 从其他同步的设备上接收书签.
- `ContextualHints.FeltDeletion.Body.v122` — `zh-CN/firefox-ios.xliff` — The translation reverses the sequence/meaning: the source says tapping starts a fresh private session by deleting history and cookies, while the Chinese says to delete data after browsing.
    - Current: `点按此处新建隐私浏览，浏览完毕后轻松删除历史记录和 Cookie 等数据。`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `点按此处开始全新的隐私浏览会话。删除您的历史记录、Cookie 等一切数据。`
    - en-US: "Tap here to start a fresh private session. Delete your history, cookies — everything." The added "浏览完毕后" (after you finish browsing) is not in the source and changes when deletion happens.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `zh-CN/firefox-ios.xliff` — "Townland" (a rural land division, chiefly Irish) is rendered as 镇 (town), which is the term used for "Town"/"Township" elsewhere in the same file.
    - Current: `镇`
    - Source: `Townland`
    - Suggest: `乡村地区`
    - The developer comment specifies a townland is "a specific type of land division used in rural areas", distinct from 镇/乡镇 already used for Village or Township in Addresses.EditAddress.AutofillAddressVillageTownship.v129; using 镇 both mistranslates and creates a within-screen terminology clash.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `zh-CN/firefox-ios.xliff` — "Tracking content" is translated but the developer comment/label concerns analytics trackers; more importantly the unit counter is fine — the issue is the string renders "Tracking content" consistently, but count suffix ok
    - Current: `跟踪性内容：%@ 项`
    - Source: `Tracking content: %@`
    - Suggest: `跟踪性内容：%@`
    - The source has no measure word/unit after the number; adding 项 is acceptable style, however here it mismatches other entries — low value.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `zh-CN/firefox-ios.xliff` — The Pocket footer title reverses the meaning: the source says Pocket powers the section and is part of the Firefox family, but the target says the Firefox family product line provides Pocket in an odd merged sentence.
    - Current: `由 %2$@ 系列产品 - %1$@ 提供。`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `由 %1$@ 提供支持。%1$@ 是 %2$@ 产品家族的一员。`
    - en-US is two statements: "Powered by Pocket." and "Part of the Firefox family." The translation collapses them and mis-assigns the roles.
- `MainMenu.ToolsSection.AccessibilityLabels.LibraryOptions.v142` — `zh-CN/firefox-ios.xliff` — "Library" is rendered as 我的足迹 ("my footprints/trail") instead of the standard term 资料库.
    - Current: `我的足迹`
    - Source: `Library`
    - Suggest: `资料库`
    - The source is "Library", the accessibility label for the group containing Downloads, History, Passwords. 我的足迹 is not the Firefox term for Library and conveys a different concept (browsing traces).
- `NativeErrorPage.GenericError.Description.v134` — `zh-CN/firefox-ios.xliff` — "The owner of %@" is rendered as 管理员 (administrator) and the sentence attributes misconfiguration in a different way than the source.
    - Current: `%@ 的管理员未正确配置此网站`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `%@ 的所有者未正确设置此网站`
    - The en-US says "owner", not "administrator".
- `Onboarding.Customization.Intro.Title.v123` — `zh-CN/firefox-ios.xliff` — Adds "线上生活" (online life), which the source does not mention.
    - Current: `%@ 让您掌控线上生活`
    - Source: `%@ puts you in control`
    - Suggest: `%@ 让您掌控一切`
    - Source is simply "%@ puts you in control"; the translation narrows/expands it to controlling one's online life.
- `Onboarding.Customization.Toolbar.Description.v123` — `zh-CN/firefox-ios.xliff` — "Keep searches within reach" is rendered as "holding the phone lightly can invoke search", which is not what the source says.
    - Current: `轻松握持就可唤起搜索。`
    - Source: `Keep searches within reach.`
    - Suggest: `让搜索始终触手可及。`
    - The en-US means the search bar stays easy to reach; the Chinese asserts that merely holding the device invokes search, which is a different (and false) behaviour claim.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `zh-CN/firefox-ios.xliff` — "Browsing just got better" mistranslated as "纯粹带来更好的浏览体验", introducing "纯粹" which is not in the source.
    - Current: `纯粹带来更好的浏览体验。`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `浏览体验更上一层楼。`
    - The source simply states browsing just got better; "纯粹" (purely/simply) is an added and unsupported qualifier.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `zh-CN/firefox-ios.xliff` — "companies" rendered as "大公司" (big companies), adding a qualifier the source does not have.
    - Current: `自动阻止大公司窥探您的浏览活动`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `自动阻止各公司窥探您的点击行为`
    - The en-US says "companies", not "big companies"; the translation narrows/changes the claim about who is blocked.
- `Onboarding.Welcome.Description.TreatementA.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", overstating the product's behaviour.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US only says the browser "helps stop companies" from tracking; the translation claims automatic blocking and restricts the subject to large companies.
- `Onboarding.Welcome.Description.v120` — `zh-CN/firefox-ios.xliff` — "helps stop companies" rendered as "automatically blocks big corporations", adding a claim the source never makes.
    - Current: `会自动阻止大公司在网上偷偷跟踪您`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `有助于阻止公司在网上偷偷跟踪您`
    - The en-US says the browser "helps stop companies"; the Chinese asserts it "automatically blocks" them, and narrows "companies" to "big companies".
- `PasswordGenerator.PasswordReadoutPrefaceA11y.v132` — `zh-CN/firefox-ios.xliff` — "Generated password: %@" is rendered as a sentence "Password has been generated" instead of a noun label.
    - Current: `已生成密码：%@`
    - Source: `Generated password: %@`
    - Suggest: `生成的密码：%@`
    - The source is a noun-phrase prefix labelling the password that follows ("Generated password"), not a statement that a password was generated.
- `CreditCard.RememberCard.Header.v122` — `zh-CN/firefox-ios.xliff` — Adds "保存" (save) to "encrypts your card number", asserting behaviour the source does not state.
    - Current: `%@ 会将卡号加密保存。`
    - Source: `%@ encrypts your card number. Your security code won’t be saved.`
    - Suggest: `%@ 会加密您的卡号。`
    - The source only says the app encrypts the card number, not that it encrypts and saves it.
- `PrimaryButton.Label.v112` — `zh-CN/firefox-ios.xliff` — Action button "Take Survey" translated as the noun "Survey" instead of an action.
    - Current: `问卷调查`
    - Source: `Take Survey`
    - Suggest: `填写问卷`
    - The source is a call-to-action button label meaning the user will be taken to a survey; 问卷调查 is just the noun "survey" and loses the action.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `zh-CN/firefox-ios.xliff` — Translation adds "此链接" (this link), which the source does not state.
    - Current: `要允许 %@ 打开此链接吗？`
    - Source: `Allow %@ to open?`
    - Suggest: `要允许打开 %@ 吗？`
    - In the source, %@ is the app name and the prompt asks whether to allow the app to open; the added object "此链接" is not in the source.
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Message.v154` — `zh-CN/firefox-ios.xliff` — "Your voice" rendered as "您的声音" reads as the sound itself rather than voice input/recordings.
    - Current: `您的声音、问题和答案永远不会被存储。`
    - Source: `Your voice, questions, and answers are never stored.`
    - Suggest: `您的语音、问题和答案永远不会被存储。`
    - In the context of a Quick Answers voice feature, "voice" means voice input (语音); 声音 is generic sound.
- `Settings.Browsing.BackgroundAudio.Title.v156` — `zh-CN/firefox-ios.xliff` — "Background Audio" is translated as "背景音乐" (background music), which misstates the feature.
    - Current: `背景音乐`
    - Source: `Background Audio`
    - Suggest: `后台音频`
    - The comment says audio from web pages continues playing when the app is backgrounded; "背景音乐" means background music (a soundtrack), not audio playing in the background.
- `Settings.Notifications.TipsAndFeaturesNotificationsTitle.v112` — `zh-CN/firefox-ios.xliff` — "Tips and Features" is rendered only as "使用技巧", dropping "Features".
    - Current: `使用技巧`
    - Source: `Tips and Features`
    - Suggest: `使用技巧与功能`
    - The source title is "Tips and Features"; the translation omits "Features", and the accompanying description does mention features.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `zh-CN/firefox-ios.xliff` — "suggestions" is translated as "结果" (results) instead of "建议", inconsistent with the parallel string.
    - Current: `在隐私浏览中显示来自 Firefox 建议的结果`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `在隐私浏览中显示来自 Firefox 建议的建议`
    - Source says "Show suggestions from Firefox Suggest in private sessions"; the parallel string Settings.Search.PrivateSession.Description uses "建议" for suggestions.
- `Settings.Studies.Message.v136` — `zh-CN/firefox-ios.xliff` — "before they're released to everyone" is rendered as "not yet fully rolled out", losing the meaning of trying features early.
    - Current: `抢先体验尚未全面推出的功能和概念。`
    - Source: `Try out features and ideas before they’re released to everyone.`
    - Suggest: `在功能和想法向所有人推出之前抢先体验。`
    - The source says users try features and ideas before general release; the translation states the features have not been fully rolled out, a different assertion.
- `Settings.Translation.AutoTranslate.Footer.v151` — `zh-CN/firefox-ios.xliff` — "your top preferred language" is mistranslated as "the language you know best".
    - Current: `自动将页面翻译成您最熟悉的语言。`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `自动将页面翻译成您的首选语言。`
    - The source refers to the top entry in the user's Preferred Languages list (see Settings.Translation.PreferredLanguages.SectionTitle 首选语言), not the language the user is most familiar with.
- `ContextualHints.Summarize.Description.v142` — `zh-CN/firefox-ios.xliff` — "Touch and hold for Reader View" is rendered as "按住可进入阅读模式" which drops the standard Firefox term 阅读器视图; more importantly the sentence structure is fine but the term is wrong.
    - Current: `按住可进入阅读模式`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `长按可进入阅读器视图`
    - Firefox's established zh-CN term for "Reader View" is 阅读器视图, not 阅读模式.
- `Summarizer.Footnote.Label.v144` — `zh-CN/firefox-ios.xliff` — "Summarization can make errors" is rendered as "摘要内容可能存在错误", changing the claim from the process making errors to the content containing errors — acceptable in meaning but the label is a disclaimer about the summarizer.
    - Current: `请注意：摘要内容可能存在错误。`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `请注意：摘要功能可能出错。`
    - The source disclaims that the summarization process can make mistakes; the translation asserts the produced content contains errors.
- `TabsButton.Accessibility.LargeContentTitle.v122` — `zh-CN/firefox-ios.xliff` — "Show Tabs: %@" is rendered as "显示的标签页" (tabs that are shown) instead of an action label meaning "show tabs".
    - Current: `显示的标签页：%@`
    - Source: `Show Tabs: %@`
    - Suggest: `显示标签页：%@`
    - The source is an action title for the tabs button ("Show Tabs"), not a description of tabs being displayed; 显示的标签页 turns the verb into a noun modifier.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `zh-CN/firefox-ios.xliff` — "sheet" (UI bottom sheet) is translated as 表单 (form).
    - Current: `已打开使用条款表单`
    - Source: `Terms of Use sheet opened`
    - Suggest: `已打开使用条款面板`
    - In iOS UI, "sheet" is a modal panel, not a form; 表单 means an input form and misnames the element in a VoiceOver announcement.
- `TermsOfUse.TitleValue2.v147` — `zh-CN/firefox-ios.xliff` — "A note from %@" is rendered as "%@ 提醒您" (%@ reminds you), changing the meaning.
    - Current: `%@ 提醒您`
    - Source: `A note from %@`
    - Suggest: `来自 %@ 的说明`
    - The source is a title meaning a note/message from the app, not a reminder to the user.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `zh-CN/firefox-ios.xliff` — "ROUND OF 32" is rendered as 十六分之一决赛, which names the wrong stage.
    - Current: `十六分之一决赛`
    - Source: `ROUND OF 32`
    - Suggest: `三十二强赛`
    - Round of 32 is the stage with 32 teams (32强/1/16 finals is ambiguous). In Chinese football usage, ROUND OF 16 = 八分之一决赛 (as translated above) and ROUND OF 32 should be 三十二强赛/十六分之一决赛 — but with Round of 16 already mapped to 八分之一决赛, labelling this 十六分之一决赛 is internally consistent; however the widely used term for the 2026 World Cup stage is 三十二强赛.
- `Use your fingerprint to access Logins now.` — `zh-CN/firefox-ios.xliff` — "Use your fingerprint" mistranslated as "验证您的指纹" is fine, but "Enter passcode" string uses 密码 for passcode — see separate finding.
    - Current: `验证您的指纹以访问登录信息。`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `请使用您的指纹访问登录信息。`
    - Minor, but the source asks the user to use their fingerprint now; the rendering is acceptable. (skip)
- `Closing tab` — `zh-CN/firefox-ios.xliff` — Progressive "Closing tab" notification rendered as the imperative/plain "关闭标签页" (Close tab), losing the in-progress meaning.
    - Current: `关闭标签页`
    - Source: `Closing tab`
    - Suggest: `正在关闭标签页`
    - The developer comment says it notifies the user that the tab is being closed; the target reads as the action label "Close tab" rather than an ongoing process.
- `ContextualHints.TabTray.InactiveTabs` — `zh-CN/firefox-ios.xliff` — Reversed meaning: source says tabs not viewed FOR two weeks, target says tabs not viewed WITHIN two weeks get moved.
    - Current: `两周内未查看的标签页将移至此处。`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `超过两周未查看的标签页将移至此处。`
    - "Tabs you haven’t viewed for two weeks" means tabs untouched for at least two weeks; "两周内未查看" states a different (shorter/inverted) condition.
- `CoverSheet.v24.ETP.Description` — `zh-CN/firefox-ios.xliff` — The item "ads" is dropped from the list of things Strict mode blocks.
    - Current: `开启“严格”模式则可拦截更多跟踪器和弹窗。`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `开启“严格”模式则可拦截更多跟踪器、广告和弹窗。`
    - Source lists "more trackers, ads, and popups"; the translation omits "ads".
- `Dark` — `zh-CN/firefox-ios.xliff` — "Dark" theme rendered as 深邃 ("profound/deep") instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - This is the dark theme setting in reader mode; the established term is 深色.
- `ErrorPages.CertWarning.Description` — `zh-CN/firefox-ios.xliff` — "The owner of %@" is rendered as "管理员" (administrator) instead of "所有者/拥有者".
    - Current: `%@ 的管理员未正确配置网站。`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `%@ 的所有者未正确配置网站。`
    - en-US says "The owner of %@"; 管理员 means administrator, a different party.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `zh-CN/firefox-ios.xliff` — Translation drops the notion of disconnecting "from" Firefox Sync, reading as "a device has disconnected Firefox Sync".
    - Current: `一台设备已断开 Firefox 同步`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `一台设备已断开与 Firefox 同步的连接`
    - Source is "A device has disconnected from Firefox Sync"; the Chinese omits 与…的连接, making 同步 the object of 断开 rather than the service disconnected from.
- `Increase text size` — `zh-CN/firefox-ios.xliff` — "Increase text size" is rendered as "增大文字", dropping "size".
    - Current: `增大文字`
    - Source: `Increase text size`
    - Suggest: `增大文字大小`
    - The source refers to increasing the font size in reader mode display settings; 增大文字 alone omits 大小/字号.
- `Menu.AddPin.Confirm2` — `zh-CN/firefox-ios.xliff` — Toast says the shortcut itself was added rather than the item was added to Shortcuts.
    - Current: `快捷方式已添加`
    - Source: `Added to Shortcuts`
    - Suggest: `已添加到快捷方式`
    - en-US "Added to Shortcuts" and the comment state the item was added to the Shortcuts list; the translation reverses the relationship, matching neither the source nor the parallel string Menu.AddToReadingList.Confirm (已添加到阅读列表).
- `Menu.RemovedFromShortcuts.v99` — `zh-CN/firefox-ios.xliff` — "Remove from Shortcuts" is rendered as "移除快捷方式" (remove the shortcut(s)) instead of "从快捷方式移除".
    - Current: `移除快捷方式`
    - Source: `Remove from Shortcuts`
    - Suggest: `从快捷方式移除`
    - The source means removing the current site from the Shortcuts section; the related toast Menu.RemovePin.Confirm2.v99 correctly uses "已从快捷方式移除". "移除快捷方式" reads as deleting the Shortcuts feature/entry itself.
- `SentTab_TabArrivingNotification_WithDevice_body` — `zh-CN/firefox-ios.xliff` — The placeholder is the app name where the tab arrived, but the translation makes it the subject that received the tab.
    - Current: `%@ 收到了新的标签页`
    - Source: `New tab arrived in %@`
    - Suggest: `新标签页已送达 %@`
    - Source: "New tab arrived in %@" with %@ = app name; the tab arrives in the app, it is not the app/device receiving as an agent in a title sense. Also it duplicates the title string wording.
- `SentTab_TabArrivingNotification_WithDevice_title` — `zh-CN/firefox-ios.xliff` — "Tab received from %@" is rendered as "%@ received a new tab", reversing the direction of the transfer.
    - Current: `%@ 收到新的标签页`
    - Source: `Tab received from %@`
    - Suggest: `收到来自 %@ 的标签页`
    - The source says the tab was received FROM the named device; the translation says the named device received the tab.
- `Settings.DataManagement.SearchLabel` — `zh-CN/firefox-ios.xliff` — "Filter Sites" (an imperative placeholder in a search bar) rendered as the noun phrase 网站过滤.
    - Current: `网站过滤`
    - Source: `Filter Sites`
    - Suggest: `过滤网站`
    - The source is a verb phrase prompting the user to filter sites; 网站过滤 reads as the noun "site filtering".
- `Settings.Home.Option.Wallpaper.LimitedEdition.IndependentVoices.Description.v106` — `zh-CN/firefox-ios.xliff` — "Independent Voices" collection name mistranslated as "凡人之声" (voices of mortals).
    - Current: `全新“凡人之声”壁纸集。`
    - Source: `The new Independent Voices collection.`
    - Suggest: `全新“独立之声”壁纸集。`
    - The en-US collection name is "Independent Voices"; 凡人 means "mortals/ordinary people", not "independent".
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `zh-CN/firefox-ios.xliff` — "Sponsored Shortcuts" rendered as "赞助商网站" (sponsor websites), dropping the Shortcuts term used consistently elsewhere on the same screen.
    - Current: `赞助商网站`
    - Source: `Sponsored Shortcuts`
    - Suggest: `赞助商快捷方式`
    - Source is "Sponsored Shortcuts"; other strings on the same screen translate Shortcuts as 快捷方式, so 网站 (websites) is both a mistranslation and inconsistent.
- `Settings.NoImageModeBlockImages.Label.v99` — `zh-CN/firefox-ios.xliff` — "Block Images" rendered as "无图模式" (no-image mode) instead of the action label.
    - Current: `无图模式`
    - Source: `Block Images`
    - Suggest: `屏蔽图片`
    - The source label is "Block Images", the toggle action; "无图模式" names a mode not present in the source.
- `Settings.OfferClipboardBar.Status.v128` — `zh-CN/firefox-ios.xliff` — Translation adds "询问" (ask/prompt) which is not in the source "When opening %@".
    - Current: `打开 %@ 时询问`
    - Source: `When opening %@`
    - Suggest: `打开 %@ 时`
    - The source is just the status description "When opening %@"; the older variant Settings.OfferClipboardBar.Status is correctly rendered as "当打开 Firefox 时" without the added verb.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `zh-CN/firefox-ios.xliff` — The description reverses the timing condition and mistranslates "inactive section" as a sleep state.
    - Current: `两周内未查看的标签页将进入休眠状态。`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `超过两周未查看的标签页将被移至“不活跃”版块。`
    - en-US says tabs you haven't viewed FOR two weeks (i.e. for longer than two weeks) get moved to the inactive section; "两周内未查看" means "not viewed within two weeks" which is ambiguous/reversed, and "进入休眠状态" claims the tabs are suspended rather than moved to a separate section of the tab tray.
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-CN/firefox-ios.xliff` — "helps stop" is rendered as an absolute "阻止", overstating the protection.
    - Current: `减少定向广告，并阻止广告商跟踪您的浏览。`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `减少定向广告，并帮助阻止广告商跟踪您的浏览。`
    - en-US says "helps stop advertisers from tracking"; the Chinese asserts the product stops tracking outright, a claim the source does not make.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `zh-CN/firefox-ios.xliff` — "ads" is dropped from the list of blocked items.
    - Current: `拦截更多跟踪器和弹窗。`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `拦截更多跟踪器、广告和弹窗。`
    - The source lists "more trackers, ads, and popups"; the translation omits ads.
- `fxa.signin.qr-link-instruction` — `zh-CN/firefox-ios.xliff` — Instruction mistranslated: source says open Firefox and go to firefox.com/pair, translation says use Firefox to open firefox.com/pair, dropping the two-step meaning is acceptable but "在计算机上" omits "your" — main issue is the merged instruction
    - Current: `在计算机上使用 Firefox 打开 firefox.com/pair`
    - Source: `On your computer open Firefox and go to firefox.com/pair`
    - Suggest: `在您的计算机上打开 Firefox 并访问 firefox.com/pair`
    - The en-US instructs the user to open Firefox and then navigate to firefox.com/pair; the translation collapses this into using Firefox to open a URL, losing the explicit step of opening the browser.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `zh-CN/firefox-ios.xliff` — "any of your history or cookies" is rendered as "历史记录和 Cookie" (and), weakening the negation to "won't remember both".
    - Current: `Firefox 不会记住您的历史记录和 Cookie`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox 不会记住您的任何历史记录或 Cookie`
    - The en-US negates each item individually ("any of ... or ..."); "和" under negation in Chinese can be read as negating the combination rather than each item.
- `TodayWidget.TopSitesGalleryDescription` — `zh-CN/firefox-ios.xliff` — Translation drops "and recently visited" from "frequently and recently visited sites".
    - Current: `添加“常用网站”快捷方式。`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `添加常用和最近访问网站的快捷方式。`
    - The source describes shortcuts to frequently AND recently visited sites; the target only mentions frequently visited sites.

### C. Grammar, agreement & spelling

- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `zh-CN/firefox-ios.xliff` — Missing measure word/unit after the count placeholder in the footer text.
    - Current: `已拦截 %1$@ 跟踪器`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `已拦截 %1$@ 个跟踪器`
    - %1$@ is a number; Chinese requires a measure word (个/项) between the number and 跟踪器, as done in HeaderLabelAccessibilityLabel.
- `TermsOfUse.Description.v142` — `zh-CN/firefox-ios.xliff` — "制订" is a misspelling/wrong word choice for 制定 in "We've introduced".
    - Current: `我们制订了 %@ 使用条款`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `我们推出了 %@ 使用条款`
    - The source says the Terms of Use were introduced; 制订 (draft) is the wrong form here and misstates the action.
- `WebCompatReporter.SubOption.ImagesNotLoaded.v154` — `zh-CN/firefox-ios.xliff` — "Images not loaded" rendered as the ungrammatical "图像不加载" instead of "图像未加载".
    - Current: `图像不加载`
    - Source: `Images not loaded`
    - Suggest: `图像未加载`
    - The source describes a state (images failed to load); Chinese uses 未加载 for that, while 不加载 reads as "does not load (by choice)" and is unidiomatic.
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `zh-CN/firefox-ios.xliff` — 放大缩放比例 is an incorrect collocation and inconsistent with the paired 减小缩放比例.
    - Current: `放大缩放比例`
    - Source: `Increase Zoom Level`
    - Suggest: `增大缩放比例`
    - The counterpart string uses 减小缩放比例 for "Decrease Zoom Level"; "Increase Zoom Level" should use the matching 增大, since 放大…比例 is not a valid collocation.
- `You don’t have any tabs open in Firefox on your other devices.` — `zh-CN/firefox-ios.xliff` — Awkward/ungrammatical rendering of "You don't have any tabs open in Firefox on your other devices."
    - Current: `您没有在其他设备的 Firefox 上已经打开的标签页。`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `您的其他设备上的 Firefox 未打开任何标签页。`
    - The Chinese sentence structure "没有…已经打开的标签页" is ungrammatical/garbled; the source simply states no tabs are open in Firefox on other devices.
- `TodayWidget.MoreTabsLabel` — `zh-CN/firefox-ios.xliff` — "+还有另 %d 个…" is redundant/ungrammatical for "+%d More…".
    - Current: `+还有另 %d 个…`
    - Source: `+%d More…`
    - Suggest: `+另 %d 个…`
    - "还有" and "另" duplicate the same meaning; source is a compact widget label "+%d More…" and space is tight.

### D. Terminology, register & consistency

- `Biometry.Screen.UniversalAuthenticationReason.v122` — `zh-CN/firefox-ios.xliff` — Imperative prompt rendered as a restrictive statement ("only after authenticating can you access") instead of a request to authenticate.
    - Current: `进行身份验证后才能访问保存的密码和付款方式。`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `请验证身份后访问保存的密码和付款方式。`
    - The source "Authenticate to access your saved passwords and payment methods." is an instruction to the user, matching the sibling v115 string translated as 请验证身份后访问密码。; the current wording changes register and phrasing inconsistently within the same file.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `zh-CN/firefox-ios.xliff` — Register inconsistency: the informal 你们 is used in the same sentence that begins with the formal 您.
    - Current: `若您使用的是企业网络，那么你们的支持团队可能了解更多信息。`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `若您使用的是企业网络，贵单位的支持团队可能了解更多信息。`
    - zh-CN convention is the formal 您; mixing 您 and 你们 within one sentence violates the established form of address.
- `WebCompatReporter.Toast.ReportSent.v155` — `zh-CN/firefox-ios.xliff` — "Report" is translated as 反馈 here but as 报告 in the other Report strings on the same feature.
    - Current: `反馈已发送`
    - Source: `Report sent`
    - Suggest: `报告已发送`
    - WebCompatReporter.Preview.Title and SendButton.Title use 报告 for "Report"; using 反馈 in the confirmation toast is inconsistent within the same flow.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `zh-CN/firefox-ios.xliff` — Fingerprinters is rendered "数字指纹追踪程序" here but "数字指纹跟踪程序" in the related title string.
    - Current: `数字指纹追踪程序`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `数字指纹跟踪程序`
    - Menu.TrackingProtectionFingerprintersBlocked.Title on the same screen uses "数字指纹跟踪程序"; the term should be consistent.
- `Settings.DisplayTheme.OptionDark` — `zh-CN/firefox-ios.xliff` — "Dark" theme option translated as 深邃 ("deep/profound") instead of the standard 深色.
    - Current: `深邃`
    - Source: `Dark`
    - Suggest: `深色`
    - The source is the dark theme option; zh-CN uses 深色 consistently elsewhere in this file (e.g. 网站深色模式, 使用系统浅/深色模式). 深邃 means "profound/deep" and is not a theme term.
- `Settings.DisplayTheme.OptionLight` — `zh-CN/firefox-ios.xliff` — "Light" theme option translated as 明亮 instead of the standard 浅色.
    - Current: `明亮`
    - Source: `Light`
    - Suggest: `浅色`
    - Paired with the dark option; the file elsewhere uses 浅/深色模式. 明亮 ("bright") is inconsistent with the established theme terminology.
- `Menu.ViewDekstopSiteAction.Title` — `zh-CN/firefox-ios.xliff` — "Request Desktop Site" is rendered as 要求桌面版网站 while the parallel "Request Mobile Site" uses 请求移动版网站, an inconsistent rendering of the same verb on the same menu.
    - Current: `要求桌面版网站`
    - Source: `Request Desktop Site`
    - Suggest: `请求桌面版网站`
    - Same source verb "Request" in two adjacent menu items translated differently; 请求 is the established term used in the sibling string.

### E. Typography, punctuation & spacing

- `DefaultBrowserPopup.ThirdLabel.v114` — `zh-CN/firefox-ios.xliff` — Missing space after the list number, inconsistent with the first and second labels.
    - Current: `3.选择 *%@*`
    - Source: `3. Select *%@*`
    - Suggest: `3. 选择 *%@*`
    - Sibling strings use "1. 前往" and "2. 轻点" with a space after the numeral; this one omits it.
- `TabTrayCloseTabsOlderThanTitle.v140` — `zh-CN/firefox-ios.xliff` — The trailing ellipsis of the source menu title is dropped.
    - Current: `关闭早于特定时间的标签页`
    - Source: `Close tabs older than…`
    - Suggest: `关闭早于特定时间的标签页…`
    - Source is "Close tabs older than…" with an ellipsis indicating a submenu; the translation omits it, unlike the sibling string 关闭旧标签页….
- `FirefoxHomepage.ContextualMenu.SponsoredContent.v101` — `zh-CN/firefox-ios.xliff` — Uses fullwidth ampersand "＆" instead of the Chinese conjunction/standard punctuation.
    - Current: `我们的赞助商＆您的隐私`
    - Source: `Our Sponsors & Your Privacy`
    - Suggest: `我们的赞助商与您的隐私`
    - zh-CN convention renders "&" as 与/和; the fullwidth ampersand is not used elsewhere (e.g. FxA.ManageAccount uses 和).
- `OpenURL.Error.Message` — `zh-CN/firefox-ios.xliff` — Missing space between the Chinese text and the Latin brand name "Firefox".
    - Current: `地址无效，因此Firefox 无法打开该页面。`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `地址无效，因此 Firefox 无法打开该页面。`
    - The locale inserts a space between CJK text and Latin words, as done elsewhere in the same string ("Firefox 无法").
- `Settings.Passwords.OnboardingMessage.v103` — `zh-CN/firefox-ios.xliff` — Missing space/separator between "触控 ID" and "或设备密码".
    - Current: `面容 ID、触控 ID或设备密码保护`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `面容 ID、触控 ID 或设备密码保护`
    - Latin text "ID" abutting the following Chinese character without the spacing used elsewhere in the same sentence ("面容 ID、").

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
