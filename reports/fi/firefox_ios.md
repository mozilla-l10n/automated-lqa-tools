# Firefox iOS l10n QA — fi

| | |
|---|---|
| **Generated** | 2026-10-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 1,907 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fi: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,907 |
| Missing strings | 20 |
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

**20 strings** are not translated yet, concentrated in:

- `fi/firefox-ios.xliff` — 8
- `fi/firefox-ios.xliff` — 7
- `fi/firefox-ios.xliff` — 3
- `fi/firefox-ios.xliff` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 10, `curly-double` 4 | _mixed_ |
| ellipsis | `char` 27 | **char** |
| dash | `em` 2, `en` 4 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (41)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `fi/firefox-ios.xliff` — "that you use it" is rendered as "how you use it", widening the data shared with marketing partners.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The en-US says only the fact that the user uses the app is shared; "kuinka käytät sitä" means "how you use it", so the product appears to share usage details with marketing partners, a broader data-sharing claim than the source makes.
- `CoverSheet.v24.ETP.Description` — `fi/firefox-ios.xliff` — The hedge "helps stop" is rendered as an unqualified "stops", so the Finnish promises full prevention of ad tracking.
    - Current: `estää mainoksia seuraamasta sinua`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `auttaa estämään mainoksia seuraamasta sinua`
    - The en-US says Enhanced Tracking Protection "helps stop ads from following you around". The Finnish "estää" means "prevents", which makes the product promise complete protection that the source does not claim.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 19 |
