# Firefox l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `38d706ee4004` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `4aab78fe6cf4` |
| **Previous run** | 2026-08-31 @ `67b14d26eb36` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,213 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-BR: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 362 |
| Strings | 18,213 |
| Missing strings | 6 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 3 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 28 |

### Completeness

**6 strings** are not translated yet, concentrated in:

- `browser/browser/sharePanel.ftl` — 3
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/preferences/formAutofill.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 646, `curly-single` 131, `straight-double` 73 | **curly-double** |
| apostrophe | `typographic` 144, `straight` 108 | _mixed_ |
| ellipsis | `char` 455, `ascii` 3 | **char** |
| dash | `em` 78, `en` 1 | **em** |
| nbsp | `total` 13, `narrow` 11, `before-punctuation` 5, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 1733 | **informal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 28 strings** — 28 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `AutomaticAuth`, `CookieLaxForcedForBeta2`, `CookieRejectedNonRequiresSecure2`, `CookieSameSiteValueInvalid2`, `IneligibleResource`, `MalformedIntegrityHash`, `MathML_DeprecatedMathSizeValueWarning`, `MediaLoadUnsupportedMimeType`, `MediaLoadUnsupportedTypeAttribute`, `PrincipalWritingModePropagationWarning`, `SuperfluousAuth`, `UnsupportedHashAlg` …and 16 more

---

## 3. Open findings (563)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 12 |
| 2 | Wrong content (says something other than the English) | 193 |
| 3 | Degraded language (grammar, spelling, terminology) | 287 |
| 4 | Cosmetic (typography, spacing) | 71 |

### A. Functional, markup, variables & plurals

- `xpinstall-prompt-install` — `browser/browser/addonNotifications.ftl` — Access key `C` of `xpinstall-prompt-install` is not present in its label
    - Current: `C`
    - Source: `accesskey: C label: Continue to Installation`
    - Suggest: `F`
    - The label is “Avançar para a instalação”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `firefox-relay-offer-legal-notice` — `browser/browser/browser.ftl` — stray space inside the link text: …Aviso de privacidade </label> → …Aviso de privacidade</label>
    - Source: `By clicking “Use email mask”, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
- `newtab-widget-lists-completed-list` — `browser/browser/newtab/newtab.ftl` — the parentheses of the en-US format are dropped, leaving a bare number. Current: Tarefas concluídas { $number } → Suggest: Concluídas ({ $number })
    - Current: `Tarefas concluídas { $number }`
    - Source: `Completed ({ $number })`
    - Suggest: `Concluídas ({ $number })`
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — trailing space inside the link text: >Apple App Store </a> → >Apple App Store</a>
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — stray > character left in the text: …Aviso de privacidade</a> >.<br><br> → remove the >
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Suggest: `>`
- `perftools-menu-more-actions-copy-for-startup` — `devtools/client/perftools.ftl` — contains two U+200B zero-width spaces ("variáveis ​​de ambiente"). Only invisible-character occurrence in the tree; remove them.
    - Source: `Copy environment variables for startup profiling`
- `inactive-css-no-size-containment-fix` — `devtools/client/tooltips.ftl` — inactive-css-no-size-containment-fix, inactive-css-no-size-containment-fix-1 — devtools/client/tooltips.ftl — stray space captured inside the CSS-keyword element: <strong>inline-table </strong> → <strong>inline-table</strong>
    - Source: `Try setting its <strong>display</strong> property to something else than <strong>none</strong>, <strong>contents</strong>, <strong>table</strong>, or <strong>inline-table</strong> and make sure it’s not within a table o…`
- `inactive-css-no-size-containment-fix-1` — `devtools/client/tooltips.ftl` — inactive-css-no-size-containment-fix, inactive-css-no-size-containment-fix-1 — devtools/client/tooltips.ftl — stray space captured inside the CSS-keyword element: <strong>inline-table </strong> → <strong>inline-table</strong>
    - Source: `Try setting its <strong>display</strong> property to something else than <strong>none</strong>, <strong>contents</strong>, <strong>table</strong>, or <strong>inline-table</strong> and make sure it’s not within a table o…`
- `about-glean-adhoc-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-adhoc-explanation, about-glean-adhoc-explanation2 — toolkit/toolkit/about/aboutGlean.ftl — the <i>ad hoc</i> emphasis from en-US is dropped (translated as "mais específicos"). Low impact; restore the italics if the wording is revised.
    - Source: `For more <i>ad hoc</i> testing, you can also determine the current value of a particular piece of instrumentation by opening a devtools console here on <code>about:glean</code> and using the <code>testGetValue()</code>…`
- `about-glean-adhoc-explanation2` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-adhoc-explanation, about-glean-adhoc-explanation2 — toolkit/toolkit/about/aboutGlean.ftl — the <i>ad hoc</i> emphasis from en-US is dropped (translated as "mais específicos"). Low impact; restore the italics if the wording is revised.
    - Source: `For more <i>ad hoc</i> testing, you can also determine the current value of a particular piece of instrumentation by opening a devtools console here on <code>about:glean</code> and using the <code>testGetValue()</code>…`
- `about-logging-log-tutorial` — `toolkit/toolkit/about/aboutLogging.ftl` — trailing space inside the link text: >Log de HTTP </a> → >Log de HTTP</a>
    - Source: `See <a data-l10n-name="logging">HTTP Logging</a> for instructions on how to use this tool.`
- `wizard-macos-button-back` — `toolkit/toolkit/global/wizard.ftl` — Access key `B` of `wizard-macos-button-back` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Go Back`
    - Suggest: `F`
    - The label is “Voltar”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-vulnerable-alert-text2` — `browser/browser/aboutLogins.ftl` — en-US hedges ("was likely in a data breach"); pt-BR asserts it and shifts the subject to "um site". Suggest: …usada em outra conta que provavelmente foi afetada por um vazamento de dados.
    - Source: `This password has been used on another account that was likely in a data breach. Reusing credentials puts all your accounts at risk. Change this password.`
- `pocket-panel-saved-removed-updated` — `browser/browser/aboutPocket.ftl` — "from Saves" dropped, making it identical to pocket-panel-saved-page-removed. Suggest: Página removida do que você salvou
    - Source: `Page Removed from Saves`
    - Suggest: `Página removida do que você salvou`
- `about-private-browsing-focus-promo-cta` — `browser/browser/aboutPrivateBrowsing.ftl` — en-US "Download". Current: Instale o { -focus-brand-name } → Suggest: Baixe o { -focus-brand-name }
    - Current: `Instale o { -focus-brand-name }`
    - Source: `Download { -focus-brand-name }`
    - Suggest: `Baixe o { -focus-brand-name }`
- `about-unloads-column-processes` — `browser/browser/aboutUnloads.ftl` — Current: IDs dos processos encarregados pelo conteúdo da aba → Suggest: IDs dos processos que hospedam o conteúdo da aba
    - Current: `IDs dos processos encarregados pelo conteúdo da aba`
    - Source: `(value): Process IDs title: IDs of the processes hosting tab’s content`
    - Suggest: `IDs dos processos que hospedam o conteúdo da aba`
- `aiwindow-feedback-choose-any` — `browser/browser/aiWindow.ftl` — a multi-select prompt read as single choice. Current: Escolha qualquer um que se aplique → Suggest: Escolha todas as opções que se aplicam
    - Current: `Escolha qualquer um que se aplique`
    - Source: `Choose any that apply`
    - Suggest: `Escolha todas as opções que se aplicam`
- `aiwindow-firstrun-memories-title` — `browser/browser/aiWindow.ftl` — the comparative attaches to "helpful", not to the count. Current: Mais respostas úteis, nos seus termos → Suggest: Respostas mais úteis, nos seus termos
    - Current: `Mais respostas úteis, nos seus termos`
    - Source: `More helpful answers, on your terms`
    - Suggest: `Respostas mais úteis, nos seus termos`
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — the comment says "Read is past tense, to indicate that the action has been completed". Current: Ler o conteúdo da página → Suggest: Leu o conteúdo da página (the siblings action-log-searched-web, -checked-memories are past tense)
    - Current: `Ler o conteúdo da página`
    - Source: `Read page content`
    - Suggest: `Leu o conteúdo da página`
- `extension-default-theme-description` — `browser/browser/appExtensionFields.ftl` — the missing preposition makes the noun list attach to "sistema operacional". Current: Seguir a configuração do sistema operacional de botões, menus e janelas. → Suggest: …do sistema operacional para botões, menus e janelas.
    - Current: `Seguir a configuração do sistema operacional de botões, menus e janelas.`
    - Source: `Follow the operating system setting for buttons, menus, and windows.`
    - Suggest: `…do sistema operacional para botões, menus e janelas.`
- `appmenuitem-banner-update-restart` — `browser/browser/appmenu.ftl` — hardcodes "Firefox" instead of the brand term, and replaces the em dash with a comma. Current: Atualização disponível, reiniciar o Firefox → Suggest: Atualização disponível — reiniciar agora
    - Current: `Atualização disponível, reiniciar o Firefox`
    - Source: `label: Update available — restart now`
    - Suggest: `Atualização disponível — reiniciar agora`
- `turn-on-scheduled-backups-description` — `browser/browser/backupSettings.ftl` — the second condition became a coordinated action. Current: Você pode restaurar se houver um problema ou usar um novo dispositivo. → Suggest: Você pode restaurá-la se houver um problema ou se você tiver um novo dispositivo.
    - Current: `Você pode restaurar se houver um problema ou usar um novo dispositivo.`
    - Source: `{ -brand-short-name } will create a snapshot of your data every 24 hours. You can restore it if there’s a problem or you get a new device.`
    - Suggest: `Você pode restaurá-la se houver um problema ou se você tiver um novo dispositivo.`
- `crashed-subframe-title` — `browser/browser/contentCrash.ftl` — the comment requires this to match crashed-subframe-message minus markup; the wording and clause order differ.
    - Source: `title: Part of this page crashed. To let { -brand-product-name } know about this issue and get it fixed faster, please submit a report.`
    - Suggest: `.title`
- `customkeys-nav-reload-skip-cache` — `browser/browser/customkeys.ftl` — en-US "Override Cache" = bypass. Current: Recarregar (substituir cache) → Suggest: Recarregar (ignorar cache)
    - Current: `Recarregar (substituir cache)`
    - Source: `Reload (Override Cache)`
    - Suggest: `Recarregar (ignorar cache)`
