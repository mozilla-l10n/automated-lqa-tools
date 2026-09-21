# Firefox l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `3f7b6c3c060f` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `749ea3a23fef` |
| **Previous run** | 2026-09-14 @ `e44f1369fb6d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 10 of 15,810 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `genai-shortcut-button-2` — `browser/browser/genai.ftl` — "Preguntar { $provider }" lacks the preposition "a" required before the provider name in Spanish.
    - Current: `Preguntar { $provider }`
    - Source: `aria-label: Ask { $provider } tooltiptext: Ask { $provider }`
    - Suggest: `Preguntar a { $provider }`
    - In Spanish the person/entity asked takes the preposition "a"; "Preguntar Claude" is ungrammatical for en-US "Ask { $provider }".
- `user-context-shopping2` — `toolkit/toolkit/global/contextual-identity.ftl` — "Shopping" as a container label is rendered with the verb "Comprar" instead of a noun like "Compras".
    - Current: `Comprar`
    - Source: `label: Shopping`
    - Suggest: `Compras`
    - The sibling labels (Trabajo, Banca) are nouns naming a context; en-US "Shopping" is a noun here, not an action.

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
| Files | 320 |
| Strings | 15,810 |
| Missing strings | 423 |
| Obsolete strings | 0 |
| Files absent from the locale | 6 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 121 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 108 |

### Completeness

**423 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 99
- `toolkit/services/aboutSyncLog.ftl` — 28
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 23
- `toolkit/toolkit/about/aboutPDF.ftl` — 21
- `browser/browser/newtab/onboarding.ftl` — 19
- `browser/browser/sharePanel.ftl` — 17
- `toolkit/toolkit/about/aboutAddons.ftl` — 17
- `toolkit/toolkit/main-window/autocomplete.ftl` — 16
- `toolkit/toolkit/neterror/netError.ftl` — 14
- `browser/browser/preferences/preferences.ftl` — 12
- `browser/browser/ipProtection.ftl` — 11
- `browser/browser/featureCallout.ftl` — 10

**Files absent from the locale:**

- `browser/browser/sharePanel.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 461, `straight-double` 130, `curly-single` 78, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 90, `straight` 37 | _mixed_ |
| ellipsis | `char` 362, `ascii` 19 | **char** |
| dash | `em` 50, `en` 1 | **em** |
| nbsp | `total` 16, `narrow` 10, `before-punctuation` 12, `space-before-punctuation` 6 | _mixed_ |
| inverted marks | `open-question` 316, `open-exclamation` 72 | **open-question** |
| register | `informal` 1208, `formal` 206 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 121 strings** — 121 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
    - Affected: `addressbar-locbar-clipboard-option`, `addressbar-locbar-openpage-option`, `addressbar-locbar-quickactions-option`, `appmenu-addon-post-install-pin-toolbarbutton-checkbox`, `appmenu-help-more-troubleshooting-info`, `appmenu-help-not-deceptive`, `appmenu-homepage-controlled-changes`, `appmenu-new-tab-controlled-changes`, `appmenu-tab-hide-controlled`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2` …and 108 more
- **typography — 108 strings** — 108 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CORSPreflightDidNotSucceed3`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords`, `ImageMapRectBoundsError` …and 96 more

---

## 3. Open findings (43)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 14 |
| 3 | Degraded language (grammar, spelling, terminology) | 23 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `migration-safari-password-import-post-sequoia-step2` — `browser/browser/migrationWizard.ftl` — The menu path "Export All Passwords to File…" lost the "to File" part.
    - Current: `Exportar todas las contraseñas…`
    - Source: `From the menu bar at the top of the screen, choose File > Export All Passwords to File…`
    - Suggest: `Exportar todas las contraseñas a un archivo…`
    - The source names the actual macOS menu item "Export All Passwords to File…"; omitting "to File" makes the instruction not match the UI the user must find.
- `refresh-reinstalled-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — "you’ve reinstalled" turned into an impersonal passive, dropping the second person.
    - Current: `Parece que se ha reinstalado { -brand-short-name }.`
    - Source: `Looks like you’ve reinstalled { -brand-short-name }. Want us to clean it up for a fresh, like-new experience?`
    - Suggest: `Parece que has reinstalado { -brand-short-name }.`
    - The en-US addresses the user directly ("you've reinstalled"); the Spanish removes the agent.
