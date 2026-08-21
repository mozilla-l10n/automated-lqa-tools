# Android l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `ac24476c7ff2` |
| **Previous run** | 2026-08-21 @ `7134a6c77a67` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,886 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-MX: [firefox](firefox.md)

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
| Strings | 2,886 |
| Missing strings | 25 |
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
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 4 |

### Completeness

**25 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — 25

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 12, `straight-double` 4 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| inverted marks | `open-question` 113, `open-exclamation` 30 | **open-question** |
| register | `informal` 199, `formal` 12 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (177)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 95 |
| 3 | Degraded language (grammar, spelling, terminology) | 71 |
| 4 | Cosmetic (typography, spacing) | 11 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_archive_unreachable` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — "the archive service" is translated as "el servicio de archivos" (file service) instead of the archiving service.
    - Current: `No pudimos acceder al servicio de archivos.`
    - Source: `Couldn’t reach the archive service.`
    - Suggest: `No pudimos acceder al servicio de archivo.`
    - Per the developer comment this is the archive (archived-copy lookup) service, consistent with "Buscando en el archivo"; "servicio de archivos" reads as a file service.
- `mozac_browser_errorpages_content_crashed_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — "Content crashed" is rendered as "Contenido bloqueado", which means "content blocked", not "content crashed".
    - Current: `Contenido bloqueado`
    - Source: `Content crashed`
    - Suggest: `El contenido falló`
    - The source refers to the content process crashing; "bloqueado" means blocked, a different (and misleading) meaning also used for blocked-site error pages.
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — "compression" is translated as "comprensión" (comprehension) instead of "compresión".
    - Current: `una forma no válida o no admitida de comprensión`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `una forma no válida o no admitida de compresión`
    - The source says the page uses an invalid or unsupported form of compression; "comprensión" means comprehension/understanding.
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — "requests" (solicita) is rendered as "requiere" (requires), changing the meaning of the permission-request dialog title.
    - Current: `%1$s requiere ajustes adicionales`
    - Source: `%1$s requests additional settings`
    - Suggest: `%1$s solicita ajustes adicionales`
    - The source says the add-on requests additional settings; "requiere" states a requirement rather than a request, and the dialog is asking the user to grant optional permissions.
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — "requests" is translated as "requiere" (requires) instead of "solicita" in an optional-permission dialog title.
    - Current: `%1$s requiere recolección de datos adicionales`
    - Source: `%1$s requests additional data collection`
    - Suggest: `%1$s solicita recopilación de datos adicional`
    - The dialog asks for optional data collection permission; the source "requests" is a request, not a requirement. Also "recopilar/recopilación" is the term used elsewhere in this file (see data_collection_optional_description).
- `mozac_feature_addons_permissions_extra_domains_description_plural_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — Plural "other domains" rendered as singular "otro dominio".
    - Current: `Acceder a tus datos en otro dominio.`
    - Source: `Access your data on other domains.`
    - Suggest: `Acceder a tus datos en otros dominios.`
    - The source says "Access your data on other domains." (plural, referring to the remaining collapsed domains); the translation says a single domain.
- `mozac_feature_addons_permissions_extra_sites_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — "other sites" translated as "más sitios web" and verb form inconsistent with parallel strings.
    - Current: `Acceso a tus datos en más sitios web`
    - Source: `Access your data on other sites`
    - Suggest: `Acceder a tus datos en otros sitios`
    - Source is "Access your data on other sites"; "más sitios web" means "more websites", not "other sites", and the parallel _for_update string uses "Acceder a tus datos en otros sitios".
- `mozac_feature_addons_permissions_one_extra_site_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — The permission description is rendered as an imperative "Autoriza la lectura..." and uses "página" instead of "sitio", diverging from the source and from the parallel strings.
    - Current: `Autoriza la lectura de tus datos en otra página`
    - Source: `Access your data on another site`
    - Suggest: `Acceder a tus datos en otro sitio`
    - Source is "Access your data on another site", an infinitive permission label; all sibling strings (e.g. _for_update, _one_extra_domain_description_2) use "Acceder a tus datos en otro sitio/dominio". The current text changes both the form and the term (site → página).
- `mozac_feature_addons_unavailable_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — Section header "Not yet available" translated as a sentence about a single item rather than a section label.
    - Current: `Aún no está disponible`
    - Source: `Not yet available`
    - Suggest: `Aún no disponibles`
    - The string labels a section listing add-ons that are not yet available; the singular verb phrase misrepresents it as a statement about one item.
- `switch_to_tab_description` — `mozilla-mobile/android-components/components/feature/awesomebar/src/main/res/values-es-rMX/strings.xml` — Singular "tab" rendered as plural "pestañas".
    - Current: `Cambiar a pestañas`
    - Source: `Switch to tab`
    - Suggest: `Cambiar a la pestaña`
    - The source "Switch to tab" refers to a single open tab suggestion; the plural changes the meaning.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-es-rMX/strings.xml` — "choose tabs to close" is rendered as "elige qué pestañas cerrar", adding a meaning shift is minor, but "podría estar visible" mistranslates "may be visible" as a state instead of "podría ser visible".
    - Current: `tu ubicación podría estar visible`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `tu ubicación podría ser visible`
    - The source says the location may be visible to others; "estar visible" is not idiomatic Spanish here.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — "may not be saved" is rendered as "podrían perderse" (could be lost), changing the meaning.
    - Current: `Los datos que has ingresado podrían perderse`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `Los datos que has ingresado podrían no guardarse`
    - The source says the entered data may not be saved, not that it could be lost.
- `mozac_feature_prompts_suggest_strong_password_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — Imperative "Usa" used where the source is the dialog title/action "Use strong password: %1$s", inconsistent with the related title and button strings.
    - Current: `Usa una contraseña segura: %1$s`
    - Source: `Use strong password: %1$s`
    - Suggest: `Usar contraseña segura: %1$s`
    - The related strings use the infinitive ("¿Usar contraseña segura?", "Usar contraseña"); this label is the same action and should match, not be an informal imperative command.