- `firefox-relay-offer-why-to-use-relay-1` — `browser/browser/firefoxRelay.ftl` — the final clause turns "with your email hidden" into "stays safe"; the en-US string is identical to firefox-relay-and-fxa-popup-notification-first-sentence. Suggest aligning with that translation.
    - Source: `Protect your inbox from spam by using a free <label data-l10n-name="firefox-relay-learn-more-url">{ -relay-brand-name } email mask</label> to hide your real address. Emails from <label data-l10n-name="firefox-fxa-and-re…`
- `ip-protection-vpn-upgrade-link` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
    - Source: `description: Choose custom VPN locations and add protection to all your apps on up to five devices, whether you’re at home or on public Wi-Fi. label: Get even more protection outside { -brand-short-name } with { -mozill…`
    - Suggest: `WiFi`
- `ipprotection-bandwidth-upgrade-text` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
    - Source: `Choose a VPN location and add protection to all your apps on up to 5 devices, whether you’re at home or on public Wi-Fi.`
    - Suggest: `WiFi`
- `ipprotection-feature-introduction-description-captive-portal` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
    - Source: `Browse with extra protection by hiding your location, even on public Wi-Fi.`
    - Suggest: `WiFi`
- `ipprotection-feature-introduction-title-captive-portal` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
    - Source: `On public Wi-Fi? Try { -brand-product-name }’s built-in VPN.`
    - Suggest: `WiFi`
- `upgrade-vpn-description` — `browser/browser/ipProtection.ftl` — Wi-Fi → WiFi (9 strings; en-US uses the trademarked hyphenated form): ipprotection-feature-introduction-title-captive-portal, ipprotection-feature-introduction-description-captive-portal, upgrade-vpn-description, ipprotection-bandwidth-upgrade-text, ip-protection-vpn-upgrade-link (.description) — ipProtection.ftl; about-private-browsing-hide-activity-1 — aboutPrivateBrowsing.ftl; spotlight-public…
    - Source: `Choose your VPN location, use VPN for all of your apps and up to 5 devices, and stay secure on any network — at home or on public Wi-Fi.`
    - Suggest: `WiFi`
- `upgrade-vpn-title` — `browser/browser/ipProtection.ftl` — en-US "beyond the browser". Current: Tenha proteção extra, além da no navegador → Suggest: Tenha proteção extra, além do navegador
    - Current: `Tenha proteção extra, além da no navegador`
    - Source: `Get extra protection beyond the browser`
    - Suggest: `Tenha proteção extra, além do navegador`
- `menu-bookmarks-all-tabs` — `browser/browser/menubar.ftl` — en-US "Bookmark All Tabs…"; without the object the action is undefined. Current: Adicionar todas as abas… → Suggest: Adicionar todas as abas aos favoritos…
    - Current: `Adicionar todas as abas…`
    - Source: `label: Bookmark All Tabs…`
    - Suggest: `Adicionar todas as abas aos favoritos…`
- `set-default-menu-message-split-layout-title` — `browser/browser/newtab/asrouter.ftl` — the [macos] variant ("Keep { -brand-short-name } at your fingertips") was translated identically to [other], losing the Dock-specific message. Suggest: Tenha o { -brand-short-name } sempre à mão
    - Current: `[macos]`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } at your fingertips [other] Open all links with { -brand-short-name }`
    - Suggest: `[other]`
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — en-US "coffee shops". Current: aeroportos e restaurantes → Suggest: aeroportos e cafés
    - Current: `aeroportos e restaurantes`
    - Source: `To hide your location and browsing activity, consider a Virtual Private Network. It will help keep you protected when browsing in public places like airports and coffee shops.`
    - Suggest: `aeroportos e cafés`
- `newtab-appearance-explore-more-themes-button` — `browser/browser/newtab/newtab.ftl` — "Explore more themes" and "See more themes" (newtab-appearance-more-themes-button) both became Mais temas. Suggest: Explorar mais temas for the former.
    - Source: `Explore more themes`
    - Suggest: `Mais temas`
- `newtab-clock-city-us-new-york` — `browser/browser/newtab/newtab.ftl` — newtab-clock-city-us-new-york (Nova Iorque) vs newtab-weather-static-city (Cidade de Nova York) — same city, two spellings in one file.
    - Source: `New York`
    - Suggest: `Nova Iorque`
- `newtab-clock-city-us-washington-dc` — `browser/browser/newtab/newtab.ftl` — Current: Washington D.C. → Suggest: Washington, D.C.
    - Current: `Washington D.C.`
    - Source: `Washington, D.C.`
    - Suggest: `Washington, D.C.`
- `newtab-section-follow-highlight-subtitle` — `browser/browser/newtab/newtab.ftl` — Current: Siga o que você se interessa para aparecer mais do que você gosta. → Suggest: Siga seus interesses para ver mais do que você gosta.
    - Current: `Siga o que você se interessa para aparecer mais do que você gosta.`
    - Source: `Follow your interests to see more of what you like.`
    - Suggest: `Siga seus interesses para ver mais do que você gosta.`
- `newtab-sports-widget-delayed` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — two distinct match statuses both render as Adiado. Suggest: Atrasado for delayed, keep Adiado for postponed. Same collision in newtab-sports-widget-match-aria-label-upcoming-delayed vs -postponed.
    - Source: `Delayed`
    - Suggest: `Adiado`
- `newtab-sports-widget-keep-tabs` — `browser/browser/newtab/newtab.ftl` — the dev comment explains "Keep tabs on" is an idiom for staying updated; it was translated with browser tabs. Current: Mantenha abas sobre a Copa do Mundo → Suggest: Fique por dentro da Copa do Mundo
    - Current: `Mantenha abas sobre a Copa do Mundo`
    - Source: `Keep tabs on the World Cup`
    - Suggest: `Fique por dentro da Copa do Mundo`
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — "matches" = football matches. Current: Carregando mais ocorrências… → Suggest: Carregando mais jogos…
    - Current: `Carregando mais ocorrências…`
    - Source: `Loading more matches…`
    - Suggest: `Carregando mais jogos…`
- `newtab-sports-widget-message-day-in-play-title` — `browser/browser/newtab/newtab.ftl` — Current: Acompanhe os jogos diariamente com widgets do { -brand-product-name } → Suggest: Mantenha seu dia em jogo com os widgets do { -brand-product-name }
    - Current: `Acompanhe os jogos diariamente com widgets do { -brand-product-name }`
    - Source: `Keep your day in play with { -brand-product-name } widgets`
    - Suggest: `Mantenha seu dia em jogo com os widgets do { -brand-product-name }`
- `newtab-sports-widget-postponed` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — two distinct match statuses both render as Adiado. Suggest: Atrasado for delayed, keep Adiado for postponed. Same collision in newtab-sports-widget-match-aria-label-upcoming-delayed vs -postponed.
    - Source: `Postponed`
    - Suggest: `Adiado`
- `newtab-sports-widget-round-32` — `browser/browser/newtab/newtab.ftl` — newtab.ftl — Brazilian football terms. Current: Rodada de 16 / Rodada de 32 → Suggest: Oitavas de final / 16 avos de final (the file already uses "Quartas de final"/"Semifinais")
    - Current: `Rodada de 32`
    - Source: `Round of 32`
    - Suggest: `Oitavas de final`
- `newtab-sports-widget-team-name-label-bih` — `browser/browser/newtab/newtab.ftl` — Inconsistent with newtab.ftl: region-name-ba = Bósnia-Herzegovina vs newtab-sports-widget-team-name-label-bih = Bósnia e Herzegovina.
    - Source: `label: Bosnia and Herzegovina`
- `newtab-sports-widget-upcoming` — `browser/browser/newtab/newtab.ftl` — Current: Seguintes → Suggest: Próximos (matches newtab-sports-widget-menu-view-upcoming = "Ver próximos")
    - Current: `Seguintes`
    - Source: `Upcoming`
    - Suggest: `Próximos`
- `newtab-weather-static-city` — `browser/browser/newtab/newtab.ftl` — newtab-clock-city-us-new-york (Nova Iorque) vs newtab-weather-static-city (Cidade de Nova York) — same city, two spellings in one file.
    - Source: `New York City`
    - Suggest: `Nova Iorque`
- `create-backup-screen-1-subtitle` — `browser/browser/newtab/onboarding.ftl` — en-US "in 1–2 minutes". Current: em menos de 2 minutos → Suggest: em 1 a 2 minutos
    - Current: `em menos de 2 minutos`
    - Source: `Automatically protect your passwords, bookmarks, and more in 1–2 minutes.`
    - Suggest: `em 1 a 2 minutos`
- `mr1-onboarding-get-started-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — a button label rendered as a noun. Current: Introdução → Suggest: Começar
    - Current: `Introdução`
    - Source: `Get started`
    - Suggest: `Começar`
- `mr2022-onboarding-welcome-pin-header` — `browser/browser/newtab/onboarding.ftl` — Current: Abra-se uma internet incrível (ungrammatical) → Suggest: Descubra uma internet incrível (the dev comment explicitly allows "discover")
    - Current: `Abra-se uma internet incrível`
    - Source: `Open up an amazing internet`
    - Suggest: `Descubra uma internet incrível`
- `origin-controls-state-temporary-access` — `browser/browser/originControls.ftl` — en-US "for this visit" = for the duration of the visit. Current: dados desta visita → Suggest: dados nesta visita
    - Current: `dados desta visita`
    - Source: `Can read and change data for this visit`
    - Suggest: `dados nesta visita`
- `policy-DisableDefaultBrowserAgent` — `browser/browser/policies/policies-descriptions.ftl` — modifier scope. Current: o agente padrão do navegador → Suggest: o agente de navegador padrão
    - Current: `o agente padrão do navegador`
    - Source: `Prevent the default browser agent from taking any actions. Only applicable to Windows; other platforms don’t have the agent.`
    - Suggest: `o agente de navegador padrão`
- `policy-DisableFirefoxScreenshots` — `browser/browser/policies/policies-descriptions.ftl` — the dev comment says "Firefox Screenshots is the name of the feature, and should not be translated". Current: Desativar o recurso de captura de tela do Firefox. → Suggest: Desativar o recurso Firefox Screenshots.
    - Current: `Desativar o recurso de captura de tela do Firefox.`
    - Source: `Disable the Firefox Screenshots feature.`
    - Suggest: `Desativar o recurso Firefox Screenshots.`
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — the policy disables specific ciphers, not encryption. Current: Desativar criptografia. → Suggest: Desativar cifras.
    - Current: `Desativar criptografia.`
    - Source: `Disable ciphers.`
    - Suggest: `Desativar cifras.`
