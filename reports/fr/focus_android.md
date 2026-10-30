# Focus for Android l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 250 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

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
| Strings | 250 |
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
| apostrophe | `typographic` 693 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |
| nbsp | `total` 211, `before-punctuation` 142, `space-before-punctuation` 64 | _mixed_ |
| register | `formal` 442 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `content_description_back` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "Navigate back" is rendered as the label "Précédent" instead of an action description, inconsistent with content_description_forward ("Avancer dans l’historique").
    - Current: `Précédent`
    - Source: `Navigate back`
    - Suggest: `Reculer dans l’historique`
    - The source is an action content description read by screen readers; the sibling string content_description_forward is translated as "Avancer dans l’historique", so "Précédent" is both inconsistent and not describing the action.
- `firstrun_privacy_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "Make privacy a habit" is translated as "Reprenez votre vie privée en main" (take back control of your privacy), a different meaning.
    - Current: `Reprenez votre vie privée en main`
    - Source: `Make privacy a habit`
    - Suggest: `Faites de la vie privée une habitude`
    - The source urges making privacy a habit, not regaining control of it.
- `preference_phone_feature_notification` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — Singular "Notification" (a site-permission category label) is rendered in the plural.
    - Current: `Notifications`
    - Source: `Notification`
    - Suggest: `Notification`
    - The source is the singular permission name "Notification", matching the other site-permission entries; the French pluralises it.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — "top sites" rendered as "sites les plus populaires" instead of the established "sites les plus visités" used elsewhere for top sites.
    - Current: `Pour les sites les plus populaires`
    - Source: `For top sites`
    - Suggest: `Pour les sites les plus visités`
    - "Top sites" in Mozilla French is consistently "sites les plus visités"; "populaires" changes the meaning (popularity vs. the user's own most-visited sites).

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fr/strings.xml` — fixed 2026-10-18