- `mozac_summarize_download_consent_button_positive` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rMX/strings.xml` — "Download to summarize" is rendered as the noun "Descarga para resumir" instead of the imperative verb.
    - Current: `Descarga para resumir`
    - Source: `Download to summarize`
    - Suggest: `Descargar para resumir`
    - The source is a button action "Download to summarize"; the target reads as a noun phrase ("a download to summarize"), changing the meaning.
- `mozac_summarize_shake_consent_off_device_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rMX/strings.xml` — "Summarize with a shake?" is rendered as "¿Resumir sacudiendo el celular?", adding "celular" which is not in the source.
    - Current: `¿Resumir sacudiendo el celular?`
    - Source: `Summarize with a shake?`
    - Suggest: `¿Resumir con una sacudida?`
    - The source does not mention a phone; the component is shared and the device may not be a celular. Other strings in the same file use "dispositivo".
- `a11y_action_label_expand` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "expand" (UI expand action) is translated as "aumentar" (increase) instead of "expandir"/"desplegar".
    - Current: `aumentar`
    - Source: `expand`
    - Suggest: `expandir`
    - The developer comment says Talkback will say "Double tap to expand"; the counterpart string uses "contraer", so the opposite action must be "expandir"/"desplegar", not "aumentar" (to increase in size/amount).
- `a11y_selected_locale_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Selected language" is rendered as an imperative "Seleccionar idioma" (Select language) instead of describing the selected language.
    - Current: `Seleccionar idioma`
    - Source: `Selected language`
    - Suggest: `Idioma seleccionado`
    - The developer comment says it is the content description for the tick mark on the currently selected language, not an action to select one.
- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is mistranslated as "Regresar a la navegación" (return to navigation).
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Navegar hacia atrás`
    - The source means going back/exiting the add login view; the translation reverses the sense to "return to the navigation".
- `addresses_county` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "County" is translated as "Municipio o Alcaldía", substituting Mexican divisions for the source term.
    - Current: `Municipio o Alcaldía`
    - Source: `County`
    - Suggest: `Condado`
    - The source labels a county field for regions where county lines matter in postal services; "Alcaldía" is a Mexico City-specific unit not applicable there.
- `addresses_do_si` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Do/Si" (South Korean provincial-level division) is rendered as "Delegación / Barrio", which names Mexican local divisions instead.
    - Current: `Delegación / Barrio`
    - Source: `Do/Si`
    - Suggest: `Do/Si`
    - The developer comment states Do/Si refers to provincial-level divisions in South Korea; "Delegación / Barrio" denotes sub-city Mexican units and is the wrong administrative level and wrong region.
- `addresses_oblast` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Oblast" is translated as "Estado", naming a different administrative division.
    - Current: `Estado`
    - Source: `Oblast`
    - Suggest: `Óblast`
    - The developer comment says the field is for Russia/Ukraine oblasts; "Estado" is not the oblast and collides with the separate addresses_state string.
- `addresses_parish` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Parish" is rendered as "Localidad" rather than "Parroquia".
    - Current: `Localidad`
    - Source: `Parish`
    - Suggest: `Parroquia`
    - The comment says the field must let users specify parish details (Barbados, Jamaica); "Localidad" is a generic locality and loses that meaning.
- `addresses_prefecture` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Prefecture" is translated as "Estado" instead of "Prefectura".
    - Current: `Estado`
    - Source: `Prefecture`
    - Suggest: `Prefectura`
    - The comment specifies Japanese prefectures; "Estado" names a different division and duplicates addresses_state.
- `ai_controls_block_ai_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Block AI enhancements" is mistranslated as "Mejoras en el bloqueo de IA" (improvements to AI blocking), reversing the meaning.
    - Current: `Mejoras en el bloqueo de IA`
    - Source: `Block AI enhancements`
    - Suggest: `Bloquear mejoras de IA`
    - The source is an imperative toggle title meaning to block AI enhancements; the related dialog title uses "¿Bloquear mejoras de IA?". The current text says "enhancements in AI blocking", which is a different meaning.
- `bookmark_error_edit_folder` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Says "could not add folder" instead of "could not edit folder".
    - Current: `No se pudo agregar la carpeta`
    - Source: `Could not edit folder`
    - Suggest: `No se pudo editar la carpeta`
    - Source is "Could not edit folder"; the target duplicates the add-folder error message.
- `bookmark_error_select_folder` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "parent folder" rendered as "carpeta raíz" (root folder).
    - Current: `No se pudo cambiar la carpeta raíz`
    - Source: `Could not change parent folder`
    - Suggest: `No se pudo cambiar la carpeta principal`
    - Source says "Could not change parent folder"; "raíz" means root, a different concept.
- `bookmark_moved_single_item` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Translation reverses the meaning: %1$s is the moved item, not the source folder.
    - Current: `Movido de %1$s a %2$s`
    - Source: `Moved %1$s to %2$s`
    - Suggest: `Se movió %1$s a %2$s`
    - Source "Moved %1$s to %2$s" — %1$s is the item title; "de" wrongly turns it into an origin folder.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" mistranslated as "Regresar a la navegación".
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Navegar hacia atrás`
    - Source means going back; the target says "return to navigation", a different meaning.
- `bookmark_sort_menu_custom` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Completely unrelated text used for the custom sort order label.
    - Current: `El sitio no carga`
    - Source: `Sort by custom order`
    - Suggest: `Ordenar por orden personalizado`
    - Source is "Sort by custom order"; the target says "The site is not loading".
- `bookmarks_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Multi-select count label is rendered as a past-tense sentence instead of the count label "%1$d selected".
    - Current: `Se seleccionó %1$d`
    - Source: `%1$d selected`
    - Suggest: `%1$d seleccionados`
    - The source is an app-bar title showing how many bookmarks are selected; "Se seleccionó %1$d" reads as a singular past-tense statement and misrepresents plural counts.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Translation says "menu of custom tabs" (plural, possessive) instead of "custom tab menu sheet".
    - Current: `Cerrar el menú de pestañas personalizadas`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Cerrar la hoja del menú de la pestaña personalizada`
    - The source refers to the bottom sheet menu of a single custom tab; the target changes it to a menu of multiple custom tabs and drops "sheet".
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Never" is translated as "Manualmente" instead of "Nunca".
    - Current: `Manualmente`
    - Source: `Never`
    - Suggest: `Nunca`
    - The source option label is "Never" (never auto-close tabs); the target says "Manually", which is a different word and duplicates the wording of the separate summary string "Cerrar manualmente".
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is rendered as "Regresar a la navegación" (return to navigation), reversing the meaning.
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Navegar hacia atrás`
    - The source describes a back button action: navigate back. The translation says "return to the navigation", which is a different meaning.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Debug locales" is translated as "Idiomas de depuración" (languages) instead of locales/regional settings.
    - Current: `Idiomas de depuración para habilitar`
    - Source: `Debug locales to enable`
    - Suggest: `Configuraciones regionales de depuración para habilitar`
    - The feature enables address locales (region/locale formats), not languages; the related string uses "localidad" for locale.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" within the debug drawer is translated as going to the previous web page.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Navegar hacia atrás`
    - The developer comment specifies navigating back within the debug drawer, not to a previous web page.