- `policy-PostQuantumKeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — "key agreement" is acordo de chaves in policy-CNSA2KeyAgreementEnabled. Current: Ativar aceitação de chave pós-quantum para TLS. → Suggest: Ativar acordo de chaves pós-quântico para TLS.
    - Current: `Ativar aceitação de chave pós-quantum para TLS.`
    - Source: `Enable post-quantum key agreement for TLS.`
    - Suggest: `Ativar acordo de chaves pós-quântico para TLS.`
- `colors-text-and-background` — `browser/browser/preferences/colors.ftl` — group header for the two pickers below. Current: Cores padrão (= Default colors) → Suggest: Texto e fundo
    - Current: `Cores padrão`
    - Source: `Text and Background`
    - Suggest: `Texto e fundo`
- `connection-proxy-socks` — `browser/browser/preferences/connection.ftl` — "Host" is not "Domínio" (which is already used for Domain in permissions-doh-col). Current: Domínio SOCKS → Suggest: Servidor SOCKS
    - Current: `Domínio SOCKS`
    - Source: `(value): SOCKS Host accesskey: C`
    - Suggest: `Servidor SOCKS`
- `autofill-address-country` — `browser/browser/preferences/formAutofill.ftl` — en-US distinguishes "Country or Region" from "Country" (autofill-address-country-only); both are País. Suggest: País ou região
    - Source: `Country or Region`
    - Suggest: `País`
- `fxa-qrcode-error-title` — `browser/browser/preferences/fxaPairDevice.ftl` — en-US "Pairing unsuccessful." Current: Conexão falhou. → Suggest: Falha no pareamento.
    - Current: `Conexão falhou.`
    - Source: `Pairing unsuccessful.`
    - Suggest: `Falha no pareamento.`
- `more-from-moz-mozilla-monitor-global-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Current: Receba alertas quando seus dados estiverem em vazamentos de dados. → Suggest: Receba alertas quando seus dados aparecerem em um vazamento.
    - Current: `Receba alertas quando seus dados estiverem em vazamentos de dados.`
    - Source: `Get alerts when your data has been in a breach.`
    - Suggest: `Receba alertas quando seus dados aparecerem em um vazamento.`
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — home-prefs-highlights-option-most-recent-download (.label) — preferences.ftl / newtab.ftl — en-US is singular. Current: Downloads mais recentes → Suggest: Download mais recente
    - Current: `Downloads mais recentes`
    - Source: `label: Most recent download`
    - Suggest: `Download mais recente`
- `performance-use-recommended-settings-desc` — `browser/browser/preferences/preferences.ftl` — contains a sentence that no longer exists in en-US: "Desmarque se quiser alterar o uso de aceleração de hardware." Suggest: drop it.
    - Source: `These settings are tailored to your computer’s hardware and operating system.`
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — en-US "Manage what websites can access…". Current: Gerencie quais sites podem acessar, controlar ou acionar. → Suggest: Gerencie o que os sites podem acessar, controlar ou acionar.
    - Current: `Gerencie quais sites podem acessar, controlar ou acionar.`
    - Source: `description: Manage what websites can access, control, or trigger. label: Permissions`
    - Suggest: `Gerencie o que os sites podem acessar, controlar ou acionar.`
- `preferences-ai-controls-tab-group-suggestions-control` — `browser/browser/preferences/preferences.ftl` — en-US "Get suggestions to name and organize your tabs." Current: Receber sugestões de nome e organizar suas abas. → Suggest: Receba sugestões para nomear e organizar suas abas.
    - Current: `Receber sugestões de nome e organizar suas abas.`
    - Source: `description: Get suggestions to name and organize your tabs. label: Tab group suggestions`
    - Suggest: `Receba sugestões para nomear e organizar suas abas.`
- `referrals-section-header` — `browser/browser/preferences/preferences.ftl` — the object is dropped, leaving the sentence incomplete. Current: Convidar a usar o navegador que põe a privacidade em primeiro lugar. → Suggest: Convide alguém a escolher o navegador que põe a privacidade em primeiro lugar.
    - Current: `Convidar a usar o navegador que põe a privacidade em primeiro lugar.`
    - Source: `description: Invite someone to choose the browser that puts privacy first. label: Share { -brand-short-name }`
    - Suggest: `Convide alguém a escolher o navegador que põe a privacidade em primeiro lugar.`
- `referrals-section-header2` — `browser/browser/preferences/preferences.ftl` — The description drops the object "someone" from "Invite someone to choose the browser…".
    - Current: `description: Convidar a usar o navegador que põe a privacidade em primeiro lugar.`
    - Source: `description: Invite someone to choose the browser that puts privacy first. label: Share { -brand-product-name }`
    - Suggest: `description: Convide alguém a escolher o navegador que põe a privacidade em primeiro lugar.`
    - en-US reads "Invite someone to choose the browser that puts privacy first"; the translation omits "someone" and replaces "choose" with "use", leaving an incomplete sentence without a direct object.
- `existing-user-tou-message` — `browser/browser/termsofuse.ftl` — en-US "take a moment". Current: Dê uma pausa para revisar e aceitar. → Suggest: Reserve um momento para revisar e aceitar.
    - Current: `Dê uma pausa para revisar e aceitar.`
    - Source: `<strong>Update</strong> We’ve introduced a { -brand-short-name } <a data-l10n-name="terms-of-use-link">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice-link">Privacy Notice</a>. Please take a moment to…`
    - Suggest: `Reserve um momento para revisar e aceitar.`
- `e10s.accessibilityNotice.jawsMessage` — `browser/chrome/browser/browser.properties` — e10s.accessibilityNotice.jawsMessage (browser.properties) — subject "A exibição" is feminine: foi desativado → foi desativada
    - Current: `foi desativado`
    - Source: `Display of tab content is disabled due to incompatibility between %S and your accessibility software. Please update your screen reader or switch to Firefox Extended Support Release.`
    - Suggest: `foi desativada`
- `sidebar.moveToRight` — `browser/chrome/browser/browser.properties` — sidebar.moveToLeft, sidebar.moveToRight (browser.properties) — Mover painel para esquerda / para direita → para a esquerda / para a direita
    - Current: `para direita`
    - Source: `Move Sidebar to Right`
    - Suggest: `para a esquerda`
- `permission.canvas.label` — `browser/chrome/browser/sitePermissions.properties` — permission.canvas.label (sitePermissions.properties) — "canvas" rendered as tela, colliding with permission.screen.label (Compartilhar a tela); browser.properties keeps "canvas". Current: Extrair dados da tela → Suggest: Extrair dados do canvas
    - Current: `Extrair dados da tela`
    - Source: `Extract canvas data`
    - Suggest: `Extrair dados do canvas`
- `permission.popup-only.label` — `browser/chrome/browser/sitePermissions.properties` — permission.popup-only.label, permission.popup.label, permission.popup-and-framebusting.label (sitePermissions.properties) — the pop-up qualifier is dropped, so the permission reads as any window/tab opening: Abrir janelas ou abas → Abrir janelas popup; Abertura de janelas e redirecionamento de terceiros → Janelas popup e redirecionamentos de terceiros
    - Current: `Abrir janelas ou abas`
    - Source: `Open pop-up windows`
    - Suggest: `Abrir janelas popup`
- `permission.popup.label` — `browser/chrome/browser/sitePermissions.properties` — permission.popup-only.label, permission.popup.label, permission.popup-and-framebusting.label (sitePermissions.properties) — the pop-up qualifier is dropped, so the permission reads as any window/tab opening: Abrir janelas ou abas → Abrir janelas popup; Abertura de janelas e redirecionamento de terceiros → Janelas popup e redirecionamentos de terceiros
    - Current: `Abrir janelas ou abas`
    - Source: `Open pop-up windows`
    - Suggest: `Abrir janelas popup`
- _…and 130 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-dialog-message, about-logins-confirm-remove-all-sync-dialog-message (all variants) — aboutLogins.ftl — restrictive relative with indefinite antecedent: quaisquer alertas de vazamento que aparecem aqui → que apareçam aqui (the newer …-message2/-message3 avoid the construction)
    - Current: `quaisquer alertas de vazamento que aparecem aqui`
    - Source: `{$count ->} [1] This will remove the login you’ve saved to { -brand-short-name } and any breach alerts that appear here. You won’t be able to undo this action. [other] This will remove the logins you’ve saved to { -bran…`
    - Suggest: `que apareçam aqui`
