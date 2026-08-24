# Firefox iOS l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **Previous run** | 2026-08-22 @ `112744e9d020` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,910 |

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
| quotes | `straight-double` 13, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 20 | **char** |
| dash | `en` 10 | **en** |
| register | `informal` 2, `formal` 65 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (74)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 26 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

- `CloseTab.ArrivingNotification.title.v133` — `sl/firefox-ios.xliff` — The two placeholders are swapped in meaning: %1$@ is the app name and %2$@ the tab count, but the translation reads as if %1$@ were the number.
    - Current: `Zaprtih %1$@ zavihkov: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ – zaprti zavihki: %2$@`
    - Per the developer comment %1$@ is the app name (e.g. Firefox) and %2$@ is the number of tabs; the Slovenian places the app name where a number belongs ("Zaprtih Firefox zavihkov: 5"), producing nonsense.

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSLocationWhenInUseUsageDescription` — `sl/firefox-ios.xliff` — The translation drops "you visit" from the source.
    - Current: `Spletne strani lahko zahtevajo vašo lokacijo.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Spletne strani, ki jih obiščete, lahko zahtevajo vašo lokacijo.`
    - en-US says "Websites you visit may request your location"; the qualifier "you visit" is omitted.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `sl/firefox-ios.xliff` — "%@ is off-duty" rendered as "%@ does not protect you".
    - Current: `%@ vas ne varuje.`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `%@ je na dopustu.`
    - The source's idiom means protections are currently paused/off-duty; the target asserts the app does not protect you at all.
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `sl/firefox-ios.xliff` — "expiration date" translated as "leto poteka" (expiration year).
    - Current: `Vnesite veljavno leto poteka`
    - Source: `Enter a valid expiration date`
    - Suggest: `Vnesite veljaven datum poteka`
    - The source asks for a valid expiration date, not just the year.
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation says "Open the default email application?" instead of "Open email in the default mail application?".
    - Current: `Želite odpreti privzeto aplikacijo za e-pošto?`
    - Source: `Open email in the default mail application?`
    - Suggest: `Želite odpreti e-pošto v privzeti aplikaciji za e-pošto?`
    - The object of "open" in the source is the email, opened in the default mail application; the target drops the email.
- `ExternalLink.ExternalSmsLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation says "Open an external application for messages?" instead of "Open sms in an external application?".
    - Current: `Želite odpreti zunanjo aplikacijo za sporočila?`
    - Source: `Open sms in an external application?`
    - Suggest: `Želite odpreti SMS v zunanji aplikaciji?`
    - The source opens the SMS in an external app; the target drops the SMS object.
- `MainMenu.HeaderBanner.Subtitle.v142` — `sl/firefox-ios.xliff` — "Takes seconds" (plural) is rendered as singular "Vzame vam sekundo" (takes one second).
    - Current: `Vzame vam sekundo.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Vzame le nekaj sekund.`
    - The source says it takes seconds (a few seconds), not one second.