- `debug_drawer_override_region` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "home and current region" is mistranslated as "el inicio y la región actual", losing the meaning of "home region".
    - Current: `Reemplazar el inicio y la región actual`
    - Source: `Override home and current region`
    - Suggest: `Reemplazar la región de origen y la región actual`
    - The source overrides the home region and the current region; elsewhere "home region" is correctly rendered "región de origen", so "el inicio" is wrong.
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "home ... region values" rendered as "valores de inicio", losing the "home region" meaning, and the verb form is infinitive instead of third person.
    - Current: `Reemplazar temporalmente los valores de inicio y de región actual para realizar pruebas.`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `Reemplaza temporalmente los valores de la región de origen y de la región actual para realizar pruebas.`
    - The source is a descriptive sentence ("Temporarily overrides…") about the home region and the current region; the target changes it to an infinitive command and mistranslates "home region" as "inicio".
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is rendered as "Regresar a la navegación" (return to browsing) instead of "Regresar"/"Navegar hacia atrás".
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Regresar`
    - The source is a back-button content description meaning to go back; the translation says "return to the navigation", which changes the meaning.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is mistranslated as "Regresar a la navegación" (go back to navigation).
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Regresar`
    - The source means to navigate backwards/exit the edit view; the same source string is correctly rendered as "Regresar" in etp_back_button_content_description.
- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Known Fingerprinters" is rendered as "Huellas dactilares conocidas" (known fingerprints), naming the data rather than the trackers.
    - Current: `Huellas dactilares conocidas`
    - Source: `Known Fingerprinters`
    - Suggest: `Detectores de huellas digitales conocidos`
    - Fingerprinters are the trackers that collect fingerprints; the related string etp_suspected_fingerprinters_title uses "detectores de huellas digitales", so this is also inconsistent.
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Button label translated as an imperative command to the user instead of the action label "Try restarting extensions".
    - Current: `Intenta reiniciar las extensiones`
    - Source: `Try restarting extensions`
    - Suggest: `Intentar reiniciar las extensiones`
    - The source is a button label describing the action the app will take (retry restarting extensions), not an instruction to the user; other buttons in this dialog use the infinitive ("Continuar con las extensiones deshabilitadas").
- `home_screen_shortcut_open_new_private_tab_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "New private tab" is translated as "Pestaña privada", dropping "New".
    - Current: `Pestaña privada`
    - Source: `New private tab`
    - Suggest: `Nueva pestaña privada`
    - The source says "New private tab"; the parallel string home_screen_shortcut_open_new_tab_2 correctly renders "Nueva pestaña".
- `inactive_tabs_collapse_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Collapse inactive tabs" rendered as "Ocultar" (hide) instead of "Contraer", inconsistent with the paired "Expandir" string.
    - Current: `Ocultar pestañas inactivas`
    - Source: `Collapse inactive tabs`
    - Suggest: `Contraer pestañas inactivas`
    - Source is "Collapse", the opposite of "Expand" which is translated as "Expandir"; "Ocultar" means "hide".
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Switched to the recommended location." is translated as "Conectado a la ubicación recomendada." (connected), duplicating a different string's meaning.
    - Current: `Conectado a la ubicación recomendada.`
    - Source: `Switched to the recommended location.`
    - Suggest: `Se cambió a la ubicación recomendada.`
    - The source says the app switched to the recommended location, not that it is connected; a separate string (ip_protection_location_unavailable_recommended_description) is the "Connected to…" one.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is rendered as "Regresar a la navegación" (go back to navigation), changing the meaning and diverging from the parallel string.
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Regresar`
    - Source means to go back; the identical source string ip_protection_locations_navigate_back_button_content_description is translated as "Regresar".
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "through %1$s" (a date) is translated as "a través de" (by means of) instead of "hasta" (until that date).
    - Current: `ancho de banda ilimitado a través de %1$s`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `ancho de banda ilimitado hasta el %1$s`
    - %1$s is a localized date indicating the end of the promotional period, so "through" means "until", not "by means of".
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is mistranslated as "Regresar a la navegación" (return to navigation).
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Navegar hacia atrás`
    - The source instructs the screen reader user to go back/exit the detail view; the target says "return to the navigation", which is a different meaning.
- `microsurvey_homepage_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "How satisfied are you" is rendered as a yes/no question "¿Estás satisfecho?", losing the degree question.
    - Current: `¿Estás satisfecho con la página de inicio de Firefox?`
    - Source: `How satisfied are you with your Firefox homepage?`
    - Suggest: `¿Qué tan satisfecho estás con tu página de inicio de Firefox?`
    - The source asks the degree of satisfaction (a likert-scale question); the translation asks a yes/no question and also drops "your".
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "that you use it" is mistranslated as "cómo lo usas" (how you use it).
    - Current: `cómo descubriste Firefox y cómo lo usas`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `cómo descubriste Firefox y que lo usas`
    - The source shares the fact that the user uses Firefox, not how they use it; the translation adds a meaning about usage details that the source explicitly avoids.
- `onboarding_redesign_sync_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — The translation says "Sync Firefox on all your devices" instead of "Sync everywhere you use Firefox".
    - Current: `Sincroniza Firefox en todos tus dispositivos`
    - Source: `Sync everywhere you use Firefox`
    - Suggest: `Sincroniza en todos los lugares donde uses Firefox`
    - The source means syncing across every place where Firefox is used; the target reverses the object, making Firefox the thing being synced onto all devices.
