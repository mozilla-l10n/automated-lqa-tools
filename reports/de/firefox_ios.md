# Firefox iOS l10n QA — de

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8f5aca68ae4b` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8f5aca68ae4b` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for de: [android](android.md) · [firefox](firefox.md)

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
| quotes | `german-double` 16 | **german-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 8 | **en** |
| register | `informal` 1, `formal` 420 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (88)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `TabToolbar.Accessibility.DataClearance.v122` — `de/firefox-ios.xliff` — "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Source: `Data Clearance`
    - Suggest: `Datenlöschung`
    - The developer comment says the button ends and deletes private session data; "Datenfreigabe" means sharing/releasing data, the opposite impression.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 25 |
| 3 | Degraded language (grammar, spelling, terminology) | 52 |
| 4 | Cosmetic (typography, spacing) | 10 |

### A. Functional, markup, variables & plurals

- `TranslationToastHandler.PromptTranslate.Title` — `de/firefox-ios.xliff` — Reordered numbered placeholders are fine, but %1$@ preceded by "auf" should agree; main issue is the swapped order of %3$@ and %2$@ relative to the source sentence structure.
    - Current: `Mit %3$@ auf %2$@ übersetzen?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Mit %3$@ in %2$@ übersetzen?`
    - "auf %2$@ übersetzen" is wrong preposition for a language name; German uses "ins Deutsche übersetzen" / "in %2$@ übersetzen".

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `de/firefox-ios.xliff` — "record and upload audio" is narrowed to "Sprachaufnahmen" (voice recordings) and reads redundantly.
    - Current: `Firefox verwendet Ihr Mikrofon, um Sprachaufnahmen aufzunehmen und hochzuladen.`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `Firefox verwendet Ihr Mikrofon, um Audioaufnahmen aufzuzeichnen und hochzuladen.`
    - The source refers to audio generally, not specifically speech; "Sprachaufnahmen aufnehmen" is also tautological.
- `Logins.DevicePasscodeRequired.Message.v122` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" (device passphrase) instead of the established term "Gerätecode".
    - Current: `Gerätepasssatz`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Gerätecode`
    - iOS uses "Code" (Gerätecode) for the device passcode; "Passsatz" means passphrase and is not an iOS term.
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" (device passphrase) instead of the established term "Gerätecode".
    - Current: `Gerätepasssatz`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Gerätecode`
    - iOS uses "Code" (Gerätecode) for the device passcode; "Passsatz" means passphrase and is not an iOS term.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `de/firefox-ios.xliff` — "Post town" left untranslated as "Post Town" while all other address field labels are translated.
    - Current: `Post Town`
    - Source: `Post town`
    - Suggest: `Poststadt`
    - The field label should be localized like the surrounding address fields (Stadt, Bezirk, Distrikt); "Post Town" is English.