- `Onboarding.IntroDescriptionPart1.v114` — `sl/firefox-ios.xliff` — "For good" (meaning 'for the benefit of all / for good causes') is rendered as "Za vedno" ("forever").
    - Current: `Za vedno.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Za dobro vseh.`
    - En-US "For good." in this Mozilla context means acting for good/benefit, not 'permanently'; "Za vedno" reverses the sense to a time expression.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — "marketing partners" is translated as "tehnološkim partnerjem ... za trženje", introducing "technology" which is not in the source.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The source says only "%2$@’s marketing partners"; "tehnološkim" (technology) adds content that is not in the English string.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManageLink.v148` — `sl/firefox-ios.xliff` — "Manage settings" is rendered only as "Nastavitve", dropping the "manage" action.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - Source is "Manage settings", a link that takes the user to manage data collection preferences; the translation says just "Settings".
- `Onboarding.Modern.BrandRefresh.Welcome.TitleV3.v149` — `sl/firefox-ios.xliff` — The word "all" from "Open all your links" is dropped, making it identical to the v2 string.
    - Current: `Odpirajte povezave z vgrajeno zasebnostjo`
    - Source: `Open all your links with built-in privacy`
    - Suggest: `Odpirajte vse povezave z vgrajeno zasebnostjo`
    - The en-US v149 title adds "all" ("Open all your links") compared to the v2 title; the translation omits it.
- `Onboarding.Modern.Sync.Description.v145` — `sl/firefox-ios.xliff` — "sync on any device" is rendered as syncing "with any other device", changing the meaning.
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says your bookmarks and passwords sync on any device (they are available on all devices), not that they sync with some other single device.
- `Onboarding.Modern.TermsOfService.Description.v145` — `sl/firefox-ios.xliff` — "trusted for over 20 years" is translated as "which you have trusted for over 20 years", addressing the individual user instead of general trust.
    - Current: `ki ji zaupate že več kot 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `ki ji ljudje zaupajo že več kot 20 let`
    - The source states the non-profit has been trusted (by people generally) for over 20 years; the translation asserts the individual user has trusted it for 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `sl/firefox-ios.xliff` — "Manage settings" is translated only as "Nastavitve" (Settings), dropping the verb.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - The source is "Manage settings", a link to manage data collection preferences; the translation omits "Manage".
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `sl/firefox-ios.xliff` — "for everyone" is mistranslated as "for users all over the world".
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users all over the world", which adds meaning not present in the en-US text.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `sl/firefox-ios.xliff` — Accessibility label drops the word "Wallpaper" present in the source and in the parallel Classic string.
    - Current: `Omejena izdaja`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Ozadje omejene izdaje`
    - Source is "Limited Edition Wallpaper"; the sibling string "Classic Wallpaper" is translated as "Klasično ozadje", so this accessibility label should also state that it is a wallpaper.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `sl/firefox-ios.xliff` — The translation reverses the roles: it says "Allow opening of %@" instead of allowing the app (%@) to open the URL.
    - Current: `Dovoli odpiranje %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Ali dovolite, da %@ odpre povezavo?`
    - The developer comment states %@ is the app name (e.g. Firefox); the source asks permission for the app to open a URL. The Slovenian reads as permission to open the app itself.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, changing the scope of the second sentence.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki teče na napravi, bodo odstranjeni vsi preneseni modeli.`
    - The en-US restricts model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation omits this condition.
- `Settings.AIControls.BlockedInformation.v151` — `sl/firefox-ios.xliff` — "Unblock specific features below" is rendered as "omogočite" (enable) losing the unblock sense and the wording adds "posebej".
    - Current: `Določene možnosti lahko posebej omogočite spodaj.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Prepoved za posamezne možnosti lahko odpravite spodaj.`
    - Source says to unblock specific features; the section otherwise uses "prepoved/prepovedano" terminology, so "omogočite" is inconsistent with the block/unblock wording.
- `Settings.Rollouts.Message.v148` — `sl/firefox-ios.xliff` — The list "features, performance, and stability" is mistranslated; "features" is dropped and replaced by duplicated performance terms.
    - Current: `bo izboljševal zmogljivosti, zanesljivost in učinkovitost delovanja med posodobitvami`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `bo izboljševal funkcije, zmogljivost in stabilnost med posodobitvami`
    - en-US lists features, performance and stability; the translation omits "features" and renders the remaining items inaccurately.
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `sl/firefox-ios.xliff` — "Search Browsing History" is rendered as "search history" instead of "browsing history".
    - Current: `Iskanje po zgodovini iskanja`
    - Source: `Search Browsing History`
    - Suggest: `Iskanje po zgodovini brskanja`
    - The source refers to browsing history (zgodovina brskanja), not search history (zgodovina iskanja).
- `Settings.Summarize.GesturesSection.FooterTitle.v142` — `sl/firefox-ios.xliff` — The detail "from side to side" is dropped from the shake gesture description.
    - Current: `Potresite napravo, da povzamete vsebino strani.`
    - Source: `Shake your device from side to side to summarize a page.`
    - Suggest: `Napravo potresite z ene strani na drugo, da povzamete vsebino strani.`
    - en-US says "Shake your device from side to side"; the manner of the gesture is omitted in the translation.