- `open_all_warning_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Opening this many tabs" is rendered as "Abrir varias pestañas", losing the "this many" (large number) meaning.
    - Current: `Abrir varias pestañas puede ralentizar`
    - Source: `Opening this many tabs may slow down %s while the pages are loading. Are you sure you want to continue?`
    - Suggest: `Abrir esta cantidad de pestañas puede ralentizar`
    - The source warns about opening this many (a large number of) tabs; "varias" means just "several", weakening/altering the meaning per the developer comment about a large number of tabs.
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Leave private tabs" (exit private browsing) is mistranslated as "Dejar pestañas privadas", which reads as "keep/leave behind private tabs".
    - Current: `Dejar pestañas privadas`
    - Source: `Leave private tabs`
    - Suggest: `Salir de las pestañas privadas`
    - The developer comment says this is the secondary action to exit private browsing mode; "Dejar" does not convey exiting.
- `preference_enhanced_tracking_protection_allow_list_convenience_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "major issues" translated as "problemas críticos" instead of "problemas importantes", breaking consistency with the related label.
    - Current: `Debe usarse con correcciones para problemas críticos.`
    - Source: `Must be used with fixes for major issues.`
    - Suggest: `Debe usarse con correcciones para problemas importantes.`
    - The paired string preference_enhanced_tracking_protection_allow_list_baseline_2 renders "major site issues" as "problemas importantes del sitio"; "críticos" is a different severity term on the same surface.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "will cause websites to break" is weakened to "algunos sitios no funcionarán correctamente", losing the certainty/scope contrast with the "may cause" option.
    - Current: `Todas las cookies (algunos sitios no funcionarán correctamente)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `Todas las cookies (causará errores en los sitios web)`
    - The source deliberately contrasts "may cause websites to break" (option 3) with "will cause websites to break"; the target adds "algunos" and drops the certainty.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Adds the possessive "mis" not present in the source "data".
    - Current: `Decir a los sitios web que no vendan ni compartan mis datos`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `Decir a los sitios web que no compartan ni vendan datos`
    - The source is "Tell websites not to share & sell data" without a possessive.
- `preference_enhanced_tracking_protection_custom_info_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "custom tracking protection" is translated as "protección de rastreo estándar" (standard) instead of "personalizada".
    - Current: `Esto es lo que está bloqueado por la protección de rastreo estándar`
    - Source: `What’s blocked by custom tracking protection`
    - Suggest: `Qué es lo que está bloqueado por la protección de rastreo personalizada`
    - The source refers to the custom protection level; the developer comment/id confirm it is the custom setting, not standard.
- `preference_enhanced_tracking_protection_custom_known_fingerprinters` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Known Fingerprinters" is rendered as "Huellas dactilares conocidas", which names the fingerprints rather than the trackers that create them.
    - Current: `Huellas dactilares conocidas`
    - Source: `Known Fingerprinters`
    - Suggest: `Detectores de huellas digitales conocidos`
    - Fingerprinters are scripts/entities that perform digital fingerprinting; "huellas dactilares" (physical fingerprints) names the wrong thing.
- `preference_enhanced_tracking_protection_strict_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Stronger tracking protection" translated as "Protección contra rastreo mejorada", which duplicates the feature name "Enhanced Tracking Protection".
    - Current: `Protección contra rastreo mejorada y mayor rendimiento`
    - Source: `Stronger tracking protection and faster performance, but some sites may not work properly.`
    - Suggest: `Protección contra rastreo más fuerte y mayor rendimiento`
    - "Stronger" is a comparative describing the strict level; "mejorada" is the established rendering of "Enhanced" in preference_enhanced_tracking_protection, creating a confusing collision.
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — The product name "Firefox Suggest" is translated here but left untranslated in the related string.
    - Current: `Sugerencias de Firefox`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a Mozilla product name that must stay untranslated; the sibling string preference_search_learn_about_fx_suggest keeps it in English, creating inconsistency on the same settings screen.
- `preferences_category_select_default_search_engine_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Default search engine" is rendered as "Buscador principal" instead of "predeterminado".
    - Current: `Buscador principal para la navegación estándar`
    - Source: `Normal browsing default search engine`
    - Suggest: `Buscador predeterminado para la navegación estándar`
    - The source says "default search engine"; "principal" means primary/main, not default, and the rest of the tree uses "predeterminado" for "default".
- _…and 38 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — Ungrammatical question: "¿Estás conectado el equipo...?" mixes second person verb with third-person subject.
    - Current: `¿Estás conectado el equipo a una red activa?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `¿Está conectado el equipo a una red activa?`
    - Source is "Is the device connected to an active network?"; the subject is "el equipo", so the verb must be "Está". The parallel string mozac_browser_errorpages_unknown_proxy_host_message correctly uses "¿Está conectado el equipo a una red activa?".
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — Missing article: "para dirección proporcionada" should be "para la dirección proporcionada".
    - Current: `el servidor para dirección proporcionada`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `el servidor para la dirección proporcionada`
    - Grammatical error; the source reads "the host server for the provided address".
- `mozac_feature_contextmenu_snackbar_email_address_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-es-rMX/strings.xml` — "portapeles" is a misspelling of "portapapeles".
    - Current: `Dirección de correo copiada al portapeles`
    - Source: `Email address copied to clipboard`
    - Suggest: `Dirección de correo copiada al portapapeles`
    - The Spanish word for clipboard is "portapapeles"; the other snackbar strings in the same file use it correctly.
- `mozac_feature_downloads_failed_notification_text2` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-es-rMX/strings.xml` — "Descarga fallada" is incorrect Spanish for "Download failed".
    - Current: `Descarga fallada`
    - Source: `Download failed`
    - Suggest: `Descarga fallida`
    - The correct adjective is "fallida"; "fallada" is not used in this sense.
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — Literal calque "Prevenir ... desde la creación" is ungrammatical Spanish.
    - Current: `Prevenir esta página desde la creación de cuadros de diálogo adicionales`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `Evitar que esta página cree cuadros de diálogo adicionales`
    - The source means to stop the page from creating more dialogs; the word-for-word rendering of "prevent ... from" is not valid Spanish and obscures the meaning.
- `mozac_feature_prompts_set_month` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — "Eligir" is a misspelling of the verb "Elegir".
    - Current: `Eligir un mes`
    - Source: `Pick a month`
    - Suggest: `Elegir un mes`
    - The Spanish infinitive is "elegir"; "eligir" is not a word.
- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-es-rMX/strings.xml` — "por que" should be "por qué" (interrogative, needs accent).
    - Current: `si no está claro por que %s necesita estos datos`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - Suggest: `si no está claro por qué %s necesita estos datos`
    - Indirect interrogative "why" requires the accented form "por qué"; "por que" is a spelling error here.
- `mozac_summarize_settings_shake_sensitivity_medium` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rMX/strings.xml` — Gender agreement inconsistency: "Mediano" should be feminine to match "Alta"/"Baja" for "sensibilidad".
    - Current: `Mediano`
    - Source: `Medium`
    - Suggest: `Media`
    - The sensitivity slider options are Low/Medium/High, translated as "Baja"/"Alta" (feminine, agreeing with "sensibilidad"); "Mediano" is masculine and inconsistent.
