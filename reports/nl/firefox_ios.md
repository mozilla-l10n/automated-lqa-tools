# Firefox iOS l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,902 of 1,918 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (49)

- `NSFaceIDUsageDescription` — `nl/firefox-ios.xliff` — "saved passwords" is rendered as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `uw opgeslagen aanmeldingen en betalingsmethoden`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `uw opgeslagen wachtwoorden en betalingsmethoden`
    - The en-US says "saved passwords"; the Dutch says "logins", a different term than the source uses.
- `LibraryPanel.History.AllTimeOption.v138` — `nl/firefox-ios.xliff` — “All Time” (time range covering everything) is translated as “Altijd” (always), not the time-range sense.
    - Current: `Altijd`
    - Source: `All Time`
    - Suggest: `Alles`
    - The option clears browsing history for the entire period; Dutch “Altijd” means “always” and does not convey the ‘all time’ range used alongside ‘Laatste uur’, ‘Afgelopen 7 dagen’.
- `Previous in-page result` — `nl/firefox-ios.xliff` — Wrong adjective inflection: “Vorige resultaat” should be “Vorig resultaat” with a neuter noun.
    - Current: `Vorige resultaat op pagina`
    - Source: `Previous in-page result`
    - Suggest: `Vorig resultaat op pagina`
    - ‘resultaat’ is a neuter (het) noun without article, so the adjective takes the uninflected form ‘vorig’.
- `ErrorPages.CertWarning.Title` — `nl/firefox-ios.xliff` — ‘Untrusted’ is rendered as ‘niet beveiligd’ (not secure) instead of ‘niet vertrouwd’.
    - Current: `Deze verbinding is niet beveiligd`
    - Source: `This Connection is Untrusted`
    - Suggest: `Deze verbinding is niet vertrouwd`
    - The source says the connection is untrusted, not insecure; ‘beveiligd’ means secure/encrypted, which is a different claim.
- `Menu.TrackingProtectionBlockedContent.Title` — `nl/firefox-ios.xliff` — "Tracking content" is rendered as "Volginhoud", inconsistent with the "trackers" terminology used in the surrounding tracking-protection strings.
    - Current: `Volginhoud`
    - Source: `Tracking content`
    - Suggest: `Volgende inhoud`
    - The other strings on this screen keep the English term ("Sociale trackers", "Cross-site-trackers", "Fingerprinters"); the Dutch Firefox term for "tracking content" is "volgende inhoud", not the coined "Volginhoud".
- `Search.SuggestSectionTitle.v102` — `nl/firefox-ios.xliff` — Brand name “Firefox Suggest” has been partially translated.
    - Current: `Firefox Suggesties`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - “Firefox Suggest” is a product/feature brand name that must stay untranslated; “Suggesties” alters the brand.
- `PhotoLibrary.FirefoxWouldLikeAccessTitle` — `nl/firefox-ios.xliff` — “would like to access” rendered as “vraagt om toegang” (is asking for access) instead of “wil toegang”.
    - Current: `Firefox vraagt om toegang tot uw foto’s`
    - Source: `Firefox would like to access your Photos`
    - Suggest: `Firefox wil toegang tot uw foto’s`
    - The source states Firefox would like to access your Photos; the Dutch changes it to Firefox requesting access.
- `Remove from Reading List` — `nl/firefox-ios.xliff` — Wrong preposition: “verwijderen van leeslijst” should be “verwijderen uit leeslijst”.
    - Current: `Verwijderen van leeslijst`
    - Source: `Remove from Reading List`
    - Suggest: `Verwijderen uit leeslijst`
    - Dutch uses “uit” for removing an item from a list; “van” is ungrammatical/ambiguous here.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `nl/firefox-ios.xliff` — "some ad tracking" is rendered as "enkele advertentietrackers" (some ad trackers), naming objects instead of the activity.
    - Current: `Staat enkele advertentietrackers toe`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Staat enige advertentietracking toe`
    - The source says the standard level allows some ad tracking (the activity), not that it permits specific ad trackers.
- `Toolbar.Menu.CloseAllTabs` — `nl/firefox-ios.xliff` — Spelling error: “All” should be “Alle”.
    - Current: `All tabbladen sluiten`
    - Source: `Close All Tabs`
    - Suggest: `Alle tabbladen sluiten`
    - Dutch for “all” is “alle”; the same source string elsewhere (TabTray.CloseAllTabs.KeyCodeTitle) is correctly “Alle tabbladen sluiten”.
- `Biometry.Screen.UniversalAuthenticationReason.v122` — `nl/firefox-ios.xliff` — ‘saved passwords’ is translated as ‘opgeslagen aanmeldingen’ (saved logins) instead of ‘opgeslagen wachtwoorden’.
    - Current: `uw opgeslagen aanmeldingen en betalingsmethoden`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `uw opgeslagen wachtwoorden en betalingsmethoden`
    - The source says ‘passwords’; the sibling string v115 correctly uses ‘wachtwoorden’, making the terminology inconsistent as well.
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `nl/firefox-ios.xliff` — ‘DESKTOP BOOKMARKS’ is rendered as the malformed compound ‘BUREAUBLADWIJZERS’ instead of ‘BUREAUBLADBLADWIJZERS’ / ‘BLADWIJZERS VAN BUREAUBLAD’.
    - Current: `BUREAUBLADWIJZERS`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `BUREAUBLAD-BLADWIJZERS`
    - The source means bookmarks synced from desktop; the blend ‘bureaubladwijzers’ collapses ‘bureaublad’ and ‘bladwijzers’ into a non-word and loses the meaning, and it is inconsistent with ‘MOBIELE BLADWIJZERS’ on the same screen.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `nl/firefox-ios.xliff` — "Tracking content" is translated as "Volginhoud" while the rest of the screen consistently uses the loanword "trackers"/"tracking".
    - Current: `Volginhoud: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Trackinginhoud: %@`
    - The surrounding strings in the same screen use "trackers" and "trackingcookies"; "Volginhoud" introduces an inconsistent term for "tracking content".
- `MainMenu.HeaderBanner.Subtitle.v142` — `nl/firefox-ios.xliff` — "Takes seconds. Change anytime." is rendered with an odd phrase and an imperative that loses the meaning "you can change it at any time".
    - Current: `Zo gebeurd. Wijzig op elk moment.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Duurt maar enkele seconden. U kunt dit altijd wijzigen.`
    - The source says the action takes only seconds and can be changed at any time; the Dutch 'Wijzig op elk moment' is an imperative command to change it, not a statement that it can be changed later.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `nl/firefox-ios.xliff` — "Home" (iOS Home screen) is translated as "Startpagina" (homepage) instead of "Beginscherm/Startscherm".
    - Current: `Startpagina`
    - Source: `Home`
    - Suggest: `Startscherm`
    - The developer comment says this refers to the iOS Home screen, and the related title string uses 'startscherm'; 'Startpagina' means homepage, a different concept used elsewhere for Customize Homepage.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `nl/firefox-ios.xliff` — Inconsistent rendering of "Tools" submenu: elsewhere "Hulpmiddelen", here "Extra".
    - Current: `Submenu Extra`
    - Source: `Turn off Reader View`
    - Suggest: `Submenu Hulpmiddelen`
    - MainMenu.ToolsSection.AccessibilityLabels.Tools.v132 translates "Tools" as "Hulpmiddelen"; the same term on the same screen must be consistent.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `nl/firefox-ios.xliff` — Ungrammatical compound "mobielwebsite".
    - Current: `Naar mobielwebsite`
    - Source: `Switch to mobile site`
    - Suggest: `Naar mobiele website`
    - Dutch does not compound an adjective with a noun this way; the correct form is "mobiele website" (compare "desktopwebsite", where "desktop" is a noun).
- `MainMenu.ToolsSection.SwitchToMobileSite.Title.v131` — `nl/firefox-ios.xliff` — Compound 'mobielwebsite' is ungrammatical; the adjective must be inflected as a separate word.
    - Current: `Naar mobielwebsite`
    - Source: `Switch to Mobile Site`
    - Suggest: `Naar mobiele website`
    - 'mobiel' is an adjective, not a noun that can form a compound like 'desktopwebsite'; correct Dutch is 'mobiele website'.
- `Microsurvey.Survey.Options.Neutral.v132` — `nl/firefox-ios.xliff` — 'Neutral' rendered as 'Gemiddeld' (average) instead of 'Neutraal'.
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
    - The source option is 'Neutral', the mid-point of a satisfaction scale; 'Gemiddeld' means 'average' and is a different term.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `nl/firefox-ios.xliff` — Untranslated English article 'the' left in the Dutch sentence, producing ungrammatical text.
    - Current: `van the Internet Archive`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `van het Internet Archive`
    - The source reads "the Internet Archive’s %2$@"; the Dutch keeps the English article "the" inside a Dutch sentence, which is ungrammatical.
- `Onboarding.Customization.Theme.System.Action.v123` — `nl/firefox-ios.xliff` — "System Auto" is rendered as "Systeemthema", dropping the automatic aspect and matching the wrong concept.
    - Current: `Systeemthema`
    - Source: `System Auto`
    - Suggest: `Systeem automatisch`
    - The source option is "System Auto" (follow the device automatically); "Systeemthema" just means "system theme" and loses the 'auto' meaning.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `nl/firefox-ios.xliff` — "marketing partners" is translated as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `marketingtechnologiepartners`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `marketingpartners`
    - The source says only "%2$@’s marketing partners"; the Dutch claims data is shared with marketing technology partners, which the source never states.
- `Onboarding.Modern.BrandRefresh.Notification.TurnOn.Action.v148` — `nl/firefox-ios.xliff` — "notifications" is translated as "Notificaties" here but as "Meldingen" in the title on the same card.
    - Current: `Notificaties inschakelen`
    - Source: `Turn on notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Modern.BrandRefresh.Notification.Title.v148 uses "Meldingen" for the same source term on the same screen; inconsistent terminology.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `nl/firefox-ios.xliff` — "all in one place" is weakened and the em/en dash structure dropped, changing "get ... – all in one place" to "ontvangen op één plek".
    - Current: `op één plek te ontvangen`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `te krijgen – allemaal op één plek`
    - The source lists items then emphasizes "– all in one place"; the Dutch drops "all" and the dash, altering the emphasis of the sentence.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `nl/firefox-ios.xliff` — "get search suggestions ... – all in one place" is rendered as "ontvangen" (receive) and the "all in one place" emphasis is dropped/merged.
    - Current: `om zoeksuggesties, uw topwebsites, bladwijzers, geschiedenis en zoekmachines op één plek te ontvangen`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `om zoeksuggesties, uw topwebsites, bladwijzers, geschiedenis en zoekmachines te krijgen – alles op één plek`
    - The source lists items and then adds "– all in one place" as an appositive; the Dutch loses the dash construction and uses "ontvangen", which does not convey "get" here.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `nl/firefox-ios.xliff` — "have %@ match your device" mistranslated as "laat %@ met uw apparaat overeenkomen", which reverses/obscures that the app should match the device theme.
    - Current: `of laat %@ met uw apparaat overeenkomen`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `of laat %@ het thema van uw apparaat volgen`
    - The source means Firefox should follow the device's theme; the Dutch phrasing is ambiguous/incorrect Dutch for that meaning.