- `Settings.Translation.AutoTranslate.Footer.v151` — `sl/firefox-ios.xliff` — "your top preferred language" is translated as merely "vaš izbrani jezik", losing the notion of the highest-ranked preferred language.
    - Current: `Samodejno prevede strani v vaš izbrani jezik.`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `Samodejno prevede strani v vaš najbolj prednostni jezik.`
    - The source refers to the first/top language in the Preferred Languages list, not just any selected language.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `sl/firefox-ios.xliff` — "Spread the word" is rendered as the literal calque "Širite besedo", which is not idiomatic Slovenian and does not convey the meaning.
    - Current: `Širite besedo o %1$@u`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `Razširite glas o %1$@u`
    - en-US "Spread the word about %1$@" means to tell others about the app; "širite besedo" is a literal word-for-word calque that does not carry that meaning in Slovenian.
- `TabTrayOneDayAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Day Ago" is rendered as "1 dneva", which is ungrammatical and drops the meaning of the time reference.
    - Current: `1 dneva`
    - Source: `1 Day Ago`
    - Suggest: `1 dan`
    - The menu items follow "Zapri zavihke, starejše od …", so the correct genitive singular is "enega dne"/"1 dneva" is wrong agreement with numeral 1; as a standalone label it should read "1 dan" (or "pred 1 dnevom").
- `WorldCup.CountryPicker.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "World Cup country picker" mistranslated as "country picker at the World Cup".
    - Current: `Zapri izbirnik držav na svetovnem prvenstvu`
    - Source: `Close World Cup country picker`
    - Suggest: `Zapri izbirnik držav svetovnega prvenstva`
    - The English means the country picker belonging to the World Cup widget; "na svetovnem prvenstvu" states the picker is located at the championship.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Description.v151` — `sl/firefox-ios.xliff` — Translation adds "progress of that team" and paraphrases rather than rendering "keep up with the World Cup".
    - Current: `Izberite še kakšno ekipo, katere napredek na svetovnem prvenstvu želite spremljati.`
    - Source: `Choose another team to keep up with the World Cup.`
    - Suggest: `Izberite drugo ekipo in ostanite na tekočem s svetovnim prvenstvom.`
    - en-US says "Choose another team to keep up with the World Cup"; the Slovenian shifts the object of following to the team's progress and renders "another" as "some other/one more".
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `sl/firefox-ios.xliff` — The title drops the meaning of "follow along", leaving a vague question.
    - Current: `Vas še zanima?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Želite še naprej spremljati dogajanje?`
    - en-US "Still want to Follow Along?" asks whether the user wants to keep following the World Cup; the translation only says "Are you still interested?", losing the follow/track meaning central to this widget.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `sl/firefox-ios.xliff` — "Please refresh." is rendered as "Refresh the widget", adding an object not in the source.
    - Current: `Osvežite pripomoček.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Osvežite.`
    - The source says only "Please refresh." without specifying the widget; the added noun changes the instruction's content.
- `WorldCup.HomepageWidget.FollowTeamCard.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "updates" translated as "podatki" (data) instead of updates/news.
    - Current: `Skrij podatke o svetovnem prvenstvu`
    - Source: `Hide World Cup updates`
    - Suggest: `Skrij novosti o svetovnem prvenstvu`
    - The source "Hide World Cup updates" refers to updates/news, not generic data.
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `sl/firefox-ios.xliff` — "live match updates" is mistranslated as receiving notifications "live".
    - Current: `V živo prejemajte obvestila o dogajanju na tekmah in še več.`
    - Source: `Get live match updates and more.`
    - Suggest: `Prejemajte obvestila o dogajanju na tekmah v živo in še več.`
    - In the source "live" modifies the matches/updates, not the act of receiving; the Slovenian word order attaches "v živo" to the receiving.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `sl/firefox-ios.xliff` — Singular "match info" rendered as plural "podatki o tekmah".
    - Current: `Podatki o tekmah ta trenutek niso na voljo.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Podatki o tekmi trenutno niso na voljo.`
    - The source refers to the info of the displayed match (singular); the widget shows one match at a time.
