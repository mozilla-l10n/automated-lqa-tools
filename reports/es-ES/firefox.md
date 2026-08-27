# Firefox l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-08-27 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `caafd8e1597e` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 17,181 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-ES: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 355 |
| Strings | 17,181 |
| Missing strings | 1,029 |
| Obsolete strings | 0 |
| Files absent from the locale | 7 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 15 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 106 |

### Completeness

**1,029 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 153
- `browser/browser/aiWindow.ftl` — 131
- `browser/browser/appmenu.ftl` — 67
- `browser/browser/aiWindowContent.ftl` — 51
- `browser/browser/preferences/preferences.ftl` — 41
- `browser/browser/browser.ftl` — 33
- `toolkit/toolkit/global/theme-picker.ftl` — 28
- `devtools/client/toolbox-options.ftl` — 28
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `toolkit/services/aboutSyncLog.ftl` — 26
- `browser/browser/ipProtection.ftl` — 26
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 24

**Files absent from the locale:**

- `browser/browser/preferences/browserIcon.ftl`
- `browser/browser/sharePanel.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`
- `toolkit/toolkit/global/theme-picker.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 497, `straight-double` 150, `curly-single` 44, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 59, `straight` 76 | _mixed_ |
| ellipsis | `char` 440 | **char** |
| dash | `em` 76, `en` 1 | **em** |
| nbsp | `total` 9, `before-punctuation` 3, `space-before-punctuation` 6 | _mixed_ |
| inverted marks | `open-question` 348, `open-exclamation` 79 | **open-question** |
| register | `informal` 3, `formal` 1367 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 106 strings** — 106 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `BlockTopLevelDataURINavigation`, `CORSPreflightDidNotSucceed3`, `CSPROViolation`, `CSPROViolationWithURI`, `CookieLaxForced2`, `CookieOversize`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius` …and 92 more

---

