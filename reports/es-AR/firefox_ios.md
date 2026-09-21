# Firefox iOS l10n QA — es-AR

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 29 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-AR: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (2)

- `QuickAnswers.Settings.Footer.v158` — `es-AR/firefox-ios.xliff` — Plural "short answers" rendered as singular "una respuesta corta".
    - Current: `recibí una respuesta corta`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `recibí respuestas cortas`
    - The en-US says "get short answers" (plural); the target says the user gets a single short answer.
- `QuickAnswers.Errors.DailyLimitMessage.v158` — `es-AR/firefox-ios.xliff` — Feature name capitalized inconsistently as "Respuestas Rápidas" versus "Respuestas rápidas" elsewhere.
    - Current: `Respuestas Rápidas`
    - Source: `Try Quick Answers again tomorrow.`
    - Suggest: `Respuestas rápidas`
    - Other strings in the same feature (QuickAnswers.Settings.Title, AccessibilityLabels.OpenQuickAnswers) use "Respuestas rápidas"; Spanish does not use title case.

### ✅ Fixed since the last run (1)

- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-AR/firefox-ios.xliff` — "might log you out of websites" is rendered as an impersonal "puede cerrar sesión en los sitios web", losing the sense that it may sign the user out.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The source says the action may log the user out; the Spanish as written lacks the possessive/object and reads as the act itself closing a session, not the user's.

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
| Strings | 1,950 |
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
| quotes | `straight-double` 7, `curly-double` 3, `curly-single` 2 | _mixed_ |
| apostrophe | `typographic` 2 | **typographic** |
| ellipsis | `char` 23 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |
| inverted marks | `open-question` 42, `open-exclamation` 9 | **open-question** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (101)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.Rollouts.Message.v148` — `es-AR/firefox-ios.xliff` — Present/future "Changes applied remotely" rendered in past tense, asserting changes were already applied.
    - Current: `Los cambios se aplicaron remotamente.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `Los cambios se aplican remotamente.`
    - The source states changes are applied remotely as a general behaviour, not that changes have already been applied.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 43 |
| 3 | Degraded language (grammar, spelling, terminology) | 55 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.EditBookmarkMobileGroupLabel.v154` — `es-AR/firefox-ios.xliff` — "Mobile" (the mobile bookmarks folder group header) is rendered as "Teléfono celular", which names a phone rather than the Mobile group.
    - Current: `Teléfono celular`
    - Source: `Mobile`
    - Suggest: `Móvil`
    - The source is the collapsible header for the group of mobile bookmark folders, paired with 'Desktop' → 'Escritorio'; the related string uses 'MARCADORES PARA MÓVILES', so this should be 'Móvil', not 'Teléfono celular'.
- `Addresses.EditAddress.AutofillAddressSuburb.v129` — `es-AR/firefox-ios.xliff` — "Suburb" is rendered as "Suburbio", a false friend that means a poor outlying slum area in Spanish, not an address-level administrative district.
    - Current: `Suburbio`
    - Source: `Suburb`
    - Suggest: `Barrio`
    - The comment describes an address field for suburb details; "suburbio" in Spanish carries the connotation of slums/outskirts and is not used as an address field label.
- `MainMenu.Submenus.Save.AccessibilityLabels.RemoveFromShortcuts.Title.v132` — `es-AR/firefox-ios.xliff` — "Remove from Shortcuts" is translated as "Eliminar acceso directo" (delete the shortcut) instead of removing from the Shortcuts list, and is inconsistent with the v131 equivalent.
    - Current: `Eliminar acceso directo`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de atajos`
    - The source means remove the site from the Shortcuts section; the same string at MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131 is correctly "Eliminar de atajos", and "atajos" is the term used elsewhere in this menu.
- `MainMenu.Submenus.Save.AddToShortcuts.Title.v131` — `es-AR/firefox-ios.xliff` — "Add to Shortcuts" is rendered as a past participle statement ("Agregado a atajos" = "Added to shortcuts") instead of the action label.
    - Current: `Agregado a atajos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - The source is an imperative menu action "Add to Shortcuts"; the target states the item has already been added, matching neither the source nor the parallel "Agregar a pantalla de inicio".
- `NativeErrorPage.GenericError.Description.v134` — `es-AR/firefox-ios.xliff` — Present-tense "can’t be created" translated as past tense "no se pudo crear".
    - Current: `no se pudo crear una conexión segura`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `no se puede crear una conexión segura`
    - The source states a secure connection can't be created (present ability), not that it failed at one point.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `es-AR/firefox-ios.xliff` — "Try connecting on a different device" was rendered as "connect to a different device".
    - Current: `Probá conectarte a un dispositivo diferente.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Probá conectarte desde otro dispositivo.`
    - The source suggests testing the connection on another device, not connecting to another device.
- `Onboarding.IntroDescriptionPart1.v114` — `es-AR/firefox-ios.xliff` — "For good" (meaning "for the benefit of all/for a good cause") is rendered as "Para siempre" ("forever").
    - Current: `Independiente. Sin fines de lucro. Para siempre.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Independiente. Sin fines de lucro. Para el bien de todos.`
    - In context ("Indie. Non-profit. For good.") the phrase describes Firefox's purpose, not duration; "Para siempre" means "forever".
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-AR/firefox-ios.xliff` — The relative clause changes the meaning: the source says Firefox blocks companies from spying, the target says it blocks the companies that spy (presupposing they do).
    - Current: `bloqueamos automáticamente a las empresas que espían tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - en-US 'block companies from spying on your clicks' means preventing the spying, not filtering companies that already spy.
