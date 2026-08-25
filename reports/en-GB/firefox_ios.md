# Firefox iOS l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-25 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `edf993984c10` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `edf993984c10` |
| **Previous run** | 2026-08-24 @ `21033d5fb0bb` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 1,912 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-GB: [android](android.md) · [firefox](firefox.md)

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

## 3. Open findings (3)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `MainMenu.Account.AccessibilityLabels.MainButton.v132` — `en-GB/firefox-ios.xliff` — Serial (Oxford) comma retained here while it is removed in the parallel sync strings in the same file.
    - Current: `Sign in to synchronise passwords, tabs, and more`
    - Source: `Sign in to sync passwords, tabs, and more`
    - Suggest: `Sign in to synchronise passwords, tabs and more`
    - MainMenu.Account.SignedOut.Description.v131/v141 and ContextualHints.MainMenu.MenuRedesign.Body.v142 all drop the serial comma in this locale; this identical phrase keeps it, which is inconsistent within the same file.
- `TabLocation.Share.A11y.Label.v119` — `en-GB/firefox-ios.xliff` — Capitalisation changed from sentence case to title case without any en-GB reason.
    - Current: `Share This Page`
    - Source: `Share this page`
    - Suggest: `Share this page`
    - The source uses sentence case for this accessibility label; en-GB has no convention requiring title case, so this is an unwarranted deviation.
- `HistoryPanel.RecentlyClosedTabsButton.Title` — `en-GB/firefox-ios.xliff` — Title case of the button label was changed to sentence case, inconsistent with neighbouring History Panel titles.
    - Current: `Recently closed`
    - Source: `Recently Closed`
    - Suggest: `Recently Closed`
    - Sibling strings in the same panel ("Clear Recent History…", "Today and Yesterday", "The Last Hour") retain the source title case; en-GB has no capitalisation rule requiring the change here.

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

### Fixed to date (0)

_Nothing fixed yet._