## 3. Open findings (30)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 18 |
| 3 | Degraded language (grammar, spelling, terminology) | 12 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `appmenu-homepage-controlled-changes` — `browser/browser/appMenuNotifications.ftl` — Access key `K` of `appmenu-homepage-controlled-changes` is not present in its label
    - Current: `K`
    - Source: `buttonaccesskey: K buttonlabel: Keep Changes label: Your homepage has changed. secondarybuttonaccesskey: M secondarybuttonlabel: Manage Homepage`
    - The label is “Mantener los cambios”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-new-tab-controlled-changes` — `browser/browser/appMenuNotifications.ftl` — Access key `K` of `appmenu-new-tab-controlled-changes` is not present in its label
    - Current: `K`
    - Source: `buttonaccesskey: K buttonlabel: Keep Changes label: Your new tab has changed. secondarybuttonaccesskey: M secondarybuttonlabel: Manage New Tabs`
    - The label is “Mantener los cambios”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-help-more-troubleshooting-info` — `browser/browser/appmenu.ftl` — Access key `T` of `appmenu-help-more-troubleshooting-info` is not present in its label
    - Current: `T`
    - Source: `accesskey: t label: More troubleshooting information`
    - The label is “Más información para solucionar problemas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
    - Current: `B`
    - Source: `accesskey: B aria-label: Bookmarks toolbarname: Bookmarks Toolbar`
    - The label is “Marcadores”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `picture-in-picture-hide-toggle` — `browser/browser/browser.ftl` — Access key `H` of `picture-in-picture-hide-toggle` is not present in its label
    - Current: `H`
    - Source: `accesskey: H label: Hide Picture-in-Picture Toggle`
    - The label is “Ocultar botón de Picture-in-Picture”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `downloads-cmd-always-use-system-default` — `browser/browser/downloads.ftl` — Access key `w` of `downloads-cmd-always-use-system-default` is not present in its label
    - Current: `w`
    - Source: `accesskey: w label: Always Open In System Viewer`
    - The label is “Abrir siempre en el visor del sistema”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `menu-edit-find-in-page` — `browser/browser/menubar.ftl` — Access key `F` of `menu-edit-find-in-page` is not present in its label
    - Current: `F`
    - Source: `accesskey: F label: Find in Page…`
    - The label is “Buscar en la página…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `menu-help-more-troubleshooting-info` — `browser/browser/menubar.ftl` — Access key `T` of `menu-help-more-troubleshooting-info` is not present in its label
    - Current: `T`
    - Source: `accesskey: T label: More Troubleshooting Information`
    - The label is “Más información para solucionar problemas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `confirm-on-quit-with-key` — `browser/browser/preferences/preferences.ftl` — Access key `b` of `confirm-on-quit-with-key` is not present in its label
    - Current: `b`
    - Source: `accesskey: b label: Confirm before quitting with { $quitKey }`
    - The label is “Confirmar antes de salir con { $quitKey }”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `forms-primary-pw-change` — `browser/browser/preferences/preferences.ftl` — Access key `P` of `forms-primary-pw-change` is not present in its label
    - Current: `P`
    - Source: `accesskey: P label: Change Primary Password…`
    - The label is “Cambiar la contraseña maestra…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `protections-panel-content-blocking-manage-settings` — `browser/browser/protectionsPanel.ftl` — Access key `M` of `protections-panel-content-blocking-manage-settings` is not present in its label
    - Current: `M`
    - Source: `accesskey: M label: Manage protection settings`
    - The label is “Gestionar los ajustes de protección”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `bookmark-selected-tabs` — `browser/browser/tabContextMenu.ftl` — Access key `k` of `bookmark-selected-tabs` is not present in its label
    - Current: `k`
    - Source: `accesskey: B label: Bookmark Tabs…`
    - The label is “Añadir pestañas a marcadores…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-play-tabs` — `browser/browser/tabContextMenu.ftl` — Access key `y` of `tab-context-play-tabs` is not present in its label
    - Current: `y`
    - Source: `accesskey: y label: Play Tabs`
    - The label is “Reproducir pestañas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `unpin-selected-tabs` — `browser/browser/tabContextMenu.ftl` — Access key `b` of `unpin-selected-tabs` is not present in its label
    - Current: `b`
    - Source: `accesskey: p label: Unpin Tabs`
    - The label is “Soltar pestañas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — Access key `G` of `styleeditor-visibility-toggle` is not present in its label
    - Current: `G`
    - Source: `accesskey: S tooltiptext: Toggle style sheet visibility`
    - The label is “Cambiar la visibilidad de la hoja de estilos”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `manifest-loading` — `devtools/client/application.ftl` — "manifesto" is not the Spanish word for a web app manifest file; the correct term is "manifiesto".
    - Current: `Cargando manifesto…`
    - Source: `Loading manifest…`
    - Suggest: `Cargando manifiesto…`
    - en-US "Loading manifest…" refers to the manifest file; Spanish spells this "manifiesto". "Manifesto" is a misspelling/anglicism.

### D. Terminology, register & consistency

- `backup-service-error-corrupt-file` — `browser/browser/backupSettings.ftl` — backup — "respaldo" (backup-service-error-corrupt-file) vs "copia de seguridad" (rest of backupSettings.ftl).
    - Source: `heading: This file isn’t working message: There was a problem with your backup file. Choose a different file and try again.`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Sincronizar con móvil” but the string it names, `sync-to-mobile-button-label`, reads “Sincronización con el móvil”
    - Current: `Escanee el código QR para descargar { -brand-product-name } para dispositivos móviles. Una vez instalado, seleccione “Sincronizar con móvil” para acceder a las contraseñas, marcadores y más sobre la marcha.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Sincronización con el móvil`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `connection-proxy-socks-remote-dns` — `browser/browser/preferences/connection.ftl` — SOCKS DNS — connection-proxy-socks-remote-dns "Proxy DNS al usar SOCKS v4" vs -socks4-remote-dns "DNS proxy usando SOCKS v5".
    - Source: `accesskey: D label: Proxy DNS when using SOCKS v5`
    - Suggest: `-socks4-remote-dns`
- `backup-multi-profile-warning-message` — `browser/browser/preferences/preferences.ftl` — `backup-multi-profile-warning-message` quotes “Hacer copia de seguridad ahora” but the string it names, `settings-data-backup-trigger-button`, reads “Hacer ahora copia de seguridad”
    - Current: `message: Para garantizar que este cambio sea incluido en sus copias de seguridad, abra cada perfil y seleccione “Hacer copia de seguridad ahora” en Ajustes.`
    - Source: `message: To make sure this change is included in your backups, open each profile and choose “Backup now” in Settings.`
    - Suggest: `Hacer ahora copia de seguridad`
    - In the source this string quotes “Backup now”, which is exactly the value of `settings-data-backup-trigger-button` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `protections-panel-content-blocking-breakage-report-view-send-report` — `browser/browser/protectionsPanel.ftl` — protections-panel-content-blocking-breakage-report-view-send-report "Enviar reporte" vs the file's "informe" → informe.
    - Source: `label: Send Report`
    - Suggest: `informe.`
- `tracking-protection-icon-active` — `browser/browser/siteProtections.ftl` — "entre sitios" vs "sitios cruzados" (tracking-protection-icon-active and prefs). Unify to entre sitios.
    - Source: `Blocking social media trackers, cross-site tracking cookies, and fingerprinters.`
- `manifest-empty-intro2` — `devtools/client/application.ftl` — manifest — "Manifesto" (manifest-view-header, manifest-loading, etc.) vs "Manifiesto" (manifest-empty-intro2) → Manifiesto.
    - Source: `No web app manifest detected`
    - Suggest: `Manifiesto.`
- `manifest-view-header` — `devtools/client/application.ftl` — manifest — "Manifesto" (manifest-view-header, manifest-loading, etc.) vs "Manifiesto" (manifest-empty-intro2) → Manifiesto.
    - Source: `App Manifest`
    - Suggest: `Manifiesto.`
- `toolbox-meatball-menu-dock-bottom-label` — `devtools/client/toolbox.ftl` — Dock — "Fijar" (toolbox-meatball-menu-dock-bottom-label) vs "Anclar" (left/right).
    - Source: `Dock to Bottom`
- `certificate-viewer-subject-name` — `toolkit/toolkit/about/certviewer.ftl` — Subject (cert) — "asunto" (certificate-viewer-subject-name/-key-id) vs "sujeto" (-subject-alt-names).
    - Source: `Subject Name`
    - Suggest: `-key-id`
- `neterror-net-offline` — `toolkit/toolkit/neterror/netError.ftl` — `neterror-net-offline` quotes “Probar de nuevo” but the string it names, `neterror-try-again-button`, reads “Reintentar”
    - Current: `Presione “Probar de nuevo” para cambiar al modo con conexión y recargar la página.`
    - Source: `Press “Try Again” to switch to online mode and reload the page.`
    - Suggest: `Reintentar`
    - In the source this string quotes “Try Again”, which is exactly the value of `neterror-try-again-button` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `primary-password-prompt-message` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — Primary Password — contraseña maestra (in failed-pp-change, incorrect-pp, primary-password-, remove-primary-password, primary-password-prompt-message) vs contraseña principal (settings-pp-erased-ok, settings-pp-not-wanted). Unify to contraseña principal.
    - Current: `contraseña maestra`
    - Source: `Please enter your Primary Password.`
- `failed-pp-change` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password — contraseña maestra (in failed-pp-change, incorrect-pp, primary-password-, remove-primary-password, primary-password-prompt-message) vs contraseña principal (settings-pp-erased-ok, settings-pp-not-wanted). Unify to contraseña principal.
    - Current: `contraseña maestra`
    - Source: `Unable to change Primary Password.`
- `incorrect-pp` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password — contraseña maestra (in failed-pp-change, incorrect-pp, primary-password-, remove-primary-password, primary-password-prompt-message) vs contraseña principal (settings-pp-erased-ok, settings-pp-not-wanted). Unify to contraseña principal.
    - Current: `contraseña maestra`
    - Source: `You did not enter the correct current Primary Password. Please try again.`

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-ES/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (111)

- `about-logins-error-message-duplicate-login-with-link` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `about-logins-export-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `restore-page-error-title` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-24
- `welcome-back-page-info-link` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-24
- `addon-install-error-not-signed` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-24
- `ai-window-memories-section` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-24
- `ai-window-open-sidebar` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-24
- `contextual-manager-passwords-username-tooltip` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-24
- `taskbar-tabs-value-prop-callout-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `annotations-make-default-pdf-handler-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `etp-strict-exceptions-infobar-message` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-toast-thumbs-up-or-down2` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-wallpaper-celestial-river` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `mr2022-onboarding-colorway-description-visionary` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `onboarding-new-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `onboarding-new-user-time-based-survey-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `general-meta-tags` — `browser/browser/pageInfo.ftl` — fixed 2026-08-24
- `app-manager-handle-file` — `browser/browser/preferences/applicationManager.ftl` — fixed 2026-08-24
- `app-manager-handle-protocol` — `browser/browser/preferences/applicationManager.ftl` — fixed 2026-08-24
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — fixed 2026-08-24
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — fixed 2026-08-24
- `permissions-site-notification-disable-desc` — `browser/browser/preferences/permissions.ftl` — fixed 2026-08-24
- `info-known-breaches-found` — `browser/browser/protections.ftl` — fixed 2026-08-24
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — fixed 2026-08-24
- `report-broken-site-panel-reason-account2` — `browser/browser/reportBrokenSite.ftl` — fixed 2026-08-24
- `protections-blocking-tracking-content` — `browser/browser/siteProtections.ftl` — fixed 2026-08-24
- `protections-not-blocking-cross-site-tracking-cookies` — `browser/browser/siteProtections.ftl` — fixed 2026-08-24
- `webrtc-allow-share-screen-with-file` — `browser/browser/webrtcIndicator.ftl` — fixed 2026-08-24
- `manifest-loading` — `devtools/client/application.ftl` — fixed 2026-08-24
- `options-show-user-agent-shadow-dom-label` — `devtools/client/toolbox-options.ftl` — fixed 2026-08-24
- `inactive-css-no-width-height` — `devtools/client/tooltips.ftl` — fixed 2026-08-24
- `inactive-css-not-grid-or-flex-item` — `devtools/client/tooltips.ftl` — fixed 2026-08-24
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `pippki-incorrect-pw` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `protected-auth-alert` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `details-notification-soft-blocked-other-disabled` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-08-24
