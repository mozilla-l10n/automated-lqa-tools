# Firefox l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `5cbe42651962` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `f2e9b7fce093` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,843 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md)

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
| Strings | 17,843 |
| Missing strings | 337 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 142 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 131 |

### Completeness

**337 strings** are not translated yet, concentrated in:

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
| inverted marks | `open-question` 367, `open-exclamation` 84 | **open-question** |
| register | `informal` 1359, `formal` 237 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 142 strings** — 142 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
    - Affected: `addressbar-locbar-clipboard-option`, `addressbar-locbar-openpage-option`, `addressbar-locbar-quickactions-option`, `appmenu-addon-post-install-pin-toolbarbutton-checkbox`, `appmenu-help-more-troubleshooting-info`, `appmenu-help-not-deceptive`, `appmenu-homepage-controlled-changes`, `appmenu-new-tab-controlled-changes`, `appmenu-tab-hide-controlled`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2` …and 129 more
- **typography — 131 strings** — 131 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `AutomaticAuth`, `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CORSPreflightDidNotSucceed3`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolationWithURI`, `CompositorAnimationWarningTransformWithSyncGeometricAnimations`, `CookieRejectedByPermissionManager`, `CookieRejectedInvalidCharName`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed` …and 117 more

---

## 3. Open findings (132)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 9 |
| 2 | Wrong content (says something other than the English) | 44 |
| 3 | Degraded language (grammar, spelling, terminology) | 61 |
| 4 | Cosmetic (typography, spacing) | 18 |

### A. Functional, markup, variables & plurals

- `login-intro-instructions-fxa-settings` — `browser/browser/aboutLogins.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `Go to Settings > Sync > Turn on syncing… Select the Logins and passwords checkbox.`
    - Suggest: `Ajustes>`
- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — account-tabs-closed-remotely (accounts.ftl) — missing spaces around brand: { $closedCount }{ -brand-short-name } pestaña renders e.g. "1Firefox…".
    - Source: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab closed [other] { $closedCount } { -brand-short-name } tabs closed`
- `main-context-menu-edit-bookmark-with-shortcut` — `browser/browser/browserContext.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `accesskey: m aria-label: Edit Bookmark… tooltiptext: Edit bookmark ({ $shortcut })`
    - Suggest: `Ajustes>`
- `tab-context-close-n-tabs` — `browser/browser/tabContextMenu.ftl` — tab-context-close-n-tabs (tabContextMenu.ftl) — plural variants reversed: [one] reads "pestañas" (plural), [other] reads singular "pestaña" — visible bug for counts ≥2.
    - Source: `accesskey: C label: {$tabCount ->} [1] Close Tab [other] Close { $tabCount } Tabs`
- `tab-context-move-tab-to-new-group` — `browser/browser/tabbrowser.ftl` — tab-context-move-tab-to-new-group (tabbrowser.ftl) — stray backtick: Agregar pestaña `.
    - Source: `accesskey: G label: {$tabCount ->} [1] Add Tab to New Group [other] Add Tabs to New Group`
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — inverted <strong> tags: </strong>{ $property }<strong> → <strong>{ $property }</strong>.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it cannot be applied to internal table elements where <strong>border-collapse</strong> is set to <strong>collapse</strong> on the parent table element.`
- `about-logging-log-tutorial` — `toolkit/toolkit/about/aboutLogging.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `See <a data-l10n-name="logging">HTTP Logging</a> for instructions on how to use this tool.`
    - Suggest: `Ajustes>`
- `rights-webservices` — `toolkit/toolkit/about/aboutRights.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `{ -brand-full-name } uses web-based information services (“Services”) to provide some of the features provided for your use with this binary version of { -brand-short-name } under the terms described below. If you do no…`
    - Suggest: `Ajustes>`
