# Firefox l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `d411ef0407f1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `d411ef0407f1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,521 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (1)

- `main-context-menu-media-video-leave-fullscreen` — `browser/browser/browserContext.ftl` — Access key `j` of `main-context-menu-media-video-leave-fullscreen` is not present in its label
  - Current: `j`
  - The label is “Izhod iz celozaslonskega načina”. An access key not in the label cannot be underlined and is unreachable by keyboard.

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
| Strings | 17,521 |
| Missing strings | 642 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 34 |

### Completeness

**642 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 136
- `browser/browser/aiWindowContent.ftl` — 71
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 48
- `dom/chrome/dom/dom.properties` — 45
- `browser/browser/ipProtection.ftl` — 37
- `browser/browser/newtab/newtab.ftl` — 30
- `browser/browser/aiFeatures.ftl` — 26
- `devtools/client/toolbox-options.ftl` — 24
- `dom/chrome/security/security.properties` — 23
- `browser/browser/preferences/preferences.ftl` — 21
- `toolkit/toolkit/about/aboutNetworking.ftl` — 20
- `devtools/client/debugger.properties` — 17

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 303, `straight-double` 285, `curly-single` 54, `guillemet` 7 | _mixed_ |
| apostrophe | `typographic` 54, `straight` 52 | _mixed_ |
| ellipsis | `char` 420, `ascii` 40 | **char** |
| dash | `em` 13, `en` 150 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 9 | _mixed_ |
| register | `informal` 11, `formal` 605 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 34 strings** — 34 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `Strings.Details`, `Strings.ReportResubmit`, `about-debugging-sidebar-runtime-item-waiting-for-browser`, `about-logins-menu-menuitem-export-logins2`, `browser-languages-downloading`, `browser-languages-search`, `browser-languages-searching`, `choose-other-app-window-title`, `crashreporter-button-details`, `crashreporter-resubmit-status`, `diffing.state.taking-diff`, `diffing.state.taking-diff.full` …and 22 more

---

## 3. Open findings (32)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 24 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

- `main-context-menu-media-video-leave-fullscreen` — `browser/browser/browserContext.ftl` — Access key `j` of `main-context-menu-media-video-leave-fullscreen` is not present in its label
  - Current: `j`
  - The label is “Izhod iz celozaslonskega načina”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — Label is "Copy links in group" but every plural form uses "Zapri" (Close) instead of "Kopiraj" (Copy). The verb is reversed across all variants.

### C. Grammar, agreement & spelling

- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — "Strani a deljenje…" → "Strani za deljenje…".
  - en-US: `"Strani za deljenje…".`
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Last coordinated item not in instrumental to match "se strinjate z … in …". "…in <a>obvestilo o zasebnosti…</a>" → "…in <a>obvestilom…</a>".
- `privacy-metrics-cookies` — `browser/browser/protections.ftl` — privacy-metrics-cookies ([other]) — browser/browser/protections.ftl — "{ $count } sledilnih piškotov" → "…piškotkov" (genitive plural of piškotek).
  - en-US: `"…piškotkov"`
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — Same dual defect: [two]/[few] … zavihkov → zavihka / zavihke.
  - en-US: `zavihka`
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — [two]/[few] forms use genitive plural "zavihkov" instead of the dual/paucal. → [two] … zavihka / [few] … zavihke (the parallel mute string is correct).
  - Current: `[few]`
  - en-US: `[two] … zavihka`
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — security/manager/security/certificates/certManager.ftl — Nonstandard participle "Vnešeno/vnešeno" → "Vneseno/vneseno" (also inconsistent with pippki-incorrect-pw, which is correct).
- `pkcs12-decode-err` — `security/manager/security/certificates/certManager.ftl` — security/manager/security/certificates/certManager.ftl — Nonstandard participle "Vnešeno/vnešeno" → "Vneseno/vneseno" (also inconsistent with pippki-incorrect-pw, which is correct).
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — Wrong case. "…zbirko barvnih kombinacije." → "…kombinacij." (genitive plural).
  - en-US: `"…kombinacij."`
- `touch-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — toolkit/toolkit/about/aboutSupport.ftl — "…zaradi nedpodprte nastavitve…" → "…nepodprte…" (both strings).
  - en-US: `"…nepodprte…"`
- `wheel-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — toolkit/toolkit/about/aboutSupport.ftl — "…zaradi nedpodprte nastavitve…" → "…nepodprte…" (both strings).
  - en-US: `"…nepodprte…"`
