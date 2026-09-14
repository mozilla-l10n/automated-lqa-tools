# Firefox iOS l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,867 of 1,883 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (122)

- `NSFaceIDUsageDescription` — `es-MX/firefox-ios.xliff` — Parenthetical gloss uses hyphens without surrounding spaces, producing "facial-para" with no space.
    - Current: `Firefox requiere Face ID - reconocimiento facial-para acceder`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Firefox requiere Face ID (reconocimiento facial) para acceder`
    - The added explanatory aside is punctuated inconsistently and the closing hyphen is glued to the next word, leaving no space between "facial" and "para".
- `This action will clear all of your private data. It cannot be undone.` — `es-MX/firefox-ios.xliff` — Uses formal "sus" while the locale convention and the parallel string in ClearHistoryConfirm use informal "tus".
    - Current: `Esta acción borrará todos sus datos privados.`
    - Source: `This action will clear all of your private data. It cannot be undone.`
    - Suggest: `Esta acción borrará todos tus datos privados.`
    - es-MX is established as informal; the equivalent string in ClearHistoryConfirm.strings uses "tus datos privados".
- `DefaultBrowserCard.Description` — `es-MX/firefox-ios.xliff` — Translation says links, emails and messages open in Firefox, dropping that it is links from websites, emails and Messages.
    - Current: `Abrir vínculos, correos electrónicos y mensajes automáticamente en Firefox.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Haz que los enlaces de sitios web, correos electrónicos y Mensajes se abran automáticamente en Firefox.`
    - The source sets links coming from websites, emails and Messages to open in Firefox; the target implies the emails and messages themselves open in Firefox.
- `Done` — `es-MX/firefox-ios.xliff` — "Done" is translated as "Cerrar" (Close) instead of "Listo"/"Hecho".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the "Done" button of the Find in Page toolbar; "Cerrar" means "Close", a different label from the en-US "Done".
- `DefaultBrowserOnboarding.Description2` — `es-MX/firefox-ios.xliff` — "Default Browser App" is rendered as "navegador por defecto" here and in the screenshot string while other strings on the same feature use "navegador predeterminado".
    - Current: `2. Pulsar la Aplicación del navegador por defecto`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Pulsar Aplicación de navegador predeterminado`
    - The same source term "Default Browser" is translated "predeterminado" in DefaultBrowserCard.Title and Settings.DefaultBrowserMenuItem but "por defecto" here, an inconsistency within the same feature file.
- `Changes color theme.` — `es-MX/firefox-ios.xliff` — "Changes color theme" is rendered as "changes the theme's color", inverting the noun phrase.
    - Current: `Cambiar el color del tema.`
    - Source: `Changes color theme.`
    - Suggest: `Cambia el tema de color.`
    - The source refers to changing the color theme, not the color of the theme; the accessibility hint should also be third person like the source.
- `ContextMenu.ButtonToast.NewPrivateTabOpened.LabelText` — `es-MX/firefox-ios.xliff` — Unnecessary title-case capitalization in Spanish.
    - Current: `Nueva Pestaña Privada abierta`
    - Source: `New Private Tab opened`
    - Suggest: `Nueva pestaña privada abierta`
    - Spanish does not use English title case; the parallel v113 string correctly uses "Nueva pestaña privada abierta", creating an inconsistency.
- `Done` — `es-MX/firefox-ios.xliff` — "Done" is translated as "Cerrar" (Close) instead of "Listo"/"Hecho".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the Done button in the Settings title bar; "Cerrar" means Close, a different action/label, and duplicates the Close strings in the same file.
- `Downloads.CancelDialog.Resume` — `es-MX/firefox-ios.xliff` — "Resume" rendered as "Continuar" is acceptable, but more precisely "Reanudar".
    - Current: `Continuar`
    - Source: `Resume`
    - Suggest: `Reanudar`
    - Source "Resume" declines cancellation and resumes the download; "Reanudar" is the standard Firefox term, while "Continuar" reads as a generic Continue.
- `ContextMenu.ButtonToast.NewTabOpened.LabelText` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Pestaña" mid-sentence.
    - Current: `Nueva Pestaña abierta`
    - Source: `New Tab opened`
    - Suggest: `Nueva pestaña abierta`
    - Spanish does not use title case; the v114 variant of the same string correctly reads "Nueva pestaña abierta".
- `Could not load page.` — `es-MX/firefox-ios.xliff` — Final period from the source sentence is missing.
    - Current: `No se pudo cargar la página`
    - Source: `Could not load page.`
    - Suggest: `No se pudo cargar la página.`
    - The en-US string ends with a period; the translation drops it.
- `Downloads.CancelDialog.Message` — `es-MX/firefox-ios.xliff` — Missing preposition "de" after "seguro" and "this download" rendered as "la descarga".
    - Current: `¿Estás seguro que quieres cancelar la descarga?`
    - Source: `Are you sure you want to cancel this download?`
    - Suggest: `¿Estás seguro de que quieres cancelar esta descarga?`
    - "estar seguro de que" requires the preposition; also the source says "this download".
- `ErrorPages.AdvancedWarning1.Text` — `es-MX/firefox-ios.xliff` — Formal "su conexión" breaks the locale's informal register used in the adjacent strings, and the adjective doesn't agree with "conexión".
    - Current: `no podemos confirmar que su conexión a este sitio sea seguro`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `no podemos confirmar que tu conexión a este sitio sea segura`
    - es-MX convention is informal address ("tu"), as in the neighboring ErrorPages.AdvancedWarning2.Text ("Sigue adelante si aceptas"); also "seguro" must agree with the feminine noun "conexión".
- `ErrorPages.AdvancedWarning2.Text` — `es-MX/firefox-ios.xliff` — "tampering by an attacker" is rendered as "una falsificación de un atacante" (a forgery), changing the meaning.
    - Current: `una falsificación de un atacante`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `una manipulación por parte de un atacante`
    - The source says the connection may have been tampered with by an attacker, not that it is a forgery.
- `Hotkeys.Forward.DiscoveryTitle` — `es-MX/firefox-ios.xliff` — "Forward" (navigation forward in session history) is rendered as "Siguiente", which does not convey the browser navigation action.
    - Current: `Siguiente`
    - Source: `Forward`
    - Suggest: `Adelante`
    - The string pairs with Hotkeys.Back.DiscoveryTitle ("Atrás"); the browser navigation term is "Adelante", not the generic "Siguiente".
- `Keyboard.Shortcuts.ActualSize` — `es-MX/firefox-ios.xliff` — "Actual Size" mistranslated as "Tamaño actual" (current size) instead of the real/original size.
    - Current: `Tamaño actual`
    - Source: `Actual Size`
    - Suggest: `Tamaño real`
    - Per the comment, it resets the page view to the standard viewing size; "actual" is a false friend in Spanish meaning "current".
- `Menu.AddToShortcuts.v99` — `es-MX/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the related toast on the same feature.
    - Current: `Agregar a accesos directos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - Menu.AddPin.Confirm2 translates the same "Shortcuts" feature name as "atajos"; using two different terms for the same home-screen feature is inconsistent.
- `Looks like Firefox crashed previously. Would you like to restore your tabs?` — `es-MX/firefox-ios.xliff` — "restore your tabs" is translated as "restablecer" (reset) instead of "restaurar".
    - Current: `¿Te gustaría restablecer tus pestañas?`
    - Source: `Looks like Firefox crashed previously. Would you like to restore your tabs?`
    - Suggest: `¿Te gustaría restaurar tus pestañas?`
    - The prompt restores previously open tabs; "restablecer" means reset/re-establish and is the wrong term for restoring tabs after a crash.
- `Menu.CopyURL.Confirm` — `es-MX/firefox-ios.xliff` — Adds "Enlace" (link), which the source does not contain.
    - Current: `Enlace URL copiado al portapapeles`
    - Source: `URL Copied To Clipboard`
    - Suggest: `URL copiada al portapapeles`
    - Source is "URL Copied To Clipboard"; "Enlace URL" is redundant and adds a word not in the source.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-MX/firefox-ios.xliff` — The translation says blocking reduces the number of social media companies, instead of reducing how much they can see of what you do online.
    - Current: `reduce la cantidad de empresas de redes sociales que pueden ver lo que haces en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce lo que las empresas de redes sociales pueden ver de lo que haces en línea`
    - The en-US says "reduces how much social media companies can see what do you online" — it limits their visibility, not the number of companies.
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-MX/firefox-ios.xliff` — "linea" is missing its accent (should be "línea").
    - Current: `tu actividad en linea`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `tu actividad en línea`
    - Spelling/accent error; the same phrase is correctly written "en línea" elsewhere in this file.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `es-MX/firefox-ios.xliff` — Register switches to formal "su" mid-sentence after informal "te".
    - Current: `Esto te permite guardar la imagen en su rollo de cámara.`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Esto te permite guardar la imagen en tu carrete de fotos.`
    - es-MX convention is informal address; "te permite ... en su" mixes informal and formal in the same sentence.
- `Open Tabs` — `es-MX/firefox-ios.xliff` — "Open Tabs" (a sync setting label, a noun phrase) is translated as the imperative "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - The developer comment says this toggles the tab syncing setting, so "Open Tabs" is a noun phrase meaning currently open tabs, not a command to open tabs.
- `Search.SuggestSectionTitle.v102` — `es-MX/firefox-ios.xliff` — "Firefox Suggest" is a feature/brand name and was translated as "Sugerencia de Firefox" (a Firefox suggestion).
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the product feature name "Firefox Suggest", used as a section header; it should not be turned into a generic singular noun phrase.
- `Search.ThirdPartyEngines.AddTitle` — `es-MX/firefox-ios.xliff` — Translation adds "nuevo", which is not in the source "Add Search Provider?".
    - Current: `¿Agregar nuevo proveedor de búsqueda?`
    - Source: `Add Search Provider?`
    - Suggest: `¿Agregar proveedor de búsqueda?`
    - The en-US source says "Add Search Provider?" with no "new".
- `ScanQRCode.PermissionError.Message.v100` — `es-MX/firefox-ios.xliff` — Wrong preposition: "el acceso de la cámara" should be "el acceso a la cámara".
    - Current: `Permitir a Firefox el acceso de la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Permitir a Firefox el acceso a la cámara.`
    - "Allow Firefox to access camera" requires "acceso a la cámara" in Spanish; "acceso de la cámara" means the camera's access.
- `ScanQRCode.PermissionError.Message.v100` — `es-MX/firefox-ios.xliff` — "device" is dropped from "Go to device ‘Settings’".
    - Current: `Ir a ‘Configuración’ > ‘Firefox’.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Ir a ‘Configuración’ del dispositivo > ‘Firefox’.`
    - The source specifies the device's Settings app, which the translation omits, losing the distinction from Firefox's own settings.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-MX/firefox-ios.xliff` — "New tab arrived from another device" is rendered as "Nueva pestaña agregada desde otro dispositivo" (added), losing the "arrived/received" meaning.
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Llegó una nueva pestaña desde otro dispositivo.`
    - The source says a tab arrived (was received) from another device; "agregada" says it was added, which differs from the en-US and from the sibling string's "Se recibió una pestaña".
- `SendTo.NoDevicesFound.Message` — `es-MX/firefox-ios.xliff` — Plural "any other devices" rendered as singular "otro dispositivo".
    - Current: `No tienes otro dispositivo conectado`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `No tienes otros dispositivos conectados`
    - The en-US says the user has no other devices (plural) connected to the account.
- `SendTo.NotSignedIn.Title` — `es-MX/firefox-ios.xliff` — Wrong preposition: "iniciado sesión a tu cuenta" should be "en tu cuenta".
    - Current: `No has iniciado sesión a tu cuenta de Firefox.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `No has iniciado sesión en tu cuenta de Firefox.`
    - Spanish requires "iniciar sesión en" a account, not "a".
