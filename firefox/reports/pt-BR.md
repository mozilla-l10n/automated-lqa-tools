# Firefox l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `d411ef0407f1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `d411ef0407f1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,127 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

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
| Strings | 18,127 |
| Missing strings | 36 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Access keys not in their label | 3 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 28 |

### Completeness

**36 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 5
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `browser/browser/profiles.ftl` — 1
- `browser/browser/sidebar.ftl` — 1
- `toolkit/toolkit/about/aboutPDF.ftl` — 1
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 645, `curly-single` 131, `straight-double` 73 | **curly-double** |
| apostrophe | `typographic` 144, `straight` 108 | _mixed_ |
| ellipsis | `char` 454, `ascii` 3 | **char** |
| dash | `em` 78, `en` 1 | **em** |
| nbsp | `total` 13, `narrow` 11, `before-punctuation` 5, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 1729 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 28 strings** — 28 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `AutomaticAuth`, `CookieLaxForcedForBeta2`, `CookieRejectedNonRequiresSecure2`, `CookieSameSiteValueInvalid2`, `IneligibleResource`, `MalformedIntegrityHash`, `MathML_DeprecatedMathSizeValueWarning`, `MediaLoadUnsupportedMimeType`, `MediaLoadUnsupportedTypeAttribute`, `PrincipalWritingModePropagationWarning`, `SuperfluousAuth`, `UnsupportedHashAlg` …and 16 more

---

## 3. Open findings (570)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 16 |
| 2 | Wrong content (says something other than the English) | 190 |
| 3 | Degraded language (grammar, spelling, terminology) | 292 |
| 4 | Cosmetic (typography, spacing) | 72 |

### A. Functional, markup, variables & plurals

- `xpinstall-prompt-install` — `browser/browser/addonNotifications.ftl` — Access key `C` of `xpinstall-prompt-install` is not present in its label
  - Current: `C`
  - en-US: `F`
  - The label is “Avançar para a instalação”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `firefox-relay-offer-legal-notice` — `browser/browser/browser.ftl` — stray space inside the link text: …Aviso de privacidade </label> → …Aviso de privacidade</label>
- `firefox-relay-offer-legal-notice-1` — `browser/browser/browser.ftl` — broken closing tag. Current: …>Aviso de privacidade</label label>. → Suggest: …>Aviso de privacidade</label>.
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — same broken tag: </label label> → </label>
- `firefoxview-history-context-forget-site` — `browser/browser/firefoxView.ftl` — Access key `F` of `firefoxview-history-context-forget-site` is not present in its label
  - Current: `F`
  - The label is “Esquecer este site…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `newtab-widget-lists-completed-list` — `browser/browser/newtab/newtab.ftl` — the parentheses of the en-US format are dropped, leaving a bare number. Current: Tarefas concluídas { $number } → Suggest: Concluídas ({ $number })
  - Current: `Tarefas concluídas { $number }`
  - en-US: `Concluídas ({ $number })`
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — trailing space inside the link text: >Apple App Store </a> → >Apple App Store</a>
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — stray > character left in the text: …Aviso de privacidade</a> >.<br><br> → remove the >
  - en-US: `>`
- `perftools-menu-more-actions-copy-for-startup` — `devtools/client/perftools.ftl` — contains two U+200B zero-width spaces ("variáveis ​​de ambiente"). Only invisible-character occurrence in the tree; remove them.
- `inactive-css-no-size-containment-fix` — `devtools/client/tooltips.ftl` — inactive-css-no-size-containment-fix, inactive-css-no-size-containment-fix-1 — devtools/client/tooltips.ftl — stray space captured inside the CSS-keyword element: <strong>inline-table </strong> → <strong>inline-table</strong>
- `inactive-css-no-size-containment-fix-1` — `devtools/client/tooltips.ftl` — inactive-css-no-size-containment-fix, inactive-css-no-size-containment-fix-1 — devtools/client/tooltips.ftl — stray space captured inside the CSS-keyword element: <strong>inline-table </strong> → <strong>inline-table</strong>
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — missing space renders as "GleanDicionário". Current: <a …>{ -glean-brand-name }Dicionário</a> → Suggest: <a …>Dicionário do { -glean-brand-name }</a>
- `about-glean-adhoc-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-adhoc-explanation, about-glean-adhoc-explanation2 — toolkit/toolkit/about/aboutGlean.ftl — the <i>ad hoc</i> emphasis from en-US is dropped (translated as "mais específicos"). Low impact; restore the italics if the wording is revised.
- `about-glean-adhoc-explanation2` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-adhoc-explanation, about-glean-adhoc-explanation2 — toolkit/toolkit/about/aboutGlean.ftl — the <i>ad hoc</i> emphasis from en-US is dropped (translated as "mais específicos"). Low impact; restore the italics if the wording is revised.
- `about-logging-log-tutorial` — `toolkit/toolkit/about/aboutLogging.ftl` — trailing space inside the link text: >Log de HTTP </a> → >Log de HTTP</a>
- `wizard-macos-button-back` — `toolkit/toolkit/global/wizard.ftl` — Access key `B` of `wizard-macos-button-back` is not present in its label
  - Current: `B`
  - en-US: `F`
  - The label is “Voltar”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-vulnerable-alert-text2` — `browser/browser/aboutLogins.ftl` — en-US hedges ("was likely in a data breach"); pt-BR asserts it and shifts the subject to "um site". Suggest: …usada em outra conta que provavelmente foi afetada por um vazamento de dados.
- `pocket-panel-saved-removed-updated` — `browser/browser/aboutPocket.ftl` — "from Saves" dropped, making it identical to pocket-panel-saved-page-removed. Suggest: Página removida do que você salvou
  - en-US: `Página removida do que você salvou`
- `about-private-browsing-focus-promo-cta` — `browser/browser/aboutPrivateBrowsing.ftl` — en-US "Download". Current: Instale o { -focus-brand-name } → Suggest: Baixe o { -focus-brand-name }
  - Current: `Instale o { -focus-brand-name }`
  - en-US: `Baixe o { -focus-brand-name }`
- `about-unloads-column-processes` — `browser/browser/aboutUnloads.ftl` — Current: IDs dos processos encarregados pelo conteúdo da aba → Suggest: IDs dos processos que hospedam o conteúdo da aba
  - Current: `IDs dos processos encarregados pelo conteúdo da aba`
  - en-US: `IDs dos processos que hospedam o conteúdo da aba`
- `aiwindow-feedback-choose-any` — `browser/browser/aiWindow.ftl` — a multi-select prompt read as single choice. Current: Escolha qualquer um que se aplique → Suggest: Escolha todas as opções que se aplicam
  - Current: `Escolha qualquer um que se aplique`
  - en-US: `Escolha todas as opções que se aplicam`
- `aiwindow-firstrun-memories-title` — `browser/browser/aiWindow.ftl` — the comparative attaches to "helpful", not to the count. Current: Mais respostas úteis, nos seus termos → Suggest: Respostas mais úteis, nos seus termos
  - Current: `Mais respostas úteis, nos seus termos`
  - en-US: `Respostas mais úteis, nos seus termos`
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — the comment says "Read is past tense, to indicate that the action has been completed". Current: Ler o conteúdo da página → Suggest: Leu o conteúdo da página (the siblings action-log-searched-web, -checked-memories are past tense)
  - Current: `Ler o conteúdo da página`
  - en-US: `Leu o conteúdo da página`
- `extension-default-theme-description` — `browser/browser/appExtensionFields.ftl` — the missing preposition makes the noun list attach to "sistema operacional". Current: Seguir a configuração do sistema operacional de botões, menus e janelas. → Suggest: …do sistema operacional para botões, menus e janelas.
  - Current: `Seguir a configuração do sistema operacional de botões, menus e janelas.`
  - en-US: `…do sistema operacional para botões, menus e janelas.`
