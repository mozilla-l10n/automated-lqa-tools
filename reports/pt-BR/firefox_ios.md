# Firefox iOS l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-BR: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (57)

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
- `Block Pop-up Windows` — `pt-BR/firefox-ios.xliff` — Translation adds "ou abas" (or tabs), which the source does not say.
    - Current: `Bloquear abertura de janelas ou abas`
    - Source: `Block Pop-up Windows`
    - Suggest: `Bloquear janelas pop-up`
    - The en-US setting is "Block Pop-up Windows"; the target drops "pop-up" and claims tabs are blocked too.
- `Authentication required` — `pt-BR/firefox-ios.xliff` — "Authentication required" rendered as "Requer autenticação" (requires authentication), changing the subject.
    - Current: `Requer autenticação`
    - Source: `Authentication required`
    - Suggest: `Autenticação necessária`
    - The source is a prompt title stating that authentication is required; the target reads as "[it] requires authentication".
- `Decrease text size` — `pt-BR/firefox-ios.xliff` — Accessibility label uses a conjugated verb form instead of the infinitive/noun form used for the action label.
    - Current: `Diminui o tamanho do texto`
    - Source: `Decrease text size`
    - Suggest: `Diminuir o tamanho do texto`
    - The source "Decrease text size" is an imperative/infinitive button label; "Diminui" is the third-person present indicative, which is grammatically wrong for a button accessibility label.
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
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `pt-BR/firefox-ios.xliff` — Stray capital letter mid-phrase in "Recarregar Ignorando cache".
    - Current: `Recarregar Ignorando cache`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Recarregar ignorando cache`
    - pt-BR uses sentence case in these shortcut labels (see the other entries, e.g. "Limpar histórico recente"); "Ignorando" should not be capitalized mid-sentence.
- `Menu.TrackingProtectionBlockedContent.Title` — `pt-BR/firefox-ios.xliff` — "Tracking content" translated as "Conteúdo com rastreamento" instead of the standard "Conteúdo de rastreamento".
    - Current: `Conteúdo com rastreamento`
    - Source: `Tracking content`
    - Suggest: `Conteúdo de rastreamento`
    - The source refers to content that performs tracking (tracking content), not content that has tracking applied to it; Firefox pt-BR uses "Conteúdo de rastreamento".
- `Menu.TrackingProtection.Details.Verifier` — `pt-BR/firefox-ios.xliff` — "Verified by %@" rendered as "Homologado por %@" (approved/certified) instead of "Verificado por %@".
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The source states the SSL certificate signer verified the site; "homologado" means approved/ratified, a different claim.
- `Settings.ClearAllWebsiteData.Clear.Button` — `pt-BR/firefox-ios.xliff` — Plural "Website Data" rendered as singular "dados do site", implying only one site's data is cleared.
    - Current: `Limpar todos os dados do site`
    - Source: `Clear All Website Data`
    - Suggest: `Limpar todos os dados de sites`
    - The source "Clear All Website Data" refers to data from all websites, not a single site; the singular "do site" changes the scope of the action.
- `Settings.DisplayTheme.BrightnessThreshold.SectionHeader` — `pt-BR/firefox-ios.xliff` — "Threshold" translated as "Tolerância", inconsistent with "limiar" used for the same term in the section footer.
    - Current: `Tolerância`
    - Source: `Threshold`
    - Suggest: `Limiar`
    - Settings.DisplayTheme.SectionFooter on the same screen translates "threshold" as "limiar"; the header should use the same term.
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
- `TodayWidget.MoreTabsLabel` — `pt-BR/firefox-ios.xliff` — The "+" sign placement produces "Mais +5…" instead of the intended "+5 mais".
    - Current: `Mais +%d…`
    - Source: `+%d More…`
    - Suggest: `+%d mais…`
    - The developer comment states it becomes something like "+5 more"; placing "Mais" before "+5" reads oddly and capitalizes mid-label.
- `TodayWidget.TopSitesGalleryTitle` — `pt-BR/firefox-ios.xliff` — "Top Sites" translated as "Sites preferidos" (favorite sites) instead of the frequently/recently visited sense used elsewhere.
    - Current: `Sites preferidos`
    - Source: `Top Sites`
    - Suggest: `Sites mais visitados`
    - The widget's own description says it adds shortcuts to frequently and recently visited sites, not user-selected favorites.
- `Bookmarks.Menu.AllBookmarks.v131` — `pt-BR/firefox-ios.xliff` — Back button label "All" (all bookmarks) translated as "Tudo" instead of the plural agreeing with "favoritos".
    - Current: `Tudo`
    - Source: `All`
    - Suggest: `Todos`
    - The comment says this is an `All` (bookmarks) back label; in pt-BR it should agree with "favoritos" ("Todos"), not the neuter "Tudo".
- `ContextualHints.FeltDeletion.Body.v122` — `pt-BR/firefox-ios.xliff` — Imperative sentence rendered in third person singular, breaking the parallel with the preceding imperative.
    - Current: `Exclui o histórico, cookies, tudo.`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `Exclua o histórico, os cookies, tudo.`
    - The source "Delete your history, cookies — everything." is an imperative like the preceding "Tap here"; "Exclui" reads as indicative third person.
- `ContextualHints.FeltDeletion.Body.v122` — `pt-BR/firefox-ios.xliff` — The em dash of the source was replaced by a comma, and the locale convention is the em dash.
    - Current: `cookies, tudo`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `cookies — tudo`
    - Source uses an em dash before "everything"; pt-BR house dash is the em dash, so the punctuation should be preserved.
- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `pt-BR/firefox-ios.xliff` — "Prefecture" is translated as "Província" (province) instead of "Prefeitura".
    - Current: `Província`
    - Source: `Prefecture`
    - Suggest: `Prefeitura`
    - The developer comment specifies the prefecture field used in countries like Japan; "Província" names a different administrative division (province), and pt-BR uses "Prefeitura" for Japanese prefectures.
- `Addresses.EditAddress.AutofillAddressCounty.v129` — `pt-BR/firefox-ios.xliff` — "County" is rendered as "Município", which conflicts with the neighboring "City" field and names the wrong division.
    - Current: `Município`
    - Source: `County`
    - Suggest: `Condado`
    - The comment describes the county field as a distinct administrative division above the city; "Município" means municipality/city and is the standard pt-BR term for a city-level unit, while "County" is "Condado".
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `pt-BR/firefox-ios.xliff` — "you may see" (possibility) rendered as "deve aparecer" (expectation/likelihood), inconsistent with the parallel standard-mode string which uses "pode aparecer".
    - Current: `então deve aparecer uma contagem menor de rastreadores`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `então pode aparecer uma contagem menor de rastreadores`
    - The source says "so you may see a lower tracker count"; "deve" asserts an expected outcome rather than a possibility, and the sibling string translates the identical construction as "pode aparecer".
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `pt-BR/firefox-ios.xliff` — "Conteúdo com rastreamento" translates "Tracking content" but the developer comment says this counts analytics trackers.
    - Current: `Conteúdo com rastreamento: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Conteúdo de rastreamento: %@`
    - Minor wording: Firefox's established term for "Tracking content" in pt-BR is "Conteúdo de rastreamento"; "com rastreamento" deviates from the product's standard terminology used elsewhere in ETP.
- `Menu.EnhancedTrackingProtection.Details.Verifier.v128` — `pt-BR/firefox-ios.xliff` — "Verified by" translated as "Homologado por" (certified/approved) instead of the certificate-verification term.
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The string states which certificate authority verified the site; "homologado" means approved/certified by an authority and is not the standard term for certificate verification.
- `Menu.EnhancedTrackingProtection.Certificates.ValidityNotAfter.v131` — `pt-BR/firefox-ios.xliff` — Inconsistent phrasing between the paired validity labels: "Não após" vs "Não antes de".
    - Current: `Não após`
    - Source: `Not After`
    - Suggest: `Não depois de`
    - "Not After"/"Not Before" are a pair; the two labels use mismatched constructions ("Não após" without preposition vs "Não antes de"), which reads inconsistently on the same screen.
- `CreditCard.ErrorState.NameOnCardSublabel.v112` — `pt-BR/firefox-ios.xliff` — Error message rendered as an infinitive command label instead of an imperative instruction, inconsistent with the sibling error strings.
    - Current: `Adicionar um nome`
    - Source: `Add a name`
    - Suggest: `Adicione um nome`
    - "Add a name" here is an inline error instruction to the user, like "Insira uma data de expiração válida" and "Digite um número de cartão válido" in the same file; the infinitive "Adicionar" reads as a button label and breaks consistency on the same screen.
- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `pt-BR/firefox-ios.xliff` — The action label drops the "Switch to" verb, becoming a noun phrase inconsistent with its counterpart string.
    - Current: `Site de computador`
    - Source: `Switch to Desktop Site`
    - Suggest: `Mudar para versão para computador`
    - en-US is "Switch to Desktop Site", an action; the counterpart string "Switch to Mobile Site" is correctly rendered as "Mudar para versão de dispositivos móveis", so this one omits the action verb and is inconsistent on the same menu.
- `NativeErrorPage.CellularDataRestricted.TitleLabel.v156` — `pt-BR/firefox-ios.xliff` — Subject-verb agreement error: "Dados móveis" is plural but the verb is singular.
    - Current: `Dados móveis está desativado para o %@.`
    - Source: `Cellular data is turned off for %@.`
    - Suggest: `Os dados móveis estão desativados para o %@.`
    - "Dados móveis" is plural in Portuguese, so it requires "estão desativados".
- `DefaultBrowserPopup.DescriptionFooter.v124` — `pt-BR/firefox-ios.xliff` — "tap Skip" was translated as "toque em Agora não" (tap Not now), naming a different button.
    - Current: `toque em Agora não`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `toque em Pular`
    - The source instructs the user to tap the "Skip" button; rendering it as "Agora não" (Not now) points to a different label than the one on screen.
- `NativeErrorPage.GenericError.Description.v134` — `pt-BR/firefox-ios.xliff` — Missing object pronoun and comma splice instead of the coordinating conjunction of the source.
    - Current: `O proprietário de %@ não configurou corretamente, não foi possível criar conexão segura.`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `O proprietário de %@ não o configurou corretamente e não é possível criar uma conexão segura.`
    - The source says the owner "hasn’t set it up properly and a secure connection can’t be created"; the translation drops the object of "configurou" and joins the clauses with a comma instead of "e".
- `Onboarding.IntroDescriptionPart1.v114` — `pt-BR/firefox-ios.xliff` — "For good" (meaning "for the common good") is rendered as "Para sempre" ("forever").
    - Current: `Independente. Sem fins lucrativos. Para sempre.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Independente. Sem fins lucrativos. Para o bem de todos.`
    - In context (indie, non-profit), "For good" means for the benefit of people, not "forever"; the pt-BR asserts a permanence claim the source never made.
- `Onboarding.Modern.General.Skip.v145` — `pt-BR/firefox-ios.xliff` — "Skip" translated as "Agora não" ("Not now") instead of "Pular".
    - Current: `Agora não`
    - Source: `Skip`
    - Suggest: `Pular`
    - The source is "Skip" (button to skip the entire onboarding flow); "Agora não" is the translation used for "Not now" elsewhere in this file, conflating two distinct labels.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `pt-BR/firefox-ios.xliff` — "Browsing just got better" rendered as "Navegar ficou ainda melhor" adds "ainda" (even better), a minor shift; main issue is acceptable — see rationale.
    - Current: `Navegar ficou ainda melhor.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Navegar ficou melhor.`
    - The source says browsing just got better, not "even better"; the added intensifier changes the claim.
- `Onboarding.Notification.Skip.Action.v115` — `pt-BR/firefox-ios.xliff` — "Skip" is translated as "Agora não" (Not now) instead of "Pular"/"Ignorar".
    - Current: `Agora não`
    - Source: `Skip`
    - Suggest: `Pular`
    - The source is "Skip"; "Agora não" corresponds to "Not Now", which is a separate string (Onboarding.Modern.Welcome.Skip) in this same file, creating inconsistency.
- `Onboarding.Modern.Welcome.Title.v140` — `pt-BR/firefox-ios.xliff` — "creepy ads" rendered as "anúncios invasivos" while the phrase "Say goodbye" is dropped; acceptable, but "invasivos" changes the meaning of "creepy".
    - Current: `Chega de anúncios invasivos`
    - Source: `Say goodbye to creepy ads`
    - Suggest: `Diga adeus a anúncios sinistros`
    - The en-US says "Say goodbye to creepy ads"; the sibling v145 string translates the same construction as "Diga adeus a rastreadores sinistros", so the v140 rendering is inconsistent and loses "creepy".
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
- `Settings.Appearance.NavigationToolbar.Description.v145` — `pt-BR/firefox-ios.xliff` — Infinitive "Alterar" used where the source is a descriptive third-person statement "Changes the button".
    - Current: `Alterar o botão no centro da barra de ferramentas.`
    - Source: `Changes the button in the center of the toolbar.`
    - Suggest: `Altera o botão no centro da barra de ferramentas.`
    - The developer comment says this is a section description explaining what the setting does, not an action label; en-US "Changes the button..." is declarative.
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
- `Settings.Studies.Message.v136` — `pt-BR/firefox-ios.xliff` — Agreement error: "antes de ser liberados" should agree in number with "recursos e ideias".
    - Current: `Experimentar recursos e ideias antes de ser liberados para todos.`
    - Source: `Try out features and ideas before they’re released to everyone.`
    - Suggest: `Experimente recursos e ideias antes de serem liberados para todos.`
    - The verb must agree with the plural subject ("recursos e ideias"); "ser" is singular and lacks the pronoun/number agreement required.
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
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `pt-BR/firefox-ios.xliff` — Hyphenation is wrong in "OITAVAS-DE FINAL"; the standard form is "OITAVAS DE FINAL".
    - Current: `OITAVAS-DE FINAL`
    - Source: `ROUND OF 16`
    - Suggest: `OITAVAS DE FINAL`
    - The Portuguese term for "Round of 16" is "oitavas de final" (cf. "QUARTAS DE FINAL" in the sibling string); the misplaced hyphen is a spelling error.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `pt-BR/firefox-ios.xliff` — "ROUND OF 32" rendered in sentence case and with inconsistent phrasing compared to the other round-phase labels.
    - Current: `Fase dos 32`
    - Source: `ROUND OF 32`
    - Suggest: `DEZESSEIS AVOS DE FINAL`
    - All other round-phase labels are uppercase (QUARTAS DE FINAL, SEMIFINAIS, TERCEIRO LUGAR), matching the uppercase source; this one breaks the casing and terminology pattern on the same screen.
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

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (46)

- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Prefecture" is translated as "Província", duplicating the translation of "Province" in the same form.
    - Current: `Província`
    - Suggest: `Prefeitura`
    - The source distinguishes "Prefecture" (Japanese administrative division) from "Province"; both are rendered "Província", so the two address fields become indistinguishable on the same screen.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — Analytics trackers count is translated as "Conteúdo com rastreamento" (tracking content), which names a different tracker category.
    - Current: `Conteúdo com rastreamento: %@`
    - Suggest: `Rastreadores de análise: %@`
    - The developer comment says this row reports how many analytics trackers were blocked; "Conteúdo com rastreamento" is the label for a different ETP category (tracking content) and would duplicate/mislabel this row.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "you may see" rendered as "deve aparecer" (should/will appear), overstating certainty, and inconsistent with the standard-mode string which uses "pode aparecer".
    - Current: `então deve aparecer uma contagem menor de rastreadores`
    - Suggest: `então pode aparecer uma contagem menor de rastreadores`
    - The en-US source says "so you may see a lower tracker count"; the parallel standard-mode string correctly uses "pode aparecer".
- `Menu.EnhancedTrackingProtection.Details.Verifier.v128` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Verified by" translated as "Homologado por" (approved/certified by), not the certificate-verification sense.
    - Current: `Homologado por %@`
    - Suggest: `Verificado por %@`
    - The comment states %@ is the SSL certificate signer that verified the site; "homologado" means officially approved, a different concept from certificate verification.
- `CreditCard.ErrorState.NameOnCardSublabel.v112` — `Shared/Supporting Files/en.lproj/ErrorState.strings` — Imperative instruction rendered as an infinitive, unlike the sibling error strings which use the imperative.
    - Current: `Adicionar um nome`
    - Suggest: `Adicione um nome`
    - Source "Add a name" is an instruction to the user, like "Insira uma data..." and "Digite um número..." in the same file; the infinitive reads as a button label instead of an error message.
- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Switch to Desktop Site" is translated as just "Site de computador", dropping the "Switch to" action.
    - Current: `Site de computador`
    - Suggest: `Mudar para site de computador`
    - The source is an action title "Switch to Desktop Site"; the parallel string SwitchToMobileSite.Title.v131 keeps "Mudar para…", and the accessibility label uses "Mudar para site de computador". The current text only names the site type, not the action.
- `NativeErrorPage.GenericError.Description.v134` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Missing object pronoun and comma splice make the sentence ungrammatical.
    - Current: `O proprietário de %@ não configurou corretamente, não foi possível criar conexão segura.`
    - Suggest: `O proprietário de %@ não configurou o site corretamente e não foi possível criar uma conexão segura.`
    - The en-US "hasn’t set it up properly and a secure connection can’t be created" requires an object and a coordinating conjunction; the current text drops both.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The button name "Skip" is rendered as "Agora não" ("Not now"), naming a different UI control.
    - Current: `toque em Agora não`
    - Suggest: `toque em Pular`
    - The source instructs the user to tap "Skip"; "Agora não" means "Not now", which does not match the referenced button label.
- `Onboarding.IntroDescriptionPart1.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "For good" (meaning "for the good of all / for good causes") is translated as "Para sempre" ("forever").
    - Current: `Para sempre.`
    - Suggest: `Para o bem.`
    - In this Mozilla tagline, "For good" means for the common good, not "permanently"; "Para sempre" conveys a different meaning.
