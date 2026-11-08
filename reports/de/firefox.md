# Firefox l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-08 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `363d50704369` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-05 @ `324a294b9f2a` |
| **Mode** | incremental |
| **Strings reviewed this run** | 45 of 17,104 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (1)

- `EditContextCharacterBoundsWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate event name "characterboundsupdate" is misspelled as "charactersboundsupdate".
    - Current: `charactersboundsupdate-Ereignis-Listener`
    - Source: `EditContext.updateCharacterBounds() was not called synchronously in characterboundsupdate event listener. IME interface may move around unexpectedly for some users. More information: https://developer.mozilla.org/docs/W…`
    - Suggest: `characterboundsupdate-Ereignis-Listener`
    - The developer comment says not to translate "characterboundsupdate". It is a DOM event name, and the extra "s" turns it into an event that does not exist, which misleads developers reading the console warning.

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
| Files | 341 |
| Strings | 17,104 |
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

_229 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 750, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 115 | **straight** |
| ellipsis | `char` 416 | **char** |
| dash | `em` 19, `en` 70 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 4056 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (28)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 16 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
| 4 | Cosmetic (typography, spacing) | 2 |

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
- `restart-required-why-now-answer` — `browser/browser/aboutRestartRequired.ftl` — Brand placeable replaced with hardcoded "Firefox" in the first occurrence.
    - Current: `wenn ein anderes Firefox-Profil`
    - Source: `This can happen when another { -brand-short-name } profile or instance updates, or when an update can’t wait until your next restart.`
    - Suggest: `wenn ein anderes { -brand-short-name }-Profil`
    - The en-US uses { -brand-short-name } for the profile reference; hardcoding "Firefox" breaks brand substitution for other builds.
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
- `policy-PasswordManagerEnabled2` — `browser/browser/policies/policies-descriptions.ftl` — The German says using passwords is blocked, but the source means the Passwords page (about:logins) is blocked.
    - Current: `wird die Verwendung von Passwörtern (about:logins) ebenfalls blockiert`
    - Source: `Enable or disable saving passwords to the password manager. If disabled, Passwords (about:logins) is also blocked.`
    - Suggest: `wird die Seite Passwörter (about:logins) ebenfalls blockiert`
    - In en-US, "Passwords (about:logins)" is the name of the Passwords page, and the policy blocks that page. "Die Verwendung von Passwörtern" means using passwords in general, which describes a broader effect than the policy has.
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
- `search-engine-list` — `browser/browser/preferences/preferences.ftl` — "shortcuts" (search shortcuts/keywords) is rendered as "Tastenkombinationen" (keyboard shortcuts).
    - Current: `Suchmaschinen und Tastenkombinationen`
    - Source: `aria-label: Search engines and shortcuts`
    - Suggest: `Suchmaschinen und Suchverknüpfungen`
    - The list in search preferences contains search engines and search shortcuts (e.g. @bookmarks keywords), not keyboard combinations; "Tastenkombinationen" names the wrong thing for screen reader users.
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — The tooltip turns the adjective "Open" into an imperative ("Öffnen Sie Tabs").
    - Current: `Öffnen Sie Tabs von Ihren anderen Geräten`
    - Source: `accesskey: t label: Open tabs tooltiptext: Open tabs from your other devices`
    - Suggest: `Offene Tabs von Ihren anderen Geräten`
    - The developer comment says "Open" modifies the noun (tabs that are open), so it is not an instruction to open tabs.
- `sync-syncing-across-devices-heading-3` — `browser/browser/preferences/preferences.ftl` — "Data syncing on this device" translated as "Auf diesem Gerät synchronisierte Daten" (data already synced), changing the heading's meaning.
    - Current: `Auf diesem Gerät synchronisierte Daten`
    - Source: `Data syncing on this device`
    - Suggest: `Datensynchronisation auf diesem Gerät`
    - The source is about the ongoing syncing of data on this device, not a list of data that has been synced; the German past participle asserts completed action.
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — "Tabs duplizieren" means "duplicate (copy) tabs" instead of naming the duplicate tabs that get closed.
    - Current: `Tabs duplizieren`
    - Source: `accesskey: x label: Duplicate Tabs`
    - Suggest: `Doppelte Tabs`
    - The developer comment says this item closes duplicate tabs in the "Close Multiple" menu. "Duplicate" is an adjective here, but it was translated as a verb (to copy).
