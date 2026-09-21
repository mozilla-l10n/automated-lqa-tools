# Firefox iOS l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 32 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (1)

- `QuickAnswers.Settings.Title.v158` — `nl/firefox-ios.xliff` — Feature name capitalized inconsistently: "Snelle Antwoorden" here vs. "Snelle antwoorden" elsewhere in the same feature.
    - Current: `Snelle Antwoorden`
    - Source: `Quick Answers`
    - Suggest: `Snelle antwoorden`
    - Other strings in this batch (QuickAnswers.Errors.DailyLimitMessage, PermissionAlertTitle, AccessibilityLabels.OpenQuickAnswers) render the feature name as "Snelle antwoorden"; Dutch does not use title case.

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
| Strings | 1,950 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 14 | **curly-single** |
| apostrophe | `typographic` 31 | **typographic** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 4 | **en** |
| register | `formal` 287 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (50)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 22 |
| 3 | Degraded language (grammar, spelling, terminology) | 27 |
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
- `QuickAnswers.Settings.Title.v158` — `nl/firefox-ios.xliff` — Feature name capitalized inconsistently: "Snelle Antwoorden" here vs. "Snelle antwoorden" elsewhere in the same feature.
    - Current: `Snelle Antwoorden`
    - Source: `Quick Answers`
    - Suggest: `Snelle antwoorden`
    - Other strings in this batch (QuickAnswers.Errors.DailyLimitMessage, PermissionAlertTitle, AccessibilityLabels.OpenQuickAnswers) render the feature name as "Snelle antwoorden"; Dutch does not use title case.
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
