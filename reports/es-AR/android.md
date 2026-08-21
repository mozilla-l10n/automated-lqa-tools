# Android l10n QA — es-AR

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `7134a6c77a67` |
| **Previous run** | 2026-08-21 @ `0d02c6c9f0f6` |
| **Mode** | incremental |
| **Strings reviewed this run** | 3 of 2,911 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-AR: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (5)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Intentar de nuevo” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Probar de nuevo”
    - Current: `{ <p> }El navegador está funcionando en el modo sin conexión y no puede conectarse al ítem solicitado.{ </p> }{ <ul> }{ <li> }¿El dispositivo está conectado a una red activa?{ </li> }{ <li> }Presioná “Intentar de nuevo”…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Probar de nuevo`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Elimina automáticamente los datos de navegación cuando seleccionás "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Salir”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `search_add_custom_engine_search_string_example` uses straight double quotes
    - Current: `Reemplazar la consulta con "%s". Ejemplo: https://www.google.com/search?q=%s`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `Reemplazar la consulta con “%s”. Ejemplo:`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `debe contener “https://” o “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Volvé a tus sitios favoritos en %1$s rápidamente. Seleccioná "Agregar a pantalla de inicio" en el menú de %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `“Agregar a pantalla de inicio”`
    - The locale's quote convention is `curly-double` (12 occurrences).

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
| Strings | 2,911 |
| Missing strings | 0 |
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
| Typography deviations from this locale's own norm | 4 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 12, `straight-double` 4 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |
| inverted marks | `open-question` 114, `open-exclamation` 27 | **open-question** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (138)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 47 |
| 3 | Degraded language (grammar, spelling, terminology) | 82 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_httpsonly_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Singular "Secure Site Not Available" translated as a plural statement that no secure sites are available.
    - Current: `No hay sitios seguros disponibles`
    - Source: `Secure Site Not Available`
    - Suggest: `Sitio seguro no disponible`
    - The source refers to this specific site having no HTTPS version, not to secure sites in general being unavailable.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — First paragraph is a copy of the net_interrupt message instead of translating "The network link was interrupted while negotiating a connection."
    - Current: `El navegador se conectó con éxito, pero se interrumpió la conexión mientras se transfería la información. Volvé a probar.`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `El enlace de red se interrumpió mientras se negociaba una conexión. Volvé a probar.`
    - The source says the network link was interrupted while negotiating a connection; the target instead states the browser connected successfully and the connection was interrupted while transferring information, which is the text of a different error page.
- `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — "The connection was reset" is rendered as "the connection was re-established", reversing the meaning.
    - Current: `Se restableció la conexión`
    - Source: `The connection was reset`
    - Suggest: `Se reinició la conexión`
    - "Reset" here means the connection was dropped/reset by the peer; "Se restableció la conexión" reads as the connection being restored, the opposite of an error.
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — "Try connecting on a different device" mistranslated as connecting to a different device.
    - Current: `Probá conectarte a un dispositivo diferente.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `Probá conectarte desde un dispositivo diferente.`
    - The source suggests using another device to connect, not connecting to another device.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Button name in the message does not match the actual button label "Probar de nuevo".
    - Current: `Presioná “Intentar de nuevo”`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Presioná “Probar de nuevo”`
    - The source quotes the “Try Again” button, which is translated as "Probar de nuevo" in mozac_browser_errorpages_page_refresh; the quoted label must match.
- `mozac_browser_errorpages_safe_browsing_unwanted_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — "serving unwanted software" mistranslated as "instalar software no deseado".
    - Current: `por instalar software no deseado`
    - Source: `{ <p> }The site at %1$s has been reported as serving unwanted software and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `por distribuir software no deseado`
    - The source says the site has been reported as serving (distributing) unwanted software, not installing it.
- `mozac_browser_toolbar_content_description_tracking_protection_off_for_a_site1` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-es-rAR/strings.xml` — The translation adds "ahora" (now), which is not in the source.
    - Current: `La protección de rastreo ahora está deshabilitada para este sitio`
    - Source: `Tracking Protection is off for this site`
    - Suggest: `La protección contra rastreo está deshabilitada para este sitio`
    - Source is "Tracking Protection is off for this site"; there is no "now". Also "protección de rastreo" is inconsistent with "protección contra rastreo" used in the neighboring strings.
- `mozac_feature_addons_permissions_downloads_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — "read and modify" translated as "leer o modificar" (or instead of and).
    - Current: `leer o modificar el historial de descargas del navegador`
    - Source: `Download files and read and modify the browser’s download history`
    - Suggest: `leer y modificar el historial de descargas del navegador`
    - Source says "read and modify"; the conjunction was changed to "o", and the parallel _for_update string correctly uses "y".
- `mozac_feature_addons_unsupported_caption_plural_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — "extensions" is rendered as "complementos" (add-ons) instead of "extensiones", inconsistent with the singular string.
    - Current: `%1$s complementos`
    - Source: `%1$s extensions`
    - Suggest: `%1$s extensiones`
    - Source says "extensions"; the singular counterpart mozac_feature_addons_unsupported_caption_2 correctly uses "extensión".
- `mozac_feature_applinks_normal_confirm_dialog_message` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-es-rAR/strings.xml` — The message reverses the meaning: the source asks whether the user wants to leave the browser app to view the content, not whether the app should show the content.
    - Current: `¿Querés dejar que %s muestre este contenido?`
    - Source: `Would you like to leave %s to view this content?`
    - Suggest: `¿Querés salir de %s para ver este contenido?`
    - Source: "Would you like to leave %s to view this content?" where %s is the browser app name; the translation says "let %s show this content", which is the opposite action.
- `mozac_feature_contextmenu_snackbar_action_switch` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-es-rAR/strings.xml` — "Switch" (switch to the newly opened tab) is rendered as "Intercambiar" (exchange/swap).
    - Current: `Intercambiar`
    - Source: `Switch`
    - Suggest: `Cambiar`
    - Per the developer comment, clicking the action switches to the newly opened tab; "Intercambiar" means to swap/exchange things, not to switch views.
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rAR/strings.xml` — The translation reverses the meaning: the source labels a text input field, not an instruction to "enter a field".
    - Current: `Etiqueta para ingresar un campo de entrada de texto`
    - Source: `Label for entering a text input field`
    - Suggest: `Etiqueta del campo de entrada de texto`
    - "Label for entering a text input field" refers to the label of the text input field; the target reads "Label to enter a text input field", changing the meaning.
- `mozac_summarize_download_progress_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rAR/strings.xml` — "One-time download" is rendered as an imperative/verbal phrase instead of a noun phrase describing the download.
    - Current: `Descarga una sola vez para resúmenes privados.`
    - Source: `One-time download for private summaries.`
    - Suggest: `Descarga única para resúmenes privados.`
    - The source is a noun phrase describing the in-progress download ("One-time download for private summaries."); "Descarga una sola vez" reads as the imperative "Download one time", changing the meaning.
