# Firefox iOS l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 1,918 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (1)

- `WebCompatReporter.Fields.ChooseIssueTypeAccessibilityHint.v156` — `fr/firefox-ios.xliff` — "issue type" rendered as "type de ticket", inconsistent with "type de problème" used for the same term in the sibling string.
    - Current: `Choisir d’abord un type de ticket`
    - Source: `Choose an issue type first`
    - Suggest: `Choisir d’abord un type de problème`
    - The en-US "issue type" is translated "type de problème" in WebCompatReporter.Fields.ChooseSubOptionAccessibilityHint.v156 on the same form; "ticket" introduces a support-ticket concept absent from the source.

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
| Files | 96 |
| Strings | 1,918 |
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
| apostrophe | `typographic` 358 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3, `en` 1 | **em** |
| nbsp | `total` 152, `before-punctuation` 94 | _mixed_ |
| register | `formal` 285 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (45)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 29 |
| 3 | Degraded language (grammar, spelling, terminology) | 14 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `fr/firefox-ios.xliff` — The French adds "et mots de passe" (and passwords), which is not in the source about credit cards only.
    - Current: `Pour enregistrer et remplir automatiquement les cartes bancaires et mots de passe, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Pour enregistrer et remplir automatiquement les cartes bancaires, activez Face ID, Touch ID ou un code pour l’appareil.`
    - Source says "To save and autofill credit cards"; this message is shown when entering Payment Methods, not passwords.
- `Addresses.EditAddress.AutofillAddressOrganization.v129` — `fr/firefox-ios.xliff` — "Organization" is rendered as "Entreprise" (company), narrowing the meaning.
    - Current: `Entreprise`
    - Source: `Organization`
    - Suggest: `Organisation`
    - The source field is generic ("the organization's name related to the address"), covering non-business organizations; "Entreprise" means specifically a business.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `fr/firefox-ios.xliff` — "Townland" (a rural land division, chiefly Irish) is translated as "Commune", which designates a municipality, a different administrative unit.
    - Current: `Commune`
    - Source: `Townland`
    - Suggest: `Townland (division rurale)`
    - The developer comment specifies "a specific type of land division used in rural areas"; "Commune" is the French term for a municipality/township, which conflicts with the separate Village/Township field and misnames the concept.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `fr/firefox-ios.xliff` — "ZIP Code" translated with an added qualifier "(États-Unis)" not present in the source, and identical wording to the Postal Code field.
    - Current: `Code postal (États-Unis)`
    - Source: `ZIP Code`
    - Suggest: `Code ZIP`
    - The source is simply "ZIP Code"; the added parenthetical is extra content, and duplicating "Code postal" collides with the separate Postal Code label.
