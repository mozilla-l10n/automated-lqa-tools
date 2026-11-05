# Firefox iOS l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `101a216ab7b8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `101a216ab7b8` |
| **Previous run** | 2026-11-03 @ `4006ca053edd` |
| **Mode** | incremental |
| **Strings reviewed this run** | 3 of 1,980 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Strings | 1,980 |
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
| quotes | `guillemet` 18 | **guillemet** |
| apostrophe | `typographic` 376 | **typographic** |
| ellipsis | `char` 31 | **char** |
| dash | `em` 4, `en` 1 | **em** |
| nbsp | `total` 167, `before-punctuation` 99 | _mixed_ |
| register | `formal` 332 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (25)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 19 |
| 3 | Degraded language (grammar, spelling, terminology) | 6 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `fr/firefox-ios.xliff` — "upload audio" is rendered as "charger des fichiers audio" (load audio files) instead of envoyer/téléverser.
    - Current: `charger des fichiers audio`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `envoyer des fichiers audio`
    - en-US "upload" means sending audio to a server; "charger" reads as loading/opening files, which is a different action.
- `Settings.AppIconSelection.SectionNames.Gradients.Title.v139` — `fr/firefox-ios.xliff` — Plural section heading "Gradients" rendered as singular "Fond en dégradé", inconsistent with the other plural section headings.
    - Current: `Fond en dégradé`
    - Source: `Gradients`
    - Suggest: `Dégradés`
    - The source is the plural section name "Gradients", matching sibling headings "Basiques", "Colorées", "Autres"; the French introduces a singular "background" noun not in the source.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `fr/firefox-ios.xliff` — "Townland" is rendered as "Commune", which names a different administrative unit.
    - Current: `Commune`
    - Source: `Townland`
    - Suggest: `Townland`
    - A townland is a small rural land division (Ireland); "Commune" is the French municipality level and is also used for other address fields, so the label names the wrong thing.
- `CloseTab.ArrivingNotification.title.v133` — `fr/firefox-ios.xliff` — The app name placeholder is attached to "Onglets" as a modifier, changing the meaning.
    - Current: `Onglets %1$@ fermés : %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ : onglets fermés : %2$@`
    - The comment says %1$@ is the app name (e.g. Firefox) and the source reads "%1$@ tabs closed", i.e. Firefox announcing closed tabs; "Onglets Firefox fermés" reads as "Firefox tabs", a different meaning.
- `LibraryPanel.Section.Older` — `fr/firefox-ios.xliff` — "Older" (items older than thirty days) rendered as "Avant le mois dernier".
    - Current: `Avant le mois dernier`
    - Source: `Older`
    - Suggest: `Plus ancien`
    - The source is a generic "Older" section label for entries older than thirty days; "Avant le mois dernier" asserts a specific calendar-month boundary the source does not state.
- `NativeErrorPage.BadCertDomain.Description.v149` — `fr/firefox-ios.xliff` — "could also be set up incorrectly" (possibility) is rendered with the indicative "peuvent également être mal configurés", asserting it more strongly than the source.
    - Current: `Vos paramètres de connexion peuvent également être mal configurés.`
    - Source: `Someone pretending to be the site could try to steal your personal info. Your connection settings could also be set up incorrectly.`
    - Suggest: `Vos paramètres de connexion pourraient également être mal configurés.`
    - The source uses the conditional "could", matching the preceding "pourrait"; the indicative weakens the hypothetical framing.
- `NativeErrorPage.BadCertDomain.HideAdvancedButton.v149` — `fr/firefox-ios.xliff` — "Hide advanced" is translated as just "Masquer", dropping the object of the action.
    - Current: `Masquer`
    - Source: `Hide advanced`
    - Suggest: `Masquer les détails avancés`
    - The source names the advanced section that will be hidden; the French only says "Hide", losing the pairing with the "Avancé" button.
- `NativeErrorPage.CellularDataRestricted.Description.v156` — `fr/firefox-ios.xliff` — "go to iOS Settings and turn on cellular data for %@" is rephrased as "ouvrez les réglages d’iOS pour autoriser %@ à utiliser les données cellulaires", changing the instruction from turning on a setting to granting permission.
    - Current: `ouvrez les réglages d’iOS pour autoriser %@ à utiliser les données cellulaires`
    - Source: `Connect to Wi-Fi or go to iOS Settings and turn on cellular data for %@.`
    - Suggest: `ouvrez les réglages d’iOS et activez les données cellulaires pour %@`
    - The source gives two explicit steps (go to Settings, turn on cellular data for the app); the French merges them into a purpose clause and loses the "activez" instruction.