- `appmenuitem-banner-update-restart` — `browser/browser/appmenu.ftl` — hardcodes "Firefox" instead of the brand term, and replaces the em dash with a comma. Current: Atualização disponível, reiniciar o Firefox → Suggest: Atualização disponível — reiniciar agora
  - Current: `Atualização disponível, reiniciar o Firefox`
  - en-US: `Atualização disponível — reiniciar agora`
- `turn-on-scheduled-backups-description` — `browser/browser/backupSettings.ftl` — the second condition became a coordinated action. Current: Você pode restaurar se houver um problema ou usar um novo dispositivo. → Suggest: Você pode restaurá-la se houver um problema ou se você tiver um novo dispositivo.
  - Current: `Você pode restaurar se houver um problema ou usar um novo dispositivo.`
  - en-US: `Você pode restaurá-la se houver um problema ou se você tiver um novo dispositivo.`
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — the count is attached to the wrong noun; en-US counts pop-up windows. Suggest: …impediu que este site abrisse mais de { $popupCount } janelas, além de redirecionamentos.
- `crashed-subframe-title` — `browser/browser/contentCrash.ftl` — the comment requires this to match crashed-subframe-message minus markup; the wording and clause order differ.
  - en-US: `.title`
- `customkeys-nav-reload-skip-cache` — `browser/browser/customkeys.ftl` — en-US "Override Cache" = bypass. Current: Recarregar (substituir cache) → Suggest: Recarregar (ignorar cache)
  - Current: `Recarregar (substituir cache)`
  - en-US: `Recarregar (ignorar cache)`
- `firefox-relay-offer-why-to-use-relay-1` — `browser/browser/firefoxRelay.ftl` — the final clause turns "with your email hidden" into "stays safe"; the en-US string is identical to firefox-relay-and-fxa-popup-notification-first-sentence. Suggest aligning with that translation.
- `ip-protection-vpn-upgrade-link` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
  - en-US: `WiFi`
- `ipprotection-bandwidth-upgrade-text` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
  - en-US: `WiFi`
- `ipprotection-feature-introduction-description-captive-portal` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
  - en-US: `WiFi`
- `ipprotection-feature-introduction-title-captive-portal` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
  - en-US: `WiFi`
- `upgrade-vpn-description` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
  - en-US: `WiFi`
- `upgrade-vpn-title` — `browser/browser/ipProtection.ftl` — en-US "beyond the browser". Current: Tenha proteção extra, além da no navegador → Suggest: Tenha proteção extra, além do navegador
  - Current: `Tenha proteção extra, além da no navegador`
  - en-US: `Tenha proteção extra, além do navegador`
- `menu-bookmarks-all-tabs` — `browser/browser/menubar.ftl` — en-US "Bookmark All Tabs…"; without the object the action is undefined. Current: Adicionar todas as abas… → Suggest: Adicionar todas as abas aos favoritos…
  - Current: `Adicionar todas as abas…`
  - en-US: `Adicionar todas as abas aos favoritos…`
- `set-default-menu-message-split-layout-title` — `browser/browser/newtab/asrouter.ftl` — the [macos] variant ("Keep { -brand-short-name } at your fingertips") was translated identically to [other], losing the Dock-specific message. Suggest: Tenha o { -brand-short-name } sempre à mão
  - Current: `[macos]`
  - en-US: `[other]`
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — en-US "coffee shops". Current: aeroportos e restaurantes → Suggest: aeroportos e cafés
  - Current: `aeroportos e restaurantes`
  - en-US: `aeroportos e cafés`
- `newtab-appearance-explore-more-themes-button` — `browser/browser/newtab/newtab.ftl` — "Explore more themes" and "See more themes" (newtab-appearance-more-themes-button) both became Mais temas. Suggest: Explorar mais temas for the former.
  - en-US: `Mais temas`
- `newtab-clock-city-us-new-york` — `browser/browser/newtab/newtab.ftl` — newtab-clock-city-us-new-york (Nova Iorque) vs newtab-weather-static-city (Cidade de Nova York) — same city, two spellings in one file.
  - en-US: `Nova Iorque`
- `newtab-clock-city-us-washington-dc` — `browser/browser/newtab/newtab.ftl` — Current: Washington D.C. → Suggest: Washington, D.C.
  - Current: `Washington D.C.`
  - en-US: `Washington, D.C.`
- `newtab-section-follow-highlight-subtitle` — `browser/browser/newtab/newtab.ftl` — Current: Siga o que você se interessa para aparecer mais do que você gosta. → Suggest: Siga seus interesses para ver mais do que você gosta.
  - Current: `Siga o que você se interessa para aparecer mais do que você gosta.`
  - en-US: `Siga seus interesses para ver mais do que você gosta.`
- `newtab-sports-widget-delayed` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — two distinct match statuses both render as Adiado. Suggest: Atrasado for delayed, keep Adiado for postponed. Same collision in newtab-sports-widget-match-aria-label-upcoming-delayed vs -postponed.
  - en-US: `Adiado`
- `newtab-sports-widget-keep-tabs` — `browser/browser/newtab/newtab.ftl` — the dev comment explains "Keep tabs on" is an idiom for staying updated; it was translated with browser tabs. Current: Mantenha abas sobre a Copa do Mundo → Suggest: Fique por dentro da Copa do Mundo
  - Current: `Mantenha abas sobre a Copa do Mundo`
  - en-US: `Fique por dentro da Copa do Mundo`
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — "matches" = football matches. Current: Carregando mais ocorrências… → Suggest: Carregando mais jogos…
  - Current: `Carregando mais ocorrências…`
  - en-US: `Carregando mais jogos…`
- `newtab-sports-widget-message-day-in-play-title` — `browser/browser/newtab/newtab.ftl` — Current: Acompanhe os jogos diariamente com widgets do { -brand-product-name } → Suggest: Mantenha seu dia em jogo com os widgets do { -brand-product-name }
  - Current: `Acompanhe os jogos diariamente com widgets do { -brand-product-name }`
  - en-US: `Mantenha seu dia em jogo com os widgets do { -brand-product-name }`
- `newtab-sports-widget-postponed` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — two distinct match statuses both render as Adiado. Suggest: Atrasado for delayed, keep Adiado for postponed. Same collision in newtab-sports-widget-match-aria-label-upcoming-delayed vs -postponed.
  - en-US: `Adiado`
- `newtab-sports-widget-round-32` — `browser/browser/newtab/newtab.ftl` — newtab.ftl — Brazilian football terms. Current: Rodada de 16 / Rodada de 32 → Suggest: Oitavas de final / 16 avos de final (the file already uses "Quartas de final"/"Semifinais")
  - Current: `Rodada de 32`
  - en-US: `Oitavas de final`
- `newtab-sports-widget-team-name-label-bih` — `browser/browser/newtab/newtab.ftl` — Inconsistent with newtab.ftl: region-name-ba = Bósnia-Herzegovina vs newtab-sports-widget-team-name-label-bih = Bósnia e Herzegovina.
- `newtab-sports-widget-upcoming` — `browser/browser/newtab/newtab.ftl` — Current: Seguintes → Suggest: Próximos (matches newtab-sports-widget-menu-view-upcoming = "Ver próximos")
  - Current: `Seguintes`
  - en-US: `Próximos`
- `newtab-weather-static-city` — `browser/browser/newtab/newtab.ftl` — newtab-clock-city-us-new-york (Nova Iorque) vs newtab-weather-static-city (Cidade de Nova York) — same city, two spellings in one file.
  - en-US: `Nova Iorque`
