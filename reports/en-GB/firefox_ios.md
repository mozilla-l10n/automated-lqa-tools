# Firefox iOS l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `21033d5fb0bb` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `21033d5fb0bb` |
| **Previous run** | 2026-08-24 @ `21033d5fb0bb` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,910 |

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
| Strings | 1,910 |
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

## 3. Open findings (24)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 10 |
| 3 | Degraded language (grammar, spelling, terminology) | 11 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.EmptyState.Root.ButtonTitle.v136` — `en-GB/firefox-ios.xliff` — "Sync" is a Mozilla feature/product name and must not be expanded to "Synchronise".
    - Current: `Sign in to Synchronise`
    - Source: `Sign in to Sync`
    - Suggest: `Sign in to Sync`
    - The developer comment identifies "Sync" as the capitalised feature name (Mozilla Account sync); en-GB uses the same brand term "Sync", so replacing it with "Synchronise" damages the product name.
- `Onboarding.Modern.Sync.Description.v145` — `en-GB/firefox-ios.xliff` — The Sync feature name has been wrongly expanded to "synchronise", damaging the product feature name.
    - Current: `more synchronise on any device`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `more sync on any device`
    - "Sync" here is the Firefox Sync feature name/verb used in the product UI; en-GB uses "Sync" too. Replacing it with "synchronise" breaks the feature branding and reads unidiomatically.
- `Onboarding.Modern.Sync.SignIn.Action.v140` — `en-GB/firefox-ios.xliff` — Button label replaces the Firefox Sync feature name with "Synchronising".
    - Current: `Start Synchronising`
    - Source: `Start Syncing`
    - Suggest: `Start Syncing`
    - "Sync" is the product feature name (Firefox Sync), retained in en-GB; expanding it to "Synchronising" mangles the brand term and lengthens a button label.
- `Onboarding.Modern.Sync.SignIn.Action.v145` — `en-GB/firefox-ios.xliff` — Button label replaces the Firefox Sync feature name with "Synchronising".
    - Current: `Start Synchronising`
    - Source: `Start Syncing`
    - Suggest: `Start Syncing`
    - "Sync" is the product feature name (Firefox Sync), retained in en-GB; expanding it to "Synchronising" mangles the brand term and lengthens a button label.
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `en-GB/firefox-ios.xliff` — "Sync on all your devices" rendered as "Synchronise", replacing the feature name.
    - Current: `Synchronise on all your devices`
    - Source: `Load sites lightning fast Automatic tracking protection Sync on all your devices`
    - Suggest: `Sync on all your devices`
    - "Sync" refers to the Firefox Sync feature, which keeps its name in en-GB; substituting "Synchronise" damages the product term.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `en-GB/firefox-ios.xliff` — "synced" was expanded to "synchronised", damaging the established Firefox Sync terminology used elsewhere in the locale.
    - Current: `Open synchronised tab`
    - Source: `Open synced tab`
    - Suggest: `Open synced tab`
    - "Synced tab" is Firefox product terminology tied to the Sync feature and is retained in en-GB; expanding it to "synchronised" is an over-correction and inconsistent with other sync-related strings.
- `Menu.SyncAndSaveData.v103` — `en-GB/firefox-ios.xliff` — "Sync" (referring to the Firefox Sync feature) has been needlessly expanded to "Synchronise", damaging the feature name and lengthening a menu label.
    - Current: `Synchronise and Save Data`
    - Source: `Sync and Save Data`
    - Suggest: `Sync and Save Data`
    - The developer comment states this is the Firefox Sync button; "Sync" is the product feature name and is used unchanged in British English. "Synchronise" also makes the menu label longer on a phone.
- `Settings.Sync.ButtonTitle.v103` — `en-GB/firefox-ios.xliff` — "Sync" as the Firefox Sync feature name was expanded to "Synchronise", damaging the product/feature name.
    - Current: `Synchronise and Save Data`
    - Source: `Sync and Save Data`
    - Suggest: `Sync and Save Data`
    - The developer comment refers to the "Firefox for iOS sync service"; Sync is a brand/feature name and is kept as "Sync" in en-GB (see Settings.TroubleShootSync.Title referring to Sync issues).
- `Settings.Sync.SignInView.Title.v103` — `en-GB/firefox-ios.xliff` — Feature name "Sync" expanded to "Synchronise" in the sign-in page title.
    - Current: `Synchronise and Save Data`
    - Source: `Sync and Save Data`
    - Suggest: `Sync and Save Data`
    - The comment identifies this as the Firefox Sync account page; "Sync" is the feature name and should not be expanded, and it is left as "Sync" elsewhere in the locale.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `CreditCard.SnackBar.RemoveCardSublabel.v112` — `en-GB/firefox-ios.xliff` — "synced" was expanded to "synchronised", departing from the Firefox Sync terminology used consistently in the locale.
    - Current: `This will remove the card from all of your synchronised devices.`
    - Source: `This will remove the card from all of your synced devices.`
    - Suggest: `This will remove the card from all of your synced devices.`
    - "Synced" is the standard product term tied to Firefox Sync and is used elsewhere in en-GB; replacing it with "synchronised" is an over-correction of a technical term.
- `Bookmarks.EmptyState.Root.Body.v135` — `en-GB/firefox-ios.xliff` — "synced" was over-corrected to "synchronised"; en-GB uses "synced devices" as the standard term.
    - Current: `other synchronised devices`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `other synced devices`
    - "Synced" is standard in British English for the Firefox Sync feature and is not an Americanism requiring adaptation; expanding it is an over-correction and inconsistent with the Sync product terminology.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `en-GB/firefox-ios.xliff` — "synced" was over-corrected to "synchronised"; en-GB uses "synced devices" as the standard term.
    - Current: `other synchronised devices`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `other synced devices`
    - "Synced" is standard in British English and refers to the Firefox Sync feature; expanding it is an over-correction and inconsistent with the product terminology.
- `LoginsList.NoLoginsFound.Description.v122` — `en-GB/firefox-ios.xliff` — "sync" has been changed to "synchronise", altering the established product term used elsewhere in the locale.
    - Current: `save or synchronise to %@`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `save or sync to %@`
    - "Sync" is Firefox's product terminology (Firefox Sync) and is standard in British English too; expanding it to "synchronise" is an over-correction and is inconsistent with other sync strings in the locale.
- `Addresses.EditAddress.Alert.Message.v129` — `en-GB/firefox-ios.xliff` — "synced devices" has been over-corrected to "synchronised devices".
    - Current: `all of your synchronised devices`
    - Source: `The address will be removed from all of your synced devices.`
    - Suggest: `all of your synced devices`
    - "Synced devices" is the Firefox Sync product term and is used unchanged in British English; expanding it is an unnecessary over-correction and inconsistent with the rest of the locale.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `en-GB/firefox-ios.xliff` — "syncing" was expanded to "synchronising", which departs from the product term "Sync" used consistently elsewhere in the locale.
    - Current: `Your tabs are synchronising!`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Your tabs are syncing!`
    - Firefox Sync terminology ("Sync", "syncing") is retained in en-GB, e.g. FirefoxSync.strings toggles and the "Settings > Sync Data" menu; replacing it with "synchronising" is an inconsistent over-correction.
