# Firefox iOS l10n QA — da

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | baseline |
| **Strings reviewed this run** | 1,847 of 1,847 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




---

## Changes in this run

### 🆕 New findings (33)

- `AddressToolbar.GoogleLens.A11yLabel.v153.v2` — `da/firefox-ios.xliff` — "Søg efter billede" means searching for an image rather than searching using an image.
    - Current: `Søg efter billede med Google Lens`
    - Source: `Search image with Google Lens`
    - Suggest: `Søg med billede via Google Lens`
    - Per the developer comment, the user takes or selects a photo to search with Google Lens; the image is the query, not the target. "søge efter" means "look for".
- `Settings.AppIconSelection.AppIconNames.GoldenHour.Title.v137` — `da/firefox-ios.xliff` — Definite adjective form "Gyldne" is used without an article, which is ungrammatical.
    - Current: `Gyldne time`
    - Source: `Golden Hour`
    - Suggest: `Gylden time`
    - In Danish the weak form "gyldne" needs a definite article ("Den gyldne time"). Without one, the indefinite "Gylden time" is correct and matches "Blå time" for Blue Hour.
- `Settings.AppIconSelection.AppIconNames.SystemAuto.Title.v139` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated; Danish writes it as one word.
    - Current: `System-tema`
    - Source: `System Theme`
    - Suggest: `Systemtema`
    - Danish compounds of native words are written together; "System-tema" is a spelling error.
- `Logins.DevicePasscodeRequired.Message.v122` — `da/firefox-ios.xliff` — "autofylde" is inconsistent with "autoudfylde"/"autoudfyldning" used for autofill elsewhere in the same feature.
    - Current: `autofylde`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `autoudfylde`
    - The sibling string Logins.PaymentMethods.DevicePasscodeRequired.Message uses "autoudfylde", and the CredentialProvider strings use "autoudfyldning". "autofylde" is the odd one out for the same term.
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `da/firefox-ios.xliff` — The label leaves the English words "Village" and "Township" untranslated.
    - Current: `Village eller Township`
    - Source: `Village or Township`
    - Suggest: `Landsby eller kommune`
    - "Village" and "Township" are English, not Danish, so Danish users see an English field label. "Landsby" is the Danish word for village.
- `Addresses.Toast.AddressUpdatedConfirmation.v129` — `da/firefox-ios.xliff` — The compound noun has an unnecessary hyphen.
    - Current: `Adresse-oplysningerne`
    - Source: `Address Information Updated`
    - Suggest: `Adresseoplysningerne`
    - Danish compound nouns are written as one word. A hyphen is not used between "adresse" and "oplysninger".
- `Menu.EnhancedTrackingProtection.ClearData.AlertTitle.v128` — `da/firefox-ios.xliff` — The compound "websteds-data" is hyphenated, but it is written "webstedsdata" elsewhere on the same screen.
    - Current: `websteds-data`
    - Source: `Clear cookies and site data`
    - Suggest: `webstedsdata`
    - Danish normally writes compounds like this closed. The alert text and toast on the same screen already use "webstedsdata", so the two spellings are inconsistent.
