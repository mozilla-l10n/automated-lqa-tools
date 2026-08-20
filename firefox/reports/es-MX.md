# Firefox l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,843 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (2)

- `unified-extensions-mb-blocklist-warning-multiple` — `browser/browser/unifiedExtensions.ftl` — `unified-extensions-mb-blocklist-warning-multiple` (`.message`) references ['extensionsCount'], which en-US does not pass
  - Current: `{ $extensionsCount } extensiones deshabilitadas`
  - en-US: `Some of your extensions have been disabled for violating Mozilla’s policies. You can enable them in settings, but this may be risky.`
  - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `unified-extensions-mb-blocklist-error-multiple` — `browser/browser/unifiedExtensions.ftl` — `unified-extensions-mb-blocklist-error-multiple` (`.message`) references ['extensionsCount'], which en-US does not pass
  - Current: `{ $extensionsCount } extensiones deshabilitadas`
  - en-US: `Some of your extensions have been disabled for violating Mozilla’s policies.`
  - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 357 |
| Strings | 17,843 |
| Missing strings | 320 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 2 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Access keys not in their label | 142 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 131 |

### Completeness

**320 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 67
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 23
- `toolkit/toolkit/about/aboutNetworking.ftl` — 20
- `toolkit/toolkit/about/aboutAddons.ftl` — 15
- `browser/browser/newtab/onboarding.ftl` — 13
- `toolkit/toolkit/neterror/netError.ftl` — 13
- `browser/browser/sharePanel.ftl` — 12
- `browser/browser/sidebar.ftl` — 12
- `browser/browser/preferences/preferences.ftl` — 12
- `browser/browser/newtab/asrouter.ftl` — 11
- `devtools/client/toolbox-options.ftl` — 11

**Files absent from the locale:**

- `browser/browser/sharePanel.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/rosettaNotification.ftl`

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
| inverted marks | `open-question` 367, `open-exclamation` 84 | **open-question** |
| register | `informal` 1359, `formal` 237 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 142 strings** — 142 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
  - Affected: `addressbar-locbar-clipboard-option`, `addressbar-locbar-openpage-option`, `addressbar-locbar-quickactions-option`, `appmenu-addon-post-install-pin-toolbarbutton-checkbox`, `appmenu-help-more-troubleshooting-info`, `appmenu-help-not-deceptive`, `appmenu-homepage-controlled-changes`, `appmenu-new-tab-controlled-changes`, `appmenu-tab-hide-controlled`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2` …and 129 more
- **typography — 131 strings** — 131 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `AutomaticAuth`, `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CORSPreflightDidNotSucceed3`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolationWithURI`, `CompositorAnimationWarningTransformWithSyncGeometricAnimations`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed` …and 117 more

---

## 3. Open findings (134)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 11 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 65 |
| 4 | Cosmetic (typography, spacing) | 18 |

### A. Functional, markup, variables & plurals

- `login-intro-instructions-fxa-settings` — `browser/browser/aboutLogins.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - en-US: `Ajustes>`
- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — account-tabs-closed-remotely (accounts.ftl) — missing spaces around brand: { $closedCount }{ -brand-short-name } pestaña renders e.g. "1Firefox…".
- `main-context-menu-edit-bookmark-with-shortcut` — `browser/browser/browserContext.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - en-US: `Ajustes>`
- `tab-context-close-n-tabs` — `browser/browser/tabContextMenu.ftl` — tab-context-close-n-tabs (tabContextMenu.ftl) — plural variants reversed: [one] reads "pestañas" (plural), [other] reads singular "pestaña" — visible bug for counts ≥2.
- `tab-context-move-tab-to-new-group` — `browser/browser/tabbrowser.ftl` — tab-context-move-tab-to-new-group (tabbrowser.ftl) — stray backtick: Agregar pestaña `.
- `unified-extensions-mb-blocklist-error-multiple` — `browser/browser/unifiedExtensions.ftl` — `unified-extensions-mb-blocklist-error-multiple` (`.message`) references ['extensionsCount'], which en-US does not pass
  - Current: `{ $extensionsCount } extensiones deshabilitadas`
  - en-US: `Some of your extensions have been disabled for violating Mozilla’s policies.`
  - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `unified-extensions-mb-blocklist-warning-multiple` — `browser/browser/unifiedExtensions.ftl` — `unified-extensions-mb-blocklist-warning-multiple` (`.message`) references ['extensionsCount'], which en-US does not pass
  - Current: `{ $extensionsCount } extensiones deshabilitadas`
  - en-US: `Some of your extensions have been disabled for violating Mozilla’s policies. You can enable them in settings, but this may be risky.`
  - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — inverted <strong> tags: </strong>{ $property }<strong> → <strong>{ $property }</strong>.
