# Firefox iOS l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-ES: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (61)

- `DefaultBrowserOnboarding.Screenshot` — `es-ES/firefox-ios.xliff` — Gender agreement error: "predeterminado" should agree with "Aplicación".
    - Current: `Aplicación de navegador predeterminado`
    - Source: `Default Browser App`
    - Suggest: `Aplicación de navegador predeterminada`
    - The en-US "Default Browser App" refers to the app (feminine "aplicación"); the parallel string DefaultBrowserOnboarding.Description2 uses "aplicación de navegador predeterminada", so the masculine form here is inconsistent and wrong.
- `ActivityStream.ContextMenu.UnpinTopsite` — `es-ES/firefox-ios.xliff` — "Unpin" is translated as "Desanclar" while the paired "Pin" is "Fijar", breaking terminology consistency.
    - Current: `Desanclar`
    - Source: `Unpin`
    - Suggest: `Dejar de fijar`
    - ActivityStream.ContextMenu.PinTopsite2 renders "Pin" as "Fijar"; the opposite action in the same context menu must use the same verb.
- `AddPass.Error.Message` — `es-ES/firefox-ios.xliff` — "Wallet" is rendered as the obsolete brand name "Passbook".
    - Current: `Passbook`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Wallet`
    - The source names Apple's Wallet app; the developer comment explicitly refers to Wallet. "Passbook" is a different (legacy) brand name.
- `Address and Search` — `es-ES/firefox-ios.xliff` — Singular "Address" translated as plural "Direcciones".
    - Current: `Direcciones y búsqueda`
    - Source: `Address and Search`
    - Suggest: `Dirección y búsqueda`
    - The comment states both words are nouns in singular; "Address" refers to the address field, not multiple addresses.
- `BreachAlerts.Description` — `es-ES/firefox-ios.xliff` — "log in to the site" mistranslated as "conéctate en el sitio" with wrong preposition/meaning.
    - Current: `conéctate en el sitio`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `inicia sesión en el sitio`
    - The source instructs the user to log in to the site; "conéctate en el sitio" is not the standard rendering of "log in" and is ungrammatical with "en".
- `ErrorPages.CertWarning.Title` — `es-ES/firefox-ios.xliff` — "This Connection is Untrusted" translated as "Tu conexión no está verificada" (not verified) instead of not trusted.
    - Current: `Tu conexión no está verificada`
    - Source: `This Connection is Untrusted`
    - Suggest: `Esta conexión no es de confianza`
    - The source says the connection is untrusted, and uses "This", not "Your"; "no está verificada" changes the meaning.
- `ErrorPages.AdvancedWarning2.Text` — `es-ES/firefox-ios.xliff` — "tampering by an attacker" rendered as "una falsificación de un atacante" (a forgery by an attacker).
    - Current: `una falsificación de un atacante`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `una manipulación por parte de un atacante`
    - "Tampering" means manipulation/interference, not forgery/falsification.
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `es-ES/firefox-ios.xliff` — "Tab pickup" (feature that resumes tabs from other devices) translated as "Selector de pestañas" (tab picker/selector).
    - Current: `Selector de pestañas`
    - Source: `Tab pickup`
    - Suggest: `Recogida de pestañas`
    - The developer comment explains this labels the section showing a recent tab synced from another device; "Selector de pestañas" describes a tab picker UI, a different thing.
- `Hotkeys.Forward.DiscoveryTitle` — `es-ES/firefox-ios.xliff` — Wrong meaning: "Actual Size" means the original/standard size, not the current one.
    - Current: `Tamaño actual`
    - Source: `Forward`
    - Suggest: `Tamaño real`
    - Per the developer comment, "Actual Size" resets the page view to the standard viewing size; "Tamaño actual" is a false friend meaning "current size".
- `Logins.Onboarding.LearnMoreButtonTitle` — `es-ES/firefox-ios.xliff` — "Learn More" is rendered as "Aprender más" while the identical source string elsewhere in the same file uses "Saber más".
    - Current: `Aprender más`
    - Source: `Learn More`
    - Suggest: `Saber más`
    - Logins.DevicePasscodeRequired.LearnMoreButtonTitle has the same source and same developer comment but is translated "Saber más"; "Aprender más" is a literal rendering inconsistent with the established Firefox term.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-ES/firefox-ios.xliff` — The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener acceso a tus datos y…`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de lo que haces en lín…`
    - Source says social networks place trackers on other websites (not so that other sites build a profile), and that blocking reduces how much they can see — not that they will lose access to your data entirely.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `es-ES/firefox-ios.xliff` — "can make websites load faster" rendered as a certainty ("hará que").
    - Current: `Bloquearlos hará que los sitios web carguen más rápido`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `Bloquearlos puede hacer que los sitios web carguen más rápido`
    - The en-US hedges with "can make"; the Spanish asserts it as a guaranteed outcome.
- `OpenURL.Error.Message` — `es-ES/firefox-ios.xliff` — "cannot open the page" translated as "no pudo encontrar la página" (could not find).
    - Current: `Firefox no pudo encontrar la página porque la dirección no es válida.`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox no puede abrir la página porque la dirección no es válida.`
    - Source says Firefox cannot open the page, not that it could not find it.
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-ES/firefox-ios.xliff` — "set by third parties such as advertisers and analytics companies" narrowed to only advertising and analytics companies.
    - Current: `Están configuradas por empresas externas de anuncios y de analítica web.`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Las establecen terceros, como anunciantes y empresas de analítica web.`
    - The source gives advertisers/analytics as examples of third parties; the translation presents them as the only source.
- `Open Tabs` — `es-ES/firefox-ios.xliff` — The noun phrase "Open Tabs" (a sync data-type toggle) is translated as the verb phrase "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - Per the developer comment this toggles syncing of open tabs; the label names the data type, not an action.
- `Menu.TrackingProtectionCryptominersBlocked.Title` — `es-ES/firefox-ios.xliff` — "Cryptomineros" is a misspelling; the description string in the same screen uses "criptomineros".
    - Current: `Cryptomineros`
    - Source: `Cryptominers`
    - Suggest: `Criptomineros`
    - Spanish spelling is "criptomineros", as used in Menu.TrackingProtectionDescription.CryptominersNew on the same screen.
- `Search.SuggestSectionTitle.v102` — `es-ES/firefox-ios.xliff` — "Firefox Suggest" (a feature/brand name) is rendered as "Sugerencia de Firefox", changing a product name into a singular common noun.
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the brand/feature name "Firefox Suggest" used as a section header; brand names must not be translated.
- `ScanQRCode.PermissionError.Message.v100` — `es-ES/firefox-ios.xliff` — Second sentence uses an infinitive instead of the imperative, breaking parallelism with the first sentence and the informal register.
    - Current: `Permitir que Firefox acceda a la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Permite que Firefox acceda a la cámara.`
    - The source "Allow Firefox to access camera." is an instruction to the user; the first sentence is translated with the informal imperative ("Vete"), so the second should be too.
- `ScanQRCode.PermissionError.Message.v100` — `es-ES/firefox-ios.xliff` — "device 'Settings'" is translated as just "'Ajustes'", dropping the reference to the device settings.
    - Current: `Vete a ‘Ajustes’`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Ve a los ‘Ajustes’ del dispositivo`
    - The en-US says to go to the device's Settings app; the word "device" is omitted in the Spanish.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-ES/firefox-ios.xliff` — "arrived from another device" translated as "agregada" (added), losing the meaning of a tab arriving/received.
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Ha llegado una nueva pestaña desde otro dispositivo.`
    - The source says a new tab arrived from another device; "agregada" means it was added, which is a different action.
- `Settings.AddCustomEngine.URLPlaceholder` — `es-ES/firefox-ios.xliff` — "Replace Query with %s" mistranslated as "Cambia búsqueda con %s", losing the instruction to substitute the query term with %s.
    - Current: `URL (Cambia búsqueda con %s)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (Reemplaza la consulta con %s)`
    - The source instructs the user to replace the query part of the URL with %s; "Cambia búsqueda con" is unclear and does not convey substitution of the query string.
- `Settings.Home.Option.JumpBackIn` — `es-ES/firefox-ios.xliff` — "Jump Back In" (resume browsing) rendered as "Saltar hacia atrás" (skip/jump backwards).
    - Current: `Saltar hacia atrás`
    - Source: `Jump Back In`
    - Suggest: `Volver a la carga`
    - The feature name means resuming recent browsing; "Saltar hacia atrás" reads as skipping backwards and does not convey the section's meaning (Firefox uses "Volver a la carga"/"Retomar donde lo dejaste").
- `Settings.Home.Option.StartAtHome.Description` — `es-ES/firefox-ios.xliff` — Interrogative "qué" is missing its accent in "Elige que ver".
    - Current: `Elige que ver cuando regreses a Firefox.`
    - Source: `Choose what you see when you return to Firefox.`
    - Suggest: `Elige qué ver cuando regreses a Firefox.`
    - "Choose what you see" requires the accented interrogative pronoun "qué".
- `Settings.NewTab.CustomURL` — `es-ES/firefox-ios.xliff` — "Custom URL" is rendered as an imperative "Personalizar URL" (Customize URL) instead of a noun label.
    - Current: `Personalizar URL`
    - Source: `Custom URL`
    - Suggest: `URL personalizada`
    - The source is a label naming the custom URL option, not a command to customize; the sibling string Settings.NewTab.Option.Custom correctly uses the adjective "Personalizado".
- `Settings.SendUsage.Message` — `es-ES/firefox-ios.xliff` — "provide ... Firefox" mistranslated as "ejecutar" (run/execute) Firefox.
    - Current: `para poder ejecutar y mejorar Firefox`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `para poder ofrecer y mejorar Firefox`
    - The en-US says Mozilla collects only what it needs to provide and improve Firefox; "ejecutar" means to run/execute, which is not the source meaning.
- `Settings.Studies.Toggle.Link` — `es-ES/firefox-ios.xliff` — "Learn More." rendered as "Aprender más." while the identical source elsewhere in the same screen uses "Descubrir más."
    - Current: `Aprender más.`
    - Source: `Learn More.`
    - Suggest: `Descubrir más.`
    - Settings.SendUsage.Link translates the same source string as "Descubrir más."; inconsistent rendering of the same link label on the same settings screen.
- `Settings.WebsiteData.ConfirmPrompt` — `es-ES/firefox-ios.xliff` — Formal address "sus" used where the locale convention is informal (tú).
    - Current: `Esta acción eliminará los datos de todos sus sitios.`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `Esta acción eliminará los datos de todos tus sitios.`
    - es-ES convention is informal address; other strings in this batch use "toca", "no has visto", "te rastreen".
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `es-ES/firefox-ios.xliff` — Mistranslation: source says some ad tracking is allowed SO THAT sites work properly; target says "por lo que" (therefore) and adds an incorrect preposition "a".
    - Current: `Permite a algunas publicidades rastreadoras por lo que los sitios funcionan adecuadamente.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Permite cierto rastreo publicitario para que los sitios web funcionen correctamente.`
    - "so websites function properly" expresses purpose (para que), not consequence; "Permite a algunas publicidades rastreadoras" is also ungrammatical.
- `TranslationToastHandler.PromptTranslate.Title` — `es-ES/firefox-ios.xliff` — The translation misassigns placeholders: %2$@ is the target language and %3$@ is the service name, but the Spanish reads "from %2$@ to %3$@".
    - Current: `¿Quieres traducirla de %2$@ a %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `¿Quieres traducirla a %2$@ con %3$@?`
    - Per the comment, %2$@ is the local language and %3$@ is the translation service; the source says "Translate to %2$@ with %3$@", not "from ... to ...".