- `fp-certerror-bad-domain-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
    - Source: `The site is set up to allow only secure connections, but there’s a problem with the site’s certificate. It’s possible that a bad actor is trying to impersonate the site. Sites use certificates issued by a certificate au…`
    - Suggest: `Ajustes>`

### B. Mistranslation, reversed meaning, wrong names & brand

- `urlbar-result-search-with` — `browser/browser/browser.ftl` — urlbar-result-search-with (browser.ftl) — "Search with" → "Navegue con" (wrong verb + usted) → "Buscar con".
    - Source: `Search with { $engine }`
    - Suggest: `"Navegue con"`
- `genai-onboarding-gemini-tooltip` — `browser/browser/genai.ftl` — genai-onboarding-gemini-tooltip (genai.ftl) — "Google Géminis" → "Google Gemini" (brand; correct in sibling strings).
    - Source: `title: Google Gemini`
    - Suggest: `"Google Gemini"`
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — genai-settings-chat-chatgpt-links (genai.ftl) — "chatGPT" → "ChatGPT".
    - Source: `By choosing ChatGPT, you agree to the OpenAI <a data-l10n-name="link1">Terms of Use</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
    - Suggest: `"ChatGPT".`
- `newtab-section-menu-collapse-section` — `browser/browser/newtab/newtab.ftl` — newtab-section-menu-collapse-section (newtab.ftl) — "Collapse Section" → "Sección de colapso" → "Contraer sección".
    - Source: `Collapse Section`
    - Suggest: `"Sección de colapso" → "Contraer sección".`
- `newtab-weather-sponsored` — `browser/browser/newtab/newtab.ftl` — newtab-weather-sponsored (newtab.ftl) — "Sponsored" → "Patrocinador" (sponsor) → "Patrocinado".
    - Source: `{ $provider } ∙ Sponsored`
    - Suggest: `"Patrocinador"`
- `newtab-widget-timer-notification-break` — `browser/browser/newtab/newtab.ftl` — newtab-widget-timer-notification-break (newtab.ftl) — "Your break is over" → "Se acabaron tus vacaciones" (vacation) → "Se acabó tu descanso".
    - Source: `Your break is over. Ready to focus?`
    - Suggest: `"Se acabaron tus vacaciones"`
- `media-count` — `browser/browser/pageInfo.ftl` — media-count (pageInfo.ftl) — "Count" (tally) → "Cuenta" (account) → "Cantidad".
    - Source: `label: Count`
    - Suggest: `"Cuenta"`
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — panic-button-open-new-window (panicButton.ftl) — dropped "clean": "Open a new clean window".
    - Source: `Open a new clean Window`
- `places-load-js-data-url-error` — `browser/browser/placesPrompts.ftl` — places-load-js-data-url-error (placesPrompts.ftl) — dropped scheme colon from javascript:/data: (comment: do not translate).
    - Source: `For security reasons, “javascript:” or “data:” URLs cannot be loaded from the history window or sidebar.`
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — dropped "/8" from "127.0.0.1/8" (comment: do not translate).
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
- `content-blocking-warning-title-2` — `browser/browser/preferences/preferences.ftl` — content-blocking-warning-title-2 (preferences.ftl) — meaning inverted ("sites break the protection" instead of "sites may break with strict protection").
    - Source: `Some sites may break with strict tracking protection`
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — preferences-data-migration-description (preferences.ftl) — garbled "…datos de autocompletadomarcar en…".
    - Source: `Import bookmarks, passwords, history, and autofill data into { -brand-short-name }.`
- `security-privacy-issue-warning-extension-install` — `browser/browser/preferences/preferences.ftl` — security-privacy-issue-warning-extension-install (preferences.ftl) — "extensions" → "excepciones" → "extensiones".
    - Source: `description: Websites can install extensions to { -brand-short-name } without asking. label: Websites can install extensions`
    - Suggest: `"excepciones" → "extensiones".`
- `sync-signedin-login-failure` — `browser/browser/preferences/preferences.ftl` — sync-signedin-login-failure (preferences.ftl) — duplicated clause ("Inicia sesión para reconectar … Favor de iniciar la sesión para reconectar").
    - Source: `Please sign in to reconnect { $email }`
