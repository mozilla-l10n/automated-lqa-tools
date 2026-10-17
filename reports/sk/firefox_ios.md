# Firefox iOS l10n QA — sk

| | |
|---|---|
| **Generated** | 2026-10-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sk: [android](android.md) · [firefox](firefox.md)

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
| quotes | `curly-single` 10, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 10 | **typographic** |
| ellipsis | `char` 28 | **char** |
| dash | `en` 5 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (36)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `NSMicrophoneUsageDescription` — `sk/firefox-ios.xliff` — The translation leaves out that Firefox uploads the recorded audio; it only mentions recording.
    - Current: `na nahrávanie zvuku`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `na nahrávanie a nahrávanie zvuku na server`
    - The en-US says Firefox uses the microphone 'to record and upload audio'. The sk drops 'upload'. In a privacy permission description, this tells the user the audio is only recorded and not sent anywhere.
- `Settings.TrackingProtection.ProtectionCellFooter` — `sk/firefox-ios.xliff` — The hedged "helps stop advertisers from tracking" has been translated as a flat promise that the feature prevents tracking.
    - Current: `zabraňuje inzerentom sledovať vás na internete`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `pomáha zabrániť inzerentom sledovať vás na internete`
    - The en-US only claims the feature helps stop tracking. "zabraňuje" (prevents) makes the product promise it stops advertisers from tracking, a guarantee the source does not make.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 18 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `sk/firefox-ios.xliff` — The translation leaves out that Firefox uploads the recorded audio; it only mentions recording.
    - Current: `na nahrávanie zvuku`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `na nahrávanie a nahrávanie zvuku na server`
    - The en-US says Firefox uses the microphone 'to record and upload audio'. The sk drops 'upload'. In a privacy permission description, this tells the user the audio is only recorded and not sent anywhere.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `sk/firefox-ios.xliff` — Strict mode is described as blocking "common" trackers rather than "more" trackers, and the hedge "may see" became a certain outcome.
    - Current: `blokuje bežné sledovacie prvky ešte pred načítaním stránky, čo vedie k`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `blokuje viac sledovacích prvkov tým, že ich zastaví ešte pred načítaním stránky, takže môžete vidieť`
    - The source says Strict blocks MORE trackers by stopping them before the page loads, so the user MAY see a lower count. The translation says Strict blocks "bežné" (common) trackers, which repeats the Standard footer and loses the contrast between the two modes. It also states the lower count as a certainty.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `sk/firefox-ios.xliff` — The Slovak tells the user to continue on the other device, not to continue here from where they left off on the other device.
    - Current: `Na druhom zariadení pokračujte tam, kde ste prestali.`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Pokračujte tam, kde ste prestali na druhom zariadení.`
    - The hint points to a tab synced from another device, shown in Jump Back In on this device. The English means 'continue here from where you stopped on your other device'. With 'Na druhom zariadení' at the start, the phrase attaches to 'pokračujte', so it reads as an instruction to continue on the other device.
- `MainMenu.PanelLinkSection.AccessibilityLabels.Downloads.v132` — `sk/firefox-ios.xliff` — The label for the Downloads panel is translated as the verb "to download" instead of the panel's name.
    - Current: `Stiahnuť`
    - Source: `Downloads`
    - Suggest: `Stiahnuté súbory`
    - The comment says this label is for the action that opens the Downloads panel. "Stiahnuť" is an infinitive meaning "download (something)", so VoiceOver announces an action instead of the panel name.
- `UnifiedSearch.SearchEngineSelection.AccessibilityLabels.SearchSettings.Label.v133` — `sk/firefox-ios.xliff` — The label 'Search settings' (a noun phrase naming the settings screen) was translated as 'Hľadať v nastaveniach', meaning 'Search in settings'.
    - Current: `Hľadať v nastaveniach`
    - Source: `Search settings`
    - Suggest: `Nastavenia vyhľadávania`
    - The developer comment says this row opens the app's search settings screen. The Slovak instead tells screen-reader users the row searches inside settings. The visible title and hint on the same screen correctly use 'Nastavenia vyhľadávania' / 'nastavenia vyhľadávania'.
- `Settings.Summarize.FooterTitle.v142` — `sk/firefox-ios.xliff` — "súhrnným stránkam" means "summary pages", not access to the feature that summarizes pages.
    - Current: `k súhrnným stránkam`
    - Source: `Provides access to summarize pages.`
    - Suggest: `k vytváraniu súhrnov stránok`
    - The en-US "Provides access to summarize pages" describes the Summarize feature (making summaries of pages). The sk instead says it gives access to "summary pages", a different thing.
- `Translations.Sheet.TranslateTo.AccessibilityLabel.v145` — `sk/firefox-ios.xliff` — The accessibility label says 'Translated to %@' (past participle) instead of 'Translate to %@'.
    - Current: `Preložené do jazyka %@`
    - Source: `Translate To %@`
    - Suggest: `Preložiť do jazyka %@`
    - The source and developer comment describe the cell where you select the target language. 'Preložené' says the page has already been translated. It also doesn't match the visible label 'Preložiť do jazyka' or the sibling 'Preložiť z jazyka %@'.
- `Offline Website Data` — `sk/firefox-ios.xliff` — "Offline Website Data" is rendered as "pages in offline mode" instead of offline website data.
    - Current: `Stránky v režime offline`
    - Source: `Offline Website Data`
    - Suggest: `Údaje stránok v režime offline`
    - The setting item clears stored website data (per comment), not 'pages in offline mode'; the translation names a different thing.
- `DefaultBrowserCard.Description` — `sk/firefox-ios.xliff` — Translation says websites, emails and messages themselves open in Firefox, dropping 'links from'.
    - Current: `automatické otváranie webových stránok, e‑mailov a správ vo Firefoxe`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `automatické otváranie odkazov z webových stránok, e‑mailov a správ vo Firefoxe`
    - Source is about links from websites, emails and Messages opening in Firefox; the sk claims emails and messages open in Firefox.
- `Added page to Reading List` — `sk/firefox-ios.xliff` — The preposition 'zo' (from) reverses the direction: the message says the page was added from the Reading List, not to it.
    - Current: `pridaná zo Zoznamu na prečítanie`
    - Source: `Added page to Reading List`
    - Suggest: `pridaná do Zoznamu na prečítanie`
    - The source says the page was added to the Reading List. 'zo' means 'from', while 'do' means 'to', which is what the other Reading List strings use.
- `Decrease text size` — `sk/firefox-ios.xliff` — "Decrease text size" is translated as "Change text size", which loses the direction of the change.
    - Current: `Zmeniť veľkosť textu`
    - Source: `Decrease text size`
    - Suggest: `Zmenšiť veľkosť textu`
    - The source and comment describe the button that decreases font size. "Zmeniť" means "change", so VoiceOver users can't tell which way it changes the size.
- `HomePanel.ContextMenu.Bookmark` — `sk/firefox-ios.xliff` — The 'Bookmark' context menu action is translated as the plural noun 'Záložky' ('Bookmarks') instead of an action.
    - Current: `Záložky`
    - Source: `Bookmark`
    - Suggest: `Pridať medzi záložky`
    - The developer comment says this is the title of the Bookmark context menu action, which bookmarks the site. 'Záložky' names the bookmarks collection rather than the action. The Add Bookmark shortcut already uses 'Pridať medzi záložky'.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sk/firefox-ios.xliff` — "Cross-Site" is dropped, so this category is labelled simply "trackers".
    - Current: `Sledovacie prvky`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledovacie prvky medzi stránkami`
    - The source names one specific category (cross-site trackers). The generic "Sledovacie prvky" can't be told apart from the other tracker categories on the same screen, such as "Sledovacie prvky sociálnych sietí".
- `Settings.TrackingProtection.ProtectionCellFooter` — `sk/firefox-ios.xliff` — The hedged "helps stop advertisers from tracking" has been translated as a flat promise that the feature prevents tracking.
    - Current: `zabraňuje inzerentom sledovať vás na internete`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `pomáha zabrániť inzerentom sledovať vás na internete`
    - The en-US only claims the feature helps stop tracking. "zabraňuje" (prevents) makes the product promise it stops advertisers from tracking, a guarantee the source does not make.
- `Menu.NewPrivateTabAction.Title` — `sk/firefox-ios.xliff` — The translation says 'Open in private tab' instead of 'Open New Private Tab'.
    - Current: `Otvoriť na súkromnej karte`
    - Source: `Open New Private Tab`
    - Suggest: `Otvoriť novú súkromnú kartu`
    - The menu button opens a new private tab, as the developer comment says. 'Otvoriť na súkromnej karte' means opening something (e.g. a link) in a private tab, which is a different action. It is also inconsistent with 'Otvoriť novú kartu' for the normal tab.

### C. Grammar, agreement & spelling

- `Biometry.Screen.UniversalAuthenticationReason.v122` — `sk/firefox-ios.xliff` — Wrong case ending: "uloženým heslá" should be dative "uloženým heslám".
    - Current: `uloženým heslá`
    - Source: `Authenticate to access your saved passwords and payment methods.`
    - Suggest: `uloženým heslám`
    - The preposition "k" takes the dative case. The adjective is already dative, but the noun is left in the nominative/accusative plural, so they don't agree.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `sk/firefox-ios.xliff` — The reflexive pronoun "sa" appears twice.
    - Current: `prihláste sa a`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `prihláste a`
    - "Alebo sa prihláste sa a získajte" repeats "sa". The correct form is "Alebo sa prihláste a získajte".
- `LoginsList.NoLoginsFound.Description.v122` — `sk/firefox-ios.xliff` — Two embedded relative clauses are left without their closing commas.
    - Current: `synchronizujete do %@u budú zobrazené tu. Všetky heslá, ktoré uložíte sú šifrované.`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `synchronizujete do %@u, budú zobrazené tu. Všetky heslá, ktoré uložíte, sú šifrované.`
    - In Slovak, a relative clause inside a sentence must be set off by commas on both sides. The clauses 'ktoré uložíte alebo synchronizujete do %@u' and 'ktoré uložíte' each have an opening comma but no closing one before the main verb ('budú', 'sú').
- `Menu.EnhancedTrackingProtection.SwitchOff.Text.v129` — `sk/firefox-ios.xliff` — Verb does not agree with its subject: the singular "Ochrana" is paired with the plural "sú".
    - Current: `Ochrana sú VYPNUTÁ`
    - Source: `Protections are OFF. We suggest turning them back on.`
    - Suggest: `Ochrana je VYPNUTÁ`
    - "Ochrana" is feminine singular, so the verb must be "je". The rest of the sentence ("VYPNUTÁ", "ju") is singular too.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `sk/firefox-ios.xliff` — Button label mixes a first-person verb (Súhlasím) with an infinitive (pokračovať), which is ungrammatical.
    - Current: `Súhlasím a pokračovať`
    - Source: `Agree and continue`
    - Suggest: `Súhlasiť a pokračovať`
    - Coordinated verbs in a button label must share the same form; other buttons in this file use the infinitive (e.g. 'Uložiť a začať prehliadať').
- `ContextualHints.Summarize.Description.v142` — `sk/firefox-ios.xliff` — Case error: the genitive after "obsah" requires "tejto stránky", not "tejto stránku".
    - Current: `obsah tejto stránku`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `obsah tejto stránky`
    - "stránku" is accusative; the noun depends on "obsah" and must be genitive ("stránky") to agree with "tejto".
- `Summarizer.TabSnapshot.Accessibility.Label.v145` — `sk/firefox-ios.xliff` — Wrong case: the object of "zatvoriť" must be the accusative "súhrn", not "súhrnu", and the comma closing the clause is missing.
    - Current: `zatvoriť súhrnu potiahnite`
    - Source: `Drag or tap the web page to close the summary`
    - Suggest: `zatvoriť súhrn, potiahnite`
    - "súhrn" (masc. inanimate) has the accusative form "súhrn"; "súhrnu" is genitive/dative. Slovak also requires a comma after the subordinate clause "Ak chcete…".
- `AddPass.Error.Title` — `sk/firefox-ios.xliff` — Wrong genitive form: 'lístok' takes the genitive 'lístka', not 'lístku'.
    - Current: `Pridanie lístku zlyhalo`
    - Source: `Failed to Add Pass`
    - Suggest: `Pridanie lístka zlyhalo`
    - After 'Pridanie' the noun must be in the genitive, and the standard genitive singular of 'lístok' is 'lístka'.
- `ErrorPages.AdvancedWarning2.Text` — `sk/firefox-ios.xliff` — Spelling error: "potencionálne" should be "potenciálne".
    - Current: `potencionálne`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `potenciálne`
    - The standard Slovak adjective is "potenciálny". "Potencionálny" is a common non-standard form.
- `ReaderMode.Available.VoiceOverAnnouncement` — `sk/firefox-ios.xliff` — "Režim" is capitalised in the middle of the sentence.
    - Current: `K dispozícii je Režim Čítačka`
    - Source: `Reader Mode available`
    - Suggest: `K dispozícii je režim Čítačka`
    - In Slovak the common noun "režim" is lowercase mid-sentence. Only the feature name is capitalised, matching "Zobrazenie Čítačka" elsewhere.
- `SendTo.Error.Title` — `sk/firefox-ios.xliff` — The relative clause in the middle of the sentence is missing its closing comma.
    - Current: `Odkaz, ktorý sa pokúšate zdieľať nemôže byť zdieľaný.`
    - Source: `The link you are trying to share cannot be shared.`
    - Suggest: `Odkaz, ktorý sa pokúšate zdieľať, nemôže byť zdieľaný.`
    - Slovak punctuation rules require a relative clause in the middle of a sentence to be set off by commas on both sides. The comma before 'nemôže' is missing.
- `Settings.Disconnect.Body` — `sk/firefox-ios.xliff` — The possessive uses the wrong case: the instrumental singular masculine form is “vaším”, not “vašim”.
    - Current: `s vašim účtom`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `s vaším účtom`
    - After “s” (with), Slovak needs the instrumental singular, which is “vaším účtom”. “vašim” is the dative plural form, so this is a common spelling and grammar error.
- `Settings.Disconnect.Body` — `sk/firefox-ios.xliff` — “z toho zariadenia” says “from that device”; the source says “this device”, which should be “z tohto zariadenia”.
    - Current: `z toho zariadenia`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `z tohto zariadenia`
    - The en-US says “on this device”. In standard Slovak the genitive of “this” is “tohto”; “toho” means “that”, or is a colloquial shortening.
- `Settings.Tabs.CustomizeTabsSection.Title` — `sk/firefox-ios.xliff` — "zasobník" is misspelled; it is missing the accent on á.
    - Current: `zasobník`
    - Source: `Customize Tab Tray`
    - Suggest: `zásobník`
    - The correct Slovak spelling of "tray" is "zásobník".

### D. Terminology, register & consistency

- `Bookmarks.Menu.EditBookmarkChangeLocationLabel.v154` — `sk/firefox-ios.xliff` — "Location" is translated as "lokalitu" here but as "Umiestnenie" in the caption on the same picker.
    - Current: `Zmeniť lokalitu`
    - Source: `Change Location`
    - Suggest: `Zmeniť umiestnenie`
    - This link expands the Location summary whose caption reads "Umiestnenie". "Lokalita" suggests a geographic place and doesn't fit a folder location.
- `MainMenu.ToolsSection.AccessibilityLabels.SummarizePage.v142` — `sk/firefox-ios.xliff` — Accessibility label uses an informal second-person imperative instead of the infinitive used for the other menu actions.
    - Current: `Vytvor súhrn stránky`
    - Source: `Summarize Page`
    - Suggest: `Vytvoriť súhrn stránky`
    - The other action labels in this file use the infinitive (Prepnúť, Nahlásiť, Preložiť). 'Vytvor' is an informal command to the user and is inconsistent with them.
- `MainMenu.ToolsSection.SummarizePage.Title.v142` — `sk/firefox-ios.xliff` — Action uses an informal second-person imperative instead of the infinitive used by every other menu action.
    - Current: `Vytvor súhrn stránky`
    - Source: `Summarize Page`
    - Suggest: `Vytvoriť súhrn stránky`
    - The other menu actions in this file use the infinitive (Prepnúť, Nahlásiť, Preložiť). 'Vytvor' is an informal command to the user, which breaks both the register and consistency on the same menu.
- `ReaderModeBar.SummarizeButtonAccessibilityLabel.v150` — `sk/firefox-ios.xliff` — Button label uses an informal second-person singular imperative instead of the infinitive used for actions everywhere else.
    - Current: `Vytvor súhrn stránky`
    - Source: `Summarize Page`
    - Suggest: `Vytvoriť súhrn stránky`
    - The other action labels and buttons in this batch use the infinitive (Uložiť, Spravovať, Použiť) or the formal plural. 'Vytvor' is the informal 'ty' imperative, which breaks the locale's form of address.

### E. Typography, punctuation & spacing

- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `sk/firefox-ios.xliff` — A spaced hyphen is used as a dash where the locale convention is the en dash.
    - Current: `Pošta - mesto`
    - Source: `Post town`
    - Suggest: `Pošta – mesto`
    - The sk conventions set the en dash as the house dash; a hyphen with spaces around it is typographically wrong here.
- `Settings.Siri.SectionName` — `sk/firefox-ios.xliff` — A hyphen is used as a separating dash; the sk convention is the en dash.
    - Current: `Siri - skratky`
    - Source: `Siri Shortcuts`
    - Suggest: `Siri – skratky`
    - The sk convention uses the en dash; a spaced hyphen used as a dash breaks it.
- `TopSites.RemovePage.Button` — `sk/firefox-ios.xliff` — A spaced hyphen is used as the separator where the locale convention calls for an en dash.
    - Current: `Odstrániť stránku - %@`
    - Source: `Remove page — %@`
    - Suggest: `Odstrániť stránku – %@`
    - The source uses a dash as the separator, and the sk house dash is the en dash. A hyphen with spaces around it is not the correct dash here.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
