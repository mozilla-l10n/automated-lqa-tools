# Android l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **Previous run** | 2026-08-21 @ `d368c9040c12` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,897 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-BR: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Files | 43 |
| Strings | 2,897 |
| Missing strings | 14 |
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
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 3 |

### Completeness

**14 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — 14

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 3 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 239 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (123)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 75 |
| 3 | Degraded language (grammar, spelling, terminology) | 38 |
| 4 | Cosmetic (typography, spacing) | 10 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rBR/strings.xml` — "switch to online mode" was rendered as "sair do modo offline" — acceptable meaning, but the button label reference "Try Again" matches; issue is the phrase changes the instruction sense.
    - Current: `Pressione “Tentar novamente” para sair do modo offline e recarregar a página.`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Pressione “Tentar novamente” para mudar para o modo online e recarregar a página.`
    - Source says "switch to online mode"; the translation says "leave offline mode", altering the wording of the instruction.
- `mozac_feature_addons_settings_run_in_private_browsing` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rBR/strings.xml` — "Run in private browsing" is rendered as an action "Ativar" (Enable) instead of describing that the add-on runs in private browsing.
    - Current: `Ativar na navegação privativa`
    - Source: `Run in private browsing`
    - Suggest: `Executar na navegação privativa`
    - The source is a setting label meaning the add-on is allowed to run in private browsing; "Ativar" changes the meaning to "Enable".
- `mozac_feature_contextmenu_open_link_in_private_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-pt-rBR/strings.xml` — The word "link" is dropped, unlike the parallel "Open link in new tab" string.
    - Current: `Abrir em aba privativa`
    - Source: `Open link in private tab`
    - Suggest: `Abrir link em aba privativa`
    - Source is "Open link in private tab"; the object "link" is omitted while the sibling string keeps it.
- `mozac_feature_contextmenu_snackbar_action_switch` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-pt-rBR/strings.xml` — "Switch" (switch to the newly opened tab) is rendered as "Mostrar" (show), not the source action.
    - Current: `Mostrar`
    - Source: `Switch`
    - Suggest: `Mudar`
    - The developer comment says clicking the action switches to the newly opened tab; "Mostrar" means "Show", which is a different action word than "Switch" ("Mudar"/"Alternar").
- `mozac_feature_importer_dialog_title` — `mozilla-mobile/android-components/components/feature/importer/src/main/res/values-pt-rBR/strings.xml` — Progress title "Importing bookmarks" rendered as a noun phrase "Importação de favoritos" instead of the ongoing action.
    - Current: `Importação de favoritos`
    - Source: `Importing bookmarks`
    - Suggest: `Importando favoritos`
    - The source is a present-participle title of a loading dialog indicating the action in progress; "Importação de favoritos" loses the in-progress sense.
- `mozac_feature_prompts_suggest_strong_password_description_3` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — The future tense "It’ll be saved" is rendered as present "Ela é salva".
    - Current: `Ela é salva na sua conta para uso futuro.`
    - Source: `Protect your account by using a strong, randomly generated password. It’ll be saved into your account for future use.`
    - Suggest: `Ela será salva na sua conta para uso futuro.`
    - The source states the password will be saved after the action; the present tense changes the meaning.
- `mozac_protections_dashboard_empty_subtitle` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-pt-rBR/strings.xml` — "You’ll see them here." is rendered as a passive statement "Eles são listados aqui." losing the future/user-addressed meaning.
    - Current: `Eles são listados aqui.`
    - Source: `You’ll see them here.`
    - Suggest: `Você vai vê-los aqui.`
    - The source addresses the user in the future tense; the translation changes it to a generic present-tense passive statement.
- `mozac_feature_sitepermissions_media_key_system_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-pt-rBR/strings.xml` — "DRM-controlled content" was rendered as "conteúdo controlado por direitos autorais" (copyright-controlled), losing the DRM term.
    - Current: `conteúdo controlado por direitos autorais`
    - Source: `Allow %1$s to play DRM-controlled content?`
    - Suggest: `conteúdo controlado por DRM`
    - The source says DRM-controlled content; DRM is a specific technology term and is not equivalent to "direitos autorais" (copyright).
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-pt-rBR/strings.xml` — Translation says "allow notifications from %1$s" instead of "allow notifications in %1$s" (the app), changing the meaning.
    - Current: `Precisa permitir notificações do %1$s para receber deste site.`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `Você precisa permitir notificações no %1$s para receber notificações deste site.`
    - %1$s is the app name; the source asks the user to enable notifications in the app so the website's notifications can be received, not to allow notifications coming from the app.
- `mozac_summarize_fxa_sign_in_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-pt-rBR/strings.xml` — "Sign in to summarize" is rendered as "Entre na conta para resumir", adding "na conta" which is not in the source.
    - Current: `Entre na conta para resumir`
    - Source: `Sign in to summarize`
    - Suggest: `Entre para resumir`
    - The source is simply "Sign in to summarize"; the target adds a noun not present in the source, and elsewhere in the batch "Sign in" is translated as just "Entrar".
