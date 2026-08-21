# Firefox iOS l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | 2026-08-21 @ `7e1ae61658ad` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,906 |

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
| Files | 95 |
| Strings | 1,906 |
| Missing strings | 4 |
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
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**4 strings** are not translated yet, concentrated in:

- `pt-BR/firefox-ios.xliff` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 6, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 6 | **typographic** |
| ellipsis | `char` 19 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 143 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (46)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 31 |
| 3 | Degraded language (grammar, spelling, terminology) | 12 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `pt-BR/firefox-ios.xliff` — "Prefecture" is translated as "Província", duplicating the translation of "Province" in the same form.
    - Current: `Província`
    - Source: `Prefecture`
    - Suggest: `Prefeitura`
    - The source distinguishes "Prefecture" (Japanese administrative division) from "Province"; both are rendered "Província", so the two address fields become indistinguishable on the same screen.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `pt-BR/firefox-ios.xliff` — Analytics trackers count is translated as "Conteúdo com rastreamento" (tracking content), which names a different tracker category.
    - Current: `Conteúdo com rastreamento: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Rastreadores de análise: %@`
    - The developer comment says this row reports how many analytics trackers were blocked; "Conteúdo com rastreamento" is the label for a different ETP category (tracking content) and would duplicate/mislabel this row.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `pt-BR/firefox-ios.xliff` — "you may see" rendered as "deve aparecer" (should/will appear), overstating certainty, and inconsistent with the standard-mode string which uses "pode aparecer".
    - Current: `então deve aparecer uma contagem menor de rastreadores`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `então pode aparecer uma contagem menor de rastreadores`
    - The en-US source says "so you may see a lower tracker count"; the parallel standard-mode string correctly uses "pode aparecer".
- `Menu.EnhancedTrackingProtection.Details.Verifier.v128` — `pt-BR/firefox-ios.xliff` — "Verified by" translated as "Homologado por" (approved/certified by), not the certificate-verification sense.
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The comment states %@ is the SSL certificate signer that verified the site; "homologado" means officially approved, a different concept from certificate verification.
- `MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131` — `pt-BR/firefox-ios.xliff` — "Switch to Desktop Site" is translated as just "Site de computador", dropping the "Switch to" action.
    - Current: `Site de computador`
    - Source: `Switch to Desktop Site`
    - Suggest: `Mudar para site de computador`
    - The source is an action title "Switch to Desktop Site"; the parallel string SwitchToMobileSite.Title.v131 keeps "Mudar para…", and the accessibility label uses "Mudar para site de computador". The current text only names the site type, not the action.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `pt-BR/firefox-ios.xliff` — The button name "Skip" is rendered as "Agora não" ("Not now"), naming a different UI control.
    - Current: `toque em Agora não`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `toque em Pular`
    - The source instructs the user to tap "Skip"; "Agora não" means "Not now", which does not match the referenced button label.
- `Onboarding.IntroDescriptionPart1.v114` — `pt-BR/firefox-ios.xliff` — "For good" (meaning "for the good of all / for good causes") is translated as "Para sempre" ("forever").
    - Current: `Para sempre.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Para o bem.`
    - In this Mozilla tagline, "For good" means for the common good, not "permanently"; "Para sempre" conveys a different meaning.
- `Onboarding.Modern.General.Skip.v145` — `pt-BR/firefox-ios.xliff` — "Skip" is translated as "Agora não" (Not now) instead of "Pular".
    - Current: `Agora não`
    - Source: `Skip`
    - Suggest: `Pular`
    - The source is "Skip" (skip the entire onboarding flow), not "Not Now"; the locale already uses "Agora não" for the distinct "Not Now" strings, so this conflates two different labels.
