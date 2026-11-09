# Firefox l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `74047c5347bc` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-09 @ `3685bd005e67` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 16,012 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 330 |
| Strings | 16,012 |
| Missing strings | 863 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 28 |

### Completeness

**863 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 140
- `browser/browser/ipProtection.ftl` — 86
- `browser/browser/aiWindowContent.ftl` — 58
- `dom/chrome/dom/dom.properties` — 53
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 48
- `browser/browser/preferences/preferences.ftl` — 41
- `browser/browser/newtab/newtab.ftl` — 41
- `toolkit/toolkit/about/aboutProcesses.ftl` — 33
- `dom/chrome/security/security.properties` — 30
- `browser/browser/aiFeatures.ftl` — 27
- `browser/browser/newtab/onboarding.ftl` — 24
- `browser/browser/genai.ftl` — 20

**Files absent from the locale:**

- `browser/browser/autoTabGrouping.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 268, `straight-double` 267, `curly-single` 50, `guillemet` 5 | _mixed_ |
| apostrophe | `typographic` 50, `straight` 51 | _mixed_ |
| ellipsis | `char` 365, `ascii` 33 | **char** |
| dash | `em` 15, `en` 119 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 8 | _mixed_ |
| register | `informal` 8, `formal` 543 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 28 strings** — 28 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `about-debugging-sidebar-runtime-item-waiting-for-browser`, `about-logins-menu-menuitem-export-logins2`, `browser-languages-downloading`, `browser-languages-search`, `browser-languages-searching`, `choose-other-app-window-title`, `crashreporter-button-details`, `crashreporter-resubmit-status`, `diffing.state.taking-diff`, `diffing.state.taking-diff.full`, `fxa-menu-send-tab-to-device-syncnotready`, `home-homepage-custom-url` …and 16 more

---

## 3. Open findings (20)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 15 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — The purpose clause is mistranslated so that the sentence reads "To improve the { -brand-product-name } browser" and merges the subject, changing which product is being improved and who sends the data.
    - Current: `Za izboljšanje brskalnika { -brand-product-name } { -vendor-short-name } pošilja diagnostične podatke in podatke o uporabi.`
    - Source: `By continuing, you agree to the <a data-l10n-name="terms_of_use">{ -brand-product-name } Terms of Use</a> and our <a data-l10n-name="privacy_notice">Privacy Notice</a>. To help improve the browser, { -brand-product-name…`
    - Suggest: `Za izboljšanje brskalnika { -brand-product-name } pošilja { -vendor-short-name } diagnostične podatke in podatke o uporabi.`
    - In en-US the subject is { -brand-product-name } which sends data to { -vendor-short-name }; the Slovenian makes { -vendor-short-name } the sender and attaches the brand name to "brskalnika", reversing the roles and dropping the recipient.
- `speech-recognition-model-download-message` — `browser/browser/permissions.ftl` — The Slovenian drops "when you continue" and mangles "the audio never leaves your device" into a relative clause saying the device never leaves the audio.
    - Current: `V { -brand-short-name } prepoznavanje govora poteka na napravi, ki je zvok v nobenem trenutku ne zapusti. V ta namen bo na napravo preneslo ~{ $sizeMB } MB podatkov.`
    - Source: `{ -brand-short-name } runs speech recognition locally, so the audio never leaves your device. To set this up, a ~{ $sizeMB } MB download will start when you continue.`
    - Suggest: `V { -brand-short-name } prepoznavanje govora poteka krajevno, zato zvok nikoli ne zapusti vaše naprave. Za nastavitev se bo ob nadaljevanju začel prenos velikosti ~{ $sizeMB } MB.`
    - The en-US says the download will start when you continue; the target states it will simply be downloaded, omitting the condition, and the second sentence also lacks a subject ("bo na napravo preneslo").
- `options-stylesheets-in-the-debugger-tooltip` — `devtools/client/toolbox-options.ftl` — Tooltip drops "and view" from "List and view stylesheets in the debugger".
    - Current: `Prikaži seznam slogovnih predlog v razhroščevalniku`
    - Source: `title: List and view stylesheets in the debugger`
    - Suggest: `Prikaži seznam slogovnih predlog in si jih oglej v razhroščevalniku`
    - The en-US says "List and view stylesheets"; the Slovenian only mentions listing them.
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — "export pages" rendered as "posamič izvozite" (export individually), adding a claim not in the source.
    - Current: `jih odstranite, združite ali posamič izvozite`
    - Source: `Reorder, remove, merge, and export pages.`
    - Suggest: `jih odstranite, združite in izvozite`
    - The source says "Reorder, remove, merge, and export pages" with no statement that export happens individually.
- `about-pdf-feature-organize-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — "Organize pages" translated as "Organizirajte dokumente" (organize documents) instead of pages.
    - Current: `Organizirajte dokumente`
    - Source: `Organize pages`
    - Suggest: `Organizirajte strani`
    - The en-US refers to pages within a PDF, not documents; the description in the same feature block also talks about reordering pages.

### C. Grammar, agreement & spelling

- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — "Strani a deljenje…" → "Strani za deljenje…".
    - Source: `heading: Something went wrong message: We couldn’t create your shared page this time. Try again later.`
    - Suggest: `"Strani za deljenje…".`
- `security-technical-weak-cipher` — `browser/browser/pageInfo.ftl` — Adjective–noun gender agreement error: masculine "Drugi" with feminine plural "osebe".
    - Current: `Drugi osebe`
    - Source: `Your connection to this website uses weak encryption and is not private. Other people can view your information or modify the website’s behavior.`
    - Suggest: `Druge osebe`
    - "Osebe" is feminine plural (nominative), so the adjective must be "druge". "Drugi osebe" is ungrammatical.
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — The participle "vstavljenih" (inserted) is in the wrong case; it should agree with "module" (modules, accusative plural).
    - Current: `vstavljenih v proces`
    - Source: `Prevent the user from using Third-party Module Information (about:third-party) to block third-party modules injected into the { -brand-short-name } process.`
    - Suggest: `vstavljene v proces`
    - It is the modules that are injected into the process, and "module" is the accusative object of "blokiral" (would block). The participle must therefore be accusative plural ("vstavljene"). The genitive "vstavljenih" is ungrammatical, or it wrongly attaches to "ponudnikov" (providers), as if the providers were injected.
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
- `fonts-langgroup-kannada` — `browser/browser/preferences/fonts.ftl` — "Kannada" (Indic script) rendered "kanadsko" (reads as Canadian, colliding with fonts-langgroup-canadian). → "kannada".
    - Source: `label: Kannada`
    - Suggest: `"kannada".`
- `dom-manifest-id-not-same-origin` — `dom/dom/manifest.ftl` — This string translates "origin" as "poreklo", but the rest of the same file uses "izvor".
    - Current: `enako poreklo`
    - Source: `The id member must have the same origin as the start_url member.`
    - Suggest: `enak izvor`
    - In dom-manifest-scope-not-same-origin and dom-manifest-start-url-should-be-same-origin, the web-security term "origin" is translated "izvor" ("istega izvora"). "Poreklo" means ancestry or descent and is inconsistent within these manifest error messages.
- `certificate-viewer-certificate-authority` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-certificate-authority (and authority-key-id, authority-info-aia) — toolkit/toolkit/about/certviewer.ftl — "Certificate Authority" rendered "uradna oseba za digitalna potrdila", but the CA tab (certificate-viewer-tab-ca) uses the standard "Overitelji". → align on "overitelj (digitalnih potrdil)".
    - Source: `Certificate Authority`
    - Suggest: `align on "overitelj`

### E. Typography, punctuation & spacing

- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — btp-warning-tracker-classified ([two]) — toolkit/toolkit/global/antiTracking.ftl — Missing space before the variable: "v naslednjih{ $gracePeriodSeconds } sekundah" → "v naslednjih { $gracePeriodSeconds } sekundah" (the [few]/[other] variants have the space).
    - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
    - Suggest: `[few]`

---

## 4. Appendix

### Dismissed by hand (5)

- `appmenu-fxa-sign-in-promo-heading2` — `browser/browser/appmenu.ftl` — pontoon-rejected (2026-11-04): rejected in Pontoon without comment; reason unclear
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Sprememba na narobe. Citirani niz (backup-folder-name) je "Obnovi podatke". https://pontoon.mozilla.org/sl/firefox/browser/browser/backupSettings.ftl/?string=324818</p>
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; likely reason (inferred): The quoted text is probably a button label, and this locale's convention is that short button labels use the informal singular imperative, so "Obnovi podatke" likely matches the actual button rather than the "Obnovite podatke" header the finding compared it to.
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Ni potrebe po spreminjanju, pravilno je oboje.</p>
- `onboarding-genai-sidebar-title` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; likely reason (inferred): The finding itself says both "preskusiti" and "preizkusiti" are valid and marks it low priority, so the reviewer probably saw a purely stylistic change that wasn't needed.

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (15)

- `about-pdf-feature-comments-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — auto-suggest (2026-11-09, string ee5fb1e1): unreliable finding: 'Pišite opombe' is a natural heading for the notes feature; 'Dodajte' would be a stylistic preference.
- `about-pdf-feature-presentation-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — auto-suggest (2026-11-09, string e8811c55): unreliable finding: In the about:pdf context 'dokumente' clearly means PDFs; omission is not clearly a defect.
- `newtab-recent-searches-row-remove` — `browser/browser/newtab/newtab.ftl` — auto-suggest (2026-11-03, string 2aea1636): The sl tree uses straight double quotes (259) and curly double quotes (268) about equally, so straight quotes are an accepted convention.
- `newtab-stocks-search-loading` — `browser/browser/newtab/newtab.ftl` — auto-suggest (2026-11-09, string 7b2ef640): Slovenian spelling rules put a space before an ellipsis that follows a whole word ('Nalaganje …'); this is the locale's standard.
- `options-experimental-label` — `devtools/client/toolbox-options.ftl` — auto-suggest (2026-11-09, string fae16250): unreliable finding: "Zmogljivosti" is used for "features" in Slovenian software localization; changing it is a matter of preference.
- `password-rules-email-description2` — `browser/browser/backupSettings.ftl` — auto-suggest (2026-11-09, string b5b2e01d): A predicate noun after negated 'biti' stays in the nominative ('To ni e-poštni naslov'); the genitive is only used for negated existence. The lowercase start may be on purpose.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — auto-suggest (2026-11-09, string 2fa73412): unreliable finding: The policy describes the page that opens after an update, not necessarily the menu link label, so "Kaj je novega" is plausibly acceptable.
- `refresh-reinstalled-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — auto-suggest (2026-11-09, string 0b410d55): unreliable finding: 'nameščen na novo' still conveys a reinstall; leaving out the user as the one who did it is a style choice, not a mistranslation.
- `refresh-unused-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — auto-suggest (2026-11-09, string ca644fff): unreliable finding: 'očistiti navlake' is an idiomatic way to say 'clean up' and matches what the refresh feature does; the change would be stylistic.
- `support-remote-experiments-title` — `toolkit/toolkit/about/aboutSupport.ftl` — auto-suggest (2026-11-09, string cd199e87): unreliable finding: 'Poskusi na daljavo' is an acceptable rendering of remotely delivered experiments; the alternative is a stylistic choice.
- `sync-engine-addresses` — `browser/browser/preferences/preferences.ftl` — auto-suggest (2026-11-09, string c1bd1374): unreliable finding: The sibling sync labels cannot be seen here; the accusative may follow a sentence-style pattern, so the inconsistency cannot be confirmed.
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — auto-suggest (2026-11-03, string 878a0d6f): After "glasnost" the noun is in genitive, and genitive dual and plural of zavihek are both "zavihkov" (dveh/treh zavihkov), so the forms are correct.
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — auto-suggest (2026-11-03, string 6adb9ae8): After "glasnost" the noun is in genitive, and genitive dual and plural of zavihek are both "zavihkov" (dveh/treh zavihkov); the mute string uses accusative, hence differs.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — auto-suggest (2026-11-09, string a3c02400): The quoted UI name is "lokalnega načina", which is the correctly inflected (genitive) form of the label "Lokalni način"; "z uporabo" is not inside the quotes.
- `user-context-color-violet` — `toolkit/toolkit/global/contextual-identity.ftl` — auto-suggest (2026-11-09, string a2cdbde8): unreliable finding: The feminine 'Vijolična' may be deliberate, to tell violet apart from purple ('Vijolično'), and gray is feminine too, so changing the gender would be a stylistic choice rather than fixing a confirmed error.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (2)

- **`sl-brand-case-params`** (2) — Brand terms carry a `sklon` case parameter; correct Slovenian.
    - `smartwindow-assistant-error-account-header`, `firefox-relay-must-login-to-fxa`

_Suppressions live in `locales/sl/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (2)

- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (58)

- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — fixed 2026-11-05
- `decoder-doctor-unsupported-libavcodec-message` — `browser/browser/browser.ftl` — fixed 2026-11-05
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — fixed 2026-11-05
- `newtab-wallpaper-firefox-desert-light` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `newtab-wallpaper-your-images-folder` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `privacy-metrics-cookies` — `browser/browser/protections.ftl` — fixed 2026-11-05
- `outline.placeholder.functions` — `devtools/client/debugger.properties` — fixed 2026-11-05
- `inactive-css-not-display-block-on-floated-fix` — `devtools/client/tooltips.ftl` — fixed 2026-11-05
- `network-connection-status-connecting` — `netwerk/netwerk/necko.ftl` — fixed 2026-11-05
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-11-05
- `about-networking-ssl-tokens-new` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-11-05
- `about-pdf-feature-annotate-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-05
- `language-name-ti` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-11-05
- `main-context-menu-media-video-leave-fullscreen` — `browser/browser/browserContext.ftl` — fixed 2026-09-28
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