- `Menu.EnhancedTrackingProtection.ClearData.ButtonTitle.v128` — `da/firefox-ios.xliff` — The compound "websteds-data" is hyphenated, but it is written "webstedsdata" elsewhere on the same screen.
    - Current: `websteds-data`
    - Source: `Clear cookies and site data`
    - Suggest: `webstedsdata`
    - Danish normally writes compounds like this closed. The alert text and toast on the same screen already use "webstedsdata", so the two spellings are inconsistent.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `da/firefox-ios.xliff` — The verb is in the infinitive "foreslå" where the present tense "foreslår" is required.
    - Current: `Vi foreslå,`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `Vi foreslår,`
    - "We suggest" needs the present tense in Danish. "Vi foreslå" is ungrammatical.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `da/firefox-ios.xliff` — The accessibility label calls the Tools submenu "værktøj", but the visible menu item and its other label say "Funktioner".
    - Current: `Undermenu for værktøj`
    - Source: `Tools submenu`
    - Suggest: `Undermenu for funktioner`
    - MainMenu.ToolsSection.ToolsSubmenu.Title.v131 and AccessibilityLabels.Tools.v132 translate "Tools" as "Funktioner". This label for the same submenu uses "værktøj", so VoiceOver reads a name that doesn't match what is shown on screen.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `da/firefox-ios.xliff` — "arkiveret" (archived) is used where the noun "arkivet" (the archive) is required.
    - Current: `Kontrollerer arkiveret…`
    - Source: `Checking the Archive…`
    - Suggest: `Kontrollerer arkivet…`
    - The source says "Checking the Archive…". "arkiveret" is a participle meaning "archived", so the label reads as a broken phrase. The definite noun "arkivet" is needed.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated as "virksomheds-netværk".
    - Current: `virksomheds-netværk`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `virksomhedsnetværk`
    - Danish writes compound nouns as one word. The hyphen here is a spelling error.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `da/firefox-ios.xliff` — The footer spells the compound "standard-browser" with a hyphen, but the popup title on the same screen writes it as one word, "standardbrowser".
    - Current: `standard-browser`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `standardbrowser`
    - Danish compounds are normally written as one word, and the title of the same popup (DefaultBrowserPopup.Title.v114) uses "standardbrowser". The footer should use the same spelling.
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148` — `da/firefox-ios.xliff` — Danish compound is incorrectly hyphenated.
    - Current: `sporings-mekanismer`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; there is no reason for a hyphen here.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `da/firefox-ios.xliff` — Danish compound is incorrectly hyphenated.
    - Current: `favorit-tema`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `favorittema`
    - Danish compounds are written as one word; the hyphenated form is a spelling error.
- `Onboarding.Welcome.Description.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `Onboarding.Welcome.Description.TreatementA.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `Onboarding.Modern.Welcome.Title.v145` — `da/firefox-ios.xliff` — The Danish compound is wrongly hyphenated.
    - Current: `sporings-mekanismer`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; the hyphen is a spelling error.
- `RelayMask.RelayEmailMaskSettingsDetailInfo.v147` — `da/firefox-ios.xliff` — The negation is missing, so the Danish now says that some sites support email masks.
    - Current: `Nogle websteder understøtter mail-masker.`
    - Source: `Hide your real email to protect your inbox from spam. Some sites don’t support email masks.`
    - Suggest: `Nogle websteder understøtter ikke mail-masker.`
    - The source warns that some sites don't support email masks, and the developer comment says the label must warn about this. Without "ikke" the warning becomes a positive statement, so users never get the warning.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `da/firefox-ios.xliff` — Passive "Tillad at %@ åbnes?" asks whether the app may be opened, instead of whether the app may open the scanned URL.
    - Current: `Tillad at %@ åbnes?`
    - Source: `Allow %@ to open?`
    - Suggest: `Tillad %@ at åbne?`
    - %@ is the app name (Firefox), which is already running when the QR code is scanned. The en-US asks for permission for Firefox to open the URL. The Danish passive means "Allow Firefox to be opened?".
- `Settings.Autoplay.Footer.v137` — `da/firefox-ios.xliff` — The adjective does not agree with its noun: "automatisk afspilninger" is ungrammatical.
    - Current: `Indstillinger for automatisk afspilninger`
    - Source: `Autoplay settings will only apply to newly opened tabs. Changes cannot be applied to existing tabs unless the application is restarted.`
    - Suggest: `Indstillinger for automatisk afspilning`
    - The singular adjective "automatisk" cannot go with the plural noun "afspilninger". The settings title for this feature already uses "Automatisk afspilning", so the singular is the consistent fix.
- `Settings.DailyUsagePing.Title.v135` — `da/firefox-ios.xliff` — Wrong gender agreement: "brug" is common gender, so the adjective must be "daglig", not "dagligt".
    - Current: `Ping for dagligt brug`
    - Source: `Daily Usage Ping`
    - Suggest: `Ping for daglig brug`
    - "brug" is a common-gender noun ("en brug"), so the adjective takes no -t ending: "daglig brug".
- `WebCompatReporter.Category.SiteNotUsable.v154` — `da/firefox-ios.xliff` — The predicate adjective "brugbar" doesn't agree with the neuter noun "webstedet".
    - Current: `Webstedet er ikke brugbar`
    - Source: `Site is not usable`
    - Suggest: `Webstedet er ikke brugbart`
    - "Websted" is a neuter noun (et websted), so a predicate adjective that refers to it needs the -t ending: "brugbart".
- `WebCompatReporter.SubOption.ItemsNotVisible.v154` — `da/firefox-ios.xliff` — This main clause uses subordinate-clause word order, so the sentence is ungrammatical.
    - Current: `Elementer ikke er fuldt synlige`
    - Source: `Items not fully visible`
    - Suggest: `Elementer er ikke fuldt synlige`
    - In a Danish main clause the verb comes before "ikke". The order "ikke er" is only correct after a subordinating conjunction such as "at", and there is none here.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `da/firefox-ios.xliff` — This compound noun is wrongly split with a hyphen.
    - Current: `sporings-mekanismer`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `sporingsmekanismer`
    - Danish writes compounds as one word. A hyphen is not standard for an ordinary compound like this.
- `CoverSheet.v24.ETP.Description` — `da/firefox-ios.xliff` — The hedge "helps stop" has become "forhindrer" (prevents), so the text now says tracking protection fully stops ads from following the user.
    - Current: `forhindrer reklamer i at følge dig`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `hjælper med at forhindre reklamer i at følge dig`
    - The en-US says Enhanced Tracking Protection "helps stop ads from following you". Dropping "helps" turns a partial claim into a guarantee the product does not make.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `da/firefox-ios.xliff` — The infinitive marker "at" is missing in "for kunne danne".
    - Current: `for kunne danne`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `for at kunne danne`
    - In Danish, a purpose clause needs "for at" + infinitive. Without "at", "for kunne danne" is ungrammatical.
- `Search.ThirdPartyEngines.AddMessage` — `da/firefox-ios.xliff` — The final full stop is missing at the end of the sentence.
    - Current: `i linjen "Hurtig søgning"`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `i linjen "Hurtig søgning".`
    - The en-US source is a full sentence ending with a period; the Danish ends without one.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated as "sporings-mekanismer".
    - Current: `sporings-mekanismer`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; the hyphen here is a spelling error.
- `TopSites.RemovePage.Button` — `da/firefox-ios.xliff` — A hyphen is used where the source has a dash between the label and the site title.
    - Current: `Fjern siden - %@`
    - Source: `Remove page — %@`
    - Suggest: `Fjern siden – %@`
    - The en-US uses an em dash as a separator. A spaced hyphen is not a dash in Danish typography, which uses a spaced en dash here. It also matches neither of the dashes the locale already uses.
- `TodayWidget.SearchInPrivateTabLabelV2` — `da/firefox-ios.xliff` — Singular 'Private Tab' rendered as plural 'private faneblade'.
    - Current: `Søg i private faneblade`
    - Source: `Search in Private Tab`
    - Suggest: `Søg i privat faneblad`
    - The source and comment say 'Search in private tab' (one new private tab); the Danish says 'search in private tabs'.
- `TodayWidget.TopSitesGalleryTitle` — `da/firefox-ios.xliff` — 'Sites' rendered as 'websider' (web pages) while the same widget's description and V2 title use 'websteder'.
    - Current: `Mest besøgte websider`
    - Source: `Top Sites`
    - Suggest: `Mest besøgte websteder`
    - 'Websider' means web pages, not sites; the same file uses 'websteder' for sites in TopSitesGalleryDescription and TopSitesGalleryTitleV2.
- `Mobile Bookmarks` — `da/firefox-ios.xliff` — Danish compound needlessly hyphenated.
    - Current: `Mobil-bogmærker`
    - Source: `Mobile Bookmarks`
    - Suggest: `Mobilbogmærker`
    - Danish writes compounds as one word; the other folder names in the file ('Bogmærkemenu', 'Bogmærkelinje') follow this.

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
| Strings | 1,847 |
| Missing strings | 80 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**80 strings** are not translated yet, concentrated in:

- `da/firefox-ios.xliff` — 34
- `Shared/Supporting Files/en-US.lproj/BrowserDataTransfer.strings` — 11
- `da/firefox-ios.xliff` — 11
- `da/firefox-ios.xliff` — 11
- `da/firefox-ios.xliff` — 4
- `da/firefox-ios.xliff` — 2
- `da/firefox-ios.xliff` — 2
- `da/firefox-ios.xliff` — 2
- `da/firefox-ios.xliff` — 1
- `Shared/Supporting Files/en-US.lproj/Camera.strings` — 1
- `da/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/BrowserDataTransfer.strings`
- `Shared/Supporting Files/en-US.lproj/Camera.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 17 | **straight-double** |
| apostrophe | `straight` 2 | **straight** |
| ellipsis | `char` 22 | **char** |
| dash | `em` 1, `en` 1 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (33)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Welcome.Description.TreatementA.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `Onboarding.Welcome.Description.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `CoverSheet.v24.ETP.Description` — `da/firefox-ios.xliff` — The hedge "helps stop" has become "forhindrer" (prevents), so the text now says tracking protection fully stops ads from following the user.
    - Current: `forhindrer reklamer i at følge dig`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `hjælper med at forhindre reklamer i at følge dig`
    - The en-US says Enhanced Tracking Protection "helps stop ads from following you". Dropping "helps" turns a partial claim into a guarantee the product does not make.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 23 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `AddressToolbar.GoogleLens.A11yLabel.v153.v2` — `da/firefox-ios.xliff` — "Søg efter billede" means searching for an image rather than searching using an image.
    - Current: `Søg efter billede med Google Lens`
    - Source: `Search image with Google Lens`
    - Suggest: `Søg med billede via Google Lens`
    - Per the developer comment, the user takes or selects a photo to search with Google Lens; the image is the query, not the target. "søge efter" means "look for".
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `da/firefox-ios.xliff` — The label leaves the English words "Village" and "Township" untranslated.
    - Current: `Village eller Township`
    - Source: `Village or Township`
    - Suggest: `Landsby eller kommune`
    - "Village" and "Township" are English, not Danish, so Danish users see an English field label. "Landsby" is the Danish word for village.
- `Onboarding.Welcome.Description.TreatementA.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `Onboarding.Welcome.Description.v120` — `da/firefox-ios.xliff` — "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
    - The source says the browser helps stop companies from tracking; the Danish asserts it prevents them outright, a promise the product does not make.
