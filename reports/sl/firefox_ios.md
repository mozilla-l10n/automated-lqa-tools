# Firefox iOS l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 10 of 1,929 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [android](android.md) · [firefox](firefox.md)

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
| Files | 97 |
| Strings | 1,929 |
| Missing strings | 21 |
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

**21 strings** are not translated yet, concentrated in:

- `sl/firefox-ios.xliff` — 16
- `sl/firefox-ios.xliff` — 5

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 13, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 10 | **en** |
| register | `informal` 2, `formal` 64 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (89)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, so the Slovenian states unconditionally that downloaded AI models will be removed.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki se izvaja na napravi, bodo odstranjeni vsi preneseni modeli.`
    - en-US limits the model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation makes it a general statement about the product's behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 41 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSLocationWhenInUseUsageDescription` — `sl/firefox-ios.xliff` — "Websites you visit" is rendered as just "Spletne strani", dropping "you visit".
    - Current: `Spletne strani lahko zahtevajo vašo lokacijo.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Spletne strani, ki jih obiščete, lahko zahtevajo vašo lokacijo.`
    - The en-US limits the claim to websites the user visits; the translation drops that qualifier.
- `Alerts.RestoreTabs.Message.v109` — `sl/firefox-ios.xliff` — "Sorry about that" is rendered as "Oprostite" (imperative "excuse me/forgive"), which reads as addressing the user rather than an apology.
    - Current: `Oprostite.`
    - Source: `Sorry about that. Restore tabs to pick up where you left off.`
    - Suggest: `Oprostite za nevšečnost.`
    - The source is an apology by the app for the crash; "Oprostite." alone is a bare imperative that does not convey the apology naturally.
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
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `sl/firefox-ios.xliff` — "expiration date" translated as "leto poteka" (expiration year).
    - Current: `Vnesite veljavno leto poteka`
    - Source: `Enter a valid expiration date`
    - Suggest: `Vnesite veljaven datum poteka`
    - The source asks for a valid expiration date, not year.
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
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — "marketing partners" is rendered as "tehnološkim partnerjem ... za trženje", introducing "technology" that the source never mentions.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The en-US says only "%2$@’s marketing partners"; the word "tehnološkim" (technology) is not in the source and changes who the data is shared with.
- `Onboarding.Modern.Sync.Description.v145` — `sl/firefox-ios.xliff` — "sync on any device" mistranslated as syncing "with any other device".
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says bookmarks, passwords and more sync on any device, not that they sync with some other single device; the added "drugo" (other) is not in the source and changes the meaning.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `sl/firefox-ios.xliff` — "Manage settings" is translated only as "Nastavitve" ("Settings"), dropping the verb.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - The source is an action link "Manage settings"; the translation loses the "manage" part.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `sl/firefox-ios.xliff` — "for everyone" is translated as "za uporabnike po vsem svetu" ("for users all over the world").
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The source says the data helps improve things for everyone, not specifically for users worldwide.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `sl/firefox-ios.xliff` — "for everyone" is rendered as "for users around the world", adding a claim the source does not make.
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The en-US says features, performance and stability improve "for everyone"; the Slovenian asserts "for users all over the world", which is not what the source says.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `sl/firefox-ios.xliff` — "Limited Edition Wallpaper" translated without the word "wallpaper".
    - Current: `Omejena izdaja`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Ozadje omejene izdaje`
    - The source is an accessibility label describing the wallpaper type; the parallel string uses "Klasično ozadje", so dropping "ozadje" loses the object being described.
- `PrivacyDashboard.Fingerprinters.v155` — `sl/firefox-ios.xliff` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinters.
    - Current: `Sledilci prstnih odtisov`
    - Source: `Fingerprinters`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - Firefox sl uses "Sledilci prstnih odtisov naprav"/"Jemalci prstnih odtisov" for fingerprinters; the literal phrase suggests trackers that follow fingerprints rather than scripts that fingerprint the device.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `sl/firefox-ios.xliff` — The translation reads "Allow opening of %@?" making the app the object being opened, instead of allowing the app to open (the scanned URL).
    - Current: `Dovoli odpiranje %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Ali dovolite, da %@ odpre povezavo?`
    - Per the comment, %@ is the app name and the prompt asks permission for the app to open a URL from the scanned QR code; the Slovenian instead asks permission to open the app itself.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, so the Slovenian states unconditionally that downloaded AI models will be removed.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki se izvaja na napravi, bodo odstranjeni vsi preneseni modeli.`
    - en-US limits the model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation makes it a general statement about the product's behaviour.
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
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `sl/firefox-ios.xliff` — "Search Browsing History" is rendered as "search history" instead of "browsing history".
    - Current: `Iskanje po zgodovini iskanja`
    - Source: `Search Browsing History`
    - Suggest: `Iskanje po zgodovini brskanja`
    - The source refers to browsing history (zgodovina brskanja), not search history.