- `TopSites.RemovePage.Button` — `es-ES/firefox-ios.xliff` — Em dash in the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The locale convention is the em dash, and the source uses an em dash separator.
- `fxa.signin.qr-link-instruction` — `es-ES/firefox-ios.xliff` — "computador" is Latin American usage; es-ES uses "ordenador".
    - Current: `Abre Firefox en tu computador y ve a firefox.com/pair`
    - Source: `On your computer open Firefox and go to firefox.com/pair`
    - Suggest: `Abre Firefox en tu ordenador y ve a firefox.com/pair`
    - Source "your computer"; the Spain locale term is "ordenador", not the American "computador".
- `Well, this is embarrassing.` — `es-ES/firefox-ios.xliff` — "embarazoso" is a false-friend-adjacent rendering; acceptable word but the sentence reads oddly—flagged as mistranslation of tone.
    - Current: `Bueno, esto es embarazoso.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `Bueno, esto es un poco vergonzoso.`
    - "embarrassing" here refers to the app's own awkwardness; "embarazoso" in es-ES means awkward/tricky for a situation but is commonly a translation artifact; "vergonzoso" conveys the intended tone.
- `%@ on %@` — `es-ES/firefox-ios.xliff` — The connector word is left in German ("war") instead of Spanish "en".
    - Current: `%1$@ war %2$@`
    - Source: `%1$@ on %2$@`
    - Suggest: `%1$@ en %2$@`
    - Source is "%1$@ on %2$@" (app name on device name); "war" is not Spanish and conveys no meaning here.
- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-ES/firefox-ios.xliff` — Ampersand left untranslated and capitalization copied from English in "Ajustes de Privacidad & Seguridad".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the English "&" must be rendered as "y", and common nouns are not capitalized mid-sentence as in English title case.
- `Bookmarks.DeleteFolderWarning.Description` — `es-ES/firefox-ios.xliff` — Register inconsistency and missing preposition: "¿Estás seguro que desea..." mixes informal "estás" with formal "desea" and omits "de".
    - Current: `¿Estás seguro que desea eliminar esta carpeta y su contenido?`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Seguro que quieres eliminar esta carpeta y su contenido?`
    - The locale uses the informal register; "desea" is formal and clashes with "estás". Also "seguro que" after "estar seguro" requires "de que" (queísmo).
- `Bookmarks.EmptyState.Root.Body.v135` — `es-ES/firefox-ios.xliff` — "Save sites as you browse" is rendered with an infinitive instead of the imperative used elsewhere.
    - Current: `Guardar sitios mientras navegas.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `Guarda sitios mientras navegas.`
    - The source is an imperative addressed to the user, consistent with the informal register and with the sibling string; "Guardar" is an infinitive and reads as a label rather than an instruction.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `es-ES/firefox-ios.xliff` — "Save sites as you browse" is rendered with an infinitive instead of the imperative.
    - Current: `Guardar sitios mientras navegas.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Guarda sitios mientras navegas.`
    - The source is an imperative addressed to the user, matching "Inicia sesión" in the same string; the infinitive is inconsistent.
- `Addresses.EditAddress.AutofillAddressSuburb.v129` — `es-ES/firefox-ios.xliff` — "Suburb" as an address administrative division is rendered as "Suburbio", which in Spanish means a poor/marginal outskirts district, not an address field.
    - Current: `Suburbio`
    - Source: `Suburb`
    - Suggest: `Barrio`
    - The developer comment describes an address field for suburb details; es-ES "suburbio" carries a pejorative meaning (slum outskirts) and does not name an address division. "Barrio" (or "Población") is the standard rendering.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `es-ES/firefox-ios.xliff` — "Subject Name" (certificate subject) is rendered as "Nombre del asunto" (subject/topic) instead of the certificate term "sujeto".
    - Current: `Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - In X.509 certificates, "Subject" is the entity the certificate is issued to; the same file already translates "Subject Alt Names" as "Nombres alternativos del sujeto", so "asunto" is both wrong and inconsistent.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-ES/firefox-ios.xliff` — "might log you out of websites" is rendered impersonally, losing the reference to the user's own sessions.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The en-US says the action may log *you* out; the Spanish as written lacks the possessive and reads as the sites closing a session generically.
- `ContextualHints.MainMenu.MenuRedesign.Body.v142` — `es-ES/firefox-ios.xliff` — "settings" rendered as plural "configuraciones"; the app's Settings menu is "Ajustes"/"Configuración" in es-ES.
    - Current: `Marcadores, historial y configuraciones`
    - Source: `Bookmarks, history, and settings — all at your fingertips.`
    - Suggest: `Marcadores, historial y ajustes`
    - In en-US "settings" refers to the app's Settings section, which is consistently "Ajustes" in es-ES Firefox; the plural "configuraciones" is not the product term.
- `MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131` — `es-ES/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de los atajos`
    - The same source term "Shortcuts" must be consistent within the Save submenu; MainMenu.Submenus.Save.AddToShortcuts.Title.v131 uses "Añadir a atajos" and its subtitle uses "Atajo".
- `MainMenu.Submenus.Save.AccessibilityLabels.RemoveFromShortcuts.Title.v132` — `es-ES/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de los atajos`
    - Inconsistent rendering of the same source term "Shortcuts" within the same Save submenu, where "atajos" is used for the add action.
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `es-ES/firefox-ios.xliff` — "Zoom" is translated as "Tamaño" (size) instead of "Zoom".
    - Current: `Tamaño`
    - Source: `Zoom`
    - Suggest: `Zoom`
    - The source and developer comment refer to the Zoom tool (apply zoom on a page); "Tamaño" means "size" and names a different thing.