- `tap_to_play` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-pt-rBR/strings.xml` — "tap to play!" in a game context means start playing, not play media; "reproduzir" is the media-playback sense.
    - Current: `toque para reproduzir!`
    - Source: `tap to play!`
    - Suggest: `toque para jogar!`
    - This is a game (longfox) start prompt; "reproduzir" means to play back media, changing the meaning.
- `action_bar_up_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Navigate up" (go back/up in navigation hierarchy) mistranslated as "go to the top".
    - Current: `Ir para o topo`
    - Source: `Navigate up`
    - Suggest: `Navegar para cima`
    - The action bar "up" button navigates to the parent screen, not scroll to the top of the page.
- `add_to_homescreen_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Home screen" translated as "tela do dispositivo", dropping "inicial".
    - Current: `Adicionar à tela do dispositivo`
    - Source: `Add to Home screen`
    - Suggest: `Adicionar à tela inicial`
    - Source says "Home screen"; the related description string correctly uses "tela inicial do dispositivo".
- `addresses_county` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "County" is rendered as "Município", which corresponds to a city-level division rather than a county.
    - Current: `Município`
    - Source: `County`
    - Suggest: `Condado`
    - The comment describes county lines used in postal addressing (US/UK-style counties); pt-BR standard rendering is "Condado". "Município" collides conceptually with city ("Cidade").
- `addresses_prefecture` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Prefecture" is translated as "Província", duplicating the translation of "Province" and naming the wrong administrative division.
    - Current: `Província`
    - Source: `Prefecture`
    - Suggest: `Prefeitura`
    - The developer comment says this field is for Japanese prefectures; pt-BR uses "Prefeitura" for that. Using "Província" makes it identical to addresses_province, creating an ambiguous, wrong label.
- `ai_controls_block_ai_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "pop-ups" was rendered as "notificações" (notifications) instead of pop-ups/janelas instantâneas.
    - Current: `nem notificações sobre eles`
    - Source: `Blocking means you won’t see new or current AI enhancements in %s, or pop-ups about them.`
    - Suggest: `nem pop-ups sobre eles`
    - The source says "or pop-ups about them"; "notificações" refers to a different UI concept (notifications).
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "pop-ups" translated as "notificações" (notifications).
    - Current: `nem notificações sobre eles`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `nem pop-ups sobre eles`
    - The source says "or pop-ups about them"; notifications are a distinct concept in the app.
- `alternative_app_icon_option_cuddling` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Cuddling" is translated as "Aconchegante" (cozy), losing the intended meaning.
    - Current: `Aconchegante`
    - Source: `Cuddling`
    - Suggest: `Fofinho`
    - The developer comment describes a playful, adorable design; "Cuddling" refers to snuggling/cuteness, not "cozy".
- `alternative_app_icon_option_purple_dark` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Dark Purple" is rendered as "Roxo com escuro", which is not the meaning of the source.
    - Current: `Roxo com escuro`
    - Source: `Dark Purple`
    - Suggest: `Roxo escuro`
    - The source names the color "Dark Purple"; "Roxo com escuro" ("purple with dark") is ungrammatical and wrong. The correct name is "Roxo escuro".
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Custom tab menu" was rendered as "menu de personalização de abas" (tab customization menu), which is a different feature.
    - Current: `Fechar menu de personalização de abas`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Fechar painel do menu da aba personalizada`
    - The source refers to closing the bottom sheet menu of a custom tab (aba personalizada), not a menu for customizing tabs.
- `browser_menu_add_to_homescreen` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Home screen" translated as "tela do dispositivo", dropping "inicial".
    - Current: `Adicionar à tela do dispositivo`
    - Source: `Add to Home screen`
    - Suggest: `Adicionar à tela inicial`
    - Source is "Add to Home screen"; the translation says just "device screen", losing the "Home" qualifier used consistently elsewhere (e.g. browser_menu_add_app_to_homescreen).
- `camera_permissions_needed_message` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The translation omits the specific steps (go to Android settings, tap permissions, tap allow) and replaces them with a vague instruction.
    - Current: `Use as configurações do Android para mudar as permissões para permitir acesso.`
    - Source: `Camera access needed. Go to Android settings, tap permissions, and tap allow.`
    - Suggest: `Vá para as configurações do Android, toque em permissões e toque em permitir.`
    - The source gives a concrete three-step instruction; the target generalizes it, losing the instructions the user needs.
- `connection_security_panel_verified_by` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Verified by" is rendered as "Homologado por" (approved/certified by) instead of "Verificado por".
    - Current: `Homologado por %s`
    - Source: `Verified by %s`
    - Suggest: `Verificado por %s`
    - The source indicates who verified the certificate; "Homologado" means approved/homologated, a different concept, and it is inconsistent with the standard Firefox term "Verificado por".
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Navigate back" is rendered as "Voltar à página anterior" (go back to previous page), which is not what the back button in the credit card settings screen does.
    - Current: `Voltar à página anterior`
    - Source: `Navigate back`
    - Suggest: `Voltar`
    - The source is a generic back-navigation content description for the credit card feature top bar; "página anterior" wrongly implies a web page.
- `credit_cards_warning_dialog_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The condition "if someone else has your device" is translated as "caso outras pessoas usem seu dispositivo", changing the meaning.
    - Current: `caso outras pessoas usem seu dispositivo`
    - Source: `Set up a device lock pattern, PIN, or password to protect your saved payment methods from being accessed if someone else has your device.`
    - Suggest: `caso outra pessoa tenha acesso ao seu dispositivo`
    - The source warns about someone else having (possessing) the device, not about other people using it.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Content description says "go back to the previous page" though it navigates back within the debug drawer.
    - Current: `Voltar à página anterior`
    - Source: `Navigate back`
    - Suggest: `Voltar`
    - The developer comment states it navigates back within the debug drawer, not to a web page.