- `create-backup-screen-1-subtitle` — `browser/browser/newtab/onboarding.ftl` — en-US "in 1–2 minutes". Current: em menos de 2 minutos → Suggest: em 1 a 2 minutos
  - Current: `em menos de 2 minutos`
  - en-US: `em 1 a 2 minutos`
- `mr1-onboarding-get-started-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — a button label rendered as a noun. Current: Introdução → Suggest: Começar
  - Current: `Introdução`
  - en-US: `Começar`
- `mr2022-onboarding-welcome-pin-header` — `browser/browser/newtab/onboarding.ftl` — Current: Abra-se uma internet incrível (ungrammatical) → Suggest: Descubra uma internet incrível (the dev comment explicitly allows "discover")
  - Current: `Abra-se uma internet incrível`
  - en-US: `Descubra uma internet incrível`
- `origin-controls-state-temporary-access` — `browser/browser/originControls.ftl` — en-US "for this visit" = for the duration of the visit. Current: dados desta visita → Suggest: dados nesta visita
  - Current: `dados desta visita`
  - en-US: `dados nesta visita`
- `policy-DisableDefaultBrowserAgent` — `browser/browser/policies/policies-descriptions.ftl` — modifier scope. Current: o agente padrão do navegador → Suggest: o agente de navegador padrão
  - Current: `o agente padrão do navegador`
  - en-US: `o agente de navegador padrão`
- `policy-DisableFirefoxScreenshots` — `browser/browser/policies/policies-descriptions.ftl` — the dev comment says "Firefox Screenshots is the name of the feature, and should not be translated". Current: Desativar o recurso de captura de tela do Firefox. → Suggest: Desativar o recurso Firefox Screenshots.
  - Current: `Desativar o recurso de captura de tela do Firefox.`
  - en-US: `Desativar o recurso Firefox Screenshots.`
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — the policy disables specific ciphers, not encryption. Current: Desativar criptografia. → Suggest: Desativar cifras.
  - Current: `Desativar criptografia.`
  - en-US: `Desativar cifras.`
- `policy-PostQuantumKeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — "key agreement" is acordo de chaves in policy-CNSA2KeyAgreementEnabled. Current: Ativar aceitação de chave pós-quantum para TLS. → Suggest: Ativar acordo de chaves pós-quântico para TLS.
  - Current: `Ativar aceitação de chave pós-quantum para TLS.`
  - en-US: `Ativar acordo de chaves pós-quântico para TLS.`
- `colors-text-and-background` — `browser/browser/preferences/colors.ftl` — group header for the two pickers below. Current: Cores padrão (= Default colors) → Suggest: Texto e fundo
  - Current: `Cores padrão`
  - en-US: `Texto e fundo`
- `connection-proxy-socks` — `browser/browser/preferences/connection.ftl` — "Host" is not "Domínio" (which is already used for Domain in permissions-doh-col). Current: Domínio SOCKS → Suggest: Servidor SOCKS
  - Current: `Domínio SOCKS`
  - en-US: `Servidor SOCKS`
- `autofill-address-country` — `browser/browser/preferences/formAutofill.ftl` — en-US distinguishes "Country or Region" from "Country" (autofill-address-country-only); both are País. Suggest: País ou região
  - en-US: `País`
- `fxa-qrcode-error-title` — `browser/browser/preferences/fxaPairDevice.ftl` — en-US "Pairing unsuccessful." Current: Conexão falhou. → Suggest: Falha no pareamento.
  - Current: `Conexão falhou.`
  - en-US: `Falha no pareamento.`
- `more-from-moz-mozilla-monitor-global-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Current: Receba alertas quando seus dados estiverem em vazamentos de dados. → Suggest: Receba alertas quando seus dados aparecerem em um vazamento.
  - Current: `Receba alertas quando seus dados estiverem em vazamentos de dados.`
  - en-US: `Receba alertas quando seus dados aparecerem em um vazamento.`
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — home-prefs-highlights-option-most-recent-download (.label) — preferences.ftl / newtab.ftl — en-US is singular. Current: Downloads mais recentes → Suggest: Download mais recente
  - Current: `Downloads mais recentes`
  - en-US: `Download mais recente`
- `performance-use-recommended-settings-desc` — `browser/browser/preferences/preferences.ftl` — contains a sentence that no longer exists in en-US: "Desmarque se quiser alterar o uso de aceleração de hardware." Suggest: drop it.
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — en-US "Manage what websites can access…". Current: Gerencie quais sites podem acessar, controlar ou acionar. → Suggest: Gerencie o que os sites podem acessar, controlar ou acionar.
  - Current: `Gerencie quais sites podem acessar, controlar ou acionar.`
  - en-US: `Gerencie o que os sites podem acessar, controlar ou acionar.`
- `preferences-ai-controls-tab-group-suggestions-control` — `browser/browser/preferences/preferences.ftl` — en-US "Get suggestions to name and organize your tabs." Current: Receber sugestões de nome e organizar suas abas. → Suggest: Receba sugestões para nomear e organizar suas abas.
  - Current: `Receber sugestões de nome e organizar suas abas.`
  - en-US: `Receba sugestões para nomear e organizar suas abas.`
- `referrals-section-header` — `browser/browser/preferences/preferences.ftl` — the object is dropped, leaving the sentence incomplete. Current: Convidar a usar o navegador que põe a privacidade em primeiro lugar. → Suggest: Convide alguém a escolher o navegador que põe a privacidade em primeiro lugar.
  - Current: `Convidar a usar o navegador que põe a privacidade em primeiro lugar.`
  - en-US: `Convide alguém a escolher o navegador que põe a privacidade em primeiro lugar.`
- `report-broken-site-panel-reason-choose` — `browser/browser/reportBrokenSite.ftl` — en-US "Choose reason". Current: Escolha → Suggest: Escolha um motivo
  - Current: `Escolha`
  - en-US: `Escolha um motivo`
- `existing-user-tou-message` — `browser/browser/termsofuse.ftl` — en-US "take a moment". Current: Dê uma pausa para revisar e aceitar. → Suggest: Reserve um momento para revisar e aceitar.
  - Current: `Dê uma pausa para revisar e aceitar.`
  - en-US: `Reserve um momento para revisar e aceitar.`
- `e10s.accessibilityNotice.jawsMessage` — `browser/chrome/browser/browser.properties` — e10s.accessibilityNotice.jawsMessage (browser.properties) — subject "A exibição" is feminine: foi desativado → foi desativada
  - Current: `foi desativado`
  - en-US: `foi desativada`
- `sidebar.moveToRight` — `browser/chrome/browser/browser.properties` — sidebar.moveToLeft, sidebar.moveToRight (browser.properties) — Mover painel para esquerda / para direita → para a esquerda / para a direita
  - Current: `para direita`
  - en-US: `para a esquerda`
- `permission.canvas.label` — `browser/chrome/browser/sitePermissions.properties` — permission.canvas.label (sitePermissions.properties) — "canvas" rendered as tela, colliding with permission.screen.label (Compartilhar a tela); browser.properties keeps "canvas". Current: Extrair dados da tela → Suggest: Extrair dados do canvas
  - Current: `Extrair dados da tela`
  - en-US: `Extrair dados do canvas`
- `permission.popup-only.label` — `browser/chrome/browser/sitePermissions.properties` — permission.popup-only.label, permission.popup.label, permission.popup-and-framebusting.label (sitePermissions.properties) — the pop-up qualifier is dropped, so the permission reads as any window/tab opening: Abrir janelas ou abas → Abrir janelas popup; Abertura de janelas e redirecionamento de terceiros → Janelas popup e redirecionamentos de terceiros
  - Current: `Abrir janelas ou abas`
  - en-US: `Abrir janelas popup`
- _…and 130 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-dialog-message, about-logins-confirm-remove-all-sync-dialog-message (all variants) — aboutLogins.ftl — restrictive relative with indefinite antecedent: quaisquer alertas de vazamento que aparecem aqui → que apareçam aqui (the newer …-message2/-message3 avoid the construction)
  - Current: `quaisquer alertas de vazamento que aparecem aqui`
  - en-US: `que apareçam aqui`
- `about-logins-confirm-remove-all-sync-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-sync-dialog-message ([other]) — aboutLogins.ftl — Serão removidas todos as contas → todas as contas
  - Current: `Serão removidas todos as contas`
  - en-US: `todas as contas`
