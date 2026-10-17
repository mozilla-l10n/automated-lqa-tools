# Firefox iOS l10n QA — pt-PT

| | |
|---|---|
| **Generated** | 2026-10-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-PT: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,927 |
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
| quotes | `curly-single` 10, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 10 | **typographic** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 1, `en` 4 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (65)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Keyboard.Shortcuts.ClearRecentHistory` — `pt-PT/firefox-ios.xliff` — "Recent" is dropped, so the label says it clears the whole history.
    - Current: `Limpar histórico`
    - Source: `Clear Recent History`
    - Suggest: `Limpar histórico recente`
    - The source and comment say the shortcut clears recent history. "Limpar histórico" claims a wider deletion than the action performs.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 17 |
| 3 | Degraded language (grammar, spelling, terminology) | 35 |
| 4 | Cosmetic (typography, spacing) | 13 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `pt-PT/firefox-ios.xliff` — The translation says Firefox lets the user use the microphone, not that Firefox uses it to record and upload audio.
    - Current: `O Firefox permite-lhe usar o seu microfone para gravar e carregar áudio.`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `O Firefox utiliza o seu microfone para gravar e carregar áudio.`
    - The en-US 'Firefox uses your microphone to record and upload audio' is a permission justification saying the app uses the mic. The pt-PT 'permite-lhe usar' ('lets you use') makes the user the one acting, so it no longer explains why the app needs the permission.
- `Addresses.EditAddress.AutofillAddressCounty.v129` — `pt-PT/firefox-ios.xliff` — "County" is translated as "País" (country), which is wrong.
    - Current: `País`
    - Source: `County`
    - Suggest: `Condado`
    - The source and comment describe a county field (an administrative division). "País" means country, so the label is wrong and looks the same as the Country field.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `pt-PT/firefox-ios.xliff` — "Townland" is translated as "Cidade" (city), which is wrong and collides with the City label.
    - Current: `Cidade`
    - Source: `Townland`
    - Suggest: `Localidade`
    - The comment describes a townland as a rural land division. "Cidade" means city and is already the translation of the City field, so a form that shows both would have two identical labels.
- `QuickAnswers.PrivacyBanner.Description.v158` — `pt-PT/firefox-ios.xliff` — The last item in the list has no negation, so the text literally says the app uses your voice to identify you.
    - Current: `ou utiliza a sua voz para o identificar`
    - Source: `%@ doesn’t store your audio or questions, use your data to train AI models, or use your voice to identify you.`
    - Suggest: `nem utiliza a sua voz para o identificar`
    - The source negates all three items (doesn't store, doesn't use for training, doesn't use voice to identify). Here 'não' is repeated only for the first two, and the third clause 'ou utiliza' is affirmative in Portuguese. It needs 'nem'.
- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `pt-PT/firefox-ios.xliff` — The brand 'Relay' is lowercased and split from the product name '%@ Relay'.
    - Current: `máscaras de e-mail relay do %@`
    - Source: `New! %@ Relay email masks are now available on mobile.`
    - Suggest: `máscaras de e-mail do %@ Relay`
    - '%@ Relay' (Firefox Relay) is a product name. Lowercase 'relay' reads as an ordinary word and breaks the brand.
- `RelayMask.RelayEmailMaskGenericErrorMessage.v146` — `pt-PT/firefox-ios.xliff` — 'ainda não' (not yet) turns a temporary error into a claim that the feature isn't available yet.
    - Current: `ainda não estão disponíveis`
    - Source: `Email masks aren’t available right now. Try again in a few minutes.`
    - Suggest: `não estão disponíveis neste momento`
    - The source 'aren't available right now' describes a temporary error, per the developer comment. 'ainda não' means 'not yet'.
- `Settings.Autoplay.Footer.v137` — `pt-PT/firefox-ios.xliff` — "Changes cannot be applied" is rendered as "changes may not be applied", which softens a definite statement into a possibility.
    - Current: `As alterações podem não ser aplicadas`
    - Source: `Autoplay settings will only apply to newly opened tabs. Changes cannot be applied to existing tabs unless the application is restarted.`
    - Suggest: `As alterações não podem ser aplicadas`
    - The en-US says existing tabs cannot get the changes without a restart. The translation says they might not, so the user is left thinking it could work.
- `ContextMenu.DownloadLinkButtonTitle` — `pt-PT/firefox-ios.xliff` — The menu action "Download Link" was translated as a noun phrase meaning "a download link".
    - Current: `Ligação de transferência`
    - Source: `Download Link`
    - Suggest: `Transferir ligação`
    - The developer comment says this is a context menu item for downloading a link URL, so "Download" is a verb. "Ligação de transferência" names an object instead of an action, unlike sibling items such as "Copiar ligação" and "Partilhar ligação".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `pt-PT/firefox-ios.xliff` — "Tab pickup" is rendered as "Escolha de separador" (choice of tab) instead of conveying resuming a synced tab.
    - Current: `Escolha de separador`
    - Source: `Tab pickup`
    - Suggest: `Retomar separador`
    - Per the developer comment, the label marks the cell showing the most recent tab from another device, so the user can pick up where they left off. "Escolha" means selection/choice, which is a different meaning.
- `Keyboard.Shortcuts.ClearRecentHistory` — `pt-PT/firefox-ios.xliff` — "Recent" is dropped, so the label says it clears the whole history.
    - Current: `Limpar histórico`
    - Source: `Clear Recent History`
    - Suggest: `Limpar histórico recente`
    - The source and comment say the shortcut clears recent history. "Limpar histórico" claims a wider deletion than the action performs.
- `Keyboard.Shortcuts.ShowBookmarks` — `pt-PT/firefox-ios.xliff` — "Show Bookmarks" is translated as "New bookmarks".
    - Current: `Novos marcadores`
    - Source: `Show Bookmarks`
    - Suggest: `Mostrar marcadores`
    - The en-US and the comment describe a shortcut that shows all bookmarks, but "Novos marcadores" means "New bookmarks".
- `Keyboard.Shortcuts.ShowDownloads` — `pt-PT/firefox-ios.xliff` — "Show Downloads" is translated as "No downloads".
    - Current: `Nenhuma transferência`
    - Source: `Show Downloads`
    - Suggest: `Mostrar transferências`
    - The shortcut shows all downloads, but "Nenhuma transferência" means "No download", which reads as an empty-state message rather than an action.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `pt-PT/firefox-ios.xliff` — The translation drops "and computer", so only browser settings are described as unique.
    - Current: `As definições do seu navegador são únicas.`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `As definições do seu navegador e computador são únicas.`
    - The source says "The settings on your browser and computer are unique". Leaving out the computer narrows what fingerprinters are described as collecting.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `pt-PT/firefox-ios.xliff` — "popups" is rendered as "outras janelas" (other windows) instead of pop-up windows.
    - Current: `outras janelas`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `janelas pop-up`
    - The source says strict mode blocks popups. "Outras janelas" means "other windows", which doesn't say what gets blocked.
- `read` — `pt-PT/firefox-ios.xliff` — Past participle 'read' translated as the infinitive 'ler' instead of the adjective 'lido'.
    - Current: `ler`
    - Source: `read`
    - Suggest: `lido`
    - The developer comment says this is a past participle working as an adjective (the article has been read). 'ler' is the verb 'to read', so the accessibility label says the wrong thing. It also doesn't match 'não lido' for unread.
- `Search Input Field` — `pt-PT/firefox-ios.xliff` — The accessibility label for the search field is translated as an instruction ("Search in the input field"), not as the name of the field.
    - Current: `Pesquisar no campo de inserção`
    - Source: `Search Input Field`
    - Suggest: `Campo de pesquisa`
    - The en-US "Search Input Field" names a UI element for VoiceOver. The pt-PT reads as a verb phrase meaning "search in the input field", so screen-reader users hear an instruction where they should hear what the element is.
- `Menu.NewPrivateTabAction.Title` — `pt-PT/firefox-ios.xliff` — "Open New Private Tab" is translated as "Open in a new private tab", as if it opened content inside the tab instead of opening a new private tab.
    - Current: `Abrir num novo separador privado`
    - Source: `Open New Private Tab`
    - Suggest: `Abrir novo separador privado`
    - The comment says the button opens a new private tab. "Abrir num novo separador privado" means "open in a new private tab", which is the wording of the separate link context-menu option.
- `Menu.NewTabAction.Title` — `pt-PT/firefox-ios.xliff` — "Open New Tab" is translated as "Open in a new tab", so the menu item seems to open something inside a new tab instead of opening a new tab.
    - Current: `Abrir num novo separador`
    - Source: `Open New Tab`
    - Suggest: `Abrir novo separador`
    - The comment says the button opens a new tab. "Abrir num novo separador" means "open in a new tab", which suggests the current page or a link will open there. That wording belongs to the context-menu string, not to this menu action.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.AppIconNames.Midnight.Title.v137` — `pt-PT/firefox-ios.xliff` — "Meia noite" is missing its hyphen; the correct spelling is "Meia-noite".
    - Current: `Meia noite`
    - Source: `Midnight`
    - Suggest: `Meia-noite`
    - In pt-PT, the word for midnight is the hyphenated compound "meia-noite". The sibling string on the same screen correctly uses "Meio-dia", so this one is also inconsistent with it.
