# Firefox iOS l10n QA — de

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 1,918 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


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
| quotes | `german-double` 16 | **german-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 8 | **en** |
| register | `informal` 1, `formal` 418 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (76)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 33 |
| 3 | Degraded language (grammar, spelling, terminology) | 34 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSPhotoLibraryAddUsageDescription` — `de/firefox-ios.xliff` — Adds "Ihre" not present in the source "This lets you save photos."
    - Current: `Damit können Sie Ihre Fotos speichern.`
    - Source: `This lets you save photos.`
    - Suggest: `Damit können Sie Fotos speichern.`
    - The source says simply "save photos"; "Ihre Fotos" changes the meaning to saving the user's own photos rather than saving photos to the library.
- `Settings.AppIconSelection.AppIconNames.Fun.Flaming.Title.146` — `de/firefox-ios.xliff` — "Flaming" (adjective describing the flame-outlined fox) is rendered as the noun "Flamme" (flame).
    - Current: `Flamme`
    - Source: `Flaming`
    - Suggest: `Flammend`
    - The source is an adjectival form describing the icon; "Flamme" names an object instead, unlike the sibling entry "Cuddling" which was kept as an activity.
- `Settings.AppIconSelection.AppIconNames.Sunrise.Title.v137` — `de/firefox-ios.xliff` — "Sunrise" is translated as "Sonnenuntergang" (sunset).
    - Current: `Sonnenuntergang`
    - Source: `Sunrise`
    - Suggest: `Sonnenaufgang`
    - en-US "Sunrise" means Sonnenaufgang; the target says the opposite (sunset), and it is swapped with the Sunset entry.
- `Settings.AppIconSelection.AppIconNames.Sunset.Title.v137` — `de/firefox-ios.xliff` — "Sunset" is translated as "Sonnenaufgang" (sunrise).
    - Current: `Sonnenaufgang`
    - Source: `Sunset`
    - Suggest: `Sonnenuntergang`
    - en-US "Sunset" means Sonnenuntergang; the target says the opposite (sunrise), swapped with the Sunrise entry.
- `Addresses.EditAddress.AutofillAddressState.v129` — `de/firefox-ios.xliff` — "State" as an address-form administrative division is rendered as "Staat" (sovereign country) instead of "Bundesstaat".
    - Current: `Staat`
    - Source: `State`
    - Suggest: `Bundesstaat`
    - The developer comment says this is the state field of an address, especially in the USA. German "Staat" means a sovereign state/country and duplicates the Country field; the correct term for a US state in an address form is "Bundesstaat".
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `de/firefox-ios.xliff` — "after a page starts loading" translated as "nachdem eine Seite geladen wurde" (after a page has loaded).
    - Current: `nachdem eine Seite geladen wurde`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `nachdem das Laden einer Seite begonnen hat`
    - The source says blocking happens after loading starts, not after loading has completed; this contrast with strict mode (before the page loads) is lost.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `de/firefox-ios.xliff` — "more trackers" rendered as "weitere Elemente" (additional elements) rather than a greater number of trackers.
    - Current: `Streng blockiert weitere Elemente zur Aktivitätenverfolgung`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `Streng blockiert mehr Skripte zur Aktivitätenverfolgung`
    - The source compares quantity (blocks more trackers than standard); "weitere Elemente" reads as "further elements" and also breaks terminology consistency with the standard-mode string's "Skripte zur Aktivitätenverfolgung".
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `de/firefox-ios.xliff` — "looks broken" mistranslated as "beschädigt aussieht" (physically damaged) instead of not working correctly.
    - Current: `Wenn etwas auf dieser Website beschädigt aussieht, deaktivieren Sie ihn.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Wenn diese Website nicht richtig funktioniert, deaktivieren Sie ihn.`
    - The source means the site may not work properly; "beschädigt aussieht" says something looks damaged, which is not the meaning.
- `MainMenu.Account.SigningOut.Title.v154` — `de/firefox-ios.xliff` — The transient progress message "Signing out…" is rendered as the plain infinitive "Abmelden…", which reads as an action label rather than an ongoing process.
    - Current: `Abmelden…`
    - Source: `Signing out…`
    - Suggest: `Abmeldung läuft…`
    - The developer comment says this is shown transiently while the user is being signed out; the source uses the progressive form. "Abmelden…" is the imperative/infinitive used for the sign-out button, losing the in-progress meaning.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `de/firefox-ios.xliff` — "Save submenu" is translated as a verb phrase ("save the submenu") instead of naming the Save submenu.
    - Current: `Untermenü speichern`
    - Source: `Save submenu`
    - Suggest: `Untermenü „Speichern“`
    - The source names the submenu called "Save"; "Untermenü speichern" reads as the imperative "save the submenu". Compare the parallel string Tools submenu → „Untermenü „Werkzeuge““.
- `NativeErrorPage.Wayback.Error.Title.v154` — `de/firefox-ios.xliff` — Translation adds a "Fehler:" prefix not present in the source title "Unable to connect".
    - Current: `Fehler: Verbindung fehlgeschlagen`
    - Source: `Unable to connect`
    - Suggest: `Verbindung fehlgeschlagen`
    - The en-US title is simply "Unable to connect"; the added "Fehler:" label is extra content.
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `de/firefox-ios.xliff` — The German reverses the meaning: it says notifications make Firefox safer, not that they help the user stay safer with Firefox.
    - Current: `Benachrichtigungen helfen Ihnen, %@ noch sicherer zu machen`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `Benachrichtigungen helfen Ihnen, mit %@ noch sicherer zu sein`
    - Source: "Notifications help you stay safer with %@" — the user stays safer using the app; the translation states the user makes the app safer.
- `Onboarding.Modern.TermsOfService.Description.v145` — `de/firefox-ios.xliff` — The relative clause reverses who trusts whom: the source says the non-profit is trusted, the German says "we have trusted for over 20 years".
    - Current: `Von der gemeinnützigen Organisation %@, der wir seit über 20 Jahren vertrauen`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Von der gemeinnützigen Organisation %@, der seit über 20 Jahren vertraut wird`
    - en-US "Brought to you by the non-profit %@, trusted for over 20 years" means the organization is trusted (by users), not that Mozilla/the app trusts it.