- `mozac_ui_tabcounter_duplicate_tab` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-es-rAR/strings.xml` — Menu action "Duplicate tab" translated as a noun phrase "Pestaña duplicada" (duplicated tab) instead of the imperative verb.
    - Current: `Pestaña duplicada`
    - Source: `Duplicate tab`
    - Suggest: `Duplicar pestaña`
    - The developer comment says it is a menu option to duplicate the current tab; the target reads as a status message "tab duplicated", not an action.
- `a11y_completed_task_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Completed task" translated as "Tarea completa" (complete/whole task) rather than "Tarea completada".
    - Current: `Tarea completa`
    - Source: `Completed task`
    - Suggest: `Tarea completada`
    - The accessibility description marks a task as finished; "completa" means full/whole, while "completada" conveys completion.
- `addresses_oblast` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Oblast" is rendered as "Provincia autónoma", which names a different administrative concept.
    - Current: `Provincia autónoma`
    - Source: `Oblast`
    - Suggest: `Óblast`
    - The source term "Oblast" is the administrative division used in Russia and Ukraine; "provincia autónoma" is not equivalent and misnames the field.
- `bookmarks_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Count label translated as a past-tense sentence instead of the adjective "selected".
    - Current: `Se seleccionó %1$d`
    - Source: `%1$d selected`
    - Suggest: `%1$d seleccionados`
    - Source "%1$d selected" is a title showing how many bookmarks are selected; "Se seleccionó %1$d" reads as a singular past action and does not agree when the count is plural.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Singular "this permission" is rendered as "todos los permisos" (all permissions).
    - Current: `¿Estás seguro de que querés eliminar todos los permisos de este sitio?`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `¿Estás seguro de que querés eliminar este permiso de este sitio?`
    - Source clears a single permission for the site; the translation says all permissions, duplicating the meaning of confirm_clear_permissions_site.
- `confirm_clear_permissions_site` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "for this site" is translated as "de todos los sitios" (all sites).
    - Current: `¿Estás seguro de que querés eliminar todos los permisos de todos los sitios?`
    - Source: `Are you sure that you want to clear all the permissions for this site?`
    - Suggest: `¿Estás seguro de que querés eliminar todos los permisos de este sitio?`
    - The dialog clears permissions for one site only, per the developer comment; the translation says all sites, matching confirm_clear_permissions_on_all_sites instead.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Debug locales" is translated as "Idiomas de depuración" (debug languages) instead of locales/configuraciones regionales.
    - Current: `Idiomas de depuración para habilitar`
    - Source: `Debug locales to enable`
    - Suggest: `Configuraciones regionales de depuración para habilitar`
    - The source refers to locales (region/language combinations used for address formats), not just languages; the related string uses "localización" for locale.
- `download_languages_fetch_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Please check back later" is translated as "Intentalo de nuevo más tarde" (try again later).
    - Current: `Intentalo de nuevo más tarde.`
    - Source: `Couldn’t load languages. Please check back later.`
    - Suggest: `Volvé a revisar más tarde.`
    - The source asks the user to check back later, not to retry the action; also the enclitic pronoun conflicts with the pronoun-free style of the other error strings ("Probá de nuevo").
- `download_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "%1$d selected" is rendered as a singular past-tense sentence that misstates the count label.
    - Current: `Se seleccionó %1$d`
    - Source: `%1$d selected`
    - Suggest: `%1$d seleccionados`
    - The source is a count label (number of downloads selected) shown in the app bar; "Se seleccionó %1$d" reads as a singular statement and does not match the plural-neutral label form used elsewhere.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Redirect Trackers" (a noun category of trackers) is rendered as the verb phrase "Redirigir rastreadores" ("redirect trackers").
    - Current: `Redirigir rastreadores`
    - Source: `Redirect Trackers`
    - Suggest: `Rastreadores de redireccionamiento`
    - Per the developer comment this is a category of trackers, not an action; the translation reverses it into an imperative verb phrase.
- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — The product name "Firefox Suggest" is translated instead of kept as-is.
    - Current: `Sugerencia de Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a Mozilla feature/brand name that should remain untranslated; the target also changes it to a singular "suggestion".
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Shortcuts" (home screen site shortcuts) is rendered as "atajos de teclado" (keyboard shortcuts).
    - Current: `Mostrar todos los atajos de teclado`
    - Source: `Show all shortcuts`
    - Suggest: `Mostrar todos los atajos`
    - The developer comment says the button navigates to a screen displaying all the home screen shortcuts, not keyboard shortcuts; the sibling string homepage_shortcuts_add_shortcut uses "atajo" alone.
- `ip_protection_mozilla_vpn_upsell_headline` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Protect more with Mozilla VPN" is rendered as a reflexive "protect yourself more", changing the meaning.
    - Current: `Protegete más con Mozilla VPN`
    - Source: `Protect more with Mozilla VPN`
    - Suggest: `Protegé más con Mozilla VPN`
    - The source means protecting more things (apps/devices) with Mozilla VPN, not protecting oneself more; the transitive verb should be kept.
- `ip_protection_promo_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Imperative "Browse with extra protection" was turned into a noun phrase, and the possessive "your location" was dropped.
    - Current: `Navegación con protección adicional ocultando la ubicación`
    - Source: `Browse with extra protection by hiding your location, even on public Wi-Fi. %s`
    - Suggest: `Navegá con protección adicional ocultando tu ubicación`
    - The source is an imperative sentence addressed to the user ("Browse ... by hiding your location"), matching ip_protection_onboarding_body_link which is translated as "Navegá con protección adicional".
- `never_translate_site_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Please check back later" is translated as "Intentalo de nuevo más tarde" (try again later), changing the meaning.
    - Current: `Intentalo de nuevo más tarde.`
    - Source: `Couldn’t load sites. Please check back later.`
    - Suggest: `Volvé a consultar más tarde.`
    - The source asks the user to check back later, not to retry the action.
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "No site exceptions" (there are no exceptions for any site) is rendered as "Sin excepciones para el sitio" (no exceptions for the site).
    - Current: `Sin excepciones para el sitio`
    - Source: `No site exceptions`
    - Suggest: `Sin excepciones de sitios`
    - The label appears when there are no site exceptions in the settings list; the source refers to the absence of any site exceptions, not to exceptions of one particular site.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Open tabs menu" (the menu of open tabs) is rendered as an imperative "Abrir menú de pestañas".
    - Current: `Abrir menú de pestañas`
    - Source: `Open tabs menu`
    - Suggest: `Menú de pestañas abiertas`
    - The developer comment says it opens the open tabs menu; the source noun phrase refers to the "open tabs" menu. The translation drops "open" as a modifier of tabs and turns it into a verb.