- `Settings.Studies.Message.v148` — `sl/firefox-ios.xliff` — "features" translated as "novosti" (new things) rather than features.
    - Current: `za preizkušanje novosti`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `za preizkušanje funkcij`
    - The source says users are selected to test features; "novosti" means novelties/new items and is inconsistent with "funkcije" used elsewhere.
- `Settings.TechnicalData.Message.v136` — `sl/firefox-ios.xliff` — "hardware configuration" mistranslated as "nastavitvi strojne opreme" (hardware setting) and "features" dropped/merged.
    - Current: `nastavitvi strojne opreme in uporabi nam pomagajo izboljševati zmogljivosti, delovanje in zanesljivost`
    - Source: `Data about your device, hardware configuration, and usage helps us improve %@ features, performance and stability.`
    - Suggest: `nastavitvah strojne opreme in uporabi nam pomagajo izboljševati funkcije, zmogljivost in stabilnost`
    - The source lists "features, performance and stability"; the target lists "zmogljivosti, delovanje in zanesljivost", losing "features" and rendering "configuration" as a singular setting.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `sl/firefox-ios.xliff` — The a11y label is translated as an instruction to the user instead of naming the button action.
    - Current: `Poskusite znova za povzetek spletne strani`
    - Source: `Retry to summarize web page`
    - Suggest: `Znova poskusi povzeti spletno stran`
    - Source "Retry to summarize web page" labels the button action; also inconsistent with the button label "Poskusi znova" (imperative 2nd person singular) for the same control.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `sl/firefox-ios.xliff` — "Terms of Use sheet opened" translated as "Stran s pogoji uporabe odprta" ("page" instead of the bottom sheet/panel).
    - Current: `Stran s pogoji uporabe odprta`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Pogoji uporabe odprti`
    - The source refers to a bottom sheet, not a page; the app elsewhere uses "pogoji uporabe" without "stran".
- `WebCompatReporter.SubOption.MissingItems.v154` — `sl/firefox-ios.xliff` — "Missing items" translated as "Manjkajoči elementi strani", adding "strani" (of the page) not present in the source.
    - Current: `Manjkajoči elementi strani`
    - Source: `Missing items`
    - Suggest: `Manjkajoči elementi`
    - The source says only "Missing items"; "strani" adds information the source does not state.
- `ContextMenu.GoogleLensButtonTitle.v153` — `sl/firefox-ios.xliff` — "Search Image" (singular, the specific image) rendered as plural "slike", changing the meaning to searching for images generally.
    - Current: `Išči slike z Google Lens`
    - Source: `Search Image with Google Lens`
    - Suggest: `Išči sliko z Google Lens`
    - The source refers to searching for the selected image with Google Lens, not for images in general.
- `WorldCup.CountryPicker.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "World Cup country picker" mistranslated as "country picker at the World Cup" instead of the picker belonging to the World Cup widget.
    - Current: `Zapri izbirnik držav na svetovnem prvenstvu`
    - Source: `Close World Cup country picker`
    - Suggest: `Zapri izbirnik držav svetovnega prvenstva`
    - The label closes the World Cup country picker; "na svetovnem prvenstvu" reads as being located at the championship.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Description.v151` — `sl/firefox-ios.xliff` — "Choose another team" is rendered as "Choose some other team whose progress you want to follow", altering the meaning.
    - Current: `Izberite še kakšno ekipo, katere napredek na svetovnem prvenstvu želite spremljati.`
    - Source: `Choose another team to keep up with the World Cup.`
    - Suggest: `Izberite drugo ekipo, da boste v koraku s svetovnim prvenstvom.`
    - The source says to choose another team to keep up with the World Cup; the target says to choose yet another team whose progress at the World Cup you want to follow, which changes the meaning ("še kakšno" = one more, in addition).
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `sl/firefox-ios.xliff` — "Still want to Follow Along?" is reduced to "Are you still interested?", dropping the sense of continuing to follow.
    - Current: `Vas še zanima?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Bi radi še naprej spremljali dogajanje?`
    - The source asks whether the user wants to keep following along; the target's vague "Are you still interested?" loses that meaning.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `sl/firefox-ios.xliff` — "Please refresh." is translated as "Refresh the widget.", adding an object not in the source.
    - Current: `Osvežite pripomoček.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Osvežite.`
    - The source is a generic "Please refresh." without specifying the widget.
- `WorldCup.HomepageWidget.FollowTeamCard.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "updates" translated as "podatke" (data) instead of updates/news.
    - Current: `Skrij podatke o svetovnem prvenstvu`
    - Source: `Hide World Cup updates`
    - Suggest: `Skrij novosti o svetovnem prvenstvu`
    - The source refers to World Cup updates, not to data.
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `sl/firefox-ios.xliff` — "live match updates" is rendered as "receive updates live", shifting "live" from the matches to the receiving.
    - Current: `V živo prejemajte obvestila o dogajanju na tekmah in še več.`
    - Source: `Get live match updates and more.`
    - Suggest: `Prejemajte obvestila o dogajanju na tekmah v živo in še več.`
    - In en-US "live" modifies the match updates; the Slovene word order attaches it to the act of receiving.
