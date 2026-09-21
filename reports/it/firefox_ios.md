# Firefox iOS l10n QA — it

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 28 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for it: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,950 |
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
| quotes | `curly-double` 15 | **curly-double** |
| apostrophe | `typographic` 72 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 74, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (7)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.Studies.Message.v148` — `it/firefox-ios.xliff` — Translation adds "del browser" (of the browser), which the source does not say.
    - Current: `contribuendo così a migliorare la qualità del browser per tutti`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `contribuendo così a migliorare la qualità per tutti`
    - The en-US says "which improves quality for everyone" without specifying the browser; the Italian adds an unsourced object.
- `ActivityStream.Library.Title` — `it/firefox-ios.xliff` — "Recently Saved" translated as "Aggiunti di recente" (recently added) rather than "Salvati di recente".
    - Current: `Aggiunti di recente`
    - Source: `Recently Saved`
    - Suggest: `Salvati di recente`
    - The section lists recently saved items (bookmarks/reading list); the Italian says "added" instead of "saved", diverging from the source term.
- `HistoryPanel.ClearHistoryMenuOptionTodayAndYesterday` — `it/firefox-ios.xliff` — Order of days reversed relative to source "Today and Yesterday".
    - Current: `Ieri e oggi`
    - Source: `Today and Yesterday`
    - Suggest: `Oggi e ieri`
    - The source lists "Today and Yesterday"; the Italian inverts the order.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `it/firefox-ios.xliff` — "Cross-Site Trackers" translated as "Contenuti traccianti intersito", duplicating the wording used for "Tracking content" and adding "Contenuti".
    - Current: `Contenuti traccianti intersito`
    - Source: `Cross-Site Trackers`
    - Suggest: `Traccianti intersito`
    - The source says "Cross-Site Trackers" (trackers), not "tracking content"; the current wording collides with Menu.TrackingProtectionBlockedContent.Title ("Contenuti traccianti") on the same screen.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `it/firefox-ios.xliff` — "collect" rendered as "memorizzano" (store) instead of "raccolgono" (collect).
    - Current: `I fingerprinter memorizzano vari tipi di impostazioni distintive`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `I fingerprinter raccolgono vari tipi di impostazioni distintive`
    - The source says fingerprinters collect these settings, not that they store them.
- `Settings.Siri.SectionDescription` — `it/firefox-ios.xliff` — The translation drops "Siri shortcuts", turning "Use Siri shortcuts to quickly open Firefox via Siri" into "Use Siri to quickly open Firefox".
    - Current: `Utilizza Siri per aprire velocemente Firefox`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Utilizza i comandi di Siri per aprire velocemente Firefox con Siri`
    - The source describes using Siri shortcuts; the Italian omits the shortcut concept, which is the subject of this settings section (see Settings.Siri.SectionName “Comandi di Siri”).

### C. Grammar, agreement & spelling

- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `it/firefox-ios.xliff` — Singular "the image" rendered as plural "le immagini".
    - Current: `Permette di salvare le immagini nel Rullino.`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Permette di salvare l’immagine nel Rullino.`
    - The en-US source refers to a single image ("save the image to your Camera Roll").

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (21)

- `ActivityStream.ContextMenu.UnpinTopsite` — `it/firefox-ios.xliff` — “Rilascia” is the established opposite of “Appunta” in this menu
- `ActivityStream.ContextMenu.UnpinTopsite` — `Shared/en.lproj/Localizable.strings` — “Rilascia” is the established opposite of “Appunta” in this menu
- `ContextualHints.Toolbar.GoogleLens.Description.v154` — `it/firefox-ios.xliff` — Better sounding variation, same meaning.
- `ContextualHints.Toolbar.GoogleLens.Description.v154` — `Shared/Supporting Files/en.lproj/ContextualHints.strings` — Better sounding variation, same meaning.
- `DefaultBrowserOnboarding.Description2` — `it/firefox-ios.xliff` — “di default” mirrors the wording iOS itself shows in Settings
- `DefaultBrowserOnboarding.Description2` — `Shared/en.lproj/Default Browser.strings` — “di default” mirrors the wording iOS itself shows in Settings
- `DefaultBrowserOnboarding.Screenshot` — `it/firefox-ios.xliff` — “di default” mirrors the wording iOS itself shows in Settings
- `DefaultBrowserOnboarding.Screenshot` — `Shared/en.lproj/Default Browser.strings` — “di default” mirrors the wording iOS itself shows in Settings
- `DefaultBrowserPopup.SecondLabel.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — “di default” mirrors the wording iOS itself shows in Settings
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `it/firefox-ios.xliff` — “invadenti” might be more accurate, but it results in a weird phrase (need to be placed at the end)
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en.lproj/PrivateBrowsing.strings` — “invadenti” might be more accurate, but it results in a weird phrase (need to be placed at the end)
- `Onboarding.Modern.Welcome.Title.v145` — `it/firefox-ios.xliff` — DRAFT: the Italian wording is the agreed rendering for this screen
- `Onboarding.Modern.Welcome.Title.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — DRAFT: the Italian wording is the agreed rendering for this screen
- `Onboarding.Welcome.Description.TreatementA.v120` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — “invadenti” might be more accurate, but it results in a weird phrase (need to be placed at the end)
- `Onboarding.Welcome.Title.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — “Benvenuti” is inclusive and shorter than “Ti diamo il benvenuto”
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `it/firefox-ios.xliff` — False positive (“book” is there)
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `Shared/en.lproj/Localizable.strings` — False positive (“book” is there)
- `Settings.AppIconSelection.AppIconNames.Retro2004.Title.v139` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — “Rétro” is correct https://www.treccani.it/vocabolario/retro_res-0f8f0e80-002f-11de-9d89-0016357eee51/
- `Settings.AppIconSelection.AppIconNames.Retro2017.Title.v139` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — “Rétro” is correct https://www.treccani.it/vocabolario/retro_res-0f8f0e80-002f-11de-9d89-0016357eee51/
- `Settings.AppIconSelection.AppIconNames.Yellow.Title.v137` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — Agrees with “icona”, which is feminine
- `Settings.Homepage.Shortcuts.ToggleOff.v100` — `Shared/en.lproj/Localizable.strings` — Refers to the section.

_One line each in `locales/it/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (2)

- **`it-attiva-not-attivata`** (1) — The expected pair is `Attiva`/`Attivo`/`Attivi` with `Disattivata`/`Disattivato`/`Disattivati`. The asymmetry is deliberate and borne out by the tree, which uses `attiva` 279 times against 35 for the participle forms. A suggestion to "restore symmetry" with `Attivata`/`Attivato`/`Attivi` is wrong. The regex is word-anchored because a plain substring would also match `disattivato`.
    - `Settings.Translation.SettingOn.v145`
- **`it-crittare`** (1) — `crittare` and its forms (`critta`, `crittato`) are the correct Italian verb for "to encrypt" — not a typo for `criptare`. Confirmed by the maintainer. Scoped to spelling findings so a mistranslation in the same string still reports.
    - `CreditCard.RememberCard.Header.v122`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (16)

- `Biometry.Screen.UniversalAuthenticationReason.v115` — `Shared/Supporting Files/en.lproj/BiometricAuthentication.strings` — fixed 2026-08-21
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — fixed 2026-08-21
- `Onboarding.Welcome.Description.v120` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — fixed 2026-08-21
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `Shared/Supporting Files/en.lproj/ScanQRCode.strings` — fixed 2026-08-21
- `Settings.AIControls.BlockedInformation.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-21
- `Settings.Translation.AutoTranslate.Footer.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-21
- `Settings.Translation.ToggleFooter.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-21
- `Hotkeys.ShowPreviousTab.DiscoveryTitle` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `SendTo.NotSignedIn.Message` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `SentTab_TabArrivingNotification_NoDevice_title` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `SentTab_TabArrivingNotification_WithDevice_title` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `Settings.Tabs.CustomizeTabsSection.Title` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `Tabs Tray` — `Shared/en.lproj/Localizable.strings` — fixed 2026-08-21
- `No logins found` — `Shared/en.lproj/LoginManager.strings` — fixed 2026-08-21
- `TodayWidget.TopSitesGalleryDescription` — `Shared/en.lproj/Today.strings` — fixed 2026-08-21