- `RelayMask.RelayEmailMaskSettingsDetailInfo.v147` — `da/firefox-ios.xliff` — The negation is missing, so the Danish now says that some sites support email masks.
    - Current: `Nogle websteder understøtter mail-masker.`
    - Source: `Hide your real email to protect your inbox from spam. Some sites don’t support email masks.`
    - Suggest: `Nogle websteder understøtter ikke mail-masker.`
    - The source warns that some sites don't support email masks, and the developer comment says the label must warn about this. Without "ikke" the warning becomes a positive statement, so users never get the warning.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `da/firefox-ios.xliff` — Passive "Tillad at %@ åbnes?" asks whether the app may be opened, instead of whether the app may open the scanned URL.
    - Current: `Tillad at %@ åbnes?`
    - Source: `Allow %@ to open?`
    - Suggest: `Tillad %@ at åbne?`
    - %@ is the app name (Firefox), which is already running when the QR code is scanned. The en-US asks for permission for Firefox to open the URL. The Danish passive means "Allow Firefox to be opened?".
- `CoverSheet.v24.ETP.Description` — `da/firefox-ios.xliff` — The hedge "helps stop" has become "forhindrer" (prevents), so the text now says tracking protection fully stops ads from following the user.
    - Current: `forhindrer reklamer i at følge dig`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `hjælper med at forhindre reklamer i at følge dig`
    - The en-US says Enhanced Tracking Protection "helps stop ads from following you". Dropping "helps" turns a partial claim into a guarantee the product does not make.
