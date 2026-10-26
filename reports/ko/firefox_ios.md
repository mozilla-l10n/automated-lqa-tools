# Firefox iOS l10n QA — ko

| | |
|---|---|
| **Generated** | 2026-10-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **Previous run** | 2026-10-19 @ `ec61063c1c68` |
| **Mode** | incremental |
| **Strings reviewed this run** | 46 of 1,973 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ko: [android](android.md)

---

## Changes in this run

### 🆕 New findings (4)

- `VPN.ErrorBrowsingPopup.ClosedOneTab.v160` — `ko/firefox-ios.xliff` — The confirmation 'Closed 1 Tab' is translated as an action label ('Close 1 tab') instead of a completed action.
    - Current: `1개 탭 닫기`
    - Source: `Closed 1 Tab`
    - Suggest: `1개 탭 닫음`
    - Per the comment, this is a confirmation shown after the tab was closed. '닫기' reads as a button or command. The plural string uses '닫음', which is the correct past/result form.
- `VPN.Settings.DataUsage.AccessibilityLabel.v160` — `ko/firefox-ios.xliff` — The VoiceOver label keeps the abbreviation 'GB', but the comment requires the unit to be written out.
    - Current: `GB 사용함`
    - Source: `%1$@ of %2$@ gigabytes used`
    - Suggest: `기가바이트 사용함`
    - The developer comment says this label is the same as the visible text but with 'gigabytes' written out instead of 'GB'. The translation is identical to the visible string.
- `VPN.ReachedDataLimitPopup.ClosedOneTab.v160` — `ko/firefox-ios.xliff` — The confirmation "Closed 1 Tab" is written as the command "Close 1 tab" (the button-label ~기 form) instead of saying the tab has been closed.
    - Current: `1개 탭 닫기`
    - Source: `Closed 1 Tab`
    - Suggest: `탭 1개를 닫았습니다`
    - The developer comment says this is a confirmation shown after the tab was closed. "닫기" is the form Korean uses for action buttons, so it reads as an instruction to close a tab, not as a statement that one was closed.
- `VPN.ReachedDataLimitPopup.ClosedXTabs.v160` — `ko/firefox-ios.xliff` — The confirmation "Closed %1$@ Tabs" is written as the command "Close %1$@ tabs" instead of saying the tabs have been closed.
    - Current: `%1$@개 탭 닫기`
    - Source: `Closed %1$@ Tabs`
    - Suggest: `탭 %1$@개를 닫았습니다`
    - The developer comment says this is a confirmation shown after the tabs were closed. The ~기 form reads as a button that closes tabs, not as a past-tense confirmation.

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
| Files | 98 |
| Strings | 1,973 |
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
| quotes | `curly-single` 10, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 10 | **typographic** |
| ellipsis | `char` 31 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (97)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `ko/firefox-ios.xliff` — "and that you use it" is translated as "and how you use it", which claims usage behaviour is shared with marketing partners.
    - Current: `%1$@를 발견한 방법과 사용 방법을 공유하세요`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `%1$@를 발견한 방법과 %1$@를 사용한다는 사실을 공유하세요`
    - The source shares only the fact that the user uses the app. '사용 방법' (how you use it) says detailed usage data goes to marketing partners, a wider data share than the product describes.
- `CoverSheet.v24.ETP.Description` — `ko/firefox-ios.xliff` — "helps stop ads from following you" is rendered as an unconditional claim that protection prevents ads from tracking the user.
    - Current: `광고가 사용자를 추적하지 못하게합니다`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `광고가 사용자를 따라다니는 것을 막는 데 도움을 줍니다`
    - The source hedges with "helps stop". The Korean says the feature prevents ads from tracking you, which is a guarantee the product does not make.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 45 |