- `NativeErrorPage.GenericError.Description.v134` — `fr/firefox-ios.xliff` — Present tense "can’t be created" is rendered in the past as "n’a pas pu être établie".
    - Current: `une connexion sécurisée n’a pas pu être établie`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `une connexion sécurisée ne peut pas être établie`
    - The en-US states an ongoing impossibility ("a secure connection can’t be created"), not a past failed attempt.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `fr/firefox-ios.xliff` — "won’t sell you out" is rendered as "digne de confiance" (trustworthy), losing the meaning of not selling out/betraying the user.
    - Current: `Rapide, sûr et digne de confiance.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Rapide, sûr, et qui ne vous trahira pas.`
    - The en-US promises the browser will not sell the user out (i.e. not sell their data/betray them); "digne de confiance" is a vague generic claim that drops that specific commitment.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `fr/firefox-ios.xliff` — "your top sites" translated as "vos sites préférés" (favourite sites) instead of the Firefox term for Top Sites.
    - Current: `vos sites préférés`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `vos sites les plus visités`
    - "Top sites" is a Firefox feature name rendered elsewhere in fr as "sites les plus visités"; "sites préférés" suggests favourites/bookmarks, a different concept especially next to "marque-pages" in the same sentence.
- `Onboarding.Modern.TermsOfService.Description.v145` — `fr/firefox-ios.xliff` — "Brought to you by" rendered as "Conçu par" (designed by) and "non-profit" as "organisation" — acceptable, but "Conçu" asserts authorship rather than sponsorship.
    - Current: `Conçu par l’organisation à but non lucratif %@`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Proposé par l’organisation à but non lucratif %@`
    - The en-US says the product is "brought to you by" the non-profit, not designed/engineered by it.
- `QuickAnswers.ContentView.Answering.v158` — `fr/firefox-ios.xliff` — The loading label "Answering…" (an ongoing action) is rendered as the noun "Réponse…".
    - Current: `Réponse…`
    - Source: `Answering…`
    - Suggest: `Réponse en cours…`
    - The source is a progress indicator shown while the answer is being fetched; the bare noun "Réponse…" reads as a label for the answer itself rather than an in-progress state.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `fr/firefox-ios.xliff` — The French reverses the roles: it says "allow opening Firefox" instead of "allow Firefox to open" (the scanned URL).
    - Current: `Autoriser l’ouverture de %@ ?`
    - Source: `Allow %@ to open?`
    - Suggest: `Autoriser %@ à ouvrir cette adresse ?`
    - Source "Allow %@ to open?" asks permission for the app (%@ = Firefox) to open the scanned URL; the French makes Firefox the object being opened.
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `fr/firefox-ios.xliff` — The French adds "des conseils" (tips), which is not in the source "Learn about useful features and how to get the most out of %@."
    - Current: `Découvrez des fonctionnalités utiles et des conseils pour tirer le meilleur parti de %@.`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `Découvrez des fonctionnalités utiles et comment tirer le meilleur parti de %@.`
    - The source describes learning about features and how to get the most out of the app; "et des conseils" introduces content the source does not state.
- `Settings.Search.GoogleLens.Footnote.v153` — `fr/firefox-ios.xliff` — "your active search engine" is translated as "moteur de recherche principal" (main/primary), changing the meaning.
    - Current: `défini comme moteur de recherche principal lors de la navigation`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `défini comme moteur de recherche actif lors de la navigation`
    - The source says the engine must be the active one while browsing, not the "main" one; French "principal" is also confusable with "par défaut" used elsewhere on this screen.
- `Settings.Translation.AutoTranslate.Footer.v151` — `fr/firefox-ios.xliff` — "your top preferred language" is rendered as "la langue de votre choix", losing the notion of the highest-ranked preferred language.
    - Current: `Traduit automatiquement les pages dans la langue de votre choix.`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `Traduit automatiquement les pages dans votre première langue préférée.`
    - The source refers to the top entry of the Preferred Languages list, not simply any language the user chooses; the section is named « Langues préférées » in the same screen.
- `Open Last Bookmark` — `fr/firefox-ios.xliff` — The action verb "Open" is dropped, leaving only a noun phrase instead of an action label.
    - Current: `Dernier marque-page`
    - Source: `Open Last Bookmark`
    - Suggest: `Ouvrir le dernier marque-page`
    - en-US "Open Last Bookmark" describes the action of opening the last added bookmark; the French only names the bookmark and loses the verb.
- `Hotkeys.Forward.DiscoveryTitle` — `fr/firefox-ios.xliff` — Navigation "Forward" (page suivante dans l'historique) est traduit par « Suivant », mais le pendant de « Retour » dans la barre de navigation est « Suivant »/« Avancer » — ici le libellé doit correspondre à l'action de navigation avant.
    - Current: `Suivant`
    - Source: `Forward`
    - Suggest: `Avancer`
    - Paired with Hotkeys.Back.DiscoveryTitle ("Retour"), the source "Forward" refers to navigating forward in session history; French Firefox uses « Avancer » for this toolbar/shortcut action.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `fr/firefox-ios.xliff` — "some ad tracking" is rendered as "certains traqueurs publicitaires" (some ad trackers) and "websites" becomes the vague "des sites".
    - Current: `Autorise certains traqueurs publicitaires afin que des sites fonctionnent correctement.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Autorise une partie du pistage publicitaire afin que les sites web fonctionnent correctement.`
    - The source allows a certain amount of ad tracking, not a subset of trackers; "les sites web" is the correct rendering of "websites".
- `Search Input Field` — `fr/firefox-ios.xliff` — Accessibility label renders "Search Input Field" as an action "Rechercher des identifiants" instead of naming the field.
    - Current: `Rechercher des identifiants`
    - Source: `Search Input Field`
    - Suggest: `Champ de recherche`
    - The en-US string names the UI element (search input field) for VoiceOver; the French says "Search for logins", which is a different, action-style label.

### C. Grammar, agreement & spelling

- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `fr/firefox-ios.xliff` — "la barre d’adresse et d’onglets" incorrectly merges two separate bars (tab bar and address bar) into one.
    - Current: `Faire défiler pour masquer la barre d’adresse et d’onglets`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Faire défiler pour masquer la barre d’onglets et la barre d’adresse`
    - The source refers to the tab bar and the address bar as two distinct UI elements that are hidden on scroll.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `fr/firefox-ios.xliff` — Missing preposition: "des suggestions %@" should be "des suggestions de %@" (get suggestions from Firefox).
    - Current: `Obtenir des suggestions %@ en rapport avec votre recherche`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `Obtenir des suggestions de %@ en rapport avec votre recherche`
    - Source is "Get suggestions from %@"; the French drops the "from" preposition, leaving an ungrammatical noun juxtaposition.