- `WorldCup.HomepageWidget.RoundPhase.ScrollIndicatorAccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "matches" mistranslated as "zadetke" (goals/hits) instead of "tekme".
    - Current: `Pomaknite se na prejšnje ali naslednje zadetke`
    - Source: `Scroll to see previous or next matches`
    - Suggest: `Pomaknite se na prejšnje ali naslednje tekme`
    - The source refers to previous or next matches (tekme); "zadetki" means goals or search hits, not matches.
- `Offline Website Data` — `sl/firefox-ios.xliff` — "Offline Website Data" translated as "Podatke pri delu brez povezave", dropping "Website".
    - Current: `Podatke pri delu brez povezave`
    - Source: `Offline Website Data`
    - Suggest: `Podatke spletnih strani brez povezave`
    - The source names data stored by websites for offline use; the translation says only "data when working offline", losing the website reference.
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `sl/firefox-ios.xliff` — "blocks" trackers translated as "zavrne" (rejects/declines) instead of "blokira/zablokira".
    - Current: `Firefox vsak mesec zavrne povprečno več kot 3000 sledilcev na uporabnika.`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `Firefox vsak mesec blokira povprečno več kot 3000 sledilcev na uporabnika.`
    - The product's established term for blocking trackers is "blokira"; "zavrne" describes a different action.
- `ErrorPages.CertWarning.Title` — `sl/firefox-ios.xliff` — Title says "Your connection is not private" instead of "This Connection is Untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Source: `This Connection is Untrusted`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US says the connection is untrusted; the Slovenian asserts it is not private, a different claim.
- `Hotkeys.Forward.DiscoveryTitle` — `sl/firefox-ios.xliff` — Ambiguous/wrong rendering: source "Forward" refers to navigating forward in session history, and the translation reads as "Next"; however per the comment context it should be navigation forward.
    - Current: `Naprej`
    - Source: `Forward`
    - Suggest: `Naprej (po zgodovini)`
    - The paired Back shortcut is "Nazaj"; "Naprej" is acceptable but the developer comment describes switching to a subsequent tab. Low-risk ambiguity.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sl/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as "Spletni sledilci" (web trackers), losing the cross-site meaning.
    - Current: `Spletni sledilci`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledilci med spletnimi mesti`
    - The source specifies trackers that follow users across sites; "Spletni sledilci" just means "web trackers" and does not convey "cross-site".