- `Addresses.Settings.Switch.Description.v124` — `pt-BR/firefox-ios.xliff` — "Includes" rendered as the imperative/infinitive "Incluir" instead of the descriptive "Inclui".
    - Current: `Incluir números de telefone e endereços de email`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Inclui números de telefone e endereços de email`
    - The string is a descriptive subtitle explaining what the toggle covers, not an action; "Includes" is third-person present.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `pt-BR/firefox-ios.xliff` — "pop-ups" was translated as "notificações" (notifications), and the pronoun agreement is wrong.
    - Current: `nem notificações sobre elas`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `nem pop-ups sobre eles`
    - The en-US says "pop-ups about them", referring to the AI enhancements (masculine plural "aprimoramentos"); "notificações" is a different concept and "elas" disagrees in gender.
- `Settings.Rollouts.Message.v148` — `pt-BR/firefox-ios.xliff` — "between updates" was translated as "a cada atualização" (with each update), reversing the meaning.
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
    - The source says changes happen between updates (remotely, without an app update); "a cada atualização" says the opposite — that improvements come with each update.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `pt-BR/firefox-ios.xliff` — The feature name "Firefox Suggest" is rendered as just "Firefox", dropping the product name used elsewhere in the same section.
    - Current: `Mostrar sugestões do Firefox em sessões privativas`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Mostrar sugestões do Sugestões Firefox em sessões privativas`
    - Source is "Show suggestions from Firefox Suggest in private sessions"; other strings on the same screen render Firefox Suggest as "Sugestões Firefox", so this one names the wrong thing.
- `Settings.Summarize.FooterTitle.v142` — `pt-BR/firefox-ios.xliff` — "Provides access" was translated as "Permitir acesso" (allow access), changing the meaning/mood.
    - Current: `Permitir acesso ao recurso de resumir páginas.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Fornece acesso ao recurso de resumir páginas.`
    - The source is a descriptive footer stating that the setting provides access, not an imperative to allow access.
