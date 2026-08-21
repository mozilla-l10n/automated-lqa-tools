# Firefox iOS l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | 2026-08-21 @ `7e1ae61658ad` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,906 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for nl: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,906 |
| Missing strings | 4 |
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

**4 strings** are not translated yet, concentrated in:

- `nl/firefox-ios.xliff` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 14 | **curly-single** |
| apostrophe | `typographic` 31 | **typographic** |
| ellipsis | `char` 19 | **char** |
| dash | `en` 4 | **en** |
| register | `formal` 279 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (43)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 25 |
| 3 | Degraded language (grammar, spelling, terminology) | 16 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `nl/firefox-ios.xliff` — "saved passwords" is translated as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `opgeslagen aanmeldingen`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `opgeslagen wachtwoorden`
    - The en-US source says "saved passwords"; Firefox terminology for passwords in nl is "wachtwoorden", while "aanmeldingen" renders the older term "logins".
- `Biometry.Screen.UniversalAuthenticationReason.v122` — `nl/firefox-ios.xliff` — "saved passwords" is translated as "opgeslagen aanmeldingen" (saved logins) instead of "opgeslagen wachtwoorden".
    - Current: `opgeslagen aanmeldingen`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `opgeslagen wachtwoorden`
    - The source says "your saved passwords"; the v115 sibling string correctly uses "wachtwoorden". "Aanmeldingen" is the older "logins" term and is inconsistent with the source and the neighbouring string.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `nl/firefox-ios.xliff` — "Department" as an administrative division (France/Colombia) is translated as "Afdeling" (organizational department).
    - Current: `Afdeling`
    - Source: `Department`
    - Suggest: `Departement`
    - The developer comment states this is the administrative division used in countries like France and Colombia; Dutch uses "departement" for that, whereas "afdeling" means a company/organizational department.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `nl/firefox-ios.xliff` — "Tracking content" is rendered as "Volginhoud" but the label needs to convey tracking content, and here the Dutch term used is inconsistent/incorrect relative to the other tracker labels which keep "tracking".
    - Current: `Volginhoud: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Volgende inhoud: %@`
    - The other strings in this screen keep the English-based term ("trackingcookies", "trackers"); "Volginhoud" is not the established Dutch Firefox term for "Tracking content", which is "Volgende inhoud".
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `nl/firefox-ios.xliff` — Singular "email" is translated as plural "E-mailberichten".
    - Current: `E-mailberichten openen in de standaard e-mailtoepassing?`
    - Source: `Open email in the default mail application?`
    - Suggest: `E-mailbericht openen in de standaard e-mailtoepassing?`
    - The source asks about opening the single mail link the user tapped, not multiple messages.
- `MainMenu.HeaderBanner.Subtitle.v142` — `nl/firefox-ios.xliff` — "Takes seconds." is translated as "Zo gebeurd." and the second sentence uses an informal imperative inconsistent with the u-register.
    - Current: `Zo gebeurd. Wijzig op elk moment.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Duurt maar enkele seconden. U kunt dit altijd wijzigen.`
    - The source states the action takes only seconds and can be changed anytime; 'Zo gebeurd' loses that meaning, and elsewhere in this file the polite 'u' form with full sentences is used.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `nl/firefox-ios.xliff` — "Home" here refers to the iOS home screen, not a home page.
    - Current: `Startpagina`
    - Source: `Home`
    - Suggest: `Beginscherm`
    - The developer comment states this is for the Add to Home screen tool for the iOS Home screen; the paired title uses "startscherm", so "Startpagina" (home page) is the wrong referent.
- `MainMenu.Submenus.Save.AddToHomeScreen.Subtitle.v131` — `nl/firefox-ios.xliff` — "Home" here refers to the iOS home screen, not a home page.
    - Current: `Startpagina`
    - Source: `Home`
    - Suggest: `Beginscherm`
    - The developer comment says this subtitle belongs to the Add to Homescreen tool; the accompanying title is translated as "Toevoegen aan startscherm", so "Startpagina" (home page) names the wrong thing and is inconsistent.
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `nl/firefox-ios.xliff` — "Unselected" (a state) is rendered as "Selectie opgeheven" (an action/event, deselected).
    - Current: `Selectie opgeheven`
    - Source: `Unselected`
    - Suggest: `Niet geselecteerd`
    - The comment says this label states that the survey option was not selected — a state, not the action of deselecting.