- `Menu.TrackingProtectionDescription.ContentTrackers` — `sl/firefox-ios.xliff` — Translation drops "outside" ads and omits "login fields" from the list of things that might not work.
    - Current: `vendar nekateri gumbi in obrazci morda ne bodo delovali`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `vendar nekateri gumbi, obrazci in prijavna polja morda ne bodo delovali`
    - The en-US lists "buttons, forms, and login fields"; the Slovenian omits login fields.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `sl/firefox-ios.xliff` — "secretly use your system's computing power" loses "secretly", and "increase your energy bill" is rendered with the colloquial "zasolijo račun".
    - Current: `Kriptorudarji izrabljajo zmogljivost vašega računalnika za rudarjenje digitalnega denarja.`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Kriptorudarji na skrivaj izrabljajo računsko zmogljivost vašega sistema za rudarjenje digitalnega denarja.`
    - The source says cryptominers "secretly use your system’s computing power"; the omission of "secretly" drops meaning.
- `ScanQRCode.PermissionError.Message.v100` — `sl/firefox-ios.xliff` — The instruction to go to the device settings is reduced to "Izberite" (Select), dropping "device".
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’"; the reference to the device's Settings app is lost.
- `Settings.BlockOpeningExternalApps.Title` — `sl/firefox-ios.xliff` — "Block" translated as "Zavrni" (reject/decline) instead of "Prepreči"/"Blokiraj".
    - Current: `Zavrni odpiranje zunanjih aplikacij`
    - Source: `Block Opening External Apps`
    - Suggest: `Prepreči odpiranje zunanjih aplikacij`
    - The setting blocks external apps from opening; "zavrni" implies a one-time refusal rather than a persistent block.
- `Settings.NoImageModeBlockImages.Label.v99` — `sl/firefox-ios.xliff` — "Block Images" translated as "Zavračaj slike" (reject images) instead of "Zavrni/Blokiraj slike".
    - Current: `Zavračaj slike`
    - Source: `Block Images`
    - Suggest: `Blokiraj slike`
    - The source means blocking images from loading; "zavračaj" (reject) is not the established term for blocking content in Firefox sl, which uses "blokiraj".
- `Settings.Siri.SectionDescription` — `sl/firefox-ios.xliff` — "Siri shortcuts" rendered as just "bližnjice", dropping Siri from the phrase.
    - Current: `Uporabi bližnjice za hitro odpiranje Firefoxa s Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Uporabite bližnjice Siri za hitro odpiranje Firefoxa s Siri`
    - The source says "Use Siri shortcuts…"; the translation omits "Siri" as the qualifier of shortcuts.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `sl/firefox-ios.xliff` — "haven't viewed" is rendered as "niste odprli" (haven't opened) — different action.
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - The source says tabs you haven't viewed for two weeks; opening and viewing are different actions.
- `Settings.TrackingProtection.Info.BlocksTitle` — `sl/firefox-ios.xliff` — "BLOCKS" (list of blocked sites/trackers) translated as "ZAVRNJENO" (rejected/declined) instead of "BLOKIRANO"/"ZAVRNJENI".
    - Current: `ZAVRNJENO`
    - Source: `BLOCKS`
    - Suggest: `BLOKIRANO`
    - The header labels a list of blocked websites; "zavrnjeno" means rejected, not blocked, and is inconsistent with the blocking terminology used elsewhere.
- `You don’t have any tabs open in Firefox on your other devices.` — `sl/firefox-ios.xliff` — Added word "drugih" changes the meaning to "no other tabs open".
    - Current: `V Firefoxu na drugih napravah nimate odprtih drugih zavihkov.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `V Firefoxu na drugih napravah nimate odprtih zavihkov.`
    - The source says the user has no tabs open; the translation says no *other* tabs are open, implying some tabs exist.
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `sl/firefox-ios.xliff` — "New" is dropped, so the option reads "Open in private tab" instead of "Open in New Private Tab".
    - Current: `Odpri v zasebnem zavihku`
    - Source: `Open in New Private Tab`
    - Suggest: `Odpri v novem zasebnem zavihku`
    - The source says "Open in New Private Tab"; the translation omits "New", changing the action's meaning (an existing vs. a new tab).

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
- `TabTrayOneDayAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Day Ago" rendered as "1 dneva", an ungrammatical number-noun agreement (should be "1 dan" / "1 dnevom").
    - Current: `1 dneva`
    - Source: `1 Day Ago`
    - Suggest: `1 dan`
    - In Slovenian the numeral 1 takes the nominative singular "dan", not the genitive/dual form "dneva"; the source is "1 Day Ago".
- `TabTrayOneMonthAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Month Ago" rendered as "1 meseca", wrong case/number agreement with the numeral 1.
    - Current: `1 meseca`
    - Source: `1 Month Ago`
    - Suggest: `1 mesec`
    - Numeral 1 requires singular nominative "mesec"; "meseca" is dual/genitive and is ungrammatical here.
