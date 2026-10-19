# Firefox iOS l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `ec61063c1c68` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `ec61063c1c68` |
| **Previous run** | 2026-10-17 @ `09d125f6a298` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [android](android.md) · [firefox](firefox.md)

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
| Files | 97 |
| Strings | 1,927 |
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
| quotes | `corner` 27 | **corner** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 1 | **em** |
| fullwidth | `punctuation` 631 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (30)

> **Reads as a deliberate edit (4).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `zh-TW/firefox-ios.xliff` — "and that you use it" is rendered as "and how you use it", so the text describes more data being shared than the source says.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用它的事實`
    - The en-US says only that users share how they discovered the app and the fact that they use it. The translation says users share how they use it, which implies usage data goes to marketing partners. That is a wider data-sharing claim than the product makes.
- `Onboarding.Welcome.Description.TreatementA.v120` — `zh-TW/firefox-ios.xliff` — "helps stop companies from secretly following you" is rendered as a promise that the browser automatically blocks the tracking programs.
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `能協助阻止大企業在網路上偷偷跟蹤您`
    - The en-US makes a hedged claim ("helps stop"). The translation says the browser "will automatically block" tracking programs, which is a guarantee the product never made and a more specific description of how it works.
- `Onboarding.Welcome.Description.v120` — `zh-TW/firefox-ios.xliff` — "helps stop companies from secretly following you" is rendered as a promise that the browser automatically blocks the tracking programs.
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `能協助阻止大企業在網路上偷偷跟蹤您`
    - The en-US makes a hedged claim ("helps stop"). The translation says the browser "will automatically block" tracking programs, which is a guarantee the product never made and a more specific description of how it works.
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-TW/firefox-ios.xliff` — The hedged "helps stop advertisers from tracking" is turned into a flat claim that advertisers are prevented from tracking.
    - Current: `不讓廣告商追蹤您的瀏覽行為`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `協助阻止廣告商追蹤您的瀏覽行為`
    - The en-US only says the feature helps stop tracking. 「不讓」(does not let) says tracking is fully prevented, which is a guarantee the source never makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 8 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `zh-TW/firefox-ios.xliff` — The translation drops "blocks more trackers", so the verb 封鎖 has no object.
    - Current: `就自動封鎖`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `就封鎖更多追蹤器`
    - The source says strict mode blocks more trackers by stopping them before the page loads. The translation only says it blocks automatically before loading. It never says what is blocked or that more is blocked, and that is what explains the lower tracker count.
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `zh-TW/firefox-ios.xliff` — "Expiration date" is rendered as "expiration year" (到期年分).
    - Current: `到期年分`
    - Source: `Enter a valid expiration date`
    - Suggest: `到期日`
    - The source asks for a valid expiration date, which on a card is a month and a year. 年分 means only the year, so the error message misdescribes the field.
- `FirefoxSync.AddressAutofillEngine.v124` — `zh-TW/firefox-ios.xliff` — "Addresses" (postal addresses for autofill) is translated as "網址", which means web address/URL.
    - Current: `網址`
    - Source: `Addresses`
    - Suggest: `地址`
    - The developer comment says this is the toggle for syncing address autofill data, meaning street or postal addresses. "網址" means URL, so users would think the toggle syncs web addresses.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `zh-TW/firefox-ios.xliff` — "Try connecting on a different device" is rendered as connecting *to* another device.
    - Current: `試著連線到其他裝置`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `試著使用其他裝置連線`
    - The source advises the user to try going online with a different device, which helps rule out a problem with the device itself. 連線到其他裝置 means "connect to another device", which is a different and confusing instruction.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `zh-TW/firefox-ios.xliff` — "and that you use it" is rendered as "and how you use it", so the text describes more data being shared than the source says.
    - Current: `以及是如何使用的`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `以及您正在使用它的事實`
    - The en-US says only that users share how they discovered the app and the fact that they use it. The translation says users share how they use it, which implies usage data goes to marketing partners. That is a wider data-sharing claim than the product makes.