- `CloseTab.ArrivingNotification.title.v133` — `fr/firefox-ios.xliff` — The app name placeholder is placed after "Onglets", turning "%1$@ tabs closed" into "Tabs %1$@ closed".
    - Current: `Onglets %1$@ fermés : %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `Onglets fermés dans %1$@ : %2$@`
    - %1$@ is the app name (e.g. Firefox) qualifying "tabs"; "Onglets Firefox fermés" reads as if Firefox were an adjective placed oddly and the meaning "Firefox tabs closed" is garbled in French word order.
- `LibraryPanel.Section.Older` — `fr/firefox-ios.xliff` — "Older" (items older than thirty days) is rendered as "Avant le mois dernier" (before last month).
    - Current: `Avant le mois dernier`
    - Source: `Older`
    - Suggest: `Plus ancien`
    - The source and developer comment say the section groups items older than thirty days; "Avant le mois dernier" states a different time frame (before last month).
- `MainMenu.ToolsSection.Translation.Translated.Title.v151` — `fr/firefox-ios.xliff` — "Translated…" is rendered as "Page traduite…", adding a noun not present in the source and diverging from the v145 variant "Traduit".
    - Current: `Page traduite…`
    - Source: `Translated…`
    - Suggest: `Traduit…`
    - The source is just "Translated…"; the parallel string MainMenu.ToolsSection.Translation.Translated.Title.v145 is translated as "Traduit".
- `NativeErrorPage.GenericError.Description.v134` — `fr/firefox-ios.xliff` — Present tense "can't be created" rendered as past tense "n'a pas pu être établie".
    - Current: `une connexion sécurisée n’a pas pu être établie`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `une connexion sécurisée ne peut pas être établie`
    - The en-US source says "a secure connection can’t be created" (present), not "could not be established".
- `Onboarding.Modern.BrandRefresh.Sync.Description.v148` — `fr/firefox-ios.xliff` — "stays safe and secure with encryption" loses "safe and secure" nuance but mainly the translation drops nothing critical; however "Grab bookmarks, passwords, and more" is fine — issue is omission of "safe and secure".
    - Current: `Vos données personnelles sont protégées grâce au chiffrement.`
    - Source: `Grab bookmarks, passwords, and more on any device in a snap. Your personal data stays safe and secure with encryption.`
    - Suggest: `Vos données personnelles restent en sécurité grâce au chiffrement.`
    - Minor omission of "stays"; acceptable rendering.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `fr/firefox-ios.xliff` — "won't sell you out" (won't betray/sell your data) is rendered as "digne de confiance" (trustworthy), losing the source meaning.
    - Current: `Rapide, sûr et digne de confiance.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Rapide, sûr et qui ne vous trahit pas.`
    - The en-US phrase means the browser will not betray the user / sell their data; "digne de confiance" is a generic, weaker claim that does not convey it.
- `Onboarding.Modern.Sync.Description.v145` — `fr/firefox-ios.xliff` — "sync on any device" rendered as "sur tous vos appareils" (on all your devices) instead of "sur n'importe quel appareil".
    - Current: `sont synchronisés sur tous vos appareils`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `sont synchronisés sur n’importe quel appareil`
    - The en-US says "on any device"; the v140 sibling string correctly uses "n’importe quel appareil". "tous vos appareils" changes the meaning.
- `Onboarding.Modern.TermsOfService.Description.v145` — `fr/firefox-ios.xliff` — "Brought to you by" translated as "Conçu par" (designed by), altering the meaning.
    - Current: `Conçu par l’organisation à but non lucratif %@`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Proposé par l’organisation à but non lucratif %@`
    - "Brought to you by" means offered/provided by, not designed by.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `fr/firefox-ios.xliff` — The translation says "allow opening of <app>" instead of allowing the app to open the URL.
    - Current: `Autoriser l’ouverture de %@ ?`
    - Source: `Allow %@ to open?`
    - Suggest: `Autoriser %@ à ouvrir ce lien ?`
    - Per the developer comment, %@ is the app name; the source asks permission for the app to open the scanned URL, not permission to open the app itself.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `fr/firefox-ios.xliff` — "Tab and Address Bar" is rendered as "la barre d’adresse et d’onglets", turning two bars into one and losing the tab bar.
    - Current: `masquer la barre d’adresse et d’onglets`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `masquer la barre d’onglets et la barre d’adresse`
    - The source refers to hiding both the tab bar and the address bar; the French merges them into a single "barre d’adresse et d’onglets".
- `Settings.Search.Accessibility.LearnAboutSuggestions.v124` — `fr/firefox-ios.xliff` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `En savoir plus sur Firefox suggère`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `En savoir plus sur Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must remain untranslated; it is kept in English elsewhere in the same file.
- `Settings.Search.GoogleLens.Footnote.v153` — `fr/firefox-ios.xliff` — "your active search engine" is translated as "moteur de recherche principal" (main/default) instead of active.
    - Current: `défini comme moteur de recherche principal`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `défini comme votre moteur de recherche actif`
    - The source says "is your active search engine while browsing", not the main/primary one.
- `Settings.Search.Suggest.AddressBarSetting.Title.v124` — `fr/firefox-ios.xliff` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `Barre d’adresse - Firefox suggère`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Barre d’adresse - Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must stay untranslated; the same file renders it correctly as "Firefox Suggest" in Settings.Search.Suggest.PrivateSession.Description.v125.
- `Settings.Search.Suggest.LearnAboutSuggestions.v124` — `fr/firefox-ios.xliff` — The brand name "Firefox Suggest" is translated as "Firefox suggère".
    - Current: `En savoir plus sur Firefox suggère`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `En savoir plus sur Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand name and must remain untranslated; it is kept in English elsewhere in the same file.