| 3 | Degraded language (grammar, spelling, terminology) | 20 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `fi/firefox-ios.xliff` — "Autofill" is translated as plain "fill", so the word "automatically" is lost.
    - Current: `Tallentaaksesi ja täyttääksesi luottokorttitiedot`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Tallentaaksesi ja täyttääksesi luottokorttitiedot automaattisesti`
    - The source says "autofill credit cards". The matching password message keeps "automaattisesti", but this one drops it.
- `Addresses.EditAddress.AutofillAddressParish.v129` — `fi/firefox-ios.xliff` — 'Parish' is translated as 'Kirkonkylä' (church village) rather than the administrative parish.
    - Current: `Kirkonkylä`
    - Source: `Parish`
    - Suggest: `Pitäjä`
    - The comment describes parish as a unit of local administration and addressing. 'Kirkonkylä' is the village around a parish church, which is a different thing. 'Pitäjä' (or 'Seurakunta') is the matching term.
- `FirefoxHomepage.Shortcuts.AddShortcut.CancelButtonTitle.v153` — `fi/firefox-ios.xliff` — The Cancel button is translated as "Kumoa", which means "Undo", not "Cancel".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - Per the developer comment, this button cancels adding a new shortcut. In Finnish, "Kumoa" means undo or revert an action. The standard word for Cancel, used throughout Finnish Firefox, is "Peruuta".
- `GoogleLens.Interstitial.CancelButtonTitle.v156` — `fi/firefox-ios.xliff` — "Cancel" is translated as "Kumoa" (Undo) instead of "Peruuta".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The button cancels a Google Lens search that is still running. "Kumoa" means undo, and the standard Finnish term for cancelling an action is "Peruuta".
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `fi/firefox-ios.xliff` — "save actions" (actions for saving, e.g. bookmarking) is rendered as "saving of actions".
    - Current: `toimintojen tallentamiseen`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `tallennustoimintoihin`
    - In the en-US, "save actions" names the menu's save-related options (bookmark, reading list, etc.). The Finnish "toimintojen tallentamiseen" means "to saving actions", as if the actions themselves were being saved.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `fi/firefox-ios.xliff` — "Home" for the iOS Home Screen tool is rendered as "Etusivu" (website/browser home page) instead of the home screen sense used in the sibling string ("Koti").
    - Current: `Etusivu`
    - Source: `Home`
    - Suggest: `Koti`
    - The comment says this subtitle refers to the Add to Home screen tool for the iOS Home screen; "Etusivu" means a website's front page or the browser homepage, so it names the wrong thing and is inconsistent with the non-accessibility subtitle "Koti" on the same menu.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `fi/firefox-ios.xliff` — "that you use it" is rendered as "how you use it", widening the data shared with marketing partners.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The en-US says only the fact that the user uses the app is shared; "kuinka käytät sitä" means "how you use it", so the product appears to share usage details with marketing partners, a broader data-sharing claim than the source makes.
- `Onboarding.Welcome.Description.TreatementA.v120` — `fi/firefox-ios.xliff` — The translation leaves out "secretly", so it no longer says the tracking is covert.
    - Current: `auttaa sinua estämään yrityksiä seuraamasta sinua verkossa`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `auttaa estämään yrityksiä seuraamasta sinua salaa verkossa`
    - The en-US says the browser helps stop companies from *secretly* following you around the web. The Finnish leaves out "salaa", which the other variant of this string (Onboarding.Welcome.Description.v120) includes. The wording should match that variant.
- `QuickAnswers.Errors.Cancel.v158` — `fi/firefox-ios.xliff` — "Cancel" on the alert's dismiss button is rendered as "Kumoa", which means "Undo".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The developer comment says the button closes the permission alert without taking action. In Finnish, "Kumoa" means undo or revert, and Firefox's Finnish translation uses "Peruuta" for Cancel.
- `Upgrade.SyncSign.Description.v114` — `fi/firefox-ios.xliff` — The translation drops "now on your homepage", the key information that tabs from other devices now appear on the homepage.
    - Current: `Jatka siitä, mihin jäit muiden laitteidesi välilehdillä.`
    - Source: `Pick up where you left off with tabs from other devices now on your homepage.`
    - Suggest: `Jatka siitä, mihin jäit muiden laitteidesi välilehdillä, jotka näkyvät nyt aloitussivullasi.`
    - The en-US says the tabs from other devices are now on the homepage. The Finnish leaves that out, so the new feature this upgrade screen announces is lost.
- `WebCompatReporter.Category.DesignBroken.v154` — `fi/firefox-ios.xliff` — The 'Design is broken' category is translated as a generic 'something is wrong with the page', so the layout/design meaning is lost.
    - Current: `Sivussa on jotain vikaa`
    - Source: `Design is broken`
    - Suggest: `Sivun ulkoasu on rikki`
    - The en-US source and the developer comment both say this category is for a broken layout or design. The Finnish says only that something is wrong with the page. That doesn't tell it apart from the 'Site is not usable' and 'Other' categories in the same picker.
- `CoverSheet.v24.ETP.Description` — `fi/firefox-ios.xliff` — The hedge "helps stop" is rendered as an unqualified "stops", so the Finnish promises full prevention of ad tracking.
    - Current: `estää mainoksia seuraamasta sinua`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `auttaa estämään mainoksia seuraamasta sinua`
    - The en-US says Enhanced Tracking Protection "helps stop ads from following you around". The Finnish "estää" means "prevents", which makes the product promise complete protection that the source does not claim.
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `fi/firefox-ios.xliff` — "Tab pickup" is rendered as "Välilehden valinta" (tab selection), which loses the meaning of continuing a synced tab from another device.
    - Current: `Välilehden valinta`
    - Source: `Tab pickup`
    - Suggest: `Jatka välilehdeltä`
    - The developer comment says the label marks the most recent tab from another signed-in device, which the user picks up to continue with. "Valinta" means choosing or selecting, so it does not convey that meaning.
- `LibraryPanel.History.ClearGroupedTabsCancel.v100` — `fi/firefox-ios.xliff` — "Cancel" in a delete confirmation dialog is rendered as "Kumoa" (Undo) instead of "Peruuta" (Cancel).
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The comment says this button cancels the pending deletion. "Kumoa" means undo/revert something already done, while the standard Finnish for dismissing a confirmation is "Peruuta".
- `Privacy Policy` — `fi/firefox-ios.xliff` — "Privacy Policy" is rendered as "Yksityisyydensuoja" (privacy protection), not as the policy document.
    - Current: `Yksityisyydensuoja`
    - Source: `Privacy Policy`
    - Suggest: `Tietosuojakäytäntö`
    - The comment says this opens the Firefox Privacy Policy page. "Yksityisyydensuoja" means privacy protection, not a policy.
- `ReopenAlert.Title` — `fi/firefox-ios.xliff` — "Last" is dropped, so the title reads "Reopen closed tab" instead of "Reopen Last Closed Tab".
    - Current: `Avaa uudelleen suljettu välilehti`
    - Source: `Reopen Last Closed Tab`
    - Suggest: `Avaa viimeksi suljettu välilehti uudelleen`
    - The source says it reopens specifically the last closed tab. The Finnish leaves out "viimeksi".
- `SentTab_TabArrivingNotification_WithDevice_body` — `fi/firefox-ios.xliff` — The translation says the tab came 'from device %@', but %@ is the app name and the tab arrived in it.
    - Current: `Uusi välilehti saapui laitteesta %@`
    - Source: `New tab arrived in %@`
    - Suggest: `Uusi välilehti saapui sovellukseen %@`
    - The developer comment says %@ is the app name, and the source reads 'New tab arrived in %@'. 'laitteesta' means 'from the device', which would show the app name as a sending device.
- `Wallpaper.Error.Dismiss.v106` — `fi/firefox-ios.xliff` — "Cancel" is rendered as "Kumoa", which means "Undo", not "Cancel".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The button dismisses the wallpaper error dialog (Cancel). "Kumoa" means "undo/revert", which suggests reverting an action. The standard Finnish rendering of Cancel is "Peruuta", as used for "Cancel" elsewhere in this batch.
- `DeleteLoginAlert.DeleteButton.Cancel.v122` — `fi/firefox-ios.xliff` — Cancel button in the delete-confirmation dialog is rendered as "Kumoa" (Undo) instead of "Peruuta" (Cancel).
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The source and comment describe a dismiss/cancel option for the deletion prompt; "Kumoa" means undo/revert an action already done, which is a different action and confusing in a confirmation dialog. Standard Finnish for Cancel is "Peruuta".

### C. Grammar, agreement & spelling

- `Bookmarks.Menu.EditBookmarkGroupExpandedValue.v154` — `fi/firefox-ios.xliff` — "Laajennuttu" is not a correct Finnish form for "Expanded"; the correct form is "Laajennettu".
    - Current: `Laajennuttu`
    - Source: `Expanded`
    - Suggest: `Laajennettu`
    - The passive past participle of "laajentaa" (to expand) is "laajennettu". This also matches "Kutistettu", which is used for the Collapsed value.
- `MainMenu.ToolsSection.AccessibilityLabels.ExpandedHint.v142` — `fi/firefox-ios.xliff` — "Laajennuttu" is not a valid Finnish word form; the past passive participle of "laajentaa" is "laajennettu".
    - Current: `Laajennuttu`
    - Source: `Expanded`
    - Suggest: `Laajennettu`
    - The source "Expanded" describes a menu section that has been expanded. In Finnish that is "laajennettu". "Laajennuttu" is a misspelling, and screen readers will read it aloud as it is written.
- `Summarizer.Error.RateLimited.Message.v142` — `fi/firefox-ios.xliff` — The verb "pystyä" is followed by the basic infinitive instead of the required 3rd infinitive (illative) form.
    - Current: `Tätä ei pysty käsitellä`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Tätä ei pystytä käsittelemään`
    - In standard Finnish, "pystyä" takes the -maan/-mään form ("pystyä käsittelemään"). "ei pysty käsitellä" is colloquial and grammatically incorrect in UI text.
