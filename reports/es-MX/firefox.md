# Firefox l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `bcd40327226f` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `4aab78fe6cf4` |
| **Previous run** | 2026-08-31 @ `67b14d26eb36` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,841 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 357 |
| Strings | 17,841 |
| Missing strings | 378 |
| Obsolete strings | 0 |
| Files absent from the locale | 5 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 142 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 131 |

### Completeness

**378 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 81
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `toolkit/services/aboutSyncLog.ftl` — 26
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 23
- `toolkit/toolkit/about/aboutNetworking.ftl` — 20
- `browser/browser/sharePanel.ftl` — 17
- `browser/browser/preferences/preferences.ftl` — 17
- `toolkit/toolkit/about/aboutAddons.ftl` — 15
- `toolkit/toolkit/neterror/netError.ftl` — 13
- `browser/browser/newtab/onboarding.ftl` — 13
- `browser/browser/sidebar.ftl` — 12
- `browser/browser/newtab/asrouter.ftl` — 11

**Files absent from the locale:**

- `browser/browser/sharePanel.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 504, `straight-double` 158, `curly-single` 84, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 96, `straight` 38 | _mixed_ |
| ellipsis | `char` 433, `ascii` 21 | **char** |
| dash | `em` 75, `en` 1 | **em** |
| nbsp | `total` 14, `narrow` 10, `before-punctuation` 10, `space-before-punctuation` 8 | _mixed_ |
| inverted marks | `open-question` 368, `open-exclamation` 85 | **open-question** |
| register | `informal` 1357, `formal` 237 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 142 strings** — 142 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
    - Affected: `addressbar-locbar-clipboard-option`, `addressbar-locbar-openpage-option`, `addressbar-locbar-quickactions-option`, `appmenu-addon-post-install-pin-toolbarbutton-checkbox`, `appmenu-help-more-troubleshooting-info`, `appmenu-help-not-deceptive`, `appmenu-homepage-controlled-changes`, `appmenu-new-tab-controlled-changes`, `appmenu-tab-hide-controlled`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2` …and 129 more
- **typography — 131 strings** — 131 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `AutomaticAuth`, `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CORSPreflightDidNotSucceed3`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolationWithURI`, `CompositorAnimationWarningTransformWithSyncGeometricAnimations`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed` …and 117 more

---

## 3. Open findings (21)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 6 |
| 3 | Degraded language (grammar, spelling, terminology) | 13 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-webrtc-closed-peerconnection-disclosure-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "PeerConnections" translated to "conexiones de pares" in the hide-msg variant only (comment: keep PeerConnection).
    - Source: `Show Closed PeerConnections`
- `moz-box-link-opens-in-new-tab` — `toolkit/toolkit/global/mozBoxBase.ftl` — Descriptive text "Opens in a new tab" was rendered as an imperative/infinitive command "Abrir en una nueva pestaña".
    - Current: `Abrir en una nueva pestaña`
    - Source: `Opens in a new tab`
    - Suggest: `Se abre en una nueva pestaña`
    - The en-US string describes the link's behavior (third person, "Opens in a new tab"), typically used as an accessible label; the Spanish infinitive reads as an action command, changing the meaning.

### C. Grammar, agreement & spelling

- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Unspecified size icon`

### D. Terminology, register & consistency

- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Sincronizar con el móvil” but the string it names, `sync-to-mobile-button-label`, reads “Sincronización con el móvil”
    - Current: `Escanea el código QR para descargar { -brand-product-name } para móvil. Una vez instalado, seleccione "Sincronizar con el móvil" para acceder a sus contraseñas, marcadores y mucho más sobre la marcha.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Sincronización con el móvil`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `content-blocking-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `Fingerprinters`