- `Onboarding.Welcome.Description.TreatementA.v120` — `zh-TW/firefox-ios.xliff` — "helps stop companies from secretly following you" is rendered as a promise that the browser automatically blocks the tracking programs.
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `能協助阻止大企業在網路上偷偷跟蹤您`
    - The en-US makes a hedged claim ("helps stop"). The translation says the browser "will automatically block" tracking programs, which is a guarantee the product never made and a more specific description of how it works.
- `Onboarding.Welcome.Description.v120` — `zh-TW/firefox-ios.xliff` — "helps stop companies from secretly following you" is rendered as a promise that the browser automatically blocks the tracking programs.
    - Current: `會自動封鎖讓大企業在網路上偷偷跟蹤您的程式`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `能協助阻止大企業在網路上偷偷跟蹤您`
    - The en-US makes a hedged claim ("helps stop"). The translation says the browser "will automatically block" tracking programs, which is a guarantee the product never made and a more specific description of how it works.
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `zh-TW/firefox-ios.xliff` — "Search Browsing History" is rendered as "Show Browsing History", inconsistent with the sibling toggles that use 搜尋.
    - Current: `顯示瀏覽紀錄`
    - Source: `Search Browsing History`
    - Suggest: `搜尋瀏覽紀錄`
    - The toggle enables searching browsing history in address bar suggestions; 顯示 means 'show', which changes the meaning and breaks consistency with 搜尋書籤 / 搜尋同步的分頁 in the same section.
- `Address.Bar.Reload.A11y.Hint.v124` — `zh-TW/firefox-ios.xliff` — "more options" is translated as "more information" (更多資訊).
    - Current: `取得更多資訊`
    - Source: `Double tap and hold for more options`
    - Suggest: `取得更多選項`
    - The source says that double tapping and holding the reload button gives more options, meaning a menu. 資訊 means information, so the hint describes the wrong thing.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `zh-TW/firefox-ios.xliff` — The product name "Firefox Sync" was cut to "Firefox", so the notice says the device disconnected from Firefox.
    - Current: `已與 Firefox 取消連線`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `已與 Firefox Sync 取消連線`
    - The source says the device disconnected from Firefox Sync, not from Firefox. The neighbouring string (ThisDevice_body) uses 「Firefox Sync」.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `zh-TW/firefox-ios.xliff` — "Camera Roll" is rendered as 照片串流 (Photo Stream), which names a different iOS feature.
    - Current: `照片串流`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `相機膠卷`
    - The source refers to the Camera Roll (相機膠卷), where saved images go. 照片串流 is the iCloud Photo Stream feature, which is a different thing.
- `Settings.Home.Option.Wallpaper.Accessibility.DefaultWallpaper.v99` — `zh-TW/firefox-ios.xliff` — "Clear" (plain/no-image wallpaper) is rendered as 明亮 ("bright"), describing a different wallpaper.
    - Current: `預設的明亮 Firefox 背景圖`
    - Source: `Default clear wallpaper.`
    - Suggest: `預設的無圖案背景圖。`
    - The en-US "Default clear wallpaper." refers to the plain default wallpaper with no pattern. 明亮 means bright, so screen-reader users hear a wrong description. The translation also adds "Firefox", which the source lacks, and drops the final period that the sibling strings use.
- `Settings.TrackingProtection.ProtectionCellFooter` — `zh-TW/firefox-ios.xliff` — The hedged "helps stop advertisers from tracking" is turned into a flat claim that advertisers are prevented from tracking.
    - Current: `不讓廣告商追蹤您的瀏覽行為`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `協助阻止廣告商追蹤您的瀏覽行為`
    - The en-US only says the feature helps stop tracking. 「不讓」(does not let) says tracking is fully prevented, which is a guarantee the source never makes.
