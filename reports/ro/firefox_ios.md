# Firefox iOS l10n QA — ro

| | |
|---|---|
| **Generated** | 2026-10-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **Previous run** | 2026-10-19 @ `ec61063c1c68` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ro: [android](android.md)

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
| Strings | 1,927 |
| Missing strings | 46 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**46 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/VPN.strings` — 20
- `ro/firefox-ios.xliff` — 17
- `ro/firefox-ios.xliff` — 7
- `ro/firefox-ios.xliff` — 2

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/VPN.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 14 | **polish-double** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (40)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 21 |
| 3 | Degraded language (grammar, spelling, terminology) | 17 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `DefaultBrowserPopup.DescriptionFooter.v124` — `ro/firefox-ios.xliff` — A space was inserted after the opening bold asterisk, which can stop the bold markup from working.
    - Current: `* %@ este deja implicit?*`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `*%@ este deja implicit?*`
    - The developer comment says to keep the text inside the asterisks so it is bolded correctly. The source has no space after the opening '*'. If the app uses Markdown-style parsing, a space after the opening delimiter breaks the bold and the asterisks show up as text. If it just splits on asterisks, it only adds a stray leading space.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `ro/firefox-ios.xliff` — "Noțiuni de bază" means "basic concepts/fundamentals", not the basic icon variants this heading names.
    - Current: `Noțiuni de bază`
    - Source: `Basics`
    - Suggest: `De bază`
    - Per the developer comment, this heading labels the basic variants of the app icon (default, white, black, legacy). "Noțiuni de bază" means introductory knowledge, as in a tutorial, so it misdescribes the section.
- `BrowserDataTransfer.ImportedBookmarksFolder.Title.v160` — `ro/firefox-ios.xliff` — The folder name makes the date the thing that was imported ("<date> was imported") instead of labelling the folder as bookmarks imported on that date.
    - Current: `%@ a fost importat`
    - Source: `Imported %@`
    - Suggest: `Importate %@`
    - The developer comment says %@ is the import date, so the en-US 'Imported %@' means 'Imported (on) <date>'. The Romanian '%@ a fost importat' reads '<date> was imported', which turns the date into the subject. It is also odd as a folder name.
- `Addresses.EditAddress.AutofillAddressPin.v129` — `ro/firefox-ios.xliff` — The label for the Indian PIN postal code field is translated as the verb "to pin" (Fixează).
    - Current: `Fixează`
    - Source: `Pin`
    - Suggest: `Cod PIN`
    - The developer comment says this is the Postal Index Number field used in India. "Fixează" means "pin" as in fixing or pinning something, which makes no sense as a form field label.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `ro/firefox-ios.xliff` — "Post town" is translated as "post office" (Oficiu poștal) instead of a town or locality.
    - Current: `Oficiu poștal`
    - Source: `Post town`
    - Suggest: `Localitate poștală`
    - A UK post town is the town used for sorting mail. "Oficiu poștal" means a post office building, so users would be asked for the wrong information.
- `FirefoxHomepage.FeltPrivacyUI.Body.v122` — `ro/firefox-ios.xliff` — 'private tabs' is rendered as 'ferestrele private' (private windows) instead of 'filele private'.
    - Current: `toate ferestrele private`
    - Source: `%@ deletes your cookies, history, and site data when you close all your private tabs.`
    - Suggest: `toate filele private`
    - The source says data is deleted when you close all your private tabs. Firefox for iOS has private tabs, not private windows, and 'file' is the Romanian Firefox term for tabs.
- `MainMenu.Account.SignedIn.Description.v141` — `ro/firefox-ios.xliff` — Translation narrows "what you back up" to "files" and puts "sync" in the wrong person, so it reads as a separate command.
    - Current: `Gestionează fișierele pentru care faci copii de rezervă și sincronizează`
    - Source: `Manage what you back up and sync`
    - Suggest: `Gestionează ce salvezi și sincronizezi`
    - The en-US means managing what data (bookmarks, passwords, tabs, etc.) the user backs up and syncs. Account sync does not handle 'fișiere' (files), and 'sincronizează' (imperative/3rd person) does not match 'faci' (2nd person), which changes the sentence structure.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `ro/firefox-ios.xliff` — "Home" for the iOS Home screen tool is translated as "Pagină de start", which means the browser homepage, not the device home screen.
    - Current: `Pagină de start`
    - Source: `Home`
    - Suggest: `Ecran de pornire`
    - The comment says this subtitle is for the Add to Home screen tool for the iOS Home screen. The matching title uses "ecranul de pornire", while "Pagină de start" is the Firefox homepage term, so this names a different feature.
- `MainMenu.Submenus.Save.AddToHomeScreen.Subtitle.v131` — `ro/firefox-ios.xliff` — "Home" for the Add to Home Screen tool is translated as "Pagină de start" (browser homepage) instead of the home screen.
    - Current: `Pagină de start`
    - Source: `Home`
    - Suggest: `Ecran de pornire`
    - This subtitle belongs to the Add to Home Screen tool, whose title says "ecranul de pornire". "Pagină de start" refers to the Firefox homepage, which is a different thing.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `ro/firefox-ios.xliff` — The label "Save submenu" is translated as an imperative meaning "Save the submenu" rather than naming the Save submenu.
    - Current: `Salvează submeniul`
    - Source: `Save submenu`
    - Suggest: `Submeniul Salvează`
    - The developer comment says this accessibility label names the Save submenu. "Salvează submeniul" reads as a command to save the submenu itself, so screen-reader users hear the wrong thing. The matching Tools label is phrased as a noun ("Submeniu de Instrumente"), so this one should be a noun too.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `ro/firefox-ios.xliff` — "Agreează" is a false friend: in Romanian it means to like or favour someone, not to agree to terms.
    - Current: `Agreează și continuă`
    - Source: `Agree and continue`
    - Suggest: `Acceptă și continuă`
    - The en-US "Agree and continue" means accepting the Terms of Use. Romanian "a agrea" means to look on someone favourably, so the button doesn't say "accept". Standard renderings are "Acceptă și continuă" or "Sunt de acord și continui".
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `ro/firefox-ios.xliff` — The app name is made the object being opened instead of the subject doing the opening.
    - Current: `Permiți deschiderea %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Permiți ca %@ să deschidă?`
    - The source asks whether the app (%@, e.g. Firefox) may open the scanned URL. The Romanian reads 'Do you allow opening Firefox?', which asks about opening the app itself.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `ro/firefox-ios.xliff` — The title is translated as 'scroll to [a setting called] Hide tab and Address bar' instead of 'scroll to hide the tab and address bar'.
    - Current: `Derulează la Ascunde fila și Bară de adrese`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Derulează pentru a ascunde fila și bara de adrese`
    - The en-US describes the feature: scrolling hides the tab and address bar. The ro uses 'la' (to/at) with capitalized fragments, so it reads as if the user is being sent to an item named 'Ascunde fila'. The article on 'bara' is also missing.
