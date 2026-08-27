# Firefox l10n QA — de

| | |
|---|---|
| **Generated** | 2026-08-27 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `caafd8e1597e` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 36 of 18,397 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (11)

- `blocked-by-policy-title-enterprise` — `browser/browser/enterprise/enterprise.ftl` — Wrong preposition: "Zugriff zu" instead of "Zugriff auf".
    - Current: `Der Zugriff zu dieser Website ist eingeschränkt`
    - Suggest: `Der Zugriff auf diese Website ist eingeschränkt`
    - German requires "Zugriff auf" (as used correctly in enterprise-access-connector-info-active and neterror-blocked-by-policy-contact-admin); "Zugriff zu" is ungrammatical.
- `enterprise-close-prompt-message-reauth` — `browser/browser/enterprise/enterprise.ftl` — Acronym "SSO" is misspelled as "SSo".
    - Current: `SSo-Anbieter`
    - Suggest: `SSO-Anbieter`
    - The same acronym is correctly written "SSO-Anbieter" in enterprise-quit-shortcut-prompt-message; "SSo" is a spelling error in a proper acronym.
- `neterror-blocked-by-policy-page-title-enterprise` — `browser/browser/enterprise/enterprise.ftl` — Wrong preposition: "Zugriff zu" instead of "Zugriff auf".
    - Current: `Der Zugriff zu dieser Website ist eingeschränkt`
    - Suggest: `Der Zugriff auf diese Website ist eingeschränkt`
    - German requires "Zugriff auf"; "Zugriff zu" is ungrammatical and inconsistent with other strings in the same file.
- `restart-forced-heading` — `browser/browser/enterprise/enterprise.ftl` — Sentence fragment with stray period; a heading like "Restart to keep using …" should be an infinitive clause without final period.
    - Current: `Neustart, um { -brand-short-name } weiterhin zu verwenden.`
    - Suggest: `Neu starten, um { -brand-short-name } weiterhin zu verwenden`
    - The heading mixes a noun ("Neustart") with an infinitive purpose clause, which is ungrammatical, and headings do not take a final period.
- `felt-sso-input-email` — `browser/browser/enterprise/felt.ftl` — Label "E-Mail-Adresse dienstlich" has inverted word order for a field label.
    - Current: `label: E-Mail-Adresse dienstlich`
    - Suggest: `label: Dienstliche E-Mail-Adresse`
    - The adjective must precede the noun in German; "E-Mail-Adresse dienstlich" is ungrammatical as a form label for a work email address.
- `felt-updates-title` — `browser/browser/enterprise/felt.ftl` — Title for the updates panel reads "Guten Morgen" ("Good morning"), which is unrelated to updates.
    - Current: `Guten Morgen`
    - Suggest: `Updates`
    - String id felt-updates-title belongs to the update UI alongside felt-updates-checking/-application/-uptodate; a greeting "Guten Morgen" asserts something the update panel never said and is clearly not an update title.
- `blocked-by-policy-title-enterprise` — `toolkit/toolkit/enterprise/enterprise.ftl` — Wrong preposition: "Zugriff" governs "auf", not "zu".
    - Current: `Der Zugriff zu dieser Website ist eingeschränkt`
    - Suggest: `Der Zugriff auf diese Website ist eingeschränkt`
    - German requires "Zugriff auf" + accusative; "Zugriff zu dieser Website" is grammatically incorrect.
- `enterprise-close-prompt-message-with-tabcount` — `toolkit/toolkit/enterprise/enterprise.ftl` — String named "...-with-tabcount" lacks the plural selector and $tabCount variable present in its counterpart, so the tab count is never shown.
    - Current: `Wenn Sie { -brand-short-name } schließen, werden Sie ebenfalls abgemeldet.`
    - Suggest: `{$tabCount ->} [one] Wenn Sie { -brand-short-name } und { $tabCount } Tab schließen, werden Sie ebenfalls abgemeldet. [other] Wenn Sie { -brand-short-name } und { $tabCount } Tabs schließen, werden Sie ebenfalls abgemel…`
    - All other "-with-tabcount" IDs in this file use the $tabCount plural selector; here the count is dropped entirely, so the message does not convey how many tabs are affected.
- `neterror-blocked-by-policy-page-title-enterprise` — `toolkit/toolkit/enterprise/enterprise.ftl` — Wrong preposition: "Zugriff" requires "auf", not "zu".
    - Current: `Der Zugriff zu dieser Website ist eingeschränkt`
    - Suggest: `Der Zugriff auf diese Website ist eingeschränkt`
    - German "Zugriff" governs "auf" + accusative; "Zugriff zu dieser Website" is ungrammatical, and the same file uses "Zugriff auf diese Website" elsewhere.
- `felt-sso-input-email` — `toolkit/toolkit/enterprise/felt.ftl` — Label "E-Mail-Adresse dienstlich" has reversed/ungrammatical word order for a form label.
    - Current: `label: E-Mail-Adresse dienstlich`
    - Suggest: `label: Dienstliche E-Mail-Adresse`
    - An attributive adjective must precede the noun in German; the postposed "dienstlich" is not grammatical German for a field label ("work email").
- `felt-updates-application` — `toolkit/toolkit/enterprise/felt.ftl` — "Updates anwenden…" states an action to perform rather than the ongoing progress "Applying updates…".
    - Current: `Updates anwenden…`
    - Suggest: `Updates werden angewendet…`
    - The surrounding progress strings ("Nach Updates suchen…") describe an in-progress update flow; the infinitive form reads as a command/menu item instead of a status message.

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 372 |
| Strings | 18,397 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 7 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 2 |
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

