# Firefox iOS l10n QA — es-AR

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 1,918 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-AR: [android](android.md) · [firefox](firefox.md)

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
| Files | 96 |
| Strings | 1,918 |
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
| ellipsis | `char` 21 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |
| inverted marks | `open-question` 42, `open-exclamation` 9 | **open-question** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (85)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 36 |
| 3 | Degraded language (grammar, spelling, terminology) | 46 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.EditBookmarkMobileGroupLabel.v154` — `es-AR/firefox-ios.xliff` — "Mobile" (bookmark folder group name, paired with "Desktop") is rendered as "Teléfono celular".
    - Current: `Teléfono celular`
    - Source: `Mobile`
    - Suggest: `Móvil`
    - The source "Mobile" is the counterpart of "Desktop"/"Escritorio" and refers to the mobile bookmarks folder group, not to a cell phone device; the related header string uses "MARCADORES PARA MÓVILES".
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `es-AR/firefox-ios.xliff` — "Subject Name" in a certificate context is mistranslated as "Nombre del asunto" (email subject) instead of "Nombre del sujeto".
    - Current: `Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - In X.509 certificates, "Subject" is the certificate holder entity, rendered "sujeto" in Spanish; the sibling string SubjectAltNames already uses "sujeto", so "asunto" is both wrong and inconsistent within the same screen.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-AR/firefox-ios.xliff` — "might log you out of websites" is rendered as an impersonal "puede cerrar sesión en los sitios web", losing the meaning that the user will be logged out.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The source says the removal may log the user out; the translation omits the possessive/object making it ambiguous about whose session is closed.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `es-AR/firefox-ios.xliff` — "Tracking content" is translated as "Contenido de rastreo" but the developer comment says this line reports analytics trackers; more importantly the term should read as content that tracks.
    - Current: `Contenido de rastreo: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Contenido que rastrea: %@`
    - In Firefox the ETP category "Tracking content" is rendered as "Contenido que rastrea" in Spanish; "Contenido de rastreo" is inconsistent with the established product terminology.
- `MainMenu.Submenus.Save.AccessibilityLabels.RemoveFromShortcuts.Title.v132` — `es-AR/firefox-ios.xliff` — "Remove from Shortcuts" is translated as "Eliminar acceso directo" (delete the shortcut), losing the "from Shortcuts" sense.
    - Current: `Eliminar acceso directo`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de accesos directos`
    - The source means removing the site from the Shortcuts list; the target says "delete shortcut". The v131 counterpart correctly says "Eliminar de atajos".
- `MainMenu.Submenus.Save.AddToShortcuts.Title.v131` — `es-AR/firefox-ios.xliff` — "Add to Shortcuts" is rendered as a past participle "Agregado a atajos" (added), not as the action.
    - Current: `Agregado a atajos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - The source is an imperative menu action "Add to Shortcuts"; the target states "Added to shortcuts", changing the meaning. The parallel accessibility label uses "Agregar a accesos directos".
- `NativeErrorPage.NoInternetConnection.Description.v131` — `es-AR/firefox-ios.xliff` — "Try connecting on a different device" was rendered as "conectarte a un dispositivo diferente" (connect to a different device).
    - Current: `Probá conectarte a un dispositivo diferente.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Probá conectarte desde otro dispositivo.`
    - The source tells the user to try connecting from another device; "conectarte a un dispositivo" means connecting to a device, which is a different instruction.
- `Onboarding.IntroDescriptionPart1.v114` — `es-AR/firefox-ios.xliff` — "For good" (for the common good) is mistranslated as "Para siempre" (forever).
    - Current: `Para siempre.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Para el bien común.`
    - In the source, "Indie. Non-profit. For good." describes Firefox as being for the public good, not something permanent.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-AR/firefox-ios.xliff` — The relative clause changes the meaning: the source says Firefox blocks companies from spying, not that it blocks companies that spy.
    - Current: `bloqueamos automáticamente a las empresas que espían tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - en-US: "automatically block companies from spying on your clicks" — the blocking is of the spying action, not a filter of companies that already spy.
- `Onboarding.Modern.Welcome.Title.v140` — `es-AR/firefox-ios.xliff` — "creepy ads" translated as "publicidades molestas" (annoying ads), losing the intrusive/creepy meaning.
    - Current: `las publicidades molestas`
    - Source: `Say goodbye to creepy ads`
    - Suggest: `las publicidades invasivas`
    - "Creepy" refers to invasive/tracking ads, not merely annoying ones.
- `Settings.Rollouts.Message.v148` — `es-AR/firefox-ios.xliff` — Present/future "Changes applied remotely" rendered in past tense.
    - Current: `Los cambios se aplicaron remotamente.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `Los cambios se aplican remotamente.`
    - The source states that changes are applied remotely (general statement), not that they were already applied.