- `Onboarding.Modern.Welcome.Title.v140` — `es-AR/firefox-ios.xliff` — "creepy ads" translated as "publicidades molestas" (annoying ads), losing the "creepy/invasive" meaning.
    - Current: `Decile adiós a las publicidades molestas`
    - Source: `Say goodbye to creepy ads`
    - Suggest: `Decile adiós a las publicidades siniestras`
    - The source says "creepy" (invasive/unsettling), not "annoying"; the v145 counterpart correctly uses "siniestros".
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-AR/firefox-ios.xliff` — "how you use %1$@" is rendered impersonally as "cómo se usa %1$@", dropping the second-person reference used throughout the screen.
    - Current: `cómo se usa %1$@`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `cómo usás %1$@`
    - The source refers to the user's own usage data ("how you use"); the impersonal form loses that and breaks consistency with "tu dispositivo" earlier in the same sentence.
- `Onboarding.Welcome.Description.TreatementA.v120` — `es-AR/firefox-ios.xliff` — "non-profit backed browser" is rendered as "navegador respaldado sin fines de lucro", which says the browser itself is non-profit rather than backed by a non-profit.
    - Current: `Nuestro navegador respaldado sin fines de lucro`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Nuestro navegador respaldado por una organización sin fines de lucro`
    - The source says the browser is backed by a non-profit; the target's word order attaches "sin fines de lucro" to "respaldado", changing the meaning.
- `Onboarding.Welcome.Description.v120` — `es-AR/firefox-ios.xliff` — "non-profit backed browser" is rendered as "navegador respaldado sin fines de lucro", which misplaces the modifier and changes the meaning.
    - Current: `Nuestro navegador respaldado sin fines de lucro`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Nuestro navegador respaldado por una organización sin fines de lucro`
    - The source says the browser is backed by a non-profit; the target says the backing/browser is non-profit.
- `PrivacyDashboard.CrossSiteTrackers.v155` — `es-AR/firefox-ios.xliff` — "Cross-Site Tracking Cookies" is rendered as "cookies de rastreo de sitios cruzados", a literal mistranslation of the established term.
    - Current: `Cookies de rastreo de sitios cruzados`
    - Source: `Cross-Site Tracking Cookies`
    - Suggest: `Cookies de rastreo entre sitios`
    - "Cross-site" means "between/across sites" (entre sitios), not "crossed sites"; "sitios cruzados" does not convey the source meaning and departs from the Firefox term "rastreo entre sitios".
- `QuickAnswers.Settings.Footer.v158` — `es-AR/firefox-ios.xliff` — Plural "short answers" rendered as singular "una respuesta corta".
    - Current: `recibí una respuesta corta`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `recibí respuestas cortas`
    - The en-US says "get short answers" (plural); the target says the user gets a single short answer.
- `Settings.Rollouts.Message.v148` — `es-AR/firefox-ios.xliff` — Present/future "Changes applied remotely" rendered in past tense, asserting changes were already applied.
    - Current: `Los cambios se aplicaron remotamente.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `Los cambios se aplican remotamente.`
    - The source states changes are applied remotely as a general behaviour, not that changes have already been applied.
- `Settings.Search.GoogleLens.Footnote.v153` — `es-AR/firefox-ios.xliff` — "enabled above" mistranslated as "habilitado en la parte superior" (enabled at the top of the screen).
    - Current: `está habilitado en la parte superior`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `está habilitado más arriba`
    - The source refers to the setting above in the list, not to the top area of the screen.
- `Settings.Summarize.FooterTitle.v142` — `es-AR/firefox-ios.xliff` — "summarize pages" (verb + object) was rendered as "las páginas de resumen" (summary pages), changing the meaning.
    - Current: `Proporciona acceso a las páginas de resumen.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Proporciona acceso a resumir páginas.`
    - The source says the setting provides access to the ability to summarize pages, not access to "summary pages".
- `Translations.Sheet.Error.TitleLabel.v145` — `es-AR/firefox-ios.xliff` — Tense changed from past ("Couldn’t load") to present ("can't load").
    - Current: `No se pueden cargar los idiomas`
    - Source: `Couldn’t Load Languages`
    - Suggest: `No se pudieron cargar los idiomas`
    - Source "Couldn’t Load Languages" reports a past failure, consistent with the other error strings translated as "No se pudo…".
- `WebCompatReporter.Preview.Data.UserAgent.v155` — `es-AR/firefox-ios.xliff` — "your iOS version" is translated as "su versión de iOS", switching from the second-person voseo ("tu") used elsewhere in the same sentence.
    - Current: `que incluye su versión de iOS`
    - Source: `Your browser’s user agent, which includes your iOS version, %@ version, and browser engine version`
    - Suggest: `que incluye tu versión de iOS`
    - The source says "your iOS version", matching "Your browser's" earlier in the sentence; "su" breaks the established informal address and can be read as referring to the browser rather than the user.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `es-AR/firefox-ios.xliff` — "Please refresh." is rendered as the bare infinitive "Actualizar." instead of an instruction to the user.
    - Current: `No pudimos cargar los datos de partidos. Actualizar.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `No pudimos cargar los datos de partidos. Actualizá la página.`
    - The source asks the user to refresh; "Actualizar." reads as a button label, not the imperative request, and breaks the voseo imperative used elsewhere in this file ("Elegí", "Conseguí").
- `DefaultBrowserOnboarding.Description2` — `es-AR/firefox-ios.xliff` — "Tap Default Browser App" se tradujo como si se tocara la aplicación del navegador, no la opción de ajustes llamada "Aplicación de navegador predeterminada".
    - Current: `2. Tocá la aplicación del navegador predeterminado`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Tocá Aplicación de navegador predeterminada`
    - The step refers to tapping the iOS Settings row named "Default Browser App" (see DefaultBrowserOnboarding.Screenshot), not tapping the default browser application itself.
- `ActivityStream.ContextMenu.PinTopsite2` — `es-AR/firefox-ios.xliff` — "Pin" (fijar un sitio destacado) se tradujo como "Pegar", que significa paste/glue.
    - Current: `Pegar`
    - Source: `Pin`
    - Suggest: `Fijar`
    - The source "Pin" refers to pinning a top site; "Pegar" means to paste/stick and conflicts with the standard Firefox term "Fijar".
