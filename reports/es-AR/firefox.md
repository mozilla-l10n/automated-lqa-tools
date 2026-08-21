# Firefox l10n QA — es-AR

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `5cbe42651962` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `f2e9b7fce093` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,129 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-AR: [android](android.md)

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
| Strings | 18,129 |
| Missing strings | 51 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 4 |
| Markup & `data-l10n-name` defects | 3 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

**51 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 17
- `toolkit/toolkit/about/url-classifier.ftl` — 7
- `browser/browser/appmenu.ftl` — 5
- `browser/browser/preferences/preferences.ftl` — 5
- `browser/browser/featureCallout.ftl` — 4
- `browser/browser/menubar.ftl` — 2
- `browser/browser/sharePanel.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/aiWindowContent.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `browser/browser/newtab/asrouter.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 497, `straight-double` 174, `curly-single` 98 | _mixed_ |
| apostrophe | `typographic` 110, `straight` 70 | _mixed_ |
| ellipsis | `char` 459, `ascii` 2 | **char** |
| dash | `em` 86, `en` 1 | **em** |
| nbsp | `total` 5, `before-punctuation` 3, `space-before-punctuation` 9 | _mixed_ |
| inverted marks | `open-question` 368, `open-exclamation` 81 | **open-question** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (420)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 70 |
| 2 | Wrong content (says something other than the English) | 169 |
| 3 | Degraded language (grammar, spelling, terminology) | 135 |
| 4 | Cosmetic (typography, spacing) | 40 |

### A. Functional, markup, variables & plurals

- `about-private-browsing-pin-promo-link-text` — `browser/browser/aboutPrivateBrowsing.ftl` — macOS variant says taskbar instead of Dock.
    - Current: `[macos] Fijar en la barra de tareas`
    - Source: `{$sel_1 ->} [macos] Keep in Dock [other] Pin to taskbar`
    - Suggest: `[macos] Mantener en el Dock`
    - en-US macOS variant is “Keep in Dock”; macOS has no taskbar, and the variant is now identical to the *[other] one.
- `xpinstall-disabled` — `browser/browser/addonNotifications.ftl` — Instruction points to a non-existent “Editar opciones…” control instead of the Enable button.
    - Current: `Haga click en Editar opciones… para habilitarla y vuelva a intentar.`
    - Source: `Software installation is currently disabled. Click Enable and try again.`
    - Suggest: `Haga clic en Habilitar y vuelva a intentarlo.`
    - en-US says “Click Enable and try again.” and the adjacent button is labelled «Habilitar»; the current text instructs the user to use a control that isn't there.
- `appmenu-homepage-controlled-changes` — `browser/browser/appMenuNotifications.ftl` — Access key `K` of `appmenu-homepage-controlled-changes` is not present in its label
    - Current: `K`
    - Source: `buttonaccesskey: K buttonlabel: Keep Changes label: Your homepage has changed. secondarybuttonaccesskey: M secondarybuttonlabel: Manage Homepage`
    - The label is “Mantener los cambios”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-new-tab-controlled-changes` — `browser/browser/appMenuNotifications.ftl` — Access key `K` of `appmenu-new-tab-controlled-changes` is not present in its label
    - Current: `K`
    - Source: `buttonaccesskey: K buttonlabel: Keep Changes label: Your new tab has changed. secondarybuttonaccesskey: M secondarybuttonlabel: Manage New Tabs`
    - The label is “Mantener los cambios”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
    - Current: `B`
    - Source: `accesskey: B aria-label: Bookmarks toolbarname: Bookmarks Toolbar`
    - The label is “Marcadores”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `picture-in-picture-enable-toggle` — `browser/browser/browser.ftl` — “Enable anyway” translated as «Habilitar lo mismo», which does not mean “anyway”.
    - Current: `Habilitar lo mismo`
    - Source: `label: Enable anyway`
    - Suggest: `Habilitar de todos modos`
    - «lo mismo» means “the same thing”; the button enables PiP despite the site's recommendation.
- `urlbar-web-rtc-share-speaker-notification-anchor` — `browser/browser/browser.ftl` — Speakers rendered as «micrófono», naming the wrong device.
    - Current: `Administrar el compartir micrófono con el sitio`
    - Source: `tooltiptext: Manage sharing other speakers with the site`
    - Suggest: `Administrar el compartir altavoces con el sitio`
    - en-US is “Manage sharing other speakers with the site”; the tooltip is for audio output, and it duplicates the microphone tooltip above it.
- `bookmark-overlay-location-2` — `browser/browser/editBookmarkOverlay.ftl` — “Location” (folder position) translated as «Dirección» (address), contradicting the developer comment.
    - Current: `Dirección`
    - Source: `accesskey: L value: Location`
    - Suggest: `Ubicación`
    - The comment states Location refers to the bookmark's position among bookmarks, not its URL; «Dirección» collides with the URL field right above.
- `migration-safari-password-import-step4` — `browser/browser/migrationWizard.ftl` — "the passwords file you saved" turned into "the passwords file to save".
    - Current: `elegir el archivo de contraseñas a guardar`
    - Source: `Use “Select file” below to choose the passwords file you saved`
    - Suggest: `elegir el archivo de contraseñas que guardó`
    - The step tells the user to pick the previously saved file; the localization inverts it into a file yet to be saved.
- `fxa-menu-message-sync-devices-secondary-text` — `browser/browser/newtab/asrouter.ftl` — “passwords” was rendered as “contrato” (contract) instead of “contraseñas”.
    - Current: `como marcadores y contrato`
    - Source: `Instantly get your info — like bookmarks and passwords — everywhere you use { -brand-short-name }.`
    - Suggest: `como marcadores y contraseñas`
    - en-US: “like bookmarks and passwords”. “contrato” is a different concept and makes the sentence nonsensical.
- `newtab-discovery-empty-section-topstories-header` — `browser/browser/newtab/newtab.ftl` — “You are caught up!” translated as “you are trapped”.
    - Current: `¡Estás atrapado!`
    - Source: `You are caught up!`
    - Suggest: `¡Estás al día!`
    - “caught up” means having read everything; “atrapado” means trapped/caught, reversing the intended positive meaning.
- `newtab-picture-widget-menu-button` — `browser/browser/newtab/newtab.ftl` — The .title and .aria-label of the same button say different things (singular vs plural).
    - Current: `.title = Opción de foto del día`
    - Source: `aria-label: Picture of the day options title: Picture of the day options`
    - Suggest: `.title = Opciones de foto del día`
    - Both attributes render “Picture of the day options” in en-US; the tooltip says “Opción” (one option) while the aria-label says “Opciones de fotos del día”.
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — “Rest assured, your browsing data never leaves…” became “data security never leave…”, with a subject/verb disagreement.
    - Current: `la seguridad de los datos de su navegación      nunca dejan su copia personal`
    - Source: `In addition to dishing up captivating stories, we also show you relevant, highly-vetted content from select sponsors. Rest assured, <strong>your browsing data never leaves your personal copy of { -brand-product-name }</…`
    - Suggest: `los datos de su navegación nunca dejan su copia personal`
    - en-US states the browsing data never leaves the user's copy of Firefox; “la seguridad de” is spurious and also breaks agreement with the plural verb “dejan”.
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — “matches” (football games) translated as search “coincidencias”.
    - Current: `Cargando más coincidencias…`
    - Source: `Loading more matches…`
    - Suggest: `Cargando más partidos…`
    - Developer comment: “Status shown when more matches are being fetched.” The rest of the sports widget consistently uses “partidos”.
- `newtab-widget-timer-label-play` — `browser/browser/newtab/newtab.ftl` — Timer “Play” control translated as “let's play” (a game).
    - Current: `A jugar`
    - Source: `label: Play`
    - Suggest: `Iniciar`
    - This is the play/pause control of the Pomodoro-style timer (paired with newtab-widget-timer-label-pause = Pausa), not a game.
- `mr2022-onboarding-existing-colorway-checkbox-label` — `browser/browser/newtab/onboarding.ftl` — “homepage” rendered as “entrada” (entrance).
    - Current: `una entrada colorida`
    - Source: `Make { -firefox-home-brand-name } your colorful homepage`
    - Suggest: `su página de inicio colorida`
    - en-US “Make { -firefox-home-brand-name } your colorful homepage”; the tree elsewhere translates homepage as “página de inicio” (see home-homepage-title in newtab.ftl).
- `origin-controls-state-temporary-access` — `browser/browser/originControls.ftl` — Temporary, single-visit access described as permanent and recurring.
    - Current: `Siempre podrá leer y cambiar los datos para cada visita`
    - Source: `Can read and change data for this visit`
    - Suggest: `Puede leer y cambiar datos en esta visita`
    - en-US is "Can read and change data for this visit"; adding "Siempre" and "cada visita" reverses the temporary nature of the grant and duplicates origin-controls-state-always-on.
- `security-view-identity-owner` — `browser/browser/pageInfo.ftl` — "Owner:" translated as "Autor:" (Author).
    - Current: `Autor:`
    - Source: `value: Owner:`
    - Suggest: `Propietario:`
    - The field shows the certificate/site owner, not an author; page-info-security-no-owner in the same file uses "propietario".
- `policy-DisableSetAsDesktopBackground` — `browser/browser/policies/policies-descriptions.ftl` — The menu command name “Set as Desktop Background” was translated as a past participle phrase.
    - Current: `el comando de menú configurado como Fondo de escritorio`
    - Source: `Disable the menu command Set as Desktop Background for images.`
    - Suggest: `el comando de menú Establecer como fondo de escritorio`
    - en-US refers to the menu command named “Set as Desktop Background”; “configurado como” turns it into “the menu command configured as…”, changing the meaning.
- `clear-site-data-cache-info` — `browser/browser/preferences/clearSiteData.ftl` — Meaning inverted: says sites will be needed, not that sites will have to reload data.
    - Current: `Se necesitarán sitios para recargar imágenes y datos`
    - Source: `Will require websites to reload images and data`
    - Suggest: `Los sitios web tendrán que volver a cargar imágenes y datos`
    - en-US: “Will require websites to reload images and data”. The subject/object are swapped, producing a nonsensical sentence.
- `colors-background` — `browser/browser/preferences/colors.ftl` — “Background” rendered as “Fondo de pantalla” (wallpaper).
    - Current: `Fondo de pantalla`
    - Source: `(value): Background accesskey: B`
    - Suggest: `Fondo`
    - Same defect as colors-text-background: this label is the website background colour, not the desktop wallpaper.
- `colors-page-override` — `browser/browser/preferences/colors.ftl` — “debajo” reverses the en-US reference to the selections above.
    - Current: `con las opciones que están debajo`
    - Source: `(value): Override the colors specified by the page with your selections above accesskey: O`
    - Suggest: `con las opciones seleccionadas más arriba`
    - en-US: “with your selections above”. The controls referenced are above this checkbox, so “debajo” points the user to the wrong place.
- `colors-text-background` — `browser/browser/preferences/colors.ftl` — “Background” (page background colour) rendered as “Fondo de pantalla” (wallpaper).
    - Current: `Fondo de pantalla`
    - Source: `accesskey: B label: Background`
    - Suggest: `Fondo`
    - In the Colors dialog “Background” is the page background colour paired with “Texto”; “fondo de pantalla” means wallpaper (see home-prefs-choose-wallpaper-link, “Elegir un fondo de pantalla”).
- `containers-icon-fence` — `browser/browser/preferences/containers.ftl` — Icon name “Fence” translated as the verb “Cercar”.
    - Current: `Cercar`
    - Source: `label: Fence`
    - Suggest: `Cerca`
    - All the other icon names in this list are nouns (Maletín, Regalo, Árbol); “Fence” here is the object, not the action.
- `autofill-country-warning-message` — `browser/browser/preferences/formAutofill.ftl` — “Form autofill” rendered as “the autofill form”.
    - Current: `El formulario de autocompletado`
    - Source: `Form autofill is currently available only for certain countries.`
    - Suggest: `El autocompletado de formularios`
    - en-US: “Form autofill is currently available only for certain countries.” The sibling string autofill-country-warning-message-2 already uses the correct “El autocompletado de formularios”.
- `permissions-site-camera-disable-desc` — `browser/browser/preferences/permissions.ftl` — “no listados debajo” reverses the en-US “not listed above”.
    - Current: `los sitios web no listados debajo`
    - Source: `This will prevent any websites not listed above from requesting permission to access your camera. Blocking access to your camera may break some website features.`
    - Suggest: `los sitios web no listados arriba`
    - en-US: “any websites not listed above”; the site list is above the checkbox, and sibling strings such as permissions-site-notification-disable-desc use “no incluidos en la lista”.
- `permissions-site-microphone-disable-desc` — `browser/browser/preferences/permissions.ftl` — “no listados debajo” reverses the en-US “not listed above”.
    - Current: `los sitios web no listados debajo`
    - Source: `This will prevent any websites not listed above from requesting permission to access your microphone. Blocking access to your microphone may break some website features.`
    - Suggest: `los sitios web no listados arriba`
    - Same inversion as the camera description; en-US reads “any websites not listed above”.
- `permissions-site-xr-disable-desc` — `browser/browser/preferences/permissions.ftl` — Virtual-reality permission description talks about location instead of VR devices.
    - Current: `soliciten permiso para acceder a tu ubicación. Bloquear el acceso a tu ubicación`
    - Source: `This will prevent any websites not listed above from requesting permission to access your virtual reality devices. Blocking access to your virtual reality devices may break some website features.`
    - Suggest: `soliciten permiso para acceder a tus dispositivos de realidad virtual. Bloquear el acceso a tus dispositivos de realidad virtual`
    - en-US: “…from requesting permission to access your virtual reality devices. Blocking access to your virtual reality devices…”. The string was copied from the Location pane and describes the wrong permission.
- `content-blocking-known-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Agreement makes “known” modify the fingerprints instead of the fingerprinters.
    - Current: `Detectores de huellas digitales conocidas`
    - Source: `accesskey: K label: Known fingerprinters`
    - Suggest: `Detectores de huellas digitales conocidos`
    - The developer comment states the known fingerprinters are the trackers that are known; content-blocking-known-and-suspected-fingerprinters in the same file correctly uses “conocidos y sospechosos”.