- `Settings.Search.Suggest.SearchSyncedTabs.Title.v124` — `fr/firefox-ios.xliff` — The toggle title "Search Synced Tabs" is rendered as an instruction to search within synced tabs rather than the setting name.
    - Current: `Rechercher dans les onglets synchronisés`
    - Source: `Search Synced Tabs`
    - Suggest: `Rechercher les onglets synchronisés`
    - The setting enables searching synced tabs; the French adds "dans" which changes it to "search inside the synced tabs". Other setting titles in this screen are noun/verb labels matching the source.
- `Settings.Translation.AutoTranslate.Footer.v151` — `fr/firefox-ios.xliff` — "your top preferred language" is rendered as "la langue de votre choix", losing the meaning of the highest-ranked preferred language.
    - Current: `Traduit automatiquement les pages dans la langue de votre choix.`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `Traduit automatiquement les pages dans votre langue préférée principale.`
    - The source refers to the top entry of the Preferred Languages list, not any language the user picks each time.
- `Offline Website Data` — `fr/firefox-ios.xliff` — "Offline Website Data" is rendered as "Données hors connexion", dropping "Website".
    - Current: `Données hors connexion`
    - Source: `Offline Website Data`
    - Suggest: `Données de sites web hors connexion`
    - The source refers specifically to website data stored for offline use; the French omits "des sites web", making the settings item vaguer than the source.
- `LibraryPanel.Section.Older` — `fr/firefox-ios.xliff` — "Older" (items older than thirty days) is rendered as "Avant le mois dernier" (before last month), which states a different time boundary.
    - Current: `Avant le mois dernier`
    - Source: `Older`
    - Suggest: `Plus anciens`
    - The source label is simply "Older", meaning items older than thirty days; "Avant le mois dernier" means "before last month" and misstates the section's scope.
- `Logins.PasscodeRequirement.Warning` — `fr/firefox-ios.xliff` — The brand reference "for Firefox" is dropped from the translation.
    - Current: `Pour utiliser la fonctionnalité de remplissage automatique, vous devez avoir un code d’appareil actif.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Pour utiliser la fonctionnalité de remplissage automatique de Firefox, vous devez avoir un code d’appareil actif.`
    - The en-US source says "the AutoFill feature for Firefox"; the French omits Firefox entirely.
- `Search.SuggestSectionTitle.v102` — `fr/firefox-ios.xliff` — "Firefox Suggest" is a product/feature name and must not be translated as a verb phrase.
    - Current: `Firefox suggère`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the brand feature name "Firefox Suggest"; rendering it as "Firefox suggère" turns the name into a sentence and loses the brand.