- `preference_enhanced_tracking_protection_custom_info_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Custom protection info button says "estándar" (standard) instead of "personalizada" (custom).
    - Current: `Esto es lo que está bloqueado por la protección de rastreo estándar`
    - Source: `What’s blocked by custom tracking protection`
    - Suggest: `Qué es lo que está bloqueado por la protección de rastreo personalizada`
    - Source is "What's blocked by custom tracking protection"; the translation duplicates the standard-protection string and names the wrong protection level.
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Present-tense generic description rendered in the past tense.
    - Current: `El archivo se borró del dispositivo y se eliminó del historial de descargas`
    - Source: `File is deleted from your device and removed from download history`
    - Suggest: `El archivo se borra del dispositivo y se elimina del historial de descargas`
    - The source "File is deleted from your device and removed from download history" describes what the setting does in general, not a completed action.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Present-tense generic description rendered in the past tense.
    - Current: `El archivo se eliminó del historial de descargas, pero aún está guardado en el dispositivo`
    - Source: `File is removed from your download history, but is still saved on your device`
    - Suggest: `El archivo se elimina del historial de descargas, pero sigue guardado en el dispositivo`
    - The source "File is removed from your download history, but is still saved on your device" describes the option's behaviour, not a past event.
- `preferences_show_search_optimization_cards` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Retrieve suggestions from Mozilla as you type" is rendered as "Mostrar sugerencias…" (show) instead of retrieve/obtain.
    - Current: `Mostrar sugerencias de Mozilla mientras se escribe`
    - Source: `Retrieve suggestions from Mozilla as you type`
    - Suggest: `Obtener sugerencias de Mozilla mientras se escribe`
    - The source verb is "Retrieve" (fetch from Mozilla), not "Show"; other strings in the same surface use "Obtener" for retrieving suggestions (e.g. preferences_show_nonsponsored_suggestions_summary).
- `preferences_show_trending_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Show trending suggestions" is translated as "las sugerencias más populares" (the most popular suggestions), a superlative not in the source.
    - Current: `Mostrar las sugerencias más populares`
    - Source: `Show trending suggestions`
    - Suggest: `Mostrar sugerencias en tendencia`
    - The source means trending suggestions, not "the most popular" ones; the added definite article and superlative change the meaning.
- `qr_code_display_share_nearby` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Share link nearby" mistranslated as "share nearby link".
    - Current: `Compartir enlace cercano`
    - Source: `Share link nearby`
    - Suggest: `Compartir enlace con dispositivos cercanos`
    - In the source, "nearby" modifies the sharing action (share the link with people nearby), not the link; the translation says the link itself is nearby.
- `remote_improvements_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Present-tense "Changes applied remotely" rendered as a past tense statement.
    - Current: `Los cambios se aplicaron remotamente.`
    - Source: `Firefox will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `Los cambios se aplican remotamente.`
    - The source states that changes are applied remotely (general/ongoing), not that they were already applied.
- `search_engine_edit_custom_search_engine_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Edit search engine" was translated as "Agregar buscador" (Add search engine).
    - Current: `Agregar buscador`
    - Source: `Edit search engine`
    - Suggest: `Editar buscador`
    - The source and developer comment refer to the Edit search engine screen, not adding one.
- `settings_search_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Content description for the button that opens search-through-settings is translated as "Botón de búsqueda de configuración", reversing the meaning.
    - Current: `Botón de búsqueda de configuración`
    - Source: `Settings search button`
    - Suggest: `Botón para buscar en la configuración`
    - The comment states the button opens Settings Search (to search through settings), not settings for search.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Search settings" (with "Search" as a verb per the comment) is rendered as "Configuración de búsqueda", meaning search-related settings.
    - Current: `Configuración de búsqueda`
    - Source: `Search settings`
    - Suggest: `Buscar en la configuración`
    - The developer comment explicitly says "Search" is a verb here: the screen lets the user search through settings, not configure search.
- `tab_tray_inactive_auto_close_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "haven’t viewed" mistranslated as "no abriste" (didn't open) instead of "no viste".
    - Current: `pestañas que no abriste durante el último mes`
    - Source: `%1$s can close tabs you haven’t viewed over the past month.`
    - Suggest: `pestañas que no viste durante el último mes`
    - The source says tabs you haven't viewed, not tabs you haven't opened; the sibling string tab_tray_inactive_onboarding_message correctly uses "no se vieron".
- `add_custom_autocomplete_label` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Add link to autocomplete" (add the link to the autocomplete list) is rendered as "Agregar el enlace para autocompletar" (add the link in order to autocomplete).
    - Current: `Agregar el enlace para autocompletar`
    - Source: `Add link to autocomplete`
    - Suggest: `Agregar el enlace a autocompletado`
    - The developer comment says the button quick-adds the current URL to the custom autocomplete list; "para autocompletar" states a purpose rather than the destination list.
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "site" is translated as "página web" (web page) while the rest of the file uses "sitio web", and "any time" is dropped.
    - Current: `Evitamos que esta página web te espíe. Presioná el escudo para ver lo que estamos bloqueando.`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `Evitamos que este sitio web te espíe. Presioná el escudo en cualquier momento para ver lo que estamos bloqueando.`
    - The source says "this site" (elsewhere rendered "sitio web", e.g. content_description_reload) and "Tap the shield any time"; the time qualifier is omitted.
- `cookie_banner_exception_panel_description_site_is_not_supported` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Reverses the subject: the source says the feature does not support the site, the translation says the site does not support the feature.
    - Current: `Este sitio actualmente no soporta la reducción de mensajes de cookies.`
    - Source: `This site is currently not supported by Cookie Banner Reduction. Would you like to request our team review this website and add support in the future?`
    - Suggest: `Este sitio actualmente no es compatible con la reducción de mensajes de cookies.`
    - en-US: "This site is currently not supported by Cookie Banner Reduction" — the site is unsupported by the feature, not the other way around.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Plural "custom URLs" rendered as singular.
    - Current: `Borrar URL personalizada`
    - Source: `Remove custom URLs`
    - Suggest: `Borrar URL personalizadas`
    - The source is "Remove custom URLs" (plural, screen for removing multiple URLs), but the target reads as a single URL, identical in form to the singular add-title string.
- `preference_category_switching_apps` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Switching Apps" (changing between apps) is rendered as "Intercambio de aplicaciones" (exchange of apps).
    - Current: `Intercambio de aplicaciones`
    - Source: `Switching Apps`
    - Suggest: `Cambio entre aplicaciones`
    - The developer comment says the category covers stealth settings while switching between apps, not exchanging apps.
- `preference_open_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Switch to link in new tab" is mistranslated as "Cambiar a enlazar" (switch to linking), turning the noun "link" into a verb.
    - Current: `Cambiar a enlazar en nueva pestaña inmediatamente`
    - Source: `Switch to link in new tab immediately`
    - Suggest: `Cambiar al enlace en nueva pestaña inmediatamente`
    - The source refers to switching to the opened link's new tab; "enlazar" is the verb "to link" and changes the meaning.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Regulation (EU)" is rendered as "Regulación (EU)" instead of the official Spanish name "Reglamento (UE)".
    - Current: `la Regulación (EU) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `el Reglamento (UE) 2024/1183`
    - The EU legal instrument "Regulation" is officially "Reglamento" in Spanish and the country code is "UE", not "EU"; the current text names the instrument incorrectly.
- `tip_autocomplete_url` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Autocomplete URLs" (a noun-phrase feature description) is rendered as the imperative "Autocomplete las URLs", and the string uses formal usted instead of the locale's voseo.
    - Current: `Autocomplete las URLs para los sitios que más usa Mantenga presionada cualquier URL en la barra de direcciones`
    - Source: `Autocomplete URLs for sites you use most  Long-press any URL in the address bar`
    - Suggest: `Autocompletá las URL de los sitios que más usás Mantené presionada cualquier URL en la barra de direcciones`
    - The source tip tells the user how to autocomplete URLs; the target's formal imperatives ("Autocomplete", "usa", "Mantenga") clash with the voseo register used in the other tips ("Conseguí acceso… que más usás").

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_net_interrupt_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Imperative "revisa" is not the voseo form used consistently elsewhere ("revisá").
    - Current: `revisa la conexión wifi`
    - Source: `{ <p> }The browser connected successfully, but the connection was interrupted while transferring information. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again i…`
    - Suggest: `revisá la conexión wifi`
    - es-AR uses voseo imperatives; the parallel string mozac_browser_errorpages_net_reset_message uses "revisá".
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Gender agreement error: "una pedido".
    - Current: `no respondió a una pedido de conexión`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `no respondió a un pedido de conexión`
    - "pedido" is masculine, so the article must be "un".
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Misspelling "Verifiá" instead of "Verificá".
    - Current: `Verifiá el sitio`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `Verificá el sitio`
    - Typo in the voseo imperative of "verificar".
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Duplicated/garbled clause: "el proxy no se encontró el servidor".
    - Current: `pero el proxy no se encontró el servidor`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `pero no se pudo encontrar el proxy`
    - The source says "but the proxy could not be found"; the target sentence is ungrammatical and mixes two constructions.
- `mozac_feature_addons_find_more_extensions_button_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — Missing accent on "más" in the button label.
    - Current: `Buscar mas extensiones`
    - Source: `Find more extensions`
    - Suggest: `Buscar más extensiones`
    - "mas" without accent is the conjunction "but"; the quantifier "more" requires the accented "más".