- `performance-limit-content-process-blocked-desc` — `browser/browser/preferences/preferences.ftl` — “content processes” rendered as “procesos contenidos” (contained processes).
    - Current: `el número de procesos contenidos`
    - Source: `Modifying the number of content processes is only possible with multiprocess { -brand-short-name }. <a data-l10n-name="learn-more">Learn how to check if multiprocess is enabled</a>`
    - Suggest: `el número de procesos de contenido`
    - The adjacent performance-limit-content-process-enabled-desc correctly uses “procesos de contenido”.
- `graph-private-window` — `browser/browser/protections.ftl` — "Private Windows" rendered as just "ventanas", dropping the key qualifier.
    - Current: `bloqueando rastreadores en ventanas , pero`
    - Source: `{ -brand-short-name } continues to  block trackers in Private Windows, but does not keep a record of what was blocked.`
    - Suggest: `bloqueando rastreadores en ventanas privadas, pero`
    - en-US says "in Private Windows"; the localized text drops "privadas" (and leaves a stray space), changing the meaning to all windows. privacy-metrics-private-window in the same file translates it correctly.
- `protections-panel-fingerprinters` — `browser/browser/protectionsPanel.ftl` — "this digital fingerprint" rendered as "this fingerprint detector".
    - Current: `Usando este detector de huella digital pueden seguirlo`
    - Source: `Fingerprinters collect settings from your browser and computer to create a profile of you. Using this digital fingerprint, they can track you across different websites.`
    - Suggest: `Usando esta huella digital pueden seguirlo`
    - The English refers to the fingerprint itself, not the detector; fingerprinter-tab-content in protections.ftl translates the same sentence as "Usando esta huella digital".
- `protections-milestone` — `browser/browser/siteProtections.ftl` — Plural variant is garbled: missing space and a stray literal "# 2" where the count belongs.
    - Current: `{ -brand-short-name }más de # 2 rastreadores bloqueados desde`
    - Source: `{$trackerCount ->} [one] { -brand-short-name } blocked { $trackerCount } tracker since { $date } [other] { -brand-short-name } blocked over { $trackerCount } trackers since { $date }`
    - Suggest: `{ -brand-short-name } bloqueó más de { $trackerCount } rastreadores desde`
    - en-US is "blocked over { $trackerCount } trackers since"; the localized text runs the brand into "más de" and shows a literal "# 2" instead of the number.
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
    - Current: `Introducimos <a data-l10n-name="terms-of-use">Términos de uso</a> y actualizamos nuestra <a data-l10n-name="privacy-notice">Nota de privacidad</a >.<br><br> Tómese un momento para revisar y aceptar. <a data-l10n-name="l…`
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Suggest: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Whitespace inside a closing tag makes it render as literal text.
- `permission.open-protocol-handler.label` — `browser/chrome/browser/sitePermissions.properties` — "Open applications" rendered as an adjective phrase, contrary to the developer comment
    - Current: `Aplicaciones abiertas`
    - Source: `Open applications`
    - Suggest: `Abrir aplicaciones`
    - The developer comment explicitly says "Open as a verb. 'This site may open applications'." "Aplicaciones abiertas" means "opened applications", so the permission label reads as a state instead of an action.
- `useCreditCardPasswordPrompt.linux` — `browser/extensions/formautofill/formautofill.properties` — "use stored credit card information" rendered as "show"
    - Current: `está intentando mostrar la información de la tarjeta de crédito.`
    - Source: `%S is trying to use stored credit card information.`
    - Suggest: `está intentando usar la información almacenada de la tarjeta de crédito.`
    - en-US is "is trying to use stored credit card information"; the Windows variant in the same file correctly says "usar la información almacenada".
- `WARN_WRITE_ACCESS` — `browser/installer/custom.properties` — Untranslated English fragment left appended to the translated sentence.
    - Current: `Haga clic en Aceptar para seleccionar un directorio diferente OK to select a different directory.`
    - Source: `You don’t have access to write to the installation directory.  Click OK to select a different directory.`
    - Suggest: `Haga clic en Aceptar para seleccionar un directorio diferente.`
    - The English source tail was left in the string, producing a duplicated bilingual sentence in the installer dialog.
- `FileError` — `browser/installer/override.properties` — English conjunction “or” left untranslated mid-sentence.
    - Current: `en Reintentar para tratar nuevamente or en`
    - Source: `Error opening file for writing:   $0  Click Abort to stop the installation, Retry to try again, or Ignore to skip this file.`
    - Suggest: `en Reintentar para tratar nuevamente o en`
    - Source “Retry to try again, or Ignore…”; “or” should be Spanish “o”. The parallel string FileError_NoIgnore correctly uses “o”.
- `document_properties_page_size_orientation_portrait` — `browser/pdfviewer/viewer.properties` — "portrait" translated as "normal"
    - Current: `document_properties_page_size_orientation_portrait = normal`
    - Source: `portrait`
    - Suggest: `vertical`
    - "normal" does not name a page orientation; paired with "apaisado" for landscape, the expected term is "vertical".
- `document_properties_page_size_unit_inches` — `browser/pdfviewer/viewer.properties` — Inches unit translated as the preposition "en"
    - Current: `document_properties_page_size_unit_inches = en`
    - Source: `in`
    - Suggest: `pulg.`
    - en-US "in" is the abbreviation for inches; "en" is the Spanish preposition and displays as e.g. "8,5 × 11 en (apaisado)", which is not a unit of measure.
- `document_properties_producer` — `browser/pdfviewer/viewer.properties` — English word order kept in "PDF Productor:"
    - Current: `document_properties_producer = PDF Productor:`
    - Source: `PDF Producer:`
    - Suggest: `Productor del PDF:`
    - en-US "PDF Producer:"; Spanish places the modifier after the noun, as the next line already does ("Versión de PDF:").
- `find_match_count[one]` — `browser/pdfviewer/viewer.properties` — Singular plural form uses the plural noun
    - Current: `find_match_count[one] = {{current}} de {{total}} coincidencias`
    - Source: `{{current}} of {{total}} match`
    - Suggest: `{{current}} de {{total}} coincidencia`
    - en-US [one] is "match" (singular); the singular category displays "1 de 1 coincidencias". find_match_count_limit[one] has the mirror-image defect ("Más de {{limit}} coinciden", a verb instead of a noun).
- `scroll_horizontal.title` — `browser/pdfviewer/viewer.properties` — Horizontal scrolling tooltip says "vertical"
    - Current: `scroll_horizontal.title = Usar desplazamiento vertical`
    - Source: `Use Horizontal Scrolling`
    - Suggest: `Usar desplazamiento horizontal`
    - en-US is "Use Horizontal Scrolling"; the label right below correctly says "Desplazamiento horizontal", so the tooltip duplicates the vertical-scrolling tooltip and names the wrong option.
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — “Profile performance” rendered as “Rendimiento del perfil”
    - Current: `Rendimiento del perfil`
    - Source: `Profile performance`
    - Suggest: `Perfilar rendimiento`
    - en-US “Profile performance” is a verb+object button label; the translation inverts it into “performance of the profile”, which does not describe the button’s action.
- `accessibility-best-practices` — `devtools/client/accessibility.ftl` — “Best Practices” translated as “Buenas costumbres” (good manners)
    - Current: `Buenas costumbres`
    - Source: `alt: Best Practices`
    - Suggest: `Buenas prácticas`
    - “Best Practices” is the accessibility-audit category; “costumbres” means customs/manners and is not the established term for practices.
- `accessibility.badge.contrast.tooltip` — `devtools/client/accessibility.properties` — Negation broken: “Con cumple” instead of “No cumple”, reversing the meaning
    - Current: `Con cumple los estándares de WCAG para texto accesible.`
    - Source: `Does not meet WCAG standards for accessible text.`
    - Suggest: `No cumple con los estándares WCAG para texto accesible.`
    - en-US: “Does not meet WCAG standards for accessible text.” The badge flags a failure; the current text reads as if the criterion were met.
- `accessibility.contrast.annotation.AAA` — `devtools/client/accessibility.properties` — AAA conformance message says WCAG AA instead of AAA, duplicating the AA string
    - Current: `Cumple con las normas WCAG AA para el texto accesible. %S`
    - Source: `Meets WCAG AAA standards for accessible text. %S`
    - Suggest: `Cumple con las normas WCAG AAA para el texto accesible. %S`
    - en-US is “Meets WCAG AAA standards for accessible text.”; as translated it is identical to accessibility.contrast.annotation.AA, so the user can no longer tell AA from AAA contrast.
- `scopes.block` — `devtools/client/debugger.properties` — “Block” (a code block) translated as the verb “Bloquear”
    - Current: `Bloquear`
    - Source: `Block`
    - Suggest: `Bloque`
    - The developer comment says it “refers to a block of code in the scopes pane”; “Bloquear” means “to block”, showing a verb where a scope name is expected.
- `unignoreAllOutsideDir.label` — `devtools/client/debugger.properties` — “Unignore files outside this directory” translated as “in this directory”
    - Current: `Dejar de ignorar archivos en este directorio`
    - Source: `Unignore files outside this directory`
    - Suggest: `Dejar de ignorar archivos fuera de este directorio`
    - en-US: “Unignore files outside this directory”. Identical to unignoreAllInDir.label, so the user cannot distinguish the two opposite menu entries.
- `unignoreAllOutsideGroup.label` — `devtools/client/debugger.properties` — “Unignore files outside this group” translated as “in this group”
    - Current: `Dejar de ignorar archivos en este grupo`
    - Source: `Unignore files outside this group`
    - Suggest: `Dejar de ignorar archivos fuera de este grupo`
    - en-US: “Unignore files outside this group”. As translated it is identical to unignoreAllInGroup.label, so two context-menu items with opposite effects read the same.
- `markupView.display.grid.tooltiptext2` — `devtools/client/inspector.properties` — Grid display tooltip describes the flexbox model and flexbox overlay
    - Current: `presenta su contenido de acuerdo con el modelo flexbox. Haga clic para alternar la superposición de flexbox para este elemento.`
    - Source: `This element behaves like a block element and lays out its content according to the grid model. Click to toggle the grid overlay for this element.`
    - Suggest: `presenta su contenido de acuerdo con el modelo de cuadrícula. Haga clic para alternar la superposición de cuadrícula para este elemento.`
    - en-US says “grid model … grid overlay”; hovering the display badge of a `display:grid` element states the wrong layout model and the wrong highlighter.
- `markupView.display.inlineFlex.tooltiptext2` — `devtools/client/inspector.properties` — inline-flex tooltip says the element behaves like a block element
    - Current: `Este elemento se comporta como un elemento de bloqueo y presenta su contenido`
    - Source: `This element behaves like an inline element and lays out its content according to the flexbox model. Click to toggle the flexbox overlay for this element.`
    - Suggest: `Este elemento se comporta como un elemento en línea y presenta su contenido`
    - en-US: “behaves like an inline element”; the translation duplicates the flex (block) string, so inline-flex and flex tooltips are indistinguishable. “de bloqueo” (blocking) is also the wrong rendering of “block”.
- `markupView.display.inlineGrid.tooltiptext2` — `devtools/client/inspector.properties` — inline-grid tooltip says block element and flexbox model
    - Current: `Este elemento se comporta como un elemento de bloqueo y presenta su contenido de acuerdo con el modelo flexbox. Haga clic para alternar la superposición de flexbox para este elemento.`
    - Source: `This element behaves like an inline element and lays out its content according to the grid model. Click to toggle the grid overlay for this element.`
    - Suggest: `Este elemento se comporta como un elemento en línea y presenta su contenido de acuerdo con el modelo de cuadrícula. Haga clic para alternar la superposición de cuadrícula para este elemento.`
    - en-US: “behaves like an inline element and lays out its content according to the grid model … grid overlay”. Both the display type and the layout model are wrong.
- `dominatortree.field.label` — `devtools/client/memory.properties` — Dominator tree column header translated as “Etiqueta” instead of “Dominador”
    - Current: `Etiqueta`
    - Source: `Dominator`
    - Suggest: `Dominador`
    - en-US value is “Dominator”; the translator rendered the key name (label) instead of the string, mislabelling the dominator column in the memory tool.