- `Onboarding.Notification.Title.v120` — `de/firefox-ios.xliff` — The German reverses the meaning: it says notifications help make Firefox safer, instead of helping the user stay safer with Firefox.
    - Current: `Benachrichtigungen helfen Ihnen, %@ noch sicherer zu machen`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `Benachrichtigungen helfen Ihnen, mit %@ sicherer zu bleiben`
    - en-US "Notifications help you stay safer with %@" means the user stays safer using the app; the translation states the user makes the app safer.
- `Onboarding.Sync.Title.v120` — `de/firefox-ios.xliff` — "Stay encrypted when you hop between devices" is rendered as an imperative to encrypt one's data, changing the meaning.
    - Current: `Verschlüsseln Sie Ihre Daten, wenn Sie geräteübergreifend arbeiten`
    - Source: `Stay encrypted when you hop between devices`
    - Suggest: `Bleiben Sie verschlüsselt, wenn Sie zwischen Geräten wechseln`
    - The source states the data stays encrypted while switching devices; the German asks the user to encrypt their data.
- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `de/firefox-ios.xliff` — The celebratory emoji present in the source footer text is missing from the translation.
    - Current: `%1$@ seit %2$@`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `%1$@ seit %2$@ 🎉`
    - en-US reads "%1$@ since %2$@ 🎉"; the 🎉 character was dropped in the German string.
- `Settings.AIControls.AIPoweredFeaturesSection.Title.v151` — `de/firefox-ios.xliff` — "AI-POWERED FEATURES" rendered as "KI-BEREITGESTELLTE FUNKTIONEN" ("AI-provided"), which is not the source meaning.
    - Current: `KI-BEREITGESTELLTE FUNKTIONEN`
    - Source: `AI-POWERED FEATURES`
    - Suggest: `FUNKTIONEN MIT KI-UNTERSTÜTZUNG`
    - "AI-powered" means powered/supported by AI, not "provided by AI"; German Firefox uses "KI-gestützt".
- `Settings.AIControls.BlockedInformation.v151` — `de/firefox-ios.xliff` — "Unblock specific features below" is translated as "Blockieren Sie ... bestimmte Funktionen", reversing the meaning.
    - Current: `Blockieren Sie im Folgenden bestimmte Funktionen.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Heben Sie im Folgenden die Blockierung bestimmter Funktionen auf.`
    - The source instructs the user to unblock specific features; the German says to block them, reversing the meaning.
