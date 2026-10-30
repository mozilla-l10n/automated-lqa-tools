# Focus for Android l10n QA — es-ES

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

Also for es-ES: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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

- `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 12, `straight-double` 3 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| inverted marks | `open-question` 105, `open-exclamation` 26 | **open-question** |
| register | `informal` 179, `formal` 11 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (10)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 6 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — The translation drops the word "disabled", reversing the meaning of the warning.
    - Current: `El acceso directo se abrirá con la protección mejorada contra el rastreo`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `El acceso directo se abrirá con la protección mejorada contra el rastreo desactivada`
    - Source says the shortcut will open with Enhanced Tracking Protection *disabled*; the Spanish says it opens with the protection (implicitly enabled), reversing the warning.
- `preference_autocomplete_title_add` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "URL to add" (label for the input field) is rendered as "Agregar URL" ("Add URL"), which is the action, not the field label.
    - Current: `Agregar URL`
    - Source: `Add custom URL`
    - Suggest: `URL a añadir`
    - The developer comment says this is the label for the "custom autocomplete URL" input field; the source is the noun phrase "URL to add", not an imperative action. It also collides with preference_autocomplete_action_add2.
- `preference_mozilla_telemetry2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "usage data" mistranslated as "datos de consumo" (consumption data).
    - Current: `Enviar datos de consumo`
    - Source: `Send usage data`
    - Suggest: `Enviar datos de uso`
    - The source refers to usage/telemetry data; "datos de consumo" suggests data consumption, and other strings use "uso" (e.g. "Ping de uso diario").
- `promote_search_widget_dialog_picture_content_description` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rES/strings.xml` — "Search widget" (a noun phrase naming the widget) is translated as the imperative "Buscar widget" ("Search for widget").
    - Current: `Buscar widget`
    - Source: `Search widget`
    - Suggest: `Widget de búsqueda`
    - The developer comment says this describes a picture of the search widget; the source is a noun phrase, not a command. Other strings in the same dialog use "widget" as a noun.

### C. Grammar, agreement & spelling

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

_Nothing in this category._

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