- `TabTrayOneWeekAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Week Ago" rendered as "1 tedna", wrong case/number agreement with the numeral 1.
    - Current: `1 tedna`
    - Source: `1 Week Ago`
    - Suggest: `1 teden`
    - Numeral 1 requires singular nominative "teden"; "tedna" is dual/genitive and is ungrammatical here.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `sl/firefox-ios.xliff` — Sentence "Captions are missing" rendered as a noun phrase "Manjkajoči napisi", inconsistent with the other sub-options which are full clauses.
    - Current: `Manjkajoči napisi`
    - Source: `Captions are missing`
    - Suggest: `Napisi manjkajo`
    - Source is a clause ("Captions are missing"), like the sibling options rendered as clauses ("Gumbi ali povezave ne delujejo").
- `FxA.FirefoxAccount` — `sl/firefox-ios.xliff` — "Firefox Račun" uses English word order; Slovenian requires "Račun Firefox".
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Račun Firefox`
    - Slovenian noun phrase order places the brand after the noun; also the common noun should not be capitalized mid-phrase.
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sl/firefox-ios.xliff` — Misspelling of "Logotip" as "Logtip".
    - Current: `Logtip Firefoxa`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logotip Firefoxa`
    - The Slovenian word for "logo" is "logotip"; "Logtip" is a typo.
- `Search.ThirdPartyEngines.AddMessage` — `sl/firefox-ios.xliff` — Typo: "isklanik" should be "iskalnik".
    - Current: `Novi isklanik se bo pojavil v vrstici za hitro iskanje.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Novi iskalnik se bo pojavil v vrstici za hitro iskanje.`
    - The Slovenian word for "search engine" is "iskalnik"; the letters are transposed.
- `SendTo.NoDevicesFound.Message` — `sl/firefox-ios.xliff` — "Firefox Računom" uses English-style capitalization and word order for "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `S tem računom Firefox`
    - In Slovenian the generic noun is lowercase and follows the brand name: "račun Firefox".
- `SendTo.NotSignedIn.Title` — `sl/firefox-ios.xliff` — Incorrect case and unnecessary possessive pronoun; also "Firefox Račun" should not be capitalized mid-phrase as two nouns.
    - Current: `Niste prijavljeni v vaš Firefox Račun.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Niste prijavljeni v svoj račun Firefox.`
    - Slovenian requires the reflexive possessive "svoj", and the noun order/capitalization "Firefox Račun" is a calque of English; correct form is "račun Firefox".