- `mozac_feature_addons_permissions_user_scripts_extra_warning` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — Misspelled verb form "confíés" (double accent).
    - Current: `en las que confíés`
    - Source: `Unverified scripts can pose security and privacy risks. Only run scripts from extensions or sources you trust.`
    - Suggest: `en las que confíes`
    - The present subjunctive of "confiar" is "confíes"; "confíés" carries an extra accent and is not a valid Spanish form.
- `mozac_feature_addons_unavailable_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — Section heading for multiple add-ons is rendered in singular verb form instead of a plural/neutral heading.
    - Current: `Todavía no está disponible`
    - Source: `Not yet available`
    - Suggest: `Todavía no disponibles`
    - The string labels a section listing add-ons that are not yet available; the singular "está disponible" does not agree with the section of items.
- `mozac_feature_addons_unsupported_section` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — Section heading uses a singular verb form instead of a plural/neutral heading.
    - Current: `Todavía no es compatible`
    - Source: `Not yet supported`
    - Suggest: `Todavía no compatibles`
    - The string labels a section of not-yet-supported add-ons; singular "es compatible" does not agree with the listed items.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Menú ítem para %s" is ungrammatical; Spanish requires a preposition between the nouns.
    - Current: `Menú ítem para %s`
    - Source: `Item Menu for %s`
    - Suggest: `Menú del ítem para %s`
    - The source "Item Menu for %s" is a noun-noun compound; Spanish cannot juxtapose nouns this way, it needs "Menú de ítem/del ítem". This is a screen-reader content description, so clarity matters.
- `create_collection_deselect_all` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Dejar deseleccionar todo" is ungrammatical for "Deselect all".
    - Current: `Dejar deseleccionar todo`
    - Source: `Deselect all`
    - Suggest: `Deseleccionar todo`
    - The source is a simple button label "Deselect all"; the extra verb "Dejar" makes the phrase ungrammatical and changes the meaning.
- `debug_drawer_tab_tools_tab_count_active` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Gender inconsistency: "Activo" is masculine while the parallel tab-count labels use feminine ("Inactiva", "Privada") agreeing with "pestaña".
    - Current: `Activo`
    - Source: `Active`
    - Suggest: `Activa`
    - All three strings label tab count categories (pestañas), so the adjective should agree in feminine like the sibling strings.
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Gender inconsistency between the On/Off pair: "Desactivada" (feminine) vs "Activado" (masculine) for the same preference summary.
    - Current: `Desactivada`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The paired string delete_browsing_data_quit_on is translated as "Activado"; the off state must agree in gender with the same referent.
- `firefox_labs_banner_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Typo in "Pruobá" (should be "Probá").
    - Current: `¡Pruobá nuestras funciones experimentales!`
    - Source: `Try our experimental features!`
    - Suggest: `¡Probá nuestras funciones experimentales!`
    - "Pruobá" is not a Spanish word; the voseo imperative of "probar" is "probá".
- `firefox_labs_restore_defaults_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Infinitive "reiniciar" used instead of the voseo imperative used in the parallel dialog strings.
    - Current: `Para restaurar los valores predeterminados, reiniciar %s.`
    - Source: `To restore defaults, restart %s.`
    - Suggest: `Para restaurar los valores predeterminados, reiniciá %s.`
    - The source is an imperative addressed to the user, and the sibling strings firefox_labs_feature_enable/disable_dialog_message use "reiniciá %s".
- `lens_camera_qr_no_code_found` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Definite article used where the source is indefinite: "No QR code found" refers to any QR code.
    - Current: `No se encontró el código QR en la imagen`
    - Source: `No QR code found in image`
    - Suggest: `No se encontró ningún código QR en la imagen`
    - The source states no QR code at all was found in the image; "el código QR" implies a specific, previously known code.
- `nova_onboarding_marketing_body_link_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Missing accent on the interrogative/relative adverb "Cómo" in the link text.
    - Current: `Como usamos los datos`
    - Source: `How we use the data`
    - Suggest: `Cómo usamos los datos`
    - In "How we use the data" rendered as a nominal phrase, Spanish requires the accented "Cómo"; "Como" without accent means "as/like" or "I eat".
- `onboarding_marketing_redesign_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Missing accent on the interrogative/relative adverb "Cómo" in "Como usamos los datos".
    - Current: `Como usamos los datos`
    - Source: `How we use the data`
    - Suggest: `Cómo usamos los datos`
    - The source "How we use the data" is an indirect-question/nominalized phrase requiring the accented "Cómo"; "Como" without accent means "as/like".
- `onboarding_redesign_tou_subheader_two` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Adjective agreement misattaches "automática" to "protección" instead of "rastreo", changing the meaning from automatic protection to automatic tracking.
    - Current: `Protección contra rastreo automática`
    - Source: `Automatic tracking protection`
    - Suggest: `Protección automática contra rastreo`
    - The source is "Automatic tracking protection": the protection is automatic, not the tracking. The current word order reads ambiguously/incorrectly.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Missing accent on interrogative "qué" and dropped preposition/subject in the relative clause.
    - Current: `haciendo más difícil que otros vean que sitio web está tratando de acceder`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `haciendo más difícil que otros vean a qué sitio web está tratando de acceder`
    - The source says "see which website you’re about to access"; "que sitio web está tratando de acceder" lacks the accent on "qué" and the required preposition "a" (acceder a).
- `preference_enhanced_tracking_protection_standard_description_5` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Verb tense/subject mismatch: "bloquean" should agree with the future/impersonal construction used for "block fewer trackers".
    - Current: `Las páginas se van a cargar normalmente, pero bloquean menos rastreadores`
    - Source: `Pages will load normally, but block fewer trackers.`
    - Suggest: `Las páginas se van a cargar normalmente, pero se van a bloquear menos rastreadores`
    - In the source, the subject of "block fewer trackers" is the protection setting, not the pages; "las páginas … bloquean menos rastreadores" says the pages do the blocking, and the tenses are inconsistent.
- `preferences_open_links_in_a_private_tab` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Plural "links" rendered as singular "enlace".
    - Current: `Abrir enlace en una pestaña privada`
    - Source: `Open links in a private tab`
    - Suggest: `Abrir enlaces en una pestaña privada`
    - Source says "Open links in a private tab" (plural), and the sibling string preferences_open_links_in_apps uses "enlaces".
- `restart_and_shortcuts_removal_warning_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Ungrammatical fragment "que haya se guardado" and inconsistent formal/informal address within the same string.
    - Current: `cualquier sitio y acceso directo que haya se guardado en la pantalla de inicio.`
    - Source: `Changing the icon will remove any sites and shortcuts you’ve saved to your Home screen.   %1$s may close. Tap your new icon to reopen.`
    - Suggest: `cualquier sitio y acceso directo que hayas guardado en la pantalla de inicio.`
    - "haya se guardado" is not valid Spanish; also the rest of the string uses voseo ("Tocá tu nuevo ícono"), so the second person should be consistent.
