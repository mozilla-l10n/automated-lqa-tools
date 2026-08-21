# Android l10n QA — es-MX

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,886 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for es-MX: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (7)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Volver a intentarlo” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Intenta de nuevo”
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Intenta de nuevo`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `never_translate_site_header_preference` quotes “No traducir nunca este sitio” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Nunca traducir este sitio”
    - Current: `Para añadir un sitio nuevo: visítalo y selecciona “No traducir nunca este sitio” en el menú de traducción.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Nunca traducir este sitio`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` quotes “agregar a la página de inicio” but the string it names, `menu_add_to_home_screen`, reads “Agregar a la pantalla de inicio”
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Agregar a la pantalla de inicio`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Eliminar automáticamente los datos de navegación cuando selecciones "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
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
| Strings | 2,886 |
| Missing strings | 22 |
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

**22 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — 22

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

## 3. Open findings (7)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Volver a intentarlo” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Intenta de nuevo”
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Intenta de nuevo`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `never_translate_site_header_preference` quotes “No traducir nunca este sitio” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Nunca traducir este sitio”
    - Current: `Para añadir un sitio nuevo: visítalo y selecciona “No traducir nunca este sitio” en el menú de traducción.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Nunca traducir este sitio`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` quotes “agregar a la página de inicio” but the string it names, `menu_add_to_home_screen`, reads “Agregar a la pantalla de inicio”
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - Suggest: `Agregar a la pantalla de inicio`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-es-rMX/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }El navegador está operando en modo sin conexión y no puede conectarse con el elemento solicitado.{ </p> } { <ul> } { <li> }¿Estás conectado el equipo a una red activa?{ </li> } { <li> }Presiona "Volver a intentar…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `La dirección web debe contener "https://" o "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-es-rMX/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Eliminar automáticamente los datos de navegación cuando selecciones "Salir" en el menú principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (12 occurrences).
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rMX/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `Regresa rápidamente a tus sitios favoritos en %1$s. Selecciona "agregar a la página de inicio" desde el menú %1$s.`
    - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
    - The locale's quote convention is `curly-double` (12 occurrences).

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