- `storage-table-type-localstorage-hint` — `devtools/client/storage.ftl` — Local storage hint talks about cookies
    - Current: `Ver y editar cookies seleccionando un host.`
    - Source: `View and edit the local storage by selecting a host. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `Ver y editar el almacenamiento local seleccionando un host.`
    - en-US: “View and edit the local storage by selecting a host.” The string was copied from the cookies hint, so the Local Storage panel describes the wrong storage type.
- `storage-table-type-sessionstorage-hint` — `devtools/client/storage.ftl` — Session storage hint talks about cookies
    - Current: `Ver y editar cookies seleccionando un host.`
    - Source: `View and edit the session storage by selecting a host. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `Ver y editar el almacenamiento de sesión seleccionando un host.`
    - en-US: “View and edit the session storage by selecting a host.” Copied from the cookies hint; the Session Storage panel names the wrong storage type.
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — Access key `G` of `styleeditor-visibility-toggle` is not present in its label
    - Current: `G`
    - Source: `accesskey: S tooltiptext: Toggle style sheet visibility`
    - The label is “Alternar visibilidad de la hoja de estilo”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix` — `devtools/client/tooltips.ftl` — Malformed closing tag `</strong >` in `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix`
    - Current: `Intente agregar <strong>position:absolute</strong> al elemento, o <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong > o <strong>display:inline-flex</strong> al padre del e…`
    - Source: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong>, or <strong>display:inline-flex</strong> to the element…`
    - Suggest: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong>, or <strong>display:inline-flex</strong> to the element…`
    - Whitespace inside a closing tag makes it render as literal text.
- `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix-1` — `devtools/client/tooltips.ftl` — Malformed closing tag `</strong >` in `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix-1`
    - Current: `Intente agregar <strong>position:absolute</strong> al elemento, o <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong > o <strong>display:inline-flex</strong> al padre del e…`
    - Source: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong>, or <strong>display:inline-flex</strong> to the element…`
    - Suggest: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong>, or <strong>display:inline-flex</strong> to the element…`
    - Whitespace inside a closing tag makes it render as literal text.
- `parentProcessBrowserConsole.title` — `devtools/client/webconsole.properties` — Browser Console window title says “Caja de herramientas” (Toolbox)
    - Current: `Caja de herramientas del navegador del proceso principal`
    - Source: `Parent process Browser Console`
    - Suggest: `Consola del navegador del proceso principal`
    - en-US: “Parent process Browser Console”. The window is the Browser Console, not the Browser Toolbox; multiProcessBrowserConsole.title in the same file correctly uses “Consola”.
- _…and 59 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `autofill-address-oblast` — `browser/browser/preferences/formAutofill.ftl` — “Oblast” replaced by “Provincia autónoma”, which names a different kind of entity.
    - Current: `Provincia autónoma`
    - Source: `Oblast`
    - Suggest: `Óblast`
    - The developer comment identifies this as the primary administrative division used in Russia and Ukraine; an óblast is not an autonomous province, and neighbouring entries (Do/Si, Eircode, Townland) keep the local term.
- `DrawWindowCanvasRenderingContext2DWarning` — `dom/chrome/dom/dom.properties` — The API name tabs.captureTab was translated to “pestañas.captureTab”.
    - Current: `Usar las pestañas.captureTab extensions API en lugar de`
    - Source: `Use of drawWindow method from CanvasRenderingContext2D is deprecated. Use tabs.captureTab extensions API instead https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/tabs/captureTab`
    - Suggest: `Use la API de extensiones tabs.captureTab en su lugar:`
    - Developer comment: “Do not translate CanvasRenderingContext2D, drawWindow and tabs.captureTab.”
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — The literal key/modifiers labels were translated despite the do-not-localize note.
    - Current: `clave="%S" modificadores="%S"id=“%S”`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - Suggest: `key=“%S” modifiers=“%S” id=“%S”`
    - Developer comment: “do not localize key=“%S” modifiers=“%S” id=“%S””. WinConflict2 has the same problem.
- `MathML_DeprecatedMathSizeValueWarning` — `dom/chrome/dom/dom.properties` — The mathsize keyword values small/normal/big were translated despite the do-not-translate note.
    - Current: `“Pequeño”, “normal” y “grande” son valores obsoletos`
    - Source: `“small”, “normal” and “big” are deprecated values for the mathsize attribute and will be removed at a future date.`
    - Suggest: `“small”, “normal” y “big” son valores obsoletos`
    - Developer comment: “Do not translate small, normal, big and mathsize.” The translated words do not match any real attribute value.
- `MathML_DeprecatedStyleAttributeWarning` — `dom/chrome/dom/dom.properties` — MathML attribute names were translated despite the do-not-translate note.
    - Current: `Los atributos MathML "fondo", "color", "familia de fuentes", "tamaño de fuente", "estilo de fuente" y "fontweight"`
    - Source: `MathML attributes “background”, “color”, “fontfamily”, “fontsize”, “fontstyle” and “fontweight” are deprecated and will be removed at a future date.`
    - Suggest: `Los atributos MathML “background”, “color”, “fontfamily”, “fontsize”, “fontstyle” y “fontweight”`
    - Developer comment: “Do not translate MathML, background, color, fontfamily, fontsize, fontstyle and fontweight.” Only fontweight was left intact.
- `PreloadIgnoredInvalidAttr` — `dom/chrome/dom/dom.properties` — HTML attribute names “as”, “type” and “media” translated as words.
    - Current: `valores desconocidos de "como" o "tipo", o al atributo "media" que no coincide`
    - Source: `Preload of %S was ignored due to unknown “as” or “type” values, or non-matching “media” attribute.`
    - Suggest: `valores desconocidos de “as” o “type”, o al atributo “media” que no coincide`
    - en-US quotes the literal attribute names (“as”, “type”, “media”); “como”/“tipo” are not attributes a developer can look for.
- `UseSendBeaconDuringUnloadAndPagehideWarning` — `dom/chrome/dom/dom.properties` — navigator.sendBeacon was translated to “navegador.sendBeacon”.
    - Current: `El uso del navegador.sendBeacon`
    - Source: `Use of navigator.sendBeacon instead of synchronous XMLHttpRequest during unload and pagehide improves user experience.`
    - Suggest: `El uso de navigator.sendBeacon`
    - Developer comment: “Do not translate navigator.sendBeacon, unload, pagehide, or XMLHttpRequest.”
- `errAlmostStandardsDoctypeVerbose` — `dom/chrome/layout/htmlparser.properties` — Stray space inserted inside the doctype literal.
    - Current: `“<! DOCTYPE html>”`
    - Source: `This page is in Almost Standards Mode. Page layout may be impacted. For Standards Mode use “<!DOCTYPE html>”.`
    - Suggest: `“<!DOCTYPE html>”`
    - The doctype is code; “<! DOCTYPE html>” is not valid and misleads authors who copy it. errQuirkyDoctypeVerbose has the same defect, while errAlmostStandardsDoctype/errQuirkyDoctype are correct.
- `CompositorAnimationWarningHasCurrentColor` — `dom/chrome/layout/layout_errors.properties` — CSS identifiers ‘background-color’ and ‘current-color’ were translated.
    - Current: `Las animaciones de "color de fondo" no se pueden ejecutar en el compositor con el punto de control de "color actual".`
    - Source: `Animations of ‘background-color’ cannot be run on the compositor with ‘current-color’ keyframe.`
    - Suggest: `Las animaciones de ‘background-color’ no se pueden ejecutar en el compositor con un keyframe ‘current-color’.`
    - en-US: “Animations of ‘background-color’ cannot be run on the compositor with ‘current-color’ keyframe.” The surrounding strings in this file keep ‘transform’ and ‘opacity’ untranslated per the file’s notes.
- `PrincipalWritingModePropagationWarning` — `dom/chrome/layout/layout_errors.properties` — CSS property names and :root marked do-not-translate were translated.
    - Current: `las propiedades CSS "modo de escritura", "dirección" y "orientación de texto"`
    - Source: `When rendering the <html> element, the used values of CSS properties “writing-mode”, “direction”, and “text-orientation” on the <html> element are taken from the computed values of the <body> element, not from the <html…`
    - Suggest: `las propiedades CSS “writing-mode”, “direction” y “text-orientation”`
    - Developer comment: “Do not translate <html>, <body>, CSS, "writing-mode", "direction", "text-orientation", :root, and "The Principal Writing Mode"”. The same string also renders :root as “la pseudoclase: raíz CSS”.
- `ignoringScriptSrcForStrictDynamic` — `dom/chrome/security/csp.properties` — The CSP keyword 'strict-dynamic' was translated despite the do-not-localize note.
    - Current: `'estricto-dinámico'`
    - Source: `Ignoring “%1$S” within %2$S: ‘strict-dynamic’ specified`
    - Suggest: `‘strict-dynamic’ especificado`
    - Developer comment: “'strict-dynamic' should not be localized”. The neighbouring string strictDynamicButNoHashOrNonce correctly keeps ‘strict-dynamic’.
- `about-glean-about-data-list-item-about-telemetry` — `toolkit/toolkit/about/aboutGlean.ftl` — Spurious space inside the about: URL, which must not be altered.
    - Current: `<a data-l10n-name="about-telemetry-link">about: telemetry</a>`
    - Source: `To browse the data being collected by legacy telemetry, please consult <a data-l10n-name="about-telemetry-link">about:telemetry</a>.`
    - Suggest: `<a data-l10n-name="about-telemetry-link">about:telemetry</a>`
    - “about:telemetry” is a browser URL and a do-not-translate identifier; with the inserted space it no longer names a valid page.
- `language-name-af` — `toolkit/toolkit/intl/languageNames.ftl` — Afrikaans rendered as "Africano" (African)
    - Current: `language-name-af = Africano`
    - Source: `Afrikaans`
    - Suggest: `language-name-af = Afrikáans`
    - "Africano" names the continent's inhabitants, not the language Afrikaans.
- `language-name-hi` — `toolkit/toolkit/intl/languageNames.ftl` — Hindi rendered as "Hindú" (a Hindu person)
    - Current: `language-name-hi = Hindú`
    - Source: `Hindi`
    - Suggest: `language-name-hi = Hindi`
    - "hindú" designates an adherent of Hinduism; the language is "hindi".
- `language-name-lo` — `toolkit/toolkit/intl/languageNames.ftl` — Lao language named with the country "Laos"
    - Current: `language-name-lo = Laos`
    - Source: `Lao`
    - Suggest: `language-name-lo = Lao`
    - en-US is "Lao" (the language); "Laos" is the country, already used as region-name-la.
- `language-name-ml` — `toolkit/toolkit/intl/languageNames.ftl` — Malayalam labelled "Malayo", duplicating Malay (ms)
    - Current: `language-name-ml = Malayo`
    - Source: `Malayalam`
    - Suggest: `language-name-ml = Malayalam`
    - en-US ml is Malayalam and ms is Malay; both are "Malayo" here, so Malayalam names the wrong language.
- `language-name-sg` — `toolkit/toolkit/intl/languageNames.ftl` — Sango misspelled as "Sangro"
    - Current: `language-name-sg = Sangro`
    - Source: `Sango`
    - Suggest: `language-name-sg = Sango`
    - en-US "Sango"; "Sangro" is not a language name.
- `language-name-su` — `toolkit/toolkit/intl/languageNames.ftl` — Sundanese rendered as "Sudanés" (Sudanese)
    - Current: `language-name-su = Sudanés`
    - Source: `Sundanese`
    - Suggest: `language-name-su = Sundanés`
    - en-US "Sundanese" is the language of Java; "sudanés" refers to Sudan.
- `region-name-ae` — `toolkit/toolkit/intl/regionNames.ftl` — English abbreviation "U.A.E." left untranslated
    - Current: `region-name-ae = U.A.E.`
    - Source: `United Arab Emirates`
    - Suggest: `region-name-ae = Emiratos Árabes Unidos`
    - en-US spells out "United Arab Emirates" and every other country in the file is given its Spanish name.
- `region-name-fo` — `toolkit/toolkit/intl/regionNames.ftl` — Faroe Islands left in English form
    - Current: `region-name-fo = Islas Faroe`
    - Source: `Faroe Islands`
    - Suggest: `region-name-fo = Islas Feroe`
    - The Spanish exonym is "Islas Feroe".
- `region-name-sb` — `toolkit/toolkit/intl/regionNames.ftl` — Solomon Islands half-untranslated
    - Current: `region-name-sb = Islas Solomon`
    - Source: `Solomon Islands`
    - Suggest: `region-name-sb = Islas Salomón`
    - The Spanish name is "Islas Salomón"; the locale translates every other island group in this file.
- `region-name-sz-2019` — `toolkit/toolkit/intl/regionNames.ftl` — Uses the pre-2018 name Swaziland instead of Eswatini
    - Current: `region-name-sz-2019 = Suazilandia`
    - Source: `Eswatini`
    - Suggest: `region-name-sz-2019 = Esuatini`
    - en-US is "Eswatini"; the -2019 key suffix exists precisely because the country was renamed, so the old name is now the wrong name.

### C. Grammar, agreement & spelling

- `migration-no-selected-data-label` — `browser/browser/migrationWizard.ftl` — Accented "sé" used instead of the reflexive pronoun "se".
    - Current: `No sé seleccionaron datos a importar`
    - Source: `No data selected for import`
    - Suggest: `No se seleccionaron datos a importar`
    - "sé" is the verb "saber"; the impersonal reflexive requires unaccented "se".
- `migration-wizard-progress-extensions-support-link` — `browser/browser/migrationWizard.ftl` — Interrogative "cómo" missing its accent.
    - Current: `Conocer como { -brand-product-name } hace coincidir`
    - Source: `Learn how { -brand-product-name } matches extensions`
    - Suggest: `Conocer cómo { -brand-product-name } hace coincidir`
    - Indirect interrogative "cómo" is written with an accent.
- `saved-passwords-yes` — `browser/browser/pageInfo.ftl` — "Si" missing its accent.
    - Current: `Si`
    - Source: `Yes`
    - Suggest: `Sí`
    - The affirmative adverb requires the accent; security-visits-number in the same file uses "Sí".
- `panic-button-thankyou-msg1` — `browser/browser/panelUI.ftl` — "es" written instead of the article "el".
    - Current: `Se limpió es historial reciente`
    - Source: `Your recent history is cleared.`
    - Suggest: `Se limpió el historial reciente`
    - "es historial" is ungrammatical; the definite article "el" is required.
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — Do-not-translate literal “127.0.0.1/8” was altered to “127.0.0.1”.
    - Current: `Las conexiones a localhost, 127.0.0.1 y ::1 nunca pasan por proxy.`
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
    - Suggest: `Las conexiones a localhost, 127.0.0.1/8 y ::1 nunca pasan por proxy.`
    - The developer comment says: Do not translate "localhost", "127.0.0.1/8" and "::1". The CIDR suffix /8 was dropped, changing the technical statement.
- `content-blocking-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — English term “Fingerprinters” left untranslated although the locale translates it everywhere else.
    - Current: `Fingerprinters`
    - Source: `accesskey: F label: Fingerprinters`
    - Suggest: `Detectores de huellas digitales`
    - The same en-US term is rendered “Detectores de huellas digitales” in content-blocking-fingerprinters and in the ETP custom labels in this file, so the English label is inconsistent in the same surface.