- `Addresses.EditAddress.AutofillAddressState.v129` — `de/firefox-ios.xliff` — "State" as an administrative subdivision of an address is rendered as "Staat" (sovereign country) instead of "Bundesstaat".
    - Current: `Staat`
    - Source: `State`
    - Suggest: `Bundesstaat`
    - The developer comment says this is the state field within an address, especially in the USA. German "Staat" means country/nation; the address subdivision is "Bundesstaat", and next to the separate country field "Staat" is misleading.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `de/firefox-ios.xliff` — Analytics tracker count is labelled "Tracking-Inhalt" although the source/comment refers to analytics trackers.
    - Current: `Tracking-Inhalt: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Analyse-Tracker: %@`
    - The developer comment says this is the count of analytics trackers; the German "Tracking-Inhalt" (tracking content) names a different category and is inconsistent with the other tracker labels in the same screen.
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `de/firefox-ios.xliff` — "after a page starts loading" is rendered as "nachdem eine Seite geladen wurde" (after a page has loaded).
    - Current: `nachdem eine Seite geladen wurde`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `nachdem eine Seite mit dem Laden begonnen hat`
    - The source says blocking happens after the page starts loading, not after it has finished loading; this contrasts with the strict-mode string which blocks before the page loads.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `de/firefox-ios.xliff` — "blocks more trackers" translated as "blockiert weitere Elemente", meaning "additional elements" rather than a greater number of trackers.
    - Current: `Streng blockiert weitere Elemente zur Aktivitätenverfolgung`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `Streng blockiert mehr Skripte zur Aktivitätenverfolgung`
    - The source compares quantity ("more trackers" than standard mode); "weitere Elemente" reads as "further elements" and also uses a different term ("Elemente") than the parallel standard-mode string ("Skripte").
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `de/firefox-ios.xliff` — "looks broken" mistranslated as "beschädigt aussieht" (looks damaged).
    - Current: `Wenn etwas auf dieser Website beschädigt aussieht`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Wenn auf dieser Website etwas nicht richtig funktioniert`
    - The source means the site appears not to work correctly, not that something looks physically damaged.
- `LiveActivity.Downloads.FileCountText.v138` — `de/firefox-ios.xliff` — "Downloading Files: %@" is rendered as "Aktive Downloads" (Active downloads), losing the "downloading files" meaning.
    - Current: `Aktive Downloads: %@`
    - Source: `Downloading Files: %@`
    - Suggest: `Dateien werden heruntergeladen: %@`
    - The source states files are being downloaded; "Aktive Downloads" says something different (active downloads) and does not mention files.
- `MainMenu.Account.SigningOut.Title.v154` — `de/firefox-ios.xliff` — "Signing out…" (progress in course) is rendered as the imperative/infinitive "Abmelden…", which reads as the action label "Sign out" rather than an ongoing process.
    - Current: `Abmelden…`
    - Source: `Signing out…`
    - Suggest: `Abmeldung läuft…`
    - The developer comment says it is shown transiently while the user is being signed out; the German must express the in-progress state, not the command.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `de/firefox-ios.xliff` — "Save submenu" is rendered as the imperative "Untermenü speichern" (save the submenu) instead of the noun phrase "submenu Save".
    - Current: `Untermenü speichern`
    - Source: `Save submenu`
    - Suggest: `Untermenü „Speichern“`
    - The source is a noun phrase naming the Save submenu (cf. the parallel string "Tools submenu" → "Untermenü „Werkzeuge“"). The German reads as a command to save the submenu, which is a different meaning.
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `de/firefox-ios.xliff` — "Unselected" (state: not selected) is rendered as "Auswahl aufgehoben" (selection removed/deselected), describing an action rather than the state.
    - Current: `Auswahl aufgehoben`
    - Source: `Unselected`
    - Suggest: `Nicht ausgewählt`
    - The developer comment says this accessibility label "states whether the survey option was not selected", i.e. a static state, not an action of deselecting.
- `NativeErrorPage.Wayback.Error.Title.v154` — `de/firefox-ios.xliff` — Adds an "Fehler:" prefix not present in the source "Unable to connect".
    - Current: `Fehler: Verbindung fehlgeschlagen`
    - Source: `Unable to connect`
    - Suggest: `Verbindung fehlgeschlagen`
    - The en-US title is simply "Unable to connect"; the German introduces an extra "Error:" label.
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `de/firefox-ios.xliff` — The German reverses the subject: source says notifications help the user stay safer with Firefox, German says they help the user make Firefox safer.
    - Current: `Benachrichtigungen helfen Ihnen, %@ noch sicherer zu machen`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `Benachrichtigungen helfen Ihnen, mit %@ sicherer zu surfen`
    - en-US: "Notifications help you stay safer with %@" — the user stays safer; the German claims the user makes the app safer.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `de/firefox-ios.xliff` — The source's "all in one place" emphasis is dropped/weakened and rendered simply as "an einem Ort" without "alles".
    - Current: `und Suchmaschinen an einem Ort zu erhalten`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `und Suchmaschinen zu erhalten – alles an einem Ort`
    - en-US reads "– all in one place"; the German omits "all" and the separating dash, changing the emphasis of the sentence.
- `Onboarding.Modern.Sync.Description.v145` — `de/firefox-ios.xliff` — "sync on any device" is mistranslated as "werden mit jedem Gerät synchronisiert" (synced with every device) instead of being available/synced on any device.
    - Current: `Ihre Lesezeichen, Passwörter und mehr werden mit jedem Gerät synchronisiert.`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Ihre Lesezeichen, Passwörter und mehr werden auf allen Geräten synchronisiert.`
    - The source says data syncs on any device; "mit jedem Gerät" states syncing with every device, a different claim.
- `Onboarding.Notification.Title.v120` — `de/firefox-ios.xliff` — "Notifications help you stay safer with %@" is translated as helping to make Firefox safer instead of helping the user stay safer.
    - Current: `Benachrichtigungen helfen Ihnen, %@ noch sicherer zu machen`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `Benachrichtigungen helfen Ihnen, mit %@ noch sicherer zu bleiben`
    - The source says notifications help the user stay safer with Firefox; the German says they help the user make Firefox safer.
- `Onboarding.Sync.Title.v120` — `de/firefox-ios.xliff` — Source says data stays encrypted when switching devices; German turns it into an instruction to encrypt your data.
    - Current: `Verschlüsseln Sie Ihre Daten, wenn Sie geräteübergreifend arbeiten`
    - Source: `Stay encrypted when you hop between devices`
    - Suggest: `Bleiben Sie verschlüsselt, wenn Sie zwischen Geräten wechseln`
    - "Stay encrypted when you hop between devices" describes the app's behaviour; the German asks the user to encrypt their data themselves.
- `Onboarding.Welcome.Description.TreatementA.v120` — `de/firefox-ios.xliff` — "non-profit backed" mistranslated as the browser itself being non-profit.
    - Current: `Unser gemeinnütziger Browser`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Unser von einer gemeinnützigen Organisation unterstützter Browser`
    - The source says the browser is backed by a non-profit, not that the browser is a non-profit.
- `Onboarding.Welcome.Description.v120` — `de/firefox-ios.xliff` — "non-profit backed" mistranslated as the browser itself being non-profit.
    - Current: `Unser gemeinnütziger Browser`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Unser von einer gemeinnützigen Organisation unterstützter Browser`
    - The source says the browser is backed by a non-profit, not that the browser is a non-profit.
- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `de/firefox-ios.xliff` — The celebratory emoji present in the source is dropped from the translation.
    - Current: `%1$@ seit %2$@`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `%1$@ seit %2$@ 🎉`
    - The en-US footer text ends with the 🎉 emoji, which is part of the user-visible string and is missing in German.
- `Settings.AIControls.BlockedInformation.v151` — `de/firefox-ios.xliff` — "Unblock specific features below" is translated as "Block specific features below", reversing the meaning.
    - Current: `Blockieren Sie im Folgenden bestimmte Funktionen.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Heben Sie im Folgenden die Blockierung bestimmter Funktionen auf.`
    - The source says to unblock ('Unblock specific features below'), while the German instructs the user to block them — the opposite instruction.
- `Settings.Browsing.AdBlocker.Description.v155` — `de/firefox-ios.xliff` — "If a site looks broken" is rendered as "beschädigt" (physically damaged) instead of broken/faulty display.
    - Current: `Wenn eine Website beschädigt aussieht`
    - Source: `Reduces ads and ad-related trackers. If a site looks broken, try turning this off.`
    - Suggest: `Wenn eine Website nicht richtig dargestellt wird`
    - 'broken' here means the site does not display/function correctly; 'beschädigt' means damaged and does not convey this.
- `Settings.Summarize.FooterTitle.v142` — `de/firefox-ios.xliff` — "summarize pages" (verb phrase) mistranslated as "Zusammenfassungsseiten" (summary pages).
    - Current: `Bietet Zugriff auf Zusammenfassungsseiten.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Ermöglicht das Zusammenfassen von Seiten.`
    - The source says the setting provides access to summarizing pages, not access to pages of summaries.
- `Settings.Translation.AutoTranslate.Footer.v151` — `de/firefox-ios.xliff` — "top preferred language" rendered without the ranking notion.
    - Current: `in Ihre bevorzugte Sprache`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `in Ihre bevorzugte Hauptsprache`
    - The source specifies the top-ranked language of the preferred languages list; the German loses that distinction.
- `Summarizer.Footnote.Label.v144` — `de/firefox-ios.xliff` — "Summarization can make errors" is weakened to "errors can occur", shifting the statement about the feature.
    - Current: `Beim Zusammenfassen können Fehler auftreten.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Die Zusammenfassung kann Fehler enthalten.`
    - The source states the summarization itself can make errors (i.e. the output may be wrong); the German says errors may occur during the process, which suggests operational failures rather than inaccurate content.
- `TabToolbar.Accessibility.DataClearance.v122` — `de/firefox-ios.xliff` — "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Source: `Data Clearance`
    - Suggest: `Datenlöschung`
    - The developer comment says the button ends and deletes private session data; "Datenfreigabe" means sharing/releasing data, the opposite impression.
- `CloseTabsToast.Title.v113` — `de/firefox-ios.xliff` — "Tabs Closed: %d" rendered as "Geschlossene Tabs: %d" reads as a label for a list rather than a confirmation message.
    - Current: `Geschlossene Tabs: %d`
    - Source: `Tabs Closed: %d`
    - Suggest: `Tabs geschlossen: %d`
    - The popup informs the user how many tabs were just closed, consistent with the sibling string "Tab geschlossen".
- `Upgrade.Welcome.Description.v114` — `de/firefox-ios.xliff` — "Same commitment to people over profits" is translated word-for-word into ungrammatical/meaningless German.
    - Current: `Gleiches Engagement für Menschen über Gewinne.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Das gleiche Engagement: Menschen vor Profit.`
    - The English means putting people ahead of profits; "für Menschen über Gewinne" is not idiomatic German and does not convey that meaning.
- `WebCompatReporter.Preview.Data.PixelDensity.v155` — `de/firefox-ios.xliff` — "pixel density" is rendered as "Pixelgröße" (pixel size), naming a different property.
    - Current: `Pixelgröße Ihres Bildschirms`
    - Source: `Your screen’s pixel density`
    - Suggest: `Pixeldichte Ihres Bildschirms`
    - The source and comment refer to the screen's pixel density (physical pixels per layout point), not pixel size.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `de/firefox-ios.xliff` — In a video/audio context, "Captions" is translated as "Bildunterschriften" (image captions) instead of subtitles/closed captions.
    - Current: `Bildunterschriften fehlen`
    - Source: `Captions are missing`
    - Suggest: `Untertitel fehlen`
    - The developer comment places this under the 'Video or audio does not play' category, where "Captions" means subtitles, not image captions.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `de/firefox-ios.xliff` — "Get custom wallpaper" is translated as "herunterladen" (download), adding a meaning the source does not have.
    - Current: `Benutzerdefiniertes Hintergrundbild herunterladen`
    - Source: `Get custom wallpaper`
    - Suggest: `Benutzerdefiniertes Hintergrundbild erhalten`
    - The source says "Get", not "Download"; the button selects/applies a wallpaper rather than downloading one.