- `Settings.AddCustomEngine.Title` — `es-MX/firefox-ios.xliff` — "Add Search Engine" translated as "Agregar motor", dropping "search" and diverging from the identical source string elsewhere.
    - Current: `Agregar motor`
    - Source: `Add Search Engine`
    - Suggest: `Agregar motor de búsqueda`
    - Source is "Add Search Engine"; Settings.AddCustomEngine with the same source is translated "Agregar motor de búsqueda".
- `Settings.Disconnect.Body` — `es-MX/firefox-ios.xliff` — "any of your browsing data" mistranslated as "nada en tu historial de navegación" (browsing history).
    - Current: `no eliminará nada en tu historial de navegación en este dispositivo`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `no eliminará ninguno de tus datos de navegación en este dispositivo`
    - The source says browsing data, not browsing history; the Spanish narrows the scope of what is preserved.
- `Settings.FxA.Sync.SectionName` — `es-MX/firefox-ios.xliff` — "Sync Settings" (noun phrase, section title) rendered as an imperative "Sincronizar configuraciones" (Sync the settings).
    - Current: `Sincronizar configuraciones`
    - Source: `Sync Settings`
    - Suggest: `Configuración de Sync`
    - The developer comment says it is a section title for sync settings; the translation reverses the head noun and reads as a command to sync settings.
- `Settings.Home.Current.Description.v101` — `es-MX/firefox-ios.xliff` — Missing accent on interrogative/relative "qué" in "Elige que mostrar".
    - Current: `Elige que mostrar como página de inicio.`
    - Source: `Choose what displays as the homepage.`
    - Suggest: `Elige qué mostrar como página de inicio.`
    - Indirect interrogative requires the accented "qué", as done correctly in Settings.Home.Option.Description.v101.
- `Settings.Homepage.Shortcuts.ToggleOn.v100` — `es-MX/firefox-ios.xliff` — "On" (toggle state) is translated as "Incluir" (Include), which is not the state label.
    - Current: `Incluir`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this is the ON state of the shortcuts toggle; "Incluir" means "Include", not "On". It is also inconsistent with the paired Off string.
- `Settings.Homepage.Shortcuts.ToggleOff.v100` — `es-MX/firefox-ios.xliff` — "Off" (toggle state) is rendered as the verb "Apagar" (to turn off) instead of a state label.
    - Current: `Apagar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The comment indicates this labels the OFF state of the shortcuts section toggle; "Apagar" is an imperative verb, not the state.
- `Settings.Sync.ButtonDescription.v103` — `es-MX/firefox-ios.xliff` — "tabs" mistranslated as "contraseñas", duplicating the word and dropping "pestañas".
    - Current: `Inicia sesión para sincronizar contraseñas, marcadores, contraseñas y más.`
    - Source: `Sign in to sync tabs, bookmarks, passwords, and more.`
    - Suggest: `Inicia sesión para sincronizar pestañas, marcadores, contraseñas y más.`
    - Source lists "tabs, bookmarks, passwords, and more"; the target lists "contraseñas" twice and never mentions tabs.
- `Settings.Passwords.OnboardingMessage.v103` — `es-MX/firefox-ios.xliff` — "or" translated as "y", changing alternatives into a requirement of all three.
    - Current: `protegidas por Face ID, Touch ID y código de acceso en el dispositivo`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `protegidas por Face ID, Touch ID o el código de acceso del dispositivo`
    - Source says "Face ID, Touch ID or a device passcode" (alternatives), not a conjunction of all.
- `Settings.SaveLogins.Title` — `es-MX/firefox-ios.xliff` — "Save Logins" (an action/setting to enable saving) rendered as "Inicios de sesión guardados" (saved logins).
    - Current: `Inicios de sesión guardados`
    - Source: `Save Logins`
    - Suggest: `Guardar inicios de sesión`
    - Developer comment says it is the setting to enable the built-in password manager; the source is a verb phrase, not a noun label for existing items.
- `Settings.Search.Done.Button` — `es-MX/firefox-ios.xliff` — "Done" translated as "Cerrar" (Close).
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source button is "Done", the standard iOS label rendered "Listo" in es-MX; "Cerrar" means "Close".
- `Settings.OfferClipboardBar.Status` — `es-MX/firefox-ios.xliff` — "When Opening Firefox" rendered with an odd progressive construction.
    - Current: `Cuando esté abriendo Firefox`
    - Source: `When Opening Firefox`
    - Suggest: `Al abrir Firefox`
    - The source is a simple temporal phrase; the parallel string Settings.OfferClipboardBar.Status.v128 uses "Al abrir %@".
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `es-MX/firefox-ios.xliff` — "ad tracking" is rendered simply as "publicidad", dropping the tracking aspect.
    - Current: `Permitir algo de publicidad para que los sitios web funcionen adecuadamente.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Permite cierto rastreo publicitario para que los sitios web funcionen correctamente.`
    - The en-US says it allows some ad tracking, not some advertising; the meaning of the protection setting is changed. Also the source is descriptive ("Allows"), not an imperative.
- `Settings.WebsiteData.SelectedConfirmPrompt` — `es-MX/firefox-ios.xliff` — Adds "todos" which is not in the source: it clears the selected items, not all of them.
    - Current: `Esta acción eliminará todos los elementos seleccionados.`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `Esta acción eliminará los elementos seleccionados.`
    - en-US: "This action will clear the selected items." The added "todos" overstates the scope of the deletion.
- `TabTray.Title` — `es-MX/firefox-ios.xliff` — "Open Tabs" (a title listing currently open tabs) is translated as the imperative "Abrir pestañas" ("Open tabs" as an action).
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - Developer comment says it is the title for the tab tray, i.e. the noun phrase "Open Tabs" = tabs that are open, not a command to open tabs.
- `TopSites.RemovePage.Button` — `es-MX/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The source uses an em dash and the locale convention is the em dash; a plain hyphen deviates.
- `Wallpaper.Download.Error.Title.v106` — `es-MX/firefox-ios.xliff` — Download error title translated as "could not change wallpaper" instead of "could not download wallpaper".
    - Current: `No se pudo cambiar el fondo de pantalla`
    - Source: `Couldn’t Download Wallpaper`
    - Suggest: `No se pudo descargar el fondo de pantalla`
    - Source is "Couldn’t Download Wallpaper"; the target duplicates the Change error title and loses the download meaning.
- `read` — `es-MX/firefox-ios.xliff` — Past participle "read" translated as the infinitive verb "leer".
    - Current: `leer`
    - Source: `read`
    - Suggest: `leído`
    - The developer comment states it is a past participle functioning as an adjective (accessibility label for a read article), matching the counterpart "unread" → "no leído".
- `You don’t have any tabs open in Firefox on your other devices.` — `es-MX/firefox-ios.xliff` — Translation says "no other tabs open" instead of "you don't have any tabs open".
    - Current: `No hay otras pestañas abiertas de Firefox en tus otros dispositivos.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `No tienes ninguna pestaña abierta en Firefox en tus otros dispositivos.`
    - The source states the user has no tabs open at all on other devices; "otras pestañas" implies there are some tabs but no others.
- `Search Input Field` — `es-MX/firefox-ios.xliff` — "Search Input Field" (a noun phrase naming the field) is rendered as an imperative "Buscar campo de entrada" ("Search the input field").
    - Current: `Buscar campo de entrada`
    - Source: `Search Input Field`
    - Suggest: `Campo de búsqueda`
    - The developer comment says this is the accessibility label for the search input field; the Spanish turns the noun phrase into a command to search a field.
- `Off` — `es-MX/firefox-ios.xliff` — Accessibility value "Off" is translated as the verb "Apagar" (turn off) instead of the state "Desactivado".
    - Current: `Apagar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The comment says it is a toggled-OFF accessibility value, i.e. a state, and the paired "On" string is correctly rendered as the state "Activado".
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `es-MX/firefox-ios.xliff` — The translation adds "de esta sesión" and drops "any of your", altering the scope of what Firefox will not remember.
    - Current: `Firefox no recordará el historial ni las cookies de esta sesión, pero guardará marcadores que agregues.`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox no recordará nada de tu historial ni tus cookies, pero se guardarán los marcadores nuevos.`
    - The en-US says Firefox won’t remember any of your history or cookies and that new bookmarks will be saved; the Spanish limits it to "de esta sesión", a claim the source never makes.
- `Alerts.AddToCalendar.BodyDefault.v134` — `es-MX/firefox-ios.xliff` — Misspelling of "agregar".
    - Current: `agrear`
    - Source: `This site is asking to download a file and add an event to your calendar.`
    - Suggest: `agregar`
    - The source says "add an event"; the Spanish verb is misspelled as "agrear" instead of "agregar" (correct in the sibling string Alerts.AddToCalendar.Body.v134).
- `Alerts.RestoreTabs.Title.v109.v2` — `es-MX/firefox-ios.xliff` — Missing accent on the preterite verb "falló".
    - Current: `%@ fallo.`
    - Source: `%@ crashed. Restore your tabs?`
    - Suggest: `%@ falló.`
    - Source "%@ crashed" requires the past-tense verb "falló"; without the accent "fallo" is the noun "failure"/present tense.
- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-MX/firefox-ios.xliff` — Ampersand kept instead of Spanish conjunction "y".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the English "&" should be rendered as "y"; the accessibility label would be read aloud incorrectly.
- `Bookmarks.EmptyState.Root.ButtonTitle.v136` — `es-MX/firefox-ios.xliff` — "Sign in to Sync" uses "Sync" as a verb, but the translation treats it as a product name/destination.
    - Current: `Inicia sesión en Sync`
    - Source: `Sign in to Sync`
    - Suggest: `Inicia sesión para sincronizar`
    - The developer comment explicitly states that "Sync" is used as a verb (capitalized per iOS title-case convention), so the meaning is "sign in in order to sync", not "sign in to [the] Sync [service]".
- `Bookmarks.EmptyState.Nested.Body.v135` — `es-MX/firefox-ios.xliff` — Infinitive "Agregar" used instead of the imperative required by the source instruction.
    - Current: `Agregar marcadores mientras navegas`
    - Source: `Add bookmarks as you browse so you can find your favorite sites later.`
    - Suggest: `Agrega marcadores mientras navegas`
    - The en-US "Add bookmarks as you browse" is an imperative addressed to the user; the rest of the sentence uses informal second person ("navegas", "puedas"), so the infinitive is inconsistent and ungrammatical here.
- `Bookmarks.EmptyState.Root.Body.v135` — `es-MX/firefox-ios.xliff` — "We’ll also grab bookmarks from other synced devices" rendered as "we will show you" instead of fetching/importing them.
    - Current: `También te mostraremos los marcadores de tus otros dispositivos sincronizados`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `También tomaremos los marcadores de tus otros dispositivos sincronizados`
    - The source says Firefox will grab (retrieve) bookmarks from other synced devices, not merely display them.
