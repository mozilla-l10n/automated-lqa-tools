# Firefox l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `39e5663f3de7` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `50d2f3b3f7c8` |
| **Previous run** | 2026-08-22 @ `9441127ed8c4` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,185 |

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
| Strings | 17,185 |
| Missing strings | 995 |
| Obsolete strings | 0 |
| Files absent from the locale | 5 |
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

**995 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 147
- `browser/browser/aiWindow.ftl` — 131
- `browser/browser/appmenu.ftl` — 67
- `browser/browser/aiWindowContent.ftl` — 51
- `browser/browser/preferences/preferences.ftl` — 41
- `browser/browser/browser.ftl` — 33
- `toolkit/toolkit/global/theme-picker.ftl` — 28
- `devtools/client/toolbox-options.ftl` — 28
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `browser/browser/ipProtection.ftl` — 26
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 24
- `browser/browser/firefoxView.ftl` — 23

**Files absent from the locale:**

- `browser/browser/preferences/browserIcon.ftl`
- `browser/browser/sharePanel.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`
- `toolkit/toolkit/global/theme-picker.ftl`

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

## 3. Open findings (101)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 2 |
| 2 | Wrong content (says something other than the English) | 41 |
| 3 | Degraded language (grammar, spelling, terminology) | 42 |
| 4 | Cosmetic (typography, spacing) | 16 |

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
- `general-meta-tags` — `browser/browser/pageInfo.ftl` — the [one] plural variant is garbled: it renders "Meta (1 etiqueta)" followed by four duplicated untranslated "Meta (1 tag)" lines → collapse to a single [one] Meta (1 etiqueta).
    - Current: `[one]`
    - Source: `value: {$tags ->} [one] Meta (1 tag) [other] Meta ({ $tags } tags)`
    - Suggest: `[one] Meta (1 etiqueta)`
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
- `inactive-css-no-width-height` — `devtools/client/tooltips.ftl` — missing space after </strong> glues words ("propiedadno tiene") → add a space.
    - Source: `<strong>{ $property }</strong> has no effect on this element since its width and height cannot be set.`
    - Suggest: `add a space.`

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-export-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-export-password-os-auth-dialog-message-macosx (aboutLogins.ftl) — "logins" → "usuarios" → "inicios de sesión".
    - Source: `export saved logins and passwords`
    - Suggest: `"usuarios" → "inicios de sesión".`
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — dropped "/8" from "127.0.0.1/8" (comment: do not translate).
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — cert-format-pkcs7-chain (certManager.ftl) — "(PKCX#7)" → "(PKCS#7)".
    - Source: `X.509 Certificate with chain (PKCS#7)`
    - Suggest: `"`
- `pippki-incorrect-pw` — `security/manager/security/pippki/pippki.ftl` — pippki-incorrect-pw (pippki.ftl) — adds "maestra": "contraseña maestra" → "contraseña actual" (source: "current password").
    - Source: `You did not enter the correct current password. Please try again.`
    - Suggest: `"contraseña actual"`
- `support-remote-settings-status-ok` — `toolkit/toolkit/about/aboutSupport.ftl` — support-remote-settings-status-ok (aboutSupport.ftl) — status "OK" → "Aceptar" (the verb) → "Correcto"/"OK".
    - Source: `OK`
    - Suggest: `"Aceptar"`
