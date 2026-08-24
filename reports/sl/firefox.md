# Firefox l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `907043d6ea4b` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `50d2f3b3f7c8` |
| **Previous run** | 2026-08-24 @ `39e5663f3de7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 17,550 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (1)

- `pkcs12-decode-err` — `security/manager/security/certificates/certManager.ftl` — security/manager/security/certificates/certManager.ftl — Nonstandard participle "Vnešeno/vnešeno" → "Vneseno/vneseno" (also inconsistent with pippki-incorrect-pw, which is correct).
    - Source: `Failed to decode the file. Either it is not in PKCS #12 format, has been corrupted, or the password you entered was incorrect.`

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
| Strings | 17,550 |
| Missing strings | 630 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 34 |

### Completeness

**630 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 136
- `browser/browser/aiWindowContent.ftl` — 71
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 48
- `dom/chrome/dom/dom.properties` — 45
- `browser/browser/ipProtection.ftl` — 37
- `browser/browser/newtab/newtab.ftl` — 28
- `browser/browser/aiFeatures.ftl` — 26
- `devtools/client/toolbox-options.ftl` — 24
- `dom/chrome/security/security.properties` — 23
- `toolkit/toolkit/about/aboutNetworking.ftl` — 20
- `browser/browser/preferences/preferences.ftl` — 19
- `devtools/client/debugger.properties` — 17

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 303, `straight-double` 285, `curly-single` 54, `guillemet` 7 | _mixed_ |
| apostrophe | `typographic` 54, `straight` 52 | _mixed_ |
| ellipsis | `char` 421, `ascii` 40 | **char** |
| dash | `em` 13, `en` 150 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 9 | _mixed_ |
| register | `informal` 11, `formal` 605 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 34 strings** — 34 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `Strings.Details`, `Strings.ReportResubmit`, `about-debugging-sidebar-runtime-item-waiting-for-browser`, `about-logins-menu-menuitem-export-logins2`, `browser-languages-downloading`, `browser-languages-search`, `browser-languages-searching`, `choose-other-app-window-title`, `crashreporter-button-details`, `crashreporter-resubmit-status`, `diffing.state.taking-diff`, `diffing.state.taking-diff.full` …and 22 more

---

## 3. Open findings (33)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 22 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

- `main-context-menu-media-video-leave-fullscreen` — `browser/browser/browserContext.ftl` — Access key `j` of `main-context-menu-media-video-leave-fullscreen` is not present in its label
    - Current: `j`
    - Source: `accesskey: u label: Exit Full Screen`
    - The label is “Izhod iz celozaslonskega načina”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — "Strani a deljenje…" → "Strani za deljenje…".
    - Source: `heading: Something went wrong message: We couldn’t create your shared page this time. Try again later.`
    - Suggest: `"Strani za deljenje…".`
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Last coordinated item not in instrumental to match "se strinjate z … in …". "…in <a>obvestilo o zasebnosti…</a>" → "…in <a>obvestilom…</a>".
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
- `privacy-metrics-cookies` — `browser/browser/protections.ftl` — privacy-metrics-cookies ([other]) — browser/browser/protections.ftl — "{ $count } sledilnih piškotov" → "…piškotkov" (genitive plural of piškotek).
    - Source: `{$count ->} [one] { $count } tracking cookie [other] { $count } tracking cookies`
    - Suggest: `"…piškotkov"`
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — Same dual defect: [two]/[few] … zavihkov → zavihka / zavihke.
    - Source: `label: {$tabCount ->} [one] Unmute tab [other] Unmute { $tabCount } tabs`
    - Suggest: `zavihka`
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — [two]/[few] forms use genitive plural "zavihkov" instead of the dual/paucal. → [two] … zavihka / [few] … zavihke (the parallel mute string is correct).
    - Current: `[few]`
    - Source: `label: {$tabCount ->} [one] Unmute tab ({ $shortcut }) [other] Unmute { $tabCount } tabs ({ $shortcut })`
    - Suggest: `[two] … zavihka`
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — security/manager/security/certificates/certManager.ftl — Nonstandard participle "Vnešeno/vnešeno" → "Vneseno/vneseno" (also inconsistent with pippki-incorrect-pw, which is correct).
    - Source: `The password entered was incorrect.`
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — Wrong case. "…zbirko barvnih kombinacije." → "…kombinacij." (genitive plural).
    - Source: `heading: Your colorway theme(s) were removed. message: { -brand-product-name } updated its colorways collection. We removed the old version(s) from your “Saved Themes” list. Get new versions on the add-ons site.`
    - Suggest: `"…kombinacij."`