- `TodayWidget.SearchInPrivateTabLabelV2` — `da/firefox-ios.xliff` — Singular 'Private Tab' rendered as plural 'private faneblade'.
    - Current: `Søg i private faneblade`
    - Source: `Search in Private Tab`
    - Suggest: `Søg i privat faneblad`
    - The source and comment say 'Search in private tab' (one new private tab); the Danish says 'search in private tabs'.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.AppIconNames.GoldenHour.Title.v137` — `da/firefox-ios.xliff` — Definite adjective form "Gyldne" is used without an article, which is ungrammatical.
    - Current: `Gyldne time`
    - Source: `Golden Hour`
    - Suggest: `Gylden time`
    - In Danish the weak form "gyldne" needs a definite article ("Den gyldne time"). Without one, the indefinite "Gylden time" is correct and matches "Blå time" for Blue Hour.
- `Settings.AppIconSelection.AppIconNames.SystemAuto.Title.v139` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated; Danish writes it as one word.
    - Current: `System-tema`
    - Source: `System Theme`
    - Suggest: `Systemtema`
    - Danish compounds of native words are written together; "System-tema" is a spelling error.
- `Addresses.Toast.AddressUpdatedConfirmation.v129` — `da/firefox-ios.xliff` — The compound noun has an unnecessary hyphen.
    - Current: `Adresse-oplysningerne`
    - Source: `Address Information Updated`
    - Suggest: `Adresseoplysningerne`
    - Danish compound nouns are written as one word. A hyphen is not used between "adresse" and "oplysninger".
- `Menu.EnhancedTrackingProtection.ClearData.AlertTitle.v128` — `da/firefox-ios.xliff` — The compound "websteds-data" is hyphenated, but it is written "webstedsdata" elsewhere on the same screen.
    - Current: `websteds-data`
    - Source: `Clear cookies and site data`
    - Suggest: `webstedsdata`
    - Danish normally writes compounds like this closed. The alert text and toast on the same screen already use "webstedsdata", so the two spellings are inconsistent.
- `Menu.EnhancedTrackingProtection.ClearData.ButtonTitle.v128` — `da/firefox-ios.xliff` — The compound "websteds-data" is hyphenated, but it is written "webstedsdata" elsewhere on the same screen.
    - Current: `websteds-data`
    - Source: `Clear cookies and site data`
    - Suggest: `webstedsdata`
    - Danish normally writes compounds like this closed. The alert text and toast on the same screen already use "webstedsdata", so the two spellings are inconsistent.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `da/firefox-ios.xliff` — The verb is in the infinitive "foreslå" where the present tense "foreslår" is required.
    - Current: `Vi foreslå,`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `Vi foreslår,`
    - "We suggest" needs the present tense in Danish. "Vi foreslå" is ungrammatical.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated as "virksomheds-netværk".
    - Current: `virksomheds-netværk`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `virksomhedsnetværk`
    - Danish writes compound nouns as one word. The hyphen here is a spelling error.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `da/firefox-ios.xliff` — "arkiveret" (archived) is used where the noun "arkivet" (the archive) is required.
    - Current: `Kontrollerer arkiveret…`
    - Source: `Checking the Archive…`
    - Suggest: `Kontrollerer arkivet…`
    - The source says "Checking the Archive…". "arkiveret" is a participle meaning "archived", so the label reads as a broken phrase. The definite noun "arkivet" is needed.
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148` — `da/firefox-ios.xliff` — Danish compound is incorrectly hyphenated.
    - Current: `sporings-mekanismer`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; there is no reason for a hyphen here.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `da/firefox-ios.xliff` — Danish compound is incorrectly hyphenated.
    - Current: `favorit-tema`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `favorittema`
    - Danish compounds are written as one word; the hyphenated form is a spelling error.
