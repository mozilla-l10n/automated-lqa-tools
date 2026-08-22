# Firefox iOS l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `112744e9d020` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `112744e9d020` |
| **Previous run** | 2026-08-21 @ `7e1ae61658ad` |
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
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
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

## 3. Open findings (53)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 13 |
| 3 | Degraded language (grammar, spelling, terminology) | 37 |
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
- `Back` — `en-GB/firefox-ios.xliff` — The Back button accessibility label was changed to "Backwards", which is not the name of the toolbar control.
    - Current: `Backwards`
    - Source: `Back`
    - Suggest: `Back`
    - The source "Back" is the standard name of the browser's Back button; British English uses "Back" identically. "Backwards" is an adverb and misnames the control for VoiceOver users.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `en-GB/firefox-ios.xliff` — "synced" was expanded to "synchronised", damaging the established Firefox Sync terminology used elsewhere in the locale.
    - Current: `Open synchronised tab`
    - Source: `Open synced tab`
    - Suggest: `Open synced tab`
    - "Synced tab" is Firefox product terminology tied to the Sync feature and is retained in en-GB; expanding it to "synchronised" is an over-correction and inconsistent with other sync-related strings.
- `Forward` — `en-GB/firefox-ios.xliff` — Toolbar Forward button accessibility label changed to "Forwards", which is not the UI control name.
    - Current: `Forwards`
    - Source: `Forward`
    - Suggest: `Forward`
    - This is the accessibility label for the Back/Forward navigation button; en-GB uses "Forward" as the button name just as en-US does, matching the paired "Back" label. "Forwards" is an adverb and is not used as a browser control name.
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

- `NSLocationWhenInUseUsageDescription` — `en-GB/firefox-ios.xliff` — "Websites" was changed to the two-word "Web sites", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `Web sites you visit may request your location.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Websites you visit may request your location.`
    - en-GB uses "websites" as one word, same as en-US; the split form is an unnecessary and inconsistent alteration of the source.
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
- `Addresses.EditAddress.AutofillAddressPostalCode.v129` — `en-GB/firefox-ios.xliff` — "Post Code" is inconsistently capitalised/spelled; the standard UK term is "Postcode".
    - Current: `Post Code`
    - Source: `Postal Code`
    - Suggest: `Postcode`
    - en-GB renders the source "Postal Code" as a single word "Postcode", the standard British term; "Post Code" as two words is non-standard.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `en-GB/firefox-ios.xliff` — "websites" was changed to "web sites", which is inconsistent with the rest of the locale and not an en-GB requirement.
    - Current: `web sites`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `websites`
    - The source uses "websites" as a single word, and other strings in this same file (e.g. Details.ConnectionSecure comment/usage) treat "website" as one word; "web sites" is not a British English adaptation, just an inconsistent spelling.