- `about-logins-confirm-remove-all-sync-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-sync-dialog-message ([other]) — aboutLogins.ftl — Serão removidas todos as contas → todas as contas
    - Current: `Serão removidas todos as contas`
    - Source: `{$count ->} [1] This will remove the login you’ve saved to { -brand-short-name } on all devices synced to your { -fxaccount-brand-name }. This will also remove breach alerts that appear here. You won’t be able to undo t…`
    - Suggest: `todas as contas`
- `active-policies-tab` — `browser/browser/aboutPolicies.ftl` — active-policies-tab, active-policies-tab-title (.title) — aboutPolicies.ftl — "diretivas" is plural: Ativa → Ativas
    - Current: `Ativa`
    - Source: `Active`
    - Suggest: `Ativas`
- `active-policies-tab-title` — `browser/browser/aboutPolicies.ftl` — active-policies-tab, active-policies-tab-title (.title) — aboutPolicies.ftl — "diretivas" is plural: Ativa → Ativas
    - Current: `Ativa`
    - Source: `title: Active`
    - Suggest: `Ativas`
- `crashed-report-sent` — `browser/browser/aboutTabCrashed.ftl` — Relato do falha → Relato da falha
    - Current: `Relato do falha`
    - Source: `Crash report already submitted; thank you for helping make { -brand-short-name } better!`
    - Suggest: `Relato da falha`
- `about-unloads-no-unloadable-tab` — `browser/browser/aboutUnloads.ftl` — abas a ser descarregadas → abas a serem descarregadas
    - Current: `abas a ser descarregadas`
    - Source: `There are no unloadable tabs.`
    - Suggest: `abas a serem descarregadas`
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — addon-confirm-install-message, addon-confirm-install-unsigned-message, addon-confirm-install-some-unsigned-message, addon-install-error-file-access, addon-local-install-error-file-access — addonNotifications.ftl — missing definite article before the brand term: em { -brand-short-name } → no { -brand-short-name }; porque { -brand-short-name } não pode modificar → porque o { -brand-short-name } não…
    - Current: `em { -brand-short-name }`
    - Source: `{$addonCount ->} [other] Caution: This site would like to install { $addonCount } add-ons in { -brand-short-name }, some of which are unverified. Proceed at your own risk.`
    - Suggest: `no { -brand-short-name }`
- `addon-confirm-install-unsigned-message` — `browser/browser/addonNotifications.ftl` — addon-confirm-install-message, addon-confirm-install-unsigned-message, addon-confirm-install-some-unsigned-message, addon-install-error-file-access, addon-local-install-error-file-access — addonNotifications.ftl — missing definite article before the brand term: em { -brand-short-name } → no { -brand-short-name }; porque { -brand-short-name } não pode modificar → porque o { -brand-short-name } não…
    - Current: `em { -brand-short-name }`
    - Source: `{$addonCount ->} [1] Caution: This site would like to install an unverified add-on in { -brand-short-name }. Proceed at your own risk. [other] Caution: This site would like to install { $addonCount } unverified add-ons…`
    - Suggest: `no { -brand-short-name }`
- `addon-confirm-install-unsigned-message` — `browser/browser/addonNotifications.ftl` — extensão não-verificada / extensões não-verificadas → não verificada / não verificadas (addon-install-error-not-signed is already correct)
    - Current: `extensões não-verificadas`
    - Source: `{$addonCount ->} [1] Caution: This site would like to install an unverified add-on in { -brand-short-name }. Proceed at your own risk. [other] Caution: This site would like to install { $addonCount } unverified add-ons…`
    - Suggest: `não verificada`
- `xpinstall-prompt-message` — `browser/browser/addonNotifications.ftl` — Tenha certeza se confia neste site → Tenha certeza de que confia neste site (the -unknown sibling is correct)
    - Current: `Tenha certeza se confia neste site`
    - Source: `You are attempting to install an add-on from { $host }. Make sure you trust this site before continuing.`
    - Suggest: `Tenha certeza de que confia neste site`
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — matches the paired option "Aprender com conversas": Aprender da navegação em → Aprender com a navegação em
    - Current: `Aprender da navegação em`
    - Source: `label: Learn from browsing in Classic and { -smart-window-brand-name }`
    - Suggest: `Aprender com a navegação em`
- `smart-window-model-custom-name` — `browser/browser/aiFeatures.ftl` — aiFeatures.ftl — Examplo: → Exemplo: (2 instances)
    - Current: `Examplo:`
    - Source: `label: Model name placeholder: Example: glm4`
    - Suggest: `Exemplo:`
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
    - Source: `{ -smart-window-brand-name } can learn from your chats, browsing, or both to create memories. They make answers more helpful over time.`
    - Suggest: `Elas tornam`
- `aiwindow-firstrun-title` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
    - Source: `Welcome to { -smart-window-brand-name }`
    - Suggest: `Elas tornam`
- `aiwindow-history-menu-settings` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
    - Source: `{ -smart-window-brand-name } settings`
    - Suggest: `Elas tornam`
- `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
    - Source: `label: New { -smart-window-brand-name } value: New { -smart-window-brand-name }`
    - Suggest: `Elas tornam`
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — -smart-window-brand-name gender — browser/browser/aiWindow.ftl — the term is feminine in pt-BR ("Janela inteligente"), but ~9 strings use masculine articles: aiwindow-firstrun-title, -model-subtitle, -memories-subtitle, -memories-relevance-body, -memories-choose-label, -memories-checkbox-chats, -memories-no-create, -default-title, aiwindow-history-menu-settings. appmenuitem-new-ai-window and fxa-…
    - Source: `Synced data will remain in your account. Open { -smart-window-brand-name } will switch to Classic Windows.`
    - Suggest: `Elas tornam`
- `action-log-searching-web-with-exa` — `browser/browser/aiWindowContent.ftl` — an in-progress action as infinitive: Pesquisar na web com <a…>Exa</a> → Pesquisando na web com <a…>Exa</a> (cf. action-log-searching-web)
    - Source: `Searching the web with <a data-l10n-name="exa-link">Exa</a>`
- `appmenuitem-monitor-title2` — `browser/browser/appmenu.ftl` — Esteja à frente de roubo de identidade → Fique à frente do roubo de identidade
    - Current: `Esteja à frente de roubo de identidade`
    - Source: `Stay Ahead of Identity Theft`
    - Suggest: `Fique à frente do roubo de identidade`
- `identity-description-active-loaded-insecure` — `browser/browser/browser.ftl` — identity-description-insecure, identity-description-active-loaded-insecure — browser.ftl — only the head noun pluralizes: cartões de créditos → cartões de crédito
    - Current: `cartões de créditos`
    - Source: `Information you share with this site could be viewed by others (like passwords, messages, credit cards, etc.).`
    - Suggest: `cartões de crédito`
- `identity-description-insecure` — `browser/browser/browser.ftl` — identity-description-insecure, identity-description-active-loaded-insecure — browser.ftl — only the head noun pluralizes: cartões de créditos → cartões de crédito
    - Current: `cartões de créditos`
    - Source: `Your connection to this site is not private. Information you submit could be viewed by others (like passwords, messages, credit cards, etc.).`
    - Suggest: `cartões de crédito`
- `pointerlock-warning-no-domain` — `browser/browser/browser.ftl` — the sibling pointerlock-warning-domain uses the imperative: Pressionar Esc → Pressione Esc
    - Current: `Pressionar Esc`
    - Source: `This document has control of your pointer. Press Esc to take back control.`
    - Suggest: `Pressione Esc`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — redirect-warning-with-popup-message ([other]) — browser.ftl — missing conjunction (the [1] variant has it): impediu redirecionamentos { $popupCount } aberturas de janelas → impediu redirecionamentos e { $popupCount } aberturas de janelas
    - Current: `impediu redirecionamentos { $popupCount } aberturas de janelas`
    - Source: `{$popupCount ->} [0] { -brand-short-name } prevented this site from redirecting. [1] { -brand-short-name } prevented this site from opening a pop-up window and redirecting. [other] { -brand-short-name } prevented this s…`
    - Suggest: `impediu redirecionamentos e { $popupCount } aberturas de janelas`
- `trustpanel-etp-description-disabled` — `browser/browser/browser.ftl` — o máximo possivel → possível
    - Current: `o máximo possivel`
    - Source: `{ -brand-product-name } thinks companies should follow you less. We block as many trackers as we can when you turn on protections.`
    - Suggest: `possível`
- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — missing space: Tente novamentemais tarde. → Tente novamente mais tarde.
    - Current: `Tente novamentemais tarde.`
    - Source: `heading: Something went wrong message: We couldn’t create your shared page this time. Try again later.`
    - Suggest: `Tente novamente mais tarde.`
- `contextual-manager-export-passwords-dialog-message` — `browser/browser/contextual-manager.ftl` — recomendamos excluir, para que outros → recomendamos excluir o arquivo para que outras pessoas
    - Current: `recomendamos excluir, para que outros`
    - Source: `After you export, we recommend deleting it so others who may use this device can’t see your passwords.`
    - Suggest: `recomendamos excluir o arquivo para que outras pessoas`
- `contextual-manager-passwords-remove-login-card-message` — `browser/browser/contextual-manager.ftl` — Isto não pode ser defeito. → desfeito
    - Current: `Isto não pode ser defeito.`
    - Source: `You can’t undo this.`
    - Suggest: `desfeito`
- `customkeys-file-focus-search` — `browser/browser/customkeys.ftl` — duplicated article: Foco na a barra de pesquisa → Foco na barra de pesquisa
    - Current: `Foco na a barra de pesquisa`
    - Source: `Focus the Search Bar`
    - Suggest: `Foco na barra de pesquisa`
- `default-browser-guidance-notification-title` — `browser/browser/defaultBrowserNotification.ftl` — same file — stacked bare infinitives: Concluir definir o { -brand-short-name } como padrão → Conclua a definição do { -brand-short-name } como padrão
    - Current: `Concluir definir o { -brand-short-name } como padrão`
    - Source: `Finish making { -brand-short-name } your default`
    - Suggest: `Conclua a definição do { -brand-short-name } como padrão`
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — default-browser-prompt-message-pin, -pin-msix, -pin-mac — defaultBrowserNotification.ftl — missing object pronouns: torne seu navegador padrão e fixe na barra de tarefas → torne-o seu navegador padrão e fixe-o na barra de tarefas
    - Current: `torne seu navegador padrão e fixe na barra de tarefas`
    - Source: `Keep { -brand-short-name } at your fingertips — make it your default browser and pin it to your taskbar.`
    - Suggest: `torne-o seu navegador padrão e fixe-o na barra de tarefas`
- `bookmark-overlay-keyword-caption-label-2` — `browser/browser/editBookmarkOverlay.ftl` — the sibling caption uses "Use": Usar uma única palavra-chave → Use uma única palavra-chave
    - Current: `Usar uma única palavra-chave`
    - Source: `Use a single keyword to open bookmarks directly from the address bar`
    - Suggest: `Use uma única palavra-chave`
- `webext-quarantine-confirmation-line-2` — `browser/browser/extensionsUI.ftl` — em sites com restrição pela { -vendor-short-name } → em sites restritos pela { -vendor-short-name }
    - Current: `em sites com restrição pela { -vendor-short-name }`
    - Source: `Allow this extension if you trust it to read and change your data on sites restricted by { -vendor-short-name }.`
    - Suggest: `em sites restritos pela { -vendor-short-name }`
- `firefoxview-closed-tabs-placeholder-body` — `browser/browser/firefoxView.ftl` — transitive verb without object: você pode recuperar aqui → você pode recuperá-la aqui
    - Current: `você pode recuperar aqui`
    - Source: `When you close a tab in this window, you can fetch it from here.`
    - Suggest: `você pode recuperá-la aqui`
- `firefoxview-tabpickup-password-locked-description` — `browser/browser/firefoxView.ftl` — dropped subject: precisa inserir → você precisa inserir
    - Current: `precisa inserir`
    - Source: `To grab your tabs, you’ll need to enter the Primary Password for { -brand-short-name }.`
    - Suggest: `você precisa inserir`
- `link-preview-generation-error-missing-data-v2` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `{ -brand-short-name } can’t generate key points for this webpage.`
- `link-preview-key-points-disclaimer` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `Key points are AI-generated and may have mistakes.`
- `link-preview-key-points-header` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `Key points`
- `link-preview-optin-message` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `{ -brand-short-name } uses AI to read the beginning of the page and generate a few key points. To prioritize your privacy, this happens on your device.`
- `link-preview-settings-key-points` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `label: Allow AI to read the beginning of the page and generate key points`
- `link-preview-setup-faster-next-time` — `browser/browser/genai.ftl` — link-preview-generation-error-missing-data-v2, link-preview-settings-key-points (.label), link-preview-optin-message, link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-setup-faster-next-time — genai.ftl — pontos chave / Pontos chave → pontos-chave / Pontos-chave (6 instances)
    - Current: `Pontos chave`
    - Source: `You’ll see key points more quickly next time.`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — ipprotection-message-bandwidth-warning (.message), -mb (.message), ip-protection-bandwidth-warning-infobar-message-90, -90-mb — ipProtection.ftl — GB restante este mês → GB restantes este mês; Tem { $usageLeft } GB restante → Você tem { $usageLeft } GB restantes (the -75 sibling is correct)
    - Current: `GB restante este mês`
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
    - Suggest: `GB restantes este mês`
