# Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for de: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (3)

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — `mozac_feature_sitepermissions_storage_access_message` has placeholders %1$s where the source has %s
    - Current: `Möglicherweise möchten Sie den Zugriff blockieren, wenn nicht klar ist, warum %1$s diese Daten benötigt.`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — `mozac_feature_findindpage_dismiss` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).
- `accessibility_dismiss_find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — `accessibility_dismiss_find_in_page` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).

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
| Strings | 2,908 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 1 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `german-double` 25, `straight-double` 2, `curly-double` 1 | **german-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 8 | **en** |
| register | `formal` 685 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (3)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-de/strings.xml` — `mozac_feature_sitepermissions_storage_access_message` has placeholders %1$s where the source has %s
    - Current: `Möglicherweise möchten Sie den Zugriff blockieren, wenn nicht klar ist, warum %1$s diese Daten benötigt.`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - The set of placeholders must match the source: a missing one drops a value the user should see, an extra one throws.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-de/strings.xml` — `mozac_feature_findindpage_dismiss` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).
- `accessibility_dismiss_find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — `accessibility_dismiss_find_in_page` uses straight double quotes
    - Current: `"Seite durchsuchen" deaktivieren`
    - Source: `Dismiss find in page`
    - The locale's quote convention is `german-double` (25 occurrences).

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
