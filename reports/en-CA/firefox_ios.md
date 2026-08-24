# Firefox iOS l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **Previous run** | 2026-08-22 @ `112744e9d020` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,847 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-CA: [android](android.md) · [firefox](firefox.md)

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
| Files | 94 |
| Strings | 1,847 |
| Missing strings | 63 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**63 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — 49
- `en-CA/firefox-ios.xliff` — 6
- `en-CA/firefox-ios.xliff` — 5
- `en-CA/firefox-ios.xliff` — 3

**Files absent from the locale:**

- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 10, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 84 | **typographic** |
| ellipsis | `char` 18 | **char** |
| dash | `em` 3, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (16)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 9 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Biometry.Screen.UniversalAuthenticationReason.v115` — `en-CA/firefox-ios.xliff` — The en-CA string adds "using your device passcode", which is not in the en-US source and changes the meaning.
    - Current: `Authenticate using your device passcode to access passwords.`
    - Source: `Authenticate to access passwords.`
    - Suggest: `Authenticate to access passwords.`
    - The en-US source reads "Authenticate to access passwords." en-CA should not differ here; the added phrase asserts a specific authentication method (passcode) rather than the generic biometric/passcode prompt, and no locale convention requires the change.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `en-CA/firefox-ios.xliff` — The ZIP code field label was changed to "Postal Code", making it identical to the separate postal code field and losing the US-specific meaning.
    - Current: `Postal Code`
    - Source: `ZIP Code`
    - Suggest: `ZIP Code`
    - The developer comment states this label is for the ZIP code field "primarily used in the United States"; there is a separate AutofillAddressPostalCode string already rendered as "Postal Code", so the two fields become indistinguishable and the US-specific term is lost.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `en-CA/firefox-ios.xliff` — The phrase "AI enhancements" was replaced with "features with AI", changing the wording of the setting away from the source term used in the setting's title.
    - Current: `new or current features with AI`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `new or current AI enhancements`
    - The en-US source says "new or current AI enhancements"; en-CA requires no change here, and the reworded phrase no longer matches the "Block AI enhancements" setting it describes.
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `en-CA/firefox-ios.xliff` — "Block AI Enhancements" rewritten as "Block Features With AI", changing the feature name referenced elsewhere in the settings.
    - Current: `Block Features With AI`
    - Source: `Block AI Enhancements`
    - Suggest: `Block AI Enhancements`
    - The source names the toggle "Block AI Enhancements" and the developer comment for Settings.AIControls.BlockedInformation refers to "the Block AI Enhancements toggle"; en-CA requires no such rewording.
- `Settings.AIControls.BlockedInformation.v151` — `en-CA/firefox-ios.xliff` — "AI enhancements" replaced with "features with AI", altering the terminology used by the source.
    - Current: `New and current features with AI are blocked by default.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `New and current AI enhancements are blocked by default.`
    - The en-US source says "New and current AI enhancements are blocked by default."; en-CA has no vocabulary difference that requires renaming this feature.
- `Settings.AIControls.HeaderCard.Message.v151` — `en-CA/firefox-ios.xliff` — "features enhanced with AI" changed to "features with AI", dropping wording present in the source.
    - Current: `That includes whether to use features with AI.`
    - Source: `That includes whether to use features enhanced with AI.`
    - Suggest: `That includes whether to use features enhanced with AI.`
    - The en-US source reads "features enhanced with AI"; no en-CA convention requires shortening this phrase.
- `Forward` — `en-CA/firefox-ios.xliff` — The toolbar Forward button accessibility label was changed to "Forwards", which is not a UI navigation term and departs from en-US without any Canadian convention requiring it.
    - Current: `Forwards`
    - Source: `Forward`
    - Suggest: `Forward`
    - en-CA uses the same UI term "Forward" as en-US for the browser navigation button (paired with "Back"); "Forwards" is an adverb and is not used as a button label.
- `Hotkeys.Forward.DiscoveryTitle` — `en-CA/firefox-ios.xliff` — Navigation label "Forward" was changed to "Forwards", which is not the browser navigation term and does not match the paired "Back" label.
    - Current: `Forwards`
    - Source: `Forward`
    - Suggest: `Forward`
    - The source is the browser navigation command "Forward", paired with "Back" (which is left unchanged in Hotkeys.Back.DiscoveryTitle). en-CA does not require "Forwards" here; the standard UI term is "Forward".

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

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
- `Log in` — `en-CA/firefox-ios.xliff` — "Log in" was changed to "Sign in" without any en-CA requirement, diverging from the source and from related login terminology in this file.
    - Current: `Sign in`
    - Source: `Log in`
    - Suggest: `Log in`
    - en-CA uses the same terminology as en-US here; the surrounding strings all use "Login"/"logins" (LoginsHelper.SaveLogin.Button, Logins), so changing the authentication prompt button to "Sign in" is an unnecessary and inconsistent vocabulary change.

### E. Typography, punctuation & spacing

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

### Fixed to date (0)

_Nothing fixed yet._