- `BrowserDataTransfer.ImportSuccess.Title.v160` — `pt-PT/firefox-ios.xliff` — Copies the English word order, so the title is ungrammatical ("Safari Importação Concluída").
    - Current: `%@ Importação Concluída`
    - Source: `%@ Import Complete`
    - Suggest: `Importação de %@ concluída`
    - In Portuguese the browser name has to follow the noun with "de". Putting the name first does not form a grammatical phrase.
- `CameraAccess.DisabledAlertMessage.v153` — `pt-PT/firefox-ios.xliff` — The preposition "a" is wrongly capitalised in the middle of the sentence.
    - Current: `Aceda A Definições`
    - Source: `Go to Settings > %@ on your device to allow Firefox to use your camera.`
    - Suggest: `Aceda a Definições`
    - "A" here is a lowercase preposition and should not be capitalised in running text.
- `Engagement.Notification.Body.v112` — `pt-PT/firefox-ios.xliff` — "qualquer divertida" is ungrammatical: it has no noun, and "divertida" is feminine where the masculine "divertido" is needed.
    - Current: `Ou descubra qualquer divertida.`
    - Source: `Find something nearby. Or discover something fun.`
    - Suggest: `Ou descubra algo divertido.`
    - The en-US says "discover something fun". "qualquer divertida" is not valid Portuguese. It should be "algo divertido", which also matches the "algo próximo" in the first sentence.
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v153b` — `pt-PT/firefox-ios.xliff` — 'Bloqueados' is capitalized because the string copies English title case.
    - Current: `Rastreadores Bloqueados: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `Rastreadores bloqueados: %@`
    - Portuguese UI text uses sentence case. The other homepage strings do, for example 'Adicionar atalho'.
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v155` — `pt-PT/firefox-ios.xliff` — 'Bloqueados' is capitalized because the string copies English title case.
    - Current: `Rastreadores Bloqueados: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `Rastreadores bloqueados: %@`
    - Portuguese UI text uses sentence case. The other homepage strings do, for example 'Adicionar atalho'.