- `contentanalysis-slow-agent-dialog-body-file-and-more` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — contentanalysis-slow-agent-dialog-body-file-and-more ([one]) — toolkit/toolkit/contentanalysis/contentanalysis.ftl — Dual verb "sta" with singular adjective "skladen". → "skladna" (dual, agreeing with two subjects).
  - en-US: `"skladna"`

### D. Terminology, register & consistency

- `newtab-section-block-button` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
  - en-US: `standardize on one verb.`
- `newtab-section-block-topic` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
  - en-US: `standardize on one verb.`
- `newtab-section-follow-button` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
  - en-US: `pick one verb.`
- `newtab-section-follow-topic` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
  - en-US: `pick one verb.`
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — onboarding "preizkusiti" vs "preskusiti" — browser/browser/newtab/onboarding.ftl — onboarding-focused-tabs-subtitle / onboarding-genai-sidebar-title use "preskusi(te)"; most siblings use the more common "Preizkusite". → align. (both forms valid; low priority.)
  - en-US: `align.`
- `onboarding-genai-sidebar-title` — `browser/browser/newtab/onboarding.ftl` — onboarding "preizkusiti" vs "preskusiti" — browser/browser/newtab/onboarding.ftl — onboarding-focused-tabs-subtitle / onboarding-genai-sidebar-title use "preskusi(te)"; most siblings use the more common "Preizkusite". → align. (both forms valid; low priority.)
  - en-US: `align.`
- `fonts-langgroup-kannada` — `browser/browser/preferences/fonts.ftl` — "Kannada" (Indic script) rendered "kanadsko" (reads as Canadian, colliding with fonts-langgroup-canadian). → "kannada".
  - en-US: `"kannada".`
- `sync-engine-addresses` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl — Lowercase + accusative ("naslove", "kreditne kartice") break the "Choose what to sync" sibling pattern (Zaznamki, Zgodovina, Gesla…). → "Naslovi", "Kreditne kartice".
  - en-US: `"Naslovi", "Kreditne kartice".`
- `sync-engine-creditcards` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl — Lowercase + accusative ("naslove", "kreditne kartice") break the "Choose what to sync" sibling pattern (Zaznamki, Zgodovina, Gesla…). → "Naslovi", "Kreditne kartice".
  - en-US: `"Naslovi", "Kreditne kartice".`
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — The HTML element name inside <code> was translated: "…imeti <code>naslov</code>." → "<code>title</code>" (every other <code> element name in the file stays English).
  - Current: `<code>`
- `certificate-viewer-certificate-authority` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-certificate-authority (and authority-key-id, authority-info-aia) — toolkit/toolkit/about/certviewer.ftl — "Certificate Authority" rendered "uradna oseba za digitalna potrdila", but the CA tab (certificate-viewer-tab-ca) uses the standard "Overitelji". → align on "overitelj (digitalnih potrdil)".
  - en-US: `align on "overitelj`
- `user-context-color-violet` — `toolkit/toolkit/global/contextual-identity.ftl` — toolkit/toolkit/global/contextual-identity.ftl — Color labels mix gender: most are neuter (Modro, Zeleno, Rumeno, Oranžno, Rdeče, Vijolično) but violet "Vijolična" and gray "Siva" are feminine. In particular purple (Vijolično, neuter) and violet (Vijolična, feminine) clash. → unify gender.
  - Current: `Vijolična`
  - en-US: `unify gender.`
- `language-name-ti` — `toolkit/toolkit/intl/languageNames.ftl` — Tigrinya given the same name as Tigre (language-name-tig = "tigrajščina"). → "tigrinjščina" (must differ from Tigre).
  - en-US: `"tigrinjščina"`

### E. Typography, punctuation & spacing

- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — Double space before "zamenjali".
- `firefox-relay-and-fxa-popup-notification-first-sentence-basic-info` — `browser/browser/firefoxRelay.ftl` — Missing space/preposition before the link → renders "Sporočilatega spletnega mesta". → "Sporočila s <label…>tega spletnega mesta</label>".
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (every other policy description ends with one).
- `inactive-css-not-display-block-on-floated-fix` — `devtools/client/tooltips.ftl` — devtools/client/tooltips.ftl — Missing space before markup: "odstraniti<strong>float</strong>" → "odstraniti <strong>float</strong>" (renders "odstranitifloat").
- `network-connection-status-connecting` — `netwerk/netwerk/necko.ftl` — netwerk/netwerk/necko.ftl — Stray space before the ellipsis: "{ $host } …" → "{ $host }…" (siblings looking-up, sending-request, waiting are correct).
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — btp-warning-tracker-classified ([two]) — toolkit/toolkit/global/antiTracking.ftl — Missing space before the variable: "v naslednjih{ $gracePeriodSeconds } sekundah" → "v naslednjih { $gracePeriodSeconds } sekundah" (the [few]/[other] variants have the space).
  - en-US: `[few]`

