# Firefox l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `39e5663f3de7` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `50d2f3b3f7c8` |
| **Previous run** | 2026-08-24 @ `39e5663f3de7` |
| **Mode** | recheck |
| **Strings reviewed this run** | 0 of 17,847 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (112)

- `about-logins-os-auth-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-os-auth-dialog-message (aboutLogins.ftl) — "constraseñas" → "contraseñas".
    - Source: `{$sel_1 ->} [macos] change the settings for passwords [other] { -brand-short-name } is trying to change the settings for passwords. Use your device sign in to allow this.`
    - Suggest: `"contraseñas".`
- `login-intro-instructions-fxa-settings` — `browser/browser/aboutLogins.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `Go to Settings > Sync > Turn on syncing… Select the Logins and passwords checkbox.`
    - Suggest: `Ajustes>`
- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — account-tabs-closed-remotely (accounts.ftl) — missing spaces around brand: { $closedCount }{ -brand-short-name } pestaña renders e.g. "1Firefox…".
    - Source: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab closed [other] { $closedCount } { -brand-short-name } tabs closed`
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — ai-window-delete-all-memories-message (aiFeatures.ftl) — "recuerdos… será eliminados" → "serán".
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - Suggest: `"serán".`
- `smart-window-model-flexible` — `browser/browser/aiFeatures.ftl` — smart-window-model-flexible (aiFeatures.ftl) — "para la un uso general" (stray "la").
    - Source: `description: Model { $model } by { $ownerName } label: Flexible: Solid fit for most needs`
- `smartwindow-messages-document-title` — `browser/browser/aiWindowContent.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `{ -smart-window-brand-name } chat messages`
- `extension-firefox-compact-dark-description` — `browser/browser/appExtensionFields.ftl` — extension-firefox-compact-dark-description (appExtensionFields.ftl) — "una paleta de colores oscuro" → "oscuros".
    - Source: `A theme with a dark color scheme.`
    - Suggest: `"oscuros".`
- `browser-tab-audio-blocked` — `browser/browser/browser.ftl` — browser-tab-audio-blocked (browser.ftl) — "AUTOREPRODUCCIÓN BLOQUEDA" → "BLOQUEADA".
    - Source: `AUTOPLAY BLOCKED`
    - Suggest: `"BLOQUEADA".`
- `identity-description-weak-cipher-intro` — `browser/browser/browser.ftl` — identity-description-weak-cipher-intro (browser.ftl) — "no es privado" → "privada" (conexión).
    - Source: `Your connection to this website uses weak encryption and is not private.`
    - Suggest: `"privada"`
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `{$popupCount ->} [other] { -brand-short-name } prevented this site from opening more than { $popupCount } pop-up windows and redirecting.`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `{$popupCount ->} [0] { -brand-short-name } prevented this site from redirecting. [1] { -brand-short-name } prevented this site from opening a pop-up window and redirecting. [other] { -brand-short-name } prevented this s…`
- `urlbar-result-search-with` — `browser/browser/browser.ftl` — urlbar-result-search-with (browser.ftl) — "Search with" → "Navegue con" (wrong verb + usted) → "Buscar con".
    - Source: `Search with { $engine }`
    - Suggest: `"Navegue con"`
- `main-context-menu-edit-bookmark-with-shortcut` — `browser/browser/browserContext.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `accesskey: m aria-label: Edit Bookmark… tooltiptext: Edit bookmark ({ $shortcut })`
    - Suggest: `Ajustes>`
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — firefox-relay-offer-legal-notice-control and siblings (firefoxRelay.ftl) — "iniciar sesión a tu cuenta" → "en tu cuenta".
    - Source: `By signing up and creating an email mask, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
    - Suggest: `"en tu cuenta".`
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `By signing up and creating an email mask, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
- `genai-onboarding-gemini-tooltip` — `browser/browser/genai.ftl` — genai-onboarding-gemini-tooltip (genai.ftl) — "Google Géminis" → "Google Gemini" (brand; correct in sibling strings).
    - Source: `title: Google Gemini`
    - Suggest: `"Google Gemini"`
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — genai-prompts-quiz (genai.ftl) — "Hazme un prueba" → "una prueba".
    - Source: `label: Quiz me value: Please quiz me on this selection. Ask me a variety of types of questions, for example multiple choice, true or false, and short answer. Wait for my response before moving on to the next question.`
    - Suggest: `"una prueba".`
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — genai-settings-chat-chatgpt-links (genai.ftl) — "chatGPT" → "ChatGPT".
    - Source: `By choosing ChatGPT, you agree to the OpenAI <a data-l10n-name="link1">Terms of Use</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
    - Suggest: `"ChatGPT".`