- `preonboarding-manage-and-read-header-v2` — `browser/browser/preonboarding.ftl` — Garbled duplicated word at the start of the string.
    - Current: `LeeLea los términos de uso`
    - Source: `Read Terms of Use and Privacy Notice. Manage additional settings.`
    - Suggest: `Lea los términos de uso`
    - "LeeLea" is a leftover from an edit (voseo "Leé"/tuteo "Lee" merged with "Lea"); it is not a word and appears as a visible header.
- `etp-card-content-description` — `browser/browser/protections.ftl` — Missing space joins two words.
    - Current: `automáticamenteque`
    - Source: `{ -brand-short-name } automatically stops companies from secretly following you around the web.`
    - Suggest: `automáticamente que`
    - Two separate words were run together.
- `protections-vpn-header-content` — `browser/browser/protections.ftl` — Garbled text replaces "hides your location".
    - Current: `ocultattlal ubicación`
    - Source: `Protect your entire device with { -mozilla-vpn-brand-name }. One tap encrypts all traffic and hides your location.`
    - Suggest: `oculta la ubicación`
    - "ocultattlal" is corrupted; the parallel string protections-vpn-header-content-subscribed uses "oculta la ubicación".
- `protections-panel-smartblock-desc-label` — `browser/browser/protectionsPanel.ftl` — Ungrammatical clause with a stray capitalized "Este" mid-sentence.
    - Current: `mientras se navegue Este sitio a menos que se lo permita`
    - Source: `{ -brand-short-name } blocks tracking content while you’re on this site unless you allow it.`
    - Suggest: `mientras navega en este sitio, a menos que lo permita`
    - en-US is "while you're on this site"; the localized clause lacks the preposition and capitalizes "Este" mid-sentence.
- `smartblock-placeholder-desc` — `browser/browser/protectionsPanel.ftl` — Verb form "esté" used instead of the demonstrative "este".
    - Current: `bloqueó que esté contenido lo rastree`
    - Source: `Your { -brand-short-name } settings blocked this content from tracking you across sites or being used for ads.`
    - Suggest: `bloqueó que este contenido lo rastree`
    - The demonstrative adjective is unaccented "este".
- `report-broken-site-panel-header` — `browser/browser/reportBrokenSite.ftl` — Typo "rotor" in the panel label.
    - Current: `Informar sitio rotor`
    - Source: `label: Report broken site title: Report broken site`
    - Suggest: `Informar sitio roto`
    - The .title attribute of the same message correctly reads "Informar sitio roto"; "rotor" is a typo.
- `auto-safe-mode-description` — `browser/browser/safeMode.ftl` — Demonstrative pronoun "esto" incorrectly accented.
    - Current: `Ésto pudo haber sido causado`
    - Source: `{ -brand-short-name } closed unexpectedly while starting. This might be caused by add-ons or other problems. You can try to resolve the problem by troubleshooting in Safe Mode.`
    - Suggest: `Esto pudo haber sido causado`
    - The neuter demonstrative "esto" never takes a written accent.
- `troubleshoot-mode-description` — `browser/browser/safeMode.ftl` — Gender agreement error in the participle.
    - Current: `Sus complementos y personalizaciones serán deshabilitadas temporalmente.`
    - Source: `Use this special mode of { -brand-short-name } to diagnose issues. Your extensions and customizations will be temporarily disabled.`
    - Suggest: `Sus complementos y personalizaciones serán deshabilitados temporalmente.`
    - A coordinated masculine + feminine subject takes the masculine plural participle "deshabilitados".
- `safeb-blocked-harmful-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — "pagina" missing its accent
    - Current: `bloqueó esta pagina porque podría`
    - Source: `{ -brand-short-name } blocked this page because it might try to install dangerous apps that steal or delete your information (for example, photos, passwords, messages and credit cards).`
    - Suggest: `bloqueó esta página porque podría`
    - "página" is esdrújula and always accented; the surrounding strings in the same file spell it correctly.
- `safeb-blocked-phishing-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — "información personas" instead of "información personal"
    - Current: `revelar información personas como contraseñas`
    - Source: `{ -brand-short-name } blocked this page because it may trick you into doing something dangerous like installing software or revealing personal information like passwords or credit cards.`
    - Suggest: `revelar información personal como contraseñas`
    - en-US says "revealing personal information"; "información personas" is ungrammatical and loses the meaning of the security warning.