- `mozac_summarize_shake_consent_on_device_button_positive` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rMX/strings.xml` — Button label uses imperative "Descarga" instead of the infinitive used for action buttons.
    - Current: `Descarga para resumir`
    - Source: `Download to summarize`
    - Suggest: `Descargar para resumir`
    - Source "Download to summarize" is a button action; other buttons in the same file use infinitives (Cancelar, Descartar, Continuar, Resumir esta página). "Descarga para resumir" reads as a noun/imperative and is inconsistent.
- `bookmark_empty_list_folder_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Infinitive "Agregar" used where the source is an imperative addressed to the user.
    - Current: `Agregar marcadores mientras navegas`
    - Source: `Add bookmarks as you browse so you can find your favorite sites later.`
    - Suggest: `Agrega marcadores mientras navegas`
    - Source "Add bookmarks as you browse" is imperative and the rest of the sentence uses informal second person ("navegas", "puedas"), so the verb should be "Agrega".
- `clear_permission_positive` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "OK" is rendered as "Ok" with incorrect capitalization.
    - Current: `Ok`
    - Source: `OK`
    - Suggest: `Aceptar`
    - The source is the standard "OK" button; Spanish convention uses "Aceptar" or at minimum "OK" fully capitalized, not "Ok".
- `clear_permissions_positive` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "OK" is rendered as "Ok" with incorrect capitalization.
    - Current: `Ok`
    - Source: `OK`
    - Suggest: `Aceptar`
    - The source is the standard "OK" button; Spanish convention uses "Aceptar" or at minimum "OK" fully capitalized, not "Ok".
- `customize_toggle_jump_back_in` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "hacía" is misspelled; should be the preposition "hacia" (and the phrase is redundant).
    - Current: `Regresar hacía atrás`
    - Source: `Jump back in`
    - Suggest: `Retomar donde te quedaste`
    - "hacía" (verb hacer, imperfect) is a spelling error for the preposition "hacia"; the source "Jump back in" means resuming a recent tab, not moving backwards.
- `download_content_type_filter_video` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Vídeos" uses the peninsular spelling; es-MX uses "Videos".
    - Current: `Vídeos`
    - Source: `Videos`
    - Suggest: `Videos`
    - In Mexican Spanish the accepted form is "video" without accent; "vídeo" is the Spain variant.
- `download_delete_multi_select_dialog_confirmation` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Missing preposition "de" in "¿Estás seguro que..." (queísmo).
    - Current: `¿Estás seguro que deseas eliminar los elementos seleccionados?`
    - Source: `Are you sure you want to delete the selected items?`
    - Suggest: `¿Estás seguro de que deseas eliminar los elementos seleccionados?`
    - "estar seguro" requires the preposition "de" before the subordinate clause; omitting it is queísmo, a grammatical error.
- `download_languages_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Typo: "pidodo" instead of "podido".
    - Current: `No se ha pidodo descargar`
    - Source: `Couldn’t download { <b> }%1$s{ </b> }. Please try again.`
    - Suggest: `No se ha podido descargar`
    - Misspelling of the past participle "podido"; the parallel string download_languages_delete_error_warning_text uses "No se ha podido".
- `experiments_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Snackbar message uses infinitive instead of the imperative required by the source instruction.
    - Current: `Habilitar la telemetría para enviar datos.`
    - Source: `Enable telemetry to send data.`
    - Suggest: `Habilita la telemetría para enviar datos.`
    - The source "Enable telemetry to send data." is an instruction to the user shown in a snackbar; es-MX uses the informal imperative for user instructions.
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Recommended" is a label for a single location option and should be singular, not plural.
    - Current: `Recomendados`
    - Source: `Recommended`
    - Suggest: `Recomendada`
    - The label refers to the recommended automatic location option (singular, feminine "ubicación"); the plural masculine "Recomendados" does not agree.
- `nova_onboarding_customize_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "navegadas" is a misspelling of the verb form "navegabas".
    - Current: `mientras navegadas por la web`
    - Source: `{$quantity ->} [one] %1$s blocked %2$,d tracker while you roamed the web. [other] %1$s blocked %2$,d trackers while you roamed the web.`
    - Suggest: `mientras navegabas por la web`
    - The source is "while you roamed the web"; the Spanish should be the imperfect "navegabas", not the nonexistent form "navegadas". Occurs in both plural variants.
- `nova_onboarding_customize_prompt_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Button label rendered as an imperative sentence rather than an infinitive action label matching the source gerund phrase.
    - Current: `Inicia la personalización`
    - Source: `Start customizing`
    - Suggest: `Comenzar a personalizar`
    - "Start customizing" is a button label; other onboarding buttons in this batch use infinitives ("Continuar navegando", "Agregar widget de Firefox"), so the imperative here is inconsistent.
- `nova_onboarding_marketing_primary_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Ayuda Firefox" is missing the preposition "a" required before a personified direct object.
    - Current: `Ayuda Firefox`
    - Source: `Help Firefox`
    - Suggest: `Ayuda a Firefox`
    - The source "Help Firefox" is an imperative with Firefox as direct object; in Spanish this requires the personal 'a' ('Ayuda a Firefox'), otherwise the phrase reads as ungrammatical.
- `preference_gestures_swipe_toolbar_show_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Number agreement error: "pestañas abierta" should be "pestañas abiertas".
    - Current: `las pestañas abierta`
    - Source: `Swipe toolbar vertically to see open tabs`
    - Suggest: `las pestañas abiertas`
    - The adjective must agree in number with the plural noun "pestañas" (source: "open tabs").
- `preferences_choose_app_for_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Preference title translated as an imperative verb instead of an infinitive label.
    - Current: `Administra las descargas con otra aplicación`
    - Source: `Manage downloads with another app`
    - Suggest: `Administrar las descargas con otra aplicación`
    - Source "Manage downloads with another app" is a preference title; parallel entries (preferences_addresses_manage_addresses, preferences_credit_cards_manage_saved_cards_2) use the infinitive "Administrar".
- `preferences_customize_extension_collection` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Adjective agreement attaches "personalizadas" to "extensiones" instead of to the collection.
    - Current: `Colección de extensiones personalizadas`
    - Source: `Custom extension collection`
    - Suggest: `Colección personalizada de extensiones`
    - The source is "Custom extension collection" — it is the collection that is custom, not the extensions.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Tense mismatch: present-tense description rendered in past tense.
    - Current: `El archivo se quitó de tu historial de descargas`
    - Source: `File is removed from your download history, but is still saved on your device`
    - Suggest: `El archivo se quita de tu historial de descargas`
    - Source "File is removed from your download history" describes the option's effect in the present, and the parallel string uses future/present ("se eliminará"); past tense is inconsistent and wrong here.
- `privacy_notice_updated_homepage_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Plural article/possessive disagrees with the singular link text "Política de privacidad" inserted at %1$s.
    - Current: `Hemos actualizado nuestros %1$s`
    - Source: `We’ve updated our %1$s to reflect the latest features in Firefox. %2$s`
    - Suggest: `Hemos actualizado nuestra %1$s`
    - %1$s is replaced by the link text "Política de privacidad" (feminine singular), so "nuestros" produces an ungrammatical phrase.