- `ipprotection-location-selection-callout-primary-button` — `browser/browser/ipProtection.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `Try it`
- `vpn-paused-alert-title` — `browser/browser/ipProtection.ftl` — vpn-paused-alert-title (ipProtection.ftl) — "VPN pausado" → "pausada".
    - Source: `VPN paused`
    - Suggest: `"pausada".`
- `import-close-source-browser` — `browser/browser/migration.ftl` — import-close-source-browser (migration.ftl) — queísmo: "asegúrate que… está cerrado" → "asegúrate de que… esté cerrado".
    - Source: `Please ensure the selected browser is closed before continuing.`
    - Suggest: `"asegúrate de que… esté cerrado".`
- `cfr-doorhanger-bookmark-fxa-body` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-bookmark-fxa-body (asrouter.ftl) — "Coemienza" → "Comienza".
    - Source: `Great find! Now don’t be left without this bookmark on your mobile devices. Get Started with a { -fxaccount-brand-name }.`
    - Suggest: `"Comienza".`
- `colorways-cfr-header-today` — `browser/browser/newtab/asrouter.ftl` — colorways-cfr-header-today (asrouter.ftl) — "Voces Independiente" → "Independientes".
    - Source: `Independent Voices colorways expire today`
    - Suggest: `"Independientes".`
- `firefoxview-cfr-primarybutton` — `browser/browser/newtab/asrouter.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `(value): Try it accesskey: T`
- `fxa-adoption-primary-button-label` — `browser/browser/newtab/asrouter.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `Sign up`
- `root-certificate-succession-infobar-march-message` — `browser/browser/newtab/asrouter.ftl` — root-certificate-succession-infobar-march-message (asrouter.ftl) — "14 de Marzo" → "marzo" (months lowercase).
    - Source: `<strong>Update to keep using { -brand-short-name } after March 14, 2025.</strong>`
    - Suggest: `"marzo"`
- `newtab-custom-wallpaper-cta` — `browser/browser/newtab/newtab.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `Try it`
- `newtab-pocket-thumbs-down-tooltip` — `browser/browser/newtab/newtab.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `title: Not for me`
- `newtab-section-menu-collapse-section` — `browser/browser/newtab/newtab.ftl` — newtab-section-menu-collapse-section (newtab.ftl) — "Collapse Section" → "Sección de colapso" → "Contraer sección".
    - Source: `Collapse Section`
    - Suggest: `"Sección de colapso" → "Contraer sección".`
- `newtab-weather-sponsored` — `browser/browser/newtab/newtab.ftl` — newtab-weather-sponsored (newtab.ftl) — "Sponsored" → "Patrocinador" (sponsor) → "Patrocinado".
    - Source: `{ $provider } ∙ Sponsored`
    - Suggest: `"Patrocinador"`
- `newtab-widget-timer-notification-break` — `browser/browser/newtab/newtab.ftl` — newtab-widget-timer-notification-break (newtab.ftl) — "Your break is over" → "Se acabaron tus vacaciones" (vacation) → "Se acabó tu descanso".
    - Source: `Your break is over. Ready to focus?`
    - Suggest: `"Se acabaron tus vacaciones"`
- `mr2022-onboarding-colorway-subtitle` — `browser/browser/newtab/onboarding.ftl` — mr2022-onboarding-colorway-subtitle (onboarding.ftl) — "Voces independientes puede" → "pueden".
    - Source: `Independent voices can change culture.`
    - Suggest: `"pueden".`
- `mr2022-onboarding-existing-set-default-only-subtitle` — `browser/browser/newtab/onboarding.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Use a browser that defends your privacy while you zip around the web. Our latest update is packed with things that you adore.`
- `mr2022-onboarding-gratitude-title` — `browser/browser/newtab/onboarding.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `You’re helping us build a better web`
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — Trailing stray characters: onboarding-genai-sidebar-subtitle (".—" after link).
    - Source: `Summarize web content, brainstorm ideas, draft messages — all as you browse. Choose from multiple providers. Switch anytime. <a data-l10n-name="learn-more">Learn more</a>`
- `media-count` — `browser/browser/pageInfo.ftl` — media-count (pageInfo.ftl) — "Count" (tally) → "Cuenta" (account) → "Cantidad".
    - Source: `label: Count`
    - Suggest: `"Cuenta"`
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `Delete Recent <strong>History</strong>`
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — panic-button-open-new-window (panicButton.ftl) — dropped "clean": "Open a new clean window".
    - Source: `Open a new clean Window`
- `places-forget-about-this-site-confirmation-msg` — `browser/browser/places.ftl` — places-forget-about-this-site-confirmation-msg (places.ftl) — "¿Estás seguro que…?" → "seguro de que".
    - Source: `This action will remove data related to { $hostOrBaseDomain } including history, cookies, cache and content preferences. Related bookmarks and passwords will not be removed. Are you sure you want to proceed?`
    - Suggest: `"seguro de que".`