- `debug_drawer_cfr_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Acronym CFR is misspelled as "CRF".
    - Current: `Ferramentas CRF`
    - Source: `CFR Tools`
    - Suggest: `Ferramentas CFR`
    - The source acronym is CFR (contextual feature recommendation); the letters were transposed, and the related string debug_drawer_cfr_tools_reset_cfr_title correctly uses "CFRs".
- `default_browser_experiment_card_text` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The translation says "open links, emails and messages" instead of "links from websites, emails and messages".
    - Current: `Abra links, emails e mensagens automaticamente no Firefox.`
    - Source: `Set links from websites, emails, and messages to open automatically in Firefox.`
    - Suggest: `Defina para que links de sites, emails e mensagens abram automaticamente no Firefox.`
    - Source means setting links coming from websites, emails and messages to open in Firefox; the target implies opening emails and messages themselves in Firefox and drops the 'set' action.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Content description for the "Navigate back" toolbar button is translated as "Página anterior" (previous page) instead of describing the back navigation action.
    - Current: `Página anterior`
    - Source: `Navigate back`
    - Suggest: `Voltar`
    - The source "Navigate back" is a toolbar navigation button content description; "Página anterior" says "previous page", which is different content and misleading for screen reader users.
- `edit_tab_group_bottom_sheet_grabber_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "collapse drag handle" is rendered as a handle "used to collapse", changing the described control.
    - Current: `Novo grupo, alça de arrastar usada para recolher`
    - Source: `New group, collapse drag handle`
    - Suggest: `Novo grupo, recolher alça de arrastar`
    - The source is an action-style content description ("collapse drag handle"), not a description of a handle whose purpose is collapsing.
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The translation drops the noun "fingerprinters", leaving only "suspeitos" (suspects) without saying what is suspected.
    - Current: `para impedir suspeitos`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `para impedir suspeitos de rastreamento de identidade digital`
    - Source says "to stop suspected fingerprinters"; the target omits the object noun, so the sentence says merely "to stop suspects".
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Firefox Suggest" is a product/feature brand name and should not be translated.
    - Current: `Sugestões Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - Firefox Suggest is a Mozilla feature brand name that stays untranslated.
- `ip_protection_connection_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "in a few minutes" translated as "mais tarde" (later), dropping the specific timeframe.
    - Current: `Tente novamente mais tarde.`
    - Source: `Couldn’t connect to VPN. Try again in a few minutes.`
    - Suggest: `Tente novamente em alguns minutos.`
    - The source specifies "in a few minutes"; the translation loses that information.
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "on the first of every month" translated as "no início de cada mês" (at the beginning of every month).
    - Current: `no início de cada mês`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `no primeiro dia de cada mês`
    - The source states a specific day (the first), not a vague beginning of the month.
- `ip_protection_get_started` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Get started" is a button that starts the VPN flow, but it is translated as the noun "Introdução".
    - Current: `Introdução`
    - Source: `Get started`
    - Suggest: `Começar`
    - The developer comment says it is the label for the button that starts the VPN authentication flow; "Introdução" means "Introduction" and does not convey an action.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "unlimited bandwidth" was rendered as "dados ilimitados" (unlimited data) instead of bandwidth.
    - Current: `para ter dados ilimitados até %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `para ter largura de banda ilimitada até %1$s`
    - The source says "unlimited bandwidth"; the developer comment also states the promotion provides unlimited data bandwidth. "dados ilimitados" changes the meaning to unlimited data volume.
- `login_detail_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Login detail menu" is rendered as "Menu de detalhes da conta" (account), not the login/password entry.
    - Current: `Menu de detalhes da conta`
    - Source: `Login detail menu`
    - Suggest: `Menu de detalhes da credencial`
    - In this surface "login" refers to a saved login/password entry, not a user account; neighbouring strings use "senha"/"credencial". "conta" names the wrong thing.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Navigate back" is translated as "Voltar à página anterior", adding "page" which is not in the source and is wrong for exiting the login detail view.
    - Current: `Voltar à página anterior`
    - Source: `Navigate back`
    - Suggest: `Voltar`
    - The developer comment says the button goes back and exits the login detail view, not to a previous web page; the source is simply "Navigate back".
- `logins_biometric_leave_button` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Leave" (leave the logins screen) is translated as "Sair", which in context reads as exiting/logging out.
    - Current: `Sair`
    - Source: `Leave`
    - Suggest: `Sair da tela`
    - The button leaves the logins lock screen; "Sair" alone is ambiguous with quitting the app, but the meaning of leaving the section should be preserved.
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "It only takes a minute" is rendered as "é bem rápido" ("it's very quick"), losing the stated duration.
    - Current: `Ajude a melhorar a pesquisa no Firefox, é bem rápido`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `Ajude a melhorar a pesquisa no Firefox, leva só um minuto`
    - The source says the survey takes a minute; the translation replaces it with a vague "it's very quick", and matches the "sec" variant instead.