- `Settings.Summarize.FooterTitle.v142` — `es-AR/firefox-ios.xliff` — "summarize pages" (verb + object) was rendered as "páginas de resumen" (summary pages), changing the meaning.
    - Current: `Proporciona acceso a las páginas de resumen.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Proporciona acceso a la función de resumir páginas.`
    - The source says the setting provides access to summarizing pages, not to "summary pages"; the related toggle title is translated as "Resumir páginas".
- `Translations.Sheet.Error.TitleLabel.v145` — `es-AR/firefox-ios.xliff` — Past-tense failure rendered as present tense inconsistently with the other error strings.
    - Current: `No se pueden cargar los idiomas`
    - Source: `Couldn’t Load Languages`
    - Suggest: `No se pudieron cargar los idiomas`
    - Source "Couldn’t Load Languages" is a past failure, like the sibling "Couldn’t Translate Page" translated as "No se pudo traducir la página".
- `WebCompatReporter.Preview.Data.UserAgent.v155` — `es-AR/firefox-ios.xliff` — "your iOS version" is rendered as "su versión de iOS", switching from second person to third person and losing the possessive reference to the user.
    - Current: `que incluye su versión de iOS`
    - Source: `Your browser’s user agent, which includes your iOS version, %@ version, and browser engine version`
    - Suggest: `que incluye tu versión de iOS`
    - The source says "your iOS version"; the rest of the string uses the informal second person ("tu navegador"), so "su" is both inconsistent and ambiguous.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `es-AR/firefox-ios.xliff` — "Please refresh." is rendered as the infinitive "Actualizar." instead of an imperative request to the user.
    - Current: `No pudimos cargar los datos de partidos. Actualizar.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `No pudimos cargar los datos de partidos. Actualizá la página.`
    - The source is an instruction addressed to the user; the rest of the file uses the voseo imperative (Elegí, Conseguí, Mantenete). "Actualizar." reads as a button label, not a request.
- `DefaultBrowserOnboarding.Description2` — `es-AR/firefox-ios.xliff` — "Tap Default Browser App" refers to tapping the iOS setting named "Default Browser App", but the translation reads as "tap the default browser's application".
    - Current: `2. Tocá la aplicación del navegador predeterminado`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Tocá «Aplicación de navegador predeterminada»`
    - The string names the iOS Settings row (see DefaultBrowserOnboarding.Screenshot); the current wording changes the meaning to the app of the default browser.
- `ActivityStream.ContextMenu.PinTopsite2` — `es-AR/firefox-ios.xliff` — "Pin" (fijar un sitio destacado) se tradujo como "Pegar", que significa "paste/glue".
    - Current: `Pegar`
    - Source: `Pin`
    - Suggest: `Fijar`
    - El comentario indica que es la acción de fijar (pin) un sitio destacado; "Pegar" se entiende como pegar/paste y no transmite la acción.
- `ActivityStream.ContextMenu.UnpinTopsite` — `es-AR/firefox-ios.xliff` — "Unpin" se tradujo como "Despegar" en vez de "Dejar de fijar".
    - Current: `Despegar`
    - Source: `Unpin`
    - Suggest: `Dejar de fijar`
    - Es la acción inversa de fijar un sitio destacado; "Despegar" corresponde a unstick/take off, no a unpin.
- `Closing tab` — `es-AR/firefox-ios.xliff` — Progressive "Closing tab" rendered as the imperative/infinitive "Cerrar pestaña" (Close tab).
    - Current: `Cerrar pestaña`
    - Source: `Closing tab`
    - Suggest: `Cerrando pestaña`
    - The developer comment says this notifies the user that the tab is being closed; the translation reads as a command "Close tab" instead.