- `NativeErrorPage.BadCertDomain.Description.v149` — `es-ES/firefox-ios.xliff` — "your personal info" is rendered as just "tu información", dropping "personal".
    - Current: `podría intentar robar tu información`
    - Source: `Someone pretending to be the site could try to steal your personal info. Your connection settings could also be set up incorrectly.`
    - Suggest: `podría intentar robar tu información personal`
    - The en-US says "steal your personal info"; the qualifier "personal" is omitted.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `es-ES/firefox-ios.xliff` — The app name and company name placeholders are swapped, so the text says "Firefox's marketing partners" and "discovered Mozilla".
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas`
    - Per the comment, %1$@ is the app name (Firefox) and %2$@ is the company name (Mozilla). The source shares with Mozilla's marketing partners how you discovered Firefox; the translation reverses the two.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-ES/firefox-ios.xliff` — Relative clause changes meaning: source says companies are blocked from spying, target says only companies that (already) spy are blocked.
    - Current: `bloqueamos automáticamente a las empresas que espían tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - en-US "block companies from spying on your clicks" means the action of spying is prevented; the Spanish restrictive clause asserts something different about which companies are blocked.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim the source does not make.
    - Current: `la estabilidad para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `la estabilidad para todos`
    - The en-US says features, performance and stability improve "for everyone"; the Spanish adds a geographic scope ("users all over the world") that is not in the source.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says features, performance and stability improve "for everyone"; the Spanish adds a geographic scope ("users all over the world") that the source never states.
- `QRCode.Toolbar.Button.A11y.Title.v128` — `es-ES/firefox-ios.xliff` — Accessibility label for a toolbar button rendered as an imperative command instead of the noun/infinitive form used for button labels.
    - Current: `Escanea el código QR`
    - Source: `Scan QR code`
    - Suggest: `Escanear código QR`
    - The source "Scan QR code" is a button label; es-ES UI convention uses the infinitive for button/accessibility labels (cf. "Resumir página", "Usar máscara de correo electrónico" in this batch), not the second-person imperative.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `es-ES/firefox-ios.xliff` — The translation reverses subject and object: it says "Allow %@ (the app) to be opened?" instead of "Allow %@ (the app) to open [the URL]?".
    - Current: `¿Permitir que se abra %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `¿Permitir que %@ lo abra?`
    - Per the developer comment, the prompt asks permission for the app (%@, e.g. Firefox) to open a URL from a scanned QR code. The Spanish makes the app the thing being opened, which is a different assertion.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-ES/firefox-ios.xliff` — Ungrammatical "Actívalas en a Ajustes" — stray preposition.
    - Current: `Actívalas en a Ajustes del dispositivo`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Actívalas yendo a Ajustes del dispositivo`
    - The source says "Turn them on by going to device Settings"; the Spanish has two stacked prepositions "en a", which is ungrammatical.
- `Settings.Search.GoogleLens.Footnote.v153` — `es-ES/firefox-ios.xliff` — "enabled above" (i.e. in the list above) rendered as "activado en la parte superior" (activated at the top of the screen).
    - Current: `Disponible solo cuando Google está activado en la parte superior y es el buscador activo mientras se navega.`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Disponible solo cuando Google está activado más arriba y es tu buscador activo mientras navegas.`
    - The source refers to the Google toggle appearing above in the same settings page; "activado en la parte superior" misstates this as being enabled at the top, and "your active search engine" loses the possessive.
- `Summarizer.Error.MissingPageContent.Message.v142` — `es-ES/firefox-ios.xliff` — "hit summarize" is rendered as "haz clic en Resumir" (click), which is wrong on a touch phone.
    - Current: `haz clic en Resumir`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `toca Resumir`
    - The source says "hit summarize"; on iOS the interaction is a tap, and the rest of the batch uses "Toca". "Haz clic" instructs a mouse click that does not exist on the device.
- `ContextualHints.Summarize.Description.v142` — `es-ES/firefox-ios.xliff` — "Touch and hold for Reader View" adds "ver" and drops the sense of activating Reader View.
    - Current: `Mantén presionado para ver la vista de lectura`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Mantén presionado para la vista de lectura`
    - The source instructs the user to touch and hold to get Reader View, not to "view the reader view"; the extra verb makes the phrase redundant.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `es-ES/firefox-ios.xliff` — "Enhanced" is attached to the wrong noun, breaking the product name "Protección contra el rastreo mejorada"/ETP and making "configuración" the thing that is enhanced.
    - Current: `Configuración de protección contra el rastreo mejorada para este sitio`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Ajustes de la protección antirrastreo mejorada para este sitio`
    - The source refers to the "Enhanced Tracking Protection" feature setting; as written, the feminine agreement of "mejorada" is ambiguous/attaches to "configuración" rather than to the feature name.
- `WebCompatReporter.SubOption.NoVideo.v154` — `es-ES/firefox-ios.xliff` — "video" is written without the accent used elsewhere in the same screen ("vídeo" in PlaybackFails), an es-ES inconsistency.
    - Current: `No hay video`
    - Source: `There is no video`
    - Suggest: `No hay vídeo`
    - es-ES uses "vídeo"; the sibling string WebCompatReporter.SubOption.PlaybackFails.v154 uses "vídeo" on the same screen.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `es-ES/firefox-ios.xliff` — "Please refresh." is rendered as "actualiza la página" (refresh the page), adding a page that the source never mentions; the widget is refreshed, not a page.
    - Current: `Por favor, actualiza la página.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Por favor, actualiza.`
    - The source says only "Please refresh." referring to the widget's match data, not a web page.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `es-ES/firefox-ios.xliff` — "Penalties" left in English instead of the Spanish football term "Penaltis".
    - Current: `Penalties (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Penaltis (%@)`
    - The source term is a common noun, not a brand; es-ES uses "penaltis" for penalty shoot-out scores.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `es-ES/firefox-ios.xliff` — "BRONZE FINAL" (the match) and "THIRD PLACE" (the winner) are both rendered "TERCER PUESTO", losing the distinction between the two labels in the same widget.
    - Current: `TERCER PUESTO`
    - Source: `BRONZE FINAL`
    - Suggest: `FINAL POR EL TERCER PUESTO`
    - The source distinguishes the bronze-final match label from the third-place winner label; using the identical string for both makes the widget ambiguous. The dev comments explicitly mark one as the match and the other as the winner.
- _…and 1 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (48)

- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `Shared/Supporting Files/en.lproj/AddressToolbar.strings` — The ampersand is kept instead of the Spanish conjunction "y", and "Privacidad"/"Seguridad" are capitalized mid-phrase.
    - Current: `Ajustes de Privacidad & Seguridad`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the "&" symbol is not used as a conjunction; it should be "y". Spanish also uses sentence case for such labels.
- `Bookmarks.DeleteFolderWarning.Description` — `Shared/Supporting Files/en.lproj/BookmarkPanelDeleteConfirm.strings` — Mixed forms of address (tú/usted) within one sentence and missing preposition "de" in "estás seguro que".
    - Current: `¿Estás seguro que desea eliminar esta carpeta y su contenido?`
    - Suggest: `¿Estás seguro de que quieres eliminar esta carpeta y su contenido?`
    - The string starts with the informal "Estás" but then switches to the formal "desea"; also "seguro que" is a queísmo, the correct form is "seguro de que". The rest of the batch uses the informal tú form consistently.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Subject Name" (certificate subject) is translated as "Nombre del asunto" (name of the topic/matter) instead of the certificate term "sujeto".
    - Current: `Nombre del asunto`
    - Suggest: `Nombre del sujeto`
    - In X.509 certificates the "Subject" is the entity the certificate is issued to; the sibling string SubjectAltNames correctly uses "sujeto", making this both wrong and inconsistent within the same screen.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "might log you out of websites" is rendered as an impersonal "puede cerrar sesión en los sitios web", losing the meaning that the user will be logged out.
    - Current: `puede cerrar sesión en los sitios web`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The source says the removal may log the user out; the Spanish as written reads as if the action closes a session generically, omitting the user as the affected party.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — Analytics trackers label translated as "Contenido de rastreo" instead of referring to analytics trackers.
    - Current: `Contenido de rastreo: %@`
    - Suggest: `Rastreadores de analítica: %@`
    - The developer comment says the string reports how many analytics trackers were blocked; "Contenido de rastreo" is the label for a different category (tracking content) and conflicts with the other tracker categories on the same screen.
