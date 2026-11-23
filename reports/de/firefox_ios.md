# Firefox iOS l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3a2fd7dbacf7` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `3a2fd7dbacf7` |
| **Previous run** | 2026-11-16 @ `3575a882abe1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 11 of 1,993 |

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
| Files | 99 |
| Strings | 1,993 |
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
| quotes | `german-double` 17 | **german-double** |
| ellipsis | `char` 31 | **char** |
| dash | `en` 8 | **en** |
| register | `formal` 483 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (3)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `de/firefox-ios.xliff` — "record and upload audio" is narrowed to "Sprachaufnahmen" (voice recordings) and reads redundantly.
    - Current: `Firefox verwendet Ihr Mikrofon, um Sprachaufnahmen aufzunehmen und hochzuladen.`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `Firefox verwendet Ihr Mikrofon, um Audioaufnahmen aufzuzeichnen und hochzuladen.`
    - The source refers to audio generally, not specifically speech; "Sprachaufnahmen aufnehmen" is also tautological.
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

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (7)

- `Bookmarks.NewBookmark.Label` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>We use „Lesezeichen hinzufügen“ everywhere else, as far as I can tell.</p>
- `MainMenu.Account.SigningOut.Title.v154` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-09): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>Process is signified by the …, that should suffice.</p>
- `NativeErrorPage.BadCertDomain.TitleLabel.v149` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; likely reason (inferred): The original was probably already acceptable: "sieht nicht gut aus" is a correct and closer rendering of "doesn't look right", and the wording difference from a separate generic-error string is a style variation, not an error.
- `PasswordAutofill.LoginListCellNoUsername.v129` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>I prefer this with a capital letter.</p>
- `Settings.Home.Option.Pocket` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>I prefer the noun here.</p>
- `Settings.Studies.Toggle.Link` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-09): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>No complete sentence imho, therefore no full stop,</p>
- `fi3W24-scEmjs` — `de/firefox-ios.xliff` — pontoon-rejected (2026-11-02): rejected in Pontoon: k0V4UFt5TWwQnn4xMvAosRkgFS0: <p>„Private Suche“ is a name, so capital letters are ok.</p>

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (26)

- `ActivityStream.ContextMenu.UnpinTopsite` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 5cb9d3a2): unreliable finding: "Ablösen" may be the established project term for Unpin; inconsistency cannot be confirmed from the given data.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 31b2b7d6): unreliable finding: "Post Town" is a UK-specific address concept and may be deliberately kept; "Poststadt" is not an established German term.
- `Changes color theme.` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 9dd3134e): unreliable finding: "Farbeinstellung" is a plausible description of the reader-mode colour choice; the change is stylistic.
- `CloseTabsToast.Title.v113` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string a35856b3): "Geschlossene Tabs: %d" is correct, natural German that conveys the number of tabs closed; no meaning is lost.
- `FxAPush_DeviceConnected_body` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 6de95c61): unreliable finding: "ist mit %@ verbunden" is a natural and correct German rendering of the notification; the change is stylistic.
- `LiveActivity.Downloads.FileCountText.v138` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 6442e1ac): unreliable finding: "Aktive Downloads: %@" is an idiomatic German label for an ongoing download count and conveys the same information.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 6ae43602): The en-US source itself reads "Tracking content", which "Tracking-Inhalt" renders faithfully.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 3a1d8a54): unreliable finding: "weitere" can convey "more" in this context; the wording is acceptable and the change is stylistic.
- `Menu.OpenSettingsAction.Title` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 1d9ab467): unreliable finding: A soft hyphen is invisible unless the word wraps and is likely a deliberate hyphenation hint for a narrow menu label.
- `Menu.ZoomPage.Close.AccessibilityLabel.v113` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 46014250): unreliable finding: "Zoom-Ansicht" is an acceptable name for the zoom panel; the suggested change is stylistic.
- `NativeErrorPage.GenericError.Description.v158.withoutURL` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string c5fbf62a): unreliable finding: "konnte nicht auf die URL zugreifen" is a common, acceptable German rendering of failing to reach a URL.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 8192ee1a): unreliable finding: "an einem Ort" keeps the meaning; adding "alles" with a dash is a stylistic preference.
- `Onboarding.TermsOfService.TermsOfServiceAgreement.v135` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 644b92f4): unreliable finding: The claim that the link text already ends with a period cannot be verified, and a sentence-final period is normal German.
- `QuickAnswers.Settings.Footer.v158` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 0b14c912): unreliable finding: The singular reads as a generic description in German and conveys the same meaning; the change is stylistic.
- `ReopenAlert.Title` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string ee60c2dc): unreliable finding: "wiederherstellen" is established German Firefox wording for reopening closed tabs; meaning is preserved.
- `SendTo.NotSignedIn.Title` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 5439a704): unreliable finding: "mit Ihrem Konto angemeldet" is idiomatic German (signed in with your account); "bei" is a preference.
- `SendTo.NotSignedIn.Title.v119` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string bbad985c): "mit Ihrem Konto angemeldet" is idiomatic German (cf. "Angemeldet mit Ihrem Google-Konto"); mit is not ungrammatical.
- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 43563939): unreliable finding: Section heading vs. icon name reuse is a terminology choice; the suggested "Grundlagen" is not clearly better for an icon section.
- `Settings.Home.Option.Wallpaper.Classic.Title.v106` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 4013c8e6): unreliable finding: "%@ klassisch" is an acceptable label-style title for a wallpaper group; the suggested alternative is stylistic.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `de/firefox-ios.xliff` — auto-suggest (2026-11-02, string 44e07fd5): "jemandem erlauben, etwas zu tun" takes a dative object, and "bestimmter Werbung" is the correct feminine dative, so the sentence is grammatical.
- `Settings.Translation.AutoTranslate.Footer.v151` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string b27e52dc): unreliable finding: "Ihre bevorzugte Sprache" adequately conveys the top preferred language; the suggested wording is a stylistic preference.
- `Summarizer.Footnote.Label.v144` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 0a5105df): unreliable finding: "Beim Zusammenfassen können Fehler auftreten" is natural German for this disclaimer and does not clearly imply operational failures.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 1d278339): unreliable finding: "Blatt" is a plausible rendering of the iOS sheet element in an accessibility announcement; no established alternative term is shown.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 31b38f29): unreliable finding: "auf Ihrem Startbildschirm hinzufügen" is grammatical, common German; the finding's claim of ungrammaticality is incorrect.
- `TranslationToastHandler.PromptTranslate.Title` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string 67c2f571): unreliable finding: "auf <Sprache> übersetzen" is widely used and accepted German; placeholders are all intact.
- `WebCompatReporter.Fields.DetailsPlaceholder.v154` — `de/firefox-ios.xliff` — auto-suggest (2026-11-09, string dc2dc280): unreliable finding: "freiwillig" is a common, correct German marker for optional form input; the change is a preference.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/de/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (53)

- `Addresses.EditAddress.AutofillAddressState.v129` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Engagement.Notification.Treatment.B.Body.v114` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Menu.EnhancedTrackingProtection.On.Header.v128` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `Onboarding.Notification.Title.v120` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `BreachAlerts.Link` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `DownloadsPanel.Delete.Title` — `de/firefox-ios.xliff` — fixed 2026-11-09
- `FirefoxHome.CustomizeHomeButton.Title` — `de/firefox-ios.xliff` — fixed 2026-11-09
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