- `GoogleLens.Interstitial.LoadingLabel.v156` — `pt-PT/firefox-ios.xliff` — This label copies English title case, which Portuguese doesn't use.
    - Current: `A Procurar Resultados de Imagens…`
    - Source: `Finding Image Results…`
    - Suggest: `A procurar resultados de imagens…`
    - Portuguese uses sentence case for UI labels. The other pt-PT strings follow this, for example 'Adicionar atalho' and 'Ver separadores fechados recentemente'.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `pt-PT/firefox-ios.xliff` — "Sub-menu" is misspelled; the standard pt-PT spelling is "submenu".
    - Current: `Sub-menu Guardar`
    - Source: `Save submenu`
    - Suggest: `Submenu Guardar`
    - Under current Portuguese spelling rules, the prefix "sub-" only takes a hyphen before b, h or r. "Submenu" is written as one word.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `pt-PT/firefox-ios.xliff` — "Sub-menu" is misspelled; the standard pt-PT spelling is "submenu".
    - Current: `Sub-menu Ferramentas`
    - Source: `Tools submenu`
    - Suggest: `Submenu Ferramentas`
    - Under current Portuguese spelling rules, the prefix "sub-" only takes a hyphen before b, h or r. "Submenu" is written as one word.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `pt-PT/firefox-ios.xliff` — The phrase "on a corporate network" is missing its preposition, so the sentence is ungrammatical.
    - Current: `Se está uma rede empresarial`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `Se está numa rede empresarial`
    - The en-US says "If you're on a corporate network". Portuguese needs the contraction "numa" (em + uma) here. Without it, "Se está uma rede empresarial" is ungrammatical.