- `Settings.Summarize.FooterTitle.v142` — `de/firefox-ios.xliff` — "summarize pages" (verb + object) mistranslated as the noun "Zusammenfassungsseiten" (summary pages).
    - Current: `Bietet Zugriff auf Zusammenfassungsseiten.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Bietet Zugriff auf das Zusammenfassen von Seiten.`
    - The source means access to the feature that summarizes pages, not access to pages of summaries.
- `Summarizer.Error.MissingPageContent.Message.v142` — `de/firefox-ios.xliff` — "hit summarize" rendered as "klicken Sie" (click) although this is a touch-only phone UI.
    - Current: `klicken Sie dann auf Zusammenfassen`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `tippen Sie dann auf Zusammenfassen`
    - On iOS the interaction is tapping, not clicking; other strings in this file use "tippen/antippen".
- `TabToolbar.Accessibility.DataClearance.v122` — `de/firefox-ios.xliff` — "Data Clearance" (deleting private session data) is mistranslated as "Datenfreigabe" (data sharing/release).
    - Current: `Datenfreigabe`
    - Source: `Data Clearance`
    - Suggest: `Daten löschen`
    - The developer comment says the button ends and deletes private session data; "Datenfreigabe" means sharing/releasing data, the opposite intent.
- `TabTrayOneDayAgoTitle.v140` — `de/firefox-ios.xliff` — "1 Day Ago" is rendered as "1 Tag", dropping the "ago" relation.
    - Current: `1 Tag`
    - Source: `1 Day Ago`
    - Suggest: `Vor 1 Tag`
    - The source is a relative time label ("1 Day Ago"); "1 Tag" only means "1 day".
- `TabTrayOneMonthAgoTitle.v140` — `de/firefox-ios.xliff` — "1 Month Ago" is rendered as "1 Monat", dropping the "ago" relation.
    - Current: `1 Monat`
    - Source: `1 Month Ago`
    - Suggest: `Vor 1 Monat`
    - The source is a relative time label ("1 Month Ago"); "1 Monat" only means "1 month".
- `TabTrayOneWeekAgoTitle.v140` — `de/firefox-ios.xliff` — "1 Week Ago" is rendered as "1 Woche", dropping the "ago" relation.
    - Current: `1 Woche`
    - Source: `1 Week Ago`
    - Suggest: `Vor 1 Woche`
    - The source is a relative time label ("1 Week Ago"); "1 Woche" only means "1 week".
- `TermsOfUse.TermsOfUseHasOpened.v142` — `de/firefox-ios.xliff` — "sheet" (UI panel) is literally translated as "Blatt" (sheet of paper).
    - Current: `Blatt mit Nutzungsbedingungen geöffnet`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Ansicht mit Nutzungsbedingungen geöffnet`
    - In iOS UI terminology "sheet" is a modal panel; "Blatt" means a sheet of paper and misleads VoiceOver users.
- `WebCompatReporter.Preview.Data.PixelDensity.v155` — `de/firefox-ios.xliff` — "Pixel density" is rendered as "Pixelgröße" (pixel size), which is a different concept.
    - Current: `Pixelgröße Ihres Bildschirms`
    - Source: `Your screen’s pixel density`
    - Suggest: `Pixeldichte Ihres Bildschirms`
    - The source says "pixel density" (physical pixels per layout point); "Pixelgröße" means pixel size, not density.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `de/firefox-ios.xliff` — "Captions" in the video/audio context means subtitles, not image captions ("Bildunterschriften").
    - Current: `Bildunterschriften fehlen`
    - Source: `Captions are missing`
    - Suggest: `Untertitel fehlen`
    - The sub-option belongs to the 'Video or audio does not play' category, so "Captions" refers to subtitles/closed captions, not picture captions.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `de/firefox-ios.xliff` — "Get custom wallpaper" is rendered as "herunterladen" (download), adding meaning not in the source.
    - Current: `Benutzerdefiniertes Hintergrundbild herunterladen`
    - Source: `Get custom wallpaper`
    - Suggest: `Benutzerdefiniertes Hintergrundbild holen`
    - The source says "Get", not "Download"; the action selects/applies a wallpaper rather than downloading it.
- `This action will clear all of your private data, including history from your synced devices.` — `de/firefox-ios.xliff` — The word "all" is dropped from the translation.
    - Current: `Diese Aktion löscht Ihre persönlichen Daten`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Diese Aktion löscht alle Ihre persönlichen Daten`
    - en-US says "will clear all of your private data"; the German omits "alle", weakening the warning.