- `sports_widget_go_to_world_cup_site_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Incorrect capitalization of the article in "Copa Del Mundo".
    - Current: `Copa Del Mundo`
    - Source: `Go to World Cup site`
    - Suggest: `Copa del Mundo`
    - In Spanish the article in "Copa del Mundo" is lowercase, as correctly written in the other sports_widget strings (e.g. sports_widget_final_results_content_description).
- `tab_tray_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Singular verb form doesn't agree with the variable count in the multi-select title.
    - Current: `Se seleccionó %1$d`
    - Source: `%1$d selected`
    - Suggest: `%1$d seleccionadas`
    - %1$d is the number of selected tabs, which is usually plural; "Se seleccionó %1$d" forces a singular agreement and is ungrammatical for counts greater than one.
- `top_sites_sponsored_label` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Singular label for a single sponsored top site rendered in plural.
    - Current: `Patrocinados`
    - Source: `Sponsored`
    - Suggest: `Patrocinado`
    - The developer comment says the label is displayed for a (single) sponsored top site; the source "Sponsored" is singular.
- `trackers_blocked_panel_num_cross_site_cookies` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Singular variant uses the plural noun "cookies".
    - Current: `[one] %1$d cookies de rastreo de sitios cruzados`
    - Source: `{$quantity ->} [one] %1$d cross-site tracking cookie [other] %1$d cross-site tracking cookies`
    - Suggest: `[one] %1$d cookie de rastreo de sitios cruzados`
    - The source singular is "cross-site tracking cookie"; the es-AR singular form must agree in number.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Dangling gerund construction "Enviándolo nos ayudará" is ungrammatical as the subject of the verb.
    - Current: `Enviándolo nos ayudará a mejorar %1$s.`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Enviarlo nos ayudará a mejorar %1$s.`
    - In Spanish the subject of "ayudará" must be a noun/infinitive, not a gerund; the parallel plural string correctly uses "Enviarlos nos ayudará".
- `firstrun_defaultbrowser_text2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Bloquéa" is misspelled (accent on wrong syllable) and the imperative form is inconsistent with the voseo used elsewhere.
    - Current: `Bloquéa publicidades`
    - Source: `Take private browsing to the next level. Block ads and other content that can track you across sites and bog down page load times.`
    - Suggest: `Bloqueá publicidades`
    - The es-AR voseo imperative of "bloquear" is "bloqueá"; "Bloquéa" is not a valid Spanish form.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Ésto" is misspelled; the neuter demonstrative "esto" never takes an accent.
    - Current: `Ésto podría ser un problema`
    - Source: `This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server. { <br/> }{ <br/> } If you’ve connected to this server successfully in the past, the error may be temporar…`
    - Suggest: `Esto podría ser un problema`
    - Per RAE, the neuter demonstrative pronoun "esto" is never accented.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Extra preposition "de" makes the phrase ungrammatical.
    - Current: `Usar la huella digital de para desbloquear la aplicación`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `Usar la huella digital para desbloquear la aplicación`
    - Source is "Use fingerprint to unlock app"; the stray "de" before "para" is a typo.
- `tip_add_to_homescreen` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Stray preposition "a" before the line-break placeholder makes the sentence ungrammatical.
    - Current: `con un toque a %1$s Menú`
    - Source: `Get one-tap access to sites you use most%1$s Menu > Add to Home screen`
    - Suggest: `con un toque%1$s Menú`
    - The source ends the first clause at "you use most" and %1$s is a line break, so the trailing "a" is a leftover that breaks the sentence.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Intentar de nuevo” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Probar de nuevo”
    - Current: `{ <p> }El navegador está funcionando en el modo sin conexión y no puede conectarse al ítem solicitado.{ </p> }{ <ul> }{ <li> }¿El dispositivo está conectado a una red activa?{ </li> }{ <li> }Presioná “Intentar de nuevo”…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Probar de nuevo`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mozac_feature_addons_permissions_all_urls_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — The update variant uses the noun "Acceso" while the base string uses the infinitive "Acceder" for the same source.
    - Current: `Acceso a los datos para todos los sitios web.`
    - Source: `Access your data for all websites.`
    - Suggest: `Acceder a los datos para todos los sitios web.`
    - mozac_feature_addons_permissions_all_urls_description renders the identical source "Access your data for all websites" as "Acceder a los datos para todos los sitios web"; inconsistent verb form on the same permission list.
- `mozac_feature_addons_permissions_browser_settings_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — "browser settings" is rendered as "configuración" here but as "ajustes" in the equivalent base permission string.
    - Current: `Leer y modificar la configuración del navegador.`
    - Source: `Read and modify browser settings.`
    - Suggest: `Leer y modificar los ajustes del navegador.`
    - mozac_feature_addons_permissions_browser_setting_description translates the same source as "Leer y modificar los ajustes del navegador"; the pair shown together must use the same term.
- `mozac_feature_addons_permissions_clipboard_write_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — The update-notification variant uses a different verb than the base string for the same source text "Input data to the clipboard".
    - Current: `Enviar datos al portapapeles.`
    - Source: `Input data to the clipboard.`
    - Suggest: `Ingresar datos al portapapeles.`
    - mozac_feature_addons_permissions_clipboard_write_description translates the identical source as "Ingresar datos al portapapeles"; the update variant should be consistent on the same surface.
- `mozac_feature_addons_permissions_trial_ml_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rAR/strings.xml` — Permission description rendered as an imperative command to the user instead of an infinitive describing what the add-on can do.
    - Current: `Descargá y ejecutá modelos de IA en tu dispositivo`
    - Source: `Download and run AI models on your device`
    - Suggest: `Descargar y ejecutar modelos de IA en el dispositivo`
    - The source "Download and run AI models on your device" describes a capability the extension requests, like all other permission descriptions in this file ("Acceder a…", "Controlar…"). The voseo imperative turns it into an instruction to the user; the parallel _for_update string correctly uses "Descargar y ejecutar…".