- `Menu.AddToShortcuts.v99` — `es-AR/firefox-ios.xliff` — Menu action "Add to Shortcuts" is translated as a past-tense confirmation "Agregado a atajos" instead of an action label.
    - Current: `Agregado a atajos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - The developer comment says this is a button label to pin the current site; en-US is the imperative "Add to Shortcuts", not the confirmation toast "Added to Shortcuts" (Menu.AddPin.Confirm2).
- `Menu.TrackingProtectionDescription.ContentTrackers` — `es-AR/firefox-ios.xliff` — "hidden trackers" is translated as just "rastreadores", dropping "hidden".
    - Current: `otro contenido que contenga rastreadores`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `otro contenido que contenga rastreadores ocultos`
    - en-US: "other content that contains hidden trackers"; the qualifier "hidden" is missing.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `es-AR/firefox-ios.xliff` — "secretly" is dropped and "Cryptomining scripts" is mistranslated as "secuencias de comandos de cifrado" (encryption scripts).
    - Current: `Los criptomineros utilizan la potencia informática de su sistema para extraer dinero digital. Las secuencias de comandos de cifrado de los mismos agotan`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Los criptomineros utilizan en secreto la potencia informática de su sistema para extraer dinero digital. Los scripts de criptominería agotan`
    - en-US says "secretly use" and "Cryptomining scripts"; the translation omits "secretly" and renders cryptomining as "cifrado" (encryption).
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-AR/firefox-ios.xliff` — The translation says blocking trackers reduces the number of social media companies, instead of reducing how much they can see of what you do online.
    - Current: `reduce la cantidad de empresas de redes sociales que pueden ver lo que hace en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce cuánto pueden ver las empresas de redes sociales lo que hace en línea`
    - en-US: "reduces how much social media companies can see what do you online" — the quantity refers to what they can see, not to the number of companies.
- `Open Tabs` — `es-AR/firefox-ios.xliff` — "Open Tabs" is a sync setting label (noun phrase), but was translated as the imperative verb "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - The developer comment says "Toggle tabs syncing setting", so "Open Tabs" is the category of synced data (open tabs), not an action to open tabs.
- `Search.SuggestSectionTitle.v102` — `es-AR/firefox-ios.xliff` — "Firefox Suggest" is a feature/brand name and has been translated as "Sugerencia de Firefox".
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the Firefox Suggest feature name used as a section header; translating it as "Sugerencia de Firefox" (singular "suggestion of Firefox") changes the brand/feature name.
- `Settings.ClearAllWebsiteData.Clear.Button` — `es-AR/firefox-ios.xliff` — Plural "Website Data" rendered as singular "del sitio", dropping "sitios web".
    - Current: `Eliminar todos los datos del sitio`
    - Source: `Clear All Website Data`
    - Suggest: `Eliminar todos los datos de los sitios web`
    - The source clears data for all websites, not a single site; "del sitio" narrows the meaning.
- `Settings.NewTab.Option.Custom` — `es-AR/firefox-ios.xliff` — "Custom" (an option label, adjective) is translated as the verb "Personalizar" (to customize).
    - Current: `Personalizar`
    - Source: `Custom`
    - Suggest: `Personalizada`
    - The source is the option name "Custom" describing a custom URL option (cf. Settings.NewTab.CustomURL = "URL personalizada"), not the action "Customize".
- `Settings.OfferClipboardBar.Title` — `es-AR/firefox-ios.xliff` — "Offer to Open Copied Links" is rendered with the noun "Oferta" instead of the verbal sense "offer to".
    - Current: `Oferta para abrir enlaces copiados`
    - Source: `Offer to Open Copied Links`
    - Suggest: `Ofrecer abrir enlaces copiados`
    - In English "Offer to Open" means the app offers/proposes to open copied links; "Oferta" (a commercial offer/sale) mistranslates the meaning.
- `Settings.Siri.SectionDescription` — `es-AR/firefox-ios.xliff` — "Siri shortcuts" is rendered as "atajos de teclado de Siri" (keyboard shortcuts), which is a different feature.
    - Current: `Utilizar los atajos de teclado de Siri para abrir Firefox rápidamente vía Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Usar los atajos de Siri para abrir Firefox rápidamente vía Siri`
    - The source says "Siri shortcuts"; "atajos de teclado" means keyboard shortcuts, which is not what Siri Shortcuts are.
- `Settings.Siri.SectionName` — `es-AR/firefox-ios.xliff` — "Siri Shortcuts" translated as "Atajos de teclado de Siri" (Siri keyboard shortcuts).
    - Current: `Atajos de teclado de Siri`
    - Source: `Siri Shortcuts`
    - Suggest: `Atajos de Siri`
    - The source refers to the Siri Shortcuts feature, not keyboard shortcuts.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `es-AR/firefox-ios.xliff` — "some functionality may not work" is mistranslated as "puede perder cierta funcionalidad" (you may lose some functionality).
    - Current: `pero puede perder cierta funcionalidad`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `pero es posible que algunas funciones no anden`
    - The source says some functionality may not work, not that the user will lose functionality; it also uses formal address implicitly.
- `Logins will be permanently removed.` — `es-AR/firefox-ios.xliff` — "Logins" is mistranslated as "ingresos" (income/entries) instead of "inicios de sesión".
    - Current: `Los ingresos se eliminarán permanentemente.`
    - Source: `Logins will be permanently removed.`
    - Suggest: `Los inicios de sesión se eliminarán permanentemente.`
    - "Logins" refers to saved credentials; elsewhere in the same file it is rendered "inicios de sesión". "Ingresos" means income/revenue and is wrong.
- `Logins will be removed from all connected devices.` — `es-AR/firefox-ios.xliff` — "Logins" is mistranslated as "ingresos" (income) instead of "inicios de sesión".
    - Current: `Los ingresos se eliminarán de todos los dispositivos conectados.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `Los inicios de sesión se eliminarán de todos los dispositivos conectados.`
    - "Logins" means saved credentials, translated as "inicios de sesión" elsewhere in this file; "ingresos" means income and is incorrect.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `es-AR/firefox-ios.xliff` — The brand name "Firefox" is dropped from the widget description.
    - Current: `Agregá accesos directos a la pantalla principal.`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `Agregá accesos directos de Firefox a la pantalla principal.`
    - The en-US source reads "Add Firefox shortcuts to your Home screen." — the product name Firefox is omitted in the translation, losing content.