- `WorldCup.HomepageWidget.RoundPhase.ScrollIndicatorAccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "matches" is translated as "zadetki" (goals/hits) instead of "tekme" (matches).
    - Current: `Pomaknite se na prejšnje ali naslednje zadetke`
    - Source: `Scroll to see previous or next matches`
    - Suggest: `Pomaknite se na prejšnje ali naslednje tekme`
    - The source refers to navigating between matches in the widget; "zadetki" means goals or search hits, and the rest of the file uses "tekma" for match.
- `ErrorPages.CertWarning.Title` — `sl/firefox-ios.xliff` — Title says "Your connection is not private" instead of "This connection is untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Source: `This Connection is Untrusted`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US source is "This Connection is Untrusted", which is about trust, not privacy.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sl/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as "Spletni sledilci" (web trackers), losing the cross-site meaning.
    - Current: `Spletni sledilci`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledilci med spletnimi mesti`
    - The source specifies trackers that follow users across sites; "Spletni sledilci" just means "web trackers" and drops the cross-site distinction, which is the key differentiator from the other categories on the same screen.
- `ScanQRCode.PermissionError.Message.v100` — `sl/firefox-ios.xliff` — The word "device" is dropped from the instruction to go to the device Settings.
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’", clarifying it is the iOS device settings, not the app's own settings.
- `Settings.Disconnect.Button` — `sl/firefox-ios.xliff` — "Disconnect Sync" translated without the Sync component, making it identical to the generic "Disconnect" button.
    - Current: `Prekini povezavo`
    - Source: `Disconnect Sync`
    - Suggest: `Prekini sinhronizacijo`
    - The source distinguishes "Disconnect Sync" from "Disconnect" (Settings.Disconnect.DestructiveButton); both are rendered identically, dropping the Sync reference.