- `microsurvey_prompt_sync_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "It only takes a minute" is rendered as "é bem rápido" ("it's very quick"), losing the stated duration.
    - Current: `Ajude a melhorar a sincronização no Firefox, é bem rápido`
    - Source: `Help make sync in Firefox better. It only takes a minute`
    - Suggest: `Ajude a melhorar a sincronização no Firefox, leva só um minuto`
    - The source specifies a minute; the translation drops that and duplicates the wording used for the "only takes a sec" string.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Visit it" is mistranslated as "Abra em uma aba" ("Open it in a tab").
    - Current: `Para adicionar um site: Abra em uma aba e selecione`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Para adicionar um site: Acesse o site e selecione`
    - The source instructs the user to visit the site; the translation invents an instruction about opening it in a tab.
- `opening_screen_after_four_hours_of_inactivity` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Translation adds "Aba mais recente, ou" which is not in the source and duplicates the "Last tab" option label.
    - Current: `Aba mais recente, ou tela inicial após quatro horas sem atividade`
    - Source: `Homepage after four hours of inactivity`
    - Suggest: `Tela inicial após quatro horas sem atividade`
    - Source is "Homepage after four hours of inactivity"; the added "Aba mais recente, ou" states content not present in the source and conflicts with the separate "Last tab" option.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The translation omits the "Enable to allow" instruction and mistranslates "prevent" as "try to prevent".
    - Current: `Permitir zoom com movimento de pinça com dois dedos, mesmo em sites que tentam impedir este gesto.`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `Ative para permitir zoom com movimento de pinça, mesmo em sites que impedem este gesto.`
    - Source says "Enable to allow pinch and zoom, even on websites that prevent this gesture." The target drops the "Enable to" instruction and changes "prevent" to "tentam impedir" (try to prevent).
- `preference_doh_max_protection_info_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Translation weakens the source: "sites will not load" became "alguns sites podem não ser carregados" (some sites may not load).
    - Current: `alguns sites podem não ser carregados ou não funcionar corretamente`
    - Source: `If secure DNS is not available sites will not load or function properly`
    - Suggest: `os sites não serão carregados ou não funcionarão corretamente`
    - The source states categorically that sites will not load or function properly; the target adds "alguns" (some) and hedges with "podem" (may), changing the meaning.
- `preference_doh_max_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "You'll see a security risk warning" is rendered impersonally, dropping the subject reference and the future tense.
    - Current: `Aparece um aviso de risco de segurança antes de usar o DNS do seu sistema.`
    - Source: `%1$s will always use secure DNS. You’ll see a security risk warning before we use your system DNS.`
    - Suggest: `Você verá um aviso de risco de segurança antes de usarmos o DNS do seu sistema.`
    - The source explicitly addresses the user ("You'll see") and says "before we use your system DNS"; the target drops both agents, making it ambiguous who sees the warning and who uses the DNS.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Translation adds "meus" (my), which is not in the source "data".
    - Current: `não compartilhar nem vender meus dados`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `não compartilhar nem vender dados`
    - The source says "not to share & sell data" without a possessive; adding "meus" changes the wording and mixes person with the rest of the settings UI.
- `preference_phone_feature_media_key_system_access` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "DRM-controlled content" is rendered as "controlado por direitos autorais" (copyright-controlled), dropping the DRM term.
    - Current: `Conteúdo controlado por direitos autorais`
    - Source: `DRM-controlled content`
    - Suggest: `Conteúdo controlado por DRM`
    - The source refers specifically to DRM (digital rights management), not copyright; the established Mozilla pt-BR term is "conteúdo controlado por DRM".
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Translation adds "selecionados abaixo" and says "ao tocar" instead of "quando você seleciona", altering the source meaning.
    - Current: `Excluir automaticamente os dados de navegação selecionados abaixo ao tocar em "Sair" no menu principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `Exclui automaticamente os dados de navegação quando você seleciona “Sair” no menu principal`
    - The source is "Automatically deletes browsing data when you select “Quit” from the main menu" — there is no "selected below" qualifier, and the pt-BR quoting convention is curly double quotes.
- `preferences_addresses_save_and_autofill_addresses_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Includes" (descriptive) rendered as the infinitive "Incluir" (an action).
    - Current: `Incluir números de telefone e endereços de email`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Inclui números de telefone e endereços de email`
    - The source is a summary describing what is saved ("Includes phone numbers and email addresses"), not an action to perform.
- `qr_code_display_instructions` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "scan the QR code" is rendered as "capturem o código QR" instead of "escaneiem/leiam".
    - Current: `peça que capturem o código QR abaixo`
    - Source: `To share this link with people nearby, have them scan the QR code below.`
    - Suggest: `peça que escaneiem o código QR abaixo`
    - The source says to scan the QR code; "capturar" (capture/take a picture) is not the established pt-BR term for scanning a QR code, which is "escanear"/"ler".
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "between updates" mistranslated as "a cada atualização" (with each update).
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
    - The source says improvements happen between updates (remotely, without an app update); the translation reverses this to say they happen with each update.
- `saved_logins_sort_strategy_last_used` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Last used" translated as "Data de uso" (usage date), losing the "last" qualifier.
    - Current: `Data de uso`
    - Source: `Last used`
    - Suggest: `Último uso`
    - The sorting option sorts by last used; "Data de uso" does not convey "last".
- `search_add_custom_engine_error_empty_search_string` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "search string" is rendered as "código de pesquisa" (search code) instead of the search string/URL.
    - Current: `Digite um código de pesquisa`
    - Source: `Enter a search string`
    - Suggest: `Digite um texto de pesquisa`
    - The source refers to the search string (the query URL template), not a "code"; "código" says something different from the source.
- `search_add_custom_engine_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Search string URL" translated as "URL do código de pesquisa" (URL of the search code).
    - Current: `URL do código de pesquisa`
    - Source: `Search string URL`
    - Suggest: `URL do texto de pesquisa`
    - "string" here is the search query string, not a "código" (code); the rendering conveys a different meaning.
