# Firefox iOS l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **Previous run** | 2026-08-22 @ `112744e9d020` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,815 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-ES: [android](android.md) · [firefox](firefox.md)

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
| Files | 91 |
| Strings | 1,815 |
| Missing strings | 95 |
| Obsolete strings | 0 |
| Files absent from the locale | 4 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**95 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — 49
- `es-ES/firefox-ios.xliff` — 11
- `es-ES/firefox-ios.xliff` — 9
- `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — 7
- `es-ES/firefox-ios.xliff` — 5
- `es-ES/firefox-ios.xliff` — 3
- `es-ES/firefox-ios.xliff` — 3
- `es-ES/firefox-ios.xliff` — 2
- `es-ES/firefox-ios.xliff` — 2
- `es-ES/firefox-ios.xliff` — 1
- `es-ES/firefox-ios.xliff` — 1
- `Shared/Supporting Files/en.lproj/Camera.strings` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en.lproj/Camera.strings`
- `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings`
- `Shared/Supporting Files/en.lproj/WebCompatReporter.strings`
- `Shared/Supporting Files/en.lproj/WebContextMenu.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 6, `curly-double` 4, `curly-single` 2 | _mixed_ |
| apostrophe | `typographic` 2 | **typographic** |
| ellipsis | `char` 17 | **char** |
| dash | `em` 1 | **em** |
| inverted marks | `open-question` 41, `open-exclamation` 8 | **open-question** |
| register | `informal` 139, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (48)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 26 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `es-ES/firefox-ios.xliff` — The placeholders are swapped: %1$@ (app name) and %2$@ (company name) are used in the wrong roles.
    - Current: `Comparte con los socios de marketing de %1$@ cómo descubriste %2$@ y cómo lo usas.`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `Comparte con los socios de marketing de %2$@ cómo descubriste %1$@ y que lo usas.`
    - Source: "Share how you discovered %1$@ (app name), and that you use it, with %2$@’s (company name) marketing partners." The translation attributes the marketing partners to the app and says you discovered the company, reversing the two.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `es-ES/firefox-ios.xliff` — "Subject Name" (certificate subject) is translated as "Nombre del asunto" (name of the topic/matter) instead of the certificate term "sujeto".
    - Current: `Nombre del asunto`
    - Source: `Subject Name`
    - Suggest: `Nombre del sujeto`
    - In X.509 certificates the "Subject" is the entity the certificate is issued to; the sibling string SubjectAltNames correctly uses "sujeto", making this both wrong and inconsistent within the same screen.
- `Menu.EnhancedTrackingProtection.ClearData.AlertText.v128` — `es-ES/firefox-ios.xliff` — "might log you out of websites" is rendered as an impersonal "puede cerrar sesión en los sitios web", losing the meaning that the user will be logged out.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for %@ might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - The source says the removal may log the user out; the Spanish as written reads as if the action closes a session generically, omitting the user as the affected party.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `es-ES/firefox-ios.xliff` — "get search suggestions" is translated as "recibir" and the whole clause list is fine, but "Start typing to get" is fine; however "tus sitios principales" etc. — the real issue is none.
    - Current: `Comienza a escribir para recibir sugerencias de búsqueda`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `Comienza a escribir para obtener sugerencias de búsqueda`
    - Minor wording; source "get" is better rendered as "obtener".
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users worldwide), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todos`
    - The en-US source says "for everyone", not "for users all over the world"; the translation invents a geographical scope.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `es-ES/firefox-ios.xliff` — "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding meaning not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `para todo el mundo`
    - The en-US text says the data helps improve features, performance and stability "for everyone"; the Spanish adds a geographic claim ("users all over the world") that the source does not make.
- `Summarizer.Error.MissingPageContent.Message.v142` — `es-ES/firefox-ios.xliff` — "hit summarize" is rendered as "haz clic en Resumir" (click), which is wrong on a touch-only iOS device.
    - Current: `haz clic en Resumir`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `toca Resumir`
    - The source says "hit summarize" on a phone UI; "haz clic" implies a mouse click, inconsistent with the touch wording used elsewhere in the same feature (e.g. "Toca para resumir esta página").
- `AddPass.Error.Message` — `es-ES/firefox-ios.xliff` — The brand name "Wallet" was replaced with the obsolete brand "Passbook".
    - Current: `agregar el pase a Passbook`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `agregar el pase a Wallet`
    - The en-US source and developer comment refer to Apple's Wallet; the product name must not be changed to Passbook.