- `TodayWidget.QuickActionGalleryDescription` — `es-AR/firefox-ios.xliff` — "Firefox" dropped from "Add a Firefox shortcut".
    - Current: `Agregar un atajo a la pantalla de inicio.`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `Agregar un atajo de Firefox a la pantalla de inicio.`
    - The source specifies a Firefox shortcut; the brand name is omitted in the translation.
- `eV8mOT` — `es-AR/firefox-ios.xliff` — "Quick Action Type" translated as plural "Acciones rápidas", losing "Type".
    - Current: `Acciones rápidas`
    - Source: `Quick Action Type`
    - Suggest: `Tipo de acción rápida`
    - The source is "Quick Action Type"; the translation drops "Type" and pluralizes, making it identical to the unrelated "Quick Actions" label.

### C. Grammar, agreement & spelling

- `CreditCard.SnackBar.RemoveCardSublabel.v112` — `es-AR/firefox-ios.xliff` — "Ésto" is misspelled; the demonstrative pronoun "esto" never takes an accent.
    - Current: `Ésto eliminará la tarjeta`
    - Source: `This will remove the card from all of your synced devices.`
    - Suggest: `Esto eliminará la tarjeta`
    - Per RAE orthography, the neuter demonstrative "esto" is never accented.
- `Settings.AppIconSelection.AppIconNames.Midday.Title.v137` — `es-AR/firefox-ios.xliff` — Missing accent in "Mediodía".
    - Current: `Mediodia`
    - Source: `Midday`
    - Suggest: `Mediodía`
    - The Spanish word for midday is "mediodía", with an accent on the í.
- `Settings.AppIconSelection.ScreenTitle.v136` — `es-AR/firefox-ios.xliff` — "Icono" lacks the accent used elsewhere in the same screen ("ícono").
    - Current: `Icono de la aplicación`
    - Source: `App Icon`
    - Suggest: `Ícono de la aplicación`
    - Other strings in the same file use "ícono" (e.g. "Seleccionar el ícono de la aplicación %@", "el ícono de tu aplicación"); es-AR prefers the accented form, so this is inconsistent within the screen.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `es-AR/firefox-ios.xliff` — Inconsistent verb form: "Guarda" is tuteo imperative while the rest of the string (and the parallel string) uses voseo "Guardá".
    - Current: `Guarda sitios mientras navegás.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Guardá sitios mientras navegás.`
    - es-AR uses voseo imperatives; the parallel string Bookmarks.EmptyState.Root.Body.v135 uses "Guardá", and this string mixes "Guarda" with "navegás"/"Iniciá".
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `es-AR/firefox-ios.xliff` — Pronoun gender mismatch: "desactivarla" refers to the protection switch but the antecedent in the string is unclear/feminine while the surrounding UI uses masculine "Estándar/Estricto"; the source refers to the protection feature.
    - Current: `probá desactivarla`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `probá desactivarlo`
    - The "it" in the source refers to Enhanced Tracking Protection toggle; as written the feminine pronoun disagrees with the referent used on the same screen.
- `LibraryPanel.Sections.LastHour.v134` — `es-AR/firefox-ios.xliff` — Section title is lowercase and includes an article, unlike the other section titles.
    - Current: `la última hora`
    - Source: `Last Hour`
    - Suggest: `Última hora`
    - "Last Hour" is a section title; sibling sections use capitalized noun phrases ("Últimas 24 horas", "Últimos 7 días"). The lowercase article-led "la última hora" is inconsistent and grammatically odd as a title.