_187 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 811, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 120 | **straight** |
| ellipsis | `char` 476 | **char** |
| dash | `em` 16, `en` 95 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 4380 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (16)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 11 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-link-send-to-device` is not present in its label
    - Current: `X`
    - Source: `accesskey: n label: Send Link to Device`
    - The label is “Link an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `main-context-menu-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-send-to-device` is not present in its label
    - Current: `X`
    - Source: `accesskey: n label: Send Page to Device`
    - The label is “Seite an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — The [one] plural variant uses the plural form "Aktien" instead of the singular "Aktie".
    - Current: `[one] Sie können bis zu { $limit } Aktien hinzufügen.`
    - Source: `{$limit ->} [one] You can add up to { $limit } stock. Remove one to add another. [other] You can add up to { $limit } stocks. Remove one to add another.`
    - Suggest: `[one] Sie können bis zu { $limit } Aktie hinzufügen.`
    - en-US [one] uses the singular "stock"; the German singular variant must agree with $limit = 1.

### B. Mistranslation, reversed meaning, wrong names & brand

- `statePartiallyChecked` — `dom/chrome/accessibility/AccessFu.properties` — "partially checked" is translated as "teilweise ausgewählt" (partially selected) instead of "teilweise aktiviert/angekreuzt".
    - Current: `teilweise ausgewählt`
    - Source: `partially checked`
    - Suggest: `teilweise aktiviert`
    - The accessibility state refers to a checkbox being checked, not selected; "ausgewählt" is the German term for "selected", a distinct accessibility state.

### C. Grammar, agreement & spelling

- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — ip-protection-description-1 (.description) — browser/browser/ipProtection.ftl:236 — "ihren Standort" → "Ihren".
    - Source: `description: Get extra privacy by hiding your location while browsing. label: Built-in VPN`
    - Suggest: `"Ihren".`
- `containers-sites-card-header` — `browser/browser/preferences/preferences.ftl` — Pronoun does not agree with the feminine noun "Tab-Umgebung".
    - Current: `verwendet ihn jedes Mal`
    - Source: `description: Choose a container for a site and { -brand-short-name } will use it every time the site opens. label: Site-specific containers`
    - Suggest: `verwendet sie jedes Mal`
    - "Tab-Umgebung" is feminine, so the referring pronoun must be "sie", not "ihn".

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
- `preventedConsoleClear` — `devtools/client/webconsole.properties` — `preventedConsoleClear` quotes “Logs nicht leeren” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “Log nicht leeren”
    - Current: `console.clear() wurde aufgrund von "Logs nicht leeren" verhindert`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `Log nicht leeren`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
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

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (11)

- `blocked-by-policy-title-enterprise` — `browser/browser/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `enterprise-close-prompt-message-reauth` — `browser/browser/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `neterror-blocked-by-policy-page-title-enterprise` — `browser/browser/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `restart-forced-heading` — `browser/browser/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `felt-sso-input-email` — `browser/browser/enterprise/felt.ftl` — raised by `llm`, withdrawn 2026-08-27
- `felt-updates-title` — `browser/browser/enterprise/felt.ftl` — raised by `llm`, withdrawn 2026-08-27
- `blocked-by-policy-title-enterprise` — `toolkit/toolkit/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `enterprise-close-prompt-message-with-tabcount` — `toolkit/toolkit/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `neterror-blocked-by-policy-page-title-enterprise` — `toolkit/toolkit/enterprise/enterprise.ftl` — raised by `llm`, withdrawn 2026-08-27
- `felt-sso-input-email` — `toolkit/toolkit/enterprise/felt.ftl` — raised by `llm`, withdrawn 2026-08-27
- `felt-updates-application` — `toolkit/toolkit/enterprise/felt.ftl` — raised by `llm`, withdrawn 2026-08-27

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (71)

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `appmenuitem-new-window` — `browser/browser/appmenu.ftl` — fixed 2026-08-24
- `toolbar-button-email-link` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `toolbar-button-open-file` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `toolbar-button-save-page` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `urlbar-result-market-opt-in-description` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `urlbar-web-notifications-blocked` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — fixed 2026-08-24
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — fixed 2026-08-24
- `ipprotection-message-bandwidth-warning-mb` — `browser/browser/ipProtection.ftl` — fixed 2026-08-24
- `menu-file-new-window` — `browser/browser/menubar.ftl` — fixed 2026-08-24
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-sports-widget-cancelled` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-sports-widget-suspended` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `containers-disable-alert-title` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `containers-remove-alert-msg` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `network-proxy-connection-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-custom-cookie-behavior-block-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-level-standard` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `info-known-breaches-resolved` — `browser/browser/protections.ftl` — fixed 2026-08-24
- `duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — fixed 2026-08-24
- `tab-group-editor-color-selector` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `tabbrowser-mute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `webauthn-uv-invalid-long-prompt` — `browser/browser/webauthnDialog.ftl` — fixed 2026-08-24
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — fixed 2026-08-24
- `sidebar-item-session-history` — `devtools/client/application.ftl` — fixed 2026-08-24
- `third-party-detail-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — fixed 2026-08-24
- `about-webrtc-fold-default-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-08-24
- `about-webrtc-log-section-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-08-24
- `about-webrtc-raw-local-candidate` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-08-24
- `pdfjs-text-annotation-type` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-08-24
- `pdfjs-text-annotation-type` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-08-24
- `pocket-panel-saved-error-tag-length` — `browser/browser/aboutPocket.ftl` — fixed 2026-07-27
- `site-permission-install-first-prompt-midi-message` — `browser/browser/addonNotifications.ftl` — fixed 2026-07-27
- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `content-sharing-modal-sign-in-2` — `browser/browser/contentSharing.ftl` — fixed 2026-07-27