| 3 | Degraded language (grammar, spelling, terminology) | 52 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Alerts.AddToCalendar.Body.v134` — `ko/firefox-ios.xliff` — The Korean says the site adds the event to the calendar; the source says the site is asking to.
    - Current: `%@가 파일 다운로드를 요청하고 캘린더에 이벤트를 추가합니다.`
    - Source: `%@ is asking to download a file and add an event to your calendar.`
    - Suggest: `%@에서 파일을 다운로드하고 캘린더에 이벤트를 추가하려고 합니다.`
    - The en-US says the site is asking both to download a file and to add an event; this is a confirmation dialog. In the Korean, 요청 only covers the download, and '이벤트를 추가합니다' says the event is being added before the user agrees.
- `Alerts.AddToCalendar.BodyDefault.v134` — `ko/firefox-ios.xliff` — The Korean says the site adds the event to the calendar; the source says the site is asking to.
    - Current: `이 사이트가 파일 다운로드를 요청하고 캘린더에 이벤트를 추가합니다.`
    - Source: `This site is asking to download a file and add an event to your calendar.`
    - Suggest: `이 사이트에서 파일을 다운로드하고 캘린더에 이벤트를 추가하려고 합니다.`
    - The en-US says the site is asking both to download a file and to add an event, pending the user's confirmation. In the Korean, the request covers only the download, and the event is said to be added already.
- `Settings.AppIconSelection.AppIconNames.Pride.Title.v136` — `ko/firefox-ios.xliff` — The LGBT+ Pride icon name is translated as "자부심" (pride in the sense of self-esteem) instead of the term used for Pride.
    - Current: `자부심`
    - Source: `Pride`
    - Suggest: `프라이드`
    - The developer comment says this is the LGBT+ pride fox logo. In Korean, Pride in this sense is usually called 프라이드 (e.g. 퀴어 프라이드). 자부심 means personal self-esteem, so the icon name loses what it refers to.
- `ContextualHints.Translations.Body.v145` — `ko/firefox-ios.xliff` — 'private' translations rendered as 'safe' (안전한).
    - Current: `빠르고 안전한 번역`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `빠르고 비공개로 처리되는 번역`
    - The source claims privacy, i.e. translation happens privately. 안전한 means safe or secure, which is a different property.
- `Addresses.EditAddress.AutofillAddressCounty.v129` — `ko/firefox-ios.xliff` — 'County' translated as 주 (state/province) instead of a county-level term.
    - Current: `주`
    - Source: `County`
    - Suggest: `군`
    - A county is a sub-state division. 주 means state or province, which is a different administrative level.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `ko/firefox-ios.xliff` — Administrative 'Department' translated as an organizational department (부서).
    - Current: `부서`
    - Source: `Department`
    - Suggest: `도`
    - The comment says this is the administrative division used in France and Colombia. 부서 means a department in a company or office.
- `Addresses.EditAddress.AutofillAddressPin.v129` — `ko/firefox-ios.xliff` — "Pin" (India's Postal Index Number) is translated as "고정", the verb "pin/fix in place".
    - Current: `고정`
    - Source: `Pin`
    - Suggest: `PIN 코드`
    - The developer comment says this is the PIN (Postal Index Number) field used in India, which is a postal code. "고정" means pinning or fixing something in place, as in pinning a tab, so it labels the address field with an unrelated word.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `ko/firefox-ios.xliff` — "Tracking content" (a category of trackers) is rendered as "콘텐츠 추적", meaning the act of tracking content.
    - Current: `콘텐츠 추적`
    - Source: `Tracking content: %@`
    - Suggest: `추적 콘텐츠`
    - The label names a category of blocked items, "tracking content", as a noun phrase. "콘텐츠 추적" reads as "tracking of content", which is an action, not the tracker category.
- `MainMenu.ToolsSection.AccessibilityLabels.ExpandedHint.v142` — `ko/firefox-ios.xliff` — The 'Expanded' state hint is translated as the action 'Open' (열기) instead of a state.
    - Current: `열기`
    - Source: `Expanded`
    - Suggest: `펼쳐짐`
    - The comment says this hint is read out when the menu is expanded, so it describes a state. Its counterpart 'Collapsed' is correctly rendered as the state '접힘', but '열기' is an imperative action ('open'), which misleads VoiceOver users.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `ko/firefox-ios.xliff` — "Save submenu" is rendered as an action ("save the submenu") instead of naming the Save submenu.
    - Current: `하위 메뉴 저장`
    - Source: `Save submenu`
    - Suggest: `저장 하위 메뉴`
    - The comment says this label names the Save submenu. "하위 메뉴 저장" reads as "save the submenu". The parallel label for Tools is "도구 하위 메뉴".
- `MainMenu.ToolsSection.ReaderViewOff.Title.v150` — `ko/firefox-ios.xliff` — State label uses the action verb "끄기" (turn off) instead of the state "꺼짐" (off).
    - Current: `끄기`
    - Source: `Off`
    - Suggest: `꺼짐`
    - The comment says this label shows that Reader View is turned off, so it is a state, not a command. The Dark Mode labels in the same menu use "꺼짐".
- `MainMenu.ToolsSection.ReaderViewOn.Title.v150` — `ko/firefox-ios.xliff` — State label uses the action verb "켜기" (turn on) instead of the state "켜짐" (on).
    - Current: `켜기`
    - Source: `On`
    - Suggest: `켜짐`
    - The comment says this label shows that Reader View is turned on, so it is a state. The Dark Mode labels in the same menu use "켜짐".
- `MainMenu.ToolsSection.Translation.Off.v151` — `ko/firefox-ios.xliff` — Badge showing that translation is inactive uses the action verb "끄기" instead of the state "꺼짐".
    - Current: `끄기`
    - Source: `Off`
    - Suggest: `꺼짐`
    - The comment says this badge is shown when translation is inactive, so it is a state, not a command to turn translation off.
- `NativeErrorPage.BadCertDomain.AdvancedWarning1.v149` — `ko/firefox-ios.xliff` — The hedge "might" is dropped, so a possible fix becomes a definite requirement.
    - Current: `Wi-Fi 네트워크에 로그인해야 하거나 VPN 설정을 확인해야 합니다.`
    - Source: `You might need to sign in to your Wi-Fi network, or check your VPN settings.`
    - Suggest: `Wi-Fi 네트워크에 로그인하거나 VPN 설정을 확인해야 할 수도 있습니다.`
    - The source says the user 'might need to' do these things, offering them as possible solutions. The Korean says they must.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `ko/firefox-ios.xliff` — "Try connecting on a different device" is rendered as "try connecting to a different device".
    - Current: `다른 기기에 연결해 보세요.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `다른 기기에서 연결해 보세요.`
    - The source tells the user to try the connection from another device. '기기에 연결' means connecting to another device, which is a different instruction.
- `NativeErrorPage.Wayback.Error.Description.v154` — `ko/firefox-ios.xliff` — The hedge "may be" is missing, so a possible cause of the error reads as a confirmed one.
    - Current: `서버가 바쁘거나 사용할 수 없습니다.`
    - Source: `The site may be busy or unavailable. Try again later. If other pages won’t load, check your Wi-Fi or data connection. %@ can also search the Wayback Machine for an earlier version of this page.`
    - Suggest: `사이트가 바쁘거나 사용할 수 없는 것 같습니다.`
    - The source says "The site may be busy or unavailable", which is only a guess. The Korean states as fact that the server is busy or unavailable, which the app can't know.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `ko/firefox-ios.xliff` — "have %@ match your device" is translated as "connect %@ to your device" instead of having the theme follow the device setting.
    - Current: `기기에 %@를 연결하여`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `%@가 기기 테마를 따르도록 하여`
    - The source means letting the app follow the device's system theme. '연결하여' means connecting or linking the app to the device, which is a different action.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `ko/firefox-ios.xliff` — "and that you use it" is translated as "and how you use it", which claims usage behaviour is shared with marketing partners.
    - Current: `%1$@를 발견한 방법과 사용 방법을 공유하세요`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `%1$@를 발견한 방법과 %1$@를 사용한다는 사실을 공유하세요`
    - The source shares only the fact that the user uses the app. '사용 방법' (how you use it) says detailed usage data goes to marketing partners, a wider data share than the product describes.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `ko/firefox-ios.xliff` — "have %@ match your device" is translated as "connect %@ to your device" instead of having the theme follow the device setting.
    - Current: `기기에 %@를 연결하여`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `%@가 기기 테마를 따르도록 하여`
    - The source means letting the app follow the device's system theme. '연결하여' means connecting or linking the app to the device, which is a different action.
