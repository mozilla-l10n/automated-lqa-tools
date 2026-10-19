# Firefox l10n QA — de

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-12 @ `9b5f3e8ca0a3` |
| **Mode** | incremental |
| **Strings reviewed this run** | 130 of 16,742 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (3)

- `ip-protection-site-rules-button-1` — `browser/browser/ipProtection.ftl` — Incorrect comma before "oder" joining two coordinated relative clauses.
    - Current: `die mehr Datenschutz, oder die ein deaktiviertes VPN benötigen`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage VPN rules`
    - Suggest: `die mehr Datenschutz oder ein deaktiviertes VPN benötigen`
    - German comma rules do not allow a comma before "oder" when it links parallel clause parts like these. The comma here is a punctuation error.
- `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl` — The German drops "ask", so it says sites may open app links rather than ask to open them.
    - Current: `Websites erlauben, App-Links zu öffnen.`
    - Source: `accesskey: A label: Allow sites to ask to open app links.`
    - Suggest: `Websites erlauben, das Öffnen von App-Links anzufragen.`
    - The en-US "Allow sites to ask to open app links" grants permission to ask, which matches the related strings ("Fragen, ob App-Links geöffnet werden sollen"). The German claims sites may open app links directly, a wider permission than the setting gives.
- `policy-PasswordManagerEnabled2` — `browser/browser/policies/policies-descriptions.ftl` — A full stop is missing between the two sentences.
    - Current: `aktivieren oder deaktivieren Wenn`
    - Source: `Enable or disable saving passwords to the password manager. If disabled, Passwords (about:logins) is also blocked.`
    - Suggest: `aktivieren oder deaktivieren. Wenn`
    - The en-US has two sentences. In the German the first runs into the second with no punctuation.

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
| Files | 338 |
| Strings | 16,742 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 6 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**Files present but identical to en-US:**

- `toolkit/toolkit/about/aboutMozilla.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Files with no en-US counterpart

- `browser/branding/enterprise/brand.ftl`
- `browser/branding/enterprise/brand.properties`
- `browser/browser/enterprise/enterprise-policies-descriptions.ftl`
- `browser/browser/enterprise/enterprise.ftl`
- `browser/browser/enterprise/felt.ftl`
- `browser/chrome/overrides/enterprise.properties`
- `dom/chrome/enterprise.properties`
- `toolkit/crashreporter/crashreporter-enterprise.ftl`
- `toolkit/toolkit/enterprise/enterprise.ftl`
- `toolkit/toolkit/enterprise/felt.ftl`

_222 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 741, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 114 | **straight** |
| ellipsis | `char` 414 | **char** |
| dash | `em` 17, `en` 69 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 3965 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (40)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — "Nice work organizing your tabs" is turned into a factual claim that the user's tabs are now perfectly organized.
    - Current: `Ihre Tabs sind jetzt bestens organisiert`
    - Source: `Nice work organizing your tabs`
    - Suggest: `Gut gemacht beim Organisieren Ihrer Tabs`
    - The source praises the user's action; the German instead asserts a state ("your tabs are now optimally organized") that the source never claims.
- `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl` — The German drops "ask", so it says sites may open app links rather than ask to open them.
    - Current: `Websites erlauben, App-Links zu öffnen.`
    - Source: `accesskey: A label: Allow sites to ask to open app links.`
    - Suggest: `Websites erlauben, das Öffnen von App-Links anzufragen.`
    - The en-US "Allow sites to ask to open app links" grants permission to ask, which matches the related strings ("Fragen, ob App-Links geöffnet werden sollen"). The German claims sites may open app links directly, a wider permission than the setting gives.
- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Source: `Split, merge, and more. <a data-l10n-name="features-link">See PDF features</a>`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
    - en-US "Split, merge, and more" refers to splitting a PDF into parts; "teilen" reads as sharing, giving users a different feature claim.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 21 |
