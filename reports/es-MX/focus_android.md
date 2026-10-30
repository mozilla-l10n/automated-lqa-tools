# Focus for Android l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 249 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for es-MX: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Files | 1 |
| Strings | 249 |
| Missing strings | 1 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**1 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 15 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| inverted marks | `open-question` 105, `open-exclamation` 29 | **open-question** |
| register | `informal` 195, `formal` 12 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (15)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 9 |
| 3 | Degraded language (grammar, spelling, terminology) | 6 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `cfr_for_toolbar_delete_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "start fresh on a new tab" is rendered as "inicia en una nueva pestaña", losing the "start fresh" meaning.
    - Current: `e inicia en una nueva pestaña`
    - Source: `Tap here to trash it all — history, cookies, everything — and start fresh on a new tab.`
    - Suggest: `y empieza de cero en una nueva pestaña`
    - The source conveys starting over clean on a new tab; the target merely says "start on a new tab".
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — The phrase "any time" is dropped from the translation.
    - Current: `Presiona el escudo para ver lo que estamos bloqueando.`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `Presiona el escudo en cualquier momento para ver lo que estamos bloqueando.`
    - The source says "Tap the shield any time"; the target omits "any time".
- `content_description_back` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Navigate back" is translated as "Regresar a la navegación" (return to browsing) instead of navigating back in history.
    - Current: `Regresar a la navegación`
    - Source: `Navigate back`
    - Suggest: `Retroceder`
    - The source and comment mean navigating back through browsing history; the target says "return to browsing", a different meaning, and it is inconsistent with content_description_forward ("Ir hacia delante").
- `preference_mozilla_telemetry2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "usage data" is rendered as "datos de consumo" (consumption data) instead of usage/utilization data.
    - Current: `Enviar datos de consumo`
    - Source: `Send usage data`
    - Suggest: `Enviar datos de uso`
    - "Usage data" refers to telemetry about how the app is used; "datos de consumo" suggests data consumption (bandwidth), a different meaning.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "switching apps" mistranslated as "intercambiar aplicaciones" (exchanging apps).
    - Current: `Ocultar páginas al intercambiar aplicaciones`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `Ocultar páginas al cambiar de aplicación`
    - The source means switching between apps, not exchanging/swapping apps.
- `preference_search_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Set default" is translated as "Establecer como predeterminado" (set as default), reversing the sense of setting the default engine.
    - Current: `Establecer como predeterminado, autocompletar`
    - Source: `Set default, autocomplete`
    - Suggest: `Establecer predeterminado, autocompletar`
    - The source describes settings available in the search screen: setting the default search engine, not marking something as default.
- `preference_state_off` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Off" (a state shown below a switch) is translated as the verb "Desactivar" ("turn off") instead of the state "Desactivado".
    - Current: `Desactivar`
    - Source: `Off`
    - Suggest: `Desactivado`
    - The developer comment says this is text shown below a disabled switch, i.e. a state label, not an action.
- `preference_state_on` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "On" (a state shown below a switch) is translated as the verb "Activar" ("turn on") instead of the state "Activado".
    - Current: `Activar`
    - Source: `On`
    - Suggest: `Activado`
    - The developer comment says this is text shown below an enabled switch, i.e. a state label, not an action.
- `search_add_error_empty_name` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "search engine" is rendered as "motor de navegación" (navigation engine) instead of "motor de búsqueda".
    - Current: `Introducir el nombre del motor de navegación`
    - Source: `Enter search engine name`
    - Suggest: `Introducir el nombre del motor de búsqueda`
    - The source says "search engine name"; the related string search_add_manually_name_hint correctly uses "motor de búsqueda".
- `search_add_manually_string` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — "Search string to use" is mistranslated as an imperative "Buscar cadena para usar" (search for a string).
    - Current: `Buscar cadena para usar`
    - Source: `Search string to use`
    - Suggest: `Cadena de búsqueda a usar`
    - The source is a noun phrase label for the search string field, not an instruction to search; other strings render "search string" as "cadena de búsqueda".
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — The present tense "we never save" is rendered as a past tense "no hemos guardado".
    - Current: `no hemos guardado ni podemos restaurar esta pestaña`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `nunca guardamos ni podemos restaurar esta pestaña`
    - Source states a general policy ("we never save"), not a past event.

### C. Grammar, agreement & spelling

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

### E. Typography, punctuation & spacing

_Nothing in this category._

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

### Fixed to date (0)

_Nothing fixed yet._