- `Bookmarks.NewBookmark.Label` — `de/firefox-ios.xliff` — "New Bookmark" translated as "Lesezeichen hinzufügen" (Add bookmark) instead of "Neues Lesezeichen".
    - Current: `Lesezeichen hinzufügen`
    - Source: `New Bookmark`
    - Suggest: `Neues Lesezeichen`
    - The source says "New Bookmark", parallel to "New Folder"/"Neuer Ordner" and "New Separator"/"Neue Trennlinie" in the same group; the German deviates from the source wording and from the group's pattern.
- `DownloadsPanel.Delete.Title` — `de/firefox-ios.xliff` — "Delete" is translated as "Entfernen" (Remove), conflicting with the separate "Remove" string translated identically.
    - Current: `Entfernen`
    - Source: `Delete`
    - Suggest: `Löschen`
    - en-US "Delete" means Löschen; "Entfernen" is the translation used for "Remove" (FirefoxHome.RecentHistory.Remove), creating a terminology mismatch and wrong meaning for deleting downloaded files.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `de/firefox-ios.xliff` — "Fingerprinters" rendered as "Fingerabdrücke" (fingerprints), which names the data rather than the tracking scripts.
    - Current: `Fingerabdrücke erfassen`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `Identifizierer (Fingerprinter) erfassen`
    - The source refers to fingerprinters (the scripts that collect settings), and the related string Menu.TrackingProtectionFingerprintersBlocked.Title uses "Identifizierer (Fingerprinter)"; "Fingerabdrücke" is inconsistent and factually wrong as the actor of "erfassen".
- `Settings.Passwords.OnboardingMessage.v103` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz", which is not a German word and means "device pass-phrase/set".
    - Current: `Gerätepasssatz`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `Gerätecode`
    - The en-US "device passcode" refers to the iOS device passcode; the standard German term is "Gerätecode" (or "Gerätepasscode"). "Passsatz" is not an existing term.
- `Settings.Sync.SigningOut.Title.v154` — `de/firefox-ios.xliff` — "Signing out…" (ongoing process) is rendered as the imperative/infinitive "Abmelden…" instead of a progress phrase.
    - Current: `Abmelden…`
    - Source: `Signing out…`
    - Suggest: `Wird abgemeldet…`
    - The developer comment says the text is shown transiently while the user is being signed out; "Abmelden…" reads as an action button label, not a status.

### C. Grammar, agreement & spelling

- `Alerts.AddToCalendar.Body.v134` — `de/firefox-ios.xliff` — Wrong preposition/case: "in Ihrem Kalender hinzufügen" should be "zu Ihrem Kalender hinzufügen".
    - Current: `einen Termin in Ihrem Kalender hinzuzufügen`
    - Source: `%@ is asking to download a file and add an event to your calendar.`
    - Suggest: `einen Termin zu Ihrem Kalender hinzuzufügen`
    - "hinzufügen" takes "zu" + dative (or "in" + accusative); "in Ihrem Kalender hinzufügen" is ungrammatical, and the parallel string BodyDefault correctly uses "zu Ihrem Kalender hinzufügen".
- `Settings.AppIconSelection.AppIconNames.SystemAuto.Title.v139` — `de/firefox-ios.xliff` — "Systemtheme" is a misleading compound; the established German term is "Systemdesign" or "System-Theme".
    - Current: `Systemtheme`
    - Source: `System Theme`
    - Suggest: `Systemdesign`
    - "Systemtheme" reads as an unrecognizable German word (and can be misread as "System-Theme" vs "Thema"); Mozilla German uses "Design" for "Theme".