- `ContextualHints.MainMenu.MenuRedesign.Body.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "settings" is rendered as plural "configuraciones" instead of the standard Firefox term "ajustes".
    - Current: `Marcadores, historial y configuraciones`
    - Suggest: `Marcadores, historial y ajustes`
    - In es-ES Firefox, "Settings" is consistently translated as "Ajustes" (singular collective); "configuraciones" in plural is not the established term and reads as Latin American usage.
- `MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the paired Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Suggest: `Eliminar de los atajos`
    - MainMenu.Submenus.Save.AddToShortcuts.Title/Subtitle translate "Shortcut(s)" as "Atajo"/"atajos"; the same term on the same screen must be consistent.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The placeholders are swapped: %1$@ (app name) and %2$@ (company name) are used in the wrong roles.
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas.`
    - Source: "Share how you discovered %1$@ (app name), and that you use it, with %2$@’s (company name) marketing partners." The translation attributes the marketing partners to the app and says you discovered the company, reversing the two.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "get search suggestions" is translated as "recibir" and the whole clause list is fine, but "Start typing to get" is fine; however "tus sitios principales" etc. — the real issue is none.
    - Current: `Comienza a escribir para recibir sugerencias de búsqueda`
    - Suggest: `Comienza a escribir para obtener sugerencias de búsqueda`
    - Minor wording; source "get" is better rendered as "obtener".
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users worldwide), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Suggest: `para todos`
    - The en-US source says "for everyone", not "for users all over the world"; the translation invents a geographical scope.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Suggest: `para todo el mundo`
    - The en-US text says the data helps improve features, performance and stability "for everyone"; the Spanish adds a geographic claim ("users all over the world") that the source does not make.
- `QRCode.Toolbar.Button.A11y.Title.v128` — `Shared/Supporting Files/en.lproj/QRCode.strings` — Accessibility label uses imperative "Escanea" instead of the infinitive form used consistently for other button labels.
    - Current: `Escanea el código QR`
    - Suggest: `Escanear código QR`
    - Other button/accessibility labels in this batch use the infinitive (e.g. "Resumir página", "Generar una nueva contraseña segura", "Administrar contraseñas"); the imperative here is inconsistent with the established button label register.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — Ungrammatical "Actívalas en a Ajustes" contains a stray preposition.
    - Current: `Actívalas en a Ajustes del dispositivo`
    - Suggest: `Actívalas en Ajustes del dispositivo`
    - The source says "Turn them on by going to device Settings"; "en a" is not valid Spanish.
- `Settings.Search.GoogleLens.Footnote.v153` — `Shared/Supporting Files/en.lproj/Settings.strings` — "enabled above" mistranslated as "activado en la parte superior" (activated at the top).
    - Current: `cuando Google está activado en la parte superior`
    - Suggest: `cuando Google está activado más arriba`
    - The source means Google is enabled in the setting above this one, not that it is 'activated at the top' of something.
- `Summarizer.Error.MissingPageContent.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "hit summarize" is rendered as "haz clic en Resumir" (click), which is wrong on a touch-only iOS device.
    - Current: `haz clic en Resumir`
    - Suggest: `toca Resumir`
    - The source says "hit summarize" on a phone UI; "haz clic" implies a mouse click, inconsistent with the touch wording used elsewhere in the same feature (e.g. "Toca para resumir esta página").
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — Agreement error: "mejorada" modifies "protección" instead of forming the product term "Protección contra el rastreo mejorada" — as written it reads as 'enhanced setting'... actually the adjective is misplaced relative to "Configuración".
    - Current: `Configuración de protección contra el rastreo mejorada para este sitio`
    - Suggest: `Configuración de la protección antirrastreo mejorada para este sitio`
    - "mejorada" can be read as agreeing with "Configuración", making it "enhanced setting" rather than "Enhanced Tracking Protection"; the established Firefox term is "Protección antirrastreo mejorada".