- `safeb-blocked-unwanted-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Verb form "está" used for the demonstrative "esta"
    - Current: `bloqueó está página porque puede intentar`
    - Source: `{ -brand-short-name } blocked this page because it might try to trick you into installing programs that harm your browsing experience (for example, by changing your homepage or showing extra ads on sites you visit).`
    - Suggest: `bloqueó esta página porque puede intentar`
    - "está" is the verb "estar"; the demonstrative adjective is unaccented "esta". Same error in safeb-blocked-addon-page-short-desc.
- `screenshots-generic-error-details` — `browser/browser/screenshots.ftl` — Misspelling "intenar".
    - Current: `¿Quiere intenar de nuevo`
    - Source: `We’re not sure what just happened. Care to try again or take a shot of a different page?`
    - Suggest: `¿Quiere intentar de nuevo`
    - The verb is "intentar".
- `protections-milestone` — `browser/browser/siteProtections.ftl` — Singular variant uses the participle instead of the verb.
    - Current: `{ -brand-short-name } bloqueado { $trackerCount } rastreador desde`
    - Source: `{$trackerCount ->} [one] { -brand-short-name } blocked { $trackerCount } tracker since { $date } [other] { -brand-short-name } blocked over { $trackerCount } trackers since { $date }`
    - Suggest: `{ -brand-short-name } bloqueó { $trackerCount } rastreador desde`
    - "bloqueado" is a past participle; the sentence needs the preterite "bloqueó" as in graph-week-summary.
- `tab-context-bookmark-tab2` — `browser/browser/tabContextMenu.ftl` — Misspelling "marcdores".
    - Current: `Agregar a marcdores`
    - Source: `accesskey: B label: Bookmark`
    - Suggest: `Agregar a marcadores`
    - The correct spelling is "marcadores", used everywhere else in the same file.
- `tab-context-move-tab-to-group` — `browser/browser/tabbrowser.ftl` — Missing space in "ungrupo" in the plural variant.
    - Current: `Agregar pestañas a ungrupo`
    - Source: `accesskey: G label: {$tabCount ->} [1] Add Tab to Group [other] Add Tabs to Group`
    - Suggest: `Agregar pestañas a un grupo`
    - The article and noun were run together.
- `tabbrowser-confirm-open-multiple-tabs-message` — `browser/browser/tabbrowser.ftl` — Demonstrative pronoun "esto" incorrectly accented.
    - Current: `Ésto puede hacer que`
    - Source: `{$tabCount ->} [other] You are about to open { $tabCount } tabs. This might slow down { -brand-short-name } while the pages are loading. Are you sure you want to continue?`
    - Suggest: `Esto puede hacer que`
    - The neuter demonstrative "esto" never takes a written accent.
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — Duplicated noun in the plural variant.
    - Current: `Desenmudecer pestaña { $tabCount } pestañas ({ $shortcut })`
    - Source: `label: {$tabCount ->} [one] Unmute tab ({ $shortcut }) [other] Unmute { $tabCount } tabs ({ $shortcut })`
    - Suggest: `Desenmudecer { $tabCount } pestañas ({ $shortcut })`
    - "pestaña" is repeated before the count; the parallel mute tooltip has the correct form.
- `translations-panel-revisit-header` — `browser/browser/translations.ftl` — Verb form "Está" used instead of the demonstrative "Esta".
    - Current: `Está página está traducida`
    - Source: `This page is translated from { $fromLanguage } to { $toLanguage }`
    - Suggest: `Esta página está traducida`
    - The demonstrative adjective is unaccented "Esta"; "Está" is the verb, producing "Is page is translated".
- `unified-extensions-mb-blocklist-error-single` — `browser/browser/unifiedExtensions.ftl` — Verb form "Está" used instead of the demonstrative "Esta".
    - Current: `Está extensión viola las políticas de Mozilla y ha sido deshabilitada.`
    - Source: `heading: { $extensionName } disabled message: This extension violates Mozilla’s policies and has been disabled.`
    - Suggest: `Esta extensión viola las políticas de Mozilla y ha sido deshabilitada.`
    - The demonstrative adjective is unaccented "Esta".
- `unified-extensions-mb-blocklist-warning-single` — `browser/browser/unifiedExtensions.ftl` — Verb form "Está" used instead of the demonstrative "Esta".
    - Current: `Está extensión viola las políticas de Mozilla`
    - Source: `heading: { $extensionName } disabled message: This extension violates Mozilla’s policies and has been disabled. You can enable it in settings, but this may be risky.`
    - Suggest: `Esta extensión viola las políticas de Mozilla`
    - The demonstrative adjective is unaccented "Esta"; the -single2 variant correctly reads "Esta extensión".
- `webrtc-allow-share-camera-and-microphone-with-file` — `browser/browser/webrtcIndicator.ftl` — Verb form "esté" used instead of the demonstrative "este" (also in the other -with-file prompts).
    - Current: `¿Permitir que esté archivo local use la cámara y el micrófono?`
    - Source: `Allow this local file to use your camera and microphone?`
    - Suggest: `¿Permitir que este archivo local use la cámara y el micrófono?`
    - The demonstrative adjective is unaccented "este"; webrtc-allow-share-camera-with-file in the same section spells it correctly.
- `webrtc-indicator-menuitem-sharing-application-with-n-tabs` — `browser/browser/webrtcIndicator.ftl` — Misspelling "Compatiendo" in the singular variant.
    - Current: `Compatiendo una aplicación`
    - Source: `label: {$tabCount ->} [one] Sharing an Application with { $tabCount } tab [other] Sharing Applications with { $tabCount } tabs`
    - Suggest: `Compartiendo una aplicación`
    - The gerund is "Compartiendo", as in every sibling string.
- `webrtc-indicator-menuitem-sharing-camera-with-n-tabs` — `browser/browser/webrtcIndicator.ftl` — Spurious accent in "pestañás".
    - Current: `Compartiendo cámara con { $tabCount } pestañás`
    - Source: `label: {$tabCount ->} [one] Sharing Camera with { $tabCount } tab [other] Sharing Camera with { $tabCount } tabs`
    - Suggest: `Compartiendo cámara con { $tabCount } pestañas`
    - "pestañas" carries no accent; all parallel strings spell it correctly.
- `webrtc-sharing-screen` — `browser/browser/webrtcIndicator.ftl` — Voseo verb mixed with usted possessive in the same sentence.
    - Current: `Estás compartiendo toda su pantalla.`
    - Source: `You are sharing your entire screen.`
    - Suggest: `Está compartiendo toda su pantalla.`
    - "Estás" (vos/tú) clashes with "su"; the adjacent webrtc-sharing-window and webrtc-sharing-browser-window use "Está".
- `contentBlocking.cookies.blockingUnvisited2.label` — `browser/chrome/browser/browser.properties` — Number disagreement between "sitio" and "no visitados"
    - Current: `Cookies de sitio no visitados`
    - Source: `Unvisited Site Cookies`
    - Suggest: `Cookies de sitios no visitados`
    - The adjective is plural while the noun it modifies is singular; en-US is "Unvisited Site Cookies".
- `decoder.noCodecs.button` — `browser/chrome/browser/browser.properties` — Interrogative "cómo" written without accent
    - Current: `Aprender como`
    - Source: `Learn how`
    - Suggest: `Aprender cómo`
    - en-US "Learn how"; the indirect interrogative requires an accent.
- `keywordURIFixup.goTo` — `browser/chrome/browser/browser.properties` — Missing accent on affirmative "Sí"
    - Current: `Si, ir a %S`
    - Source: `Yes, take me to %S`
    - Suggest: `Sí, ir a %S`
    - en-US is "Yes, take me to %S"; unaccented "si" is the conditional conjunction "if".
- `privacy.spoof_english` — `browser/chrome/browser/browser.properties` — Language name capitalized as in English
    - Current: `Cambiar la configuración de idioma a Inglés`
    - Source: `Changing your language setting to English will make you more difficult to identify and enhance your privacy. Do you want to request English language versions of web pages?`
    - Suggest: `Cambiar la configuración de idioma a inglés`
    - Spanish writes language names in lowercase; "Inglés" is capitalized twice in this string.
- `processHang.nonspecific_tab.label` — `browser/chrome/browser/browser.properties` — Spurious reflexive "se" reverses who is slowing down whom
    - Current: `Una página web se está ralentizando %1$S.`
    - Source: `A web page is slowing down %1$S. To speed up your browser, stop that page.`
    - Suggest: `Una página web está ralentizando %1$S.`
    - en-US: "A web page is slowing down %1$S". With "se", the sentence reads as the page slowing itself; the parallel strings processHang.selected_tab.label and processHang.specific_tab.label correctly omit it.
- `webauthn.anonymize` — `browser/chrome/browser/browser.properties` — Incorrect accent in "Anónimizar"
    - Current: `Anónimizar de todas formas`
    - Source: `Anonymize anyway`
    - Suggest: `Anonimizar de todas formas`
    - The verb is "anonimizar"; only the adjective "anónimo" carries the accent.
- `webauthn.selectSignResultPrompt` — `browser/chrome/browser/browser.properties` — Interrogative "cuál" written without accent
    - Current: `Seleccione cual usar o cancelar.`
    - Source: `Multiple accounts found for %S. Select which to use or cancel.`
    - Suggest: `Seleccione cuál usar o cancelar.`
    - Indirect interrogative pronoun requires an accent ("Select which to use").
- `unblockTypeUncommon2` — `browser/chrome/browser/downloads/downloads.properties` — Missing accent in "comunmente"
    - Current: `Este archivo no es comunmente descargado`
    - Source: `This file is not commonly downloaded and may not be safe to open. It may contain a virus or make unexpected changes to your programs and settings.`
    - Suggest: `Este archivo no es comúnmente descargado`
    - The adverb formed from "común" keeps the accent: "comúnmente".
- `clearSiteDataPromptText` — `browser/chrome/browser/siteData.properties` — "Este" should be the neuter "Esto"
    - Current: `Este puede desconectarlo de sitios web`
    - Source: `Selecting ‘Clear Now’ will clear all cookies and site data stored by %S. This may sign you out of websites and remove offline web content.`
    - Suggest: `Esto puede desconectarlo de sitios web`
    - en-US "This may sign you out of websites" refers to the whole preceding action, which requires the neuter demonstrative "Esto"; "Este" would have to agree with a masculine noun.
- `permission.midi.label` — `browser/chrome/browser/sitePermissions.properties` — Missing preposition "a" after "Acceder"
    - Current: `Acceder dispositivos MIDI`
    - Source: `Access MIDI devices`
    - Suggest: `Acceder a dispositivos MIDI`
    - "Acceder" governs "a"; the neighbouring permission.serial.label correctly reads "Acceder a puertos serie". Same defect in permission.midi-sysex.label.
- `clientSocketMisconfiguration` — `browser/chrome/overrides/appstrings.properties` — Interrogative "cómo" written without accent
    - Current: `Firefox no sabe como comunicarse con el servidor.`
    - Source: `Firefox doesn’t know how to communicate with the server.`
    - Suggest: `Firefox no sabe cómo comunicarse con el servidor.`
    - Indirect interrogative "cómo" requires the accent; the identical text in unknownSocketType has the same defect.
- `cspBlocked` — `browser/chrome/overrides/appstrings.properties` — Missing conjunction "que" after "evita"
    - Current: `una política de seguridad de contenido que evita sea cargada de esta forma`
    - Source: `This page has a content security policy that prevents it from being loaded in this way.`
    - Suggest: `una política de seguridad de contenido que evita que se cargue de esta forma`
    - "evitar" requires "que" before the subordinate clause; the parallel string xfoBlocked correctly writes "evita que se cargue".
- `externalProtocolPrompt` — `browser/chrome/overrides/appstrings.properties` — Misspelling "Apliación" and missing accent in "este seguro"
    - Current: `Apliación: %3$S`
    - Source: `An external application must be launched to handle %1$S: links.   Requested link:  %2$S  Application: %3$S   If you were not expecting this request it may be an attempt to exploit a weakness in that other program. Cance…`
    - Suggest: `Aplicación: %3$S`
    - "Apliación" is a typo for "Aplicación"; the same string also has "a menos que este seguro", which needs the subjunctive "esté".
- `unknownProtocolFound` — `browser/chrome/overrides/appstrings.properties` — Interrogative "cómo" written without accent
    - Current: `Firefox no sabe como abrir esta dirección`
    - Source: `Firefox doesn’t know how to open this address, because one of the following protocols (%S) isn’t associated with any program or is not allowed in this context.`
    - Suggest: `Firefox no sabe cómo abrir esta dirección`
    - Indirect interrogative "cómo" is always accented. Same error in clientSocketMisconfiguration and unknownSocketType ("no sabe como comunicarse").
- `autofillReauthCheckboxLin` — `browser/extensions/formautofill/formautofill.properties` — Indicative "Requiere" instead of the infinitive used by the parallel checkboxes
    - Current: `Requiere autenticación de Linux para autocompletar`
    - Source: `Require Linux authentication to autofill, view, or edit stored credit cards.`
    - Suggest: `Requerir autenticación de Linux para autocompletar`
    - en-US "Require Linux authentication…"; the Mac and Windows variants of the same checkbox both use "Requerir", so this one reads as a statement of fact instead of a setting.
- `unsupported_feature_forms` — `browser/pdfviewer/chrome.properties` — Misspelling "cotiene"
    - Current: `cotiene`
    - Source: `This PDF document contains forms. The filling of form fields is not supported.`
    - Suggest: `contiene`
    - Missing letter; "cotiene" is not a Spanish word.
- `document_properties_file_size` — `browser/pdfviewer/viewer.properties` — Misspelling "archovo"
    - Current: `Tamaño de archovo:`
    - Source: `File size:`
    - Suggest: `Tamaño de archivo:`
    - Typo for "archivo"; the line above correctly uses "Nombre de archivo:".
- `find_reached_bottom` — `browser/pdfviewer/viewer.properties` — "alcanzando" should be "alcanzado"
    - Current: `Fin de documento alcanzando, continuando desde arriba`
    - Source: `Reached end of document, continued from top`
    - Suggest: `Fin de documento alcanzado, continuando desde arriba`
    - Gerund used where the past participle is required; find_reached_top correctly uses "alcanzado".
- `invalid_file_error` — `browser/pdfviewer/viewer.properties` — Misspelling "cocrrupto"
    - Current: `cocrrupto`
    - Source: `Invalid or corrupted PDF file.`
    - Suggest: `corrupto`
    - Typo for "corrupto".
- `networkMenu.summary.tooltip.domContentLoaded` — `devtools/client/netmonitor.properties` — DOM event name corrupted to “DOMContentLoad”
    - Current: `Momento en el que ocurrió el evento “DOMContentLoad”`
    - Source: `Time when “DOMContentLoad” event occurred`
    - Suggest: `Momento en el que ocurrió el evento “DOMContentLoaded”`
    - DOMContentLoaded is a Web platform event name and must not be altered; netmonitor.ftl keeps it correct.
- `perftools-intro-description` — `devtools/client/perftools.ftl` — Profiler URL misspelled as perfiler.firefox.com
    - Current: `Las grabaciones inician el perfiler.firefox.com en una nueva pestaña.`
    - Source: `Recordings launch profiler.firefox.com in a new tab. All data is stored locally, but you can choose to upload it for sharing.`
    - Suggest: `Las grabaciones inician profiler.firefox.com en una nueva pestaña.`
    - profiler.firefox.com is a domain name and must not be altered; the string points users to a non-existent host (perftools-description-intro in the same file has it right).
- `clientSocketMisconfiguration` — `dom/chrome/appstrings.properties` — Missing accent on the interrogative “cómo”.
    - Current: `no sabe como comunicarse con el servidor`
    - Source: `The client is misconfigured and doesn’t know how to communicate with the server.`
    - Suggest: `no sabe cómo comunicarse con el servidor`
    - Indirect interrogative requires the accented form.
- `unsafeContentType` — `dom/chrome/appstrings.properties` — Untranslated English fragment left inside the sentence.
    - Current: `Contacte a los dueños del sitio web  contact the website owners para informarles`
    - Source: `The page you are trying to view cannot be shown because it is contained in a file type that may not be safe to open. Please contact the website owners to inform them of this problem.`
    - Suggest: `Contacte a los dueños del sitio web para informarles`
    - The English source phrase was pasted into the middle of the Spanish sentence, producing visibly broken user-facing text.
- `weakCryptoUsed` — `dom/chrome/appstrings.properties` — Sentence starts with “EL” instead of “El”.
    - Current: `EL dueño de %S`
    - Source: `The owner of %S has configured their website improperly. To protect your information from being stolen, the connection to this website has not been established.`
    - Suggest: `El dueño de %S`
    - Spelling/capitalization error in a user-facing error page.
- `DocumentWriteIgnored` — `dom/chrome/dom/dom.properties` — Typo “ingorada”.
    - Current: `fue ingorada`
    - Source: `A call to document.write() from an asynchronously-loaded external script was ignored.`
    - Suggest: `fue ignorada`
    - Misspelling of “ignorada”. The same typo appears in IgnoringWillChangeOverBudgetWarning (“ingoradas”).
- `FormValidationDateTimeRangeUnderflow` — `dom/chrome/dom/dom.properties` — Typo “Seleccone”.
    - Current: `Seleccone un valor que no sea anterior a %S.`
    - Source: `Please select a value that is no earlier than %S.`
    - Suggest: `Seleccione un valor que no sea anterior a %S.`
    - Misspelling of “Seleccione” in a form-validation bubble shown to end users.
- `FullscreenDeniedContainerNotAllowed` — `dom/chrome/dom/dom.properties` — Untranslated English word “attribute” left at the end.
    - Current: `no tiene un atributo "allowfullscreen" attribute.`
    - Source: `Request for fullscreen was denied because at least one of the document’s containing elements is not an iframe or does not have an “allowfullscreen” attribute.`
    - Suggest: `no tiene un atributo “allowfullscreen”.`
    - Leftover from the English source; the noun is duplicated.
- `ImportMapNotAllowedMultiple` — `dom/chrome/dom/dom.properties` — Wrong accent: “sé” instead of the pronoun “se”.
    - Current: `No sé permite la importación múltiple de mapas.`
    - Source: `Multiple import maps are not allowed.`
    - Suggest: `No se permiten varios mapas de importación.`
    - “sé” is the verb form; the impersonal pronoun “se” is required.
- `JSONCharsetWarning` — `dom/chrome/dom/dom.properties` — Typo “recueprada”.
    - Current: `para JSON recueprada usando XMLHttpRequest`
    - Source: `An attempt was made to declare a non-UTF-8 encoding for JSON retrieved using XMLHttpRequest. Only UTF-8 is supported for decoding JSON.`
    - Suggest: `para JSON recuperada usando XMLHttpRequest`
    - Misspelling of “recuperada”.
- `KillScriptWithDebugMessage` — `dom/chrome/dom/dom.properties` — Typo “el el debugger”.
    - Current: `abrir el script el el debugger`
    - Source: `A script on this page may be busy, or it may have stopped responding. You can stop the script now, open the script in the debugger, or let the script continue.`
    - Suggest: `abrir el script en el depurador`
    - Duplicated article instead of the preposition “en”; appears in a user-facing dialog.
- _…and 28 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `about-logins-breach-alert-date` — `browser/browser/aboutLogins.ftl` — «Está filtración» — verb form used instead of the demonstrative «Esta».
    - Current: `Está filtración se produjo el`
    - Source: `This breach occurred on { $date }`
    - Suggest: `Esta filtración se produjo el`
    - Demonstrative adjective «esta» carries no accent.
- `about-logins-confirm-remove-all-dialog-message2` — `browser/browser/aboutLogins.ftl` — «No sé puede» — misplaced accent turns the verb into the first person of «saber».
    - Current: `No sé puede deshacer esta acción.`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach alert…`
    - Suggest: `No se puede deshacer esta acción.`
    - Reflexive «se» must be unaccented; the accented «sé» is the verb «saber». Occurs in all three plural variants of this message.
- `pocket-panel-saved-error-only-links` — `browser/browser/aboutPocket.ftl` — Ungrammatical passive: «pueden guardarle enlaces».
    - Current: `Solamente pueden guardarle enlaces`
    - Source: `Only links can be saved`
    - Suggest: `Solamente se pueden guardar enlaces`
    - en-US: “Only links can be saved.” The current wording says something else and is not grammatical.
- `pocket-panel-signup-signup-cta` — `browser/browser/aboutPocket.ftl` — «En grátis» — wrong verb and a spurious accent on «gratis».
    - Current: `Registrarse en { -pocket-brand-name }. En grátis.`
    - Source: `Sign up for { -pocket-brand-name }. It’s free.`
    - Suggest: `Registrarse en { -pocket-brand-name }. Es gratis.`
    - en-US: “It’s free.” «gratis» is a llana word ending in -s and carries no accent; «En» should be «Es».
- `restore-page-show-tabs` — `browser/browser/aboutSessionRestore.ftl` — Number agreement: «pestaña anteriores».
    - Current: `Mostrar pestaña anteriores`
    - Source: `View Previous Tabs`
    - Suggest: `Mostrar pestañas anteriores`
    - Adjective is plural, noun is singular; the companion string uses «Ocultar pestañas anteriores».
- `crashed-include-URL-2` — `browser/browser/aboutTabCrashed.ftl` — Number agreement: «la URLs».
    - Current: `Incluir la URLs de los sitios`
    - Source: `Include the URLs of the sites you were on when { -brand-short-name } crashed`
    - Suggest: `Incluir las URLs de los sitios`
    - Plural noun requires plural article.
- `addon-install-error-corrupt-file` — `browser/browser/addonNotifications.ftl` — Typo «descargdo».
    - Current: `El complemento descargdo de este sitio`
    - Source: `The add-on downloaded from this site could not be installed because it appears to be corrupt.`
    - Suggest: `El complemento descargado de este sitio`
    - Missing letter in «descargado».
- `ai-window-open-sidebar` — `browser/browser/aiFeatures.ftl` — Typo «Se pude cerrar».
    - Current: `Se pude cerrar en cualquier momento.`
    - Source: `description: Show the assistant sidebar on each new tab. Close it anytime. label: Open assistant automatically`
    - Suggest: `Se puede cerrar en cualquier momento.`
    - Letter transposition in «puede».
- `appmenu-homepage-controlled-changes` — `browser/browser/appMenuNotifications.ftl` — Typo «incio» for «inicio».
    - Current: `Administrar la página de incio`
    - Source: `buttonaccesskey: K buttonlabel: Keep Changes label: Your homepage has changed. secondarybuttonaccesskey: M secondarybuttonlabel: Manage Homepage`
    - Suggest: `Administrar la página de inicio`
    - Missing letter.
- `appmenu-remote-tabs-tabsnotsyncing` — `browser/browser/appmenu.ftl` — Misspelling «pestañás» with a spurious accent.
    - Current: `una lista de pestañás de los otros dispositivos`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `una lista de pestañas de los otros dispositivos`
    - «pestañas» carries no written accent.