### D. Terminology, register & consistency

- `Microsurvey.Survey.Sheet.AccessibilityLabel.v130` — `fr/firefox-ios.xliff` — "Survey" in the microsurvey context is translated as "Enquête" (investigation/inquiry) instead of the usual "Sondage".
    - Current: `Enquête`
    - Source: `Survey`
    - Suggest: `Sondage`
    - The feature is a microsurvey (questionnaire); French Firefox uses "sondage" for survey, while "enquête" suggests an investigation.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `fr/firefox-ios.xliff` — "Firefox Suggest" is rendered as "Firefox Suggest" here but as "Firefox suggère" in the neighbouring strings on the same settings screen.
    - Current: `Afficher les suggestions de Firefox Suggest dans les sessions privées`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Afficher les suggestions de Firefox suggère dans les sessions privées`
    - Settings.Search.Suggest.AddressBarSetting.Title.v124, Settings.Search.Suggest.LearnAboutSuggestions.v124 and Settings.Search.Accessibility.LearnAboutSuggestions.v124 all use "Firefox suggère" for the same product name on the same screen; one of the two renderings is inconsistent.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (8)

- `Keyboard.Shortcuts.FindAgain` — `fr/firefox-ios.xliff` — auto-suggest (2026-11-02): 'Find Again' (Cmd+G) jumps to the next match, and French Firefox labels this action 'Rechercher le suivant'.
- `PasswordGenerator.Description.v132` — `fr/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `Search.SuggestSectionTitle.v102` — `fr/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `fr/firefox-ios.xliff` — auto-suggest (2026-11-02): The en-US source is literally "OPENING SCREEN" and "ÉCRAN À L’OUVERTURE" translates it faithfully; any mismatch with the section purpose lies in the source.
- `Summarizer.Error.RateLimited.Message.v142` — `fr/firefox-ios.xliff` — auto-suggest (2026-11-02): In this Summarizer error, 'this one' means the page being summarized, so 'Impossible de résumer cette page pour l’instant' says the same thing.
- `Summarizer.Error.Unknown.Message.v142` — `fr/firefox-ios.xliff` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear
- `Summarizer.Footnote.Label.v144` — `fr/firefox-ios.xliff` — auto-suggest (2026-11-02): 'Le résumé peut contenir des erreurs' is a natural and accurate disclaimer for 'Summarization can make errors'.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `fr/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (20)

- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Onboarding.Customization.Intro.Description.v123` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `QuickAnswers.OptInRedesign.PrivateByDesignTitle.v158` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `QuickAnswers.PrivacyBanner.Title.v158` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `VPN.LocationPicker.FindingLocationsText.v160` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `VPN.Settings.DataUsage.AccessibilityLabel.v160` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Summarizer.Error.MissingPageContent.Message.v142` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `VPN.ReachedDataLimitPopup.AltPopupBody.v160` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Logins.PasscodeRequirement.Warning` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Quick-Search Engines` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Settings.WebsiteData.SelectedConfirmPrompt` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `Clear Search` — `fr/firefox-ios.xliff` — fixed 2026-11-02
- `BrowserDataTransfer.ImportSuccess.Title.v160` — `fr/firefox-ios.xliff` — fixed 2026-10-26
- `BrowserDataTransfer.ImportedBookmarksFolder.Title.v160` — `fr/firefox-ios.xliff` — fixed 2026-10-26
- `TopSites.RemovePage.Button` — `fr/firefox-ios.xliff` — fixed 2026-10-17
- `QuickAnswers.ContentView.Footer.v158` — `fr/firefox-ios.xliff` — fixed 2026-09-28
