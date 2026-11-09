# Firefox iOS l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3d5d050768b7` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3d5d050768b7` |
| **Previous run** | 2026-11-09 @ `372c1b986f13` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,903 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Strings | 1,903 |
| Missing strings | 80 |
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

**80 strings** are not translated yet, concentrated in:

- `sl/firefox-ios.xliff` — 35
- `sl/firefox-ios.xliff` — 20
- `sl/firefox-ios.xliff` — 8
- `sl/firefox-ios.xliff` — 6
- `sl/firefox-ios.xliff` — 5
- `sl/firefox-ios.xliff` — 2
- `sl/firefox-ios.xliff` — 2
- `sl/firefox-ios.xliff` — 1
- `sl/firefox-ios.xliff` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 15 | **straight-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 11 | **en** |
| register | `informal` 2, `formal` 64 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (24)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 12 |
| 3 | Degraded language (grammar, spelling, terminology) | 12 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `LoginsList.NoLoginsFound.Description.v122` — `sl/firefox-ios.xliff` — "All passwords you save are encrypted" is rendered as "all passwords are stored encrypted", dropping the restriction to saved passwords.
    - Current: `Vsa gesla so shranjena v šifrirani obliki.`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `Vsa gesla, ki jih shranite, so šifrirana.`
    - The source limits the claim to passwords the user saves; the translation asserts that all passwords are stored encrypted.
- `Menu.EnhancedTrackingProtection.Details.Trackers.v128` — `sl/firefox-ios.xliff` — "Trackers blocked" is translated as "Zavrnjenih sledilcev" (rejected) instead of blocked.
    - Current: `Zavrnjenih sledilcev: %@`
    - Source: `Trackers blocked: %@`
    - Suggest: `Blokiranih sledilcev: %@`
    - The source says blocked; elsewhere in the same file "blocks" is translated as "blokira", so "zavrnjenih" is both inaccurate and inconsistent.
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open email", saying only "open the default mail application".
    - Current: `Želite odpreti privzeto aplikacijo za e-pošto?`
    - Source: `Open email in the default mail application?`
    - Suggest: `Želite odpreti e-pošto v privzeti aplikaciji za e-pošto?`
    - Source is "Open email in the default mail application?"; the object of opening (the email) is lost.
