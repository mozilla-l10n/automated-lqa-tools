# Firefox iOS l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-CN: [android](android.md) · [firefox](firefox.md)

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
| Files | 96 |
| Strings | 1,922 |
| Missing strings | 28 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**28 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings` — 22
- `zh-CN/firefox-ios.xliff` — 6

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

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

## 3. Open findings (69)

> **Reads as a deliberate edit (5).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

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
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-CN/firefox-ios.xliff` — "helps stop" is rendered as an absolute "阻止", overstating the protection.
    - Current: `减少定向广告，并阻止广告商跟踪您的浏览。`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `减少定向广告，并帮助阻止广告商跟踪您的浏览。`
    - en-US says "helps stop advertisers from tracking"; the Chinese asserts the product stops tracking outright, a claim the source does not make.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 41 |
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