- `TermsOfUse.ReviewAndAcceptText.v142` — `pt-PT/firefox-ios.xliff` — "despender" takes a direct object; "despenda de um momento" is ungrammatical.
    - Current: `despenda de um momento`
    - Source: `Please take a moment to review and accept. Learn more`
    - Suggest: `despenda um momento`
    - The correct construction is "despender um momento" with no preposition. The "de" is a grammar error.
- `WebCompatReporter.Preview.Data.PixelDensity.v155` — `pt-PT/firefox-ios.xliff` — The plural of "píxel" is missing its accent: it should be "píxeis", not "pixeis".
    - Current: `Densidade de pixeis`
    - Source: `Your screen’s pixel density`
    - Suggest: `Densidade de píxeis`
    - In Portuguese, "píxel" is stressed on the second-to-last syllable and ends in -el, so it takes an accent, and so does its plural "píxeis" (like fácil/fáceis). I believe Mozilla's pt-PT uses "píxeis" (not checked).
- `DefaultBrowserCard.BetterInternet.Title.v108` — `pt-PT/firefox-ios.xliff` — The title uses the Brazilian "padrão", the phrasing is ungrammatical, and every word is capitalised.
    - Current: `Por padrão uma Internet Melhor`
    - Source: `Default to a Better Internet`
    - Suggest: `Predefina uma Internet melhor`
    - "Por padrão uma Internet Melhor" does not form a coherent Portuguese phrase. "padrão" is pt-BR, unlike the file's "predefinido". The other titles in the file use sentence case.
- `ContextualHints.TabTray.InactiveTabs` — `pt-PT/firefox-ios.xliff` — The relative clause leaves out the preposition that the verb "aceder" requires.
    - Current: `Os separadores que não acede`
    - Source: `Tabs you haven’t viewed for two weeks get moved here.`
    - Suggest: `Os separadores a que não acede`
    - "Aceder" takes its object with the preposition "a", so the relative clause must be "a que não acede".
- `FirefoxHome.Stories.Minutes.v140` — `pt-PT/firefox-ios.xliff` — Minutes are abbreviated as "mín.", which in Portuguese is the abbreviation for "mínimo" rather than minutes.
    - Current: `mín.: %d`
    - Source: `min: %d`
    - Suggest: `min: %d`
    - The standard Portuguese abbreviation/symbol for minutes is "min", with no accent or full stop. "mín." reads as "mínimo" (minimum), so "mín.: 5" suggests "minimum: 5".
- `Settings.DisplayTheme.SectionFooter` — `pt-PT/firefox-ios.xliff` — The infinitive "alterar" is used where a conjugated verb is needed.
    - Current: `em que o tema alterar`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `em que o tema muda`
    - "o limite em que o tema alterar" is ungrammatical. The relative clause needs a finite verb, e.g. "em que o tema muda".
- `Settings.DisplayTheme.SectionFooter` — `pt-PT/firefox-ios.xliff` — The intransitive sense of "alterar" needs the reflexive pronoun.
    - Current: `O tema irá alterar automaticamente`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `O tema irá alterar-se automaticamente`
    - The theme changes by itself, so pt-PT needs the pronominal form "alterar-se". Without it, "alterar" is transitive and has no object.
- `Settings.DisplayTheme.SectionFooter` — `pt-PT/firefox-ios.xliff` — "circulo" is missing its accent.
    - Current: `O circulo`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `O círculo`
    - The noun is spelled "círculo". "circulo" is the verb form "I circulate".

### D. Terminology, register & consistency

- `ContextualHints.Translations.Body.v145` — `pt-PT/firefox-ios.xliff` — Uses the Brazilian "você", which breaks the pt-PT form of address.
    - Current: `quando você estiver`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `quando estiver`
    - pt-PT addresses the user with the implicit formal third person ("Toque", "Utilize") and leaves out the subject. "Você" is pt-BR usage.