- `FirefoxHomepage.Shortcuts.AddShortcut.AlertDescription.v153.v2` — `en-GB/firefox-ios.xliff` — "website" was changed to "web site", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `Enter the URL for the web site.`
    - Source: `Enter the URL for the website.`
    - Suggest: `Enter the URL for the website.`
    - en-GB uses "website" as one word, as elsewhere in this locale (e.g. the tracking protection strings' developer usage and other UI strings). Splitting it into "web site" is an unnecessary and inconsistent change from the en-US source.
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `en-GB/firefox-ios.xliff` — "Website URL" was changed to "Web Site URL", an unnecessary and non-standard alteration.
    - Current: `Web Site URL`
    - Source: `Website URL`
    - Suggest: `Website URL`
    - en-GB uses "website" as one word, the same as the source; "Web Site" is an over-correction inconsistent with the rest of the locale (developer comments and other strings use "website").
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `en-GB/firefox-ios.xliff` — "syncing" was expanded to "synchronising", which departs from the product term "Sync" used consistently elsewhere in the locale.
    - Current: `Your tabs are synchronising!`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Your tabs are syncing!`
    - Firefox Sync terminology ("Sync", "syncing") is retained in en-GB, e.g. FirefoxSync.strings toggles and the "Settings > Sync Data" menu; replacing it with "synchronising" is an inconsistent over-correction.
- `MainMenu.Submenus.Tools.WebsiteDarkMode.Title.v141` — `en-GB/firefox-ios.xliff` — "Website" was needlessly split into "Web Site", which is inconsistent with the rest of the locale.
    - Current: `Web Site Dark Mode`
    - Source: `Website Dark Mode`
    - Suggest: `Website Dark Mode`
    - en-GB uses "website" as one word, as elsewhere in this file (e.g. "Report Broken Site" strings refer to a "broken website"). "Web Site" is not a British adaptation and departs from the source without reason.
- `MainMenu.ToolsSection.AccessibilityLabels.WebsiteDarkMode.Title.v142` — `en-GB/firefox-ios.xliff` — "Website" was needlessly split into "Web Site", diverging from the term used elsewhere in the locale.
    - Current: `Web Site Dark Mode`
    - Source: `Website Dark Mode`
    - Suggest: `Website Dark Mode`
    - The en-US source is "Website Dark Mode" and "website" is the standard form in British English too; the related strings (MainMenu.WebsiteDarkModeOnV2/OffV2 comments, and other 'site' strings in this file) use "Website". This is an over-correction that makes the accessibility label inconsistent.
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
- `Settings.Summarize.LanguageSection.WebsiteLanguageLabel.v149` — `en-GB/firefox-ios.xliff` — "Website" was needlessly split into "Web Site", which is not a British English convention and is inconsistent with the rest of the locale.
    - Current: `Web Site Language`
    - Source: `Website Language`
    - Suggest: `Website Language`
    - en-GB uses "website" as a single word, same as en-US; there is no spelling rule requiring the split form, so this is an over-correction.
- `Summarizer.Error.UnsupportedContent.Message.v142` — `en-GB/firefox-ios.xliff` — "website" was incorrectly split into "web site", which is not an en-GB adaptation and is inconsistent with the rest of the locale.
    - Current: `This web site doesn’t allow content summarisation.`
    - Source: `This website doesn’t allow content summarization. Try a different page.`
    - Suggest: `This website doesn’t allow content summarisation.`
    - en-GB uses "website" as one word, as elsewhere in this locale (e.g. "web page" strings retain source forms); "web site" is an over-correction of the source "website".
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
- `Offline Website Data` — `en-GB/firefox-ios.xliff` — "Website" was split into "Web Site", an outdated form not used in en-GB and inconsistent with other strings in the locale.
    - Current: `Offline Web Site Data`
    - Source: `Offline Website Data`
    - Suggest: `Offline Website Data`
    - en-GB uses "website" as one word, as elsewhere in the tree; "Web Site" is an unnecessary and inconsistent alteration of the source.
- `DefaultBrowserCard.Description` — `en-GB/firefox-ios.xliff` — "websites" rendered as "web sites", inconsistent with en-GB usage elsewhere.
    - Current: `links from web sites`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `links from websites`
    - The source says "websites"; en-GB writes this as one word, so the split form is an unwarranted, inconsistent change.
- `BreachAlerts.Title` — `en-GB/firefox-ios.xliff` — "Website" was needlessly changed to "Web Site", inconsistent with the term used elsewhere in the locale.
    - Current: `Web Site Breach`
    - Source: `Website Breach`
    - Suggest: `Website Breach`
    - en-GB uses "website" as one word, as in the related string BreachAlerts.Link ("Leads to a link to the breached website") and the source; "Web Site" is an unnecessary and inconsistent alteration.
- `ErrorPages.AdvancedWarning1.Text` — `en-GB/firefox-ios.xliff` — "website" was needlessly split into "web site", a form not used in en-GB and inconsistent with the rest of the locale.
    - Current: `web site`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `website`
    - en-US source uses "website"; en-GB uses the same closed compound. This is an over-correction that departs from the source without any British convention requiring it.
- `ErrorPages.CertWarning.Description` — `en-GB/firefox-ios.xliff` — "website" rendered as "web site" twice, an unnecessary and non-standard change.
    - Current: `has configured their web site improperly`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `has configured their website improperly`
    - The en-US source uses "website"; British English also uses "website" as one word. The split form is an over-correction.
- `HistoryPanel.EmptyState.Title` — `en-GB/firefox-ios.xliff` — "Websites" was split into "Web sites", an outdated form inconsistent with standard en-GB usage.
    - Current: `Web sites`
    - Source: `Websites you’ve visited recently will show up here.`
    - Suggest: `Websites`
    - en-GB does not require splitting "websites"; the closed compound is standard in British English and matches the en-US source.
- `Hotkeys.Forward.DiscoveryTitle` — `en-GB/firefox-ios.xliff` — Navigation command "Forward" changed to "Forwards", which is not the standard UI label for the browser Forward action.
    - Current: `Forwards`
    - Source: `Forward`
    - Suggest: `Forward`
    - The source is the browser navigation command "Forward" (paired with "Back"); en-GB uses the same noun/command form "Forward" in browser UI. "Forwards" is the adverb and also risks being read as the verb "forwards" (e.g. forwarding a message).
- `LibraryPanel.History.SyncedHistory.v100` — `en-GB/firefox-ios.xliff` — "Synced" was expanded to "Synchronised", changing the established Firefox Sync feature terminology.
    - Current: `Synchronised History`
    - Source: `Synced History`
    - Suggest: `Synced History`
    - "Synced" is the product term tied to the Firefox Sync feature and is used unchanged in en-GB; "Synchronised" is an unnecessary expansion that also lengthens a panel title on a phone screen.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `en-GB/firefox-ios.xliff` — "websites" has been split into "web sites", inconsistent with the rest of the locale which keeps "website(s)".
    - Current: `Web sites may load outside ads, videos and other content that contains hidden trackers. Blocking this can make web sites load faster`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `Websites may load outside ads, videos and other content that contains hidden trackers. Blocking this can make websites load faster`
    - en-GB does not require splitting "website"; other strings in this group (e.g. Menu.ReloadWithTrackingProtection.Title comment, Menu.Share.v99) use "website", making this an inconsistent adaptation.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `en-GB/firefox-ios.xliff` — "websites" has been split into "web sites", inconsistent with the locale's usual "websites".
    - Current: `trackers on other web sites to build`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `trackers on other websites to build`
    - en-GB uses "websites" as one word, as elsewhere in this locale; the split form is an unnecessary and inconsistent change from the source.
- `Settings.Appearance.WebsiteAppearance.SectionHeader.v137` — `en-GB/firefox-ios.xliff` — "Website" has been split into "Web Site", which is not a British English convention and is inconsistent with the rest of the locale.
    - Current: `Web Site Appearance`
    - Source: `Website Appearance`
    - Suggest: `Website Appearance`
    - en-GB uses "website" as a single word, exactly as en-US does; no spelling rule requires splitting it. The same file keeps "websites" elsewhere, so this is an inconsistent over-correction of the source term.
- `Settings.Appearance.WebsiteDarkMode.Description.v137` — `en-GB/firefox-ios.xliff` — "websites" rendered as "web sites", an unwarranted change from the source term.
    - Current: `Gives web sites a dark appearance.`
    - Source: `Gives websites a dark appearance. Some sites might not look right.`
    - Suggest: `Gives websites a dark appearance.`
    - British English writes "website" as one word, same as en-US; there is no locale rule requiring the two-word form.
- `Settings.Appearance.WebsiteDarkModeToggle.Title.v137` — `en-GB/firefox-ios.xliff` — "Website" split into "Web Site" in the toggle title.
    - Current: `Web Site Dark Mode`
    - Source: `Website Dark Mode`
    - Suggest: `Website Dark Mode`
    - en-GB does not split "website"; the change departs from the source term without any variant requirement and is inconsistent with other strings.
- `Settings.ClearAllWebsiteData.Clear.Button` — `en-GB/firefox-ios.xliff` — "Website" split into "Web Site" in the Clear All Website Data button.
    - Current: `Clear All Web Site Data`
    - Source: `Clear All Website Data`
    - Suggest: `Clear All Website Data`
    - British English uses "website" as one word, identical to en-US; the two-word form is an unwarranted change and lengthens the button label.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `en-GB/firefox-ios.xliff` — "websites" was needlessly split into "web sites", inconsistent with other en-GB strings that keep "websites".
    - Current: `web sites`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `websites`
    - en-GB uses "websites" as one word, as in Settings.WebsiteData.ButtonShowMore ("Button shows all websites...") and other strings; splitting it is an unwarranted change from the source.
- `Settings.WebsiteData.ConfirmPrompt` — `en-GB/firefox-ios.xliff` — "website data" rendered as "web site data", inconsistent with the rest of the locale.
    - Current: `web site data`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `website data`
    - The source says "website data"; en-GB does not require splitting the compound, and other strings in this file use "websites".
- `Settings.WebsiteData.Title` — `en-GB/firefox-ios.xliff` — "Website Data" was changed to "Web Site Data", which is not a British English variation and departs from the standard term used elsewhere.
    - Current: `Web Site Data`
    - Source: `Website Data`
    - Suggest: `Website Data`
    - "Website" is one word in British English as in en-US; splitting it into "Web Site" is an unwarranted change to a standard UI term.
- `TabTray.SegmentedControlTitles.SyncedTabs` — `en-GB/firefox-ios.xliff` — "Synced" was expanded to "Synchronised", inconsistent with the Sync product terminology used elsewhere in the locale and much longer for a segmented control on a phone.
    - Current: `Synchronised`
    - Source: `Synced`
    - Suggest: `Synced`
    - British English uses "Synced" for the Firefox Sync feature (cf. Sync.SyncingEllipsis.Label "Syncing…" and SyncState.Offline.Title "Sync is offline" kept unchanged); the longer form is inconsistent and risks truncation in a segmented control.
- `Website` — `en-GB/firefox-ios.xliff` — "Website" has been split into "Web Site", which is not a British English form and is inconsistent with the rest of the locale.
    - Current: `Web Site`
    - Source: `Website`
    - Suggest: `Website`
    - en-GB uses "Website" as a single word, identical to en-US; "Web Site" is an obsolete/US-styled form and an unnecessary, incorrect adaptation of the source label.
- `TodayWidget.TopSitesGalleryTitleV2` — `en-GB/firefox-ios.xliff` — "Website" has been split into "Web Site", which is not a British English convention and is inconsistent with the rest of the locale.
    - Current: `Web Site Shortcuts`
    - Source: `Website Shortcuts`
    - Suggest: `Website Shortcuts`
    - en-US source is "Website Shortcuts"; British English also writes "website" as one word, so this change is an unwarranted alteration of a standard term (elsewhere the locale uses "sites"/"website").

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

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