- `select_bookmark_search_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Search folders" (search the folders themselves) was rendered as "Pesquisar em pastas" (search inside folders).
    - Current: `Pesquisar em pastas`
    - Source: `Search folders`
    - Suggest: `Pesquisar pastas`
    - The developer comment says "search" is a verb and the object is the folders; the target changes the meaning to searching within folders.
- `setup_checklist_subtitle_6_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "all 6 setup steps" is rendered as "todas as 6 etapas", dropping the "setup" qualifier.
    - Current: `Você completou todas as 6 etapas.`
    - Source: `You’ve completed all 6 setup steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `Você completou todas as 6 etapas de configuração.`
    - The source specifies "setup steps"; the translation omits that the steps are configuration steps.
- `sports_widget_get_custom_wallpaper` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The action verb "Get" is dropped, turning a menu action into a noun phrase.
    - Current: `Fundo de tela personalizado`
    - Source: `Get custom wallpaper`
    - Suggest: `Obter fundo de tela personalizado`
    - Source is a menu item action "Get custom wallpaper"; the translation omits the verb and no longer states the action.
- `sports_widget_runner_up_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Runners-up" (second place) is translated as "Finalistas", which means finalists (both teams in the final), not the runner-up.
    - Current: `Finalistas`
    - Source: `Runners-up`
    - Suggest: `Vice-campeão`
    - The developer comment states Runners-up means second place; "Finalistas" includes the champion and so says something different from the source.
- `sports_widget_upcoming` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Upcoming" (section header for matches not yet started) is rendered as "Seguintes" ("following/next ones") instead of a term meaning upcoming.
    - Current: `Seguintes`
    - Source: `Upcoming`
    - Suggest: `Próximos`
    - The source means matches that have not yet started; "Seguintes" means "the following", not "upcoming". The related string sports_widget_upcoming_match_content_description uses "Em breve".
- _…and 15 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rBR/strings.xml` — Agreement error: "uma forma que nunca será concluído" should agree with "o pedido" or be restructured.
    - Current: `O site está redirecionando o pedido de uma forma que nunca será concluído.`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `O site está redirecionando o pedido de uma forma que nunca será concluída.`
    - The relative clause modifies "forma" (feminine), so the participle must be "concluída"; as written the agreement is broken.
- `mozac_feature_addons_permissions_clipboard_write_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rBR/strings.xml` — Missing definite article before "área de transferência", inconsistent with the parallel _for_update string.
    - Current: `Enviar dados para área de transferência`
    - Source: `Input data to the clipboard`
    - Suggest: `Enviar dados para a área de transferência`
    - Portuguese requires the article here ("para a área de transferência"), as used in the corresponding update string.
- `mozac_feature_applinks_open_in` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-pt-rBR/strings.xml` — "Abrir no…" uses a contracted preposition that has no referent; the source is a generic "Open in…" title for a list of apps.
    - Current: `Abrir no…`
    - Source: `Open in…`
    - Suggest: `Abrir em…`
    - The developer comment says this is the title for the list of external apps to open the link in; "Abrir no…" (in the) is ungrammatical without a following noun.
- `mozac_feature_media_sharing_camera_and_microphone_text` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-pt-rBR/strings.xml` — Present continuous "that’s using" translated as simple present "que usa", inconsistent with the parallel camera-only string.
    - Current: `Toque para abrir a aba que usa seu microfone e câmera.`
    - Source: `Tap to open the tab that’s using your microphone and camera.`
    - Suggest: `Toque para abrir a aba que está usando seu microfone e câmera.`
    - Source says "the tab that’s using your microphone and camera"; the sibling string mozac_feature_media_sharing_camera_text correctly uses "está usando".
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — "Tenha certeza se confia" is ungrammatical; should be "de que confia".
    - Current: `Tenha certeza se confia neste site`
    - Source: `Make sure you trust this site before you upload from “%1$s”.`
    - Suggest: `Certifique-se de que você confia neste site`
    - The source says "Make sure you trust this site"; "Tenha certeza se confia" is not grammatical Portuguese (the conjunction "se" cannot follow "ter certeza" in this affirmative construction).
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — Missing preposition and inconsistent term in "provedor acesso a contas".
    - Current: `Usar %1$s como um provedor acesso a contas`
    - Source: `Use %1$s as a login provider`
    - Suggest: `Usar %1$s como um provedor de autenticação`
    - "provedor acesso a contas" is ungrammatical (missing "de") and diverges from "provedor de autenticação" used for the same "login provider" term in mozac_feature_prompts_identity_credentials_choose_provider.
- `mozac_feature_prompts_popup_dialog_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — Awkward/incorrect construction "Permitir a este site abrir".
    - Current: `Permitir a este site abrir uma janela?`
    - Source: `Allow this site to open?`
    - Suggest: `Permitir que este site abra uma janela?`
    - The Portuguese construction requires "permitir que este site abra"; "Permitir a este site abrir" is ungrammatical in pt-BR usage.