- `ContextualHints.Summarize.Description.v142` — `pt-BR/firefox-ios.xliff` — "Touch and hold" is rendered with an added "mudar para" (switch to) that is not in the source, though the main issue is fine; actually the added wording changes nothing critical.
    - Current: `Mantenha pressionado para mudar para o modo de leitura.`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Mantenha pressionado para o modo de leitura.`
    - The source says "Touch and hold for Reader View."; the target adds "mudar para" (switch to), wording not present in the source.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `pt-BR/firefox-ios.xliff` — "Sync" (button to view synced tabs) is rendered as the adjective "Sincronizado" instead of the noun "Sincronização".
    - Current: `Sincronizado`
    - Source: `Sync`
    - Suggest: `Sincronização`
    - The source "Sync" is a tab-selector title parallel to "Tabs"; pt-BR uses the noun "Sincronização", not the past participle "Sincronizado".
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `pt-BR/firefox-ios.xliff` — "BRONZE FINAL" rendered as "FINAL DO BRONZE", which is not the match name in pt-BR.
    - Current: `FINAL DO BRONZE`
    - Source: `BRONZE FINAL`
    - Suggest: `FINAL DE BRONZE`
    - The phase is the bronze (third-place) final; "FINAL DO BRONZE" reads as 'final of the bronze', an incorrect construction for the match name.
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `pt-BR/firefox-ios.xliff` — "Upcoming" (a match yet to be played) translated as "Seguintes" (following/next ones).
    - Current: `Seguintes`
    - Source: `Upcoming`
    - Suggest: `A seguir`
    - The comment says it labels an upcoming match; "Seguintes" is plural and means 'the following ones', not 'upcoming'.
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `pt-BR/firefox-ios.xliff` — "Make us your default browser" was rendered as "Torne seu navegador padrão", dropping the object "us" and changing the meaning.
    - Current: `Torne seu navegador padrão para ter tranquilidade`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `Defina o Firefox como seu navegador padrão para ter tranquilidade`
    - The source asks the user to make Firefox (us) the default browser; the translation reads as "Make your default browser" with no object, which is incomplete/incorrect.
- `AddPass.Error.Message` — `pt-BR/firefox-ios.xliff` — "Wallet" was rendered as "Passbook" and "pass" as "senha" (password).
    - Current: `Ocorreu um erro ao adicionar a senha no Passbook.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Ocorreu um erro ao adicionar o passe à Carteira.`
    - The source says the pass (a Wallet pass) is being added to Wallet, not a password to Passbook; the sibling string AddPass.Error.Title correctly uses "passe".
- `Block Pop-up Windows` — `pt-BR/firefox-ios.xliff` — Translation adds "ou abas" (or tabs), which is not in the source.
    - Current: `Bloquear abertura de janelas ou abas`
    - Source: `Block Pop-up Windows`
    - Suggest: `Bloquear janelas pop-up`
    - The source is "Block Pop-up Windows"; the target mentions tabs and drops the pop-up concept.
- `CoverSheet.v24.ETP.Description` — `pt-BR/firefox-ios.xliff` — "popups" was translated as "notificações" (notifications) instead of "pop-ups".
    - Current: `anúncios e notificações`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `anúncios e pop-ups`
    - The source says "trackers, ads, and popups"; "notificações" means notifications, a different concept.
- `HomePanel.ContextMenu.Bookmark` — `pt-BR/firefox-ios.xliff` — The verb action "Bookmark" is translated as the plural noun "Favoritos" instead of the action "Adicionar aos favoritos".
    - Current: `Favoritos`
    - Source: `Bookmark`
    - Suggest: `Adicionar aos favoritos`
    - Source is a context menu action to bookmark a site; the sibling string uses "Remover favorito". "Favoritos" names a section rather than the action.
- `Menu.TrackingProtection.Details.Verifier` — `pt-BR/firefox-ios.xliff` — "Verified by" is rendered as "Homologado por" (approved/certified by) instead of "Verificado por".
    - Current: `Homologado por %@`
    - Source: `Verified by %@`
    - Suggest: `Verificado por %@`
    - The source states the site verifier (SSL certificate signer); "homologado" means approved/homologated, not verified.
- `Settings.ClearAllWebsiteData.Clear.Button` — `pt-BR/firefox-ios.xliff` — "All Website Data" translated as data of a single site instead of all websites.
    - Current: `Limpar todos os dados do site`
    - Source: `Clear All Website Data`
    - Suggest: `Limpar todos os dados de sites`
    - The source refers to clearing data of all websites (Data Management screen); "dados do site" implies one specific site.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `pt-BR/firefox-ios.xliff` — "popups" was translated as "notificações" (notifications) instead of "pop-ups".
    - Current: `Bloquear mais rastreadores, anúncios e notificações.`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `Bloquear mais rastreadores, anúncios e pop-ups.`
    - The en-US source says "Blocks more trackers, ads, and popups"; "notificações" means notifications, a different concept.
- `DeleteLoginAlert.Message.Synced.v122` — `pt-BR/firefox-ios.xliff` — Declarative warning turned into an imperative/infinitive phrase, losing the statement of consequence.
    - Current: `Remover esta senha de todos os seus dispositivos sincronizados.`
    - Source: `This will remove the password from all of your synced devices.`
    - Suggest: `Isso removerá a senha de todos os seus dispositivos sincronizados.`
    - The source "This will remove the password from all of your synced devices." is a warning describing what will happen; the translation reads as a command/label "Remove this password from all your synced devices."
- `Menu.ViewDekstopSiteAction.Title` — `pt-BR/firefox-ios.xliff` — "Request Desktop Site" is translated as just "Site de computador", dropping the action verb.
    - Current: `Site de computador`
    - Source: `Request Desktop Site`
    - Suggest: `Solicitar site de computador`
    - The source is an action label ("Request Desktop Site") for a menu button; the translation states only "Desktop site" and omits the request action.
- `Menu.ViewMobileSiteAction.Title` — `pt-BR/firefox-ios.xliff` — "Request Mobile Site" is translated as just "Site de dispositivo móvel", dropping the action verb.
    - Current: `Site de dispositivo móvel`
    - Source: `Request Mobile Site`
    - Suggest: `Solicitar site de dispositivo móvel`
    - The source is an action label ("Request Mobile Site") for a menu button; the translation omits the request action.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `pt-BR/firefox-ios.xliff` — Imperative "Add Firefox shortcuts" rendered as third-person indicative "Adiciona".
    - Current: `Adiciona atalhos do Firefox à tela inicial.`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `Adicione atalhos do Firefox à tela inicial.`
    - The en-US source is an imperative instruction to the user; "Adiciona" is a statement of what the widget does, inconsistent with the imperative in the rest of the same description set.
- `TodayWidget.QuickActionGalleryDescription` — `pt-BR/firefox-ios.xliff` — Imperative "Add a Firefox shortcut" rendered as third-person indicative "Adiciona", inconsistent with the imperatives later in the same string.
    - Current: `Adiciona um atalho do Firefox à tela inicial.`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `Adicione um atalho do Firefox à tela inicial.`
    - The source uses the imperative addressed to the user, and the rest of the same string already uses imperatives ("mantenha pressionado"), so "Adiciona" is inconsistent and wrong.
- `TodayWidget.TopSitesGalleryTitle` — `pt-BR/firefox-ios.xliff` — "Top Sites" rendered as "Sites preferidos" (favorite sites) instead of the frequently/recently visited sites meaning.
    - Current: `Sites preferidos`
    - Source: `Top Sites`
    - Suggest: `Sites mais visitados`
    - Top Sites in Firefox refers to frequently and recently visited sites, as the widget description states, not to user-selected favorites.

### C. Grammar, agreement & spelling

- `CreditCard.ErrorState.NameOnCardSublabel.v112` — `pt-BR/firefox-ios.xliff` — Imperative instruction rendered as an infinitive, unlike the sibling error strings which use the imperative.
    - Current: `Adicionar um nome`
    - Source: `Add a name`
    - Suggest: `Adicione um nome`
    - Source "Add a name" is an instruction to the user, like "Insira uma data..." and "Digite um número..." in the same file; the infinitive reads as a button label instead of an error message.
- `NativeErrorPage.GenericError.Description.v134` — `pt-BR/firefox-ios.xliff` — Missing object pronoun and comma splice make the sentence ungrammatical.
    - Current: `O proprietário de %@ não configurou corretamente, não foi possível criar conexão segura.`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `O proprietário de %@ não configurou o site corretamente e não foi possível criar uma conexão segura.`
    - The en-US "hasn’t set it up properly and a secure connection can’t be created" requires an object and a coordinating conjunction; the current text drops both.
- `Onboarding.Wallpaper.Action.v114` — `pt-BR/firefox-ios.xliff` — "fundo da tela" should be "fundo de tela", inconsistent with the other wallpaper strings in the same screen.
    - Current: `Escolha um fundo da tela`
    - Source: `Set Wallpaper`
    - Suggest: `Escolha um fundo de tela`
    - The other strings in the same group render "wallpaper" as "fundo de tela"; "fundo da tela" is a different (and incorrect) construction.
- `Onboarding.Wallpaper.Title.v114` — `pt-BR/firefox-ios.xliff` — "fundo da tela do %@" uses the wrong term; should be "fundo de tela do %@" for consistency with the other wallpaper strings.
    - Current: `Escolha um fundo da tela do %@`
    - Source: `Choose a %@ Wallpaper`
    - Suggest: `Escolha um fundo de tela do %@`
    - Elsewhere in the same file "wallpaper" is "fundo de tela"; "fundo da tela" is inconsistent and reads as "the screen's background".
- `Settings.AIControls.AIPoweredFeaturesSection.AvailableStatusDescription.v151` — `pt-BR/firefox-ios.xliff` — Duplicated/incorrect wording "você e pode usar" instead of "você pode usar".
    - Current: `O recurso aparece e você e pode usar.`
    - Source: `**Available**: You’ll see the feature and can use it.`
    - Suggest: `O recurso aparece e você pode usar.`
    - The source says "You’ll see the feature and can use it."; the extra "e" makes the sentence ungrammatical.
- `Settings.Studies.Message.v136` — `pt-BR/firefox-ios.xliff` — Agreement error: "antes de ser liberados" should agree in number with "recursos e ideias".
    - Current: `Experimentar recursos e ideias antes de ser liberados para todos.`
    - Source: `Try out features and ideas before they’re released to everyone.`
    - Suggest: `Experimente recursos e ideias antes de serem liberados para todos.`
    - The verb must agree with the plural subject ("recursos e ideias"): "antes de serem liberados".
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `pt-BR/firefox-ios.xliff` — Misplaced hyphen in "OITAVAS-DE FINAL".
    - Current: `OITAVAS-DE FINAL`
    - Source: `ROUND OF 16`
    - Suggest: `OITAVAS DE FINAL`
    - The pt-BR term for 'Round of 16' is "oitavas de final" (matching the sibling string "QUARTAS DE FINAL"); the hyphen after OITAVAS is a spelling error.
- `DefaultBrowserCard.NextLevel.Description.v108` — `pt-BR/firefox-ios.xliff` — Adjective does not agree with the plural list of nouns.
    - Current: `para tornar automático velocidade, segurança e privacidade`
    - Source: `Choose Firefox as your default browser to make speed, safety, and privacy automatic.`
    - Suggest: `para tornar automáticas a velocidade, a segurança e a privacidade`
    - "tornar automático" must agree with the feminine plural nouns (velocidade, segurança, privacidade).
- `Decrease text size` — `pt-BR/firefox-ios.xliff` — Accessibility label rendered as a third-person verb phrase instead of the noun phrase label "Diminuir o tamanho do texto".
    - Current: `Diminui o tamanho do texto`
    - Source: `Decrease text size`
    - Suggest: `Diminuir o tamanho do texto`
    - The source "Decrease text size" is an accessibility label for a button (an action name), which in pt-BR uses the infinitive; "Diminui" is the indicative third person, appropriate for hints, not labels.
- `TodayWidget.TopSitesGalleryDescription` — `pt-BR/firefox-ios.xliff` — Verb conjugated in third person singular instead of the imperative used elsewhere for widget descriptions.
    - Current: `Adiciona atalhos para sites visitados recentemente e com frequência.`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `Adicione atalhos para sites visitados recentemente e com frequência.`
    - The en-US "Add shortcuts to…" is imperative, and the parallel string TodayWidget.QuickViewGalleryDescriptionV2 uses "Adicione"; "Adiciona" is indicative and inconsistent.

### D. Terminology, register & consistency

- `Onboarding.Modern.Customization.Toolbar.Continue.Action.v145` — `pt-BR/firefox-ios.xliff` — "Continue" rendered as "Avançar" while every other Continue button in the same flow uses "Continuar".
    - Current: `Avançar`
    - Source: `Continue`
    - Suggest: `Continuar`
    - Inconsistent with Onboarding.Modern.Customization.Theme.Continue.Action.v140 and the Terms of Use continue button, which both use "Continuar" for the same source term on the same onboarding screens.
- `Settings.DisplayTheme.BrightnessThreshold.SectionHeader` — `pt-BR/firefox-ios.xliff` — "Threshold" rendered as "Tolerância", inconsistent with "limiar" used in the same screen's footer.
    - Current: `Tolerância`
    - Source: `Threshold`
    - Suggest: `Limiar`
    - Settings.DisplayTheme.SectionFooter translates "threshold" as "limiar"; the section header for the same slider should use the same term.

### E. Typography, punctuation & spacing

- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `pt-BR/firefox-ios.xliff` — Label not capitalized like the other round-phase labels.
    - Current: `Fase dos 32`
    - Source: `ROUND OF 32`
    - Suggest: `FASE DOS 32`
    - All sibling round-phase labels (QUARTAS DE FINAL, SEMIFINAIS, TERCEIRO LUGAR) are uppercase, mirroring the all-caps en-US source "ROUND OF 32".
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `pt-BR/firefox-ios.xliff` — Mid-sentence word "Ignorando" is incorrectly capitalized in pt-BR.
    - Current: `Recarregar Ignorando cache`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Recarregar ignorando cache`
    - pt-BR uses sentence case; English title case should not be carried over, and the capital I appears mid-phrase inconsistently with the rest of the translated shortcut labels (e.g. "Limpar histórico recente").
- `When Leaving Private Browsing` — `pt-BR/firefox-ios.xliff` — Setting label starts with a lowercase letter instead of a capital.
    - Current: `ao sair da navegação privativa`
    - Source: `When Leaving Private Browsing`
    - Suggest: `Ao sair da navegação privativa`
    - The source "When Leaving Private Browsing" is a settings label displayed under 'Close Private Tabs'; it should begin with a capital letter.

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