- `TodayWidget.NewTabButtonLabelV1` — `zh-TW/firefox-ios.xliff` — "New Search" button label is rendered as "new search results" instead of the action "new search".
    - Current: `新搜尋結果`
    - Source: `New Search`
    - Suggest: `新搜尋`
    - The source is a button label for starting a new search (opens a new tab per the comment); 新搜尋結果 means 'new search results', which names a result list rather than the action. Other strings in the batch render it as 進行新搜尋.

### C. Grammar, agreement & spelling

- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `zh-TW/firefox-ios.xliff` — "行動板" uses the wrong character; it should be "行動版" (mobile version).
    - Current: `行動板`
    - Source: `New! %@ Relay email masks are now available on mobile.`
    - Suggest: `行動版`
    - The source says "available on mobile". The word for a mobile edition is 版 (version). 板 means board, so this is a spelling error.
- `Settings.DisplayTheme.SectionFooter` — `zh-TW/firefox-ios.xliff` — The adverb 自動 is duplicated in the same clause.
    - Current: `佈景主題將自動根據螢幕顯示亮度自動切換`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `佈景主題將根據螢幕顯示亮度自動切換`
    - The source says 'automatically' once. The translation has 「自動」 both before and after the 根據 phrase, which is a redundant doubling and reads as an editing slip.

### D. Terminology, register & consistency

- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `zh-TW/firefox-ios.xliff` — The description calls the address bar 網址框, but the title of the same card calls it 網址列.
    - Current: `在網址框輸入`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `在網址列輸入`
    - The card title (Toolbar.Title.v148) uses 網址列 for the address bar. The description on the same card should use the same term.
- `QuickAnswers.Errors.OpenSettings.v158` — `zh-TW/firefox-ios.xliff` — "Open Settings" is rendered as 開啟選項, which names Firefox's preferences rather than the iOS Settings app that this button opens.
    - Current: `開啟選項`
    - Source: `Open Settings`
    - Suggest: `開啟設定`
    - The developer comment says this button opens the iOS Settings app, which is called 設定 in zh-TW. The title of the same alert also uses 設定 (變更設定以使用「快速解答」), so 選項 is both inconsistent with it and points to the wrong place.
- `FxAPush_DeviceConnected_body` — `zh-TW/firefox-ios.xliff` — "Firefox Sync" is translated as 「Firefox 同步」, while the other notifications in this group keep 「Firefox Sync」.
    - Current: `Firefox 同步已連結到 %@`
    - Source: `Firefox Sync has connected to %@`
    - Suggest: `Firefox Sync 已連結到 %@`
    - The same product name is handled differently across the Sync notifications in this group. ThisDevice_body uses 「Firefox Sync」 and the titles use 「Sync」.
- `Keyboard.Shortcuts.ClearRecentHistory` — `zh-TW/firefox-ios.xliff` — The "Clear Recent History" shortcut uses 歷史記錄, while the History section heading on the same overlay uses 瀏覽紀錄.
    - Current: `清除最近的歷史記錄`
    - Source: `Clear Recent History`
    - Suggest: `清除最近的瀏覽紀錄`
    - Both strings appear on the same Discoverability overlay (section Keyboard.Shortcuts.Section.History = 瀏覽紀錄). Using a different term and a different character (記錄 vs 紀錄) for the same History concept is inconsistent. The History panel also uses 瀏覽紀錄.
- `LibraryPanel.History.SyncedHistory.v100` — `zh-TW/firefox-ios.xliff` — Uses 瀏覽記錄 while the rest of the History panel uses 瀏覽紀錄 for "history".
    - Current: `瀏覽記錄`
    - Source: `Synced History`
    - Suggest: `瀏覽紀錄`
    - The same History panel group writes the term as 紀錄 (Show History 顯示瀏覽紀錄, History 瀏覽紀錄, the ClearHistoryMenuTitle string 同步自其他裝置的紀錄). Writing it 記錄 here makes the term inconsistent on one screen.