- `Onboarding.Welcome.Title.v114` — `ko/firefox-ios.xliff` — "Independent internet" is rendered as "나만의 인터넷" (your own internet), which changes the meaning.
    - Current: `나만의 인터넷에 오신 것을 환영합니다`
    - Source: `Welcome to an independent internet`
    - Suggest: `독립적인 인터넷에 오신 것을 환영합니다`
    - The source says "Welcome to an independent internet". "나만의" means "my own/personal", not "independent".
- `QuickAnswers.ContentView.Listening.v158` — `ko/firefox-ios.xliff` — "Listening" is dropped, so this string is identical to the idle placeholder and no longer shows that the microphone is active.
    - Current: `무엇이든 물어보세요…`
    - Source: `Listening, ask anything…`
    - Suggest: `듣고 있습니다. 무엇이든 물어보세요…`
    - The developer comment says this text appears while the microphone is active. The source's "Listening" is the only thing that sets it apart from the "Ask anything…" placeholder, and the Korean leaves it out.
- `QuickAnswers.ReturnPill.Subtitle.v158` — `ko/firefox-ios.xliff` — "탭으로 돌아가기" reads as "Return to the tab" instead of "Tap to return".
    - Current: `탭으로 돌아가기`
    - Source: `Tap to return`
    - Suggest: `눌러서 돌아가기`
    - The source means tapping the pill returns to the answer. In Korean, 탭 + 으로 + 돌아가기 is naturally read as "go back to the tab" (탭 = tab), which changes the meaning.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `ko/firefox-ios.xliff` — The translation asks to allow opening "the %@ address", but %@ is the app name.
    - Current: `%@ 주소를 열도록 허용하시겠습니까?`
    - Source: `Allow %@ to open?`
    - Suggest: `%@에서 열도록 허용하시겠습니까?`
    - Per the comment, %@ is the app name (Firefox). The Korean says "Allow opening the Firefox address?", which misreads the placeholder. The source asks whether to allow the app to open the URL.
- `QuickAnswers.Settings.StatusOff.v158` — `ko/firefox-ios.xliff` — Status label 'Off' is rendered as the action verb '끄기' (turn off) instead of a state.
    - Current: `끄기`
    - Source: `Off`
    - Suggest: `끔`
    - The comment says this is status text shown when the feature is disabled. '끄기' means 'turning off' (an action), not the state 'off'.
- `QuickAnswers.Settings.StatusOn.v158` — `ko/firefox-ios.xliff` — Status label 'On' is rendered as the action verb '켜기' (turn on) instead of a state.
    - Current: `켜기`
    - Source: `On`
    - Suggest: `켬`
    - The comment says this is status text shown when the feature is enabled. '켜기' means 'turning on' (an action/button label), not the state 'on'.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `ko/firefox-ios.xliff` — The counter '개' is attached to %1$@, which holds the app name, not a number.
    - Current: `모든 %1$@개의 알림을 껐습니다.`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `%1$@ 알림을 모두 껐습니다.`
    - The developer comment says %1$@ is the app name (e.g. Firefox), so the text renders as '모든 Firefox개의 알림', which treats the name as a count.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `ko/firefox-ios.xliff` — The title reads as 'scroll toward hiding tab and address bar' instead of 'scroll to hide the tab and address bar'.
    - Current: `탭과 주소 표시줄 숨기기로 스크롤`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `스크롤하여 탭과 주소 표시줄 숨기기`
    - In the source, 'to' marks purpose: scrolling hides the bars. '~로 스크롤' makes 'hiding' the destination of the scroll, which garbles the setting's meaning.
- `Settings.Studies.Title.v148` — `ko/firefox-ios.xliff` — The word order is reversed, so the label reads as "allow the research feature" instead of "allow feature studies".
    - Current: `연구 기능 허용`
    - Source: `Allow Feature Studies`
    - Suggest: `기능 연구 허용`
    - The source means studies of features. "연구 기능" means a feature for research.
- `Settings.Summarize.FooterTitle.v142` — `ko/firefox-ios.xliff` — "요약 페이지" reads as "summary page" when the source means the ability to summarize pages.
    - Current: `요약 페이지에 대한 접근을 제공합니다.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `페이지 요약 기능을 제공합니다.`
    - The source means the setting lets you summarize web pages. It does not mean access to a page of summaries.
- `SentFromFirefox.SocialShare.SettingsToggle.Title.v134` — `ko/firefox-ios.xliff` — The English word "Shares" was left untranslated.
    - Current: `%2$@ Shares에`
    - Source: `Include %1$@ Download Link on %2$@ Shares`
    - Suggest: `%2$@ 공유에`
    - "Shares" is an ordinary word meaning shared links, not a brand name, so it should be translated into Korean.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `ko/firefox-ios.xliff` — "Sent from" is attached to the download link (%3$@) instead of the app name (%2$@).
    - Current: `%2$@ 🦊 %3$@에서 보냄`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@에서 보냄 🦊 %3$@`
    - The source says the link was sent from the app (%2$@) and then gives the download link (%3$@). The Korean puts 에서 보냄 after %3$@, so it reads 'sent from <download link>'. It also does not match the v134 version of this string, which is correct.
