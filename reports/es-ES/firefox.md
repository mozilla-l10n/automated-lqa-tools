# Firefox l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `3f7b6c3c060f` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `749ea3a23fef` |
| **Previous run** | 2026-09-14 @ `e44f1369fb6d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 11 of 15,167 |

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
| Files | 318 |
| Strings | 15,167 |
| Missing strings | 1,066 |
| Obsolete strings | 0 |
| Files absent from the locale | 8 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 12 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 93 |

### Completeness

**1,066 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 202
- `browser/browser/aiWindow.ftl` — 134
- `browser/browser/appmenu.ftl` — 65
- `browser/browser/aiWindowContent.ftl` — 51
- `browser/browser/newtab/onboarding.ftl` — 42
- `browser/browser/browser.ftl` — 30
- `toolkit/toolkit/global/theme-picker.ftl` — 29
- `devtools/client/toolbox-options.ftl` — 28
- `toolkit/services/aboutSyncLog.ftl` — 28
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `browser/browser/firefoxView.ftl` — 23
- `toolkit/toolkit/about/aboutPDF.ftl` — 22

**Files absent from the locale:**

- `browser/browser/preferences/browserIcon.ftl`
- `browser/browser/sharePanel.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`
- `toolkit/toolkit/global/theme-picker.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 444, `straight-double` 136, `curly-single` 42, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 57, `straight` 70 | _mixed_ |
| ellipsis | `char` 370 | **char** |
| dash | `em` 55, `en` 1 | **em** |
| nbsp | `total` 8, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| inverted marks | `open-question` 296, `open-exclamation` 66 | **open-question** |
| register | `informal` 4, `formal` 1169 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 93 strings** — 93 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `BlockTopLevelDataURINavigation`, `CORSPreflightDidNotSucceed3`, `CookieLaxForced2`, `CookieOversize`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords` …and 81 more

---

## 3. Open findings (36)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 20 |
| 3 | Degraded language (grammar, spelling, terminology) | 16 |
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
- `picture-in-picture-hide-toggle` — `browser/browser/browser.ftl` — Access key `H` of `picture-in-picture-hide-toggle` is not present in its label
    - Current: `H`
    - Source: `accesskey: H label: Hide Picture-in-Picture Toggle`
    - The label is “Ocultar botón de Picture-in-Picture”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `downloads-cmd-always-use-system-default` — `browser/browser/downloads.ftl` — Access key `w` of `downloads-cmd-always-use-system-default` is not present in its label
    - Current: `w`
    - Source: `accesskey: w label: Always Open In System Viewer`
    - The label is “Abrir siempre en el visor del sistema”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `ipprotection-feature-introduction-link-text-privacy-2` — `browser/browser/ipProtection.ftl` — The link text scope was changed: the source links the whole phrase "{ -brand-product-name }'s built-in VPN" while the target links only the brand name.
    - Current: `La VPN integrada de <a data-l10n-name="learn-more-vpn">{ -brand-product-name }</a>`
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> helps protect your browsing. Choose from multiple locations to keep where you browse more private.`
    - Suggest: `<a data-l10n-name="learn-more-vpn">La VPN integrada de { -brand-product-name }</a>`
    - In en-US the anchor wraps "{ -brand-product-name }’s built-in VPN"; moving the tag so it wraps only the brand name changes the clickable text.
- `menu-edit-find-in-page` — `browser/browser/menubar.ftl` — Access key `F` of `menu-edit-find-in-page` is not present in its label
    - Current: `F`
    - Source: `accesskey: F label: Find in Page…`
    - The label is “Buscar en la página…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `menu-help-more-troubleshooting-info` — `browser/browser/menubar.ftl` — Access key `T` of `menu-help-more-troubleshooting-info` is not present in its label
    - Current: `T`
    - Source: `accesskey: T label: More Troubleshooting Information`
    - The label is “Más información para solucionar problemas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
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

### B. Mistranslation, reversed meaning, wrong names & brand

- `taskbar-tabs-media-callout-title-v3` — `browser/browser/featureCallout.ftl` — "Keep your streaming" rendered as "sus vídeos", narrowing/changing the meaning.
    - Current: `Mantenga sus vídeos en la barra de tareas`
    - Source: `Keep your streaming in your taskbar`
    - Suggest: `Mantenga sus sitios de streaming en la barra de tareas`
    - The en-US refers to streaming (media) sites, not to the user's videos; the subtitle also refers to "sitios de medios".
- `site-rules-status-heading` — `browser/browser/ipProtection.ftl` — "Your rule" translated as "Regla personalizada" (custom rule).
    - Current: `Regla personalizada`
    - Source: `Your rule`
    - Suggest: `Su regla`
    - The source heading is "Your rule", referring to the user's rule for this site, not "custom rule".
- `refresh-profile-infobar-button` — `browser/browser/newtab/asrouter.ftl` — "Refresh { -brand-short-name }" is rendered as "Reiniciar" (restart) instead of the established "Restaurar" for profile refresh.
    - Current: `Reiniciar { -brand-short-name }…`
    - Source: `(value): Refresh { -brand-short-name }… accesskey: e`
    - Suggest: `Restaurar { -brand-short-name }…`
    - The button triggers the profile refresh (reset) feature, not a restart; "Reiniciar" tells the user the browser will simply be restarted, which is a different action. Firefox es-ES uses "Restaurar { -brand-short-name }" for Refresh.
- `permissions-exceptions-shutdown-clearing-window` — `browser/browser/preferences/permissions.ftl` — "on Shutdown" refers to closing Firefox, not shutting down the system.
    - Current: `Excepciones: Borrar el historial al apagar el sistema`
    - Source: `style: { permissions-window2.style } title: Exceptions - Clear History on Shutdown`
    - Suggest: `Excepciones: Borrar el historial al cerrar`
    - The related description string clarifies it is "when { -brand-short-name } clears history on close"; "apagar el sistema" wrongly says the operating system shuts down.