- `Settings.Search.Suggest.AddressBarSetting.Title.v124` — `ro/firefox-ios.xliff` — The product name 'Firefox Suggest' is translated as 'sugestii Firefox', unlike the other strings on the same screen.
    - Current: `sugestii Firefox`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - Firefox Suggest is a product name. Other strings in this file keep it untranslated ('Afișează sugestii de la Firefox Suggest', 'Află mai multe despre Firefox Suggest'), so the name is inconsistent on this screen.
- `Settings.Search.Suggest.LearnAboutSuggestions.v124` — `ro/firefox-ios.xliff` — The product name 'Firefox Suggest' is translated as 'sugestiile Firefox', which doesn't match its accessibility label, where the name stays in English.
    - Current: `despre sugestiile Firefox`
    - Source: `Learn more about Firefox Suggest`
    - Suggest: `despre Firefox Suggest`
    - The matching accessibility string Settings.Search.Accessibility.LearnAboutSuggestions.v124 keeps 'Firefox Suggest'. The product name should not be translated.
- `DefaultBrowserOnboarding.Description2` — `ro/firefox-ios.xliff` — Step names a non-existent iOS settings item ("Set as default browser") instead of the Default Browser App setting.
    - Current: `Atinge Setează ca browser implicit`
    - Source: `2. Tap Default Browser App`
    - Suggest: `Atinge Browser implicit`
    - The source refers to the iOS Settings item "Default Browser App", shown in the screenshot string as "Browser implicit"; the translation instead uses Firefox's own menu label "Set as Default Browser", so the instruction doesn't match what the user sees.
- `ActivityStream.JumpBackIn.SectionTitle` — `ro/firefox-ios.xliff` — The section title says 'Return to this tab', but the section lists several recent tabs.
    - Current: `Revino la fila aceasta`
    - Source: `Jump Back In`
    - Suggest: `Revino`
    - Per the comment, this is a section title for recently viewed tabs. 'Fila aceasta' (this tab) points to one specific tab, which does not match a section header.
- `AddPass.Error.Message` — `ro/firefox-ios.xliff` — Wallet 'pass' is translated as 'parolă' (password).
    - Current: `adăugarea parolei în Wallet`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `adăugarea permisului în Wallet`
    - Per the comment and the Apple link, a Wallet pass is a card, ticket or boarding pass, not a password. 'Parolă' means password, so the message misleads the user.