- `fi3W24-scEmjs` — `zh-TW/firefox-ios.xliff` — The option name in quotes (進行新隱私搜尋) doesn't match the menu item it refers to, which this file translates as 新隱私搜尋.
    - Current: `「進行新隱私搜尋」`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `「新隱私搜尋」`
    - This label quotes the name of the 'New Private Search' option. The menu item scEmjs is translated 新隱私搜尋, so the two names are inconsistent.
- `fi3W24-xRJbBP` — `zh-TW/firefox-ios.xliff` — The option name in quotes (進行新搜尋) doesn't match the menu item it refers to, which this file translates as 新搜尋.
    - Current: `「進行新搜尋」`
    - Source: `There are ${count} options matching ‘New Search’.`
    - Suggest: `「新搜尋」`
    - This label quotes the name of the 'New Search' option. The menu item xRJbBP is translated 新搜尋, so the name a user sees here is not the name they see in the menu.

### E. Typography, punctuation & spacing

- `Onboarding.Modern.TermsOfService.PrivacyNoticeLink.v140` — `zh-TW/firefox-ios.xliff` — The link text ends with a full stop but sits mid-sentence in zh-TW, so the sentence on screen reads '到我們的隱私權公告。閱讀更多資訊。'
    - Current: `隱私權公告。`
    - Source: `Privacy Notice.`
    - Suggest: `隱私權公告`
    - The zh-TW agreement string '到我們的%2$@閱讀更多資訊。' puts text after the link, so a full stop at the end of the link text breaks the sentence in the middle.
- `Onboarding.Modern.TermsOfService.PrivacyNoticeLink.v145` — `zh-TW/firefox-ios.xliff` — The link text ends with a full stop but sits mid-sentence in zh-TW, so the sentence on screen reads '到我們的隱私權公告。閱讀更多資訊。'
    - Current: `隱私權公告。`
    - Source: `Privacy Notice.`
    - Suggest: `隱私權公告`
    - In English the link comes at the end of the sentence, so its trailing period ends the sentence. The zh-TW agreement string '到我們的%2$@閱讀更多資訊。' puts text after the link, so this full stop splits the sentence. The same fix applies to the v140 string.
- `A username and password are being requested by %@. The site says: %@` — `zh-TW/firefox-ios.xliff` — Halfwidth colon plus space used after Chinese text instead of the fullwidth colon.
    - Current: `此網站說:`
    - Source: `A username and password are being requested by %1$@. The site says: %2$@`
    - Suggest: `此網站說：`
    - zh-TW convention is fullwidth punctuation; a halfwidth colon after Chinese text deviates from it.
- `ActivityStream.JumpBackIn.TabGroup.SiteCount` — `zh-TW/firefox-ios.xliff` — Halfwidth colon used after Chinese text instead of the fullwidth colon.
    - Current: `分頁: %d`
    - Source: `Tabs: %d`
    - Suggest: `分頁：%d`
    - zh-TW convention is fullwidth punctuation; a halfwidth colon after Chinese text deviates from it.
- `ErrorPages.AdvancedWarning1.Text` — `zh-TW/firefox-ios.xliff` — Half-width colon followed by a space is used instead of the locale's full-width colon.
    - Current: `警告:`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `警告：`
    - zh-TW conventions use full-width punctuation (631 occurrences); a half-width colon plus space after Chinese text breaks that convention.
- `SendTo.DeviceList.Text` — `zh-TW/firefox-ios.xliff` — The header uses a half-width colon, but the locale convention is full-width punctuation.
    - Current: `可用裝置:`
    - Source: `Available devices:`
    - Suggest: `可用裝置：`
    - zh-TW consistently uses full-width punctuation. An ASCII colon after Chinese text breaks that convention.
- `TopSites.RemovePage.Button` — `zh-TW/firefox-ios.xliff` — The em dash separator from the source is rendered as a spaced ASCII hyphen.
    - Current: `移除頁面 - %@`
    - Source: `Remove page — %@`
    - Suggest: `移除頁面—%@`
    - The en-US uses an em dash, and the zh-TW convention is the em dash. A hyphen is the wrong dash.

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