- `Onboarding.Customization.Theme.System.Action.v123` — `nl/firefox-ios.xliff` — "System Auto" is translated as "Systeemthema" (system theme), losing the automatic aspect.
    - Current: `Systeemthema`
    - Source: `System Auto`
    - Suggest: `Systeem automatisch`
    - The source option is "System Auto", indicating automatic following of the system setting, not simply "system theme".
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `nl/firefox-ios.xliff` — "get search suggestions ... all in one place" is translated as "ontvangen" (receive) and the "all in one place" emphasis is dropped.
    - Current: `en zoekmachines op één plek te ontvangen`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `en zoekmachines te krijgen – alles op één plek`
    - The source lists items and then concludes with "– all in one place"; the Dutch merges it and loses the "all" summary clause.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `nl/firefox-ios.xliff` — "marketing partners" is rendered as "marketingtechnologiepartners" (marketing technology partners), adding a term not in the source.
    - Current: `%2$@’s marketingtechnologiepartners`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `%2$@’s marketingpartners`
    - The en-US source says "%2$@’s marketing partners", not "marketing technology partners".
- `Onboarding.Modern.Customization.Theme.Description.v145` — `nl/firefox-ios.xliff` — "have %@ match your device" is mistranslated as "laat %@ met uw apparaat overeenkomen", which reverses/obscures the meaning of the theme following the device setting.
    - Current: `of laat %@ met uw apparaat overeenkomen`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `of laat %@ overeenkomen met uw apparaatinstelling`
    - The source means the app's theme should match the device theme; the Dutch literal rendering is ambiguous but arguably acceptable — however "laat %@ met uw apparaat overeenkomen" states the app matches the device rather than the theme.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `nl/firefox-ios.xliff` — "for everyone" is mistranslated as "voor gebruikers overal" (for users everywhere).
    - Current: `voor gebruikers overal`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `voor iedereen`
    - The source says the data helps improve features for everyone, not for users everywhere.
- `Summarizer.Error.MissingPageContent.Message.v142` — `nl/firefox-ios.xliff` — "hit summarize" is rendered as "klik op" (click) on a touch device, and "Wacht tot deze is voltooid" misattributes completion to the page.
    - Current: `Wacht tot deze is voltooid en klik daarna op samenvatten.`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `Wacht tot het laden is voltooid en tik daarna op Samenvatten.`
    - The source says to wait for the loading to finish and then tap summarize; on iOS the interaction is tapping, not clicking.
- `Toolbar.Translation.LoadingButton.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — Progressive state "Translating page" is rendered as the infinitive "Pagina vertalen" (Translate page), losing the in-progress meaning.
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The source indicates the page is currently being translated; the Dutch reads as the command/label "Translate page", identical to Toolbar.Translation.ButtonInactive ("Translate page"), so the two opposite states are indistinguishable.
- `Translations.Banner.Loading.Button.AccessibilityLabel.v145` — `nl/firefox-ios.xliff` — "Translating page" (in progress) is translated as "Pagina vertalen" (Translate page).
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The loading state must convey that translation is ongoing; the Dutch is identical to the title "Translate Page" (Translations.Sheet.TitleLabel), so it does not express the progressive state.
- `Translations.Sheet.LoadingButton.v145` — `nl/firefox-ios.xliff` — "Translating page" (in progress) is translated as "Pagina vertalen" (Translate page).
    - Current: `Pagina vertalen`
    - Source: `Translating page`
    - Suggest: `Pagina wordt vertaald`
    - The button indicates the page is being translated; the Dutch infinitive reads as the action label and duplicates Translations.Sheet.TitleLabel "Pagina vertalen".
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `nl/firefox-ios.xliff` — Modifier attached to the wrong noun: it now says hostnames blocked on this page instead of trackers blocked on this page.
    - Current: `Op deze pagina geblokkeerde hostnamen van trackers`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Hostnamen van op deze pagina geblokkeerde trackers`
    - Source "Hostnames of trackers blocked on this page" — the blocking applies to the trackers, not to the hostnames.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `nl/firefox-ios.xliff` — "Full time" is translated as "Gelijkspel" (draw) instead of end of match.
    - Current: `Gelijkspel • Penalty’s (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Wedstrijd afgelopen • Penalty’s (%@)`
    - The source says "Full time" (end of regular play), which the sibling strings FTLabel/FTNoParenthesisLabel render as "Wedstrijd afgelopen". "Gelijkspel" means "draw", a different meaning and inconsistent with the same term elsewhere on the screen.
- `LibraryPanel.History.AllTimeOption.v138` — `nl/firefox-ios.xliff` — 'All Time' as a time-range option is translated as 'Altijd' (always) instead of 'Alles'/'Alle tijd'.
    - Current: `Altijd`
    - Source: `All Time`
    - Suggest: `Alles`
    - The option clears all browsing history regardless of period; 'Altijd' means 'always' and does not convey the time-range 'All Time'.
- `ContextMenu.BookmarkLinkButtonTitle` — `nl/firefox-ios.xliff` — "Bookmark Link" is translated without the "link" part, losing the distinction from bookmarking the page.
    - Current: `Bladwijzer maken`
    - Source: `Bookmark Link`
    - Suggest: `Bladwijzer voor koppeling maken`
    - The source specifies bookmarking a link URL; the other context-menu items in this group consistently render "Link" as "koppeling" (e.g. "Koppeling kopiëren", "Koppeling delen"), so omitting it here is inconsistent and drops meaning.