- `active-policies-tab` — `browser/browser/aboutPolicies.ftl` — active-policies-tab, active-policies-tab-title (.title) — aboutPolicies.ftl — "diretivas" is plural: Ativa → Ativas
  - Current: `Ativa`
  - en-US: `Ativas`
- `active-policies-tab-title` — `browser/browser/aboutPolicies.ftl` — active-policies-tab, active-policies-tab-title (.title) — aboutPolicies.ftl — "diretivas" is plural: Ativa → Ativas
  - Current: `Ativa`
  - en-US: `Ativas`
- `about-private-browsing-nova-info-subheader` — `browser/browser/aboutPrivateBrowsing.ftl` — about-private-browsing-nova-info-subheader, -subheader2 — aboutPrivateBrowsing.ftl — mixed-gender subject "pesquisas e acessos" → masculine: serão excluídas → serão excluídos
  - en-US: `serão excluídas`
- `crashed-report-sent` — `browser/browser/aboutTabCrashed.ftl` — Relato do falha → Relato da falha
  - Current: `Relato do falha`
  - en-US: `Relato da falha`
- `about-unloads-no-unloadable-tab` — `browser/browser/aboutUnloads.ftl` — abas a ser descarregadas → abas a serem descarregadas
  - Current: `abas a ser descarregadas`
  - en-US: `abas a serem descarregadas`
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — addon-confirm-install-message, addon-confirm-install-unsigned-message, addon-confirm-install-some-unsigned-message, addon-install-error-file-access, addon-local-install-error-file-access — addonNotifications.ftl — missing definite article before the brand term: em { -brand-short-name } → no { -brand-short-name }; porque { -brand-short-name } não pode modificar → porque o { -brand-short-name } não…
  - Current: `em { -brand-short-name }`
  - en-US: `no { -brand-short-name }`
- `addon-confirm-install-unsigned-message` — `browser/browser/addonNotifications.ftl` — addon-confirm-install-message, addon-confirm-install-unsigned-message, addon-confirm-install-some-unsigned-message, addon-install-error-file-access, addon-local-install-error-file-access — addonNotifications.ftl — missing definite article before the brand term: em { -brand-short-name } → no { -brand-short-name }; porque { -brand-short-name } não pode modificar → porque o { -brand-short-name } não…
  - Current: `em { -brand-short-name }`
  - en-US: `no { -brand-short-name }`
- `addon-confirm-install-unsigned-message` — `browser/browser/addonNotifications.ftl` — extensão não-verificada / extensões não-verificadas → não verificada / não verificadas (addon-install-error-not-signed is already correct)
  - Current: `extensões não-verificadas`
  - en-US: `não verificada`
- `xpinstall-prompt-message` — `browser/browser/addonNotifications.ftl` — Tenha certeza se confia neste site → Tenha certeza de que confia neste site (the -unknown sibling is correct)
  - Current: `Tenha certeza se confia neste site`
  - en-US: `Tenha certeza de que confia neste site`
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — matches the paired option "Aprender com conversas": Aprender da navegação em → Aprender com a navegação em
  - Current: `Aprender da navegação em`
  - en-US: `Aprender com a navegação em`
- `smart-window-model-custom-name` — `browser/browser/aiFeatures.ftl` — aiFeatures.ftl — Examplo: → Exemplo: (2 instances)
  - Current: `Examplo:`
  - en-US: `Exemplo:`
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
  - en-US: `Elas tornam`
- `aiwindow-firstrun-title` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
  - en-US: `Elas tornam`
- `aiwindow-history-menu-settings` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
  - en-US: `Elas tornam`
