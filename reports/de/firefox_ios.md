# Firefox iOS l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a6af93c85149` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a6af93c85149` |
| **Previous run** | 2026-11-09 @ `62ca1adeb53c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,983 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Strings | 1,983 |
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
| ellipsis | `char` 31 | **char** |
| dash | `en` 8 | **en** |
| register | `formal` 479 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (39)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 4 |

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
- `NativeErrorPage.GenericError.Description.v158.withoutURL` — `de/firefox-ios.xliff` — "couldn’t reach the requested URL" rendered as "couldn't access the requested URL".
    - Current: `konnte nicht auf die angeforderte URL zugreifen`
    - Source: `%1$@ couldn’t reach the requested URL.`
    - Suggest: `konnte die angeforderte URL nicht erreichen`
    - The source says the app could not reach (connect to) the URL; "zugreifen" means access, shifting the meaning from a connection failure to an access/permission problem.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `de/firefox-ios.xliff` — The source's "all in one place" emphasis is dropped/weakened and rendered simply as "an einem Ort" without "alles".
    - Current: `und Suchmaschinen an einem Ort zu erhalten`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `und Suchmaschinen zu erhalten – alles an einem Ort`
    - en-US reads "– all in one place"; the German omits "all" and the separating dash, changing the emphasis of the sentence.
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
- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `de/firefox-ios.xliff` — The celebratory emoji present in the source is dropped from the translation.
    - Current: `%1$@ seit %2$@`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `%1$@ seit %2$@ 🎉`
    - The en-US footer text ends with the 🎉 emoji, which is part of the user-visible string and is missing in German.
- `QuickAnswers.Settings.Footer.v158` — `de/firefox-ios.xliff` — Plural "get short answers" is rendered as singular "erhalten Sie eine kurze Antwort".
    - Current: `Stellen Sie Ihre Frage einfach laut und erhalten Sie eine kurze Antwort.`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `Stellen Sie Ihre Fragen einfach laut und erhalten Sie kurze Antworten.`
    - The en-US settings footer says "Ask out loud and get short answers" (plural, describing repeated use), while the German limits it to one question and one answer.
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
- `Menu.ZoomPage.Close.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — "Zoom Panel" rendered as "Zoom-Ansicht" (zoom view) instead of the zoom panel/bar.
    - Current: `Zoom-Ansicht schließen`
    - Source: `Close Zoom Panel`
    - Suggest: `Zoom-Leiste schließen`
    - The source refers to closing the zoom panel (the Zoom Page Bar), not a zoom "view".
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
- `ReopenAlert.Title` — `de/firefox-ios.xliff` — "Reopen" is translated as "wiederherstellen" (restore), inconsistent with "Erneut öffnen" used for the alert's button.
    - Current: `Zuletzt geschlossenen Tab wiederherstellen`
    - Source: `Reopen Last Closed Tab`
    - Suggest: `Zuletzt geschlossenen Tab erneut öffnen`
    - The en-US title is "Reopen Last Closed Tab"; the corresponding action button ReopenAlert.Actions.Reopen is rendered "Erneut öffnen", so the title should use the same term.
- `Settings.Home.Option.Wallpaper.Classic.Title.v106` — `de/firefox-ios.xliff` — "Classic %@" is rendered as "%@ klassisch", turning the group title into a predicative phrase instead of "Klassisches <App>".
    - Current: `%@ klassisch`
    - Source: `Classic %@`
    - Suggest: `Klassisch: %@`
    - The source is a noun phrase naming the wallpaper group ("Classic Firefox"); "%@ klassisch" reads as an adjective trailing the app name and is not a valid German title.

### C. Grammar, agreement & spelling

- `Menu.EnhancedTrackingProtection.On.Header.v128` — `de/firefox-ios.xliff` — Wrong pronoun order/case in "sagen wir Ihnen es".
    - Current: `sagen wir Ihnen es`
    - Source: `You’re protected. If we spot something, we’ll let you know.`
    - Suggest: `sagen wir Ihnen Bescheid`
    - German requires the pronoun order "sagen wir es Ihnen"; "sagen wir Ihnen es" is ungrammatical.