- `MainMenu.Submenus.Tools.ReportBrokenSite.Title.v133` — `es-AR/firefox-ios.xliff` — "a cerca de" is a misspelling of "acerca de".
    - Current: `Informar a cerca de sitio roto…`
    - Source: `Report Broken Site…`
    - Suggest: `Informar sitio roto…`
    - "a cerca de" is not valid Spanish; the correct form is "acerca de" (and the parallel accessibility label uses "Informar sitio roto", so consistency favors that wording).
- `NativeErrorPage.GenericError.Description.v134` — `es-AR/firefox-ios.xliff` — Present-tense "can’t be created" translated as past tense "no se pudo crear".
    - Current: `no se pudo crear una conexión segura`
    - Source: `The owner of %@ hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `no se puede crear una conexión segura`
    - The source states a present inability ("a secure connection can’t be created"), not a past event.
- `Onboarding.Modern.BrandRefresh.Marketing.LearnMoreLink.v148` — `es-AR/firefox-ios.xliff` — Missing accent on the interrogative-relative adverb "Cómo" in "Como usamos los datos".
    - Current: `Como usamos los datos`
    - Source: `How we use the data`
    - Suggest: `Cómo usamos los datos`
    - "How we use the data" is an indirect interrogative; Spanish requires the accented "cómo".
- `Onboarding.Modern.Welcome.Title.v145` — `es-AR/firefox-ios.xliff` — "Decile" is the wrong voseo imperative for "decir adiós"; it should be "Decí".
    - Current: `Decile adiós a los rastreadores siniestros`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `Decí adiós a los rastreadores siniestros`
    - "Decile" means "say to him/her" (with indirect object clitic), which adds an unintended recipient; the source is simply "Say goodbye to creepy trackers".
- `Onboarding.Sync.Title.v120` — `es-AR/firefox-ios.xliff` — "cambiés" uses a non-standard accented voseo subjunctive; correct form is "cambies".
    - Current: `cuando cambiés entre dispositivos`
    - Source: `Stay encrypted when you hop between devices`
    - Suggest: `cuando cambies entre dispositivos`
    - The standard subjunctive form after "cuando" is "cambies"; "cambiés" is a nonstandard voseo spelling not used in written Argentine Spanish.
- `Onboarding.Welcome.Description.TreatementA.v120` — `es-AR/firefox-ios.xliff` — Word order makes "respaldado sin fines de lucro" nonsensical; the source says the browser is backed by a non-profit.
    - Current: `Nuestro navegador respaldado sin fines de lucro`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Nuestro navegador respaldado por una organización sin fines de lucro`
    - "non-profit backed browser" means backed by a non-profit organization; the current wording attaches "sin fines de lucro" to "respaldado", which is ungrammatical/meaningless.