- `AddPass.Error.Title` — `ro/firefox-ios.xliff` — Wallet 'pass' is translated as 'parolă' (password) in the alert title.
    - Current: `Eșec la adăugarea parolei`
    - Source: `Failed to Add Pass`
    - Suggest: `Eșec la adăugarea permisului`
    - 'Pass' here means an Apple Wallet pass, not a password, as the comment and linked support article show.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `ro/firefox-ios.xliff` — Translation says blocking reduces how many social media companies can see, not how much they can see.
    - Current: `reduce cât de multe companii de social media pot vedea ce faci online`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce cât de mult pot vedea companiile de social media din ceea ce faci online`
    - The source means blocking limits the amount the companies can see. "cât de multe companii" means "how many companies", which is a different statement.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `ro/firefox-ios.xliff` — "Camera Roll" is translated as "rolul camerei", which means "the role of the camera", not a photo roll.
    - Current: `rolul camerei`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `rola camerei`
    - "Camera Roll" is the iOS photo album. In Romanian "rol" means role, while a roll (of film) is "rolă". As it stands the sentence says the image is saved to the camera's role.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `ro/firefox-ios.xliff` — "din lista de lectură" means "from the reading list" instead of "to your Reading List".
    - Current: `Salvează paginile din lista de lectură`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Salvează paginile în lista de lectură`
    - The source says pages are saved to the Reading List. The translation says they are saved from it, which reverses the direction of the action.
- `Settings.Home.Option.Wallpaper.LimitedEdition.IndependentVoices.Description.v106` — `ro/firefox-ios.xliff` — The translation reads "Try the Independent Voices collection": it adds "try" and drops "new" from the source.
    - Current: `Încearcă colecția Voci Independente.`
    - Source: `The new Independent Voices collection.`
    - Suggest: `Noua colecție Voci Independente.`
    - The en-US is a descriptive phrase, "The new Independent Voices collection." The ro turns it into an imperative ("Try...") and loses the information that the collection is new. The developer comment describes it as a description of the seasonal wallpaper group, not a call to action.

### C. Grammar, agreement & spelling

- `ContextualHints.MainMenu.NewMenu.Body.v132` — `ro/firefox-ios.xliff` — The preposition "de" is missing, which "a avea nevoie de" requires.
    - Current: `Găsește mai rapid ce ai nevoie`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `Găsește mai rapid de ce ai nevoie`
    - Standard Romanian requires 'de ce ai nevoie'; 'ce ai nevoie' is a grammatical error.
- `Microsurvey.Survey.Options.Dissatisfied.v132` — `ro/firefox-ios.xliff` — Uses the cedilla letter ţ instead of the correct comma-below ț, which doesn't match the other options.
    - Current: `Nemulţumit(ă)`
    - Source: `Dissatisfied`
    - Suggest: `Nemulțumit(ă)`
    - Standard Romanian spelling uses ț (U+021B), not the cedilla form ţ (U+0163). The sibling options on the same screen use ț.
- `Microsurvey.Survey.Options.Neutral.v132` — `ro/firefox-ios.xliff` — The gender-suffix pattern "(ă)" produces the invalid form "neutruă".
    - Current: `Neutru(ă)`
    - Source: `Neutral`
    - Suggest: `Neutru/Neutră`
    - The feminine of "neutru" is "neutră", so you can't just append ă the way you can with "mulțumit(ă)". The current text implies a word that doesn't exist.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatus.v151` — `ro/firefox-ios.xliff` — Status label for a single feature uses plural "Disponibile", inconsistent with "Blocată" and "Disponibilă" on the same screen.
    - Current: `Disponibile`
    - Source: `Available`
    - Suggest: `Disponibilă`
    - The status describes one feature (funcționalitate, feminine singular); the paired status "Blocată" and the description "**Disponibilă**" both use feminine singular.
- `Settings.Browsing.AdBlocker.Description.v155` — `ro/firefox-ios.xliff` — The imperative of „a încerca” is misspelled as „încercă”.
    - Current: `încercă să dezactivezi`
    - Source: `Reduces ads and ad-related trackers. If a site looks broken, try turning this off.`
    - Suggest: `încearcă să dezactivezi`
    - The informal second-person imperative of „a încerca” is „încearcă”. „Încercă” is not a valid form.
- `Downloads.CancelDialog.Message` — `ro/firefox-ios.xliff` — The verb „a renunța” is missing the preposition „la” it needs before its object.
    - Current: `să renunți această descărcare`
    - Source: `Are you sure you want to cancel this download?`
    - Suggest: `să renunți la această descărcare`
    - In Romanian, „a renunța” takes its object through „la”. Without it, „renunți această descărcare” is ungrammatical.
- `Menu.AddPin.Confirm2` — `ro/firefox-ios.xliff` — Participle "Adăugate" is feminine plural although the toast refers to a single added item.
    - Current: `Adăugate la comenzi rapide`
    - Source: `Added to Shortcuts`
    - Suggest: `Adăugat la comenzi rapide`
    - The toast confirms one item (the current site) was added to Shortcuts; the participle should be singular "Adăugat", as in the parallel toast "Adăugat în lista de lectură".
- `Menu.TabSent.Confirm` — `ro/firefox-ios.xliff` — Definite article in the toast: "Fila trimisă" reads as "the sent tab" instead of the confirmation "Tab sent".
    - Current: `Fila trimisă`
    - Source: `Tab Sent`
    - Suggest: `Filă trimisă`
    - Confirmation messages in this file use the bare form ("Marcaj eliminat", "URL copiat"). The articled form makes the phrase a noun phrase, not a confirmation.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `ro/firefox-ios.xliff` — Typo: "Criptomomerii" instead of "Criptominerii".
    - Current: `Criptomomerii`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Criptominerii`
    - The word for cryptominers is spelled "Criptomineri" elsewhere on this screen; "Criptomomerii" is a misspelling.