- `Onboarding.Modern.Sync.Description.v145` — `nl/firefox-ios.xliff` — Superfluous comma before "en meer" in a Dutch enumeration.
    - Current: `Uw bladwijzers, wachtwoorden, en meer`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Uw bladwijzers, wachtwoorden en meer`
    - Dutch does not use a serial comma before "en"; the source's Oxford comma should not be carried over.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `nl/firefox-ios.xliff` — "for everyone" is rendered as "voor gebruikers overal" (for users everywhere), changing the meaning.
    - Current: `voor gebruikers overal`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users everywhere".
- `Onboarding.Notification.TurnOnNotifications.Action.v114` — `nl/firefox-ios.xliff` — "Notifications" is translated as "Notificaties" here while the related notification onboarding strings use "Meldingen".
    - Current: `Notificaties inschakelen`
    - Source: `Turn On Notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Notification.Title.v120 on the same screen uses "Meldingen" for Notifications; the two renderings are inconsistent within one screen.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `nl/firefox-ios.xliff` — "for everyone" is rendered as "voor gebruikers overal" (for users everywhere), changing the meaning.
    - Current: `voor gebruikers overal`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users everywhere".
- `Search.Google.Title.v108` — `nl/firefox-ios.xliff` — Incorrect capitalization of the common noun in "Google Zoeken".
    - Current: `Google Zoeken`
    - Source: `Google Search`
    - Suggest: `Google-zoekopdracht`
    - Dutch does not use English title case; "Zoeken" should not be capitalized mid-phrase.
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Title.v154` — `nl/firefox-ios.xliff` — English title case carried over: "Antwoorden" should be lowercase in Dutch.
    - Current: `Snelle Antwoorden`
    - Source: `Quick Answers`
    - Suggest: `Snelle antwoorden`
    - Dutch sentence-case capitalization rules; the parallel string "Paginasamenvattingen" is not title-cased either.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `nl/firefox-ios.xliff` — Incorrect Dutch compound ellipsis: 'tabbladen- en adresbalk' should be 'tabblad- en adresbalk'.
    - Current: `Scrollen om tabbladen- en adresbalk te verbergen`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Scrollen om tabblad- en adresbalk te verbergen`
    - The source is 'Tab and Address Bar' (singular 'tab bar'); the elided compound part must be 'tabbalk', so the correct ellipsis form is 'tabblad- en adresbalk'.
- `Summarizer.Error.MissingPageContent.Message.v142` — `nl/firefox-ios.xliff` — "hit summarize" is rendered as "klik op samenvatten" (click) on a touch-only iOS device.
    - Current: `klik daarna op samenvatten`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `tik daarna op samenvatten`
    - This is a phone UI; the source says "hit summarize" and other strings in this file use "Tik" for tapping. "Klik" (click) is wrong terminology for iOS.
- `Summarizer.Footnote.Label.v144` — `nl/firefox-ios.xliff` — "Summarization can make errors" is translated as "samenvattingen kunnen fouten bevatten", shifting the meaning about the feature.
    - Current: `Noot: samenvattingen kunnen fouten bevatten.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Noot: samenvatten kan fouten opleveren.`
    - The source warns that the summarization process can make mistakes; the Dutch states the summaries contain errors, a slightly different assertion about the product output.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `nl/firefox-ios.xliff` — The subtitle lacks a subject/verb and reads as a fragment rather than a sentence.
    - Current: `Over %1$@ vertellen telkens als u een koppeling op %2$@ deelt.`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `Vertel anderen over %1$@ telkens als u een koppeling op %2$@ deelt.`
    - The en-US is an imperative sentence "Spread the word about %1$@…"; the Dutch infinitive fragment is ungrammatical as a standalone sentence.