- `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
  - en-US: `Elas tornam`
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
  - en-US: `Elas tornam`
- `action-log-searching-web-with-exa` — `browser/browser/aiWindowContent.ftl` — an in-progress action as infinitive: Pesquisar na web com <a…>Exa</a> → Pesquisando na web com <a…>Exa</a> (cf. action-log-searching-web)
- `appmenuitem-monitor-title2` — `browser/browser/appmenu.ftl` — Esteja à frente de roubo de identidade → Fique à frente do roubo de identidade
  - Current: `Esteja à frente de roubo de identidade`
  - en-US: `Fique à frente do roubo de identidade`
- `identity-description-active-loaded-insecure` — `browser/browser/browser.ftl` — identity-description-insecure, identity-description-active-loaded-insecure — browser.ftl — only the head noun pluralizes: cartões de créditos → cartões de crédito
  - Current: `cartões de créditos`
  - en-US: `cartões de crédito`
- `identity-description-insecure` — `browser/browser/browser.ftl` — identity-description-insecure, identity-description-active-loaded-insecure — browser.ftl — only the head noun pluralizes: cartões de créditos → cartões de crédito
  - Current: `cartões de créditos`
  - en-US: `cartões de crédito`
- `pointerlock-warning-no-domain` — `browser/browser/browser.ftl` — the sibling pointerlock-warning-domain uses the imperative: Pressionar Esc → Pressione Esc
  - Current: `Pressionar Esc`
  - en-US: `Pressione Esc`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — redirect-warning-with-popup-message ([other]) — browser.ftl — missing conjunction (the [1] variant has it): impediu redirecionamentos { $popupCount } aberturas de janelas → impediu redirecionamentos e { $popupCount } aberturas de janelas
  - Current: `impediu redirecionamentos { $popupCount } aberturas de janelas`
  - en-US: `impediu redirecionamentos e { $popupCount } aberturas de janelas`
- `trustpanel-etp-description-disabled` — `browser/browser/browser.ftl` — o máximo possivel → possível
  - Current: `o máximo possivel`
  - en-US: `possível`
- `urlbar-dismissal-acknowledgment-weather` — `browser/browser/browser.ftl` — urlbar-dismissal-acknowledgment-weather, urlbar-trending-dismissal-acknowledgment, urlbar-result-dismissal-acknowledgment-market, urlbar-result-dismissal-acknowledgment-all — browser.ftl — postposed plural subject: Não irá mais aparecer sugestões → Não irão mais aparecer sugestões; Não aparecerá mais pesquisas populares → Não aparecerão
  - Current: `Não irá mais aparecer sugestões`
  - en-US: `Não irão mais aparecer sugestões`
- `urlbar-result-dismissal-acknowledgment-market` — `browser/browser/browser.ftl` — urlbar-dismissal-acknowledgment-weather, urlbar-trending-dismissal-acknowledgment, urlbar-result-dismissal-acknowledgment-market, urlbar-result-dismissal-acknowledgment-all — browser.ftl — postposed plural subject: Não irá mais aparecer sugestões → Não irão mais aparecer sugestões; Não aparecerá mais pesquisas populares → Não aparecerão
  - Current: `Não irá mais aparecer sugestões`
  - en-US: `Não irão mais aparecer sugestões`
- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — missing space: Tente novamentemais tarde. → Tente novamente mais tarde.
  - Current: `Tente novamentemais tarde.`
  - en-US: `Tente novamente mais tarde.`
- `contextual-manager-export-passwords-dialog-message` — `browser/browser/contextual-manager.ftl` — recomendamos excluir, para que outros → recomendamos excluir o arquivo para que outras pessoas
  - Current: `recomendamos excluir, para que outros`
  - en-US: `recomendamos excluir o arquivo para que outras pessoas`
- `contextual-manager-passwords-remove-login-card-message` — `browser/browser/contextual-manager.ftl` — Isto não pode ser defeito. → desfeito
  - Current: `Isto não pode ser defeito.`
  - en-US: `desfeito`
- `customkeys-file-focus-search` — `browser/browser/customkeys.ftl` — duplicated article: Foco na a barra de pesquisa → Foco na barra de pesquisa
  - Current: `Foco na a barra de pesquisa`
  - en-US: `Foco na barra de pesquisa`
- `default-browser-guidance-notification-title` — `browser/browser/defaultBrowserNotification.ftl` — same file — stacked bare infinitives: Concluir definir o { -brand-short-name } como padrão → Conclua a definição do { -brand-short-name } como padrão
  - Current: `Concluir definir o { -brand-short-name } como padrão`
  - en-US: `Conclua a definição do { -brand-short-name } como padrão`
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — default-browser-prompt-message-pin, -pin-msix, -pin-mac — defaultBrowserNotification.ftl — missing object pronouns: torne seu navegador padrão e fixe na barra de tarefas → torne-o seu navegador padrão e fixe-o na barra de tarefas
  - Current: `torne seu navegador padrão e fixe na barra de tarefas`
  - en-US: `torne-o seu navegador padrão e fixe-o na barra de tarefas`
- `bookmark-overlay-keyword-caption-label-2` — `browser/browser/editBookmarkOverlay.ftl` — the sibling caption uses "Use": Usar uma única palavra-chave → Use uma única palavra-chave
  - Current: `Usar uma única palavra-chave`
  - en-US: `Use uma única palavra-chave`
- `webext-quarantine-confirmation-line-2` — `browser/browser/extensionsUI.ftl` — em sites com restrição pela { -vendor-short-name } → em sites restritos pela { -vendor-short-name }
  - Current: `em sites com restrição pela { -vendor-short-name }`
  - en-US: `em sites restritos pela { -vendor-short-name }`
- `firefoxview-closed-tabs-placeholder-body` — `browser/browser/firefoxView.ftl` — transitive verb without object: você pode recuperar aqui → você pode recuperá-la aqui
  - Current: `você pode recuperar aqui`
  - en-US: `você pode recuperá-la aqui`
- `firefoxview-tabpickup-password-locked-description` — `browser/browser/firefoxView.ftl` — dropped subject: precisa inserir → você precisa inserir
  - Current: `precisa inserir`
  - en-US: `você precisa inserir`
- `link-preview-generation-error-missing-data-v2` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `link-preview-key-points-disclaimer` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `link-preview-key-points-header` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `link-preview-optin-message` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `link-preview-settings-key-points` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `link-preview-setup-faster-next-time` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
  - Current: `Pontos chave`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — ipprotection-message-bandwidth-warning (.message), -mb (.message), ip-protection-bandwidth-warning-infobar-message-90, -90-mb — ipProtection.ftl — GB restante este mês → GB restantes este mês; Tem { $usageLeft } GB restante → Você tem { $usageLeft } GB restantes (the -75 sibling is correct)
  - Current: `GB restante este mês`
  - en-US: `GB restantes este mês`
- `cfr-doorhanger-doh-body` — `browser/browser/newtab/asrouter.ftl` — suas requisição de DNS → suas requisições de DNS
  - Current: `suas requisição de DNS`
  - en-US: `suas requisições de DNS`
- `mr2022-background-update-toast-text` — `browser/browser/newtab/asrouter.ftl` — anti-rastreamento → antirrastreamento
  - en-US: `antirrastreamento`
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — doubled preposition: bloqueia em média de mais de 3.000 rastreadores → bloqueia em média mais de 3.000 rastreadores (the july-jam-body sibling is correct)
  - Current: `bloqueia em média de mais de 3.000 rastreadores`
  - en-US: `bloqueia em média mais de 3.000 rastreadores`
- `newtab-download-mobile-highlight-image` — `browser/browser/newtab/newtab.ftl` — more-from-moz-qr-code-firefox-mobile-img (.alt) and newtab-download-mobile-highlight-image (.aria-label) — moreFromMozilla.ftl / newtab.ftl — o { -brand-product-name } de dispositivos móveis → o { -brand-product-name } para dispositivos móveis
  - Current: `o { -brand-product-name } de dispositivos móveis`
  - en-US: `o { -brand-product-name } para dispositivos móveis`
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — mais grandes histórias através da web → mais grandes histórias de toda a web (the generic variant uses "na web")
  - Current: `mais grandes histórias através da web`
  - en-US: `mais grandes histórias de toda a web`
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — "confiar" requires "em": para quem você confia → para as pessoas em quem você confia
  - Current: `para quem você confia`
  - en-US: `para as pessoas em quem você confia`
- `newtab-section-toast-block` — `browser/browser/newtab/newtab.ftl` — Não aparecerá mais histórias → Não aparecerão mais histórias
  - Current: `Não aparecerá mais histórias`
  - en-US: `Não aparecerão mais histórias`
- `newtab-sports-widget-message-wallpapers-semifinals-title` — `browser/browser/newtab/newtab.ftl` — semi-finais → semifinais (the file's own newtab-sports-widget-semi-finals uses "Semifinais")
  - en-US: `semifinais`
- `newtab-topsites-url-validation` — `browser/browser/newtab/newtab.ftl` — É necessário uma URL válida → É necessária uma URL válida
  - Current: `É necessário uma URL válida`
  - en-US: `É necessária uma URL válida`
- `newtab-wallpaper-beach-at-sunrise` — `browser/browser/newtab/newtab.ftl` — duplicated word: Praia ao ao nascer do sol → Praia ao nascer do sol
  - Current: `Praia ao ao nascer do sol`
  - en-US: `Praia ao nascer do sol`
- `newtab-wallpaper-blue-flowers` — `browser/browser/newtab/newtab.ftl` — the "a + infinitive" progressive is European Portuguese: flores de pétalas azuis a desabrochar → flores de pétalas azuis desabrochando
  - Current: `flores de pétalas azuis a desabrochar`
  - en-US: `flores de pétalas azuis desabrochando`
- `newtab-wallpaper-dark-color` — `browser/browser/newtab/newtab.ftl` — newtab-wallpaper-light-color, newtab-wallpaper-dark-color — newtab.ftl — colors must agree with "Formas": Formas azul, rosa e amarelo / Formas vermelho e azul → Formas em tons de azul, rosa e amarelo / Formas em tons de vermelho e azul (matching the newtab-wallpaper-abstract- pattern)
  - Current: `Formas vermelho e azul`
  - en-US: `Formas em tons de azul, rosa e amarelo`
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — intervalos para estivar as pernas → esticar as pernas ("estivar" = to stow cargo)
  - Current: `intervalos para estivar as pernas`
  - en-US: `esticar as pernas`
- `fx-backup-confirmation-screen-easy-setup-item-text-3` — `browser/browser/newtab/onboarding.ftl` — métodos de pagamentos → métodos de pagamento
  - Current: `métodos de pagamentos`
  - en-US: `métodos de pagamento`
- `mr2022-onboarding-get-started-primary-subtitle` — `browser/browser/newtab/onboarding.ftl` — refers to "versão": Está repleto → Está repleta
  - Current: `Está repleto`
  - en-US: `Está repleta`
- `multi-profile-spotlight-body` — `browser/browser/newtab/onboarding.ftl` — Alterne facilmente entre navegação de trabalho ou diversão. → …entre navegação de trabalho e diversão.
  - Current: `Alterne facilmente entre navegação de trabalho ou diversão.`
  - en-US: `…entre navegação de trabalho e diversão.`
- _…and 107 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `about-logins-list-item-breach-icon` — `browser/browser/aboutLogins.ftl` — "Site vazado" (about-logins-list-item-breach-icon.title) reads as though the site leaked → Site com vazamento de dados (matching about-logins-list-section-breach)
  - en-US: `Site com vazamento de dados`
- `about-logins-list-section-breach` — `browser/browser/aboutLogins.ftl` — "Site vazado" (about-logins-list-item-breach-icon.title) reads as though the site leaked → Site com vazamento de dados (matching about-logins-list-section-breach)
  - en-US: `Site com vazamento de dados`
- `login-item-timeline-action-created` — `browser/browser/aboutLogins.ftl` — the three timeline labels are parallel participles (Atualizada, Usada) except this one: Criação → Criada
  - Current: `Criação`
  - en-US: `Criada`
- `about-private-browsing-search-placeholder` — `browser/browser/aboutPrivateBrowsing.ftl` — "Search the web": Pesquisar na web vs Pesquisar na internet — adjacent strings about-private-browsing-search-placeholder/-search-btn.title and newtab-search-box-input/newtab-search-box-text
  - Current: `Pesquisar na web`
  - en-US: `Pesquisar na internet`
- `crashed-request-auto-submit-title` — `browser/browser/aboutTabCrashed.ftl` — "Report"/"Relatar": crashed-request-auto-submit-title uses Informar; the rest of aboutTabCrashed.ftl uses Relatar
  - en-US: `Informar`
- `addon-domain-blocked-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `addon-install-domain-blocked-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `xpinstall-disabled` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `xpinstall-disabled-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `xpinstall-disabled-locked` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `xpinstall-prompt` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
- `aiwindow-feedback-include-page-content` — `browser/browser/aiWindow.ftl` — "chat": aiwindow-feedback-include-page-content leaves chat in English; the file uses conversa
  - en-US: `chat`