- `Address and Search` — `es-ES/firefox-ios.xliff` — Singular "Address" rendered as plural "Direcciones".
    - Current: `Direcciones y búsqueda`
    - Source: `Address and Search`
    - Suggest: `Dirección y búsqueda`
    - The comment states both words are nouns in singular (Address, Search); the accessibility label refers to the address and search field.
- `ErrorPages.CertWarning.Title` — `es-ES/firefox-ios.xliff` — "This Connection is Untrusted" is rendered as "Tu conexión no está verificada" (your connection is not verified), changing the meaning.
    - Current: `Tu conexión no está verificada`
    - Source: `This Connection is Untrusted`
    - Suggest: `Esta conexión no es de confianza`
    - The source says the connection is untrusted, not "not verified", and uses "This", not "Your".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `es-ES/firefox-ios.xliff` — "Tab pickup" (feature showing a recent tab from another device) is translated as "Selector de pestañas" (tab selector/picker).
    - Current: `Selector de pestañas`
    - Source: `Tab pickup`
    - Suggest: `Retomar pestañas`
    - Per the developer comment, this labels the section showing a synced tab from another device to resume, not a tab picker/selector UI.
- `Keyboard.Shortcuts.ActualSize` — `es-ES/firefox-ios.xliff` — "Actual Size" (i.e. real/original size) translated as "Tamaño actual" (current size).
    - Current: `Tamaño actual`
    - Source: `Actual Size`
    - Suggest: `Tamaño real`
    - The comment says the shortcut resets the page view to the standard viewing size; "actual" is a false friend — Spanish "actual" means "current", not "real/original".
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `es-ES/firefox-ios.xliff` — "Están configuradas por empresas externas de anuncios y de analítica web" drops "third parties such as", narrowing the meaning.
    - Current: `Están configuradas por empresas externas de anuncios y de analítica web.`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Las establecen terceros, como los anunciantes y las empresas de analítica web.`
    - Source says "set by third parties such as advertisers and analytics companies", i.e. advertisers are examples of third parties, not the exhaustive set.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `es-ES/firefox-ios.xliff` — Second sentence mistranslated: source says blocking reduces how much social media companies can see, not that "many companies will lose access to your data".
    - Current: `muchas empresas de medios sociales dejarán de tener acceso a tus datos y no podrán ver tus actividades en línea`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `se reducirá lo que las empresas de redes sociales pueden ver de tu actividad en línea`
    - "Blocking these trackers reduces how much social media companies can see what do you online" expresses a reduction, not a total loss of access by "many" companies.
- `Open Tabs` — `es-ES/firefox-ios.xliff` — "Abrir pestañas" reads as the imperative "open tabs"; the string is a sync toggle label meaning currently open tabs.
    - Current: `Abrir pestañas`
    - Source: `Open Tabs`
    - Suggest: `Pestañas abiertas`
    - Developer comment says "Toggle tabs syncing setting", so "Open Tabs" is a noun phrase for the open tabs being synced.
- `OpenURL.Error.Message` — `es-ES/firefox-ios.xliff` — "no pudo encontrar la página" says Firefox could not find the page, while the source says it cannot open the page.
    - Current: `Firefox no pudo encontrar la página porque la dirección no es válida.`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox no puede abrir la página porque la dirección no es válida.`
    - Source: "Firefox cannot open the page because it has an invalid address."
- `Search.SuggestSectionTitle.v102` — `es-ES/firefox-ios.xliff` — "Firefox Suggest" (a feature/brand name) is rendered as a singular "Sugerencia de Firefox", changing the meaning.
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - The source is the product feature name "Firefox Suggest" used as a section header; translating it as "Sugerencia de Firefox" (a single suggestion) misnames the feature.
- `SentTab_TabArrivingNotification_NoDevice_body` — `es-ES/firefox-ios.xliff` — "New tab arrived from another device" is translated as "agregada" (added) instead of "arrived/received".
    - Current: `Nueva pestaña agregada desde otro dispositivo.`
    - Source: `New tab arrived from another device.`
    - Suggest: `Ha llegado una nueva pestaña desde otro dispositivo.`
    - The source says the tab arrived from another device; "agregada desde" (added from) changes the meaning and is inconsistent with the sibling title "Pestaña recibida".
- `Settings.AddCustomEngine.URLPlaceholder` — `es-ES/firefox-ios.xliff` — "Replace Query with %s" is mistranslated as "Cambia búsqueda con %s", losing the instruction to substitute the query term.
    - Current: `URL (Cambia búsqueda con %s)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (Reemplaza la búsqueda con %s)`
    - The source instructs the user to replace the query part of the URL with %s; "Cambia búsqueda con" is ambiguous/incorrect Spanish for that instruction.