- `recent_tabs_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "hacía" is misspelled; it should be the preposition "hacia" (and the phrase is redundant).
    - Current: `Regresar hacía atrás`
    - Source: `Jump back in`
    - Suggest: `Volver atrás`
    - "hacía" is the verb form of "hacer"; the intended word is the preposition "hacia" (no accent). "Jump back in" means returning to a recent tab.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Word-order error: "Estás a 1 solo un paso de la meta" contains a duplicated/misplaced quantifier.
    - Current: `Estás a 1 solo un paso de la meta.`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Estás a solo 1 paso de la meta.`
    - "1 solo un paso" is ungrammatical; the parallel string setup_checklist_subtitle_6_steps_fifth_step correctly reads "Estás a solo 1 paso de la meta".
- `share_tab_group_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — The singular variant reads "Compartir al grupo pestañas", which is ungrammatical and inconsistent with the plural variant.
    - Current: `Compartir al grupo pestañas %1$s con %2$d pestaña.`
    - Source: `{$quantity ->} [one] Share %1$s tab group with %2$d tab. [other] Share %1$s tab group with %2$d tabs.`
    - Suggest: `Compartir grupo de pestañas %1$s con %2$d pestaña.`
    - Source is "Share %1$s tab group with %2$d tab."; the stray "al" and missing "de" make it ungrammatical, while the other variant correctly uses "Compartir grupo de pestañas".
- `sports_widget_follow_another_team` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Button label uses an imperative verb form instead of the infinitive used for action labels.
    - Current: `Sigue a otro equipo`
    - Source: `Follow another team`
    - Suggest: `Seguir a otro equipo`
    - Source is a button label "Follow another team"; Spanish button/action labels use the infinitive, as in sports_widget_error_refresh ("Actualizar").
- `sports_widget_get_custom_wallpaper` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Menu item uses an imperative verb form instead of the infinitive used for menu actions.
    - Current: `Obtén un fondo de pantalla personalizado`
    - Source: `Get custom wallpaper`
    - Suggest: `Obtener fondo de pantalla personalizado`
    - The developer comment states this is a menu item; Spanish menu items use the infinitive form.
- `sports_widget_go_to_world_cup_site_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Content description uses an imperative verb instead of describing the action.
    - Current: `Visita el sitio web del Mundial`
    - Source: `Go to World Cup site`
    - Suggest: `Ir al sitio del Mundial`
    - Content descriptions describe the control; the source "Go to World Cup site" is a label for an action, not a command to the user.
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Toggle label reads as an imperative "Descarga siempre" instead of the infinitive used for settings labels.
    - Current: `Descarga siempre idiomas en modo de ahorro de datos`
    - Source: `Always download languages in data saving mode`
    - Suggest: `Descargar siempre idiomas en modo de ahorro de datos`
    - The source "Always download languages…" is a setting label; other toggle labels in this batch use the infinitive ("Nunca traducir…", "Ofrecer traducción…").
- `translation_settings_translation_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Improper capitalization of "Traducción" mid-phrase.
    - Current: `Preferencias de Traducción`
    - Source: `Translation preferences`
    - Suggest: `Preferencias de traducción`
    - Spanish uses sentence case; "traducción" should be lowercase, as in the other translation strings in this batch.
- `uninstall_survey_option_2_v2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Past tense of the source is rendered in present tense.
    - Current: `Los sitios web no funcionan correctamente`
    - Source: `Websites didn’t work properly`
    - Suggest: `Los sitios web no funcionaban correctamente`
    - Source "Websites didn’t work properly" is past tense, describing past experience; the translation uses present tense.
- `uninstall_survey_option_4_v2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Past tense of the source is rendered in present tense.
    - Current: `No funcionan los videos, descargas o archivos multimedia`
    - Source: `Videos, downloads, or media didn’t work`
    - Suggest: `No funcionaban los videos, descargas o archivos multimedia`
    - Source "Videos, downloads, or media didn’t work" is past tense; translation uses present tense.
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — Missing accent on the future-tense verb "intentará".
    - Current: `%1$s intentara rechazar las solicitudes de cookies`
    - Source: `%1$s tries to reject cookie requests to dismiss annoying cookie banners.  Manage cookie banner preferences in %2$s.`
    - Suggest: `%1$s intentará rechazar las solicitudes de cookies`
    - The source "tries to reject" requires an accented verb form; "intentara" without accent is the subjunctive past, an orthographic error.
- `download_firefox` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Download Firefox" is a list item label and should be an infinitive, not the imperative/indicative "Descarga".
    - Current: `Descarga Firefox`
    - Source: `Download Firefox`
    - Suggest: `Descargar Firefox`
    - The developer comment says this is an item in a list of browsers; Spanish UI list/action labels use the infinitive, and "Descarga Firefox" reads as a sentence.
- `preference_search_restore` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — Word order breaks the noun phrase: "motores predeterminados de búsqueda" instead of "motores de búsqueda predeterminados".
    - Current: `Restaurar motores predeterminados de búsqueda`
    - Source: `Restore default search engines`
    - Suggest: `Restaurar los motores de búsqueda predeterminados`
    - "Motor de búsqueda" is a fixed compound; the adjective must follow the whole phrase, as in the other strings in this file.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_harmful_addon_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — Formal "su seguridad" breaks the locale's informal register used in the body of the same error page ("tus complementos").
    - Current: `Sitio bloqueado por su seguridad`
    - Source: `Site blocked for your safety`
    - Suggest: `Sitio bloqueado por tu seguridad`
    - es-MX convention is informal address, and the accompanying message string uses "tus complementos"/"tu información".
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — Formal "su administrador de red" mixes with the informal address used throughout the same string.
    - Current: `Consulta con su administrador de red`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Consulta con tu administrador de red`
    - The rest of the string uses informal "tu red", "Comprueba", "Vuelve a intentarlo"; es-MX convention is informal.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Volver a intentarlo” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Intenta de nuevo”
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Intenta de nuevo`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — Formal "su" used in a string that otherwise addresses the user informally (tú).
    - Current: `Consulta con su administrador de red`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Consulta con tu administrador de red`
    - The locale's register is informal, and the rest of the same string uses tú forms ("Comprueba", "vuelve a intentarlo"); the parallel proxy_connection_refused string uses "tu administrador de red".