- `SentTab_TabArrivingNotification_WithDevice_title` — `sl/firefox-ios.xliff` — Wrong preposition/case for device name: "z %@" should be "iz naprave %@" or "z naprave %@" — but here the source says "from %@" meaning received from a device.
    - Current: `Zavihek prejet z %@`
    - Source: `Tab received from %@`
    - Suggest: `Zavihek prejet iz %@`
    - The placeholder holds a device name; "prejet z %@" is ungrammatical/ambiguous, standard Slovenian uses "iz" for origin from a device.
- `Settings.ClearAllWebsiteData.Clear.Button` — `sl/firefox-ios.xliff` — "all website data" rendered with a singular noun phrase, so it reads "all data of the website".
    - Current: `Izbriši vse podatke spletne strani`
    - Source: `Clear All Website Data`
    - Suggest: `Izbriši vse podatke spletnih strani`
    - The source clears data for all websites; the singular genitive "spletne strani" restricts it to one site.
- `Settings.FxA.Title` — `sl/firefox-ios.xliff` — Brand-plus-noun compound needs Slovenian possessive form and lowercase noun.
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Firefoxov račun`
    - "Firefox Račun" is an ungrammatical calque of English title case; Slovenian requires "Firefoxov račun" (cf. "Firefoxova domača stran" used elsewhere in this batch).
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `sl/firefox-ios.xliff` — Missing contrastive conjunction "vendar"/"a" before the second clause; two clauses are joined by a comma only.
    - Current: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni.`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni`
    - Source contrasts with "but"; the Slovenian uses only "pa" which is acceptable, so this should not be reported.

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
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `sl/firefox-ios.xliff` — Informal imperative "nadaljuj" breaks the locale's formal register.
    - Current: `Strinjam se, nadaljuj`
    - Source: `Agree and continue`
    - Suggest: `Strinjam se in nadaljuj`
    - The sl locale uses the formal register; button text mixing first-person "Strinjam se" with informal imperative "nadaljuj" is inconsistent with the established address form used elsewhere ("Strinjam se in nadaljuj").
- `CreditCard.Settings.Yes.v122` — `sl/firefox-ios.xliff` — Inconsistent question/answer register: the prompt uses first person ("Posodobim kartico?") while other prompts use the formal second person ("Želite varno shraniti to kartico?").
    - Current: `Posodobim kartico?`
    - Source: `Update`
    - Suggest: `Želite posodobiti kartico?`
    - The locale convention is formal address; CreditCard.Settings.RememberThisCard.v122 on the same screen uses "Želite …", so "Posodobim kartico?" is inconsistent.
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `sl/firefox-ios.xliff` — Abbreviation "UI" for AI is used here and in BlockedInformation, while other strings on the same screen spell out "umetne inteligence"; inconsistent terminology within one screen.
    - Current: `Prepovej izboljšave s pomočjo UI`
    - Source: `Block AI Enhancements`
    - Suggest: `Prepovej izboljšave z umetno inteligenco`
    - The same source term "AI" is rendered as both "umetna inteligenca" and "UI" on the same settings screen.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `sl/firefox-ios.xliff` — Setting label turned into an instruction addressed to the user instead of a noun-style toggle title.
    - Current: `Podrsajte, da skrijete vrstico z zavihki in naslovom`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Drsenje skrije vrstico z zavihki in naslovno vrstico`
    - En-US is a settings toggle title "Scroll to Hide Tab and Address Bar"; the Slovenian reads as a command telling the user to swipe, and merges the two bars into one.
- `Settings.Studies.Title.v148` — `sl/firefox-ios.xliff` — "Feature Studies" rendered as "raziskave značilnosti" instead of the established term for features ("funkcije").
    - Current: `Dovoli raziskave značilnosti`
    - Source: `Allow Feature Studies`
    - Suggest: `Dovoli raziskave funkcij`
    - Elsewhere in this file "features" is translated as "funkcije" (e.g. Settings.Studies.Message.v136: "Preizkusite funkcije in ideje"); "značilnosti" is inconsistent terminology for feature studies.
