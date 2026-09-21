# Firefox iOS l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,922 |

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
| Files | 96 |
| Strings | 1,922 |
| Missing strings | 28 |
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

**28 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings` — 22
- `es-ES/firefox-ios.xliff` — 6

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

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

## 3. Open findings (63)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

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
| 2 | Wrong content (says something other than the English) | 33 |
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