- `about-webauthn-auth-info-true` — `toolkit/toolkit/about/aboutWebauthn.ftl` — about-webauthn-auth-info-true (aboutWebauthn.ftl) — "Verdadero" → True (comment: don't translate; -auth-option-true correctly kept "True").
    - Source: `True`
    - Suggest: `-auth-option-true`
- `about-webrtc-track-identifier` — `toolkit/toolkit/about/aboutWebrtc.ftl` — about-webrtc-track-identifier (aboutWebrtc.ftl) — "MediaStreamTrack" → "Identificador de rastreo" (tracking) → "…de pista".
    - Source: `Track Identifier`
    - Suggest: `"Identificador de rastreo"`
- `certificate-viewer-ocsp-stapling` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-ocsp-stapling (certviewer.ftl) — "OCSP Stapling" → "Sello de tiempo OCSP" (timestamp) → "Grapado OCSP".
    - Source: `OCSP Stapling`
    - Suggest: `"Sello de tiempo OCSP"`
- `contentanalysis-operationtype-print` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — contentanalysis-operationtype-print (contentanalysis.ftl) — noun "print" → verb "imprimir" → "impresión" (companions are nouns).
    - Source: `print`
    - Suggest: `verb "imprimir" → "impresión"`
- `language-name-af` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Afrikaans`
- `language-name-hi` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Hindi`
- `language-name-hsb` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Upper Sorbian`
- `language-name-wa` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Walloon`
- `language-name-wen` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Sorbian`
- `language-name-yi` — `toolkit/toolkit/intl/languageNames.ftl` — Language names (intl/languageNames.ftl): language-name-af "Africano" → Afrikáans; language-name-yi "Judío" → Yidis; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Sorbio superior; language-name-wen "Serbio" → Sorbio; language-name-wa "valón" → Valón (capitalize).
    - Source: `Yiddish`
- `region-name-az` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Azerbaijan`
- `region-name-ci` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Côte d’Ivoire`
- `region-name-fo` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Faroe Islands`
- `region-name-ht` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Haiti`
- `region-name-st` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `São Tomé and Príncipe`
- `region-name-sz-2019` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Eswatini`
- `region-name-vn` — `toolkit/toolkit/intl/regionNames.ftl` — Region names (intl/regionNames.ftl): region-name-ci "Costa Ivory" → Costa de Marfil; region-name-fo "Islas Faroe" → Islas Feroe; region-name-sz-2019 "Suazilandia" → Esuatini (source updated to Eswatini); region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-ht "Haiti" → Haití; region-name-vn "Vietnám" → Vietnam; region-name-az "Azerbayán" → Azerbaiyán.
    - Source: `Vietnam`
- `pdfjs-views-manager-pages-status-undo-copy-label` — `toolkit/toolkit/pdfviewer/viewer.ftl` — pdfjs-views-manager-pages-status-undo-copy-label (viewer.ftl) — [other] "{ $count } páginas cortadas" → "copiadas" (this is the copy label).
    - Current: `[other]`
    - Source: `{$count ->} [one] 1 page copied [other] { $count } pages copied`
    - Suggest: `"copiadas"`

### C. Grammar, agreement & spelling

- `restore-page-error-title` — `browser/browser/aboutSessionRestore.ftl` — restore-page-error-title (aboutSessionRestore.ftl) — "Tenemos problema" → "problemas".
    - Source: `Sorry. We’re having trouble getting your pages back.`
    - Suggest: `"problemas".`
- `welcome-back-page-info-link` — `browser/browser/aboutSessionRestore.ftl` — welcome-back-page-info-link (aboutSessionRestore.ftl) — "valores predeterminado" → "predeterminados".
    - Source: `Your add-ons and customizations have been removed and your browser settings have been restored to their defaults. If this didn’t fix your issue, <a data-l10n-name="link-more">learn more about what you can do.</a>`
    - Suggest: `"predeterminados".`
- `addon-install-error-not-signed` — `browser/browser/addonNotifications.ftl` — addon-install-error-not-signed (addonNotifications.ftl) — "que este sitio instala" → "instale" (subjunctive).
    - Source: `{ -brand-short-name } has prevented this site from installing an unverified add-on.`
    - Suggest: `"instale"`
- `ai-window-memories-section` — `browser/browser/aiFeatures.ftl` — ai-window-memories-section (aiFeatures.ftl) — "…recuerdos. SE usan…" → "Se usan".
    - Source: `description: { -brand-short-name } can learn from your activity to create memories. They’re used to help personalize responses and are stored locally on this device. label: Memories`
    - Suggest: `"Se usan".`
- `ai-window-open-sidebar` — `browser/browser/aiFeatures.ftl` — ai-window-open-sidebar (aiFeatures.ftl) — "Ciérrrelo" (triple r) → "Ciérrelo".
    - Source: `description: Show the assistant sidebar on each new tab. Close it anytime. label: Open assistant automatically`
    - Suggest: `"Ciérrelo".`
- `contextual-manager-passwords-username-tooltip` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-username-tooltip (contextual-manager.ftl) — "Introduca" → "Introduzca".
    - Source: `Enter the username, email address, or account number you use to sign in.`
    - Suggest: `"Introduzca".`
- `taskbar-tabs-value-prop-callout-subtitle` — `browser/browser/featureCallout.ftl` — taskbar-tabs-value-prop-callout-subtitle (featureCallout.ftl) — "Abralo" → "Ábralo".
    - Source: `Launch it in its own window and a simplified interface with a single click.`
    - Suggest: `"Ábralo".`
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — vertical-tabs-callout-2-subtitle (featureCallout.ftl) — "facilita la explorar" → "facilita explorar".
    - Source: `This layout makes it easy to quickly scan your list of tabs. Plus, you can adjust the width to see more or less of your tab titles.`
    - Suggest: `"facilita explorar".`
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — spotlight-peace-mind-body (asrouter.ftl) — "nada… deberían meterse" → "debería interponerse".
    - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
    - Suggest: `"debería interponerse".`
- `newtab-wallpaper-celestial-river` — `browser/browser/newtab/newtab.ftl` — newtab-wallpaper-celestial-river (newtab.ftl) — "satelite"/"rio" → "satélite"/"río".
    - Source: `Satellite image of river`
- `onboarding-new-user-time-based-survey-title` — `browser/browser/newtab/onboarding.ftl` — onboarding-new-user-time-based-survey-title (onboarding.ftl) — "¿Cuanto tiempo…" → "¿Cuánto".
    - Source: `How long have you been using { -brand-short-name }?`
    - Suggest: `"¿Cuánto".`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — Duplicated words: private-browsing-description2 (aboutAddons.ftl) "la la extensión"; inactive-css-not-grid-or-flex-item (tooltips.ftl) "un un ítem"; onboarding-refresh-gratitude-subtitle (onboarding.ftl) "más más".
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
- `permissions-site-notification-disable-desc` — `browser/browser/preferences/permissions.ftl` — permissions-site-notification-disable-desc (permissions.ftl) — "envirle" → "enviarle".
    - Source: `This will prevent any websites not listed above from requesting permission to send notifications. Blocking notifications may break some website features.`
    - Suggest: `"enviarle".`
- `info-known-breaches-found` — `browser/browser/protections.ftl` — info-known-breaches-found (protections.ftl) — [other] "La filtraciones" → "Las filtraciones".
    - Current: `[other]`
    - Source: `{$count ->} [one] Known data breach has exposed your information [other] Known data breaches have exposed your information`
    - Suggest: `"Las filtraciones".`
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — recently-closed-window-panel-tooltip (recentlyClosed.ftl) — [one] word order "pestaña { $tabCount }" → "{ $tabCount } pestaña".
    - Current: `[one]`
    - Source: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } ({ $tabCount } tab, closed at { $closedAt }) [other] { $winTitle } ({ $tabCount } tabs, closed at { $closedAt })`
    - Suggest: `"{ $tabCount } pestaña".`
- `report-broken-site-panel-reason-account2` — `browser/browser/reportBrokenSite.ftl` — report-broken-site-panel-reason-account2 (reportBrokenSite.ftl) — "No se puede iniciar sesión ni registrarme" → "registrarse".
    - Source: `label: Can’t sign in or register`
    - Suggest: `"registrarse".`
- `webrtc-allow-share-screen-with-file` — `browser/browser/webrtcIndicator.ftl` — webrtc-allow-share-screen-with-file (webrtcIndicator.ftl) — "esté archivo local" → "este archivo local".
    - Source: `Allow this local file to see your screen?`
    - Suggest: `"este archivo local".`
- `options-show-user-agent-shadow-dom-label` — `devtools/client/toolbox-options.ftl` — options-show-user-agent-shadow-dom-label (toolbox-options.ftl) — "Mostra" → "Mostrar".
    - Source: `Show Browser Shadow DOM`
    - Suggest: `"Mostrar".`
- `inactive-css-not-grid-or-flex-item` — `devtools/client/tooltips.ftl` — Duplicated words: private-browsing-description2 (aboutAddons.ftl) "la la extensión"; inactive-css-not-grid-or-flex-item (tooltips.ftl) "un un ítem"; onboarding-refresh-gratitude-subtitle (onboarding.ftl) "más más".
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not a grid or flex item.`
- `protected-auth-alert` — `security/manager/security/pippki/pippki.ftl` — protected-auth-alert (pippki.ftl) — "introducoiendo" → "introduciendo".
    - Source: `Please authenticate to the token “{ $tokenName }”. How to do so depends on the token (for example, using a fingerprint reader or entering a code with a keypad).`
    - Suggest: `"introduciendo".`