- `ActivityStream.ContextMenu.UnpinTopsite` — `es-AR/firefox-ios.xliff` — "Unpin" se tradujo como "Despegar" en vez de "Dejar de fijar".
    - Current: `Despegar`
    - Source: `Unpin`
    - Suggest: `Dejar de fijar`
    - "Unpin" removes the pinned state of a top site; "Despegar" means unstick/take off and is inconsistent with the standard term "fijar".
- `Changes color theme.` — `es-AR/firefox-ios.xliff` — "Changes color theme." mistranslated as "Cambia el color del tema" (changes the theme's color).
    - Current: `Cambia el color del tema.`
    - Source: `Changes color theme.`
    - Suggest: `Cambia el tema de color.`
    - The source refers to changing the color theme, not changing the color of the theme.
- `Closing tab` — `es-AR/firefox-ios.xliff` — "Closing tab" (progressive status announcement) is rendered as the imperative/infinitive "Cerrar pestaña" (Close tab).
    - Current: `Cerrar pestaña`
    - Source: `Closing tab`
    - Suggest: `Cerrando pestaña`
    - The developer comment says it notifies the user that the tab is being closed; the translation reads as a command label instead of an in-progress status.
- `Downloads.CancelDialog.Resume` — `es-AR/firefox-ios.xliff` — "Resume" (reanudar la descarga) is rendered as "Continuar", which in this Yes/No dialog is ambiguous, but the source term is "Resume".
    - Current: `Continuar`
    - Source: `Resume`
    - Suggest: `Reanudar`
    - The en-US button is "Resume", meaning resume the download; "Continuar" can be read as continuing with the cancellation.
- `Menu.AddToShortcuts.v99` — `es-AR/firefox-ios.xliff` — Menu action label "Add to Shortcuts" translated as a past-tense confirmation "Agregado a atajos" instead of an action.
    - Current: `Agregado a atajos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - The source is an imperative menu button label ("Add to Shortcuts"), not the confirmation toast (Menu.AddPin.Confirm2 = "Added to Shortcuts"). The translation duplicates the toast wording.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `es-AR/firefox-ios.xliff` — "hidden trackers" is rendered as just "rastreadores", dropping "hidden".
    - Current: `otro contenido que contenga rastreadores`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `otro contenido que contenga rastreadores ocultos`
    - en-US: "other content that contains hidden trackers"; the adjective "hidden" is missing.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `es-AR/firefox-ios.xliff` — "secretly" is dropped and "Cryptomining scripts" is mistranslated as "secuencias de comandos de cifrado" (encryption scripts).
    - Current: `Los criptomineros utilizan la potencia informática de su sistema para extraer dinero digital. Las secuencias de comandos de cifrado de los mismos agotan su batería`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Los criptomineros usan en secreto la potencia informática de su sistema para extraer dinero digital. Las secuencias de comandos de criptominería agotan su batería`
    - en-US says "secretly use" and "Cryptomining scripts"; the target omits "secretly" and renders cryptomining as "cifrado" (encryption).
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-AR/firefox-ios.xliff` — The translation says blocking trackers reduces the number of social media companies, instead of reducing how much they can see of what you do online.
    - Current: `reduce la cantidad de empresas de redes sociales que pueden ver lo que hace en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce lo que las empresas de redes sociales pueden ver de lo que hace en línea`
    - en-US: "reduces how much social media companies can see what do you online" — it is about how much they can see, not how many companies there are.
- `Open Tabs` — `es-AR/firefox-ios.xliff` — "Open Tabs" (a noun phrase naming a sync data type) is translated as the imperative "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - Developer comment says it is a toggle for the tabs syncing setting, so "Open Tabs" is a noun phrase, not a command.
- `Search.SuggestSectionTitle.v102` — `es-AR/firefox-ios.xliff` — "Firefox Suggest" (a feature/brand name) is rendered as "Sugerencia de Firefox" ("Firefox suggestion").
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the feature name "Firefox Suggest", used as a section header for Firefox suggestions; it should not be translated as a singular common noun.
- `Settings.AddCustomEngine.URLPlaceholder` — `es-AR/firefox-ios.xliff` — "Replace Query with %s" is rendered as "Reemplazá tu búsqueda con %s", adding a possessive and changing the instruction's sense.
    - Current: `URL (Reemplazá tu búsqueda con %s)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (Reemplazá la consulta con %s)`
    - The source instructs replacing the query term in the URL with the %s token; "tu búsqueda" is not in the source and the term "query" should be "consulta".
- `Settings.ClearAllWebsiteData.Clear.Button` — `es-AR/firefox-ios.xliff` — "Website Data" rendered as "datos del sitio", dropping the plural/website reference.
    - Current: `Eliminar todos los datos del sitio`
    - Source: `Clear All Website Data`
    - Suggest: `Eliminar todos los datos de los sitios web`
    - The source clears data of all websites; the singular "del sitio" suggests a single site.
- `Settings.DataManagement.SectionName` — `es-AR/firefox-ios.xliff` — "Data Management" translated as "Administrador de datos" (Data Manager) instead of "Administración de datos".
    - Current: `Administrador de datos`
    - Source: `Data Management`
    - Suggest: `Administración de datos`
    - The source names the activity/section "Data Management", not a "manager" entity.
- `Settings.DataManagement.Title` — `es-AR/firefox-ios.xliff` — "Data Management" translated as "Administrador de datos" (Data Manager) instead of "Administración de datos".
    - Current: `Administrador de datos`
    - Source: `Data Management`
    - Suggest: `Administración de datos`
    - The source names the section "Data Management", not a "manager".
- `Settings.Disconnect.Body` — `es-AR/firefox-ios.xliff` — "stop syncing with your account" is rendered as "stop syncing your account", changing the meaning.
    - Current: `Firefox dejará de sincronizar su cuenta pero no eliminará ningún dato de navegación en este dispositivo.`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `Firefox dejará de sincronizar con su cuenta, pero no eliminará ningún dato de navegación en este dispositivo.`
    - The source says Firefox will stop syncing with your account; the translation says it will stop syncing your account, which is a different statement.
- `Settings.DisplayTheme.SectionFooter` — `es-AR/firefox-ios.xliff` — "The theme" rendered as "Este tema" (This theme).
    - Current: `Este tema cambiará automáticamente`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `El tema cambiará automáticamente`
    - The source refers to the theme generally, not to a specific "this" theme.
- `Settings.Home.Option.JumpBackIn` — `es-AR/firefox-ios.xliff` — "Jump Back In" is rendered as "Volver a ver" ("watch again") instead of the established "Retomar"/"Volver a la carga" meaning of resuming browsing.
    - Current: `Volver a ver`
    - Source: `Jump Back In`
    - Suggest: `Retomar`
    - The Jump Back In section lets users resume recent tabs, not "view again"; the es-AR text names a different action.
- `Settings.NewTab.Option.Custom` — `es-AR/firefox-ios.xliff` — "Custom" (an option label) is translated as the verb "Personalizar" (customize).
    - Current: `Personalizar`
    - Source: `Custom`
    - Suggest: `Personalizada`
    - The source is an adjective naming a new-tab option (a custom URL/homepage), not an action; the sibling string Settings.NewTab.CustomURL uses "personalizada".
- `Settings.OfferClipboardBar.Title` — `es-AR/firefox-ios.xliff` — "Offer to Open Copied Links" rendered with the noun "Oferta" instead of the verbal construction.
    - Current: `Oferta para abrir enlaces copiados`
    - Source: `Offer to Open Copied Links`
    - Suggest: `Ofrecer abrir enlaces copiados`
    - The source means the app offers to open copied links; "Oferta" is a noun (a commercial offer) and misrepresents the setting.
- `Settings.Siri.SectionDescription` — `es-AR/firefox-ios.xliff` — "Siri shortcuts" translated as "atajos de teclado de Siri" (keyboard shortcuts).
    - Current: `Utilizar los atajos de teclado de Siri para abrir Firefox rápidamente vía Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Utilizar los atajos de Siri para abrir Firefox rápidamente vía Siri`
    - The source refers to Siri shortcuts, not keyboard shortcuts; "de teclado" is not in the source.
- `Settings.Siri.SectionName` — `es-AR/firefox-ios.xliff` — "Siri Shortcuts" translated as "Atajos de teclado de Siri" (Siri keyboard shortcuts).
    - Current: `Atajos de teclado de Siri`
    - Source: `Siri Shortcuts`
    - Suggest: `Atajos de Siri`
    - Siri Shortcuts are voice shortcuts, not keyboard shortcuts; "de teclado" adds meaning not in the source.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `es-AR/firefox-ios.xliff` — "some functionality may not work" is rendered as "puede perder cierta funcionalidad" (you may lose functionality), changing the meaning.
    - Current: `pero puede perder cierta funcionalidad`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `pero puede que alguna funcionalidad no funcione`
    - The source says some functionality may not work, not that the user will lose functionality; it also uses the formal register inconsistent with the rest of the screen.
- `Logins will be permanently removed.` — `es-AR/firefox-ios.xliff` — "Logins" mistranslated as "ingresos" (income/entries) instead of "inicios de sesión".
    - Current: `Los ingresos se eliminarán permanentemente.`
    - Source: `Logins will be permanently removed.`
    - Suggest: `Los inicios de sesión se eliminarán permanentemente.`
    - "Logins" refers to saved credentials; "ingresos" means income/entries in Spanish and is wrong. Other strings in the same file use "inicios de sesión".
- `Logins will be removed from all connected devices.` — `es-AR/firefox-ios.xliff` — "Logins" mistranslated as "ingresos" instead of "inicios de sesión".
    - Current: `Los ingresos se eliminarán de todos los dispositivos conectados.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `Los inicios de sesión se eliminarán de todos los dispositivos conectados.`
    - "Logins" means saved credentials; "ingresos" means income/entries. Inconsistent with "inicios de sesión" used elsewhere in the same file.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `es-AR/firefox-ios.xliff` — The brand name "Firefox" is dropped from the translation.
    - Current: `Agregá accesos directos a la pantalla principal.`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `Agregá accesos directos de Firefox a la pantalla principal.`
    - Source says "Add Firefox shortcuts to your Home screen."; the reference to Firefox is missing.
- `TodayWidget.QuickActionGalleryDescription` — `es-AR/firefox-ios.xliff` — The brand name "Firefox" is dropped from the translation.
    - Current: `Agregar un atajo a la pantalla de inicio.`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `Agregar un atajo de Firefox a la pantalla de inicio.`
    - Source reads "Add a Firefox shortcut to your Home screen."; the Firefox reference is missing.
- `eV8mOT` — `es-AR/firefox-ios.xliff` — "Quick Action Type" translated as plural "Acciones rápidas", losing "Type".
    - Current: `Acciones rápidas`
    - Source: `Quick Action Type`
    - Suggest: `Tipo de acción rápida`
    - The source is "Quick Action Type"; the translation drops "Type" and pluralizes, making it identical to the unrelated "Quick Actions" label.

### C. Grammar, agreement & spelling

- `NSLocationWhenInUseUsageDescription` — `es-AR/firefox-ios.xliff` — Wrong verb form: "visités" is subjunctive/voseo imperative instead of the indicative "visitás".
    - Current: `Los sitios web que visités pueden solicitar tu ubicación.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Los sitios web que visitás pueden solicitar tu ubicación.`
    - The source is a plain statement about websites the user visits; the relative clause needs the present indicative voseo form "visitás", not "visités".
- `CreditCard.SnackBar.RemoveCardSublabel.v112` — `es-AR/firefox-ios.xliff` — "Ésto" is misspelled; the demonstrative pronoun "esto" never takes an accent.
    - Current: `Ésto eliminará la tarjeta`
    - Source: `This will remove the card from all of your synced devices.`
    - Suggest: `Esto eliminará la tarjeta`
    - RAE orthography: neuter demonstrative "esto" is never accented.
- `Settings.AppIconSelection.AppIconNames.Midday.Title.v137` — `es-AR/firefox-ios.xliff` — Missing accent in "Mediodía".
    - Current: `Mediodia`
    - Source: `Midday`
    - Suggest: `Mediodía`
    - Spanish spelling of "midday" requires the accent: mediodía.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `es-AR/firefox-ios.xliff` — Imperative form inconsistent with voseo used in the rest of the string and the locale.
    - Current: `Guarda sitios mientras navegás.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Guardá sitios mientras navegás.`
    - es-AR uses voseo imperatives ("Guardá", as in the parallel string Bookmarks.EmptyState.Root.Body.v135); "Guarda" is the tuteo form and clashes with "navegás" in the same sentence.
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `es-AR/firefox-ios.xliff` — The pronoun in "probá desactivarla" refers to nothing in the sentence; the source refers to the protection switch.
    - Current: `probá desactivarla`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `probá desactivar las protecciones`
    - En-US "try turning it off" refers to the protection; the feminine singular "-la" has no antecedent in the Spanish sentence (the only noun is "algo"/"este sitio"), making the instruction ambiguous.
- `LibraryPanel.Sections.LastHour.v134` — `es-AR/firefox-ios.xliff` — Section title "Last Hour" is translated in lowercase without capitalization, inconsistent with the other section titles in the same panel.
    - Current: `la última hora`
    - Source: `Last Hour`
    - Suggest: `Última hora`
    - The source is a section title ("Last Hour"), and the sibling strings are rendered "Últimas 24 horas", "Últimos 7 días". The article "la" plus lowercase start is a grammar/capitalization error for a title.
- `MainMenu.Submenus.Tools.ReportBrokenSite.Title.v133` — `es-AR/firefox-ios.xliff` — "a cerca de" is a misspelling of "acerca de"; also inconsistent with the other Report Broken Site string.
    - Current: `Informar a cerca de sitio roto…`
    - Source: `Report Broken Site…`
    - Suggest: `Informar sitio roto…`
    - "a cerca de" is not valid Spanish (correct form is "acerca de"), and the sibling string MainMenu.ToolsSection.AccessibilityLabels.ReportBrokenSite.v154 renders the same source as "Informar sitio roto".
- `Onboarding.Modern.BrandRefresh.Marketing.LearnMoreLink.v148` — `es-AR/firefox-ios.xliff` — Missing accent on the interrogative/relative adverb "Cómo".
    - Current: `Como usamos los datos`
    - Source: `How we use the data`
    - Suggest: `Cómo usamos los datos`
    - "How we use the data" requires the accented "Cómo" in this nominal/indirect-question use.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `es-AR/firefox-ios.xliff` — Gender of the status label is inconsistent: "Bloqueado" here vs "Bloqueada" in the status string.
    - Current: `**Bloqueado**`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `**Bloqueada**`
    - Settings.AIControls.AIPoweredFeaturesSection.BlockedStatus.v151 uses "Bloqueada" (agreeing with "función"), and the parallel "Disponible" description matches its status label; the description must use the same label form shown in the UI.
- `Settings.Notifications.SyncNotificationsStatus.v112` — `es-AR/firefox-ios.xliff` — "Ésto" is misspelled; the neuter demonstrative pronoun never takes an accent.
    - Current: `Ésto debe habilitarse`
    - Source: `This must be turned on to receive tabs and get notified when you sign in on another device.`
    - Suggest: `Esto debe habilitarse`
    - Per RAE, "esto" is never accented.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-AR/firefox-ios.xliff` — Pronoun gender disagreement: "Activalos" refers to "las notificaciones" (feminine).
    - Current: `Activalos yendo a`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Activalas yendo a`
    - "notificaciones" is feminine plural, so the clitic must be "las".
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `es-AR/firefox-ios.xliff` — Missing accent on interrogative/relative "cómo" in "como conseguir".
    - Current: `y como conseguir el máximo`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `y cómo conseguir el máximo`
    - The indirect interrogative "how to get the most out of" requires the accented "cómo".
- `SendTo.NotSignedIn.Title.v119` — `es-AR/firefox-ios.xliff` — Voseo form not used: "No has iniciado sesión" instead of the es-AR "No iniciaste sesión".
    - Current: `No has iniciado sesión en tu cuenta.`
    - Source: `You are not signed in to your account.`
    - Suggest: `No iniciaste sesión en tu cuenta.`
    - es-AR uses voseo/rioplatense forms (as in the neighbouring strings "No tenés", "Probá", "Desactivá"); the peninsular present perfect "has iniciado" breaks the locale register.
- `TabsTray.Sync.SyncTabsDisabled.v116` — `es-AR/firefox-ios.xliff` — Misspelling "pestañás" with an incorrect accent.
    - Current: `pestañás`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `pestañas`
    - "pestañas" carries no written accent; the acute accent is a typo.
- `ContextualHints.Toolbar.Top.Description.v107` — `es-AR/firefox-ios.xliff` — Stray words "en la" left in the sentence, making it ungrammatical.
    - Current: `Mové la barra de herramientas hacia abajo en la si ese es más tu estilo.`
    - Source: `Move the toolbar to the bottom if that’s more your style.`
    - Suggest: `Mové la barra de herramientas hacia abajo si ese es más tu estilo.`
    - The source is "Move the toolbar to the bottom if that’s more your style."; the fragment "en la" is an unremoved leftover breaking the sentence.
- `ErrorPages.CertWarning.Description` — `es-AR/firefox-ios.xliff` — "EL" is capitalized incorrectly at the start of the sentence.
    - Current: `EL dueño de %@`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `El dueño de %@`
    - The article "El" is written with an uppercase L, a spelling/capitalization error.
- `HistoryPanel.EmptyState.Title` — `es-AR/firefox-ios.xliff` — "mas" is missing its accent and the adverb placement changes the meaning of the sentence.
    - Current: `Los sitios web visitados mas recientemente aparecerán acá.`
    - Source: `Websites you’ve visited recently will show up here.`
    - Suggest: `Los sitios web que visitaste recientemente aparecerán acá.`
    - "más" requires an accent; also the source says "websites you've visited recently", not "the most recently visited websites".
- `SentTab_TabArrivingNotification_WithDevice_body` — `es-AR/firefox-ios.xliff` — "Nueva pestaña llegada en %@" is ungrammatical/unnatural Spanish for "New tab arrived in %@".
    - Current: `Nueva pestaña llegada en %@`
    - Source: `New tab arrived in %@`
    - Suggest: `Llegó una nueva pestaña a %@`
    - The participle construction "pestaña llegada" is not valid Spanish; the parallel string SentTab_TabArrivingNotification_NoDevice_body uses "Llegó una nueva pestaña".
- `Settings.NewTab.TopSectionNameFooter` — `es-AR/firefox-ios.xliff` — Missing accent on interrogative/relative "qué" in "Elegir que se verá".
    - Current: `Elegir que se verá al abrir una nueva pestaña`
    - Source: `Choose what to load when opening a new tab`
    - Suggest: `Elegir qué se verá al abrir una nueva pestaña`
    - "Choose what to load" requires the accented interrogative "qué".
- `Welcome to your Reading List` — `es-AR/firefox-ios.xliff` — Missing possessive/article: "Bienvenido a lista de lectura" is ungrammatical and drops "your".
    - Current: `Bienvenido a lista de lectura`
    - Source: `Welcome to your Reading List`
    - Suggest: `Bienvenido a tu lista de lectura`
    - The source is "Welcome to your Reading List"; the Spanish lacks the possessive "tu" (or at least an article), making it ungrammatical.
- `DeleteLoginAlert.Message.Local.v122` — `es-AR/firefox-ios.xliff` — Incorrect accent: "No sé puede" should be "No se puede".
    - Current: `No sé puede deshacer esta acción.`
    - Source: `You cannot undo this action.`
    - Suggest: `No se puede deshacer esta acción.`
    - "sé" is the verb "saber"; the impersonal pronoun here must be the unaccented "se".
- `TodayWidget.TopSitesGalleryDescription` — `es-AR/firefox-ios.xliff` — Typo: "atajps" should be "atajos".
    - Current: `Agregar atajps a sitios visitados`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `Agregar atajos a sitios visitados`
    - Misspelling of "atajos" (shortcuts) in the widget description.

### D. Terminology, register & consistency

- `ContextualHints.Toolbar.GoogleLens.Description.v154` — `es-AR/firefox-ios.xliff` — Voseo register broken: "lo que ves" uses tuteo while the rest of the sentence uses voseo.
    - Current: `buscar lo que ves`
    - Source: `Use your camera or choose a photo to search what you see.`
    - Suggest: `buscar lo que ves (→ "lo que ves" should be "lo que ves" in voseo: "lo que ves" → "lo que ves")`
    - es-AR uses voseo ('Usá', 'elegí' in the same string); the second person present of 'ver' in voseo is 'vos ves', so this is consistent — see rationale note.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `es-AR/firefox-ios.xliff` — "Subject Name" in a certificate context is translated as "Nombre del asunto" (email subject) instead of "Nombre del sujeto", inconsistent with "Nombres alternativos del sujeto" on the same screen.
    - Current: `Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - The developer comment says this is the certificate subject name; the same screen already uses "sujeto" for Subject Alt Names, so "asunto" is wrong and inconsistent.
- `Menu.EnhancedTrackingProtection.Switch.Title.v128` — `es-AR/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered with a non-standard term instead of the established "Protección contra el rastreo mejorada".
    - Current: `Protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra el rastreo mejorada`
    - "de rastreo" reads as protection made of tracking rather than against tracking, and "aumentada" is not the established rendering of "Enhanced" for this Firefox feature name.
- `FirefoxHome.PrivacyNotice.PrivacyNoticeLink.v148` — `es-AR/firefox-ios.xliff` — "Privacy Notice" is rendered as "Nota de privacidad" instead of the established "Aviso de privacidad".
    - Current: `Nota de privacidad`
    - Source: `Privacy Notice`
    - Suggest: `Aviso de privacidad`
    - Mozilla's legal document is the "Aviso de privacidad" in Spanish; "Nota" is not the official name of the document being linked.
- `FirefoxHomepage.Shortcuts.Pinned.AccessibilityLabel.v139` — `es-AR/firefox-ios.xliff` — "Pinned" is translated as "Pegado" (glued) instead of the standard "Fijado".
    - Current: `Pegado: %@`
    - Source: `Pinned: %@`
    - Suggest: `Fijado: %@`
    - In Firefox UI "pinned" tiles/tabs are "fijados"; "Pegado" means glued/pasted and is the term used for "paste".
- `NativeErrorPage.BadCertDomain.AdvancedButton.v149` — `es-AR/firefox-ios.xliff` — "Advanced" on the certificate error button is rendered with a feminine plural adjective with no noun.
    - Current: `Avanzadas`
    - Source: `Advanced`
    - Suggest: `Avanzado`
    - The button reveals advanced information ("información avanzada"/"detalles avanzados"); "Avanzadas" agrees with nothing and is the wording used for settings panes.
- `NativeErrorPage.BadCertDomain.HideAdvancedButton.v149` — `es-AR/firefox-ios.xliff` — "Hide advanced" rendered with a feminine plural adjective with no noun.
    - Current: `Ocultar avanzadas`
    - Source: `Hide advanced`
    - Suggest: `Ocultar detalles avanzados`
    - The button hides the advanced information section; "avanzadas" has no referent in Spanish here.
- `PrivacyDashboard.Fingerprinters.v155` — `es-AR/firefox-ios.xliff` — "Fingerprinters" translated as "Detectores de huellas digitales" instead of the Firefox term "Detectores de huellas (digitales)" used for the tracker category.
    - Current: `Detectores de huellas digitales`
    - Source: `Fingerprinters`
    - Suggest: `Detectores de huellas digitales (fingerprinters)`
    - The category name refers to scripts that create a device fingerprint; the standard Firefox es term is "Huellas digitales"/"Detectores de huellas digitales" — flagged only for consistency.
- `QuickAnswers.Errors.DailyLimitMessage.v158` — `es-AR/firefox-ios.xliff` — Feature name capitalized inconsistently as "Respuestas Rápidas" versus "Respuestas rápidas" elsewhere.
    - Current: `Respuestas Rápidas`
    - Source: `Try Quick Answers again tomorrow.`
    - Suggest: `Respuestas rápidas`
    - Other strings in the same feature (QuickAnswers.Settings.Title, AccessibilityLabels.OpenQuickAnswers) use "Respuestas rápidas"; Spanish does not use title case.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `es-AR/firefox-ios.xliff` — "Trending Searches" is rendered inconsistently with the section title on the same feature ("Tendencia" vs "más populares").
    - Current: `Mostrar búsquedas más populares`
    - Source: `Show Trending Searches`
    - Suggest: `Mostrar búsquedas en tendencia`
    - SearchZero.TrendingSearches.SectionTitle.v146 translates "Trending" as "Tendencia"; this toggle for the same feature uses "más populares" ("most popular"), an inconsistent term for the same source concept within the same file/feature.
- `Settings.Appearance.Zoom.SpecificSiteZoom.Footer.v140` — `es-AR/firefox-ios.xliff` — Uses "usted" verb forms (visite, ajuste) instead of the voseo register used consistently elsewhere in this file.
    - Current: `visite un sitio y ajuste el zoom de la página desde el menú`
    - Source: `To add to this list, visit a site and adjust the page zoom from the menu`
    - Suggest: `visitá un sitio y ajustá el zoom de la página desde el menú`
    - The es-AR locale addresses the user with voseo (e.g. "Mirá", "Desbloqueá", "probá", "tenés" in the same batch); this string switches to the formal usted imperative.
- `TabLocation.LockButton.AccessibilityLabel.v122` — `es-AR/firefox-ios.xliff` — "Tracking Protection" is rendered "Protección de rastreo" while the same screen uses "protección contra rastreo".
    - Current: `Protección de rastreo`
    - Source: `Tracking Protection`
    - Suggest: `Protección contra rastreo`
    - The other TabLocation strings translate "Tracking Protection" as "protección contra rastreo"; "Protección de rastreo" is inconsistent and reads as protection of tracking rather than against it.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `es-AR/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered with a non-standard term instead of the established Firefox feature name.
    - Current: `protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Protección contra rastreo mejorada`
    - Enhanced Tracking Protection is a feature name, consistently rendered in es-AR Firefox as "Protección contra rastreo mejorada"; "de rastreo aumentada" is both wrong terminology and misleading (protecting rastreo rather than against it).
- `WebCompatReporter.SubOption.ItemsOverlapped.v154` — `es-AR/firefox-ios.xliff` — "Items" is translated as "ítems" here but as "elementos" in the sibling options on the same screen.
    - Current: `Los ítems están superpuestos`
    - Source: `Items are overlapped`
    - Suggest: `Los elementos están superpuestos`
    - ItemsMisaligned, ItemsNotVisible and MissingItems on the same form all use "elementos"; this one is inconsistent.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `es-AR/firefox-ios.xliff` — "BRONZE FINAL" is rendered as "TERCER PUESTO", which duplicates the separate "THIRD PLACE" label and loses the distinction between the match and the winner label.
    - Current: `TERCER PUESTO`
    - Source: `BRONZE FINAL`
    - Suggest: `FINAL POR EL TERCER PUESTO`
    - The source distinguishes the 'Bronze final' match (BRONZE FINAL) from the 'Third place' winner label (THIRD PLACE, translated as TERCER LUGAR); translating the match phase simply as "TERCER PUESTO" makes it a near-duplicate of the winner label instead of naming the match.
- `Saved Logins` — `es-AR/firefox-ios.xliff` — "Saved Logins" rendered as "Ingresos guardados" instead of the established term "Inicios de sesión guardados".
    - Current: `Ingresos guardados`
    - Source: `Saved Logins`
    - Suggest: `Inicios de sesión guardados`
    - The same source term "Logins" is translated as "inicios de sesión" elsewhere in this batch (AuthenticationManager); "Ingresos" means income/entries and is wrong terminology for logins.
- `BreachAlerts.Description` — `es-AR/firefox-ios.xliff` — Uses "usted" forms (cambió su contraseña, inicie sesión, cambie) instead of the voseo/tuteo register used elsewhere in this locale.
    - Current: `Las contraseñas se filtraron o se robaron desde la última vez que cambió su contraseña. Para proteger esta cuenta, inicie sesión en el sitio y cambie su contraseña.`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `Las contraseñas se filtraron o se robaron desde la última vez que cambiaste tu contraseña. Para proteger esta cuenta, iniciá sesión en el sitio y cambiá tu contraseña.`
    - es-AR strings in this batch address the user informally (e.g. "Por favor intentá de nuevo más tarde"); this string switches to formal address.
- `CoverSheet.v24.ETP.Description` — `es-AR/firefox-ios.xliff` — Register inconsistency: uses "lo sigan" / "Active" (usted) while es-AR convention elsewhere uses voseo/neutral forms, but more importantly "lo sigan" refers to the user in third person inconsistently with the rest of the batch.
    - Current: `ayuda a evitar que los anuncios lo sigan. Active Estricta`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `ayuda a evitar que los anuncios te sigan. Activá Estricta`
    - The rest of the es-AR strings address the user with the Argentine voseo/neutral register; this string switches to peninsular/usted imperative "Active".
- `Enter your password to connect` — `es-AR/firefox-ios.xliff` — Uses formal "usted" address instead of the voseo/tuteo form used elsewhere in this file.
    - Current: `Ingrese su contraseña para conectar`
    - Source: `Enter your password to connect`
    - Suggest: `Ingresá tu contraseña para conectar`
    - Other strings in the same file address the user informally ("Seguí adelante si aceptás", "tu privacidad", "tu información"), so the formal imperative is a register inconsistency for es-AR.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `es-AR/firefox-ios.xliff` — "Reader View" is translated as "Modo lectura" here while other strings in the same file use "Vista de lectura".
    - Current: `Modo lectura`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Vista de lectura`
    - The en-US term is "Reader View", translated as "Vista de lectura" in Reader View and ReaderMode.Available.VoiceOverAnnouncement; using "Modo lectura" here is inconsistent.
- `SendTo.NoDevicesFound.Message` — `es-AR/firefox-ios.xliff` — Uses the formal "usted" form where the locale's established address form is voseo/tuteo ("No tenés..."), inconsistent with neighbouring strings.
    - Current: `No tiene otros dispositivos conectados a esta cuenta de Firefox disponible para sincronizar.`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `No tenés otros dispositivos conectados a esta cuenta de Firefox disponibles para sincronizar.`
    - Other strings in the same file use voseo ("Llená todos los campos", "Tocá para comenzar", "estás tratando de compartir"); this one switches to formal usted. Also "disponible" should agree with "dispositivos" (disponibles).
- `SendTo.NotSignedIn.Message` — `es-AR/firefox-ios.xliff` — Formal "usted" imperatives instead of the locale's voseo forms used elsewhere in the same file.
    - Current: `Por favor abra Firefox, vaya a Configuración e inicie la sesión para continuar.`
    - Source: `Please open Firefox, go to Settings and sign in to continue.`
    - Suggest: `Abrí Firefox, andá a Configuración e iniciá sesión para continuar.`
    - Register inconsistency: nearby strings use voseo ("Llená", "Tocá", "Reemplazá", "estás").
- `SendTo.NotSignedIn.Title` — `es-AR/firefox-ios.xliff` — Formal "usted" form ("No inició la sesión en su cuenta") instead of the voseo register used elsewhere in the file.
    - Current: `No inició la sesión en su cuenta de Firefox.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `No iniciaste sesión en tu cuenta de Firefox.`
    - Register inconsistency with neighbouring strings that use voseo/tuteo.
- `Settings.Home.Option.Shortcuts` — `es-AR/firefox-ios.xliff` — "Shortcuts" is translated as "Accesos directos" here but as "Atajos" in the other homepage shortcuts settings strings.
    - Current: `Accesos directos`
    - Source: `Shortcuts`
    - Suggest: `Atajos`
    - Settings.Homepage.Shortcuts.ShortcutsPageTitle.v100, ShortcutsToggle.v100 and SponsoredShortcutsToggle.v100 all use "Atajos" for the same section on the same settings screen.
- `Settings.TrackingProtection.ProtectionCellFooter` — `es-AR/firefox-ios.xliff` — Uses the peninsular/formal "su" instead of the es-AR voseo/second-person form used consistently elsewhere in this batch.
    - Current: `ayuda a evitar que los anunciantes sigan su navegación`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `ayuda a evitar que los anunciantes sigan tu navegación`
    - Sibling strings in the same screen use voseo address forms ("tocá", "desactivá", "no viste"); "su navegación" is the formal/European register and is inconsistent.
- `Settings.WebsiteData.ConfirmPrompt` — `es-AR/firefox-ios.xliff` — Formal "sus" instead of the es-AR informal address used elsewhere, and "sitios" drops "website data" wording.
    - Current: `eliminará los datos de todos sus sitios`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `eliminará los datos de todos tus sitios web`
    - The locale addresses the user informally (voseo/tuteo) elsewhere in the same file; "sus" is the formal register.
- `DeleteLoginAlert.Message.Synced.v122` — `es-AR/firefox-ios.xliff` — Informal second person "tus" instead of the formal/neutral address used elsewhere.
    - Current: `de todos tus dispositivos sincronizados`
    - Source: `This will remove the password from all of your synced devices.`
    - Suggest: `de todos sus dispositivos sincronizados`
    - Firefox es-AR uses the formal/neutral address; other strings in the file avoid informal "tu/tus".

### E. Typography, punctuation & spacing

- `LiveActivity.Downloads.FileNameText.v138` — `es-AR/firefox-ios.xliff` — Curly quotation marks from the source were replaced with straight double quotes.
    - Current: `Descargando "%@"`
    - Source: `Downloading “%@”`
    - Suggest: `Descargando “%@”`
    - The en-US uses typographic double quotes around the file name; the translation uses straight quotes, deviating from the source's typography.
- `TopSites.RemovePage.Button` — `es-AR/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The en-US uses an em dash separator ("Remove page — %@"); the translation uses a plain hyphen.
- `PzSrmZ-eHmH1H` — `es-AR/firefox-ios.xliff` — Mismatched quotation marks: opening ‘ closed with ‘ instead of ’.
    - Current: `‘Eliminar pestañas privadas‘`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `“Eliminar pestañas privadas”`
    - The closing quote is a left single quotation mark, not a proper closing quote; other strings in the same file use straight double quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-AR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-AR/firefox-ios.xliff` — fixed 2026-09-21