- `Settings.Home.Option.JumpBackIn` — `es-ES/firefox-ios.xliff` — "Jump Back In" (resume browsing where you left off) is rendered as "Saltar hacia atrás" (jump backwards), which conveys the wrong meaning.
    - Current: `Saltar hacia atrás`
    - Source: `Jump Back In`
    - Suggest: `Retomar donde lo dejaste`
    - The Jump Back In homepage section lets users resume recent tabs; the Spanish literal "Saltar hacia atrás" means physically jumping backwards and does not convey resuming.
- `Settings.NewTab.CustomURL` — `es-ES/firefox-ios.xliff` — "Custom URL" is translated as an imperative "Personalizar URL" (Customize URL) instead of a noun label.
    - Current: `Personalizar URL`
    - Source: `Custom URL`
    - Suggest: `URL personalizada`
    - The source is a label naming the option "Custom URL", not an action to customize a URL; the sibling option Settings.NewTab.Option.Custom uses the adjective "Personalizado".
- `Settings.SendUsage.Message` — `es-ES/firefox-ios.xliff` — "provide" is mistranslated as "ejecutar" (run/execute).
    - Current: `para poder ejecutar y mejorar Firefox`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `para poder ofrecer y mejorar Firefox`
    - The en-US says Mozilla collects what it needs to provide and improve Firefox; "ejecutar" means to run/execute, which changes the meaning.
- `TranslationToastHandler.PromptTranslate.Title` — `es-ES/firefox-ios.xliff` — The translation prompt misassigns the placeholders: %2$@ is the user's local language (target) and %3$@ is the service name, but the Spanish reads "from %2$@ to %3$@".
    - Current: `¿Quieres traducirla de %2$@ a %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `¿Quieres traducirla a %2$@ con %3$@?`
    - Per the developer comment, %2$@ is the name of the local language and %3$@ is the name of the translation service; the source says "Translate to %2$@ with %3$@?". The translation turns the service name into a target language.
- `Well, this is embarrassing.` — `es-ES/firefox-ios.xliff` — "embarazoso" here is fine but the intended sense of embarrassing is mistranslated as awkward-pregnancy false friend risk; actual issue: meaning kept.
    - Current: `Bueno, esto es embarazoso.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `Bueno, esto es vergonzoso.`
    - "embarazoso" means awkward/troublesome rather than the intended sense of personal embarrassment; the standard es-ES rendering is "vergonzoso".
- `%@ on %@` — `es-ES/firefox-ios.xliff` — "on" is rendered as the German word "war" instead of Spanish "en".
    - Current: `%1$@ war %2$@`
    - Source: `%1$@ on %2$@`
    - Suggest: `%1$@ en %2$@`
    - Source is "%1$@ on %2$@" (app name on device name); "war" is not Spanish and conveys the wrong meaning.
- `w9jdPK` — `es-ES/firefox-ios.xliff` — Singular 'Quick Action' is rendered in the plural, inconsistent with the identical source string eqyNJg.
    - Current: `Acciones rápidas`
    - Source: `Quick Action`
    - Suggest: `Acción rápida`
    - The source is singular 'Quick Action' (the label for the dropdown selecting one action), and eqyNJg with the same source is translated "Acción rápida".

### C. Grammar, agreement & spelling

