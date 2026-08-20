# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `2d2a35f255d4` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `2d2a35f255d4` |
| **Previous run** | 2026-08-20 @ `2d2a35f255d4` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,937 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

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
| Strings | 2,937 |
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
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 25 | **curly-double** |
| apostrophe | `typographic` 171 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 2 | **em** |
| register | `informal` 90, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (6)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 2 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `mozac_feature_contextmenu_open_image_in_new_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-it/strings.xml` — "Open image in new tab" translated as "open image in new window"
  - Current: `Apri immagine in nuova finestra`
  - en-US: `Apri immagine in nuova scheda`
  - The source says "new tab", and every other entry in this context menu renders "tab" as "scheda" (e.g. mozac_feature_contextmenu_open_link_in_new_tab). The action opens a tab, not a window.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — Ungrammatical sequence "non è può essere verificato"
  - Current: `%1$s è stato disattivato in quanto non è può essere verificato come sicuro.`
  - en-US: `%1$s è stato disattivato in quanto non può essere verificato come sicuro.`
  - "non è può" is a leftover word; the verb sequence is broken.

### D. Terminology, register & consistency

- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — Wrong apostrophe character (opening quote U+2018 instead of ’)
  - Current: `Informazioni sull‘aggiornamento`
  - en-US: `Informazioni sull’aggiornamento`
  - The whole tree uses the right single quotation mark U+2019 as apostrophe (e.g. "sull’aggiornamento" pattern in dell’estensione, l’estensione); here a left quote glyph is used.
- `external_app_prompt_no_app_title` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — Missing elision/wrong article before the feminine noun "app".
  - Current: `Trova un app per aprire il link`
  - en-US: `Trova un’app per aprire il link`
  - "App" is feminine in Italian, so the article must be elided as "un’app"; "un app" is a spelling/agreement error.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — Message quotes a button label that does not match the actual button text
  - Current: `Selezionare “Riprova” per passare alla modalità in linea e ricaricare la pagina.`
  - en-US: `Selezionare “Riprovare” per passare alla modalità in linea e ricaricare la pagina.`
  - The button on the error page (mozac_browser_errorpages_page_refresh) is labelled "Riprovare"; the message tells the user to press "Riprova", so the quoted label does not exist on screen.
- `content_description_trackers_blocked` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — "trackers" rendered as "tracciamenti" (tracking events) instead of the term used everywhere else in the file.
  - Current: `Numero di tracciamenti bloccati`
  - en-US: `Numero di elementi traccianti bloccati`
  - The same surface uses "Traccianti bloccati" (menu_trackers_blocked_title) and "Elementi traccianti bloccati" (trackers_count_note); "tracciamenti" denotes tracking actions, not trackers.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