- `about-logging-log-tutorial` — `toolkit/toolkit/about/aboutLogging.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - en-US: `Ajustes>`
- `rights-webservices` — `toolkit/toolkit/about/aboutRights.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - en-US: `Ajustes>`
- `fp-certerror-bad-domain-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - en-US: `Ajustes>`

### B. Mistranslation, reversed meaning, wrong names & brand

- `urlbar-result-search-with` — `browser/browser/browser.ftl` — urlbar-result-search-with (browser.ftl) — "Search with" → "Navegue con" (wrong verb + usted) → "Buscar con".
  - en-US: `"Navegue con"`
- `genai-onboarding-gemini-tooltip` — `browser/browser/genai.ftl` — genai-onboarding-gemini-tooltip (genai.ftl) — "Google Géminis" → "Google Gemini" (brand; correct in sibling strings).
  - en-US: `"Google Gemini"`
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — genai-settings-chat-chatgpt-links (genai.ftl) — "chatGPT" → "ChatGPT".
  - en-US: `"ChatGPT".`
- `newtab-section-menu-collapse-section` — `browser/browser/newtab/newtab.ftl` — newtab-section-menu-collapse-section (newtab.ftl) — "Collapse Section" → "Sección de colapso" → "Contraer sección".
  - en-US: `"Sección de colapso" → "Contraer sección".`
- `newtab-weather-sponsored` — `browser/browser/newtab/newtab.ftl` — newtab-weather-sponsored (newtab.ftl) — "Sponsored" → "Patrocinador" (sponsor) → "Patrocinado".
  - en-US: `"Patrocinador"`
- `newtab-widget-timer-notification-break` — `browser/browser/newtab/newtab.ftl` — newtab-widget-timer-notification-break (newtab.ftl) — "Your break is over" → "Se acabaron tus vacaciones" (vacation) → "Se acabó tu descanso".
  - en-US: `"Se acabaron tus vacaciones"`
- `media-count` — `browser/browser/pageInfo.ftl` — media-count (pageInfo.ftl) — "Count" (tally) → "Cuenta" (account) → "Cantidad".
  - en-US: `"Cuenta"`
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — panic-button-open-new-window (panicButton.ftl) — dropped "clean": "Open a new clean window".
- `places-load-js-data-url-error` — `browser/browser/placesPrompts.ftl` — places-load-js-data-url-error (placesPrompts.ftl) — dropped scheme colon from javascript:/data: (comment: do not translate).
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — dropped "/8" from "127.0.0.1/8" (comment: do not translate).
- `content-blocking-warning-title-2` — `browser/browser/preferences/preferences.ftl` — content-blocking-warning-title-2 (preferences.ftl) — meaning inverted ("sites break the protection" instead of "sites may break with strict protection").
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — preferences-data-migration-description (preferences.ftl) — garbled "…datos de autocompletadomarcar en…".
- `security-privacy-issue-warning-extension-install` — `browser/browser/preferences/preferences.ftl` — security-privacy-issue-warning-extension-install (preferences.ftl) — "extensions" → "excepciones" → "extensiones".
  - en-US: `"excepciones" → "extensiones".`
- `sync-signedin-login-failure` — `browser/browser/preferences/preferences.ftl` — sync-signedin-login-failure (preferences.ftl) — duplicated clause ("Inicia sesión para reconectar … Favor de iniciar la sesión para reconectar").
- `profile-card-edit-button` — `browser/browser/profiles.ftl` — profile-card-edit-button (profiles.ftl) — "Edit perfil" left in English → "Editar perfil".
  - en-US: `"Editar perfil".`
- `screenshots-private-window-error-title` — `browser/browser/screenshots.ftl` — screenshots-private-window-error-title (screenshots.ftl) — redundant "Firefox { -screenshots-brand-name }".
- `sidebar-menu-open-ai-chatbot-tooltip-generic` — `browser/browser/sidebar.ftl` — sidebar-menu-open-ai-chatbot-tooltip-generic (sidebar.ftl) — "Open AI chatbot" (verb) → "Chatbot de IA abierta" (state, wrong gender) → "Abrir el chatbot de IA".
  - en-US: `"Chatbot de IA abierta"`
- `sidebar-menu-open-tabs-label` — `browser/browser/sidebar.ftl` — sidebar-menu-open-tabs-label (sidebar.ftl) — "Open tabs" is a noun (per comment) → "Abrir pestañas" (imperative) → "Pestañas abiertas".
  - en-US: `"Abrir pestañas"`
- `text-recognition-modal-searching-title` — `browser/browser/textRecognition.ftl` — text-recognition-modal-searching-title (textRecognition.ftl) — reversed: "Buscando imagen para texto" → "Buscando texto en la imagen".
  - en-US: `"Buscando texto en la imagen".`
- `touchbar-fullscreen-exit` — `browser/browser/touchbar/touchbar.ftl` — touchbar-fullscreen-exit (touchbar.ftl) — "fullscreen" → "ventana completa" → "pantalla completa".
  - en-US: `"ventana completa" → "pantalla completa".`
- `webrtc-reason-for-no-permanent-allow-insecure` — `browser/browser/webrtcIndicator.ftl` — webrtc-reason-for-no-permanent-allow-insecure (webrtcIndicator.ftl) — "for this session" → "…por esta razón" (reason) → "durante esta sesión".
  - en-US: `"…por esta razón"`
- `add-exception-domain-mismatch-long` — `security/manager/security/certificates/certManager.ftl` — add-exception-domain-mismatch-long (certManager.ftl) — ungrammatical connector + wrong mood ("y lo cual significa que alguien intente…").
- `pippki-incorrect-pw` — `security/manager/security/pippki/pippki.ftl` — pippki-incorrect-pw (pippki.ftl) — "current password" → "contraseña principal" → "contraseña actual".
  - en-US: `"contraseña principal" → "contraseña actual".`
- `about-webrtc-closed-peerconnection-disclosure-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "PeerConnections" translated to "conexiones de pares" in the hide-msg variant only (comment: keep PeerConnection).
- `language-name-ab` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-af` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-fj` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-hi` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-hsb` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-ky` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-tg` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-ty` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-uz` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-wen` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `language-name-yi` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
- `region-name-ai` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
- `region-name-az` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
- `region-name-cv-2020` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
- `region-name-st` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
- `region-name-vn` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.

### C. Grammar, agreement & spelling

- `about-logins-os-auth-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-os-auth-dialog-message (aboutLogins.ftl) — "constraseñas" → "contraseñas".
  - en-US: `"contraseñas".`
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — ai-window-delete-all-memories-message (aiFeatures.ftl) — "recuerdos… será eliminados" → "serán".
  - en-US: `"serán".`