- `cfr-doorhanger-doh-body` — `browser/browser/newtab/asrouter.ftl` — suas requisição de DNS → suas requisições de DNS
    - Current: `suas requisição de DNS`
    - Source: `Your privacy matters. { -brand-short-name } now securely routes your DNS requests whenever possible to a partner service to protect you while you browse.`
    - Suggest: `suas requisições de DNS`
- `mr2022-background-update-toast-text` — `browser/browser/newtab/asrouter.ftl` — anti-rastreamento → antirrastreamento
    - Source: `Try the newest { -brand-short-name } now, upgraded with our strongest anti-tracking protection yet.`
    - Suggest: `antirrastreamento`
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — doubled preposition: bloqueia em média de mais de 3.000 rastreadores → bloqueia em média mais de 3.000 rastreadores (the july-jam-body sibling is correct)
    - Current: `bloqueia em média de mais de 3.000 rastreadores`
    - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
    - Suggest: `bloqueia em média mais de 3.000 rastreadores`
- `newtab-download-mobile-highlight-image` — `browser/browser/newtab/newtab.ftl` — more-from-moz-qr-code-firefox-mobile-img (.alt) and newtab-download-mobile-highlight-image (.aria-label) — moreFromMozilla.ftl / newtab.ftl — o { -brand-product-name } de dispositivos móveis → o { -brand-product-name } para dispositivos móveis
    - Current: `o { -brand-product-name } de dispositivos móveis`
    - Source: `aria-label: QR code to download { -brand-product-name } for mobile`
    - Suggest: `o { -brand-product-name } para dispositivos móveis`
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — mais grandes histórias através da web → mais grandes histórias de toda a web (the generic variant uses "na web")
    - Current: `mais grandes histórias através da web`
    - Source: `You’ve caught up. Check back later for more top stories from { $provider }. Can’t wait? Select a popular topic to find more great stories from around the web.`
    - Suggest: `mais grandes histórias de toda a web`
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — "confiar" requires "em": para quem você confia → para as pessoas em quem você confia
    - Current: `para quem você confia`
    - Source: `Save your real email for people you trust; use an email mask for sign-ups.`
    - Suggest: `para as pessoas em quem você confia`
- `newtab-section-toast-block` — `browser/browser/newtab/newtab.ftl` — Não aparecerá mais histórias → Não aparecerão mais histórias
    - Current: `Não aparecerá mais histórias`
    - Source: `message: You won’t see stories about { $topic } anymore.`
    - Suggest: `Não aparecerão mais histórias`