- `CredentialProvider.RetryAllert.Title.v137` — `pt-PT/firefox-ios.xliff` — The title says "auto-preenchimento" but the message of the same alert says "preenchimento automático", and the hyphenated form is outdated spelling.
    - Current: `Erro de auto-preenchimento`
    - Source: `Autofill Error`
    - Suggest: `Erro de preenchimento automático`
    - The same term appears twice on one alert and should match. The message's "preenchimento automático" is the standard form.
- `NativeErrorPage.Wayback.Error.Title.v154` — `pt-PT/firefox-ios.xliff` — Title uses the Brazilian verb "conectar" and a calqued "Incapaz de" instead of the pt-PT "ligar" used throughout this screen.
    - Current: `Incapaz de conectar`
    - Source: `Unable to connect`
    - Suggest: `Não foi possível ligar`
    - pt-PT strings in this same file use "ligar"/"ligação" (e.g. "não conseguiu ligar a", "ligação segura"); "conectar" is pt-BR usage and "Incapaz de" is an unnatural literal rendering of "Unable to".
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `pt-PT/firefox-ios.xliff` — The string uses the Brazilian-style "Você" form of address, which doesn't match the rest of the pt-PT strings.
    - Current: `Você desativou`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Desativou`
    - pt-PT strings address the user with verbs alone ("Aceda", "Saiba"). An explicit "Você" is Brazilian usage and breaks the locale's register.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `pt-PT/firefox-ios.xliff` — The iOS Settings app is called "Configurações" (the Brazilian term) instead of "Definições".
    - Current: `Configurações do dispositivo`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Definições do dispositivo`
    - In pt-PT the iOS Settings app is "Definições", and the sibling string TurnOnNotificationsMessage on the same screen uses "Definições do seu dispositivo". The path the user is told to follow should match the real menu name.
- `TabLocation.ETP.Off.NotSecure.A11y.Label.v119` — `pt-PT/firefox-ios.xliff` — "Tracking" rendered as Brazilian "rastreamento", inconsistent with "monitorização" used for Tracking Protection in the same file.
    - Current: `Proteção Melhorada contra rastreamento`
    - Source: `Connection not secure. Enhanced Tracking Protection is off.`
    - Suggest: `Proteção melhorada contra monitorização`
    - The lock button strings in this file use "Proteção contra monitorização". "rastreamento" is the pt-BR term, and the same feature gets two names on one screen.
- `TabLocation.ETP.Off.Secure.A11y.Label.v119` — `pt-PT/firefox-ios.xliff` — "Tracking" rendered as Brazilian "rastreamento", inconsistent with "monitorização" used for Tracking Protection in the same file.
    - Current: `Proteção Melhorada contra rastreamento`
    - Source: `Secure connection. Enhanced Tracking Protection is off.`
    - Suggest: `Proteção melhorada contra monitorização`
    - The lock button strings in this file use "Proteção contra monitorização". "rastreamento" is the pt-BR term, and the same feature gets two names on one screen.
- `Enter passcode` — `pt-PT/firefox-ios.xliff` — Uses the Brazilian verb "Digite" instead of the pt-PT "Introduza".
    - Current: `Digite o código`
    - Source: `Enter passcode`
    - Suggest: `Introduza o código`
    - In pt-PT, "digitar" for entering input is a Brazilian usage; pt-PT localizations use "introduzir".
- `DefaultBrowserCard.BetterInternet.Description.v108` — `pt-PT/firefox-ios.xliff` — "navegador padrão" is the Brazilian term and clashes with "navegador predefinido" on the same screen.
    - Current: `navegador padrão`
    - Source: `Making Firefox your default browser is a vote for an open, accessible internet.`
    - Suggest: `navegador predefinido`
    - Other strings in this file use "predefinido" for "default", which is the pt-PT term; "padrão" is pt-BR.
