# Focus for Android l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **Previous run** | 2026-11-08 @ `c1a76afc1b60` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Strings | 245 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 23 | **guillemet** |
| apostrophe | `typographic` 696 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| nbsp | `total` 214, `before-punctuation` 144, `space-before-punctuation` 62 | _mixed_ |
| register | `formal` 443 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `content_description_back` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "Navigate back" is rendered as the label "Précédent" instead of an action description, inconsistent with content_description_forward ("Avancer dans l’historique").
    - Current: `Précédent`
    - Source: `Navigate back`
    - Suggest: `Reculer dans l’historique`
    - The source is an action content description read by screen readers; the sibling string content_description_forward is translated as "Avancer dans l’historique", so "Précédent" is both inconsistent and not describing the action.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (2)

- `preference_phone_feature_notification` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02): French UI idiomatically names this permission category in the plural ("Notifications"), as in Firefox's French site-permission settings.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — auto-suggest (2026-11-02): In Focus this setting autocompletes from a bundled list of globally popular sites, not the user's history, so "sites les plus populaires" is accurate.

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — fixed 2026-10-18