- `ExternalLink.ExternalSmsLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open sms", saying only "open an external messaging application".
    - Current: `Želite odpreti zunanjo aplikacijo za sporočila?`
    - Source: `Open sms in an external application?`
    - Suggest: `Želite odpreti sporočilo SMS v zunanji aplikaciji?`
    - Source is "Open sms in an external application?"; the object of opening (the SMS) is lost.
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `sl/firefox-ios.xliff` — "Website URL" rendered as "Naslov spletne strani", omitting URL and using "spletna stran" instead of "spletno mesto".
    - Current: `Naslov spletne strani`
    - Source: `Website URL`
    - Suggest: `Naslov URL spletnega mesta`
    - The related alert description uses "naslov URL spletnega mesta" for the same concept; this placeholder is inconsistent with it.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `sl/firefox-ios.xliff` — "your support team" is rendered as "IT-služba" (IT department), introducing a term the source does not use.
    - Current: `vam morda lahko več informacij nudi IT-služba`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `ima morda več informacij vaša služba za podporo`
    - The en-US refers generically to "your support team", not specifically an IT department.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `sl/firefox-ios.xliff` — "Checking the Archive…" is rendered as "Iskanje po arhivu …" ("Searching the archive"), a noun phrase rather than the source's progress label, though meaning is close.
    - Current: `Iskanje po arhivu …`
    - Source: `Checking the Archive…`
    - Suggest: `Preverjanje arhiva …`
    - The source says "Checking the Archive…"; the Slovenian says "searching the archive", which duplicates the wording of the separate search string.
- `Onboarding.IntroDescriptionPart1.v114` — `sl/firefox-ios.xliff` — "For good" (meaning "for the benefit of all/for good causes") is rendered as "Za vedno" ("forever").
    - Current: `Neodvisni. Neprofitni. Za vedno.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Neodvisni. Neprofitni. Za dobro vseh.`
    - The source describes Firefox as being for good (a good cause); "Za vedno" means "forever", a different claim.
- `Onboarding.Modern.Sync.Description.v145` — `sl/firefox-ios.xliff` — "sync on any device" mistranslated as syncing "with any other device".
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says bookmarks, passwords and more sync on any device, not that they sync with some other single device; the added "drugo" (other) is not in the source and changes the meaning.
- `PrivacyDashboard.Fingerprinters.v155` — `sl/firefox-ios.xliff` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinters.
    - Current: `Sledilci prstnih odtisov`
    - Source: `Fingerprinters`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - Firefox sl uses "Sledilci prstnih odtisov naprav"/"Jemalci prstnih odtisov" for fingerprinters; the literal phrase suggests trackers that follow fingerprints rather than scripts that fingerprint the device.
- `Settings.AIControls.AIPoweredFeaturesSection.Title.v151` — `sl/firefox-ios.xliff` — "AI-POWERED FEATURES" translated as "MOŽNOSTI UMETNE INTELIGENCE" (features of AI) instead of features powered by AI.
    - Current: `MOŽNOSTI UMETNE INTELIGENCE`
    - Source: `AI-POWERED FEATURES`
    - Suggest: `MOŽNOSTI Z UMETNO INTELIGENCO`
    - The source describes features enhanced/powered by AI, not features belonging to AI.
- `Settings.AIControls.BlockedInformation.v151` — `sl/firefox-ios.xliff` — "Unblock specific features below" is rendered as "Določene možnosti lahko posebej omogočite spodaj", adding "lahko ... posebej" and losing the imperative, but more importantly the sentence structure changes the instruction.
    - Current: `Določene možnosti lahko posebej omogočite spodaj.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Spodaj odblokirajte posamezne možnosti.`
    - The source is an imperative instruction "Unblock specific features below."; the translation turns it into a statement of possibility.
- `Settings.Rollouts.Message.v148` — `sl/firefox-ios.xliff` — "features" is mistranslated and the list of items does not match the source.
    - Current: `bo izboljševal zmogljivosti, zanesljivost in učinkovitost delovanja`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `bo izboljševal funkcije, učinkovitost delovanja in stabilnost`
    - The source lists features, performance and stability; the translation drops "features" and renders the list as performance/reliability/performance.
- `Offline Website Data` — `sl/firefox-ios.xliff` — "Offline Website Data" translated as "Podatke pri delu brez povezave", dropping "Website".
    - Current: `Podatke pri delu brez povezave`
    - Source: `Offline Website Data`
    - Suggest: `Podatke spletnih strani brez povezave`
    - The source names data stored by websites for offline use; the translation says only "data when working offline", losing the website reference.
- `ErrorPages.CertWarning.Title` — `sl/firefox-ios.xliff` — Title says "Your connection is not private" instead of "This Connection is Untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Source: `This Connection is Untrusted`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US says the connection is untrusted; the Slovenian asserts it is not private, a different claim.
- `ScanQRCode.PermissionError.Message.v100` — `sl/firefox-ios.xliff` — The instruction to go to the device settings is reduced to "Izberite" (Select), dropping "device".
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’"; the reference to the device's Settings app is lost.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `sl/firefox-ios.xliff` — The placeholder (app name, e.g. Firefox) is given a Slovenian genitive suffix glued to it, producing "ikono Firefoxa" via "%@a" which mangles the brand name for other values.
    - Current: `Izberite ikono %@a`
    - Source: `Select the %@ app icon`
    - Suggest: `Izberite ikono aplikacije %@`
    - Appending the case ending directly to the placeholder alters the brand name string and breaks for any app name not ending in a consonant.
- `MainMenu.HeaderBanner.Subtitle.v142` — `sl/firefox-ios.xliff` — "Kadarkoli" should be written as two words ("kadar koli") and the plural "seconds" is rendered as singular.
    - Current: `Vzame vam sekundo. Kadarkoli lahko spremenite.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Vzame le nekaj sekund. Kadar koli lahko spremenite.`
    - en-US says "Takes seconds" (plural, a few seconds); the Slovenian says "takes you a second". Also, Slovenian orthography requires "kadar koli" as two words.
- `VPN.ReachedDataLimitPopup.ClosedXTabs.v160` — `sl/firefox-ios.xliff` — Fixed genitive plural "zavihkov zaprtih" is ungrammatical for counts 2–4 (the comment's own example is 3).
    - Current: `%1$@ zavihkov zaprtih`
    - Source: `Closed %1$@ Tabs`
    - Suggest: `Zaprti zavihki: %1$@`
    - The string has no plural variants, so a single form is used for every count above one. In Slovenian "zavihkov zaprtih" is correct only for 5 and above. For 2 it should be "zavihka zaprta" and for 3–4 "zavihki zaprti", and the comment gives 3 as an example. A form that works for any number avoids the agreement error.
- `SendTo.NoDevicesFound.Message` — `sl/firefox-ios.xliff` — "Firefox Računom" uses English-style capitalization and word order for "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `S tem računom Firefox`
    - In Slovenian the generic noun is lowercase and follows the brand name: "račun Firefox".

### D. Terminology, register & consistency

- `Scan QR Code` — `sl/firefox-ios.xliff` — QR code term inconsistent with "kode QR" used in NSCameraUsageDescription.
    - Current: `Skeniraj QR-kodo`
    - Source: `Scan QR Code`
    - Suggest: `Skeniraj kodo QR`
    - The same source term "QR code" is rendered "kode QR" elsewhere in the same file; one form should be used.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `sl/firefox-ios.xliff` — "site data" is translated as "podatki spletnega mesta" here but as "podatke strani" in the related alert/button strings on the same screen.
    - Current: `Piškotki in podatki spletnega mesta odstranjeni`
    - Source: `Cookies and site data removed`
    - Suggest: `Piškotki in podatki strani odstranjeni`
    - Terminology inconsistency within the same feature: Menu.EnhancedTrackingProtection.ClearData.AlertTitle/ButtonTitle use "podatke strani".
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `sl/firefox-ios.xliff` — "Tracking content" is rendered as "Sledilna vsebina" but the developer comment identifies analytics trackers; more importantly the label is inconsistent with the other tracker rows which use the genitive count pattern.
    - Current: `Sledilna vsebina: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledilne vsebine: %@`
    - The other rows on the same screen (Piškotkov za sledenje..., Sledilcev prstnih odtisov..., Sledilcev družbenih omrežij...) use the genitive counting form; this row breaks the pattern on the same screen.
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `sl/firefox-ios.xliff` — Abbreviation "UI" for AI is used here and in BlockedInformation, while other strings on the same screen spell out "umetne inteligence"; inconsistent terminology within one screen.
    - Current: `Prepovej izboljšave s pomočjo UI`
    - Source: `Block AI Enhancements`
    - Suggest: `Prepovej izboljšave z umetno inteligenco`
    - The same source term "AI" is rendered as both "umetna inteligenca" and "UI" on the same settings screen.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (2)

- `FxA.FirefoxAccount` — `sl/firefox-ios.xliff` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; likely reason (inferred): The original capitalizes "Račun", so it likely treats "Firefox Račun" as a fixed product name, and the reviewer probably kept that brand form instead of reordering it into an ordinary noun phrase.
- `Settings.Studies.Title.v148` — `sl/firefox-ios.xliff` — pontoon-rejected (2026-11-04): rejected in Pontoon without comment; reason unclear

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (31)

- `Alerts.RestoreTabs.Message.v109` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string 2112de14): "Oprostite." is the standard formal Slovenian apology equivalent to "Sorry (about that)".
- `CreditCard.Settings.Yes.v122` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string ef6a551a): The quoted text "Posodobim kartico?" is not in this string; the translation "Posodobi" correctly renders "Update".
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string 85acf892): Slovenian Mozilla products consistently render tracker blocking with 'zavračati/zavrniti' (cf. 'Zavračanje' in string 10), so 'zavrne' is the established term.
- `Enter passcode` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 3ec7da51): unreliable finding: "geslo" is a plausible rendering, and nothing visible shows which passcode term the file uses.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string 48d8d948): The quoted text "Prijavi nedelujočo stran …" does not appear in this translation, which has no ellipsis.
- `Menu.Share.v99` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string c33ddeac): "Deli" is the usual Slovenian Mozilla label for the Share command.
- `NSLocationWhenInUseUsageDescription` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 14bbba07): unreliable finding: Omitting 'you visit' does not change the practical meaning; the translation is plausibly acceptable.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string d3acda8b): Singular imperative is the standard Slovenian button form (cf. "Posodobi", "Dovoli"); the reviewer's own suggestion keeps "nadaljuj".
- `PzSrmZ-2GqvPe` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string 984e0ea4): The sl tree mostly uses straight double quotes (13 vs 2 curly), so they are the locale's convention.
- `PzSrmZ-eHmH1H` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string b8f37ed5): The sl tree mostly uses straight double quotes (13 vs 2 curly), so they are the locale's convention.
- `PzSrmZ-scEmjs` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string 9076ae3b): The sl tree mostly uses straight double quotes (13 vs 2 curly), so they are the locale's convention.
- `PzSrmZ-xRJbBP` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-03, string a772c74b): The sl tree mostly uses straight double quotes (13 vs 2 curly), so they are the locale's convention.
- `SentTab_TabArrivingNotification_WithDevice_title` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 155dc453): unreliable finding: "z" + device name is a normal way to say a tab came from a device; "iz" would be a preference, not a correction.
- `Settings.BlockOpeningExternalApps.Title` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 0c3b3d24): unreliable finding: Slovenian Mozilla localizations commonly render 'block' as 'zavrni/zavračanje', so this is plausibly established terminology rather than an error.
- `Settings.FxA.Title` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string f7b01f8a): unreliable finding: 'Firefox Račun' may be a deliberate product-name rendering of 'Firefox Account'; the established sl form cannot be confirmed from here.
- `Settings.NoImageModeBlockImages.Label.v99` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 2088c97e): unreliable finding: 'Zavračaj/zavrni' is the commonly used sl Mozilla term for blocking content, so the claim that 'blokiraj' is established cannot be confirmed.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string b581f424): unreliable finding: The wording is understandable as a setting description, and in this app the tab and address bar can be a single combined bar, so changing it would be a matter of style.
- `Settings.Siri.SectionDescription` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 24c5d52f): unreliable finding: Siri is still named in the sentence ('s Siri'), so the meaning is conveyed; the change is stylistic.
- `Settings.Studies.Message.v148` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string aa170d32): unreliable finding: Studies test new features, so "preizkušanje novosti" (testing new things) gets the meaning across; switching to "funkcij" would be a preference.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 6ef4e42a): unreliable finding: For tabs, 'odprli' (opened/visited) is a natural way to say 'viewed'; the meaning is preserved.
- `Settings.TechnicalData.Message.v136` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 58f2457b): unreliable finding: "zmogljivosti, delovanje in zanesljivost" is a reasonable way to say capabilities/features, performance and stability, and "nastavitev strojne opreme" is an acceptable rendering of hardware configuration.
- `Settings.TrackingProtection.Info.BlocksTitle` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 0a12b5e2): unreliable finding: 'Zavrnjeno' matches the 'zavrni' terminology sl uses for blocking, so this is plausibly consistent rather than wrong.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 0148e86d): unreliable finding: This accessibility label gets the action across correctly; the formal-versus-informal phrasing is a style choice, not a mistranslation.
- `Summarizer.ToS.InfoPanel.Title.Label.v143` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string d8035e69): unreliable finding: First-person prompts like "Povzamem…?" are a common, natural way to ask questions in Slovenian UI, so this cannot be confirmed as an error.
- `TabTrayOneDayAgoTitle.v140` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 2e7846e5): unreliable finding: All three time strings use the same genitive form, which suggests they were fitted to a surrounding phrase; the suggested "1 dan" would also drop "ago", so the right fix depends on context I can't see.
- `TabTrayOneMonthAgoTitle.v140` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 46df1983): unreliable finding: Same genitive form as the sibling strings, which suggests a surrounding phrase; "1 mesec" would lose "ago", so this can't be confirmed without context.
- `TabTrayOneWeekAgoTitle.v140` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string eb7fb2fc): unreliable finding: Same genitive form as the sibling strings, which suggests a surrounding phrase; "1 teden" would lose "ago", so this can't be confirmed without context.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string c59b84b6): unreliable finding: "Stran" is a reasonable word for the sheet in a screen-reader announcement; dropping it would be a style choice.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 7d9dae70): unreliable finding: The noun phrase is an acceptable label for a sub-option; changing it to a clause would only be a style choice.
- `WebCompatReporter.SubOption.MissingItems.v154` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string 25fc0261): unreliable finding: In a web-page compatibility reporter, "strani" is a harmless clarification and doesn't change the meaning.
- `WebCompatReporter.Toast.ReportSent.v155` — `sl/firefox-ios.xliff` — auto-suggest (2026-11-09, string ff0f6ce4): unreliable finding: The sibling strings that supposedly use "prijava" can't be checked here, and "Poročilo poslano" is a correct translation.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (23)

- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Summarizer.Error.RateLimited.Message.v142` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Upgrade.SyncSign.Description.v114` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `ContextMenu.GoogleLensButtonTitle.v153` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `FirefoxHome.Stories.Minutes.v140` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Menu.TrackingProtectionDescription.ContentTrackers` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Menu.TrackingProtectionDescription.CryptominersNew` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Search.ThirdPartyEngines.AddMessage` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `SendTo.NotSignedIn.Title` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `Settings.ClearAllWebsiteData.Clear.Button` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `You don’t have any tabs open in Firefox on your other devices.` — `sl/firefox-ios.xliff` — fixed 2026-11-05
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `sl/firefox-ios.xliff` — fixed 2026-11-05