- `details-notification-soft-blocked-other-disabled` — `toolkit/toolkit/about/aboutAddons.ftl` — "ha sido desactivada" / "Usarla" → "desactivado" / "Usarlo" (masc. "complemento").
    - Source: `message: This add-on is restricted for violating Mozilla’s policies and has been disabled. You can enable it, but this may be risky.`
- `private-browsing-description2` — `toolkit/toolkit/about/aboutAddons.ftl` — Duplicated words: private-browsing-description2 (aboutAddons.ftl) "la la extensión"; inactive-css-not-grid-or-flex-item (tooltips.ftl) "un un ítem"; onboarding-refresh-gratitude-subtitle (onboarding.ftl) "más más".
    - Source: `{ -brand-short-name } is changing how extensions work in private browsing. Any new extensions you add to { -brand-short-name } won’t run by default in Private Windows. Unless you allow it in settings, the extension won’…`
- `rights-intro-point-5` — `toolkit/toolkit/about/aboutRights.ftl` — rights-intro-point-5 (aboutRights.ftl) — "en la términos del servicio" → "los términos".
    - Source: `Some { -brand-short-name } features make use of web-based information services, however, we cannot guarantee they are 100% accurate or error-free. More details, including information on how to disable the features that…`
    - Suggest: `"los términos".`
