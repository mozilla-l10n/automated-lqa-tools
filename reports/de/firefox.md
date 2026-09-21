# Firefox l10n QA — de

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `3f7b6c3c060f` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `749ea3a23fef` |
| **Previous run** | 2026-09-14 @ `e44f1369fb6d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 65 of 16,447 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (4)

- `splitter.label` — `devtools/client/components.properties` — Plural "panels" rendered as singular "des Bereichs".
    - Current: `Größe des Bereichs ändern`
    - Source: `Resize panels`
    - Suggest: `Größe der Bereiche ändern`
    - The source says "Resize panels" (both panels of a split view, per the comment); the German refers to only one panel.
- `translations-panel-revisit-to-label` — `browser/browser/translations.ftl` — Wrong preposition for "Translate to".
    - Current: `Übersetzen auf`
    - Source: `Translate to`
    - Suggest: `Übersetzen in`
    - German uses "übersetzen in" (eine Sprache), not "übersetzen auf".
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — "Reorder" is translated as "sortieren" (sort) instead of "neu anordnen" (reorder).
    - Current: `Seiten sortieren, löschen, zusammenführen und exportieren.`
    - Source: `Reorder, remove, merge, and export pages.`
    - Suggest: `Seiten neu anordnen, löschen, zusammenführen und exportieren.`
    - The en-US "Reorder" means rearranging pages manually, not sorting them; "sortieren" names a different function.
- `user-context-personal2` — `toolkit/toolkit/global/contextual-identity.ftl` — "Personal" is rendered as "Freizeit" (leisure), which names a different category.
    - Current: `Freizeit`
    - Source: `label: Personal`
    - Suggest: `Persönlich`
    - The en-US container label "Personal" contrasts with "Work"; "Freizeit" means leisure/free time, not personal.

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
| Files | 336 |
| Strings | 16,447 |
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

_214 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 729, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 114 | **straight** |
| ellipsis | `char` 405 | **char** |
| dash | `em` 17, `en` 69 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 3868 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (23)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Source: `Split, merge, and more. <a data-l10n-name="features-link">See PDF features</a>`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
    - en-US "Split, merge, and more" refers to splitting a PDF into parts; "teilen" reads as sharing, giving users a different feature claim.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 14 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-link-send-to-device` is not present in its label
    - Current: `X`
    - Source: `accesskey: n label: Send Link to Device`
    - The label is “Link an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

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

- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — Clause structure makes the user the subject of hiding, breaking agreement with the impersonal main clause.
    - Current: `Sorgt für mehr Privatsphäre, indem Sie Ihren Standort beim Surfen verbergen.`
    - Source: `description: Get extra privacy by hiding your location while browsing. label: Built-in VPN`
    - Suggest: `Sorgt für mehr Privatsphäre, indem Ihr Standort beim Surfen verborgen wird.`
    - In en-US the VPN hides the user's location; the German makes the user do the hiding, contradicting the impersonal subject of the main clause.
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