- `appmenu-tab-hide-controlled` — `browser/browser/appMenuNotifications.ftl` — "hidden tabs": abas ocultadas (appmenu-tab-hide-controlled) vs abas ocultas (all-tabs-menu-hidden-tabs)
  - Current: `abas ocultadas`
- `profiler-button-dropmarker` — `browser/browser/appmenu.ftl` — profiler-button-dropmarker (.label, .tooltiptext) — painel do profiler → painel do Analisador (as in profiler-popup-button-)
  - Current: `painel do profiler`
  - en-US: `painel do Analisador`
- `settings-data-backup-toggle-on2` — `browser/browser/backupSettings.ftl` — "backup": backup on the toggles (settings-data-backup-toggle-on2) vs cópia de segurança in the modals (turn-on-scheduled-backups-header, -confirm-button, -encryption-label, enable-backup-encryption-header) and windows-10-eos-global-infobar-primary-button
  - Current: `backup`
- `identity-etsi` — `browser/browser/browser.ftl` — Regulamento (EU) 2024/1183 → Regulamento (UE) 2024/1183 (União Europeia)
- `urlbar-placeholder-search-mode-other-bookmarks` — `browser/browser/browser.ftl` — "search terms": urlbar-placeholder-search-mode-other-bookmarks (.placeholder) uses busca, its four siblings use pesquisa
  - en-US: `.placeholder`
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, -body — chave (= key/password) for a keyboard key → tecla (customkeys-conflict-confirm-body is correct)
  - Current: `chave`
  - en-US: `tecla`
- `customkeys-dev-profiler-capture` — `browser/browser/customkeys.ftl` — um profile de desempenho → um perfil de desempenho; customkeys-dev-debugger — Debugger de JavaScript → Depurador de JavaScript
  - Current: `um profile de desempenho`
  - en-US: `um perfil de desempenho`
- `bookmark-overlay-keyword-2` — `browser/browser/editBookmarkOverlay.ftl` — bookmark-overlay-keyword-2 (.value) — the field is labelled Atalho while its own caption calls it "palavra-chave" → Palavra-chave
  - Current: `Atalho`
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — "AI chatbot": robô de conversa (genai-onboarding-description, sidebar-customization-callout-1-subtitle) vs chatbot de inteligência artificial everywhere else — including the next sentence of genai-onboarding-description itself
  - Current: `robô de conversa`
- `firefoxview-syncedtabs-adddevice-primarybutton` — `browser/browser/firefoxView.ftl` — para celular → para dispositivos móveis (as in the two sibling promos)
  - Current: `para celular`
  - en-US: `para dispositivos móveis`
- `firefoxview-tabpickup-header` — `browser/browser/firefoxView.ftl` — "tab pickup": Escolha de abas (firefoxview-tabpickup-header) vs coleta de abas (continuous-onboarding-firefox-view-tab-pickup-title) vs sincronização de abas (callout-firefox-view-tab-pickup-title)
  - Current: `Escolha de abas`
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — "sidebar": genai-chatbot-summarize-footer-generic-subtitle uses barra lateral; every other string uses painel lateral
  - en-US: `barra lateral`
- `genai-input-ask-provider` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
  - Current: `Consultar`
- `genai-menu-ask-provider` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
  - Current: `Consultar`
- `genai-onboarding-description` — `browser/browser/genai.ftl` — "AI chatbot": robô de conversa (genai-onboarding-description, sidebar-customization-callout-1-subtitle) vs chatbot de inteligência artificial everywhere else — including the next sentence of genai-onboarding-description itself
  - Current: `robô de conversa`
- `genai-shortcut-button` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
  - Current: `Consultar`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body (asrouter.ftl) and mr2022-onboarding-get-started-primary-subtitle (onboarding.ftl) address the user as vocês (plural) while the rest of the tree uses singular você
- `windows-10-eos-sync-callout-privacy-screen-1-title` — `browser/browser/newtab/asrouter.ftl` — bloqueia mineração de criptomoedas → bloqueia mineradores de criptomoedas (cryptominers are agents; preferences.ftl uses "mineradores de criptomoedas")
  - Current: `bloqueia mineração de criptomoedas`
  - en-US: `bloqueia mineradores de criptomoedas`
- `newtab-menu-dismiss` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
  - en-US: `Dispensar`
- `newtab-search-box-input` — `browser/browser/newtab/newtab.ftl` — "Search the web": Pesquisar na web vs Pesquisar na internet — adjacent strings about-private-browsing-search-placeholder/-search-btn.title and newtab-search-box-input/newtab-search-box-text
  - Current: `Pesquisar na web`
  - en-US: `Pesquisar na internet`
- `newtab-section-unfollow-button` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
  - en-US: `Dispensar`
- `newtab-sports-widget-follow-teams-title` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
  - en-US: `Dispensar`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle tells the user to select "Sincronizar com dispositivos móveis" but the button reads "Sincronização com dispositivos móveis"
- `mr2022-onboarding-get-started-primary-subtitle` — `browser/browser/newtab/onboarding.ftl` — july-jam-body (asrouter.ftl) and mr2022-onboarding-get-started-primary-subtitle (onboarding.ftl) address the user as vocês (plural) while the rest of the tree uses singular você
- `onboarding-live-language-skip-button-label` — `browser/browser/newtab/onboarding.ftl` — Ignorar → Pular (used by the three other "Skip" strings)
  - Current: `Ignorar`
  - en-US: `Pular`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — o único principal navegador → o único grande navegador (as in welcome-back-spotlight-subtitle)
  - Current: `o único principal navegador`
  - en-US: `o único grande navegador`
