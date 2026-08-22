# Android l10n QA — es-ES

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `eda9938ab8c3` |
| **Previous run** | 2026-08-21 @ `d368c9040c12` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,834 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for es-ES: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 2,834 |
| Missing strings | 77 |
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

**77 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — 67
- `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — 6
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rES/strings.xml` — 3
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 12, `straight-double` 4 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |
| inverted marks | `open-question` 111, `open-exclamation` 26 | **open-question** |
| register | `informal` 179, `formal` 11 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (133)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 62 |
| 3 | Degraded language (grammar, spelling, terminology) | 63 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_content_crashed_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — "Content crashed" is rendered as "Contenido bloqueado", which means "content blocked" rather than the content process having crashed.
    - Current: `Contenido bloqueado`
    - Source: `Content crashed`
    - Suggest: `El contenido ha fallado`
    - The source refers to a crash of the content process, not to blocked content; "bloqueado" is the established translation of "blocked" and is used for blocking messages elsewhere in the same file (e.g. "Sitio bloqueado por tu seguridad"), so the meaning is wrong and inconsistent.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — "not your device" is translated as "no del equipo" (computer) instead of device.
    - Current: `no del equipo`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `no de tu dispositivo`
    - The source refers to the user's device, not a computer; other strings in the same file use "dispositivo".
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — "there is nothing you can do to resolve it" loses the second-person reference, becoming impersonal.
    - Current: `no hay nada que se pueda hacer para resolverlo`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `no hay nada que puedas hacer para resolverlo`
    - The source addresses the user directly ("you"), and the locale convention is informal second person.