- `Bookmarks.EmptyState.Root.Body.v135` — `de/firefox-ios.xliff` — Polite form "Sie" is written lowercase as "sie", and the subordinate clause lacks a comma.
    - Current: `Speichern Sie Websites während sie surfen.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `Speichern Sie Websites, während Sie surfen.`
    - The address form is the polite "Sie" (as in the parallel string BodySignedOut), which must be capitalized; German also requires a comma before the subordinate clause "während".
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `de/firefox-ios.xliff` — "Post town" left in English with incorrect German capitalization instead of being translated.
    - Current: `Post Town`
    - Source: `Post town`
    - Suggest: `Poststadt`
    - The English term is untranslated and, as a two-word English phrase, the mid-word capitalization is not German orthography; other address labels in this file are translated.
- `Menu.EnhancedTrackingProtection.On.Header.v128` — `de/firefox-ios.xliff` — Ungrammatical word order/pronoun use in "sagen wir Ihnen es".
    - Current: `Wenn wir etwas entdecken, sagen wir Ihnen es.`
    - Source: `You’re protected. If we spot something, we’ll let you know.`
    - Suggest: `Wenn wir etwas entdecken, sagen wir es Ihnen.`
    - In German the accusative pronoun "es" precedes the dative "Ihnen"; "sagen wir Ihnen es" is grammatically incorrect.
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `de/firefox-ios.xliff` — "risikant" is a misspelling of German "riskant".
    - Current: `(risikant)`
    - Source: `Proceed to %@ (Risky)`
    - Suggest: `(riskant)`
    - The correct German adjective for "risky" is "riskant"; "risikant" is not a valid spelling.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `de/firefox-ios.xliff` — Missing article/case agreement in "Ihr Modem oder Router".
    - Current: `Überprüfen Sie Ihr Modem oder Router.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Überprüfen Sie Ihr Modem oder Ihren Router.`
    - "Router" is masculine and requires the accusative "Ihren Router"; sharing the neuter "Ihr" is ungrammatical.
- `Onboarding.Modern.Welcome.Description.v140` — `de/firefox-ios.xliff` — Pronoun "ihn" does not agree with the feminine antecedent "Entscheidung".
    - Current: `Sie können ihn später jederzeit ändern.`
    - Source: `One choice protects you everywhere you go on the web. You can always change it later.`
    - Suggest: `Sie können sie später jederzeit ändern.`
    - "it" refers to the choice ("Entscheidung", feminine), so the pronoun must be "sie", not masculine "ihn".
- `Onboarding.Modern.Welcome.Description.v145` — `de/firefox-ios.xliff` — Pronoun "ihn" does not agree with the feminine antecedent "Entscheidung".
    - Current: `Sie können ihn später jederzeit ändern.`
    - Source: `One choice protects you everywhere you go on the web. You can always change it later.`
    - Suggest: `Sie können sie später jederzeit ändern.`
    - "it" refers to the choice ("Entscheidung", feminine), so the pronoun must be "sie", not masculine "ihn".
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `de/firefox-ios.xliff` — "gelegentlich gesponserten" misplaces the adverb; source says occasional sponsored suggestions.
    - Current: `mit gelegentlich gesponserten Vorschlägen`
    - Source: `Support %@ with occasional sponsored suggestions`
    - Suggest: `mit gelegentlichen gesponserten Vorschlägen`
    - "occasional" modifies the suggestions, not the degree of sponsorship; German adverb form changes the meaning to "occasionally sponsored".
- `SendTo.NotSignedIn.Title.v119` — `de/firefox-ios.xliff` — Wrong preposition: "mit Ihrem Konto angemeldet" should be "bei Ihrem Konto/in Ihrem Konto angemeldet".
    - Current: `Sie sind nicht mit Ihrem Konto angemeldet.`
    - Source: `You are not signed in to your account.`
    - Suggest: `Sie sind nicht bei Ihrem Konto angemeldet.`
    - German uses "bei/in einem Konto angemeldet sein" for "signed in to your account"; "mit ... angemeldet" is ungrammatical collocation.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `de/firefox-ios.xliff` — Ungrammatical infinitive clause: "Erneut versuchen, um Webseite zusammenzufassen" misuses the purpose clause.
    - Current: `Erneut versuchen, um Webseite zusammenzufassen`
    - Source: `Retry to summarize web page`
    - Suggest: `Erneut versuchen, die Webseite zusammenzufassen`
    - The source means retrying the action of summarizing, not doing something in order to summarize; also the article before "Webseite" is missing.
- `TermsOfUse.Title.v142` — `de/firefox-ios.xliff` — "Wir haben ein Update" is an incomplete/awkward rendering of "We’ve got an update".
    - Current: `Wir haben ein Update`
    - Source: `We’ve got an update`
    - Suggest: `Es gibt eine Neuigkeit`
    - The German literal phrase reads as unfinished ("Wir haben ein Update" without context) and does not convey the announcement of an update.
- `Upgrade.Welcome.Description.v114` — `de/firefox-ios.xliff` — "Engagement für Menschen über Gewinne" is an ungrammatical literal rendering of "commitment to people over profits".
    - Current: `Gleiches Engagement für Menschen über Gewinne.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Gleicher Einsatz für Menschen statt für Profit.`
    - German "für … über …" does not express the English "people over profits" comparison and reads as broken grammar.
- `WorldCup.HomepageWidget.FollowTeamLabel.v151` — `de/firefox-ios.xliff` — "Team folgen" uses the wrong case; "folgen" governs the dative, so it must be "Einem Team folgen" or "Team verfolgen".
    - Current: `Team folgen`
    - Source: `Follow team`
    - Suggest: `Einem Team folgen`
    - German "folgen" requires a dative object; the bare accusative-looking "Team folgen" is ungrammatical, and the parallel string uses "Team ändern" (transitive) correctly.
- `Logins.PasscodeRequirement.Warning` — `de/firefox-ios.xliff` — "Gerätepasssatz" is not a German word; the standard term for device passcode is "Gerätecode".
    - Current: `Gerätepasssatz`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Gerätecode`
    - The source says "device passcode"; "Passsatz" (passphrase) is both a misrendering and a nonstandard/incorrect compound for iOS's passcode.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `de/firefox-ios.xliff` — Wrong adjective/noun agreement: "andere Inhalten" should be "andere Inhalte".
    - Current: `andere Inhalten laden`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `andere Inhalte laden`
    - Accusative plural of "Inhalt" is "Inhalte"; "Inhalten" is dative plural and does not agree with "andere" as object of "laden".