- `mozac_feature_addons_permissions_downloads_open_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — "device" translated as "equipo" while the parallel update string uses "dispositivo".
    - Current: `Abrir archivos descargados en tu equipo`
    - Source: `Open files downloaded to your device`
    - Suggest: `Abrir archivos descargados en tu dispositivo`
    - Source term "device" is rendered inconsistently on the same surface: the _for_update variant uses "dispositivo".
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — "manage" translated as "gestionar" while the identical non-update string uses "administrar".
    - Current: `Monitorear el uso de extensiones y gestionar temas.`
    - Source: `Monitor extension usage and manage themes.`
    - Suggest: `Monitorear el uso de extensiones y administrar temas.`
    - Same source sentence is translated with two different verbs on the same surface; keep consistent with mozac_feature_addons_permissions_management_description.
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rMX/strings.xml` — Uses formal "su sistema" instead of the locale's informal register ("tu sistema").
    - Current: `lo que hizo que su sistema fuera inestable`
    - Source: `One or more extensions stopped working, making your system unstable.`
    - Suggest: `lo que hizo que tu sistema fuera inestable`
    - es-MX convention is informal address (tú); other strings in this batch use "tu versión", "tu recopilación", etc.
- `mozac_feature_media_sharing_camera_and_microphone_reminder_text_2` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-es-rMX/strings.xml` — Formal "Toque" breaks the locale's informal register used in the parallel strings ("Toca").
    - Current: `Toque para abrir la pestaña.`
    - Source: `Reminder: %1$s is still using your microphone and camera. Tap to open the tab.`
    - Suggest: `Toca para abrir la pestaña.`
    - es-MX convention is informal (tú); the sibling strings use "Toca para abrir la pestaña".
- `mozac_feature_media_sharing_microphone_reminder_text_2` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-es-rMX/strings.xml` — Formal "Toque" breaks the locale's informal register used in the parallel strings ("Toca").
    - Current: `Toque para abrir la pestaña.`
    - Source: `Reminder: %1$s is still using your microphone. Tap to open the tab.`
    - Suggest: `Toca para abrir la pestaña.`
    - es-MX convention is informal (tú); the sibling notification strings use "Toca para abrir la pestaña".
- `mozac_feature_prompts_identity_credentials_choose_account_for_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — "Sign in" is translated as "Conéctate" instead of the standard "Inicia sesión".
    - Current: `Conéctate con una cuenta de %1$s`
    - Source: `Sign in with a %1$s account`
    - Suggest: `Inicia sesión con una cuenta de %1$s`
    - Other strings in the same dialog group use "inicio de sesión"/"Iniciar sesión" for sign in/login; "Conéctate" is inconsistent terminology.
- `mozac_feature_prompts_suggest_strong_password_content_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — "strong password" is rendered as "contraseña fuerte" here but "contraseña segura" in the related visible label.
    - Current: `Sugerir una contraseña fuerte`
    - Source: `Suggest strong password`
    - Suggest: `Sugerir una contraseña segura`
    - Inconsistent terminology on the same prompt surface (mozac_feature_prompts_suggest_strong_password_2 uses "contraseña segura").
- `webauthn_related_origin_use_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — "passkey" is rendered as "llave de acceso" here but as "clave de acceso" in the parallel create message.
    - Current: `llave de acceso`
    - Source: `%1$s wants to use a passkey for %2$s.`
    - Suggest: `clave de acceso`
    - The sibling string webauthn_related_origin_create_message translates "passkey" as "clave de acceso"; the same term on the same surface must be consistent.
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Register shifts to formal "se encuentra" in a sentence that otherwise uses informal "seguirte".
    - Current: `del sitio en el que se encuentra`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `del sitio en el que estás`
    - The locale convention is informal address; "you're on" should be tú-form, matching "seguirte" later in the same string.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `never_translate_site_header_preference` quotes “No traducir nunca este sitio” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Nunca traducir este sitio”
    - Current: `Para añadir un sitio nuevo: visítalo y selecciona “No traducir nunca este sitio” en el menú de traducción.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Nunca traducir este sitio`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `notification_erase_text_android_14` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Uses formal address ("Toque o deslice") instead of the locale's informal register.
    - Current: `Toque o deslice esta notificación para cerrar las pestañas privadas.`
    - Source: `Tap or swipe this notification to close private tabs.`
    - Suggest: `Toca o desliza esta notificación para cerrar las pestañas privadas.`
    - es-MX convention is informal (tú); the rest of the batch uses informal forms.
- `onboarding_redesign_tou_body_two_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Privacy Notice" is rendered as "Política de privacidad" here but as "Aviso de privacidad" in the parallel string onboarding_term_of_service_line_two_link_text.
    - Current: `Política de privacidad`
    - Source: `Privacy Notice`
    - Suggest: `Aviso de privacidad`
    - The same source term "Privacy Notice" on the same onboarding surface is translated two different ways; Mozilla's standard rendering is "Aviso de privacidad" ("Política de privacidad" corresponds to "Privacy Policy").
- `preferences_delete_browsing_data` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Browsing data" is translated inconsistently as "datos del navegador" here but "datos de navegación" in the sibling strings.
    - Current: `Eliminar datos del navegador`
    - Source: `Delete browsing data`
    - Suggest: `Eliminar datos de navegación`
    - preferences_delete_browsing_data_button and _on_quit use "datos de navegación" for the same source term on the same surface.
- `preferences_delete_browsing_data_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Browsing data" rendered as "datos del navegador" instead of the consistent "datos de navegación".
    - Current: `Se han eliminado los datos del navegador`
    - Source: `Browsing data deleted`
    - Suggest: `Se han eliminado los datos de navegación`
    - Inconsistent with the other Delete browsing data strings in the same screen, which use "datos de navegación".
- `protection_panel_etp_toggle_label` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Enhanced Tracking Protection" rendered inconsistently with the established term used elsewhere in the same panel.
    - Current: `Protección de seguimiento mejorada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra el rastreo mejorada`
    - Sibling strings in the same protection panel use "rastreo"/"rastreadores" (e.g. "protección contra el rastreo", "Los rastreadores no están bloqueados"); using "seguimiento" here is inconsistent.
- `saved_login_password_required_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Imperative form inconsistent with sibling error strings using tú form ("Ingresa").
    - Current: `Ingresar una contraseña`
    - Source: `Enter a password`
    - Suggest: `Ingresa una contraseña`
    - Parallel strings saved_login_username_required_2 and saved_login_hostname_required_2 use "Ingresa" (informal imperative); the infinitive here breaks the locale's informal register convention and consistency.
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "Shortcut" is rendered as "acceso directo" here while the sibling shortcut strings use "atajo".
    - Current: `URL del acceso directo`
    - Source: `Shortcut URL`
    - Suggest: `URL del atajo`
    - shortcut_name_hint, shortcut_max_limit_title/content all translate "shortcut" as "atajo"; using a different term on the same surface is inconsistent.