- `Settings.Siri.SectionDescription` — `sl/firefox-ios.xliff` — The translation drops "Siri" from "Siri shortcuts".
    - Current: `Uporabi bližnjice za hitro odpiranje Firefoxa s Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Uporabite bližnjice Siri za hitro odpiranje Firefoxa prek Siri`
    - The en-US source says "Use Siri shortcuts"; the Slovenian says only "Uporabi bližnjice", losing the Siri qualifier used elsewhere (Settings.Siri.SectionName: "Bližnjice Siri").
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `sl/firefox-ios.xliff` — "haven’t viewed" is translated as "niste odprli" (haven't opened).
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - The source refers to tabs not viewed for two weeks, not tabs not opened.
- `Settings.TrackingProtection.Info.BlocksTitle` — `sl/firefox-ios.xliff` — "BLOCKS" (list of blocked items) is rendered as "ZAVRNJENO" (rejected/declined) instead of blocked.
    - Current: `ZAVRNJENO`
    - Source: `BLOCKS`
    - Suggest: `BLOKIRANO`
    - The header labels a list of blocked websites/trackers; "zavrnjeno" means rejected/refused, not blocked, and is inconsistent with blocking terminology.
- `You don’t have any tabs open in Firefox on your other devices.` — `sl/firefox-ios.xliff` — Translation adds "drugih" (other tabs), changing the meaning of the message.
    - Current: `V Firefoxu na drugih napravah nimate odprtih drugih zavihkov.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `V Firefoxu na drugih napravah nimate odprtih zavihkov.`
    - The source says the user has no tabs open at all on other devices; "drugih zavihkov" implies no *other* tabs are open.
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `sl/firefox-ios.xliff` — Translation drops "New" from "Open in New Private Tab".
    - Current: `Odpri v zasebnem zavihku`
    - Source: `Open in New Private Tab`
    - Suggest: `Odpri v novem zasebnem zavihku`
    - The source specifies opening in a *new* private tab; the target says only "in a private tab".

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `sl/firefox-ios.xliff` — The placeholder (app name, e.g. "Firefox") is given a suffixed genitive ending "-a", which mangles the brand name in the accessibility hint.
    - Current: `Izberite ikono %@a`
    - Source: `Select the %@ app icon`
    - Suggest: `Izberite ikono aplikacije %@`
    - Source is "Select the %@ app icon"; %@ is the app name. Appending an inflectional "a" directly to the placeholder produces forms like "Firefoxa" glued to the substituted brand string, altering the brand name and breaking for other app names (e.g. Klar, Focus).
- `MainMenu.HeaderBanner.Subtitle.v142` — `sl/firefox-ios.xliff` — "Kadarkoli" should be written as two words in standard Slovenian.
    - Current: `Kadarkoli lahko spremenite.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Kadar koli lahko spremenite.`
    - Slovenian orthography writes indefinite pronoun/adverb + koli separately: 'kadar koli'.
- `Microsurvey.Prompt.LogoImage.AccessibilityLabel.v129` — `sl/firefox-ios.xliff` — The declension suffix "a" is appended directly to the app-name placeholder, producing an incorrect form such as "Logotip Firefoxa" only by chance and breaking for other app names.
    - Current: `Logotip %@a`
    - Source: `%@ Logo`
    - Suggest: `Logotip %@`
    - %@ is substituted with the app name verbatim; appending a case ending to a placeholder is not valid and yields wrong output for names that do not take -a (e.g. Focus, Klar).
- `Summarizer.RetryButton.Accessibility.Label.v145` — `sl/firefox-ios.xliff` — The a11y label for the retry button uses a second-person plural imperative addressed to the user instead of an action label matching the button's own action.
    - Current: `Poskusite znova za povzetek spletne strani`
    - Source: `Retry to summarize web page`
    - Suggest: `Poskusi znova povzeti spletno stran`
    - The visible button label (Summarizer.RetryButton.Label.v142) is "Poskusi znova"; the accessibility label for the same control should use the same imperative form for consistency.
- `ContextMenu.GoogleLensButtonTitle.v153` — `sl/firefox-ios.xliff` — Singular "Search Image" rendered as plural "Išči slike".
    - Current: `Išči slike z Google Lens`
    - Source: `Search Image with Google Lens`
    - Suggest: `Išči sliko z Google Lens`
    - The source refers to searching for a single image (the one right-clicked), not images in general.
- `Offline Website Data` — `sl/firefox-ios.xliff` — Settings item is in the accusative case and mistranslates "Offline Website Data" as "data while working offline".
    - Current: `Podatke pri delu brez povezave`
    - Source: `Offline Website Data`
    - Suggest: `Podatki spletnih strani brez povezave`
    - The en-US source is a noun-phrase settings item "Offline Website Data"; the Slovenian uses the accusative "Podatke" instead of the nominative and drops "website" entirely.
- `FxA.FirefoxAccount` — `sl/firefox-ios.xliff` — Improper capitalization/word order in "Firefox Račun".
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Račun Firefox`
    - Slovenian does not capitalize the common noun mid-phrase, and the standard rendering of "Firefox Account" is "Račun Firefox".
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sl/firefox-ios.xliff` — Misspelling of "logotip" as "Logtip".
    - Current: `Logtip Firefoxa, spremeni ozadje.`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logotip Firefoxa, spremeni ozadje.`
    - The source says "Firefox logo"; the Slovenian word is "logotip", not "Logtip".
- `Search.ThirdPartyEngines.AddMessage` — `sl/firefox-ios.xliff` — Misspelled "iskalnik" as "isklanik".
    - Current: `Novi isklanik se bo pojavil`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Novi iskalnik se bo pojavil`
    - "isklanik" is a typo; the correct Slovenian word for search engine is "iskalnik", as used in the neighbouring strings.
- `SendTo.NoDevicesFound.Message` — `sl/firefox-ios.xliff` — "Firefox Računom" incorrectly capitalizes and leaves untranslated-style the product term "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `S tem Računom Firefox`
    - In Slovenian the noun follows the brand name; "Firefox Računom" is an English word-order calque with wrong capitalization of the common noun.
- `SendTo.NotSignedIn.Title` — `sl/firefox-ios.xliff` — "v vaš Firefox Račun" uses English word order/capitalization and a redundant possessive.
    - Current: `Niste prijavljeni v vaš Firefox Račun.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Niste prijavljeni v svoj Račun Firefox.`
    - Slovenian requires the reflexive possessive "svoj" and places the common noun before the brand name; "Firefox Račun" is an English calque.
- `Settings.ClearAllWebsiteData.Clear.Button` — `sl/firefox-ios.xliff` — "Website Data" is rendered in the singular genitive, contradicting "all" (plural sites).
    - Current: `Izbriši vse podatke spletne strani`
    - Source: `Clear All Website Data`
    - Suggest: `Izbriši podatke vseh spletnih strani`
    - en-US "Clear All Website Data" clears data for all sites; the Slovenian says "all data of the website" (one site).
- `Settings.FxA.Title` — `sl/firefox-ios.xliff` — "Firefox Račun" uses English word order/capitalization; Slovenian should be "Račun Firefox".
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Račun Firefox`
    - Slovenian does not place a brand name attributively before a noun with capitalized common noun; the standard rendering is "Račun Firefox" (or "Firefoxov račun"). "Račun" should also not be capitalized mid-phrase.
- `Settings.WebsiteData.ConfirmPrompt` — `sl/firefox-ios.xliff` — "all of your website data" is translated with a singular "spletne strani", implying one website.
    - Current: `vse podatke spletne strani`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `vse podatke spletnih strani`
    - The source refers to data of all websites (plural); the singular genitive suggests a single site.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `sl/firefox-ios.xliff` — Adjective "domač" should be "domači" (definite form) in "domači zaslon".
    - Current: `na domač zaslon`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `na domači zaslon`
    - Slovenian requires the definite adjective form for the fixed term "domači zaslon" (Home screen); "domač zaslon" is ungrammatical here.

### D. Terminology, register & consistency

- `Scan QR Code` — `sl/firefox-ios.xliff` — "QR code" is rendered inconsistently with the other InfoPlist string that uses "kode QR".
    - Current: `Skeniraj QR-kodo`
    - Source: `Scan QR Code`
    - Suggest: `Skeniraj kodo QR`
    - NSCameraUsageDescription in the same file uses "kode QR"; the same term should be consistent within the screen/file.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `sl/firefox-ios.xliff` — "site data" is rendered as "podatki spletnega mesta" here but as "podatki strani" in the other clear-data strings on the same screen.
    - Current: `Piškotki in podatki spletnega mesta odstranjeni`
    - Source: `Cookies and site data removed`
    - Suggest: `Piškotki in podatki strani odstranjeni`
    - The same source term "site data" appears in AlertTitle, ButtonTitle and AlertText as "podatki strani"; the toast uses a different rendering on the same screen.
- `MainMenu.ToolsSection.DesktopSite.Title.v141` — `sl/firefox-ios.xliff` — "Desktop Site" is rendered as "Stran za namizja" while the parallel switch actions in the same menu use "stran za računalnike".
    - Current: `Stran za namizja`
    - Source: `Desktop Site`
    - Suggest: `Stran za računalnike`
    - Within the same Tools section, MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131 and its accessibility label translate "desktop site" as "stran za računalnike"; this string uses a different term for the same source concept.
- `PrivacyDashboard.Fingerprinters.v155` — `sl/firefox-ios.xliff` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinting scripts.
    - Current: `Sledilci prstnih odtisov`
    - Source: `Fingerprinters`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - In Firefox Slovenian the term for "Fingerprinters" is "Sledilci prstnih odtisov naprav"; the shortened form loses the meaning of device fingerprinting.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `sl/firefox-ios.xliff` — Setting title translated as an imperative sentence instead of a noun-phrase label.
    - Current: `Podrsajte, da skrijete vrstico z zavihki in naslovom`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Drsenje skrije vrstico z zavihki in naslovno vrstico`
    - The source is a settings option title ("Scroll to Hide Tab and Address Bar"), a label rather than an instruction addressed to the user; it also conflates the tab bar and address bar into one bar.
- `Settings.Studies.Title.v148` — `sl/firefox-ios.xliff` — "Feature Studies" is rendered as "raziskave značilnosti" instead of the established term for features ("funkcije").
    - Current: `Dovoli raziskave značilnosti`
    - Source: `Allow Feature Studies`
    - Suggest: `Dovoli raziskave funkcij`
    - Elsewhere in this same file "features" is translated as "funkcije" (e.g. Settings.Studies.Message.v136 "Preizkusite funkcije in ideje"); "značilnosti" is inconsistent and misleading here.
- `Summarizer.Error.RateLimited.Message.v142` — `sl/firefox-ios.xliff` — The translation uses a first-person anthropomorphic voice ("ne morem narediti") absent from the source and against product register.
    - Current: `Tega trenutno ne morem narediti.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Tega trenutno ni mogoče obdelati.`
    - en-US "Can’t handle this one at the moment." is impersonal; the Slovenian introduces a first-person "I can't", a register the app does not use elsewhere.
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `sl/firefox-ios.xliff` — "OPENING SCREEN" is translated as "ZAČETNI ZASLON" while the same source term is "Uvodni zaslon" in Settings.Home.Option.StartAtHome.Title.
    - Current: `ZAČETNI ZASLON`
    - Source: `OPENING SCREEN`
    - Suggest: `UVODNI ZASLON`
    - Same source term "Opening screen" is rendered inconsistently within the same settings area.
- `TodayWidget.TopSitesGalleryTitle` — `sl/firefox-ios.xliff` — "Top Sites" is rendered as "Glavne strani" instead of the established Slovenian term "Najbolj obiskane strani".
    - Current: `Glavne strani`
    - Source: `Top Sites`
    - Suggest: `Najbolj obiskane strani`
    - "Top Sites" refers to frequently visited sites; "Glavne strani" means "main pages" and does not convey the source meaning nor the term used elsewhere in Firefox sl.

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.DeletedBookmark.v131` — `sl/firefox-ios.xliff` — Straight ASCII quotes used instead of the typographic quotes of the source.
    - Current: `"%@" izbrisan`
    - Source: `Deleted “%@”`
    - Suggest: `»%@« izbrisan`
    - The source uses curly quotes “%@”; the translation uses straight ASCII quotes, inconsistent with the other toast strings in the same file which keep typographic quotes.
- `LiveActivity.Downloads.FileNameText.v138` — `sl/firefox-ios.xliff` — Straight ASCII quotes used instead of the typographic quotation marks of the source.
    - Current: `Prenašanje "%@"`
    - Source: `Downloading “%@”`
    - Suggest: `Prenašanje „%@“`
    - The en-US source uses curly quotes “%@”; the Slovenian uses straight ASCII double quotes, deviating from the source typography.
- `Upgrade.SyncSign.Description.v114` — `sl/firefox-ios.xliff` — Hyphen used instead of an en dash as a sentence-level dash.
    - Current: `končali - z zavihki`
    - Source: `Pick up where you left off with tabs from other devices now on your homepage.`
    - Suggest: `končali – z zavihki`
    - Slovenian typography requires an en dash (–) with spaces for parenthetical/appositive dashes, not a hyphen.
- `DefaultBrowserOnboarding.Description2` — `sl/firefox-ios.xliff` — Uses straight ASCII double quotes around the iOS setting name and leaves it untranslated inconsistently with DefaultBrowserOnboarding.Screenshot.
    - Current: `2. Tapnite "Default Browser App"`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Tapnite „Privzeti brskalnik“`
    - Slovenian typography uses „ “ quotation marks, and the same iOS setting is rendered as "Privzet brskalnik" in DefaultBrowserOnboarding.Screenshot, making the two references inconsistent.
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