- `appmenuitem-vpn-description3` — `browser/browser/appmenu.ftl` — Two words run together: «quetla».
    - Current: `Hace quetla navegación sea más difícil de rastrear`
    - Source: `Make your browsing harder to trace`
    - Suggest: `Hace que la navegación sea más difícil de rastrear`
    - Missing space plus stray letter.
- `appmenuitem-vpn-description5` — `browser/browser/appmenu.ftl` — Gender agreement: «todas los dispositivos».
    - Current: `Obtener protección adicional en todas los dispositivos`
    - Source: `Get extra protection across devices`
    - Suggest: `Obtener protección adicional en todos los dispositivos`
    - «dispositivos» is masculine.
- `browser-tab-audio-blocked` — `browser/browser/browser.ftl` — Diaeresis characters used instead of accents.
    - Current: `REPRODUCCIÖN AUTOMÄTICA BLOQUEADA`
    - Source: `AUTOPLAY BLOCKED`
    - Suggest: `REPRODUCCIÓN AUTOMÁTICA BLOQUEADA`
    - «Ö» and «Ä» are not Spanish letters; the intended characters are Ó and Á.
- `data-reporting-notification-button` — `browser/browser/browser.ftl` — Missing accent on interrogative/relative «qué».
    - Current: `Seleccionar que compartir`
    - Source: `accesskey: C label: Choose What I Share`
    - Suggest: `Seleccionar qué compartir`
    - en-US “Choose What I Share”; the indirect interrogative requires the accent.
- `identity-description-insecure-login-forms` — `browser/browser/browser.ftl` — Missing conjunction leaves two clauses spliced together.
    - Current: `no es segura puede estar comprometida`
    - Source: `The login information you enter on this page is not secure and could be compromised.`
    - Suggest: `no es segura y puede estar comprometida`
    - en-US: “…is not secure and could be compromised.” The sentence is ungrammatical as written.
- `restore-session-startup-suggestion-button` — `browser/browser/browser.ftl` — “Show me how” rendered with unaccented «como», changing the meaning.
    - Current: `Mostrarme como`
    - Source: `Show me how`
    - Suggest: `Mostrarme cómo`
    - Interrogative «cómo» requires the accent; without it the label reads “show me as/like”.
- `toolbar-button-share-tab` — `browser/browser/browser.ftl` — «está página» — verb form instead of demonstrative «esta».
    - Current: `Compartir está página`
    - Source: `label: Share tooltiptext: Share this page`
    - Suggest: `Compartir esta página`
    - Demonstrative adjective carries no accent.
- `trustpanel-clear-cookies-description` — `browser/browser/browser.ftl` — Stray «para» leaves the sentence ungrammatical.
    - Current: `Eliminar cookies y datos del sitio para puede cerrar sesión`
    - Source: `Removing cookies and site data might log you out of websites and clear shopping carts.`
    - Suggest: `Eliminar cookies y datos del sitio puede cerrar sesión`
    - en-US: “Removing cookies and site data might log you out of websites…”; the dangling preposition breaks the clause.
- `urlbar-tabtosearch-onboard` — `browser/browser/browser.ftl` — Typo «tecaldo» for «teclado».
    - Current: `atajo de tecaldo`
    - Source: `Select this shortcut to find what you need faster.`
    - Suggest: `atajo de teclado`
    - Letter transposition.
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — «No sé puede» — misplaced accent (same defect as in aboutLogins).
    - Current: `No sé puede deshacer esta acción.`
    - Source: `{$total ->} [1] This will remove your password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach aler…`
    - Suggest: `No se puede deshacer esta acción.`
    - Reflexive «se» must be unaccented. Present in all three variants of this message.
- `contextual-manager-passwords-vulnerable-password-heading-and-message` — `browser/browser/contextual-manager.ftl` — «Está contraseña» — verb form instead of demonstrative «Esta».
    - Current: `Está contraseña es fácil de adivinar.`
    - Source: `heading: Password change recommended message: This password is easily guessable. Change your password to protect your account.`
    - Suggest: `Esta contraseña es fácil de adivinar.`
    - Demonstrative adjective carries no accent.
- `customkeys-description` — `browser/browser/customkeys.ftl` — Duplicated word fragment at the start of the string.
    - Current: `ControlaControlar cómo se mueve`
    - Source: `Control how you move around and interact with { -brand-short-name }.`
    - Suggest: `Controlar cómo se mueve`
    - Editing artifact; «ControlaControlar» is not a word.
- `bookmarks-toolbar-callout-2a-title` — `browser/browser/featureCallout.ftl` — Spurious accent on «Agregár».
    - Current: `Agregár más marcadores fácilmente`
    - Source: `Easily add more bookmarks`
    - Suggest: `Agregar más marcadores fácilmente`
    - The infinitive «agregar» takes no written accent.
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — Missing accent on «arrástrela».
    - Current: `arrastrela al comienzo de la barra de pestañas`
    - Source: `To pin any tab, drag it to the start of the tab strip. Or right-click and choose Pin Tab.`
    - Suggest: `arrástrela al comienzo de la barra de pestañas`
    - Esdrújula formed by the enclitic pronoun requires a written accent.
- `taskbar-tabs-value-prop-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — Number agreement: «cualquier sitios».
    - Current: `Abra cualquier sitios como una aplicación`
    - Source: `Launch any site like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `Abra cualquier sitio como una aplicación`
    - «cualquier» requires a singular noun; en-US is “Launch any site”.
- `firefoxview-dont-remember-history-empty-header-2` — `browser/browser/firefoxView.ftl` — Missing accent on «qué» in an indirect question.
    - Current: `Tiene el control sobre que recuerda { -brand-short-name }`
    - Source: `You’re in control of what { -brand-short-name } remembers`
    - Suggest: `Tiene el control sobre qué recuerda { -brand-short-name }`
    - en-US “what { -brand-short-name } remembers”; indirect interrogative needs the accent.
- `firefoxview-syncedtabs-adddevice-description-3` — `browser/browser/firefoxView.ftl` — Typo «ycempiece» (missing space, stray letter).
    - Current: `para dispositivos móviles ycempiece a sincronizar`
    - Source: `Scan the QR code to get { -brand-product-name } for mobile and start syncing your open tabs and more. Learn how to <a data-l10n-name="url">connect additional devices</a>.`
    - Suggest: `para dispositivos móviles y empiece a sincronizar`
    - Word run-on with an inserted character.
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — Wrong accent on «mí» and two words run together in «seguircon».
    - Current: `Espera mí respuesta antes de seguircon la próxima pregunta.`
    - Source: `label: Quiz me value: Please quiz me on this selection. Ask me a variety of types of questions, for example multiple choice, true or false, and short answer. Wait for my response before moving on to the next question.`
    - Suggest: `Espera mi respuesta antes de seguir con la próxima pregunta.`
    - Possessive «mi» is unaccented; «seguir con» needs a space.
- `link-preview-optin-message` — `browser/browser/genai.ftl` — «comiendo» (eating) instead of «comienzo» (beginning).
    - Current: `leer el comiendo de la página`
    - Source: `{ -brand-short-name } uses AI to read the beginning of the page and generate a few key points. To prioritize your privacy, this happens on your device.`
    - Suggest: `leer el comienzo de la página`
    - en-US: “read the beginning of the page”; the typo yields a different word.
- `ipprotection-come-back-title` — `browser/browser/ipProtection.ftl` — Typo «VPNinctegrada».
    - Current: `Vuelva para probar la VPNinctegrada`
    - Source: `Come back to try built-in VPN`
    - Suggest: `Vuelva para probar la VPN integrada`
    - Missing space and extra letters garble the product term.
- `ipprotection-locations-unavailable-label-1` — `browser/browser/ipProtection.ftl` — «deshabitado» (uninhabited) instead of «deshabilitado» (disabled).
    - Current: `No disponible, deshabitado`
    - Source: `(value): Unavailable aria-label: Unavailable, disabled`
    - Suggest: `No disponible, deshabilitado`
    - en-US aria-label is “Unavailable, disabled”; the typo produces a different real word.
- `unauthenticated-private-location-message` — `browser/browser/ipProtection.ftl` — Duplicated preposition «a a».
    - Current: `Ayuda a <a data-l10n-name="learn-more-vpn">a mantener privada la ubicación</a>`
    - Source: `Helps <a data-l10n-name="learn-more-vpn">keep your location private</a> in { -brand-product-name }.`
    - Suggest: `Ayuda a <a data-l10n-name="learn-more-vpn">mantener privada la ubicación</a>`
    - The preposition appears both before and inside the link.
- `annotations-default-pdf-handler-body` — `browser/browser/newtab/asrouter.ftl` — Missing accent on the enclitic verb form “colóquela”.
    - Current: `luego coloquela exactamente donde quiera`
    - Source: `Draw, type, or upload your signature, then place it exactly where you want. Save your go-to signatures for next time.`
    - Suggest: `luego colóquela exactamente donde quiera`
    - Verb plus enclitic pronoun becomes esdrújula and must carry the accent.
- `firefoxview-spotlight-promo-primarybutton` — `browser/browser/newtab/asrouter.ftl` — Interrogative “cómo” written without accent.
    - Current: `Vea como funciona`
    - Source: `See how it works`
    - Suggest: `Vea cómo funciona`
    - “See how it works” requires the accented interrogative “cómo”.
- `mr2022-background-update-toast-title` — `browser/browser/newtab/asrouter.ftl` — Missing accent on “Más”.
    - Current: `Mas privado.`
    - Source: `New { -brand-short-name }. More private. Fewer trackers. No compromises.`
    - Suggest: `Más privado.`
    - “Mas” without accent is the archaic conjunction “but”; the comparative requires “Más”.
- `welcome-back-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — Person shifts mid-sentence between “tú” and “usted”.
    - Current: `proteger tus datos donde quiera que vaya`
    - Source: `Welcome back to the only major browser backed by a non-profit. We take extra steps to protect your data wherever you roam.`
    - Suggest: `proteger sus datos donde quiera que vaya`
    - “tus” (tú) and “vaya” (usted) refer to the same addressee in one sentence; the surrounding strings in this file use usted.
- `newtab-toast-thumbs-up-or-down2` — `browser/browser/newtab/newtab.ftl` — Missing period after “Gracias”, running two sentences together.
    - Current: `Gracias Su opinión nos ayudará`
    - Source: `message: Thanks. Your feedback will help us improve your feed.`
    - Suggest: `Gracias. Su opinión nos ayudará`
    - en-US “Thanks. Your feedback will help us improve your feed.” has two sentences.
- `newtab-wallpaper-celestial-river` — `browser/browser/newtab/newtab.ftl` — Two missing accents: “satelite” and “rio”.
    - Current: `Imagen de satelite de un rio`
    - Source: `Satellite image of river`
    - Suggest: `Imagen de satélite de un río`
    - Both words require written accents (“satélite”, “río”).
- `newtab-wallpaper-reset` — `browser/browser/newtab/newtab.ftl` — Spelling error: “Reniciar”.
    - Current: `Reniciar como predeterminado`
    - Source: `Reset to default`
    - Suggest: `Restablecer los valores predeterminados`
    - “Reniciar” is not a Spanish word (typo for “Reiniciar”); en-US is “Reset to default”.
- `newtab-widget-section-feedback` — `browser/browser/newtab/newtab.ftl` — Interrogative “qué” written without accent.
    - Current: `Díganos que piensa`
    - Source: `Tell us what you think`
    - Suggest: `Díganos qué piensa`
    - “Tell us what you think” requires the accented interrogative “qué”.
- `mr2022-onboarding-gratitude-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — Interrogative “qué” written without accent.
    - Current: `Veamos que hay de nuevo`
    - Source: `See what’s new`
    - Suggest: `Veamos qué hay de nuevo`
    - “See what's new” requires the accented interrogative “qué”.