- `Onboarding.Modern.Welcome.Title.v145` — `da/firefox-ios.xliff` — The Danish compound is wrongly hyphenated.
    - Current: `sporings-mekanismer`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; the hyphen is a spelling error.
- `Settings.Autoplay.Footer.v137` — `da/firefox-ios.xliff` — The adjective does not agree with its noun: "automatisk afspilninger" is ungrammatical.
    - Current: `Indstillinger for automatisk afspilninger`
    - Source: `Autoplay settings will only apply to newly opened tabs. Changes cannot be applied to existing tabs unless the application is restarted.`
    - Suggest: `Indstillinger for automatisk afspilning`
    - The singular adjective "automatisk" cannot go with the plural noun "afspilninger". The settings title for this feature already uses "Automatisk afspilning", so the singular is the consistent fix.
- `Settings.DailyUsagePing.Title.v135` — `da/firefox-ios.xliff` — Wrong gender agreement: "brug" is common gender, so the adjective must be "daglig", not "dagligt".
    - Current: `Ping for dagligt brug`
    - Source: `Daily Usage Ping`
    - Suggest: `Ping for daglig brug`
    - "brug" is a common-gender noun ("en brug"), so the adjective takes no -t ending: "daglig brug".
- `WebCompatReporter.Category.SiteNotUsable.v154` — `da/firefox-ios.xliff` — The predicate adjective "brugbar" doesn't agree with the neuter noun "webstedet".
    - Current: `Webstedet er ikke brugbar`
    - Source: `Site is not usable`
    - Suggest: `Webstedet er ikke brugbart`
    - "Websted" is a neuter noun (et websted), so a predicate adjective that refers to it needs the -t ending: "brugbart".
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `da/firefox-ios.xliff` — This compound noun is wrongly split with a hyphen.
    - Current: `sporings-mekanismer`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `sporingsmekanismer`
    - Danish writes compounds as one word. A hyphen is not standard for an ordinary compound like this.