- `rights-intro-point-6` — `toolkit/toolkit/about/aboutRights.ftl` — rights-intro-point-6 (aboutRights.ftl) — "contenido de víeo" → "vídeo".
    - Source: `In order to play back certain types of video content, { -brand-short-name } downloads certain content decryption modules from third parties.`
    - Suggest: `"vídeo".`
- `rights-locationawarebrowsing` — `toolkit/toolkit/about/aboutRights.ftl` — rights-locationawarebrowsing (aboutRights.ftl) — "siga esto pasos" → "estos pasos".
    - Source: `<strong>Location Aware Browsing: </strong>is always opt-in. No location information is ever sent without your permission. If you wish to disable the feature completely, follow these steps:`
    - Suggest: `"estos pasos".`
- `blocked-mismatched-version` — `toolkit/toolkit/about/aboutSupport.ftl` — blocked-mismatched-version (aboutSupport.ftl) — "diferencia e versión" → "de versión".
    - Source: `Blocked for your graphics driver version mismatch between registry and DLL.`
    - Suggest: `"de versión".`
- `intl-locales-default` — `toolkit/toolkit/about/aboutSupport.ftl` — intl-locales-default (aboutSupport.ftl) — "Idioma preterminado" → "predeterminado".
    - Source: `Default Locale`
    - Suggest: `"predeterminado".`
- `about-telemetry-no-search-results-all` — `toolkit/toolkit/about/aboutTelemetry.ftl` — about-telemetry-no-search-results-all (aboutTelemetry.ftl) — "ningun sección" → "ninguna sección".
    - Source: `Sorry! There are no results in any sections for “{ $searchTerms }”`
    - Suggest: `"ninguna sección".`
- `about-webrtc-configuration-element-not-provided` — `toolkit/toolkit/about/aboutWebrtc.ftl` — about-webrtc-configuration-element-not-provided (aboutWebrtc.ftl) — "No porporcionado" → "proporcionado".
    - Source: `Not Provided`
    - Suggest: `"proporcionado".`
- `pdfjs-editor-alt-text-dialog-label` — `toolkit/toolkit/pdfviewer/viewer.ftl` — pdfjs-editor-alt-text-dialog-label (viewer.ftl) — "Eligir una opción" → "Elegir".
    - Source: `Choose an option`
    - Suggest: `"Elegir".`

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
- `manifest-loading` — `devtools/client/application.ftl` — manifest — "Manifesto" (manifest-view-header, manifest-loading, etc.) vs "Manifiesto" (manifest-empty-intro2) → Manifiesto.
    - Source: `Loading manifest…`
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

- `about-logins-error-message-duplicate-login-with-link` — `browser/browser/aboutLogins.ftl` — Wrong/extra punctuation. newtab-privacy-modal-paragraph-2 spurious comma ("de que, <strong>"); about-logins-error-message-duplicate-login-with-link stray spaces inside the link.
    - Source: `An entry for { $loginTitle } with that username already exists. <a data-l10n-name="duplicate-link">Go to existing entry?</a>`
- `annotations-make-default-pdf-handler-title` — `browser/browser/newtab/asrouter.ftl` — Missing space after markup / brand. fxa-qrcode-pair-step2-signin ("/>en Android)"), annotations-make-default-pdf-handler-title ("que{ -brand }").
    - Source: `Make { -brand-short-name } your default PDF editor?`