- `sync-to-mobile-button-label` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle tells the user to select "Sincronizar com dispositivos móveis" but the button reads "Sincronização com dispositivos móveis"
- `security-view-identity-verifier` — `browser/browser/pageInfo.ftl` — "Verified by": Homologado por: (security-view-identity-verifier.value, pageInfo.ftl) vs Verificado por: (identity-verifier-label, browser.ftl)
  - Current: `Homologado por:`
- `places-sortby-name` — `browser/browser/places.ftl` — "Sort by name": Ordenar pelo nome (places-sortby-name) vs Ordenar por nome (places-view-sortby-name)
  - Current: `Ordenar pelo nome`
- `policy-Extensions` — `browser/browser/policies/policies-descriptions.ftl` — the comment says the keys may be translated as verbs: "Bloqueado" → “Bloquear”
  - Current: `"Bloqueado"`
  - en-US: `“Bloquear”`
- `appearance-browser-icon-unlocked` — `browser/browser/preferences/browserIcon.ftl` — appearance-browser-icon-unlocked (.message) — "bonus icons" is ícones de bônus here but ícones extras de raposas in appearance-browser-icon-requirement
  - en-US: `.message`
- `containers-dialog` — `browser/browser/preferences/containers.ftl` — containers-dialog (.buttonlabelaccept) — "Done" is Concluído here and Pronto in containers-panel-create-button
  - en-US: `.buttonlabelaccept`
- `autofill-address-prefecture` — `browser/browser/preferences/formAutofill.ftl` — Província collides with autofill-address-province → Prefeitura for the Japanese prefecture field
  - en-US: `Prefeitura`
- `browser-languages-error` — `browser/browser/preferences/languages.ftl` — browser-languages-error and browser-language-install-error (.message) — à Internet capitalized; the rest of the tree uses lowercase internet
- `languages-customize-select-language` — `browser/browser/preferences/languages.ftl` — languages-customize-select-language (.placeholder) — um idioma a adicionar vs um idioma para adicionar in browser-languages-select-language
  - en-US: `.placeholder`
- `permissions-disable-etp` — `browser/browser/preferences/permissions.ftl` — certmgr-add-exception (Adicionar exceção…) vs permissions-disable-etp (Adicionar exceção)
  - en-US: `Adicionar exceção…`
- `applications-use-os-default` — `browser/browser/preferences/preferences.ftl` — applications-use-os-default (.label, all three PLATFORM variants) — aplicação appears only here; the whole scope uses aplicativo. Same pt-PT term in safeb-blocked-harmful-page-error-desc-override/-no-override and policy-AppAutoUpdate/policy-RequestedLocales
  - en-US: `.label`
- `browser-language-install-error` — `browser/browser/preferences/preferences.ftl` — browser-languages-error and browser-language-install-error (.message) — à Internet capitalized; the rest of the tree uses lowercase internet
- `forms-primary-pw-fips-title` — `browser/browser/preferences/preferences.ftl` — forms-primary-pw-fips-title (O FIPS exige) vs pp-change2empty-in-fips-mode (O modo FIPS exige)
  - en-US: `O FIPS exige`
- `preferences-ai-controls-block-confirmation-description` — `browser/browser/preferences/preferences.ftl` — melhorias → aprimoramentos de inteligência artificial (as in the rest of the section)
  - Current: `melhorias`
  - en-US: `aprimoramentos de inteligência artificial`
- `search-suggestions-cant-show` — `browser/browser/preferences/preferences.ftl` — search-suggestions-cant-show, search-suggestions-cant-show-2 (.message) — barra de endereço (singular); ~20 other strings use barra de endereços
- `search-suggestions-cant-show-2` — `browser/browser/preferences/preferences.ftl` — search-suggestions-cant-show, search-suggestions-cant-show-2 (.message) — barra de endereço (singular); ~20 other strings use barra de endereços
- `settings-translations-subpage-download-progress` — `browser/browser/preferences/preferences.ftl` — Transferência em andamento… → Download em andamento… (the file uses "Download"/"Baixar" throughout)
  - Current: `Transferência em andamento…`
  - en-US: `Download em andamento…`
- `edit-profile-page-avatar-header-2` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
- `folder-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
- `palette-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
- `picture-avatar` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
- `picture-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
- _…and 65 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `about-logins-import-report-added2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-added2, -modified2, -no-change2 — aboutLogins.ftl — the details spans start lowercase, unlike the identical non-2 variants and en-US
  - en-US: `-modified2`
- `restore-page-problem-desc` — `browser/browser/aboutSessionRestore.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `crashed-multiple-offer-help-message` — `browser/browser/aboutTabCrashed.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `crashed-single-offer-help-message` — `browser/browser/aboutTabCrashed.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `bookmarks-tools-toolbar-visibility-menuitem` — `browser/browser/browser.ftl` — the [true] variant is Ocultar Barra de Favoritos while [other] is sentence case
  - en-US: `.label`
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `quickactions-cmd-clearhistory` — `browser/browser/browser.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
  - en-US: `-show-msg`
- `quickactions-cmd-private` — `browser/browser/browser.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
  - en-US: `-show-msg`
- `main-context-menu-pdfjs-save-page` — `browser/browser/browserContext.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
  - en-US: `.label`
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — Comma where a period belongs: contextual-manager-passwords-no-passwords-message (contextual-manager.ftl) — são criptografadas, Estamos atentos → criptografadas. Estamos atentos
  - Current: `são criptografadas, Estamos atentos`
  - en-US: `criptografadas. Estamos atentos`
- `pin-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — escolha 'Fixar aba'
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — da Mistral AI . → da Mistral AI.
  - Current: `da Mistral AI .`
  - en-US: `da Mistral AI.`
- `ipprotection-connection-status-blocked-error-title-1` — `browser/browser/ipProtection.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `ipprotection-feature-introduction-link-text-captive-portal-1` — `browser/browser/ipProtection.ftl` — Final period dropped: ipprotection-feature-introduction-link-text-captive-portal-1 (ipProtection.ftl), policy-GenerativeAI (policies-descriptions.ftl)
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — Comma splice: ipprotection-site-settings-callout-subtitle (ipProtection.ftl) — em um site específico, isso será lembrado → …e isso será lembrado; about-logins-confirm-export-dialog-message (aboutLogins.ftl) — also drops the consecutive "so" and the object pronoun → …, portanto qualquer pessoa … poderá vê-las.
  - Current: `em um site específico, isso será lembrado`
  - en-US: `…e isso será lembrado`
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Ocultar Outros → Ocultar outros
  - Current: `Ocultar Outros`
  - en-US: `Ocultar outros`
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — a pasta “Safari“ → “Safari” (the other quotes in the same string are correct; note en-US also has this defect in this string)
  - Current: `a pasta “Safari“`
  - en-US: `“Safari”`
- `migration-list-payment-methods-label` — `browser/browser/migrationWizard.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
  - en-US: `-show-msg`
- `windows-10-eos-callout-addons-title` — `browser/browser/newtab/asrouter.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `newtab-discovery-empty-section-topstories-loading` — `browser/browser/newtab/newtab.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
  - en-US: `.label`
- `newtab-report-ads-reason-seen-it-too-many-times` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `newtab-wallpaper-sky-with-pink-clouds` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `smartwindow-sidebar-auto-open-callout-accepted-subtitle` — `browser/browser/newtab/onboarding.ftl` — uses U+02DD (˝) instead of quotes: Use ˝Fazer uma pergunta˝ → Use “Fazer uma pergunta”
  - Current: `Use ˝Fazer uma pergunta˝`
  - en-US: `Use “Fazer uma pergunta”`
- `tab-groups-onboarding-feature-callout-title` — `browser/browser/newtab/onboarding.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `page-info-frame` — `browser/browser/pageInfo.ftl` — the separator was dropped entirely: Informações do frame { $website } → Informações do frame — { $website }
  - Current: `Informações do frame { $website }`
  - en-US: `Informações do frame — { $website }`