- `newtab-privacy-message-info-9` — `browser/browser/newtab/newtab.ftl` — "go-to browser for built-in privacy" rendered as making Firefox the default browser, changing the meaning.
    - Current: `Utiliza { -brand-short-name } como navegador predeterminado para una protección de privacidad integrada.`
    - Source: `Make { -brand-short-name } your go-to browser for built-in privacy.`
    - Suggest: `Haz de { -brand-short-name } tu navegador de referencia por su privacidad integrada.`
    - The en-US says to make Firefox your go-to browser thanks to its built-in privacy, not to set it as the system default browser (though the CTA is "Make default", the message itself does not say "predeterminado"); the Spanish also reverses the causal relation, stating the purpose is to get privacy protection.
- `newtab-sports-widget-message-survey-widget-body` — `browser/browser/newtab/newtab.ftl` — "try the new one in your lineup" rendered as "prueba el nuevo widget destacado" (the new featured widget).
    - Current: `prueba el nuevo widget destacado`
    - Source: `Share your feedback to help us improve future widgets. Then, try the new one in your lineup.`
    - Suggest: `prueba el nuevo widget de tu selección`
    - en-US refers to the new widget in the user's lineup; "destacado" (featured) invents a qualifier not in the source.
- `smartwindow-onboarding-title` — `browser/browser/newtab/onboarding.ftl` — "Make it your go-to" mistranslated as "use it as a starting point".
    - Current: `Utiliza { -smart-window-brand-name } como punto de partida`
    - Source: `Make { -smart-window-brand-name } your go-to`
    - Suggest: `Haz de { -smart-window-brand-name } tu opción preferida`
    - en-US "your go-to" means the preferred/default choice, not a "punto de partida" (starting point).
- `smartwindow-sidebar-auto-open-callout-body` — `browser/browser/newtab/onboarding.ftl` — Present-tense "You can still open it" rendered as future, dropping "still".
    - Current: `Podrás abrirlo cuando lo necesites.`
    - Source: `You can still open it whenever you need it.`
    - Suggest: `Aún puedes abrirlo cuando lo necesites.`
    - en-US says "You can still open it whenever you need it" — present ability with "still"; the Spanish states a future capability and omits "still".
- `passports-no-passports-stored-message` — `browser/browser/preferences/preferences.ftl` — "No passports added" translated as "No hay pasaportes guardados" (stored/saved).
    - Current: `No hay pasaportes guardados`
    - Source: `label: No passports added`
    - Suggest: `No se han agregado pasaportes`
    - The source label says "added", not "stored"; the developer comment distinguishes stored vs. the label wording.
- `preferences-ai-controls-sidebar-chatbot-group-2` — `browser/browser/preferences/preferences.ftl` — "Keep a chatbot in view" rendered as "Mantén tu chatbot" (your chatbot).
    - Current: `Mantén tu chatbot a la vista mientras navegas.`
    - Source: `description: Keep a chatbot in view as you browse. Choose from Anthropic Claude, ChatGPT, Copilot, Google Gemini, and Mistral Vibe. label: AI chatbot providers in sidebar`
    - Suggest: `Mantén un chatbot a la vista mientras navegas.`
    - The source uses the indefinite "a chatbot"; "tu chatbot" asserts the user already has one.
- `security-privacy-issue-warning-doh2` — `browser/browser/preferences/preferences.ftl` — "sites you’re about to visit" translated as "sitios que visitas", losing the future sense.
    - Current: `conozca los sitios que visitas`
    - Source: `description: DNS over HTTPS helps hide what sites you’re about to visit from your network provider. label: DNS over HTTPS is disabled`
    - Suggest: `conozca los sitios que estás por visitar`
    - The en-US refers to sites the user is about to visit; the Spanish states sites the user visits generally.