- `sports_widget_final_results_page_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "World Cup" is rendered as "Copa del Mundo" here while all other sports widget strings use "Mundial".
    - Current: `Resultados finales de la Copa del Mundo, página %1$d de %2$d`
    - Source: `World Cup final results, page %1$d of %2$d`
    - Suggest: `Resultados finales del Mundial, página %1$d de %2$d`
    - Inconsistent with sports_widget_final_results_content_description ("Resultados finales del Mundial") and other strings on the same surface.
- `sports_widget_view_schedule` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "View schedule" (match calendar) is translated as "Ver horario", suggesting a time schedule rather than the fixture list.
    - Current: `Ver horario`
    - Source: `View schedule`
    - Suggest: `Ver calendario`
    - The comment says the button navigates to the full tournament match schedule, i.e., the fixture calendar.
- `trackers_blocked_panel_num_social_media_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "social media" left in English instead of the Spanish term.
    - Current: `rastreador de social media`
    - Source: `{$quantity ->} [one] %1$d social media tracker [other] %1$d social media trackers`
    - Suggest: `rastreador de redes sociales`
    - "Social media" is not a brand; the established Spanish term is "redes sociales", used elsewhere in the tracking protection UI.
- `translations_bottom_sheet_translate_from_unsupported_language` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Formal address "Pruebe" breaks the locale's informal register used in the surrounding translation dialog strings.
    - Current: `Pruebe con otro idioma de origen`
    - Source: `Try another source language`
    - Suggest: `Prueba con otro idioma de origen`
    - es-MX convention is informal (tú); neighboring strings use "Selecciona", "Prueba traducciones privadas".
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — "crash report" is rendered as "informe de error" while the sibling crash strings use "reporte de fallo"/"informe", creating inconsistent terminology on the same surface.
    - Current: `Tienes un informe de error sin enviar sobre fallas bajo investigación.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Tienes un informe de fallo sin enviar sobre fallas bajo investigación.`
    - Same feature (unsubmitted crash dialogs) uses "reporte de fallo" in unsubmitted_crash_dialog_positive_button; "error" vs "fallo" is inconsistent for "crash".
- `a11y_link_available` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Link" left in English instead of the standard Spanish term "enlace" used elsewhere in the same file.
    - Current: `Link disponible`
    - Source: `Link available`
    - Suggest: `Enlace disponible`
    - Other strings (add_custom_autocomplete_label, biometric_auth_open_link_new_session) translate "link" as "enlace"; leaving it as "Link" is inconsistent terminology.
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — The ampersand in the settings path is left untranslated instead of using "y".
    - Current: `Privacidad &amp; Seguridad`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `Privacidad y seguridad`
    - Spanish does not use "&" as a conjunction in menu paths; the en-US "Privacy & Security" should be rendered with "y".
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` quotes “agregar a la página de inicio” but the string it names, `menu_add_to_home_screen`, reads “Agregar a la pantalla de inicio”
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Agregar a la pantalla de inicio`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Presiona “Volver a intentarlo”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `mozac_feature_prompts_identity_credentials_privacy_policy_description` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rMX/strings.xml` — A period was added after "Términos de Servicio" that is not in the source.
    - Current: `Términos de Servicio.{ </a> }`
    - Source: `Logging in to %1$s with a %2$s account is subject to their <a href="%3$s">Privacy Policy{ </a> } and <a href="%4$s">Terms of Service{ </a> }`
    - Suggest: `Términos de Servicio{ </a> }`
    - The source string has no final period inside the link text; the added period appears inside/next to the link markup.
- `mozac_feature_pwa_site_controls_notification_text` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-es-rMX/strings.xml` — Trailing period added that is not in the source.
    - Current: `Toca para copiar la URL de esta aplicación.`
    - Source: `Tap to copy the URL for this app`
    - Suggest: `Toca para copiar la URL de esta aplicación`
    - The source "Tap to copy the URL for this app" has no final punctuation.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” o “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Curly quotation marks are reversed (closing mark used to open and vice versa).
    - Current: `las preferencias de ”siempre traducir“ y ”nunca traducir“`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `las preferencias de “siempre traducir” y “nunca traducir”`
    - The locale convention is curly double quotes; here the opening quote uses ” and the closing uses “, inverted from correct usage.
- `download_language_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Unnecessary capitalization of "Idiomas" copied from English title case.
    - Current: `Descargar Idiomas`
    - Source: `Download Languages`
    - Suggest: `Descargar idiomas`
    - Spanish does not use English title case; the parallel string download_languages_translations_toolbar_title_preference is "Descargar idiomas".
- `micro_survey_privacy_notice_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Unnecessary capitalization of "Privacidad" in a sentence-case link label.
    - Current: `Aviso de Privacidad`
    - Source: `Privacy notice`
    - Suggest: `Aviso de privacidad`
    - Spanish uses sentence case; the source "Privacy notice" is not capitalized on the second word.
- `preference_enhanced_tracking_protection_custom_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — Final period from the source sentence is missing.
    - Current: `Elige qué rastreadores y secuencias de comandos bloquear`
    - Source: `Choose which trackers and scripts to block.`
    - Suggest: `Elige qué rastreadores y secuencias de comandos bloquear.`
    - The source "Choose which trackers and scripts to block." ends with a period, as do the sibling description strings.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Eliminar automáticamente los datos de navegación cuando selecciones "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Salir”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `sports_widget_error_connection_interrupted` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — The em dash of the source was replaced with a colon, deviating from the em-dash convention.
    - Current: `Conexión interrumpida: actualizaciones en vivo pausadas.`
    - Source: `Connection interrupted — live updates paused.`
    - Suggest: `Conexión interrumpida — actualizaciones en vivo pausadas.`
    - Source uses an em dash and the locale convention is em dash; the punctuation should be preserved.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `“Agregar a la pantalla de inicio”`
    - The locale's quote convention is `curly-double` (12 occurrences).

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

### Resolved to date (0)

_Nothing resolved yet._