- `Onboarding.Welcome.Description.v120` — `es-AR/firefox-ios.xliff` — Word order makes "respaldado sin fines de lucro" nonsensical; the source says the browser is backed by a non-profit.
    - Current: `Nuestro navegador respaldado sin fines de lucro`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Nuestro navegador respaldado por una organización sin fines de lucro`
    - "non-profit backed browser" means backed by a non-profit organization; the current wording attaches "sin fines de lucro" to "respaldado", which is ungrammatical/meaningless.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `es-AR/firefox-ios.xliff` — Gender of the status label is inconsistent with the sibling string "Bloqueada" for the same status.
    - Current: `**Bloqueado**`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `**Bloqueada**`
    - Settings.AIControls.AIPoweredFeaturesSection.BlockedStatus.v151 translates the same status "Blocked" as "Bloqueada" (referring to la función); the description uses the masculine form for the same label on the same screen.
- `Settings.Notifications.SyncNotificationsStatus.v112` — `es-AR/firefox-ios.xliff` — "Ésto" is misspelled; the neuter demonstrative pronoun never takes an accent.
    - Current: `Ésto debe habilitarse`
    - Source: `This must be turned on to receive tabs and get notified when you sign in on another device.`
    - Suggest: `Esto debe habilitarse`
    - RAE: "esto" is never written with an accent.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-AR/firefox-ios.xliff` — Pronoun gender/number disagreement: "Activalos" refers to "las notificaciones".
    - Current: `Activalos yendo a`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Activalas yendo a`
    - The antecedent is "las notificaciones" (feminine), so the clitic must be "las".
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `es-AR/firefox-ios.xliff` — Missing accent on interrogative-like "cómo" in "y como conseguir".
    - Current: `y como conseguir el máximo`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `y cómo sacarle el máximo provecho`
    - "how to get the most out of" requires the accented "cómo" as an indirect interrogative.
- `TabsTray.Sync.SyncTabsDisabled.v116` — `es-AR/firefox-ios.xliff` — Misspelling: "pestañás" has an incorrect accent.
    - Current: `pestañás`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `pestañas`
    - "pestañas" carries no written accent; the acute accent on the final 'a' is a typo.
- `ContextualHints.Toolbar.Top.Description.v107` — `es-AR/firefox-ios.xliff` — Stray words "en la" left in the sentence make it ungrammatical.
    - Current: `Mové la barra de herramientas hacia abajo en la si ese es más tu estilo.`
    - Source: `Move the toolbar to the bottom if that’s more your style.`
    - Suggest: `Mové la barra de herramientas hacia abajo si ese es más tu estilo.`
    - The source is "Move the toolbar to the bottom if that’s more your style."; the extra "en la" is a leftover fragment that breaks the sentence.
- `ErrorPages.CertWarning.Description` — `es-AR/firefox-ios.xliff` — "EL" is misspelled with a capital L at the start of the sentence.
    - Current: `EL dueño de %@`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `El dueño de %@`
    - Spelling/capitalization error: the Spanish article should be "El", not "EL".
- `HistoryPanel.EmptyState.Title` — `es-AR/firefox-ios.xliff` — "mas" is missing its accent (should be "más") and the phrase misrenders "visited recently".
    - Current: `Los sitios web visitados mas recientemente aparecerán acá.`
    - Source: `Websites you’ve visited recently will show up here.`
    - Suggest: `Los sitios web que visitaste recientemente aparecerán acá.`
    - The comparative/adverb "más" requires an accent; also the source says "websites you've visited recently", not "most recently visited".
- `SentTab_TabArrivingNotification_WithDevice_body` — `es-AR/firefox-ios.xliff` — Ungrammatical rendering "Nueva pestaña llegada en %@".
    - Current: `Nueva pestaña llegada en %@`
    - Source: `New tab arrived in %@`
    - Suggest: `Llegó una nueva pestaña a %@`
    - "pestaña llegada" is not grammatical Spanish; the source means a new tab arrived in the named app/device.
- `Settings.NewTab.TopSectionNameFooter` — `es-AR/firefox-ios.xliff` — Missing accent on the interrogative/relative "qué".
    - Current: `Elegir que se verá al abrir una nueva pestaña`
    - Source: `Choose what to load when opening a new tab`
    - Suggest: `Elegir qué se verá al abrir una nueva pestaña`
    - "Choose what to load" requires the accented interrogative "qué" in Spanish.
- `Welcome to your Reading List` — `es-AR/firefox-ios.xliff` — Missing possessive/article makes the phrase ungrammatical.
    - Current: `Bienvenido a lista de lectura`
    - Source: `Welcome to your Reading List`
    - Suggest: `Bienvenido a tu lista de lectura`
    - The en-US says "your Reading List"; the Spanish drops both the possessive and the article, which is ungrammatical.
- `DeleteLoginAlert.Message.Local.v122` — `es-AR/firefox-ios.xliff` — "No sé puede" has an incorrect accent on the impersonal pronoun "se".
    - Current: `No sé puede deshacer esta acción.`
    - Source: `You cannot undo this action.`
    - Suggest: `No se puede deshacer esta acción.`
    - The impersonal reflexive pronoun is "se" (unaccented); "sé" is the verb form of saber, producing an ungrammatical sentence.
- `TodayWidget.TopSitesGalleryDescription` — `es-AR/firefox-ios.xliff` — Typo: "atajps" should be "atajos".
    - Current: `Agregar atajps a sitios visitados`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `Agregar atajos a sitios visitados`
    - "atajps" is a misspelling of "atajos" (shortcuts).

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Switch.Title.v128` — `es-AR/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered as "Protección de rastreo aumentada" instead of the established Firefox term.
    - Current: `Protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra el rastreo mejorada`
    - "Protección de rastreo" reverses the sense (protection of tracking rather than against tracking), and the established Firefox term is "Protección contra el rastreo mejorada".
- `FirefoxHomepage.Shortcuts.Pinned.AccessibilityLabel.v139` — `es-AR/firefox-ios.xliff` — "Pinned" is rendered as "Pegado" (glued) instead of the standard "Anclado".
    - Current: `Pegado: %@`
    - Source: `Pinned: %@`
    - Suggest: `Anclado: %@`
    - Firefox uses "anclado/fijado" for pinned items; "Pegado" means glued/pasted and misstates the state of the tile.
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToShortcuts.Subtitle.v132` — `es-AR/firefox-ios.xliff` — "Shortcut" is translated as "Acceso directo" here but as "Atajo" in the equivalent v131 strings on the same menu.
    - Current: `Acceso directo`
    - Source: `Shortcut`
    - Suggest: `Atajo`
    - The Save submenu uses "atajos" for Shortcuts (AddToShortcuts.Subtitle.v131, RemoveFromShortcuts.Title.v131); the accessibility labels use "accesos directos", an inconsistent term for the same UI item.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `es-AR/firefox-ios.xliff` — "Manage settings" is rendered as "Administrar preferencias" (preferences) instead of "configuración"/"ajustes".
    - Current: `Administrar preferencias`
    - Source: `Manage settings`
    - Suggest: `Administrar configuración`
    - The source says "settings", not "preferences"; Firefox iOS uses "Configuración" for Settings in es-AR.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `es-AR/firefox-ios.xliff` — "Trending Searches" is rendered inconsistently with the related section title, which uses "Tendencia".
    - Current: `Mostrar búsquedas más populares`
    - Source: `Show Trending Searches`
    - Suggest: `Mostrar búsquedas en tendencia`
    - The same feature is called "Tendencia en %@" in SearchZero.TrendingSearches.SectionTitle.v146; "búsquedas más populares" (most popular searches) uses different terminology for the same source term on a related settings screen.