- `ErrorPages.CertWarning.Title` — `nl/firefox-ios.xliff` — "Untrusted" is rendered as "niet beveiligd" (not secure) instead of "niet vertrouwd".
    - Current: `Deze verbinding is niet beveiligd`
    - Source: `This Connection is Untrusted`
    - Suggest: `Deze verbinding is niet vertrouwd`
    - The source says the connection is untrusted, not insecure; "beveiligd" translates "secure", which is a different concept and is already used for "secure" in ErrorPages.AdvancedWarning1.Text.
- `Search.SuggestSectionTitle.v102` — `nl/firefox-ios.xliff` — "Firefox Suggest" is a product/feature name that must remain untranslated, but it has been rendered as "Firefox Suggesties".
    - Current: `Firefox Suggesties`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a brand feature name; translating "Suggest" to "Suggesties" changes the product name.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `nl/firefox-ios.xliff` — "some ad tracking" is rendered as "enkele advertentietrackers" (some ad trackers), changing the meaning.
    - Current: `Staat enkele advertentietrackers toe`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Staat enige advertentietracking toe`
    - The source says it allows some ad tracking (the activity), not some ad trackers (entities).

### C. Grammar, agreement & spelling

- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `nl/firefox-ios.xliff` — "BUREAUBLADWIJZERS" is a malformed blend; it should be "BUREAUBLADBLADWIJZERS" or better "BLADWIJZERS OP BUREAUBLAD".
    - Current: `BUREAUBLADWIJZERS`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `BUREAUBLADBLADWIJZERS`
    - "Desktop bookmarks" is "bureaublad" + "bladwijzers"; the current form collapses the two words into a nonword that reads as "desk-pointers", losing the "bookmarks" meaning. The parallel string uses "MOBIELE BLADWIJZERS".
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `nl/firefox-ios.xliff` — "mobielwebsite" is not a valid Dutch compound; the adjective should be "mobiele".
    - Current: `Naar mobielwebsite`
    - Source: `Switch to mobile site`
    - Suggest: `Naar mobiele website`
    - "mobiel" is an adjective and must be inflected before a de-word ("mobiele website"); it cannot be glued into a compound like "desktopwebsite" (where "desktop" is a noun).
- `MainMenu.ToolsSection.SwitchToMobileSite.Title.v131` — `nl/firefox-ios.xliff` — "mobielwebsite" is not a valid Dutch compound; the adjective should be "mobiele".
    - Current: `Naar mobielwebsite`
    - Source: `Switch to Mobile Site`
    - Suggest: `Naar mobiele website`
    - "mobiel" is an adjective requiring inflection before a de-word: "mobiele website". Unlike "desktopwebsite", it cannot form a compound.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `nl/firefox-ios.xliff` — Untranslated English article "the" left inside the Dutch sentence.
    - Current: `vanuit %2$@ van the Internet Archive`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `vanuit de %2$@ van het Internet Archive`
    - "van the Internet Archive" mixes English article into Dutch; the source is "from the Internet Archive’s Wayback Machine".
- `Settings.AIControls.AIPoweredFeaturesSection.QuickAnswersSection.Title.v154` — `nl/firefox-ios.xliff` — Unnecessary capitalization of the second word; Dutch uses sentence case.
    - Current: `Snelle Antwoorden`
    - Source: `Quick Answers`
    - Suggest: `Snelle antwoorden`
    - Dutch capitalization rules capitalize only the first word of a title; the sibling feature titles in the same section ("Paginasamenvattingen", "Vertaling", "AI-verbeteringen blokkeren") follow sentence case.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `nl/firefox-ios.xliff` — Incorrect compound coordination "tabbladen- en adresbalk" instead of "tabblad- en adresbalk".
    - Current: `Scrollen om tabbladen- en adresbalk te verbergen`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Scrollen om tabblad- en adresbalk te verbergen`
    - The source is "Tab and Address Bar" (singular tab bar); the Dutch elided compound should use the singular stem "tabbalk" → "tabblad- en adresbalk".
- `TermsOfUse.LearnMoreHere.v147` — `nl/firefox-ios.xliff` — Word order places the 'here' link incorrectly, producing ungrammatical Dutch.
    - Current: `U vindt %@ meer info.`
    - Source: `You can learn more %@.`
    - Suggest: `U kunt %@ meer info vinden.`
    - The source is 'You can learn more %@.' where %@ is the link text 'hier'. 'U vindt hier meer info.' would be acceptable, but 'U vindt %@ meer info.' with the placeholder in that slot reads as broken; the intended sentence requires the link at the natural adverbial position, e.g. 'U kunt %@ meer info vinden.'