| 3 | Degraded language (grammar, spelling, terminology) | 16 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-link-send-to-device` is not present in its label
    - Current: `X`
    - Source: `accesskey: n label: Send Link to Device`
    - The label is “Link an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `restart-required-fix-answer` — `browser/browser/aboutRestartRequired.ftl` — "Follow our progress in Bugzilla bug 2072739" is rendered as "Den aktuellen Stand finden Sie …", dropping the sense of following ongoing progress.
    - Current: `Den aktuellen Stand finden Sie im Bugzilla-Fehler 2072739.`
    - Source: `Yes. We know this is disruptive, and we’re working on a fix to prevent it. Follow our progress in Bugzilla bug 2072739.`
    - Suggest: `Verfolgen Sie unseren Fortschritt im Bugzilla-Fehler 2072739.`
    - The English asks users to follow the team's progress; the German states the current status can be found there, a different statement.
- `restart-required-see-more-button` — `browser/browser/aboutRestartRequired.ftl` — "See more" (expand the details section) is rendered as "Mehr erfahren" (learn more), inconsistent with its counterpart "Weniger anzeigen".
    - Current: `Mehr erfahren`
    - Source: `See more`
    - Suggest: `Mehr anzeigen`
    - The developer comment says the button expands the "More details" section; the collapse counterpart is translated "Weniger anzeigen", so the expand label should be "Mehr anzeigen", not a "learn more" link phrase.
- `restart-required-why-now-answer` — `browser/browser/aboutRestartRequired.ftl` — Brand placeable replaced with hardcoded "Firefox" in the first occurrence.
    - Current: `wenn ein anderes Firefox-Profil`
    - Source: `This can happen when another { -brand-short-name } profile or instance updates, or when an update can’t wait until your next restart.`
    - Suggest: `wenn ein anderes { -brand-short-name }-Profil`
    - The en-US uses { -brand-short-name } for the profile reference; hardcoding "Firefox" breaks brand substitution for other builds.
- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — "Nice work organizing your tabs" is turned into a factual claim that the user's tabs are now perfectly organized.
    - Current: `Ihre Tabs sind jetzt bestens organisiert`
    - Source: `Nice work organizing your tabs`
    - Suggest: `Gut gemacht beim Organisieren Ihrer Tabs`
    - The source praises the user's action; the German instead asserts a state ("your tabs are now optimally organized") that the source never claims.
- `smartwindow-group-tabs-loading` — `browser/browser/autoTabGrouping.ftl` — The German says tabs are being checked "for useful groups" in a way that implies searching for existing groups, contrary to the developer comment.
    - Current: `Tabs werden auf nützliche Gruppen überprüft…`
    - Source: `Checking tabs for useful groups…`
    - Suggest: `Tabs werden auf nützliche Gruppierungen geprüft…`
    - The comment states the model is forming new groups from the tabs, not searching for groups that already exist; "Tabs werden auf … Gruppen überprüft" reads as inspecting tabs for groups they belong to.
- `smartwindow-organize-tabs-button` — `browser/browser/autoTabGrouping.ftl` — "Organize Tabs" is rendered as "Tabs verwalten" (manage tabs) instead of "Tabs organisieren".
    - Current: `label: Tabs verwalten`
    - Source: `label: Organize Tabs tooltiptext: Organize Tabs`
    - Suggest: `label: Tabs organisieren`
    - The en-US "Organize" means arranging/grouping tabs (the feature clusters tabs into groups); "verwalten" is the established German rendering of "Manage", which is a different term used elsewhere (e.g. "Manage shortcuts" → "Tastenkombinationen verwalten").
- `ipprotection-site-inclusions-callout-title-lapsed-users` — `browser/browser/ipProtection.ftl` — "Try built-in VPN, now site by site" loses "site by site" nuance, rendered as "gezielt für einzelne Websites testen".
    - Current: `Integriertes VPN jetzt gezielt für einzelne Websites testen`
    - Source: `Try built-in VPN, now site by site`
    - Suggest: `Integriertes VPN testen – jetzt Website für Website`
    - The English emphasizes the new per-site capability ("site by site"); the German adds "gezielt" and blurs it, though meaning is close.
- `newtab-wallpaper-firefox-sky-light` — `browser/browser/newtab/newtab.ftl` — "Light hills" (helle Hügel) mistranslated as "Leichte Hügel" (lightweight hills).
    - Current: `Leichte Hügel unter einem sanften Himmel`
    - Source: `Light hills under a soft sky`
    - Suggest: `Helle Hügel unter einem sanften Himmel`
    - In this wallpaper set "light" means bright/hell (contrast with "dark purple hills"), not "leicht" (not heavy). Other strings in the same set correctly use "helle Hügel".
- `onboarding-refresh-fro-import-header` — `browser/browser/newtab/onboarding.ftl` — "Bring in your data" (import data) rendered as "Geben Sie Ihre Daten ein" (enter your data).
    - Current: `Geben Sie Ihre Daten ein`
    - Source: `Bring in your data`
    - Suggest: `Importieren Sie Ihre Daten`
    - The string heads the import step of onboarding; en-US means importing existing data, not typing data in.
- `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl` — The German drops "ask", so it says sites may open app links rather than ask to open them.
    - Current: `Websites erlauben, App-Links zu öffnen.`
    - Source: `accesskey: A label: Allow sites to ask to open app links.`
    - Suggest: `Websites erlauben, das Öffnen von App-Links anzufragen.`
    - The en-US "Allow sites to ask to open app links" grants permission to ask, which matches the related strings ("Fragen, ob App-Links geöffnet werden sollen"). The German claims sites may open app links directly, a wider permission than the setting gives.
- `prefs-syncing-off-3` — `browser/browser/preferences/preferences.ftl` — "get ... on this device" rendered as "auf dieses Gerät zu übertragen" (transfer onto this device) changes the stated action direction/claim of sync.
    - Current: `um Ihre Lesezeichen, Passwörter, Chronik und mehr auf dieses Gerät zu übertragen`
    - Source: `description: Turn on sync to get your bookmarks, passwords, history, and more on this device. label: Syncing is OFF`
    - Suggest: `um Ihre Lesezeichen, Passwörter, Chronik und mehr auf diesem Gerät zu erhalten`
    - The en-US says to get the data on this device (sync); the German says it will be transferred to this device, a one-directional claim not in the source.
- `sync-syncing-across-devices-heading-3` — `browser/browser/preferences/preferences.ftl` — "Data syncing on this device" translated as "Auf diesem Gerät synchronisierte Daten" (data already synced), changing the heading's meaning.
    - Current: `Auf diesem Gerät synchronisierte Daten`
    - Source: `Data syncing on this device`
    - Suggest: `Datensynchronisation auf diesem Gerät`
    - The source is about the ongoing syncing of data on this device, not a list of data that has been synced; the German past participle asserts completed action.
- `splitter.label` — `devtools/client/components.properties` — Plural "panels" rendered as singular "des Bereichs".
    - Current: `Größe des Bereichs ändern`
    - Source: `Resize panels`
    - Suggest: `Größe der Bereiche ändern`
    - The source says "Resize panels" (both panels of a split view, per the comment); the German refers to only one panel.
- `statePartiallyChecked` — `dom/chrome/accessibility/AccessFu.properties` — "partially checked" is translated as "teilweise ausgewählt" (partially selected) instead of "teilweise aktiviert/angekreuzt".
    - Current: `teilweise ausgewählt`
    - Source: `partially checked`
    - Suggest: `teilweise aktiviert`
    - The accessibility state refers to a checkbox being checked, not selected; "ausgewählt" is the German term for "selected", a distinct accessibility state.
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — "SpeechRecognition" was translated although the developer comment forbids it.
    - Current: `daher meldet die Spracherkennung sich selbst als nicht verfügbar`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `daher meldet SpeechRecognition sich selbst als nicht verfügbar`
    - The developer comment states: Do not translate "SpeechRecognition" — it is the Web API interface name, but it was localized as "die Spracherkennung".
- `SecureUpgradeRequest` — `dom/chrome/security/security.properties` — "insecure request" rendered as "nicht verschlüsselte Anfrage" (unencrypted), narrowing the meaning.
    - Current: `Die nicht verschlüsselte Anfrage`
    - Source: `%1$S: Upgrading insecure request “%2$S” to use “%3$S”.`
    - Suggest: `Die unsichere Anfrage`
    - The en-US says "insecure", which is the established term (unsicher); "nicht verschlüsselt" states a different, narrower fact about the request.
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — "Reorder" is translated as "sortieren" (sort) instead of "neu anordnen" (reorder).
    - Current: `Seiten sortieren, löschen, zusammenführen und exportieren.`
    - Source: `Reorder, remove, merge, and export pages.`
    - Suggest: `Seiten neu anordnen, löschen, zusammenführen und exportieren.`
    - The en-US "Reorder" means rearranging pages manually, not sorting them; "sortieren" names a different function.
- `pdf-features-notification` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — "just got easier" translated as "sind noch einfacher", losing the meaning of a new improvement.
    - Current: `PDFs sind in { -brand-short-name } noch einfacher.`
    - Source: `aria-label: Notification heading: PDFs just got easier in { -brand-short-name }.`
    - Suggest: `PDFs sind in { -brand-short-name } jetzt noch einfacher.`
    - en-US states the experience has just improved; the German drops the temporal "just/now", changing the statement.
- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Source: `Split, merge, and more. <a data-l10n-name="features-link">See PDF features</a>`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
    - en-US "Split, merge, and more" refers to splitting a PDF into parts; "teilen" reads as sharing, giving users a different feature claim.
- `user-context-personal2` — `toolkit/toolkit/global/contextual-identity.ftl` — "Personal" is rendered as "Freizeit" (leisure), which names a different category.
    - Current: `Freizeit`
    - Source: `label: Personal`
    - Suggest: `Persönlich`
    - The en-US container label "Personal" contrasts with "Work"; "Freizeit" means leisure/free time, not personal.

### C. Grammar, agreement & spelling

- `content-analysis-indicator-tooltip` — `browser/browser/browser.ftl` — Wrong preposition in "Verhinderung vor Datenverlust".
    - Current: `Verhinderung vor Datenverlust (DLP)`
    - Source: `tooltiptext: Data Loss Prevention (DLP) by { $agentName }. Click for more info.`
    - Suggest: `Verhinderung von Datenverlust (DLP)`
    - German "Verhinderung" takes the genitive/"von", not "vor"; "Verhinderung vor" is ungrammatical.
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — Clause structure makes the user the subject of hiding, breaking agreement with the impersonal main clause.
    - Current: `Sorgt für mehr Privatsphäre, indem Sie Ihren Standort beim Surfen verbergen.`
    - Source: `description: Get extra privacy by hiding your location while browsing. label: Built-in VPN`
    - Suggest: `Sorgt für mehr Privatsphäre, indem Ihr Standort beim Surfen verborgen wird.`
    - In en-US the VPN hides the user's location; the German makes the user do the hiding, contradicting the impersonal subject of the main clause.
- `ip-protection-site-rules-button-1` — `browser/browser/ipProtection.ftl` — Incorrect comma before "oder" joining two coordinated relative clauses.
    - Current: `die mehr Datenschutz, oder die ein deaktiviertes VPN benötigen`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage VPN rules`
    - Suggest: `die mehr Datenschutz oder ein deaktiviertes VPN benötigen`
    - German comma rules do not allow a comma before "oder" when it links parallel clause parts like these. The comma here is a punctuation error.