- `TermsOfUse.LearnMoreHere.v147` — `ko/firefox-ios.xliff` — With %@ = '여기', the Korean reads 'You can learn more about here' instead of 'You can learn more here'.
    - Current: `%@에 대해 더 알아볼 수 있습니다.`
    - Source: `You can learn more %@.`
    - Suggest: `%@에서 더 알아볼 수 있습니다.`
    - The source means learn more at the 'here' link; '에 대해' (about) is the wrong particle for the link text '여기' and makes the sentence nonsensical.
- `VPN.ErrorBrowsingPopup.ClosedOneTab.v160` — `ko/firefox-ios.xliff` — The confirmation 'Closed 1 Tab' is translated as an action label ('Close 1 tab') instead of a completed action.
    - Current: `1개 탭 닫기`
    - Source: `Closed 1 Tab`
    - Suggest: `1개 탭 닫음`
    - Per the comment, this is a confirmation shown after the tab was closed. '닫기' reads as a button or command. The plural string uses '닫음', which is the correct past/result form.
- `VPN.ReachedDataLimitPopup.ClosedOneTab.v160` — `ko/firefox-ios.xliff` — The confirmation "Closed 1 Tab" is written as the command "Close 1 tab" (the button-label ~기 form) instead of saying the tab has been closed.
    - Current: `1개 탭 닫기`
    - Source: `Closed 1 Tab`
    - Suggest: `탭 1개를 닫았습니다`
    - The developer comment says this is a confirmation shown after the tab was closed. "닫기" is the form Korean uses for action buttons, so it reads as an instruction to close a tab, not as a statement that one was closed.
- `VPN.ReachedDataLimitPopup.ClosedXTabs.v160` — `ko/firefox-ios.xliff` — The confirmation "Closed %1$@ Tabs" is written as the command "Close %1$@ tabs" instead of saying the tabs have been closed.
    - Current: `%1$@개 탭 닫기`
    - Source: `Closed %1$@ Tabs`
    - Suggest: `탭 %1$@개를 닫았습니다`
    - The developer comment says this is a confirmation shown after the tabs were closed. The ~기 form reads as a button that closes tabs, not as a past-tense confirmation.
- `Next in-page result` — `ko/firefox-ios.xliff` — "다음 페이지 결과" reads as "results of the next page" rather than "next result within the page".
    - Current: `다음 페이지 결과`
    - Source: `Next in-page result`
    - Suggest: `페이지 내 다음 결과`
    - The accessibility label is for the button that moves to the next match on the current page; the Korean suggests navigating to a next page.
- `Previous in-page result` — `ko/firefox-ios.xliff` — "이전 페이지 결과" reads as "results of the previous page" rather than "previous result within the page".
    - Current: `이전 페이지 결과`
    - Source: `Previous in-page result`
    - Suggest: `페이지 내 이전 결과`
    - The accessibility label is for the button that moves to the previous match on the current page; the Korean suggests a previous page.
- `ContextMenu.ButtonToast.NewTabOpened.ButtonText` — `ko/firefox-ios.xliff` — The button verb "Switch" (switch to the new tab) is transliterated as the noun "스위치" (a hardware switch).
    - Current: `스위치`
    - Source: `Switch`
    - Suggest: `전환`
    - The developer comment says the button switches to the newly opened tab. "스위치" is a noun meaning a physical switch, not the action.
- `ContextMenu.DownloadLinkButtonTitle` — `ko/firefox-ios.xliff` — The context menu action "Download Link" is rendered as the noun phrase "download link" instead of the action "download the link".
    - Current: `다운로드 링크`
    - Source: `Download Link`
    - Suggest: `링크 다운로드`
    - This is a menu action for downloading a link URL. The sibling items use the object+verb pattern (e.g. 링크 복사, 이미지 저장), while "다운로드 링크" reads as "a download link".
- `CoverSheet.v24.ETP.Description` — `ko/firefox-ios.xliff` — "helps stop ads from following you" is rendered as an unconditional claim that protection prevents ads from tracking the user.
    - Current: `광고가 사용자를 추적하지 못하게합니다`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `광고가 사용자를 따라다니는 것을 막는 데 도움을 줍니다`
    - The source hedges with "helps stop". The Korean says the feature prevents ads from tracking you, which is a guarantee the product does not make.
- `FxAPush_DeviceDisconnected_ThisDevice_body` — `ko/firefox-ios.xliff` — "This device" is rendered as just "기기는" (the device), dropping "이" (this), so the notification no longer says it is the current device that was disconnected.
    - Current: `기기는 Firefox Sync와 연결이 끊어졌습니다.`
    - Source: `This device has been successfully disconnected from Firefox Sync.`
    - Suggest: `이 기기는 Firefox Sync와 연결이 성공적으로 끊어졌습니다.`
    - The source and comment say this device was disconnected by another device. Without "이", the Korean names no device, which is ambiguous.
- `Menu.RemoveReadingList.Confirm.v99` — `ko/firefox-ios.xliff` — The confirmation toast reads as the action "Remove from Reading List" instead of "Removed".
    - Current: `읽기 목록에서 제거`
    - Source: `Removed from Reading List`
    - Suggest: `읽기 목록에서 제거됨`
    - The developer comment says this toast confirms the item was removed. The other toasts in this file use the completed form -됨 (바로 가기에서 제거됨, 북마크 제거됨).
- `Menu.TrackingProtectionDescription.CryptominersNew` — `ko/firefox-ios.xliff` — "Cryptomining scripts" is translated as "암호 해독 스크립트" (decryption scripts).
    - Current: `암호 해독 스크립트는`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `암호화폐 채굴 스크립트는`
    - The source means scripts that mine cryptocurrency. 암호 해독 means decryption, which is a different thing and doesn't match the 암호화폐 채굴기 used just before it.