- `SendTo.NotSignedIn.Title` — `de/firefox-ios.xliff` — Wrong preposition: "mit Ihrem Firefox-Konto angemeldet" should be "bei Ihrem Firefox-Konto angemeldet".
    - Current: `Sie sind nicht mit Ihrem Firefox-Konto angemeldet.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Sie sind nicht bei Ihrem Firefox-Konto angemeldet.`
    - "You are not signed in to your Firefox Account" — standard German Mozilla wording is "bei ... angemeldet"; "mit ... angemeldet" is not idiomatic.
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

### E. Typography, punctuation & spacing

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
- `Settings.Studies.Toggle.Link` — `de/firefox-ios.xliff` — Trailing period from the source "Learn More." is missing.
    - Current: `Weitere Informationen`
    - Source: `Learn More.`
    - Suggest: `Weitere Informationen.`
    - The en-US string ends with a period, and the parallel string Settings.SendUsage.Link keeps it.
- `Menu.OpenSettingsAction.Title` — `de/firefox-ios.xliff` — The translation contains a stray soft hyphen inside the word "Einstellungen".
    - Current: `Einstel­lungen`
    - Source: `Settings`
    - Suggest: `Einstellungen`
    - A U+00AD soft hyphen has been inserted mid-word; the source is a plain menu label and no hyphenation control is intended.

---

## 4. Appendix

### Dismissed by hand (5)

- `Bookmarks.NewBookmark.Label` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>We use „Lesezeichen hinzufügen“ everywhere else, as far as I can tell.</p>
- `NativeErrorPage.BadCertDomain.TitleLabel.v149` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; likely reason (inferred): The original was probably already acceptable: "sieht nicht gut aus" is a correct and closer rendering of "doesn't look right", and the wording difference from a separate generic-error string is a style variation, not an error.
- `PasswordAutofill.LoginListCellNoUsername.v129` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>I prefer this with a capital letter.</p>
- `Settings.Home.Option.Pocket` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>I prefer the noun here.</p>
- `fi3W24-scEmjs` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>„Private Suche“ is a name, so capital letters are ok.</p>

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (3)

- `CloseTabsToast.Title.v113` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string a35856b3): "Geschlossene Tabs: %d" is correct, natural German that conveys the number of tabs closed; no meaning is lost.
- `SendTo.NotSignedIn.Title.v119` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string bbad985c): "mit Ihrem Konto angemeldet" is idiomatic German (cf. "Angemeldet mit Ihrem Google-Konto"); mit is not ungrammatical.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string 44e07fd5): "jemandem erlauben, etwas zu tun" takes a dative object, and "bestimmter Werbung" is the correct feminine dative, so the sentence is grammatical.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/de/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (42)

- `Alerts.AddToCalendar.Body.v134` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Bookmarks.EmptyState.Root.Body.v135` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Logins.DevicePasscodeRequired.Message.v122` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `NativeErrorPage.NoInternetConnection.Description.v131` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `NativeErrorPage.Wayback.Error.Title.v154` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Modern.Sync.Description.v145` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Modern.Welcome.Title.v145` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.MultiDay.SyncCard.BodyText.v159` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Welcome.Description.TreatementA.v120` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Onboarding.Welcome.Description.v120` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `QuickAnswers.ContentView.Answering.v158` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `QuickAnswers.ContentView.ResultHeader.v160` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.AIControls.BlockedInformation.v151` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.Browsing.AdBlocker.Description.v155` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.Summarize.FooterTitle.v142` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Summarizer.Error.MissingPageContent.Message.v142` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `TabToolbar.Accessibility.DataClearance.v122` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Upgrade.Welcome.Description.v114` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `WebCompatReporter.Preview.Data.PixelDensity.v155` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Menu.ZoomPage.DecreaseZoom.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Menu.ZoomPage.IncreaseZoom.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `This action will clear all of your private data, including history from your synced devices.` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Logins.PasscodeRequirement.Warning` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Menu.TrackingProtectionDescription.ContentTrackers` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Menu.TrackingProtectionDescription.Fingerprinters` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `SentTab_TabArrivingNotification_NoDevice_body` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Settings.Passwords.OnboardingMessage.v103` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `SyncState.Offline.Title` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Tabs.DeleteAllUndo.Button` — `de/firefox-ios.xliff` — fixed 2026-11-03
- `Modified %@` — `de/firefox-ios.xliff` — fixed 2026-11-03