- `bookmark_deletion_snackbar_message` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Deleted %1$s" is translated with the active verb form "Excluiu" instead of the past participle.
    - Current: `Excluiu %1$s`
    - Source: `Deleted %1$s`
    - Suggest: `%1$s excluído`
    - The source is a snackbar confirming a bookmark was deleted; "Excluiu %1$s" reads as "(he/she/you) deleted %1$s" rather than a status confirmation.
- `bookmark_moved_single_item` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — The snackbar uses the active third-person verb "Moveu" (he/she moved) instead of the passive/participle form describing the completed action.
    - Current: `Moveu %1$s para %2$s`
    - Source: `Moved %1$s to %2$s`
    - Suggest: `%1$s movido para %2$s`
    - The source "Moved %1$s to %2$s" is a status confirmation, not an action performed by a third person; "Moveu" reads as "he/she moved" in pt-BR.
- `browser_menu_default_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Ungrammatical construction "Tornar o %1$s como padrão".
    - Current: `Tornar o %1$s como padrão`
    - Source: `Make %1$s your default`
    - Suggest: `Tornar o %1$s seu navegador padrão`
    - "Tornar ... como" is incorrect in Portuguese; the verb tornar does not take "como".
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Missing preposition contraction: "a partir 14 de março" lacks "de".
    - Current: `deixarão de funcionar a partir 14 de março.`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `deixarão de funcionar a partir de 14 de março.`
    - "a partir" requires "de" before the date; grammatical error.
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Gender/number disagreement: "Ativo" instead of feminine plural matching the sibling tab-count categories.
    - Current: `Ativo`
    - Source: `Active`
    - Suggest: `Ativas`
    - This is the active tab count category; sibling strings use "Inativas" and "Privativas" (feminine plural, agreeing with "abas"), so "Ativo" is inconsistent and mismatched.
- `ip_protection_location_recommended_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Infinitive "Selecionar" used where source is a third-person descriptive sentence "Selects".
    - Current: `Selecionar o local de VPN mais rápido para você.`
    - Source: `Selects the fastest VPN location for you.`
    - Suggest: `Seleciona o local de VPN mais rápido para você.`
    - The source "Selects the fastest VPN location for you." is a description of what the option does, so pt-BR should use the third-person present "Seleciona".
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Switched to the recommended location." rendered with an active verb implying the user switched.
    - Current: `Mudou para o local recomendado.`
    - Source: `Switched to the recommended location.`
    - Suggest: `Alterado para o local recomendado.`
    - The source is a passive/participial statement about the app having switched; "Mudou para" reads as "(You/it) switched", which is ambiguous and grammatically off for a status card.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Misspelling of "permitir" as "permitr".
    - Current: `ao permitr que a Mozilla`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `ao permitir que a Mozilla`
    - "permitr" is a typo; the correct verb is "permitir", as in the parallel strings nova_onboarding_marketing_body_5 and _7.
- `search_settings_google_lens_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Descriptive third-person "Sends" rendered as infinitive "Enviar".
    - Current: `Enviar imagens e fotos ao Google para pesquisa visual.`
    - Source: `Sends images and photos to Google for visual search.`
    - Suggest: `Envia imagens e fotos ao Google para pesquisa visual.`
    - The source is a description of what the toggle does ("Sends images..."), not an action label; pt-BR should use the third-person present "Envia".
- `tab_tray_inactive_onboarding_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Action link label starts with a lowercase letter although the source is capitalized.
    - Current: `desativar nas configurações`
    - Source: `Turn off in settings`
    - Suggest: `Desativar nas configurações`
    - Source "Turn off in settings" is a sentence-case action label; the pt-BR text lacks the initial capital.
- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — Redundant/incorrect wording "com contendo" in the safe browsing summary.
    - Current: `sites com contendo software indesejado`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `sites com software indesejado`
    - "com contendo" is ungrammatical; the source reads "unwanted software sites".
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — The EU abbreviation is written "EU" instead of the Portuguese "UE" in the regulation reference.
    - Current: `Regulamento (EU) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Regulamento (UE) 2024/1183`
    - In Portuguese the European Union regulation designation is "(UE)"; "EU" is the English abbreviation and in pt means "I".

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-pt-rBR/strings.xml` — "developer tools" is rendered as "ferramentas de desenvolvimento" here but as "ferramentas do desenvolvedor" in the paired non-update string.
    - Current: `Estender as ferramentas de desenvolvimento para acessar seus dados em abas abertas.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Estender as ferramentas do desenvolvedor para acessar seus dados nas abas abertas.`
    - mozac_feature_addons_permissions_devtools_description translates the same source phrase as "ferramentas do desenvolvedor ... nas abas abertas"; the update variant must match for consistency on the same surface.
- `mozac_feature_contextmenu_open_link_in_external_app` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-pt-rBR/strings.xml` — "app" is used instead of "aplicativo", inconsistent with the other strings on the same surface.
    - Current: `Abrir link em app externo`
    - Source: `Open link in external app`
    - Suggest: `Abrir link em aplicativo externo`
    - Elsewhere in the same batch "app" is consistently translated as "aplicativo" (e.g. "Abrir em aplicativo", "Sempre abrir links em aplicativos").