- `profile-card-edit-button` — `browser/browser/profiles.ftl` — profile-card-edit-button (profiles.ftl) — "Edit perfil" left in English → "Editar perfil".
    - Source: `aria-label: Edit profile title: Edit profile`
    - Suggest: `"Editar perfil".`
- `screenshots-private-window-error-title` — `browser/browser/screenshots.ftl` — screenshots-private-window-error-title (screenshots.ftl) — redundant "Firefox { -screenshots-brand-name }".
    - Source: `{ -screenshots-brand-name } is disabled in Private Browsing Mode`
- `sidebar-menu-open-ai-chatbot-tooltip-generic` — `browser/browser/sidebar.ftl` — sidebar-menu-open-ai-chatbot-tooltip-generic (sidebar.ftl) — "Open AI chatbot" (verb) → "Chatbot de IA abierta" (state, wrong gender) → "Abrir el chatbot de IA".
    - Source: `Open AI chatbot ({ $shortcut })`
    - Suggest: `"Chatbot de IA abierta"`
- `sidebar-menu-open-tabs-label` — `browser/browser/sidebar.ftl` — sidebar-menu-open-tabs-label (sidebar.ftl) — "Open tabs" is a noun (per comment) → "Abrir pestañas" (imperative) → "Pestañas abiertas".
    - Source: `label: Open tabs`
    - Suggest: `"Abrir pestañas"`
- `text-recognition-modal-searching-title` — `browser/browser/textRecognition.ftl` — text-recognition-modal-searching-title (textRecognition.ftl) — reversed: "Buscando imagen para texto" → "Buscando texto en la imagen".
    - Source: `Searching image for text…`
    - Suggest: `"Buscando texto en la imagen".`
- `touchbar-fullscreen-exit` — `browser/browser/touchbar/touchbar.ftl` — touchbar-fullscreen-exit (touchbar.ftl) — "fullscreen" → "ventana completa" → "pantalla completa".
    - Source: `Exit Fullscreen`
    - Suggest: `"ventana completa" → "pantalla completa".`
- `webrtc-reason-for-no-permanent-allow-insecure` — `browser/browser/webrtcIndicator.ftl` — webrtc-reason-for-no-permanent-allow-insecure (webrtcIndicator.ftl) — "for this session" → "…por esta razón" (reason) → "durante esta sesión".
    - Source: `Your connection to this site is not secure. To protect you, { -brand-short-name } will only allow access for this session.`
    - Suggest: `"…por esta razón"`
- `add-exception-domain-mismatch-long` — `security/manager/security/certificates/certManager.ftl` — add-exception-domain-mismatch-long (certManager.ftl) — ungrammatical connector + wrong mood ("y lo cual significa que alguien intente…").
    - Source: `The certificate belongs to a different site, which could mean that someone is trying to impersonate this site.`
- `pippki-incorrect-pw` — `security/manager/security/pippki/pippki.ftl` — pippki-incorrect-pw (pippki.ftl) — "current password" → "contraseña principal" → "contraseña actual".
    - Source: `You did not enter the correct current password. Please try again.`
    - Suggest: `"contraseña principal" → "contraseña actual".`
