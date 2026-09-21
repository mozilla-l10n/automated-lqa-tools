# Firefox iOS l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 27 of 1,949 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-BR: [android](android.md) · [firefox](firefox.md)

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
| Files | 97 |
| Strings | 1,949 |
| Missing strings | 1 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**1 strings** are not translated yet, concentrated in:

- `pt-BR/firefox-ios.xliff` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 6, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 6 | **typographic** |
| ellipsis | `char` 23 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 145 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (57)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.Rollouts.Message.v148` — `pt-BR/firefox-ios.xliff` — "between updates" was rendered as "a cada atualização" (with each update), reversing the meaning.
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
    - The source says improvements happen remotely between updates, not at each update; this is the whole point of the remote rollouts setting.
- `Block Pop-up Windows` — `pt-BR/firefox-ios.xliff` — Translation adds "ou abas" (or tabs), which the source does not say.
    - Current: `Bloquear abertura de janelas ou abas`
    - Source: `Block Pop-up Windows`
    - Suggest: `Bloquear janelas pop-up`
    - The en-US setting is "Block Pop-up Windows"; the target drops "pop-up" and claims tabs are blocked too.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 35 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.AllBookmarks.v131` — `pt-BR/firefox-ios.xliff` — Back button label "All" (all bookmarks) translated as "Tudo" instead of the plural agreeing with "favoritos".
    - Current: `Tudo`
    - Source: `All`
    - Suggest: `Todos`
    - The comment says this is an `All` (bookmarks) back label; in pt-BR it should agree with "favoritos" ("Todos"), not the neuter "Tudo".
- `Addresses.EditAddress.AutofillAddressCounty.v129` — `pt-BR/firefox-ios.xliff` — "County" is rendered as "Município", which conflicts with the neighboring "City" field and names the wrong division.
    - Current: `Município`
    - Source: `County`
    - Suggest: `Condado`
    - The comment describes the county field as a distinct administrative division above the city; "Município" means municipality/city and is the standard pt-BR term for a city-level unit, while "County" is "Condado".
- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `pt-BR/firefox-ios.xliff` — "Prefecture" is translated as "Província" (province) instead of "Prefeitura".
    - Current: `Província`
    - Source: `Prefecture`
    - Suggest: `Prefeitura`
    - The developer comment specifies the prefecture field used in countries like Japan; "Província" names a different administrative division (province), and pt-BR uses "Prefeitura" for Japanese prefectures.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `pt-BR/firefox-ios.xliff` — "Conteúdo com rastreamento" translates "Tracking content" but the developer comment says this counts analytics trackers.
    - Current: `Conteúdo com rastreamento: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Conteúdo de rastreamento: %@`
    - Minor wording: Firefox's established term for "Tracking content" in pt-BR is "Conteúdo de rastreamento"; "com rastreamento" deviates from the product's standard terminology used elsewhere in ETP.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `pt-BR/firefox-ios.xliff` — "you may see" (possibility) rendered as "deve aparecer" (expectation/likelihood), inconsistent with the parallel standard-mode string which uses "pode aparecer".
    - Current: `então deve aparecer uma contagem menor de rastreadores`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `então pode aparecer uma contagem menor de rastreadores`
    - The source says "so you may see a lower tracker count"; "deve" asserts an expected outcome rather than a possibility, and the sibling string translates the identical construction as "pode aparecer".
- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `pt-BR/firefox-ios.xliff` — The action label drops the "Switch to" verb, becoming a noun phrase inconsistent with its counterpart string.
    - Current: `Site de computador`
    - Source: `Switch to Desktop Site`
    - Suggest: `Mudar para versão para computador`
    - en-US is "Switch to Desktop Site", an action; the counterpart string "Switch to Mobile Site" is correctly rendered as "Mudar para versão de dispositivos móveis", so this one omits the action verb and is inconsistent on the same menu.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `pt-BR/firefox-ios.xliff` — "tap Skip" was translated as "toque em Agora não" (tap Not now), naming a different button.
    - Current: `toque em Agora não`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `toque em Pular`
    - The source instructs the user to tap the "Skip" button; rendering it as "Agora não" (Not now) points to a different label than the one on screen.