- `WebCompatReporter.SubOption.NoVideo.v154` — `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — "video" is missing the accent used in es-ES and in the sibling string.
    - Current: `No hay video`
    - Suggest: `No hay vídeo`
    - es-ES uses "vídeo"; the related string WebCompatReporter.SubOption.PlaybackFails uses "El vídeo", so this is inconsistent and incorrect for Spain.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Penalties" left in English instead of the Spanish football term "Penaltis".
    - Current: `Finalizado • Penalties (%@)`
    - Suggest: `Finalizado • Penaltis (%@)`
    - "Penalties" is an English word; the es-ES term for a penalty shoot-out score is "penaltis" (or "penaltis"/"tanda de penaltis"), and the rest of the string is translated.
- `DefaultBrowserOnboarding.Screenshot` — `Shared/en.lproj/Default Browser.strings` — Gender agreement error: "predeterminado" should agree with "aplicación".
    - Current: `Aplicación de navegador predeterminado`
    - Suggest: `Aplicación de navegador predeterminada`
    - The iOS setting is "Default Browser App" — the adjective modifies "Aplicación" (feminine), as rendered consistently in DefaultBrowserOnboarding.Description2 ("aplicación de navegador predeterminada").
- `ActivityStream.ContextMenu.UnpinTopsite` — `Shared/en.lproj/Localizable.strings` — "Unpin" translated as "Desanclar" while the paired "Pin" is "Fijar", breaking terminology consistency.
    - Current: `Desanclar`
    - Suggest: `Dejar de fijar`
    - ActivityStream.ContextMenu.PinTopsite2 uses "Fijar" for Pin; the opposite action in the same context menu must use the matching verb.
- `AddPass.Error.Message` — `Shared/en.lproj/Localizable.strings` — The brand name "Wallet" was replaced with the obsolete brand "Passbook".
    - Current: `agregar el pase a Passbook`
    - Suggest: `agregar el pase a Wallet`
    - The en-US source and developer comment refer to Apple's Wallet; the product name must not be changed to Passbook.
- `Address and Search` — `Shared/en.lproj/Localizable.strings` — Singular "Address" rendered as plural "Direcciones".
    - Current: `Direcciones y búsqueda`
    - Suggest: `Dirección y búsqueda`
    - The comment states both words are nouns in singular (Address, Search); the accessibility label refers to the address and search field.
- `ErrorPages.CertWarning.Title` — `Shared/en.lproj/Localizable.strings` — "This Connection is Untrusted" is rendered as "Tu conexión no está verificada" (your connection is not verified), changing the meaning.
    - Current: `Tu conexión no está verificada`
    - Suggest: `Esta conexión no es de confianza`
    - The source says the connection is untrusted, not "not verified", and uses "This", not "Your".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `Shared/en.lproj/Localizable.strings` — "Tab pickup" (feature showing a recent tab from another device) is translated as "Selector de pestañas" (tab selector/picker).
    - Current: `Selector de pestañas`
    - Suggest: `Retomar pestañas`
    - Per the developer comment, this labels the section showing a synced tab from another device to resume, not a tab picker/selector UI.
- `HomePanel.ContextMenu.OpenInNewTab` — `Shared/en.lproj/Localizable.strings` — Unnecessary mid-sentence capitalization of "Nueva" copied from English title case.
    - Current: `Abrir en Nueva pestaña`
    - Suggest: `Abrir en una nueva pestaña`
    - Spanish does not use title case; "Nueva" should be lowercase, matching the sibling string "Abrir en una pestaña privada".
- `Keyboard.Shortcuts.ActualSize` — `Shared/en.lproj/Localizable.strings` — "Actual Size" (i.e. real/original size) translated as "Tamaño actual" (current size).
    - Current: `Tamaño actual`
    - Suggest: `Tamaño real`
    - The comment says the shortcut resets the page view to the standard viewing size; "actual" is a false friend — Spanish "actual" means "current", not "real/original".
- `Logins.Onboarding.LearnMoreButtonTitle` — `Shared/en.lproj/Localizable.strings` — "Learn More" is translated inconsistently as "Aprender más" here while the identical string elsewhere in the same file uses "Saber más".
    - Current: `Aprender más`
    - Suggest: `Saber más`
    - Logins.DevicePasscodeRequired.LearnMoreButtonTitle has the same source and comment ("Learn More" button linking to a support page) and is translated "Saber más"; "Aprender más" is also not the standard Mozilla es-ES rendering.
- `Menu.TrackingProtectionCryptominersBlocked.Title` — `Shared/en.lproj/Localizable.strings` — "Cryptomineros" is an anglicized spelling inconsistent with "criptomineros" used in the description string on the same screen.
    - Current: `Cryptomineros`
    - Suggest: `Criptomineros`
    - Menu.TrackingProtectionDescription.CryptominersNew uses "Los criptomineros"; the Spanish spelling is "cripto-".
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `Shared/en.lproj/Localizable.strings` — "Están configuradas por empresas externas de anuncios y de analítica web" drops "third parties such as", narrowing the meaning.
    - Current: `Están configuradas por empresas externas de anuncios y de analítica web.`
    - Suggest: `Las establecen terceros, como los anunciantes y las empresas de analítica web.`
    - Source says "set by third parties such as advertisers and analytics companies", i.e. advertisers are examples of third parties, not the exhaustive set.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `Shared/en.lproj/Localizable.strings` — Second sentence mistranslated: source says blocking reduces how much social media companies can see, not that "many companies will lose access to your data".
    - Current: `muchas empresas de medios sociales dejarán de tener acceso a tus datos y no podrán ver tus actividades en línea`
    - Suggest: `se reducirá lo que las empresas de redes sociales pueden ver de tu actividad en línea`
    - "Blocking these trackers reduces how much social media companies can see what do you online" expresses a reduction, not a total loss of access by "many" companies.
- `Open Tabs` — `Shared/en.lproj/Localizable.strings` — "Abrir pestañas" reads as the imperative "open tabs"; the string is a sync toggle label meaning currently open tabs.
    - Current: `Abrir pestañas`
    - Suggest: `Pestañas abiertas`
    - Developer comment says "Toggle tabs syncing setting", so "Open Tabs" is a noun phrase for the open tabs being synced.
- `OpenURL.Error.Message` — `Shared/en.lproj/Localizable.strings` — "no pudo encontrar la página" says Firefox could not find the page, while the source says it cannot open the page.
    - Current: `Firefox no pudo encontrar la página porque la dirección no es válida.`
    - Suggest: `Firefox no puede abrir la página porque la dirección no es válida.`
    - Source: "Firefox cannot open the page because it has an invalid address."
- `ScanQRCode.PermissionError.Message.v100` — `Shared/en.lproj/Localizable.strings` — The second sentence uses an infinitive instead of the imperative, breaking the parallel with the first sentence, and "device" is dropped.
    - Current: `Vete a ‘Ajustes’ > ‘Firefox’. Permitir que Firefox acceda a la cámara.`
    - Suggest: `Ve a los ‘Ajustes’ del dispositivo > ‘Firefox’. Permite que Firefox acceda a la cámara.`
    - en-US uses imperative "Allow Firefox to access camera" addressed to the user; the Spanish switches to an impersonal infinitive and omits "device".
- `Search.SuggestSectionTitle.v102` — `Shared/en.lproj/Localizable.strings` — "Firefox Suggest" (a feature/brand name) is rendered as a singular "Sugerencia de Firefox", changing the meaning.
    - Current: `Sugerencia de Firefox`
    - Suggest: `Firefox Suggest`
    - The source is the product feature name "Firefox Suggest" used as a section header; translating it as "Sugerencia de Firefox" (a single suggestion) misnames the feature.
- `SentTab_TabArrivingNotification_NoDevice_body` — `Shared/en.lproj/Localizable.strings` — "New tab arrived from another device" is translated as "agregada" (added) instead of "arrived/received".
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Suggest: `Ha llegado una nueva pestaña desde otro dispositivo.`
    - The source says the tab arrived from another device; "agregada desde" (added from) changes the meaning and is inconsistent with the sibling title "Pestaña recibida".
- `Settings.AddCustomEngine.URLPlaceholder` — `Shared/en.lproj/Localizable.strings` — "Replace Query with %s" is mistranslated as "Cambia búsqueda con %s", losing the instruction to substitute the query term.
    - Current: `URL (Cambia búsqueda con %s)`
    - Suggest: `URL (Reemplaza la búsqueda con %s)`
    - The source instructs the user to replace the query part of the URL with %s; "Cambia búsqueda con" is ambiguous/incorrect Spanish for that instruction.
- `Settings.Home.Option.JumpBackIn` — `Shared/en.lproj/Localizable.strings` — "Jump Back In" (resume browsing where you left off) is rendered as "Saltar hacia atrás" (jump backwards), which conveys the wrong meaning.
    - Current: `Saltar hacia atrás`
    - Suggest: `Retomar donde lo dejaste`
    - The Jump Back In homepage section lets users resume recent tabs; the Spanish literal "Saltar hacia atrás" means physically jumping backwards and does not convey resuming.
- `Settings.Home.Option.StartAtHome.Description` — `Shared/en.lproj/Localizable.strings` — Missing accent on interrogative/relative "qué" in "Elige que ver".
    - Current: `Elige que ver cuando regreses a Firefox.`
    - Suggest: `Elige qué ver cuando regreses a Firefox.`
    - In "Choose what you see", the indirect interrogative "qué" requires a written accent in Spanish.
- `Settings.NewTab.CustomURL` — `Shared/en.lproj/Localizable.strings` — "Custom URL" is translated as an imperative "Personalizar URL" (Customize URL) instead of a noun label.
    - Current: `Personalizar URL`
    - Suggest: `URL personalizada`
    - The source is a label naming the option "Custom URL", not an action to customize a URL; the sibling option Settings.NewTab.Option.Custom uses the adjective "Personalizado".
- `Settings.SendUsage.Message` — `Shared/en.lproj/Localizable.strings` — "provide" is mistranslated as "ejecutar" (run/execute).
    - Current: `para poder ejecutar y mejorar Firefox`
    - Suggest: `para poder ofrecer y mejorar Firefox`
    - The en-US says Mozilla collects what it needs to provide and improve Firefox; "ejecutar" means to run/execute, which changes the meaning.
- `Settings.Studies.Toggle.Link` — `Shared/en.lproj/Localizable.strings` — "Learn More." is rendered as "Aprender más." while the identical source in Settings.SendUsage.Link uses "Descubrir más.", an inconsistency on the same settings screen.
    - Current: `Aprender más.`
    - Suggest: `Descubrir más.`
    - The same source string "Learn More." appears twice in the same settings screen with two different translations.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `Shared/en.lproj/Localizable.strings` — Ungrammatical/mistranslated rendering of "Allows some ad tracking so websites function properly."
    - Current: `Permite a algunas publicidades rastreadoras por lo que los sitios funcionan adecuadamente.`
    - Suggest: `Permite cierto rastreo publicitario para que los sitios funcionen correctamente.`
    - The source says tracking is allowed *so that* sites work; "por lo que" states a consequence, and "Permite a algunas publicidades rastreadoras" is grammatically wrong (dative "a" with no object).
- `Settings.WebsiteData.ConfirmPrompt` — `Shared/en.lproj/Localizable.strings` — Register inconsistency: uses formal "sus" while surrounding strings use the informal "tú" form.
    - Current: `los datos de todos sus sitios`
    - Suggest: `los datos de todos tus sitios`
    - Nearby strings (e.g. Settings.TrackingProtection.Alert.Description: "toca el candado… desactiva…", "para que no te rastreen") use the informal address; this string switches to formal "sus".
- `TopSites.RemovePage.Button` — `Shared/en.lproj/Localizable.strings` — Em dash in the source replaced by a hyphen.
    - Current: `Eliminar página - %@`
    - Suggest: `Eliminar página — %@`
    - The en-US string uses an em dash (—) as separator; the Spanish uses a plain hyphen.
- `TranslationToastHandler.PromptTranslate.Title` — `Shared/en.lproj/Localizable.strings` — The translation prompt misassigns the placeholders: %2$@ is the user's local language (target) and %3$@ is the service name, but the Spanish reads "from %2$@ to %3$@".
    - Current: `¿Quieres traducirla de %2$@ a %3$@?`
    - Suggest: `¿Quieres traducirla a %2$@ con %3$@?`
    - Per the developer comment, %2$@ is the name of the local language and %3$@ is the name of the translation service; the source says "Translate to %2$@ with %3$@?". The translation turns the service name into a target language.
- `Well, this is embarrassing.` — `Shared/en.lproj/Localizable.strings` — "embarazoso" here is fine but the intended sense of embarrassing is mistranslated as awkward-pregnancy false friend risk; actual issue: meaning kept.
    - Current: `Bueno, esto es embarazoso.`
    - Suggest: `Bueno, esto es vergonzoso.`
    - "embarazoso" means awkward/troublesome rather than the intended sense of personal embarrassment; the standard es-ES rendering is "vergonzoso".
- `fxa.signin.qr-link-instruction` — `Shared/en.lproj/Localizable.strings` — "computador" is Latin American usage; es-ES uses "ordenador".
    - Current: `Abre Firefox en tu computador y ve a firefox.com/pair`
    - Suggest: `Abre Firefox en tu ordenador y ve a firefox.com/pair`
    - In Spain, "computer" is rendered as "ordenador"; "computador" is not the es-ES term.
- `%@ on %@` — `Shared/en.lproj/Shared.strings` — "on" is rendered as the German word "war" instead of Spanish "en".
    - Current: `%1$@ war %2$@`
    - Suggest: `%1$@ en %2$@`
    - Source is "%1$@ on %2$@" (app name on device name); "war" is not Spanish and conveys the wrong meaning.

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
| quotes | `straight-double` 6, `curly-double` 4, `curly-single` 2 | _mixed_ |
| apostrophe | `typographic` 2 | **typographic** |
| ellipsis | `char` 22 | **char** |
| dash | `em` 1 | **em** |
| inverted marks | `open-question` 41, `open-exclamation` 8 | **open-question** |
| register | `informal` 153, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (64)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says features, performance and stability improve "for everyone"; the Spanish adds a geographic scope ("users all over the world") that the source never states.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `es-ES/firefox-ios.xliff` — "can make websites load faster" rendered as a certainty ("hará que").
    - Current: `Bloquearlos hará que los sitios web carguen más rápido`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `Bloquearlos puede hacer que los sitios web carguen más rápido`
    - The en-US hedges with "can make"; the Spanish asserts it as a guaranteed outcome.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-ES/firefox-ios.xliff` — The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener acceso a tus datos y…`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de lo que haces en lín…`
    - Source says social networks place trackers on other websites (not so that other sites build a profile), and that blocking reduces how much they can see — not that they will lose access to your data entirely.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 34 |