### D. Terminology, register & consistency

- `MainMenu.Submenus.Tools.AccessibilityLabels.Share.Title.v144` — `ro/firefox-ios.xliff` — Accessibility label uses "Distribuie" while the visible Share title (v144) and all other Share strings in this menu use "Partajează".
    - Current: `Distribuie`
    - Source: `Share`
    - Suggest: `Partajează`
    - The same Share action is called "Partajează" in the visible title MainMenu.Submenus.Tools.Share.Title.v144 and in every other Share string in this file. If the accessibility label uses a different word, screen-reader and voice-control users get a label that doesn't match what is on screen.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `ro/firefox-ios.xliff` — Bolded status term "Blocat" does not match the status label "Blocată" it explains.
    - Current: `**Blocat**`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `**Blocată**`
    - The description defines the status label shown as "Blocată" (feminine, agreeing with funcționalitate); the parallel Available description uses feminine "Disponibilă".
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `ro/firefox-ios.xliff` — English word "user" left untranslated in Romanian sentence.
    - Current: `per user`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `per utilizator`
    - "user" is English; the standard Romanian term is "utilizator".
- `TodayWidget.TopSitesGalleryDescription` — `ro/firefox-ios.xliff` — 'Shortcuts' rendered as 'scurtături' while every other widget string, including this widget's title, uses 'comenzi rapide'.
    - Current: `Adaugă scurtături către`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `Adaugă comenzi rapide către`
    - Within the same widget gallery, 'shortcuts' is consistently 'comenzi rapide' (e.g. TopSitesGalleryTitleV2 'Comenzi rapide pentru site-uri web'); this description diverges.
- `PzSrmZ-eHmH1H` — `ro/firefox-ios.xliff` — Confirmation quotes the option as „Șterge filele private” but the menu item it refers to is labelled „Elimină filele private”.
    - Current: `„Șterge filele private”`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `„Elimină filele private”`
    - The string quotes the 'Clear Private Tabs' menu item (eHmH1H), which is translated 'Elimină filele private'; the quoted label should match the visible item.
- `fi3W24-eHmH1H` — `ro/firefox-ios.xliff` — Match-count label quotes „Șterge filele private” while the menu item is „Elimină filele private”.
    - Current: `„Șterge filele private”`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `„Elimină filele private”`
    - Quotes the 'Clear Private Tabs' option, whose label (eHmH1H) is 'Elimină filele private'; inconsistent quoted name.

### E. Typography, punctuation & spacing

- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `ro/firefox-ios.xliff` — A full stop wrongly splits the sentence before a lower-case 'așa că'; it should be a comma.
    - Current: `înainte să se încarce pagina. așa că`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `înainte să se încarce pagina, așa că`
    - The en-US is one sentence ('…before a page loads, so you may see…'). The full stop leaves a lower-case clause after it. The Standard mode footer correctly uses a comma here.
- `TopSites.RemovePage.Button` — `ro/firefox-ios.xliff` — The em dash in the source was replaced with a plain hyphen.
    - Current: `Elimină pagina - %@`
    - Source: `Remove page — %@`
    - Suggest: `Elimină pagina – %@`
    - The en-US uses an em dash as a separator. The ro tree uses en or em dashes for this, never a hyphen with spaces around it, so the hyphen is a typographic deviation.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ro/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