- `Onboarding.Modern.BrandRefresh.Sync.SignIn.Action.v148` — `en-GB/firefox-ios.xliff` — "Start Syncing" was expanded to "Start Synchronising", an over-correction of a standard product term that also lengthens a button label.
    - Current: `Start Synchronising`
    - Source: `Start Syncing`
    - Suggest: `Start Syncing`
    - "Sync"/"syncing" is the established Firefox feature term in en-GB (Firefox Sync) and is not a US-only spelling; changing it to "Synchronising" departs from the product terminology and makes a button label substantially longer on a phone.
- `Onboarding.Sync.Description.v123` — `en-GB/firefox-ios.xliff` — "synced" was needlessly expanded to "synchronised", departing from the Sync feature terminology used elsewhere.
    - Current: `when you’re synchronised`
    - Source: `%@ encrypts your passwords, bookmarks, and more when you’re synced.`
    - Suggest: `when you’re synced`
    - "Synced" is the standard product term for the Sync feature and is equally correct in British English; changing it to "synchronised" is an over-correction that breaks terminology consistency with the Sync onboarding page title/buttons.
- `TabsTray.Sync.SyncTabsDisabled.v116` — `en-GB/firefox-ios.xliff` — "tab syncing" was needlessly expanded to "tab synchronising", inconsistent with the untranslated "Sync" feature name used elsewhere in the file.
    - Current: `tab synchronising`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `tab syncing`
    - "Sync"/"syncing" is standard in en-GB Firefox and matches the "Sync" label kept elsewhere in this file; "synchronising" is an over-correction of a product term.