| 3 | Degraded language (grammar, spelling, terminology) | 28 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `es-ES/firefox-ios.xliff` — The app name and company name placeholders are swapped, so the text says "Firefox's marketing partners" and "discovered Mozilla".
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas`
    - Per the comment, %1$@ is the app name (Firefox) and %2$@ is the company name (Mozilla). The source shares with Mozilla's marketing partners how you discovered Firefox; the translation reverses the two.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Addresses.EditAddress.AutofillAddressSuburb.v129` — `es-ES/firefox-ios.xliff` — "Suburb" as an address administrative division is rendered as "Suburbio", which in Spanish means a poor/marginal outskirts district, not an address field.
    - Current: `Suburbio`
    - Source: `Suburb`
    - Suggest: `Barrio`
    - The developer comment describes an address field for suburb details; es-ES "suburbio" carries a pejorative meaning (slum outskirts) and does not name an address division. "Barrio" (or "Población") is the standard rendering.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `es-ES/firefox-ios.xliff` — "Subject Name" (certificate subject) is rendered as "Nombre del asunto" (subject/topic) instead of the certificate term "sujeto".
    - Current: `Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - In X.509 certificates, "Subject" is the entity the certificate is issued to; the same file already translates "Subject Alt Names" as "Nombres alternativos del sujeto", so "asunto" is both wrong and inconsistent.
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `es-ES/firefox-ios.xliff` — "Zoom" is translated as "Tamaño" (size) instead of "Zoom".
    - Current: `Tamaño`
    - Source: `Zoom`
    - Suggest: `Zoom`
    - The source and developer comment refer to the Zoom tool (apply zoom on a page); "Tamaño" means "size" and names a different thing.
- `NativeErrorPage.BadCertDomain.Description.v149` — `es-ES/firefox-ios.xliff` — "your personal info" is rendered as just "tu información", dropping "personal".
    - Current: `podría intentar robar tu información`
    - Source: `Someone pretending to be the site could try to steal your personal info. Your connection settings could also be set up incorrectly.`
    - Suggest: `podría intentar robar tu información personal`
    - The en-US says "steal your personal info"; the qualifier "personal" is omitted.
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `es-ES/firefox-ios.xliff` — Relative clause changes meaning: source says companies are blocked from spying, target says only companies that (already) spy are blocked.
    - Current: `bloqueamos automáticamente a las empresas que espían tus clics`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
    - en-US "block companies from spying on your clicks" means the action of spying is prevented; the Spanish restrictive clause asserts something different about which companies are blocked.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim the source does not make.
    - Current: `la estabilidad para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `la estabilidad para todos`
    - The en-US says features, performance and stability improve "for everyone"; the Spanish adds a geographic scope ("users all over the world") that is not in the source.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US says features, performance and stability improve "for everyone"; the Spanish adds a geographic scope ("users all over the world") that the source never states.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `es-ES/firefox-ios.xliff` — The translation reverses subject and object: it says "Allow %@ (the app) to be opened?" instead of "Allow %@ (the app) to open [the URL]?".
    - Current: `¿Permitir que se abra %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `¿Permitir que %@ lo abra?`
    - Per the developer comment, the prompt asks permission for the app (%@, e.g. Firefox) to open a URL from a scanned QR code. The Spanish makes the app the thing being opened, which is a different assertion.
- `Settings.Search.GoogleLens.Footnote.v153` — `es-ES/firefox-ios.xliff` — "enabled above" (i.e. in the list above) rendered as "activado en la parte superior" (activated at the top of the screen).
    - Current: `Disponible solo cuando Google está activado en la parte superior y es el buscador activo mientras se navega.`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Disponible solo cuando Google está activado más arriba y es tu buscador activo mientras navegas.`
    - The source refers to the Google toggle appearing above in the same settings page; "activado en la parte superior" misstates this as being enabled at the top, and "your active search engine" loses the possessive.
- `ContextualHints.Summarize.Description.v142` — `es-ES/firefox-ios.xliff` — "Touch and hold for Reader View" adds "ver" and drops the sense of activating Reader View.
    - Current: `Mantén presionado para ver la vista de lectura`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Mantén presionado para la vista de lectura`
    - The source instructs the user to touch and hold to get Reader View, not to "view the reader view"; the extra verb makes the phrase redundant.
- `Summarizer.Error.MissingPageContent.Message.v142` — `es-ES/firefox-ios.xliff` — "hit summarize" is rendered as "haz clic en Resumir" (click), which is wrong on a touch phone.
    - Current: `haz clic en Resumir`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `toca Resumir`
    - The source says "hit summarize"; on iOS the interaction is a tap, and the rest of the batch uses "Toca". "Haz clic" instructs a mouse click that does not exist on the device.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `es-ES/firefox-ios.xliff` — "Enhanced" is attached to the wrong noun, breaking the product name "Protección contra el rastreo mejorada"/ETP and making "configuración" the thing that is enhanced.
    - Current: `Configuración de protección contra el rastreo mejorada para este sitio`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Ajustes de la protección antirrastreo mejorada para este sitio`
    - The source refers to the "Enhanced Tracking Protection" feature setting; as written, the feminine agreement of "mejorada" is ambiguous/attaches to "configuración" rather than to the feature name.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `es-ES/firefox-ios.xliff` — "Please refresh." is rendered as "actualiza la página" (refresh the page), adding a page that the source never mentions; the widget is refreshed, not a page.
    - Current: `Por favor, actualiza la página.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Por favor, actualiza.`
    - The source says only "Please refresh." referring to the widget's match data, not a web page.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `es-ES/firefox-ios.xliff` — "Try refreshing" is rendered as "actualizar la página" (refresh the page), but the widget refreshes match data, not a page.
    - Current: `Intenta actualizar la página en unos minutos.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Intenta actualizar en unos minutos.`
    - The source says "Try refreshing in a few minutes"; the dev comment states the button retries loading match data in the widget, so adding "la página" asserts something the source does not.
- `AddPass.Error.Message` — `es-ES/firefox-ios.xliff` — "Wallet" is rendered as the obsolete brand name "Passbook".
    - Current: `Passbook`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Wallet`
    - The source names Apple's Wallet app; the developer comment explicitly refers to Wallet. "Passbook" is a different (legacy) brand name.
- `Address and Search` — `es-ES/firefox-ios.xliff` — Singular "Address" translated as plural "Direcciones".
    - Current: `Direcciones y búsqueda`
    - Source: `Address and Search`
    - Suggest: `Dirección y búsqueda`
    - The comment states both words are nouns in singular; "Address" refers to the address field, not multiple addresses.
- `BreachAlerts.Description` — `es-ES/firefox-ios.xliff` — "log in to the site" mistranslated as "conéctate en el sitio" with wrong preposition/meaning.
    - Current: `conéctate en el sitio`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `inicia sesión en el sitio`
    - The source instructs the user to log in to the site; "conéctate en el sitio" is not the standard rendering of "log in" and is ungrammatical with "en".
- `ErrorPages.AdvancedWarning2.Text` — `es-ES/firefox-ios.xliff` — "tampering by an attacker" rendered as "una falsificación de un atacante" (a forgery by an attacker).
    - Current: `una falsificación de un atacante`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `una manipulación por parte de un atacante`
    - "Tampering" means manipulation/interference, not forgery/falsification.
- `ErrorPages.CertWarning.Title` — `es-ES/firefox-ios.xliff` — "This Connection is Untrusted" translated as "Tu conexión no está verificada" (not verified) instead of not trusted.
    - Current: `Tu conexión no está verificada`
    - Source: `This Connection is Untrusted`
    - Suggest: `Esta conexión no es de confianza`
    - The source says the connection is untrusted, and uses "This", not "Your"; "no está verificada" changes the meaning.
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `es-ES/firefox-ios.xliff` — "Tab pickup" (feature that resumes tabs from other devices) translated as "Selector de pestañas" (tab picker/selector).
    - Current: `Selector de pestañas`
    - Source: `Tab pickup`
    - Suggest: `Recogida de pestañas`
    - The developer comment explains this labels the section showing a recent tab synced from another device; "Selector de pestañas" describes a tab picker UI, a different thing.
- `Hotkeys.Forward.DiscoveryTitle` — `es-ES/firefox-ios.xliff` — Wrong meaning: "Actual Size" means the original/standard size, not the current one.
    - Current: `Tamaño actual`
    - Source: `Forward`
    - Suggest: `Tamaño real`
    - Per the developer comment, "Actual Size" resets the page view to the standard viewing size; "Tamaño actual" is a false friend meaning "current size".
- `Menu.TrackingProtectionDescription.ContentTrackers` — `es-ES/firefox-ios.xliff` — "can make websites load faster" rendered as a certainty ("hará que").
    - Current: `Bloquearlos hará que los sitios web carguen más rápido`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `Bloquearlos puede hacer que los sitios web carguen más rápido`
    - The en-US hedges with "can make"; the Spanish asserts it as a guaranteed outcome.
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-ES/firefox-ios.xliff` — "set by third parties such as advertisers and analytics companies" narrowed to only advertising and analytics companies.
    - Current: `Están configuradas por empresas externas de anuncios y de analítica web.`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Las establecen terceros, como anunciantes y empresas de analítica web.`
    - The source gives advertisers/analytics as examples of third parties; the translation presents them as the only source.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-ES/firefox-ios.xliff` — The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener acceso a tus datos y…`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de lo que haces en lín…`
    - Source says social networks place trackers on other websites (not so that other sites build a profile), and that blocking reduces how much they can see — not that they will lose access to your data entirely.