- `Bookmarks.DeleteFolderWarning.Description` — `es-MX/firefox-ios.xliff` — Missing preposition "de" after "estás seguro".
    - Current: `¿Estás seguro que quieres eliminarlo`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Estás seguro de que quieres eliminarlo`
    - Standard Spanish requires "seguro de que"; the omission (queísmo) is a grammatical error.
- `ContextualHints.Translations.Body.v145` — `es-MX/firefox-ios.xliff` — Missing accent on the pronoun "tú".
    - Current: `cuando tu lo estés`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `cuando tú lo estés`
    - "tu" is the possessive adjective; the stressed subject pronoun requires the accent: "tú".
- `Bookmarks.Menu.DeleteBookmark.v132` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Marcador", inconsistent with other bookmark strings in the same file.
    - Current: `Eliminar Marcador`
    - Source: `Delete Bookmark`
    - Suggest: `Eliminar marcador`
    - Spanish uses sentence case; sibling strings render "Editar marcador" and "Eliminar carpeta" in lowercase.
- _…and 62 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (110)

- `NSFaceIDUsageDescription` — `Client/en.lproj/InfoPlist.strings` — Malformed parenthetical dashes with missing spacing around the inserted gloss.
    - Current: `Face ID - reconocimiento facial-para acceder`
    - Suggest: `Face ID (reconocimiento facial) para acceder`
    - The dash pair is unbalanced and there is no space before "para", producing broken typography not present in the en-US source.
- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `Shared/Supporting Files/en.lproj/AddressToolbar.strings` — Ampersand kept instead of the Spanish conjunction "y".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Suggest: `Ajustes de privacidad y seguridad`
    - Spanish does not use "&" as a conjunction in UI labels; the en-US "&" should be rendered as "y".
- `Alerts.AddToCalendar.BodyDefault.v134` — `Shared/Supporting Files/en.lproj/Alerts.strings` — Misspelling of "agregar" as "agrear".
    - Current: `agrear un evento`
    - Suggest: `agregar un evento`
    - "agrear" is not a Spanish word; the source says "add an event", which is "agregar un evento" (as correctly used in the sibling string Alerts.AddToCalendar.Body.v134).
- `Alerts.RestoreTabs.Title.v109.v2` — `Shared/Supporting Files/en.lproj/Alerts.strings` — Missing accent in the verb "falló".
    - Current: `%@ fallo.`
    - Suggest: `%@ falló.`
    - The source "%@ crashed" is past tense; without the accent "fallo" is a noun, not the verb form.
- `Biometry.Screen.UniversalAuthenticationReason.v115` — `Shared/Supporting Files/en.lproj/BiometricAuthentication.strings` — Impersonal infinitive "Autenticarse" conflicts with the second-person imperative used in the parallel v122 string.
    - Current: `Autenticarse para acceder a las contraseñas.`
    - Suggest: `Autentícate para acceder a las contraseñas.`
    - The same source pattern is translated as "Autentícate..." in Biometry.Screen.UniversalAuthenticationReason.v122; the register should be consistent within the file.
- `Bookmarks.DeleteFolderWarning.Description` — `Shared/Supporting Files/en.lproj/BookmarkPanelDeleteConfirm.strings` — Missing preposition "de" after "seguro" (queísmo).
    - Current: `¿Estás seguro que quieres eliminarlo`
    - Suggest: `¿Estás seguro de que quieres eliminarlo`
    - Standard Spanish requires "estar seguro de que"; omitting "de" is queísmo.
- `Bookmarks.EmptyState.Nested.Body.v135` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — Infinitive "Agregar" used instead of the imperative required by the source instruction "Add bookmarks as you browse".
    - Current: `Agregar marcadores mientras navegas`
    - Suggest: `Agrega marcadores mientras navegas`
    - The en-US is an imperative addressed to the user; the rest of the sentence uses second person ("navegas", "puedas"), so the infinitive is inconsistent and ungrammatical.
- `Bookmarks.EmptyState.Root.Body.v135` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — "We’ll also grab bookmarks from other synced devices" rendered as "we'll also show you", changing the meaning of importing/fetching bookmarks.
    - Current: `También te mostraremos los marcadores de tus otros dispositivos sincronizados.`
    - Suggest: `También traeremos los marcadores de tus otros dispositivos sincronizados.`
    - The source says the browser will grab/retrieve the bookmarks, not merely display them.
- `Bookmarks.Menu.DeleteBookmark.v132` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — Unnecessary capitalization of "Marcador" in mid-sentence, inconsistent with other entries like "Eliminar carpeta" and "Editar marcador".
    - Current: `Eliminar Marcador`
    - Suggest: `Eliminar marcador`
    - Spanish does not use English title case; sibling strings in the same file use "Eliminar carpeta" and "Editar marcador".
- `ContextualHints.Translations.Body.v145` — `Shared/Supporting Files/en.lproj/ContextualHints.strings` — Missing accent on the pronoun "tú".
    - Current: `cuando tu lo estés`
    - Suggest: `cuando tú lo estés`
    - Here "tú" is the subject pronoun and requires the written accent; "tu" is the possessive.
- `CredentialProvider.RetryAllert.Message.v137` — `Shared/Supporting Files/en.lproj/CredentialProvider.strings` — Past tense "There was an issue" rendered as present tense.
    - Current: `Hay un problema con el autocompletado.`
    - Suggest: `Hubo un problema con el autocompletado.`
    - The source reports a problem that already occurred; the present tense changes the meaning.
- `Settings.Home.Option.ThoughtProvokingStories.subtitle.v116` — `Shared/Supporting Files/en.lproj/CustomizeFirefoxHome.strings` — "powered by" mistranslated as "desarrollados por" (developed by).
    - Current: `Artículos desarrollados por %@`
    - Suggest: `Artículos proporcionados por %@`
    - The source means the articles are provided/powered by Pocket, not developed by it.
- `CreditCard.EditCard.CardNumberTitle.v112` — `Shared/Supporting Files/en.lproj/EditCard.strings` — "Card Number" is translated as "credit card number", adding information not in the source.
    - Current: `Número de tarjeta de crédito`
    - Suggest: `Número de tarjeta`
    - The en-US source is simply "Card Number"; the label should not specify "de crédito", especially as the sibling string "Add Card" is rendered "Agregar tarjeta".
- `Menu.EnhancedTrackingProtection.SwitchOff.Text.v129` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Protections are OFF" was translated as "Protección de navegación DESACTIVADA", inventing "browsing protection" and changing plural protections to singular.
    - Current: `Protección de navegación DESACTIVADA. Te sugerimos reactivarla.`
    - Suggest: `Las protecciones están DESACTIVADAS. Te sugerimos volver a activarlas.`
    - The source says "Protections are OFF. We suggest turning them back on." with no mention of "navegación"; other strings in the same screen render "protections" as "las protecciones".
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `Shared/Supporting Files/en.lproj/FirefoxHomepage.strings` — "Website URL" is rendered as "Enlace del sitio web" (website link) instead of URL.
    - Current: `Enlace del sitio web`
    - Suggest: `URL del sitio web`
    - The source says URL, and the sibling error string uses "URL" ("Ingresa una URL válida"); "Enlace" changes the term and is inconsistent within the same alert.
- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `Shared/Supporting Files/en.lproj/FirefoxHomepage.strings` — "You’re Protected" is translated as "Protección de navegación activada" (browsing protection enabled), which states something different.
    - Current: `Protección de navegación activada`
    - Suggest: `Estás protegido`
    - The source is a statement about the user being protected, not about a setting being enabled.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `Shared/Supporting Files/en.lproj/JumpBackIn.strings` — Missing accent in the imperative "Continua".
    - Current: `Continua donde te quedaste`
    - Suggest: `Continúa donde te quedaste`
    - The imperative of "continuar" is "continúa" with an accent; "continua" is the adjective.
- `LibraryPanel.Sections.LastSevenDays.v138` — `Shared/Supporting Files/en.lproj/LibraryPanel.strings` — "Last 7 Days" uses a different pattern than the sibling section titles.
    - Current: `Los últimos 7 días`
    - Suggest: `Últimos 7 días`
    - The neighboring sections on the same screen are "Últimas 4 semanas" and "Últimas 24 horas" without the article; the added "Los" is inconsistent.
- `MainMenu.DesktopSiteOff.Title.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — State label "Off" translated as the imperative action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Suggest: `Desactivado`
    - The developer comment says this is a label indicating that the Desktop Site option is OFF, i.e. a state, not an action to turn it off.
- `MainMenu.DesktopSiteOn.Title.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — State label "On" translated as the imperative action "Activar" instead of the state "Activado".
    - Current: `Activar`
    - Suggest: `Activado`
    - The developer comment says this is a label indicating that the Desktop Site option is ON, i.e. a state, not an action to enable it.
- `MainMenu.HeaderBanner.Subtitle.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — Subtitle mistranslated and expanded: "Takes seconds. Change anytime." became "Toma solo un segundo y puedes cambiar tus preferencias cuando quieras."
    - Current: `Toma solo un segundo y puedes cambiar tus preferencias cuando quieras.`
    - Suggest: `Toma unos segundos. Cámbialo cuando quieras.`
    - The source says it takes seconds (plural) and is two short sentences for a banner; the translation says "only one second" and adds "tus preferencias", making it much longer than the source in a space-constrained banner.
- `MainMenu.SiteProtection.ProtectionsOff.Title.v141` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Protections" is translated as "Protección de navegación" here while the sibling badge string uses "Protecciones".
    - Current: `Protección de navegación DESACTIVADA`
    - Suggest: `Protecciones DESACTIVADAS`
    - The en-US source is "Protections are OFF"; MainMenu.SiteProtection.Protections.Title.v153 on the same screen renders "Protections" as "Protecciones", so the term should be consistent and not expanded to "Protección de navegación".
- `MainMenu.SiteProtection.ProtectionsOn.Title.v141` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Protections" is translated as "Protección de navegación" here while the sibling badge string uses "Protecciones".
    - Current: `Protección de navegación ACTIVADA`
    - Suggest: `Protecciones ACTIVADAS`
    - The en-US source is "Protections are ON"; MainMenu.SiteProtection.Protections.Title.v153 on the same screen renders "Protections" as "Protecciones", so the term should be consistent and not expanded to "Protección de navegación".
- `MainMenu.Submenus.Save.AddToShortcuts.Subtitle.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Shortcut" is rendered as "Atajo" here but as "Acceso directo" in the parallel accessibility-label string and in the related Add/Remove from Shortcuts items.
    - Current: `Atajo`
    - Suggest: `Acceso directo`
    - MainMenu.Submenus.Save.AccessibilityLabels.AddToShortcuts.Subtitle.v132 has the identical source "Shortcut" translated as "Acceso directo", and the surrounding Shortcuts strings use "accesos directos"; the same term on the same screen must be consistent.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reader View" is rendered as "vista de lector" here but as "vista de lectura" in the sibling On/Subtitle strings on the same menu.
    - Current: `Desactivar la vista de lector`
    - Suggest: `Desactivar la vista de lectura`
    - MainMenu.Submenus.Tools.ReaderView.On.Title.v131 and .Subtitle.v131 both use "vista de lectura" for the same source term "Reader View"; this inconsistency appears on the same submenu.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Switch to mobile site" is rendered as "Cambiar el sitio móvil" (change the mobile site) instead of "Cambiar al sitio móvil".
    - Current: `Cambiar el sitio móvil`
    - Suggest: `Cambiar al sitio móvil`
    - The source means switching to the mobile version; the missing "a" changes the meaning and is inconsistent with MainMenu.ToolsSection.SwitchToMobileSite.Title.v131 ("Cambiar al sitio móvil").
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Tools submenu" is translated as "Herramientas del submenú" (submenu's tools), reversing the relationship.
    - Current: `Herramientas del submenú`
    - Suggest: `Submenú Herramientas`
    - The source names the submenu called "Tools"; the translation says "tools of the submenu", which is a different meaning.
- `MainMenu.ToolsSection.ReaderViewOff.Title.v150` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — State label "Off" is translated as the imperative action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Suggest: `Desactivado`
    - The developer comment says this label indicates that Reader view is turned off (a state), not a command to turn it off.
- `MainMenu.ToolsSection.ReaderViewOn.Title.v150` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — State label "On" is translated as the imperative action "Activar" instead of the state "Activado".
    - Current: `Activar`
    - Suggest: `Activado`
    - The developer comment says this label indicates that Reader view is turned on (a state), not a command.
- `MainMenu.ToolsSection.Translation.Off.v151` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — Badge "Off" showing translation is inactive is translated as the action "Desactivar".
    - Current: `Desactivar`
    - Suggest: `Desactivado`
    - The comment describes a badge indicating the inactive state, not an action to turn translation off.
- `MainMenu.ToolsSection.Translation.Translated.Title.v151` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Translated…" is rendered as "Traducción finalizada…" (translation finished), not matching the source and inconsistent with the v145 string.
    - Current: `Traducción finalizada…`
    - Suggest: `Traducido…`
    - The source is the state label "Translated", already translated elsewhere as "Traducido"; "Traducción finalizada" adds a different meaning.
- `MainMenu.WebsiteDarkModeOffV2.Title.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — Label indicating Website Dark Mode is OFF is translated as the action "Desactivar".
    - Current: `Desactivar`
    - Suggest: `Desactivado`
    - The comment states this label indicates the option is OFF (a state), not an action.