- `Onboarding.Modern.Customization.Toolbar.Continue.Action.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Continue" rendered as "Avançar" while every other Continue button in the same flow uses "Continuar".
    - Current: `Avançar`
    - Suggest: `Continuar`
    - Inconsistent with Onboarding.Modern.Customization.Theme.Continue.Action.v140 and the Terms of Use continue button, which both use "Continuar" for the same source term on the same onboarding screens.
- `Onboarding.Modern.General.Skip.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Skip" is translated as "Agora não" (Not now) instead of "Pular".
    - Current: `Agora não`
    - Suggest: `Pular`
    - The source is "Skip" (skip the entire onboarding flow), not "Not Now"; the locale already uses "Agora não" for the distinct "Not Now" strings, so this conflates two different labels.
- `Onboarding.Wallpaper.Action.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "fundo da tela" should be "fundo de tela", inconsistent with the other wallpaper strings in the same screen.
    - Current: `Escolha um fundo da tela`
    - Suggest: `Escolha um fundo de tela`
    - The other strings in the same group render "wallpaper" as "fundo de tela"; "fundo da tela" is a different (and incorrect) construction.
- `Onboarding.Wallpaper.Title.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "fundo da tela do %@" uses the wrong term; should be "fundo de tela do %@" for consistency with the other wallpaper strings.
    - Current: `Escolha um fundo da tela do %@`
    - Suggest: `Escolha um fundo de tela do %@`
    - Elsewhere in the same file "wallpaper" is "fundo de tela"; "fundo da tela" is inconsistent and reads as "the screen's background".