- `mozac_feature_autofill_confirmation_authenticity` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-es-rAR/strings.xml` — Uses "Desea" (usted) instead of the voseo/tuteo register used throughout es-AR strings.
    - Current: `¿Desea continuar autocompletando las credenciales seleccionadas?`
    - Source: `%1$s could not verify the authenticity of the application. Do you want to proceed with autofilling the selected credentials?`
    - Suggest: `¿Querés continuar autocompletando las credenciales seleccionadas?`
    - es-AR uses voseo (e.g. "¿Querés…" in mozac_feature_applinks_normal_confirm_dialog_message); "Desea" is the formal usted form and breaks the locale's form of address.
- `mozac_feature_prompts_choose_a_color` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rAR/strings.xml` — Uses "usted" imperative instead of the voseo register used throughout es-AR.
    - Current: `Elija un color`
    - Source: `Choose a color`
    - Suggest: `Elegí un color`
    - The rest of the batch uses voseo ("Tocá", "Mantené", "Asegurate", "¿Querés?"); "Elija" is the usted form and breaks the locale's established form of address.
- `mozac_feature_prompts_jan` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rAR/strings.xml` — The short form for January in Spanish is "Ene", not "En".
    - Current: `En`
    - Source: `Jan`
    - Suggest: `Ene`
    - Standard Spanish three-letter month abbreviation for enero is "Ene"; "En" is inconsistent with the other abbreviations such as "Dic".
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-es-rAR/strings.xml` — "crash" rendered as "colgada", inconsistent with "fallo(s)" used in all other crash strings in the same file.
    - Current: `Recopilando datos de la colgada`
    - Source: `Gathering crash data`
    - Suggest: `Recopilando datos del fallo`
    - Every other string in this file translates "crash" as "fallo"; "colgada" is an inconsistent and colloquial term for the same surface.
- `addons_does_not_require_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "extension" is rendered as "complemento" (add-on) instead of "extensión", inconsistent with the other extension strings in this batch.
    - Current: `Este complemento no requiere ningún permiso.`
    - Source: `This extension doesn’t require any permissions.`
    - Suggest: `Esta extensión no requiere ningún permiso.`
    - The source says "extension"; elsewhere (addon_ga_message_*) the locale correctly uses "extensiones". "Complemento" is the term for "add-on".
- `addons_permissions_allow_for_all_sites_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses tuteo forms ("confías", "puedes") instead of the voseo/es-AR form of address used elsewhere in the locale.
    - Current: `Si confías en esta extensión, puedes darle permisos en todos los sitios web.`
    - Source: `If you trust this extension, you can give it permission on every website.`
    - Suggest: `Si confiás en esta extensión, podés darle permisos en todos los sitios web.`
    - es-AR consistently uses voseo (confiás, podés) for second-person address; "confías/puedes" is es-ES/neutral tuteo and breaks register consistency.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Register switches from impersonal to voseo within the same string.
    - Current: `Después, se podrá desbloquear todo lo que quieras seguir usando.`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `Después, vas a poder desbloquear todo lo que quieras seguir usando.`
    - The source uses second person throughout ("You won’t see…", "you can unblock"); the translation mixes impersonal "se verán"/"se podrá" with the voseo "quieras", inconsistent with the voseo register used in the surrounding AI-controls strings.
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Regulation (EU)" rendered as "Regulación (EU)" instead of the standard Spanish "Reglamento (UE)".
    - Current: `la Regulación (EU) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `el Reglamento (UE) 2024/1183`
    - The official Spanish name of an EU Regulation is "Reglamento (UE)"; "Regulación (EU)" is a calque with an untranslated abbreviation.
- `download_pause_action` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Content description for the pause action button uses the noun "Pausa" instead of the verb.
    - Current: `Pausa`
    - Source: `Pause`
    - Suggest: `Pausar`
    - The source "Pause" is an action button label/content description; Spanish action labels use the infinitive (cf. "Descargar", "Cancelar", "Borrar" in this batch).
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses the formal "usted" form instead of the voseo/tuteo register used throughout the es-AR locale.
    - Current: `Si continúa al sitio web, no debe ingresar ninguna información sensible. Si continúa, el modo solo HTTPS se desactivará temporalmente para el sitio.`
    - Source: `However, it’s also possible that an attacker is involved. If you continue to the website, you should not enter any sensitive info. If you continue, HTTPS-Only mode will be turned off temporarily for the site.`
    - Suggest: `Si continuás al sitio web, no debés ingresar ninguna información sensible. Si continuás, el modo solo HTTPS se desactivará temporalmente para el sitio.`
    - es-AR strings address the user with voseo (e.g. "Probá de nuevo", "Usaste tus 5 máscaras"); this string switches to formal "usted", breaking the locale's form of address.
- `experiments_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — English term "telemetry" left untranslated in an otherwise Spanish sentence.
    - Current: `Habilitar telemetry para enviar datos.`
    - Source: `Enable telemetry to send data.`
    - Suggest: `Habilitar la telemetría para enviar datos.`
    - "telemetry" is a common noun, not a brand; es-AR uses "telemetría".
- `ip_protection_data_limit_reached_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses formal/third-person "su" instead of the voseo second person used consistently elsewhere in es-AR.
    - Current: `Se usaron los %1$d GB de datos de su VPN.`
    - Source: `You’ve used all %1$d GB of your VPN data. Access resets next month.`
    - Suggest: `Usaste los %1$d GB de datos de tu VPN.`
    - The source "You’ve used all %1$d GB of your VPN data" addresses the user directly; the rest of the batch uses voseo/informal forms ("Probá de nuevo", "para vos"), so "su" breaks the locale's established form of address.
- `phone_feature_blocked_step_settings` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses the tuteo/usted form "Vaya" instead of the voseo form used in the surrounding steps.
    - Current: `1. Vaya a los ajustes de Android`
    - Source: `1. Go to Android Settings`
    - Suggest: `1. Andá a los ajustes de Android`
    - The sibling steps use voseo ("Tocá", "Cambiá"), the established es-AR form of address; "Vaya" is inconsistent usted form.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses peninsular "aquí" alongside voseo, inconsistent with es-AR "acá".
    - Current: `Desactivá aquí para administrar el tamaño de la fuente.`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `Desactivá acá para administrar el tamaño de la fuente.`
    - es-AR convention uses "acá" rather than "aquí"; the string already uses voseo elsewhere.
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Imperative "Usá" breaks the infinitive pattern of the other bullet points in the same list.
    - Current: `Usá la resolución de DNS predeterminada`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `Usar la resolución de DNS predeterminada`
    - Bullets 1, 3, 4 and 5 all use the infinitive ("Usar", "Desactivar"); this one switches to the voseo imperative for the same source construction "Use ...".
- `preference_doh_default_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses formal "su privacidad" where es-AR addresses the user with "tu".
    - Current: `para proteger su privacidad.`
    - Source: `%1$s decides when to use secure DNS to protect your privacy.`
    - Suggest: `para proteger tu privacidad.`
    - The locale addresses the user informally (voseo/tu), as in the neighboring strings; "su" is the usted form.