- `Open Tabs` — `ko/firefox-ios.xliff` — "Open Tabs" names the synced tabs, but the translation turns it into the action "open tabs".
    - Current: `탭 열기`
    - Source: `Open Tabs`
    - Suggest: `열린 탭`
    - The developer comment says this is the toggle for syncing tabs, so "Open Tabs" is a noun phrase meaning tabs that are open. 탭 열기 reads as an instruction to open tabs.
- `Settings.Home.Option.StartAtHome.AfterFourHours` — `ko/firefox-ios.xliff` — The Korean says "a homepage that has had no activity for 4 hours" instead of "the homepage, after 4 hours of inactivity".
    - Current: `4시간 동안 활동이 없는 홈페이지`
    - Source: `Homepage after four hours of inactivity`
    - Suggest: `4시간 동안 활동이 없으면 홈페이지`
    - The comment says this option returns the user to the homepage after four hours of inactivity. The relative clause '없는' makes the inactivity describe the homepage itself, so the condition is lost.
- `Settings.OfferClipboardBar.Status` — `ko/firefox-ios.xliff` — The brand name Firefox is transliterated into Hangul instead of being kept as is.
    - Current: `파이어 폭스를 열 때`
    - Source: `When Opening Firefox`
    - Suggest: `Firefox를 열 때`
    - Firefox is a do-not-translate brand name, and the rest of the locale writes it in Latin script (e.g. 'Firefox 홈').
- `Clear Search` — `ko/firefox-ios.xliff` — 'Clear Search' is translated as 'clear search history' instead of clearing the search field.
    - Current: `검색 기록 지우기`
    - Source: `Clear Search`
    - Suggest: `검색 지우기`
    - Per the comment, this is spoken after the user taps the close button to clear the search field and exit search mode; it does not delete any search history.
- `TodayWidget.TopSitesGalleryDescription` — `ko/firefox-ios.xliff` — 'Frequently and recently visited sites' became 'sites frequently visited recently', so the two separate categories are merged into one.
    - Current: `최근에 자주 방문한 사이트`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `자주 방문한 사이트 및 최근 방문한 사이트`
    - The source covers sites visited frequently and sites visited recently. The Korean only covers sites visited often in the recent past.

### C. Grammar, agreement & spelling

- `FirefoxHome.PrivacyNotice.Body.v148` — `ko/firefox-ios.xliff` — Object particle 을 follows %1$@, which is filled with "개인정보 고지" (vowel-final), so it should be 를.
    - Current: `%1$@을`
    - Source: `We’ve updated our %1$@ to reflect the latest features in %2$@. %3$@`
    - Suggest: `%1$@를`
    - The comment says %1$@ is the "Privacy Notice" string, translated as "개인정보 고지". It ends in a vowel, so the object particle must be 를. As written, the screen shows "개인정보 고지을", which is ungrammatical.
- `MainMenu.SettingsSection.WhatsNew.Title.v131` — `ko/firefox-ios.xliff` — "새기능" should be spaced as "새 기능" per Korean spacing rules.
    - Current: `새기능`
    - Source: `New in %@`
    - Suggest: `새 기능`
    - 새 is a determiner (관형사) and 기능 is a separate noun; 새기능 is not a registered compound, so standard orthography requires a space.
- `MainMenu.ToolsSection.AccessibilityLabels.FindInPage.v132` — `ko/firefox-ios.xliff` — Korean spacing error: the bound noun '내' must be written separately from '페이지'.
    - Current: `페이지내 검색`
    - Source: `Find in page`
    - Suggest: `페이지 내 검색`
    - Under standard Korean spacing rules, '내' (within) is a bound noun and takes a space after the preceding noun.
- `MainMenu.ToolsSection.FindInPageV2.Title.v141` — `ko/firefox-ios.xliff` — Missing space before "내" in "페이지내".
    - Current: `페이지내 검색`
    - Source: `Find in Page`
    - Suggest: `페이지 내 검색`
    - Here "내" is a dependent noun, and standard Korean spacing writes it as a separate word: "페이지 내".
- `NativeErrorPage.BadCertDomain.Description.v149` — `ko/firefox-ios.xliff` — Misspelling: '훔질' should be '훔칠'.
    - Current: `훔질 수 있습니다`
    - Source: `Someone pretending to be the site could try to steal your personal info. Your connection settings could also be set up incorrectly.`
    - Suggest: `훔칠 수 있습니다`
    - 'Steal' is 훔치다, so the correct form is 훔칠 수 있습니다. '훔질' is not a valid word.
- `QuickAnswers.ContentView.Answering.v158` — `ko/firefox-ios.xliff` — The dependent noun 중 needs a space before it.
    - Current: `답변중…`
    - Source: `Answering…`
    - Suggest: `답변 중…`
    - Under standard Korean spacing rules 중 is written apart from the word before it. The same screen already uses "생각 중…".
- `QuickAnswers.ContentView.SearchingSources.v158` — `ko/firefox-ios.xliff` — The dependent noun 중 needs a space before it.
    - Current: `소스 검색중…`
    - Source: `Searching sources…`
    - Suggest: `소스 검색 중…`
    - Under standard Korean spacing rules 중 is written apart from the word before it. The same screen already uses "생각 중…".
- `QuickAnswers.PrivacyBanner.Description.v158` — `ko/firefox-ios.xliff` — The dependent noun 데 (meaning "for the purpose of") needs a space before it.
    - Current: `식별하는데`
    - Source: `%@ doesn’t store your audio or questions, use your data to train AI models, or use your voice to identify you.`
    - Suggest: `식별하는 데`
    - In "식별하는 데", 데 is a dependent noun and takes a space. The same sentence spaces "훈련하는 데" correctly.
- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `ko/firefox-ios.xliff` — "추가 됐습니다" is incorrectly spaced; it should be the single word "추가됐습니다".
    - Current: `새로 추가 됐습니다!`
    - Source: `New! %@ Relay email masks are now available on mobile.`
    - Suggest: `새로 추가됐습니다!`
    - In Korean spelling, the suffix -되다 attaches to the noun with no space (추가되다).
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `ko/firefox-ios.xliff` — The object marker is doubled in "마스크를 하나를", and the clause doesn't say the free masks were used up.
    - Current: `5개의 무료 이메일 마스크를 사용해서 재사용할 마스크를 하나를 선택했습니다.`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `5개의 무료 이메일 마스크를 모두 사용하여 재사용할 마스크 하나를 선택했습니다.`
    - "마스크를 하나를" is ungrammatical (two object markers). "사용해서" without "모두" doesn't make clear that the limit of 5 was reached, which is the reason given in the source.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `ko/firefox-ios.xliff` — '다운로드 된' has a spacing error; the suffix -되다 should attach to the noun.
    - Current: `다운로드 된`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `다운로드된`
    - Under Korean spelling rules, the passive suffix '-되다' attaches directly to the noun ('다운로드된').
- `Settings.CrashReports.Message.v136` — `ko/firefox-ios.xliff` — The dependent noun 데 needs a space before it: it should be '해결하는 데', not '해결하는데'.
    - Current: `해결하는데 도움이`
    - Source: `This helps us diagnose and fix issues with the browser.`
    - Suggest: `해결하는 데 도움이`
    - In '~하는 데 도움이 되다', 데 is a dependent noun, and standard Korean spacing separates it from the verb before it. The nearby string Settings.DailyUsagePing.Message.v135 spells the same pattern correctly as '예측하는 데'.
- `WebCompatReporter.Preview.Data.PageLanguages.v155` — `ko/firefox-ios.xliff` — The bullet is ungrammatical: '언어 설정이 이 페이지로 보냄' makes the language settings the ones doing the sending.
    - Current: `언어 설정이 이 페이지로 보냄`
    - Source: `Language preferences sent to this page`
    - Suggest: `이 페이지로 보낸 언어 설정`
    - The source is a noun phrase, 'Language preferences sent to this page', meaning preferences the browser sent to the page. The Korean uses the subject particle 이 with the finite form 보냄, which makes it a broken clause in which the settings send something. It should be a noun phrase with a relative clause.
- `Find in Page` — `ko/firefox-ios.xliff` — Missing word space: "페이지내" should be "페이지 내" per Korean spacing rules.
    - Current: `페이지내 검색`
    - Source: `Find in Page`
    - Suggest: `페이지 내 검색`
    - The bound noun 내 (in/within) is written with a space after the noun in standard Korean orthography.
- `DownloadsPanel.EmptyState.Title` — `ko/firefox-ios.xliff` — "표시 됩니다" is wrongly spaced; the passive suffix -되다 attaches to the noun.
    - Current: `표시 됩니다`
    - Source: `Downloaded files will show up here.`
    - Suggest: `표시됩니다`
    - Under Korean spacing rules, 표시되다 is a single word, so it must not be split.
- `ErrorPages.AdvancedWarning2.Text` — `ko/firefox-ios.xliff` — "잘 못 되었거나" is misspelled as three words; the correct form is the single verb 잘못되다.
    - Current: `잘 못 되었거나`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `잘못되었거나`
    - 잘못되다 ('to be wrong/misconfigured') is one word, and 잘 못 means 'cannot do well', which is wrong in this sentence.
- `Loading content…` — `ko/firefox-ios.xliff` — The dependent noun 중 must be spaced from the preceding word.
    - Current: `읽는중…`
    - Source: `Loading content…`
    - Suggest: `읽는 중…`
    - Standard Korean spacing rules require 중 (a dependent noun) to be written separately: 읽는 중.
- `Mark as Unread` — `ko/firefox-ios.xliff` — The negative adverb 안 must be spaced from 읽음.
    - Current: `안읽음으로 표시`
    - Source: `Mark as Unread`
    - Suggest: `안 읽음으로 표시`
    - Under standard Korean spacing, the negator 안 is a separate word and should be written 안 읽음.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `ko/firefox-ios.xliff` — Passive suffix 되다 is wrongly spaced from the noun in "추가 되었습니다".
    - Current: `추가 되었습니다`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `추가되었습니다`
    - In standard Korean spacing, 되다 attaches directly to a Sino-Korean noun (추가되다), so it should not be written apart.
- `SendTo.NoDevicesFound.Message` — `ko/firefox-ios.xliff` — Verb-forming 하다 is wrongly spaced from the noun in "동기화 할".
    - Current: `동기화 할 수 있는`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `동기화할 수 있는`
    - 동기화하다 is a single verb, so its form 동기화할 is written as one word.
- `SendTo.NotSignedIn.Message` — `ko/firefox-ios.xliff` — Verb-forming 하다 is wrongly spaced from the noun in "이동 한".
    - Current: `이동 한 다음`
    - Source: `Please open Firefox, go to Settings and sign in to continue.`
    - Suggest: `이동한 다음`
    - 이동하다 is a single verb, so its form 이동한 is written as one word.
- `Settings.TrackingProtectionOption.BlockListStrict` — `ko/firefox-ios.xliff` — "Strict" option label is rendered as the adverb "엄격히" instead of a noun/adjectival label.
    - Current: `엄격히`
    - Source: `Strict`
    - Suggest: `엄격`
    - The option name sits alongside "표준" (Standard), which is a noun. "엄격히" means "strictly" and doesn't work as an option name.