- `smart-window-model-flexible` — `browser/browser/aiFeatures.ftl` — smart-window-model-flexible (aiFeatures.ftl) — "para la un uso general" (stray "la").
- `smartwindow-assistant-error-budget-header` — `browser/browser/aiWindowContent.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
  - Current: `has`
  - en-US: `haz`
- `extension-firefox-compact-dark-description` — `browser/browser/appExtensionFields.ftl` — extension-firefox-compact-dark-description (appExtensionFields.ftl) — "una paleta de colores oscuro" → "oscuros".
  - en-US: `"oscuros".`
- `browser-tab-audio-blocked` — `browser/browser/browser.ftl` — browser-tab-audio-blocked (browser.ftl) — "AUTOREPRODUCCIÓN BLOQUEDA" → "BLOQUEADA".
  - en-US: `"BLOQUEADA".`
- `identity-description-weak-cipher-intro` — `browser/browser/browser.ftl` — identity-description-weak-cipher-intro (browser.ftl) — "no es privado" → "privada" (conexión).
  - en-US: `"privada"`
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
- `urlbar-midi-blocked` — `browser/browser/browser.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
  - Current: `has`
  - en-US: `haz`
- `content-sharing-modal-too-many-pages` — `browser/browser/contentSharing.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
  - Current: `has`
  - en-US: `haz`
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — firefox-relay-offer-legal-notice-control and siblings (firefoxRelay.ftl) — "iniciar sesión a tu cuenta" → "en tu cuenta".
  - en-US: `"en tu cuenta".`
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — genai-prompts-quiz (genai.ftl) — "Hazme un prueba" → "una prueba".
  - en-US: `"una prueba".`
- `ipprotection-location-selection-callout-primary-button` — `browser/browser/ipProtection.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `vpn-paused-alert-title` — `browser/browser/ipProtection.ftl` — vpn-paused-alert-title (ipProtection.ftl) — "VPN pausado" → "pausada".
  - en-US: `"pausada".`
