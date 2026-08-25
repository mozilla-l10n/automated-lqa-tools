# Firefox iOS l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-08-25 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `4de01f1b366e` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `4de01f1b366e` |
| **Previous run** | 2026-08-25 @ `edf993984c10` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 1,912 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-CA: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (8)

- `MainMenu.SettingsSection.AccessibilityLabels.GetHelp.v132` — `en-CA/firefox-ios.xliff` — Accessibility label capitalization diverges from source and from the parallel labels in the same section.
    - Current: `Get help`
    - Source: `Get Help`
    - Suggest: `Get Help`
    - Source is "Get Help"; sibling accessibility labels (Customize Homepage, Settings, Bookmark Page) retain title case, so this lowercase form is an inconsistent, unmotivated change.
- `MainMenu.SettingsSection.GetHelp.Title.v131` — `en-CA/firefox-ios.xliff` — Title case of the source menu item was changed to sentence case without any en-CA rule requiring it.
    - Current: `Get help`
    - Source: `Get Help`
    - Suggest: `Get Help`
    - en-US source is "Get Help" and other menu titles in this file (Customize Homepage, Bookmark Page, Sign In) keep title case; en-CA has no convention that lowercases menu item titles.
- `Settings.CrashReports.Link.v136` — `en-CA/firefox-ios.xliff` — Link label changed from title case "Learn More" to "Learn more", departing from the source capitalization without any en-CA rule requiring it.
    - Current: `Learn more`
    - Source: `Learn More`
    - Suggest: `Learn More`
    - The en-US source is "Learn More"; en-CA has no capitalization convention that differs from en-US here, so the change is an unnecessary inconsistency.
- `Settings.DailyUsagePing.Link.v136` — `en-CA/firefox-ios.xliff` — Link label changed from title case "Learn More" to "Learn more", departing from the source capitalization without any en-CA rule requiring it.
    - Current: `Learn more`
    - Source: `Learn More`
    - Suggest: `Learn More`
    - The en-US source is "Learn More"; en-CA capitalization matches en-US, so lowercasing is an unwarranted deviation.
- `CreditCard.SnackBar.RemovedCardLabel.v112` — `en-CA/firefox-ios.xliff` — Capitalization changed from the source's title case, inconsistent with the sibling snackbar string that keeps title case.
    - Current: `Card removed`
    - Source: `Card Removed`
    - Suggest: `Card Removed`
    - en-CA differs from en-US only in spelling/vocabulary conventions, not capitalization; the parallel string CreditCard.SnackBar.UpdatedCardLabel.v122 retains 'Card Information Updated' in title case, so this is an inconsistent deviation.
- `CreditCard.SnackBar.SavedCardLabel.v112` — `en-CA/firefox-ios.xliff` — Capitalization changed from the source's title case, inconsistent with the sibling snackbar string that keeps title case.
    - Current: `New card saved`
    - Source: `New Card Saved`
    - Suggest: `New Card Saved`
    - en-CA has no capitalization rule differing from en-US; the parallel string 'Card Information Updated' keeps title case, making this deviation inconsistent within the same file.
- `HistoryPanel.RecentlyClosedTabsButton.Title` — `en-CA/firefox-ios.xliff` — Title case of the source button label was changed to sentence case with no en-CA rule requiring it, breaking consistency with other title-cased labels in the same panel.
    - Current: `Recently closed`
    - Source: `Recently Closed`
    - Suggest: `Recently Closed`
    - en-CA does not differ from en-US in capitalization conventions; surrounding History Panel and menu titles (e.g. "Delete from History", "Remove Bookmark", "Close All Inactive Tabs") retain the source title case.
- `Log in` — `en-CA/firefox-ios.xliff` — "Log in" was changed to "Sign in" without any en-CA requirement, diverging from the source and from related login terminology in this file.
    - Current: `Sign in`
    - Source: `Log in`
    - Suggest: `Log in`
    - en-CA uses the same terminology as en-US here; the surrounding strings all use "Login"/"logins" (LoginsHelper.SaveLogin.Button, Logins), so changing the authentication prompt button to "Sign in" is an unnecessary and inconsistent vocabulary change.

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
| Files | 95 |
| Strings | 1,912 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
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
| apostrophe | `typographic` 90 | **typographic** |
| ellipsis | `char` 20 | **char** |
| dash | `em` 3, `en` 2 | _mixed_ |

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

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/en-CA/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (16)

- `Biometry.Screen.UniversalAuthenticationReason.v115` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Addresses.EditAddress.AutofillAddressZip.v129` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `MainMenu.SettingsSection.AccessibilityLabels.GetHelp.v132` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `MainMenu.SettingsSection.GetHelp.Title.v131` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.AIControls.BlockedInformation.v151` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.AIControls.HeaderCard.Message.v151` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.CrashReports.Link.v136` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Settings.DailyUsagePing.Link.v136` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `CreditCard.SnackBar.RemovedCardLabel.v112` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `CreditCard.SnackBar.SavedCardLabel.v112` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Forward` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `HistoryPanel.RecentlyClosedTabsButton.Title` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Hotkeys.Forward.DiscoveryTitle` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
- `Log in` — `en-CA/firefox-ios.xliff` — fixed 2026-08-25