- `Tab %@ of %@` — `ko/firefox-ios.xliff` — The ordinal suffix '번째' is wrongly split as '번 째'.
    - Current: `%1$@ 번 째 탭`
    - Source: `Tab %1$@ of %2$@`
    - Suggest: `%1$@번째 탭`
    - In Korean spelling, '째' is a suffix attached to '번'. '번 째' is a spacing error.
- `Tabs %@ to %@ of %@` — `ko/firefox-ios.xliff` — The ordinal suffix '번째' is wrongly split as '번 째'.
    - Current: `%2$@ 번 째 탭`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `%2$@번째 탭`
    - In Korean spelling, '째' is a suffix attached to '번'. '번 째' is a spacing error.
- `The page could not be displayed in Reader View.` — `ko/firefox-ios.xliff` — The copula '입니다' is wrongly separated from the noun it follows.
    - Current: `페이지 입니다`
    - Source: `The page could not be displayed in Reader View.`
    - Suggest: `페이지입니다`
    - The Korean copula '이다' attaches directly to the preceding noun, so '페이지 입니다' is a spacing error.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `ko/firefox-ios.xliff` — Spacing errors: '잠시후' and '접근하는데' should be '잠시 후' and '접근하는 데'.
    - Current: `접근하는데 문제가 발생했습니다. 잠시후 다시`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `접근하는 데 문제가 발생했습니다. 잠시 후 다시`
    - '후' and the bound noun '데' are separate words under Korean spacing rules.
- `There was an error converting the page` — `ko/firefox-ios.xliff` — Spacing error: '변환하는데' should be '변환하는 데'.
    - Current: `변환하는데`
    - Source: `There was an error converting the page`
    - Suggest: `변환하는 데`
    - Here '데' is a bound noun meaning 'in doing X', so it needs a space before it.
- `just now` — `ko/firefox-ios.xliff` — Spacing error: '방금전' should be '방금 전'.
    - Current: `방금전`
    - Source: `just now`
    - Suggest: `방금 전`
    - '전' is a separate word and must be spaced.
- `more than a month ago` — `ko/firefox-ios.xliff` — Spacing error: '한달전' should be '한 달 전'.
    - Current: `한달전`
    - Source: `more than a month ago`
    - Suggest: `한 달 전`
    - The unit noun '달' and '전' must each be written as separate words.
- `more than a week ago` — `ko/firefox-ios.xliff` — Spacing error: '일주일전' should be '일주일 전'.
    - Current: `일주일전`
    - Source: `more than a week ago`
    - Suggest: `일주일 전`
    - '전' is a separate word and must be spaced.
- `unread` — `ko/firefox-ios.xliff` — Misspelled negation: '않읽음' is not valid Korean.
    - Current: `않읽음`
    - Source: `unread`
    - Suggest: `안 읽음`
    - The short negation before a verb is '안' (안 읽음) or '읽지 않음'; '않' cannot be used as a standalone prefix. It should also match '읽었음' for 'read'.
- `Logins will be permanently removed.` — `ko/firefox-ios.xliff` — Wrong word spacing: '제거 합니다' should be one word.
    - Current: `제거 합니다`
    - Source: `Logins will be permanently removed.`
    - Suggest: `제거합니다`
    - '제거하다' is a single verb with the suffix -하다 and is written without a space, as in the neighbouring string '제거합니다'.
- `When Leaving Private Browsing` — `ko/firefox-ios.xliff` — Missing space before the dependent noun 때 in "나갈때".
    - Current: `나갈때`
    - Source: `When Leaving Private Browsing`
    - Suggest: `나갈 때`
    - Under standard Korean spacing rules, the dependent noun 때 is written as a separate word after the modifier form 나갈, so it must be "나갈 때".

### D. Terminology, register & consistency

- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `ko/firefox-ios.xliff` — 'device passcode' rendered as 장치 암호 with -하십시오, inconsistent with the sibling string's 기기 비밀번호 / -하세요.
    - Current: `장치 암호를 활성화하십시오`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `기기 비밀번호를 활성화하세요`
    - The logins message in the same file uses 기기 비밀번호 and the -하세요 ending for the same concept and the same message type.
- `Menu.EnhancedTrackingProtection.Details.Trackers.SocialMedia.v129` — `ko/firefox-ios.xliff` — Here "trackers" is translated as 추적자 (a person who tracks), but the same screen uses 추적기 everywhere else.
    - Current: `소셜 미디어 추적자`
    - Source: `Social media trackers: %@`
    - Suggest: `소셜 미디어 추적기`
    - The other tracker strings on this screen (Trackers blocked, the Standard and Strict footers) use 추적기. 추적자 usually means a human pursuer and doesn't match the rest of the screen.
- `Microsurvey.Survey.Sheet.AccessibilityLabel.v130` — `ko/firefox-ios.xliff` — 'Survey' is rendered as '조사', while the rest of the survey screen uses '설문조사'.
    - Current: `조사`
    - Source: `Survey`
    - Suggest: `설문조사`
    - The other strings in this file render 'survey' as 설문조사. On its own, 조사 can also mean investigation.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `ko/firefox-ios.xliff` — "Wallpaper" is rendered as "바탕화면" here but as "배경화면" in every other wallpaper string in the same file.
    - Current: `한정판 바탕화면`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `한정판 배경화면`
    - The same term should be translated the same way on one screen. Classic Wallpaper, Set Wallpaper and the other wallpaper strings all use 배경화면.
- `QuickAnswers.ContentView.Sources.v158` — `ko/firefox-ios.xliff` — "Sources" is rendered as "원본" (original), which doesn't match the "출처" used elsewhere in the feature for an answer's sources.
    - Current: `원본`
    - Source: `Sources`
    - Suggest: `출처`
    - This header names the sources an answer is built from. "원본" means "original copy". The opt-in description in the same feature uses "출처" for the same idea.