- `preference_doh_off_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Summary rendered as an imperative while parallel option summaries use infinitive form.
    - Current: `Usá la resolución de DNS predeterminada`
    - Source: `Use your default DNS resolver`
    - Suggest: `Usar la resolución de DNS predeterminada`
    - This is the summary of an option in the same list as "Usar el proveedor seleccionado" / "Solo usar la resolución de DNS predeterminada…", which use the infinitive; the imperative is inconsistent on the same surface.
- `preference_downloads_folder_permission_lost` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses "usted" form instead of the voseo register used elsewhere in es-AR.
    - Current: `No tiene permiso para usar esta carpeta. Pruebe elegir una diferente.`
    - Source: `You don’t have permission to use this folder. Try choosing a different one.`
    - Suggest: `No tenés permiso para usar esta carpeta. Probá elegir una diferente.`
    - es-AR strings address the user with voseo (e.g. "Vos controlás cuándo usar DNS seguro", "¿Estás seguro…?"); the formal "usted" form breaks the locale's form of address.
- `preferences_email_masks_suggest_summary` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Uses the "usted" form ("Oculte su") instead of the voseo/tuteo register used throughout es-AR strings.
    - Current: `Oculte su correo electrónico real para proteger la bandeja de entrada del spam.`
    - Source: `Hide your real email to protect your inbox from spam. Some sites don’t support email masks.`
    - Suggest: `Ocultá tu correo electrónico real para proteger la bandeja de entrada del spam.`
    - es-AR Firefox strings address the user informally (e.g. "Las pestañas que no viste..."); the formal imperative "Oculte su" breaks the established form of address.
- `protection_panel_etp_toggle_label` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Enhanced Tracking Protection" is rendered with a non-standard term instead of the established "Protección contra rastreo mejorada".
    - Current: `Protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra rastreo mejorada`
    - Mozilla's established Spanish term for Enhanced Tracking Protection is "Protección contra rastreo mejorada"; the surrounding strings already use "protección contra rastreo", so "Protección de rastreo aumentada" is inconsistent and mistranslates "Enhanced" as "aumentada".
- `restart_warning_dialog_button_positive_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "icono" is inconsistent with "ícono" used in the surrounding icon-change strings.
    - Current: `Cambiar icono`
    - Source: `Change icon`
    - Suggest: `Cambiar ícono`
    - The related strings (restart_warning_dialog_title, restart_and_shortcuts_removal_warning_dialog_body) use the es-AR spelling "ícono".
- `saved_login_clear_hostname` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Clear" rendered as "Eliminar" while all sibling Clear-field strings use "Borrar".
    - Current: `Eliminar nombre de host`
    - Source: `Clear hostname`
    - Suggest: `Borrar nombre de host`
    - saved_login_clear_username, saved_logins_clear_password and saved_logins_clear_search_text_button_content_description all translate "Clear" as "Borrar"; "Eliminar" (delete) is inconsistent on the same surface.
- `settings_search_clear_recent_searches_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Clear all" is translated as "Eliminar todo" (Delete all) instead of the standard "Borrar todo".
    - Current: `Eliminar todo`
    - Source: `Clear all`
    - Suggest: `Borrar todo`
    - "Clear" is consistently rendered as "Borrar" in Firefox es-AR; "Eliminar" corresponds to "Delete".
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Shortcut" is rendered as "acceso directo" here while the neighbouring shortcut strings use "atajo".
    - Current: `URL del acceso directo`
    - Source: `Shortcut URL`
    - Suggest: `URL del atajo`
    - shortcut_name_hint, shortcut_max_limit_title and shortcut_max_limit_content all translate "shortcut" as "atajo"; this string on the same surface uses a different term.
- `synced_tabs_collapse_group` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Collapse" is rendered as "Ocultar" (hide) instead of "Contraer", inconsistent with the paired "Expandir" string.
    - Current: `Ocultar grupo de pestañas sincronizadas`
    - Source: `Collapse group of synced tabs`
    - Suggest: `Contraer grupo de pestañas sincronizadas`
    - The source says "Collapse group of synced tabs"; the counterpart string uses "Expandir", so the standard antonym "Contraer" is expected. "Ocultar" means "hide".
- `tab_group_onboarding_item_dismiss_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Onboarding" rendered as "incorporación", which is wrong in this UI context.
    - Current: `Descartar la incorporación del grupo de pestañas`
    - Source: `Dismiss tab group onboarding`
    - Suggest: `Descartar la introducción a los grupos de pestañas`
    - The source refers to the onboarding card introducing tab groups; "incorporación" (hiring/joining) is a misleading rendering of the product term.
- `top_sites_menu_settings` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "Settings" translated as "Opciones" instead of the standard "Ajustes/Configuración" used elsewhere.
    - Current: `Opciones`
    - Source: `Settings`
    - Suggest: `Configuración`
    - Inconsistent with the term used for "Settings" elsewhere in the app; "Opciones" corresponds to "Options".
- `uninstall_survey_error_failed` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — "prompt" rendered as "indicador", which does not mean a system dialog/prompt.
    - Current: `No se pudo abrir el indicador de desinstalación del sistema`
    - Source: `Failed to open the system uninstall prompt, please use the system uninstall action directly.`
    - Suggest: `No se pudo abrir el diálogo de desinstalación del sistema`
    - The source refers to the system uninstall prompt (a dialog); "indicador" means an indicator/gauge and misleads the user.
- `biometric_auth_moved_too_quickly` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the "usted" form "Pruebe" instead of the voseo register used elsewhere in es-AR (e.g. "Podés", "Tocá", "Presioná").
    - Current: `El dedo se movió muy rápido. Pruebe de nuevo.`
    - Source: `Finger moved too fast. Try again.`
    - Suggest: `El dedo se movió muy rápido. Probá de nuevo.`
    - The es-AR locale consistently addresses the user with voseo ("Podés usar tu huella digital", "Iniciá tu sesión"); "Pruebe" is the usted imperative and breaks the established form of address.
- `biometric_auth_not_recognized_error` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the "usted" form "Pruebe" instead of the voseo register used elsewhere in es-AR.
    - Current: `Huella digital no reconocida. Pruebe de nuevo.`
    - Source: `Fingerprint not recognized. Try again.`
    - Suggest: `Huella digital no reconocida. Probá de nuevo.`
    - Surrounding biometric strings use voseo ("Podés usar tu huella digital…"); "Pruebe" is the usted imperative and is inconsistent with the locale's form of address.
- `cookie_banner_reject_all_option_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the "usted" imperative "Vea" instead of the es-AR voseo form used throughout the file, and renders "banners" as "anuncios".
    - Current: `Vea menos anuncios rechazando automáticamente`
    - Source: `See fewer banners by automatically rejecting cookie requests, when possible.`
    - Suggest: `Vé menos mensajes de cookies rechazando automáticamente`
    - Other strings in the same file use voseo ("¿Querés pedirle…", "lo que escribás"); "Vea" is the usted form. Also "banners" here refers to cookie banners, translated elsewhere as "mensajes de cookies", not "anuncios" (ads).
- `external_app_prompt` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the formal "Puede" whereas the parallel string external_app_prompt_no_app uses the informal voseo "Podés".
    - Current: `Puede dejar que %1$s abra este enlace en %2$s.`
    - Source: `You can leave %1$s to open this link in %2$s.`
    - Suggest: `Podés dejar que %1$s abra este enlace en %2$s.`
    - es-AR uses the informal voseo register; the sibling string external_app_prompt_no_app renders the same "You can leave %1$s…" as "Podés dejar que %1$s…".
- `firstrun_defaultbrowser_text2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Lleva" uses tuteo imperative while the surrounding first-run strings use voseo ("Potenciá", "Establecé", "Elegí").
    - Current: `Lleva la navegación privada`
    - Source: `Take private browsing to the next level. Block ads and other content that can track you across sites and bog down page load times.`
    - Suggest: `Llevá la navegación privada`
    - es-AR convention is voseo imperatives, as used in the neighboring first-run strings.
