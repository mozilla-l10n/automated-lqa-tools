# Firefox l10n QA — de

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b95608d528c8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `d411ef0407f1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,131 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

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
| Files | 360 |
| Strings | 18,131 |
| Missing strings | 32 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 2 |
| Markup & `data-l10n-name` defects | 1 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**32 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 4
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

**Files present but identical to en-US:**

- `toolkit/toolkit/about/aboutMozilla.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 810, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 120 | **straight** |
| ellipsis | `char` 465 | **char** |
| dash | `em` 16, `en` 87 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 4235 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (40)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 10 |
| 2 | Wrong content (says something other than the English) | 6 |
| 3 | Degraded language (grammar, spelling, terminology) | 24 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — Malformed closing tag `</span >` in `about-logins-import-dialog-items-no-change2`
  - Current: `{$count ->} [one] <span>Doppelte Einträge gefunden:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(nicht importiert)</span > [other] <span>Doppelte Einträge gefunden:</span> <span dat…`
  - en-US: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
  - Whitespace inside a closing tag makes it render as literal text.
- `appmenuitem-new-window` — `browser/browser/appmenu.ftl` — appmenuitem-new-window (.label) — browser/browser/appmenu.ftl:27 — stray soft hyphen U+00AD before "Neues Fenster" (byte-confirmed c2 ad). Remove it.
  - en-US: `.label`
- `toolbar-button-email-link` — `browser/browser/browser.ftl` — browser/browser/browser.ftl:1389,1413,1418 — each has a stray leading soft hyphen U+00AD.
- `toolbar-button-open-file` — `browser/browser/browser.ftl` — browser/browser/browser.ftl:1389,1413,1418 — each has a stray leading soft hyphen U+00AD.
- `toolbar-button-save-page` — `browser/browser/browser.ftl` — browser/browser/browser.ftl:1389,1413,1418 — each has a stray leading soft hyphen U+00AD.
- `urlbar-result-market-opt-in-description` — `browser/browser/browser.ftl` — starts with a stray acute accent U+00B4: ´Markt-Updates…. Remove it.
- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-link-send-to-device` is not present in its label
  - Current: `X`
  - The label is “Link an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `main-context-menu-send-to-device` — `browser/browser/browserContext.ftl` — Access key `X` of `main-context-menu-send-to-device` is not present in its label
  - Current: `X`
  - The label is “Seite an Gerät senden”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — browser/browser/genai.ftl:8,9 — missing space around <a>: Datenschutzerklärung</a>von OpenAI → </a> von; und der<a …> → und der <a.
- `menu-file-new-window` — `browser/browser/menubar.ftl` — same stray soft hyphen U+00AD before "Neues Fenster".
- `webauthn-uv-invalid-long-prompt` — `browser/browser/webauthnDialog.ftl` — the [one]/[other] plural variants are swapped ([one] shows "Versuche" plural, [other] shows "Versuch" singular). Swap them (cf. correct webauthn-pin-invalid-long-prompt).
  - Current: `[one]`
  - en-US: `[other]`
- `pdfjs-text-annotation-type` — `toolkit/toolkit/pdfviewer/viewer.ftl` — pdfjs-text-annotation-type (.alt) — toolkit/toolkit/pdfviewer/viewer.ftl:302 — see C (mistranslation).
  - en-US: `.alt`

### B. Mistranslation, reversed meaning, wrong names & brand

- `ipprotection-message-bandwidth-warning-mb` — `browser/browser/ipProtection.ftl` — ipprotection-message-bandwidth-warning-mb (.message) — browser/browser/ipProtection.ftl:201 — untranslated English: "…{ $usageLeft } MB of { $maxUsage } GB…" → "MB von GB" (the GB variant at line 195 uses "von").
  - en-US: `"MB von GB"`
- `newtab-sports-widget-suspended` — `browser/browser/newtab/newtab.ftl` — DE: "Gesperrt" (= locked/banned) → "Unterbrochen" (EN match status "Suspended"; the aria-label at line 1498 already uses "unterbrochen").
  - en-US: `"Unterbrochen"`
- `preferences-etp-level-standard` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-standard (.label) — browser/browser/preferences/preferences.ftl:2674 — DE: "Standard" drops the "(default)" marker present in EN "Standard (default)" → e.g. "Standard (Voreinstellung)".
  - en-US: `e.g. "Standard`
- `pdfjs-text-annotation-type` — `toolkit/toolkit/pdfviewer/viewer.ftl` — pdfjs-text-annotation-type (.alt) — toolkit/toolkit/pdfviewer/viewer.ftl:302 — DE: "[Anlage: { $type }]" (= attachment) → "[{ $type }-Anmerkung]" (EN "annotation"; "Anmerkung" is used elsewhere in the file).
  - en-US: `"[{ $type }-Anmerkung]"`

### C. Grammar, agreement & spelling