- `DefaultBrowserCard.NextLevel.Description.v108` — `fi/firefox-ios.xliff` — Misspelling: "automaatisesti" is missing a 't'.
    - Current: `automaatisesti`
    - Source: `Choose Firefox as your default browser to make speed, safety, and privacy automatic.`
    - Suggest: `automaattisesti`
    - The correct Finnish spelling of 'automatically' is "automaattisesti". It is spelled correctly elsewhere in the same file (DefaultBrowserCard.Description).
- `BreachAlerts.Description` — `fi/firefox-ios.xliff` — The verb form "Suojaaksesi" is misspelled; the correct form of "suojata" is "Suojataksesi".
    - Current: `Suojaaksesi tilin`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `Suojataksesi tilin`
    - The verb is "suojata", so its purpose form ("in order to protect") is built from "suojata-" and gives "suojataksesi". "Suojaaksesi" is a spelling error.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `fi/firefox-ios.xliff` — The verb form "luodaksesi" is second person, but its subject is "Yksilöijät" (third person plural), so it should be "luodakseen".
    - Current: `luodaksesi`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `luodakseen`
    - In the en-US the fingerprinters create the profile. The Finnish "luodaksesi" means "in order for you to create", which is a grammatical error and makes it sound as though the user builds the profile.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `fi/firefox-ios.xliff` — The sentence is ungrammatical: "Tämän" is the wrong case and the subject of the saving is missing.
    - Current: `Tämän antaa tallentaa kuvan`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Tämä antaa sinun tallentaa kuvan`
    - "Tämän antaa tallentaa" is not grammatical Finnish. It needs the nominative "Tämä" and an agent ("sinun").
- `Search` — `fi/firefox-ios.xliff` — The settings section title uses the imperative verb "Hae" instead of the noun "Haku".
    - Current: `Hae`
    - Source: `Search`
    - Suggest: `Haku`
    - The comment says this is the Search section of settings. A section heading needs the noun form.
- `Search.ThirdPartyEngines.AddMessage` — `fi/firefox-ios.xliff` — Typo: 'pkahakupalkkiin' should be 'pikahakupalkkiin'.
    - Current: `pkahakupalkkiin`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `pikahakupalkkiin`
    - The Finnish word for quick search bar is 'pikahakupalkki', but the 'i' is missing.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `fi/firefox-ios.xliff` — The verb is in the imperative ("Salli") where the description needs the third-person indicative ("Sallii").
    - Current: `Salli joitain seuraimia`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Sallii joitain seuraimia`
    - The en-US "Allows some ad tracking" describes what the protection level does, in the same way the Strict description says "Estää…". The imperative "Salli" turns it into an instruction to the user.