- `about-webrtc-closed-peerconnection-disclosure-show-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "PeerConnections" translated to "conexiones de pares" in the hide-msg variant only (comment: keep PeerConnection).
    - Source: `Show Closed PeerConnections`
- `language-name-ab` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Abkhazian`
- `language-name-af` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Afrikaans`
- `language-name-fj` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Fijian`
- `language-name-hi` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Hindi`
- `language-name-hsb` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Upper Sorbian`
- `language-name-ky` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Kirghiz`
- `language-name-tg` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Tajik`
- `language-name-ty` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Tahitian`
- `language-name-uz` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Uzbek`
- `language-name-wen` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Sorbian`
- `language-name-yi` — `toolkit/toolkit/intl/languageNames.ftl` — language-name-af "Africano" → Afrikáans; language-name-ab "Abjasia" → Abjaso; language-name-hi "Hindú" → Hindi; language-name-hsb "Serbio superior" → Alto sorabo; language-name-wen "Serbio" → Sorabo; language-name-tg "Tayikistán" → Tayiko; language-name-uz "Uzbekistán" → Uzbeko; language-name-yi "Judío" → Yidis; language-name-fj "Fiji" → Fiyiano; language-name-ty "Tahití" → Tahitiano; language-na…
    - Source: `Yiddish`
- `region-name-ai` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
    - Source: `Anguilla`
- `region-name-az` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
    - Source: `Azerbaijan`
- `region-name-cv-2020` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
    - Source: `Cape Verde`
- `region-name-st` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
    - Source: `São Tomé and Príncipe`
- `region-name-vn` — `toolkit/toolkit/intl/regionNames.ftl` — region-name-ai "Anquilla" → Anguila; region-name-az "Azerbayán" → Azerbaiyán; region-name-cv-2020 "Cabo verde" → Cabo Verde; region-name-st "San Tome y Príncipe" → Santo Tomé y Príncipe; region-name-vn "Vietnám" → Vietnam.
    - Source: `Vietnam`

### C. Grammar, agreement & spelling

- `about-logins-os-auth-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-os-auth-dialog-message (aboutLogins.ftl) — "constraseñas" → "contraseñas".
    - Source: `{$sel_1 ->} [macos] change the settings for passwords [other] { -brand-short-name } is trying to change the settings for passwords. Use your device sign in to allow this.`
    - Suggest: `"contraseñas".`
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — ai-window-delete-all-memories-message (aiFeatures.ftl) — "recuerdos… será eliminados" → "serán".
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - Suggest: `"serán".`
- `smart-window-model-flexible` — `browser/browser/aiFeatures.ftl` — smart-window-model-flexible (aiFeatures.ftl) — "para la un uso general" (stray "la").
    - Source: `description: Model { $model } by { $ownerName } label: Flexible: Solid fit for most needs`
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
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — firefox-relay-offer-legal-notice-control and siblings (firefoxRelay.ftl) — "iniciar sesión a tu cuenta" → "en tu cuenta".
    - Source: `By signing up and creating an email mask, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
    - Suggest: `"en tu cuenta".`
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — genai-prompts-quiz (genai.ftl) — "Hazme un prueba" → "una prueba".
    - Source: `label: Quiz me value: Please quiz me on this selection. Ask me a variety of types of questions, for example multiple choice, true or false, and short answer. Wait for my response before moving on to the next question.`
    - Suggest: `"una prueba".`
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
- `mr2022-onboarding-colorway-subtitle` — `browser/browser/newtab/onboarding.ftl` — mr2022-onboarding-colorway-subtitle (onboarding.ftl) — "Voces independientes puede" → "pueden".
    - Source: `Independent voices can change culture.`
    - Suggest: `"pueden".`
- `mr2022-onboarding-existing-set-default-only-subtitle` — `browser/browser/newtab/onboarding.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Use a browser that defends your privacy while you zip around the web. Our latest update is packed with things that you adore.`
- `mr2022-onboarding-gratitude-title` — `browser/browser/newtab/onboarding.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `You’re helping us build a better web`
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `Delete Recent <strong>History</strong>`
- `places-forget-about-this-site-confirmation-msg` — `browser/browser/places.ftl` — places-forget-about-this-site-confirmation-msg (places.ftl) — "¿Estás seguro que…?" → "seguro de que".
    - Source: `This action will remove data related to { $hostOrBaseDomain } including history, cookies, cache and content preferences. Related bookmarks and passwords will not be removed. Are you sure you want to proceed?`
    - Suggest: `"seguro de que".`
- `more-from-moz-qr-code-box-firefox-mobile-title` — `browser/browser/preferences/moreFromMozilla.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `Download using your mobile device. Point your camera at the QR code. When a link appears, tap it.`
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `You can specify which websites have Enhanced Tracking Protection turned off. Type the exact address of the site you want to manage and then click Add Exception.`
- `httpsonly-radio-disabled3` — `browser/browser/preferences/preferences.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `description: { -brand-short-name } may still upgrade some connections label: Don’t enable HTTPS-Only Mode`
- `performance-use-recommended-settings-checkbox` — `browser/browser/preferences/preferences.ftl` — performance-use-recommended-settings-checkbox (preferences.ftl) — "ajustes… recomendadas" → "recomendados".
    - Source: `accesskey: U label: Use recommended performance settings`
    - Suggest: `"recomendados".`