- `WorldCup.HomepageWidget.GroupPhase.RelatedMatchesLabel.v151` — `de/firefox-ios.xliff` — "Related matches" translated as "Verwandte Spiele" (kinship-related), the wrong sense of "related".
    - Current: `Verwandte Spiele`
    - Source: `Related matches`
    - Suggest: `Zugehörige Spiele`
    - In this context "related matches" means the matches associated with the team's group; "verwandt" means related by kinship/similarity and reads wrong for sports fixtures.
- `Menu.ZoomPage.Close.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — "Zoom Panel" rendered as "Zoom-Ansicht" (zoom view) instead of the zoom panel/bar.
    - Current: `Zoom-Ansicht schließen`
    - Source: `Close Zoom Panel`
    - Suggest: `Zoom-Leiste schließen`
    - The source refers to closing the zoom panel (the Zoom Page Bar), not a zoom "view".
- `This action will clear all of your private data, including history from your synced devices.` — `de/firefox-ios.xliff` — "all of your private data" is rendered without "alle", weakening the meaning.
    - Current: `Diese Aktion löscht Ihre persönlichen Daten, einschließlich Chronik von Ihren synchronisierten Geräten.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Diese Aktion löscht alle Ihre persönlichen Daten, einschließlich der Chronik von Ihren synchronisierten Geräten.`
    - The source says "all of your private data"; the German drops "all", unlike the parallel string in ClearPrivateDataConfirm which keeps "alle".
- `Bookmarks.NewBookmark.Label` — `de/firefox-ios.xliff` — "New Bookmark" is rendered as "Lesezeichen hinzufügen" (Add bookmark) instead of "Neues Lesezeichen", inconsistent with the parallel New Folder/New Separator strings.
    - Current: `Lesezeichen hinzufügen`
    - Source: `New Bookmark`
    - Suggest: `Neues Lesezeichen`
    - Source is "New Bookmark", a noun label, translated consistently as "Neuer Ordner"/"Neue Trennlinie" for the sibling strings; "Lesezeichen hinzufügen" means "Add bookmark".
- `Changes color theme.` — `de/firefox-ios.xliff` — "color theme" translated as "Farbeinstellung" (color setting) rather than color theme/scheme.
    - Current: `Ändert Farbeinstellung.`
    - Source: `Changes color theme.`
    - Suggest: `Ändert das Farbschema.`
    - The source refers to the reader-mode color theme; "Farbeinstellung" names a setting, not the theme.
- `FirefoxHome.CustomizeHomeButton.Title` — `de/firefox-ios.xliff` — "Homepage" translated as "Startbildschirm" (home screen) instead of "Startseite".
    - Current: `Startbildschirm anpassen`
    - Source: `Customize Homepage`
    - Suggest: `Startseite anpassen`
    - en-US says "Customize Homepage"; elsewhere "Home Page" is rendered "Startseite" (Firefox.HomePage.Title), so "Startbildschirm" is inconsistent and names a different concept.
- `FxAPush_DeviceConnected_body` — `de/firefox-ios.xliff` — "has connected to" rendered as a state ("ist verbunden") rather than the completed action.
    - Current: `Firefox Sync ist mit %@ verbunden`
    - Source: `Firefox Sync has connected to %@`
    - Suggest: `Firefox Sync hat sich mit %@ verbunden`
    - The source reports the event that Sync connected to the newly connected device; the German states an ongoing state instead.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `de/firefox-ios.xliff` — "Fingerprinters" translated as "Fingerabdrücke" (fingerprints), naming the data instead of the trackers.
    - Current: `Fingerabdrücke erfassen`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `Identifizierer (Fingerprinter) erfassen`
    - The source says fingerprinters (the scripts) collect settings; "Fingerabdrücke" means fingerprints, and it is also inconsistent with Menu.TrackingProtectionFingerprintersBlocked.Title, which uses "Identifizierer (Fingerprinter)".
- `ReopenAlert.Title` — `de/firefox-ios.xliff` — "Reopen" is translated as "wiederherstellen" (restore), inconsistent with "Erneut öffnen" used for the alert's button.
    - Current: `Zuletzt geschlossenen Tab wiederherstellen`
    - Source: `Reopen Last Closed Tab`
    - Suggest: `Zuletzt geschlossenen Tab erneut öffnen`
    - The en-US title is "Reopen Last Closed Tab"; the corresponding action button ReopenAlert.Actions.Reopen is rendered "Erneut öffnen", so the title should use the same term.
- `Settings.Home.Option.Pocket` — `de/firefox-ios.xliff` — "Recommended by Pocket" is rendered with the singular noun "Empfehlung von Pocket" instead of the plural/participle form.
    - Current: `Empfehlung von Pocket`
    - Source: `Recommended by Pocket`
    - Suggest: `Von Pocket empfohlen`
    - The source labels a section of multiple recommendations; the singular noun changes the meaning to a single recommendation.
- `Settings.Home.Option.Wallpaper.Classic.Title.v106` — `de/firefox-ios.xliff` — "Classic %@" is rendered as "%@ klassisch", turning the group title into a predicative phrase instead of "Klassisches <App>".
    - Current: `%@ klassisch`
    - Source: `Classic %@`
    - Suggest: `Klassisch: %@`
    - The source is a noun phrase naming the wallpaper group ("Classic Firefox"); "%@ klassisch" reads as an adjective trailing the app name and is not a valid German title.
- `Settings.Passwords.OnboardingMessage.v103` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" (device passphrase) instead of "Gerätecode"/"Gerätepasscode".
    - Current: `Gerätepasssatz`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `Gerätecode`
    - en-US "device passcode" is the iOS device PIN/passcode; "Passsatz" means passphrase and is not the established iOS term (Apple uses "Code"/"Gerätecode").

### C. Grammar, agreement & spelling

- `Alerts.AddToCalendar.Body.v134` — `de/firefox-ios.xliff` — Wrong preposition/case combination: "einen Termin in Ihrem Kalender hinzufügen" is ungrammatical; should be "zu Ihrem Kalender hinzufügen".
    - Current: `einen Termin in Ihrem Kalender hinzufügen`
    - Source: `%@ is asking to download a file and add an event to your calendar.`
    - Suggest: `einen Termin zu Ihrem Kalender hinzufügen`
    - "hinzufügen" requires "zu" + dative (or "in" + accusative); "in Ihrem Kalender hinzufügen" is wrong, and the parallel string BodyDefault uses "zu Ihrem Kalender hinzufügen".
- `Bookmarks.EmptyState.Root.Body.v135` — `de/firefox-ios.xliff` — Lowercase "sie" used instead of the formal "Sie", and the subordinate clause needs a comma.
    - Current: `Speichern Sie Websites während sie surfen.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `Speichern Sie Websites, während Sie surfen.`
    - The formal address requires capitalized "Sie"; lowercase "sie" means "they/she". German also requires a comma before the subordinate clause "während …" (cf. the parallel string BodySignedOut).