- `Settings.Search.PrivateSession.Setting.v124` — `ko/firefox-ios.xliff` — 'Private Sessions' is translated as '사생활 보호 세션' here but as '비공개 세션' in the descriptions on the same screen.
    - Current: `사생활 보호 세션에서 보기`
    - Source: `Show in Private Sessions`
    - Suggest: `비공개 세션에서 보기`
    - Settings.Search.PrivateSession.Description and Settings.Search.Suggest.PrivateSession.Description, which sit next to this toggle, both use '비공개 세션'.
- `VPN.Settings.DataUsage.AccessibilityLabel.v160` — `ko/firefox-ios.xliff` — The VoiceOver label keeps the abbreviation 'GB', but the comment requires the unit to be written out.
    - Current: `GB 사용함`
    - Source: `%1$@ of %2$@ gigabytes used`
    - Suggest: `기가바이트 사용함`
    - The developer comment says this label is the same as the visible text but with 'gigabytes' written out instead of 'GB'. The translation is identical to the visible string.
- `TermsOfUse.Link.PrivacyNotice.v142` — `ko/firefox-ios.xliff` — 'Privacy Notice' is translated '개인 정보 보호 정책' in the link but '개인정보 고지' in the description on the same sheet.
    - Current: `개인 정보 보호 정책`
    - Source: `Privacy Notice`
    - Suggest: `개인정보 고지`
    - The description sentence (TermsOfUse.Description.v142) says '개인정보 고지' for the same document the link points to. The two terms should match on one screen.
- `Menu.Bookmarks.Label` — `ko/firefox-ios.xliff` — "Bookmarks" is rendered as 즐겨찾기 while the same menu uses 북마크 for bookmark (e.g. 북마크 추가됨).
    - Current: `즐겨찾기`
    - Source: `Bookmarks`
    - Suggest: `북마크`
    - The term is inconsistent within the same menu screen: Menu.AddBookmark.Confirm uses 북마크, and Firefox Korean terminology uses 북마크 for bookmarks.
- `Menu.RemovedFromShortcuts.v99` — `ko/firefox-ios.xliff` — "Shortcuts" is written "바로가기" here but "바로 가기" in the related toast in the same file.
    - Current: `바로가기에서 제거`
    - Source: `Remove from Shortcuts`
    - Suggest: `바로 가기에서 제거`
    - The same term on the same feature is spelled two ways. Menu.RemovePin.Confirm2.v99 uses 바로 가기.
- `Settings.Homepage.Shortcuts.SponsoredShortcutsToggle.v100` — `ko/firefox-ios.xliff` — 'Shortcuts' is spelled '바로가기' here but '바로 가기' in the other strings on the same shortcuts settings page.
    - Current: `후원된 바로가기`
    - Source: `Sponsored Shortcuts`
    - Suggest: `후원된 바로 가기`
    - Within the same screen, ShortcutsPageTitle and ShortcutsToggle use '바로 가기'. This toggle should use the same spacing.
- `Settings.TrackingProtection.ProtectionLevel.Footer` — `ko/firefox-ios.xliff` — "Enhanced Tracking Protection" is written "향상된 추적 보호" here but "향상된 추적 방지 기능" on the setting label in the same screen.
    - Current: `향상된 추적 보호를`
    - Source: `If a site doesn’t work as expected, tap the lock in the address bar and turn off Enhanced Tracking Protection for that page.`
    - Suggest: `향상된 추적 방지 기능을`
    - The footer tells users to turn off a feature, so its name should match the label on the toggle (Settings.TrackingProtectionOption.NormalBrowsingLabelOn) and the section name "추적 방지". The same wording also appears in .Footer.Lock and Alert.Description.
- `Wallpaper.Download.Error.Title.v106` — `ko/firefox-ios.xliff` — '배경 화면' is spaced here, but the other wallpaper error strings write '배경화면' as one word.
    - Current: `배경 화면을`
    - Source: `Couldn’t Download Wallpaper`
    - Suggest: `배경화면을`
    - The same term appears two ways on the same error screens; the other wallpaper strings use '배경화면'.
- `TodayWidget.QuickActionsGalleryTitleV2` — `ko/firefox-ios.xliff` — 'Shortcuts' is rendered as 단축키 (keyboard shortcut) instead of 바로 가기, the term used everywhere else in the widget strings.
    - Current: `Firefox 단축키`
    - Source: `Firefox Shortcuts`
    - Suggest: `Firefox 바로 가기`
    - Here 'shortcuts' means home-screen shortcuts. The widget strings translate that as 바로 가기 everywhere else (e.g. QuickActionGalleryDescription, TopSitesGalleryTitleV2). 단축키 means a keyboard shortcut.
- `PzSrmZ-eHmH1H` — `ko/firefox-ios.xliff` — The quoted action name ‘사생활 보호 탭을 삭제’ does not match the menu item ‘사생활 보호 탭 지우기’, unlike the sibling confirmations, which quote their item exactly.
    - Current: `‘사생활 보호 탭을 삭제’ 하시겠습니까?`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘사생활 보호 탭 지우기’를 하시겠습니까?`
    - The source quotes the exact option label 'Clear Private Tabs'. The other confirmation strings quote their Korean menu item verbatim (‘새 검색’, ‘복사한 링크로 이동’).
- `fi3W24-eHmH1H` — `ko/firefox-ios.xliff` — The quoted action name ‘개인 탭 지우기’ does not match the menu item it refers to, ‘사생활 보호 탭 지우기’.
    - Current: `‘개인 탭 지우기’`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `‘사생활 보호 탭 지우기’`
    - This message quotes the 'Clear Private Tabs' option, which is translated '사생활 보호 탭 지우기' (eHmH1H). Every other string uses 사생활 보호 for 'private'.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ko/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