- `SendTo.NotSignedIn.Title` — `de/firefox-ios.xliff` — Wrong preposition: "mit Ihrem Firefox-Konto angemeldet" should be "bei/in Ihrem Firefox-Konto angemeldet".
    - Current: `Sie sind nicht mit Ihrem Firefox-Konto angemeldet.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Sie sind nicht in Ihrem Firefox-Konto angemeldet.`
    - en-US "You are not signed in to your Firefox Account"; German Mozilla terminology uses "in Ihrem Firefox-Konto angemeldet" (or "bei"), not "mit".
- `SentTab_TabArrivingNotification_NoDevice_body` — `de/firefox-ios.xliff` — Grammatical agreement error: "von andere Gerät" is ungrammatical and the case of "Neuen Tab" is wrong.
    - Current: `Neuen Tab von andere Gerät erhalten.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Neuer Tab von einem anderen Gerät erhalten.`
    - The German requires dative after "von" ("von einem anderen Gerät"), and the subject of the notification should be nominative "Neuer Tab", matching the en-US "New tab arrived from another device."
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `de/firefox-ios.xliff` — Wrong case/agreement: "Erlaubt bestimmter Werbung" should use accusative "bestimmte Werbung".
    - Current: `Erlaubt bestimmter Werbung („Trackern“), Ihre Aktivitäten zu verfolgen`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Erlaubt bestimmter Werbung („Trackern“) das Verfolgen Ihrer Aktivitäten`
    - "erlauben" takes a dative for the person allowed and an accusative object; "Erlaubt bestimmter Werbung ... zu verfolgen" mixes constructions ungrammatically.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `de/firefox-ios.xliff` — Wrong case/preposition with "hinzufügen": should be dative "zu Ihrem Startbildschirm".
    - Current: `Fügen Sie Firefox-Verknüpfungen auf Ihrem Startbildschirm hinzu.`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `Fügen Sie Firefox-Verknüpfungen zu Ihrem Startbildschirm hinzu.`
    - German "hinzufügen" takes "zu" + dative; "auf ... hinzufügen" is ungrammatical for "Add ... to your Home screen".

### D. Terminology, register & consistency

- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `de/firefox-ios.xliff` — Section heading "Basics" is rendered "Standard", colliding with the icon name "Default" already translated as "Standard".
    - Current: `Standard`
    - Source: `Basics`
    - Suggest: `Grundlagen`
    - "Basics" is a section grouping; using "Standard" duplicates the translation of the "Default" icon name on the same screen and is ambiguous.
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `de/firefox-ios.xliff` — Header is not in all caps, unlike the parallel MOBILE BOOKMARKS header on the same screen.
    - Current: `Desktop-Lesezeichen`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `DESKTOP-LESEZEICHEN`
    - The source is "DESKTOP BOOKMARKS" in all caps and the sibling header Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154 is translated as "MOBILE LESEZEICHEN"; the two headers appear together and are inconsistent.
- `Logins.DevicePasscodeRequired.Message.v122` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" (passphrase) instead of the established "Gerätecode".
    - Current: `Gerätepasssatz`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Gerätecode`
    - iOS calls it "Code"/"Gerätecode"; "Passsatz" means passphrase and is not the device passcode.
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `de/firefox-ios.xliff` — "device passcode" is rendered as "Gerätepasssatz" (passphrase) instead of the established "Gerätecode".
    - Current: `Gerätepasssatz`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Gerätecode`
    - iOS calls it "Code"/"Gerätecode"; "Passsatz" means passphrase and is not the device passcode.
- `Settings.Home.Option.TopStories.v143` — `de/firefox-ios.xliff` — "Stories" is translated inconsistently as "Meldungen" here but "Geschichten" in the neighbouring options on the same settings screen.
    - Current: `Meistgelesene Meldungen`
    - Source: `Top Stories`
    - Suggest: `Top-Geschichten`
    - Settings.Home.Option.Stories.v140 uses "Geschichten" for the same source term on the same screen; "Meistgelesene Meldungen" also adds a "most read" meaning not in "Top Stories".
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `de/firefox-ios.xliff` — Third line uses informal "du" address, inconsistent with the formal "Sie" used throughout the onboarding strings.
    - Current: `Synchronisiere auf allen deinen Geräten`
    - Source: `Load sites lightning fast Automatic tracking protection Sync on all your devices`
    - Suggest: `Synchronisieren Sie auf allen Ihren Geräten`
    - German Firefox uses the formal "Sie" form, as in the neighbouring lines and other onboarding strings.
- `Settings.Search.GoogleLens.Description.v153` — `de/firefox-ios.xliff` — "images" is rendered as "Grafiken" (graphics) instead of "Bilder".
    - Current: `Grafiken zur Suche an Google senden.`
    - Source: `Send images to Google to search.`
    - Suggest: `Bilder zur Suche an Google senden.`
    - The en-US source says "Send images to Google to search."; Google Lens deals with photos/images (Bilder), not graphics (Grafiken).
- `WebCompatReporter.Fields.DetailsPlaceholder.v154` — `de/firefox-ios.xliff` — "(optional)" is rendered as "(freiwillig)" instead of the standard German UI term "(optional)".
    - Current: `(freiwillig)`
    - Source: `Describe the issue in detail (optional)`
    - Suggest: `(optional)`
    - "freiwillig" means "voluntary"; the established Firefox German term for form fields marked "optional" is "optional".
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `de/firefox-ios.xliff` — "Full time" is rendered as "Reguläre Spielzeit" here but as "Spielende" in the other full-time strings on the same widget.
    - Current: `Reguläre Spielzeit • Elfmeterschießen (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Spielende • Elfmeterschießen (%@)`
    - WorldCup.HomepageWidget.FTLabel and FTNoParenthesisLabel translate the same source term "Full Time" as "Spielende"; the inconsistent term appears in the same widget.
- `ActivityStream.ContextMenu.UnpinTopsite` — `de/firefox-ios.xliff` — "Unpin" is rendered as "Ablösen" instead of the established counterpart to "Anheften".
    - Current: `Ablösen`
    - Source: `Unpin`
    - Suggest: `Lösen`
    - The paired action is "Pin" = "Anheften"; Firefox uses "Lösen" (or "Nicht mehr anheften") for Unpin. "Ablösen" means detach/peel off and is inconsistent terminology on the same screen.
- `BreachAlerts.Link` — `de/firefox-ios.xliff` — Informal imperative "Gehe zu" violates the formal register used throughout the German Firefox UI.
    - Current: `Gehe zu`
    - Source: `Go to`
    - Suggest: `Gehen Sie zu`
    - German Firefox consistently uses the formal "Sie" address (see the sibling string BreachAlerts.Description: "melden Sie sich ... an"); the du-imperative is inconsistent with the locale's register.
- `Settings.TrackingProtectionOption.NormalBrowsingLabelOn` — `de/firefox-ios.xliff` — "Enhanced Tracking Protection" is translated as "Verbesserter Tracking-Schutz" while other strings on the same screen use "erweiterter Tracking-Schutz".
    - Current: `Verbesserter Tracking-Schutz`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Erweiterter Tracking-Schutz`
    - Same source term rendered inconsistently within the same feature group (see Settings.TrackingProtection.Alert.Description and ProtectionLevel.Footer).
- `fi3W24-scEmjs` — `de/firefox-ios.xliff` — The menu item ‘New Private Search’ is rendered as „Neue Private Suche“ here but as „Neue private Suche“ in the corresponding menu item string scEmjs.
    - Current: `„Neue Private Suche“`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `„Neue private Suche“`
    - The same quoted UI item must match the menu item label (scEmjs: „Neue private Suche“); also German capitalizes the adjective only if it is part of a proper name.

### E. Typography, punctuation & spacing

- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `de/firefox-ios.xliff` — Missing comma before the subordinate clause introduced by "während".
    - Current: `Speichern Sie Websites während Sie surfen.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Speichern Sie Websites, während Sie surfen.`
    - German punctuation requires a comma separating the subordinate clause.
- `Engagement.Notification.Treatment.B.Body.v114` — `de/firefox-ios.xliff` — Missing sentence-final period and missing comma before the infinitive clause.
    - Current: `Surfen Sie mit %@ ohne Cookies oder eine Chronik zu speichern`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `Surfen Sie mit %@, ohne Cookies oder eine Chronik zu speichern.`
    - The en-US source ends with a period, and German requires a comma before the "ohne … zu" infinitive clause.
- `Onboarding.Modern.TermsOfService.TermsOfUseLink.v145` — `de/firefox-ios.xliff` — The trailing period present in the source link text is missing.
    - Current: `Nutzungsbedingungen von %@`
    - Source: `%@ Terms of Use.`
    - Suggest: `Nutzungsbedingungen von %@.`
    - Source is "%@ Terms of Use." with a final period, which completes the surrounding agreement sentence.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `de/firefox-ios.xliff` — Round phase label is not in all caps, unlike the source and the sibling round-phase labels.
    - Current: `Achtelfinale`
    - Source: `ROUND OF 16`
    - Suggest: `ACHTELFINALE`
    - Source is "ROUND OF 16" in all caps and all other round-phase labels (VIERTELFINALE, HALBFINALE, FINALE) are capitalized in German; this one breaks the pattern.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `de/firefox-ios.xliff` — Round phase label is not in all caps, unlike the source and sibling round-phase labels.
    - Current: `Runde der letzten 32`
    - Source: `ROUND OF 32`
    - Suggest: `RUNDE DER LETZTEN 32`
    - Source "ROUND OF 32" is all caps and the other round-phase labels in this file are rendered in all caps in German.
- `Sync.SyncingEllipsis.Label` — `de/firefox-ios.xliff` — Missing space before the ellipsis per German typography.
    - Current: `Synchronisation läuft…`
    - Source: `Syncing…`
    - Suggest: `Synchronisation läuft …`
    - German convention (and Mozilla de style) puts a space before an ellipsis that follows a complete word.
- `SyncState.Offline.Title` — `de/firefox-ios.xliff` — Trailing period added to a title that has none in the source.
    - Current: `Sync ist offline.`
    - Source: `Sync is offline`
    - Suggest: `Sync ist offline`
    - The en-US title "Sync is offline" has no final punctuation; titles should not add one.
- `Menu.OpenSettingsAction.Title` — `de/firefox-ios.xliff` — The translation contains a soft-hyphen character inside "Einstellungen".
    - Current: `Einstel­lungen`
    - Source: `Settings`
    - Suggest: `Einstellungen`
    - An invisible soft hyphen (U+00AD) was inserted in the middle of the word; it does not belong in a menu label and can break search/display.

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

### Fixed to date (0)

_Nothing fixed yet._