- `speech-recognition-model-download-progress-message` — `browser/browser/permissions.ftl` — Progress message rendered as an imperative/infinitive instead of a status statement.
    - Current: `Spracherkennungsmodell herunterladen`
    - Source: `Downloading speech recognition model`
    - Suggest: `Spracherkennungsmodell wird heruntergeladen`
    - The en-US "Downloading speech recognition model" describes an ongoing action; the German reads as a command/label "Download speech recognition model".
- `translations-panel-revisit-to-label` — `browser/browser/translations.ftl` — Wrong preposition for "Translate to".
    - Current: `Übersetzen auf`
    - Source: `Translate to`
    - Suggest: `Übersetzen in`
    - German uses "übersetzen in" (eine Sprache), not "übersetzen auf".

### D. Terminology, register & consistency

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — "share Firefox" is rendered as "Teilen Sie Firefox" here but as "Firefox empfehlen" in all other referral strings of this batch.
    - Current: `Teilen Sie { -brand-product-name }`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `empfehlen Sie { -brand-product-name }`
    - The developer comments for the parallel referral strings state that "Share" means recommending/referring the browser; the de tree consistently uses "empfehlen", so "Teilen" (file sharing sense) is inconsistent and misleading.
- `appmenu-fxa-sign-in-promo-link` — `browser/browser/appmenu.ftl` — "Sign in" is translated "Einloggen" instead of the established Firefox German term "Anmelden".
    - Current: `Einloggen`
    - Source: `Sign in`
    - Suggest: `Anmelden`
    - Firefox de consistently uses "Anmelden" for "Sign in"; the sibling string in the same promo even says "Promo für Anmeldung schließen", making this inconsistent.
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Ihre Daten wiederherstellen” but the string it names, `restore-from-backup-header`, reads “Daten wiederherstellen”
    - Current: `Klicken Sie auf "Ihre Daten wiederherstellen" und wählen Sie diese Datei`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Daten wiederherstellen`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Ihre Daten wiederherstellen” but the string it names, `restore-from-backup-header`, reads “Daten wiederherstellen”
    - Current: `Klicken Sie auf "Ihre Daten wiederherstellen" und wählen Sie diese Datei`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Daten wiederherstellen`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “Webbrowser” but the string it names, `desktop-entry-generic-name`, reads “Internet-Browser”
    - Current: `Schritt 1: Gehen Sie zu Einstellungen > Standard-Apps Schritt 2: Scrollen Sie nach unten zu "Webbrowser" Schritt 3: { -brand-short-name } markieren und auswählen`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `Internet-Browser`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `migration-chrome-windows-password-import-step3` — `browser/browser/migrationWizard.ftl` — `migration-chrome-windows-password-import-step3` quotes “Datei herunterladen” but the string it names, `downloadFile.label`, reads “Datei speichern unter…”
    - Current: `Wählen Sie "Datei herunterladen" und speichern Sie sie auf Ihrem Gerät.`
    - Source: `Choose “Download file” and save it to your device.`
    - Suggest: `Datei speichern unter…`
    - In the source this string quotes “Download file”, which is exactly the value of `downloadFile.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `addressbar-skip-result-menu-on-tab` — `browser/browser/preferences/preferences.ftl` — Checkbox label rendered as an imperative instruction instead of a noun/infinitive setting label.
    - Current: `Überspringen Sie das Ergebnismenü, wenn Sie die Tab-Taste zum Verschieben des Fokus verwenden`
    - Source: `label: Skip the results menu when using the tab key to move focus`
    - Suggest: `Ergebnismenü überspringen, wenn Sie die Tab-Taste zum Verschieben des Fokus verwenden`
    - The en-US "Skip the results menu when…" is a settings checkbox label, not a command to the user; the parallel menu item urlbar-view-context-menu-skip-menu-with-tab is correctly rendered as "Dieses Menü überspringen, wenn …".
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “Lokalen Modus” but the string it names, `options-local-mode-label`, reads “Lokaler Modus”
    - Current: `Dieses Dokument kann auch über den "Lokalen Modus" der DevTools von "{ $url }" geladen werden, der im Einstellungsbereich aktiviert werden kann.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Lokaler Modus`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — `preventedConsoleClear` quotes “Logs nicht leeren” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “Log nicht leeren”
    - Current: `console.clear() wurde aufgrund von "Logs nicht leeren" verhindert`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `Log nicht leeren`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `xslt-bad-value` — `dom/dom/xslt.ftl` — "Chronik" is the established term.
    - Source: `Attribute value illegal in XSLT 1.0.`
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Descriptive label rendered as an imperative addressed to the user instead of a noun-phrase description of the preset.
    - Current: `Protokollieren Sie Module zur Diagnose`
    - Source: `Log modules to diagnose IP Protection (VPN) issues`
    - Suggest: `Module zur Diagnose von Problemen mit dem IP-Schutz (VPN) protokollieren`
    - The en-US "Log modules to diagnose…" is a preset description, not an instruction to the user; sibling preset descriptions use an infinitive/noun phrase.

### E. Typography, punctuation & spacing

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — Superfluous comma before "oder" in the enumeration.
    - Current: `Teilen Sie { -brand-product-name }</label>, oder`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `Teilen Sie { -brand-product-name }</label> oder`
    - German does not use a comma before "oder" joining the last item of a simple enumeration; the comma is a direct carry-over of the English serial comma.
- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — Stray space and misplaced verb inside the link text: "Datenschutzhinweis zu </a>" puts "zu" inside the anchor with a trailing space.
    - Current: `<a data-l10n-name="privacy_notice">Datenschutzhinweis zu </a>`
    - Source: `By continuing, you agree to the <a data-l10n-name="terms_of_use">{ -brand-product-name } Terms of Use</a> and our <a data-l10n-name="privacy_notice">Privacy Notice</a>. To help improve the browser, { -brand-product-name…`
    - Suggest: `<a data-l10n-name="privacy_notice">Datenschutzhinweis</a> zu`
    - The en-US link text is only "Privacy Notice"; including "zu " plus a trailing space in the linked text makes the hyperlink text wrong and leaves a space before the period.
- `policy-PasswordManagerEnabled2` — `browser/browser/policies/policies-descriptions.ftl` — A full stop is missing between the two sentences.
    - Current: `aktivieren oder deaktivieren Wenn`
    - Source: `Enable or disable saving passwords to the password manager. If disabled, Passwords (about:logins) is also blocked.`
    - Suggest: `aktivieren oder deaktivieren. Wenn`
    - The en-US has two sentences. In the German the first runs into the second with no punctuation.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (43)

- `appmenuitem-new-window` — `browser/browser/appmenu.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `toolbar-button-email-link` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `toolbar-button-open-file` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `toolbar-button-save-page` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `urlbar-result-market-opt-in-description` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `urlbar-web-notifications-blocked` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `ipprotection-message-bandwidth-warning-mb` — `browser/browser/ipProtection.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `menu-file-new-window` — `browser/browser/menubar.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `newtab-sports-widget-cancelled` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `newtab-sports-widget-suspended` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `containers-disable-alert-title` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `containers-remove-alert-msg` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `preferences-etp-custom-cookie-behavior-block-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `preferences-etp-level-standard` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (42)

- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — fixed 2026-09-07
- `containers-sites-card-header` — `browser/browser/preferences/preferences.ftl` — fixed 2026-09-07
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — fixed 2026-09-03
- `webauthn-uv-invalid-long-prompt` — `browser/browser/webauthnDialog.ftl` — fixed 2026-09-03
- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `network-proxy-connection-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — fixed 2026-08-24
- `pocket-panel-saved-error-tag-length` — `browser/browser/aboutPocket.ftl` — fixed 2026-07-27
- `site-permission-install-first-prompt-midi-message` — `browser/browser/addonNotifications.ftl` — fixed 2026-07-27
- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `content-sharing-modal-sign-in-2` — `browser/browser/contentSharing.ftl` — fixed 2026-07-27
- `customkeys-conflict-confirm-body` — `browser/browser/customkeys.ftl` — fixed 2026-07-27
- `default-browser-guidance-notification-title` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-07-27
- `migration-no-permissions-instructions` — `browser/browser/migrationWizard.ftl` — fixed 2026-07-27
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-27
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-27
- `windows-10-eos-challenger-sync-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-27
- `windows-10-eos-sync-callout-privacy-screen-1-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-27
- `windows-10-eos-sync-toast-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-27
- `newtab-sports-widget-match-penalties` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-27
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-27
- `fxa-qrcode-error-title` — `browser/browser/preferences/fxaPairDevice.ftl` — fixed 2026-07-27
- `extension-controlling-privacy-containers` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-27
- `search-keyword-warning-title` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-27
- `report-broken-site-panel-reason-deceptive-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — fixed 2026-07-27
- `sync-setup-verify-title` — `browser/browser/sync.ftl` — fixed 2026-07-27
- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — fixed 2026-07-27
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — fixed 2026-07-27
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — fixed 2026-07-27
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — fixed 2026-07-27
- `about-networking-ssl-tokens-built-in-root` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-07-27
- `content-uses-tiling` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-27
- `certificate-viewer-extended-key-usages` — `toolkit/toolkit/about/certviewer.ftl` — fixed 2026-07-27
- `url-classifier-content-classifier-verdict-miss` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-27
- `contentanalysis-slow-agent-dialog-body-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — fixed 2026-07-27
- `csp-error-missing-directive` — `toolkit/toolkit/global/cspErrors.ftl` — fixed 2026-07-27
- `privacy-spoof-english` — `toolkit/toolkit/global/resistFingerPrinting.ftl` — fixed 2026-07-27
- `sec-error-cert-no-response` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-27
- `sec-error-ocsp-unknown-response-type` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-27
- `sec-error-token-not-logged-in` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-27
