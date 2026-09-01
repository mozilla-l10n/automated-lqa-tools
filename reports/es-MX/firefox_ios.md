# Firefox iOS l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 1,884 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,884 |
| Missing strings | 34 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**34 strings** are not translated yet, concentrated in:

- `es-MX/firefox-ios.xliff` — 18
- `es-MX/firefox-ios.xliff` — 6
- `es-MX/firefox-ios.xliff` — 6
- `Shared/Supporting Files/en.lproj/GoogleLens.strings` — 2
- `es-MX/firefox-ios.xliff` — 2

**Files absent from the locale:**

- `Shared/Supporting Files/en.lproj/GoogleLens.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 8, `curly-double` 4, `straight-double` 3 | _mixed_ |
| apostrophe | `typographic` 8 | **typographic** |
| ellipsis | `char` 19 | **char** |
| dash | `em` 2 | **em** |
| inverted marks | `open-question` 42, `open-exclamation` 8 | **open-question** |
| register | `informal` 151, `formal` 5 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (114)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 64 |
| 3 | Degraded language (grammar, spelling, terminology) | 41 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `es-MX/firefox-ios.xliff` — The two placeholders are swapped: %1$@ (app name) and %2$@ (company name) are used in the wrong positions.
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas.`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas.`
    - Per the comment, %1$@ is the app name (Firefox) and %2$@ is the company name (Mozilla). The source says share with Mozilla's marketing partners how you discovered Firefox; the translation says share with Firefox's marketing partners how you discovered Mozilla.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.EmptyState.Root.Body.v135` — `es-MX/firefox-ios.xliff` — "We’ll also grab bookmarks from other synced devices" rendered as "we'll also show you", changing the meaning of importing/fetching bookmarks.
    - Current: `También te mostraremos los marcadores de tus otros dispositivos sincronizados.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `También traeremos los marcadores de tus otros dispositivos sincronizados.`
    - The source says the browser will grab/retrieve the bookmarks, not merely display them.
- `CredentialProvider.RetryAllert.Message.v137` — `es-MX/firefox-ios.xliff` — Past tense "There was an issue" rendered as present tense.
    - Current: `Hay un problema con el autocompletado.`
    - Source: `There was an issue with autofill. Please try again.`
    - Suggest: `Hubo un problema con el autocompletado.`
    - The source reports a problem that already occurred; the present tense changes the meaning.
- `Settings.Home.Option.ThoughtProvokingStories.subtitle.v116` — `es-MX/firefox-ios.xliff` — "powered by" mistranslated as "desarrollados por" (developed by).
    - Current: `Artículos desarrollados por %@`
    - Source: `Articles powered by %@`
    - Suggest: `Artículos proporcionados por %@`
    - The source means the articles are provided/powered by Pocket, not developed by it.
- `CreditCard.EditCard.CardNumberTitle.v112` — `es-MX/firefox-ios.xliff` — "Card Number" is translated as "credit card number", adding information not in the source.
    - Current: `Número de tarjeta de crédito`
    - Source: `Card Number`
    - Suggest: `Número de tarjeta`
    - The en-US source is simply "Card Number"; the label should not specify "de crédito", especially as the sibling string "Add Card" is rendered "Agregar tarjeta".
- `Menu.EnhancedTrackingProtection.SwitchOff.Text.v129` — `es-MX/firefox-ios.xliff` — "Protections are OFF" was translated as "Protección de navegación DESACTIVADA", inventing "browsing protection" and changing plural protections to singular.
    - Current: `Protección de navegación DESACTIVADA. Te sugerimos reactivarla.`
    - Source: `Protections are OFF. We suggest turning them back on.`
    - Suggest: `Las protecciones están DESACTIVADAS. Te sugerimos volver a activarlas.`
    - The source says "Protections are OFF. We suggest turning them back on." with no mention of "navegación"; other strings in the same screen render "protections" as "las protecciones".
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `es-MX/firefox-ios.xliff` — "Website URL" is rendered as "Enlace del sitio web" (website link) instead of URL.
    - Current: `Enlace del sitio web`
    - Source: `Website URL`
    - Suggest: `URL del sitio web`
    - The source says URL, and the sibling error string uses "URL" ("Ingresa una URL válida"); "Enlace" changes the term and is inconsistent within the same alert.
- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `es-MX/firefox-ios.xliff` — "You’re Protected" is translated as "Protección de navegación activada" (browsing protection enabled), which states something different.
    - Current: `Protección de navegación activada`
    - Source: `You’re Protected`
    - Suggest: `Estás protegido`
    - The source is a statement about the user being protected, not about a setting being enabled.
- `MainMenu.DesktopSiteOff.Title.v142` — `es-MX/firefox-ios.xliff` — State label "Off" translated as the imperative action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this is a label indicating that the Desktop Site option is OFF, i.e. a state, not an action to turn it off.
- `MainMenu.DesktopSiteOn.Title.v142` — `es-MX/firefox-ios.xliff` — State label "On" translated as the imperative action "Activar" instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this is a label indicating that the Desktop Site option is ON, i.e. a state, not an action to enable it.
- `MainMenu.HeaderBanner.Subtitle.v142` — `es-MX/firefox-ios.xliff` — Subtitle mistranslated and expanded: "Takes seconds. Change anytime." became "Toma solo un segundo y puedes cambiar tus preferencias cuando quieras."
    - Current: `Toma solo un segundo y puedes cambiar tus preferencias cuando quieras.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Toma unos segundos. Cámbialo cuando quieras.`
    - The source says it takes seconds (plural) and is two short sentences for a banner; the translation says "only one second" and adds "tus preferencias", making it much longer than the source in a space-constrained banner.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `es-MX/firefox-ios.xliff` — "Switch to mobile site" is rendered as "Cambiar el sitio móvil" (change the mobile site) instead of "Cambiar al sitio móvil".
    - Current: `Cambiar el sitio móvil`
    - Source: `Switch to mobile site`
    - Suggest: `Cambiar al sitio móvil`
    - The source means switching to the mobile version; the missing "a" changes the meaning and is inconsistent with MainMenu.ToolsSection.SwitchToMobileSite.Title.v131 ("Cambiar al sitio móvil").
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `es-MX/firefox-ios.xliff` — "Tools submenu" is translated as "Herramientas del submenú" (submenu's tools), reversing the relationship.
    - Current: `Herramientas del submenú`
    - Source: `Tools submenu`
    - Suggest: `Submenú Herramientas`
    - The source names the submenu called "Tools"; the translation says "tools of the submenu", which is a different meaning.
- `MainMenu.ToolsSection.ReaderViewOff.Title.v150` — `es-MX/firefox-ios.xliff` — State label "Off" is translated as the imperative action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this label indicates that Reader view is turned off (a state), not a command to turn it off.
- `MainMenu.ToolsSection.ReaderViewOn.Title.v150` — `es-MX/firefox-ios.xliff` — State label "On" is translated as the imperative action "Activar" instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this label indicates that Reader view is turned on (a state), not a command.
- `MainMenu.ToolsSection.Translation.Off.v151` — `es-MX/firefox-ios.xliff` — Badge "Off" showing translation is inactive is translated as the action "Desactivar".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The comment describes a badge indicating the inactive state, not an action to turn translation off.
- `MainMenu.ToolsSection.Translation.Translated.Title.v151` — `es-MX/firefox-ios.xliff` — "Translated…" is rendered as "Traducción finalizada…" (translation finished), not matching the source and inconsistent with the v145 string.
    - Current: `Traducción finalizada…`
    - Source: `Translated…`
    - Suggest: `Traducido…`
    - The source is the state label "Translated", already translated elsewhere as "Traducido"; "Traducción finalizada" adds a different meaning.
- `MainMenu.WebsiteDarkModeOffV2.Title.v142` — `es-MX/firefox-ios.xliff` — Label indicating Website Dark Mode is OFF is translated as the action "Desactivar".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The comment states this label indicates the option is OFF (a state), not an action.
- `MainMenu.WebsiteDarkModeOnV2.Title.v142` — `es-MX/firefox-ios.xliff` — Label indicating Website Dark Mode is ON is translated as the action "Activar".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The comment states this label indicates the option is ON (a state), not an action.
- `NativeErrorPage.Wayback.Error.Title.v154` — `es-MX/firefox-ios.xliff` — "Unable to connect" is rendered as "Error de conexión" (connection error) instead of the inability to connect.
    - Current: `Error de conexión`
    - Source: `Unable to connect`
    - Suggest: `No se puede conectar`
    - The source states the app is unable to connect; "Error de conexión" changes the message to a generic connection error rather than the state described in en-US.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `es-MX/firefox-ios.xliff` — "won’t sell you out" is rendered as "confiable", dropping the meaning that the browser will not betray/sell out the user.
    - Current: `Rápido, seguro y confiable.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Rápido, seguro y no te traiciona.`
    - The en-US states the browser will not sell the user out (privacy claim); "confiable" (trustworthy) is a generic substitution that loses the source's meaning.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `es-MX/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says features improve "for everyone"; the translation invents a geographic scope ("all over the world").
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-MX/firefox-ios.xliff` — "for everyone" is mistranslated as "para los usuarios en todo el mundo" (for users all over the world).
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The source says the data helps improve features, performance and stability "for everyone"; the translation adds a geographic claim not present in the en-US.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `es-MX/firefox-ios.xliff` — The status label "Blocked" is rendered as a past-tense verb phrase instead of matching the status term used elsewhere.
    - Current: `**Se bloqueó**`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `**Bloqueada**`
    - The bolded word is the status name defined in Settings.AIControls.AIPoweredFeaturesSection.BlockedStatus.v151 as "Bloqueada"; "Se bloqueó" states an event occurred rather than naming the status, breaking consistency on the same screen.
- `Settings.Notifications.SyncNotificationsTitle.v112` — `es-MX/firefox-ios.xliff` — The setting title "Sync" (a noun naming the feature) is rendered as the verb "Sincronizar".
    - Current: `Sincronizar`
    - Source: `Sync`
    - Suggest: `Sincronización`
    - The comment says it is the title of the Sync-related notifications setting, i.e. the feature name Sync, not an action.
- `Settings.Studies.Message.v148` — `es-MX/firefox-ios.xliff` — "randomly selects users" is translated without the object "users", losing the meaning.
    - Current: `realiza selecciones aleatorias para probar funciones`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `selecciona usuarios al azar para probar funciones`
    - The source states that the app randomly selects users to test features; the translation omits who is selected.
- `Settings.Summarize.FooterTitle.v142` — `es-MX/firefox-ios.xliff` — "Provides access" rendered as "Habilita el acceso" (enables access).
    - Current: `Habilita el acceso a la funcionalidad para resumir páginas.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Brinda acceso a la función de resumir páginas.`
    - The source states the setting provides access to summarizing pages; "habilita" changes the meaning to enabling.
- `Settings.Translation.SettingOff.v145` — `es-MX/firefox-ios.xliff` — "Off" is a state label but was translated as the imperative verb "Desactivar" (Turn off).
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The comment says this text indicates the translation feature has been disabled — a status, not an action.
- `Settings.Translation.SettingOn.v145` — `es-MX/firefox-ios.xliff` — "On" is a state label but was translated as the imperative verb "Activar" (Turn on).
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The comment says this text indicates the translation feature has been enabled — a status, not an action.
- `TermsOfUse.Description.v142` — `es-MX/firefox-ios.xliff` — The source says new Terms of Use were introduced, but the translation says they were updated.
    - Current: `Hemos actualizado los Términos de uso de %@ y nuestro Aviso de privacidad.`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Hemos introducido los Términos de uso de %@ y actualizado nuestro Aviso de privacidad.`
    - en-US: "We’ve introduced a %@ Terms of Use and updated our Privacy Notice." — the Terms of Use are new (introduced), only the Privacy Notice was updated.