- `sync-engine-settings` — `browser/browser/preferences/preferences.ftl` — has (haber) written as haz (hacer): smartwindow-assistant-error-budget-header (aiWindowContent.ftl), urlbar-midi-blocked (browser.ftl), content-sharing-modal-too-many-pages (contentSharing.ftl), the older about-logins-confirm-remove-all- strings, sync-engine-settings (.tooltiptext, "que haz modificado").
    - Current: `has`
    - Source: `accesskey: s label: Settings tooltiptext: General, Privacy, and Security settings you’ve changed`
    - Suggest: `haz`
- `graph-private-window` — `browser/browser/protections.ftl` — 3rd-person subject written 2nd-person: redirect-warning-with-popup-message / popup-warning-exceeded-with-redirect-message (browser.ftl, "{ -brand-short-name } has evitado" → "ha evitado"); httpsonly-radio-disabled3 (preferences.ftl); graph-private-window (protections.ftl, "sigue bloqueado" → "bloqueando"); panic-button-delete-history (panicButton.ftl, "Se borran el Historial" → "borra").
    - Source: `{ -brand-short-name } continues to  block trackers in Private Windows, but does not keep a record of what was blocked.`
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — protections-panel-cross-site-tracking-cookies (protectionsPanel.ftl) — "Ellos son creados" → "Son creadas" (cookies fem.).
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `"Son creadas"`
- `protections-panel-etp-toggle-off` — `browser/browser/protectionsPanel.ftl` — protections-panel-etp-toggle-off (aria, protectionsPanel.ftl) — "Desactiva" → "Desactivada".
    - Source: `aria-label: Enhanced Tracking Protection: Off for { $host } description: Off for this site label: Enhanced Tracking Protection`
    - Suggest: `"Desactivada".`