- `TermsOfUse.LearnMoreHere.v147` — `nl/firefox-ios.xliff` — Word order makes the sentence with the 'here' link read incorrectly in Dutch.
    - Current: `U vindt %@ meer info.`
    - Source: `You can learn more %@.`
    - Suggest: `U kunt %@ meer info vinden.`
    - The source is 'You can learn more %@.' where %@ is the link text 'hier'. 'U vindt hier meer info' is only correct with the link directly after the verb; as rendered the placeholder sits between 'vindt' and 'meer info', which is awkward/ungrammatical word order for the intended 'here' link.
- `Toolbar.Translation.LoadingButton.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — "Translating page" (progress state) is rendered as an imperative/infinitive "Pagina vertalen", identical to the inactive "Translate page" label.
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The source is a progress indication that translation is in progress, not the action label; it is also indistinguishable from Toolbar.Translation.ButtonInactive.AccessibilityLabel.v145 ("Translate page"), defeating the accessibility distinction.
- `Translations.Banner.Loading.Button.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — "Translating page" (in-progress state) is translated as "Pagina vertalen", which means "Translate page".
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The source describes an ongoing process (loading button while the page is being translated), not an action to perform.
- `Translations.Sheet.LoadingButton.v145` — `nl/firefox-ios.xliff` — "Translating page" (in-progress state) is translated as "Pagina vertalen" ("Translate page").
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - Per the comment the button indicates that the page is being translated; the Dutch reads as the action label instead, and duplicates Translations.Sheet.TitleLabel "Pagina vertalen".
- `Translations.Sheet.TranslateFromLabel.v145` — `nl/firefox-ios.xliff` — Label ends with a dangling article "het" although no language name follows in this string.
    - Current: `Vertalen vanuit het`
    - Source: `Translate From`
    - Suggest: `Vertalen vanuit`
    - This is a standalone cell label ("Translate From") with no language placeholder, so the trailing article is ungrammatical.
- `Translations.Sheet.TranslateToLabel.v145` — `nl/firefox-ios.xliff` — Label ends with a dangling article "het" although no language name follows in this string.
    - Current: `Vertalen naar het`
    - Source: `Translate To`
    - Suggest: `Vertalen naar`
    - This is a standalone cell label ("Translate To") without a language placeholder, so the trailing article is ungrammatical.