- `Settings.Appearance.Zoom.SpecificSiteZoom.Footer.v140` — `es-AR/firefox-ios.xliff` — Uses "usted" forms (visite, ajuste) while the rest of the batch consistently uses the voseo/tuteo register (probá, verás, agregá).
    - Current: `Para agregar a esta lista, visite un sitio y ajuste el zoom de la página desde el menú`
    - Source: `To add to this list, visit a site and adjust the page zoom from the menu`
    - Suggest: `Para agregar a esta lista, visitá un sitio y ajustá el zoom de la página desde el menú`
    - es-AR strings in this same file address the user informally ("Mirá", "probá", "Desbloqueá", "Verás"); this string switches to the formal usted register.
- `SendTo.NotSignedIn.Title.v119` — `es-AR/firefox-ios.xliff` — Uses peninsular "has iniciado" instead of the voseo form used throughout the es-AR locale.
    - Current: `No has iniciado sesión en tu cuenta.`
    - Source: `You are not signed in to your account.`
    - Suggest: `No iniciaste sesión en tu cuenta.`
    - es-AR uses voseo (e.g. "No tenés ningún otro dispositivo…" in the same file); "has iniciado" is inconsistent with the locale's established form of address.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `es-AR/firefox-ios.xliff` — "Enhanced Tracking Protection" is a Firefox feature name rendered incorrectly as "protección de rastreo aumentada".
    - Current: `Configuración de protección de rastreo aumentada para este sitio`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Configuración de la protección antirrastreo mejorada para este sitio`
    - The established Spanish term for the Firefox feature "Enhanced Tracking Protection" is "Protección antirrastreo mejorada"; "aumentada" is not the product terminology.
- `WebCompatReporter.SubOption.ItemsOverlapped.v154` — `es-AR/firefox-ios.xliff` — "Items" is translated as "ítems" here while the sibling sub-options on the same screen use "elementos".
    - Current: `Los ítems están superpuestos`
    - Source: `Items are overlapped`
    - Suggest: `Los elementos están superpuestos`
    - Inconsistent terminology within the same 'Design is broken' group, where ItemsMisaligned, ItemsNotVisible and MissingItems all use "elementos".
- `Saved Logins` — `es-AR/firefox-ios.xliff` — "Saved Logins" is rendered as "Ingresos guardados", which means "saved entries/income" rather than saved login credentials.
    - Current: `Ingresos guardados`
    - Source: `Saved Logins`
    - Suggest: `Inicios de sesión guardados`
    - The developer comment says this clears passwords and login data; "Ingresos" is not the Firefox term for logins in Spanish (standard is "Inicios de sesión"), and elsewhere in the batch "Sign In" is translated "Iniciar sesión".
- `BreachAlerts.Description` — `es-AR/firefox-ios.xliff` — Uses the "usted" form of address, inconsistent with the voseo/tuteo register used in es-AR Firefox.
    - Current: `desde la última vez que cambió su contraseña. Para proteger esta cuenta, inicie sesión en el sitio y cambie su contraseña.`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `desde la última vez que cambiaste tu contraseña. Para proteger esta cuenta, iniciá sesión en el sitio y cambiá tu contraseña.`
    - es-AR Firefox addresses the user informally (voseo); the formal imperatives "inicie"/"cambie" and "su" break the locale's register.
- `CoverSheet.v24.ETP.Description` — `es-AR/firefox-ios.xliff` — Formal "usted" register ("lo sigan", "Active") instead of the es-AR informal voseo form.
    - Current: `ayuda a evitar que los anuncios lo sigan. Active Estricta`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `ayuda a evitar que los anuncios te sigan. Activá Estricta`
    - es-AR localization addresses users informally; the formal imperative and object pronoun break the locale register.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `es-AR/firefox-ios.xliff` — Uses "le permite" (usted) whereas es-AR uses the voseo/tú-based informal address used elsewhere in the file.
    - Current: `Esto le permite guardar la imagen en la galería.`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Esto te permite guardar la imagen en tu Carrete.`
    - es-AR Firefox uses informal address; other strings in the batch ("Abre artículos…") avoid the formal "usted" form, so registers are inconsistent.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `es-AR/firefox-ios.xliff` — "Reader View" is rendered as "Modo lectura" here while other strings in the same file use "Vista de lectura".
    - Current: `Modo lectura`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Vista de lectura`
    - Inconsistent terminology within the same file: "Reader View" is translated "Vista de lectura" in the other strings.
- `SendTo.NoDevicesFound.Message` — `es-AR/firefox-ios.xliff` — Uses "usted" form while the rest of the batch addresses the user with "vos"/tuteo.
    - Current: `No tiene otros dispositivos conectados`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `No tenés otros dispositivos conectados`
    - Other strings in the same file use voseo ("Tocá para comenzar", "Llená todos los campos", "El enlace que estás tratando de compartir"), so the formal "usted" register here is inconsistent.
- `SendTo.NotSignedIn.Message` — `es-AR/firefox-ios.xliff` — Uses formal "usted" imperatives instead of the voseo register used elsewhere in the file.
    - Current: `Por favor abra Firefox, vaya a Configuración e inicie la sesión para continuar.`
    - Source: `Please open Firefox, go to Settings and sign in to continue.`
    - Suggest: `Por favor abrí Firefox, andá a Configuración e iniciá sesión para continuar.`
    - Inconsistent form of address: neighbouring strings use voseo ("Tocá", "Llená", "estás tratando").
- `SendTo.NotSignedIn.Title` — `es-AR/firefox-ios.xliff` — Uses formal "usted" ("No inició la sesión en su cuenta") instead of the voseo register used elsewhere in the file.
    - Current: `No inició la sesión en su cuenta de Firefox.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `No iniciaste sesión en tu cuenta de Firefox.`
    - Inconsistent form of address with the voseo/tuteo used in other strings of the same screen group.