- `mozac_browser_errorpages_unknown_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — "device" is rendered as "dispositivo móvil" (mobile device), adding meaning not in the source, and "host server" is reduced to "servidor".
    - Current: `revisa la conexión wifi o de datos del dispositivo móvil`
    - Source: `{ <p> }The browser could not find the host server for the provided address.{ </p> } { <ul> } { <li> }Check the address for typing errors such as { <strong> }ww{ </strong> }.example.com instead of { <strong> }www{ </stro…`
    - Suggest: `revisa la conexión de datos o wifi de tu dispositivo`
    - The source says "your device’s data or Wi-Fi connection" with no mention of a mobile device; this component is shared and must stay generic.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — "Is the device connected to an active network?" is translated using "equipo" (computer) instead of device.
    - Current: `¿Está conectado el equipo a una red activa?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `¿Está el dispositivo conectado a una red activa?`
    - Source says "device"; "equipo" means computer and is inconsistent with "dispositivo" used elsewhere in the same file.
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — "extension developer" is rendered as "desarrollador de extensiones" instead of "desarrollador de la extensión", inconsistent with all sibling strings.
    - Current: `desarrollador de extensiones`
    - Source: `Share technical and interaction data with extension developer`
    - Suggest: `desarrollador de la extensión`
    - The source refers to the developer of this specific extension, and every other data-collection long description in this file uses "el desarrollador de la extensión".
- `mozac_feature_addons_report` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — "Report" as a button action is translated as the noun "Informe" instead of the verb "Denunciar/Informar".
    - Current: `Informe`
    - Source: `Report`
    - Suggest: `Denunciar`
    - The developer comment says this is a button to report an add-on, so it must be an action verb; "Informe" is the noun "a report".
- `mozac_lib_crash_notification_action_report` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-es-rES/strings.xml` — "Report" is a notification action button (a verb) but is translated as the noun "Informe".
    - Current: `Informe`
    - Source: `Report`
    - Suggest: `Informar`
    - Developer comment says it is a notification action/button that sends the crash report, so the imperative verb is required, not the noun.
- `alternative_app_icon_option_cool` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Cool" (stylish/modern look) is rendered as "Fresco", which conveys temperature/freshness rather than the intended sense.
    - Current: `Fresco`
    - Source: `Cool`
    - Suggest: `Molón`
    - The developer comment describes a warm orange-to-yellow gradient with a sleek, modern twist, so "Cool" means stylish, not cold/fresh; "Fresco" also clashes with the warm-color description.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" is rendered as "go to the previous page", which misdescribes the bookmarks navigation-bar back button.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The comment says it is the content description for the bookmark navigation bar back button; the source does not mention a page, and in the bookmarks screen there is no page to go back to.
- `bookmarks_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Multi-select count title is translated as a past-tense sentence instead of the label "%1$d selected".
    - Current: `Se seleccionó %1$d`
    - Source: `%1$d selected`
    - Suggest: `%1$d seleccionados`
    - The source is a title in the app bar showing how many bookmarks are currently selected; "Se seleccionó %1$d" reads as a completed action and puts the number after the verb, changing the meaning and breaking the count-label pattern.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Singular "custom tab menu sheet" is translated as plural "pestañas personalizadas" and the "sheet" element is dropped.
    - Current: `Cerrar el menú de pestañas personalizadas`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Cerrar el panel del menú de la pestaña personalizada`
    - The source refers to the bottom sheet of the menu of a single custom tab; the plural changes the meaning of which menu is being closed.
- `browser_menu_forward` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Forward" (navigate forward in browsing history) is rendered as "Siguiente" instead of "Adelante".
    - Current: `Siguiente`
    - Source: `Forward`
    - Suggest: `Adelante`
    - The developer comment says this is the content description for navigating forward in browsing history, the counterpart of "Back" = "Atrás"; the standard Spanish term is "Adelante", while "Siguiente" means "Next".
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — The translation loses the subject "you": "puede cerrar sesión en los sitios web" omits that the user is logged out.
    - Current: `puede cerrar sesión en los sitios web`
    - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
    - Suggest: `puede cerrar tu sesión en los sitios web`
    - Source says "might log you out of websites"; the current wording reads as if the user closes the session rather than being logged out.
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Never" is translated as "Manualmente" instead of "Nunca".
    - Current: `Manualmente`
    - Source: `Never`
    - Suggest: `Nunca`
    - The source option label is "Never" (never auto-close tabs); "Manualmente" belongs to the summary string close_tabs_manually_summary, not this option label.
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" is translated as "Ir a la página anterior" (go to previous page), but the control is a top bar back button in the credit card settings, not page navigation.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The developer comment specifies the top bar back button of the credit card feature; referring to a "page" misdescribes the control for screen reader users.
- `customize_toggle_jump_back_in` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Jump back in" is rendered as "Volver a esta pestaña" ("Return to this tab"), which names a specific tab rather than the home-screen section title.
    - Current: `Volver a esta pestaña`
    - Source: `Jump back in`
    - Suggest: `Retomar donde lo dejaste`
    - The source is a section header on the customize home screen listing recent tabs; "esta pestaña" refers to a single, non-existent tab and changes the meaning.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Debug locales to enable" is translated as "Lista de idiomas para activar", losing "debug" and rendering "locales" as "idiomas" (languages).
    - Current: `Lista de idiomas para activar`
    - Source: `Debug locales to enable`
    - Suggest: `Configuraciones regionales de depuración para activar`
    - The developer comment says these are debug locales that can be enabled/disabled; "idiomas" is the wrong term and "debug" is dropped.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" within the debug drawer is translated as "Ir a la página anterior" (go to previous page), which misdescribes in-drawer navigation.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The developer comment states this navigates back within the debug drawer, not to a previous web page.
- `debug_drawer_logins_add_login_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "login" (credential) is mistranslated as "conexión", inconsistent with "inicio de sesión" used in sibling strings.
    - Current: `Añade una conexión falsa para este dominio`
    - Source: `Add a fake login for this domain`
    - Suggest: `Añadir un inicio de sesión falso para este dominio`
    - The source refers to a stored login credential; other strings in the same feature use "inicio de sesión"/"Inicios de sesión". "Conexión" means a network connection.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "download partial languages" is mistranslated as "descargará parcialmente idiomas" (downloads partially), changing the meaning.
    - Current: `%1$s descargará parcialmente idiomas a la caché durante la traducción`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `%1$s descargará idiomas parciales a tu caché a medida que traduzcas`
    - The source says the app will download partial language packs into the cache; the target says it will download languages partially, shifting the adverb and altering the meaning.
- `delete_language_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "download partial languages" is mistranslated as "descargará parcialmente idiomas" (downloads partially), changing the meaning.
    - Current: `%1$s descargará parcialmente idiomas a la caché durante la traducción`
    - Source: `If you delete this language, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `%1$s descargará idiomas parciales a tu caché a medida que traduzcas`
    - The source says partial language packs will be downloaded to the cache; the target turns the adjective "partial" into an adverb modifying the download action.
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" (toolbar back button) is rendered as "go to the previous page", which is wrong for a downloads-screen toolbar button.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The source is a generic back-navigation content description for the downloads toolbar, not a web page navigation; "página anterior" states something the source does not.
- `edit_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Edit login" translated as "Editar cuenta" (edit account), which names the wrong object.
    - Current: `Editar cuenta`
    - Source: `Edit login`
    - Suggest: `Editar inicio de sesión`
    - "Login" here refers to a saved credential entry, not a user account; "cuenta" is a different concept and conflicts with the password/credential terminology used elsewhere.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" in the edit-login view is translated as "go to the previous page".
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The comment says the button exits the edit login view; there is no page involved, so "página anterior" is inaccurate.
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "suspected fingerprinters" is rendered as "rastreadores sospechosos" (suspicious trackers), losing the fingerprinter term used consistently elsewhere.
    - Current: `para evitar rastreadores sospechosos`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `para detener los detectores de huellas digitales sospechosos`
    - The source says "stop suspected fingerprinters"; the sibling string etp_suspected_fingerprinters_title correctly uses "Detectores de huellas digitales sospechosos", so this is both a mistranslation and an inconsistency.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — The app-name placeholder is read as a modifier of "pestañas", changing the meaning of the notification title.
    - Current: `%1$s pestañas cerradas: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s: pestañas cerradas: %2$d`
    - Per the comment, %1$s is the app name and %2$d the number of tabs closed; source is "%1$s tabs closed: %2$d". In Spanish "%1$s pestañas cerradas" reads as "<app> tabs closed" with the app name modifying the noun, losing the app-name-as-label sense.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" for a top-bar back button is rendered as "Ir a la página anterior" (go to the previous page), which describes page navigation rather than returning to the previous screen.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The developer comment says it is the back button of the VPN settings screen top bar, not a web page back action.
- `lens_camera_qr_no_code_found` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Definite article used where the source is indefinite: "No QR code found" becomes "No se encontró el código QR".
    - Current: `No se encontró el código QR en la imagen`
    - Source: `No QR code found in image`
    - Suggest: `No se ha encontrado ningún código QR en la imagen`
    - The source states that no QR code at all was found in the image; the Spanish implies a specific expected QR code was not found.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" is rendered as "Ir a la página anterior" (go to the previous page), but the control exits the login detail view, not a web page.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The developer comment says the button goes back and exits the login detail view; "página anterior" wrongly implies web page navigation.
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "No site exceptions" (no exceptions for any site) is rendered as "Sin excepciones para el sitio" (no exceptions for the site).
    - Current: `Sin excepciones para el sitio`
    - Source: `No site exceptions`
    - Suggest: `Sin excepciones de sitios`
    - The label is shown when the site-exceptions list is empty; the source refers to site exceptions in general, not to a particular site.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "that you use it" is mistranslated as "cómo lo usas" (how you use it).
    - Current: `cómo descubriste Firefox y cómo lo usas`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `cómo descubriste Firefox y que lo usas`
    - The source shares the fact that the user uses Firefox, not how they use it; this overstates the data shared.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "that you use it" is mistranslated as "cómo lo usas" (how you use it).
    - Current: `cómo descubriste Firefox y cómo lo usas`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `cómo descubriste Firefox y que lo usas`
    - The source shares the fact that the user uses Firefox, not how they use it; this overstates the data shared.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "that you use it" is mistranslated as "cómo lo usas" (how you use it).
    - Current: `cómo descubriste Firefox y cómo lo usas`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `cómo descubriste Firefox y que lo usas`
    - The source says the data shared is the fact that you use Firefox, not how you use it; "cómo lo usas" implies sharing usage details, a different and privacy-relevant meaning.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "that you use it" is mistranslated as "cómo lo usas" (how you use it).
    - Current: `cómo descubriste Firefox y cómo lo usas`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `cómo descubriste Firefox y que lo usas`
    - The source shares the fact that you use Firefox, not how you use it; the translation changes the scope of data sharing.
- `onboarding_marketing_redesign_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Help us grow Firefox" is translated as "Ayúdanos a mejorar Firefox" (help us improve).
    - Current: `Ayúdanos a mejorar Firefox`
    - Source: `Help us grow Firefox`
    - Suggest: `Ayúdanos a hacer crecer Firefox`
    - The source says "grow", not "improve"; it also collides with onboarding_preferences_dialog_title ("Help us make Firefox better"), which is legitimately "mejorar".
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Cross-site" is dropped, rendering "Cross-site and social media trackers" as "Rastreadores de sitios y redes sociales".
    - Current: `Rastreadores de sitios y redes sociales`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Rastreadores entre sitios y de redes sociales`
    - The option targets cross-site trackers; "de sitios" loses that meaning, and cookies_5 correctly uses "entre sitios".
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Translation weakens "will cause websites to break" to "algunos sitios no funcionarán correctamente".
    - Current: `Todas las cookies (algunos sitios no funcionarán correctamente)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `Todas las cookies (hará que los sitios web no funcionen)`
    - Source states all websites will break, not just some; the parallel string cookies_3 uses "puede causar errores en los sitios web".
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Translation adds "mis" (my data) not present in the source.
    - Current: `que no vendan ni compartan mis datos`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `que no compartan ni vendan datos`
    - Source is "Tell websites not to share & sell data" without a possessive.
- `preference_enhanced_tracking_protection_custom_info_button` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "custom tracking protection" is translated as "protección de rastreo estándar" (standard).
    - Current: `Esto es lo que está bloqueado por la protección de rastreo estándar`
    - Source: `What’s blocked by custom tracking protection`
    - Suggest: `Esto es lo que está bloqueado por la protección de rastreo personalizada`
    - The source refers to custom protection, not standard; it also conflicts with the separate standard_info_button string.
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — The product name "Firefox Suggest" is translated instead of kept as a brand name.
    - Current: `Sugerencias de Firefox`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Firefox Suggest`
    - "Firefox Suggest" is a product/feature brand kept untranslated, as done in preference_search_learn_about_fx_suggest in the same file.
- `preferences_downloads_ask_when_to_delete_files` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Ask when I delete files" is rendered as "Preguntar antes de eliminar archivos" (ask before deleting), changing the meaning.
    - Current: `Preguntar antes de eliminar archivos`
    - Source: `Ask when I delete files`
    - Suggest: `Preguntar cuando elimine archivos`
    - The source asks to be prompted when the user deletes files, not before deletion; "antes de" adds a meaning not in the source.
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "enabled above" is rendered as "activado en la parte superior" (enabled at the top of the screen) rather than referring to the setting above.
    - Current: `Google está activado en la parte superior`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Google está activado más arriba`
    - The source refers to the Google toggle located above this caption; "en la parte superior" misstates it as a location at the top.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "that you use it" is mistranslated as "cómo lo utilizas" (how you use it), which the developer comment explicitly warns against.
    - Current: `Comparte cómo descubriste Firefox y cómo lo utilizas con los socios tecnológicos de marketing de Mozilla.`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `Comparte con los socios tecnológicos de marketing de Mozilla cómo descubriste Firefox y que lo utilizas.`
    - The comment states "That you use it" means sharing that the user continues to use Firefox, not what they use it for; "cómo lo utilizas" reverses that meaning.
- `preferences_show_trending_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Show trending suggestions" rendered as "the most popular suggestions", changing the meaning.
    - Current: `Mostrar las sugerencias más populares`
    - Source: `Show trending suggestions`
    - Suggest: `Mostrar sugerencias de tendencias`
    - The source refers to trending searches, not to a superlative ranking of most popular suggestions.
- `qr_code_display_share_nearby` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Share link nearby" is rendered as "Compartir enlace cercano", which says the link is nearby instead of sharing it with nearby people.
    - Current: `Compartir enlace cercano`
    - Source: `Share link nearby`
    - Suggest: `Compartir enlace con dispositivos cercanos`
    - In the source "nearby" modifies the sharing action (share with people/devices nearby), not the link; the Spanish makes "cercano" an adjective of "enlace".
- `recent_tabs_header` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Header text mistranslated as referring to a specific tab.
    - Current: `Volver a esta pestaña`
    - Source: `Jump back in`
    - Suggest: `Retomar donde lo dejaste`
    - "Jump back in" is a generic home-screen section header, not a reference to "this tab".
- `recent_tabs_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Content description misparses the source: it says "show the button of all recent tabs" instead of naming the button.
    - Current: `Mostrar el botón de todas las pestañas recientes`
    - Source: `Show all recent tabs button`
    - Suggest: `Botón de mostrar todas las pestañas recientes`
    - Source "Show all recent tabs button" names the control (a button that shows all recent tabs); the translation turns "button" into the object being shown.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Search settings" (verb + object) is translated as "Ajustes de búsqueda" (search settings as a noun phrase), reversing the meaning.
    - Current: `Ajustes de búsqueda`
    - Source: `Search settings`
    - Suggest: `Buscar en los ajustes`
    - The developer comment states "Search" is a verb here; the title is for searching within settings, not for settings about search.
- `sports_widget_error_load_failed` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Translation adds "la página" (the page), which is not in the source and refers to refreshing the widget data, not a page.
    - Current: `Intenta actualizar la página en unos minutos.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Intenta actualizar en unos minutos.`
    - Source is "Try refreshing in a few minutes." with no mention of a page; the sibling string sports_widget_error_load_failed_description correctly renders it as "Intenta actualizar en unos minutos."
- `sports_widget_runner_up_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Runners-up" (second place) is rendered as "Finalistas", which in Spanish covers both teams reaching the final, not the second-place team.
    - Current: `Finalistas`
    - Source: `Runners-up`
    - Suggest: `Subcampeones`
    - The developer comment explicitly states runners-up means second place; "Finalistas" designates all finalists, including the champion, so the meaning is wrong.
- `sports_widget_team_followed_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Translation adds "esta página", which is not in the source and is inaccurate for a home-screen widget.
    - Current: `Consulta de nuevo esta página para obtener información`
    - Source: `Check back for match info as the tournament approaches.`
    - Suggest: `Vuelve a consultarlo para obtener información`
    - The source "Check back for match info" does not mention a page; the widget is on the homepage, not a page.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Navigate back" is rendered as "Ir a la página anterior", which refers to a previous web page rather than navigating back from the Stories screen.
    - Current: `Ir a la página anterior`
    - Source: `Navigate back`
    - Suggest: `Volver atrás`
    - The developer comment says this is the "Navigate back" button on the top app bar of the Stories screen, not a web page back action; the translation adds "página" which is not in the source and misdescribes the control for screen-reader users.
- `tab_group_onboarding_item_dismiss_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "tab group onboarding" is mistranslated as "incorporación al grupo de pestañas", implying joining a group rather than the onboarding card about tab groups.
    - Current: `Descartar la incorporación al grupo de pestañas`
    - Source: `Dismiss tab group onboarding`
    - Suggest: `Descartar la introducción a los grupos de pestañas`
    - The source refers to dismissing the onboarding (introductory) card for tab groups; "incorporación al grupo de pestañas" reads as being added to a tab group, which is a different meaning.
- `add_custom_autocomplete_label` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Add link to autocomplete" (add the link to the autocomplete list) is mistranslated as adding the link in order to autocomplete.
    - Current: `Añadir el enlace para completar automáticamente`
    - Source: `Add link to autocomplete`
    - Suggest: `Añadir el enlace a autocompletado`
    - Per the developer comment, the button adds the current URL to the custom autocomplete list; the Spanish reads as "add the link in order to complete automatically".
- `cfr_cookie_banner` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — Redundant added wording: "en los ajustes en %2$s" duplicates the linked word "ajustes".
    - Current: `Administra las preferencias de avisos de cookies en los ajustes en %2$s.`
    - Source: `%1$s tries to reject cookie requests to dismiss annoying cookie banners.  Manage cookie banner preferences in %2$s.`
    - Suggest: `Administra las preferencias de avisos de cookies en %2$s.`
    - %2$s is already the link text "ajustes"; the source is "Manage cookie banner preferences in %2$s." so "en los ajustes" is an unwarranted duplication.
- `content_description_clear_input` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Clear input" (clear the text in the URL bar) is rendered as "Limpiar registro" (clear log/record).
    - Current: `Limpiar registro`
    - Source: `Clear input`
    - Suggest: `Borrar el texto introducido`
    - The developer comment says it clears text in the URL bar; "registro" means log/record, which is a different thing.
- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — The translation drops the word "disabled", reversing the meaning of the warning.
    - Current: `El acceso directo se abrirá con la protección mejorada contra el rastreo`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `El acceso directo se abrirá con la protección mejorada contra el rastreo desactivada`
    - Source says the shortcut will open with Enhanced Tracking Protection *disabled*; the Spanish says it opens with the protection (implicitly enabled), reversing the warning.
- `feedback_erase` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "browsing history" was translated as "historial de búsqueda" (search history).
    - Current: `Se ha eliminado tu historial de búsqueda.`
    - Source: `Your browsing history has been erased.`
    - Suggest: `Se ha eliminado tu historial de navegación.`
    - The source says "Your browsing history has been erased.", not search history; other strings in the same file use "historial de navegación".
- `preference_autocomplete_custom_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "custom autocomplete URLs" is mistranslated as "autocompletado personalizado de URLs" (custom autocompletion of URLs).
    - Current: `Agregar y gestionar autocompletado personalizado de URLs.`
    - Source: `Add and manage custom autocomplete URLs.`
    - Suggest: `Agregar y gestionar URLs de autocompletado personalizadas.`
    - The source refers to custom autocomplete URLs (user-defined URL entries), not to a custom autocomplete feature.
- _…and 4 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Duplicated/incorrect preposition sequence "para como" makes the sentence ungrammatical.
    - Current: `no ha podido ser verificado para como seguro`
    - Source: `%1$s could not be verified as secure and has been disabled.`
    - Suggest: `no ha podido verificarse como seguro`
    - The source is "could not be verified as secure"; "verificado para como seguro" contains a stray "para" and is ungrammatical.
- `mozac_summarize_shake_consent_on_device_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-es-rES/strings.xml` — Verb agreement error: the subject is the app name (%s), so the verb must be third person, not second person "puedes".
    - Current: `%s puedes resumir las páginas cuando sacudes tu dispositivo`
    - Source: `After a quick one-time download, %s can summarize pages when you shake your device.`
    - Suggest: `%s puede resumir las páginas cuando sacudes tu dispositivo`
    - Source: "%s can summarize pages when you shake your device" — %s is the app name and is the subject of "can summarize", so Spanish requires "puede".
- `ai_controls_voice_search_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Awkward/incorrect passive with agent; Google Speech Services brand name order is also altered.
    - Current: `El audio se convierte a texto por los servicios de Google Speech.`
    - Source: `Audio is converted to text by Google Speech Services.`
    - Suggest: `Google Speech Services convierte el audio en texto.`
    - Spanish does not use "se convierte ... por" (reflexive passive with an explicit agent); also the product name "Google Speech Services" should not be reordered into "los servicios de Google Speech".
- `download_completed_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Download completed" rendered as "Descarga completa" (complete/full) instead of the past participle "completada".
    - Current: `Descarga completa`
    - Source: `Download completed`
    - Suggest: `Descarga completada`
    - The source states the download has finished; "completa" means "full/entire" while "completada" is the correct past participle for a finished download.
- `download_languages_error_warning_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Spelling error: "pidodo" instead of "podido".
    - Current: `No se ha pidodo descargar`
    - Source: `Couldn’t download { <b> }%1$s{ </b> }. Please try again.`
    - Suggest: `No se ha podido descargar`
    - The source says "Couldn’t download"; the Spanish verb form is misspelled ("pidodo" is not a word), unlike the parallel string download_languages_delete_error_warning_text which correctly uses "No se ha podido borrar".
- `download_navigate_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Content description uses a third-person verb form ("Abre") instead of a noun phrase describing the control.
    - Current: `Abre los ajustes de descargas`
    - Source: `Navigate to Downloads Settings`
    - Suggest: `Ir a los ajustes de descargas`
    - Source "Navigate to Downloads Settings" is a label for the control; "Abre..." reads as an imperative/third-person statement rather than the action label.
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Button label uses an imperative addressed at the user instead of an infinitive action label.
    - Current: `Intenta reiniciar las extensiones`
    - Source: `Try restarting extensions`
    - Suggest: `Intentar reiniciar las extensiones`
    - "Try restarting extensions" is a button action; Spanish UI buttons use the infinitive, and the surrounding buttons ("Continuar con las extensiones desactivadas") do so as well.
- `logins_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Imperative form missing: "Unlock your device" is a dialog title/instruction and should be "Desbloquea tu dispositivo" to match the informal register used in the sibling string.
    - Current: `Desbloquear tu dispositivo`
    - Source: `Unlock your device`
    - Suggest: `Desbloquea tu dispositivo`
    - The parallel string logins_biometric_prompt_message_2 uses the imperative "Desbloquea…"; "Desbloquear tu dispositivo" mixes infinitive with a possessive addressed to the user.
- `pair_instructions_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Misspelled verb form "Escaneae" instead of "Escanea".
    - Current: `Escaneae el código QR`
    - Source: `Scan the QR code shown at { <b> }firefox.com/pair{ </b> }`
    - Suggest: `Escanea el código QR`
    - The informal imperative of "escanear" is "escanea"; "Escaneae" is not a valid word.
- `preferences_screenshots_in_private_mode_disclaimer` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Incorrect use of plural "hayan" for existential haber, which is invariable.
    - Current: `cuando hayan varias aplicaciones abiertas`
    - Source: `If allowed, private tabs will also be visible when multiple apps are open`
    - Suggest: `cuando haya varias aplicaciones abiertas`
    - Existential "haber" is impersonal and always singular: "cuando haya varias aplicaciones abiertas".
- `recent_tabs_synced_device_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Number agreement error: plural noun with singular adjective.
    - Current: `Dispositivos sincronizado`
    - Source: `Synced device`
    - Suggest: `Dispositivo sincronizado`
    - The source "Synced device" is singular; the translation mixes a plural noun with a singular adjective.
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Agreement error: "abiertas" should agree with "grupo(s)", not "pestañas".
    - Current: `%1$d grupo de pestañas abiertas`
    - Source: `{$quantity ->} [one] %1$d tab group open. Tap to switch tabs. [other] %1$d tab groups open. Tap to switch tabs.`
    - Suggest: `%1$d grupo de pestañas abierto`
    - The source says "%1$d tab group open" — it is the group that is open, so the adjective must agree with the masculine noun "grupo" (and "grupos ... abiertos" in the other variant).
- `webcompat_reporter_reason_account2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Inconsistent impersonal/personal construction: "No se puede iniciar sesión ni registrarme" mixes impersonal "se puede" with first-person "registrarme".
    - Current: `No se puede iniciar sesión ni registrarme`
    - Source: `Can’t sign in or register`
    - Suggest: `No se puede iniciar sesión ni registrarse`
    - The source "Can’t sign in or register" uses one consistent subject; the Spanish mixes an impersonal passive with a first-person reflexive pronoun, which is ungrammatical.
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — Misspelling of "sitio" as "sito".
    - Current: `este sito web`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `este sitio web`
    - "sito" is a typo for "sitio".
- `enable_search_suggestions_yes` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Si" is missing the accent; the affirmative adverb is "Sí".
    - Current: `Si`
    - Source: `Yes`
    - Suggest: `Sí`
    - Source is "Yes"; without the accent "si" means "if" in Spanish.
- `preference_privacy_should_block_cookies_third_party_only_option` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "sólo" is written with an obsolete accent, inconsistent with "solo" used in the neighbouring option string.
    - Current: `Bloquear sólo cookies de terceros`
    - Source: `Block 3rd-party cookies only`
    - Suggest: `Bloquear solo cookies de terceros`
    - RAE no longer accents the adverb "solo", and the sibling string preference_privacy_should_block_cookies_third_party_tracker_cookies_option uses "solo" unaccented, creating an inconsistency.
- `preference_search_add3` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — Action label uses an imperative verb form instead of the infinitive used in the parallel string preference_search_add2.
    - Current: `Añade otro motor de búsqueda`
    - Source: `Add another search engine`
    - Suggest: `Añadir otro motor de búsqueda`
    - "Add another search engine" is an action label; es-ES uses the infinitive for actions, as in preference_search_add2 ("+ Añadir otro motor de búsqueda").

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_all_urls_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Uses formal "sus" while the sibling string and locale convention use informal "tus".
    - Current: `Acceder a sus datos de todos los sitios web.`
    - Source: `Access your data for all websites.`
    - Suggest: `Acceder a tus datos de todos los sitios web.`
    - es-ES uses the informal register, and the parallel string mozac_feature_addons_permissions_all_urls_description translates the same source as "Acceder a tus datos de todos los sitios web".
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Formal address "identificarle" conflicts with the locale's informal register convention.
    - Current: `El desarrollador dice que esta extensión quiere recopilar: %1$s`
    - Source: `The developer says the extension wants to collect: %1$s`
    - Suggest: `El desarrollador dice que la extensión quiere recopilar: %1$s`
    - Source says "the extension"; the target adds the demonstrative "esta", changing the reference.
- `mozac_feature_addons_permissions_data_collection_personallyIdentifyingInfo_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Uses formal "identificarle" although the locale convention is the informal register.
    - Current: `información que puede identificarle personalmente`
    - Source: `Share personally identifying information with extension developer`
    - Suggest: `información que puede identificarte personalmente`
    - es-ES convention is informal address (tú); "identificarle" is the formal/usted form.
- `mozac_feature_addons_permissions_data_collection_personallyIdentifyingInfo_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Uses formal "identificarle" although the locale convention is the informal register.
    - Current: `información que puede identificarle personalmente`
    - Source: `personally identifying information`
    - Suggest: `información que puede identificarte personalmente`
    - es-ES convention is informal address (tú); "identificarle" is the formal/usted form.
- `mozac_feature_addons_permissions_dialog_heading_required_data_collection` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — "Data collection" is rendered as "Recolección de datos" while the parallel heading and other strings use "recopilación de datos".
    - Current: `Recolección de datos requerida:`
    - Source: `Required data collection:`
    - Suggest: `Recopilación de datos requerida:`
    - Inconsistent terminology on the same dialog: mozac_feature_addons_permissions_dialog_heading_optional_data_collection uses "Nueva recopilación de datos:" and the none-required string uses "recopilación de datos".
- `mozac_feature_addons_permissions_geolocation_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Formal "su" used instead of the informal "tu" that the locale and the sibling string use.
    - Current: `Acceder a su ubicación.`
    - Source: `Access your location.`
    - Suggest: `Acceder a tu ubicación.`
    - es-ES uses the informal register, and the non-update variant (mozac_feature_addons_permissions_geolocation_description) reads "Acceder a tu ubicación".
- `mozac_feature_addons_updater_notification_short_intro` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — Formal address "su" used where the locale convention is informal.
    - Current: `conservar su versión y configuración actuales`
    - Source: `Cancel to keep your current version and settings.`
    - Suggest: `conservar tu versión y configuración actuales`
    - es-ES convention is informal (tú); the source "your current version and settings" should use "tu".
- `mozac_feature_addons_user_rating_count_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-es-rES/strings.xml` — "Reviews" for add-on ratings is rendered as "Revisiones" instead of the established "Reseñas".
    - Current: `Revisiones: %1$s`
    - Source: `Reviews: %1$s`
    - Suggest: `Reseñas: %1$s`
    - In the add-ons context "Reviews" means user reviews/ratings; "Revisiones" means inspections/revisions and is the wrong term.
- `mozac_feature_applinks_normal_confirm_dialog_message` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-es-rES/strings.xml` — Formal address used where the locale convention is informal (tú).
    - Current: `¿Quiere dejar %s para ver este contenido?`
    - Source: `Would you like to leave %s to view this content?`
    - Suggest: `¿Quieres salir de %s para ver este contenido?`
    - es-ES convention is the informal register (as in the neighbouring autofill string "¿Quieres continuar..."); "Quiere" is formal usted.
- `mozac_feature_downloads_button_pause` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-es-rES/strings.xml` — Button label uses the noun "Pausa" instead of the verb form used for the other download action buttons.
    - Current: `Pausa`
    - Source: `Pause`
    - Suggest: `Pausar`
    - The developer comment says it is a button that pauses the download; sibling buttons use infinitives (Cancelar, Abrir, Continuar, Reintentar), so the noun is inconsistent.
- `mozac_feature_downloads_cancel_active_private_downloads_warning_content_body` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-es-rES/strings.xml` — Mixes formal "cierra" (usted) with informal "estás/quieres" in the same string; es-ES convention is informal throughout.
    - Current: `Si cierra todas las pestañas privadas ahora`
    - Source: `If you close all Private tabs now, %1$s download will be canceled. Are you sure you want to leave Private Browsing?`
    - Suggest: `Si cierras todas las pestañas privadas ahora`
    - The locale's established register is informal (tú), and the second sentence already uses "¿Estás seguro de que quieres...?"; the first clause uses the formal third person.
- `mozac_feature_prompt_folder_upload_confirm_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Formal address ("Asegúrese") used where the locale convention is informal (tú).
    - Current: `Asegúrese de que confía en este sitio antes de subir desde “%1$s”.`
    - Source: `Make sure you trust this site before you upload from “%1$s”.`
    - Suggest: `Asegúrate de que confías en este sitio antes de subir desde “%1$s”.`
    - es-ES convention is the informal register (as in "¿Estás seguro?", "Introduce una contraseña" in the same file); this string uses usted.
- `mozac_feature_prompts_apr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation rendered as the full month name, inconsistent with other months (e.g. "Dic").
    - Current: `Abril`
    - Source: `Apr`
    - Suggest: `Abr`
    - The developer comment specifies the short description of April for a month chooser; other months in the same file use abbreviations (Dec → Dic).
- `mozac_feature_prompts_aug` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation rendered as the full month name, inconsistent with other months (e.g. "Dic").
    - Current: `Agosto`
    - Source: `Aug`
    - Suggest: `Ago`
    - The developer comment specifies the short description of August for a month chooser; other months in the same file use abbreviations (Dec → Dic).
- `mozac_feature_prompts_content_description_input_label` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — "ingresar" is Latin American usage; es-ES uses "introducir".
    - Current: `Etiqueta para ingresar un campo de entrada de texto`
    - Source: `Label for entering a text input field`
    - Suggest: `Etiqueta para introducir un campo de entrada de texto`
    - Elsewhere in the same file "Enter a password" is translated as "Introduce una contraseña"; "ingresar" is not the es-ES term.
- `mozac_feature_prompts_feb` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation "Feb" is rendered as the full month name.
    - Current: `Febrero`
    - Source: `Feb`
    - Suggest: `Feb`
    - The developer comment specifies a short description used in the month chooser dialog; the target uses the full month name instead of an abbreviation (other months in this batch, e.g. Sep → Sept, are abbreviated).
- `mozac_feature_prompts_identity_credentials_choose_account_for_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — "Sign in" is translated as "Conéctate" instead of the established "Iniciar sesión".
    - Current: `Conéctate con una cuenta de %1$s`
    - Source: `Sign in with a %1$s account`
    - Suggest: `Iniciar sesión con una cuenta de %1$s`
    - Sibling strings in the same dialog family use "inicio de sesión"/"Iniciar sesión" for login/sign in; "Conéctate" is inconsistent terminology on the same surface.
- `mozac_feature_prompts_jan` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation "Jan" is rendered as the full month name.
    - Current: `Enero`
    - Source: `Jan`
    - Suggest: `Ene`
    - The developer comment specifies a short description for the month chooser dialog; the target gives the full month name rather than an abbreviation.
- `mozac_feature_prompts_jul` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation "Jul" is rendered as the full month name.
    - Current: `Julio`
    - Source: `Jul`
    - Suggest: `Jul`
    - The developer comment specifies a short description for the month chooser dialog; the target gives the full month name rather than an abbreviation.
- `mozac_feature_prompts_jun` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-es-rES/strings.xml` — Short month abbreviation "Jun" is rendered as the full month name.
    - Current: `Junio`
    - Source: `Jun`
    - Suggest: `Jun`
    - The developer comment specifies a short description for the month chooser dialog; the target gives the full month name rather than an abbreviation.
- `mozac_feature_sitepermissions_local_network_access_title` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-es-rES/strings.xml` — Formal address "su red local" breaks the locale's informal register used in the surrounding permission dialogs.
    - Current: `conectados a su red local?`
    - Source: `Allow %1$s to access apps and services on devices connected to your local network?`
    - Suggest: `conectados a tu red local?`
    - es-ES convention is informal address; sibling strings use "tu ubicación", "tu micrófono".
- `add_login_save_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "login" rendered as "cuenta" instead of the password terminology used elsewhere in this screen.
    - Current: `Guardar nueva cuenta`
    - Source: `Save new login`
    - Suggest: `Guardar nueva contraseña`
    - The add login screen uses "contraseña" for login (see add_login_2 "Añadir contraseña"); "cuenta" is inconsistent and means "account".
- `add_tab` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Add" translated as "Agregar" while the parallel string add_private_tab and other add strings use "Añadir".
    - Current: `Agregar pestaña`
    - Source: `Add tab`
    - Suggest: `Añadir pestaña`
    - Inconsistent terminology on the same surface: add_private_tab uses "Añadir pestaña privada"; es-ES convention favours "Añadir".
- `bookmark_add_folder` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Agregar" is inconsistent with the es-ES term "Añadir" used in the sibling bookmark strings.
    - Current: `Agregar carpeta`
    - Source: `Add folder`
    - Suggest: `Añadir carpeta`
    - Other strings on the same surface translate "Add" as "Añadir" (bookmark_add_new_folder_button_content_description, bookmark_error_add_folder); es-ES prefers "Añadir".
- `bookmark_delete_folders_confirmation_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — English word "items" left untranslated instead of "elementos".
    - Current: `los items seleccionados`
    - Source: `Are you sure you want to delete the selected items?`
    - Suggest: `los elementos seleccionados`
    - The source "items" should be rendered as "elementos" in es-ES; "items" is an unadapted anglicism.
- `browser_menu_add_to_homescreen` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Add to Home screen" uses "Agregar" and capitalised "Inicio", inconsistent with the neighbouring string that uses "Añadir ... pantalla de inicio".
    - Current: `Agregar a la pantalla de Inicio`
    - Source: `Add to Home screen`
    - Suggest: `Añadir a la pantalla de inicio`
    - browser_menu_add_app_to_homescreen on the same menu surface renders "Add ... to Home screen" as "Añadir app a la pantalla de inicio"; the two adjacent menu items should use the same verb and casing, and "Añadir" is the es-ES form.
- `debug_drawer_override_region` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "home region" rendered as "región de inicio" here but "región de origen" in the related labels.
    - Current: `Reemplazar la región de inicio y la actual`
    - Source: `Override home and current region`
    - Suggest: `Reemplazar la región de origen y la actual`
    - Inconsistent with debug_drawer_home_region_label and debug_drawer_override_home_region_label, which translate "home region" as "región de origen".
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "home region" rendered as "región de inicio" instead of the "región de origen" used elsewhere.
    - Current: `Temporalmente reemplaza los valores de la región de inicio y actual para la prueba.`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `Reemplaza temporalmente los valores de la región de origen y actual para pruebas.`
    - Inconsistent terminology with debug_drawer_home_region_label ("Región de origen"); also "for testing" is generic, not "para la prueba".
- `download_pause_action` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Pause" (action button) translated as the noun "Pausa" while the parallel actions use verbs.
    - Current: `Pausa`
    - Source: `Pause`
    - Suggest: `Pausar`
    - Source is a verb action label, and the sibling strings use verbs ("Continuar", "Reintentar"); "Pausa" is inconsistent as an action label.
- `onboarding_preferences_dialog_usage_data_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Formal address "usa" used instead of the locale's informal register.
    - Current: `cómo usa Firefox`
    - Source: `Data about your device, hardware configuration, and how you use Firefox helps improve features, performance, and stability for everyone.`
    - Suggest: `cómo usas Firefox`
    - es-ES convention is informal (tú); the surrounding onboarding strings use "descubriste", "aceptas", "quieres".
- `preference_enhanced_tracking_protection_allow_list_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Formal address ("desactiva" with usted) breaks the informal register used elsewhere in the batch.
    - Current: `Si la desactiva, es posible que algunos sitios no funcionen`
    - Source: `This setting helps fix the most common site problems. If you turn it off, some sites may not work, and %1$s won’t be able to help troubleshoot those issues.`
    - Suggest: `Si la desactivas, es posible que algunos sitios no funcionen`
    - es-ES convention is informal (tú); the sibling dialog title uses "¿Estás seguro...?".
- `preferences_delete_browsing_data` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Delete browsing data" is translated inconsistently as "Eliminar datos del navegador" here but "Eliminar datos de navegación" in the button and on-quit strings.
    - Current: `Eliminar datos del navegador`
    - Source: `Delete browsing data`
    - Suggest: `Eliminar datos de navegación`
    - The same source phrase on the same settings surface uses two different renderings; "datos de navegación" is the correct one for "browsing data".
- `preferences_delete_browsing_data_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "Browsing data deleted" uses "datos del navegador", inconsistent with "datos de navegación" used elsewhere for browsing data.
    - Current: `Se han eliminado los datos del navegador`
    - Source: `Browsing data deleted`
    - Suggest: `Se han eliminado los datos de navegación`
    - "Browsing data" is rendered "datos de navegación" in the related Delete browsing data strings; "datos del navegador" means browser data.
- `preferences_pbm_lock_screen_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Preference title rendered as an imperative sentence instead of an infinitive label.
    - Current: `Utiliza el bloqueo de pantalla para ocultar pestañas en la navegación privada`
    - Source: `Use screen lock to hide tabs in private browsing`
    - Suggest: `Usar el bloqueo de pantalla para ocultar pestañas en la navegación privada`
    - The source "Use screen lock to hide tabs in private browsing" is a settings toggle title; es-ES convention renders such labels with the infinitive, as in the sibling strings ("Guardar contraseñas", "Mostrar búsquedas recientes").
- `preferences_toolbar_select_shortcut` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Formal address "Seleccione" breaks the locale's informal register.
    - Current: `Seleccione un acceso directo`
    - Source: `Select a shortcut`
    - Suggest: `Selecciona un acceso directo`
    - es-ES uses the informal (tú) form throughout; other imperatives in this batch use "Elige", "Obtén", "Inicia sesión".
- `saved_logins_add_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — "login" rendered as "cuenta", inconsistent with "inicio de sesión" used elsewhere in the same surface.
    - Current: `Añadir nueva cuenta`
    - Source: `Add new login`
    - Suggest: `Añadir nuevo inicio de sesión`
    - Other login strings in this batch translate "login" as "inicio de sesión" (see saved_login_duplicate); "cuenta" means account.
- `sports_widget_get_custom_wallpaper` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Menu item label rendered as an imperative sentence instead of a noun/infinitive label like the other menu items.
    - Current: `Obtén un fondo de pantalla personalizado`
    - Source: `Get custom wallpaper`
    - Suggest: `Obtener un fondo de pantalla personalizado`
    - It is a menu item parallel to "Cambiar equipo" (sports_widget_change_team) and "Seguir a otro equipo"; menu labels use the infinitive in es-ES, not the imperative.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Uses the formal "Tiene" instead of the locale's established informal address.
    - Current: `Tiene un informe de fallos sin enviar`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `Tienes un informe de fallos sin enviar`
    - es-ES convention is informal (tú); other strings in this batch use informal forms (e.g. "utiliza", "Habla ahora").
- `unsubmitted_crashes_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Uses the formal "Tiene" instead of the locale's established informal address.
    - Current: `Tiene informes de fallos sin enviar`
    - Source: `You have unsent crash reports (%1$d) related to crashes being investigated. Sending them will help us improve %2$s. Closing this notification will ignore these reports.`
    - Suggest: `Tienes informes de fallos sin enviar`
    - es-ES convention is informal (tú); the rest of the UI addresses the user informally.
- `cookie_banner_exception_panel_title_state_off_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Cookie Banner Reduction" rendered as "reducción de aviso de cookies" in singular, inconsistent with "reducción de avisos de cookies" used elsewhere.
    - Current: `reducción de aviso de cookies`
    - Source: `Turn off Cookie Banner Reduction for %1$s?`
    - Suggest: `reducción de avisos de cookies`
    - The same feature name is translated as "Reducción de avisos de cookies" in cookie_banner_exception_item_title and other strings on the same surface.
- `cookie_banner_exception_panel_title_state_on_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Cookie Banner Reduction" rendered as "reducción de aviso de cookies" in singular, inconsistent with "reducción de avisos de cookies" used elsewhere.
    - Current: `reducción de aviso de cookies`
    - Source: `Turn on Cookie Banner Reduction for %1$s?`
    - Suggest: `reducción de avisos de cookies`
    - The same feature name is translated as "Reducción de avisos de cookies" in the other cookie banner strings in this file.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — `firstrun_shortcut_text` quotes “Agregar a la pantalla de inicio” but the string it names, `menu_add_to_home_screen`, reads “Añadir a pantalla de inicio”
    - Current: `Vuelve a visitar tus sitios favoritos en %1$s de forma instantánea. En el menú %1$s, selecciona "Agregar a la pantalla de inicio".`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Añadir a pantalla de inicio`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — Formal address used where the locale convention is informal (tú).
    - Current: `Ha desactivado el bloqueo de contenido para estos sitios.`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `Has desactivado el bloqueo de contenido para estos sitios.`
    - es-ES convention is the informal register; other strings in this batch use "Elige", "tu navegador".
- `preference_mozilla_telemetry_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Learn more" translated inconsistently with the same source string elsewhere in the file.
    - Current: `Descubrir más`
    - Source: `Learn more`
    - Suggest: `Saber más`
    - preference_daily_usage_ping_learn_more renders the identical source "Learn more" as "Saber más" on the same settings surface.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Está conectado el equipo a una red activa?{ </li> } { <li> }Pulsa "Volver a intentarlo"…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Pulsa “Volver a intentarlo”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rES/strings.xml` — Stray space before the closing label tag after the first sentence.
    - Current: `no deberías continuar. { </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `no deberías continuar.{ </label> }`
    - The source has no space before { </label> }; the extra space is a typography deviation introduced by the translation.
- `mozac_feature_pwa_site_controls_notification_text` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-es-rES/strings.xml` — Trailing period added that is not in the source notification text.
    - Current: `Toca para copiar la URL de esta aplicación.`
    - Source: `Tap to copy the URL for this app`
    - Suggest: `Toca para copiar la URL de esta aplicación`
    - The en-US string "Tap to copy the URL for this app" has no final period; the translation adds one.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” o “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Curly quotation marks are reversed (closing mark used as opening and vice versa).
    - Current: `”traducir siempre“ y ”no traducir nunca“`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `“traducir siempre” y “no traducir nunca”`
    - es-ES convention is curly double quotes correctly paired; the target opens with ” and closes with “, inverting the marks.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Eliminar automáticamente los datos de navegación cuando selecciones "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Salir”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `preferences_android_autofill` — `mozilla-mobile/fenix/app/src/main/res/values-es-rES/strings.xml` — Trailing period added to a preference title that has none in the source.
    - Current: `Autocompletar en otras aplicaciones.`
    - Source: `Autofill in other apps`
    - Suggest: `Autocompletar en otras aplicaciones`
    - The source "Autofill in other apps" is a preference title with no final period; the extra period is inconsistent with other preference titles.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Vuelve a visitar tus sitios favoritos en %1$s de forma instantánea. En el menú %1$s, selecciona "Agregar a la pantalla de inicio".`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `selecciona “Añadir a pantalla de inicio”`
    - The locale's quote convention is `curly-double` (12 occurrences).

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