- `webauthn_related_origin_create_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — "passkey" is translated as "senha" (password) instead of the established term "chave de acesso".
    - Current: `%1$s quer criar uma senha para %2$s.`
    - Source: `%1$s wants to create a passkey for %2$s.`
    - Suggest: `%1$s quer criar uma chave de acesso para %2$s.`
    - A passkey is not a password; Mozilla pt-BR uses "chave de acesso". Using "senha" confuses it with password prompts in the same file.
- `webauthn_related_origin_use_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-pt-rBR/strings.xml` — "passkey" is translated as "senha" (password) instead of "chave de acesso".
    - Current: `%1$s quer usar uma senha de %2$s.`
    - Source: `%1$s wants to use a passkey for %2$s.`
    - Suggest: `%1$s quer usar uma chave de acesso de %2$s.`
    - A passkey is a distinct credential type; rendering it as "senha" says something other than the source.
- `mozac_summarize_shake_consent_off_device_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-pt-rBR/strings.xml` — "Shake your device" is translated as "Agite o dispositivo", inconsistent with "balançar" used for the same gesture in the other summarize strings.
    - Current: `Agite o dispositivo`
    - Source: `Shake your device, get a page summary from %1$s in seconds.`
    - Suggest: `Balance o dispositivo`
    - The same source verb "shake" is translated as "balançar" in mozac_summarize_settings_shake_to_summarize and mozac_summarize_shake_consent_on_device_message; mixing verbs on the same feature surface is inconsistent.
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-pt-rBR/strings.xml` — "shake" is rendered as "sacudindo" here but as "balançar"/"agite" in the other shake-to-summarize strings, breaking terminology consistency on the same surface.
    - Current: `Resumir sacudindo o dispositivo?`
    - Source: `Summarize with a shake?`
    - Suggest: `Resumir balançando o dispositivo?`
    - The feature label mozac_summarize_settings_shake_to_summarize uses "Balançar para resumir"; using a third verb for the same gesture is inconsistent.
- `mozac_lib_crash_dialog_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-pt-rBR/strings.xml` — "crashed" rendered as "falhou" while the rest of the crash strings use "travamento/travar".
    - Current: `teve um problema e falhou`
    - Source: `Sorry. %1$s had a problem and crashed.`
    - Suggest: `teve um problema e travou`
    - The same surface (crash reporter) uses "travamento" consistently elsewhere (mozac_lib_crash_channel, dialog_checkbox, no_crashes); "falhou" is inconsistent terminology.
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-pt-rBR/strings.xml` — "crash data" translated as "dados de falha" while the sibling telemetry string and the rest of the file use "travamento".
    - Current: `Coletando dados de falha`
    - Source: `Gathering crash data`
    - Suggest: `Coletando dados de travamento`
    - Inconsistent with mozac_lib_gathering_crash_telemetry_in_progress ("dados de telemetria de travamentos") and the other crash strings in the same file.
- `mozac_lib_gathering_crash_telemetry_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-pt-rBR/strings.xml` — "Gathering" rendered as "Recolhendo" whereas the parallel string uses "Coletando".
    - Current: `Recolhendo dados de telemetria de travamentos`
    - Source: `Gathering crash telemetry data`
    - Suggest: `Coletando dados de telemetria de travamentos`
    - The sibling string mozac_lib_gathering_crash_data_in_progress translates "Gathering" as "Coletando"; "Recolhendo" is also European Portuguese usage.
- `add_login_save_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "login" rendered as "conta" while the surrounding add-login screen strings use "senha".
    - Current: `Salvar nova conta`
    - Source: `Save new login`
    - Suggest: `Salvar nova senha`
    - Related strings (add_login_2 "Adicionar senha") use "senha" for login; "conta" is inconsistent on the same surface.
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "home region" rendered as "região local" instead of the "região inicial" used in all other region strings.
    - Current: `Substituir região local permanentemente`
    - Source: `Override home region permanently`
    - Suggest: `Substituir região inicial permanentemente`
    - Other strings (debug_drawer_home_region_label, debug_drawer_override_home_region_label, debug_drawer_override_region) translate "home region" as "região inicial"; this one is inconsistent.