- `Translations.LanguagePicker.Title.v151` — `nl/firefox-ios.xliff` — Title ends with a dangling article "het" before the ellipsis.
    - Current: `Pagina vertalen naar het…`
    - Source: `Translate Page to…`
    - Suggest: `Pagina vertalen naar…`
    - There is no language name in this string, so the article "het" has nothing to modify and the phrase is ungrammatical.
- `Translations.Sheet.TranslateFromLabel.v145` — `nl/firefox-ios.xliff` — Standalone cell label ends in a dangling article "het" with no language name following.
    - Current: `Vertalen vanuit het`
    - Source: `Translate From`
    - Suggest: `Vertalen vanuit`
    - Unlike the accessibility label where %@ supplies the language, this string has no placeholder, so "het" is left hanging and ungrammatical.
- `Translations.Sheet.TranslateToLabel.v145` — `nl/firefox-ios.xliff` — Dangling article "het" at the end of the label makes the phrase ungrammatical.
    - Current: `Vertalen naar het`
    - Source: `Translate To`
    - Suggest: `Vertalen naar`
    - The source is "Translate To"; the trailing definite article "het" has no noun to attach to and leaves an incomplete Dutch phrase.
- `WorldCup.HomepageWidget.RoundPhase.QuarterFinalsLabel.v151` — `nl/firefox-ios.xliff` — Plural 'QUARTER-FINALS' rendered as singular 'KWARTFINALE'.
    - Current: `KWARTFINALE`
    - Source: `QUARTER-FINALS`
    - Suggest: `KWARTFINALES`
    - The source is plural (compare SEMI-FINALS translated as 'HALVE FINALES'), so the quarter-finals label should also be plural.
- `Previous in-page result` — `nl/firefox-ios.xliff` — Wrong adjective inflection with the neuter noun 'resultaat'.
    - Current: `Vorige resultaat op pagina`
    - Source: `Previous in-page result`
    - Suggest: `Vorig resultaat op pagina`
    - 'Resultaat' is a neuter noun; without an article the attributive adjective takes no -e ending, so it must be 'Vorig resultaat' (compare 'Volgende', which is invariable).
- `Toolbar.Menu.CloseAllTabs` — `nl/firefox-ios.xliff` — Spelling error: "All" should be "Alle" in Dutch.
    - Current: `All tabbladen sluiten`
    - Source: `Close All Tabs`
    - Suggest: `Alle tabbladen sluiten`
    - "All" is the English word; the Dutch determiner is "Alle".

### D. Terminology, register & consistency

- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `nl/firefox-ios.xliff` — "Tools" is rendered as "Extra" here but as "Hulpmiddelen" in the other Tools strings on the same menu.
    - Current: `Submenu Extra`
    - Source: `Tools submenu`
    - Suggest: `Submenu Hulpmiddelen`
    - MainMenu.ToolsSection.AccessibilityLabels.Tools.v132 and ToolsSubmenu.Title.v131 both translate "Tools" as "Hulpmiddelen"; the same submenu must be named consistently.
- `Onboarding.Modern.BrandRefresh.Notification.TurnOn.Action.v148` — `nl/firefox-ios.xliff` — "notifications" is rendered as "Notificaties" here but as "Meldingen" in the title of the same onboarding card.
    - Current: `Notificaties inschakelen`
    - Source: `Turn on notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Modern.BrandRefresh.Notification.Title.v148 uses "Meldingen" for the same source term on the same card; Mozilla nl standard term is "Meldingen".
- `Onboarding.Notification.TurnOnNotifications.Action.v114` — `nl/firefox-ios.xliff` — "Notifications" is rendered as "Notificaties" here but as "Meldingen" in the sibling notification onboarding title.
    - Current: `Notificaties inschakelen`
    - Source: `Turn On Notifications`
    - Suggest: `Meldingen inschakelen`
    - Onboarding.Notification.Title.v120 in the same screen translates "Notifications" as "Meldingen"; the same term should be used consistently.

### E. Typography, punctuation & spacing

- `Onboarding.Modern.Sync.Description.v145` — `nl/firefox-ios.xliff` — Superfluous comma before "en meer" in a Dutch enumeration.
    - Current: `Uw bladwijzers, wachtwoorden, en meer`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Uw bladwijzers, wachtwoorden en meer`
    - Dutch does not use the serial (Oxford) comma before "en"; the parallel string Onboarding.Modern.BrandRefresh.Sync.Description.v148 correctly omits it.
- `TopSites.RemovePage.Button` — `nl/firefox-ios.xliff` — Em dash from the source replaced with an en dash.
    - Current: `Pagina verwijderen – %@`
    - Source: `Remove page — %@`
    - Suggest: `Pagina verwijderen — %@`
    - The en-US string uses an em dash (—); the translation uses an en dash (–).

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