- `page-info-page` — `browser/browser/pageInfo.ftl` — Informações da página - { $website } → —
  - Current: `Informações da página - { $website }`
  - en-US: `—`
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — Final period dropped: ipprotection-feature-introduction-link-text-captive-portal-1 (ipProtection.ftl), policy-GenerativeAI (policies-descriptions.ftl)
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — serial comma before "e" is not pt-BR usage: 127.0.0.1/8, e ::1 → 127.0.0.1/8 e ::1
- `autofill-card-expires-year` — `browser/browser/preferences/formAutofill.ftl` — autofill-card-expires-month, autofill-card-expires-year — preferences/formAutofill.ftl — Mês de Expiração / Ano de Expiração → sentence case (the -2 variants are correct)
  - Current: `Ano de Expiração`
  - en-US: `-2`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — { $locale } [{ $code }] → single space
  - Current: `{ $locale } [{ $code }]`
  - en-US: `single space`
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `addons-button-label` — `browser/browser/preferences/preferences.ftl` — addons-button-label2 (.label, .title), addons-button-label — preferences.ftl — Extensões e Temas → Extensões e temas
  - Current: `Extensões e Temas`
  - en-US: `Extensões e temas`
- `addons-button-label2` — `browser/browser/preferences/preferences.ftl` — addons-button-label2 (.label, .title), addons-button-label — preferences.ftl — Extensões e Temas → Extensões e temas
  - Current: `Extensões e Temas`
  - en-US: `Extensões e temas`
- `home-homepage-custom-url` — `browser/browser/preferences/preferences.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
  - en-US: `.label`
- `security-privacy-issue-warning-third-party-cookies` — `browser/browser/preferences/preferences.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
  - en-US: `.aria-label`
- `update-setting-write-failure-message2` — `browser/browser/preferences/preferences.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `tabbrowser-container-tab-title` — `browser/browser/tabbrowser.ftl` — { $title } - { $containerName } → —
  - Current: `{ $title } - { $containerName }`
  - en-US: `—`
- `tabbrowser-tab-label-tab-split-view-right` — `browser/browser/tabbrowser.ftl` — , Exibição dividida à direita → lowercase (the -left pair is lowercase)
  - Current: `, Exibição dividida à direita`
  - en-US: `-left`
- `taskbar-tab-title-profile` — `browser/browser/taskbartabs.ftl` — - { -brand-full-name } → — { -brand-full-name }
  - Current: `- { -brand-full-name }`
  - en-US: `— { -brand-full-name }`
- `webrtc-allow-share-camera-and-microphone-with-file` — `browser/browser/webrtcIndicator.ftl` — sua câmera e microfone? (also missing the possessive: → sua câmera e seu microfone?)
  - Current: `sua câmera e microfone?`
  - en-US: `sua câmera e seu microfone?`
- `storage-add-button` — `devtools/client/storage.ftl` — storage-add-button (.title), storage-context-menu-add-item (.label) — devtools/client/storage.ftl — Adicionar Item → Adicionar item
  - Current: `Adicionar Item`
  - en-US: `Adicionar item`
- `storage-context-menu-add-item` — `devtools/client/storage.ftl` — storage-add-button (.title), storage-context-menu-add-item (.label) — devtools/client/storage.ftl — Adicionar Item → Adicionar item
  - Current: `Adicionar Item`
  - en-US: `Adicionar item`
- `toolbox-always-on-top-enabled2` — `devtools/client/toolbox.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `inactive-css-cue-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
  - Current: `Não há suporte para<strong>`
  - en-US: `para <strong>`
- `inactive-css-first-letter-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
  - Current: `Não há suporte para<strong>`
  - en-US: `para <strong>`
- `inactive-css-placeholder-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
  - Current: `Não há suporte para<strong>`
  - en-US: `para <strong>`
- `inactive-css-resize` — `devtools/client/tooltips.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `pageInfo_Privacy_None2` — `security/manager/chrome/pippki/pippki.properties` — explicit trailing not present in en-US
- `crashreporter-error-no-home-dir` — `toolkit/crashreporter/crashreporter.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
- `discopane-notice-recommendations` — `toolkit/toolkit/about/aboutAddons.ftl` — discopane-notice-recommendations, discopane-notice-recommendations2 (.message) — aboutAddons.ftl — trailing space before the line wrap
- `discopane-notice-recommendations2` — `toolkit/toolkit/about/aboutAddons.ftl` — discopane-notice-recommendations, discopane-notice-recommendations2 (.message) — aboutAddons.ftl — trailing space before the line wrap
- `about-processes-remote-sandbox-broker-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — remoto ({ $pid }) → single space
  - Current: `remoto ({ $pid })`
  - en-US: `single space`
- `a11y-instantiator` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
- `audio-backend` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
- `max-audio-channels` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
- `about-telemetry-current-data-sidebar` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
  - en-US: `-show-msg`
- _…and 12 more; see `state/` for the full list._

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (131)

- `about-logins-confirm-remove-all-sync-dialog-message` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-07
- `login-intro-instructions-fxa` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-07
- `addon-confirm-install-message` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-07
- `addon-install-error-file-access` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-07
- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-07
- `addon-local-install-error-file-access` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-07
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-07
- `all-tabs-menu-hidden-tabs` — `browser/browser/allTabsMenu.ftl` — fixed 2026-08-07
- `appmenu-fxa-header2` — `browser/browser/appmenu.ftl` — fixed 2026-08-07
- `enable-backup-encryption-header` — `browser/browser/backupSettings.ftl` — fixed 2026-08-07
- `turn-on-scheduled-backups-header` — `browser/browser/backupSettings.ftl` — fixed 2026-08-07
- `browser-main-private-window-title` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `identity-verifier-label` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `urlbar-dismissal-acknowledgment-weather` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `urlbar-result-dismissal-acknowledgment-all` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `urlbar-trending-dismissal-acknowledgment` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `urlbar-trending-dismissal-acknowledgment` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `main-context-menu-media-play-speed-slow-2` — `browser/browser/browserContext.ftl` — fixed 2026-08-07
- `main-context-menu-video-take-snapshot` — `browser/browser/browserContext.ftl` — fixed 2026-08-07
- `toolbar-button-fxaccount` — `browser/browser/browserContext.ftl` — fixed 2026-08-07
- `default-browser-guidance-notification-v2-body` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-08-07
- `downloads-blocked-download-detailed-info` — `browser/browser/downloads.ftl` — fixed 2026-08-07
- `downloads-error-generic` — `browser/browser/downloads.ftl` — fixed 2026-08-07
- `callout-firefox-view-tab-pickup-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `continuous-onboarding-firefox-view-tab-pickup-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `link-preview-onboarding-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `perplexity-callout-theme-1-subtitle-1` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `perplexity-callout-theme-2-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `firefoxview-closed-tabs-description2` — `browser/browser/firefoxView.ftl` — fixed 2026-08-07
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-menu-ask-provider-2` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-onboarding-copilot-learn` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `identity-credential-policy-description` — `browser/browser/identityCredentialNotification.ftl` — fixed 2026-08-07
- `ip-protection-bandwidth-warning-infobar-message-90` — `browser/browser/ipProtection.ftl` — fixed 2026-08-07
- `ipprotection-location-selection-callout-description-1` — `browser/browser/ipProtection.ftl` — fixed 2026-08-07
- `nova-early-access-infobar-primary-button` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-07
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-07
- `windows-10-eos-global-infobar-primary-button` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-07
- `home-prefs-firefox-home-disabled-notice` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