- `Onboarding.IntroDescriptionPart1.v114` — `pt-BR/firefox-ios.xliff` — "For good" (meaning "for the common good") is rendered as "Para sempre" ("forever").
    - Current: `Independente. Sem fins lucrativos. Para sempre.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Independente. Sem fins lucrativos. Para o bem de todos.`
    - In context (indie, non-profit), "For good" means for the benefit of people, not "forever"; the pt-BR asserts a permanence claim the source never made.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `pt-BR/firefox-ios.xliff` — "Browsing just got better" rendered as "Navegar ficou ainda melhor" adds "ainda" (even better), a minor shift; main issue is acceptable — see rationale.
    - Current: `Navegar ficou ainda melhor.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Navegar ficou melhor.`
    - The source says browsing just got better, not "even better"; the added intensifier changes the claim.
- `Onboarding.Modern.General.Skip.v145` — `pt-BR/firefox-ios.xliff` — "Skip" translated as "Agora não" ("Not now") instead of "Pular".
    - Current: `Agora não`
    - Source: `Skip`
    - Suggest: `Pular`
    - The source is "Skip" (button to skip the entire onboarding flow); "Agora não" is the translation used for "Not now" elsewhere in this file, conflating two distinct labels.
- `Onboarding.Modern.Welcome.Title.v140` — `pt-BR/firefox-ios.xliff` — "creepy ads" rendered as "anúncios invasivos" while the phrase "Say goodbye" is dropped; acceptable, but "invasivos" changes the meaning of "creepy".
    - Current: `Chega de anúncios invasivos`
    - Source: `Say goodbye to creepy ads`
    - Suggest: `Diga adeus a anúncios sinistros`
    - The en-US says "Say goodbye to creepy ads"; the sibling v145 string translates the same construction as "Diga adeus a rastreadores sinistros", so the v140 rendering is inconsistent and loses "creepy".
- `Onboarding.Notification.Skip.Action.v115` — `pt-BR/firefox-ios.xliff` — "Skip" is translated as "Agora não" (Not now) instead of "Pular"/"Ignorar".
    - Current: `Agora não`
    - Source: `Skip`
    - Suggest: `Pular`
    - The source is "Skip"; "Agora não" corresponds to "Not Now", which is a separate string (Onboarding.Modern.Welcome.Skip) in this same file, creating inconsistency.
- `Addresses.Settings.Switch.Description.v124` — `pt-BR/firefox-ios.xliff` — "Includes" translated as the imperative/infinitive "Incluir" instead of the descriptive "Inclui".
    - Current: `Incluir números de telefone e endereços de email`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Inclui números de telefone e endereços de email`
    - The source is a descriptive statement about what the toggle covers, not an action; "Incluir" reads as a command/option label.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `pt-BR/firefox-ios.xliff` — "pop-ups" was translated as "notificações" (notifications), which names a different UI concept.
    - Current: `nem notificações sobre elas`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `nem pop-ups sobre eles`
    - The source says "or pop-ups about them"; "notificações" means notifications, a different feature. Also the pronoun should agree with "aprimoramentos" (masculine).
- `Settings.Rollouts.Message.v148` — `pt-BR/firefox-ios.xliff` — "between updates" was rendered as "a cada atualização" (with each update), reversing the meaning.
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
    - The source says improvements happen remotely between updates, not at each update; this is the whole point of the remote rollouts setting.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `pt-BR/firefox-ios.xliff` — "Firefox Suggest" was shortened to just "Firefox", losing the feature name used elsewhere on the same screen.
    - Current: `Mostrar sugestões do Firefox em sessões privativas`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Mostrar sugestões do Sugestões Firefox em sessões privativas`
    - Source is "Show suggestions from Firefox Suggest in private sessions"; the sibling strings on this screen render the feature as "Sugestões Firefox".