---

## 4. Appendix

### Suppressed as false positives (1)

- **`sl-brand-case-params`** (1) — Brand terms carry a `sklon` case parameter; correct Slovenian.
  - `firefox-relay-must-login-to-fxa`

_Suppressions live in `locales/sl/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (42)

- `about-logins-confirm-export-dialog-message2` — `browser/browser/aboutLogins.ftl` — fixed 2026-07-29 (undated)
- `restore-page-problem-desc` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-07-29 (undated)
- `addon-mlmodel-removal-body` — `browser/browser/addonNotifications.ftl` — fixed 2026-07-29 (undated)
- `crashed-subframe-message` — `browser/browser/contentCrash.ftl` — fixed 2026-07-29 (undated)
- `contextual-manager-export-passwords-dialog-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-07-29 (undated)
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — fixed 2026-07-29 (undated)
- `vpn-error-alert-body` — `browser/browser/ipProtection.ftl` — fixed 2026-07-29 (undated)
- `migration-wizard-migrator-display-name-file-password-csv` — `browser/browser/migrationWizard.ftl` — fixed 2026-07-29 (undated)
- `newtab-widget-lists-button-add-item` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-29 (undated)
- `policy-AIControls` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
- `policy-PopupBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
- `connection-proxy-noproxy-desc` — `browser/browser/preferences/connection.ftl` — fixed 2026-07-29 (undated)
- `fxa-qrcode-error-body` — `browser/browser/preferences/fxaPairDevice.ftl` — fixed 2026-07-29 (undated)
- `browser-theme-group` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-29 (undated)
- `protections-panel-site-not-working-view-issue-list-fonts` — `browser/browser/protectionsPanel.ftl` — fixed 2026-07-29 (undated)
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — fixed 2026-07-29 (undated)
- `protections-not-blocking-tracking-content` — `browser/browser/siteProtections.ftl` — fixed 2026-07-29 (undated)
- `accessibility-keyboard-issue-mouse-only` — `devtools/client/accessibility.ftl` — fixed 2026-07-29 (undated)
- `options-disable-http-cache-tooltip` — `devtools/client/toolbox-options.ftl` — fixed 2026-07-29 (undated)
- `xslt-network-error` — `dom/dom/xslt.ftl` — fixed 2026-07-29 (undated)
- `certmgr-edit-cert-trust-email` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-29 (undated)
- `pkcs12-unknown-err-restore` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-29 (undated)
- `devinfo-fwversion` — `security/manager/security/certificates/deviceManager.ftl` — fixed 2026-07-29 (undated)
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — fixed 2026-07-29 (undated)
- `client-auth-cert-details-serial-number` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-07-29 (undated)
- `rights-webservices-term-4` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-07-29 (undated)
- `fission-status-enabled-by-rollout` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-29 (undated)
- `about-telemetry-page-subtitle` — `toolkit/toolkit/about/aboutTelemetry.ftl` — fixed 2026-07-29 (undated)
- `about-webrtc-ice-restart-count-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-07-29 (undated)
- `certificate-viewer-modulus` — `toolkit/toolkit/about/certviewer.ftl` — fixed 2026-07-29 (undated)
- `contentanalysis-slow-agent-dialog-body-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — fixed 2026-07-29 (undated)
- `user-context-color-gray` — `toolkit/toolkit/global/contextual-identity.ftl` — fixed 2026-07-29 (undated)
- `language-name-xh` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-07-29 (undated)
- `region-name-cw` — `toolkit/toolkit/intl/regionNames.ftl` — fixed 2026-07-29 (undated)
- `region-name-tr` — `toolkit/toolkit/intl/regionNames.ftl` — fixed 2026-07-29 (undated)
- `cert-error-symantec-distrust-description` — `toolkit/toolkit/neterror/certError.ftl` — fixed 2026-07-29 (undated)
- `cert-error-trust-cert-invalid` — `toolkit/toolkit/neterror/certError.ftl` — fixed 2026-07-29 (undated)
- `certerror-mitm-what-can-you-do-about-it-corporate` — `toolkit/toolkit/neterror/netError.ftl` — fixed 2026-07-29 (undated)
- `pdfjs-document-properties-page-size-name-legal` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-07-29 (undated)
