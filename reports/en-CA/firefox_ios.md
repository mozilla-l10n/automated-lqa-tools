# Firefox iOS l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,895 of 1,911 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-CA: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (2)

- `MainMenu.TabsSection.AccessibilityLabels.NewPrivateTab.v132` — `en-CA/firefox-ios.xliff` — Capitalization changed from source sentence case to title case in an accessibility label.
    - Current: `New Private Tab`
    - Source: `New private tab`
    - Suggest: `New private tab`
    - The en-US accessibility label is "New private tab" (sentence case); en-CA has no capitalization rule requiring title case, and sibling accessibility labels in this file (e.g. "Find in page", "Switch to desktop site") keep sentence case.
- `MainMenu.TabsSection.AccessibilityLabels.NewTab.v132` — `en-CA/firefox-ios.xliff` — Capitalization changed from source sentence case to title case in an accessibility label.
    - Current: `New Tab`
    - Source: `New tab`
    - Suggest: `New tab`
    - The en-US accessibility label is "New tab" (sentence case); other accessibility labels in this file retain sentence case, so this is an inconsistent, unneeded change.

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
| Files | 95 |
| Strings | 1,911 |
| Missing strings | 11 |
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

**11 strings** are not translated yet, concentrated in:

- `en-CA/firefox-ios.xliff` — 3
- `Shared/Supporting Files/en-US.lproj/GoogleLens.strings` — 2
- `en-CA/firefox-ios.xliff` — 2
- `en-CA/firefox-ios.xliff` — 2
- `en-CA/firefox-ios.xliff` — 1
- `en-CA/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/GoogleLens.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

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

## 3. Open findings (2)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `MainMenu.TabsSection.AccessibilityLabels.NewPrivateTab.v132` — `en-CA/firefox-ios.xliff` — Capitalization changed from source sentence case to title case in an accessibility label.
    - Current: `New Private Tab`
    - Source: `New private tab`
    - Suggest: `New private tab`
    - The en-US accessibility label is "New private tab" (sentence case); en-CA has no capitalization rule requiring title case, and sibling accessibility labels in this file (e.g. "Find in page", "Switch to desktop site") keep sentence case.
- `MainMenu.TabsSection.AccessibilityLabels.NewTab.v132` — `en-CA/firefox-ios.xliff` — Capitalization changed from source sentence case to title case in an accessibility label.
    - Current: `New Tab`
    - Source: `New tab`
    - Suggest: `New tab`
    - The en-US accessibility label is "New tab" (sentence case); other accessibility labels in this file retain sentence case, so this is an inconsistent, unneeded change.

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

- `Biometry.Screen.UniversalAuthenticationReason.v115` — `Shared/Supporting Files/en.lproj/BiometricAuthentication.strings` — fixed 2026-08-25
- `Addresses.EditAddress.AutofillAddressZip.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — fixed 2026-08-25
- `MainMenu.SettingsSection.AccessibilityLabels.GetHelp.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — fixed 2026-08-25
- `MainMenu.SettingsSection.GetHelp.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — fixed 2026-08-25
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `Settings.AIControls.BlockedInformation.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `Settings.AIControls.HeaderCard.Message.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `Settings.CrashReports.Link.v136` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `Settings.DailyUsagePing.Link.v136` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-25
- `CreditCard.SnackBar.RemovedCardLabel.v112` — `Shared/Supporting Files/en.lproj/SnackBar.strings` — fixed 2026-08-25
- `CreditCard.SnackBar.SavedCardLabel.v112` — `Shared/Supporting Files/en.lproj/SnackBar.strings` — fixed 2026-08-25
- `Forward` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-25
- `HistoryPanel.RecentlyClosedTabsButton.Title` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-25
- `Hotkeys.Forward.DiscoveryTitle` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-25
- `Log in` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-25