- `Menu.EnhancedTrackingProtection.On.Header.v128` — `de/firefox-ios.xliff` — Wrong pronoun order/case in "sagen wir Ihnen es".
    - Current: `sagen wir Ihnen es`
    - Source: `You’re protected. If we spot something, we’ll let you know.`
    - Suggest: `sagen wir Ihnen Bescheid`
    - German requires the pronoun order "sagen wir es Ihnen"; "sagen wir Ihnen es" is ungrammatical.
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `de/firefox-ios.xliff` — Misspelling of "riskant".
    - Current: `(risikant)`
    - Source: `Proceed to %@ (Risky)`
    - Suggest: `(riskant)`
    - German adjective is "riskant"; "risikant" is not a word.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `de/firefox-ios.xliff` — Missing case agreement in "Ihr Modem oder Router" after "Überprüfen Sie" (accusative required).
    - Current: `Überprüfen Sie Ihr Modem oder Router.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Überprüfen Sie Ihr Modem oder Ihren Router.`
    - "Router" needs the accusative article "Ihren"; as written the phrase is ungrammatical.
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `de/firefox-ios.xliff` — Missing hyphen in the compound with the app-name placeholder.
    - Current: `%@ Onboarding beenden und schließen`
    - Source: `Close and exit %@ onboarding`
    - Suggest: `%@-Onboarding beenden und schließen`
    - German compounds with a proper-name placeholder require a hyphen (cf. "%@-Hintergrundbild" in the same file).
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `de/firefox-ios.xliff` — "gelegentlich gesponserten" should be "gelegentliche gesponserte"; the adverb changes the meaning to "occasionally sponsored".
    - Current: `mit gelegentlich gesponserten Vorschlägen`
    - Source: `Support %@ with occasional sponsored suggestions`
    - Suggest: `mit gelegentlichen gesponserten Vorschlägen`
    - The source means occasional suggestions that are sponsored, not suggestions that are occasionally sponsored.
- `SendTo.NotSignedIn.Title.v119` — `de/firefox-ios.xliff` — Wrong preposition: "mit Ihrem Konto angemeldet" should be "bei Ihrem Konto/in Ihrem Konto angemeldet".
    - Current: `Sie sind nicht mit Ihrem Konto angemeldet.`
    - Source: `You are not signed in to your account.`
    - Suggest: `Sie sind nicht bei Ihrem Konto angemeldet.`
    - German uses "bei einem Konto angemeldet sein"; "mit" is ungrammatical here.
- `WorldCup.HomepageWidget.FollowTeamLabel.v151` — `de/firefox-ios.xliff` — Wrong case: "folgen" governs the dative, so "Team folgen" needs an article or different wording.
    - Current: `Team folgen`
    - Source: `Follow team`
    - Suggest: `Einem Team folgen`
    - German "folgen" takes a dative object; the bare accusative-looking "Team folgen" is ungrammatical, unlike the parallel "Team ändern"/"Team auswählen" which take the accusative.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `de/firefox-ios.xliff` — Wrong plural/case form "andere Inhalten".
    - Current: `und andere Inhalten laden`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `und andere Inhalte laden`
    - Accusative plural of "Inhalt" is "Inhalte"; "Inhalten" is the dative form and ungrammatical here.