- `statePartiallyChecked` — `dom/chrome/accessibility/AccessFu.properties` — "partially checked" is translated as "teilweise ausgewählt" (partially selected) instead of "teilweise aktiviert/angekreuzt".
    - Current: `teilweise ausgewählt`
    - Source: `partially checked`
    - Suggest: `teilweise aktiviert`
    - The accessibility state refers to a checkbox being checked, not selected; "ausgewählt" is the German term for "selected", a distinct accessibility state.
- `EditContextCharacterBoundsWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate event name "characterboundsupdate" is misspelled as "charactersboundsupdate".
    - Current: `charactersboundsupdate-Ereignis-Listener`
    - Source: `EditContext.updateCharacterBounds() was not called synchronously in characterboundsupdate event listener. IME interface may move around unexpectedly for some users. More information: https://developer.mozilla.org/docs/W…`
    - Suggest: `characterboundsupdate-Ereignis-Listener`
    - The developer comment says not to translate "characterboundsupdate". It is a DOM event name, and the extra "s" turns it into an event that does not exist, which misleads developers reading the console warning.
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

### C. Grammar, agreement & spelling

- `sync-engine-settings2` — `browser/browser/preferences/preferences.ftl` — The compound of brand name and "Einstellungen" is missing its hyphen.
    - Current: `{ -brand-short-name } Einstellungen`
    - Source: `accesskey: s label: Settings tooltiptext: { -brand-short-name } settings where applicable`
    - Suggest: `{ -brand-short-name }-Einstellungen`
    - German spelling requires a hyphenated compound here (e.g. "Firefox-Einstellungen"), and the de locale uses that form elsewhere.
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — "denselben … als" is ungrammatical; the comparison after "derselbe" takes "wie".
    - Current: `denselben Ursprung (origin) als das Dokument`
    - Source: `The scope URL must be same origin as document.`
    - Suggest: `denselben Ursprung (origin) wie das Dokument`
    - German uses "derselbe … wie" for comparisons of identity. "als" is wrong here. The sibling string dom-manifest-id-not-same-origin correctly uses "wie".
- `dom-manifest-start-url-should-be-same-origin` — `dom/dom/manifest.ftl` — "denselben … als" is ungrammatical; the comparison after "derselbe" takes "wie".
    - Current: `denselben Ursprung (origin) als das Dokument`
    - Source: `The start URL must be same origin as document.`
    - Suggest: `denselben Ursprung (origin) wie das Dokument`
    - German uses "derselbe … wie" for comparisons of identity. "als" is wrong here.

### D. Terminology, register & consistency

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — "share Firefox" is rendered as "Teilen Sie Firefox" here but as "Firefox empfehlen" in all other referral strings of this batch.
    - Current: `Teilen Sie { -brand-product-name }`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `empfehlen Sie { -brand-product-name }`
    - The developer comments for the parallel referral strings state that "Share" means recommending/referring the browser; the de tree consistently uses "empfehlen", so "Teilen" (file sharing sense) is inconsistent and misleading.
- `close-tabs-to-the-end-alt` — `browser/browser/tabContextMenu.ftl` — The label adds a redundant "schließen" inside the "Close Multiple" submenu and doesn't match its sibling "Tabs links davon".
    - Current: `Tabs rechts schließen`
    - Source: `accesskey: i label: Tabs to Right`
    - Suggest: `Tabs rechts davon`
    - The source is "Tabs to Right", parallel to "Tabs to Left" ("Tabs links davon"). The verb is already in the parent menu.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “Lokalen Modus” but the string it names, `options-local-mode-label`, reads “Lokaler Modus”
    - Current: `Dieses Dokument kann auch über den "Lokalen Modus" der DevTools von "{ $url }" geladen werden, der im Einstellungsbereich aktiviert werden kann.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Lokaler Modus`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Descriptive label rendered as an imperative addressed to the user instead of a noun-phrase description of the preset.
    - Current: `Protokollieren Sie Module zur Diagnose`
    - Source: `Log modules to diagnose IP Protection (VPN) issues`
    - Suggest: `Module zur Diagnose von Problemen mit dem IP-Schutz (VPN) protokollieren`
    - The en-US "Log modules to diagnose…" is a preset description, not an instruction to the user; sibling preset descriptions use an infinitive/noun phrase.