- `touch-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — toolkit/toolkit/about/aboutSupport.ftl — "…zaradi nedpodprte nastavitve…" → "…nepodprte…" (both strings).
    - Source: `async touch input disabled due to unsupported pref: { $preferenceKey }`
    - Suggest: `"…nepodprte…"`
- `wheel-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — toolkit/toolkit/about/aboutSupport.ftl — "…zaradi nedpodprte nastavitve…" → "…nepodprte…" (both strings).
    - Source: `async wheel input disabled due to unsupported pref: { $preferenceKey }`
    - Suggest: `"…nepodprte…"`
- `contentanalysis-slow-agent-dialog-body-file-and-more` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — contentanalysis-slow-agent-dialog-body-file-and-more ([one]) — toolkit/toolkit/contentanalysis/contentanalysis.ftl — Dual verb "sta" with singular adjective "skladen". → "skladna" (dual, agreeing with two subjects).
    - Source: `{$count ->} [one] { $agent } is reviewing “{ $filename }” and { $count } additional item against your organization’s data policies. This may take a moment. [other] { $agent } is reviewing “{ $filename }” and { $count }…`
    - Suggest: `"skladna"`

### D. Terminology, register & consistency

- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Obnovi podatke” but the string it names, `restore-from-backup-header`, reads “Obnovite podatke”
    - Current: `Kliknite "Obnovi podatke" in izberite to datoteko`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovite podatke`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Obnovi podatke” but the string it names, `restore-from-backup-header`, reads “Obnovite podatke”
    - Current: `Kliknite "Obnovi podatke" in izberite to datoteko`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovite podatke`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `newtab-section-block-button` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
    - Source: `Block`
    - Suggest: `standardize on one verb.`
- `newtab-section-block-topic` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
    - Source: `aria-label: Block { $topic }`
    - Suggest: `standardize on one verb.`
- `newtab-section-follow-button` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
    - Source: `Follow`
    - Suggest: `pick one verb.`
- `newtab-section-follow-topic` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
    - Source: `aria-label: Follow { $topic }`
    - Suggest: `pick one verb.`
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — onboarding "preizkusiti" vs "preskusiti" — browser/browser/newtab/onboarding.ftl — onboarding-focused-tabs-subtitle / onboarding-genai-sidebar-title use "preskusi(te)"; most siblings use the more common "Preizkusite". → align. (both forms valid; low priority.)
    - Source: `For a streamlined view that can help you stay focused, try your tabs on the side. Or keep it classic with tabs on the top. Switch anytime.`
    - Suggest: `align.`
- `onboarding-genai-sidebar-title` — `browser/browser/newtab/onboarding.ftl` — onboarding "preizkusiti" vs "preskusiti" — browser/browser/newtab/onboarding.ftl — onboarding-focused-tabs-subtitle / onboarding-genai-sidebar-title use "preskusi(te)"; most siblings use the more common "Preizkusite". → align. (both forms valid; low priority.)
    - Source: `Try an AI chatbot in the sidebar`
    - Suggest: `align.`
- `fonts-langgroup-kannada` — `browser/browser/preferences/fonts.ftl` — "Kannada" (Indic script) rendered "kanadsko" (reads as Canadian, colliding with fonts-langgroup-canadian). → "kannada".
    - Source: `label: Kannada`
    - Suggest: `"kannada".`
- `sync-engine-addresses` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl — Lowercase + accusative ("naslove", "kreditne kartice") break the "Choose what to sync" sibling pattern (Zaznamki, Zgodovina, Gesla…). → "Naslovi", "Kreditne kartice".
    - Source: `accesskey: e label: Addresses tooltiptext: Postal addresses you’ve saved (desktop only)`
    - Suggest: `"Naslovi", "Kreditne kartice".`
