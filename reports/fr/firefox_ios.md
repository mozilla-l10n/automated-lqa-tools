# Firefox iOS l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (45)

- `Open Last Bookmark` — `fr/firefox-ios.xliff` — The action verb "Open" is dropped, leaving only a noun phrase instead of an action label.
    - Current: `Dernier marque-page`
    - Source: `Open Last Bookmark`
    - Suggest: `Ouvrir le dernier marque-page`
    - en-US "Open Last Bookmark" describes the action of opening the last added bookmark; the French only names the bookmark and loses the verb.
- `NSMicrophoneUsageDescription` — `fr/firefox-ios.xliff` — "upload audio" is rendered as "charger des fichiers audio" (load audio files) instead of envoyer/téléverser.
    - Current: `charger des fichiers audio`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `envoyer des fichiers audio`
    - en-US "upload" means sending audio to a server; "charger" reads as loading/opening files, which is a different action.
- `Hotkeys.Forward.DiscoveryTitle` — `fr/firefox-ios.xliff` — Navigation "Forward" (page suivante dans l'historique) est traduit par « Suivant », mais le pendant de « Retour » dans la barre de navigation est « Suivant »/« Avancer » — ici le libellé doit correspondre à l'action de navigation avant.
    - Current: `Suivant`
    - Source: `Forward`
    - Suggest: `Avancer`
    - Paired with Hotkeys.Back.DiscoveryTitle ("Retour"), the source "Forward" refers to navigating forward in session history; French Firefox uses « Avancer » for this toolbar/shortcut action.
- `Logins.PasscodeRequirement.Warning` — `fr/firefox-ios.xliff` — The brand name "Firefox" from the source is dropped in the French translation.
    - Current: `Pour utiliser la fonctionnalité de remplissage automatique, vous devez avoir un code d’appareil actif.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Pour utiliser la fonctionnalité de remplissage automatique de Firefox, vous devez avoir un code d’appareil actif.`
    - The en-US reads "the AutoFill feature for Firefox"; the French omits "Firefox", losing the product reference.
- `Keyboard.Shortcuts.FindAgain` — `fr/firefox-ios.xliff` — "Find Again" is rendered as "Rechercher le suivant" which names a different action.
    - Current: `Rechercher le suivant`
    - Source: `Find Again`
    - Suggest: `Rechercher à nouveau`
    - The source is "Find Again" (repeat the last search), not "find next".
- `Quick-Search Engines` — `fr/firefox-ios.xliff` — Agreement error: "Moteurs de recherches rapides" should be "Moteurs de recherche rapides".
    - Current: `Moteurs de recherches rapides`
    - Source: `Quick-Search Engines`
    - Suggest: `Moteurs de recherche rapides`
    - In "moteur de recherche", "recherche" stays singular; the adjective "rapides" agrees with "moteurs", not with "recherches".
- `Search.SuggestSectionTitle.v102` — `fr/firefox-ios.xliff` — "Firefox Suggest" is a product/feature name and was translated as a sentence "Firefox suggère".
    - Current: `Firefox suggère`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the feature brand name "Firefox Suggest", used as a section header; it must not be rendered as the verb phrase "Firefox suggère".
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `fr/firefox-ios.xliff` — Wallpaper section title is rendered as "Écran à l’ouverture" (Opening screen) instead of a wallpaper collection title.
    - Current: `ÉCRAN À L’OUVERTURE`
    - Source: `OPENING SCREEN`
    - Suggest: `FOND D’ÉCRAN`
    - The developer comment says this is the title of the section that allows users to change the wallpaper settings; the source "OPENING SCREEN" aside, the French duplicates the Start-at-Home "Écran à l’ouverture" string and misidentifies the wallpaper section.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `fr/firefox-ios.xliff` — "some ad tracking" is rendered as "certains traqueurs publicitaires" (some ad trackers) and "websites" becomes the vague "des sites".
    - Current: `Autorise certains traqueurs publicitaires afin que des sites fonctionnent correctement.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Autorise une partie du pistage publicitaire afin que les sites web fonctionnent correctement.`
    - The source allows a certain amount of ad tracking, not a subset of trackers; "les sites web" is the correct rendering of "websites".
- `Settings.WebsiteData.SelectedConfirmPrompt` — `fr/firefox-ios.xliff` — Added "l’ensemble des" (all of) which the source does not say for selected items.
    - Current: `Cette action effacera l’ensemble des éléments sélectionnés et est irréversible.`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `Cette action effacera les éléments sélectionnés et est irréversible.`
    - en-US: "This action will clear the selected items" — no "all" quantifier, unlike the other prompt which does say "all of your website data".
- `TopSites.RemovePage.Button` — `fr/firefox-ios.xliff` — Em dash from source replaced with a hyphen, contrary to the locale's em-dash convention.
    - Current: `Supprimer la page - %@`
    - Source: `Remove page — %@`
    - Suggest: `Supprimer la page — %@`
    - The en-US uses an em dash ("Remove page — %@") and the fr house dash is the em dash; a plain hyphen is a typography deviation.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `fr/firefox-ios.xliff` — "in a few moments" translated as "plus tard" (later), changing the timing meaning.
    - Current: `Veuillez réessayer plus tard.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `Veuillez réessayer dans quelques instants.`
    - The source says to retry in a few moments, not later.
- `Clear Search` — `fr/firefox-ios.xliff` — "Clear Search" is rendered as plural "Effacer les recherches" (clear the searches) instead of clearing the current search field.
    - Current: `Effacer les recherches`
    - Source: `Clear Search`
    - Suggest: `Effacer la recherche`
    - The source refers to clearing the current search query in the search field, not deleting search history/searches.
- `Search Input Field` — `fr/firefox-ios.xliff` — Accessibility label renders "Search Input Field" as an action "Rechercher des identifiants" instead of naming the field.
    - Current: `Rechercher des identifiants`
    - Source: `Search Input Field`
    - Suggest: `Champ de recherche`
    - The en-US string names the UI element (search input field) for VoiceOver; the French says "Search for logins", which is a different, action-style label.
- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `fr/firefox-ios.xliff` — "Sunrise" is misspelled as "Levé de soleil" instead of "Lever de soleil".
    - Current: `Levé de soleil`
    - Source: `Sunrise`
    - Suggest: `Lever de soleil`
    - French for sunrise is "lever de soleil" (noun "lever"), not "levé"; also contrasts with the correctly formed "Coucher de soleil" for Sunset.
- `Settings.AppIconSelection.SectionNames.Gradients.Title.v139` — `fr/firefox-ios.xliff` — Plural section heading "Gradients" rendered as singular "Fond en dégradé", inconsistent with the other plural section headings.
    - Current: `Fond en dégradé`
    - Source: `Gradients`
    - Suggest: `Dégradés`
    - The source is the plural section name "Gradients", matching sibling headings "Basiques", "Colorées", "Autres"; the French introduces a singular "background" noun not in the source.
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `fr/firefox-ios.xliff` — The French adds "et mots de passe" (and passwords), which the source does not mention; the source only refers to credit cards.
    - Current: `Pour enregistrer et remplir automatiquement les cartes bancaires et mots de passe, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Pour enregistrer et remplir automatiquement les cartes bancaires, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source: "To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode." — no mention of passwords, and this message is shown in the Payment Methods context.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `fr/firefox-ios.xliff` — "ZIP Code" is translated with an added parenthetical "(États-Unis)" that the source does not contain.
    - Current: `Code postal (États-Unis)`
    - Source: `ZIP Code`
    - Suggest: `Code postal`
    - The en-US label is simply "ZIP Code"; adding "(États-Unis)" asserts a country restriction on the field that the source never states.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `fr/firefox-ios.xliff` — "Townland" is rendered as "Commune", which names a different administrative unit.
    - Current: `Commune`
    - Source: `Townland`
    - Suggest: `Townland`
    - A townland is a small rural land division (Ireland); "Commune" is the French municipality level and is also used for other address fields, so the label names the wrong thing.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `fr/firefox-ios.xliff` — Missing "où" in the phrase "là où vous en étiez".
    - Current: `Reprenez là vous en étiez`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Reprenez là où vous en étiez`
    - The French idiom requires "là où vous en étiez"; as written the sentence is ungrammatical.
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
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `fr/firefox-ios.xliff` — "Unselected" (state: not selected) is rendered as "Désélectionné", which means "deselected" (an action/result of removing a selection).
    - Current: `Désélectionné`
    - Source: `Unselected`
    - Suggest: `Non sélectionné`
    - The accessibility label states that the survey option was not selected; French should express the state "non sélectionné", not the action of deselecting.
- `Microsurvey.Survey.Sheet.AccessibilityLabel.v130` — `fr/firefox-ios.xliff` — "Survey" in the microsurvey context is translated as "Enquête" (investigation/inquiry) instead of the usual "Sondage".
    - Current: `Enquête`
    - Source: `Survey`
    - Suggest: `Sondage`
    - The feature is a microsurvey (questionnaire); French Firefox uses "sondage" for survey, while "enquête" suggests an investigation.
- `NativeErrorPage.BadCertDomain.HideAdvancedButton.v149` — `fr/firefox-ios.xliff` — "Hide advanced" is translated as just "Masquer", dropping the object of the action.
    - Current: `Masquer`
    - Source: `Hide advanced`
    - Suggest: `Masquer les détails avancés`
    - The source names the advanced section that will be hidden; the French only says "Hide", losing the pairing with the "Avancé" button.
- `NativeErrorPage.GenericError.Description.v134` — `fr/firefox-ios.xliff` — Present tense "can’t be created" is rendered in the past as "n’a pas pu être établie".
    - Current: `une connexion sécurisée n’a pas pu être établie`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `une connexion sécurisée ne peut pas être établie`
    - The en-US states an ongoing impossibility ("a secure connection can’t be created"), not a past failed attempt.
- `NativeErrorPage.BadCertDomain.Description.v149` — `fr/firefox-ios.xliff` — "could also be set up incorrectly" (possibility) is rendered with the indicative "peuvent également être mal configurés", asserting it more strongly than the source.
    - Current: `Vos paramètres de connexion peuvent également être mal configurés.`
    - Source: `Someone pretending to be the site could try to steal your personal info. Your connection settings could also be set up incorrectly.`
    - Suggest: `Vos paramètres de connexion pourraient également être mal configurés.`
    - The source uses the conditional "could", matching the preceding "pourrait"; the indicative weakens the hypothetical framing.
- `NativeErrorPage.CellularDataRestricted.Description.v156` — `fr/firefox-ios.xliff` — "go to iOS Settings and turn on cellular data for %@" is rephrased as "ouvrez les réglages d’iOS pour autoriser %@ à utiliser les données cellulaires", changing the instruction from turning on a setting to granting permission.
    - Current: `ouvrez les réglages d’iOS pour autoriser %@ à utiliser les données cellulaires`
    - Source: `Connect to Wi-Fi or go to iOS Settings and turn on cellular data for %@.`
    - Suggest: `ouvrez les réglages d’iOS et activez les données cellulaires pour %@`
    - The source gives two explicit steps (go to Settings, turn on cellular data for the app); the French merges them into a purpose clause and loses the "activez" instruction.
- `Onboarding.Customization.Intro.Description.v123` — `fr/firefox-ios.xliff` — Ungrammatical phrase: "à votre propre façon de naviguer" lacks the verb of adaptation present in the source ("to match").
    - Current: `Configurez le thème et la barre d’outils à votre propre façon de naviguer.`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `Configurez le thème et la barre d’outils pour les adapter à votre propre façon de naviguer.`
    - The source says to set the theme and toolbar so they match your unique browsing style; "Configurez … à votre façon de naviguer" is not idiomatic French and the verb-preposition pairing is incorrect.
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
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `fr/firefox-ios.xliff` — Agreement error: "limité" should agree with the feminine noun "édition".
    - Current: `Fond d’écran en édition limité`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Fond d’écran en édition limitée`
    - "édition" is feminine, so the adjective must be "limitée" (Limited Edition Wallpaper).
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `fr/firefox-ios.xliff` — The French reverses the roles: it says "allow opening Firefox" instead of "allow Firefox to open" (the scanned URL).
    - Current: `Autoriser l’ouverture de %@ ?`
    - Source: `Allow %@ to open?`
    - Suggest: `Autoriser %@ à ouvrir cette adresse ?`
    - Source "Allow %@ to open?" asks permission for the app (%@ = Firefox) to open the scanned URL; the French makes Firefox the object being opened.
- `PasswordGenerator.Description.v132` — `fr/firefox-ios.xliff` — "strong password" rendered as "mot de passe compliqué" instead of the established "mot de passe robuste/fort".
    - Current: `un mot de passe compliqué, généré aléatoirement`
    - Source: `Protect your account by using a strong, randomly generated password.`
    - Suggest: `un mot de passe robuste, généré aléatoirement`
    - "compliqué" means complicated, not strong; Firefox fr uses "robuste"/"fort" for strong passwords.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `fr/firefox-ios.xliff` — "Firefox Suggest" is rendered as "Firefox Suggest" here but as "Firefox suggère" in the neighbouring strings on the same settings screen.
    - Current: `Afficher les suggestions de Firefox Suggest dans les sessions privées`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Afficher les suggestions de Firefox suggère dans les sessions privées`
    - Settings.Search.Suggest.AddressBarSetting.Title.v124, Settings.Search.Suggest.LearnAboutSuggestions.v124 and Settings.Search.Accessibility.LearnAboutSuggestions.v124 all use "Firefox suggère" for the same product name on the same screen; one of the two renderings is inconsistent.
- `Settings.Search.GoogleLens.Footnote.v153` — `fr/firefox-ios.xliff` — "your active search engine" is translated as "moteur de recherche principal" (main/primary), changing the meaning.
    - Current: `défini comme moteur de recherche principal lors de la navigation`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `défini comme moteur de recherche actif lors de la navigation`
    - The source says the engine must be the active one while browsing, not the "main" one; French "principal" is also confusable with "par défaut" used elsewhere on this screen.
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `fr/firefox-ios.xliff` — The French adds "des conseils" (tips), which is not in the source "Learn about useful features and how to get the most out of %@."
    - Current: `Découvrez des fonctionnalités utiles et des conseils pour tirer le meilleur parti de %@.`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `Découvrez des fonctionnalités utiles et comment tirer le meilleur parti de %@.`
    - The source describes learning about features and how to get the most out of the app; "et des conseils" introduces content the source does not state.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `fr/firefox-ios.xliff` — Missing preposition: "des suggestions %@" should be "des suggestions de %@" (get suggestions from Firefox).
    - Current: `Obtenir des suggestions %@ en rapport avec votre recherche`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `Obtenir des suggestions de %@ en rapport avec votre recherche`
    - Source is "Get suggestions from %@"; the French drops the "from" preposition, leaving an ungrammatical noun juxtaposition.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `fr/firefox-ios.xliff` — "la barre d’adresse et d’onglets" incorrectly merges two separate bars (tab bar and address bar) into one.
    - Current: `Faire défiler pour masquer la barre d’adresse et d’onglets`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Faire défiler pour masquer la barre d’onglets et la barre d’adresse`
    - The source refers to the tab bar and the address bar as two distinct UI elements that are hidden on scroll.
- `Settings.Translation.AutoTranslate.Footer.v151` — `fr/firefox-ios.xliff` — "your top preferred language" is rendered as "la langue de votre choix", losing the notion of the highest-ranked preferred language.
    - Current: `Traduit automatiquement les pages dans la langue de votre choix.`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `Traduit automatiquement les pages dans votre première langue préférée.`
    - The source refers to the top entry of the Preferred Languages list, not simply any language the user chooses; the section is named « Langues préférées » in the same screen.
- `Summarizer.Error.MissingPageContent.Message.v142` — `fr/firefox-ios.xliff` — "hit summarize" is rendered as « cliquez » (click) on a touch device, and the source says nothing about clicking.
    - Current: `puis cliquez sur « Résumer »`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `puis appuyez sur « Résumer »`
    - Firefox iOS is a touch phone app; other strings in this batch use « Appuyez ». The source says "hit summarize".
- `Summarizer.Error.RateLimited.Message.v142` — `fr/firefox-ios.xliff` — The generic "Can’t handle this one at the moment" is narrowed to an explicit statement that summarizing this page is impossible.
    - Current: `Impossible de résumer cette page pour l’instant.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Impossible de traiter cette demande pour l’instant.`
    - The source is a rate-limit message about not handling the request right now, not a claim that the page cannot be summarized.
- `Summarizer.Error.Unknown.Message.v142` — `fr/firefox-ios.xliff` — "summarizing" is translated as « synthèse » here while every other string in the same feature uses « résumé ».
    - Current: `Erreur lors de la synthèse de la page.`
    - Source: `Error summarizing page. Try again later.`
    - Suggest: `Erreur lors du résumé de la page.`
    - Terminology inconsistency within the Summarizer screen, where "summary/summarize" is consistently rendered with « résumé »/« résumer ».
- `Summarizer.Footnote.Label.v144` — `fr/firefox-ios.xliff` — "Summarization can make errors" is rendered as the summary containing errors rather than the feature making mistakes.
    - Current: `le résumé peut contenir des erreurs`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `la synthèse automatique peut faire des erreurs`
    - The source disclaims the summarization process, not the specific output; the French wording asserts something slightly different about the product's output.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (45)

- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — "Levé de soleil" is a misspelling of "Lever de soleil" (sunrise).
    - Current: `Levé de soleil`
    - Suggest: `Lever de soleil`
    - The French noun for sunrise is "lever de soleil"; "levé" is a past participle and is incorrect here.
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `Shared/Supporting Files/en.lproj/Credentials.strings` — The French adds "et mots de passe" (and passwords), which is not in the source about credit cards only.
    - Current: `Pour enregistrer et remplir automatiquement les cartes bancaires et mots de passe, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Suggest: `Pour enregistrer et remplir automatiquement les cartes bancaires, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source says "To save and autofill credit cards"; this message is shown when entering Payment Methods, not passwords.
- `Addresses.EditAddress.AutofillAddressOrganization.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Organization" is rendered as "Entreprise" (company), narrowing the meaning.
    - Current: `Entreprise`
    - Suggest: `Organisation`
    - The source field is generic ("the organization's name related to the address"), covering non-business organizations; "Entreprise" means specifically a business.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Townland" (a rural land division, chiefly Irish) is translated as "Commune", which designates a municipality, a different administrative unit.
    - Current: `Commune`
    - Suggest: `Townland (division rurale)`
    - The developer comment specifies "a specific type of land division used in rural areas"; "Commune" is the French term for a municipality/township, which conflicts with the separate Village/Township field and misnames the concept.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "ZIP Code" translated with an added qualifier "(États-Unis)" not present in the source, and identical wording to the Postal Code field.
    - Current: `Code postal (États-Unis)`
    - Suggest: `Code ZIP`
    - The source is simply "ZIP Code"; the added parenthetical is extra content, and duplicating "Code postal" collides with the separate Postal Code label.
- `CloseTab.ArrivingNotification.title.v133` — `Shared/Supporting Files/en.lproj/FxANotification.strings` — The app name placeholder is placed after "Onglets", turning "%1$@ tabs closed" into "Tabs %1$@ closed".
    - Current: `Onglets %1$@ fermés : %2$@`
    - Suggest: `Onglets fermés dans %1$@ : %2$@`
    - %1$@ is the app name (e.g. Firefox) qualifying "tabs"; "Onglets Firefox fermés" reads as if Firefox were an adjective placed oddly and the meaning "Firefox tabs closed" is garbled in French word order.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `Shared/Supporting Files/en.lproj/JumpBackIn.strings` — Missing "où" in the phrase "reprenez là où vous en étiez".
    - Current: `Reprenez là vous en étiez`
    - Suggest: `Reprenez là où vous en étiez`
    - The French idiom for "pick up where you left off" is "reprenez là où vous en étiez"; the relative pronoun "où" is missing, leaving an ungrammatical sentence.
- `LibraryPanel.Section.Older` — `Shared/Supporting Files/en.lproj/LibraryPanel.strings` — "Older" (items older than thirty days) is rendered as "Avant le mois dernier" (before last month).
    - Current: `Avant le mois dernier`
    - Suggest: `Plus ancien`
    - The source and developer comment say the section groups items older than thirty days; "Avant le mois dernier" states a different time frame (before last month).
- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Desktop site" is rendered as "version classique" here but as "version pour ordinateur"/"Version ordinateur" in the sibling strings on the same menu.
    - Current: `Passer en version classique`
    - Suggest: `Passer en version pour ordinateur`
    - MainMenu.ToolsSection.AccessibilityLabels.SwitchToDesktopSite.v132 uses "Passer en version pour ordinateur" and MainMenu.ToolsSection.DesktopSite.Title.v141 uses "Version ordinateur" for the same concept on the same screen; "classique" is inconsistent.
- `MainMenu.ToolsSection.Translation.Translated.Title.v151` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Translated…" is rendered as "Page traduite…", adding a noun not present in the source and diverging from the v145 variant "Traduit".
    - Current: `Page traduite…`
    - Suggest: `Traduit…`
    - The source is just "Translated…"; the parallel string MainMenu.ToolsSection.Translation.Translated.Title.v145 is translated as "Traduit".
- `NativeErrorPage.CellularDataRestricted.TitleLabel.v156` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — "turned off for %@" mistranslated as "désactivées pendant %@" (during), changing meaning.
    - Current: `Les données mobiles sont désactivées pendant %@.`
    - Suggest: `Les données mobiles sont désactivées pour %@.`
    - The placeholder is the app name; the source says cellular data is off *for* the app, not "during" it. The companion description string correctly uses « pour %@ ».
- `NativeErrorPage.GenericError.Description.v134` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Present tense "can't be created" rendered as past tense "n'a pas pu être établie".
    - Current: `une connexion sécurisée n’a pas pu être établie`
    - Suggest: `une connexion sécurisée ne peut pas être établie`
    - The en-US source says "a secure connection can’t be created" (present), not "could not be established".
- `DefaultBrowserPopup.SecondLabel.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Default Browser App" is rendered as "App du navigateur par défaut", which does not match the iOS French setting label "Application par défaut du navigateur".
    - Current: `2. Appuyez sur *App du navigateur par défaut*`
    - Suggest: `2. Appuyez sur *Application par défaut du navigateur*`
    - The string quotes an actual iOS Settings item; the French system wording is "Application par défaut du navigateur", and "App du navigateur par défaut" also mistakenly makes "par défaut" modify "navigateur".
- `Onboarding.Customization.Intro.Description.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Ungrammatical construction "à votre propre façon de naviguer" after "Configurez".
    - Current: `Configurez le thème et la barre d’outils à votre propre façon de naviguer.`
    - Suggest: `Adaptez le thème et la barre d’outils à votre propre façon de naviguer.`
    - "Configurez … à …" is not valid French; the source means setting theme and toolbar to match one's browsing style, which requires a verb like "adapter".
- `Onboarding.Modern.BrandRefresh.Sync.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "stays safe and secure with encryption" loses "safe and secure" nuance but mainly the translation drops nothing critical; however "Grab bookmarks, passwords, and more" is fine — issue is omission of "safe and secure".
    - Current: `Vos données personnelles sont protégées grâce au chiffrement.`
    - Suggest: `Vos données personnelles restent en sécurité grâce au chiffrement.`
    - Minor omission of "stays"; acceptable rendering.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "won't sell you out" (won't betray/sell your data) is rendered as "digne de confiance" (trustworthy), losing the source meaning.
    - Current: `Rapide, sûr et digne de confiance.`
    - Suggest: `Rapide, sûr et qui ne vous trahit pas.`
    - The en-US phrase means the browser will not betray the user / sell their data; "digne de confiance" is a generic, weaker claim that does not convey it.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The en dash separator in the source is rendered as an em dash without matching French spacing convention.
    - Current: `des moteurs de recherche — le tout`
    - Suggest: `des moteurs de recherche – le tout`
    - The source uses an en dash (–); the translation substitutes an em dash, deviating from the source typography.
- `Onboarding.Modern.Sync.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "sync on any device" rendered as "sur tous vos appareils" (on all your devices) instead of "sur n'importe quel appareil".
    - Current: `sont synchronisés sur tous vos appareils`
    - Suggest: `sont synchronisés sur n’importe quel appareil`
    - The en-US says "on any device"; the v140 sibling string correctly uses "n’importe quel appareil". "tous vos appareils" changes the meaning.
- `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Brought to you by" translated as "Conçu par" (designed by), altering the meaning.
    - Current: `Conçu par l’organisation à but non lucratif %@`
    - Suggest: `Proposé par l’organisation à but non lucratif %@`
    - "Brought to you by" means offered/provided by, not designed by.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Agreement error: "limité" must agree with the feminine noun "édition".
    - Current: `Fond d’écran en édition limité`
    - Suggest: `Fond d’écran en édition limitée`
    - "édition" is feminine, so the adjective must be "limitée" (Limited Edition Wallpaper).
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `Shared/Supporting Files/en.lproj/ScanQRCode.strings` — The translation says "allow opening of <app>" instead of allowing the app to open the URL.
    - Current: `Autoriser l’ouverture de %@ ?`
    - Suggest: `Autoriser %@ à ouvrir ce lien ?`
    - Per the developer comment, %@ is the app name; the source asks permission for the app to open the scanned URL, not permission to open the app itself.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Tab and Address Bar" is rendered as "la barre d’adresse et d’onglets", turning two bars into one and losing the tab bar.
    - Current: `masquer la barre d’adresse et d’onglets`
    - Suggest: `masquer la barre d’onglets et la barre d’adresse`
    - The source refers to hiding both the tab bar and the address bar; the French merges them into a single "barre d’adresse et d’onglets".
- `Settings.Search.Accessibility.LearnAboutSuggestions.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `En savoir plus sur Firefox suggère`
    - Suggest: `En savoir plus sur Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must remain untranslated; it is kept in English elsewhere in the same file.
- `Settings.Search.GoogleLens.Footnote.v153` — `Shared/Supporting Files/en.lproj/Settings.strings` — "your active search engine" is translated as "moteur de recherche principal" (main/default) instead of active.
    - Current: `défini comme moteur de recherche principal`
    - Suggest: `défini comme votre moteur de recherche actif`
    - The source says "is your active search engine while browsing", not the main/primary one.
- `Settings.Search.Suggest.AddressBarSetting.Title.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `Barre d’adresse - Firefox suggère`
    - Suggest: `Barre d’adresse - Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must stay untranslated; the same file renders it correctly as "Firefox Suggest" in Settings.Search.Suggest.PrivateSession.Description.v125.
- `Settings.Search.Suggest.LearnAboutSuggestions.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `En savoir plus sur Firefox suggère`
    - Suggest: `En savoir plus sur Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must remain untranslated; it is kept in English elsewhere in the same file.
- `Settings.Search.Suggest.SearchSyncedTabs.Title.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — The toggle title "Search Synced Tabs" is rendered as an instruction to search within synced tabs rather than the setting name.
    - Current: `Rechercher dans les onglets synchronisés`
    - Suggest: `Rechercher les onglets synchronisés`
    - The setting enables searching synced tabs; the French adds "dans" which changes it to "search inside the synced tabs". Other setting titles in this screen are noun/verb labels matching the source.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `Shared/Supporting Files/en.lproj/Settings.strings` — Missing preposition: "suggestions %@" should be "suggestions de %@" to render "suggestions from Firefox".
    - Current: `Obtenir des suggestions %@ en rapport avec votre recherche`
    - Suggest: `Obtenir des suggestions de %@ en rapport avec votre recherche`
    - The source is "Get suggestions from %@ related to your search"; without "de", the app name is juxtaposed ungrammatically to "suggestions".
- `Settings.Translation.AutoTranslate.Footer.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "your top preferred language" is rendered as "la langue de votre choix", losing the meaning of the highest-ranked preferred language.
    - Current: `Traduit automatiquement les pages dans la langue de votre choix.`
    - Suggest: `Traduit automatiquement les pages dans votre langue préférée principale.`
    - The source refers to the top entry of the Preferred Languages list, not any language the user picks each time.
- `Summarizer.Error.MissingPageContent.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "hit summarize" on a touch device is rendered as "cliquez" (click) instead of a tap action.
    - Current: `puis cliquez sur « Résumer »`
    - Suggest: `puis appuyez sur « Résumer »`
    - This is an iOS touch interface; elsewhere in the same feature the French uses « Appuyez » for tap (e.g. ContextualHints.Summarize.Description). "cliquez" refers to a mouse click and is inconsistent terminology.
- `Summarizer.Error.Unknown.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "summarizing" is translated as « synthèse » while every other string in the same file uses « résumé ».
    - Current: `Erreur lors de la synthèse de la page.`
    - Suggest: `Erreur lors du résumé de la page.`
    - Terminology inconsistency within the same screen: the feature is consistently called « résumé »/« résumer » in the other Summarizer strings.
- `Offline Website Data` — `Shared/en.lproj/ClearPrivateData.strings` — "Offline Website Data" is rendered as "Données hors connexion", dropping "Website".
    - Current: `Données hors connexion`
    - Suggest: `Données de sites web hors connexion`
    - The source refers specifically to website data stored for offline use; the French omits "des sites web", making the settings item vaguer than the source.
- `LibraryPanel.Section.Older` — `Shared/en.lproj/Localizable.strings` — "Older" (items older than thirty days) is rendered as "Avant le mois dernier" (before last month), which states a different time boundary.
    - Current: `Avant le mois dernier`
    - Suggest: `Plus anciens`
    - The source label is simply "Older", meaning items older than thirty days; "Avant le mois dernier" means "before last month" and misstates the section's scope.
- `Logins.PasscodeRequirement.Warning` — `Shared/en.lproj/Localizable.strings` — The brand reference "for Firefox" is dropped from the translation.
    - Current: `Pour utiliser la fonctionnalité de remplissage automatique, vous devez avoir un code d’appareil actif.`
    - Suggest: `Pour utiliser la fonctionnalité de remplissage automatique de Firefox, vous devez avoir un code d’appareil actif.`
    - The en-US source says "the AutoFill feature for Firefox"; the French omits Firefox entirely.
- `Quick-Search Engines` — `Shared/en.lproj/Localizable.strings` — Incorrect plural agreement in "Moteurs de recherches rapides".
    - Current: `Moteurs de recherches rapides`
    - Suggest: `Moteurs de recherche rapides`
    - In French, "moteur de recherche" keeps "recherche" in the singular; the adjective "rapides" agrees with "moteurs".
- `Search.SuggestSectionTitle.v102` — `Shared/en.lproj/Localizable.strings` — "Firefox Suggest" is a product/feature name and must not be translated as a verb phrase.
    - Current: `Firefox suggère`
    - Suggest: `Firefox Suggest`
    - The source is the brand feature name "Firefox Suggest"; rendering it as "Firefox suggère" turns the name into a sentence and loses the brand.
- `Search.ThirdPartyEngines.FailedMessage` — `Shared/en.lproj/Localizable.strings` — Past-tense failure message rendered as present/future impossibility.
    - Current: `Le moteur de recherche ne peut pas être ajouté.`
    - Suggest: `Le moteur de recherche n’a pas pu être ajouté.`
    - Source "The search provider could not be added." reports a failure that already occurred, not a general inability.
- `Search.ThirdPartyEngines.FormErrorTitle` — `Shared/en.lproj/Localizable.strings` — "Failed" translated as "Erreur" here while the identical source string is "Échec" in the sibling strings on the same screen.
    - Current: `Erreur`
    - Suggest: `Échec`
    - Search.ThirdPartyEngines.DuplicateErrorTitle and FailedTitle use "Échec" for the same source "Failed"; inconsistent within the same feature.
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `Shared/en.lproj/Localizable.strings` — Wallpaper collection section title is translated as "Écran à l'ouverture" (Opening screen) instead of a wallpaper-related title.
    - Current: `ÉCRAN À L’OUVERTURE`
    - Suggest: `COLLECTION`
    - The developer comment says this is the title of the wallpaper settings section; the French reuses the unrelated Start-at-Home "Opening screen" wording, which describes a different feature. (Source string itself is odd, but the French duplicates a different screen's label.)
- `Settings.TrackingProtection.Info.BlocksTitle` — `Shared/en.lproj/Localizable.strings` — "BLOCKS" is a plural noun heading (list of blocked items), rendered as a verb form "BLOQUE".
    - Current: `BLOQUE`
    - Suggest: `BLOQUÉS`
    - The comment says it is the title on an info view showing a list of all blocked websites, so the source is the plural noun/participle, not the third-person verb.
- `TopSites.RemovePage.Button` — `Shared/en.lproj/Localizable.strings` — Em dash from the source replaced by a hyphen.
    - Current: `Supprimer la page - %@`
    - Suggest: `Supprimer la page — %@`
    - The en-US source uses an em dash (—) as separator; French typography also uses the em/en dash here, not a plain hyphen.
- `Are you sure?` — `Shared/en.lproj/LoginManager.strings` — The prompt title "Are you sure?" is rendered as "Poursuivre la suppression ?" instead of an equivalent of the source.
    - Current: `Poursuivre la suppression ?`
    - Suggest: `Voulez-vous vraiment continuer ?`
    - The en-US source is a generic confirmation question "Are you sure?"; the French states "Continue with the deletion?", which is different content.
- `Clear Search` — `Shared/en.lproj/LoginManager.strings` — "Clear Search" (singular action of clearing the search) is translated as a plural "Effacer les recherches".
    - Current: `Effacer les recherches`
    - Suggest: `Effacer la recherche`
    - The developer comment says the button clears the search and exits search mode, not deletes multiple searches.
- `Search Input Field` — `Shared/en.lproj/LoginManager.strings` — Accessibility label "Search Input Field" is translated as "Rechercher des identifiants" (Search logins).
    - Current: `Rechercher des identifiants`
    - Suggest: `Champ de saisie de recherche`
    - The source names the UI element (search input field); the French turns it into an action label with different content.
- `Mobile Bookmarks` — `Shared/en.lproj/Storage.strings` — Adjective agreement error: "mobile" must agree with the plural noun "Marque-pages".
    - Current: `Marque-pages mobile`
    - Suggest: `Marque-pages mobiles`
    - "Marque-pages" is plural, so the qualifying adjective should be "mobiles".

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,922 |
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
| apostrophe | `typographic` 359 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3, `en` 1 | **em** |
| nbsp | `total` 154, `before-punctuation` 96 | _mixed_ |
| register | `formal` 285 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (45)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Addresses.EditAddress.AutofillAddressZip.v129` — `fr/firefox-ios.xliff` — "ZIP Code" is translated with an added parenthetical "(États-Unis)" that the source does not contain.
    - Current: `Code postal (États-Unis)`
    - Source: `ZIP Code`
    - Suggest: `Code postal`
    - The en-US label is simply "ZIP Code"; adding "(États-Unis)" asserts a country restriction on the field that the source never states.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 30 |
| 3 | Degraded language (grammar, spelling, terminology) | 14 |
| 4 | Cosmetic (typography, spacing) | 1 |

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
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `fr/firefox-ios.xliff` — The French adds "et mots de passe" (and passwords), which the source does not mention; the source only refers to credit cards.
    - Current: `Pour enregistrer et remplir automatiquement les cartes bancaires et mots de passe, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Pour enregistrer et remplir automatiquement les cartes bancaires, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source: "To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode." — no mention of passwords, and this message is shown in the Payment Methods context.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `fr/firefox-ios.xliff` — "Townland" is rendered as "Commune", which names a different administrative unit.
    - Current: `Commune`
    - Source: `Townland`
    - Suggest: `Townland`
    - A townland is a small rural land division (Ireland); "Commune" is the French municipality level and is also used for other address fields, so the label names the wrong thing.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `fr/firefox-ios.xliff` — "ZIP Code" is translated with an added parenthetical "(États-Unis)" that the source does not contain.
    - Current: `Code postal (États-Unis)`
    - Source: `ZIP Code`
    - Suggest: `Code postal`
    - The en-US label is simply "ZIP Code"; adding "(États-Unis)" asserts a country restriction on the field that the source never states.
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
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `fr/firefox-ios.xliff` — "Unselected" (state: not selected) is rendered as "Désélectionné", which means "deselected" (an action/result of removing a selection).
    - Current: `Désélectionné`
    - Source: `Unselected`
    - Suggest: `Non sélectionné`
    - The accessibility label states that the survey option was not selected; French should express the state "non sélectionné", not the action of deselecting.
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
- `Summarizer.Error.MissingPageContent.Message.v142` — `fr/firefox-ios.xliff` — "hit summarize" is rendered as « cliquez » (click) on a touch device, and the source says nothing about clicking.
    - Current: `puis cliquez sur « Résumer »`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `puis appuyez sur « Résumer »`
    - Firefox iOS is a touch phone app; other strings in this batch use « Appuyez ». The source says "hit summarize".
- `Summarizer.Error.RateLimited.Message.v142` — `fr/firefox-ios.xliff` — The generic "Can’t handle this one at the moment" is narrowed to an explicit statement that summarizing this page is impossible.
    - Current: `Impossible de résumer cette page pour l’instant.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Impossible de traiter cette demande pour l’instant.`
    - The source is a rate-limit message about not handling the request right now, not a claim that the page cannot be summarized.
- `Summarizer.Footnote.Label.v144` — `fr/firefox-ios.xliff` — "Summarization can make errors" is rendered as the summary containing errors rather than the feature making mistakes.
    - Current: `le résumé peut contenir des erreurs`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `la synthèse automatique peut faire des erreurs`
    - The source disclaims the summarization process, not the specific output; the French wording asserts something slightly different about the product's output.
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
- `Keyboard.Shortcuts.FindAgain` — `fr/firefox-ios.xliff` — "Find Again" is rendered as "Rechercher le suivant" which names a different action.
    - Current: `Rechercher le suivant`
    - Source: `Find Again`
    - Suggest: `Rechercher à nouveau`
    - The source is "Find Again" (repeat the last search), not "find next".
- `Logins.PasscodeRequirement.Warning` — `fr/firefox-ios.xliff` — The brand name "Firefox" from the source is dropped in the French translation.
    - Current: `Pour utiliser la fonctionnalité de remplissage automatique, vous devez avoir un code d’appareil actif.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Pour utiliser la fonctionnalité de remplissage automatique de Firefox, vous devez avoir un code d’appareil actif.`
    - The en-US reads "the AutoFill feature for Firefox"; the French omits "Firefox", losing the product reference.
- `Search.SuggestSectionTitle.v102` — `fr/firefox-ios.xliff` — "Firefox Suggest" is a product/feature name and was translated as a sentence "Firefox suggère".
    - Current: `Firefox suggère`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the feature brand name "Firefox Suggest", used as a section header; it must not be rendered as the verb phrase "Firefox suggère".
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `fr/firefox-ios.xliff` — Wallpaper section title is rendered as "Écran à l’ouverture" (Opening screen) instead of a wallpaper collection title.
    - Current: `ÉCRAN À L’OUVERTURE`
    - Source: `OPENING SCREEN`
    - Suggest: `FOND D’ÉCRAN`
    - The developer comment says this is the title of the section that allows users to change the wallpaper settings; the source "OPENING SCREEN" aside, the French duplicates the Start-at-Home "Écran à l’ouverture" string and misidentifies the wallpaper section.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `fr/firefox-ios.xliff` — "some ad tracking" is rendered as "certains traqueurs publicitaires" (some ad trackers) and "websites" becomes the vague "des sites".
    - Current: `Autorise certains traqueurs publicitaires afin que des sites fonctionnent correctement.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Autorise une partie du pistage publicitaire afin que les sites web fonctionnent correctement.`
    - The source allows a certain amount of ad tracking, not a subset of trackers; "les sites web" is the correct rendering of "websites".
- `Settings.WebsiteData.SelectedConfirmPrompt` — `fr/firefox-ios.xliff` — Added "l’ensemble des" (all of) which the source does not say for selected items.
    - Current: `Cette action effacera l’ensemble des éléments sélectionnés et est irréversible.`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `Cette action effacera les éléments sélectionnés et est irréversible.`
    - en-US: "This action will clear the selected items" — no "all" quantifier, unlike the other prompt which does say "all of your website data".
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `fr/firefox-ios.xliff` — "in a few moments" translated as "plus tard" (later), changing the timing meaning.
    - Current: `Veuillez réessayer plus tard.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `Veuillez réessayer dans quelques instants.`
    - The source says to retry in a few moments, not later.
- `Clear Search` — `fr/firefox-ios.xliff` — "Clear Search" is rendered as plural "Effacer les recherches" (clear the searches) instead of clearing the current search field.
    - Current: `Effacer les recherches`
    - Source: `Clear Search`
    - Suggest: `Effacer la recherche`
    - The source refers to clearing the current search query in the search field, not deleting search history/searches.
- `Search Input Field` — `fr/firefox-ios.xliff` — Accessibility label renders "Search Input Field" as an action "Rechercher des identifiants" instead of naming the field.
    - Current: `Rechercher des identifiants`
    - Source: `Search Input Field`
    - Suggest: `Champ de recherche`
    - The en-US string names the UI element (search input field) for VoiceOver; the French says "Search for logins", which is a different, action-style label.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `fr/firefox-ios.xliff` — "Sunrise" is misspelled as "Levé de soleil" instead of "Lever de soleil".
    - Current: `Levé de soleil`
    - Source: `Sunrise`
    - Suggest: `Lever de soleil`
    - French for sunrise is "lever de soleil" (noun "lever"), not "levé"; also contrasts with the correctly formed "Coucher de soleil" for Sunset.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `fr/firefox-ios.xliff` — Missing "où" in the phrase "là où vous en étiez".
    - Current: `Reprenez là vous en étiez`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Reprenez là où vous en étiez`
    - The French idiom requires "là où vous en étiez"; as written the sentence is ungrammatical.
- `Onboarding.Customization.Intro.Description.v123` — `fr/firefox-ios.xliff` — Ungrammatical phrase: "à votre propre façon de naviguer" lacks the verb of adaptation present in the source ("to match").
    - Current: `Configurez le thème et la barre d’outils à votre propre façon de naviguer.`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `Configurez le thème et la barre d’outils pour les adapter à votre propre façon de naviguer.`
    - The source says to set the theme and toolbar so they match your unique browsing style; "Configurez … à votre façon de naviguer" is not idiomatic French and the verb-preposition pairing is incorrect.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `fr/firefox-ios.xliff` — Agreement error: "limité" should agree with the feminine noun "édition".
    - Current: `Fond d’écran en édition limité`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Fond d’écran en édition limitée`
    - "édition" is feminine, so the adjective must be "limitée" (Limited Edition Wallpaper).
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
- `Quick-Search Engines` — `fr/firefox-ios.xliff` — Agreement error: "Moteurs de recherches rapides" should be "Moteurs de recherche rapides".
    - Current: `Moteurs de recherches rapides`
    - Source: `Quick-Search Engines`
    - Suggest: `Moteurs de recherche rapides`
    - In "moteur de recherche", "recherche" stays singular; the adjective "rapides" agrees with "moteurs", not with "recherches".

### D. Terminology, register & consistency

- `Microsurvey.Survey.Sheet.AccessibilityLabel.v130` — `fr/firefox-ios.xliff` — "Survey" in the microsurvey context is translated as "Enquête" (investigation/inquiry) instead of the usual "Sondage".
    - Current: `Enquête`
    - Source: `Survey`
    - Suggest: `Sondage`
    - The feature is a microsurvey (questionnaire); French Firefox uses "sondage" for survey, while "enquête" suggests an investigation.
- `PasswordGenerator.Description.v132` — `fr/firefox-ios.xliff` — "strong password" rendered as "mot de passe compliqué" instead of the established "mot de passe robuste/fort".
    - Current: `un mot de passe compliqué, généré aléatoirement`
    - Source: `Protect your account by using a strong, randomly generated password.`
    - Suggest: `un mot de passe robuste, généré aléatoirement`
    - "compliqué" means complicated, not strong; Firefox fr uses "robuste"/"fort" for strong passwords.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `fr/firefox-ios.xliff` — "Firefox Suggest" is rendered as "Firefox Suggest" here but as "Firefox suggère" in the neighbouring strings on the same settings screen.
    - Current: `Afficher les suggestions de Firefox Suggest dans les sessions privées`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Afficher les suggestions de Firefox suggère dans les sessions privées`
    - Settings.Search.Suggest.AddressBarSetting.Title.v124, Settings.Search.Suggest.LearnAboutSuggestions.v124 and Settings.Search.Accessibility.LearnAboutSuggestions.v124 all use "Firefox suggère" for the same product name on the same screen; one of the two renderings is inconsistent.
- `Summarizer.Error.Unknown.Message.v142` — `fr/firefox-ios.xliff` — "summarizing" is translated as « synthèse » here while every other string in the same feature uses « résumé ».
    - Current: `Erreur lors de la synthèse de la page.`
    - Source: `Error summarizing page. Try again later.`
    - Suggest: `Erreur lors du résumé de la page.`
    - Terminology inconsistency within the Summarizer screen, where "summary/summarize" is consistently rendered with « résumé »/« résumer ».

### E. Typography, punctuation & spacing

- `TopSites.RemovePage.Button` — `fr/firefox-ios.xliff` — Em dash from source replaced with a hyphen, contrary to the locale's em-dash convention.
    - Current: `Supprimer la page - %@`
    - Source: `Remove page — %@`
    - Suggest: `Supprimer la page — %@`
    - The en-US uses an em dash ("Remove page — %@") and the fr house dash is the em dash; a plain hyphen is a typography deviation.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