- `SendTo.NotSignedIn.Title` — `de/firefox-ios.xliff` — Wrong preposition: "mit Ihrem Firefox-Konto angemeldet" should be "bei Ihrem Firefox-Konto angemeldet".
    - Current: `Sie sind nicht mit Ihrem Firefox-Konto angemeldet.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Sie sind nicht bei Ihrem Firefox-Konto angemeldet.`
    - "You are not signed in to your Firefox Account" — standard German Mozilla wording is "bei ... angemeldet"; "mit ... angemeldet" is not idiomatic.
- `SentTab_TabArrivingNotification_NoDevice_body` — `de/firefox-ios.xliff` — Grammatical agreement errors: "Neuen Tab von andere Gerät" should be nominative "Neuer Tab" and dative "von einem anderen Gerät".
    - Current: `Neuen Tab von andere Gerät erhalten.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Neuer Tab von einem anderen Gerät erhalten.`
    - The en-US "New tab arrived from another device." requires correct case/declension in German; the current text has wrong case on both noun phrases.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `de/firefox-ios.xliff` — Wrong case: "Erlaubt bestimmter Werbung" should be accusative "bestimmte Werbung" (or the dative object of erlauben is the person, not the ad).
    - Current: `Erlaubt bestimmter Werbung („Trackern“), Ihre Aktivitäten zu verfolgen`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Erlaubt bestimmter Werbung („Trackern“) das Verfolgen Ihrer Aktivitäten`
    - The German construction mixes cases; "Erlaubt bestimmter Werbung ..., Ihre Aktivitäten zu verfolgen" is ungrammatical as written.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `de/firefox-ios.xliff` — Wrong case/preposition: "hinzufügen" takes a dative object, not "auf Ihrem Startbildschirm" with this verb pattern.
    - Current: `Fügen Sie Firefox-Verknüpfungen auf Ihrem Startbildschirm hinzu.`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `Fügen Sie Ihrem Startbildschirm Firefox-Verknüpfungen hinzu.`
    - "etwas hinzufügen" requires a dative indirect object (cf. the parallel string TodayWidget.QuickActionGalleryDescription: "Fügen Sie Ihrem Startbildschirm eine Firefox-Verknüpfung hinzu."); "auf Ihrem Startbildschirm hinzufügen" is ungrammatical/inconsistent.

### D. Terminology, register & consistency

- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `de/firefox-ios.xliff` — "Basics" translated as "Standard", colliding with the icon name "Default" already rendered as "Standard" on the same screen.
    - Current: `Standard`
    - Source: `Basics`
    - Suggest: `Grundlagen`
    - On the same screen Settings.AppIconSelection.AppIconNames.Regular.Title.v136 ("Default") is also "Standard", so the section heading and an icon name become indistinguishable; the source distinguishes "Basics" from "Default".
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `de/firefox-ios.xliff` — Header capitalization inconsistent with the parallel MOBILE BOOKMARKS header, which is rendered in all caps.
    - Current: `Desktop-Lesezeichen`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `DESKTOP-LESEZEICHEN`
    - Source is all-caps "DESKTOP BOOKMARKS" and the sibling header "MOBILE BOOKMARKS" was translated as "MOBILE LESEZEICHEN"; the two headers appear side by side on the same screen and must match.
- `NativeErrorPage.BadCertDomain.TitleLabel.v149` — `de/firefox-ios.xliff` — The identical source sentence "Something doesn’t look right." is translated differently here than in NativeErrorPage.GenericError.TitleLabel.v131 ("Irgendetwas stimmt hier nicht.").
    - Current: `Irgendetwas sieht nicht gut aus.`
    - Source: `Be careful. Something doesn’t look right.`
    - Suggest: `Irgendetwas stimmt hier nicht.`
    - Same source string in the same file should use the same wording; "sieht nicht gut aus" also shifts the meaning toward an aesthetic judgement.
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `de/firefox-ios.xliff` — Third line uses the informal address ("Synchronisiere auf allen deinen Geräten") instead of the established formal form.
    - Current: `Synchronisiere auf allen deinen Geräten`
    - Source: `Load sites lightning fast Automatic tracking protection Sync on all your devices`
    - Suggest: `Synchronisieren Sie auf allen Ihren Geräten`
    - The locale convention is formal address (Sie); the other lines of the same screen use formal forms.
- `Onboarding.Modern.Welcome.Title.v145` — `de/firefox-ios.xliff` — "trackers" is rendered as "Verfolgern" instead of the established term "Tracker".
    - Current: `gruseligen Verfolgern`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `gruseligen Trackern`
    - Firefox de uses "Tracker"/"Tracking-Schutz" (see Subtitle.v140 "Tracking-Schutz"); "Verfolger" is inconsistent terminology.
- `Summarizer.Error.MissingPageContent.Message.v142` — `de/firefox-ios.xliff` — "hit summarize" on a touch device is rendered as "klicken Sie" (click) instead of tap.
    - Current: `klicken Sie dann auf Zusammenfassen`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `tippen Sie dann auf Zusammenfassen`
    - This is an iOS touch UI; the rest of the batch uses "tippen/antippen". "Klicken" is desktop terminology and inconsistent with the source's "hit".
- `TermsOfUse.TermsOfUseHasOpened.v142` — `de/firefox-ios.xliff` — UI "sheet" is literally translated as "Blatt" (sheet of paper).
    - Current: `Blatt mit Nutzungsbedingungen geöffnet`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Nutzungsbedingungen geöffnet`
    - "Sheet" here is the iOS bottom-sheet UI element; "Blatt" means a piece of paper and is not the German term for this control.