- `Summarizer.Error.RateLimited.Message.v142` — `sl/firefox-ios.xliff` — The impersonal source is rendered in the first person, making the app speak as "I".
    - Current: `Tega trenutno ne morem narediti.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Tega trenutno ni mogoče narediti.`
    - The en-US "Can't handle this one at the moment." is impersonal; Slovenian UI convention avoids first-person app voice, and the rest of the file uses impersonal forms.
- `Summarizer.ToS.InfoPanel.Title.Label.v143` — `sl/firefox-ios.xliff` — "Summarize this page?" is rendered in the first person singular ("Shall I summarize").
    - Current: `Povzamem vsebino strani?`
    - Source: `Summarize this page?`
    - Suggest: `Želite povzeti vsebino strani?`
    - The source is a neutral question; the Slovenian first-person verb makes the app speak as "I", which conflicts with the formal, impersonal register used elsewhere.
- `WebCompatReporter.Toast.ReportSent.v155` — `sl/firefox-ios.xliff` — "Report" rendered as "Poročilo" here but as "prijava" in the other Report screens/buttons, breaking terminology consistency.
    - Current: `Poročilo poslano`
    - Source: `Report sent`
    - Suggest: `Prijava poslana`
    - Same source term "report" is translated "prijava" in WebCompatReporter.SendButton.Title and Preview.Title within the same feature.
- `Enter passcode` — `sl/firefox-ios.xliff` — "passcode" translated as "geslo" (password) instead of a passcode term.
    - Current: `Vnesite geslo`
    - Source: `Enter passcode`
    - Suggest: `Vnesite geslo za dostop`
    - In this file "password" and "passcode" are distinct; "geslo" is the established rendering of "password", making the passcode/password distinction disappear.
- `FirefoxHome.Stories.Minutes.v140` — `sl/firefox-ios.xliff` — "minut" is not abbreviated although the comment requires an abbreviation due to space constraints.
    - Current: `minut: %d`
    - Source: `min: %d`
    - Suggest: `min: %d`
    - Developer comment states minutes should be abbreviated due to space constraints; the source uses "min".
- `Menu.Share.v99` — `sl/firefox-ios.xliff` — "Share" translated as "Deli" (divide/share in the arithmetic sense) instead of the established "Deli z drugimi"/"Souporaba".
    - Current: `Deli`
    - Source: `Share`
    - Suggest: `Deli z drugimi`
    - In Mozilla sl terminology the share action is "Deli z drugimi"; bare "Deli" reads as the imperative of "divide".

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “Zaznamki”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `Shranjeno v mapo "Zaznamki"`
    - The sl convention is straight-double quotes; the sibling string Bookmarks.Menu.DeletedBookmark.v131 uses straight quotes.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “%@”`
    - Source: `Saved in “%@”`
    - Suggest: `Shranjeno v mapo "%@"`
    - The sl convention is straight-double quotes; the sibling toast string uses straight quotes.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `sl/firefox-ios.xliff` — Space inserted before the ellipsis character.
    - Current: `Prijavi nedelujočo stran …`
    - Source: `Turn off Reader View`
    - Suggest: `Prijavi nedelujočo stran…`
    - The en-US "Report Broken Site…" has no space before the ellipsis; Slovenian should follow the same typography.
- `Upgrade.SyncSign.Description.v114` — `sl/firefox-ios.xliff` — Hyphen used as a sentence dash instead of the house en dash.
    - Current: `kjer ste končali - z zavihki`
    - Source: `Pick up where you left off with tabs from other devices now on your homepage.`
    - Suggest: `kjer ste končali – z zavihki`
    - The locale convention is the en dash; a hyphen-minus is used here as a parenthetical dash.
- `PzSrmZ-2GqvPe` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Pojdi na kopirano povezavo"`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `„Pojdi na kopirano povezavo“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-eHmH1H` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Počisti zasebne zavihke"`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `„Počisti zasebne zavihke“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-scEmjs` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Novo zasebno iskanje"`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `„Novo zasebno iskanje“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-xRJbBP` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Novo iskanje"`
    - Source: `Just to confirm, you wanted ‘New Search’?`
    - Suggest: `„Novo iskanje“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