- `Open Tabs` — `es-ES/firefox-ios.xliff` — The noun phrase "Open Tabs" (a sync data-type toggle) is translated as the verb phrase "Abrir pestañas".
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - Per the developer comment this toggles syncing of open tabs; the label names the data type, not an action.
- `OpenURL.Error.Message` — `es-ES/firefox-ios.xliff` — "cannot open the page" translated as "no pudo encontrar la página" (could not find).
    - Current: `Firefox no pudo encontrar la página porque la dirección no es válida.`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox no puede abrir la página porque la dirección no es válida.`
    - Source says Firefox cannot open the page, not that it could not find it.
- `ScanQRCode.PermissionError.Message.v100` — `es-ES/firefox-ios.xliff` — "device 'Settings'" is translated as just "'Ajustes'", dropping the reference to the device settings.
    - Current: `Vete a ‘Ajustes’`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Ve a los ‘Ajustes’ del dispositivo`
    - The en-US says to go to the device's Settings app; the word "device" is omitted in the Spanish.
- `Search.SuggestSectionTitle.v102` — `es-ES/firefox-ios.xliff` — "Firefox Suggest" (a feature/brand name) is rendered as "Sugerencia de Firefox", changing a product name into a singular common noun.
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the brand/feature name "Firefox Suggest" used as a section header; brand names must not be translated.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-ES/firefox-ios.xliff` — "arrived from another device" translated as "agregada" (added), losing the meaning of a tab arriving/received.
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Ha llegado una nueva pestaña desde otro dispositivo.`
    - The source says a new tab arrived from another device; "agregada" means it was added, which is a different action.
- `Settings.AddCustomEngine.URLPlaceholder` — `es-ES/firefox-ios.xliff` — "Replace Query with %s" mistranslated as "Cambia búsqueda con %s", losing the instruction to substitute the query term with %s.
    - Current: `URL (Cambia búsqueda con %s)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (Reemplaza la consulta con %s)`
    - The source instructs the user to replace the query part of the URL with %s; "Cambia búsqueda con" is unclear and does not convey substitution of the query string.
- `Settings.Home.Option.JumpBackIn` — `es-ES/firefox-ios.xliff` — "Jump Back In" (resume browsing) rendered as "Saltar hacia atrás" (skip/jump backwards).
    - Current: `Saltar hacia atrás`
    - Source: `Jump Back In`
    - Suggest: `Volver a la carga`
    - The feature name means resuming recent browsing; "Saltar hacia atrás" reads as skipping backwards and does not convey the section's meaning (Firefox uses "Volver a la carga"/"Retomar donde lo dejaste").
- `Settings.NewTab.CustomURL` — `es-ES/firefox-ios.xliff` — "Custom URL" is rendered as an imperative "Personalizar URL" (Customize URL) instead of a noun label.
    - Current: `Personalizar URL`
    - Source: `Custom URL`
    - Suggest: `URL personalizada`
    - The source is a label naming the custom URL option, not a command to customize; the sibling string Settings.NewTab.Option.Custom correctly uses the adjective "Personalizado".
- `Settings.SendUsage.Message` — `es-ES/firefox-ios.xliff` — "provide ... Firefox" mistranslated as "ejecutar" (run/execute) Firefox.
    - Current: `para poder ejecutar y mejorar Firefox`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `para poder ofrecer y mejorar Firefox`
    - The en-US says Mozilla collects only what it needs to provide and improve Firefox; "ejecutar" means to run/execute, which is not the source meaning.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `es-ES/firefox-ios.xliff` — Mistranslation: source says some ad tracking is allowed SO THAT sites work properly; target says "por lo que" (therefore) and adds an incorrect preposition "a".
    - Current: `Permite a algunas publicidades rastreadoras por lo que los sitios funcionan adecuadamente.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Permite cierto rastreo publicitario para que los sitios web funcionen correctamente.`
    - "so websites function properly" expresses purpose (para que), not consequence; "Permite a algunas publicidades rastreadoras" is also ungrammatical.
- `TranslationToastHandler.PromptTranslate.Title` — `es-ES/firefox-ios.xliff` — The translation misassigns placeholders: %2$@ is the target language and %3$@ is the service name, but the Spanish reads "from %2$@ to %3$@".
    - Current: `¿Quieres traducirla de %2$@ a %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `¿Quieres traducirla a %2$@ con %3$@?`
    - Per the comment, %2$@ is the local language and %3$@ is the translation service; the source says "Translate to %2$@ with %3$@", not "from ... to ...".
- `Well, this is embarrassing.` — `es-ES/firefox-ios.xliff` — "embarazoso" is a false-friend-adjacent rendering; acceptable word but the sentence reads oddly—flagged as mistranslation of tone.
    - Current: `Bueno, esto es embarazoso.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `Bueno, esto es un poco vergonzoso.`
    - "embarrassing" here refers to the app's own awkwardness; "embarazoso" in es-ES means awkward/tricky for a situation but is commonly a translation artifact; "vergonzoso" conveys the intended tone.
- `%@ on %@` — `es-ES/firefox-ios.xliff` — The connector word is left in German ("war") instead of Spanish "en".
    - Current: `%1$@ war %2$@`
    - Source: `%1$@ on %2$@`
    - Suggest: `%1$@ en %2$@`
    - Source is "%1$@ on %2$@" (app name on device name); "war" is not Spanish and conveys no meaning here.
- `w9jdPK` — `es-ES/firefox-ios.xliff` — Singular 'Quick Action' is rendered in the plural, inconsistent with the identical source string eqyNJg.
    - Current: `Acciones rápidas`
    - Source: `Quick Action`
    - Suggest: `Acción rápida`
    - The source is singular 'Quick Action' (the label for the dropdown selecting one action), and eqyNJg with the same source is translated "Acción rápida".

### C. Grammar, agreement & spelling

- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-ES/firefox-ios.xliff` — Ampersand left untranslated and capitalization copied from English in "Ajustes de Privacidad & Seguridad".
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the English "&" must be rendered as "y", and common nouns are not capitalized mid-sentence as in English title case.
- `Bookmarks.DeleteFolderWarning.Description` — `es-ES/firefox-ios.xliff` — Register inconsistency and missing preposition: "¿Estás seguro que desea..." mixes informal "estás" with formal "desea" and omits "de".
    - Current: `¿Estás seguro que desea eliminar esta carpeta y su contenido?`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Seguro que quieres eliminar esta carpeta y su contenido?`
    - The locale uses the informal register; "desea" is formal and clashes with "estás". Also "seguro que" after "estar seguro" requires "de que" (queísmo).