- `Addresses.Settings.Switch.Description.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Includes" rendered as the imperative/infinitive "Incluir" instead of the descriptive "Inclui".
    - Current: `Incluir números de telefone e endereços de email`
    - Suggest: `Inclui números de telefone e endereços de email`
    - The string is a descriptive subtitle explaining what the toggle covers, not an action; "Includes" is third-person present.
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatusDescription.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — Duplicated/incorrect wording "você e pode usar" instead of "você pode usar".
    - Current: `O recurso aparece e você e pode usar.`
    - Suggest: `O recurso aparece e você pode usar.`
    - The source says "You’ll see the feature and can use it."; the extra "e" makes the sentence ungrammatical.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "pop-ups" was translated as "notificações" (notifications), and the pronoun agreement is wrong.
    - Current: `nem notificações sobre elas`
    - Suggest: `nem pop-ups sobre eles`
    - The en-US says "pop-ups about them", referring to the AI enhancements (masculine plural "aprimoramentos"); "notificações" is a different concept and "elas" disagrees in gender.
- `Settings.Rollouts.Message.v148` — `Shared/Supporting Files/en.lproj/Settings.strings` — "between updates" was translated as "a cada atualização" (with each update), reversing the meaning.
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
    - The source says changes happen between updates (remotely, without an app update); "a cada atualização" says the opposite — that improvements come with each update.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `Shared/Supporting Files/en.lproj/Settings.strings` — The feature name "Firefox Suggest" is rendered as just "Firefox", dropping the product name used elsewhere in the same section.
    - Current: `Mostrar sugestões do Firefox em sessões privativas`
    - Suggest: `Mostrar sugestões do Sugestões Firefox em sessões privativas`
    - Source is "Show suggestions from Firefox Suggest in private sessions"; other strings on the same screen render Firefox Suggest as "Sugestões Firefox", so this one names the wrong thing.
- `Settings.Studies.Message.v136` — `Shared/Supporting Files/en.lproj/Settings.strings` — Agreement error: "antes de ser liberados" should agree in number with "recursos e ideias".
    - Current: `Experimentar recursos e ideias antes de ser liberados para todos.`
    - Suggest: `Experimente recursos e ideias antes de serem liberados para todos.`
    - The verb must agree with the plural subject ("recursos e ideias"): "antes de serem liberados".
- `Settings.Summarize.FooterTitle.v142` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Provides access" was translated as "Permitir acesso" (allow access), changing the meaning/mood.
    - Current: `Permitir acesso ao recurso de resumir páginas.`
    - Suggest: `Fornece acesso ao recurso de resumir páginas.`
    - The source is a descriptive footer stating that the setting provides access, not an imperative to allow access.
- `ContextualHints.Summarize.Description.v142` — `Shared/Supporting Files/en.lproj/Summarize.strings` — "Touch and hold" is rendered with an added "mudar para" (switch to) that is not in the source, though the main issue is fine; actually the added wording changes nothing critical.
    - Current: `Mantenha pressionado para mudar para o modo de leitura.`
    - Suggest: `Mantenha pressionado para o modo de leitura.`
    - The source says "Touch and hold for Reader View."; the target adds "mudar para" (switch to), wording not present in the source.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `Shared/Supporting Files/en.lproj/TabsTray.strings` — "Sync" (button to view synced tabs) is rendered as the adjective "Sincronizado" instead of the noun "Sincronização".
    - Current: `Sincronizado`
    - Suggest: `Sincronização`
    - The source "Sync" is a tab-selector title parallel to "Tabs"; pt-BR uses the noun "Sincronização", not the past participle "Sincronizado".
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "BRONZE FINAL" rendered as "FINAL DO BRONZE", which is not the match name in pt-BR.
    - Current: `FINAL DO BRONZE`
    - Suggest: `FINAL DE BRONZE`
    - The phase is the bronze (third-place) final; "FINAL DO BRONZE" reads as 'final of the bronze', an incorrect construction for the match name.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — Misplaced hyphen in "OITAVAS-DE FINAL".
    - Current: `OITAVAS-DE FINAL`
    - Suggest: `OITAVAS DE FINAL`
    - The pt-BR term for 'Round of 16' is "oitavas de final" (matching the sibling string "QUARTAS DE FINAL"); the hyphen after OITAVAS is a spelling error.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — Label not capitalized like the other round-phase labels.
    - Current: `Fase dos 32`
    - Suggest: `FASE DOS 32`
    - All sibling round-phase labels (QUARTAS DE FINAL, SEMIFINAIS, TERCEIRO LUGAR) are uppercase, mirroring the all-caps en-US source "ROUND OF 32".
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Upcoming" (a match yet to be played) translated as "Seguintes" (following/next ones).
    - Current: `Seguintes`
    - Suggest: `A seguir`
    - The comment says it labels an upcoming match; "Seguintes" is plural and means 'the following ones', not 'upcoming'.
- `DefaultBrowserCard.NextLevel.Description.v108` — `Shared/en.lproj/Default Browser.strings` — Adjective does not agree with the plural list of nouns.
    - Current: `para tornar automático velocidade, segurança e privacidade`
    - Suggest: `para tornar automáticas a velocidade, a segurança e a privacidade`
    - "tornar automático" must agree with the feminine plural nouns (velocidade, segurança, privacidade).
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `Shared/en.lproj/Default Browser.strings` — "Make us your default browser" was rendered as "Torne seu navegador padrão", dropping the object "us" and changing the meaning.
    - Current: `Torne seu navegador padrão para ter tranquilidade`
    - Suggest: `Defina o Firefox como seu navegador padrão para ter tranquilidade`
    - The source asks the user to make Firefox (us) the default browser; the translation reads as "Make your default browser" with no object, which is incomplete/incorrect.
- `AddPass.Error.Message` — `Shared/en.lproj/Localizable.strings` — "Wallet" was rendered as "Passbook" and "pass" as "senha" (password).
    - Current: `Ocorreu um erro ao adicionar a senha no Passbook.`
    - Suggest: `Ocorreu um erro ao adicionar o passe à Carteira.`
    - The source says the pass (a Wallet pass) is being added to Wallet, not a password to Passbook; the sibling string AddPass.Error.Title correctly uses "passe".
- `Block Pop-up Windows` — `Shared/en.lproj/Localizable.strings` — Translation adds "ou abas" (or tabs), which is not in the source.
    - Current: `Bloquear abertura de janelas ou abas`
    - Suggest: `Bloquear janelas pop-up`
    - The source is "Block Pop-up Windows"; the target mentions tabs and drops the pop-up concept.
- `CoverSheet.v24.ETP.Description` — `Shared/en.lproj/Localizable.strings` — "popups" was translated as "notificações" (notifications) instead of "pop-ups".
    - Current: `anúncios e notificações`
    - Suggest: `anúncios e pop-ups`
    - The source says "trackers, ads, and popups"; "notificações" means notifications, a different concept.
- `Decrease text size` — `Shared/en.lproj/Localizable.strings` — Accessibility label rendered as a third-person verb phrase instead of the noun phrase label "Diminuir o tamanho do texto".
    - Current: `Diminui o tamanho do texto`
    - Suggest: `Diminuir o tamanho do texto`
    - The source "Decrease text size" is an accessibility label for a button (an action name), which in pt-BR uses the infinitive; "Diminui" is the indicative third person, appropriate for hints, not labels.
- `HomePanel.ContextMenu.Bookmark` — `Shared/en.lproj/Localizable.strings` — The verb action "Bookmark" is translated as the plural noun "Favoritos" instead of the action "Adicionar aos favoritos".
    - Current: `Favoritos`
    - Suggest: `Adicionar aos favoritos`
    - Source is a context menu action to bookmark a site; the sibling string uses "Remover favorito". "Favoritos" names a section rather than the action.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `Shared/en.lproj/Localizable.strings` — Mid-sentence word "Ignorando" is incorrectly capitalized in pt-BR.
    - Current: `Recarregar Ignorando cache`
    - Suggest: `Recarregar ignorando cache`
    - pt-BR uses sentence case; English title case should not be carried over, and the capital I appears mid-phrase inconsistently with the rest of the translated shortcut labels (e.g. "Limpar histórico recente").
- `Menu.TrackingProtection.Details.Verifier` — `Shared/en.lproj/Localizable.strings` — "Verified by" is rendered as "Homologado por" (approved/certified by) instead of "Verificado por".
    - Current: `Homologado por %@`
    - Suggest: `Verificado por %@`
    - The source states the site verifier (SSL certificate signer); "homologado" means approved/homologated, not verified.
- `Settings.ClearAllWebsiteData.Clear.Button` — `Shared/en.lproj/Localizable.strings` — "All Website Data" translated as data of a single site instead of all websites.
    - Current: `Limpar todos os dados do site`
    - Suggest: `Limpar todos os dados de sites`
    - The source refers to clearing data of all websites (Data Management screen); "dados do site" implies one specific site.
- `Settings.DisplayTheme.BrightnessThreshold.SectionHeader` — `Shared/en.lproj/Localizable.strings` — "Threshold" rendered as "Tolerância", inconsistent with "limiar" used in the same screen's footer.
    - Current: `Tolerância`
    - Suggest: `Limiar`
    - Settings.DisplayTheme.SectionFooter translates "threshold" as "limiar"; the section header for the same slider should use the same term.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `Shared/en.lproj/Localizable.strings` — "popups" was translated as "notificações" (notifications) instead of "pop-ups".
    - Current: `Bloquear mais rastreadores, anúncios e notificações.`
    - Suggest: `Bloquear mais rastreadores, anúncios e pop-ups.`
    - The en-US source says "Blocks more trackers, ads, and popups"; "notificações" means notifications, a different concept.
- `DeleteLoginAlert.Message.Synced.v122` — `Shared/en.lproj/LoginManager.strings` — Declarative warning turned into an imperative/infinitive phrase, losing the statement of consequence.
    - Current: `Remover esta senha de todos os seus dispositivos sincronizados.`
    - Suggest: `Isso removerá a senha de todos os seus dispositivos sincronizados.`
    - The source "This will remove the password from all of your synced devices." is a warning describing what will happen; the translation reads as a command/label "Remove this password from all your synced devices."
- `Menu.ViewDekstopSiteAction.Title` — `Shared/en.lproj/Menu.strings` — "Request Desktop Site" is translated as just "Site de computador", dropping the action verb.
    - Current: `Site de computador`
    - Suggest: `Solicitar site de computador`
    - The source is an action label ("Request Desktop Site") for a menu button; the translation states only "Desktop site" and omits the request action.
- `Menu.ViewMobileSiteAction.Title` — `Shared/en.lproj/Menu.strings` — "Request Mobile Site" is translated as just "Site de dispositivo móvel", dropping the action verb.
    - Current: `Site de dispositivo móvel`
    - Suggest: `Solicitar site de dispositivo móvel`
    - The source is an action label ("Request Mobile Site") for a menu button; the translation omits the request action.
- `When Leaving Private Browsing` — `Shared/en.lproj/PrivateBrowsing.strings` — Setting label starts with a lowercase letter instead of a capital.
    - Current: `ao sair da navegação privativa`
    - Suggest: `Ao sair da navegação privativa`
    - The source "When Leaving Private Browsing" is a settings label displayed under 'Close Private Tabs'; it should begin with a capital letter.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `Shared/en.lproj/Today.strings` — Imperative "Add Firefox shortcuts" rendered as third-person indicative "Adiciona".
    - Current: `Adiciona atalhos do Firefox à tela inicial.`
    - Suggest: `Adicione atalhos do Firefox à tela inicial.`
    - The en-US source is an imperative instruction to the user; "Adiciona" is a statement of what the widget does, inconsistent with the imperative in the rest of the same description set.
- `TodayWidget.QuickActionGalleryDescription` — `Shared/en.lproj/Today.strings` — Imperative "Add a Firefox shortcut" rendered as third-person indicative "Adiciona", inconsistent with the imperatives later in the same string.
    - Current: `Adiciona um atalho do Firefox à tela inicial.`
    - Suggest: `Adicione um atalho do Firefox à tela inicial.`
    - The source uses the imperative addressed to the user, and the rest of the same string already uses imperatives ("mantenha pressionado"), so "Adiciona" is inconsistent and wrong.
- `TodayWidget.TopSitesGalleryDescription` — `Shared/en.lproj/Today.strings` — Verb conjugated in third person singular instead of the imperative used elsewhere for widget descriptions.
    - Current: `Adiciona atalhos para sites visitados recentemente e com frequência.`
    - Suggest: `Adicione atalhos para sites visitados recentemente e com frequência.`
    - The en-US "Add shortcuts to…" is imperative, and the parallel string TodayWidget.QuickViewGalleryDescriptionV2 uses "Adicione"; "Adiciona" is indicative and inconsistent.
- `TodayWidget.TopSitesGalleryTitle` — `Shared/en.lproj/Today.strings` — "Top Sites" rendered as "Sites preferidos" (favorite sites) instead of the frequently/recently visited sites meaning.
    - Current: `Sites preferidos`
    - Suggest: `Sites mais visitados`
    - Top Sites in Firefox refers to frequently and recently visited sites, as the widget description states, not to user-selected favorites.

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,922 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 6, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 6 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 143 | **informal** |

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