- `etp-strict-exceptions-infobar-message` — `browser/browser/newtab/asrouter.ftl` — missing space), contentanalysis-no-agent-connected-message-content/-invalid-agent-signature-message-content ("{ $agent }.{ $content }"), backgroundupdate-task-description (space before final period).
    - Source: `<strong>Strict tracking protection can cause sites to break.</strong> Fix common issues by unblocking essential elements that could contain trackers.`
    - Suggest: `-invalid-agent-signature-message-content`
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — Wrong/extra punctuation. newtab-privacy-modal-paragraph-2 spurious comma ("de que, <strong>"); about-logins-error-message-duplicate-login-with-link stray spaces inside the link.
    - Source: `In addition to dishing up captivating stories, we also show you relevant, highly-vetted content from select sponsors. Rest assured, <strong>your browsing data never leaves your personal copy of { -brand-product-name }</…`
- `newtab-toast-thumbs-up-or-down2` — `browser/browser/newtab/newtab.ftl` — Missing period. newtab-toast-thumbs-up-or-down2 (newtab.ftl) "Gracias Su opinión…" → "Gracias. Su opinión…"; mr2022-onboarding-colorway-description-visionary/-activist (onboarding.ftl) missing period after the bold clause.
    - Source: `message: Thanks. Your feedback will help us improve your feed.`
- `mr2022-onboarding-colorway-description-visionary` — `browser/browser/newtab/onboarding.ftl` — Missing period. newtab-toast-thumbs-up-or-down2 (newtab.ftl) "Gracias Su opinión…" → "Gracias. Su opinión…"; mr2022-onboarding-colorway-description-visionary/-activist (onboarding.ftl) missing period after the bold clause.
    - Source: `<b>You are a Visionary.</b> You question the status quo and move others to imagine a better future.`
- `onboarding-new-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — missing space), contentanalysis-no-agent-connected-message-content/-invalid-agent-signature-message-content ("{ $agent }.{ $content }"), backgroundupdate-task-description (space before final period).
    - Source: `Switch it up whenever you want in the sidebar settings.`
    - Suggest: `-invalid-agent-signature-message-content`
- `app-manager-handle-file` — `browser/browser/preferences/applicationManager.ftl` — "manejar { $type } enlaces/contenido" → "gestionar los enlaces { $type }" / "el contenido { $type }".
    - Source: `The following applications can be used to handle { $type } content.`
- `app-manager-handle-protocol` — `browser/browser/preferences/applicationManager.ftl` — "manejar { $type } enlaces/contenido" → "gestionar los enlaces { $type }" / "el contenido { $type }".
    - Source: `The following applications can be used to handle { $type } links.`
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Missing space after markup / brand. fxa-qrcode-pair-step2-signin ("/>en Android)"), annotations-make-default-pdf-handler-title ("que{ -brand }").
    - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
- `protections-blocking-tracking-content` — `browser/browser/siteProtections.ftl` — Capitalization (mid-sentence). protections-blocking-tracking-content ("Bloqueado" → "bloqueado"), protections-not-blocking-cross-site-tracking-cookies ("Cookies" → "cookies") in siteProtections.ftl.
    - Source: `title: Tracking Content Blocked`
- `protections-not-blocking-cross-site-tracking-cookies` — `browser/browser/siteProtections.ftl` — Capitalization (mid-sentence). protections-blocking-tracking-content ("Bloqueado" → "bloqueado"), protections-not-blocking-cross-site-tracking-cookies ("Cookies" → "cookies") in siteProtections.ftl.
    - Source: `title: Not Blocking Cross-Site Tracking Cookies`
- `place-database-stats-size-kib` — `toolkit/toolkit/about/aboutSupport.ftl` — Units. place-database-stats-size-kib (aboutSupport.ftl) — "(KB)" → "(KiB)".
    - Source: `Size (KiB)`
    - Suggest: `"`
- `remote-debugging-title` — `toolkit/toolkit/about/aboutSupport.ftl` — missing space), contentanalysis-no-agent-connected-message-content/-invalid-agent-signature-message-content ("{ $agent }.{ $content }"), backgroundupdate-task-description (space before final period).
    - Source: `Remote Debugging (Chromium Protocol)`
    - Suggest: `-invalid-agent-signature-message-content`