- `Settings.Summarize.FooterTitle.v142` — `pt-BR/firefox-ios.xliff` — "Provides access" translated as the imperative/infinitive "Permitir acesso", changing a descriptive statement into an action label.
    - Current: `Permitir acesso ao recurso de resumir páginas.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Fornece acesso ao recurso de resumir páginas.`
    - The source is a descriptive footer ("Provides access to summarize pages."), not an instruction to allow access.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `pt-BR/firefox-ios.xliff` — "Spread the word about %1$@ every time you share a link" is rendered as an infinitive without the "every time you share" condition being properly expressed.
    - Current: `Divulgar o %1$@ toda vez que compartilhar um link no %2$@.`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `Divulgue o %1$@ toda vez que compartilhar um link no %2$@.`
    - The source is an imperative sentence addressed to the user; the infinitive "Divulgar" reads as a label rather than the sentence in the source.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `pt-BR/firefox-ios.xliff` — "Sync" (label of the synced tabs button) rendered as the adjective "Sincronizado" instead of the feature noun "Sincronizar"/"Sincronização".
    - Current: `Sincronizado`
    - Source: `Sync`
    - Suggest: `Sincronizar`
    - The source is the noun/action label "Sync" for the button that shows synced tabs; "Sincronizado" is a past participle meaning "synced", not the tab-tray section label.