- `security-privacy-issue-warning-ech2` — `browser/browser/preferences/preferences.ftl` — "sites you’re about to visit" translated as "sitios que visitas", losing the future sense.
    - Current: `conozca los sitios que visitas`
    - Source: `description: Encrypted Client Hello helps hide what sites you’re about to visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `conozca los sitios que estás por visitar`
    - The en-US refers to sites the user is about to visit; the Spanish states sites the user visits generally.
- `perftools-presets-networking-with-logs-description` — `devtools/client/perftools.ftl` — "networking logs" rendered as "registros de tráfico" and "the URLs you visit" changed to past tense.
    - Current: `incluyendo registros de tráfico`
    - Source: `Preset for investigating networking bugs in { -brand-shorter-name }, including networking logs. These logs may contain sensitive information such as the URLs you visit.`
    - Suggest: `incluyendo registros de red`
    - The source says "including networking logs"; "registros de tráfico" (traffic logs) is a different term, inconsistent with "errores de red" used in the same string for "networking".
- `options-reopen-toolbox-message` — `devtools/client/toolbox-options.ftl` — "reopening the toolbox" translated as "reiniciar la caja de herramientas" (restarting).
    - Current: `(Requiere reiniciar la caja de herramientas)`
    - Source: `(requires reopening the toolbox)`
    - Suggest: `(requiere volver a abrir la caja de herramientas)`
    - The source says the toolbox must be reopened, not restarted; also the source is lowercase inside parentheses.
- `about-webrtc-closed-peerconnection-disclosure-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "PeerConnections" translated to "conexiones de pares" in the hide-msg variant only (comment: keep PeerConnection).
    - Source: `Show Closed PeerConnections`
- `url-classifier-content-classifier-force-third-party` — `toolkit/toolkit/about/url-classifier.ftl` — The reference to the top frame is dropped from the checkbox label.
    - Current: `Forzar como solicitud de terceros`
    - Source: `Force third-party to top frame`
    - Suggest: `Forzar como de terceros respecto al marco superior`
    - en-US is "Force third-party to top frame"; the developer comment says the request is forced to be third-party relative to the top-level page. The Spanish omits "to top frame".
- `moz-box-link-opens-in-new-tab` — `toolkit/toolkit/global/mozBoxBase.ftl` — Descriptive text "Opens in a new tab" was rendered as an imperative/infinitive command "Abrir en una nueva pestaña".
    - Current: `Abrir en una nueva pestaña`
    - Source: `Opens in a new tab`
    - Suggest: `Se abre en una nueva pestaña`
    - The en-US string describes the link's behavior (third person, "Opens in a new tab"), typically used as an accessible label; the Spanish infinitive reads as an action command, changing the meaning.

### C. Grammar, agreement & spelling

- `genai-shortcut-button-2` — `browser/browser/genai.ftl` — "Preguntar { $provider }" lacks the preposition "a" required before the provider name in Spanish.
    - Current: `Preguntar { $provider }`
    - Source: `aria-label: Ask { $provider } tooltiptext: Ask { $provider }`
    - Suggest: `Preguntar a { $provider }`
    - In Spanish the person/entity asked takes the preposition "a"; "Preguntar Claude" is ungrammatical for en-US "Ask { $provider }".
- `launch-on-login-autostart-infobar-message` — `browser/browser/newtab/asrouter.ftl` — "mas" is missing its accent; should be "más adelante".
    - Current: `Puedes cambiar esta preferencia mas adelante en los ajustes.`
    - Source: `{ -brand-short-name } now starts up when you sign in to Windows. You can always change this later in settings.`
    - Suggest: `Puedes cambiar esta preferencia más adelante en los ajustes.`
    - "más" (adverb of quantity/time) requires the accent; "mas" means "but".
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Unspecified size icon`
- `url-classifier-content-classifier-col-exception` — `toolkit/toolkit/about/url-classifier.ftl` — Column header rendered in plural although the source is singular, unlike the matching verdict string.
    - Current: `Excepciones`
    - Source: `Exception`
    - Suggest: `Excepción`
    - en-US "Exception" is singular and denotes a true/false per-row value; the sibling string url-classifier-content-classifier-verdict-exception uses "Excepción".
- `url-classifier-content-classifier-probe-blocking-btn` — `toolkit/toolkit/about/url-classifier.ftl` — Plural used where the source is singular and the button runs one probe.
    - Current: `Sondar bloqueos`
    - Source: `Probe blocking`
    - Suggest: `Sondar bloqueo`
    - en-US "Probe blocking" refers to a single probe reporting whether the request would be blocked; the plural "bloqueos" does not match, while the sibling "Sondar funcionalidad" is singular.

### D. Terminology, register & consistency

- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Sincronizar con el móvil” but the string it names, `sync-to-mobile-button-label`, reads “Sincronización con el móvil”
    - Current: `Escanea el código QR para descargar { -brand-product-name } para móvil. Una vez instalado, seleccione "Sincronizar con el móvil" para acceder a sus contraseñas, marcadores y mucho más sobre la marcha.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Sincronización con el móvil`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Novedades” but the string it names, `releaseNotes-link`, reads “Qué hay de nuevo”
    - Current: `Anular la página "Novedades" posterior a la actualización. Establecer esta política en blanco si deseas deshabilitar la página posterior a la actualización.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Qué hay de nuevo`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `content-blocking-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `Fingerprinters`