- `TabsTray.SyncTabs.SyncTabsButton.Title.v119` — `en-GB/firefox-ios.xliff` — "Sync Tabs" was changed to "Synchronise Tabs", altering a Firefox feature name that en-GB does not translate.
    - Current: `Synchronise Tabs`
    - Source: `Sync Tabs`
    - Suggest: `Sync Tabs`
    - "Sync" is the Firefox feature/product name (see TabTray.TabsSelectorSyncedTabsTitle.v140 kept as "Sync" in the same file); expanding it to "Synchronise" is an over-correction and inconsistent within the locale.
- `LibraryPanel.History.SyncedHistory.v100` — `en-GB/firefox-ios.xliff` — "Synced" was expanded to "Synchronised", changing the established Firefox Sync feature terminology.
    - Current: `Synchronised History`
    - Source: `Synced History`
    - Suggest: `Synced History`
    - "Synced" is the product term tied to the Firefox Sync feature and is used unchanged in en-GB; "Synchronised" is an unnecessary expansion that also lengthens a panel title on a phone screen.
- `TabTray.SegmentedControlTitles.SyncedTabs` — `en-GB/firefox-ios.xliff` — "Synced" was expanded to "Synchronised", inconsistent with the Sync product terminology used elsewhere in the locale and much longer for a segmented control on a phone.
    - Current: `Synchronised`
    - Source: `Synced`
    - Suggest: `Synced`
    - British English uses "Synced" for the Firefox Sync feature (cf. Sync.SyncingEllipsis.Label "Syncing…" and SyncState.Offline.Title "Sync is offline" kept unchanged); the longer form is inconsistent and risks truncation in a segmented control.

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

### Suppressed as false positives (29)

- **`en-GB-backwards-forwards`** (3) — "Backwards" and "Forwards" are the en-GB house forms for the en-US "Back" and "Forward", in navigation labels and accessibility descriptions alike. See conventions.md.
    - `Back`, `Forward`, `Hotkeys.Forward.DiscoveryTitle`
- **`en-GB-post-code`** (1) — "Post Code" is the deliberate en-GB rendering of the en-US "Postal Code"; "Postcode" must not be suggested in its place. See conventions.md.
    - `Addresses.EditAddress.AutofillAddressPostalCode.v129`
- **`en-GB-web-site-two-words`** (25) — "web site" / "web sites" is the en-GB house form; a suggestion to close it up to the en-US "website" must never be accepted. See conventions.md.
    - `NSLocationWhenInUseUsageDescription`, `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128`, `FirefoxHomepage.Shortcuts.AddShortcut.AlertDescription.v153.v2`, `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153`, `MainMenu.Submenus.Tools.WebsiteDarkMode.Title.v141`, `MainMenu.ToolsSection.AccessibilityLabels.WebsiteDarkMode.Title.v142`, `Settings.Summarize.LanguageSection.WebsiteLanguageLabel.v149`, `Summarizer.Error.UnsupportedContent.Message.v142`, `Offline Website Data`, `DefaultBrowserCard.Description` …and 15 more

_Suppressions live in `locales/en-GB/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