- `import-close-source-browser` — `browser/browser/migration.ftl` — import-close-source-browser (migration.ftl) — queísmo: "asegúrate que… está cerrado" → "asegúrate de que… esté cerrado".
  - en-US: `"asegúrate de que… esté cerrado".`
- `cfr-doorhanger-bookmark-fxa-body` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-bookmark-fxa-body (asrouter.ftl) — "Coemienza" → "Comienza".
  - en-US: `"Comienza".`
- `colorways-cfr-header-today` — `browser/browser/newtab/asrouter.ftl` — colorways-cfr-header-today (asrouter.ftl) — "Voces Independiente" → "Independientes".
  - en-US: `"Independientes".`
- `firefoxview-cfr-primarybutton` — `browser/browser/newtab/asrouter.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `fxa-adoption-primary-button-label` — `browser/browser/newtab/asrouter.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `root-certificate-succession-infobar-march-message` — `browser/browser/newtab/asrouter.ftl` — root-certificate-succession-infobar-march-message (asrouter.ftl) — "14 de Marzo" → "marzo" (months lowercase).
  - en-US: `"marzo"`
- `newtab-custom-wallpaper-cta` — `browser/browser/newtab/newtab.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `newtab-pocket-thumbs-down-tooltip` — `browser/browser/newtab/newtab.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `mr2022-onboarding-colorway-subtitle` — `browser/browser/newtab/onboarding.ftl` — mr2022-onboarding-colorway-subtitle (onboarding.ftl) — "Voces independientes puede" → "pueden".
  - en-US: `"pueden".`
- `mr2022-onboarding-existing-set-default-only-subtitle` — `browser/browser/newtab/onboarding.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `mr2022-onboarding-gratitude-title` — `browser/browser/newtab/onboarding.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
- `places-forget-about-this-site-confirmation-msg` — `browser/browser/places.ftl` — places-forget-about-this-site-confirmation-msg (places.ftl) — "¿Estás seguro que…?" → "seguro de que".
  - en-US: `"seguro de que".`
- `more-from-moz-qr-code-box-firefox-mobile-title` — `browser/browser/preferences/moreFromMozilla.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `httpsonly-radio-disabled3` — `browser/browser/preferences/preferences.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
- `performance-use-recommended-settings-checkbox` — `browser/browser/preferences/preferences.ftl` — performance-use-recommended-settings-checkbox (preferences.ftl) — "ajustes… recomendadas" → "recomendados".
  - en-US: `"recomendados".`
- `sync-engine-settings` — `browser/browser/preferences/preferences.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
  - Current: `has`
  - en-US: `haz`
- `graph-private-window` — `browser/browser/protections.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — protections-panel-cross-site-tracking-cookies (protectionsPanel.ftl) — "Ellos son creados" → "Son creadas" (cookies fem.).
  - en-US: `"Son creadas"`
- `protections-panel-etp-toggle-off` — `browser/browser/protectionsPanel.ftl` — protections-panel-etp-toggle-off (aria, protectionsPanel.ftl) — "Desactiva" → "Desactivada".
  - en-US: `"Desactivada".`
- `translations-panel-revisit-header` — `browser/browser/translations.ftl` — Missing-accent typos (verb forms esta→está, etc.): update-applying / settings-update-applying ("actualizaciónes" → "actualización(es)"), update-failed ("ultima" → "última") (aboutDialog.ftl); ai-window-no-memories-learning-off (aiFeatures.ftl), link-preview-onboarding-description-long-press (genai.ftl), webext-perms-header-unsigned-with-perms (global/extensions.ftl), pdfjs-printing-not-supported…
  - Current: `esta`
  - en-US: `está`