- `Translations.LanguagePicker.Title.v151` — `nl/firefox-ios.xliff` — Title ends with a dangling article before the ellipsis.
    - Current: `Pagina vertalen naar het…`
    - Source: `Translate Page to…`
    - Suggest: `Pagina vertalen naar…`
    - The source "Translate Page to…" has no following language name in this string, so "het" is left hanging and ungrammatical.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `nl/firefox-ios.xliff` — The Dutch attaches "on this page" to the hostnames rather than to the blocking, changing the meaning.
    - Current: `Op deze pagina geblokkeerde hostnamen van trackers`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Hostnamen van trackers die op deze pagina zijn geblokkeerd`
    - Source is "Hostnames of trackers blocked on this page": the trackers were blocked on this page. The Dutch reads as "hostnames of trackers that were blocked on this page" only ambiguously; as written it modifies 'hostnamen', implying the hostnames are blocked on the page.
- `WebCompatReporter.Category.DesignBroken.v154` — `nl/firefox-ios.xliff` — "defect" is the wrong term for a broken page layout.
    - Current: `Ontwerp is defect`
    - Source: `Design is broken`
    - Suggest: `Ontwerp is kapot`
    - "defect" in Dutch describes faulty hardware/devices; for a broken site layout the established rendering is "kapot"/"werkt niet goed".
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `nl/firefox-ios.xliff` — ‘Full time’ is translated as ‘Gelijkspel’ (draw) instead of end of match.
    - Current: `Gelijkspel • Penalty’s (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Wedstrijd afgelopen • Penalty’s (%@)`
    - The source says ‘Full time’, meaning the match has ended; ‘Gelijkspel’ means ‘draw’, a different statement about the result. Other strings in this file render ‘Full Time’ as ‘Wedstrijd afgelopen’, so it is also inconsistent.
- `WorldCup.HomepageWidget.PenaltiesLabel.v151` — `nl/firefox-ios.xliff` — Dutch plural of 'penalty' is written 'penalty’s' — but here the football term should be 'Penalty’s' capitalized correctly; the apostrophe-s form is fine, however 'Penalties' should be rendered as 'Strafschoppen' or 'Penalty’s'.
    - Current: `Penalty’s (%@)`
    - Source: `Penalties (%@)`
    - Suggest: `Strafschoppen (%@)`
    - Placeholder-only concern aside, the football phase 'Penalties' (penalty shoot-out) is normally 'Strafschoppen' in Dutch; 'Penalty’s' is the plural of a single penalty kick and reads oddly as a match-phase label.
- `WorldCup.HomepageWidget.RoundPhase.QuarterFinalsLabel.v151` — `nl/firefox-ios.xliff` — Plural 'QUARTER-FINALS' rendered as singular 'KWARTFINALE'.
    - Current: `KWARTFINALE`
    - Source: `QUARTER-FINALS`
    - Suggest: `KWARTFINALES`
    - The source is plural, and the parallel string SEMI-FINALS is correctly translated as the plural 'HALVE FINALES'; the singular is inconsistent and inaccurate.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `nl/firefox-ios.xliff` — 'ROUND OF 16' is literally translated as 'RONDE VAN 16' instead of the established Dutch term.
    - Current: `RONDE VAN 16`
    - Source: `ROUND OF 16`
    - Suggest: `ACHTSTE FINALES`
    - In Dutch football terminology the round of 16 is called 'achtste finales'; 'ronde van 16' is a literal calque.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (43)

- `NSFaceIDUsageDescription` — `Client/en.lproj/InfoPlist.strings` — "saved passwords" is translated as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `opgeslagen aanmeldingen`
    - Suggest: `opgeslagen wachtwoorden`
    - The en-US source says "saved passwords"; Firefox terminology for passwords in nl is "wachtwoorden", while "aanmeldingen" renders the older term "logins".
- `Biometry.Screen.UniversalAuthenticationReason.v122` — `Shared/Supporting Files/en.lproj/BiometricAuthentication.strings` — "saved passwords" is translated as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `opgeslagen aanmeldingen`
    - Suggest: `opgeslagen wachtwoorden`
    - The source says "your saved passwords"; the v115 sibling string correctly uses "wachtwoorden". "Aanmeldingen" is the older "logins" term and is inconsistent with the source and the neighbouring string.
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — "BUREAUBLADWIJZERS" is a malformed blend; it should be "BUREAUBLADBLADWIJZERS" or better "BLADWIJZERS OP BUREAUBLAD".
    - Current: `BUREAUBLADWIJZERS`
    - Suggest: `BUREAUBLADBLADWIJZERS`
    - "Desktop bookmarks" is "bureaublad" + "bladwijzers"; the current form collapses the two words into a nonword that reads as "desk-pointers", losing the "bookmarks" meaning. The parallel string uses "MOBIELE BLADWIJZERS".
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Department" as an administrative division (France/Colombia) is translated as "Afdeling" (organizational department).
    - Current: `Afdeling`
    - Suggest: `Departement`
    - The developer comment states this is the administrative division used in countries like France and Colombia; Dutch uses "departement" for that, whereas "afdeling" means a company/organizational department.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Tracking content" is rendered as "Volginhoud" but the label needs to convey tracking content, and here the Dutch term used is inconsistent/incorrect relative to the other tracker labels which keep "tracking".
    - Current: `Volginhoud: %@`
    - Suggest: `Volgende inhoud: %@`
    - The other strings in this screen keep the English-based term ("trackingcookies", "trackers"); "Volginhoud" is not the established Dutch Firefox term for "Tracking content", which is "Volgende inhoud".
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `Shared/Supporting Files/en.lproj/ExternalLink.strings` — Singular "email" is translated as plural "E-mailberichten".
    - Current: `E-mailberichten openen in de standaard e-mailtoepassing?`
    - Suggest: `E-mailbericht openen in de standaard e-mailtoepassing?`
    - The source asks about opening the single mail link the user tapped, not multiple messages.
- `MainMenu.HeaderBanner.Subtitle.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Takes seconds." is translated as "Zo gebeurd." and the second sentence uses an informal imperative inconsistent with the u-register.
    - Current: `Zo gebeurd. Wijzig op elk moment.`
    - Suggest: `Duurt maar enkele seconden. U kunt dit altijd wijzigen.`
    - The source states the action takes only seconds and can be changed anytime; 'Zo gebeurd' loses that meaning, and elsewhere in this file the polite 'u' form with full sentences is used.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Home" here refers to the iOS home screen, not a home page.
    - Current: `Startpagina`
    - Suggest: `Beginscherm`
    - The developer comment states this is for the Add to Home screen tool for the iOS Home screen; the paired title uses "startscherm", so "Startpagina" (home page) is the wrong referent.
- `MainMenu.Submenus.Save.AddToHomeScreen.Subtitle.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Home" here refers to the iOS home screen, not a home page.
    - Current: `Startpagina`
    - Suggest: `Beginscherm`
    - The developer comment says this subtitle belongs to the Add to Homescreen tool; the accompanying title is translated as "Toevoegen aan startscherm", so "Startpagina" (home page) names the wrong thing and is inconsistent.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "mobielwebsite" is not a valid Dutch compound; the adjective should be "mobiele".
    - Current: `Naar mobielwebsite`
    - Suggest: `Naar mobiele website`
    - "mobiel" is an adjective and must be inflected before a de-word ("mobiele website"); it cannot be glued into a compound like "desktopwebsite" (where "desktop" is a noun).
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Tools" is rendered as "Extra" here but as "Hulpmiddelen" in the other Tools strings on the same menu.
    - Current: `Submenu Extra`
    - Suggest: `Submenu Hulpmiddelen`
    - MainMenu.ToolsSection.AccessibilityLabels.Tools.v132 and ToolsSubmenu.Title.v131 both translate "Tools" as "Hulpmiddelen"; the same submenu must be named consistently.
- `MainMenu.ToolsSection.SwitchToMobileSite.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "mobielwebsite" is not a valid Dutch compound; the adjective should be "mobiele".
    - Current: `Naar mobielwebsite`
    - Suggest: `Naar mobiele website`
    - "mobiel" is an adjective requiring inflection before a de-word: "mobiele website". Unlike "desktopwebsite", it cannot form a compound.
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `Shared/Supporting Files/en.lproj/Microsurvey.strings` — "Unselected" (a state) is rendered as "Selectie opgeheven" (an action/event, deselected).
    - Current: `Selectie opgeheven`
    - Suggest: `Niet geselecteerd`
    - The comment says this label states that the survey option was not selected — a state, not the action of deselecting.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Untranslated English article "the" left inside the Dutch sentence.
    - Current: `vanuit %2$@ van the Internet Archive`
    - Suggest: `vanuit de %2$@ van het Internet Archive`
    - "van the Internet Archive" mixes English article into Dutch; the source is "from the Internet Archive’s Wayback Machine".
- `Onboarding.Customization.Theme.System.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "System Auto" is translated as "Systeemthema" (system theme), losing the automatic aspect.
    - Current: `Systeemthema`
    - Suggest: `Systeem automatisch`
    - The source option is "System Auto", indicating automatic following of the system setting, not simply "system theme".
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "get search suggestions ... all in one place" is translated as "ontvangen" (receive) and the "all in one place" emphasis is dropped.
    - Current: `en zoekmachines op één plek te ontvangen`
    - Suggest: `en zoekmachines te krijgen – alles op één plek`
    - The source lists items and then concludes with "– all in one place"; the Dutch merges it and loses the "all" summary clause.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "marketing partners" is rendered as "marketingtechnologiepartners" (marketing technology partners), adding a term not in the source.
    - Current: `%2$@’s marketingtechnologiepartners`
    - Suggest: `%2$@’s marketingpartners`
    - The en-US source says "%2$@’s marketing partners", not "marketing technology partners".
- `Onboarding.Modern.BrandRefresh.Notification.TurnOn.Action.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "notifications" is rendered as "Notificaties" here but as "Meldingen" in the title of the same onboarding card.
    - Current: `Notificaties inschakelen`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Modern.BrandRefresh.Notification.Title.v148 uses "Meldingen" for the same source term on the same card; Mozilla nl standard term is "Meldingen".
- `Onboarding.Modern.Customization.Theme.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "have %@ match your device" is mistranslated as "laat %@ met uw apparaat overeenkomen", which reverses/obscures the meaning of the theme following the device setting.
    - Current: `of laat %@ met uw apparaat overeenkomen`
    - Suggest: `of laat %@ overeenkomen met uw apparaatinstelling`
    - The source means the app's theme should match the device theme; the Dutch literal rendering is ambiguous but arguably acceptable — however "laat %@ met uw apparaat overeenkomen" states the app matches the device rather than the theme.
- `Onboarding.Modern.Sync.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Superfluous comma before "en meer" in a Dutch enumeration.
    - Current: `Uw bladwijzers, wachtwoorden, en meer`
    - Suggest: `Uw bladwijzers, wachtwoorden en meer`
    - Dutch does not use the serial (Oxford) comma before "en"; the parallel string Onboarding.Modern.BrandRefresh.Sync.Description.v148 correctly omits it.
- `Onboarding.Notification.TurnOnNotifications.Action.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Notifications" is rendered as "Notificaties" here but as "Meldingen" in the sibling notification onboarding title.
    - Current: `Notificaties inschakelen`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Notification.Title.v120 in the same screen translates "Notifications" as "Meldingen"; the same term should be used consistently.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is mistranslated as "voor gebruikers overal" (for users everywhere).
    - Current: `voor gebruikers overal`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features for everyone, not for users everywhere.
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Title.v154` — `Shared/Supporting Files/en.lproj/Settings.strings` — Unnecessary capitalization of the second word; Dutch uses sentence case.
    - Current: `Snelle Antwoorden`
    - Suggest: `Snelle antwoorden`
    - Dutch capitalization rules capitalize only the first word of a title; the sibling feature titles in the same section ("Paginasamenvattingen", "Vertaling", "AI-verbeteringen blokkeren") follow sentence case.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `Shared/Supporting Files/en.lproj/Settings.strings` — Incorrect compound coordination "tabbladen- en adresbalk" instead of "tabblad- en adresbalk".
    - Current: `Scrollen om tabbladen- en adresbalk te verbergen`
    - Suggest: `Scrollen om tabblad- en adresbalk te verbergen`
    - The source is "Tab and Address Bar" (singular tab bar); the Dutch elided compound should use the singular stem "tabbalk" → "tabblad- en adresbalk".
- `Summarizer.Error.MissingPageContent.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "hit summarize" is rendered as "klik op" (click) on a touch device, and "Wacht tot deze is voltooid" misattributes completion to the page.
    - Current: `Wacht tot deze is voltooid en klik daarna op samenvatten.`
    - Suggest: `Wacht tot het laden is voltooid en tik daarna op Samenvatten.`
    - The source says to wait for the loading to finish and then tap summarize; on iOS the interaction is tapping, not clicking.
- `TermsOfUse.LearnMoreHere.v147` — `Shared/Supporting Files/en.lproj/TermsOfUse.strings` — Word order places the 'here' link incorrectly, producing ungrammatical Dutch.
    - Current: `U vindt %@ meer info.`
    - Suggest: `U kunt %@ meer info vinden.`
    - The source is 'You can learn more %@.' where %@ is the link text 'hier'. 'U vindt hier meer info.' would be acceptable, but 'U vindt %@ meer info.' with the placeholder in that slot reads as broken; the intended sentence requires the link at the natural adverbial position, e.g. 'U kunt %@ meer info vinden.'
- `Toolbar.Translation.LoadingButton.AccessibilityLabel.v145` — `Shared/Supporting Files/en.lproj/Toolbar.strings` — Progressive state "Translating page" is rendered as the infinitive "Pagina vertalen" (Translate page), losing the in-progress meaning.
    - Current: `Pagina vertalen`
    - Suggest: `Pagina wordt vertaald`
    - The source indicates the page is currently being translated; the Dutch reads as the command/label "Translate page", identical to Toolbar.Translation.ButtonInactive ("Translate page"), so the two opposite states are indistinguishable.
- `Translations.Banner.Loading.Button.AccessibilityLabel.v145` — `Shared/Supporting Files/en.lproj/Translations.strings` — "Translating page" (in progress) is translated as "Pagina vertalen" (Translate page).
    - Current: `Pagina vertalen`
    - Suggest: `Pagina wordt vertaald`
    - The loading state must convey that translation is ongoing; the Dutch is identical to the title "Translate Page" (Translations.Sheet.TitleLabel), so it does not express the progressive state.
- `Translations.LanguagePicker.Title.v151` — `Shared/Supporting Files/en.lproj/Translations.strings` — Title ends with a dangling article "het" before the ellipsis.
    - Current: `Pagina vertalen naar het…`
    - Suggest: `Pagina vertalen naar…`
    - There is no language name in this string, so the article "het" has nothing to modify and the phrase is ungrammatical.
- `Translations.Sheet.LoadingButton.v145` — `Shared/Supporting Files/en.lproj/Translations.strings` — "Translating page" (in progress) is translated as "Pagina vertalen" (Translate page).
    - Current: `Pagina vertalen`
    - Suggest: `Pagina wordt vertaald`
    - The button indicates the page is being translated; the Dutch infinitive reads as the action label and duplicates Translations.Sheet.TitleLabel "Pagina vertalen".
- `Translations.Sheet.TranslateFromLabel.v145` — `Shared/Supporting Files/en.lproj/Translations.strings` — Standalone cell label ends in a dangling article "het" with no language name following.
    - Current: `Vertalen vanuit het`
    - Suggest: `Vertalen vanuit`
    - Unlike the accessibility label where %@ supplies the language, this string has no placeholder, so "het" is left hanging and ungrammatical.
- `Translations.Sheet.TranslateToLabel.v145` — `Shared/Supporting Files/en.lproj/Translations.strings` — Dangling article "het" at the end of the label makes the phrase ungrammatical.
    - Current: `Vertalen naar het`
    - Suggest: `Vertalen naar`
    - The source is "Translate To"; the trailing definite article "het" has no noun to attach to and leaves an incomplete Dutch phrase.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — Modifier attached to the wrong noun: it now says hostnames blocked on this page instead of trackers blocked on this page.
    - Current: `Op deze pagina geblokkeerde hostnamen van trackers`
    - Suggest: `Hostnamen van op deze pagina geblokkeerde trackers`
    - Source "Hostnames of trackers blocked on this page" — the blocking applies to the trackers, not to the hostnames.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Full time" is translated as "Gelijkspel" (draw) instead of end of match.
    - Current: `Gelijkspel • Penalty’s (%@)`
    - Suggest: `Wedstrijd afgelopen • Penalty’s (%@)`
    - The source says "Full time" (end of regular play), which the sibling strings FTLabel/FTNoParenthesisLabel render as "Wedstrijd afgelopen". "Gelijkspel" means "draw", a different meaning and inconsistent with the same term elsewhere on the screen.
- `WorldCup.HomepageWidget.RoundPhase.QuarterFinalsLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — Plural 'QUARTER-FINALS' rendered as singular 'KWARTFINALE'.
    - Current: `KWARTFINALE`
    - Suggest: `KWARTFINALES`
    - The source is plural (compare SEMI-FINALS translated as 'HALVE FINALES'), so the quarter-finals label should also be plural.
- `Previous in-page result` — `Shared/en.lproj/FindInPage.strings` — Wrong adjective inflection with the neuter noun 'resultaat'.
    - Current: `Vorige resultaat op pagina`
    - Suggest: `Vorig resultaat op pagina`
    - 'Resultaat' is a neuter noun; without an article the attributive adjective takes no -e ending, so it must be 'Vorig resultaat' (compare 'Volgende', which is invariable).
- `LibraryPanel.History.AllTimeOption.v138` — `Shared/en.lproj/HistoryPanel.strings` — 'All Time' as a time-range option is translated as 'Altijd' (always) instead of 'Alles'/'Alle tijd'.
    - Current: `Altijd`
    - Suggest: `Alles`
    - The option clears all browsing history regardless of period; 'Altijd' means 'always' and does not convey the time-range 'All Time'.
- `ContextMenu.BookmarkLinkButtonTitle` — `Shared/en.lproj/Localizable.strings` — "Bookmark Link" is translated without the "link" part, losing the distinction from bookmarking the page.
    - Current: `Bladwijzer maken`
    - Suggest: `Bladwijzer voor koppeling maken`
    - The source specifies bookmarking a link URL; the other context-menu items in this group consistently render "Link" as "koppeling" (e.g. "Koppeling kopiëren", "Koppeling delen"), so omitting it here is inconsistent and drops meaning.
- `ErrorPages.CertWarning.Title` — `Shared/en.lproj/Localizable.strings` — "Untrusted" is rendered as "niet beveiligd" (not secure) instead of "niet vertrouwd".
    - Current: `Deze verbinding is niet beveiligd`
    - Suggest: `Deze verbinding is niet vertrouwd`
    - The source says the connection is untrusted, not insecure; "beveiligd" translates "secure", which is a different concept and is already used for "secure" in ErrorPages.AdvancedWarning1.Text.
- `Search.SuggestSectionTitle.v102` — `Shared/en.lproj/Localizable.strings` — "Firefox Suggest" is a product/feature name that must remain untranslated, but it has been rendered as "Firefox Suggesties".
    - Current: `Firefox Suggesties`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a brand feature name; translating "Suggest" to "Suggesties" changes the product name.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `Shared/en.lproj/Localizable.strings` — "some ad tracking" is rendered as "enkele advertentietrackers" (some ad trackers), changing the meaning.
    - Current: `Staat enkele advertentietrackers toe`
    - Suggest: `Staat enige advertentietracking toe`
    - The source says it allows some ad tracking (the activity), not some ad trackers (entities).
- `Toolbar.Menu.CloseAllTabs` — `Shared/en.lproj/Localizable.strings` — Spelling error: "All" should be "Alle" in Dutch.
    - Current: `All tabbladen sluiten`
    - Suggest: `Alle tabbladen sluiten`
    - "All" is the English word; the Dutch determiner is "Alle".
- `TopSites.RemovePage.Button` — `Shared/en.lproj/Localizable.strings` — Em dash from the source replaced with an en dash.
    - Current: `Pagina verwijderen – %@`
    - Suggest: `Pagina verwijderen — %@`
    - The en-US string uses an em dash (—); the translation uses an en dash (–).

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,918 |
| Missing strings | 4 |
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

**4 strings** are not translated yet, concentrated in:

- `nl/firefox-ios.xliff` — 2
- `nl/firefox-ios.xliff` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 14 | **curly-single** |
| apostrophe | `typographic` 31 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 4 | **en** |
| register | `formal` 280 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (49)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `nl/firefox-ios.xliff` — "marketing partners" is translated as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `marketingtechnologiepartners`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `marketingpartners`
    - The source says only "%2$@’s marketing partners"; the Dutch claims data is shared with marketing technology partners, which the source never states.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 22 |
| 3 | Degraded language (grammar, spelling, terminology) | 26 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `nl/firefox-ios.xliff` — "saved passwords" is rendered as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `uw opgeslagen aanmeldingen en betalingsmethoden`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `uw opgeslagen wachtwoorden en betalingsmethoden`
    - The en-US says "saved passwords"; the Dutch says "logins", a different term than the source uses.
- `Biometry.Screen.UniversalAuthenticationReason.v122` — `nl/firefox-ios.xliff` — ‘saved passwords’ is translated as ‘opgeslagen aanmeldingen’ (saved logins) instead of ‘opgeslagen wachtwoorden’.
    - Current: `uw opgeslagen aanmeldingen en betalingsmethoden`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `uw opgeslagen wachtwoorden en betalingsmethoden`
    - The source says ‘passwords’; the sibling string v115 correctly uses ‘wachtwoorden’, making the terminology inconsistent as well.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `nl/firefox-ios.xliff` — "Tracking content" is translated as "Volginhoud" while the rest of the screen consistently uses the loanword "trackers"/"tracking".
    - Current: `Volginhoud: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Trackinginhoud: %@`
    - The surrounding strings in the same screen use "trackers" and "trackingcookies"; "Volginhoud" introduces an inconsistent term for "tracking content".
- `MainMenu.HeaderBanner.Subtitle.v142` — `nl/firefox-ios.xliff` — "Takes seconds. Change anytime." is rendered with an odd phrase and an imperative that loses the meaning "you can change it at any time".
    - Current: `Zo gebeurd. Wijzig op elk moment.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Duurt maar enkele seconden. U kunt dit altijd wijzigen.`
    - The source says the action takes only seconds and can be changed at any time; the Dutch 'Wijzig op elk moment' is an imperative command to change it, not a statement that it can be changed later.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `nl/firefox-ios.xliff` — "Home" (iOS Home screen) is translated as "Startpagina" (homepage) instead of "Beginscherm/Startscherm".
    - Current: `Startpagina`
    - Source: `Home`
    - Suggest: `Startscherm`
    - The developer comment says this refers to the iOS Home screen, and the related title string uses 'startscherm'; 'Startpagina' means homepage, a different concept used elsewhere for Customize Homepage.
- `Microsurvey.Survey.Options.Neutral.v132` — `nl/firefox-ios.xliff` — 'Neutral' rendered as 'Gemiddeld' (average) instead of 'Neutraal'.
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
    - The source option is 'Neutral', the mid-point of a satisfaction scale; 'Gemiddeld' means 'average' and is a different term.
- `Onboarding.Customization.Theme.System.Action.v123` — `nl/firefox-ios.xliff` — "System Auto" is rendered as "Systeemthema", dropping the automatic aspect and matching the wrong concept.
    - Current: `Systeemthema`
    - Source: `System Auto`
    - Suggest: `Systeem automatisch`
    - The source option is "System Auto" (follow the device automatically); "Systeemthema" just means "system theme" and loses the 'auto' meaning.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `nl/firefox-ios.xliff` — "all in one place" is weakened and the em/en dash structure dropped, changing "get ... – all in one place" to "ontvangen op één plek".
    - Current: `op één plek te ontvangen`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `te krijgen – allemaal op één plek`
    - The source lists items then emphasizes "– all in one place"; the Dutch drops "all" and the dash, altering the emphasis of the sentence.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `nl/firefox-ios.xliff` — "marketing partners" is translated as "marketingtechnologiepartners", adding "technologie" which is not in the source.
    - Current: `marketingtechnologiepartners`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `marketingpartners`
    - The source says only "%2$@’s marketing partners"; the Dutch claims data is shared with marketing technology partners, which the source never states.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `nl/firefox-ios.xliff` — "have %@ match your device" mistranslated as "laat %@ met uw apparaat overeenkomen", which reverses/obscures that the app should match the device theme.
    - Current: `of laat %@ met uw apparaat overeenkomen`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `of laat %@ het thema van uw apparaat volgen`
    - The source means Firefox should follow the device's theme; the Dutch phrasing is ambiguous/incorrect Dutch for that meaning.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `nl/firefox-ios.xliff` — "get search suggestions ... – all in one place" is rendered as "ontvangen" (receive) and the "all in one place" emphasis is dropped/merged.
    - Current: `om zoeksuggesties, uw topwebsites, bladwijzers, geschiedenis en zoekmachines op één plek te ontvangen`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `om zoeksuggesties, uw topwebsites, bladwijzers, geschiedenis en zoekmachines te krijgen – alles op één plek`
    - The source lists items and then adds "– all in one place" as an appositive; the Dutch loses the dash construction and uses "ontvangen", which does not convey "get" here.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `nl/firefox-ios.xliff` — "for everyone" is rendered as "voor gebruikers overal" (for users everywhere), changing the meaning.
    - Current: `voor gebruikers overal`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users everywhere".
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `nl/firefox-ios.xliff` — "for everyone" is rendered as "voor gebruikers overal" (for users everywhere), changing the meaning.
    - Current: `voor gebruikers overal`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users everywhere".
- `Summarizer.Footnote.Label.v144` — `nl/firefox-ios.xliff` — "Summarization can make errors" is translated as "samenvattingen kunnen fouten bevatten", shifting the meaning about the feature.
    - Current: `Noot: samenvattingen kunnen fouten bevatten.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Noot: samenvatten kan fouten opleveren.`
    - The source warns that the summarization process can make mistakes; the Dutch states the summaries contain errors, a slightly different assertion about the product output.
- `Toolbar.Translation.LoadingButton.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — "Translating page" (progress state) is rendered as an imperative/infinitive "Pagina vertalen", identical to the inactive "Translate page" label.
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The source is a progress indication that translation is in progress, not the action label; it is also indistinguishable from Toolbar.Translation.ButtonInactive.AccessibilityLabel.v145 ("Translate page"), defeating the accessibility distinction.
- `Translations.Banner.Loading.Button.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — "Translating page" (in-progress state) is translated as "Pagina vertalen", which means "Translate page".
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The source describes an ongoing process (loading button while the page is being translated), not an action to perform.
- `Translations.Sheet.LoadingButton.v145` — `nl/firefox-ios.xliff` — "Translating page" (in-progress state) is translated as "Pagina vertalen" ("Translate page").
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - Per the comment the button indicates that the page is being translated; the Dutch reads as the action label instead, and duplicates Translations.Sheet.TitleLabel "Pagina vertalen".
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `nl/firefox-ios.xliff` — The Dutch attaches "on this page" to the hostnames rather than to the blocking, changing the meaning.
    - Current: `Op deze pagina geblokkeerde hostnamen van trackers`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Hostnamen van trackers die op deze pagina zijn geblokkeerd`
    - Source is "Hostnames of trackers blocked on this page": the trackers were blocked on this page. The Dutch reads as "hostnames of trackers that were blocked on this page" only ambiguously; as written it modifies 'hostnamen', implying the hostnames are blocked on the page.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `nl/firefox-ios.xliff` — ‘Full time’ is translated as ‘Gelijkspel’ (draw) instead of end of match.
    - Current: `Gelijkspel • Penalty’s (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Wedstrijd afgelopen • Penalty’s (%@)`
    - The source says ‘Full time’, meaning the match has ended; ‘Gelijkspel’ means ‘draw’, a different statement about the result. Other strings in this file render ‘Full Time’ as ‘Wedstrijd afgelopen’, so it is also inconsistent.
- `LibraryPanel.History.AllTimeOption.v138` — `nl/firefox-ios.xliff` — “All Time” (time range covering everything) is translated as “Altijd” (always), not the time-range sense.
    - Current: `Altijd`
    - Source: `All Time`
    - Suggest: `Alles`
    - The option clears browsing history for the entire period; Dutch “Altijd” means “always” and does not convey the ‘all time’ range used alongside ‘Laatste uur’, ‘Afgelopen 7 dagen’.
- `ErrorPages.CertWarning.Title` — `nl/firefox-ios.xliff` — ‘Untrusted’ is rendered as ‘niet beveiligd’ (not secure) instead of ‘niet vertrouwd’.
    - Current: `Deze verbinding is niet beveiligd`
    - Source: `This Connection is Untrusted`
    - Suggest: `Deze verbinding is niet vertrouwd`
    - The source says the connection is untrusted, not insecure; ‘beveiligd’ means secure/encrypted, which is a different claim.
- `PhotoLibrary.FirefoxWouldLikeAccessTitle` — `nl/firefox-ios.xliff` — “would like to access” rendered as “vraagt om toegang” (is asking for access) instead of “wil toegang”.
    - Current: `Firefox vraagt om toegang tot uw foto’s`
    - Source: `Firefox would like to access your Photos`
    - Suggest: `Firefox wil toegang tot uw foto’s`
    - The source states Firefox would like to access your Photos; the Dutch changes it to Firefox requesting access.
- `Search.SuggestSectionTitle.v102` — `nl/firefox-ios.xliff` — Brand name “Firefox Suggest” has been partially translated.
    - Current: `Firefox Suggesties`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - “Firefox Suggest” is a product/feature brand name that must stay untranslated; “Suggesties” alters the brand.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `nl/firefox-ios.xliff` — "some ad tracking" is rendered as "enkele advertentietrackers" (some ad trackers), naming objects instead of the activity.
    - Current: `Staat enkele advertentietrackers toe`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Staat enige advertentietracking toe`
    - The source says the standard level allows some ad tracking (the activity), not that it permits specific ad trackers.

### C. Grammar, agreement & spelling

- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `nl/firefox-ios.xliff` — ‘DESKTOP BOOKMARKS’ is rendered as the malformed compound ‘BUREAUBLADWIJZERS’ instead of ‘BUREAUBLADBLADWIJZERS’ / ‘BLADWIJZERS VAN BUREAUBLAD’.
    - Current: `BUREAUBLADWIJZERS`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `BUREAUBLAD-BLADWIJZERS`
    - The source means bookmarks synced from desktop; the blend ‘bureaubladwijzers’ collapses ‘bureaublad’ and ‘bladwijzers’ into a non-word and loses the meaning, and it is inconsistent with ‘MOBIELE BLADWIJZERS’ on the same screen.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `nl/firefox-ios.xliff` — Ungrammatical compound "mobielwebsite".
    - Current: `Naar mobielwebsite`
    - Source: `Switch to mobile site`
    - Suggest: `Naar mobiele website`
    - Dutch does not compound an adjective with a noun this way; the correct form is "mobiele website" (compare "desktopwebsite", where "desktop" is a noun).
- `MainMenu.ToolsSection.SwitchToMobileSite.Title.v131` — `nl/firefox-ios.xliff` — Compound 'mobielwebsite' is ungrammatical; the adjective must be inflected as a separate word.
    - Current: `Naar mobielwebsite`
    - Source: `Switch to Mobile Site`
    - Suggest: `Naar mobiele website`
    - 'mobiel' is an adjective, not a noun that can form a compound like 'desktopwebsite'; correct Dutch is 'mobiele website'.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `nl/firefox-ios.xliff` — Untranslated English article 'the' left in the Dutch sentence, producing ungrammatical text.
    - Current: `van the Internet Archive`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `van het Internet Archive`
    - The source reads "the Internet Archive’s %2$@"; the Dutch keeps the English article "the" inside a Dutch sentence, which is ungrammatical.
- `Search.Google.Title.v108` — `nl/firefox-ios.xliff` — Incorrect capitalization of the common noun in "Google Zoeken".
    - Current: `Google Zoeken`
    - Source: `Google Search`
    - Suggest: `Google-zoekopdracht`
    - Dutch does not use English title case; "Zoeken" should not be capitalized mid-phrase.
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Title.v154` — `nl/firefox-ios.xliff` — English title case carried over: "Antwoorden" should be lowercase in Dutch.
    - Current: `Snelle Antwoorden`
    - Source: `Quick Answers`
    - Suggest: `Snelle antwoorden`
    - Dutch sentence-case capitalization rules; the parallel string "Paginasamenvattingen" is not title-cased either.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `nl/firefox-ios.xliff` — Incorrect Dutch compound ellipsis: 'tabbladen- en adresbalk' should be 'tabblad- en adresbalk'.
    - Current: `Scrollen om tabbladen- en adresbalk te verbergen`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Scrollen om tabblad- en adresbalk te verbergen`
    - The source is 'Tab and Address Bar' (singular 'tab bar'); the elided compound part must be 'tabbalk', so the correct ellipsis form is 'tabblad- en adresbalk'.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `nl/firefox-ios.xliff` — The subtitle lacks a subject/verb and reads as a fragment rather than a sentence.
    - Current: `Over %1$@ vertellen telkens als u een koppeling op %2$@ deelt.`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `Vertel anderen over %1$@ telkens als u een koppeling op %2$@ deelt.`
    - The en-US is an imperative sentence "Spread the word about %1$@…"; the Dutch infinitive fragment is ungrammatical as a standalone sentence.
- `TermsOfUse.LearnMoreHere.v147` — `nl/firefox-ios.xliff` — Word order makes the sentence with the 'here' link read incorrectly in Dutch.
    - Current: `U vindt %@ meer info.`
    - Source: `You can learn more %@.`
    - Suggest: `U kunt %@ meer info vinden.`
    - The source is 'You can learn more %@.' where %@ is the link text 'hier'. 'U vindt hier meer info' is only correct with the link directly after the verb; as rendered the placeholder sits between 'vindt' and 'meer info', which is awkward/ungrammatical word order for the intended 'here' link.
- `Translations.LanguagePicker.Title.v151` — `nl/firefox-ios.xliff` — Title ends with a dangling article before the ellipsis.
    - Current: `Pagina vertalen naar het…`
    - Source: `Translate Page to…`
    - Suggest: `Pagina vertalen naar…`
    - The source "Translate Page to…" has no following language name in this string, so "het" is left hanging and ungrammatical.
- `Translations.Sheet.TranslateFromLabel.v145` — `nl/firefox-ios.xliff` — Label ends with a dangling article "het" although no language name follows in this string.
    - Current: `Vertalen vanuit het`
    - Source: `Translate From`
    - Suggest: `Vertalen vanuit`
    - This is a standalone cell label ("Translate From") with no language placeholder, so the trailing article is ungrammatical.
- `Translations.Sheet.TranslateToLabel.v145` — `nl/firefox-ios.xliff` — Label ends with a dangling article "het" although no language name follows in this string.
    - Current: `Vertalen naar het`
    - Source: `Translate To`
    - Suggest: `Vertalen naar`
    - This is a standalone cell label ("Translate To") without a language placeholder, so the trailing article is ungrammatical.
- `WorldCup.HomepageWidget.PenaltiesLabel.v151` — `nl/firefox-ios.xliff` — Dutch plural of 'penalty' is written 'penalty’s' — but here the football term should be 'Penalty’s' capitalized correctly; the apostrophe-s form is fine, however 'Penalties' should be rendered as 'Strafschoppen' or 'Penalty’s'.
    - Current: `Penalty’s (%@)`
    - Source: `Penalties (%@)`
    - Suggest: `Strafschoppen (%@)`
    - Placeholder-only concern aside, the football phase 'Penalties' (penalty shoot-out) is normally 'Strafschoppen' in Dutch; 'Penalty’s' is the plural of a single penalty kick and reads oddly as a match-phase label.
- `WorldCup.HomepageWidget.RoundPhase.QuarterFinalsLabel.v151` — `nl/firefox-ios.xliff` — Plural 'QUARTER-FINALS' rendered as singular 'KWARTFINALE'.
    - Current: `KWARTFINALE`
    - Source: `QUARTER-FINALS`
    - Suggest: `KWARTFINALES`
    - The source is plural, and the parallel string SEMI-FINALS is correctly translated as the plural 'HALVE FINALES'; the singular is inconsistent and inaccurate.
- `Previous in-page result` — `nl/firefox-ios.xliff` — Wrong adjective inflection: “Vorige resultaat” should be “Vorig resultaat” with a neuter noun.
    - Current: `Vorige resultaat op pagina`
    - Source: `Previous in-page result`
    - Suggest: `Vorig resultaat op pagina`
    - ‘resultaat’ is a neuter (het) noun without article, so the adjective takes the uninflected form ‘vorig’.
- `Remove from Reading List` — `nl/firefox-ios.xliff` — Wrong preposition: “verwijderen van leeslijst” should be “verwijderen uit leeslijst”.
    - Current: `Verwijderen van leeslijst`
    - Source: `Remove from Reading List`
    - Suggest: `Verwijderen uit leeslijst`
    - Dutch uses “uit” for removing an item from a list; “van” is ungrammatical/ambiguous here.
- `Toolbar.Menu.CloseAllTabs` — `nl/firefox-ios.xliff` — Spelling error: “All” should be “Alle”.
    - Current: `All tabbladen sluiten`
    - Source: `Close All Tabs`
    - Suggest: `Alle tabbladen sluiten`
    - Dutch for “all” is “alle”; the same source string elsewhere (TabTray.CloseAllTabs.KeyCodeTitle) is correctly “Alle tabbladen sluiten”.

### D. Terminology, register & consistency

- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `nl/firefox-ios.xliff` — Inconsistent rendering of "Tools" submenu: elsewhere "Hulpmiddelen", here "Extra".
    - Current: `Submenu Extra`
    - Source: `Turn off Reader View`
    - Suggest: `Submenu Hulpmiddelen`
    - MainMenu.ToolsSection.AccessibilityLabels.Tools.v132 translates "Tools" as "Hulpmiddelen"; the same term on the same screen must be consistent.
- `Onboarding.Modern.BrandRefresh.Notification.TurnOn.Action.v148` — `nl/firefox-ios.xliff` — "notifications" is translated as "Notificaties" here but as "Meldingen" in the title on the same card.
    - Current: `Notificaties inschakelen`
    - Source: `Turn on notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Modern.BrandRefresh.Notification.Title.v148 uses "Meldingen" for the same source term on the same screen; inconsistent terminology.
- `Onboarding.Notification.TurnOnNotifications.Action.v114` — `nl/firefox-ios.xliff` — "Notifications" is translated as "Notificaties" here while the related notification onboarding strings use "Meldingen".
    - Current: `Notificaties inschakelen`
    - Source: `Turn On Notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Notification.Title.v120 on the same screen uses "Meldingen" for Notifications; the two renderings are inconsistent within one screen.
- `Summarizer.Error.MissingPageContent.Message.v142` — `nl/firefox-ios.xliff` — "hit summarize" is rendered as "klik op samenvatten" (click) on a touch-only iOS device.
    - Current: `klik daarna op samenvatten`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `tik daarna op samenvatten`
    - This is a phone UI; the source says "hit summarize" and other strings in this file use "Tik" for tapping. "Klik" (click) is wrong terminology for iOS.
- `WebCompatReporter.Category.DesignBroken.v154` — `nl/firefox-ios.xliff` — "defect" is the wrong term for a broken page layout.
    - Current: `Ontwerp is defect`
    - Source: `Design is broken`
    - Suggest: `Ontwerp is kapot`
    - "defect" in Dutch describes faulty hardware/devices; for a broken site layout the established rendering is "kapot"/"werkt niet goed".
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `nl/firefox-ios.xliff` — 'ROUND OF 16' is literally translated as 'RONDE VAN 16' instead of the established Dutch term.
    - Current: `RONDE VAN 16`
    - Source: `ROUND OF 16`
    - Suggest: `ACHTSTE FINALES`
    - In Dutch football terminology the round of 16 is called 'achtste finales'; 'ronde van 16' is a literal calque.
- `Menu.TrackingProtectionBlockedContent.Title` — `nl/firefox-ios.xliff` — "Tracking content" is rendered as "Volginhoud", inconsistent with the "trackers" terminology used in the surrounding tracking-protection strings.
    - Current: `Volginhoud`
    - Source: `Tracking content`
    - Suggest: `Volgende inhoud`
    - The other strings on this screen keep the English term ("Sociale trackers", "Cross-site-trackers", "Fingerprinters"); the Dutch Firefox term for "tracking content" is "volgende inhoud", not the coined "Volginhoud".

### E. Typography, punctuation & spacing

- `Onboarding.Modern.Sync.Description.v145` — `nl/firefox-ios.xliff` — Superfluous comma before "en meer" in a Dutch enumeration.
    - Current: `Uw bladwijzers, wachtwoorden, en meer`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Uw bladwijzers, wachtwoorden en meer`
    - Dutch does not use a serial comma before "en"; the source's Oxford comma should not be carried over.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