- `WebCompatReporter.Fields.DetailsPlaceholder.v154` — `de/firefox-ios.xliff` — "(optional)" is rendered as "(freiwillig)" instead of the standard German UI term "(optional)".
    - Current: `(freiwillig)`
    - Source: `Describe the issue in detail (optional)`
    - Suggest: `(optional)`
    - "freiwillig" means voluntary; the established Mozilla German term for "optional" in form fields is "optional".
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `de/firefox-ios.xliff` — "Full time" is rendered as "Reguläre Spielzeit" here but as "Spielende" in the FT labels on the same widget.
    - Current: `Reguläre Spielzeit • Elfmeterschießen (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Spielende • Elfmeterschießen (%@)`
    - The same source term "Full Time" is translated "Spielende" in WorldCup.HomepageWidget.FTLabel and FTNoParenthesisLabel; "Reguläre Spielzeit" (regular playing time) is inconsistent and also inaccurate since the match ended after penalties.
- `Menu.ZoomPage.DecreaseZoom.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — "Zoom Level" translated as "Zoomfaktor" here but as "Zoomstufe" in the sibling string on the same screen.
    - Current: `Zoomfaktor verringern`
    - Source: `Decrease Zoom Level`
    - Suggest: `Zoomstufe verringern`
    - Menu.ZoomPage.CurrentZoomLevel uses "Zoomstufe" for the same source term "Zoom Level"; inconsistent terminology within one feature.
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — "Zoom Level" translated as "Zoomfaktor" here but as "Zoomstufe" in the sibling string on the same screen.
    - Current: `Zoomfaktor erhöhen`
    - Source: `Increase Zoom Level`
    - Suggest: `Zoomstufe erhöhen`
    - Menu.ZoomPage.CurrentZoomLevel uses "Zoomstufe" for the same source term "Zoom Level"; inconsistent terminology within one feature.
- `ActivityStream.ContextMenu.UnpinTopsite` — `de/firefox-ios.xliff` — "Unpin" is rendered as "Ablösen" instead of the established "Lösen"/"Nicht mehr anheften" counterpart to "Anheften".
    - Current: `Ablösen`
    - Source: `Unpin`
    - Suggest: `Nicht mehr anheften`
    - The paired action "Pin" is translated "Anheften"; "Ablösen" (detach/peel off, also 'relieve/replace') is not the standard German opposite and breaks terminology consistency on the same context menu.
- `BreachAlerts.Link` — `de/firefox-ios.xliff` — Informal imperative "Gehe zu" violates the locale's formal register.
    - Current: `Gehe zu`
    - Source: `Go to`
    - Suggest: `Gehen Sie zu`
    - The de locale uses the formal address (Sie) throughout; "Gehe zu" is the informal du-form.
- `DownloadsPanel.Delete.Title` — `de/firefox-ios.xliff` — "Delete" rendered as "Entfernen" (remove) instead of "Löschen".
    - Current: `Entfernen`
    - Source: `Delete`
    - Suggest: `Löschen`
    - The source distinguishes "Delete" (files) from "Remove"; "Entfernen" is the standard German for "Remove" (see FirefoxHome.RecentHistory.Remove), so deleting downloaded files should be "Löschen".
- `Logins.PasscodeRequirement.Warning` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" instead of the established "Gerätecode"/"Gerätepasscode".
    - Current: `Gerätepasssatz`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Gerätecode`
    - A passcode on iOS is the numeric device code ("Gerätecode"); "Passsatz" means passphrase and is not the iOS term, and it is also an awkward misspelling-like form.
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `de/firefox-ios.xliff` — "OPENING SCREEN" is translated as "ÖFFNUNGSBILDSCHIRM", inconsistent with "Startbildschirm" used for the same source term elsewhere.
    - Current: `ÖFFNUNGSBILDSCHIRM`
    - Source: `OPENING SCREEN`
    - Suggest: `STARTBILDSCHIRM`
    - Settings.Home.Option.StartAtHome.Title translates the identical source "Opening screen" as "Startbildschirm"; "Öffnungsbildschirm" is not established German terminology.