- `TermsOfUse.Title.v142` — `es-MX/firefox-ios.xliff` — "We’ve got an update" is translated as "Hay una actualización disponible" (an update is available), implying an app update to download.
    - Current: `Hay una actualización disponible`
    - Source: `We’ve got an update`
    - Suggest: `Tenemos una actualización`
    - The source announces an update to the terms, not an available download; "disponible" adds meaning not present in en-US and misleads users.
- `Translations.Sheet.ToLabel.v145` — `es-MX/firefox-ios.xliff` — "To" in the from/to language pair is translated as "Para" instead of the directional "A".
    - Current: `Para`
    - Source: `To`
    - Suggest: `A`
    - This label pairs with "From"/"De" to indicate translation direction (Translate To). In Spanish the target-language label is "A", not "Para", which reads as "for".
- `WebCompatReporter.Category.DesignBroken.v154` — `es-MX/firefox-ios.xliff` — "Design is broken" is rendered as "Problema del diseño o interfaz", adding "interfaz" and dropping the broken state.
    - Current: `Problema del diseño o interfaz`
    - Source: `Design is broken`
    - Suggest: `El diseño está roto`
    - The source names a broken design; the translation introduces "interfaz", which is not in the source, and weakens the meaning to a generic "problema".
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `es-MX/firefox-ios.xliff` — "Captions are missing" is rendered as "Los subtítulos no cargan" (subtitles don't load), changing the meaning.
    - Current: `Los subtítulos no cargan`
    - Source: `Captions are missing`
    - Suggest: `Faltan los subtítulos`
    - The source states the captions are absent, not that they fail to load.
- `WebCompatReporter.SubOption.ItemsNotVisible.v154` — `es-MX/firefox-ios.xliff` — "Items not fully visible" is translated as items being partially obstructed, which asserts a cause not in the source.
    - Current: `Hay elementos obstruidos parcialmente`
    - Source: `Items not fully visible`
    - Suggest: `Hay elementos que no se ven completamente`
    - The source only says the items are not fully visible, not that something obstructs them.
- `WebCompatReporter.SubOption.MediaControlsBroken.v154` — `es-MX/firefox-ios.xliff` — "missing" is translated as "no cargan" (do not load) instead of being absent.
    - Current: `Los controles multimedia no funcionan o no cargan`
    - Source: `Media controls are broken or missing`
    - Suggest: `Los controles multimedia no funcionan o faltan`
    - Source says media controls are broken or missing; "no cargan" states they fail to load, a different claim.
- `DefaultBrowserCard.Description` — `es-MX/firefox-ios.xliff` — Translation says links, emails and messages open in Firefox, instead of links from websites, emails and Messages opening in Firefox.
    - Current: `Abrir vínculos, correos electrónicos y mensajes automáticamente en Firefox.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Configura los enlaces de sitios web, correos electrónicos y Mensajes para que se abran automáticamente en Firefox.`
    - The source means links coming from websites, emails and Messages; the target implies the emails and messages themselves are opened in Firefox, changing the meaning.
- `Done` — `es-MX/firefox-ios.xliff` — "Done" translated as "Cerrar" (Close) instead of "Listo".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the standard iOS "Done" button, rendered "Listo" in Spanish; "Cerrar" means "Close".
- `Done` — `es-MX/firefox-ios.xliff` — "Done" is translated as "Cerrar" (Close) instead of "Listo".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the Done button in the Settings title bar; "Cerrar" means Close and duplicates the translation used for the actual Close strings in this batch.
- `Downloads.CancelDialog.Resume` — `es-MX/firefox-ios.xliff` — "Resume" rendered as "Continuar" is ambiguous but acceptable; however the dialog button declining cancellation should read "Reanudar".
    - Current: `Continuar`
    - Source: `Resume`
    - Suggest: `Reanudar`
    - Source is "Resume" (resume the download); "Continuar" reads as a generic Continue and can be confused with confirming the cancel dialog.
- `Hotkeys.Forward.DiscoveryTitle` — `es-MX/firefox-ios.xliff` — "Forward" (navigate forward in session history) is translated as "Siguiente" instead of "Adelante".
    - Current: `Siguiente`
    - Source: `Forward`
    - Suggest: `Adelante`
    - This shortcut is the counterpart of Hotkeys.Back.DiscoveryTitle ("Atrás") and refers to navigating forward through session history in the current tab; "Siguiente" means "Next" and is the wording used for the next-tab shortcut, causing confusion.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `es-MX/firefox-ios.xliff` — Descriptive third-person "Removes" rendered as an imperative/infinitive "Eliminar".
    - Current: `Eliminar historial (incluyendo historial sincronizado de otros dispositivos), cookies y otros datos de navegación.`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `Elimina el historial (incluyendo el historial sincronizado de otros dispositivos), las cookies y otros datos de navegación.`
    - The en-US string is a description of what the action does ("Removes history…"), not a button label; the Spanish infinitive turns it into a command.
- `LoginsList.LoginsListSearchPlaceholder` — `es-MX/firefox-ios.xliff` — "Filter" (verb prompt in a search box) translated as the noun "Filtro".
    - Current: `Filtro`
    - Source: `Filter`
    - Suggest: `Filtrar`
    - The developer comment says it is placeholder text in a search box, i.e. an action prompt; "Filtro" is the noun "a filter".
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-MX/firefox-ios.xliff` — The translation says blocking reduces the number of social media companies, instead of reducing how much they can see of your online activity.
    - Current: `reduce la cantidad de empresas de redes sociales que pueden ver lo que haces en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce lo que las empresas de redes sociales pueden ver de lo que haces en línea`
    - en-US: "reduces how much social media companies can see what do you online" — it is about how much they can see, not how many companies there are.
- `Open Tabs` — `es-MX/firefox-ios.xliff` — "Open Tabs" (noun phrase, the syncing setting for open tabs) is rendered as the verb phrase "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - The developer comment says this is a toggle for tabs syncing, so "Open Tabs" is a noun phrase meaning currently open tabs, not a command to open tabs.
- `Search.SuggestSectionTitle.v102` — `es-MX/firefox-ios.xliff` — "Firefox Suggest" is a feature/brand name rendered as "Sugerencia de Firefox" (a singular common noun), changing the meaning.
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the product feature name "Firefox Suggest", used as a section header to distinguish Firefox suggestions; translating it as "Sugerencia de Firefox" (singular "suggestion") misnames the feature.
- `Search.ThirdPartyEngines.AddTitle` — `es-MX/firefox-ios.xliff` — Translation adds "nuevo" which is not in the source.
    - Current: `¿Agregar nuevo proveedor de búsqueda?`
    - Source: `Add Search Provider?`
    - Suggest: `¿Agregar proveedor de búsqueda?`
    - The en-US source is "Add Search Provider?" with no "new".
- `Search.ThirdPartyEngines.FormErrorMessage` — `es-MX/firefox-ios.xliff` — "all fields" is dropped from the translation.
    - Current: `Por favor, llena los campos correctamente.`
    - Source: `Please fill all fields correctly.`
    - Suggest: `Por favor, llena todos los campos correctamente.`
    - The source says "Please fill all fields correctly"; "todos" is missing.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-MX/firefox-ios.xliff` — "New tab arrived" is rendered as "Nueva pestaña agregada" (added) instead of received/arrived.
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Llegó una nueva pestaña desde otro dispositivo.`
    - The source says a tab arrived from another device; "agregada" (added) changes the meaning and is inconsistent with the sibling string's title "Pestaña recibida".
- `Settings.Disconnect.Body` — `es-MX/firefox-ios.xliff` — "browsing data" was translated as "historial de navegación" (browsing history), narrowing the meaning.
    - Current: `no eliminará nada en tu historial de navegación en este dispositivo`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `no eliminará ninguno de tus datos de navegación en este dispositivo`
    - The source says "won’t delete any of your browsing data", not browsing history; data is broader than history.
- `Settings.FxA.Sync.SectionName` — `es-MX/firefox-ios.xliff` — "Sync Settings" (a section title for Sync settings) rendered as the verb phrase "Sincronizar configuraciones" (sync the settings).
    - Current: `Sincronizar configuraciones`
    - Source: `Sync Settings`
    - Suggest: `Ajustes de Sync`
    - The source is a noun phrase naming the section for Sync settings, not an instruction to synchronize settings; the translation reverses the head noun.
- `Settings.Homepage.Shortcuts.ToggleOff.v100` — `es-MX/firefox-ios.xliff` — "Off" (a state label) is translated as the verb "Apagar" (to turn off).
    - Current: `Apagar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The source is the state of the toggle (Off), not an action; "Apagar" is an imperative verb meaning "turn off".
- `Settings.Homepage.Shortcuts.ToggleOn.v100` — `es-MX/firefox-ios.xliff` — "On" (a state label) is rendered as "Incluir" (include), which is not the source meaning.
    - Current: `Incluir`
    - Source: `On`
    - Suggest: `Activado`
    - The source indicates the toggle is ON to show the shortcuts section; "Incluir" means "include" and is a different word/meaning.
- `Settings.Passwords.OnboardingMessage.v103` — `es-MX/firefox-ios.xliff` — Conjunction "or" rendered as "y", changing the meaning of the protection options.
    - Current: `protegidas por Face ID, Touch ID y código de acceso en el dispositivo`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `protegidas por Face ID, Touch ID o el código de acceso del dispositivo`
    - Source says "Face ID, Touch ID or a device passcode" — alternatives, not all three combined.
- `Settings.SaveLogins.Title` — `es-MX/firefox-ios.xliff` — "Save Logins" translated as a noun phrase "Saved logins" instead of the action setting.
    - Current: `Inicios de sesión guardados`
    - Source: `Save Logins`
    - Suggest: `Guardar inicios de sesión`
    - The source is a setting to enable saving logins (imperative "Save Logins"), not a label for already-saved logins.
- `Settings.Search.Done.Button` — `es-MX/firefox-ios.xliff` — "Done" translated as "Cerrar" (Close).
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source button is "Done", the standard iOS confirmation label, not "Close".
- `Settings.Sync.ButtonDescription.v103` — `es-MX/firefox-ios.xliff` — The list of synced items is wrong: "tabs" is missing and "contraseñas" is repeated.
    - Current: `Inicia sesión para sincronizar contraseñas, marcadores, contraseñas y más.`
    - Source: `Sign in to sync tabs, bookmarks, passwords, and more.`
    - Suggest: `Inicia sesión para sincronizar pestañas, marcadores, contraseñas y más.`
    - The source lists "tabs, bookmarks, passwords, and more"; the translation drops "tabs" and duplicates "passwords".
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `es-MX/firefox-ios.xliff` — "ad tracking" is rendered as just "publicidad", dropping the tracking concept.
    - Current: `Permitir algo de publicidad para que los sitios web funcionen adecuadamente.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Permite algo de rastreo publicitario para que los sitios web funcionen adecuadamente.`
    - The source says "Allows some ad tracking" — the key concept is tracking by ads, not ads themselves; also the source is descriptive ("Allows"), not imperative.
- `Settings.WebsiteData.SelectedConfirmPrompt` — `es-MX/firefox-ios.xliff` — Adds "todos", changing "the selected items" to "all the selected items".
    - Current: `eliminará todos los elementos seleccionados`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `eliminará los elementos seleccionados`
    - The en-US says "This action will clear the selected items"; the target inserts "todos", which conflicts with the sibling string for clearing all data.
- `Show Tour` — `es-MX/firefox-ios.xliff` — "Show Tour" translated as "Lanzar tutorial de uso" (launch usage tutorial).
    - Current: `Lanzar tutorial de uso`
    - Source: `Show Tour`
    - Suggest: `Mostrar el recorrido`
    - The source is "Show Tour", i.e., show the onboarding screens again; "Lanzar tutorial de uso" changes the verb and the noun.
- `TabTray.Title` — `es-MX/firefox-ios.xliff` — "Open Tabs" (a title listing open tabs) is translated as an imperative action "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - The developer comment says this is the title for the tab tray, i.e. a noun phrase meaning the tabs currently open, not a command to open tabs.
- _…and 5 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Alerts.AddToCalendar.BodyDefault.v134` — `es-MX/firefox-ios.xliff` — Misspelling of "agregar" as "agrear".
    - Current: `agrear un evento`
    - Source: `This site is asking to download a file and add an event to your calendar.`
    - Suggest: `agregar un evento`
    - "agrear" is not a Spanish word; the source says "add an event", which is "agregar un evento" (as correctly used in the sibling string Alerts.AddToCalendar.Body.v134).
- `Alerts.RestoreTabs.Title.v109.v2` — `es-MX/firefox-ios.xliff` — Missing accent in the verb "falló".
    - Current: `%@ fallo.`
    - Source: `%@ crashed. Restore your tabs?`
    - Suggest: `%@ falló.`
    - The source "%@ crashed" is past tense; without the accent "fallo" is a noun, not the verb form.
- `Bookmarks.DeleteFolderWarning.Description` — `es-MX/firefox-ios.xliff` — Missing preposition "de" after "seguro" (queísmo).
    - Current: `¿Estás seguro que quieres eliminarlo`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Estás seguro de que quieres eliminarlo`
    - Standard Spanish requires "estar seguro de que"; omitting "de" is queísmo.
- `Bookmarks.EmptyState.Nested.Body.v135` — `es-MX/firefox-ios.xliff` — Infinitive "Agregar" used instead of the imperative required by the source instruction "Add bookmarks as you browse".
    - Current: `Agregar marcadores mientras navegas`
    - Source: `Add bookmarks as you browse so you can find your favorite sites later.`
    - Suggest: `Agrega marcadores mientras navegas`
    - The en-US is an imperative addressed to the user; the rest of the sentence uses second person ("navegas", "puedas"), so the infinitive is inconsistent and ungrammatical.
- `Bookmarks.Menu.DeleteBookmark.v132` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Marcador" in mid-sentence, inconsistent with other entries like "Eliminar carpeta" and "Editar marcador".
    - Current: `Eliminar Marcador`
    - Source: `Delete Bookmark`
    - Suggest: `Eliminar marcador`
    - Spanish does not use English title case; sibling strings in the same file use "Eliminar carpeta" and "Editar marcador".
- `ContextualHints.Translations.Body.v145` — `es-MX/firefox-ios.xliff` — Missing accent on the pronoun "tú".
    - Current: `cuando tu lo estés`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `cuando tú lo estés`
    - Here "tú" is the subject pronoun and requires the written accent; "tu" is the possessive.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `es-MX/firefox-ios.xliff` — Missing accent in the imperative "Continua".
    - Current: `Continua donde te quedaste`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Continúa donde te quedaste`
    - The imperative of "continuar" is "continúa" with an accent; "continua" is the adjective.
- `DefaultBrowserPopup.SecondLabel.v114` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Predeterminado" in the middle of the phrase.
    - Current: `2. Presiona *Navegador Predeterminado*`
    - Source: `2. Tap *Default Browser App*`
    - Suggest: `2. Presiona *Navegador predeterminado*`
    - Spanish does not capitalize adjectives in a phrase; only the first word is capitalized (matching the iOS setting label style used elsewhere, e.g. "tu predeterminado").
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-MX/firefox-ios.xliff` — Subjunctive "espíen" turns the relative clause restrictive/hypothetical, changing the meaning of "block companies from spying on your clicks".
    - Current: `bloqueamos automáticamente a las empresas que espíen tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `impedimos automáticamente que las empresas espíen tus clics`
    - The source says we block companies from spying on your clicks, not that we block those companies that (may) spy.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `es-MX/firefox-ios.xliff` — Number agreement error between demonstrative and noun.
    - Current: `Si bloqueas estas funcionalidad`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `Si bloqueas esta funcionalidad`
    - "estas" (plural) does not agree with the singular noun "funcionalidad".
- `Settings.AIControls.BlockedInformation.v151` — `es-MX/firefox-ios.xliff` — "especificas" is missing its accent mark.
    - Current: `funciones especificas`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `funciones específicas`
    - The Spanish adjective is "específicas" with an accent on the second syllable; "especificas" is a misspelling (or a different verb form).
- `CloseTabsToast.SingleTabTitle.v113` — `es-MX/firefox-ios.xliff` — Incorrect capitalization of the adjective in mid-sentence; Spanish does not use title case.
    - Current: `Pestaña Cerrada`
    - Source: `Tab Closed`
    - Suggest: `Pestaña cerrada`
    - Spanish sentence case applies; the parallel string CloseTabsToast.Title.v113 correctly uses "Pestañas cerradas".
- `ErrorPages.AdvancedWarning1.Text` — `es-MX/firefox-ios.xliff` — Register inconsistency ("su" vs. tú elsewhere) and gender disagreement in "conexión ... seguro".
    - Current: `Advertencia: no podemos confirmar que su conexión a este sitio sea seguro.`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `Advertencia: no podemos confirmar que tu conexión a este sitio sea segura.`
    - "conexión" is feminine, so the adjective must be "segura"; the surrounding error-page strings use the informal "tu/tus" form (e.g. ErrorPages.AdvancedWarning2 "si aceptas", CertWarning "tu información").
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-MX/firefox-ios.xliff` — Missing accent in "linea".
    - Current: `tu actividad en linea`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `tu actividad en línea`
    - The correct spelling is "línea" with an accent.
- `ScanQRCode.PermissionError.Message.v100` — `es-MX/firefox-ios.xliff` — Wrong preposition: "acceso de la cámara" should be "acceso a la cámara"; also drops "device".
    - Current: `Permitir a Firefox el acceso de la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Permitir a Firefox el acceso a la cámara.`
    - In Spanish "acceso" takes the preposition "a"; "acceso de la cámara" is ungrammatical for "access camera".
- `Search.ThirdPartyEngines.AddSuccess` — `es-MX/firefox-ios.xliff` — Agreement/word order error: "¡Agregado nuevo motor de búsqueda!" is awkward and adds "nuevo" not in source.
    - Current: `¡Agregado nuevo motor de búsqueda!`
    - Source: `Added Search engine!`
    - Suggest: `¡Motor de búsqueda agregado!`
    - Source is "Added Search engine!"; the Spanish inverts the participle before an unarticulated noun and inserts "nuevo", which is not in the source.
- `SendTo.NotSignedIn.Title` — `es-MX/firefox-ios.xliff` — Wrong preposition: "iniciar sesión" takes "en", not "a".
    - Current: `No has iniciado sesión a tu cuenta de Firefox.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `No has iniciado sesión en tu cuenta de Firefox.`
    - Standard Spanish government is "iniciar sesión en"; "sesión a" is ungrammatical.
- `Settings.Home.Current.Description.v101` — `es-MX/firefox-ios.xliff` — Missing accent on interrogative "qué".
    - Current: `Elige que mostrar como página de inicio.`
    - Source: `Choose what displays as the homepage.`
    - Suggest: `Elige qué mostrar como página de inicio.`
    - In an indirect question, "qué" must carry a written accent, as done correctly in the parallel string Settings.Home.Option.Description.v101.
- `xRJbBP` — `es-MX/firefox-ios.xliff` — Incorrect capitalization of the second word in Spanish sentence case.
    - Current: `Nueva Búsqueda`
    - Source: `New Search`
    - Suggest: `Nueva búsqueda`
    - Spanish does not use title case; only the first word should be capitalized, as with "Acción rápida" in the same file.

### D. Terminology, register & consistency

- `Biometry.Screen.UniversalAuthenticationReason.v115` — `es-MX/firefox-ios.xliff` — Impersonal infinitive "Autenticarse" conflicts with the second-person imperative used in the parallel v122 string.
    - Current: `Autenticarse para acceder a las contraseñas.`
    - Source: `Authenticate to access passwords.`
    - Suggest: `Autentícate para acceder a las contraseñas.`
    - The same source pattern is translated as "Autentícate..." in Biometry.Screen.UniversalAuthenticationReason.v122; the register should be consistent within the file.
- `LibraryPanel.Sections.LastSevenDays.v138` — `es-MX/firefox-ios.xliff` — "Last 7 Days" uses a different pattern than the sibling section titles.
    - Current: `Los últimos 7 días`
    - Source: `Last 7 Days`
    - Suggest: `Últimos 7 días`
    - The neighboring sections on the same screen are "Últimas 4 semanas" and "Últimas 24 horas" without the article; the added "Los" is inconsistent.
- `MainMenu.SiteProtection.ProtectionsOff.Title.v141` — `es-MX/firefox-ios.xliff` — "Protections" is translated as "Protección de navegación" here while the sibling badge string uses "Protecciones".
    - Current: `Protección de navegación DESACTIVADA`
    - Source: `Protections are OFF`
    - Suggest: `Protecciones DESACTIVADAS`
    - The en-US source is "Protections are OFF"; MainMenu.SiteProtection.Protections.Title.v153 on the same screen renders "Protections" as "Protecciones", so the term should be consistent and not expanded to "Protección de navegación".
- `MainMenu.SiteProtection.ProtectionsOn.Title.v141` — `es-MX/firefox-ios.xliff` — "Protections" is translated as "Protección de navegación" here while the sibling badge string uses "Protecciones".
    - Current: `Protección de navegación ACTIVADA`
    - Source: `Protections are ON`
    - Suggest: `Protecciones ACTIVADAS`
    - The en-US source is "Protections are ON"; MainMenu.SiteProtection.Protections.Title.v153 on the same screen renders "Protections" as "Protecciones", so the term should be consistent and not expanded to "Protección de navegación".
- `MainMenu.Submenus.Save.AddToShortcuts.Subtitle.v131` — `es-MX/firefox-ios.xliff` — "Shortcut" is rendered as "Atajo" here but as "Acceso directo" in the parallel accessibility-label string and in the related Add/Remove from Shortcuts items.
    - Current: `Atajo`
    - Source: `Shortcut`
    - Suggest: `Acceso directo`
    - MainMenu.Submenus.Save.AccessibilityLabels.AddToShortcuts.Subtitle.v132 has the identical source "Shortcut" translated as "Acceso directo", and the surrounding Shortcuts strings use "accesos directos"; the same term on the same screen must be consistent.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `es-MX/firefox-ios.xliff` — "Reader View" is rendered as "vista de lector" here but as "vista de lectura" in the sibling On/Subtitle strings on the same menu.
    - Current: `Desactivar la vista de lector`
    - Source: `Turn off Reader View`
    - Suggest: `Desactivar la vista de lectura`
    - MainMenu.Submenus.Tools.ReaderView.On.Title.v131 and .Subtitle.v131 both use "vista de lectura" for the same source term "Reader View"; this inconsistency appears on the same submenu.
- `Onboarding.Customization.Toolbar.Description.v123` — `es-MX/firefox-ios.xliff` — Uses the formal 'usted' form while the rest of the onboarding screen uses informal 'tú'.
    - Current: `Mantenga las búsquedas al alcance.`
    - Source: `Keep searches within reach.`
    - Suggest: `Mantén las búsquedas al alcance.`
    - Surrounding onboarding strings address the user informally (Elige, Configura, Guarda), so the formal imperative is an inconsistent register.
- `Onboarding.Customization.Toolbar.Title.v123` — `es-MX/firefox-ios.xliff` — Uses the formal 'usted' imperative 'Elija' while parallel strings use informal 'Elige'.
    - Current: `Elija una ubicación para la barra de herramientas`
    - Source: `Pick a toolbar placement`
    - Suggest: `Elige una ubicación para la barra de herramientas`
    - Onboarding.Customization.Theme.Title.v123 uses 'Elige un tema'; mixing formal and informal address on the same flow is inconsistent register.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `es-MX/firefox-ios.xliff` — "Top" is rendered as "Arriba" while the parallel option "Bottom" is "Inferior", and the v140 pair uses Superior/Inferior.
    - Current: `Arriba`
    - Source: `Top`
    - Suggest: `Superior`
    - Same source term on the same toolbar-customization screen is translated inconsistently with its paired option (Inferior) and with Onboarding.Modern.Customization.Toolbar.Top.Action.v140 (Superior).
- `Onboarding.Modern.Welcome.Description.v145` — `es-MX/firefox-ios.xliff` — The v145 welcome description drops the second-person address used throughout the onboarding flow and in the identical v140 string.
    - Current: `Una sola elección brinda protección en toda la web. Es posible cambiarla en cualquier momento.`
    - Source: `One choice protects you everywhere you go on the web. You can always change it later.`
    - Suggest: `Una sola elección te protege donde sea que navegues en la web. Siempre puedes cambiarla más tarde.`
    - Source is "One choice protects you everywhere you go on the web. You can always change it later." — the "you" is dropped, breaking the tú register used in every other onboarding string (e.g. "te protege", "puedes cambiarla" in the identical v140 source).
- `PrivacyDashboard.Fingerprinters.v155` — `es-MX/firefox-ios.xliff` — "Fingerprinters" is rendered as "Rastreadores de huella digital", conflating it with trackers; Firefox's established Spanish term is "Detectores de huellas digitales".
    - Current: `Rastreadores de huella digital`
    - Source: `Fingerprinters`
    - Suggest: `Detectores de huellas digitales`
    - The Privacy Dashboard lists trackers and fingerprinters as separate categories; using "Rastreadores" (trackers) for fingerprinters creates terminology collision with the tracker bar on the same screen.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `es-MX/firefox-ios.xliff` — "email masks" translated as "plantillas para correos electrónicos" (templates) instead of "máscaras de correo electrónico" used everywhere else in the file.
    - Current: `Ya has usado tus 5 plantillas gratuitas para correos electrónicos`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `Ya has usado tus 5 máscaras de correo electrónico gratuitas`
    - The source says "5 free email masks"; "plantillas" means templates and is inconsistent with the term "máscaras de correo electrónico" used in all other RelayMask strings.
- `UnifiedSearch.SearchEngineSelection.SearchSettings.Title.v133` — `es-MX/firefox-ios.xliff` — "Search Settings" rendered as "Configuración de búsqueda" while the accessibility label for the same row uses "Ajustes de búsqueda".
    - Current: `Configuración de búsqueda`
    - Source: `Search Settings`
    - Suggest: `Ajustes de búsqueda`
    - Same control on the same sheet has two different renderings of "Search settings" (label vs. visible title), an inconsistency within the screen.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `es-MX/firefox-ios.xliff` — "Trending Searches" translated inconsistently with the section title on the same feature.
    - Current: `Mostrar tendencias de búsquedas`
    - Source: `Show Trending Searches`
    - Suggest: `Mostrar búsquedas en tendencia`
    - SearchZero.TrendingSearches.SectionTitle uses "Tendencias"; here "tendencias de búsquedas" shifts the meaning to trends of searches rather than the searches that are trending, and is inconsistent within the same feature.
- `Settings.Browsing.AdBlocker.Description.v155` — `es-MX/firefox-ios.xliff` — "funcionalidad" is repeated in the same sentence, and the second use mistranslates "turning this off".
    - Current: `Si tienes problemas de funcionalidad en algún sitio, intenta desactivar esta funcionalidad.`
    - Source: `Reduces ads and ad-related trackers. If a site looks broken, try turning this off.`
    - Suggest: `Si algún sitio parece no funcionar bien, intenta desactivar esta opción.`
    - The source says "If a site looks broken, try turning this off" — referring to the toggle, not a "funcionalidad"; the duplicated term is a clumsy repetition that degrades the text.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `es-MX/firefox-ios.xliff` — "Terms of Use" is rendered as "Condiciones de uso" here but as "Términos de uso" in the rest of the same file.
    - Current: `Se han abierto las Condiciones de uso`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Se han abierto los Términos de uso`
    - Inconsistent terminology within the same screen/file; other strings (TermsOfUse.TitleValue1, TermsOfUse.Link.TermsOfUse) use "Términos de uso".
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `es-MX/firefox-ios.xliff` — "Full time" is rendered as "Tiempo completo" here but as "Finalizado" in the other Full Time strings of the same widget.
    - Current: `Tiempo completo • Penales (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Finalizado • Penales (%@)`
    - WorldCup.HomepageWidget.FTLabel/FTNoParenthesisLabel translate the same source term "Full Time" as "Finalizado"; "Tiempo completo" is also not the standard football term for the end of a match in es-MX.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `es-MX/firefox-ios.xliff` — "BRONZE FINAL" is translated as "TERCER PUESTO", which duplicates the separate THIRD PLACE label and names the result rather than the match.
    - Current: `TERCER PUESTO`
    - Source: `BRONZE FINAL`
    - Suggest: `PARTIDO POR EL TERCER LUGAR`
    - The Bronze final is the third-place playoff match, a distinct item from WorldCup.HomepageWidget.RoundPhase.ThirdPlaceLabel ("TERCER LUGAR"); rendering it as "TERCER PUESTO" makes the two labels indistinguishable in meaning.
- `This action will clear all of your private data. It cannot be undone.` — `es-MX/firefox-ios.xliff` — Register switches to formal "sus" while the rest of the batch (including the parallel ClearHistoryConfirm string) uses informal "tus".
    - Current: `Esta acción borrará todos sus datos privados.`
    - Source: `This action will clear all of your private data. It cannot be undone.`
    - Suggest: `Esta acción borrará todos tus datos privados.`
    - The parallel string in ClearHistoryConfirm.strings uses "todos tus datos privados", and the locale consistently addresses the user informally ("Usa tu huella digital", "tu navegador predeterminado"). Mixing formal address is a register inconsistency.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `es-MX/firefox-ios.xliff` — Register inconsistency: "te permite" (tú) mixed with "su rollo de cámara" (usted).
    - Current: `Esto te permite guardar la imagen en su rollo de cámara.`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Esto te permite guardar la imagen en tu carrete de fotos.`
    - The rest of the file uses the informal "tú" form (e.g., "tus fotos"); "su" breaks the established address form within the same sentence.
- `fi3W24-eHmH1H` — `es-MX/firefox-ios.xliff` — ‘Clear Private Tabs’ is rendered as “Borrar Pestañas Privadas” here but as “Limpiar Pestañas Privadas” in the related strings eHmH1H and PzSrmZ-eHmH1H.
    - Current: `‘Borrar Pestañas Privadas’`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `‘Limpiar Pestañas Privadas’`
    - The same menu item name must match the label defined in eHmH1H ("Limpiar Pestañas Privadas") so Siri/voice matching and the UI stay consistent.

### E. Typography, punctuation & spacing

- `NSFaceIDUsageDescription` — `es-MX/firefox-ios.xliff` — Malformed parenthetical dashes with missing spacing around the inserted gloss.
    - Current: `Face ID - reconocimiento facial-para acceder`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Face ID (reconocimiento facial) para acceder`
    - The dash pair is unbalanced and there is no space before "para", producing broken typography not present in the en-US source.
- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-MX/firefox-ios.xliff` — Ampersand kept instead of the Spanish conjunction "y".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - Spanish does not use "&" as a conjunction in UI labels; the en-US "&" should be rendered as "y".
- `Onboarding.Customization.Theme.Continue.Action.v123` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of 'Continuar' mid-sentence; Spanish uses sentence case.
    - Current: `Guardar y Continuar`
    - Source: `Save and Continue`
    - Suggest: `Guardar y continuar`
    - Spanish does not use English title case; the parallel string Onboarding.Customization.Toolbar.Continue.Action.v123 correctly reads 'Guardar y comenzar a navegar'.
- `Onboarding.Customization.Theme.System.Action.v123` — `es-MX/firefox-ios.xliff` — Title-case capitalization of the second word does not follow Spanish sentence case.
    - Current: `Sistema Automático`
    - Source: `System Auto`
    - Suggest: `Sistema automático`
    - Spanish uses sentence case for UI labels; 'Automático' should be lowercase here.
- `TopSites.RemovePage.Button` — `es-MX/firefox-ios.xliff` — Em dash in the source replaced by a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The en-US string uses an em dash (—) as separator; the translation uses a plain hyphen.
- `Open & Fill` — `es-MX/firefox-ios.xliff` — Ampersand used as a conjunction in Spanish instead of "y".
    - Current: `Abrir & Llenar`
    - Source: `Open & Fill`
    - Suggest: `Abrir y llenar`
    - Spanish does not use "&" as a word conjunction, and sentence-case capitalization applies.
- `PzSrmZ-eHmH1H` — `es-MX/firefox-ios.xliff` — Straight double quotes used instead of the single curly quotation marks of the source.
    - Current: `"Limpiar Pestañas Privadas"`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘Limpiar Pestañas Privadas’`
    - The en-US source uses ‘…’ and the sibling strings in the same file keep those marks; this one deviates.
- `PzSrmZ-scEmjs` — `es-MX/firefox-ios.xliff` — Straight double quotes used instead of the single curly quotation marks of the source.
    - Current: `"Nueva búsqueda privada"`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `‘Nueva Búsqueda Privada’`
    - The en-US source uses ‘…’, and the item name elsewhere in the file is "Nueva Búsqueda Privada"; both the quote style and capitalization deviate here.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-MX/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-MX/firefox-ios.xliff` — fixed 2026-08-24