- `sync-engine-creditcards` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl — Lowercase + accusative ("naslove", "kreditne kartice") break the "Choose what to sync" sibling pattern (Zaznamki, Zgodovina, Gesla…). → "Naslovi", "Kreditne kartice".
    - Source: `accesskey: C label: Credit cards tooltiptext: Names, numbers and expiry dates (desktop only)`
    - Suggest: `"Naslovi", "Kreditne kartice".`
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints` quotes “Zaustavi na ...” but the string it names, `watchpoints.submenu`, reads “Zaustavi na …”
    - Current: `Z desno miškino tipko kliknite element v %Su in izberite "Zaustavi na ...", da dodate prekinitveno točko`
    - Source: `Right click an element in the %S and select “Break on…” to add a breakpoint`
    - Suggest: `Zaustavi na …`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `certificate-viewer-certificate-authority` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-certificate-authority (and authority-key-id, authority-info-aia) — toolkit/toolkit/about/certviewer.ftl — "Certificate Authority" rendered "uradna oseba za digitalna potrdila", but the CA tab (certificate-viewer-tab-ca) uses the standard "Overitelji". → align on "overitelj (digitalnih potrdil)".
    - Source: `Certificate Authority`
    - Suggest: `align on "overitelj`
- `user-context-color-violet` — `toolkit/toolkit/global/contextual-identity.ftl` — toolkit/toolkit/global/contextual-identity.ftl — Color labels mix gender: most are neuter (Modro, Zeleno, Rumeno, Oranžno, Rdeče, Vijolično) but violet "Vijolična" and gray "Siva" are feminine. In particular purple (Vijolično, neuter) and violet (Vijolična, feminine) clash. → unify gender.
    - Current: `Vijolična`
    - Source: `label: Violet`
    - Suggest: `unify gender.`
- `language-name-ti` — `toolkit/toolkit/intl/languageNames.ftl` — Tigrinya given the same name as Tigre (language-name-tig = "tigrajščina"). → "tigrinjščina" (must differ from Tigre).
    - Source: `Tigrinya`
    - Suggest: `"tigrinjščina"`

### E. Typography, punctuation & spacing

- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — Double space before "zamenjali".
    - Source: `This will replace all your current { -brand-short-name } data with your backup.`
- `firefox-relay-and-fxa-popup-notification-first-sentence-basic-info` — `browser/browser/firefoxRelay.ftl` — Missing space/preposition before the link → renders "Sporočilatega spletnega mesta". → "Sporočila s <label…>tega spletnega mesta</label>".
    - Source: `Prevent spam by hiding your real email address with a free <label data-l10n-name="firefox-relay-learn-more-url">email mask</label>. Emails from <label data-l10n-name="firefox-fxa-and-relay-offer-domain">this site</label…`
- `newtab-stocks-search-loading` — `browser/browser/newtab/newtab.ftl` — Space inserted before the ellipsis character.
    - Current: `Nalaganje …`
    - Source: `Loading…`
    - Suggest: `Nalaganje…`
    - The en-US source is "Loading…" with no space before the ellipsis; Slovenian does not insert a space before the ellipsis in such loading strings.
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (every other policy description ends with one).
    - Source: `Enable or disable Picture-in-Picture.`
- `inactive-css-not-display-block-on-floated-fix` — `devtools/client/tooltips.ftl` — devtools/client/tooltips.ftl — Missing space before markup: "odstraniti<strong>float</strong>" → "odstraniti <strong>float</strong>" (renders "odstranitifloat").
    - Source: `Try removing <strong>float</strong> or adding <strong>display:block</strong>. { learn-more }`
- `network-connection-status-connecting` — `netwerk/netwerk/necko.ftl` — netwerk/netwerk/necko.ftl — Stray space before the ellipsis: "{ $host } …" → "{ $host }…" (siblings looking-up, sending-request, waiting are correct).
    - Source: `Connecting to { $host }…`
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — btp-warning-tracker-classified ([two]) — toolkit/toolkit/global/antiTracking.ftl — Missing space before the variable: "v naslednjih{ $gracePeriodSeconds } sekundah" → "v naslednjih { $gracePeriodSeconds } sekundah" (the [few]/[other] variants have the space).
    - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
    - Suggest: `[few]`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (1)

- **`sl-brand-case-params`** (1) — Brand terms carry a `sklon` case parameter; correct Slovenian.
    - `firefox-relay-must-login-to-fxa`

_Suppressions live in `locales/sl/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (1)

- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (44)

- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `pkcs12-decode-err` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
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