- `Bookmarks.DeleteFolderWarning.Description` — `es-ES/firefox-ios.xliff` — Mixed forms of address (tú/usted) within one sentence and missing preposition "de" in "estás seguro que".
    - Current: `¿Estás seguro que desea eliminar esta carpeta y su contenido?`
    - Source: `Are you sure you want to delete it and its contents?`
    - Suggest: `¿Estás seguro de que quieres eliminar esta carpeta y su contenido?`
    - The string starts with the informal "Estás" but then switches to the formal "desea"; also "seguro que" is a queísmo, the correct form is "seguro de que". The rest of the batch uses the informal tú form consistently.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `es-ES/firefox-ios.xliff` — Ungrammatical "Actívalas en a Ajustes" contains a stray preposition.
    - Current: `Actívalas en a Ajustes del dispositivo`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Actívalas en Ajustes del dispositivo`
    - The source says "Turn them on by going to device Settings"; "en a" is not valid Spanish.
- `DefaultBrowserOnboarding.Screenshot` — `es-ES/firefox-ios.xliff` — Gender agreement error: "predeterminado" should agree with "aplicación".
    - Current: `Aplicación de navegador predeterminado`
    - Source: `Default Browser App`
    - Suggest: `Aplicación de navegador predeterminada`
    - The iOS setting is "Default Browser App" — the adjective modifies "Aplicación" (feminine), as rendered consistently in DefaultBrowserOnboarding.Description2 ("aplicación de navegador predeterminada").
- `Menu.TrackingProtectionCryptominersBlocked.Title` — `es-ES/firefox-ios.xliff` — "Cryptomineros" is an anglicized spelling inconsistent with "criptomineros" used in the description string on the same screen.
    - Current: `Cryptomineros`
    - Source: `Cryptominers`
    - Suggest: `Criptomineros`
    - Menu.TrackingProtectionDescription.CryptominersNew uses "Los criptomineros"; the Spanish spelling is "cripto-".
- `ScanQRCode.PermissionError.Message.v100` — `es-ES/firefox-ios.xliff` — The second sentence uses an infinitive instead of the imperative, breaking the parallel with the first sentence, and "device" is dropped.
    - Current: `Vete a ‘Ajustes’ > ‘Firefox’. Permitir que Firefox acceda a la cámara.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Ve a los ‘Ajustes’ del dispositivo > ‘Firefox’. Permite que Firefox acceda a la cámara.`
    - en-US uses imperative "Allow Firefox to access camera" addressed to the user; the Spanish switches to an impersonal infinitive and omits "device".
- `Settings.Home.Option.StartAtHome.Description` — `es-ES/firefox-ios.xliff` — Missing accent on interrogative/relative "qué" in "Elige que ver".
    - Current: `Elige que ver cuando regreses a Firefox.`
    - Source: `Choose what you see when you return to Firefox.`
    - Suggest: `Elige qué ver cuando regreses a Firefox.`
    - In "Choose what you see", the indirect interrogative "qué" requires a written accent in Spanish.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `es-ES/firefox-ios.xliff` — Ungrammatical/mistranslated rendering of "Allows some ad tracking so websites function properly."
    - Current: `Permite a algunas publicidades rastreadoras por lo que los sitios funcionan adecuadamente.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Permite cierto rastreo publicitario para que los sitios funcionen correctamente.`
    - The source says tracking is allowed *so that* sites work; "por lo que" states a consequence, and "Permite a algunas publicidades rastreadoras" is grammatically wrong (dative "a" with no object).

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `es-ES/firefox-ios.xliff` — Analytics trackers label translated as "Contenido de rastreo" instead of referring to analytics trackers.
    - Current: `Contenido de rastreo: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Rastreadores de analítica: %@`
    - The developer comment says the string reports how many analytics trackers were blocked; "Contenido de rastreo" is the label for a different category (tracking content) and conflicts with the other tracker categories on the same screen.
- `ContextualHints.MainMenu.MenuRedesign.Body.v142` — `es-ES/firefox-ios.xliff` — "settings" is rendered as plural "configuraciones" instead of the standard Firefox term "ajustes".
    - Current: `Marcadores, historial y configuraciones`
    - Source: `Bookmarks, history, and settings — all at your fingertips.`
    - Suggest: `Marcadores, historial y ajustes`
    - In es-ES Firefox, "Settings" is consistently translated as "Ajustes" (singular collective); "configuraciones" in plural is not the established term and reads as Latin American usage.
- `MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131` — `es-ES/firefox-ios.xliff` — "Shortcuts" is rendered as "accesos directos" here but as "atajos" in the paired Add to Shortcuts strings on the same submenu.
    - Current: `Eliminar de los accesos directos`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eliminar de los atajos`
    - MainMenu.Submenus.Save.AddToShortcuts.Title/Subtitle translate "Shortcut(s)" as "Atajo"/"atajos"; the same term on the same screen must be consistent.
- `QRCode.Toolbar.Button.A11y.Title.v128` — `es-ES/firefox-ios.xliff` — Accessibility label uses imperative "Escanea" instead of the infinitive form used consistently for other button labels.
    - Current: `Escanea el código QR`
    - Source: `Scan QR code`
    - Suggest: `Escanear código QR`
    - Other button/accessibility labels in this batch use the infinitive (e.g. "Resumir página", "Generar una nueva contraseña segura", "Administrar contraseñas"); the imperative here is inconsistent with the established button label register.