- `WebCompatReporter.SubOption.ItemsNotVisible.v154` — `da/firefox-ios.xliff` — This main clause uses subordinate-clause word order, so the sentence is ungrammatical.
    - Current: `Elementer ikke er fuldt synlige`
    - Source: `Items not fully visible`
    - Suggest: `Elementer er ikke fuldt synlige`
    - In a Danish main clause the verb comes before "ikke". The order "ikke er" is only correct after a subordinating conjunction such as "at", and there is none here.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `da/firefox-ios.xliff` — The infinitive marker "at" is missing in "for kunne danne".
    - Current: `for kunne danne`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `for at kunne danne`
    - In Danish, a purpose clause needs "for at" + infinitive. Without "at", "for kunne danne" is ungrammatical.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `da/firefox-ios.xliff` — The compound noun is wrongly hyphenated as "sporings-mekanismer".
    - Current: `sporings-mekanismer`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `sporingsmekanismer`
    - Danish compounds are written as one word; the hyphen here is a spelling error.
- `Mobile Bookmarks` — `da/firefox-ios.xliff` — Danish compound needlessly hyphenated.
    - Current: `Mobil-bogmærker`
    - Source: `Mobile Bookmarks`
    - Suggest: `Mobilbogmærker`
    - Danish writes compounds as one word; the other folder names in the file ('Bogmærkemenu', 'Bogmærkelinje') follow this.

### D. Terminology, register & consistency

- `Logins.DevicePasscodeRequired.Message.v122` — `da/firefox-ios.xliff` — "autofylde" is inconsistent with "autoudfylde"/"autoudfyldning" used for autofill elsewhere in the same feature.
    - Current: `autofylde`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `autoudfylde`
    - The sibling string Logins.PaymentMethods.DevicePasscodeRequired.Message uses "autoudfylde", and the CredentialProvider strings use "autoudfyldning". "autofylde" is the odd one out for the same term.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `da/firefox-ios.xliff` — The accessibility label calls the Tools submenu "værktøj", but the visible menu item and its other label say "Funktioner".
    - Current: `Undermenu for værktøj`
    - Source: `Tools submenu`
    - Suggest: `Undermenu for funktioner`
    - MainMenu.ToolsSection.ToolsSubmenu.Title.v131 and AccessibilityLabels.Tools.v132 translate "Tools" as "Funktioner". This label for the same submenu uses "værktøj", so VoiceOver reads a name that doesn't match what is shown on screen.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `da/firefox-ios.xliff` — The footer spells the compound "standard-browser" with a hyphen, but the popup title on the same screen writes it as one word, "standardbrowser".
    - Current: `standard-browser`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `standardbrowser`
    - Danish compounds are normally written as one word, and the title of the same popup (DefaultBrowserPopup.Title.v114) uses "standardbrowser". The footer should use the same spelling.
- `TodayWidget.TopSitesGalleryTitle` — `da/firefox-ios.xliff` — 'Sites' rendered as 'websider' (web pages) while the same widget's description and V2 title use 'websteder'.
    - Current: `Mest besøgte websider`
    - Source: `Top Sites`
    - Suggest: `Mest besøgte websteder`
    - 'Websider' means web pages, not sites; the same file uses 'websteder' for sites in TopSitesGalleryDescription and TopSitesGalleryTitleV2.

### E. Typography, punctuation & spacing

- `Search.ThirdPartyEngines.AddMessage` — `da/firefox-ios.xliff` — The final full stop is missing at the end of the sentence.
    - Current: `i linjen "Hurtig søgning"`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `i linjen "Hurtig søgning".`
    - The en-US source is a full sentence ending with a period; the Danish ends without one.
- `TopSites.RemovePage.Button` — `da/firefox-ios.xliff` — A hyphen is used where the source has a dash between the label and the site title.
    - Current: `Fjern siden - %@`
    - Source: `Remove page — %@`
    - Suggest: `Fjern siden – %@`
    - The en-US uses an em dash as a separator. A spaced hyphen is not a dash in Danish typography, which uses a spaced en dash here. It also matches neither of the dashes the locale already uses.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/da/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