- `placeholder_rename_top_site` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Shortcut" is rendered as "atajo" here but as "acceso directo" in menu_remove_from_shortcuts on the same surface.
    - Current: `Nombre del atajo`
    - Source: `Shortcut name`
    - Suggest: `Nombre del acceso directo`
    - Inconsistent terminology for the same source term "Shortcut" within the same app/feature (shortcuts on the home screen).
- `preference_autocomplete_add_error` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses "usted" form while the surrounding autocomplete strings use the "vos/tú" informal form required for es-AR.
    - Current: `Verifique la URL que escribió.`
    - Source: `Double-check the URL you entered.`
    - Suggest: `Verificá la URL que escribiste.`
    - Neighboring strings (preference_autocomplete_explanation_text "Tu lista", preference_autocomplete_user_list_summary2 "tus URLs") use informal address; this string switches to formal register, an inconsistency on the same surface.
- `preference_autocomplete_add_hint` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Formal "usted" imperative conflicts with the informal register used in the same settings screen.
    - Current: `Pegue o escriba una URL`
    - Source: `Paste or enter URL`
    - Suggest: `Pegá o escribí una URL`
    - The same autocomplete screen addresses the user informally ("Tu lista de autocompletado", "tus URLs favoritas"); this hint uses the formal form.
- `preference_category_tracking_protection3` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Enhanced Tracking Protection" uses a non-standard rendering instead of the established Mozilla term.
    - Current: `Protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra el rastreo mejorada`
    - Mozilla's established es-AR term for Enhanced Tracking Protection is "Protección contra el rastreo mejorada"; "aumentada" is inconsistent terminology.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses "usted" verb form instead of the voseo/tuteo register used elsewhere in es-AR.
    - Current: `Para los sitios que agrega`
    - Source: `For sites you add`
    - Suggest: `Para los sitios que agregás`
    - The es-AR locale addresses the user with voseo (e.g. "Te dejaremos con tu navegación privada... podés" in promote_search_widget_dialog_subtitle); "agrega" is the usted form and breaks the established form of address.
- `shortcut_erase_and_open_long_label` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Erase" is translated as "Eliminar" here while the parallel erase shortcut strings use "Borrar".
    - Current: `Eliminar y abrir %1$s`
    - Source: `Erase and open %1$s`
    - Suggest: `Borrar y abrir %1$s`
    - shortcut_erase_short_label and shortcut_erase_long_label render "Erase" as "Borrar"; using "Eliminar" for the same source term on the same surface is inconsistent.
- `shortcut_erase_and_open_short_label` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Erase" is translated as "Eliminar" here while the parallel erase shortcut strings use "Borrar".
    - Current: `Eliminar y abrir`
    - Source: `Erase & open`
    - Suggest: `Borrar y abrir`
    - shortcut_erase_short_label renders "Erase" as "Borrar"; using "Eliminar" for the same source term in the same shortcut group is inconsistent.
- `tab_crash_report_headline` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the formal "usted" imperative "Disculpe" while the locale's established address form is voseo/tuteo (used elsewhere in this batch: "Conseguí", "tus necesidades", "¡Estás protegido!").
    - Current: `Disculpe.`
    - Source: `Sorry. We’re having a problem with this tab.`
    - Suggest: `Disculpá.`
    - Register inconsistency: es-AR Focus strings address the user informally (voseo), e.g. "Conseguí acceso…", "¡Estás protegido!"; this string switches to formal usted.
- `tip_disable_tracking_protection` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Formal usted imperative "Pruebe" instead of the locale's voseo form.
    - Current: `Pruebe desactivar la Protección de rastreo`
    - Source: `Site behaving unexpectedly?  Try turning off Tracking Protection`
    - Suggest: `Probá desactivar la Protección de rastreo`
    - Register inconsistency with the voseo address used in other Focus es-AR strings ("Conseguí acceso…", "¡Estás protegido!").
- `tip_open_in_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Formal usted imperatives ("Abra", "Mantenga") instead of the locale's voseo forms.
    - Current: `Abra un enlace en una nueva pestaña Mantenga presionado cualquier enlace en una página`
    - Source: `Open a link in a new tab  Long-press any link on a page`
    - Suggest: `Abrí un enlace en una nueva pestaña Mantené presionado cualquier enlace en una página`
    - Register inconsistency with the voseo address used elsewhere in the es-AR Focus tips.
- `tip_set_default_browser` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Formal usted imperative and possessive ("Configure … su navegador") instead of the locale's voseo forms.
    - Current: `Configure %1$s como su navegador predeterminado`
    - Source: `Open every link in %1$s  Set %1$s as default browser`
    - Suggest: `Configurá %1$s como tu navegador predeterminado`
    - Register inconsistency with the voseo address used in other es-AR Focus strings ("Conseguí acceso…", "tus necesidades").

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rAR/strings.xml` — Extra spaces inserted inside the <em> markup around the placeholder.
    - Current: `{ <em> } %1$s { </em> }`
    - Source: `You’ve enabled HTTPS-Only Mode for enhanced security, and a HTTPS version of { <em> }%1$s{ </em> } is not available.`
    - Suggest: `{ <em> }%1$s{ </em> }`
    - The source has no spaces between the em tags and the placeholder; the added spaces render as stray spaces around the emphasized URL.
- `mozac_feature_pwa_site_controls_notification_text` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-es-rAR/strings.xml` — Translation adds a final period not present in the source.
    - Current: `Tocá para copiar la URL de esta aplicación.`
    - Source: `Tap to copy the URL for this app`
    - Suggest: `Tocá para copiar la URL de esta aplicación`
    - Source "Tap to copy the URL for this app" has no terminal punctuation; the notification line should match.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `debe contener “https://” o “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Quotation marks are reversed (closing mark used to open and vice versa).
    - Current: `”traducir siempre“ y ”nunca traducir“`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `“traducir siempre” y “nunca traducir”`
    - es-AR uses curly double quotes opening with “ and closing with ”; the target inverts them.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Elimina automáticamente los datos de navegación cuando seleccionás "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Salir”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — `search_add_custom_engine_search_string_example` uses straight double quotes
    - Current: `Reemplazar la consulta con "%s". Ejemplo: https://www.google.com/search?q=%s`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `Reemplazar la consulta con “%s”. Ejemplo:`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `top_sites_max_limit_confirmation_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rAR/strings.xml` — Button label ends with a period that is not in the source.
    - Current: `Listo, lo entendí.`
    - Source: `OK, Got It`
    - Suggest: `Listo, lo entendí`
    - The source "OK, Got It" is a button caption with no final punctuation; button labels should not end in a period.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Volvé a tus sitios favoritos en %1$s rápidamente. Seleccioná "Agregar a pantalla de inicio" en el menú de %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `“Agregar a pantalla de inicio”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `preference_search_add2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Missing space after the "+" sign present in the source.
    - Current: `+Agregar otro buscador`
    - Source: `+ Add another search engine`
    - Suggest: `+ Agregar otro buscador`
    - The source is "+ Add another search engine" with a space after the plus, which the developer comment highlights as emphasizing the add action.

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

### Resolved to date (0)

_Nothing resolved yet._