- `ip_protection_locations_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Navigate back" translated inconsistently as "Voltar à página anterior" here versus "Voltar" in the sibling string.
    - Current: `Voltar à página anterior`
    - Source: `Navigate back`
    - Suggest: `Voltar`
    - ip_protection_navigate_back_button_content_description has the same source "Navigate back" and is translated "Voltar"; this back button navigates within settings screens, not to a previous web page.
- `preference_option_autoplay_allowed_wifi_subtext` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Wi-Fi" is written as "WiFi", inconsistent with the source and with the sibling string using "Wi-Fi".
    - Current: `rede WiFi`
    - Source: `Audio and video will play on Wi-Fi`
    - Suggest: `rede Wi-Fi`
    - The source brand spelling is "Wi-Fi"; the same surface (autoplay settings) uses Wi-Fi elsewhere.
- `share_qr_code` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "QR Code" is rendered as "Código QR" instead of the established pt-BR term "QR Code".
    - Current: `Código QR`
    - Source: `QR Code`
    - Suggest: `QR Code`
    - pt-BR Mozilla products use "QR code"/"QR Code"; "Código QR" is the pt-PT/es form and is inconsistent with the locale's terminology.
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Round of 16" is rendered literally as "Rodada de 16" instead of the standard Brazilian football term "Oitavas de final".
    - Current: `Rodada de 16`
    - Source: `Round of 16`
    - Suggest: `Oitavas de final`
    - In pt-BR soccer terminology the knockout stage of 16 teams is "oitavas de final"; "Rodada de 16" is a literal calque that does not name the stage, and it is inconsistent with the sibling strings translated as "Quartas de final" and "Semifinais".
- `sports_widget_round_of_32` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — "Round of 32" is rendered literally as "Rodada de 32" instead of the standard Brazilian football term "Décimas sextas de final"/"Fase de 32".
    - Current: `Rodada de 32`
    - Source: `Round of 32`
    - Suggest: `Décima sexta de final`
    - Literal calque; pt-BR soccer terminology names knockout stages (oitavas, quartas, semifinais), and the sibling strings use those terms, so "Rodada de 32" is inconsistent and non-idiomatic.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` quotes “Adicionar à tela inicial” but the string it names, `menu_add_to_home_screen`, reads “Adicionar à tela do dispositivo”
    - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Adicionar à tela do dispositivo`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "search string" translated as "código de pesquisa", inconsistent with "termo de pesquisa" used elsewhere.
    - Current: `código de pesquisa`
    - Source: `Check that search string matches Example format`
    - Suggest: `termo de pesquisa`
    - Same source term "search string" is rendered as "termo de pesquisa" in search_add_manually_string; "código" (code) is not the meaning.

### E. Typography, punctuation & spacing

- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `O endereço web deve conter "https://" ou "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `O endereço web deve conter “https://” ou “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Exclamation mark added where the source ends with a period.
    - Current: `risco para o seu dispositivo!`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `risco para o seu dispositivo.`
    - The source is a neutral statement ending in a period; the exclamation mark changes the tone and punctuation.
- `connection_security_panel_local_pdf` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Translation adds a final period not present in the source.
    - Current: `Esta página está armazenada em seu dispositivo.`
    - Source: `This page is stored on your device`
    - Suggest: `Esta página está armazenada em seu dispositivo`
    - The en-US string "This page is stored on your device" has no terminating punctuation; the other panel strings mirror source punctuation.
- `enhanced_tracking_protection_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Added colon not present in the source header text.
    - Current: `Bloqueado:`
    - Source: `Blocked`
    - Suggest: `Bloqueado`
    - Source is the header "Blocked" with no punctuation; the trailing colon is added by the translation.
- `ip_protection_onboarding_body` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Brand term "Wi-Fi" written as "WiFi", dropping the hyphen used in the source.
    - Current: `redes públicas de WiFi`
    - Source: `%1$s by hiding your location, even on public Wi-Fi. Get %2$d GB free every month.`
    - Suggest: `redes públicas de Wi-Fi`
    - The source uses the official trademark spelling "Wi-Fi"; pt-BR strings elsewhere keep "Wi-Fi".
- `ip_protection_promo_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Brand term "Wi-Fi" written as "WiFi", dropping the hyphen used in the source.
    - Current: `redes públicas de WiFi`
    - Source: `Browse with extra protection by hiding your location, even on public Wi-Fi. %s`
    - Suggest: `redes públicas de Wi-Fi`
    - The source uses the official trademark spelling "Wi-Fi"; pt-BR strings elsewhere keep "Wi-Fi".
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Excluir automaticamente os dados de navegação selecionados abaixo ao tocar em "Sair" no menu principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Double space between "Firefox" and "melhora".
    - Current: `O Firefox  melhora`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `O Firefox melhora`
    - Extra whitespace not present in the source text.
- `webcompat_reporter_reason_media2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — Double space between words in the translation.
    - Current: `O vídeo não está sendo carregado ou  reproduzido`
    - Source: `Video isn’t playing or loading`
    - Suggest: `O vídeo não está sendo carregado ou reproduzido`
    - There is an extra space before “reproduzido”; the source has no such spacing.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `“Adicionar à tela inicial”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — A spurious space was inserted between "q=" and the %s placeholder, breaking the example URL format.
    - Current: `example.com/search/?q= %s`
    - Source: `Example: example.com/search/?q=%s`
    - Suggest: `example.com/search/?q=%s`
    - The source is "example.com/search/?q=%s" with no space; the example must show the exact URL format users have to match.

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