- `Tabs.DeleteAllUndo.Button` — `de/firefox-ios.xliff` — "Undo" rendered as "Wiederherstellen" (restore), inconsistent with "Rückgängig" used for the same source term in Toasts.Undo.
    - Current: `Wiederherstellen`
    - Source: `Undo`
    - Suggest: `Rückgängig`
    - Same source term "Undo" is translated as "Rückgängig" elsewhere in the same file; "Wiederherstellen" means "restore/redo".
- `Modified %@` — `de/firefox-ios.xliff` — "Modified" for a last-modified timestamp is rendered as "Verändert" with an added colon instead of the standard "Geändert".
    - Current: `Verändert: %@`
    - Source: `Modified %@`
    - Suggest: `Geändert: %@`
    - The comment says the label describes when the login was last modified; Firefox uses "Geändert" for last-modified, "Verändert" is not the established term.
- `fi3W24-scEmjs` — `de/firefox-ios.xliff` — The menu item ‘New Private Search’ is rendered as „Neue Private Suche“ here but as „Neue private Suche“ in the corresponding menu item string scEmjs.
    - Current: `„Neue Private Suche“`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `„Neue private Suche“`
    - The same quoted UI item must match the menu item label (scEmjs: „Neue private Suche“); also German capitalizes the adjective only if it is part of a proper name.

### E. Typography, punctuation & spacing

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `de/firefox-ios.xliff` — Missing comma before the subordinate clause "während Sie surfen".
    - Current: `Speichern Sie Websites während Sie surfen.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Speichern Sie Websites, während Sie surfen.`
    - German punctuation requires a comma introducing a subordinate clause with "während".
- `Engagement.Notification.Treatment.B.Body.v114` — `de/firefox-ios.xliff` — Sentence-final period from the source is missing, and the comma required before the infinitive clause is absent.
    - Current: `Surfen Sie mit %@ ohne Cookies oder eine Chronik zu speichern`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `Surfen Sie mit %@, ohne Cookies oder eine Chronik zu speichern.`
    - The en-US string ends with a period; German also requires a comma before the "ohne … zu"-infinitive clause.
- `Onboarding.TermsOfService.TermsOfServiceAgreement.v135` — `de/firefox-ios.xliff` — Trailing period added that the source does not have (the link placeholder already carries its own punctuation).
    - Current: `Indem Sie fortfahren, stimmen Sie den %@ zu.`
    - Source: `By continuing, you agree to the %@`
    - Suggest: `Indem Sie fortfahren, stimmen Sie den %@ zu`
    - Source "By continuing, you agree to the %@" ends without a period; the link text (e.g. "Nutzungsbedingungen von %@.") already includes the final period, so this yields a double period.
- `PasswordAutofill.LoginListCellNoUsername.v129` — `de/firefox-ios.xliff` — Capitalized inside parentheses where the source uses lowercase sentence style.
    - Current: `(Kein Benutzername)`
    - Source: `(no username)`
    - Suggest: `(kein Benutzername)`
    - Source is "(no username)" in lowercase; German adjective/determiner should not be capitalized here.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `de/firefox-ios.xliff` — Round phase label is not in all caps unlike the source and the other round phase labels.
    - Current: `Achtelfinale`
    - Source: `ROUND OF 16`
    - Suggest: `ACHTELFINALE`
    - Source is "ROUND OF 16" in caps, and sibling strings (VIERTELFINALE, HALBFINALE, FINALE) are capitalized; this one is not, breaking consistency on the same screen.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `de/firefox-ios.xliff` — Round phase label is not in all caps unlike the source and the other round phase labels.
    - Current: `Runde der letzten 32`
    - Source: `ROUND OF 32`
    - Suggest: `RUNDE DER LETZTEN 32`
    - Source is "ROUND OF 32" in caps and the neighbouring round-phase labels are all caps in German; this one is mixed case.
- `Settings.Studies.Toggle.Link` — `de/firefox-ios.xliff` — Trailing period from the source "Learn More." is missing.
    - Current: `Weitere Informationen`
    - Source: `Learn More.`
    - Suggest: `Weitere Informationen.`
    - The en-US string ends with a period, and the parallel string Settings.SendUsage.Link keeps it.
- `SyncState.Offline.Title` — `de/firefox-ios.xliff` — Trailing period added to a title that has none in the source.
    - Current: `Sync ist offline.`
    - Source: `Sync is offline`
    - Suggest: `Sync ist offline`
    - The en-US title "Sync is offline" has no final punctuation; titles should not add one.
- `Menu.OpenSettingsAction.Title` — `de/firefox-ios.xliff` — The translation contains a stray soft hyphen inside the word "Einstellungen".
    - Current: `Einstel­lungen`
    - Source: `Settings`
    - Suggest: `Einstellungen`
    - A U+00AD soft hyphen has been inserted mid-word; the source is a plain menu label and no hyphenation control is intended.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (2)

- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — fixed 2026-09-07
- `Settings.AppIconSelection.AppIconNames.Sunset.Title.v137` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — fixed 2026-09-07