- `eqyNJg` — `fi/firefox-ios.xliff` — Typo: "Poikatoiminto" should be "Pikatoiminto" (Quick Action).
    - Current: `Poikatoiminto`
    - Source: `Quick Action`
    - Suggest: `Pikatoiminto`
    - "Poika" means "boy"; the correct word for quick action is "pikatoiminto", as used in eV8mOT ("Pikatoiminnon tyyppi").
- `w9jdPK` — `fi/firefox-ios.xliff` — Typo: "Poikatoiminto" should be "Pikatoiminto" (Quick Action).
    - Current: `Poikatoiminto`
    - Source: `Quick Action`
    - Suggest: `Pikatoiminto`
    - "Poika" means "boy"; the correct word for quick action is "pikatoiminto", as used in eV8mOT ("Pikatoiminnon tyyppi").

### D. Terminology, register & consistency

- `Bookmarks.DeleteFolderWarning.CancelButton.Label` — `fi/firefox-ios.xliff` — The Cancel button is translated as "Kumoa" (Undo) instead of "Peruuta" (Cancel).
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - The button cancels a deletion that has not happened yet, so there is nothing to undo. In Finnish UI terminology, Cancel is "Peruuta" and "Kumoa" means Undo.
- `CredentialProvider.RetryAllert.CancelAction.Title.v137` — `fi/firefox-ios.xliff` — Cancel button rendered as "Kumoa" (Undo) instead of the standard "Peruuta".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - "Kumoa" means undo/revert; a dialog's Cancel action is conventionally "Peruuta" in Finnish.
- `Addresses.EditAddress.Alert.CancelButton.v129` — `fi/firefox-ios.xliff` — Cancel button in the remove-address alert rendered as "Kumoa" (Undo) instead of "Peruuta".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - "Kumoa" means undo; next to "Poista" it suggests undoing a removal, not dismissing the alert. The standard term is "Peruuta".
- `Menu.EnhancedTrackingProtection.ClearData.AlertCancelButton.v128` — `fi/firefox-ios.xliff` — The Cancel button of the clear-data alert is translated as "Kumoa" (Undo) instead of the standard "Peruuta".
    - Current: `Kumoa`
    - Source: `Cancel`
    - Suggest: `Peruuta`
    - "Cancel" on a confirmation dialog dismisses it without acting. "Kumoa" means undo or revert, and it is the usual term for Undo. The standard Finnish label for Cancel is "Peruuta".