- `MainMenu.WebsiteDarkModeOnV2.Title.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — Label indicating Website Dark Mode is ON is translated as the action "Activar".
    - Current: `Activar`
    - Suggest: `Activado`
    - The comment states this label indicates the option is ON (a state), not an action.
- `NativeErrorPage.Wayback.Error.Title.v154` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — "Unable to connect" is rendered as "Error de conexión" (connection error) instead of the inability to connect.
    - Current: `Error de conexión`
    - Suggest: `No se puede conectar`
    - The source states the app is unable to connect; "Error de conexión" changes the message to a generic connection error rather than the state described in en-US.
- `DefaultBrowserPopup.SecondLabel.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Unnecessary capitalization of "Predeterminado" in the middle of the phrase.
    - Current: `2. Presiona *Navegador Predeterminado*`
    - Suggest: `2. Presiona *Navegador predeterminado*`
    - Spanish does not capitalize adjectives in a phrase; only the first word is capitalized (matching the iOS setting label style used elsewhere, e.g. "tu predeterminado").
- `Onboarding.Customization.Theme.Continue.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Unnecessary capitalization of 'Continuar' mid-sentence; Spanish uses sentence case.
    - Current: `Guardar y Continuar`
    - Suggest: `Guardar y continuar`
    - Spanish does not use English title case; the parallel string Onboarding.Customization.Toolbar.Continue.Action.v123 correctly reads 'Guardar y comenzar a navegar'.
- `Onboarding.Customization.Theme.System.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Title-case capitalization of the second word does not follow Spanish sentence case.
    - Current: `Sistema Automático`
    - Suggest: `Sistema automático`
    - Spanish uses sentence case for UI labels; 'Automático' should be lowercase here.
- `Onboarding.Customization.Toolbar.Description.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Uses the formal 'usted' form while the rest of the onboarding screen uses informal 'tú'.
    - Current: `Mantenga las búsquedas al alcance.`
    - Suggest: `Mantén las búsquedas al alcance.`
    - Surrounding onboarding strings address the user informally (Elige, Configura, Guarda), so the formal imperative is an inconsistent register.
- `Onboarding.Customization.Toolbar.Title.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Uses the formal 'usted' imperative 'Elija' while parallel strings use informal 'Elige'.
    - Current: `Elija una ubicación para la barra de herramientas`
    - Suggest: `Elige una ubicación para la barra de herramientas`
    - Onboarding.Customization.Theme.Title.v123 uses 'Elige un tema'; mixing formal and informal address on the same flow is inconsistent register.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The two placeholders are swapped: %1$@ (app name) and %2$@ (company name) are used in the wrong positions.
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas.`
    - Per the comment, %1$@ is the app name (Firefox) and %2$@ is the company name (Mozilla). The source says share with Mozilla's marketing partners how you discovered Firefox; the translation says share with Firefox's marketing partners how you discovered Mozilla.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "won’t sell you out" is rendered as "confiable", dropping the meaning that the browser will not betray/sell out the user.
    - Current: `Rápido, seguro y confiable.`
    - Suggest: `Rápido, seguro y no te traiciona.`
    - The en-US states the browser will not sell the user out (privacy claim); "confiable" (trustworthy) is a generic substitution that loses the source's meaning.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Subjunctive "espíen" turns the relative clause restrictive/hypothetical, changing the meaning of "block companies from spying on your clicks".
    - Current: `bloqueamos automáticamente a las empresas que espíen tus clics`
    - Suggest: `impedimos automáticamente que las empresas espíen tus clics`
    - The source says we block companies from spying on your clicks, not that we block those companies that (may) spy.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Top" is rendered as "Arriba" while the parallel option "Bottom" is "Inferior", and the v140 pair uses Superior/Inferior.
    - Current: `Arriba`
    - Suggest: `Superior`
    - Same source term on the same toolbar-customization screen is translated inconsistently with its paired option (Inferior) and with Onboarding.Modern.Customization.Toolbar.Top.Action.v140 (Superior).
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Suggest: `para todos`
    - The en-US says features improve "for everyone"; the translation invents a geographic scope ("all over the world").
- `Onboarding.Modern.Welcome.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The v145 welcome description drops the second-person address used throughout the onboarding flow and in the identical v140 string.
    - Current: `Una sola elección brinda protección en toda la web. Es posible cambiarla en cualquier momento.`
    - Suggest: `Una sola elección te protege donde sea que navegues en la web. Siempre puedes cambiarla más tarde.`
    - Source is "One choice protects you everywhere you go on the web. You can always change it later." — the "you" is dropped, breaking the tú register used in every other onboarding string (e.g. "te protege", "puedes cambiarla" in the identical v140 source).
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is mistranslated as "para los usuarios en todo el mundo" (for users all over the world).
    - Current: `para los usuarios en todo el mundo`
    - Suggest: `para todos`
    - The source says the data helps improve features, performance and stability "for everyone"; the translation adds a geographic claim not present in the en-US.
- `PrivacyDashboard.Fingerprinters.v155` — `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — "Fingerprinters" is rendered as "Rastreadores de huella digital", conflating it with trackers; Firefox's established Spanish term is "Detectores de huellas digitales".
    - Current: `Rastreadores de huella digital`
    - Suggest: `Detectores de huellas digitales`
    - The Privacy Dashboard lists trackers and fingerprinters as separate categories; using "Rastreadores" (trackers) for fingerprinters creates terminology collision with the tracker bar on the same screen.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `Shared/Supporting Files/en.lproj/RelayMask.strings` — "email masks" translated as "plantillas para correos electrónicos" (templates) instead of "máscaras de correo electrónico" used everywhere else in the file.
    - Current: `Ya has usado tus 5 plantillas gratuitas para correos electrónicos`
    - Suggest: `Ya has usado tus 5 máscaras de correo electrónico gratuitas`
    - The source says "5 free email masks"; "plantillas" means templates and is inconsistent with the term "máscaras de correo electrónico" used in all other RelayMask strings.
- `UnifiedSearch.SearchEngineSelection.SearchSettings.Title.v133` — `Shared/Supporting Files/en.lproj/SearchEngineSelection.strings` — "Search Settings" rendered as "Configuración de búsqueda" while the accessibility label for the same row uses "Ajustes de búsqueda".
    - Current: `Configuración de búsqueda`
    - Suggest: `Ajustes de búsqueda`
    - Same control on the same sheet has two different renderings of "Search settings" (label vs. visible title), an inconsistency within the screen.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `Shared/Supporting Files/en.lproj/SearchZero.strings` — "Trending Searches" translated inconsistently with the section title on the same feature.
    - Current: `Mostrar tendencias de búsquedas`
    - Suggest: `Mostrar búsquedas en tendencia`
    - SearchZero.TrendingSearches.SectionTitle uses "Tendencias"; here "tendencias de búsquedas" shifts the meaning to trends of searches rather than the searches that are trending, and is inconsistent within the same feature.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — The status label "Blocked" is rendered as a past-tense verb phrase instead of matching the status term used elsewhere.
    - Current: `**Se bloqueó**`
    - Suggest: `**Bloqueada**`
    - The bolded word is the status name defined in Settings.AIControls.AIPoweredFeaturesSection.BlockedStatus.v151 as "Bloqueada"; "Se bloqueó" states an event occurred rather than naming the status, breaking consistency on the same screen.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — Number agreement error between demonstrative and noun.
    - Current: `Si bloqueas estas funcionalidad`
    - Suggest: `Si bloqueas esta funcionalidad`
    - "estas" (plural) does not agree with the singular noun "funcionalidad".
- `Settings.AIControls.BlockedInformation.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "especificas" is missing its accent mark.
    - Current: `funciones especificas`
    - Suggest: `funciones específicas`
    - The Spanish adjective is "específicas" with an accent on the second syllable; "especificas" is a misspelling (or a different verb form).
- `Settings.Browsing.AdBlocker.Description.v155` — `Shared/Supporting Files/en.lproj/Settings.strings` — "funcionalidad" is repeated in the same sentence, and the second use mistranslates "turning this off".
    - Current: `Si tienes problemas de funcionalidad en algún sitio, intenta desactivar esta funcionalidad.`
    - Suggest: `Si algún sitio parece no funcionar bien, intenta desactivar esta opción.`
    - The source says "If a site looks broken, try turning this off" — referring to the toggle, not a "funcionalidad"; the duplicated term is a clumsy repetition that degrades the text.