- `newtab-sports-widget-message-wallpapers-semifinals-title` — `browser/browser/newtab/newtab.ftl` — semi-finais → semifinais (the file's own newtab-sports-widget-semi-finals uses "Semifinais")
    - Source: `Get a new wallpaper for the semi-finals`
    - Suggest: `semifinais`
- `newtab-topsites-url-validation` — `browser/browser/newtab/newtab.ftl` — É necessário uma URL válida → É necessária uma URL válida
    - Current: `É necessário uma URL válida`
    - Source: `Valid URL required`
    - Suggest: `É necessária uma URL válida`
- `newtab-wallpaper-beach-at-sunrise` — `browser/browser/newtab/newtab.ftl` — duplicated word: Praia ao ao nascer do sol → Praia ao nascer do sol
    - Current: `Praia ao ao nascer do sol`
    - Source: `Beach at sunrise`
    - Suggest: `Praia ao nascer do sol`
- `newtab-wallpaper-blue-flowers` — `browser/browser/newtab/newtab.ftl` — the "a + infinitive" progressive is European Portuguese: flores de pétalas azuis a desabrochar → flores de pétalas azuis desabrochando
    - Current: `flores de pétalas azuis a desabrochar`
    - Source: `Closeup photography of blue-petaled flowers in bloom`
    - Suggest: `flores de pétalas azuis desabrochando`
- `newtab-wallpaper-dark-color` — `browser/browser/newtab/newtab.ftl` — newtab-wallpaper-light-color, newtab-wallpaper-dark-color — newtab.ftl — colors must agree with "Formas": Formas azul, rosa e amarelo / Formas vermelho e azul → Formas em tons de azul, rosa e amarelo / Formas em tons de vermelho e azul (matching the newtab-wallpaper-abstract- pattern)
    - Current: `Formas vermelho e azul`
    - Source: `Red and blue shapes`
    - Suggest: `Formas em tons de azul, rosa e amarelo`
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — intervalos para estivar as pernas → esticar as pernas ("estivar" = to stow cargo)
    - Current: `intervalos para estivar as pernas`
    - Source: `From quick reminders to daily to-dos, focus sessions to stretch breaks — stay on task and on time.`
    - Suggest: `esticar as pernas`
- `fx-backup-confirmation-screen-easy-setup-item-text-3` — `browser/browser/newtab/onboarding.ftl` — métodos de pagamentos → métodos de pagamento
    - Current: `métodos de pagamentos`
    - Source: `Passwords and payments not included`
    - Suggest: `métodos de pagamento`
- `mr2022-onboarding-get-started-primary-subtitle` — `browser/browser/newtab/onboarding.ftl` — refers to "versão": Está repleto → Está repleta
    - Current: `Está repleto`
    - Source: `Our latest version is built around you, making it easier than ever to zip around the web. It’s packed with features we think you’ll adore.`
    - Suggest: `Está repleta`
- `multi-profile-spotlight-body` — `browser/browser/newtab/onboarding.ftl` — Alterne facilmente entre navegação de trabalho ou diversão. → …entre navegação de trabalho e diversão.
    - Current: `Alterne facilmente entre navegação de trabalho ou diversão.`
    - Source: `Easily switch between browsing for work and fun. Profiles keep your browsing info, including search history and passwords, totally separate so you can stay organized.`
    - Suggest: `…entre navegação de trabalho e diversão.`
- `onboarding-infrequent-import-subtitle` — `browser/browser/newtab/onboarding.ftl` — lembre que pode importar → lembre-se de que pode importar
    - Current: `lembre que pode importar`
    - Source: `Whether you’re settling in or just stopping by, remember you can import your bookmarks, passwords, and more.`
    - Suggest: `lembre-se de que pode importar`
- `origin-controls-options` — `browser/browser/originControls.ftl` — en-US ends with a colon because the options follow directly: A extensão pode ler e alterar dados → …dados:
    - Current: `A extensão pode ler e alterar dados`
    - Source: `label: Extension Can Read and Change Data:`
    - Suggest: `…dados:`
- `policy-Bookmarks` — `browser/browser/policies/policies-descriptions.ftl` — ou uma pasta especificada dentro deles → ou em uma pasta especificada dentro deles
    - Current: `ou uma pasta especificada dentro deles`
    - Source: `Create bookmarks in the Bookmarks toolbar, Bookmarks menu, or a specified folder inside them.`
    - Suggest: `ou em uma pasta especificada dentro deles`
- _…and 105 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `about-logins-list-item-breach-icon` — `browser/browser/aboutLogins.ftl` — "Site vazado" (about-logins-list-item-breach-icon.title) reads as though the site leaked → Site com vazamento de dados (matching about-logins-list-section-breach)
    - Source: `title: Breached website`
    - Suggest: `Site com vazamento de dados`
- `about-logins-list-section-breach` — `browser/browser/aboutLogins.ftl` — "Site vazado" (about-logins-list-item-breach-icon.title) reads as though the site leaked → Site com vazamento de dados (matching about-logins-list-section-breach)
    - Source: `Breached websites`
    - Suggest: `Site com vazamento de dados`
- `login-item-timeline-action-created` — `browser/browser/aboutLogins.ftl` — the three timeline labels are parallel participles (Atualizada, Usada) except this one: Criação → Criada
    - Current: `Criação`
    - Source: `Created`
    - Suggest: `Criada`
- `about-private-browsing-search-placeholder` — `browser/browser/aboutPrivateBrowsing.ftl` — "Search the web": Pesquisar na web vs Pesquisar na internet — adjacent strings about-private-browsing-search-placeholder/-search-btn.title and newtab-search-box-input/newtab-search-box-text
    - Current: `Pesquisar na web`
    - Source: `Search the web`
    - Suggest: `Pesquisar na internet`
- `crashed-request-auto-submit-title` — `browser/browser/aboutTabCrashed.ftl` — "Report"/"Relatar": crashed-request-auto-submit-title uses Informar; the rest of aboutTabCrashed.ftl uses Relatar
    - Source: `Report background tabs`
    - Suggest: `Informar`
- `addon-domain-blocked-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `Your system administrator prevented this site from asking you to install software on your computer.`
- `addon-install-domain-blocked-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `Your organization prevented this site from asking you to install software on your computer.`
- `xpinstall-disabled` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `Software installation is currently disabled. Click Enable and try again.`
- `xpinstall-disabled-by-policy` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `Software installation has been disabled by your organization.`
- `xpinstall-disabled-locked` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `Software installation has been disabled by your system administrator.`
- `xpinstall-prompt` — `browser/browser/addonNotifications.ftl` — "software": xpinstall-prompt, xpinstall-disabled-locked, xpinstall-disabled, xpinstall-disabled-by-policy, addon-domain-blocked-by-policy, addon-install-domain-blocked-by-policy render it as um programa / software / programas
    - Source: `{ -brand-short-name } prevented this site from asking you to install software on your computer.`
- `aiwindow-feedback-include-page-content` — `browser/browser/aiWindow.ftl` — "chat": aiwindow-feedback-include-page-content leaves chat in English; the file uses conversa
    - Source: `Share the pages referenced in this chat`
    - Suggest: `chat`
- `appmenu-tab-hide-controlled` — `browser/browser/appMenuNotifications.ftl` — "hidden tabs": abas ocultadas (appmenu-tab-hide-controlled) vs abas ocultas (all-tabs-menu-hidden-tabs)
    - Current: `abas ocultadas`
    - Source: `buttonaccesskey: K buttonlabel: Keep Tabs Hidden label: Access Your Hidden Tabs secondarybuttonaccesskey: D secondarybuttonlabel: Disable Extension`
- `profiler-button-dropmarker` — `browser/browser/appmenu.ftl` — profiler-button-dropmarker (.label, .tooltiptext) — painel do profiler → painel do Analisador (as in profiler-popup-button-)
    - Current: `painel do profiler`
    - Source: `label: Open the profiler panel tooltiptext: Open the profiler panel`
    - Suggest: `painel do Analisador`
- `settings-data-backup-toggle-on2` — `browser/browser/backupSettings.ftl` — "backup": backup on the toggles (settings-data-backup-toggle-on2) vs cópia de segurança in the modals (turn-on-scheduled-backups-header, -confirm-button, -encryption-label, enable-backup-encryption-header) and windows-10-eos-global-infobar-primary-button
    - Current: `backup`
    - Source: `label: Turn on backup`
- `identity-etsi` — `browser/browser/browser.ftl` — Regulamento (EU) 2024/1183 → Regulamento (UE) 2024/1183 (União Europeia)
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
- `urlbar-placeholder-search-mode-other-bookmarks` — `browser/browser/browser.ftl` — "search terms": urlbar-placeholder-search-mode-other-bookmarks (.placeholder) uses busca, its four siblings use pesquisa
    - Source: `aria-label: Search bookmarks placeholder: Enter search terms`
    - Suggest: `.placeholder`
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, -body — chave (= key/password) for a keyboard key → tecla (customkeys-conflict-confirm-body is correct)
    - Current: `chave`
    - Source: `Key cannot be used`
    - Suggest: `tecla`
- `customkeys-dev-profiler-capture` — `browser/browser/customkeys.ftl` — um profile de desempenho → um perfil de desempenho; customkeys-dev-debugger — Debugger de JavaScript → Depurador de JavaScript
    - Current: `um profile de desempenho`
    - Source: `Capture a Performance Profile`
    - Suggest: `um perfil de desempenho`
- `bookmark-overlay-keyword-2` — `browser/browser/editBookmarkOverlay.ftl` — bookmark-overlay-keyword-2 (.value) — the field is labelled Atalho while its own caption calls it "palavra-chave" → Palavra-chave
    - Current: `Atalho`
    - Source: `accesskey: K value: Keyword`
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — "AI chatbot": robô de conversa (genai-onboarding-description, sidebar-customization-callout-1-subtitle) vs chatbot de inteligência artificial everywhere else — including the next sentence of genai-onboarding-description itself
    - Current: `robô de conversa`
    - Source: `The { -brand-product-name } sidebar gives you quick access to your browsing history, tabs from other devices, and an AI chatbot — all without leaving your main view.`
- `firefoxview-syncedtabs-adddevice-primarybutton` — `browser/browser/firefoxView.ftl` — para celular → para dispositivos móveis (as in the two sibling promos)
    - Current: `para celular`
    - Source: `Try { -brand-product-name } for mobile`
    - Suggest: `para dispositivos móveis`
- `firefoxview-tabpickup-header` — `browser/browser/firefoxView.ftl` — "tab pickup": Escolha de abas (firefoxview-tabpickup-header) vs coleta de abas (continuous-onboarding-firefox-view-tab-pickup-title) vs sincronização de abas (callout-firefox-view-tab-pickup-title)
    - Current: `Escolha de abas`
    - Source: `Tab pickup`
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — "sidebar": genai-chatbot-summarize-footer-generic-subtitle uses barra lateral; every other string uses painel lateral
    - Source: `Add an AI chatbot to the { -brand-short-name } sidebar to quickly summarize pages.`
    - Suggest: `barra lateral`
- `genai-input-ask-provider` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
    - Current: `Consultar`
    - Source: `placeholder: Ask { $provider }…`
- `genai-menu-ask-provider` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
    - Current: `Consultar`
    - Source: `label: Ask { $provider }`
- `genai-onboarding-description` — `browser/browser/genai.ftl` — "AI chatbot": robô de conversa (genai-onboarding-description, sidebar-customization-callout-1-subtitle) vs chatbot de inteligência artificial everywhere else — including the next sentence of genai-onboarding-description itself
    - Current: `robô de conversa`
    - Source: `Choose an AI chatbot to use in the { -brand-short-name } sidebar. We’ll show details about each chatbot when you select it. Switch anytime. <a data-l10n-name="learn-more">Learn more</a>`
- `genai-shortcut-button` — `browser/browser/genai.ftl` — "Ask { $provider }": Consultar (genai-menu-ask-provider, genai-input-ask-provider, genai-shortcut-button) vs Perguntar ao (genai-menu-ask-provider-2)
    - Current: `Consultar`
    - Source: `aria-label: Ask { $provider }`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body (asrouter.ftl) and mr2022-onboarding-get-started-primary-subtitle (onboarding.ftl) address the user as vocês (plural) while the rest of the tree uses singular você
    - Source: `Every month, { -brand-short-name } blocks an average of 3,000+ trackers per user, giving you safe, speedy access to the good internet.`
- `windows-10-eos-sync-callout-privacy-screen-1-title` — `browser/browser/newtab/asrouter.ftl` — bloqueia mineração de criptomoedas → bloqueia mineradores de criptomoedas (cryptominers are agents; preferences.ftl uses "mineradores de criptomoedas")
    - Current: `bloqueia mineração de criptomoedas`
    - Source: `{ -brand-product-name } blocks cryptominers, social media trackers, and fingerprinters.`
    - Suggest: `bloqueia mineradores de criptomoedas`
- `newtab-search-box-input` — `browser/browser/newtab/newtab.ftl` — "Search the web": Pesquisar na web vs Pesquisar na internet — adjacent strings about-private-browsing-search-placeholder/-search-btn.title and newtab-search-box-input/newtab-search-box-text
    - Current: `Pesquisar na web`
    - Source: `aria-label: Search the web placeholder: Search the web`
    - Suggest: `Pesquisar na internet`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Sincronizar com dispositivos móveis” but the string it names, `sync-to-mobile-button-label`, reads “Sincronização com dispositivos móveis”
    - Current: `Capture o código QR para instalar o { -brand-product-name } para dispositivos móveis. Após instalar, selecione “Sincronizar com dispositivos móveis” para acessar suas senhas, favoritos e muito mais em qualquer lugar.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Sincronização com dispositivos móveis`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mr2022-onboarding-get-started-primary-subtitle` — `browser/browser/newtab/onboarding.ftl` — july-jam-body (asrouter.ftl) and mr2022-onboarding-get-started-primary-subtitle (onboarding.ftl) address the user as vocês (plural) while the rest of the tree uses singular você
    - Source: `Our latest version is built around you, making it easier than ever to zip around the web. It’s packed with features we think you’ll adore.`
- `onboarding-live-language-skip-button-label` — `browser/browser/newtab/onboarding.ftl` — Ignorar → Pular (used by the three other "Skip" strings)
    - Current: `Ignorar`
    - Source: `Skip`
    - Suggest: `Pular`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — o único principal navegador → o único grande navegador (as in welcome-back-spotlight-subtitle)
    - Current: `o único principal navegador`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `o único grande navegador`
- `sync-to-mobile-button-label` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle tells the user to select "Sincronizar com dispositivos móveis" but the button reads "Sincronização com dispositivos móveis"
    - Source: `Sync to mobile`
- `security-view-identity-verifier` — `browser/browser/pageInfo.ftl` — "Verified by": Homologado por: (security-view-identity-verifier.value, pageInfo.ftl) vs Verificado por: (identity-verifier-label, browser.ftl)
    - Current: `Homologado por:`
    - Source: `value: Verified by:`
- `places-sortby-name` — `browser/browser/places.ftl` — "Sort by name": Ordenar pelo nome (places-sortby-name) vs Ordenar por nome (places-view-sortby-name)
    - Current: `Ordenar pelo nome`
    - Source: `accesskey: r label: Sort By Name`
- `policy-Extensions` — `browser/browser/policies/policies-descriptions.ftl` — the comment says the keys may be translated as verbs: "Bloqueado" → “Bloquear”
    - Current: `"Bloqueado"`
    - Source: `Install, uninstall or lock extensions. The Install option takes URLs or paths as parameters. The Uninstall and Locked options take extension IDs.`
    - Suggest: `“Bloquear”`
- `appearance-browser-icon-unlocked` — `browser/browser/preferences/browserIcon.ftl` — appearance-browser-icon-unlocked (.message) — "bonus icons" is ícones de bônus here but ícones extras de raposas in appearance-browser-icon-requirement
    - Source: `message: You unlocked all of the bonus icons!`
    - Suggest: `.message`
- `containers-dialog` — `browser/browser/preferences/containers.ftl` — containers-dialog (.buttonlabelaccept) — "Done" is Concluído here and Pronto in containers-panel-create-button
    - Source: `buttonaccesskeyaccept: D buttonlabelaccept: Done`
    - Suggest: `.buttonlabelaccept`
- `autofill-address-prefecture` — `browser/browser/preferences/formAutofill.ftl` — Província collides with autofill-address-province → Prefeitura for the Japanese prefecture field
    - Source: `Prefecture`
    - Suggest: `Prefeitura`
- `browser-languages-error` — `browser/browser/preferences/languages.ftl` — browser-languages-error and browser-language-install-error (.message) — à Internet capitalized; the rest of the tree uses lowercase internet
    - Source: `{ -brand-short-name } can’t update your languages right now. Check that you are connected to the internet or try again.`
- `languages-customize-select-language` — `browser/browser/preferences/languages.ftl` — languages-customize-select-language (.placeholder) — um idioma a adicionar vs um idioma para adicionar in browser-languages-select-language
    - Source: `placeholder: Select a language to add…`
    - Suggest: `.placeholder`
- `permissions-disable-etp` — `browser/browser/preferences/permissions.ftl` — certmgr-add-exception (Adicionar exceção…) vs permissions-disable-etp (Adicionar exceção)
    - Source: `accesskey: E label: Add Exception`
    - Suggest: `Adicionar exceção…`
- `applications-use-os-default` — `browser/browser/preferences/preferences.ftl` — applications-use-os-default (.label, all three PLATFORM variants) — aplicação appears only here; the whole scope uses aplicativo. Same pt-PT term in safeb-blocked-harmful-page-error-desc-override/-no-override and policy-AppAutoUpdate/policy-RequestedLocales
    - Source: `label: {$sel_1 ->} [macos] Use macOS default application [windows] Use Windows default application [other] Use system default application`
    - Suggest: `.label`
- `browser-language-install-error` — `browser/browser/preferences/preferences.ftl` — browser-languages-error and browser-language-install-error (.message) — à Internet capitalized; the rest of the tree uses lowercase internet
    - Source: `message: { -brand-short-name } can’t update your languages right now. Check that you are connected to the internet or try again.`
- `forms-primary-pw-fips-title` — `browser/browser/preferences/preferences.ftl` — forms-primary-pw-fips-title (O FIPS exige) vs pp-change2empty-in-fips-mode (O modo FIPS exige)
    - Source: `You are currently in FIPS mode. FIPS requires a non-empty Primary Password.`
    - Suggest: `O FIPS exige`
- `preferences-ai-controls-block-confirmation-description` — `browser/browser/preferences/preferences.ftl` — melhorias → aprimoramentos de inteligência artificial (as in the rest of the section)
    - Current: `melhorias`
    - Source: `You won’t see new or current AI enhancements in { -brand-short-name }, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.`
    - Suggest: `aprimoramentos de inteligência artificial`
- `referrals-link2` — `browser/browser/preferences/preferences.ftl` — "Share { -brand-product-name }" is rendered as "Recomendar" here but "Compartilhar" in the app menu and menu bar for the same feature.
    - Current: `label: Recomendar o { -brand-product-name }`
    - Source: `label: Share { -brand-product-name }`
    - Suggest: `label: Compartilhar o { -brand-product-name }`
    - The identical en-US label "Share { -brand-product-name }" is translated "Compartilhar o { -brand-product-name }" in appmenu.ftl and menubar.ftl; the differing verb here breaks terminology consistency for the same referral feature.
- `referrals-section-header2` — `browser/browser/preferences/preferences.ftl` — "Share { -brand-product-name }" is rendered as "Recomendar" here but "Compartilhar" in the app menu and menu bar for the same feature.
    - Current: `label: Recomendar o { -brand-product-name }`
    - Source: `description: Invite someone to choose the browser that puts privacy first. label: Share { -brand-product-name }`
    - Suggest: `label: Compartilhar o { -brand-product-name }`
    - The identical en-US label "Share { -brand-product-name }" with the same developer comment is translated "Compartilhar o { -brand-product-name }" in appmenu.ftl and menubar.ftl; using a different verb in preferences makes the same feature inconsistently named across surfaces.
- `search-suggestions-cant-show` — `browser/browser/preferences/preferences.ftl` — search-suggestions-cant-show, search-suggestions-cant-show-2 (.message) — barra de endereço (singular); ~20 other strings use barra de endereços
    - Source: `Search suggestions will not be shown in location bar results because you have configured { -brand-short-name } to never remember history.`
- `search-suggestions-cant-show-2` — `browser/browser/preferences/preferences.ftl` — search-suggestions-cant-show, search-suggestions-cant-show-2 (.message) — barra de endereço (singular); ~20 other strings use barra de endereços
    - Source: `message: Search suggestions will not be shown in location bar results because you have configured { -brand-short-name } to never remember history.`
- `settings-translations-subpage-download-progress` — `browser/browser/preferences/preferences.ftl` — Transferência em andamento… → Download em andamento… (the file uses "Download"/"Baixar" throughout)
    - Current: `Transferência em andamento…`
    - Source: `Download in progress…`
    - Suggest: `Download em andamento…`
- `edit-profile-page-avatar-header-2` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `label: Avatar`
- `folder-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `tooltiptext: Apply folder avatar`
- `palette-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `tooltiptext: Apply palette avatar`
- `picture-avatar` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `Picture`
- `picture-avatar-tooltip` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `tooltiptext: Apply picture avatar`
- `sparkle-single-avatar` — `browser/browser/profiles.ftl` — profiles.ftl avatar labels — edit-profile-page-avatar-header-2 uses Símbolo where the file uses avatar; sparkle-single-avatar-tooltip says brilho while sparkle-single-avatar says Faísca; video-game-controller-avatar-tooltip says controle de videogame while video-game-controller-avatar says Controlador de videogame; picture-avatar-tooltip says de imagem while picture-avatar says Foto; folder-avata…
    - Source: `Sparkle`
- _…and 65 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `about-logins-import-report-added2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-added2, -modified2, -no-change2 — aboutLogins.ftl — the details spans start lowercase, unlike the identical non-2 variants and en-US
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">New passwords added</div>`
    - Suggest: `-modified2`
- `restore-page-problem-desc` — `browser/browser/aboutSessionRestore.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `We are having trouble restoring your last browsing session. Select Restore Session to try again.`
- `crashed-multiple-offer-help-message` — `browser/browser/aboutTabCrashed.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `Choose { crashed-restore-tab-button } or { crashed-restore-all-button } to reload the page/pages.`
- `crashed-single-offer-help-message` — `browser/browser/aboutTabCrashed.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `Choose { crashed-restore-tab-button } to reload the page.`
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
- `bookmarks-tools-toolbar-visibility-menuitem` — `browser/browser/browser.ftl` — the [true] variant is Ocultar Barra de Favoritos while [other] is sentence case
    - Source: `label: {$isVisible ->} [true] Hide Bookmarks Toolbar [other] View Bookmarks Toolbar`
    - Suggest: `.label`
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `To use the F12 shortcut, first open DevTools via the Browser Tools menu.`
- `quickactions-cmd-clearhistory` — `browser/browser/browser.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
    - Source: `clear history`
    - Suggest: `-show-msg`
- `quickactions-cmd-private` — `browser/browser/browser.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
    - Source: `private browsing`
    - Suggest: `-show-msg`
- `main-context-menu-pdfjs-save-page` — `browser/browser/browserContext.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
    - Source: `label: Save selection as…`
    - Suggest: `.label`
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — Comma where a period belongs: contextual-manager-passwords-no-passwords-message (contextual-manager.ftl) — são criptografadas, Estamos atentos → criptografadas. Estamos atentos
    - Current: `são criptografadas, Estamos atentos`
    - Source: `All passwords are encrypted and we’ll watch out for breaches and alerts if you’re affected.`
    - Suggest: `criptografadas. Estamos atentos`
- `pin-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `Drag a tab to the start of the tab strip to pin it. Or right-click and choose Pin Tab.`
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `To pin any tab, drag it to the start of the tab strip. Or right-click and choose Pin Tab.`
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — escolha 'Fixar aba'
    - Source: `To pin any tab, drag it to the start of the tab strip. Or right-click and choose Pin Tab.`
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — da Mistral AI . → da Mistral AI.
    - Current: `da Mistral AI .`
    - Source: `By choosing Le Chat Mistral, you agree to the Mistral AI <a data-l10n-name="link1">Terms of Service</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
    - Suggest: `da Mistral AI.`
- `ipprotection-connection-status-blocked-error-title-1` — `browser/browser/ipProtection.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `(value): VPN is unavailable aria-label: VPN is unavailable`
    - Suggest: `.aria-label`
- `ipprotection-feature-introduction-link-text-captive-portal-1` — `browser/browser/ipProtection.ftl` — Final period dropped: ipprotection-feature-introduction-link-text-captive-portal-1 (ipProtection.ftl), policy-GenerativeAI (policies-descriptions.ftl)
    - Source: `Get <a data-l10n-name="learn-more-vpn">extra privacy</a> by choosing from several locations to hide where you browse.`
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — Comma splice: ipprotection-site-settings-callout-subtitle (ipProtection.ftl) — em um site específico, isso será lembrado → …e isso será lembrado; about-logins-confirm-export-dialog-message (aboutLogins.ftl) — also drops the consecutive "so" and the object pronoun → …, portanto qualquer pessoa … poderá vê-las.
    - Current: `em um site específico, isso será lembrado`
    - Source: `Turn VPN off for a specific site and we’ll remember it next time you visit.`
    - Suggest: `…e isso será lembrado`
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Ocultar Outros → Ocultar outros
    - Current: `Ocultar Outros`
    - Source: `label: Hide Others`
    - Suggest: `Ocultar outros`
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — a pasta “Safari“ → “Safari” (the other quotes in the same string are correct; note en-US also has this defect in this string)
    - Current: `a pasta “Safari“`
    - Source: `macOS requires you to explicitly allow { -brand-short-name } to access Safari’s data. Click “Continue”, select the “Safari“ folder in the Finder dialog that appears and then click “Open”.`
    - Suggest: `“Safari”`
- `migration-list-payment-methods-label` — `browser/browser/migrationWizard.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
    - Source: `payment methods`
    - Suggest: `-show-msg`
- `windows-10-eos-callout-addons-title` — `browser/browser/newtab/asrouter.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `Try add-ons: simple upgrades, big impacts`
    - Suggest: `.aria-label`
- `newtab-discovery-empty-section-topstories-loading` — `browser/browser/newtab/newtab.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
    - Source: `Loading…`
    - Suggest: `.label`
- `newtab-report-ads-reason-seen-it-too-many-times` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `label: I’ve seen it too many times`
    - Suggest: `.aria-label`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `Your favorites at your fingertips`
    - Suggest: `.aria-label`
- `newtab-wallpaper-sky-with-pink-clouds` — `browser/browser/newtab/newtab.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `Sky with pink clouds`
    - Suggest: `.aria-label`
- `smartwindow-sidebar-auto-open-callout-accepted-subtitle` — `browser/browser/newtab/onboarding.ftl` — uses U+02DD (˝) instead of quotes: Use ˝Fazer uma pergunta˝ → Use “Fazer uma pergunta”
    - Current: `Use ˝Fazer uma pergunta˝`
    - Source: `Use Ask to open it on any page. Change this anytime in <a data-l10n-name="settings">Settings</a>.`
    - Suggest: `Use “Fazer uma pergunta”`
- `tab-groups-onboarding-feature-callout-title` — `browser/browser/newtab/onboarding.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `Try tab groups for less clutter, more focus`
    - Suggest: `.aria-label`
- `page-info-frame` — `browser/browser/pageInfo.ftl` — the separator was dropped entirely: Informações do frame { $website } → Informações do frame — { $website }
    - Current: `Informações do frame { $website }`
    - Source: `title: Frame Info — { $website }`
    - Suggest: `Informações do frame — { $website }`
- `page-info-page` — `browser/browser/pageInfo.ftl` — Informações da página - { $website } → —
    - Current: `Informações da página - { $website }`
    - Source: `title: Page Info — { $website }`
    - Suggest: `—`
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — Final period dropped: ipprotection-feature-introduction-link-text-captive-portal-1 (ipProtection.ftl), policy-GenerativeAI (policies-descriptions.ftl)
    - Source: `Configure generative AI features.`
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — serial comma before "e" is not pt-BR usage: 127.0.0.1/8, e ::1 → 127.0.0.1/8 e ::1
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
- `autofill-card-expires-year` — `browser/browser/preferences/formAutofill.ftl` — autofill-card-expires-month, autofill-card-expires-year — preferences/formAutofill.ftl — Mês de Expiração / Ano de Expiração → sentence case (the -2 variants are correct)
    - Current: `Ano de Expiração`
    - Source: `Exp. Year`
    - Suggest: `-2`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — { $locale } [{ $code }] → single space
    - Current: `{ $locale } [{ $code }]`
    - Source: `label: { $locale } [{ $code }]`
    - Suggest: `single space`
- `permissions-exceptions-manage-etp-desc` — `browser/browser/preferences/permissions.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `You can specify which websites have Enhanced Tracking Protection turned off. Type the exact address of the site you want to manage and then click Add Exception.`
- `addons-button-label` — `browser/browser/preferences/preferences.ftl` — addons-button-label2 (.label, .title), addons-button-label — preferences.ftl — Extensões e Temas → Extensões e temas
    - Current: `Extensões e Temas`
    - Source: `Extensions and themes`
    - Suggest: `Extensões e temas`
- `addons-button-label2` — `browser/browser/preferences/preferences.ftl` — addons-button-label2 (.label, .title), addons-button-label — preferences.ftl — Extensões e Temas → Extensões e temas
    - Current: `Extensões e Temas`
    - Source: `(value): Extensions and themes title: Extensions and themes`
    - Suggest: `Extensões e temas`
- `home-homepage-custom-url` — `browser/browser/preferences/preferences.ftl` — main-context-menu-pdfjs-save-page (.label, browserContext.ftl), home-homepage-custom-url (.placeholder, preferences.ftl), newtab-discovery-empty-section-topstories-loading (newtab.ftl).
    - Source: `placeholder: Paste a URL…`
    - Suggest: `.label`
- `security-privacy-issue-warning-third-party-cookies` — `browser/browser/preferences/preferences.ftl` — Trailing period added where en-US has none: ipprotection-connection-status-blocked-error-title-1 (.aria-label too), security-privacy-issue-warning-third-party-cookies (.label, preferences.ftl), newtab-wallpaper-sky-with-pink-clouds, newtab-shortcuts-highlight-title, newtab-report-ads-reason-seen-it-too-many-times (.label) (newtab.ftl), windows-10-eos-callout-addons-title (asrouter.ftl), tab-group…
    - Source: `description: Third-party cookies are used to track you across websites. label: Third-party cookies are enabled`
    - Suggest: `.aria-label`
- `update-setting-write-failure-message2` — `browser/browser/preferences/preferences.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `{ -brand-short-name } encountered an error and didn’t save this change. Note that changing this update setting requires permission to write to the file below. You or a system administrator may be able to resolve the err…`
- `tabbrowser-container-tab-title` — `browser/browser/tabbrowser.ftl` — { $title } - { $containerName } → —
    - Current: `{ $title } - { $containerName }`
    - Source: `{ $title } — { $containerName }`
    - Suggest: `—`
- `tabbrowser-tab-label-tab-split-view-right` — `browser/browser/tabbrowser.ftl` — , Exibição dividida à direita → lowercase (the -left pair is lowercase)
    - Current: `, Exibição dividida à direita`
    - Source: `{ $label }, Split view right`
    - Suggest: `-left`
- `taskbar-tab-title-profile` — `browser/browser/taskbartabs.ftl` — - { -brand-full-name } → — { -brand-full-name }
    - Current: `- { -brand-full-name }`
    - Source: `{ $name } in { $profile } — { -brand-full-name }`
    - Suggest: `— { -brand-full-name }`
- `webrtc-allow-share-camera-and-microphone-with-file` — `browser/browser/webrtcIndicator.ftl` — sua câmera e microfone? (also missing the possessive: → sua câmera e seu microfone?)
    - Current: `sua câmera e microfone?`
    - Source: `Allow this local file to use your camera and microphone?`
    - Suggest: `sua câmera e seu microfone?`
- `storage-add-button` — `devtools/client/storage.ftl` — storage-add-button (.title), storage-context-menu-add-item (.label) — devtools/client/storage.ftl — Adicionar Item → Adicionar item
    - Current: `Adicionar Item`
    - Source: `title: Add Item`
    - Suggest: `Adicionar item`
- `storage-context-menu-add-item` — `devtools/client/storage.ftl` — storage-add-button (.title), storage-context-menu-add-item (.label) — devtools/client/storage.ftl — Adicionar Item → Adicionar item
    - Current: `Adicionar Item`
    - Source: `label: Add Item`
    - Suggest: `Adicionar item`
- `toolbox-always-on-top-enabled2` — `devtools/client/toolbox.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `(value): Disable always on top title: This will restart the Developer Tools`
- `inactive-css-cue-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
    - Current: `Não há suporte para<strong>`
    - Source: `<strong>{ $property }</strong> is not supported on ::cue pseudo-elements.`
    - Suggest: `para <strong>`
- `inactive-css-first-letter-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
    - Current: `Não há suporte para<strong>`
    - Source: `<strong>{ $property }</strong> is not supported on ::first-letter pseudo-elements.`
    - Suggest: `para <strong>`
- `inactive-css-placeholder-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — inactive-css-first-letter-pseudo-element-not-supported, inactive-css-placeholder-pseudo-element-not-supported, inactive-css-cue-pseudo-element-not-supported — devtools/client/tooltips.ftl — Não há suporte para<strong> → para <strong> (the first-line sibling has the space)
    - Current: `Não há suporte para<strong>`
    - Source: `<strong>{ $property }</strong> is not supported on ::placeholder pseudo-elements.`
    - Suggest: `para <strong>`
- `inactive-css-resize` — `devtools/client/tooltips.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `<strong>{ $property }</strong> has no effect on this element since it can only be applied to elements with an overflow value other than visible, and to certain replaced elements, such as textareas.`
- `pageInfo_Privacy_None2` — `security/manager/chrome/pippki/pippki.properties` — explicit trailing not present in en-US
    - Source: `Information sent over the Internet without encryption can be seen by other people while it is in transit.`
- `crashreporter-error-no-home-dir` — `toolkit/crashreporter/crashreporter.ftl` — restore-page-problem-desc (aboutSessionRestore.ftl), crashed-single-offer-help-message, crashed-multiple-offer-help-message (aboutTabCrashed.ftl), enable-devtools-popup-description2 (browser.ftl), pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (featureCallout.ftl), permissions-exceptions-manage-etp-desc (preferences/permissions.ftl), update-setting-write-failure-message2 (preferences.ft…
    - Source: `Missing home directory`
- `discopane-notice-recommendations` — `toolkit/toolkit/about/aboutAddons.ftl` — discopane-notice-recommendations, discopane-notice-recommendations2 (.message) — aboutAddons.ftl — trailing space before the line wrap
    - Source: `Some of these recommendations are personalized. They are based on other extensions you’ve installed, profile preferences, and usage statistics.`
- `discopane-notice-recommendations2` — `toolkit/toolkit/about/aboutAddons.ftl` — discopane-notice-recommendations, discopane-notice-recommendations2 (.message) — aboutAddons.ftl — trailing space before the line wrap
    - Source: `message: Some of these recommendations are personalized. They are based on other extensions you’ve installed, profile preferences, and usage statistics.`
- `about-processes-remote-sandbox-broker-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — remoto ({ $pid }) → single space
    - Current: `remoto ({ $pid })`
    - Source: `Remote Sandbox Broker ({ $pid })`
    - Suggest: `single space`
- `a11y-instantiator` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
    - Source: `Accessibility Instantiator`
- `audio-backend` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
    - Source: `Audio Backend`
- `max-audio-channels` — `toolkit/toolkit/about/aboutSupport.ftl` — audio-backend, max-audio-channels, a11y-instantiator (aboutSupport.ftl), about-telemetry-option-group-older (aboutTelemetry.ftl) — stray Title Case in otherwise sentence-case files
    - Source: `Max Channels`
- `about-telemetry-current-data-sidebar` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Lowercase where the sibling is capitalized: about-webrtc-fold-hide-msg/-show-msg, about-webrtc-raw-cand-hide-msg/-show-msg, about-webrtc-log-hide-msg/-show-msg and the matching .title attributes (aboutWebrtc.ftl); about-webrtc-aec-logging-off-state-msg, about-webrtc-save-page-msg (aboutWebrtc.ftl); about-telemetry-current-data-sidebar (aboutTelemetry.ftl); quickactions-cmd-clearhistory, quickacti…
    - Source: `current data`
    - Suggest: `-show-msg`
- _…and 11 more; see `state/` for the full list._

---

## 4. Appendix

### Dismissed by hand (5)

- `newtab-menu-dismiss` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
- `newtab-section-unfollow-button` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
- `newtab-sports-widget-follow-teams-title` — `browser/browser/newtab/newtab.ftl` — newtab.ftl widget terms — "Dismiss": Dispensar (newtab-menu-dismiss) vs Descartar (4 other strings); "Unfollow": Parar de seguir (newtab-section-unfollow-button) vs Deixar de seguir (3 others); "feed": canal de notícias / canal de informações / feed; "break": Intervalo vs pausa in the timer strings; "teams": equipes (newtab-sports-widget-follow-teams-title) vs times everywhere else
- `urlbar-dismissal-acknowledgment-weather` — `browser/browser/browser.ftl` — urlbar-dismissal-acknowledgment-weather, urlbar-trending-dismissal-acknowledgment, urlbar-result-dismissal-acknowledgment-market, urlbar-result-dismissal-acknowledgment-all — browser.ftl — postposed plural subject: Não irá mais aparecer sugestões → Não irão mais aparecer sugestões; Não aparecerá mais pesquisas populares → Não aparecerão
- `urlbar-result-dismissal-acknowledgment-market` — `browser/browser/browser.ftl` — urlbar-dismissal-acknowledgment-weather, urlbar-trending-dismissal-acknowledgment, urlbar-result-dismissal-acknowledgment-market, urlbar-result-dismissal-acknowledgment-all — browser.ftl — postposed plural subject: Não irá mais aparecer sugestões → Não irão mais aparecer sugestões; Não aparecerá mais pesquisas populares → Não aparecerão

_One line each in `locales/pt-BR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (3)

- `firefoxview-history-context-forget-site` — `browser/browser/firefoxView.ftl` — raised by `accesskey`, withdrawn 2026-08-20
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `neterror-proxy-connect-failure-contact-admin` — `toolkit/toolkit/neterror/netError.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (138)

- `firefox-relay-offer-legal-notice-1` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `firefox-relay-offer-legal-notice-control` — `browser/browser/firefoxRelay.ftl` — fixed 2026-08-24
- `report-broken-site-panel-reason-choose` — `browser/browser/reportBrokenSite.ftl` — fixed 2026-08-24
- `split-view-menuitem-reverse-tabs` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — fixed 2026-08-24
- `sec-error-cert-not-in-name-space` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-08-24
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