- `Search.ThirdPartyEngines.FailedMessage` — `fr/firefox-ios.xliff` — Past-tense failure message rendered as present/future impossibility.
    - Current: `Le moteur de recherche ne peut pas être ajouté.`
    - Source: `The search provider could not be added.`
    - Suggest: `Le moteur de recherche n’a pas pu être ajouté.`
    - Source "The search provider could not be added." reports a failure that already occurred, not a general inability.
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `fr/firefox-ios.xliff` — Wallpaper collection section title is translated as "Écran à l'ouverture" (Opening screen) instead of a wallpaper-related title.
    - Current: `ÉCRAN À L’OUVERTURE`
    - Source: `OPENING SCREEN`
    - Suggest: `COLLECTION`
    - The developer comment says this is the title of the wallpaper settings section; the French reuses the unrelated Start-at-Home "Opening screen" wording, which describes a different feature. (Source string itself is odd, but the French duplicates a different screen's label.)
- `Settings.TrackingProtection.Info.BlocksTitle` — `fr/firefox-ios.xliff` — "BLOCKS" is a plural noun heading (list of blocked items), rendered as a verb form "BLOQUE".
    - Current: `BLOQUE`
    - Source: `BLOCKS`
    - Suggest: `BLOQUÉS`
    - The comment says it is the title on an info view showing a list of all blocked websites, so the source is the plural noun/participle, not the third-person verb.
- `Are you sure?` — `fr/firefox-ios.xliff` — The prompt title "Are you sure?" is rendered as "Poursuivre la suppression ?" instead of an equivalent of the source.
    - Current: `Poursuivre la suppression ?`
    - Source: `Are you sure?`
    - Suggest: `Voulez-vous vraiment continuer ?`
    - The en-US source is a generic confirmation question "Are you sure?"; the French states "Continue with the deletion?", which is different content.
- `Clear Search` — `fr/firefox-ios.xliff` — "Clear Search" (singular action of clearing the search) is translated as a plural "Effacer les recherches".
    - Current: `Effacer les recherches`
    - Source: `Clear Search`
    - Suggest: `Effacer la recherche`
    - The developer comment says the button clears the search and exits search mode, not deletes multiple searches.
- `Search Input Field` — `fr/firefox-ios.xliff` — Accessibility label "Search Input Field" is translated as "Rechercher des identifiants" (Search logins).
    - Current: `Rechercher des identifiants`
    - Source: `Search Input Field`
    - Suggest: `Champ de saisie de recherche`
    - The source names the UI element (search input field); the French turns it into an action label with different content.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `fr/firefox-ios.xliff` — "Levé de soleil" is a misspelling of "Lever de soleil" (sunrise).
    - Current: `Levé de soleil`
    - Source: `Sunrise`
    - Suggest: `Lever de soleil`
    - The French noun for sunrise is "lever de soleil"; "levé" is a past participle and is incorrect here.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `fr/firefox-ios.xliff` — Missing "où" in the phrase "reprenez là où vous en étiez".
    - Current: `Reprenez là vous en étiez`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Reprenez là où vous en étiez`
    - The French idiom for "pick up where you left off" is "reprenez là où vous en étiez"; the relative pronoun "où" is missing, leaving an ungrammatical sentence.
- `Onboarding.Customization.Intro.Description.v123` — `fr/firefox-ios.xliff` — Ungrammatical construction "à votre propre façon de naviguer" after "Configurez".
    - Current: `Configurez le thème et la barre d’outils à votre propre façon de naviguer.`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `Adaptez le thème et la barre d’outils à votre propre façon de naviguer.`
    - "Configurez … à …" is not valid French; the source means setting theme and toolbar to match one's browsing style, which requires a verb like "adapter".
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `fr/firefox-ios.xliff` — Agreement error: "limité" must agree with the feminine noun "édition".
    - Current: `Fond d’écran en édition limité`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Fond d’écran en édition limitée`
    - "édition" is feminine, so the adjective must be "limitée" (Limited Edition Wallpaper).
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `fr/firefox-ios.xliff` — Missing preposition: "suggestions %@" should be "suggestions de %@" to render "suggestions from Firefox".
    - Current: `Obtenir des suggestions %@ en rapport avec votre recherche`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `Obtenir des suggestions de %@ en rapport avec votre recherche`
    - The source is "Get suggestions from %@ related to your search"; without "de", the app name is juxtaposed ungrammatically to "suggestions".
- `Quick-Search Engines` — `fr/firefox-ios.xliff` — Incorrect plural agreement in "Moteurs de recherches rapides".
    - Current: `Moteurs de recherches rapides`
    - Source: `Quick-Search Engines`
    - Suggest: `Moteurs de recherche rapides`
    - In French, "moteur de recherche" keeps "recherche" in the singular; the adjective "rapides" agrees with "moteurs".
- `Mobile Bookmarks` — `fr/firefox-ios.xliff` — Adjective agreement error: "mobile" must agree with the plural noun "Marque-pages".
    - Current: `Marque-pages mobile`
    - Source: `Mobile Bookmarks`
    - Suggest: `Marque-pages mobiles`
    - "Marque-pages" is plural, so the qualifying adjective should be "mobiles".

### D. Terminology, register & consistency

- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `fr/firefox-ios.xliff` — "Desktop site" is rendered as "version classique" here but as "version pour ordinateur"/"Version ordinateur" in the sibling strings on the same menu.
    - Current: `Passer en version classique`
    - Source: `Switch to Desktop Site`
    - Suggest: `Passer en version pour ordinateur`
    - MainMenu.ToolsSection.AccessibilityLabels.SwitchToDesktopSite.v132 uses "Passer en version pour ordinateur" and MainMenu.ToolsSection.DesktopSite.Title.v141 uses "Version ordinateur" for the same concept on the same screen; "classique" is inconsistent.
- `DefaultBrowserPopup.SecondLabel.v114` — `fr/firefox-ios.xliff` — "Default Browser App" is rendered as "App du navigateur par défaut", which does not match the iOS French setting label "Application par défaut du navigateur".
    - Current: `2. Appuyez sur *App du navigateur par défaut*`
    - Source: `2. Tap *Default Browser App*`
    - Suggest: `2. Appuyez sur *Application par défaut du navigateur*`
    - The string quotes an actual iOS Settings item; the French system wording is "Application par défaut du navigateur", and "App du navigateur par défaut" also mistakenly makes "par défaut" modify "navigateur".
- `Summarizer.Error.MissingPageContent.Message.v142` — `fr/firefox-ios.xliff` — "hit summarize" on a touch device is rendered as "cliquez" (click) instead of a tap action.
    - Current: `puis cliquez sur « Résumer »`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `puis appuyez sur « Résumer »`
    - This is an iOS touch interface; elsewhere in the same feature the French uses « Appuyez » for tap (e.g. ContextualHints.Summarize.Description). "cliquez" refers to a mouse click and is inconsistent terminology.
- `Summarizer.Error.Unknown.Message.v142` — `fr/firefox-ios.xliff` — "summarizing" is translated as « synthèse » while every other string in the same file uses « résumé ».
    - Current: `Erreur lors de la synthèse de la page.`
    - Source: `Error summarizing page. Try again later.`
    - Suggest: `Erreur lors du résumé de la page.`
    - Terminology inconsistency within the same screen: the feature is consistently called « résumé »/« résumer » in the other Summarizer strings.
- `WebCompatReporter.Fields.ChooseIssueTypeAccessibilityHint.v156` — `fr/firefox-ios.xliff` — "issue type" rendered as "type de ticket", inconsistent with "type de problème" used for the same term in the sibling string.
    - Current: `Choisir d’abord un type de ticket`
    - Source: `Choose an issue type first`
    - Suggest: `Choisir d’abord un type de problème`
    - The en-US "issue type" is translated "type de problème" in WebCompatReporter.Fields.ChooseSubOptionAccessibilityHint.v156 on the same form; "ticket" introduces a support-ticket concept absent from the source.
- `Search.ThirdPartyEngines.FormErrorTitle` — `fr/firefox-ios.xliff` — "Failed" translated as "Erreur" here while the identical source string is "Échec" in the sibling strings on the same screen.
    - Current: `Erreur`
    - Source: `Failed`
    - Suggest: `Échec`
    - Search.ThirdPartyEngines.DuplicateErrorTitle and FailedTitle use "Échec" for the same source "Failed"; inconsistent within the same feature.

### E. Typography, punctuation & spacing

- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `fr/firefox-ios.xliff` — The en dash separator in the source is rendered as an em dash without matching French spacing convention.
    - Current: `des moteurs de recherche — le tout`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `des moteurs de recherche – le tout`
    - The source uses an en dash (–); the translation substitutes an em dash, deviating from the source typography.
- `TopSites.RemovePage.Button` — `fr/firefox-ios.xliff` — Em dash from the source replaced by a hyphen.
    - Current: `Supprimer la page - %@`
    - Source: `Remove page — %@`
    - Suggest: `Supprimer la page — %@`
    - The en-US source uses an em dash (—) as separator; French typography also uses the em/en dash here, not a plain hyphen.

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