- `webrtc-allow-share-speaker-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — webrtc-allow-share-speaker-unsafe-delegation (webrtcIndicator.ftl) — "que { $origin } de acceso" → "dé acceso".
  - en-US: `"dé acceso".`
- `webrtc-indicator-menuitem-sharing-application-with` — `browser/browser/webrtcIndicator.ftl` — webrtc-indicator-menuitem-sharing-application-with (webrtcIndicator.ftl) — "un aplicación" → "una aplicación".
  - en-US: `"una aplicación".`
- `webrtc-share-screen-warning` — `browser/browser/webrtcIndicator.ftl` — webrtc-share-screen-warning (webrtcIndicator.ftl) — double "a": "permitir a sitios… a navegar" → "…navegar".
  - en-US: `"…navegar".`
- `accessibility-text-label-issue-figure` — `devtools/client/accessibility.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `perftools-description-local-build` — `devtools/client/perftools.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
- `perftools-thread-jvm-pool` — `devtools/client/perftools.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `inactive-css-not-floated-fix` — `devtools/client/tooltips.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `inactive-css-not-grid-or-flex-item` — `devtools/client/tooltips.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — cert-format-pkcs7-chain (certManager.ftl) — "(PKCX#7)" → "PKCS#7".
  - en-US: `"PKCS#7".`
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — unable-to-toggle-fips (deviceManager.ftl) — missing space "seguridad.Te" + "recomiend" → "recomendamos".
  - en-US: `"recomendamos".`
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — Missing-accent typos (verb forms esta→está, etc.): update-applying / settings-update-applying ("actualizaciónes" → "actualización(es)"), update-failed ("ultima" → "última") (aboutDialog.ftl); ai-window-no-memories-learning-off (aiFeatures.ftl), link-preview-onboarding-description-long-press (genai.ftl), webext-perms-header-unsigned-with-perms (global/extensions.ftl), pdfjs-printing-not-supported…
  - Current: `esta`
  - en-US: `está`
- `form-post-secure-to-insecure-warning-message` — `toolkit/toolkit/global/htmlForm.ftl` — Missing-accent typos (verb forms esta→está, etc.): update-applying / settings-update-applying ("actualizaciónes" → "actualización(es)"), update-failed ("ultima" → "última") (aboutDialog.ftl); ai-window-no-memories-learning-off (aiFeatures.ftl), link-preview-onboarding-description-long-press (genai.ftl), webext-perms-header-unsigned-with-perms (global/extensions.ftl), pdfjs-printing-not-supported…
  - Current: `esta`
  - en-US: `está`
- `findbar-match-diacritics-status` — `toolkit/toolkit/main-window/findbar.ftl` — findbar-match-diacritics-status (findbar.ftl) — "diacrícitos" → "diacríticos".
  - en-US: `"diacríticos".`
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — webauthn-related-origin-create-header (webauthnDialog.ftl) — "una lleva de acceso" → "llave".
  - en-US: `"llave".`

### D. Terminology, register & consistency

- `content-blocking-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
- `content-blocking-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
- `content-blocking-known-and-suspected-fingerprinters` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
- `content-blocking-known-fingerprinters-label` — `browser/browser/preferences/preferences.ftl` — Fingerprinters: "Huellas dactilares" (content-blocking-fingerprinters, content-blocking-fingerprinters-label) vs "Detectores de huellas digitales" (content-blocking-known-and-suspected-fingerprinters, content-blocking-known-fingerprinters-label).
- `sidebar-item-session-history` — `devtools/client/application.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `fips-nonempty-primary-password-required` — `security/manager/security/certificates/deviceManager.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
- `addon-detail-rating-label` — `toolkit/toolkit/about/aboutAddons.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `detail-rating` — `toolkit/toolkit/about/aboutAddons.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `certificate-viewer-subject-alt-names` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `certificate-viewer-subject-key-id` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `certificate-viewer-subject-name` — `toolkit/toolkit/about/certviewer.ftl` — click: "haz clic" vs "da clic" (permissions.ftl); Subject (cert) certificate-viewer-subject-name "interesado" / certificate-viewer-subject-alt-names "sujeto" / certificate-viewer-subject-key-id "asunto"; Rating detail-rating "Clasificación" vs addon-detail-rating-label "Calificación"; Icon "Icono" vs "Ícono" (sidebar-item-session-history and siblings).
- `primary-password-required-by-policy` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).

### E. Typography, punctuation & spacing