- `pdfjs-digital-signature-properties-timestamp` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Timestamp" translated as "Fecha" (date), losing the time component.
    - Current: `Fecha: { $dateObj }`
    - Source: `Timestamp: { $dateObj }`
    - Suggest: `Marca de tiempo: { $dateObj }`
    - The source label is "Timestamp", which includes the signing time, not just the date.

### C. Grammar, agreement & spelling

- `launch-on-login-autostart-infobar-message` — `browser/browser/newtab/asrouter.ftl` — Incorrect verb mood/agreement: "se inicia cuando usted inicie sesión" mixes indicative and subjunctive.
    - Current: `Ahora { -brand-short-name } se inicia cuando usted inicie sesión en Windows.`
    - Source: `{ -brand-short-name } now starts up when you sign in to Windows. You can always change this later in settings.`
    - Suggest: `Ahora { -brand-short-name } se inicia cuando inicia sesión en Windows.`
    - The en-US states a present habitual fact ("starts up when you sign in"); the Spanish subjunctive "inicie" after the indicative main clause is ungrammatical in this context.
- `containers-sites-card-header` — `browser/browser/preferences/preferences.ftl` — Typo: "Elia" instead of "Elija".
    - Current: `Elia un contenedor para un sitio`
    - Source: `description: Choose a container for a site and { -brand-short-name } will use it every time the site opens. label: Site-specific containers`
    - Suggest: `Elija un contenedor para un sitio`
    - "Choose a container" should be "Elija un contenedor"; "Elia" is not a Spanish word.
- `passports-no-passports-stored-message` — `browser/browser/preferences/preferences.ftl` — State description rendered as a past-tense event instead of a status.
    - Current: `No se añadieron pasaportes`
    - Source: `label: No passports added`
    - Suggest: `No hay pasaportes añadidos`
    - en-US "No passports added" is an empty-state status message; the preterite "No se añadieron" reports a past action rather than the current absence of stored passports.

### D. Terminology, register & consistency

- `backup-service-error-corrupt-file` — `browser/browser/backupSettings.ftl` — backup — "respaldo" (backup-service-error-corrupt-file) vs "copia de seguridad" (rest of backupSettings.ftl).
    - Source: `heading: This file isn’t working message: There was a problem with your backup file. Choose a different file and try again.`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Sincronizar con móvil” but the string it names, `sync-to-mobile-button-label`, reads “Sincronización con el móvil”
    - Current: `Escanee el código QR para descargar { -brand-product-name } para dispositivos móviles. Una vez instalado, seleccione “Sincronizar con móvil” para acceder a las contraseñas, marcadores y más sobre la marcha.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Sincronización con el móvil`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Qué hay de nuevo” but the string it names, `releaseNotes-link`, reads “Novedades”
    - Current: `Anular la página "Qué hay de nuevo" posterior a la actualización. Deje esta política en blanco si quiere desactivar la página posterior a la actualización.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Novedades`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `connection-proxy-socks-remote-dns` — `browser/browser/preferences/connection.ftl` — SOCKS DNS — connection-proxy-socks-remote-dns "Proxy DNS al usar SOCKS v4" vs -socks4-remote-dns "DNS proxy usando SOCKS v5".
    - Source: `accesskey: D label: Proxy DNS when using SOCKS v5`
    - Suggest: `-socks4-remote-dns`
- `backup-multi-profile-warning-message` — `browser/browser/preferences/preferences.ftl` — `backup-multi-profile-warning-message` quotes “Hacer copia de seguridad ahora” but the string it names, `settings-data-backup-trigger-button`, reads “Hacer ahora copia de seguridad”
    - Current: `message: Para garantizar que este cambio sea incluido en sus copias de seguridad, abra cada perfil y seleccione “Hacer copia de seguridad ahora” en Ajustes.`
    - Source: `message: To make sure this change is included in your backups, open each profile and choose “Backup now” in Settings.`
    - Suggest: `Hacer ahora copia de seguridad`
    - In the source this string quotes “Backup now”, which is exactly the value of `settings-data-backup-trigger-button` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `containers-new-tab-check2` — `browser/browser/preferences/preferences.ftl` — Label uses informal "Selecciona" while the description in the same string uses formal address.
    - Current: `Selecciona un contenedor para cada pestaña nueva`
    - Source: `accesskey: S description: This will open the containers menu every time you press the open new tab button. label: Select a container for each new tab`
    - Suggest: `Seleccione un contenedor para cada pestaña nueva`
    - The locale convention is formal (usted); the accompanying description uses "presione", so the informal imperative is inconsistent within the same string.
- `forms-primary-pw-on-2` — `browser/browser/preferences/preferences.ftl` — "Primary password" translated as "contraseña maestra" instead of the current term "contraseña principal".
    - Current: `La contraseña maestra está <strong>ACTIVADA</strong>`
    - Source: `Primary password is <strong>ON</strong>`
    - Suggest: `La contraseña principal está <strong>ACTIVADA</strong>`
    - Mozilla renamed "master password" to "primary password"; es-ES uses "contraseña principal" for "primary password", so this reintroduces the deprecated term.
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

### Withdrawn to date (2)

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — raised by `accesskey`, withdrawn 2026-09-03
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — raised by `accesskey`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (113)

- `neterror-net-offline` — `toolkit/toolkit/neterror/netError.ftl` — fixed 2026-09-14
- `manifest-loading` — `devtools/client/application.ftl` — fixed 2026-09-03
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