- `Settings.Notifications.SyncNotificationsTitle.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — The setting title "Sync" (a noun naming the feature) is rendered as the verb "Sincronizar".
    - Current: `Sincronizar`
    - Suggest: `Sincronización`
    - The comment says it is the title of the Sync-related notifications setting, i.e. the feature name Sync, not an action.
- `Settings.Studies.Message.v148` — `Shared/Supporting Files/en.lproj/Settings.strings` — "randomly selects users" is translated without the object "users", losing the meaning.
    - Current: `realiza selecciones aleatorias para probar funciones`
    - Suggest: `selecciona usuarios al azar para probar funciones`
    - The source states that the app randomly selects users to test features; the translation omits who is selected.
- `Settings.Summarize.FooterTitle.v142` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Provides access" rendered as "Habilita el acceso" (enables access).
    - Current: `Habilita el acceso a la funcionalidad para resumir páginas.`
    - Suggest: `Brinda acceso a la función de resumir páginas.`
    - The source states the setting provides access to summarizing pages; "habilita" changes the meaning to enabling.
- `Settings.Translation.SettingOff.v145` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Off" is a state label but was translated as the imperative verb "Desactivar" (Turn off).
    - Current: `Desactivar`
    - Suggest: `Desactivado`
    - The comment says this text indicates the translation feature has been disabled — a status, not an action.
- `Settings.Translation.SettingOn.v145` — `Shared/Supporting Files/en.lproj/Settings.strings` — "On" is a state label but was translated as the imperative verb "Activar" (Turn on).
    - Current: `Activar`
    - Suggest: `Activado`
    - The comment says this text indicates the translation feature has been enabled — a status, not an action.
- `CloseTabsToast.SingleTabTitle.v113` — `Shared/Supporting Files/en.lproj/TabsTray.strings` — Incorrect capitalization of the adjective in mid-sentence; Spanish does not use title case.
    - Current: `Pestaña Cerrada`
    - Suggest: `Pestaña cerrada`
    - Spanish sentence case applies; the parallel string CloseTabsToast.Title.v113 correctly uses "Pestañas cerradas".
- _…and 50 more._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 95 |
| Strings | 1,883 |
| Missing strings | 39 |
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

**39 strings** are not translated yet, concentrated in:

- `es-MX/firefox-ios.xliff` — 18
- `es-MX/firefox-ios.xliff` — 8
- `es-MX/firefox-ios.xliff` — 8
- `Shared/Supporting Files/en-US.lproj/GoogleLens.strings` — 2
- `es-MX/firefox-ios.xliff` — 2
- `es-MX/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/GoogleLens.strings`

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
| register | `informal` 150, `formal` 5 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (126)

> **Reads as a deliberate edit (5).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `es-MX/firefox-ios.xliff` — "You’re Protected" is translated as "Protección de navegación activada" (Browsing protection enabled), which states something different from the source.
    - Current: `Protección de navegación activada`
    - Source: `You’re Protected`
    - Suggest: `Estás protegido`
    - The en-US tells the user they are protected; the Spanish asserts that a browsing-protection feature has been turned on, which is a different claim about the product's state.
- `MainMenu.HeaderBanner.Subtitle.v142` — `es-MX/firefox-ios.xliff` — Subtitle adds content not in the source and changes "Takes seconds" to "takes only a second" plus invented "change your preferences".
    - Current: `Toma solo un segundo y puedes cambiar tus preferencias cuando quieras.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Toma solo unos segundos. Cámbialo cuando quieras.`
    - en-US is "Takes seconds. Change anytime." — the Spanish claims it takes only one second and refers to changing "tus preferencias", asserting something the source never said; it is also much longer for a banner subtitle.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-MX/firefox-ios.xliff` — Relative clause with subjunctive changes the meaning from blocking all companies from spying to only blocking those that do spy.
    - Current: `bloqueamos automáticamente a las empresas que espíen tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - The en-US says the app blocks companies from spying on your clicks; the Spanish says it blocks the companies that spy on your clicks, altering the claim about the product's behaviour.
- `TermsOfUse.Description.v142` — `es-MX/firefox-ios.xliff` — "We've introduced a %@ Terms of Use" is rendered as "we have updated" the Terms of Use, changing new terms into updated terms.
    - Current: `Hemos actualizado los Términos de uso de %@ y nuestro Aviso de privacidad.`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Presentamos los Términos de uso de %@ y actualizamos nuestro Aviso de privacidad.`
    - The source says the Terms of Use are newly introduced, while only the Privacy Notice was updated; the translation says both were updated.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `es-MX/firefox-ios.xliff` — The translation adds "de esta sesión" and drops "any of your", altering the scope of what Firefox will not remember.
    - Current: `Firefox no recordará el historial ni las cookies de esta sesión, pero guardará marcadores que agregues.`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox no recordará nada de tu historial ni tus cookies, pero se guardarán los marcadores nuevos.`
    - The en-US says Firefox won’t remember any of your history or cookies and that new bookmarks will be saved; the Spanish limits it to "de esta sesión", a claim the source never makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 68 |
| 3 | Degraded language (grammar, spelling, terminology) | 49 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `es-MX/firefox-ios.xliff` — Placeholders swapped: the app name (%1$@) is presented as the owner of the marketing partners and the company name (%2$@) as the discovered app.
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas.`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas.`
    - Per the comment, %1$@ is the app name (Firefox) and %2$@ is the company name (Mozilla); the source says share with Mozilla's marketing partners how you discovered Firefox. The translation reverses them, attributing the marketing partners to Firefox and saying you discovered Mozilla.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.EmptyState.Root.Body.v135` — `es-MX/firefox-ios.xliff` — "We’ll also grab bookmarks from other synced devices" rendered as "we will show you" instead of fetching/importing them.
    - Current: `También te mostraremos los marcadores de tus otros dispositivos sincronizados`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `También tomaremos los marcadores de tus otros dispositivos sincronizados`
    - The source says Firefox will grab (retrieve) bookmarks from other synced devices, not merely display them.
- `Bookmarks.EmptyState.Root.ButtonTitle.v136` — `es-MX/firefox-ios.xliff` — "Sign in to Sync" uses "Sync" as a verb, but the translation treats it as a product name/destination.
    - Current: `Inicia sesión en Sync`
    - Source: `Sign in to Sync`
    - Suggest: `Inicia sesión para sincronizar`
    - The developer comment explicitly states that "Sync" is used as a verb (capitalized per iOS title-case convention), so the meaning is "sign in in order to sync", not "sign in to [the] Sync [service]".
- `Bookmarks.Menu.AllBookmarks.v131` — `es-MX/firefox-ios.xliff` — "All" (referring to all bookmarks) rendered as the neuter "Todo" instead of the plural agreeing with "marcadores".
    - Current: `Todo`
    - Source: `All`
    - Suggest: `Todos`
    - Per the comment, the back button label means "All (bookmarks)"; "Todo" reads as "everything" rather than all bookmarks.
- `CredentialProvider.RetryAllert.Message.v137` — `es-MX/firefox-ios.xliff` — Present tense "Hay un problema" instead of the source's past "There was an issue".
    - Current: `Hay un problema con el autocompletado.`
    - Source: `There was an issue with autofill. Please try again.`
    - Suggest: `Hubo un problema con el autocompletado.`
    - The source reports a problem that already occurred; the Spanish states an ongoing problem.
- `Settings.Home.Option.ThoughtProvokingStories.subtitle.v116` — `es-MX/firefox-ios.xliff` — "Articles powered by Pocket" is rendered as "Artículos desarrollados por" (articles developed by), changing the meaning.
    - Current: `Artículos desarrollados por %@`
    - Source: `Articles powered by %@`
    - Suggest: `Artículos ofrecidos por %@`
    - "powered by" means the content is provided/driven by Pocket, not that Pocket develops/creates the articles; the Spanish asserts Pocket authors the articles.
- `CreditCard.EditCard.CardNumberTitle.v112` — `es-MX/firefox-ios.xliff` — "Card Number" is rendered as "Número de tarjeta de crédito", adding "de crédito" which the source does not say.
    - Current: `Número de tarjeta de crédito`
    - Source: `Card Number`
    - Suggest: `Número de tarjeta`
    - The en-US label is simply "Card Number"; other labels in this file use "tarjeta" alone (Agregar tarjeta, Eliminar tarjeta, Ver tarjeta).
- `Menu.EnhancedTrackingProtection.SwitchOff.Text.v129` — `es-MX/firefox-ios.xliff` — "Protections are OFF" translated as "Protección de navegación DESACTIVADA", introducing a term ("navegación") not in the source and inconsistent with "Protección mejorada contra el rastreo" on the same screen.
    - Current: `Protección de navegación DESACTIVADA`
    - Source: `Protections are OFF. We suggest turning them back on.`
    - Suggest: `Las protecciones están DESACTIVADAS`
    - The source refers to the enhanced tracking protections generally; the translation invents a different feature name, inconsistent with the switch title in the same file.
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `es-MX/firefox-ios.xliff` — "Website URL" rendered as "Enlace del sitio web" (website link) instead of URL, inconsistent with the sibling strings that keep "URL".
    - Current: `Enlace del sitio web`
    - Source: `Website URL`
    - Suggest: `URL del sitio web`
    - The source says "Website URL"; the related strings in the same alert use "dirección URL" and "URL válida", so "Enlace" is both a mistranslation and inconsistent terminology on the same screen.
- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `es-MX/firefox-ios.xliff` — "You’re Protected" is translated as "Protección de navegación activada" (Browsing protection enabled), which states something different from the source.
    - Current: `Protección de navegación activada`
    - Source: `You’re Protected`
    - Suggest: `Estás protegido`
    - The en-US tells the user they are protected; the Spanish asserts that a browsing-protection feature has been turned on, which is a different claim about the product's state.
- `MainMenu.Account.SignedOut.Description.v141` — `es-MX/firefox-ios.xliff` — "and more" amplified to "y mucho más", inconsistent with the v131 string's "y más".
    - Current: `Sincronizar marcadores, contraseñas, pestañas y mucho más`
    - Source: `Sync bookmarks, passwords, tabs, and more`
    - Suggest: `Sincronizar marcadores, contraseñas, pestañas y más`
    - en-US is "and more"; the parallel string MainMenu.Account.SignedOut.Description.v131 correctly uses "y más".
- `MainMenu.DesktopSiteOff.Title.v142` — `es-MX/firefox-ios.xliff` — State label "Off" translated as the action "Desactivar" (deactivate) instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this is a label indicating that the Desktop Site option is OFF, i.e. a state, not a command.
- `MainMenu.DesktopSiteOn.Title.v142` — `es-MX/firefox-ios.xliff` — State label "On" translated as the action "Activar" (activate) instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this is a label indicating that the Desktop Site option is ON, i.e. a state, not a command.
- `MainMenu.HeaderBanner.Subtitle.v142` — `es-MX/firefox-ios.xliff` — Subtitle adds content not in the source and changes "Takes seconds" to "takes only a second" plus invented "change your preferences".
    - Current: `Toma solo un segundo y puedes cambiar tus preferencias cuando quieras.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Toma solo unos segundos. Cámbialo cuando quieras.`
    - en-US is "Takes seconds. Change anytime." — the Spanish claims it takes only one second and refers to changing "tus preferencias", asserting something the source never said; it is also much longer for a banner subtitle.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `es-MX/firefox-ios.xliff` — "Save submenu" is translated as the imperative "Guardar submenú" (save the submenu).
    - Current: `Guardar submenú`
    - Source: `Save submenu`
    - Suggest: `Submenú Guardar`
    - The source is a noun phrase naming the Save submenu, not an action of saving a submenu.