- `onboarding-gratitude-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — Duplicated word “más más”.
    - Current: `que Internet sea más más segura`
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `que Internet sea más segura`
    - “más” is repeated; en-US reads “safer and more accessible”.
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — Duplicated word “más más”.
    - Current: `que Internet sea más más segura`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `que Internet sea más segura`
    - Same duplication as in onboarding-gratitude-security-and-privacy-subtitle.
- `onboarding-sign-up-description` — `browser/browser/newtab/onboarding.ftl` — Number agreement error: singular verb with plural adjective.
    - Current: `se guardará de forma segura y estará disponibles`
    - Source: `Sign up for an account and all of your important info — passwords, bookmarks, and more — will be securely stored and available when you sign in to any device.`
    - Suggest: `se guardará de forma segura y estará disponible`
    - The subject “toda la información importante” is singular, so “disponibles” must agree in the singular (or the whole clause be pluralized).
- `appearance-browser-icon-requirement` — `browser/browser/preferences/browserIcon.ftl` — Garbled words: “ydesbloqueae” (missing space, misspelled verb).
    - Current: `Complete ydesbloqueae íconos de zorros adicionales`
    - Source: `message: Complete and unlock bonus fox icons to personalize { -brand-short-name }.`
    - Suggest: `Complete y desbloquee íconos de zorros adicionales`
    - “y” and “desbloquee” are run together and the verb is misspelled; en-US is “Complete and unlock bonus fox icons”.
- `colors-page-override` — `browser/browser/preferences/colors.ftl` — Misspelling “Sobreescribir”.
    - Current: `Sobreescribir`
    - Source: `(value): Override the colors specified by the page with your selections above accesskey: O`
    - Suggest: `Sobrescribir`
    - The prefix sobre- plus escribir contracts to “sobrescribir”; “sobreescribir” is not a valid spelling.
- `connection-proxy-autologin` — `browser/browser/preferences/connection.ftl` — Two misspellings in the tooltip: “cuand” and “gardado”.
    - Current: `cuand se han gardado credenciales`
    - Source: `accesskey: i label: Do not prompt for authentication if password is saved tooltip: This option silently authenticates you to proxies when you have saved credentials for them. You will be prompted if authentication fails.`
    - Suggest: `cuando se han guardado credenciales`
    - “cuand” and “gardado” are typos for “cuando” and “guardado”.
- `connection-proxy-autologin-checkbox` — `browser/browser/preferences/connection.ftl` — Same misspellings “cuand” and “gardado” in the checkbox tooltip.
    - Current: `cuand se han gardado credenciales`
    - Source: `accesskey: i label: Do not prompt for authentication if password is saved tooltiptext: This option silently authenticates you to proxies when you have saved credentials for them. You will be prompted if authentication f…`
    - Suggest: `cuando se han guardado credenciales`
    - Duplicate of the connection-proxy-autologin tooltip; both need the same spelling fix.
- `collection-health-report-disabled2` — `browser/browser/preferences/preferences.ftl` — Gender/number agreement error “La información … está deshabilitado”.
    - Current: `La información de datos está deshabilitado`
    - Source: `Data reporting is disabled for this build configuration.`
    - Suggest: `El envío de informes de datos está desactivado`
    - “información” is feminine, so the participle must agree; compare data-collection-health-report-disabled in the same file, “El envío de informes de datos está desactivado.”
- `collection-studies` — `browser/browser/preferences/preferences.ftl` — Ungrammatical “Permitir X para instalar” construction.
    - Current: `Permitir { -brand-short-name } para instalar y ejecutar estudios`
    - Source: `label: Allow { -brand-short-name } to install and run studies`
    - Suggest: `Permitir que { -brand-short-name } instale y ejecute estudios`
    - en-US “Allow Firefox to install and run studies”; Spanish requires “permitir que + subjuntivo”, as used in collection-health-report (“Permitir que { -brand-short-name } envíe…”).
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — Duplicated word “para para”.
    - Current: `Cookies separadas por contenedor para para poder usar`
    - Source: `description: Separate cookies by container so you can use different accounts on the same site and limit cross-site tracking. label: Containers`
    - Suggest: `Cookies separadas por contenedor para poder usar`
    - Accidental repetition; en-US “Separate cookies by container so you can use…”.
- `data-collection-run-studies` — `browser/browser/preferences/preferences.ftl` — Misspelling “paar” for “para”.
    - Current: `ayuda a mejorar la calidad paar todos`
    - Source: `description: { -brand-short-name } randomly selects users to test features, which helps improve quality for everyone. label: Allow { -brand-short-name } to run feature studies`
    - Suggest: `ayuda a mejorar la calidad para todos`
    - Typo; en-US “helps improve quality for everyone”.
- `extension-controlling-password-saving` — `browser/browser/preferences/preferences.ftl` — Verb “está” used instead of the demonstrative “esta”.
    - Current: `controla está configuración.`
    - Source: `<img data-l10n-name="icon"/> <strong>{ $name }</strong> controls this setting.`
    - Suggest: `controla esta configuración.`
    - The parallel string extension-controlling-web-notifications correctly reads “controla esta configuración.”
- `extension-controlling-proxy-config` — `browser/browser/preferences/preferences.ftl` — Verb agreement error “se conectan” with a singular subject (and unaccented “como”).
    - Current: `controla como { -brand-short-name } se conectan a internet.`
    - Source: `<img data-l10n-name ="icon"/> <strong>{ $name }</strong> controls how { -brand-short-name } connects to the internet.`
    - Suggest: `controla cómo { -brand-short-name } se conecta a internet.`
    - The subject is the singular brand name, so the verb must be “se conecta”; the interrogative “cómo” also needs its accent.
- `extension-controlling-websites-content-blocking-all-trackers` — `browser/browser/preferences/preferences.ftl` — Verb “está” used instead of the demonstrative “esta”.
    - Current: `controla está configuración.`
    - Source: `<img data-l10n-name="icon"/> <strong>{ $name }</strong> controls this setting.`
    - Suggest: `controla esta configuración.`
    - Same accent error as extension-controlling-password-saving; the demonstrative adjective carries no accent.
- `network-proxy-connection-settings2` — `browser/browser/preferences/preferences.ftl` — Verb “está” used instead of the demonstrative “esta”.
    - Current: `Cambiar está configuración puede causar problemas de conexión`
    - Source: `accesskey: p description: Changing these settings may cause connections issues label: Configure proxy`
    - Suggest: `Cambiar esta configuración puede causar problemas de conexión`
    - en-US: “Changing these settings may cause connections issues”; the demonstrative adjective must be “esta”.
- `preferences-ai-controls-pdfjs-control` — `browser/browser/preferences/preferences.ftl` — Missing preposition: “agregará descripciones hacerlas más accesibles”.
    - Current: `esto agregará descripciones hacerlas más accesibles`
    - Source: `description: When you add images to PDFs, this adds descriptions to make them accessible. label: Image alt text in { -brand-short-name } PDF viewer`
    - Suggest: `esto agregará descripciones para hacerlas más accesibles`
    - en-US: “this adds descriptions to make them accessible”; the purpose clause needs “para”.
- `preferences-connection-link-section` — `browser/browser/preferences/preferences.ftl` — Misspelling “verifificados”.
    - Current: `los sitios web son verifificados`
    - Source: `description: See how connections stay secure, harmful software is blocked, and websites are verified. label: Connection and software security`
    - Suggest: `los sitios web son verificados`
    - Syllable duplicated in “verificados”.
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — Stray article in “sobre el del proveedor”.
    - Current: `con control sobre el del proveedor y comportamiento de respaldo`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior. label: Custom`
    - Suggest: `con control sobre el proveedor y el comportamiento de respaldo`
    - en-US: “with control over your provider and fallback behavior”; “el del” leaves the phrase without a referent. The same fragment appears in preferences-doh-radio-custom.
- `preferences-doh-radio-off` — `browser/browser/preferences/preferences.ftl` — Description ends in the garbled token “0red”.
    - Current: `Usar el resolvedor de DNS 0red`
    - Source: `description: Use your default DNS resolver label: Off`
    - Suggest: `Usar el resolvedor de DNS predeterminado`
    - en-US: “Use your default DNS resolver”. Compare preferences-doh-overview-off in the same file, which reads “Usar el resolvedor de DNS predeterminado.”
- _…and 86 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `about-private-browsing-pin-promo-title` — `browser/browser/aboutPrivateBrowsing.ftl` — Voseo/tuteo («tu escritorio», «Navegá», «te») in a file that uses usted throughout.
    - Current: `directamente desde tu escritorio. Navegá como si nadie te estuviera mirando.`
    - Source: `No saved cookies or history, right from your desktop. Browse like no one’s watching.`
    - Suggest: `directamente desde su escritorio. Navegue como si nadie lo estuviera mirando.`
    - Every other string in about:privatebrowsing uses usted («Oculte», «Use», «su»).
- `restart-required-intro` — `browser/browser/aboutRestartRequired.ftl` — Tuteo «Tendrás» in a file that elsewhere follows the tree's usted convention.
    - Current: `Tendrás que reiniciar para finalizar la actualización.`
    - Source: `An update to { -brand-short-name } started in the background. You’ll need to restart to finish the update.`
    - Suggest: `Tendrá que reiniciar para finalizar la actualización.`
    - The rest of the Firefox es-AR UI addresses the user with usted; the sibling string window-restoration-info also uses «Tus».
- `restore-page-problem-desc` — `browser/browser/aboutSessionRestore.ftl` — Voseo imperative «Elegí» inside a section that otherwise addresses the user with usted.
    - Current: `Elegí Restaurar sesión para volver a intentarlo.`
    - Source: `We are having trouble restoring your last browsing session. Select Restore Session to try again.`
    - Suggest: `Elija Restaurar sesión para volver a intentarlo.`
    - Neighbouring strings in the same page use usted («Mire las pestañas», «vuelva a intentarlo»).
- `aiwindow-firstrun-model-subtitle-v2` — `browser/browser/aiWindow.ftl` — Tuteo «tus pestañas» in a screen that otherwise uses usted.
    - Current: `explorar todas tus pestañas`
    - Source: `Each model can help you to summarize, compare, and explore across your tabs. Switch anytime.`
    - Suggest: `explorar todas sus pestañas`
    - The companion string aiwindow-firstrun-model-subtitle uses «Elija… Se puede cambiar», and the firstrun title uses «para usted».
- `smartwindow-assistant-error-capacity-header` — `browser/browser/aiWindowContent.ftl` — Voseo «Probá» among sibling error messages that use usted.
    - Current: `está en su máxima capacidad en este momento. Probá de nuevo más tarde.`
    - Source: `{ -smart-window-brand-name } is at capacity right now. Please try again later.`
    - Suggest: `está en su máxima capacidad en este momento. Pruebe de nuevo más tarde.`
    - Adjacent error headers use «Intente de nuevo», «Espere un momento», «Pruebe una red diferente».
- `appmenu-nova-switch-device-promo` — `browser/browser/appmenu.ftl` — Voseo «Llevate … con vos» in the app menu, which uses usted elsewhere.
    - Current: `¡Llevate { -brand-short-name } con vos!`
    - Source: `message: Getting a new device soon? Take { -brand-short-name } with you!`
    - Suggest: `¡Lleve { -brand-short-name } con usted!`
    - Surrounding app-menu strings use usted («Administre», «Proteja y acceda a sus marcadores»).
- `appmenuitem-sign-in-account` — `browser/browser/appmenu.ftl` — Tuteo «tu cuenta» next to items that use «su».
    - Current: `Ingresar a tu cuenta`
    - Source: `Sign in to your account`
    - Suggest: `Ingresar a su cuenta`
    - The same panel uses «Proteja y acceda a sus marcadores» and «Administrar cuenta».
- `profiler-popup-description` — `browser/browser/appmenu.ftl` — Voseo «Colaborá … tu equipo» inside the profiler panel.
    - Current: `Colaborá en problemas de rendimiento publicando perfiles para compartir con tu equipo.`
    - Source: `Collaborate on performance issues by publishing profiles to share with your team.`
    - Suggest: `Colabore en problemas de rendimiento publicando perfiles para compartir con su equipo.`
    - All other profiler strings in this file use usted or impersonal forms («no la use», «Editar Preferencias»).
- `identity-permissions-storage-access-hint` — `browser/browser/browser.ftl` — Tuteo «mientras estás» in the identity panel, which uses usted.
    - Current: `mientras estás en este sitio`
    - Source: `These parties can use cross-site cookies and site data while you are on this site.`
    - Suggest: `mientras está en este sitio`
    - Neighbouring identity-panel strings use «Su conexión», «Está conectado».
- `private-browsing-info-panel-title` — `browser/browser/browser.ftl` — Tuteo «Estás» where the equivalent about:privatebrowsing string uses «Está».
    - Current: `Estás en una ventana privada`
    - Source: `You’re in a Private Window`
    - Suggest: `Está en una ventana privada`
    - about-private-browsing-info-title translates the identical en-US sentence as «Está en una ventana privada»; the panel body below also uses usted.
- `urlbar-trending-dismissal-acknowledgment` — `browser/browser/browser.ftl` — Tuteo in an acknowledgment whose siblings all use usted.
    - Current: `Gracias por tu opinión. Ya no verás las búsquedas más populares.`
    - Source: `Thanks for your feedback. You won’t see trending searches anymore.`
    - Suggest: `Gracias por su opinión. Ya no verá las búsquedas más populares.`
    - urlbar-dismissal-acknowledgment-weather and urlbar-result-dismissal-acknowledgment-all in the same file read «Gracias por su opinión. Ya no verá…».
- `crashed-subframe-message` — `browser/browser/contentCrash.ftl` — Voseo «enviá» while the paired title string uses «envíe».
    - Current: `se arregle más rápido, enviá un informe.`
    - Source: `<strong>Part of this page crashed.</strong> To let { -brand-product-name } know about this issue and get it fixed faster, please submit a report.`
    - Suggest: `se arregle más rápido, envíe un informe.`
    - The developer comment requires crashed-subframe-title to match this message; the title uses the usted form, so the two now differ.
- `contextual-manager-passwords-no-passwords-get-started-message` — `browser/browser/contextual-manager.ftl` — Voseo imperative «Agregalas» in the same usted-based screen.
    - Current: `Agregalas acá para empezar.`
    - Source: `Add them here to get started.`
    - Suggest: `Agréguelas acá para empezar.`
    - The heading right above is «Guarde las contraseñas en un lugar seguro»; the voseo form would also require an accent («Agregalas» → «Agregalas» is unaccented as written).
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — Tuteo «si te ves afectado» in the password manager, which uses usted.
    - Current: `alertas si te ves afectado`
    - Source: `All passwords are encrypted and we’ll watch out for breaches and alerts if you’re affected.`
    - Suggest: `alertas si se ve afectado`
    - Every other string in this file uses usted («Guarde las contraseñas», «Ingrese la contraseña»).
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — “Key” rendered as «clave» (password/cipher key) instead of «tecla», inconsistent with the rest of the file.
    - Current: `La clave no puede ser usada`
    - Source: `Key cannot be used`
    - Suggest: `La tecla no puede ser usada`
    - This dialog is about a keyboard key; customkeys-conflict-confirm and customkeys-key-invalid use «tecla», and «clave» reads as “password” in this product.
- `sidebar-callout-survey-thank-you` — `browser/browser/featureCallout.ftl` — Tuteo «tu opinión» in a survey that otherwise uses usted.
    - Current: `¡Gracias por tu opinión!`
    - Source: `Thank you for your feedback!`
    - Suggest: `¡Gracias por su opinión!`
    - The other survey strings use «¿Qué tan satisfecho está…?» and «Ayude a mejorar».
- `start-page-callout-subtitle` — `browser/browser/featureCallout.ftl` — Voseo «Probá» while the callout's own button says «Probar Startpage».
    - Current: `Probá Startpage. Está diseñado para mantener las búsquedas más privadas desde el principio.`
    - Source: `Try Startpage. It’s designed to keep your searches more private from the start.`
    - Suggest: `Pruebe Startpage. Está diseñado para mantener las búsquedas más privadas desde el principio.`
    - The Perplexity callouts immediately above use «Pruebe», as does the rest of the file.