- `places-load-js-data-url-error` — `browser/browser/placesPrompts.ftl` — places-load-js-data-url-error (placesPrompts.ftl) — dropped scheme colon from javascript:/data: (comment: do not translate).
    - Source: `For security reasons, “javascript:” or “data:” URLs cannot be loaded from the history window or sidebar.`
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — dropped "/8" from "127.0.0.1/8" (comment: do not translate).
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
    - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `label: { $locale } [{ $code }]`
- `more-from-moz-qr-code-box-firefox-mobile-title` — `browser/browser/preferences/moreFromMozilla.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `Download using your mobile device. Point your camera at the QR code. When a link appears, tap it.`
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `You can specify which websites have Enhanced Tracking Protection turned off. Type the exact address of the site you want to manage and then click Add Exception.`
- `content-blocking-warning-title-2` — `browser/browser/preferences/preferences.ftl` — content-blocking-warning-title-2 (preferences.ftl) — meaning inverted ("sites break the protection" instead of "sites may break with strict protection").
    - Source: `Some sites may break with strict tracking protection`
- `httpsonly-radio-disabled3` — `browser/browser/preferences/preferences.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `description: { -brand-short-name } may still upgrade some connections label: Don’t enable HTTPS-Only Mode`
- `performance-use-recommended-settings-checkbox` — `browser/browser/preferences/preferences.ftl` — performance-use-recommended-settings-checkbox (preferences.ftl) — "ajustes… recomendadas" → "recomendados".
    - Source: `accesskey: U label: Use recommended performance settings`
    - Suggest: `"recomendados".`
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — preferences-data-migration-description (preferences.ftl) — garbled "…datos de autocompletadomarcar en…".
    - Source: `Import bookmarks, passwords, history, and autofill data into { -brand-short-name }.`
- `security-privacy-issue-warning-extension-install` — `browser/browser/preferences/preferences.ftl` — security-privacy-issue-warning-extension-install (preferences.ftl) — "extensions" → "excepciones" → "extensiones".
    - Source: `description: Websites can install extensions to { -brand-short-name } without asking. label: Websites can install extensions`
    - Suggest: `"excepciones" → "extensiones".`
- `settings-translations-subpage-download-language-option` — `browser/browser/preferences/preferences.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
    - Source: `(value): { $language } ({ $size }MB) label: { $language } ({ $size }MB)`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
- `sync-engine-settings` — `browser/browser/preferences/preferences.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
    - Current: `has`
    - Source: `accesskey: s label: Settings tooltiptext: General, Privacy, and Security settings you’ve changed`
    - Suggest: `haz`
- `sync-signedin-login-failure` — `browser/browser/preferences/preferences.ftl` — sync-signedin-login-failure (preferences.ftl) — duplicated clause ("Inicia sesión para reconectar … Favor de iniciar la sesión para reconectar").
    - Source: `Please sign in to reconnect { $email }`
- `profile-card-edit-button` — `browser/browser/profiles.ftl` — profile-card-edit-button (profiles.ftl) — "Edit perfil" left in English → "Editar perfil".
    - Source: `aria-label: Edit profile title: Edit profile`
    - Suggest: `"Editar perfil".`
- `graph-private-window` — `browser/browser/protections.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `{ -brand-short-name } continues to  block trackers in Private Windows, but does not keep a record of what was blocked.`
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — protections-panel-cross-site-tracking-cookies (protectionsPanel.ftl) — "Ellos son creados" → "Son creadas" (cookies fem.).
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `"Son creadas"`
- `protections-panel-etp-toggle-off` — `browser/browser/protectionsPanel.ftl` — protections-panel-etp-toggle-off (aria, protectionsPanel.ftl) — "Desactiva" → "Desactivada".
    - Source: `aria-label: Enhanced Tracking Protection: Off for { $host } description: Off for this site label: Enhanced Tracking Protection`
    - Suggest: `"Desactivada".`
- `screenshots-private-window-error-title` — `browser/browser/screenshots.ftl` — screenshots-private-window-error-title (screenshots.ftl) — redundant "Firefox { -screenshots-brand-name }".
    - Source: `{ -screenshots-brand-name } is disabled in Private Browsing Mode`
- `opensearch-error-duplicate-desc` — `browser/browser/search.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `{ -brand-short-name } could not install the search plugin from “{ $location-url }” because an engine with the same name already exists.`
- _…and 52 more._

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
| Strings | 17,847 |
| Missing strings | 333 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
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

**333 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 73
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 23
- `toolkit/toolkit/about/aboutNetworking.ftl` — 20
- `toolkit/toolkit/about/aboutAddons.ftl` — 15
- `browser/browser/sharePanel.ftl` — 14
- `browser/browser/preferences/preferences.ftl` — 14
- `browser/browser/newtab/onboarding.ftl` — 13
- `toolkit/toolkit/neterror/netError.ftl` — 13
- `browser/browser/sidebar.ftl` — 12
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
| inverted marks | `open-question` 368, `open-exclamation` 85 | **open-question** |
| register | `informal` 1359, `formal` 237 | **informal** |

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
