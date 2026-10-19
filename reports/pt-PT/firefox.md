# Firefox l10n QA — pt-PT

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 65 of 16,520 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pt-PT: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `fire-button-panel-choose-link` — `browser/browser/browser.ftl` — The label ends with three ASCII periods instead of the ellipsis character (…).
    - Current: `Escolher...`
    - Source: `Choose…`
    - Suggest: `Escolher…`
    - The locale convention is the single ellipsis character (char 371 vs ascii 27), and the en-US uses "…". The developer comment says the ellipsis tells the user that a dialog follows.
- `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl` — "app links" is rendered as "ligações da aplicação" (the application's links), which changes the meaning and conflicts with the other renderings of the term.
    - Current: `ligações da aplicação`
    - Source: `accesskey: A label: Allow sites to ask to open app links.`
    - Suggest: `ligações em aplicações`
    - The developer comment says app links are links a website asks to open in an app, like mailto: links. They are not links belonging to the application. Related strings use "ligações de aplicações" and "ligações em aplicações".

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
| Files | 328 |
| Strings | 16,520 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 23 |
| Markup & `data-l10n-name` defects | 3 |
| Typography deviations from this locale's own norm | 41 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 566, `curly-single` 114, `straight-double` 40 | **curly-double** |
| apostrophe | `typographic` 124, `straight` 31 | **typographic** |
| ellipsis | `char` 372, `ascii` 28 | **char** |
| dash | `em` 64, `en` 8 | **em** |
| nbsp | `total` 42, `before-punctuation` 2, `space-before-punctuation` 6 | **total** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 41 strings** — 41 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `LenientThisWarning`, `PushMessageBadSenderKey`, `SSL_ERROR_SYM_KEY_UNWRAP_FAILURE`, `about-debugging-setup-usb-status-updating`, `about-debugging-sidebar-runtime-item-waiting-for-browser`, `about-logins-import-dialog-error-try-import-again`, `accessibility-text-label-issue-optgroup-label2`, `appmenu-fxa-setup-sync`, `browser-languages-downloading`, `browser-languages-search`, `browser-languages-searching`, `cfr-doorhanger-bookmark-fxa-link-text` …and 28 more

---

## 3. Open findings (308)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 184 |
| 2 | Wrong content (says something other than the English) | 122 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

- `about-unloads-no-unloadable-tab` — `browser/browser/aboutUnloads.ftl` — “There are no unloadable tabs” rendered as “there are no unloaded tabs”, reversing which state is being reported.
    - Current: `Não existem separadores suspensos.`
    - Source: `There are no unloadable tabs.`
    - Suggest: `Não existem separadores que possam ser suspensos.`
    - en-US says no tabs are eligible for unloading; the Portuguese says no tabs have been unloaded, which is a different fact on a page whose purpose is to list unloadable candidates.
- `item-history-downloads-and-chat` — `browser/browser/aiWindow.ftl` — Access key `B` of `item-history-downloads-and-chat` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Browsing, download, and chat history`
    - The label is “Histórico de navegação, de transferências e de chat”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — Completed-action log entry translated as an infinitive instruction instead of past tense, contrary to the developer comment.
    - Current: `Ler conteúdo da página`
    - Source: `Read page content`
    - Suggest: `Conteúdo da página lido`
    - The comment states “Read is past tense, to indicate that the action has been completed.” Every sibling entry in the same log uses past tense (“Histórico pesquisado”, “Memórias verificadas”); this one reads as an instruction to read.
- `smart-window-default-tab-group-label` — `browser/browser/aiWindowContent.ftl` — Fallback name for a single tab group rendered in the plural.
    - Current: `Grupos de separadores`
    - Source: `Tab Group`
    - Suggest: `Grupo de separadores`
    - The comment says it is the fallback name used in place of $label for one tab group, so it must be singular.
- `reduced-protection-infobar-never-show-button` — `browser/browser/browser.ftl` — Access key `D` of `reduced-protection-infobar-never-show-button` is not present in its label
    - Current: `D`
    - Source: `(value): Don’t show again accesskey: D`
    - The label is “Não mostrar novamente”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `urlbar-autoplay-media-blocked` — `browser/browser/browser.ftl` — The qualifier “with sound” is dropped, claiming all autoplay media is blocked.
    - Current: `Bloqueou a reprodução automática de multimédia para este site.`
    - Source: `tooltiptext: You have blocked autoplay media with sound for this website.`
    - Suggest: `Bloqueou a reprodução automática de multimédia com som para este site.`
    - en-US is “autoplay media with sound”; the tooltip now describes a broader block than the permission actually applies.
- `urlbar-searchmode-bookmarks3` — `browser/browser/browser.ftl` — Access key `B` of `urlbar-searchmode-bookmarks3` is not present in its label
    - Current: `B`
    - Source: `(value): Bookmarks accesskey: B`
    - The label is “Marcadores”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `urlbar-searchmode-tabs3` — `browser/browser/browser.ftl` — Access key `T` of `urlbar-searchmode-tabs3` is not present in its label
    - Current: `T`
    - Source: `(value): Tabs accesskey: T`
    - The label is “Separadores”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `main-context-menu-bookmark-link-2` — `browser/browser/browserContext.ftl` — Access key `B` of `main-context-menu-bookmark-link-2` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Bookmark Link…`
    - The label is “Adicionar ligação aos marcadores…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `customkeys-search-input` — `browser/browser/customkeys.ftl` — “Search shortcuts” (verb) rendered as the noun phrase “search shortcuts”, changing the meaning of the search box.
    - Current: `Atalhos de pesquisa`
    - Source: `aria-label: Search shortcuts placeholder: Search shortcuts`
    - Suggest: `Pesquisar atalhos`
    - The developer comment says “Search is a verb, as in ‘search through shortcuts’”. “Atalhos de pesquisa” means “shortcuts for searching”, the opposite reading, and is used both as aria-label and placeholder of the shortcut search field.
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — “pin it to your taskbar” rendered as “pin it to your toolbar”, naming the wrong UI element.
    - Current: `fixe-o à sua barra de ferramentas`
    - Source: `Keep { -brand-short-name } at your fingertips — make it your default browser and pin it to your taskbar.`
    - Suggest: `fixe-o à sua barra de tarefas`
    - The taskbar is the OS taskbar (“barra de tarefas”), as the sibling msix string in the same file correctly renders it; “barra de ferramentas” is the browser toolbar.
- `firefoxview-closed-tabs-dismiss-tab` — `browser/browser/firefoxView.ftl` — “Dismiss {tabTitle}” rendered as “Disable {tabTitle}”.
    - Current: `Desativar { $tabTitle }`
    - Source: `title: Dismiss { $tabTitle }`
    - Suggest: `Dispensar { $tabTitle }`
    - The button dismisses a closed-tab entry from the list; “Desativar” means disable. The equivalent string in fxviewTabList.ftl uses “Ignorar”, and “Dispensar” is the tree's usual rendering of Dismiss.
- `menu-edit-find-again` — `browser/browser/menubar.ftl` — Access key `g` of `menu-edit-find-again` is not present in its label
    - Current: `g`
    - Source: `accesskey: g label: Find Again`
    - The label is “Localizar novamente”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `launch-on-login-autostart-infobar-keep-button` — `browser/browser/newtab/asrouter.ftl` — Access key `K` of `launch-on-login-autostart-infobar-keep-button` is not present in its label
    - Current: `K`
    - Source: `(value): Keep on accesskey: K`
    - The label is “Manter ligado”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `launch-on-login-autostart-infobar-turn-off-button` — `browser/browser/newtab/asrouter.ftl` — Access key `T` of `launch-on-login-autostart-infobar-turn-off-button` is not present in its label
    - Current: `T`
    - Source: `(value): Turn off accesskey: T`
    - The label is “Desligar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `multi-cta-fox-doodle-msix-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — “taskbar” rendered as “barra de ferramentas” (toolbar).
    - Current: `fixe-o à sua barra de ferramentas e menu Iniciar`
    - Source: `Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and pin it to your taskbar and Start menu.`
    - Suggest: `fixe-o à sua barra de tarefas e menu Iniciar`
    - en-US says “pin it to your taskbar and Start menu”; “barra de ferramentas” is the browser toolbar, not the Windows taskbar.
- `multi-cta-fox-doodle-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — “taskbar” rendered as “barra de ferramentas” (toolbar) in the non-macOS variant.
    - Current: `fixe-o à sua barra de ferramentas`
    - Source: `{$sel_1 ->} [macos] Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and keep it in your Dock. [other] Keep your favorite privacy-focuse…`
    - Suggest: `fixe-o à sua barra de tarefas`
    - en-US says “pin it to your taskbar”; the rest of the file consistently translates taskbar as “barra de tarefas” (e.g. multi-cta-fox-doodle-pin-checkbox), so this instructs the user to use the wrong UI element.
- `nova-early-access-infobar-primary-button` — `browser/browser/newtab/asrouter.ftl` — Access key `G` of `nova-early-access-infobar-primary-button` is not present in its label
    - Current: `G`
    - Source: `(value): Got it accesskey: G`
    - The label is “Percebi”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `nova-early-access-share-feedback-link` — `browser/browser/newtab/asrouter.ftl` — Access key `S` of `nova-early-access-share-feedback-link` is not present in its label
    - Current: `S`
    - Source: `(value): Share feedback accesskey: S`
    - The label is “Partilhar feedback”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — “isn’t preloaded” rendered as “doesn’t come crammed/bloated from the factory”.
    - Current: `não vem atochado de origem como os outros navegadores das grandes tecnológicas`
    - Source: `{ -brand-product-name } isn’t preloaded like other Big Tech browsers. That’s the point.`
    - Suggest: `não vem pré-instalado como os outros navegadores das grandes tecnológicas`
    - en-US says Firefox is not pre-installed on devices the way Big Tech browsers are; the Portuguese instead makes a claim about bloat, a different statement.
- `newtab-sports-widget-champions` — `browser/browser/newtab/newtab.ftl` — “Champions” is rendered as the name of a different competition (Champions League).
    - Current: `Liga dos Campeões`
    - Source: `Champions`
    - Suggest: `Campeões`
    - The string is the World Cup result label for the winning team, shown next to newtab-sports-widget-world-cup-champions (“Campeões do Mundial de 2026”); “Liga dos Campeões” names the UEFA Champions League, a different tournament.
- `newtab-sports-widget-keep-tabs` — `browser/browser/newtab/newtab.ftl` — The idiom “Keep tabs on the World Cup” is rendered literally as keeping browser tabs.
    - Current: `Mantenha os separadores do Mundial de Futebol`
    - Source: `Keep tabs on the World Cup`
    - Suggest: `Acompanhe o Campeonato do Mundo`
    - The developer comment states explicitly that “keep tabs on” means to stay updated on/follow something; the translation instead tells the user to keep browser tabs (“separadores”), which is meaningless here and conflicts with the widget's purpose.
- `newtab-sports-widget-watch-stream-select-games-only` — `browser/browser/newtab/newtab.ftl` — A tag meaning “only some matches are streamed” is translated as an imperative “select only games”.
    - Current: `Selecionar apenas jogos`
    - Source: `Select games only`
    - Suggest: `Apenas alguns jogos`
    - The comment says the provider only streams some matches, not the full tournament; the Portuguese reads as an instruction to select games, turning an informational tag into an action.
- `newtab-wallpaper-dark-sky` — `browser/browser/newtab/newtab.ftl` — Screen-reader description says “sunset” where the source says “night sky”.
    - Current: `Paisagem da cidade com um pôr do sol`
    - Source: `City landscape with a night sky`
    - Suggest: `Paisagem da cidade com um céu noturno`
    - en-US is “City landscape with a night sky”; the alt text describes a different image to screen-reader users.
- `media-border-img` — `browser/browser/pageInfo.ftl` — The image role "Border" is rendered "Margem" (margin).
    - Current: `Margem`
    - Source: `Border`
    - Suggest: `Contorno`
    - In the Media tab this labels a border image; "margem" names the margin, a distinct box-model concept.
- `media-save-image-as` — `browser/browser/pageInfo.ftl` — Access key `e` of `media-save-image-as` is not present in its label
    - Current: `e`
    - Source: `accesskey: v label: Save As…`
    - The label is “Guardar como…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appearance-browser-icon-requirement` — `browser/browser/preferences/browserIcon.ftl` — “Complete” rendered as “Preencha” (fill in a form).
    - Current: `Preencha e desbloqueie ícones bónus da raposa`
    - Source: `message: Complete and unlock bonus fox icons to personalize { -brand-short-name }.`
    - Suggest: `Conclua e desbloqueie ícones bónus da raposa`
    - The message asks the user to complete the actions (set as default, pin to taskbar) that unlock the bonus icons; “Preencha” means filling something in and does not describe that action.
- `autofill-address-county` — `browser/browser/preferences/formAutofill.ftl` — “County” is translated as “País” (country), duplicating the Country field label.
    - Current: `autofill-address-county = País`
    - Source: `County`
    - Suggest: `autofill-address-county = Condado`
    - “County” is an administrative subdivision (“Condado”), not a country; the file already uses “País” for autofill-address-country-only, so the address form shows two identical “País” fields.
- `fxa-qrcode-pair-step3` — `browser/browser/preferences/fxaPairDevice.ftl` — Instruction says to hold the phone *under* the code and drops the article before “telemóvel”.
    - Current: `segure seu telemóvel sob este código`
    - Source: `3. Tap <strong>Ready to Scan</strong> and hold your phone over this code`
    - Suggest: `segure o seu telemóvel sobre este código`
    - en-US “hold your phone over this code”: “sob” means underneath, reversing the physical instruction for scanning the QR code; pt-PT also requires the definite article before the possessive.
- `addressbar-locbar-quickactions-option` — `browser/browser/preferences/preferences.ftl` — Access key `Q` of `addressbar-locbar-quickactions-option` is not present in its label
    - Current: `Q`
    - Source: `accesskey: Q label: Quick actions`
    - The label is “Ações rápidas”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `containers-sites-add-button` — `browser/browser/preferences/preferences.ftl` — Access key `w` of `containers-sites-add-button` is not present in its label
    - Current: `w`
    - Source: `accesskey: w label: Add website`
    - The label is “Adicionar um site”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — The object of “aceder, controlar ou acionar” is dropped, changing what is being managed.
    - Current: `Faça a gestão dos sites que podem aceder, controlar ou acionar.`
    - Source: `description: Manage what websites can access, control, or trigger. label: Permissions`
    - Suggest: `Faça a gestão do que os sites podem aceder, controlar ou acionar.`
    - en-US “Manage what websites can access, control, or trigger.” describes managing the capabilities; the pt-PT sentence manages the sites and leaves the three verbs without an object.
- `preferences-etp-custom-cookie-behavior-block-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — Dropdown option drops the “Block” action and renames cross-site cookies as third-party cookies.
    - Current: `Todos os cookies de terceiros (poderá resultar em falhas nos sites)`
    - Source: `label: Block all cross-site cookies (may cause websites to break)`
    - Suggest: `Bloquear todos os cookies entre sites (poderá resultar em falhas nos sites)`
    - en-US is “Block all cross-site cookies (may cause websites to break)”; every sibling option in the same menu starts with Bloquear/Permitir/Isolar, so an option labelled only “Todos os cookies de terceiros” does not state that the cookies are blocked, and “de terceiros” names a different cookie class than “cross-site”.
- `settings-translations-more-settings-button` — `browser/browser/preferences/preferences.ftl` — Description text is copied from the website-language string instead of translating the source.
    - Current: `Algumas páginas Web são apresentadas em vários idiomas. Selecione os idiomas pela sua ordem de preferência.`
    - Source: `description: Set preferences for languages, websites, and offline translation. label: More translation settings`
    - Suggest: `Defina as preferências de idiomas, sites e tradução offline.`
    - en-US reads “Set preferences for languages, websites, and offline translation.”; the pt-PT text is the description of website-language-heading and tells the user something the button does not do.
- `switch-to-new-tabs-2` — `browser/browser/preferences/preferences.ftl` — Access key `h` of `switch-to-new-tabs-2` is not present in its label
    - Current: `h`
    - Source: `accesskey: h label: When opening links or media in a new tab, switch to it immediately`
    - The label is “Ao abrir ligações ou multimédia num novo separador, mudar imediatamente para o mesmo”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `bike-avatar-alt` — `browser/browser/profiles.ftl` — "Bike" (bicycle) is rendered "Mota", which means motorcycle.
    - Current: `Mota`
    - Source: `alt: Bike`
    - Suggest: `Bicicleta`
    - The avatar icon is a bicycle; "mota" names a different vehicle. The same error repeats in bike-avatar and bike-avatar-tooltip ("Aplicar avatar da mota").
- `copied-profile-page-header-description` — `browser/browser/profiles.ftl` — "We copied your data" becomes "Transferimos" (we transferred/moved it).
    - Current: `Transferimos os seus dados e definições para um novo perfil.`
    - Source: `We copied your data and settings into a new profile. Now give it a name, pick a look, and make it your own.`
    - Suggest: `Copiámos os seus dados e definições para um novo perfil.`
    - The dialog is about a copy of a profile; "transferimos" suggests the data was moved out of the original profile, and in this tree "transferir" is also the standard word for "download".
- `bar-tooltip-cookie` — `browser/browser/protections.ftl` — The singular variant contains three stacked lines, including an untranslated English copy and a typo'd duplicate, instead of a single label.
    - Current: `{ $count } cookie de monitorização entre sites ({ $percentage }%)                 { $count } cross-site tracking cookie ({ $percentage }%)                 { $count } cookie de monitorização ente sites ({ $percentage }%)`
    - Source: `aria-label: {$count ->} [one] { $count } cross-site tracking cookie ({ $percentage }%) [other] { $count } cross-site tracking cookies ({ $percentage }%) title: Cross-Site Tracking Cookies`
    - Suggest: `{ $count } cookie de monitorização entre sites ({ $percentage }%)`
    - The en-US singular is one line; the locale leaves a copy-paste residue with the English source and a misspelling ("ente sites"), which a screen reader would read out three times.
- `monitor-partial-breaches-percentage` — `browser/browser/protections.ftl` — The percent sign is dropped, so the progress label shows a bare number.
    - Current: `{ $percentageResolved } concluído`
    - Source: `{ $percentageResolved }% complete`
    - Suggest: `{ $percentageResolved }% concluído`
    - en-US is "{ $percentageResolved }% complete"; the literal "%" is text, not a placeholder, and its loss turns "50% complete" into "50 complete".
- `item-history-and-downloads-description2` — `browser/browser/sanitize.ftl` — The description adds search history to what the checkbox clears.
    - Current: `Limpa o histórico de pesquisas, sites e transferências`
    - Source: `Clears site and download history`
    - Suggest: `Limpa o histórico de sites e de transferências`
    - en-US is "Clears site and download history"; search history is a separate checkbox (item-form-search-history), so the translation claims a wider deletion than this option performs.
- `set-background-tile` — `browser/browser/setDesktopBackground.ftl` — The wallpaper layout option "Tile" is rendered "Emparelhar" (to pair/match).
    - Current: `Emparelhar`
    - Source: `label: Tile`
    - Suggest: `Mosaico`
    - "Tile" names the repeated-image layout, which pt-PT renders "Mosaico"; "Emparelhar" describes pairing devices and tells the user nothing about the layout.
- `synced-tabs-context-bookmark` — `browser/browser/syncedTabs.ftl` — Access key `B` of `synced-tabs-context-bookmark` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Bookmark Tab…`
    - The label is “Adicionar separador aos marcadores…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-bookmark-tab` — `browser/browser/tabContextMenu.ftl` — Access key `B` of `tab-context-bookmark-tab` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Bookmark Tab…`
    - The label is “Adicionar separador aos marcadores…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-bookmark-tab2` — `browser/browser/tabContextMenu.ftl` — Access key `B` of `tab-context-bookmark-tab2` is not present in its label
    - Current: `B`
    - Source: `accesskey: B label: Bookmark`
    - The label is “Marcar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-pin-tab2` — `browser/browser/tabContextMenu.ftl` — Access key `P` of `tab-context-pin-tab2` is not present in its label
    - Current: `P`
    - Source: `accesskey: P label: Pin`
    - The label is “Afixar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-unload-tabs` — `browser/browser/tabContextMenu.ftl` — Access key `U` of `tab-context-unload-tabs` is not present in its label
    - Current: `U`
    - Source: `accesskey: U label: Unload`
    - The label is “Esvaziar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tab-context-unpin-tab2` — `browser/browser/tabContextMenu.ftl` — Access key `P` of `tab-context-unpin-tab2` is not present in its label
    - Current: `P`
    - Source: `accesskey: p label: Unpin`
    - The label is “Desafixar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tabbrowser-context-mute-tab2` — `browser/browser/tabbrowser.ftl` — Access key `M` of `tabbrowser-context-mute-tab2` is not present in its label
    - Current: `M`
    - Source: `accesskey: M label: Mute`
    - The label is “Silenciar”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tabbrowser-manager-unmute-tab` — `browser/browser/tabbrowser.ftl` — "Unmute tab" becomes "Ativar separador" (activate the tab), dropping the reference to audio.
    - Current: `Ativar separador`
    - Source: `tooltiptext: Unmute tab`
    - Suggest: `Ativar som do separador`
    - Everywhere else in the file unmute is "Repor som do separador" / "Ativar som do separador"; as written the tooltip promises to activate the tab, not restore its sound.
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
    - Current: `Introduzimos os <a data-l10n-name="terms-of-use">Termos de Utilização</a> e atualizámos a nossa <a data-l10n-name="privacy-notice">Informação de Privacidade</a >.<br><br> Por favor, reveja e aceite. <a data-l10n-name="l…`
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Whitespace inside a closing tag makes it render as literal text.
- `update.downloadAndInstallButton.label` — `browser/chrome/browser/browser.properties` — Button label rendered as a noun phrase instead of the action "Atualizar para %S"
    - Current: `Atualização para %S`
    - Source: `Update to %S`
    - Suggest: `Atualizar para %S`
    - The comment makes clear this is the button that downloads and installs the update ("Update to 28.0"). "Atualização para 28.0" is a noun ("update for 28.0") and does not express the action the button performs.
- `unblockTypeMalware` — `browser/chrome/browser/downloads/downloads.properties` — Certainty weakened: "will harm your computer" rendered as "may harm"
    - Current: `outro malware que pode prejudicar o seu computador`
    - Source: `This file contains a virus or other malware that will harm your computer.`
    - Suggest: `outro malware que irá prejudicar o seu computador`
    - The en-US asserts the file will harm the computer; the pt-PT downgrades it to a possibility, weakening the highest-severity warning in this dialog. It also collides with blockedPotentiallyUnwanted ("may harm" → "pode prejudicar"), erasing the severity ordering the developer comment describes.
- `unblockTypePotentiallyUnwanted2` — `browser/chrome/browser/downloads/downloads.properties` — Possibility turned into certainty: "it can make unexpected changes" → "irá efetuar"
    - Current: `mas irá efetuar alterações inesperadas aos seus programas e definições`
    - Source: `This file is disguised as a helpful download, but it can make unexpected changes to your programs and settings.`
    - Suggest: `mas pode efetuar alterações inesperadas aos seus programas e definições`
    - The source says the file *can* make unexpected changes; the pt-PT states it *will*, asserting as fact something the product only flags as possible.
- `serverError` — `browser/chrome/overrides/appstrings.properties` — "it could have moved" rendered as "may have been downloaded/transferred"
    - Current: `pode ter sido transferido`
    - Source: `%S might have a temporary problem or it could have moved.`
    - Suggest: `pode ter mudado de endereço`
    - "moved" here means the site changed address. "transferido" is the term this tree uses throughout for "downloaded" (see downloads.properties), so the error message tells the user something entirely different from the source.
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — “Profile performance” (an action) becomes “performance of the profile”.
    - Current: `Desempenho do perfil`
    - Source: `Profile performance`
    - Suggest: `Analisar desempenho`
    - The comment says this is the label of the button that opens the performance profiler; the translation reads as a noun phrase about a profile's performance rather than the action of profiling.
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — “Offset parent of the selected element” becomes an imperative “shift the relative of the selected element”.
    - Current: `Deslocar parente do elemento selecionado`
    - Source: `Offset parent of the selected element`
    - Suggest: `Elemento pai de deslocamento do elemento selecionado`
    - The developer comment says the tooltip identifies the previewed DOM node as the offset parent; “Deslocar” reads as a verb and “parente” means a family relative, not a parent node.
- `domMutation.remove.tooltip` — `devtools/client/debugger.properties` — Tooltip for the remove-breakpoint button omits the action and just repeats the panel header.
    - Current: `Pontos de quebra de mutação do DOM`
    - Source: `Remove DOM mutation breakpoint`
    - Suggest: `Remover ponto de quebra de mutação do DOM`
    - en-US is “Remove DOM mutation breakpoint”; the developer comment says it is the tooltip of the button that removes a breakpoint. As translated it is identical to domMutationHeader and never tells the user the button removes anything.
- `pauseOnCaughtExceptionsItem` — `devtools/client/debugger.properties` — “Pause on caught exceptions” is rendered as “pause on uncaught exceptions”, reversing the setting's meaning.
    - Current: `Pausar em exceções não identificadas`
    - Source: `Pause on caught exceptions`
    - Suggest: `Pausar em exceções capturadas`
    - en-US is “Pause on caught exceptions”; “não identificadas” says uncaught, the opposite condition, and a user toggling it gets the wrong behaviour description.
- `variablesViewOptimizedOut` — `devtools/client/debugger.properties` — “optimized away” is rendered as “optimized path”.
    - Current: `(caminho otimizado)`
    - Source: `(optimized away)`
    - Suggest: `(removido pela otimização)`
    - “away” has been read as “path”; the label marks a variable the engine optimized out, not a path.
- `dropShadowPlaceholder` — `devtools/client/filterwidget.properties` — The parameter list “x y radius color” is turned into the phrase “colour of radius xy”.
    - Current: `Cor de raio xy`
    - Source: `x y radius color`
    - Suggest: `x y raio cor`
    - The comment says this is the placeholder for drop-shadow's input, i.e. the list of expected values; as translated it no longer tells the user the order or number of values.
- _…and 58 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `perplexity-callout-theme-2-title` — `browser/browser/featureCallout.ftl` — The brand name Perplexity is misspelled as “Perflexity” throughout the Perplexity callout strings.
    - Current: `Perflexity`
    - Source: `Try Perplexity: a new way to search`
    - Suggest: `Perplexity`
    - Perplexity is a product brand and must not be altered; the misspelling appears in perplexity-callout-theme-2-title, theme-1-subtitle-1/-2, theme-2-subtitle-1 and perplexity-callout-primary-label.
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — The company name OpenAI is misspelled as “OpenIA” in the ChatGPT legal-consent string.
    - Current: `OpenIA`
    - Source: `By choosing ChatGPT, you agree to the OpenAI <a data-l10n-name="link1">Terms of Use</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
    - Suggest: `OpenAI`
    - OpenAI is a brand name that must not be altered, and this string is the consent text pointing to that company's terms and privacy policy.
- `fonts-langgroup-malayalam` — `browser/browser/preferences/fonts.ftl` — Malayalam is rendered as “Malaio” (Malay), a different language.
    - Current: `Malaio`
    - Source: `label: Malayalam`
    - Suggest: `Malaiala`
    - Malayalam is the Dravidian language/script of Kerala; “Malaio” is Malay, an Austronesian language written in Latin/Jawi script, so the font group names the wrong writing system.
- `autofill-address-townland` — `browser/browser/preferences/formAutofill.ftl` — “Townland” is translated as “Cidade”, duplicating the City label.
    - Current: `autofill-address-townland = Cidade`
    - Source: `Townland`
    - Suggest: `autofill-address-townland = Lugar`
    - The developer comment says this is an Irish sublocality below a locality; a townland is a small rural division, not a city, and the file already uses “Cidade” for autofill-address-city.
- `netmonitor.security.usedOcsp` — `devtools/client/netmonitor.properties` — The OCSP acronym is misspelled as OSCSP.
    - Current: `(OSCSP)`
    - Source: `Used Online Certificate Status Protocol (OCSP):`
    - Suggest: `(OCSP)`
    - en-US is “Used Online Certificate Status Protocol (OCSP):”; OCSP is a protocol acronym and must not be altered.
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — The command's argument placeholder is misspelled as URL_STING.
    - Current: `:block URL_STING`
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
    - Suggest: `:block URL_STRING`
    - URL_STRING is the literal argument name shown in the command usage help and must not be altered; the body of the same string still says URL_STRING.
- `webconsole-commands-usage-unblock` — `devtools/shared/webconsole-commands.ftl` — The command's argument placeholder is misspelled as URL_STING.
    - Current: `:unblock URL_STING`
    - Source: `:unblock URL_STRING  Stop blocking network requests    It accepts only one argument, the exact same string previously passed to :block.`
    - Suggest: `:unblock URL_STRING`
    - URL_STRING is a literal argument name in the usage help and must match the en-US token.
- `MathML_DeprecatedMoverNonExplicitAccentWarning` — `dom/chrome/dom/dom.properties` — Attribute name “accent” translated to “acento” although the comment forbids it.
    - Current: `um atributo de acento explícito`
    - Source: `Inferring the accent property from the core operator is deprecated. Consider adding an explicit accent attribute to “%S”.`
    - Suggest: `um atributo accent explícito`
    - The comment says “Do not translate accent”; the parallel string MathML_DeprecatedMunderNonExplicitAccentunderWarning correctly keeps “accentunder” untranslated.
- `MediaStreamAudioSourceNodeCrossOrigin` — `dom/chrome/dom/dom.properties` — Wrong API name: createMediaElementSource instead of createMediaStreamSource.
    - Current: `O MediaStream passado para createMediaElementSource`
    - Source: `The MediaStream passed to createMediaStreamSource has a cross-origin resource, the node will output silence.`
    - Suggest: `O MediaStream passado para createMediaStreamSource`
    - The developer comment says “Do not translate MediaStream and createMediaStreamSource”; the translation copied the API name from the preceding string, naming the wrong function.
- `CSPTrustedTypesPolicyViolation` — `dom/chrome/security/csp.properties` — Feature name “Trusted Types” translated despite the developer comment forbidding it.
    - Current: `uma política de Tipos de Confiança`
    - Source: `The page’s settings blocked creating a Trusted Types policy because it violates the following directive: “%1$S“`
    - Suggest: `uma política Trusted Types`
    - The comment states: Don't translate "Trusted Types" because it's a feature name. CSPROTrustedTypesPolicyViolation has the same problem.
- `invalidTrustedTypesExpression` — `dom/chrome/security/csp.properties` — CSP directive name mangled from “trusted-types” to “types-trusted”.
    - Current: `‘types-trusted‘`
    - Source: `Received an invalid token for the ‘trusted-types‘ directive: %1$S`
    - Suggest: `‘trusted-types‘`
    - The directive literal must be reproduced exactly; “types-trusted” is not a CSP directive and sends the author looking for a non-existent name.
- `SanitizerAllowElementIgnored2` — `dom/chrome/security/security.properties` — API name “Sanitizer” translated as “Higienizador” against the developer comment.
    - Current: `Higienizador:`
    - Source: `Sanitizer: Calling allowElement() with “attributes” or non-empty “removeAttributes” was ignored because of the global “removeElements” list.`
    - Suggest: `Sanitizer:`
    - The comment says: Do not translate Sanitizer, allowElement, attributes, removeAttributes or removeElements.
- `CookieForeignNoPartitionedError` — `netwerk/necko.properties` — Cookie attribute name “Partitioned” translated despite the developer comment.
    - Current: `não tem o atributo “Particionado“`
    - Source: `Cookie “%1$S” has been rejected because it is foreign and does not have the “Partitioned“ attribute.`
    - Suggest: `não tem o atributo “Partitioned“`
    - The comment says: Do not translate "Partitioned". The attribute must be typed literally by the developer; CookieForeignNoPartitionedWarning has the same problem.
- `addon-badge-recommended4` — `toolkit/toolkit/about/aboutAddons.ftl` — First-person possessive added where the developer comment forbids it.
    - Current: `correspondam aos nossos padrões para segurança e desempenho`
    - Source: `title: Firefox only recommends extensions that meet standards for security and performance`
    - Suggest: `correspondam aos padrões de segurança e desempenho`
    - The comment explicitly asks to avoid personalising language such as “our” or “we”, because the string must also work in forks not built by Mozilla.
- `addon-badge-verified4` — `toolkit/toolkit/about/aboutAddons.ftl` — First-person possessive added where the developer comment forbids it.
    - Current: `cumprir com os nossos padrões de segurança e desempenho`
    - Source: `title: This extension has been reviewed to meet standards for security and performance`
    - Suggest: `cumprir os padrões de segurança e desempenho`
    - The comment says to avoid “our”/“we” so the badge does not imply that the running fork performed the review.
- `glean-debug-ping-viewer-brand-name` — `toolkit/toolkit/about/aboutGlean.ftl` — Brand name “Glean Debug Ping Viewer” translated.
    - Current: `Depurador de visualização de ping { -glean-brand-name }`
    - Source: `{ -glean-brand-name } Debug Ping Viewer`
    - Suggest: `{ -glean-brand-name } Debug Ping Viewer`
    - The message id marks this as a brand name and the file header asks for Glean terms to stay in English; it also names a specific web tool users reach by that English name.
- `about-logging-preset-networking-http3-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Protocol name HTTP/3 written as HTTPS/3.
    - Current: `diagnosticar HTTPS/3 e problemas de QUIC`
    - Source: `Log modules to diagnose HTTP/3 and QUIC issues`
    - Suggest: `diagnosticar problemas de HTTP/3 e QUIC`
    - “HTTPS/3” is not a protocol; the label of the same preset correctly uses HTTP/3.
- `about-logging-preset-networking-http3-upload-speed-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Protocol name HTTP/3 written as HTTPS/3.
    - Current: `problemas da velocidade de envio HTTPS/3`
    - Source: `Log modules to diagnose HTTP/3 upload speed issues`
    - Suggest: `problemas da velocidade de envio HTTP/3`
    - en-US says HTTP/3; “HTTPS/3” does not exist and contradicts the preset label “Velocidade de envio HTTP/3”.
- `about-webauthn-auth-option-pinuvauthtoken` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Do-not-translate identifier misspelled as “pingUvAuthToken”.
    - Current: `Permissões de comando (pingUvAuthToken)`
    - Source: `Command permissions (pinUvAuthToken)`
    - Suggest: `Permissões de comando (pinUvAuthToken)`
    - The developer comment says pinUvAuthToken must not be translated; the altered spelling no longer matches the CTAP2 option ID users search for.
- `about-webauthn-auth-option-userverificationmgmtpreview` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Do-not-translate constant FIDO_2_1_PRE lower-cased.
    - Current: `(FIDO_2_1_pre)`
    - Source: `Prototype of biometric enrollment (FIDO_2_1_PRE)`
    - Suggest: `(FIDO_2_1_PRE)`
    - The comment states FIDO_2_1_PRE should not be translated; it is a literal spec constant and its casing is part of it.
- `about-webauthn-text-non-ctap2-device` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Protocol name CTAP2 written as “CTap2”.
    - Current: `não suporta CTap2`
    - Source: `Unable to manage options because your security token does not support CTAP2.`
    - Suggest: `não suporta CTAP2`
    - The developer comment spells the protocol CTAP2 (Client to Authenticator Protocol 2); the mixed casing is not a valid form of the name.
- `about-webrtc-peerconnection-id-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — “PeerConnection” translated despite a do-not-translate comment.
    - Current: `ID da ligação do par:`
    - Source: `PeerConnection ID:`
    - Suggest: `ID da PeerConnection:`
    - The developer comment says PeerConnection is a proper noun and the string should not normally be translated; other strings in the same file keep “PeerConnections” and “RTCPeerConnection” in English.
- `language-name-af` — `toolkit/toolkit/intl/languageNames.ftl` — Afrikaans is rendered as “Africano” (African), naming a continent-wide adjective instead of the language.
    - Current: `Africano`
    - Source: `Afrikaans`
    - Suggest: `Africanders (Afrikaans)`
    - en-US “Afrikaans”; pt-PT uses “afrikaans”. “Africano” means “African”.
- `language-name-dz` — `toolkit/toolkit/intl/languageNames.ftl` — Dzongkha is rendered as “Butanês” (Bhutanese), naming the country's demonym rather than the language.
    - Current: `Butanês`
    - Source: `Dzongkha`
    - Suggest: `Dzongkha`
    - en-US “Dzongkha”; the locale names other languages by their own name, not by a country demonym.
- `language-name-hi` — `toolkit/toolkit/intl/languageNames.ftl` — Hindi is rendered as “Hindu”, which names an adherent of Hinduism, not the language.
    - Current: `Hindu`
    - Source: `Hindi`
    - Suggest: `Hindi`
    - en-US “Hindi”; pt-PT for the language is “Hindi”. “Hindu” designates a follower of Hinduism.
- `language-name-ml` — `toolkit/toolkit/intl/languageNames.ftl` — Malayalam is rendered as “Malaio”, which is Malay (already used for language-name-ms), so two different languages share one name.
    - Current: `Malaio`
    - Source: `Malayalam`
    - Suggest: `Malaiala`
    - en-US ml = “Malayalam”, ms = “Malay”; both are “Malaio” here, leaving Malayalam unnamed.
- `language-name-sg` — `toolkit/toolkit/intl/languageNames.ftl` — Sango is rendered as “Sangro”, which is not the language name.
    - Current: `Sangro`
    - Source: `Sango`
    - Suggest: `Sango`
    - en-US “Sango”; the extra “r” produces a different word.
- `language-name-su` — `toolkit/toolkit/intl/languageNames.ftl` — Sundanese is rendered as “Sudanês” (Sudanese), naming a nationality of Sudan rather than the Indonesian language.
    - Current: `Sudanês`
    - Source: `Sundanese`
    - Suggest: `Sundanês`
    - en-US “Sundanese”. Sudanese and Sundanese are unrelated.
- `region-name-ag` — `toolkit/toolkit/intl/regionNames.ftl` — Antigua and Barbuda is rendered as “Antígua e Barbados”, naming a different country (Barbados).
    - Current: `Antígua e Barbados`
    - Source: `Antigua and Barbuda`
    - Suggest: `Antígua e Barbuda`
    - en-US “Antigua and Barbuda”; Barbados is a separate country with its own entry (region-name-bb).
- `region-name-cw` — `toolkit/toolkit/intl/regionNames.ftl` — Curaçao is rendered as “Coração” (heart), not a place name.
    - Current: `Coração`
    - Source: `Curaçao`
    - Suggest: `Curaçau`
    - en-US “Curaçao”; pt-PT “Curaçau”. “Coração” means “heart”.
- `region-name-kg` — `toolkit/toolkit/intl/regionNames.ftl` — Kyrgyzstan is rendered as the non-existent “Kirziquistão”.
    - Current: `Kirziquistão`
    - Source: `Kyrgyzstan`
    - Suggest: `Quirguizistão`
    - en-US “Kyrgyzstan”; pt-PT “Quirguizistão”.
- `region-name-tw` — `toolkit/toolkit/intl/regionNames.ftl` — Taiwan is rendered with the archaic colonial name “Formosa”.
    - Current: `Formosa`
    - Source: `Taiwan`
    - Suggest: `Taiwan`
    - en-US “Taiwan”; current pt-PT usage is “Taiwan”, and “Formosa” also names a province of Argentina.
- `region-name-xw` — `toolkit/toolkit/intl/regionNames.ftl` — West Bank is rendered literally as “Banco Ocidental” (a bank, financial institution).
    - Current: `Banco Ocidental`
    - Source: `West Bank`
    - Suggest: `Cisjordânia`
    - en-US “West Bank”; the territory is “Cisjordânia” in Portuguese.

### C. Grammar, agreement & spelling

- `toolbar-switcher-customizable-label` — `browser/browser/aiWindow.ftl` — “Smart windows” translated as “janelas Inteligentes” in one tooltip and left as “Janelas Smart” in the v2 variant of the same button.
    - Current: `Alternar entre as janelas Inteligentes e Clássicas.`
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic windows.`
    - Suggest: `Alternar entre as Janelas Smart e Clássicas.`
    - The two tooltips label the same switcher button; one of them must be wrong, and “Inteligentes” diverges from the Smart Window brand used everywhere else in the file.
- `appmenu-addon-post-install-message3` — `browser/browser/appMenuNotifications.ftl` — “add-ons” rendered as “extensões”, narrowing the term the tree renders as “complementos”.
    - Current: `Controle as suas extensões e temas através do menu da aplicação.`
    - Source: `Manage your add-ons and themes through the application menu.`
    - Suggest: `Controle os seus complementos e temas através do menu da aplicação.`
    - Throughout this partition “add-on” is “complemento” and “extension” is “extensão”; here the message covers all add-ons, not only extensions.
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — “Preset” rendered as “Pré-ajuste” in one profiler preset description while all the others use “Predefinição”.
    - Current: `Pré-ajuste para investigar erros de aprendizagem automática`
    - Source: `Preset for investigating machine learning bugs in { -brand-shorter-name }.`
    - Suggest: `Predefinição para investigar erros de aprendizagem automática`
    - Same term, same list of profiler presets; the odd one out is inconsistent with its eight siblings.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — Double space in visible text before the brand placeable
    - Current: `se altera do  { -brand-short-name } para outro navegador`
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
    - Suggest: `se altera do { -brand-short-name } para outro navegador`
    - Two spaces appear between "do" and the brand name in the rendered sentence shown in the Windows Task Scheduler description.
- `trustpanel-list-label-fingerprinter` — `browser/browser/browser.ftl` — “Fingerprinters” rendered as “known identifiers”, inconsistent with “identificadores digitais” used for the same term elsewhere in the same panel.
    - Current: `{ $count } identificador conhecido`
    - Source: `{$count ->} [one] { $count } Fingerprinters [other] { $count } Fingerprinters`
    - Suggest: `{ $count } identificador digital`
    - trustpanel-fingerprinter-blocking-tab-header in the same file renders fingerprinter as “identificador digital”; “identificador conhecido” names something else entirely in the blocked-items list.
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — English “AI” left untranslated in the message body while the heading of the same warning uses “IA”.
    - Current: `chatbot AI`
    - Source: `heading: AI chatbot won’t get your full selection message: {$selectionLength ->} [other] You’ve selected about { $selectionLength } characters. The number of characters we can send to the AI chatbot is about { $maxLengt…`
    - Suggest: `chatbot de IA`
    - The heading of the same message says “O chatbot de IA…”; the body switches to the English abbreviation.
- `migration-wizard-safari-permissions-sub-header` — `browser/browser/migrationWizard.ftl` — Safari bookmarks are called "favoritos", the term this file reserves for Internet Explorer and Edge.
    - Current: `Para importar os favoritos e histórico de navegação do Safari:`
    - Source: `To import Safari bookmarks and browsing history:`
    - Suggest: `Para importar os marcadores e o histórico de navegação do Safari:`
    - The developer comment on migration-favorites-option-label states that "Favorites" is used only for IE/Edge terminology; en-US here says "Safari bookmarks", which the locale renders "marcadores".
- `newtab-clock-widget-input-nickname` — `browser/browser/newtab/newtab.ftl` — “Nickname” left in English while the same concept is translated elsewhere in the widget.
    - Current: `Nickname (opcional)`
    - Source: `aria-label: Nickname (optional) label: Nickname (optional) placeholder: Add a nickname`
    - Suggest: `Nome alternativo (opcional)`
    - newtab-clock-widget-label-nickname-with-value translates the same term as “Nome alternativo”, so the field label and the value label name the same thing differently, one of them in English.
- `fx-backup-opt-in-filepath-label` — `browser/browser/newtab/onboarding.ftl` — Microsoft brand name miscapitalized as “Onedrive”.
    - Current: `tal como o Onedrive`
    - Source: `Pick a place you plan to transfer to a new device, like OneDrive.`
    - Suggest: `tal como o OneDrive`
    - The product is “OneDrive”, spelled correctly in create-backup-screen-1-backup-body in the same file.
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — “Mozilla Foundation” translated here but kept in English in the parallel string.
    - Current: `apoiado pela Fundação Mozilla`
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet more open, accessible, and better for everyone.`
    - Suggest: `apoiado pela Mozilla Foundation`
    - onboarding-gratitude-security-and-privacy-subtitle, the same sentence on a sibling screen, keeps “Mozilla Foundation”; brand names should not be translated per the brand.ftl guidance.
- `welcome-back-onboarding-pill-label-tabs` — `browser/browser/newtab/onboarding.ftl` — Half-translated feature label leaves “Tidy” in English.
    - Current: `Separadores Tidy`
    - Source: `Tidy Tabs`
    - Suggest: `Separadores organizados`
    - “Tidy Tabs” is descriptive, not a protected brand (the matching card label translates it as “Organize com separadores verticais e grupos”); “Tidy” conveys nothing to a Portuguese reader.
- `briefcase-avatar-alt` — `browser/browser/profiles.ftl` — "Briefcase" is rendered "Pasta", colliding with the "Folder" avatar in the same list, and conflicting with its own tooltip which says "mala".
    - Current: `Pasta`
    - Source: `alt: Briefcase`
    - Suggest: `Mala`
    - folder-avatar-alt is also "Pasta", so two distinct icons get the same accessible name, while briefcase-avatar-tooltip reads "Aplicar avatar de mala".
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — The Google Play Store brand name is lowercased in the plural variant.
    - Current: `google Play Store`
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
    - Suggest: `Google Play Store`
    - Brand names must keep their official casing; the singular variant of the same message correctly reads "Google Play Store".
- `protections-panel-etp-toggle-on` — `browser/browser/protectionsPanel.ftl` — The aria-label calls the feature "Proteção avançada contra a monitorização" while the label and every sibling string use "Proteção melhorada contra a monitorização".
    - Current: `Proteção avançada contra a monitorização: ativada para { $host }`
    - Source: `aria-label: Enhanced Tracking Protection: On for { $host } description: On for this site label: Enhanced Tracking Protection`
    - Suggest: `Proteção melhorada contra a monitorização: ativada para { $host }`
    - Enhanced Tracking Protection is rendered "Proteção melhorada contra a monitorização" everywhere else, including the .label of this very message and protections-panel-etp-toggle-off.
- `safeb-blocked-phishing-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Wrong clitic pronoun: "levar-lhe" instead of "levá-lo"
    - Current: `poderia tentar levar-lhe a fazer algo perigoso`
    - Source: `{ -brand-short-name } blocked this page because it may trick you into doing something dangerous like installing software or revealing personal information like passwords or credit cards.`
    - Suggest: `poderia tentar levá-lo a fazer algo perigoso`
    - "levar" takes a direct object here, so the accusative clitic (levá-lo/levá-la) is required; the dative "lhe" is ungrammatical.
- `removed-search-engine-message2` — `browser/browser/search.ftl` — "settings" is rendered "configurações" instead of the locale's "definições".
    - Current: `vá às configurações`
    - Source: `<strong>Your default search engine has been changed.</strong> { $oldEngine } is no longer available as a default search engine in { -brand-short-name }. { $newEngine } is now your default search engine. To change to ano…`
    - Suggest: `aceda às definições`
    - pt-PT consistently renders Settings as "Definições" (see reset-search-settings-message in the same file and menu-settings in menubar.ftl); "configurações" is the Brazilian term and points the user at a menu entry with a different name.
- `split-view-menuitem-reverse-tabs` — `browser/browser/tabbrowser.ftl` — "Reverse Tabs" rendered "Reverter separadores" (revert/undo) while the identical en-US string elsewhere is "Inverter separadores".
    - Current: `Reverter separadores`
    - Source: `label: Reverse Tabs`
    - Suggest: `Inverter separadores`
    - The developer comment says "Reverse" means reversing the order of the split-view tabs; "Reverter" means to undo, and tab-context-reverse-split-view in the same file uses "Inverter".
- `unified-extensions-notice-safe-mode` — `browser/browser/unifiedExtensions.ftl` — Troubleshoot Mode is rendered "modo de Resolução de problemas" instead of the locale's "modo de diagnóstico".
    - Current: `O modo de Resolução de problemas desativou todas as extensões.`
    - Source: `message: All extensions have been disabled by Troubleshoot Mode.`
    - Suggest: `O modo de diagnóstico desativou todas as extensões.`
    - menubar.ftl and safeMode.ftl consistently name the feature "Modo de diagnóstico", so this message points users at a mode they cannot find under that name.
- `newTabContainer.tooltip` — `browser/chrome/browser/browser.properties` — Same source phrase "Open a new tab (%S)" rendered as imperative here but infinitive in newTabButton.tooltip
    - Current: `Abra um novo separador (%S)`
    - Source: `Open a new tab (%S) Press and hold to open a new container tab`
    - Suggest: `Abrir um novo separador (%S)`
    - newTabButton.tooltip translates the identical English as "Abrir um novo separador (%S)"; tooltips in this file are uniformly infinitive, so the imperative here is the inconsistent one.
- `errorReportFalseDeceptiveMessage` — `browser/chrome/browser/safebrowsing/safebrowsing.properties` — Wrong preposition in time expression: "a esta altura"
    - Current: `Não é possível reportar este erro a esta altura.`
    - Source: `It’s not possible to report this error at this time.`
    - Suggest: `Não é possível reportar este erro nesta altura.`
    - pt-PT uses "nesta altura" / "de momento"; "a esta altura" is a pt-BR construction. The same text appears in blockedSite.ftl (safeb-report-false-deceptive-error-message).
- `permission.speaker.label` — `browser/chrome/browser/sitePermissions.properties` — Permission label uses imperative "Selecione" instead of the infinitive used by all sibling labels
    - Current: `Selecione os altifalantes`
    - Source: `Select speakers`
    - Suggest: `Selecionar altifalantes`
    - The comment describes it as the short form of "(permission to) Choose and change audio output devices", and every other permission.*.label in the file is an infinitive ("Utilizar a câmara", "Aceder a dispositivos MIDI"). The imperative reads as a command to the user rather than a permission name.
- `state.current.allowedForSession` — `browser/chrome/browser/sitePermissions.properties` — Current-state label uses an infinitive ("Permitir") instead of the state "Permitido"
    - Current: `Permitir para a sessão`
    - Source: `Allowed for Session`
    - Suggest: `Permitido para a sessão`
    - The developer comment says these labels display *active permission states*; the sibling strings use participles ("Permitido", "Bloqueado", "Bloqueado temporariamente"). The infinitive reads as an action to take, not the state in effect, and duplicates state.multichoice.allowForSession.
- `state.current.allowedTemporarily` — `browser/chrome/browser/sitePermissions.properties` — Current-state label uses an infinitive instead of the state "Permitido temporariamente"
    - Current: `Permitir temporariamente`
    - Source: `Allowed Temporarily`
    - Suggest: `Permitido temporariamente`
    - Same defect as state.current.allowedForSession: the comment marks this as a displayed state, and the parallel string state.current.blockedTemporarily correctly uses "Bloqueado temporariamente".
- `unsafeContentType` — `browser/chrome/overrides/appstrings.properties` — "cuja" incorrectly followed by an article
    - Current: `cuja a abertura pode não ser segura`
    - Source: `The page you are trying to view cannot be shown because it is contained in a file type that may not be safe to open. Please contact the website owners to inform them of this problem.`
    - Suggest: `cuja abertura pode não ser segura`
    - In Portuguese the relative possessive "cujo/cuja" is never followed by a definite article.
- `DirText` — `browser/installer/override.properties` — Instruction names a button (“Procurar”) that is labelled “Explorar” in the same dialog.
    - Current: `clique em Procurar e selecione outra pasta`
    - Source: `Setup will install $BrandFullNameDA in the following folder. To install in a different folder, click Browse and select another folder. $_CLICK`
    - Suggest: `clique em Explorar e selecione outra pasta`
    - BrowseBtn in this file is translated as “Explo&rar…”, so the instruction points the user to a button that does not exist with that name.
- `netmonitor.headers.raw` — `devtools/client/netmonitor.properties` — “Raw” is rendered “Original” here but “Em bruto” on the request/response raw toggles in the same panel.
    - Current: `Original`
    - Source: `Raw`
    - Suggest: `Em bruto`
    - netmonitor.request.raw and netmonitor.response.raw both render the same en-US “Raw” as “Em bruto”; “Original” also collides with the originalFileURL tooltip wording.
- `requestCookies` — `devtools/client/netmonitor.properties` — “Request” is rendered “solicitação” here while every neighbouring label uses “pedido”.
    - Current: `Cookies de solicitação`
    - Source: `Request Cookies`
    - Suggest: `Cookies do pedido`
    - requestHeaders, paramsNoPayloadText, netmonitor.tab.request and the rest of the panel all use “pedido” for request; this single label breaks the panel's terminology.
- `netTimeout` — `dom/chrome/appstrings.properties` — Missing accent: “operaçao”.
    - Current: `A operaçao expirou ao tentar contactar %S.`
    - Source: `The operation timed out when attempting to contact %S.`
    - Suggest: `A operação expirou ao tentar contactar %S.`
    - Spelling error in a user-facing network error page.
- `PluginHangUIMessage` — `dom/chrome/dom/dom.properties` — Truncated verb: “deixado de responde”.
    - Current: `pode ter deixado de responde`
    - Source: `%S may be busy, or it may have stopped responding. You can stop the plugin now, or you can continue to see if the plugin will complete.`
    - Suggest: `pode ter deixado de responder`
    - The infinitive is “responder”; the final “r” is missing.
- `RequestStorageAccessNullPrincipal` — `dom/chrome/dom/dom.properties` — Gender disagreement: “um iframe isolada”.
    - Current: `como um iframe isolada sem o valor allow-same-origin`
    - Source: `document.requestStorageAccess() may not be called on a document with an opaque origin, such as a sandboxed iframe without allow-same-origin in its sandbox attribute.`
    - Suggest: `como uma iframe isolada sem o valor allow-same-origin`
    - “um … isolada” mixes masculine article with feminine adjective; the neighbouring string RequestStorageAccessSandboxed uses “numa iframe isolada”.
- `MimeNotCss` — `dom/chrome/layout/css.properties` — Broken clause: “devido ao seu tipo MIME … não é”.
    - Current: `não foi carregada devido ao seu tipo MIME, “%2$S”, não é “text/css”`
    - Source: `The stylesheet %1$S was not loaded because its MIME type, “%2$S”, is not “text/css”.`
    - Suggest: `não foi carregada porque o seu tipo MIME, “%2$S”, não é “text/css”`
    - “devido a” cannot introduce a finite clause; as written the sentence is ungrammatical and the reason reads as if the MIME type itself were the cause.
- `errPrematureEndOfComment` — `dom/chrome/layout/htmlparser.properties` — Missing preposition “para” makes the sentence ungrammatical.
    - Current: `Use “-->” terminar o comentário corretamente.`
    - Source: `Premature end of comment. Use “-->” to end a comment properly.`
    - Suggest: `Use “-->” para terminar o comentário corretamente.`
    - “Use X terminar” is not grammatical Portuguese; the infinitive needs “para”.
- `PERR_NOT_AVAILABLE` — `dom/chrome/layout/printing.properties` — Number disagreement: “Algumas funcionalidade”.
    - Current: `Algumas funcionalidade de impressão ainda não estão disponíveis.`
    - Source: `Some printing functionality is not currently available.`
    - Suggest: `Algumas funcionalidades de impressão ainda não estão disponíveis.`
    - “Algumas” and “estão” are plural but the noun is singular. PERR_NOT_IMPLEMENTED has the identical error.
- `accessError` — `dom/chrome/nsWebBrowserPersist.properties` — Number disagreement: “os conteúdo dessa pasta”.
    - Current: `porque não pode alterar os conteúdo dessa pasta`
    - Source: `%S could not be saved, because you cannot change the contents of that folder.  Change the folder properties and try again, or try saving in a different location.`
    - Suggest: `porque não pode alterar o conteúdo dessa pasta`
    - Plural article with singular noun; this is a user-facing save-failure dialog.
- `ignoringDuplicateSrc` — `dom/chrome/security/csp.properties` — Typo: “suplicada” instead of “duplicada”.
    - Current: `A ignorar fonte suplicada %1$S`
    - Source: `Ignoring duplicate source %1$S`
    - Suggest: `A ignorar fonte duplicada %1$S`
    - “suplicada” is not a word; the source says “duplicate source”.
- `mediastatus-fallback-title` — `dom/dom/media.ftl` — Missing “a” in the progressive construction.
    - Current: `está reproduzir media`
    - Source: `{ -brand-short-name } is playing media`
    - Suggest: `está a reproduzir multimédia`
    - European Portuguese requires “estar a + infinitive”; the string is user-visible in the media/notification title.
- `MOZILLA_PKIX_ERROR_V1_CERT_USED_AS_CA` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo: “utiliado”.
    - Current: `Foi utiliado um certificado X.509 versão 1`
    - Source: `An X.509 version 1 certificate that is not a trust anchor was used to issue the server’s certificate. X.509 version 1 certificates are deprecated and should not be used to sign other certificates.`
    - Suggest: `Foi utilizado um certificado X.509 versão 1`
    - Missing “z” in “utilizado”.
- `certErrorMitM2` — `security/manager/chrome/pipnss/pipnss.properties` — Missing infinitive ending: “ajuda a assegura”.
    - Current: `O armazenamento CA ajuda a assegura que`
    - Source: `%S is backed by the non-profit Mozilla, which administers a completely open certificate authority (CA) store. The CA store helps ensure that certificate authorities are following best practices for user security.`
    - Suggest: `O armazenamento CA ajuda a assegurar que`
    - “ajudar a” requires the infinitive “assegurar”.
- `pageInfo_WeakCipher` — `security/manager/chrome/pippki/pippki.properties` — Unconjugated verb: “Outras pessoas poder ver”.
    - Current: `Outras pessoas poder ver a sua informação`
    - Source: `Your connection to this website uses weak encryption and is not private. Other people can view your information or modify the website’s behavior.`
    - Suggest: `Outras pessoas podem ver a sua informação`
    - The main clause has no finite verb; this text is shown in the Page Info security panel.
- `pkcs12-info-no-smartcard-backup` — `security/manager/security/certificates/certManager.ftl` — Agreement error and mistranslated “hardware security device”.
    - Current: `a partir de um dispositivos com segurança como, por exemplo, um smart card`
    - Source: `It is not possible to back up certificates from a hardware security device such as a smart card.`
    - Suggest: `a partir de um dispositivo de segurança de hardware como, por exemplo, um smart card`
    - “um dispositivos” mixes singular article with plural noun, and “dispositivo com segurança” is not the established term (“dispositivo de segurança” is used throughout deviceManager.ftl and pipnss).
- `pkcs12-unknown-err-restore` — `security/manager/security/certificates/certManager.ftl` — English “for” left in place of “por”.
    - Current: `Falhou a restauração do ficheiro PKCS #12 for razões desconhecidas.`
    - Source: `Failed to restore the PKCS #12 file for unknown reasons.`
    - Suggest: `Falhou a restauração do ficheiro PKCS #12 por razões desconhecidas.`
    - The adjacent strings pkcs12-unknown-err-backup and pkcs12-unknown-err correctly use “por razões desconhecidas”.
- `mlmodel-description` — `toolkit/toolkit/about/aboutAddons.ftl` — Participle does not agree with the feminine plural subject.
    - Current: `Algumas funcionalidades e extensões no { -brand-short-name } são suportados`
    - Source: `Some features and extensions in { -brand-short-name } are powered by AI models that work locally on your device. This approach protects your privacy and, in many cases, speeds up performance. <a data-l10n-name="learn-mo…`
    - Suggest: `Algumas funcionalidades e extensões no { -brand-short-name } são suportadas`
    - “funcionalidades e extensões” are both feminine plural, so the participle must be “suportadas”.
- `about-glean-about-data-description` — `toolkit/toolkit/about/aboutGlean.ftl` — Missing preposition after “dependendo”.
    - Current: `dependendo     o que está à procura`
    - Source: `There are a few different tools you can use to see your data, depending on what you are looking for.`
    - Suggest: `dependendo do que está à procura`
    - “Depender” requires “de”; “dependendo o que” is ungrammatical.
- `about-glean-metrics-table-settings-timelines-circle-radius` — `toolkit/toolkit/about/aboutGlean.ftl` — Missing accent in “círculo”.
    - Current: `Raio do circulo`
    - Source: `Circle radius`
    - Suggest: `Raio do círculo`
    - “circulo” without the accent is a verb form; the noun is “círculo”.
- `about-logging-preset-media-playback-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Misspelled verb form “incluí” (1st person past) for “inclui”.
    - Current: `não incluí problemas de videoconferência`
    - Source: `Log modules to diagnose media playback issues (not video-conferencing issues)`
    - Suggest: `não inclui problemas de videoconferência`
    - The present-tense third person of “incluir” is “inclui”; “incluí” is the first-person preterite.
- `about-logging-unknown-logging-preset` — `toolkit/toolkit/about/aboutLogging.ftl` — Gender disagreement: masculine “Modelo” with feminine “desconhecida”.
    - Current: `Modelo de registo desconhecida`
    - Source: `Unknown logging preset “{ $v }“`
    - Suggest: `Modelo de registo desconhecido`
    - “Modelo” is masculine; the neighbouring string about-logging-unknown-profiler-preset correctly uses “desconhecido”.
- `about-logging-url-copied` — `toolkit/toolkit/about/aboutLogging.ftl` — Stray leading article makes the confirmation message an incomplete sentence.
    - Current: `As definições de registo copiadas para a área de transferência como um URL modelo`
    - Source: `Logging settings copied to the clipboard as a preset URL`
    - Suggest: `Definições de registo copiadas para a área de transferência como um URL de modelo`
    - With “As”, the clause has a subject and no predicate; en-US is a completed-action message (“Logging settings copied…”).
- `about-pdf-tagline` — `toolkit/toolkit/about/aboutPDF.ftl` — Mixed noun/infinitive list after “para”.
    - Current: `Uma ferramenta gratuita para leitura, fundir, assinar, comentar, e muito mais`
    - Source: `A free tool for reading, merging, signing, commenting, and more — with privacy built in`
    - Suggest: `Uma ferramenta gratuita para ler, fundir, assinar, comentar e muito mais`
    - “para leitura, fundir, assinar” mixes a noun with infinitives in the same coordinated list, which is ungrammatical.
- `profiles-delete-profile-confirm` — `toolkit/toolkit/about/aboutProfiles.ftl` — Stray “não” leaves a broken double negative in the deletion warning.
    - Current: `e não esta ação não pode ser desfeita`
    - Source: `Deleting a profile will remove the profile from the list of available profiles and cannot be undone. You may also choose to delete the profile data files, including your settings, certificates and other user-related dat…`
    - Suggest: `e esta ação não pode ser desfeita`
    - The first “não” is left over from an edit and makes the sentence ungrammatical in a destructive-action confirmation.
- `about-reader-custom-colors-selection-highlight2` — `toolkit/toolkit/about/aboutReader.ftl` — Wrong word order in the idiom “em voz alta”.
    - Current: `Realce para ler em alta voz`
    - Source: `label: Highlighter for read aloud title: Edit color`
    - Suggest: `Realce para ler em voz alta`
    - The Portuguese idiom for “aloud” is “em voz alta”; “em alta voz” is a calque.
- `about-telemetry-process` — `toolkit/toolkit/about/aboutTelemetry.ftl` — English word order leaves “content processo” in the subsection header.
    - Current: `{ $process } processo`
    - Source: `{ $process } process`
    - Suggest: `processo { $process }`
    - In Portuguese the noun precedes the qualifier; with $process = “content” the header currently reads “content processo”.
- `about-telemetry-telemetry-client-doc` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Misspelled verb “incluí” for “inclui”.
    - Current: `incluí definições para conceitos`
    - Source: `The <a data-l10n-name="client-doc-link">Firefox Telemetry client documentation</a> includes definitions for concepts, API documentation and data references.`
    - Suggest: `inclui definições para conceitos`
    - Third person present of “incluir” is “inclui”; “incluí” is the first-person preterite.
- `certificate-viewer-exponent` — `toolkit/toolkit/about/certviewer.ftl` — Misspelling of “Expoente”.
    - Current: `Exponente`
    - Source: `Exponent`
    - Suggest: `Expoente`
    - The Portuguese term for the RSA exponent is “expoente”; “exponente” is not a Portuguese word.
- `about-config-intro-warning-checkbox` — `toolkit/toolkit/about/config.ftl` — Indicative instead of future subjunctive after “quando”, plus redundant subject pronoun.
    - Current: `Avisar-me quando eu tento aceder a estas preferências`
    - Source: `Warn me when I attempt to access these preferences`
    - Suggest: `Avisar-me quando tentar aceder a estas preferências`
    - A future conditional clause with “quando” requires the future subjunctive (“tentar”); “quando eu tento” is ungrammatical here.
- `url-classifier-debug-modules` — `toolkit/toolkit/about/url-classifier.ftl` — Adjective does not agree with the plural noun.
    - Current: `Módulos de registo atual`
    - Source: `Current log modules`
    - Suggest: `Módulos de registo atuais`
    - en-US “Current log modules” qualifies the modules, which are plural; as written it qualifies “registo”.
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — “bounce tracker” is translated despite the developer comment saying not to translate it, and inconsistently with the sibling string.
    - Current: `um rastreador de rejeições`
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
    - Suggest: `um bounce tracker`
    - The comment states: Do not translate "bounce tracker"; btp-warning-tracker-classified in the same file keeps it in English.

### D. Terminology, register & consistency

- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — Duplicated word “como como”.
    - Current: `tais como como o bloqueio de rastreadores`
    - Source: `We’ll erase every search and sign-in when you close all your Private Windows. { -brand-short-name }’s built-in protections are on here too, like blocking trackers.`
    - Suggest: `tais como o bloqueio de rastreadores`
    - Typo repeating “como” in a user-visible sentence.
- `error-short-desc-text` — `browser/browser/aboutRobots.ftl` — “visitar-lhe” uses an indirect pronoun with a transitive verb.
    - Current: `Viemos visitar-lhe em paz e de boa vontade!`
    - Source: `We have come to visit you in peace and with goodwill!`
    - Suggest: `Viemos visitar-vos em paz e de boa vontade!`
    - “visitar” takes a direct object, so the clitic must be -o/-vos, not -lhe; the surrounding page addresses humans in the plural (“Bem-vindos, humanos!”).
- `backup-service-error-unsupported-application` — `browser/browser/backupSettings.ftl` — Duplicated negation word “não não” in the backup error message.
    - Current: `não não foi criado pelo`
    - Source: `heading: This file isn’t working message: The file you chose was not created by { -brand-short-name }. Choose a different file and try again.`
    - Suggest: `não foi criado pelo`
    - Plain typo producing an ungrammatical double negation in a user-facing error message.
- `settings-data-backup-header2` — `browser/browser/backupSettings.ftl` — Possessive without the definite article (“seus marcadores”), which is not pt-PT usage.
    - Current: `Proteja automaticamente seus marcadores, histórico e outros dados.`
    - Source: `description: Automatically protect your bookmarks, history, and other data. label: Backup`
    - Suggest: `Proteja automaticamente os seus marcadores, histórico e outros dados.`
    - The rest of the tree consistently uses “os seus …”; dropping the article is Brazilian usage.
- `settings-data-backup-restore-scheduled-off` — `browser/browser/backupSettings.ftl` — Possessive without the definite article (“seus dados”), which is not pt-PT usage.
    - Current: `para restaurar seus dados`
    - Source: `description: Use a { -brand-product-name } backup from another device to restore your data. label: Restore your data`
    - Suggest: `para restaurar os seus dados`
    - The sibling description in the same file uses “os seus dados do { -brand-product-name }”; the article is required in pt-PT.
- `data-reporting-notification-message` — `browser/browser/browser.ftl` — Stray preposition makes the clause ungrammatical: “possamos a melhorar”.
    - Current: `para que possamos a melhorar a sua experiência`
    - Source: `{ -brand-short-name } automatically sends some data to { -vendor-short-name } so that we can improve your experience.`
    - Suggest: `para que possamos melhorar a sua experiência`
    - “poder” takes a bare infinitive; the extra “a” is a grammar error.
- `reader-view-enter-button` — `browser/browser/browser.ftl` — “Enter Reader View” rendered without the required preposition: “Entrar Visualização de Leitura”.
    - Current: `Entrar Visualização de Leitura`
    - Source: `aria-label: Enter Reader View`
    - Suggest: `Entrar na Visualização de Leitura`
    - “Entrar” requires “em/na” before its complement; the current accessible name is ungrammatical.
- `urlbar-autoplay-notification-anchor` — `browser/browser/browser.ftl` — “Abrir” misspelled as “Abri” in the autoplay panel tooltip.
    - Current: `Abri painel de reprodução automática`
    - Source: `tooltiptext: Open autoplay panel`
    - Suggest: `Abrir painel de reprodução automática`
    - Missing final “r”; all sibling anchor tooltips use “Abrir painel…”.
- `urlbar-result-explanation-last-visited-days` — `browser/browser/browser.ftl` — Pleonastic “há … atrás” (and a stray double space in the plural variant).
    - Current: `Visitou pela última vez há { $daysAgo } dia atrás`
    - Source: `{$daysAgo ->} [one] You last visited { $daysAgo } day ago [other] You last visited { $daysAgo } days ago`
    - Suggest: `Visitou pela última vez há { $daysAgo } dia`
    - “há” and “atrás” both express past time; combining them is a recognised grammar error, repeated in the weeks and months variants. The plural variant also has two spaces before the number.
- `pending-crash-reports-message-new` — `browser/browser/contentCrash.ftl` — Number agreement error in the singular variant: “um relatórios”.
    - Current: `Tem um relatórios de falha não enviado`
    - Source: `{$reportCount ->} [one] You have a recent unsent crash report [other] You have { $reportCount } recent unsent crash reports`
    - Suggest: `Tem um relatório de falha não enviado`
    - Singular determiner with a plural noun; the rest of the variant is singular.
- `customize-mode-uidensity-menu-normal` — `browser/browser/customizeMode.ftl` — Stray ampersand left in the visible tooltip text: “&Normal”.
    - Current: `&Normal`
    - Source: `accesskey: N label: Normal tooltiptext: Normal`
    - Suggest: `Normal`
    - The “&” is a leftover accesskey marker that renders literally in the tooltip; the label of the same item is plain “Normal”.
- `callout-firefox-view-recently-closed-title` — `browser/browser/featureCallout.ftl` — “em um piscar de olhos” uses a non-pt-PT contraction-free form.
    - Current: `em um piscar de olhos`
    - Source: `Get back your closed tabs in a snap`
    - Suggest: `num piscar de olhos`
    - pt-PT contracts em + um to “num”; “em um” is Brazilian usage.
- `splitview-onboarding-callout-subtitle-1` — `browser/browser/featureCallout.ftl` — `splitview-onboarding-callout-subtitle-1` quotes “Adicionar vista dividida” but the string it names, `customkeys-view-add-split-view`, reads “Adicionar Vista Dividida”
    - Current: `Clique com o botão direito do rato neste separador e escolha “Adicionar vista dividida” para ver dois separadores em simultâneo.`
    - Source: `Right-click this tab and choose “Add Split View” to see two tabs at once.`
    - Suggest: `Adicionar Vista Dividida`
    - In the source this string quotes “Add Split View”, which is exactly the value of `customkeys-view-add-split-view` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firefoxview-tabpickup-signed-out-description2` — `browser/browser/firefoxView.ftl` — Ungrammatical “obter aos seus separadores”.
    - Current: `Para reassociar e obter aos seus separadores, inicie sessão na sua conta`
    - Source: `To reconnect and grab your tabs, sign in to your account.`
    - Suggest: `Para reassociar e obter os seus separadores, inicie sessão na sua conta`
    - “obter” takes a direct object; the preposition “a” is a leftover that makes the sentence ungrammatical.
- `ipprotection-feature-introduction-text-summer-promo-1` — `browser/browser/ipProtection.ftl` — Month name capitalized (“Agosto”), inconsistent with lowercase months used elsewhere in the same file.
    - Current: `31 de Agosto`
    - Source: `Turn it on to keep your browsing more private. <a data-l10n-name="summer-promo-link">Get unlimited bandwidth</a> and more locations to browse from. Now until August 31.`
    - Suggest: `31 de agosto`
    - Portuguese writes month names in lowercase, and the same file already uses “1 de setembro”; the capitalized form recurs in the summer-promo strings.
- `device-migration-fxa-spotlight-heavy-user-body` — `browser/browser/newtab/asrouter.ftl` — Agreement error: singular subject with plural verb and adjective.
    - Current: `Certifique-se que a informação importante – tais como, marcadores e palavras-passe – estão atualizadas e protegidas`
    - Source: `Make sure important info — like bookmarks and passwords — is updated and protected across all your devices.`
    - Suggest: `Certifique-se de que a informação importante — como marcadores e palavras-passe — está atualizada e protegida`
    - The subject “a informação importante” is singular, so “estão atualizadas e protegidas” does not agree; “tais como,” also carries a spurious comma.
- `pdf-default-notification-message` — `browser/browser/newtab/asrouter.ftl` — Misspelling of “predefinido” in a visible infobar heading.
    - Current: `predefindo`
    - Source: `<strong>Make { -brand-short-name } your default PDF reader?</strong> Use { -brand-short-name } to read and edit PDFs saved to your computer.`
    - Suggest: `predefinido`
    - “predefindo” is not a word; the correct spelling is used everywhere else in the same file (e.g. annotations-make-default-pdf-handler-title).
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — Subject-verb agreement error: “nada … devem”.
    - Current: `Porque nada, especialmente empecilhos de privacidade como os rastreadores, devem ficar entre si`
    - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
    - Suggest: `Porque nada, especialmente empecilhos de privacidade como os rastreadores, deve ficar entre si`
    - The subject is the singular “nada”; the verb must be “deve”.
- `newtab-custom-stories-toggle` — `browser/browser/newtab/newtab.ftl` — Pre-AO90 spelling “excepcional” where the tree uses “excecional”.
    - Current: `Conteúdo excepcional com curadoria da família { -brand-product-name }`
    - Source: `description: Exceptional content curated by the { -brand-product-name } family label: Recommended stories`
    - Suggest: `Conteúdo excecional com curadoria da família { -brand-product-name }`
    - The parallel string home-prefs-stories-header2 in the same file uses the current European Portuguese spelling “excecional”.
- `newtab-sports-widget-message-day-in-play-body` — `browser/browser/newtab/newtab.ftl` — Verb form typo “vejas” in a list of imperatives.
    - Current: `foque-se na tarefa,  vejas as horas à volta do globo`
    - Source: `Follow the World Cup, stay on task, track time around the globe, and more.`
    - Suggest: `foque-se na tarefa, veja as horas à volta do globo`
    - The surrounding verbs use the polite imperative (“Siga”, “foque-se”); “vejas” is the second-person subjunctive and does not agree.
- `newtab-topic-selection-title` — `browser/browser/newtab/newtab.ftl` — Wrong article/gender in “a seu feed”.
    - Current: `personalizar a seu feed`
    - Source: `Select topics to fine-tune your feed`
    - Suggest: `personalizar o seu feed`
    - “feed” is treated as masculine elsewhere in the file (“no seu feed” in newtab-section-confirm-block-topic-p2); “a seu” is ungrammatical in any case.
- `create-backup-screen-3-location` — `browser/browser/newtab/onboarding.ftl` — Missing conjunction makes the question ungrammatical.
    - Current: `Onde quer a sua cópia de segurança seja guardada?`
    - Source: `Where do you want your backup saved?`
    - Suggest: `Onde quer que a sua cópia de segurança seja guardada?`
    - “querer” with a subjunctive clause requires “que”; as written the sentence does not parse in Portuguese.
- `mr2-onboarding-thank-you-text` — `browser/browser/newtab/onboarding.ftl` — Missing preposition in the progressive construction “estamos a tornar”.
    - Current: `estamos tornar a Internet mais segura`
    - Source: `{ -brand-short-name } is an independent browser backed by a non-profit. Together, we’re making the web safer, healthier, and more private.`
    - Suggest: `estamos a tornar a Internet mais segura`
    - European Portuguese requires “estar a + infinitivo”; “estamos tornar” is ungrammatical.
- `mr2022-onboarding-existing-pin-subtitle` — `browser/browser/newtab/onboarding.ftl` — Misspelled imperative “Começe”.
    - Current: `Começe uma Internet mais saudável`
    - Source: `Launch a healthier internet from anywhere with a single click. Our latest update is packed with new things we think you’ll adore.`
    - Suggest: `Comece uma Internet mais saudável`
    - The imperative of “começar” is “comece”; “começe” is a spelling error in a prominent onboarding headline.
- `onboarding-existing-tabs-title` — `browser/browser/newtab/onboarding.ftl` — Number agreement error: “separadores vertical”.
    - Current: `Os separadores vertical estão aqui`
    - Source: `Vertical tabs are here`
    - Suggest: `Os separadores verticais estão aqui`
    - The adjective must agree in number with the plural noun; the sibling string onboarding-existing-tabs-title2 correctly uses “separadores verticais”.
- `welcome-back-onboarding-title` — `browser/browser/newtab/onboarding.ftl` — Missing accent in “construídas”.
    - Current: `Novas funcionalidades construidas para o ajudar`
    - Source: `New features built to help you do more`
    - Suggest: `Novas funcionalidades construídas para o ajudar`
    - The participle of “construir” carries an acute accent on the i: “construídas”.
- `policy-DisableProfileRefresh2` — `browser/browser/policies/policies-descriptions.ftl` — Stray clitic pronoun makes the final clause ungrammatical.
    - Current: `quando este não o foi utilizado durante algum tempo`
    - Source: `Disable the Refresh { -brand-short-name } button in Troubleshooting Information (about:support) and on support.mozilla.org, as well as the prompt offering to refresh { -brand-short-name } when it hasn’t been used for a…`
    - Suggest: `quando este não foi utilizado durante algum tempo`
    - The passive “foi utilizado” already has its subject in “este”; the extra “o” is a leftover object pronoun.
- `connection-proxy-autologin-checkbox` — `browser/browser/preferences/connection.ftl` — Wrong clitic: “autentica-lhe” instead of the direct-object “autentica-o”.
    - Current: `Esta opção autentica-lhe silenciosamente nos proxies`
    - Source: `accesskey: i label: Do not prompt for authentication if password is saved tooltiptext: This option silently authenticates you to proxies when you have saved credentials for them. You will be prompted if authentication f…`
    - Suggest: `Esta opção autentica-o silenciosamente nos proxies`
    - “Autenticar” takes a direct object, so the dative clitic “lhe” is ungrammatical here.
- `fonts-langgroup-khmer` — `browser/browser/preferences/fonts.ftl` — Misspelled demonym “Cambodjano”.
    - Current: `Cambodjano`
    - Source: `label: Khmer`
    - Suggest: `Khmer`
    - Current pt-PT orthography is “cambojano” (no “d”); the script name “Khmer” is also the more accurate label for this font group.
- `permissions-exceptions-popup-window3` — `browser/browser/preferences/permissions.ftl` — Typo: “Popus” for “Pop-ups”.
    - Current: `Sites permitidos - Popus e redirecionamentos de terceiros`
    - Source: `style: { permissions-window2.style } title: Allowed Websites - Pop-ups and Third-Party Redirects`
    - Suggest: `Sites permitidos - Pop-ups e redirecionamentos de terceiros`
    - The window title misspells pop-ups, which is written correctly in permissions-exceptions-popup-desc2 and in preferences.ftl.
- `permissions-site-xr-disable-desc` — `browser/browser/preferences/permissions.ftl` — Second sentence has no finite verb, leaving it ungrammatical.
    - Current: `O bloqueio de acesso aos seus dispositivos de realidade virtual impedir algumas funcionalidades dos sites.`
    - Source: `This will prevent any websites not listed above from requesting permission to access your virtual reality devices. Blocking access to your virtual reality devices may break some website features.`
    - Suggest: `O bloqueio de acesso aos seus dispositivos de realidade virtual pode quebrar algumas funcionalidades dos sites.`
    - en-US “Blocking access … may break some website features.”; “impedir” is an infinitive with no auxiliary and the modal “may” is lost, so the sentence does not parse.
- `autofill-reauth-payment-methods-checkbox-2` — `browser/browser/preferences/preferences.ftl` — Checkbox label is ungrammatical (“para o preenchimento automaticamente e gerir”).
    - Current: `Exigir início de sessão do dispositivo para o preenchimento automaticamente e gerir métodos de pagamento`
    - Source: `accesskey: o label: Require device sign in to autofill and manage payment methods`
    - Suggest: `Exigir início de sessão do dispositivo para preencher automaticamente e gerir métodos de pagamento`
    - en-US “Require device sign in to autofill and manage payment methods”; the coordination mixes a noun phrase with an adverb and then an infinitive, so the label does not read as Portuguese.
- `browsing-media-control` — `browser/browser/preferences/preferences.ftl` — Typo: “ausculatores”.
    - Current: `Controlar media via teclado, ausculatores ou interface virtual`
    - Source: `accesskey: v label: Control media via keyboard, headset, or virtual interface`
    - Suggest: `Controlar media via teclado, auscultadores ou interface virtual`
    - Misspelling of “auscultadores”.
- `content-blocking-etp-standard-tcp-rollout-description` — `browser/browser/preferences/preferences.ftl` — Gender disagreement (“as mesmas” for “os cookies”) plus Brazilian-style “você”.
    - Current: `contém cookies para o site em que você estiver, portanto, os rastreadores não podem utilizar as mesmas para o monitorizar`
    - Source: `Total Cookie Protection contains cookies to the site you’re on, so trackers can’t use them to follow you between sites.`
    - Suggest: `contém os cookies no site em que está, pelo que os rastreadores não os podem utilizar para o monitorizar`
    - “Cookies” is masculine in this tree (“os cookies”), so “as mesmas” disagrees; the rest of the tree also uses the null subject instead of “você”.
- `history-custom-section-header` — `browser/browser/preferences/preferences.ftl` — Missing relative pronoun “que” makes the sentence ungrammatical.
    - Current: `Personalize o pretende que o { -brand-short-name } memorize quando fecha o navegador.`
    - Source: `description: Customize what you want { -brand-short-name } to remember when you close the browser. label: Advanced settings`
    - Suggest: `Personalize o que pretende que o { -brand-short-name } memorize quando fecha o navegador.`
    - Same defect as history-section-header: “Personalize o pretende” is missing “que”.
- `history-section-header` — `browser/browser/preferences/preferences.ftl` — Missing relative pronoun “que” makes the sentence ungrammatical.
    - Current: `Escolha o pretende que o { -brand-short-name } memorize quando fecha o navegador.`
    - Source: `description: Choose what you want { -brand-short-name } to remember when you close the browser. label: History`
    - Suggest: `Escolha o que pretende que o { -brand-short-name } memorize quando fecha o navegador.`
    - en-US “Choose what you want { -brand-short-name } to remember…”; “Escolha o pretende” lacks the object pronoun “que”.
- `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl` — "app links" is rendered as "ligações da aplicação" (the application's links), which changes the meaning and conflicts with the other renderings of the term.
    - Current: `ligações da aplicação`
    - Source: `accesskey: A label: Allow sites to ask to open app links.`
    - Suggest: `ligações em aplicações`
    - The developer comment says app links are links a website asks to open in an app, like mailto: links. They are not links belonging to the application. Related strings use "ligações de aplicações" and "ligações em aplicações".
- `preferences-doh-default-detailed-desc-3` — `browser/browser/preferences/preferences.ftl` — Typo: “forncedor”.
    - Current: `Utilizar um forncedor local, se possível`
    - Source: `Use a local provider, if possible`
    - Suggest: `Utilizar um fornecedor local, se possível`
    - Misspelling of “fornecedor”, which is spelled correctly in every neighbouring DoH string.
- `security-block-uncommon-software` — `browser/browser/preferences/preferences.ftl` — Wrong clitic: “Avisar-lhe” instead of “Avisá-lo”.
    - Current: `Avisar-lhe acerca de software não-solicitado e incomum`
    - Source: `accesskey: c label: Warn you about unwanted and uncommon software`
    - Suggest: `Avisá-lo acerca de software não-solicitado e incomum`
    - “Avisar” takes a direct object in Portuguese, so the dative “lhe” is ungrammatical.
- `sitedata-cookies-exceptions2` — `browser/browser/preferences/preferences.ftl` — Duplicated “que” in the description.
    - Current: `Pode especificar que sites que estão, sempre ou nunca, autorizados`
    - Source: `accesskey: x description: You can specify which websites are always or never allowed to use cookies and site data. label: Manage exceptions`
    - Suggest: `Pode especificar que sites estão, sempre ou nunca, autorizados`
    - The second “que” is a leftover and makes the relative clause ungrammatical.
- `site-data-removing-single-desc` — `browser/browser/preferences/siteDataSettings.ftl` — Missing “que” in “fazer com que”.
    - Current: `pode fazer com a sua sessão nos sites seja terminada`
    - Source: `Removing cookies and site data may log you out of websites. Are you sure you want to remove cookies and site data for <strong>{ $baseDomain }</strong>?`
    - Suggest: `pode fazer com que a sua sessão nos sites seja terminada`
    - The subordinating conjunction is incomplete, leaving the clause ungrammatical.
- `monitor-emails-tooltip` — `browser/browser/protections.ftl` — "monitorados" is a Brazilian form; pt-PT uses "monitorizados".
    - Current: `Ver os endereços de e-mail monitorados no { -monitor-brand-short-name }`
    - Source: `title: View monitored email addresses on { -monitor-brand-short-name }`
    - Suggest: `Ver os endereços de e-mail monitorizados no { -monitor-brand-short-name }`
    - The rest of the file consistently uses "monitorizar/monitorização"; "monitorado" is not the pt-PT form.
- `protection-report-page-summary` — `browser/browser/protections.ftl` — Brazilian spelling "controle" used instead of European Portuguese "controlo".
    - Current: `assumir o controle da sua segurança`
    - Source: `{ -brand-short-name } can protect your privacy behind the scenes while you browse. This is a personalized summary of those protections, including tools to take control of your online security.`
    - Suggest: `assumir o controlo da sua segurança`
    - pt-PT uses "controlo"; the parallel string protection-report-page-summary-default avoids the form entirely, so this is an isolated BR spelling.
- `auto-safe-mode-description` — `browser/browser/safeMode.ftl` — Verb typo: "poder" instead of "pode".
    - Current: `Isto poder ter sido causado por complementos`
    - Source: `{ -brand-short-name } closed unexpectedly while starting. This might be caused by add-ons or other problems. You can try to resolve the problem by troubleshooting in Safe Mode.`
    - Suggest: `Isto pode ter sido causado por complementos`
    - The infinitive leaves the sentence ungrammatical; en-US is "This might be caused by…".
- `protections-blocking-cookies-third-party` — `browser/browser/siteProtections.ftl` — Feminine agreement "bloqueadas" with the masculine noun "cookies".
    - Current: `Cookies de terceiros bloqueadas`
    - Source: `title: Third-Party Cookies Blocked`
    - Suggest: `Cookies de terceiros bloqueados`
    - Same agreement error as protections-blocking-cookies-trackers; neighbouring strings in the file use the masculine "bloqueados".
- `protections-blocking-cookies-trackers` — `browser/browser/siteProtections.ftl` — Feminine agreement "bloqueadas" with the masculine noun "cookies".
    - Current: `Cookies de monitorização entre sites bloqueadas`
    - Source: `title: Cross-Site Tracking Cookies Blocked`
    - Suggest: `Cookies de monitorização entre sites bloqueados`
    - The locale treats "cookie" as masculine ("Todos os cookies bloqueados", "Cookies de sites não visitados bloqueados" in the same file), so the feminine participle is an agreement error.
- `tabbrowser-allow-dialogs-to-get-focus` — `browser/browser/tabbrowser.ftl` — Wrong verb form "encaminhei" (first-person past) where a third-person plural subjunctive is required.
    - Current: `o encaminhei para o respetivo separador`
    - Source: `label: Allow notifications like this from { $domain } to take you to their tab`
    - Suggest: `o encaminhem para o respetivo separador`
    - The subject is "notificações"; "encaminhei" means "I forwarded", leaving the permission checkbox ungrammatical and confusing.
- `webrtc-allow-share-screen-and-microphone-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — Starts with the indicative "Permite que" where every sibling prompt uses the infinitive "Permitir que".
    - Current: `Permite que { $origin } forneça acesso`
    - Source: `Allow { $origin } to give { $thirdParty } access to your microphone and see your screen?`
    - Suggest: `Permitir que { $origin } forneça acesso`
    - All other webrtc-allow-share-* prompts begin "Permitir que…"; the indicative turns the permission question into a statement.
- `webrtc-indicator-menuitem-sharing-microphone-with-n-tabs` — `browser/browser/webrtcIndicator.ftl` — Missing space between the count and the word "separadores" in the plural variant.
    - Current: `A partilhar microfone com { $tabCount }separadores`
    - Source: `label: {$tabCount ->} [one] Sharing Microphone with { $tabCount } tab [other] Sharing Microphone with { $tabCount } tabs`
    - Suggest: `A partilhar microfone com { $tabCount } separadores`
    - All sibling variants include the space; rendered output reads "com 3separadores".
- `webrtc-reason-for-no-permanent-allow-insecure` — `browser/browser/webrtcIndicator.ftl` — Wrong pronoun case: "Para lhe proteger" instead of "Para o proteger".
    - Current: `Para lhe proteger`
    - Source: `Your connection to this site is not secure. To protect you, { -brand-short-name } will only allow access for this session.`
    - Suggest: `Para o proteger`
    - "Proteger" takes a direct object in pt-PT, so the indirect-object clitic "lhe" is ungrammatical.
- `unblockInsecure2` — `browser/chrome/browser/downloads/downloads.properties` — "conexão" used where the tree consistently uses "ligação"
    - Current: `entregue através de uma conexão HTTPS segura`
    - Source: `The download is offered over HTTP even though the current document was delivered over a secure HTTPS connection. If you proceed, the download may be corrupted or tampered with during the download process.`
    - Suggest: `entregue através de uma ligação HTTPS segura`
    - "connection" is rendered "ligação" everywhere else in this partition (identity.notSecure.tooltip, connectionFailure, netInterrupt, netReset, proxyConnectFailure). "conexão" is the pt-BR term.
- `MUI_TEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — Wrong pronoun form: “guiar-lhe” instead of “guiá-lo”.
    - Current: `Este assistente irá guiar-lhe na instalação`
    - Source: `This wizard will guide you through the installation of $BrandFullNameDA.  It is recommended that you close all other applications before starting Setup. This will make it possible to update relevant system files without…`
    - Suggest: `Este assistente irá guiá-lo na instalação`
    - “guiar” takes a direct object, so the clitic must be “-lo”, not the indirect “-lhe”; the same error appears in MUI_UNTEXT_WELCOME_INFO_TEXT.
- `accessibility.enable.enabledTitle` — `devtools/client/accessibility.properties` — Number agreement error: singular subject with plural verb and participle.
    - Current: `O serviço de acessibilidade serão ligados`
    - Source: `Accessibility service will be turned on for all tabs and windows.`
    - Suggest: `O serviço de acessibilidade será ligado`
    - “O serviço” is singular; the parallel string accessibility.disable.enabledTitle correctly uses “será desligado”.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Quebrar em…” but the string it names, `watchpoints.submenu`, reads “Interromper em…”
    - Current: `Clique com o botão direito num elemento no Inspetor e selecione “Quebrar em…” para adicionar um ponto de quebra`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Interromper em…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `individuals.state.error.full` — `devtools/client/memory.properties` — Ungrammatical “enquanto ao obter”.
    - Current: `Ocorreu um erro enquanto ao obter indivíduos no grupo`
    - Source: `There was an error while fetching individuals in the group`
    - Suggest: `Ocorreu um erro ao obter indivíduos no grupo`
    - “enquanto” and “ao” cannot be stacked; one of them must go.
- `perftools-description-local-build` — `devtools/client/perftools.ftl` — The conditional clause is ungrammatical and missing prepositions.
    - Current: `Se está criar um perfil uma compilação`
    - Source: `If you’re profiling a build that you have compiled yourself, on this machine, please add your build’s objdir to the list below so that it can be used to look up symbol information.`
    - Suggest: `Se está a criar um perfil de uma compilação`
    - “está criar” lacks “a”, and “um perfil uma compilação” lacks the linking preposition, leaving the sentence unparseable.
- `options-local-mode-behavior` — `devtools/client/toolbox-options.ftl` — Gender agreement error: “Os URLs … carregadas”.
    - Current: `Os URLs só podem ser carregadas`
    - Source: `Local Mode allows you to load local files via https URL without any external dependency. The URLs can only be loaded from tabs with DevTools opened.`
    - Suggest: `Os URLs só podem ser carregados`
    - The participle must agree with the masculine “Os URLs”.
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — Verb form typo: “forme escritos” instead of “forem escritos”.
    - Current: `assim que forme escritos`
    - Source: `title: Autocomplete CSS properties, values and selectors in Style Editor as you type`
    - Suggest: `assim que forem escritos`
    - “forme” is not a valid form here; the future subjunctive “forem” is required.
- `inactive-css-column-span` — `devtools/client/tooltips.ftl` — The verb is missing: “não efeito de expansão”.
    - Current: `não efeito de expansão`
    - Source: `<strong>{ $property }</strong> has no spanning effect on this element since it is not within a multi-column container.`
    - Suggest: `não tem efeito de expansão`
    - “tem” was dropped, leaving the sentence without a verb; every sibling tooltip reads “não tem efeito”.
- `inactive-css-not-for-internal-table-elements-except-table-cells` — `devtools/client/tooltips.ftl` — Pre-reform spelling “excepção”.
    - Current: `excepção`
    - Source: `<strong>{ $property }</strong> has no effect on internal table elements except table cells.`
    - Suggest: `exceção`
    - Under the current pt-PT orthography the word is “exceção”, as used elsewhere in the tree.
- _…and 22 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `about-logins-menu-menuitem-import-from-a-file` — `browser/browser/aboutLogins.ftl` — Menu item ends with a colon instead of the ellipsis used by the source and by the neighbouring items.
    - Current: `Importar de um ficheiro:`
    - Source: `Import from a File…`
    - Suggest: `Importar de um ficheiro…`
    - en-US is “Import from a File…”; the adjacent items in the same menu correctly end with “…”, which signals that a dialog follows.
- `fire-button-panel-choose-link` — `browser/browser/browser.ftl` — The label ends with three ASCII periods instead of the ellipsis character (…).
    - Current: `Escolher...`
    - Source: `Choose…`
    - Suggest: `Escolher…`
    - The locale convention is the single ellipsis character (char 371 vs ascii 27), and the en-US uses "…". The developer comment says the ellipsis tells the user that a dialog follows.
- `main-context-menu-edit-bookmark-with-shortcut-2` — `browser/browser/browserContext.ftl` — Missing space between the label and the shortcut in parentheses.
    - Current: `Editar marcador…({ $shortcut })`
    - Source: `aria-label: Edit Bookmark… tooltiptext: Edit bookmark ({ $shortcut })`
    - Suggest: `Editar marcador ({ $shortcut })`
    - The tooltip renders as “Editar marcador…(Ctrl+D)”; the equivalent add-bookmark tooltips in the same file keep a space before the parenthesis. Same defect in main-context-menu-edit-bookmark-with-shortcut.
- `contextual-manager-passwords-command-import` — `browser/browser/contextual-manager.ftl` — Menu item ends with a colon instead of the ellipsis used by the source.
    - Current: `Importar de um ficheiro:`
    - Source: `Import from a file…`
    - Suggest: `Importar de um ficheiro…`
    - en-US is “Import from a file…”; the sibling “Importar de outro navegador…” in the same menu uses the ellipsis.
- `connection-dns-over-https-url-custom` — `browser/browser/preferences/connection.ftl` — “DNS over HTTPS” rendered as “DNS sob HTTPS”.
    - Current: `Introduza o endereço que pretende utilizar para resolver DNS sob HTTPS`
    - Source: `accesskey: C label: Custom tooltiptext: Enter your preferred URL for resolving DNS over HTTPS`
    - Suggest: `Introduza o endereço que pretende utilizar para resolver DNS sobre HTTPS`
    - Same wrong preposition as the sibling tooltip; the established term is “DNS sobre HTTPS”.
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — “DNS over HTTPS” rendered as “DNS sob HTTPS” (DNS *under* HTTPS).
    - Current: `Utilize o endereço predefinido para resolver DNS sob HTTPS`
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
    - Suggest: `Utilize o endereço predefinido para resolver DNS sobre HTTPS`
    - The whole tree uses “DNS sobre HTTPS” (preferences.ftl, permissions.ftl); “sob” means “under” and is the wrong preposition.
- `more-from-moz-new-products-card2` — `browser/browser/preferences/moreFromMozilla.ftl` — Stray space before the final period.
    - Current: `Explore as nossas tecnologias experimentais e ideias mais recentes .`
    - Source: `description: Explore our latest ideas and experimental technologies. label: { -vendor-short-name } New Products`
    - Suggest: `Explore as nossas tecnologias experimentais e ideias mais recentes.`
    - A space separates the last word from the sentence-final period in text the user reads.
- `permissions-site-speaker-desc` — `browser/browser/preferences/permissions.ftl` — Uses “Você pode” and drops the article, unlike every other permissions description.
    - Current: `Você pode especificar quais sites que têm permissão`
    - Source: `The following websites have requested to select an audio output device. You can specify which websites are allowed to select an audio output device.`
    - Suggest: `Pode especificar quais os sites que têm permissão`
    - All sibling strings in this file use “Pode especificar quais os sites…”; the explicit “Você” and the missing “os” break the file's established form of address and phrasing.
- `containers-settings-button2` — `browser/browser/preferences/preferences.ftl` — “Settings” rendered as “Configurações” instead of “Definições”.
    - Current: `Configurações`
    - Source: `title: Settings`
    - Suggest: `Definições`
    - The whole preferences surface translates “Settings” as “Definições” (settings-page-title, preferences-profiles-settings-button); “Configurações” is the Brazilian term and is inconsistent here.
- `forms-primary-pw-on-2` — `browser/browser/preferences/preferences.ftl` — “Primary password” rendered as “palavra-passe primária” where the pane otherwise uses “principal”.
    - Current: `A palavra-passe primária está <strong>ATIVADA</strong>`
    - Source: `Primary password is <strong>ON</strong>`
    - Suggest: `A palavra-passe principal está <strong>ATIVADA</strong>`
    - Every other string in this section (forms-primary-pw-use, -set, -change, -on) uses “palavra-passe principal”, so the same feature is named two ways on one screen.
- `preferences-ai-controls-description` — `browser/browser/preferences/preferences.ftl` — Explicit “Você” subject, against the locale's null-subject address.
    - Current: `Você tem sempre uma escolha no { -brand-short-name }`
    - Source: `You always have a choice in { -brand-short-name }, including whether to use features enhanced with AI. More controls coming soon.`
    - Suggest: `Tem sempre uma escolha no { -brand-short-name }`
    - The preferences tree addresses the user with implicit subject verbs (“Pode…”, “Tem…”); “Você” is a Brazilian-style deviation.
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — Quotes an option name that does not match the actual checkbox label.
    - Current: `Se “Aplicar zoom apenas em texto” estiver ativado`
    - Source: `message: If “Zoom text only” is on and your default zoom isn’t 100%, some sites might not display content correctly.`
    - Suggest: `Se “Ampliar apenas o texto” estiver ativado`
    - The referenced setting is preferences-zoom-text-only, labelled “Ampliar apenas o texto”; the warning quotes a different wording so users cannot find the option.
- `security-privacy-issue-warning-ech` — `browser/browser/preferences/preferences.ftl` — “Encrypted Client Hello” rendered as “Cliente Encriptado do Hello”, different from the ech2 strings.
    - Current: `O Cliente Encriptado do Hello está desativado`
    - Source: `description: Encrypted Client Hello hides what sites you visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `O Encrypted Client Hello está desativado`
    - security-privacy-issue-warning-ech2 calls the same protocol “Cliente Hello Encriptado”; “Cliente Encriptado do Hello” mis-parses the protocol name as a client belonging to “Hello”.
- `monitor-no-breaches-description` — `browser/browser/protections.ftl` — Uses the explicit pronoun "Você", which the locale otherwise avoids.
    - Current: `Você não tem violações de dados conhecidas.`
    - Source: `You have no known breaches. If that changes, we will let you know.`
    - Suggest: `Não tem violações de dados conhecidas.`
    - Throughout this tree the third-person polite address is used with an implicit subject; "Você" is a Brazilian register marker and appears nowhere else in these files.
- `translations-manage-settings-button` — `browser/browser/translations.ftl` — Three full stops used instead of the ellipsis character used throughout the tree.
    - Current: `Definições...`
    - Source: `accesskey: t label: Settings…`
    - Suggest: `Definições…`
    - Every other truncated label in this partition uses "…"; the same deviation also occurs in translations-panel-translate-button-loading ("Por favor, aguarde...").
- `clear-startup-cache-label` — `toolkit/toolkit/about/aboutSupport.ftl` — Three dots preceded by a space instead of the ellipsis character.
    - Current: `Limpar cache de arranque ...`
    - Source: `Clear startup cache…`
    - Suggest: `Limpar cache de arranque…`
    - The rest of the file and tree use “…” with no preceding space (e.g. “Modo de diagnóstico…”).
- `third-party-loading-data` — `toolkit/toolkit/about/aboutThirdParty.ftl` — Three dots instead of the ellipsis character used everywhere else.
    - Current: `A carregar a informação do sistema...`
    - Source: `alt: Loading system information… title: Loading system information…`
    - Suggest: `A carregar a informação do sistema…`
    - en-US uses “…” and the rest of this file does too (e.g. “Abrir localização do ficheiro…”).
- `theme-picker-default-aria-label` — `toolkit/toolkit/global/theme-picker.ftl` — The default theme is named “Padrão” in the accessible label but “Predefinição” in the visible label.
    - Current: `Padrão`
    - Source: `aria-label: Default`
    - Suggest: `Predefinição`
    - The aria-label set is meant to mirror the visible labels of the same picker; screen-reader users hear a different theme name from the one shown.
- `webauthn-related-origin-create-header` — `toolkit/toolkit/webauthnDialog.ftl` — “passkey” is rendered as “chave-passe” here but “chave de acesso” in the other strings of the same dialog.
    - Current: `chave-passe`
    - Source: `{ $origin } wants to create a passkey for { $rpId }.`
    - Suggest: `chave de acesso`
    - webauthn-a-passkey-label, webauthn-another-passkey-label and webauthn-specific-passkey-label all use “chave de acesso”; two names for one object in one dialog.

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