- `content-blocking-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `accesskey: F label: Fingerprinters`
- `content-blocking-known-and-suspected-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `Known and suspected fingerprinters`
- `content-blocking-known-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `accesskey: K label: Known fingerprinters`
- `sidebar-item-session-history` — `devtools/client/application.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `(value): Session History alt: Session History Icon title: Session History`
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints` quotes “Interrumpir en...” but the string it names, `watchpoints.submenu`, reads “Interrumpir en…”
    - Current: `Haz clic con el botón derecho sobre un elemento en el %S y selecciona “Interrumpir en...” para agregar un punto de ruptura`
    - Source: `Right click an element in the %S and select “Break on…” to add a breakpoint`
    - Suggest: `Interrumpir en…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Interrumpir en……” but the string it names, `watchpoints.submenu`, reads “Interrumpir en…”
    - Current: `Haz clic derecho en un elemento del Inspector y selecciona “Interrumpir en……” para agregar un punto de interrupción`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Interrumpir en…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `fips-nonempty-primary-password-required` — `security/manager/security/certificates/deviceManager.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
    - Source: `FIPS mode requires that you have a Primary Password set for each security device. Please set the password before trying to enable FIPS mode.`
- `addon-detail-rating-label` — `toolkit/toolkit/about/aboutAddons.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `Rating`
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — `colorway-removal-notice-message` quotes “Temas guardados” but the string it names, `theme-disabled-heading2`, reads “Guardar temas”
    - Current: `heading: Se eliminaron tus esquemas de colores. message: { -brand-product-name } actualizó su colección de esquemas de colores. Se eliminaron las versiones anteriores de tu lista de “Temas guardados”. Consigue las nueva…`
    - Source: `heading: Your colorway theme(s) were removed. message: { -brand-product-name } updated its colorways collection. We removed the old version(s) from your “Saved Themes” list. Get new versions on the add-ons site.`
    - Suggest: `Guardar temas`
    - In the source this string quotes “Saved Themes”, which is exactly the value of `theme-disabled-heading2` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `detail-rating` — `toolkit/toolkit/about/aboutAddons.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `value: Rating`
- `certificate-viewer-subject-alt-names` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `Subject Alt Names`
- `certificate-viewer-subject-key-id` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `Subject Key ID`
- `certificate-viewer-subject-name` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `Subject Name`
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
    - Source: `You have deleted your Primary Password. Stored passwords and certificate private keys managed by { -brand-short-name } will not be protected.`

### E. Typography, punctuation & spacing

- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `To see a full view of all recorded metrics, you can use the { -profiler-brand-name }. First you must <a data-l10n-name="firefox-profiler-link">capture a performance profile</a>. Once you capture the profile, select <q>M…`
- `remote-debugging-title` — `toolkit/toolkit/about/aboutSupport.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `Remote Debugging (Chromium Protocol)`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-MX/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (205)

- `about-logins-os-auth-dialog-message` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `login-intro-instructions-fxa-settings` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — fixed 2026-08-24
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-24
- `smart-window-model-flexible` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-24
- `smartwindow-messages-document-title` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-24
- `extension-firefox-compact-dark-description` — `browser/browser/appExtensionFields.ftl` — fixed 2026-08-24
- `browser-tab-audio-blocked` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `identity-description-weak-cipher-intro` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `urlbar-result-search-with` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `main-context-menu-edit-bookmark-with-shortcut` — `browser/browser/browserContext.ftl` — fixed 2026-08-24
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — fixed 2026-08-24
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — fixed 2026-08-24
- `genai-onboarding-gemini-tooltip` — `browser/browser/genai.ftl` — fixed 2026-08-24
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — fixed 2026-08-24
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — fixed 2026-08-24
- `ipprotection-location-selection-callout-primary-button` — `browser/browser/ipProtection.ftl` — fixed 2026-08-24
- `vpn-paused-alert-title` — `browser/browser/ipProtection.ftl` — fixed 2026-08-24
- `import-close-source-browser` — `browser/browser/migration.ftl` — fixed 2026-08-24
- `cfr-doorhanger-bookmark-fxa-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `colorways-cfr-header-today` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `firefoxview-cfr-primarybutton` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `fxa-adoption-primary-button-label` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `root-certificate-succession-infobar-march-message` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `newtab-custom-wallpaper-cta` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-pocket-thumbs-down-tooltip` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-section-menu-collapse-section` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-weather-sponsored` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-widget-timer-notification-break` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `mr2022-onboarding-colorway-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `mr2022-onboarding-existing-set-default-only-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `mr2022-onboarding-gratitude-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `media-count` — `browser/browser/pageInfo.ftl` — fixed 2026-08-24
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — fixed 2026-08-24
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — fixed 2026-08-24
- `places-forget-about-this-site-confirmation-msg` — `browser/browser/places.ftl` — fixed 2026-08-24
- `places-load-js-data-url-error` — `browser/browser/placesPrompts.ftl` — fixed 2026-08-24