- `DefaultBrowserCard.NextLevel.Description.v108` — `pt-PT/firefox-ios.xliff` — "navegador padrão" is the Brazilian term and clashes with "navegador predefinido" on the same screen.
    - Current: `navegador padrão`
    - Source: `Choose Firefox as your default browser to make speed, safety, and privacy automatic.`
    - Suggest: `navegador predefinido`
    - Other strings in this file use "predefinido" for "default", which is the pt-PT term; "padrão" is pt-BR.
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `pt-PT/firefox-ios.xliff` — "navegador padrão" is the Brazilian term and clashes with "navegador predefinido" on the same screen.
    - Current: `navegador padrão`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `navegador predefinido`
    - Other strings in this file use "predefinido" for "default", which is the pt-PT term; "padrão" is pt-BR.
- `Downloads.CancelDialog.Message` — `pt-PT/firefox-ios.xliff` — The dialog body says "transferência", but its title and the other download strings say "descarga".
    - Current: `cancelar esta transferência?`
    - Source: `Are you sure you want to cancel this download?`
    - Suggest: `cancelar esta descarga?`
    - The same dialog's title (Downloads.CancelDialog.Title) is "Cancelar descarga", and the toasts and panel also use "descarga". The body should use the same term on the same screen.
- `Logins.WelcomeView.TurnOnAutoFill` — `pt-PT/firefox-ios.xliff` — AutoFill is rendered as 'Preenchimento automático' (with a capital P mid-sentence) here, but as 'Autopreenchimento' in the title on the same welcome screen.
    - Current: `Ativar o Preenchimento automático`
    - Source: `Turn on AutoFill`
    - Suggest: `Ativar o autopreenchimento`
    - The welcome screen's title (Logins.WelcomeView.Title2) and the passcode warning both translate AutoFill as 'autopreenchimento'. This button on the same screen uses a different term, and capitalises it in the middle of the sentence.
- `Settings.Home.Option.Title.v101` — `pt-PT/firefox-ios.xliff` — "Homepage" is translated as "página principal" here but as "página inicial" everywhere else on the same settings screen.
    - Current: `Incluir na página principal`
    - Source: `Include on Homepage`
    - Suggest: `Incluir na página inicial`
    - The sibling strings (Settings.Home.Option.Description.v101, StartAtHome.Always, etc.) all use "página inicial" for Homepage, so this one is inconsistent.
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `pt-PT/firefox-ios.xliff` — The status label renders "Standard" as "Normal", but the option on the same screen calls it "Padrão".
    - Current: `Normal`
    - Source: `Standard`
    - Suggest: `Padrão`
    - The status shows which option is selected. The option itself is "Padrão (predefinição)", so the status should use the same term.
- `DeleteLoginAlert.Message.Local.v122` — `pt-PT/firefox-ios.xliff` — Uses 'Você', which breaks the locale's polite form without a pronoun.
    - Current: `Você não pode desfazer esta ação.`
    - Source: `You cannot undo this action.`
    - Suggest: `Não pode anular esta ação.`
    - Elsewhere the pt-PT strings address the user with the verb alone and no pronoun ('Tem a certeza?', 'Não tem quaisquer separadores'). 'Você' is the Brazilian-style register and doesn't fit pt-PT UI text.

### E. Typography, punctuation & spacing

- `BrowserDataTransfer.Settings.SupportedDataFooter.v160` — `pt-PT/firefox-ios.xliff` — Has a comma before "e" at the end of the list, copied from English.
    - Current: `histórico, e listas de leitura`
    - Source: `Bring bookmarks, history, and reading lists into %1$@, or send your %1$@ data to another browser.`
    - Suggest: `histórico e listas de leitura`
    - Portuguese does not put a comma before "e" closing a simple list.
- `CreditCard.EditCard.ViewCreditCardTitle.v116` — `pt-PT/firefox-ios.xliff` — This title uses title case, unlike the sentence-case titles on the same screen.
    - Current: `Ver Cartão`
    - Source: `View Card`
    - Suggest: `Ver cartão`
    - Similar titles in the same file use sentence case ("Adicionar cartão", "Remover cartão", "Número do cartão"), and pt-PT normally does not capitalise common nouns like this.
- `QuickAnswers.OptInRedesign.NothingGetsSavedDescription.v158` — `pt-PT/firefox-ios.xliff` — Portuguese doesn't put a comma before 'ou' at the end of a list.
    - Current: `perguntas, ou respostas`
    - Source: `We don’t store your voice, questions, or answers.`
    - Suggest: `perguntas ou respostas`
    - The serial comma comes from English and is wrong in Portuguese.