- `WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151` — `es-ES/firefox-ios.xliff` — "Penalties" left in English instead of the Spanish football term "Penaltis".
    - Current: `Finalizado • Penalties (%@)`
    - Source: `Full time • Penalties (%@)`
    - Suggest: `Finalizado • Penaltis (%@)`
    - "Penalties" is an English word; the es-ES term for a penalty shoot-out score is "penaltis" (or "penaltis"/"tanda de penaltis"), and the rest of the string is translated.
- `ActivityStream.ContextMenu.UnpinTopsite` — `es-ES/firefox-ios.xliff` — "Unpin" translated as "Desanclar" while the paired "Pin" is "Fijar", breaking terminology consistency.
    - Current: `Desanclar`
    - Source: `Unpin`
    - Suggest: `Dejar de fijar`
    - ActivityStream.ContextMenu.PinTopsite2 uses "Fijar" for Pin; the opposite action in the same context menu must use the matching verb.
- `Logins.Onboarding.LearnMoreButtonTitle` — `es-ES/firefox-ios.xliff` — "Learn More" is translated inconsistently as "Aprender más" here while the identical string elsewhere in the same file uses "Saber más".
    - Current: `Aprender más`
    - Source: `Learn More`
    - Suggest: `Saber más`
    - Logins.DevicePasscodeRequired.LearnMoreButtonTitle has the same source and comment ("Learn More" button linking to a support page) and is translated "Saber más"; "Aprender más" is also not the standard Mozilla es-ES rendering.
- `Settings.Studies.Toggle.Link` — `es-ES/firefox-ios.xliff` — "Learn More." is rendered as "Aprender más." while the identical source in Settings.SendUsage.Link uses "Descubrir más.", an inconsistency on the same settings screen.
    - Current: `Aprender más.`
    - Source: `Learn More.`
    - Suggest: `Descubrir más.`
    - The same source string "Learn More." appears twice in the same settings screen with two different translations.
- `Settings.WebsiteData.ConfirmPrompt` — `es-ES/firefox-ios.xliff` — Register inconsistency: uses formal "sus" while surrounding strings use the informal "tú" form.
    - Current: `los datos de todos sus sitios`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `los datos de todos tus sitios`
    - Nearby strings (e.g. Settings.TrackingProtection.Alert.Description: "toca el candado… desactiva…", "para que no te rastreen") use the informal address; this string switches to formal "sus".
- `fxa.signin.qr-link-instruction` — `es-ES/firefox-ios.xliff` — "computador" is Latin American usage; es-ES uses "ordenador".
    - Current: `Abre Firefox en tu computador y ve a firefox.com/pair`
    - Source: `On your computer open Firefox and go to firefox.com/pair`
    - Suggest: `Abre Firefox en tu ordenador y ve a firefox.com/pair`
    - In Spain, "computer" is rendered as "ordenador"; "computador" is not the es-ES term.
- `fi3W24-eHmH1H` — `es-ES/firefox-ios.xliff` — The menu item 'Clear Private Tabs' is translated as "Eliminar pestañas privadas" elsewhere but as "Borrar pestañas privadas" here, an inconsistency within the same feature.
    - Current: `Borrar pestañas privadas`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `Eliminar pestañas privadas`
    - String eHmH1H and PzSrmZ-eHmH1H render 'Clear Private Tabs' as "Eliminar pestañas privadas"; this confirmation label must quote the same option name.

### E. Typography, punctuation & spacing

- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `es-ES/firefox-ios.xliff` — The ampersand is kept instead of the Spanish conjunction "y", and "Privacidad"/"Seguridad" are capitalized mid-phrase.
    - Current: `Ajustes de Privacidad & Seguridad`
    - Source: `Privacy & Security Settings`
    - Suggest: `Ajustes de privacidad y seguridad`
    - In Spanish the "&" symbol is not used as a conjunction; it should be "y". Spanish also uses sentence case for such labels.
- `HomePanel.ContextMenu.OpenInNewTab` — `es-ES/firefox-ios.xliff` — Unnecessary mid-sentence capitalization of "Nueva" copied from English title case.
    - Current: `Abrir en Nueva pestaña`
    - Source: `Open in New Tab`
    - Suggest: `Abrir en una nueva pestaña`
    - Spanish does not use title case; "Nueva" should be lowercase, matching the sibling string "Abrir en una pestaña privada".
- `TopSites.RemovePage.Button` — `es-ES/firefox-ios.xliff` — Em dash in the source replaced by a hyphen.
    - Current: `Eliminar página - %@`
    - Source: `Remove page — %@`
    - Suggest: `Eliminar página — %@`
    - The en-US string uses an em dash (—) as separator; the Spanish uses a plain hyphen.
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