- `Bookmarks.EmptyState.Root.Body.v135` — `es-ES/firefox-ios.xliff` — "Save sites as you browse" is rendered with an infinitive instead of the imperative used elsewhere.
    - Current: `Guardar sitios mientras navegas.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `Guarda sitios mientras navegas.`
    - The source is an imperative addressed to the user, consistent with the informal register and with the sibling string; "Guardar" is an infinitive and reads as a label rather than an instruction.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `es-ES/firefox-ios.xliff` — "Save sites as you browse" is rendered with an infinitive instead of the imperative.
    - Current: `Guardar sitios mientras navegas.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `Guarda sitios mientras navegas.`
    - The source is an imperative addressed to the user, matching "Inicia sesión" in the same string; the infinitive is inconsistent.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-ES/firefox-ios.xliff` — "might log you out of websites" is rendered impersonally, losing the reference to the user's own sessions.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The en-US says the action may log *you* out; the Spanish as written lacks the possessive and reads as the sites closing a session generically.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-ES/firefox-ios.xliff` — Ungrammatical "Actívalas en a Ajustes" — stray preposition.
    - Current: `Actívalas en a Ajustes del dispositivo`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Actívalas yendo a Ajustes del dispositivo`
    - The source says "Turn them on by going to device Settings"; the Spanish has two stacked prepositions "en a", which is ungrammatical.
- `DefaultBrowserOnboarding.Screenshot` — `es-ES/firefox-ios.xliff` — Gender agreement error: "predeterminado" should agree with "Aplicación".
    - Current: `Aplicación de navegador predeterminado`
    - Source: `Default Browser App`
    - Suggest: `Aplicación de navegador predeterminada`
    - The en-US "Default Browser App" refers to the app (feminine "aplicación"); the parallel string DefaultBrowserOnboarding.Description2 uses "aplicación de navegador predeterminada", so the masculine form here is inconsistent and wrong.
- `Menu.TrackingProtectionCryptominersBlocked.Title` — `es-ES/firefox-ios.xliff` — "Cryptomineros" is a misspelling; the description string in the same screen uses "criptomineros".
    - Current: `Cryptomineros`
    - Source: `Cryptominers`
    - Suggest: `Criptomineros`
    - Spanish spelling is "criptomineros", as used in Menu.TrackingProtectionDescription.CryptominersNew on the same screen.
- `ScanQRCode.PermissionError.Message.v100` — `es-ES/firefox-ios.xliff` — Second sentence uses an infinitive instead of the imperative, breaking parallelism with the first sentence and the informal register.
    - Current: `Permitir que Firefox acceda a la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Permite que Firefox acceda a la cámara.`
    - The source "Allow Firefox to access camera." is an instruction to the user; the first sentence is translated with the informal imperative ("Vete"), so the second should be too.
- `Settings.Home.Option.StartAtHome.Description` — `es-ES/firefox-ios.xliff` — Interrogative "qué" is missing its accent in "Elige que ver".
    - Current: `Elige que ver cuando regreses a Firefox.`
    - Source: `Choose what you see when you return to Firefox.`
    - Suggest: `Elige qué ver cuando regreses a Firefox.`
    - "Choose what you see" requires the accented interrogative pronoun "qué".

### D. Terminology, register & consistency

- `ContextualHints.MainMenu.MenuRedesign.Body.v142` — `es-ES/firefox-ios.xliff` — "settings" rendered as plural "configuraciones"; the app's Settings menu is "Ajustes"/"Configuración" in es-ES.
    - Current: `Marcadores, historial y configuraciones`
    - Source: `Bookmarks, history, and settings — all at your fingertips.`
    - Suggest: `Marcadores, historial y ajustes`
    - In en-US "settings" refers to the app's Settings section, which is consistently "Ajustes" in es-ES Firefox; the plural "configuraciones" is not the product term.
- `MainMenu.Submenus.Save.AccessibilityLabels.RemoveFromShortcuts.Title.v132` — `es-ES/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de los atajos`
    - Inconsistent rendering of the same source term "Shortcuts" within the same Save submenu, where "atajos" is used for the add action.
- `MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131` — `es-ES/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de los atajos`
    - The same source term "Shortcuts" must be consistent within the Save submenu; MainMenu.Submenus.Save.AddToShortcuts.Title.v131 uses "Añadir a atajos" and its subtitle uses "Atajo".
- `QRCode.Toolbar.Button.A11y.Title.v128` — `es-ES/firefox-ios.xliff` — Accessibility label for a toolbar button rendered as an imperative command instead of the noun/infinitive form used for button labels.
    - Current: `Escanea el código QR`
    - Source: `Scan QR code`
    - Suggest: `Escanear código QR`
    - The source "Scan QR code" is a button label; es-ES UI convention uses the infinitive for button/accessibility labels (cf. "Resumir página", "Usar máscara de correo electrónico" in this batch), not the second-person imperative.
- `WebCompatReporter.SubOption.NoVideo.v154` — `es-ES/firefox-ios.xliff` — "video" is written without the accent used elsewhere in the same screen ("vídeo" in PlaybackFails), an es-ES inconsistency.
    - Current: `No hay video`
    - Source: `There is no video`
    - Suggest: `No hay vídeo`
    - es-ES uses "vídeo"; the sibling string WebCompatReporter.SubOption.PlaybackFails.v154 uses "vídeo" on the same screen.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `es-ES/firefox-ios.xliff` — "Penalties" left in English instead of the Spanish football term "Penaltis".
    - Current: `Penalties (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Penaltis (%@)`
    - The source term is a common noun, not a brand; es-ES uses "penaltis" for penalty shoot-out scores.
- `WorldCup.HomepageWidget.RoundPhase.BronzeFinalLabel.v151` — `es-ES/firefox-ios.xliff` — "BRONZE FINAL" (the match) and "THIRD PLACE" (the winner) are both rendered "TERCER PUESTO", losing the distinction between the two labels in the same widget.
    - Current: `TERCER PUESTO`
    - Source: `BRONZE FINAL`
    - Suggest: `FINAL POR EL TERCER PUESTO`
    - The source distinguishes the bronze-final match label from the third-place winner label; using the identical string for both makes the widget ambiguous. The dev comments explicitly mark one as the match and the other as the winner.
- `ActivityStream.ContextMenu.UnpinTopsite` — `es-ES/firefox-ios.xliff` — "Unpin" is translated as "Desanclar" while the paired "Pin" is "Fijar", breaking terminology consistency.
    - Current: `Desanclar`
    - Source: `Unpin`
    - Suggest: `Dejar de fijar`
    - ActivityStream.ContextMenu.PinTopsite2 renders "Pin" as "Fijar"; the opposite action in the same context menu must use the same verb.
- `Logins.Onboarding.LearnMoreButtonTitle` — `es-ES/firefox-ios.xliff` — "Learn More" is rendered as "Aprender más" while the identical source string elsewhere in the same file uses "Saber más".
    - Current: `Aprender más`
    - Source: `Learn More`
    - Suggest: `Saber más`
    - Logins.DevicePasscodeRequired.LearnMoreButtonTitle has the same source and same developer comment but is translated "Saber más"; "Aprender más" is a literal rendering inconsistent with the established Firefox term.
- `Settings.Studies.Toggle.Link` — `es-ES/firefox-ios.xliff` — "Learn More." rendered as "Aprender más." while the identical source elsewhere in the same screen uses "Descubrir más."
    - Current: `Aprender más.`
    - Source: `Learn More.`
    - Suggest: `Descubrir más.`
    - Settings.SendUsage.Link translates the same source string as "Descubrir más."; inconsistent rendering of the same link label on the same settings screen.
- `Settings.WebsiteData.ConfirmPrompt` — `es-ES/firefox-ios.xliff` — Formal address "sus" used where the locale convention is informal (tú).
    - Current: `Esta acción eliminará los datos de todos sus sitios.`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `Esta acción eliminará los datos de todos tus sitios.`
    - es-ES convention is informal address; other strings in this batch use "toca", "no has visto", "te rastreen".
- `fxa.signin.qr-link-instruction` — `es-ES/firefox-ios.xliff` — "computador" is Latin American usage; es-ES uses "ordenador".
    - Current: `Abre Firefox en tu computador y ve a firefox.com/pair`
    - Source: `On your computer open Firefox and go to firefox.com/pair`
    - Suggest: `Abre Firefox en tu ordenador y ve a firefox.com/pair`
    - Source "your computer"; the Spain locale term is "ordenador", not the American "computador".
- `fi3W24-eHmH1H` — `es-ES/firefox-ios.xliff` — The menu item 'Clear Private Tabs' is translated as "Eliminar pestañas privadas" elsewhere but as "Borrar pestañas privadas" here, an inconsistency within the same feature.
    - Current: `Borrar pestañas privadas`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `Eliminar pestañas privadas`
    - String eHmH1H and PzSrmZ-eHmH1H render 'Clear Private Tabs' as "Eliminar pestañas privadas"; this confirmation label must quote the same option name.

### E. Typography, punctuation & spacing

- `TopSites.RemovePage.Button` — `es-ES/firefox-ios.xliff` — Em dash in the source replaced with a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The locale convention is the em dash, and the source uses an em dash separator.
- `PzSrmZ-2GqvPe` — `es-ES/firefox-ios.xliff` — Straight double quotes used instead of the typographic quotes present in the source.
    - Current: `"Ir al enlace copiado"`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `«Ir al enlace copiado»`
    - The en-US source uses curly single quotes ‘…’; es-ES convention uses angular or curly quotes, not straight ASCII quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-ES/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