- `smartwindow-messages-document-title` — `browser/browser/aiWindowContent.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — Trailing stray characters: onboarding-genai-sidebar-subtitle (".—" after link).
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `settings-translations-subpage-download-language-option` — `browser/browser/preferences/preferences.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `opensearch-error-duplicate-desc` — `browser/browser/search.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `inactive-css-not-inline-or-tablecell` — `devtools/client/tooltips.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `about-about-note` — `toolkit/toolkit/about/aboutAbout.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
- `about-httpsonly-suggestion-box-www-text` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
- `rights-locationawarebrowsing` — `toolkit/toolkit/about/aboutRights.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `rights-safebrowsing` — `toolkit/toolkit/about/aboutRights.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
- `remote-debugging-title` — `toolkit/toolkit/about/aboutSupport.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
- `about-webauthn-ctap2-enroll-feedback-too-right` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
- `about-webauthn-text-not-available` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
- `findbar-match-diacritics` — `toolkit/toolkit/main-window/findbar.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Resolved to date (89)

- `settings-update-applying` — `browser/browser/aboutDialog.ftl` — fixed 2026-07-27
- `update-applying` — `browser/browser/aboutDialog.ftl` — fixed 2026-07-27
- `update-failed` — `browser/browser/aboutDialog.ftl` — fixed 2026-07-27
- `ai-window-no-memories-learning-off` — `browser/browser/aiFeatures.ftl` — fixed 2026-07-27
- `urlbar-result-menu-dont-show-weather-suggestions` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `urlbar-result-menu-dont-show-weather-suggestions2` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `urlbar-result-menu-tip-get-help` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `urlbar-result-menu-tip-get-help2` — `browser/browser/browser.ftl` — fixed 2026-07-27
- `firefoxview-history-empty-description` — `browser/browser/firefoxView.ftl` — fixed 2026-07-27
- `link-preview-onboarding-description-long-press` — `browser/browser/genai.ftl` — fixed 2026-07-27
- `languages-description` — `browser/browser/preferences/languages.ftl` — fixed 2026-07-27
- `permissions-window2` — `browser/browser/preferences/permissions.ftl` — fixed 2026-07-27
- `addressbar-locbar-suggest-sponsored-desc` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-27
- `addressbar-locbar-suggest-sponsored-option-2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-27
- `select-bookmark-desc` — `browser/browser/preferences/selectBookmark.ftl` — fixed 2026-07-27
- `new-profile-page-header-description` — `browser/browser/profiles.ftl` — fixed 2026-07-27
- `present-avatar-tooltip` — `browser/browser/profiles.ftl` — fixed 2026-07-27
- `restored-profile-page-header-description` — `browser/browser/profiles.ftl` — fixed 2026-07-27
- `shopping-avatar-tooltip` — `browser/browser/profiles.ftl` — fixed 2026-07-27
- `star-avatar` — `browser/browser/profiles.ftl` — fixed 2026-07-27
- `sync-account-in-use-description-merge` — `browser/browser/sync.ftl` — fixed 2026-07-27
- `sync-profile-different-account-header` — `browser/browser/sync.ftl` — fixed 2026-07-27
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-27
- `about-debugging-sidebar-runtime-item-name` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-27
- `accessibility-keyboard-issue-focusable` — `devtools/client/accessibility.ftl` — fixed 2026-07-27
- `network-menu-summary-finish` — `devtools/client/netmonitor.ftl` — fixed 2026-07-27
- `perftools-intro-description` — `devtools/client/perftools.ftl` — fixed 2026-07-27
- `options-enable-custom-formatters-label` — `devtools/client/toolbox-options.ftl` — fixed 2026-07-27
- `options-sourceeditor-detectindentation-label` — `devtools/client/toolbox-options.ftl` — fixed 2026-07-27
- `toolbox-meatball-menu-dock-separate-window-label` — `devtools/client/toolbox.ftl` — fixed 2026-07-27
- `inactive-css-not-for-internal-table-elements-except-table-cells-fix` — `devtools/client/tooltips.ftl` — fixed 2026-07-27
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — fixed 2026-07-27
- `inactive-scroll-padding-when-not-scroll-container-fix` — `devtools/client/tooltips.ftl` — fixed 2026-07-27
- `whypaused-pause-on-dom-events` — `devtools/shared/debugger-paused-reasons.ftl` — fixed 2026-07-27
- `whypaused-promise-rejection` — `devtools/shared/debugger-paused-reasons.ftl` — fixed 2026-07-27
- `certmgr-delete-builtin` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-27
- `certmgr-edit` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-27
- `discopane-notice-recommendations` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-07-27
- `extensions-warning-check-compatibility` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-07-27
- `extensions-warning-update-security` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-07-27