- `Settings.Disconnect.Body` — `es-AR/firefox-ios.xliff` — Uses the formal "su cuenta" while the locale uses voseo/informal address elsewhere in this file.
    - Current: `Firefox dejará de sincronizar su cuenta pero no eliminará ningún dato de navegación en este dispositivo.`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `Firefox dejará de sincronizar tu cuenta pero no eliminará ningún dato de navegación en este dispositivo.`
    - Other strings in the same batch use the informal voseo register ("Elegí el tema que quieras", "Reemplazá tu búsqueda"), so "su cuenta" is an inconsistent formal form for "your account".
- `Settings.TrackingProtection.ProtectionCellFooter` — `es-AR/firefox-ios.xliff` — Uses the formal "su navegación" instead of the voseo/informal address used consistently elsewhere in this file.
    - Current: `ayuda a evitar que los anunciantes sigan su navegación`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `ayuda a evitar que los anunciantes sigan tu navegación`
    - Other strings in the same screen use informal address ("tocá", "desactivá", "tus pestañas"); es-AR uses the informal/voseo register.
- `Settings.WebsiteData.ConfirmPrompt` — `es-AR/firefox-ios.xliff` — Formal "sus sitios" instead of informal address, and "all of your website data" rendered as "datos de todos sus sitios".
    - Current: `Esta acción eliminará los datos de todos sus sitios.`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `Esta acción eliminará todos los datos de tus sitios web.`
    - es-AR uses informal voseo address, as in other strings in this file; the source also refers to all website data.

### E. Typography, punctuation & spacing

- `LiveActivity.Downloads.FileNameText.v138` — `es-AR/firefox-ios.xliff` — Straight quotes used instead of the typographic quotes of the source.
    - Current: `Descargando "%@"`
    - Source: `Downloading “%@”`
    - Suggest: `Descargando “%@”`
    - The en-US source uses curly quotes (“%@”); the translation replaces them with straight ASCII quotes.
- `TopSites.RemovePage.Button` — `es-AR/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The source uses an em dash (—) as separator; the translation uses a plain hyphen.
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

### Fixed to date (0)

_Nothing fixed yet._