- `urlbar-web-notifications-blocked` — `browser/browser/browser.ftl` — urlbar-web-notifications-blocked (.tooltiptext) — browser/browser/browser.ftl:306 — "Benachrichtungen" → "Benachrichtigungen".
  - en-US: `"Benachrichtigungen".`
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — genai-shortcuts-selected-warning (.message, both plural forms) — browser/browser/genai.ftl:95,96 — "ist ewa { $maxLength }" → "etwa" (cf. lines 85/86).
  - en-US: `"etwa"`
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — ip-protection-description-1 (.description) — browser/browser/ipProtection.ftl:236 — "ihren Standort" → "Ihren".
  - en-US: `"Ihren".`
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — "geblockierter/geblockierte Tracker" → "blockierter/blockierte".
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — containers-card-header2 (.description) — browser/browser/preferences/preferences.ftl:1211 — "das Seitenübergreifende Tracking" → "seitenübergreifende".
  - en-US: `"seitenübergreifende".`
- `containers-disable-alert-title` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:309,324 — "Alle Tabs im Umgebungen schließen" → "in Umgebungen" (plural; cf. line 319).
  - en-US: `"in Umgebungen"`
- `containers-remove-alert-msg` — `browser/browser/preferences/preferences.ftl` — containers-remove-alert-msg ([other]) — browser/browser/preferences/preferences.ftl:336 — plural branch uses singular "{ $count } Tab" → "Tabs".
  - en-US: `"Tabs".`
- `preferences-etp-custom-cookie-behavior-block-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — preferences-etp-custom-cookie-behavior-block-all-cross-site-cookies (.label) — browser/browser/preferences/preferences.ftl:2734 — "Alle Seitenübergreifenden Cookies" → "seitenübergreifenden".
  - en-US: `"seitenübergreifenden".`
- `info-known-breaches-resolved` — `browser/browser/protections.ftl` — info-known-breaches-resolved ([one]) — browser/browser/protections.ftl:117 — "bekanntes Datenlecks" → "bekanntes Datenleck" (singular).
  - en-US: `"bekanntes Datenleck"`
- `duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — duplicate-tabs2 (.label) — browser/browser/tabContextMenu.ftl:37 — menu label "duplizieren" → "Duplizieren" (cf. duplicate-tab2 line 31).
- `tab-group-editor-color-selector` — `browser/browser/tabbrowser.ftl` — tab-group-editor-color-selector (.aria-label) — browser/browser/tabbrowser.ftl:246 — "Farbe der Tap-Gruppe" → "Tab-Gruppe".
  - en-US: `"Tab-Gruppe".`
- `tabbrowser-mute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — tabbrowser-mute-tab-audio-background-tooltip ([other]) — browser/browser/tabbrowser.ftl:77 — "{ $tabCount } Tab stummschalten" → "Tabs".
  - en-US: `"Tabs".`
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — browser/browser/tabbrowser.ftl:71,83 — misplaced variable: "Stummschaltung { $tabCount } für Tabs aufheben" → "Stummschaltung für { $tabCount } Tabs aufheben".
  - en-US: `"Stummschaltung für { $tabCount } Tabs aufheben".`
- `third-party-detail-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — third-party-detail-duration (.title) — toolkit/toolkit/about/aboutThirdParty.ftl:18 — "dieses Module" (sing. det. + plural noun) → "dieses Modul".
  - en-US: `"dieses Modul".`
- `about-webrtc-fold-default-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — toolkit/toolkit/about/aboutWebrtc.ftl:157,159 — same lowercase error → capitalize.
  - en-US: `capitalize.`
- `about-webrtc-log-section-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — toolkit/toolkit/about/aboutWebrtc.ftl:112,114 — "Zum erweitern des abschnitts" → "Zum Erweitern des Abschnitts" (nominalized verb + noun; cf. 108/110).
  - en-US: `"Zum Erweitern des Abschnitts"`
- `about-webrtc-raw-local-candidate` — `toolkit/toolkit/about/aboutWebrtc.ftl` — toolkit/toolkit/about/aboutWebrtc.ftl:141,142 — over-capitalized adjective: "Unformatierte Lokale / Externe Kandidaten" → "lokale / externe".

### D. Terminology, register & consistency

- `newtab-sports-widget-cancelled` — `browser/browser/newtab/newtab.ftl` — "Abgebrochen" vs aria-label "abgesagt" (1501) for "Cancelled"; align (EN "Cancelled" ≈ "Abgesagt").
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — "(RSP)" → "(RFP)" (comment: keep "Resist Fingerprinting (RFP)"; also a double space before "zum").
  - en-US: `"`
- `network-proxy-connection-description` — `browser/browser/preferences/preferences.ftl` — adds "Jetzt" not in source; newer sibling uses "Konfigurieren Sie…".
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — "(RSP)" → "(RFP)" (comment: keep "Resist Fingerprinting (RFP)"; also a double space before "zum").
  - en-US: `"`
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — manifest-icon-img-title-no-sizes region — devtools/client/toolbox-options.ftl:86 — panel called both "Netzwerkmonitor" and "Netzwerkanalyse" (section heading, line 82); align.
- `sidebar-item-session-history` — `devtools/client/application.ftl` — sidebar-item-session-history (.alt) — devtools/client/application.ftl:115 — "Icon für Chronik" → "Symbol für Sitzungsverlauf" ("Symbol" like siblings; label of the item is "Sitzungsverlauf").
  - en-US: `"Symbol für Sitzungsverlauf"`
- `xslt-bad-value` — `dom/dom/xslt.ftl` — "Chronik" is the established term.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (35)

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
- `ssl-error-handshake-not-completed` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-27
- `remove-info` — `toolkit/toolkit/preferences/preferences.ftl` — fixed 2026-07-27