- `TermsOfUse.Description.v142` — `pt-BR/firefox-ios.xliff` — "We’ve introduced a %@ Terms of Use" translated as if the terms already exist and are definite, losing the sense of newly introduced terms.
    - Current: `Apresentamos os Termos de uso do %@`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Lançamos os novos Termos de uso do %@`
    - The en-US says a Terms of Use document was newly introduced ("a ... Terms of Use"); the pt-BR definite phrasing does not convey the novelty.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `pt-BR/firefox-ios.xliff` — "BRONZE FINAL" mistranslated as "FINAL DO BRONZE".
    - Current: `FINAL DO BRONZE`
    - Source: `BRONZE FINAL`
    - Suggest: `FINAL DE BRONZE`
    - The source names the bronze-medal match; "FINAL DO BRONZE" reads as "the final of the bronze" and is not the established Portuguese term (final de bronze / disputa do terceiro lugar).
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `pt-BR/firefox-ios.xliff` — "Upcoming" translated as "Seguintes" (following), not "upcoming/next".
    - Current: `Seguintes`
    - Source: `Upcoming`
    - Suggest: `Em breve`
    - The label marks a match that has not yet happened; "Seguintes" means "following ones" and does not convey "upcoming" for a single match.
- `Use your fingerprint to access Logins now.` — `pt-BR/firefox-ios.xliff` — The source's "now" is dropped in the translation.
    - Current: `Use sua digital para acessar suas contas de acesso.`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `Use sua digital para acessar suas contas de acesso agora.`
    - en-US says "to access Logins now"; the immediacy marker "now" is missing in pt-BR.
- `AddPass.Error.Message` — `pt-BR/firefox-ios.xliff` — "Wallet" (Apple brand) rendered as "Passbook" and "pass" translated as "senha" (password).
    - Current: `Ocorreu um erro ao adicionar a senha no Passbook.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Ocorreu um erro ao adicionar o passe à Wallet.`
    - The source refers to adding a pass to Apple Wallet; "senha" means password and "Passbook" is the obsolete brand name, inconsistent with the title string which uses "passe".
- `Authentication required` — `pt-BR/firefox-ios.xliff` — "Authentication required" rendered as "Requer autenticação" (requires authentication), changing the subject.
    - Current: `Requer autenticação`
    - Source: `Authentication required`
    - Suggest: `Autenticação necessária`
    - The source is a prompt title stating that authentication is required; the target reads as "[it] requires authentication".
- `Block Pop-up Windows` — `pt-BR/firefox-ios.xliff` — Translation adds "ou abas" (or tabs), which the source does not say.
    - Current: `Bloquear abertura de janelas ou abas`
    - Source: `Block Pop-up Windows`
    - Suggest: `Bloquear janelas pop-up`
    - The en-US setting is "Block Pop-up Windows"; the target drops "pop-up" and claims tabs are blocked too.
- `CoverSheet.v24.ETP.Description` — `pt-BR/firefox-ios.xliff` — "popups" mistranslated as "notificações" (notifications).
    - Current: `anúncios e notificações`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `anúncios e janelas pop-up`
    - The source says "trackers, ads, and popups"; "notificações" means notifications, a different thing than pop-ups.
- `HomePanel.ContextMenu.Bookmark` — `pt-BR/firefox-ios.xliff` — The context-menu action verb "Bookmark" is rendered as the plural noun "Favoritos" instead of the action "Adicionar aos favoritos".
    - Current: `Favoritos`
    - Source: `Bookmark`
    - Suggest: `Adicionar aos favoritos`
    - The source is an action item in a context menu (paired with "Remove Bookmark"/"Remover favorito"); "Favoritos" names a section rather than performing the bookmarking action.
- `Menu.TrackingProtection.Details.Verifier` — `pt-BR/firefox-ios.xliff` — "Verified by %@" rendered as "Homologado por %@" (approved/certified) instead of "Verificado por %@".
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The source states the SSL certificate signer verified the site; "homologado" means approved/ratified, a different claim.
- `Menu.TrackingProtectionBlockedContent.Title` — `pt-BR/firefox-ios.xliff` — "Tracking content" translated as "Conteúdo com rastreamento" instead of the standard "Conteúdo de rastreamento".
    - Current: `Conteúdo com rastreamento`
    - Source: `Tracking content`
    - Suggest: `Conteúdo de rastreamento`
    - The source refers to content that performs tracking (tracking content), not content that has tracking applied to it; Firefox pt-BR uses "Conteúdo de rastreamento".
- `Settings.ClearAllWebsiteData.Clear.Button` — `pt-BR/firefox-ios.xliff` — Plural "Website Data" rendered as singular "dados do site", implying only one site's data is cleared.
    - Current: `Limpar todos os dados do site`
    - Source: `Clear All Website Data`
    - Suggest: `Limpar todos os dados de sites`
    - The source "Clear All Website Data" refers to data from all websites, not a single site; the singular "do site" changes the scope of the action.
- `Settings.NewTab.Option.HomePage` — `pt-BR/firefox-ios.xliff` — "Homepage" translated as "Tela inicial" (start screen) instead of "Página inicial", inconsistent with the related Firefox Home string.
    - Current: `Tela inicial`
    - Source: `Homepage`
    - Suggest: `Página inicial`
    - The source refers to the user's homepage (a page/URL), rendered as "Página inicial" in Settings.NewTab.Option.FirefoxHome on the same screen; "Tela inicial" means start screen.
- `Settings.SendUsage.Message` — `pt-BR/firefox-ios.xliff` — The source's "to provide and improve Firefox" is reduced to only "melhorar" (improve), dropping "provide".
    - Current: `coletar somente o necessário para melhorar o Firefox para todos`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `coletar somente o necessário para oferecer e melhorar o Firefox para todos`
    - en-US says Mozilla collects what is needed "to provide and improve Firefox"; the translation omits "provide".
- `Settings.Siri.SectionDescription` — `pt-BR/firefox-ios.xliff` — "via Siri" is dropped from the translation.
    - Current: `Use atalhos da Siri para abrir o Firefox rapidamente`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Use atalhos da Siri para abrir o Firefox rapidamente pela Siri`
    - The en-US text says "quickly open Firefox via Siri"; the localized text omits "via Siri".
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `pt-BR/firefox-ios.xliff` — "popups" was translated as "notificações" (notifications) instead of "janelas pop-up".
    - Current: `Bloquear mais rastreadores, anúncios e notificações.`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `Bloquear mais rastreadores, anúncios e janelas pop-up.`
    - The source says the strict level blocks popups, not notifications; these are different browser features.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `pt-BR/firefox-ios.xliff` — "won’t remember" is rendered as "não irá salvar" (won't save), changing the meaning about history and cookies.
    - Current: `O Firefox não irá salvar seu histórico nem cookies`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `O Firefox não irá lembrar seu histórico nem cookies`
    - The source says Firefox will not remember history or cookies; "salvar" also clashes with the second clause's "são salvos" for bookmarks.
- `TodayWidget.TopSitesGalleryTitle` — `pt-BR/firefox-ios.xliff` — "Top Sites" translated as "Sites preferidos" (favorite sites) instead of the frequently/recently visited sense used elsewhere.
    - Current: `Sites preferidos`
    - Source: `Top Sites`
    - Suggest: `Sites mais visitados`
    - The widget's own description says it adds shortcuts to frequently and recently visited sites, not user-selected favorites.

### C. Grammar, agreement & spelling

- `ContextualHints.FeltDeletion.Body.v122` — `pt-BR/firefox-ios.xliff` — Imperative sentence rendered in third person singular, breaking the parallel with the preceding imperative.
    - Current: `Exclui o histórico, cookies, tudo.`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `Exclua o histórico, os cookies, tudo.`
    - The source "Delete your history, cookies — everything." is an imperative like the preceding "Tap here"; "Exclui" reads as indicative third person.
- `Menu.EnhancedTrackingProtection.Certificates.ValidityNotAfter.v131` — `pt-BR/firefox-ios.xliff` — Inconsistent phrasing between the paired validity labels: "Não após" vs "Não antes de".
    - Current: `Não após`
    - Source: `Not After`
    - Suggest: `Não depois de`
    - "Not After"/"Not Before" are a pair; the two labels use mismatched constructions ("Não após" without preposition vs "Não antes de"), which reads inconsistently on the same screen.
- `NativeErrorPage.CellularDataRestricted.TitleLabel.v156` — `pt-BR/firefox-ios.xliff` — Subject-verb agreement error: "Dados móveis" is plural but the verb is singular.
    - Current: `Dados móveis está desativado para o %@.`
    - Source: `Cellular data is turned off for %@.`
    - Suggest: `Os dados móveis estão desativados para o %@.`
    - "Dados móveis" is plural in Portuguese, so it requires "estão desativados".
- `NativeErrorPage.GenericError.Description.v134` — `pt-BR/firefox-ios.xliff` — Missing object pronoun and comma splice instead of the coordinating conjunction of the source.
    - Current: `O proprietário de %@ não configurou corretamente, não foi possível criar conexão segura.`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `O proprietário de %@ não o configurou corretamente e não é possível criar uma conexão segura.`
    - The source says the owner "hasn’t set it up properly and a secure connection can’t be created"; the translation drops the object of "configurou" and joins the clauses with a comma instead of "e".
- `Onboarding.Wallpaper.Action.v114` — `pt-BR/firefox-ios.xliff` — "fundo da tela" should be "fundo de tela", inconsistent with the other wallpaper strings in the same screen.
    - Current: `Escolha um fundo da tela`
    - Source: `Set Wallpaper`
    - Suggest: `Escolha um fundo de tela`
    - The other strings in the same group use "fundo de tela" for "wallpaper"; "fundo da tela" is a different (incorrect) construction.
- `Onboarding.Wallpaper.Title.v114` — `pt-BR/firefox-ios.xliff` — "fundo da tela do %@" should be "fundo de tela do %@", inconsistent with the other wallpaper strings.
    - Current: `Escolha um fundo da tela do %@`
    - Source: `Choose a %@ Wallpaper`
    - Suggest: `Escolha um fundo de tela do %@`
    - "Wallpaper" is rendered "fundo de tela" elsewhere in the same screen; "fundo da tela" is incorrect.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatusDescription.v151` — `pt-BR/firefox-ios.xliff` — Duplicated/garbled wording "você e pode usar" instead of "você pode usar".
    - Current: `**Disponível**: O recurso aparece e você e pode usar.`
    - Source: `**Available**: You’ll see the feature and can use it.`
    - Suggest: `**Disponível**: O recurso aparece e você pode usar.`
    - The source reads "You’ll see the feature and can use it." The extra "e" makes the sentence ungrammatical.
- `Settings.Appearance.NavigationToolbar.Description.v145` — `pt-BR/firefox-ios.xliff` — Infinitive "Alterar" used where the source is a descriptive third-person statement "Changes the button".
    - Current: `Alterar o botão no centro da barra de ferramentas.`
    - Source: `Changes the button in the center of the toolbar.`
    - Suggest: `Altera o botão no centro da barra de ferramentas.`
    - The developer comment says this is a section description explaining what the setting does, not an action label; en-US "Changes the button..." is declarative.
- `Settings.Studies.Message.v136` — `pt-BR/firefox-ios.xliff` — Agreement error: "antes de ser liberados" should agree in number with "recursos e ideias".
    - Current: `Experimentar recursos e ideias antes de ser liberados para todos.`
    - Source: `Try out features and ideas before they’re released to everyone.`
    - Suggest: `Experimente recursos e ideias antes de serem liberados para todos.`
    - The verb must agree with the plural subject ("recursos e ideias"); "ser" is singular and lacks the pronoun/number agreement required.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `pt-BR/firefox-ios.xliff` — Hyphenation is wrong in "OITAVAS-DE FINAL"; the standard form is "OITAVAS DE FINAL".
    - Current: `OITAVAS-DE FINAL`
    - Source: `ROUND OF 16`
    - Suggest: `OITAVAS DE FINAL`
    - The Portuguese term for "Round of 16" is "oitavas de final" (cf. "QUARTAS DE FINAL" in the sibling string); the misplaced hyphen is a spelling error.
- `Decrease text size` — `pt-BR/firefox-ios.xliff` — Accessibility label uses a conjugated verb form instead of the infinitive/noun form used for the action label.
    - Current: `Diminui o tamanho do texto`
    - Source: `Decrease text size`
    - Suggest: `Diminuir o tamanho do texto`
    - The source "Decrease text size" is an imperative/infinitive button label; "Diminui" is the third-person present indicative, which is grammatically wrong for a button accessibility label.
- `When Leaving Private Browsing` — `pt-BR/firefox-ios.xliff` — Label starts with a lowercase letter where the source is a capitalized settings label.
    - Current: `ao sair da navegação privativa`
    - Source: `When Leaving Private Browsing`
    - Suggest: `Ao sair da navegação privativa`
    - The string is displayed in Settings under 'Close Private Tabs'; it should begin with a capital letter as in the en-US source.
- `%@ search` — `pt-BR/firefox-ios.xliff` — Button label starts with a lowercase letter.
    - Current: `pesquisar %@`
    - Source: `%@ search`
    - Suggest: `Pesquisar %@`
    - Source "%@ search" is a capitalized button label for a search engine button.

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Details.Verifier.v128` — `pt-BR/firefox-ios.xliff` — "Verified by" translated as "Homologado por" (certified/approved) instead of the certificate-verification term.
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The string states which certificate authority verified the site; "homologado" means approved/certified by an authority and is not the standard term for certificate verification.
- `CreditCard.ErrorState.NameOnCardSublabel.v112` — `pt-BR/firefox-ios.xliff` — Error message rendered as an infinitive command label instead of an imperative instruction, inconsistent with the sibling error strings.
    - Current: `Adicionar um nome`
    - Source: `Add a name`
    - Suggest: `Adicione um nome`
    - "Add a name" here is an inline error instruction to the user, like "Insira uma data de expiração válida" and "Digite um número de cartão válido" in the same file; the infinitive "Adicionar" reads as a button label and breaks consistency on the same screen.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `pt-BR/firefox-ios.xliff` — "ROUND OF 32" rendered in sentence case and with inconsistent phrasing compared to the other round-phase labels.
    - Current: `Fase dos 32`
    - Source: `ROUND OF 32`
    - Suggest: `DEZESSEIS AVOS DE FINAL`
    - All other round-phase labels are uppercase (QUARTAS DE FINAL, SEMIFINAIS, TERCEIRO LUGAR), matching the uppercase source; this one breaks the casing and terminology pattern on the same screen.
- `Settings.DisplayTheme.BrightnessThreshold.SectionHeader` — `pt-BR/firefox-ios.xliff` — "Threshold" translated as "Tolerância", inconsistent with "limiar" used for the same term in the section footer.
    - Current: `Tolerância`
    - Source: `Threshold`
    - Suggest: `Limiar`
    - Settings.DisplayTheme.SectionFooter on the same screen translates "threshold" as "limiar"; the header should use the same term.

### E. Typography, punctuation & spacing

- `ContextualHints.FeltDeletion.Body.v122` — `pt-BR/firefox-ios.xliff` — The em dash of the source was replaced by a comma, and the locale convention is the em dash.
    - Current: `cookies, tudo`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `cookies — tudo`
    - Source uses an em dash before "everything"; pt-BR house dash is the em dash, so the punctuation should be preserved.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `pt-BR/firefox-ios.xliff` — Stray capital letter mid-phrase in "Recarregar Ignorando cache".
    - Current: `Recarregar Ignorando cache`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Recarregar ignorando cache`
    - pt-BR uses sentence case in these shortcut labels (see the other entries, e.g. "Limpar histórico recente"); "Ignorando" should not be capitalized mid-sentence.
- `TodayWidget.MoreTabsLabel` — `pt-BR/firefox-ios.xliff` — The "+" sign placement produces "Mais +5…" instead of the intended "+5 mais".
    - Current: `Mais +%d…`
    - Source: `+%d More…`
    - Suggest: `+%d mais…`
    - The developer comment states it becomes something like "+5 more"; placing "Mais" before "+5" reads oddly and capitalizes mid-label.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pt-BR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
