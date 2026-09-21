# Firefox iOS l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 28 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-GB: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (1)

- `QuickAnswers.Errors.OK.v158` — `en-GB/firefox-ios.xliff` — "OK" has been changed to "Ok", which is not an en-GB adaptation and breaks the standard iOS button capitalisation.
    - Current: `Ok`
    - Source: `OK`
    - Suggest: `OK`
    - The source is "OK"; en-GB uses the same form. "Ok" is an unnecessary and non-standard alteration of a platform button label.

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
| Strings | 1,950 |
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
| apostrophe | `typographic` 93 | **typographic** |
| ellipsis | `char` 23 | **char** |
| dash | `em` 3, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

- `TodayWidget.ClosePrivateTabsLabelV2` — `en-GB/firefox-ios.xliff` — The deliberate line break in the widget label has been removed, collapsing the two-line layout into one line.
    - Current: `Close Private Tabs`
    - Source: `Close Private Tabs`
    - Suggest: `Close Private Tabs`
    - The en-US source contains an explicit newline between "Close" and "Private Tabs" so the widget button wraps as intended; the en-GB string drops it.
- `TodayWidget.GoToCopiedLinkLabelV2` — `en-GB/firefox-ios.xliff` — The deliberate line break in the widget label has been removed.
    - Current: `Go to Copied Link`
    - Source: `Go to Copied Link`
    - Suggest: `Go to Copied Link`
    - The en-US source has an explicit newline between "Go to" and "Copied Link" for the widget's two-line layout; the en-GB string is a single line.
- `TodayWidget.SearchInFirefoxV2` — `en-GB/firefox-ios.xliff` — The deliberate line break in the widget label has been removed.
    - Current: `Search in Firefox`
    - Source: `Search in Firefox`
    - Suggest: `Search in Firefox`
    - The en-US source breaks the line after "Search in" for the widget layout; the en-GB string collapses it to one line.
- `TodayWidget.SearchInPrivateTabLabelV2` — `en-GB/firefox-ios.xliff` — The deliberate line break in the widget label has been removed.
    - Current: `Search in Private Tab`
    - Source: `Search in Private Tab`
    - Suggest: `Search in Private Tab`
    - The en-US source breaks the line after "Search in" for the widget layout; the en-GB string collapses it to one line.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `CreditCard.SnackBar.RemovedCardLabel.v112` — `en-GB/firefox-ios.xliff` — Capitalisation changed from the source title case, inconsistently with the sibling string in the same file.
    - Current: `Card removed`
    - Source: `Card Removed`
    - Suggest: `Card Removed`
    - The en-US source uses title case ("Card Removed") and the neighbouring CreditCard.SnackBar.UpdatedCardLabel keeps title case ("Card Information Updated"), so lowercasing here is an unwarranted and inconsistent change; British English does not require a capitalisation change.
- `CreditCard.SnackBar.SavedCardLabel.v112` — `en-GB/firefox-ios.xliff` — Capitalisation changed from the source title case, inconsistently with the sibling string in the same file.
    - Current: `New card saved`
    - Source: `New Card Saved`
    - Suggest: `New Card Saved`
    - The en-US source uses title case ("New Card Saved") and CreditCard.SnackBar.UpdatedCardLabel in the same file retains title case, so this lowercasing is inconsistent within the file and not required by en-GB convention.

### E. Typography, punctuation & spacing

- `Onboarding.Modern.Sync.Description.v145` — `en-GB/firefox-ios.xliff` — Oxford comma retained here while it is removed in the parallel strings elsewhere in this file.
    - Current: `Your bookmarks, passwords, and more synchronise`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Your bookmarks, passwords and more synchronise`
    - The locale consistently drops the serial comma (e.g. Onboarding.Modern.Sync.Description.v140 "bookmarks, history and passwords", TermsOfUse.Description.v148 "Speedy, safe and"); this string is inconsistent with that adaptation.
- `Onboarding.Sync.Description.v123` — `en-GB/firefox-ios.xliff` — Serial (Oxford) comma retained here while the same batch removes it in the parallel list string, an inconsistent en-GB punctuation adaptation.
    - Current: `your passwords, bookmarks, and more`
    - Source: `%@ encrypts your passwords, bookmarks, and more when you’re synced.`
    - Suggest: `your passwords, bookmarks and more`
    - Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140 deliberately drops the serial commas ('hardware configuration and how you use', 'performance and stability'); this string keeps the en-US serial comma, so the file is inconsistent.
- `QuickAnswers.Errors.OK.v158` — `en-GB/firefox-ios.xliff` — "OK" has been changed to "Ok", which is not an en-GB adaptation and breaks the standard iOS button capitalisation.
    - Current: `Ok`
    - Source: `OK`
    - Suggest: `OK`
    - The source is "OK"; en-GB uses the same form. "Ok" is an unnecessary and non-standard alteration of a platform button label.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/en-GB/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (50)

- **`en-GB-backwards-forwards`** (3) — "Backwards" and "Forwards" are the en-GB house forms for the en-US "Back" and "Forward", in navigation labels and accessibility descriptions alike. See conventions.md.
    - `Back`, `Forward`, `Hotkeys.Forward.DiscoveryTitle`
- **`en-GB-post-code`** (1) — "Post Code" is the deliberate en-GB rendering of the en-US "Postal Code"; "Postcode" must not be suggested in its place. See conventions.md.
    - `Addresses.EditAddress.AutofillAddressPostalCode.v129`
- **`en-GB-sync-expanded-form-accepted`** (21) — "synchronise" / "synchronised" / "synchronising" / "synchronisation" are accepted en-GB renderings of the en-US "sync" family, so a suggestion to shorten one back to "sync" must never be accepted -- including one arguing that "Sync" is a feature name. See conventions.md.
    - `CreditCard.SnackBar.RemoveCardSublabel.v112`, `Bookmarks.EmptyState.Root.Body.v135`, `Bookmarks.EmptyState.Root.BodySignedOut.v135`, `Bookmarks.EmptyState.Root.ButtonTitle.v136`, `LoginsList.NoLoginsFound.Description.v122`, `Addresses.EditAddress.Alert.Message.v129`, `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106`, `Onboarding.Modern.BrandRefresh.Sync.SignIn.Action.v148`, `Onboarding.Modern.Sync.Description.v145`, `Onboarding.Modern.Sync.SignIn.Action.v140` …and 11 more
- **`en-GB-web-site-two-words`** (25) — "web site" / "web sites" is the en-GB house form; a suggestion to close it up to the en-US "website" must never be accepted. See conventions.md.
    - `NSLocationWhenInUseUsageDescription`, `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128`, `FirefoxHomepage.Shortcuts.AddShortcut.AlertDescription.v153.v2`, `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153`, `MainMenu.Submenus.Tools.WebsiteDarkMode.Title.v141`, `MainMenu.ToolsSection.AccessibilityLabels.WebsiteDarkMode.Title.v142`, `Settings.Summarize.LanguageSection.WebsiteLanguageLabel.v149`, `Summarizer.Error.UnsupportedContent.Message.v142`, `Offline Website Data`, `DefaultBrowserCard.Description` …and 15 more

_Suppressions live in `locales/en-GB/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (3)

- `MainMenu.Account.AccessibilityLabels.MainButton.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — fixed 2026-09-01
- `TabLocation.Share.A11y.Label.v119` — `Shared/Supporting Files/en.lproj/TabLocation.strings` — fixed 2026-09-01
- `HistoryPanel.RecentlyClosedTabsButton.Title` — `Shared/en.lproj/Localizable.strings` — fixed 2026-09-01