- `MainMenu.ToolsSection.AccessibilityLabels.SwitchToMobileSite.v132` — `es-MX/firefox-ios.xliff` — "Switch to mobile site" is rendered as "Cambiar el sitio móvil" (change the mobile site) instead of switching to the mobile site.
    - Current: `Cambiar el sitio móvil`
    - Source: `Switch to mobile site`
    - Suggest: `Cambiar al sitio móvil`
    - The source means switching to the mobile version; the parallel string SwitchToDesktopSite correctly uses "Cambiar al sitio de escritorio".
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `es-MX/firefox-ios.xliff` — "Tools submenu" is translated as "Herramientas del submenú" (submenu's tools) instead of "Submenú Herramientas".
    - Current: `Herramientas del submenú`
    - Source: `Tools submenu`
    - Suggest: `Submenú Herramientas`
    - The label names the Tools submenu; the Spanish reverses the head noun and says "tools of the submenu".
- `MainMenu.ToolsSection.ReaderViewOff.Title.v150` — `es-MX/firefox-ios.xliff` — The state label "Off" is translated as the imperative action "Desactivar" ("Deactivate") instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this is a label indicating that Reader view is turned off, i.e. a state, not an action the user performs.
- `MainMenu.ToolsSection.ReaderViewOn.Title.v150` — `es-MX/firefox-ios.xliff` — The state label "On" is translated as the imperative action "Activar" ("Activate") instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this is a label indicating that Reader view is turned on, i.e. a state, not an action.
- `MainMenu.ToolsSection.Translation.Off.v151` — `es-MX/firefox-ios.xliff` — The badge "Off" is translated as the action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment states this is a badge shown when translation is inactive, a status indicator rather than a command.
- `MainMenu.ToolsSection.Translation.Translated.Title.v151` — `es-MX/firefox-ios.xliff` — "Translated…" is rendered as "Traducción finalizada…" ("Translation finished"), which differs from the source and from the sibling string "Traducido".
    - Current: `Traducción finalizada…`
    - Source: `Translated…`
    - Suggest: `Traducido…`
    - The source is simply "Translated…", a status label indicating the page has been translated; the parallel string v145 is correctly "Traducido". "Traducción finalizada" adds a meaning of completion not in the source and is inconsistent on the same menu.
- `MainMenu.WebsiteDarkModeOffV2.Title.v142` — `es-MX/firefox-ios.xliff` — The status label "Off" for Website Dark Mode is translated as the action "Desactivar" instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says it is a label indicating the Website Dark Mode option is OFF, i.e. a state.
- `MainMenu.WebsiteDarkModeOnV2.Title.v142` — `es-MX/firefox-ios.xliff` — The status label "On" for Website Dark Mode is translated as the action "Activar" instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says it is a label indicating the Website Dark Mode option is ON, i.e. a state.
- `NativeErrorPage.Wayback.Error.Description.v154` — `es-MX/firefox-ios.xliff` — "If other pages won't load" is rendered as an assertion that the user is having trouble loading other pages.
    - Current: `Si tienes problemas al cargar otras páginas`
    - Source: `The site may be busy or unavailable. Try again later. If other pages won’t load, check your Wi-Fi or data connection. %@ can also search the Wayback Machine for an earlier version of this page.`
    - Suggest: `Si otras páginas no cargan`
    - The source conditions on other pages failing to load; the translation is close but shifts the subject. Minor, but the bigger issue is the omission of "also": %@ can *also* search the Wayback Machine.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `es-MX/firefox-ios.xliff` — "won't sell you out" is rendered as the generic "confiable", dropping the claim about not selling users out.
    - Current: `Rápido, seguro y confiable.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Rápido, seguro y nunca te venderá.`
    - The en-US asserts Firefox will not sell the user out (a privacy claim); "confiable" (trustworthy) says something different.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-MX/firefox-ios.xliff` — Relative clause with subjunctive changes the meaning from blocking all companies from spying to only blocking those that do spy.
    - Current: `bloqueamos automáticamente a las empresas que espíen tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - The en-US says the app blocks companies from spying on your clicks; the Spanish says it blocks the companies that spy on your clicks, altering the claim about the product's behaviour.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `es-MX/firefox-ios.xliff` — "your top sites" translated as "sitios favoritos", dropping the possessive and using the term for favorites/bookmarks.
    - Current: `sitios favoritos`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `tus sitios más visitados`
    - en-US "your top sites" refers to most-visited sites; "sitios favoritos" conflicts with the bookmark/favorite terminology used alongside "marcadores" in the same sentence.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `es-MX/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says the data helps improve features "for everyone"; the Spanish states it improves things for users worldwide, which is a different assertion about the product's data use.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-MX/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says "for everyone"; the translation asserts a geographic scope ("users all over the world") the source never stated.
- `CreditCards.Settings.Done.v114` — `es-MX/firefox-ios.xliff` — "Done" translated as "Cerrar" (Close) instead of "Listo".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - en-US "Done" is the standard keyboard-dismiss label, rendered "Listo" in Spanish; "Cerrar" means "Close".
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `es-MX/firefox-ios.xliff` — Status label "Blocked" rendered as a past-tense verb phrase "Se bloqueó", inconsistent with the "Bloqueada" status label used elsewhere.
    - Current: `**Se bloqueó**`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `**Bloqueada**`
    - The bolded term mirrors the status name shown in the UI (Settings.AIControls.AIPoweredFeaturesSection.BlockedStatus.v151 = "Bloqueada"); "Se bloqueó" states an action occurred rather than naming the status.
- `Settings.Browsing.AdBlocker.Description.v155` — `es-MX/firefox-ios.xliff` — "If a site looks broken" is rendered as "Si tienes problemas de funcionalidad en algún sitio" and "turning this off" as "desactivar esta funcionalidad", with awkward repetition of "funcionalidad".
    - Current: `Si tienes problemas de funcionalidad en algún sitio, intenta desactivar esta funcionalidad.`
    - Source: `Reduces ads and ad-related trackers. If a site looks broken, try turning this off.`
    - Suggest: `Si un sitio no se ve bien, intenta desactivar esta opción.`
    - The source describes the site appearing broken and suggests turning off the toggle; the target shifts the meaning and repeats "funcionalidad" for two different referents.
- `Settings.Notifications.SyncNotificationsStatus.v112` — `es-MX/firefox-ios.xliff` — Translation says "to sync tabs" instead of "to receive tabs", and turns the statement into an imperative.
    - Current: `Activa esta opción para sincronizar pestañas y recibir notificaciones cuando inicies sesión en otro dispositivo.`
    - Source: `This must be turned on to receive tabs and get notified when you sign in on another device.`
    - Suggest: `Esta opción debe estar activada para recibir pestañas y recibir notificaciones cuando inicies sesión en otro dispositivo.`
    - The en-US says "This must be turned on to receive tabs"; the Spanish changes "receive tabs" to "sincronizar pestañas" (sync tabs), altering the described behavior.
- `Settings.Search.Suggest.AddressBarSetting.Title.v124` — `es-MX/firefox-ios.xliff` — The brand name "Firefox Suggest" is translated as "Sugerencias de Firefox" while other strings on the same screen keep "Firefox Suggest".
    - Current: `Barra de direcciones - Sugerencias de Firefox`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Barra de direcciones - Firefox Suggest`
    - "Firefox Suggest" is a product name kept untranslated in Settings.Search.Accessibility.LearnAboutSuggestions.v124 and Settings.Search.Suggest.LearnAboutSuggestions.v124 on the same screen.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `es-MX/firefox-ios.xliff` — "Show suggestions from Firefox Suggest" is rendered as "Mostrar Sugerencias de Firefox", translating the brand and dropping "suggestions from".
    - Current: `Mostrar Sugerencias de Firefox en sesiones privadas`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Mostrar sugerencias de Firefox Suggest en sesiones privadas`
    - The source names the Firefox Suggest feature as the source of suggestions; the brand is kept untranslated elsewhere in this file.
- `Settings.Studies.Message.v148` — `es-MX/firefox-ios.xliff` — The translation drops "users", making the app select "selections" randomly rather than randomly selecting users.
    - Current: `%@ realiza selecciones aleatorias para probar funciones`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `%@ selecciona usuarios al azar para probar funciones`
    - en-US says "%@ randomly selects users to test features"; the object "users" is omitted, changing the meaning of what is selected.
- `Settings.Summarize.FooterTitle.v142` — `es-MX/firefox-ios.xliff` — "Provides access" is rendered as "Habilita el acceso" (enables access), adding meaning not in the source.
    - Current: `Habilita el acceso a la funcionalidad para resumir páginas.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Proporciona acceso para resumir páginas.`
    - en-US states the setting provides access to summarize pages; "habilita" and "la funcionalidad" are additions.
- `Settings.Translation.SettingOff.v145` — `es-MX/firefox-ios.xliff` — "Off" (a state label) is translated as the imperative verb "Desactivar" ("Turn off").
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this text indicates the translation feature has been disabled; it is a status, not an action.
- `Settings.Translation.SettingOn.v145` — `es-MX/firefox-ios.xliff` — "On" (a state label) is translated as the imperative verb "Activar" ("Turn on").
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this text indicates the translation feature has been enabled; it is a status, not an action.
- `TermsOfUse.Description.v142` — `es-MX/firefox-ios.xliff` — "We've introduced a %@ Terms of Use" is rendered as "we have updated" the Terms of Use, changing new terms into updated terms.
    - Current: `Hemos actualizado los Términos de uso de %@ y nuestro Aviso de privacidad.`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Presentamos los Términos de uso de %@ y actualizamos nuestro Aviso de privacidad.`
    - The source says the Terms of Use are newly introduced, while only the Privacy Notice was updated; the translation says both were updated.
- `Translations.Sheet.ToLabel.v145` — `es-MX/firefox-ios.xliff` — "To" (target language of translation) is rendered as "Para" instead of "A", inconsistent with the related "Traducir a" strings.
    - Current: `Para`
    - Source: `To`
    - Suggest: `A`
    - The label is the short form of "Translate To", which is translated elsewhere in the same sheet as "Traducir a"; "Para" is the wrong preposition here and breaks consistency with the "De" label pair.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `es-MX/firefox-ios.xliff` — "Captions are missing" is rendered as "subtitles don't load", changing the meaning.
    - Current: `Los subtítulos no cargan`
    - Source: `Captions are missing`
    - Suggest: `Faltan los subtítulos`
    - The source says the captions are missing/absent, not that they fail to load.
- `WebCompatReporter.SubOption.ItemsNotVisible.v154` — `es-MX/firefox-ios.xliff` — "Items not fully visible" translated as "elements partially obstructed", asserting a cause not in the source.
    - Current: `Hay elementos obstruidos parcialmente`
    - Source: `Items not fully visible`
    - Suggest: `Hay elementos que no se ven completamente`
    - The source only states items are not fully visible; "obstruidos" adds an obstruction claim.
- `WebCompatReporter.SubOption.MediaControlsBroken.v154` — `es-MX/firefox-ios.xliff` — "missing" media controls rendered as "no cargan" (do not load).
    - Current: `Los controles multimedia no funcionan o no cargan`
    - Source: `Media controls are broken or missing`
    - Suggest: `Los controles multimedia no funcionan o no aparecen`
    - The source says the controls are broken or missing, not that they fail to load.
- `DefaultBrowserCard.Description` — `es-MX/firefox-ios.xliff` — Translation says links, emails and messages open in Firefox, dropping that it is links from websites, emails and Messages.
    - Current: `Abrir vínculos, correos electrónicos y mensajes automáticamente en Firefox.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Haz que los enlaces de sitios web, correos electrónicos y Mensajes se abran automáticamente en Firefox.`
    - The source sets links coming from websites, emails and Messages to open in Firefox; the target implies the emails and messages themselves open in Firefox.
- `Done` — `es-MX/firefox-ios.xliff` — "Done" is translated as "Cerrar" (Close) instead of "Listo"/"Hecho".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the "Done" button of the Find in Page toolbar; "Cerrar" means "Close", a different label from the en-US "Done".
- `Changes color theme.` — `es-MX/firefox-ios.xliff` — "Changes color theme" is rendered as "changes the theme's color", inverting the noun phrase.
    - Current: `Cambiar el color del tema.`
    - Source: `Changes color theme.`
    - Suggest: `Cambia el tema de color.`
    - The source refers to changing the color theme, not the color of the theme; the accessibility hint should also be third person like the source.
- `Done` — `es-MX/firefox-ios.xliff` — "Done" is translated as "Cerrar" (Close) instead of "Listo"/"Hecho".
    - Current: `Cerrar`
    - Source: `Done`
    - Suggest: `Listo`
    - The source is the Done button in the Settings title bar; "Cerrar" means Close, a different action/label, and duplicates the Close strings in the same file.
- `Downloads.CancelDialog.Resume` — `es-MX/firefox-ios.xliff` — "Resume" rendered as "Continuar" is acceptable, but more precisely "Reanudar".
    - Current: `Continuar`
    - Source: `Resume`
    - Suggest: `Reanudar`
    - Source "Resume" declines cancellation and resumes the download; "Reanudar" is the standard Firefox term, while "Continuar" reads as a generic Continue.
- `ErrorPages.AdvancedWarning2.Text` — `es-MX/firefox-ios.xliff` — "tampering by an attacker" is rendered as "una falsificación de un atacante" (a forgery), changing the meaning.
    - Current: `una falsificación de un atacante`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `una manipulación por parte de un atacante`
    - The source says the connection may have been tampered with by an attacker, not that it is a forgery.
- `Hotkeys.Forward.DiscoveryTitle` — `es-MX/firefox-ios.xliff` — "Forward" (navigation forward in session history) is rendered as "Siguiente", which does not convey the browser navigation action.
    - Current: `Siguiente`
    - Source: `Forward`
    - Suggest: `Adelante`
    - The string pairs with Hotkeys.Back.DiscoveryTitle ("Atrás"); the browser navigation term is "Adelante", not the generic "Siguiente".
- `Keyboard.Shortcuts.ActualSize` — `es-MX/firefox-ios.xliff` — "Actual Size" mistranslated as "Tamaño actual" (current size) instead of the real/original size.
    - Current: `Tamaño actual`
    - Source: `Actual Size`
    - Suggest: `Tamaño real`
    - Per the comment, it resets the page view to the standard viewing size; "actual" is a false friend in Spanish meaning "current".
- `Looks like Firefox crashed previously. Would you like to restore your tabs?` — `es-MX/firefox-ios.xliff` — "restore your tabs" is translated as "restablecer" (reset) instead of "restaurar".
    - Current: `¿Te gustaría restablecer tus pestañas?`
    - Source: `Looks like Firefox crashed previously. Would you like to restore your tabs?`
    - Suggest: `¿Te gustaría restaurar tus pestañas?`
    - The prompt restores previously open tabs; "restablecer" means reset/re-establish and is the wrong term for restoring tabs after a crash.
- `Menu.CopyURL.Confirm` — `es-MX/firefox-ios.xliff` — Adds "Enlace" (link), which the source does not contain.
    - Current: `Enlace URL copiado al portapapeles`
    - Source: `URL Copied To Clipboard`
    - Suggest: `URL copiada al portapapeles`
    - Source is "URL Copied To Clipboard"; "Enlace URL" is redundant and adds a word not in the source.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-MX/firefox-ios.xliff` — The translation says blocking reduces the number of social media companies, instead of reducing how much they can see of what you do online.
    - Current: `reduce la cantidad de empresas de redes sociales que pueden ver lo que haces en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `reduce lo que las empresas de redes sociales pueden ver de lo que haces en línea`
    - The en-US says "reduces how much social media companies can see what do you online" — it limits their visibility, not the number of companies.
- `Open Tabs` — `es-MX/firefox-ios.xliff` — "Open Tabs" (a sync setting label, a noun phrase) is translated as the imperative "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - The developer comment says this toggles the tab syncing setting, so "Open Tabs" is a noun phrase meaning currently open tabs, not a command to open tabs.
- `ScanQRCode.PermissionError.Message.v100` — `es-MX/firefox-ios.xliff` — "device" is dropped from "Go to device ‘Settings’".
    - Current: `Ir a ‘Configuración’ > ‘Firefox’.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Ir a ‘Configuración’ del dispositivo > ‘Firefox’.`
    - The source specifies the device's Settings app, which the translation omits, losing the distinction from Firefox's own settings.
- `Search.SuggestSectionTitle.v102` — `es-MX/firefox-ios.xliff` — "Firefox Suggest" is a feature/brand name and was translated as "Sugerencia de Firefox" (a Firefox suggestion).
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the product feature name "Firefox Suggest", used as a section header; it should not be turned into a generic singular noun phrase.
- `Search.ThirdPartyEngines.AddTitle` — `es-MX/firefox-ios.xliff` — Translation adds "nuevo", which is not in the source "Add Search Provider?".
    - Current: `¿Agregar nuevo proveedor de búsqueda?`
    - Source: `Add Search Provider?`
    - Suggest: `¿Agregar proveedor de búsqueda?`
    - The en-US source says "Add Search Provider?" with no "new".
- `SendTo.NoDevicesFound.Message` — `es-MX/firefox-ios.xliff` — Plural "any other devices" rendered as singular "otro dispositivo".
    - Current: `No tienes otro dispositivo conectado`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `No tienes otros dispositivos conectados`
    - The en-US says the user has no other devices (plural) connected to the account.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-MX/firefox-ios.xliff` — "New tab arrived from another device" is rendered as "Nueva pestaña agregada desde otro dispositivo" (added), losing the "arrived/received" meaning.
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Llegó una nueva pestaña desde otro dispositivo.`
    - The source says a tab arrived (was received) from another device; "agregada" says it was added, which differs from the en-US and from the sibling string's "Se recibió una pestaña".
- _…and 18 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Alerts.AddToCalendar.BodyDefault.v134` — `es-MX/firefox-ios.xliff` — Misspelling of "agregar".
    - Current: `agrear`
    - Source: `This site is asking to download a file and add an event to your calendar.`
    - Suggest: `agregar`
    - The source says "add an event"; the Spanish verb is misspelled as "agrear" instead of "agregar" (correct in the sibling string Alerts.AddToCalendar.Body.v134).
- `Alerts.RestoreTabs.Title.v109.v2` — `es-MX/firefox-ios.xliff` — Missing accent on the preterite verb "falló".
    - Current: `%@ fallo.`
    - Source: `%@ crashed. Restore your tabs?`
    - Suggest: `%@ falló.`
    - Source "%@ crashed" requires the past-tense verb "falló"; without the accent "fallo" is the noun "failure"/present tense.
- `Bookmarks.DeleteFolderWarning.Description` — `es-MX/firefox-ios.xliff` — Missing preposition "de" after "estás seguro".
    - Current: `¿Estás seguro que quieres eliminarlo`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Estás seguro de que quieres eliminarlo`
    - Standard Spanish requires "seguro de que"; the omission (queísmo) is a grammatical error.
- `Bookmarks.EmptyState.Nested.Body.v135` — `es-MX/firefox-ios.xliff` — Infinitive "Agregar" used instead of the imperative required by the source instruction.
    - Current: `Agregar marcadores mientras navegas`
    - Source: `Add bookmarks as you browse so you can find your favorite sites later.`
    - Suggest: `Agrega marcadores mientras navegas`
    - The en-US "Add bookmarks as you browse" is an imperative addressed to the user; the rest of the sentence uses informal second person ("navegas", "puedas"), so the infinitive is inconsistent and ungrammatical here.
- `ContextualHints.Translations.Body.v145` — `es-MX/firefox-ios.xliff` — Missing accent on the pronoun "tú".
    - Current: `cuando tu lo estés`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `cuando tú lo estés`
    - "tu" is the possessive adjective; the stressed subject pronoun requires the accent: "tú".
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `es-MX/firefox-ios.xliff` — Missing accent on the imperative "Continúa".
    - Current: `Continua donde te quedaste`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `Continúa donde te quedaste`
    - The imperative of "continuar" is "continúa" with an accent; "continua" is an adjective.
- `DefaultBrowserPopup.SecondLabel.v114` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Predeterminado" in "Navegador Predeterminado".
    - Current: `*Navegador Predeterminado*`
    - Source: `2. Tap *Default Browser App*`
    - Suggest: `*Navegador predeterminado*`
    - The iOS Settings label in Spanish is "Navegador predeterminado"; Spanish uses sentence case.
- `Onboarding.Customization.Theme.Continue.Action.v123` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Continuar" mid-sentence; Spanish uses sentence case.
    - Current: `Guardar y Continuar`
    - Source: `Save and Continue`
    - Suggest: `Guardar y continuar`
    - Spanish does not use English title case; "Continuar" should be lowercase.
- `Onboarding.Customization.Theme.System.Action.v123` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Automático"; Spanish uses sentence case.
    - Current: `Sistema Automático`
    - Source: `System Auto`
    - Suggest: `Sistema automático`
    - Spanish does not use English title case for adjectives in UI labels.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `es-MX/firefox-ios.xliff` — "Mostrar tendencias de búsquedas" has an incorrect plural/construction for "Show Trending Searches".
    - Current: `Mostrar tendencias de búsquedas`
    - Source: `Show Trending Searches`
    - Suggest: `Mostrar búsquedas en tendencia`
    - The source refers to the trending searches list; "tendencias de búsquedas" is ungrammatical (should be "de búsqueda" at minimum) and does not match the section title "Tendencias en %@".
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `es-MX/firefox-ios.xliff` — Number agreement error: "estas funcionalidad" should be singular or plural consistently.
    - Current: `Si bloqueas estas funcionalidad`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `Si bloqueas estas funcionalidades`
    - Demonstrative plural "estas" does not agree with singular noun "funcionalidad".
- `Settings.AIControls.BlockedInformation.v151` — `es-MX/firefox-ios.xliff` — Missing accent in "especificas".
    - Current: `funciones especificas`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `funciones específicas`
    - The adjective is "específicas" with an accent on the antepenultimate syllable.
- `CloseTabsToast.SingleTabTitle.v113` — `es-MX/firefox-ios.xliff` — Incorrect capitalization of "Cerrada" mid-sentence in Spanish.
    - Current: `Pestaña Cerrada`
    - Source: `Tab Closed`
    - Suggest: `Pestaña cerrada`
    - Spanish does not use English title case; the sibling string CloseTabsToast.Title.v113 correctly uses "Pestañas cerradas".
- `ContextMenu.ButtonToast.NewTabOpened.LabelText` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Pestaña" mid-sentence.
    - Current: `Nueva Pestaña abierta`
    - Source: `New Tab opened`
    - Suggest: `Nueva pestaña abierta`
    - Spanish does not use title case; the v114 variant of the same string correctly reads "Nueva pestaña abierta".
- `Downloads.CancelDialog.Message` — `es-MX/firefox-ios.xliff` — Missing preposition "de" after "seguro" and "this download" rendered as "la descarga".
    - Current: `¿Estás seguro que quieres cancelar la descarga?`
    - Source: `Are you sure you want to cancel this download?`
    - Suggest: `¿Estás seguro de que quieres cancelar esta descarga?`
    - "estar seguro de que" requires the preposition; also the source says "this download".
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-MX/firefox-ios.xliff` — "linea" is missing its accent (should be "línea").
    - Current: `tu actividad en linea`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `tu actividad en línea`
    - Spelling/accent error; the same phrase is correctly written "en línea" elsewhere in this file.
- `ScanQRCode.PermissionError.Message.v100` — `es-MX/firefox-ios.xliff` — Wrong preposition: "el acceso de la cámara" should be "el acceso a la cámara".
    - Current: `Permitir a Firefox el acceso de la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Permitir a Firefox el acceso a la cámara.`
    - "Allow Firefox to access camera" requires "acceso a la cámara" in Spanish; "acceso de la cámara" means the camera's access.
- `SendTo.NotSignedIn.Title` — `es-MX/firefox-ios.xliff` — Wrong preposition: "iniciado sesión a tu cuenta" should be "en tu cuenta".
    - Current: `No has iniciado sesión a tu cuenta de Firefox.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `No has iniciado sesión en tu cuenta de Firefox.`
    - Spanish requires "iniciar sesión en" a account, not "a".
- `Settings.Home.Current.Description.v101` — `es-MX/firefox-ios.xliff` — Missing accent on interrogative/relative "qué" in "Elige que mostrar".
    - Current: `Elige que mostrar como página de inicio.`
    - Source: `Choose what displays as the homepage.`
    - Suggest: `Elige qué mostrar como página de inicio.`
    - Indirect interrogative requires the accented "qué", as done correctly in Settings.Home.Option.Description.v101.
- `Settings.OfferClipboardBar.Status` — `es-MX/firefox-ios.xliff` — "When Opening Firefox" rendered with an odd progressive construction.
    - Current: `Cuando esté abriendo Firefox`
    - Source: `When Opening Firefox`
    - Suggest: `Al abrir Firefox`
    - The source is a simple temporal phrase; the parallel string Settings.OfferClipboardBar.Status.v128 uses "Al abrir %@".
- `xRJbBP` — `es-MX/firefox-ios.xliff` — Incorrect capitalization of the second word in Spanish sentence case.
    - Current: `Nueva Búsqueda`
    - Source: `New Search`
    - Suggest: `Nueva búsqueda`
    - Spanish does not use title case; only the first word should be capitalized, as with "Acción rápida" in the same file.

### D. Terminology, register & consistency

- `LibraryPanel.Section.Older` — `es-MX/firefox-ios.xliff` — "Older" as a history section header is rendered as "Antiguo" instead of "Más antiguo"/"Más antiguos".
    - Current: `Antiguo`
    - Source: `Older`
    - Suggest: `Más antiguos`
    - The source is a comparative section title for items older than thirty days; "Antiguo" loses the comparative sense and does not agree with the plural items it groups.
- `MainMenu.SiteProtection.ProtectionsOff.Title.v141` — `es-MX/firefox-ios.xliff` — "Protections are OFF" rendered as "Protección de navegación DESACTIVADA", narrowing the term used elsewhere as "Protecciones".
    - Current: `Protección de navegación DESACTIVADA`
    - Source: `Protections are OFF`
    - Suggest: `Protecciones DESACTIVADAS`
    - The source is simply "Protections"; the same screen translates "Protections" as "Protecciones", so adding "de navegación" is inconsistent and adds unsourced content.
- `MainMenu.SiteProtection.ProtectionsOn.Title.v141` — `es-MX/firefox-ios.xliff` — "Protections are ON" rendered as "Protección de navegación ACTIVADA", inconsistent with "Protecciones" used on the same screen.
    - Current: `Protección de navegación ACTIVADA`
    - Source: `Protections are ON`
    - Suggest: `Protecciones ACTIVADAS`
    - The source is simply "Protections"; the same screen translates "Protections" as "Protecciones", so adding "de navegación" is inconsistent and adds unsourced content.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `es-MX/firefox-ios.xliff` — "Reader View" is rendered "vista de lector" here but "vista de lectura" in all other strings of the same menu.
    - Current: `Desactivar la vista de lector`
    - Source: `Turn off Reader View`
    - Suggest: `Desactivar la vista de lectura`
    - Terminology inconsistency within the same screen; the On/Subtitle/accessibility strings all use "vista de lectura".
- `Onboarding.Customization.Toolbar.Description.v123` — `es-MX/firefox-ios.xliff` — Formal address ("Mantenga") used where the locale convention and surrounding onboarding strings are informal.
    - Current: `Mantenga las búsquedas al alcance.`
    - Source: `Keep searches within reach.`
    - Suggest: `Mantén las búsquedas al alcance.`
    - es-MX convention is informal (tú); neighbouring onboarding strings use "Elige", "Guardar y comenzar a navegar", etc.
- `Onboarding.Customization.Toolbar.Title.v123` — `es-MX/firefox-ios.xliff` — Formal address ("Elija") used where the locale convention and sibling strings are informal.
    - Current: `Elija una ubicación para la barra de herramientas`
    - Source: `Pick a toolbar placement`
    - Suggest: `Elige una ubicación para la barra de herramientas`
    - es-MX convention is informal (tú); the parallel string Onboarding.Customization.Theme.Title uses "Elige".
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `es-MX/firefox-ios.xliff` — "Top" rendered as "Arriba" while the paired "Bottom" option is "Inferior" and the v140 equivalent is "Superior", making the pair inconsistent on the same screen.
    - Current: `Arriba`
    - Source: `Top`
    - Suggest: `Superior`
    - On the same toolbar customization card, Bottom is "Inferior"; Top must be "Superior" to match, as in Onboarding.Modern.Customization.Toolbar.Top.Action.v140.
- `Onboarding.Modern.Welcome.Description.v145` — `es-MX/firefox-ios.xliff` — Impersonal phrasing drops the second-person address used by the source and by the v140 variant of the same string.
    - Current: `Una sola elección brinda protección en toda la web. Es posible cambiarla en cualquier momento.`
    - Source: `One choice protects you everywhere you go on the web. You can always change it later.`
    - Suggest: `Una sola elección te protege donde sea que navegues en la web. Siempre puedes cambiarla más tarde.`
    - Source is "One choice protects you everywhere you go on the web. You can always change it later."; the locale convention is informal second person (as used in the v140 duplicate), but this version removes "you" entirely.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `es-MX/firefox-ios.xliff` — "email masks" is rendered as "plantillas para correos electrónicos" (templates) instead of "máscaras de correo electrónico" used everywhere else in this file.
    - Current: `plantillas gratuitas para correos electrónicos`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `máscaras de correo electrónico gratuitas`
    - The source term is "email masks", consistently translated as "máscaras de correo electrónico" in every other string of RelayMask.strings; "plantillas" means templates and is both inconsistent and wrong.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `es-MX/firefox-ios.xliff` — "Terms of Use" is translated as "Condiciones de uso" here while every other string in the same file uses "Términos de uso".
    - Current: `Se han abierto las Condiciones de uso`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Se han abierto los Términos de uso`
    - Terminology inconsistency within the same screen/file; TitleValue1, Link.TermsOfUse and Description all use "Términos de uso".
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `es-MX/firefox-ios.xliff` — "Full time" is rendered as "Tiempo completo" here but as "Finalizado" in the other Full Time strings in the same widget.
    - Current: `Tiempo completo • Penales (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Finalizado • Penales (%@)`
    - WorldCup.HomepageWidget.FTLabel/FTNoParenthesisLabel translate the same source term "Full Time" as "Finalizado"; "Tiempo completo" is a literal rendering that means "full duration", not a finished match, and is inconsistent on the same screen.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `es-MX/firefox-ios.xliff` — "BRONZE FINAL" (the match) is translated as "TERCER PUESTO", colliding with the separate "THIRD PLACE" label and using a non-Mexican term.
    - Current: `TERCER PUESTO`
    - Source: `BRONZE FINAL`
    - Suggest: `PARTIDO POR EL TERCER LUGAR`
    - The source distinguishes the bronze-final match label from the THIRD PLACE winner label (translated "TERCER LUGAR"); rendering the match as "TERCER PUESTO" is inconsistent within the same widget and "puesto" is not the es-MX term.
- `This action will clear all of your private data. It cannot be undone.` — `es-MX/firefox-ios.xliff` — Uses formal "sus" while the locale convention and the parallel string in ClearHistoryConfirm use informal "tus".
    - Current: `Esta acción borrará todos sus datos privados.`
    - Source: `This action will clear all of your private data. It cannot be undone.`
    - Suggest: `Esta acción borrará todos tus datos privados.`
    - es-MX is established as informal; the equivalent string in ClearHistoryConfirm.strings uses "tus datos privados".
- `DefaultBrowserOnboarding.Description2` — `es-MX/firefox-ios.xliff` — "Default Browser App" is rendered as "navegador por defecto" here and in the screenshot string while other strings on the same feature use "navegador predeterminado".
    - Current: `2. Pulsar la Aplicación del navegador por defecto`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Pulsar Aplicación de navegador predeterminado`
    - The same source term "Default Browser" is translated "predeterminado" in DefaultBrowserCard.Title and Settings.DefaultBrowserMenuItem but "por defecto" here, an inconsistency within the same feature file.
- `ErrorPages.AdvancedWarning1.Text` — `es-MX/firefox-ios.xliff` — Formal "su conexión" breaks the locale's informal register used in the adjacent strings, and the adjective doesn't agree with "conexión".
    - Current: `no podemos confirmar que su conexión a este sitio sea seguro`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `no podemos confirmar que tu conexión a este sitio sea segura`
    - es-MX convention is informal address ("tu"), as in the neighboring ErrorPages.AdvancedWarning2.Text ("Sigue adelante si aceptas"); also "seguro" must agree with the feminine noun "conexión".
- `Menu.AddToShortcuts.v99` — `es-MX/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the related toast on the same feature.
    - Current: `Agregar a accesos directos`
    - Source: `Add to Shortcuts`
    - Suggest: `Agregar a atajos`
    - Menu.AddPin.Confirm2 translates the same "Shortcuts" feature name as "atajos"; using two different terms for the same home-screen feature is inconsistent.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `es-MX/firefox-ios.xliff` — Register switches to formal "su" mid-sentence after informal "te".
    - Current: `Esto te permite guardar la imagen en su rollo de cámara.`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `Esto te permite guardar la imagen en tu carrete de fotos.`
    - es-MX convention is informal address; "te permite ... en su" mixes informal and formal in the same sentence.
- `fi3W24-eHmH1H` — `es-MX/firefox-ios.xliff` — ‘Clear Private Tabs’ is rendered as “Borrar Pestañas Privadas” here but as “Limpiar Pestañas Privadas” in the related strings eHmH1H and PzSrmZ-eHmH1H.
    - Current: `‘Borrar Pestañas Privadas’`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `‘Limpiar Pestañas Privadas’`
    - The same menu item name must match the label defined in eHmH1H ("Limpiar Pestañas Privadas") so Siri/voice matching and the UI stay consistent.

### E. Typography, punctuation & spacing

- `NSFaceIDUsageDescription` — `es-MX/firefox-ios.xliff` — Parenthetical gloss uses hyphens without surrounding spaces, producing "facial-para" with no space.
    - Current: `Firefox requiere Face ID - reconocimiento facial-para acceder`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Firefox requiere Face ID (reconocimiento facial) para acceder`
    - The added explanatory aside is punctuated inconsistently and the closing hyphen is glued to the next word, leaving no space between "facial" and "para".
- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-MX/firefox-ios.xliff` — Ampersand kept instead of Spanish conjunction "y".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the English "&" should be rendered as "y"; the accessibility label would be read aloud incorrectly.
- `Bookmarks.Menu.DeleteBookmark.v132` — `es-MX/firefox-ios.xliff` — Unnecessary capitalization of "Marcador", inconsistent with other bookmark strings in the same file.
    - Current: `Eliminar Marcador`
    - Source: `Delete Bookmark`
    - Suggest: `Eliminar marcador`
    - Spanish uses sentence case; sibling strings render "Editar marcador" and "Eliminar carpeta" in lowercase.
- `ContextMenu.ButtonToast.NewPrivateTabOpened.LabelText` — `es-MX/firefox-ios.xliff` — Unnecessary title-case capitalization in Spanish.
    - Current: `Nueva Pestaña Privada abierta`
    - Source: `New Private Tab opened`
    - Suggest: `Nueva pestaña privada abierta`
    - Spanish does not use English title case; the parallel v113 string correctly uses "Nueva pestaña privada abierta", creating an inconsistency.
- `Could not load page.` — `es-MX/firefox-ios.xliff` — Final period from the source sentence is missing.
    - Current: `No se pudo cargar la página`
    - Source: `Could not load page.`
    - Suggest: `No se pudo cargar la página.`
    - The en-US string ends with a period; the translation drops it.
- `TopSites.RemovePage.Button` — `es-MX/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The source uses an em dash and the locale convention is the em dash; a plain hyphen deviates.
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

- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — fixed 2026-08-24