- `FirefoxHomepage.Shortcuts.AddShortcut.TileTitle.v153` — `fi/firefox-ios.xliff` — "Shortcut" is rendered as "pikavalinta" on the add tile, but the same section is titled "Oikotiet".
    - Current: `Lisää pikavalinta`
    - Source: `Add Shortcut`
    - Suggest: `Lisää oikotie`
    - The Shortcuts section title and the Shortcuts Library title both use "Oikotiet". The add-shortcut tile sits in that same section, so it should use the same term.
- `Settings.Appearance.NavigationToolbar.SectionHeader.v145` — `fi/firefox-ios.xliff` — The section header calls the toolbar "työkalurivi", but the description directly under it calls it "työkalupalkki".
    - Current: `Työkalurivin painike`
    - Source: `Toolbar Button`
    - Suggest: `Työkalupalkin painike`
    - The header and the description below it both translate "toolbar" on the same Appearance settings section, but they use different Finnish words. Firefox's usual Finnish term is "työkalupalkki", which the description already uses.
- `OpenURL.Error.Message` — `fi/firefox-ios.xliff` — The message uses "sivustoa" (website) for "page", while the alert title uses "Sivua".
    - Current: `Firefox ei voi avata sivustoa`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox ei voi avata sivua`
    - The source says "page" in both the title and the message of the same alert. "Sivusto" means a whole website and doesn't match the title's "Sivua".
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `fi/firefox-ios.xliff` — The Standard protection level is called "Vakio" here but "Tavallinen" in the option label for the same level.
    - Current: `Vakio`
    - Source: `Standard`
    - Suggest: `Tavallinen`
    - Both strings render "Standard" for the same tracking-protection level in the same settings area: the option is "Tavallinen (oletus)" and the status is "Vakio". Using two names for one level is inconsistent.

### E. Typography, punctuation & spacing

- `Settings.Home.Current.Description.v101` — `fi/firefox-ios.xliff` — Missing comma before the subordinate clause introduced by "mitä".
    - Current: `Valitse mitä näytetään`
    - Source: `Choose what displays as the homepage.`
    - Suggest: `Valitse, mitä näytetään`
    - Finnish punctuation requires a comma before a subordinate clause; the same screen uses "Valitse, mitä näet" correctly.
- `Settings.Home.Option.Description.v101` — `fi/firefox-ios.xliff` — Missing comma before the subordinate clause introduced by "mitä".
    - Current: `Valitse mitä Firefoxin`
    - Source: `Choose what’s included on the Firefox homepage.`
    - Suggest: `Valitse, mitä Firefoxin`
    - Finnish punctuation requires a comma before a subordinate clause; inconsistent with "Valitse, mitä näet" on the same screen.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
