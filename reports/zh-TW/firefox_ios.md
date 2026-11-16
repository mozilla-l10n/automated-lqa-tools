# Firefox iOS l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3575a882abe1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3575a882abe1` |
| **Previous run** | 2026-11-09 @ `3d5d050768b7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 6 of 1,986 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (2)

- `FirefoxSync.AddressAutofillEngine.v124` — `zh-TW/firefox-ios.xliff` — "Addresses" (postal addresses for autofill) is translated as "網址", which means web address/URL.
    - Current: `網址`
    - Source: `Addresses`
    - Suggest: `地址`
    - The developer comment says this is the toggle for syncing address autofill data, meaning street or postal addresses. "網址" means URL, so users would think the toggle syncs web addresses.
- `fi3W24-xRJbBP` — `zh-TW/firefox-ios.xliff` — The option name in quotes (進行新搜尋) doesn't match the menu item it refers to, which this file translates as 新搜尋.
    - Current: `「進行新搜尋」`
    - Source: `There are ${count} options matching ‘New Search’.`
    - Suggest: `「新搜尋」`
    - This label quotes the name of the 'New Search' option. The menu item xRJbBP is translated 新搜尋, so the name a user sees here is not the name they see in the menu.

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
| Files | 99 |
| Strings | 1,986 |
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
| fullwidth | `punctuation` 672 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (0)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (7)

- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; reason unclear
- `NativeErrorPage.NoInternetConnection.Description.v131` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `Onboarding.Modern.TermsOfService.PrivacyNoticeLink.v140` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; likely reason (inferred): The English source ends with a full stop too, so the reviewer probably kept the original's 。 as matching the source, and nothing provided shows the sentence the finding says it sits in.
- `Onboarding.Modern.TermsOfService.PrivacyNoticeLink.v145` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-12): rejected in Pontoon without comment; likely reason (inferred): The English source ends with a full stop too, so the reviewer probably kept the original's 。 as matching the source, and nothing provided shows the sentence the finding says it sits in.
- `QuickAnswers.Errors.OpenSettings.v158` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `fi3W24-scEmjs` — `zh-TW/firefox-ios.xliff` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (1)

- `VPN.Settings.DataUsage.AccessibilityLabel.v160` — `zh-TW/firefox-ios.xliff` — auto-suggest (2026-11-09, string 29af2740): unreliable finding: zh-TW almost always writes gigabytes as GB, and VoiceOver reads it out fine; 十億位元組 is rarely used and would read oddly, so GB here is acceptable and not clearly a defect.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/zh-TW/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (27)

- `FirefoxSync.AddressAutofillEngine.v124` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-16
- `fi3W24-xRJbBP` — `zh-TW/firefox-ios.xliff` — fixed 2026-11-16
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
