# Firefox iOS l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `372c1b986f13` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `372c1b986f13` |
| **Previous run** | 2026-11-09 @ `62ca1adeb53c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,983 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Files | 98 |
| Strings | 1,983 |
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
| quotes | `corner` 29 | **corner** |
| ellipsis | `char` 31 | **char** |
| dash | `em` 2 | **em** |
| fullwidth | `punctuation` 671 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

### Proposed conventions — not applied (1)

Recurring reasons in this locale's tool-written dismissals. Nothing here reaches the reviewer until a person adds it to `firefox_ios/locales/zh-TW/conventions.md`; an inferred reason is a model's guess at why a Pontoon reviewer said no.

- Don't raise a finding just to swap a correct approved translation for a synonym or an equally valid alternative wording. If the existing zh-TW text is accurate and natural, a suggestion that is only "interchangeable" with it is not a fix. Examples: 報表 and 報告 are interchangeable for a crash "report", so don't push one over the other. Different quantifiers for permission items are also interchangeable. In the same way, don't propose rewording a tracker-protection message when the result is no better than the approved text. This does not cover real defects. Still flag a translation that drops or changes the source meaning (for example, 'older than %S months' rendered as '%S months ago'), leaves English untranslated, or breaks the glossary.
    _Behind it: 8 dismissals, 8 of them rejected in Pontoon._

    - `mozac_feature_addons_permissions_browser_settings_description_for_update` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
    - `mozac_feature_addons_permissions_content_description_item` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable for quantifiers for permission items</p>
    - `home_bookmarks_menu_item_remove` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
    - `ip_protection_location_recommended_label` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangeable; not better from original translation</p>
    - `protection_panel_banner_protected_no_blocked_trackers_description` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
    - `startup_crash_positive` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>
    - `trackers_blocked_empty` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
    - `unsubmitted_crash_dialog_positive_button` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>

---

## 3. Open findings (6)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `zh-TW/firefox-ios.xliff` — "You’re Protected" is rendered as "Let us protect you" instead of a status saying the user is protected.
    - Current: `讓我們保護您`
    - Source: `You’re Protected`
    - Suggest: `您已受到保護`
    - The source and the developer comment describe a status label saying the user is already protected (shown when zero trackers have been blocked). The translation is a request or call to action meaning "Let us protect you", which says something different.
- `FirefoxSync.AddressAutofillEngine.v124` — `zh-TW/firefox-ios.xliff` — "Addresses" (postal addresses for autofill) is translated as "網址", which means web address/URL.
    - Current: `網址`
    - Source: `Addresses`
    - Suggest: `地址`
    - The developer comment says this is the toggle for syncing address autofill data, meaning street or postal addresses. "網址" means URL, so users would think the toggle syncs web addresses.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `VPN.Settings.DataUsage.AccessibilityLabel.v160` — `zh-TW/firefox-ios.xliff` — The VoiceOver label keeps the abbreviation GB, but the comment asks for gigabytes written out.
    - Current: `每月上限為 %2$@ GB`
    - Source: `%1$@ of %2$@ gigabytes used`
    - Suggest: `每月上限為 %2$@ 十億位元組`
    - The developer comment says this label should match the visible text but with gigabytes spelled out for VoiceOver. The translation is identical to the visible string.
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

---

## 4. Appendix

### Dismissed by hand (4)

- `NativeErrorPage.NoInternetConnection.Description.v131` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `QuickAnswers.Errors.OpenSettings.v158` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `fi3W24-scEmjs` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/zh-TW/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (25)

- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Settings.TechnicalData.Message.v136` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Address.Bar.Reload.A11y.Hint.v124` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `VPN.ErrorBrowsingPopup.Body.v160` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `VPN.ErrorBrowsingPopup.ClosedOneTab.v160` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `VPN.ErrorBrowsingPopup.ClosedXTabs.v160` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `VPN.ReachedDataLimitPopup.ClosedOneTab.v160` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `VPN.ReachedDataLimitPopup.ClosedXTabs.v160` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `A username and password are being requested by %@. The site says: %@` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `ActivityStream.JumpBackIn.TabGroup.SiteCount` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `ErrorPages.AdvancedWarning1.Text` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `FxAPush_DeviceConnected_body` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Keyboard.Shortcuts.ClearRecentHistory` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `LibraryPanel.History.SyncedHistory.v100` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `SendTo.DeviceList.Text` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Settings.DisplayTheme.SectionFooter` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `Settings.Home.Option.Wallpaper.Accessibility.DefaultWallpaper.v99` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `TopSites.RemovePage.Button` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
- `TodayWidget.NewTabButtonLabelV1` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-09