- `content-blocking-known-and-suspected-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `Known and suspected fingerprinters`
- `content-blocking-known-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
    - Source: `accesskey: K label: Known fingerprinters`
- `sidebar-item-session-history` — `devtools/client/application.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
    - Source: `(value): Session History alt: Session History Icon title: Session History`
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Interrumpir en……” but the string it names, `watchpoints.submenu`, reads “Interrumpir en…”
    - Current: `Haz clic derecho en un elemento del Inspector y selecciona “Interrumpir en……” para agregar un punto de interrupción`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Interrumpir en…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `options-netmonitor-body-limit-tooltip` — `devtools/client/toolbox-options.ftl` — Formal "Establezca" used where the locale convention is informal address.
    - Current: `Establezca el valor en 0 para no aplicar ninguna limitación.`
    - Source: `title: Request or response bodies which exceed the specified size will be truncated when displayed or downloaded in the Network Monitor. Set to 0 to have no limitation.`
    - Suggest: `Establece el valor en 0 para no aplicar ninguna limitación.`
    - es-MX convention is informal (tú) address; other strings in this batch use "utiliza", "Abre", "selecciona".
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
- `user-context-shopping2` — `toolkit/toolkit/global/contextual-identity.ftl` — "Shopping" as a container label is rendered with the verb "Comprar" instead of a noun like "Compras".
    - Current: `Comprar`
    - Source: `label: Shopping`
    - Suggest: `Compras`
    - The sibling labels (Trabajo, Banca) are nouns naming a context; en-US "Shopping" is a noun here, not an action.
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
    - Source: `You have deleted your Primary Password. Stored passwords and certificate private keys managed by { -brand-short-name } will not be protected.`

### E. Typography, punctuation & spacing

- `urlbar-searchmode-dropmarker2` — `browser/browser/browser.ftl` — Unnecessary title-case capitalization of "Motor de Búsqueda"; Spanish uses sentence case.
    - Current: `Elige un Motor de Búsqueda`
    - Source: `title: Pick a search engine`
    - Suggest: `Elige un motor de búsqueda`
    - en-US uses English title-style capitalization, but Spanish convention (and the rest of the tree) uses sentence case for common nouns like "motor de búsqueda".
- `newtab-privacy-message-info-8` — `browser/browser/newtab/newtab.ftl` — Double space before the brand placeable.
    - Current: `Cuando navegas con  { -brand-short-name } apoyas`
    - Source: `Browsing with { -brand-short-name } supports { -vendor-short-name }’s mission to build a better web.`
    - Suggest: `Cuando navegas con { -brand-short-name } apoyas`
    - There is an extra space between "con" and the brand name in the user-visible text.
- `smartwindow-sidebar-auto-open-callout-accepted-subtitle` — `browser/browser/newtab/onboarding.ftl` — Closing quotation mark is a left curly quote instead of a right curly quote.
    - Current: `“Preguntar“`
    - Source: `Use Ask to open it on any page. Change this anytime in <a data-l10n-name="settings">Settings</a>.`
    - Suggest: `“Preguntar”`
    - The locale convention is curly double quotes; the closing mark here is the opening character “ instead of ”.
- `delete-profile-header-2` — `browser/browser/profiles.ftl` — Closing curly quote is an opening quote instead of a closing one.
    - Current: `¿Eliminar el perfil “{ $profilename }“?`
    - Source: `Delete “{ $profilename }” profile?`
    - Suggest: `¿Eliminar el perfil “{ $profilename }”?`
    - The source uses “…”; the localized string closes with a left double quotation mark, breaking the curly-double convention.
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