- `download-ui-confirm-quit-title` — `toolkit/toolkit/downloads/downloadUI.ftl` — "Stop" is rendered as "abbrechen" (cancel) in one variant, while the other variants of the same message use "anhalten"/"stoppen".
    - Current: `1 Download abbrechen und { -brand-short-name } beenden?`
    - Source: `{$sel_1, downloadsCount ->} [windows 1] Stop 1 download and exit { -brand-short-name }? [windows other] Stop { $downloadsCount } downloads and exit { -brand-short-name }? [other 1] Stop 1 download and quit { -brand-shor…`
    - Suggest: `1 Download stoppen und { -brand-short-name } beenden?`
    - The en-US uses "Stop" in every variant, and the follow-up message says the download will be resumed. "abbrechen" means cancel, which contradicts that. The other macOS/Linux variants use "stoppen".

### E. Typography, punctuation & spacing

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — Superfluous comma before "oder" in the enumeration.
    - Current: `Teilen Sie { -brand-product-name }</label>, oder`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `Teilen Sie { -brand-product-name }</label> oder`
    - German does not use a comma before "oder" joining the last item of a simple enumeration; the comma is a direct carry-over of the English serial comma.
- `ip-protection-site-rules-button-1` — `browser/browser/ipProtection.ftl` — There is a comma before "oder", which German doesn't use when "oder" joins two noun phrases.
    - Current: `mehr Datenschutz, oder ein deaktiviertes VPN`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage VPN rules`
    - Suggest: `mehr Datenschutz oder ein deaktiviertes VPN`
    - German doesn't put a comma before "oder" when it joins two objects of the same verb. The en-US source has no comma here either.

---

## 4. Appendix

### Dismissed by hand (8)

- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon: d3_a_WJBXT7jM9HiCUG3-gcQQl0: <p>This translation ignores the word "your" in the original string.</p>
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — auto-suggest (2026-11-02): The quoted label refers to the Windows 10 Settings > Default apps entry, which German Windows displays as "Webbrowser", not to Firefox's desktop-entry-generic-name.
- `migration-chrome-windows-password-import-step3` — `browser/browser/migrationWizard.ftl` — auto-suggest (2026-11-02): The step describes Chrome's own password-export button, not Firefox's downloadFile.label, so matching Firefox's 'Datei speichern unter…' would be wrong.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — pontoon-rejected (2026-11-03): rejected in Pontoon: d3_a_WJBXT7jM9HiCUG3-gcQQl0: <p>"Persist Logs" is a plural form in my opinion.</p>
- `translations-panel-revisit-to-label` — `browser/browser/translations.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; reason unclear
- `user-context-personal2` — `toolkit/toolkit/global/contextual-identity.ftl` — auto-suggest (2026-11-02): "Freizeit" is the long-established German Firefox name for the Personal container (paired with "Arbeit" for Work). It is a deliberate localization choice that keeps the private-vs-work contrast, not a mistranslation.
- `xslt-bad-value` — `dom/dom/xslt.ftl` — auto-suggest (2026-11-02): The string is an XSLT attribute-value error and contains no history term, so "Chronik" is irrelevant.

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

### Fixed to date (58)

- `newtab-wallpaper-firefox-sky-light` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — fixed 2026-11-05
- `restart-required-see-more-button` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-11-03
- `appmenu-fxa-sign-in-promo-link` — `browser/browser/appmenu.ftl` — fixed 2026-11-03
- `content-analysis-indicator-tooltip` — `browser/browser/browser.ftl` — fixed 2026-11-03
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — fixed 2026-11-03
- `ip-protection-site-rules-button-1` — `browser/browser/ipProtection.ftl` — fixed 2026-11-03
- `ipprotection-site-inclusions-callout-description-lapsed-users` — `browser/browser/ipProtection.ftl` — fixed 2026-11-03
- `onboarding-refresh-fro-import-header` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-03
- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-03
- `speech-recognition-model-download-progress-message` — `browser/browser/permissions.ftl` — fixed 2026-11-03
- `policy-PasswordManagerEnabled2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-03
- `more-from-moz-firefox-enterprise-card` — `browser/browser/preferences/moreFromMozilla.ftl` — fixed 2026-11-03
- `addressbar-skip-result-menu-on-tab` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-03
- `splitter.label` — `devtools/client/components.properties` — fixed 2026-11-03
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — fixed 2026-11-03
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