- `fp-certerror-bad-domain-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — missing space), contentanalysis-no-agent-connected-message-content/-invalid-agent-signature-message-content ("{ $agent }.{ $content }"), backgroundupdate-task-description (space before final period).
    - Source: `The site is set up to allow only secure connections, but there’s a problem with the site’s certificate. It’s possible that a bad actor is trying to impersonate the site. Sites use certificates issued by a certificate au…`
    - Suggest: `-invalid-agent-signature-message-content`
- `pdfjs-editor-alt-text-dialog-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Redundant parenthetical. pdfjs-editor-alt-text-dialog-description (viewer.ftl) — "El texto alternativo (texto alternativo) ayuda…" → drop the repeat.
    - Source: `Alt text (alternative text) helps when people can’t see the image or when it doesn’t load.`
    - Suggest: `drop the repeat.`

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

### Fixed to date (39)

- `picture-in-picture-panel-body` — `browser/browser/browser.ftl` — fixed 2026-07-28
- `firefoxview-history-nav` — `browser/browser/firefoxView.ftl` — fixed 2026-07-28
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-28
- `cfr-doorhanger-video-support-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-28
- `newtab-empty-section-highlights` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-28
- `amo-picker-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-28
- `blocklist-item-moz-full-description` — `browser/browser/preferences/blocklists.ftl` — fixed 2026-07-28
- `fonts-langgroup-malayalam` — `browser/browser/preferences/fonts.ftl` — fixed 2026-07-28
- `fonts-langgroup-trad-chinese` — `browser/browser/preferences/fonts.ftl` — fixed 2026-07-28
- `permissions-site-xr-disable-desc` — `browser/browser/preferences/permissions.ftl` — fixed 2026-07-28
- `permissions-window2` — `browser/browser/preferences/permissions.ftl` — fixed 2026-07-28
- `cookie-tab-content` — `browser/browser/protections.ftl` — fixed 2026-07-28
- `protections-panel-tracking-content` — `browser/browser/protectionsPanel.ftl` — fixed 2026-07-28
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — fixed 2026-07-28
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-28
- `accessibility-keyboard-issue-focusable` — `devtools/client/accessibility.ftl` — fixed 2026-07-28
- `serviceworker-worker-unregister` — `devtools/client/application.ftl` — fixed 2026-07-28
- `perftools-button-cancel-recording` — `devtools/client/perftools.ftl` — fixed 2026-07-28
- `styleeditor-no-stylesheet-tip` — `devtools/client/styleeditor.ftl` — fixed 2026-07-28
- `options-screenshot-label` — `devtools/client/toolbox-options.ftl` — fixed 2026-07-28
- `inactive-css-not-absolutely-positioned-item` — `devtools/client/tooltips.ftl` — fixed 2026-07-28
- `add-exception-domain-mismatch-long` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-28
- `add-exception-expired-long` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-28
- `text-no-overrides` — `toolkit/toolkit/about/aboutCompat.ftl` — fixed 2026-07-28
- `unregister-button` — `toolkit/toolkit/about/aboutServiceWorkers.ftl` — fixed 2026-07-28
- `about-webauthn-auth-info-false` — `toolkit/toolkit/about/aboutWebauthn.ftl` — fixed 2026-07-28
- `about-webauthn-auth-option-false` — `toolkit/toolkit/about/aboutWebauthn.ftl` — fixed 2026-07-28
- `about-webrtc-raw-local-candidate` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-07-28
- `about-webrtc-rtp-stats-heading` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-07-28
- `certificate-viewer-inc-state-province` — `toolkit/toolkit/about/certviewer.ftl` — fixed 2026-07-28
- `url-classifier-provider-back-off-time` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-28
- `experimental-features-newtab-widget-lists-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — fixed 2026-07-28
- `webext-colorway-theme-migration-notification-button` — `toolkit/toolkit/global/extensions.ftl` — fixed 2026-07-28
- `fp-certerror-unknown-issuer-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — fixed 2026-07-28
- `certerror-coep-learn-more` — `toolkit/toolkit/neterror/netError.ftl` — fixed 2026-07-28
- `pdfjs-views-manager-status-warning-delete-label` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-07-28
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — fixed 2026-07-28
- `settings-pp-not-wanted` — `toolkit/toolkit/preferences/preferences.ftl` — fixed 2026-07-28
- `printui-backgrounds-checkbox` — `toolkit/toolkit/printing/printUI.ftl` — fixed 2026-07-28