- `webrtc-allow-share-speaker-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — webrtc-allow-share-speaker-unsafe-delegation (webrtcIndicator.ftl) — "que { $origin } de acceso" → "dé acceso".
    - Source: `Allow { $origin } to give { $thirdParty } access to other speakers?`
    - Suggest: `"dé acceso".`
- `webrtc-indicator-menuitem-sharing-application-with` — `browser/browser/webrtcIndicator.ftl` — webrtc-indicator-menuitem-sharing-application-with (webrtcIndicator.ftl) — "un aplicación" → "una aplicación".
    - Source: `label: Sharing an Application with “{ $streamTitle }”`
    - Suggest: `"una aplicación".`
- `webrtc-share-screen-warning` — `browser/browser/webrtcIndicator.ftl` — webrtc-share-screen-warning (webrtcIndicator.ftl) — double "a": "permitir a sitios… a navegar" → "…navegar".
    - Source: `Only share screens with sites you trust. Sharing can allow deceptive sites to browse as you and steal your private data.`
    - Suggest: `"…navegar".`
- `accessibility-text-label-issue-figure` — `devtools/client/accessibility.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Figures with optional captions should be labeled. <a>Learn more</a>`
- `manifest-icon-img-title-no-sizes` — `devtools/client/application.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Unspecified size icon`
- `perftools-description-local-build` — `devtools/client/perftools.ftl` — Missing accent on pronouns / imperatives: newtab-pocket-thumbs-down-tooltip ("para mi" → "mí"), newtab-custom-wallpaper-cta ("Intentalo" → "Inténtalo") (newtab.ftl); perftools-description-local-build ("hiciste tu" → "tú", devtools/perftools.ftl); mr2022-onboarding-gratitude-title ("Estas ayudándonos" → "Estás", onboarding.ftl); firefoxview-cfr-primarybutton ("Intentalo"), fxa-adoption-primary-but…
    - Source: `If you’re profiling a build that you have compiled yourself, on this machine, please add your build’s objdir to the list below so that it can be used to look up symbol information.`
- `perftools-thread-jvm-pool` — `devtools/client/perftools.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `title: Threads created in an unnamed thread pool`
- `inactive-css-not-floated-fix` — `devtools/client/tooltips.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `Try adding the <strong>float</strong> property with a value other than <strong>none</strong>. { learn-more }`
- `inactive-css-not-grid-or-flex-item` — `devtools/client/tooltips.ftl` — Wrong word / duplicated word: perftools-thread-jvm-pool ("creador" → "creados", devtools/perftools.ftl); manifest-icon-img-title-no-sizes (see devtools terminology); accessibility-text-label-issue-figure ("más más", devtools/accessibility.ftl); inactive-css-not-grid-or-flex-item ("un un ítem", devtools/tooltips.ftl); permissions-exceptions-manage-etp-desc ("clic en en", preferences/permissions.ft…
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not a grid or flex item.`
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — cert-format-pkcs7-chain (certManager.ftl) — "(PKCX#7)" → "PKCS#7".
    - Source: `X.509 Certificate with chain (PKCS#7)`
    - Suggest: `"PKCS#7".`
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — unable-to-toggle-fips (deviceManager.ftl) — missing space "seguridad.Te" + "recomiend" → "recomendamos".
    - Source: `Unable to change the FIPS mode for the security device. It is recommended that you exit and restart this application.`
    - Suggest: `"recomendamos".`
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — Missing-accent typos (verb forms esta→está, etc.): update-applying / settings-update-applying ("actualizaciónes" → "actualización(es)"), update-failed ("ultima" → "última") (aboutDialog.ftl); ai-window-no-memories-learning-off (aiFeatures.ftl), link-preview-onboarding-description-long-press (genai.ftl), webext-perms-header-unsigned-with-perms (global/extensions.ftl), pdfjs-printing-not-supported…
    - Current: `esta`
    - Source: `With this feature enabled, { -brand-short-name } supports the JPEG XL (JXL) format. This is an enhanced image file format that supports lossless transition from traditional JPEG files. See <a data-l10n-name="bugzilla">b…`
    - Suggest: `está`
- `form-post-secure-to-insecure-warning-message` — `toolkit/toolkit/global/htmlForm.ftl` — Missing-accent typos (verb forms esta→está, etc.): update-applying / settings-update-applying ("actualizaciónes" → "actualización(es)"), update-failed ("ultima" → "última") (aboutDialog.ftl); ai-window-no-memories-learning-off (aiFeatures.ftl), link-preview-onboarding-description-long-press (genai.ftl), webext-perms-header-unsigned-with-perms (global/extensions.ftl), pdfjs-printing-not-supported…
    - Current: `esta`
    - Source: `The information you have entered on this page will be sent over an insecure connection and could be read by a third party.  Are you sure you want to send this information?`
    - Suggest: `está`
- `findbar-match-diacritics-status` — `toolkit/toolkit/main-window/findbar.ftl` — findbar-match-diacritics-status (findbar.ftl) — "diacrícitos" → "diacríticos".
    - Source: `value: (Matching diacritics)`
    - Suggest: `"diacríticos".`
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — webauthn-related-origin-create-header (webauthnDialog.ftl) — "una lleva de acceso" → "llave".
    - Source: `{ $origin } wants to create a passkey for { $rpId }.`
    - Suggest: `"llave".`

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
- `primary-password-required-by-policy` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
    - Source: `Your organization requires that you have a Primary Password set in order to save logins and passwords.`
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password: "contraseña primaria" vs "principal" vs "maestra" (pippki.ftl, fips-nonempty-primary-password-required, settings-pp-erased-ok, primary-password-required-by-policy).
    - Source: `You have deleted your Primary Password. Stored passwords and certificate private keys managed by { -brand-short-name } will not be protected.`

### E. Typography, punctuation & spacing