- `windows-10-eos-sync-tour-title-1` — `browser/browser/featureCallout.ftl` — Voseo «Ordenalas» while the matching subtitle uses usted.
    - Current: `¿Demasiadas pestañas? Ordenalas con grupos de pestañas.`
    - Source: `Too many tabs? Tidy up with tab groups.`
    - Suggest: `¿Demasiadas pestañas? Ordénelas con grupos de pestañas.`
    - windows-10-eos-sync-tour-subtitle-1 says «Arrastre una pestaña…»; the accent is also missing for the voseo form.
- `firefoxview-history-empty-description-two` — `browser/browser/firefoxView.ftl` — Tuteo «puedes … tu» in a page that otherwise uses usted.
    - Current: `puedes controlar la actividad que { -brand-short-name } recuerda, en tu`
    - Source: `Protecting your privacy is at the heart of what we do. It’s why you can control the activity { -brand-short-name } remembers, in your <a data-l10n-name="history-settings-url">history settings</a>.`
    - Suggest: `puede controlar la actividad que { -brand-short-name } recuerda, en su`
    - The replacement string firefoxview-history-empty-description-2 and the rest of the page use usted/impersonal forms.
- `ipprotection-bandwidth-upgrade-text` — `browser/browser/ipProtection.ftl` — Two different forms of address inside one sentence: «Selecciona» (tú) then «agregue» (usted).
    - Current: `Selecciona una ubicación de la VPN y agregue protección`
    - Source: `Choose a VPN location and add protection to all your apps on up to 5 devices, whether you’re at home or on public Wi-Fi.`
    - Suggest: `Seleccione una ubicación de la VPN y agregue protección`
    - The verbs must agree; the rest of the file uses usted.
- `ipprotection-bandwidth-upgrade-title` — `browser/browser/ipProtection.ftl` — Mixed address in one string: «¿Te gusta…?» followed by «Consiga».
    - Current: `¿Te gusta la VPN integrada? Consiga aún más protección`
    - Source: `Like built-in VPN? Get even more protection outside { -brand-product-name } with { -mozilla-vpn-brand-name }.`
    - Suggest: `¿Le gusta la VPN integrada? Consiga aún más protección`
    - The two halves of the same sentence use different persons; the file's convention is usted.
- `ipprotection-feature-introduction-title-summer-promo` — `browser/browser/ipProtection.ftl` — Voseo «¿Tenés…? Llevá … con vos» while the paired description uses usted.
    - Current: `¿Tenés planes de viaje? Llevá tu privacidad con vos.`
    - Source: `Got travel plans? Take privacy with you.`
    - Suggest: `¿Tiene planes de viaje? Lleve su privacidad con usted.`
    - ipprotection-feature-introduction-description-summer-promo and the rest of the file use usted.
- `newtab-section-mangage-topics-title` — `browser/browser/newtab/newtab.ftl` — “Topics” rendered as “Tópicos” while the same panel uses “temas”.
    - Current: `Tópicos`
    - Source: `Topics`
    - Suggest: `Temas`
    - The adjacent button newtab-section-manage-topics-button-v2 is “Administrar temas” and home-prefs-manage-topics-link2 is “Administrar temas”; “Tópicos” is an anglicism inconsistent with the same surface.
- `newtab-wallpaper-category-title-celestial` — `browser/browser/newtab/newtab.ftl` — “Celestial” rendered as “Celeste”, which is also the name used for the light-blue wallpaper color.
    - Current: `Celeste`
    - Source: `Celestial`
    - Suggest: `Celestial`
    - The developer comment says the word refers to astronomy; “Celeste” is used in this same file as the color name (newtab-wallpaper-light-blue = Celeste), so as a category title it reads as a color, not as an astronomy category.
- `policy-Windows10SSO` — `browser/browser/policies/policies-descriptions.ftl` — “single sign-on” rendered as “un solo inicio de sesión” (only one sign-in), inconsistent with the next policy.
    - Current: `Permitir un solo inicio de sesión de Windows`
    - Source: `Allow Windows single sign-on for Microsoft, work, and school accounts.`
    - Suggest: `Permitir el inicio de sesión único de Windows`
    - policy-MicrosoftEntraSSO in the same file uses the correct term “inicio de sesión único”; “un solo inicio de sesión” reads as a numeric limit rather than the SSO feature.
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Usted form in a file whose other steps address the user informally.
    - Current: `Abra el menú`
    - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
    - Suggest: `Abrí el menú`
    - The rest of the dialog uses the informal address (“tu dispositivo móvil”, “sostené el teléfono”), so this step is inconsistent within the same screen.
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — “Enhanced Tracking Protection” rendered two different ways in the same dialog.
    - Current: `protección de rastreo avanzada`
    - Source: `You can specify which websites have Enhanced Tracking Protection turned off. Type the exact address of the site you want to manage and then click Add Exception.`
    - Suggest: `protección de rastreo aumentada`
    - The dialog title permissions-exceptions-etp-window2 uses “protección de rastreo aumentada”, which is also the form used in preferences.ftl (content-blocking-enhanced-tracking-protection, preferences-etp-status-header).
- `permissions-site-xr-desc` — `browser/browser/preferences/permissions.ftl` — Voseo (“tus”, “Podés”) in a file that otherwise addresses the user with usted.
    - Current: `Podés especificar cuales son los sitios web que tienen permitido el acceso a tus dispositivos`
    - Source: `The following websites have requested to access your virtual reality devices. You can specify which websites are allowed to access your virtual reality devices. You can also block new requests asking to access your virt…`
    - Suggest: `Puede especificar cuáles son los sitios web que tienen permitido el acceso a sus dispositivos`
    - Every other permission description in this file uses usted (“Puede especificar qué sitios web…”); “cuales” also needs its accent in an indirect question.
- `content-blocking-etp-standard-tcp-rollout-description` — `browser/browser/preferences/preferences.ftl` — Voseo/tuteo (“estás”, “seguirte”) in a file that addresses the user with usted.
    - Current: `el sitio en el que estás, así que los rastreadores no pueden usarlas para seguirte entre sitios`
    - Source: `Total Cookie Protection contains cookies to the site you’re on, so trackers can’t use them to follow you between sites.`
    - Suggest: `el sitio en el que está, así que los rastreadores no pueden usarlas para seguirlo entre sitios`
    - The surrounding content-blocking and ETP strings consistently use usted (“Elija…”, “protege al navegar… usted tenga el control”).
- `content-blocking-suspected-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — “huellas dactilares” breaks with “huellas digitales” used for fingerprinters everywhere else.
    - Current: `Presuntos detectores de huellas dactilares`
    - Source: `accesskey: S label: Suspected fingerprinters`
    - Suggest: `Presuntos detectores de huellas digitales`
    - All other fingerprinter strings in this file (including preferences-etp-custom-suspect-fingerprinting-protection-enabled) use “huellas digitales”.
- `forms-primary-pw-change` — `browser/browser/preferences/preferences.ftl` — “Primary Password” rendered with the old term “maestra”, duplicating the legacy string.
    - Current: `Cambiar la contraseña maestra…`
    - Source: `accesskey: P label: Change Primary Password…`
    - Suggest: `Cambiar la contraseña primaria…`
    - forms-master-pw-change is the string that intentionally keeps the former “Master Password” name; forms-primary-pw-change is the current label and should match forms-primary-pw-set / forms-primary-pw-change-2, which use “contraseña primaria”.
- `skip-troubleshoot-refresh-profile` — `browser/browser/safeMode.ftl` — Tuteo "puedes" in a file and tree that address the user with usted.
    - Current: `También puedes omitir`
    - Source: `You can also skip troubleshooting and refresh { -brand-short-name }, instead.`
    - Suggest: `También puede omitir`
    - The rest of the file uses usted ("Sus complementos", "Puede intentar"), and usted is overwhelmingly dominant across the locale.
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints` uses three dots where this locale uses …
    - Current: `Haga clic derecho en un elemento en el %S y seleccione “Romper en...” para agregar un punto de interrupción`
    - Source: `Right click an element in the %S and select “Break on…” to add a breakpoint`
    - The tree uses … 459 times against 2 ASCII runs.
- `ImageMapPolyWrongNumberOfCoords` — `dom/chrome/layout/layout_errors.properties` — `ImageMapPolyWrongNumberOfCoords` uses three dots where this locale uses …
    - Current: `El atributo "coords" del tag <area shape="poly"> no tiene el formato "x1,y1,x2,y2 ...".`
    - Source: `The “coords” attribute of the <area shape="poly"> tag is not in the “x1,y1,x2,y2 …” format.`
    - The tree uses … 459 times against 2 ASCII runs.
- `newTabControlled.message2` — `toolkit/chrome/global/extensions.properties` — Tuteo "ves" among usted forms
    - Current: `cambió la página que ves cuando se abre una nueva pestaña`
    - Source: `An extension, %S, changed the page you see when you open a new tab.`
    - Suggest: `cambió la página que ve cuando se abre una nueva pestaña`
    - The next string in the same file (homepageControlled.message) uses "ve" and "su página de inicio".
- `content-uses-tiling` — `toolkit/toolkit/about/aboutSupport.ftl` — “Tiling” rendered as “baldosas” (floor tiles) here but as “mosaicos” in the adjacent uses-tiling row.
    - Current: `content-uses-tiling = Utiliza baldosas (contenido)`
    - Source: `Uses Tiling (Content)`
    - Suggest: `Utiliza mosaicos (contenido)`
    - Two consecutive rows for the same graphics feature use different terms, and “baldosas” is not used for graphics tiling anywhere else in the tree.
- `certificate-viewer-subject-name` — `toolkit/toolkit/about/certviewer.ftl` — “Subject” rendered as “asunto” (email subject) here, but as “sujeto” in certificate-viewer-subject-alt-names.
    - Current: `certificate-viewer-subject-name = Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - Within the same certificate viewer the X.509 subject is called “sujeto” in one label and “asunto” in two others (also certificate-viewer-subject-key-id); “asunto” names an email header, not the certificate subject.
- `experimental-features-web-gpu-description3` — `toolkit/toolkit/featuregates/features.ftl` — Voseo imperative "Consultá" among usted forms
    - Current: `Consultá el <a data-l10n-name="bugzilla">bug 1616739</a> para más detalles.`
    - Source: `The <a data-l10n-name="wikipedia-webgpu">WebGPU API</a> provides low-level support for performing computation and graphics rendering using the <a data-l10n-name="wikipedia-gpu">Graphics Processing Unit (GPU)</a> of the…`
    - Suggest: `Consulte el <a data-l10n-name="bugzilla">bug 1616739</a> para más detalles.`
    - Every other description in the same file uses the usted imperative "Consulte".
- `user-context-color-purple` — `toolkit/toolkit/global/contextual-identity.ftl` — "Purple" and "Violet" both rendered "Violeta"
    - Current: `user-context-color-purple =     .label = Violeta`
    - Source: `label: Purple`
    - Suggest: `user-context-color-purple =     .label = Púrpura`
    - These are two selectable swatches; identical labels make one colour unidentifiable, and user-context-color-violet already holds "Violeta".
- `webext-perms-description-trialML` — `toolkit/toolkit/global/extensionPermissions.ftl` — Tuteo "tu dispositivo" among usted forms
    - Current: `Descargar y ejecutar modelos de IA en tu dispositivo`
    - Source: `Download and run AI models on your device`
    - Suggest: `Descargar y ejecutar modelos de IA en su dispositivo`
    - All other permission descriptions in the file use "su" (e.g. "Acceder a su ubicación").
- `permission-dialog-unset-description` — `toolkit/toolkit/global/handlerDialog.ftl` — Tuteo "Tendrás" breaks the usted register
    - Current: `Tendrás que elegir una aplicación.`
    - Source: `You’ll need to choose an application.`
    - Suggest: `Tendrá que elegir una aplicación.`
    - Every other string in this file and the surrounding tree uses usted ("Elegir…", "se puede cambiar").
- `certerror-expired-cert-what-can-you-do-about-it-clock` — `toolkit/toolkit/neterror/netError.ftl` — Mixes "su computadora" with tuteo "tu sistema"
    - Current: `en la configuración de tu sistema`
    - Source: `Your computer clock is set to { $now }. Make sure your computer is set to the correct date, time, and time zone in your system settings, and then refresh <b>{ $hostname }</b>.`
    - Suggest: `en la configuración de su sistema`
    - The same sentence uses usted ("su computadora", "Asegúrese"); "tu" breaks the register mid-string.
- `pdfjs-editor-alt-text-settings-show-dialog-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Mixes tuteo "Te" with usted "asegurarse"
    - Current: `Te ayuda a asegurarse de que todas las imágenes tengan texto alternativo.`
    - Source: `Helps you make sure all your images have alt text.`
    - Suggest: `Ayuda a asegurarse de que todas las imágenes tengan texto alternativo.`
    - The file and the whole tree address the user with "usted"; "Te" is inconsistent even within this one sentence.
- `printui-error-invalid-start-overflow` — `toolkit/toolkit/printing/printUI.ftl` — Closing curly quote is an opening quote
    - Current: `el número “hasta“.`
    - Source: `The “from” page number must be smaller than the “to” page number.`
    - Suggest: `el número “hasta”.`
    - The pair should be “ … ”; the file (and tree) otherwise uses matched curly quotes.
- `printui-two-sided-printing-long-edge` — `toolkit/toolkit/printing/printUI.ftl` — "edge" rendered as "margen" in one string, "borde" in the next
    - Current: `Doblar por el margen largo`
    - Source: `Flip on long edge`
    - Suggest: `Doblar por el borde largo`
    - The paired string printui-two-sided-printing-short-edge uses "borde"; "margen" means margin, a different print concept already used for printui-margins.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-AR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