- `CreditCard.Settings.AddCard.AccessibilityLabel.v121` — `pt-PT/firefox-ios.xliff` — English title case was copied into the Portuguese label, so "Cartão" has a capital letter it shouldn't.
    - Current: `Adicionar Cartão`
    - Source: `Add Card`
    - Suggest: `Adicionar cartão`
    - pt-PT uses lowercase here, and every other card and address label on this screen does too, e.g. "Guardar cartões no %@" and "Gerir cartões".
- `QuickAnswers.Settings.Footer.v158` — `pt-PT/firefox-ios.xliff` — The English serial comma was carried over before "ou", which isn't correct punctuation in Portuguese.
    - Current: `perguntas, ou respostas`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `perguntas ou respostas`
    - Portuguese doesn't put a comma before the "ou" that ends a simple list.
- `Settings.BoolSetting.LearnMoreAction.v157` — `pt-PT/firefox-ios.xliff` — English-style title case is used; pt-PT uses sentence case, as in the other "Saber mais" strings in this file.
    - Current: `Saber Mais`
    - Source: `Learn More`
    - Suggest: `Saber mais`
    - Inconsistent with the other "Saber mais" strings in this file and with pt-PT capitalisation conventions.
- `Settings.Browsing.AdBlocker.Title.v155` — `pt-PT/firefox-ios.xliff` — English-style title case is used in the setting title; pt-PT uses sentence case.
    - Current: `Bloqueador de Anúncios`
    - Source: `Ad Blocker`
    - Suggest: `Bloqueador de anúncios`
    - Other setting titles in this file use sentence case (e.g. "Bloquear melhorias da IA").
- `Settings.PrivacyNotice.Title.v137` — `pt-PT/firefox-ios.xliff` — A settings menu title ends with a stray full stop.
    - Current: `Informação de privacidade.`
    - Source: `Privacy Notice`
    - Suggest: `Informação de privacidade`
    - The en-US title "Privacy Notice" has no ending punctuation, and none of the other settings titles have one.
- `QuickActions.CombineWindows.Title.v155` — `pt-PT/firefox-ios.xliff` — The label capitalises every word, while sibling quick-action labels use sentence case.
    - Current: `Combinar Janelas`
    - Source: `Combine Windows`
    - Suggest: `Combinar janelas`
    - Other labels in this file use pt-PT sentence case ("Fechar separador", "Abrir último marcador").
- `Bookmarks.NewFolder.Label` — `pt-PT/firefox-ios.xliff` — "Pasta" is capitalised, unlike the sentence-case bookmark labels around it.
    - Current: `Nova Pasta`
    - Source: `New Folder`
    - Suggest: `Nova pasta`
    - Sibling labels in the same group use sentence case ("Novo marcador", "Novo separador", "Editar pasta"). The capital P is inconsistent on the same screen.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `pt-PT/firefox-ios.xliff` — English-style title case, unlike the sentence case used by the other shortcut labels.
    - Current: `Recarregar Ignorando a Cache`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Recarregar ignorando a cache`
    - pt-PT labels in this group use sentence case (e.g. "Recarregar página", "Localizar novamente"). Capitalising "Ignorando" and "Cache" is inconsistent.
- `ShareSheet.SendToDevice.Title.v108` — `pt-PT/firefox-ios.xliff` — English-style title case is used; pt-PT strings in this batch use sentence case.
    - Current: `Enviar Ligação para o Dispositivo`
    - Source: `Send Link to Device`
    - Suggest: `Enviar ligação para o dispositivo`
    - Portuguese doesn't capitalise every word in a label. The other action labels here (e.g. "Adicionar à lista de leitura") use sentence case.
- `TopSites.RemovePage.Button` — `pt-PT/firefox-ios.xliff` — A hyphen-minus is used where the source has a dash; the pt-PT house dash is the en dash.
    - Current: `Remover página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Remover página – %@`
    - The en-US uses an em dash as a separator. The pt-PT conventions use the en dash as the house dash, so a plain hyphen with spaces around it is the wrong character.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pt-PT/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