- `smartwindow-messages-document-title` — `browser/browser/aiWindowContent.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `{ -smart-window-brand-name } chat messages`
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `By signing up and creating an email mask, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — Trailing stray characters: onboarding-genai-sidebar-subtitle (".—" after link).
    - Source: `Summarize web content, brainstorm ideas, draft messages — all as you browse. Choose from multiple providers. Switch anytime. <a data-l10n-name="learn-more">Learn more</a>`
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
    - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `label: { $locale } [{ $code }]`
- `settings-translations-subpage-download-language-option` — `browser/browser/preferences/preferences.ftl` — Unbalanced parentheses: settings-translations-subpage-download-language-option (preferences.ftl, { $size }MB) missing "("), fxa-qrcode-pair-step2-signin (preferences/fxaPairDevice.ftl, closing ")" without "(").
    - Source: `(value): { $language } ({ $size }MB) label: { $language } ({ $size }MB)`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
- `opensearch-error-duplicate-desc` — `browser/browser/search.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `{ -brand-short-name } could not install the search plugin from “{ $location-url }” because an engine with the same name already exists.`
- `inactive-css-not-inline-or-tablecell` — `devtools/client/tooltips.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not an inline or table-cell element.`
- `about-about-note` — `toolkit/toolkit/about/aboutAbout.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `This is a list of “about” pages for your convenience.<br/> Some of them might be confusing. Some are for diagnostic purposes only.<br/> And some are omitted because they require query strings.`
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `To see a full view of all recorded metrics, you can use the { -profiler-brand-name }. First you must <a data-l10n-name="firefox-profiler-link">capture a performance profile</a>. Once you capture the profile, select <q>M…`
- `about-httpsonly-suggestion-box-www-text` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `There is a secure version of <em>www.{ $websiteUrl }</em>. You can visit this page instead of <em>{ $websiteUrl }</em>.`
- `rights-locationawarebrowsing` — `toolkit/toolkit/about/aboutRights.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `<strong>Location Aware Browsing: </strong>is always opt-in. No location information is ever sent without your permission. If you wish to disable the feature completely, follow these steps:`
- `rights-safebrowsing` — `toolkit/toolkit/about/aboutRights.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `<strong>SafeBrowsing: </strong>Disabling the Safe Browsing feature is not recommended as it may result in you going to unsafe sites. If you wish to disable the feature completely, follow these steps:`
- `remote-debugging-title` — `toolkit/toolkit/about/aboutSupport.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `Remote Debugging (Chromium Protocol)`
- `about-webauthn-ctap2-enroll-feedback-too-right` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `Sample was too right.`
- `about-webauthn-text-not-available` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Missing/incorrect terminal punctuation: about-httpsonly-suggestion-box-www-text (missing "."), about-webauthn-text-not-available (comma instead of "."), about-webauthn-ctap2-enroll-feedback-too-right (missing "."), about-glean-profiler-explanation (missing "."), remote-debugging-title (space before ")").
    - Source: `Not available on this platform.`
- `findbar-match-diacritics` — `toolkit/toolkit/main-window/findbar.ftl` — Double spaces: settings-translations-subpage-never-translate-sites-description (preferences.ftl), languages-code-format (preferences/languages.ftl), opensearch-error-duplicate-desc (search.ftl), firefox-relay-offer-legal-notice-control (firefoxRelay.ftl), smartwindow-messages-document-title (aiWindowContent.ftl), about-about-note (about/aboutAbout.ftl), findbar-match-diacritics (findbar.ftl), ina…
    - Source: `accesskey: i label: Match Diacritics tooltiptext: Distinguish between accented letters and their base letters (for example, when searching for “resume”, “résumé” will not be matched)`

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

### Resolved to date (93)

- `smartwindow-assistant-error-budget-header` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-21
- `urlbar-midi-blocked` — `browser/browser/browser.ftl` — fixed 2026-08-21
- `content-sharing-modal-too-many-pages` — `browser/browser/contentSharing.ftl` — fixed 2026-08-21
- `translations-panel-revisit-header` — `browser/browser/translations.ftl` — fixed 2026-08-21
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
