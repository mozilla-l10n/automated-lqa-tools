# Focus for Android l10n QA — nl

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

Also for nl: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-single` 15 | **curly-single** |
| apostrophe | `typographic` 46 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |
| register | `formal` 436 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — "Dismiss" (close/return to browser) is translated as "Verwijderen" (delete).
    - Current: `Verwijderen`
    - Source: `Dismiss`
    - Suggest: `Sluiten`
    - Per the developer comment, tapping the overlay dismisses typing mode and returns to the browser; "Verwijderen" means "delete", which describes a destructive action, not dismissing.
- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — "Dismiss" is translated as "Verwijderen" (delete), which means something different.
    - Current: `Verwijderen`
    - Source: `Dismiss`
    - Suggest: `Sluiten`
    - The button dismisses/closes a message; "Verwijderen" means "Delete", implying data removal rather than dismissing the prompt.
- `firstrun_shortcut_title` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — ‘Shortcuts’ is translated as ‘koppelingen’ (links) instead of ‘snelkoppelingen’ (shortcuts).
    - Current: `Voeg koppelingen toe aan uw startscherm`
    - Source: `Add shortcuts to your home screen`
    - Suggest: `Voeg snelkoppelingen toe aan uw startscherm`
    - The source says 'Add shortcuts to your home screen'; 'koppelingen' means links, and elsewhere in this batch 'Shortcuts' is rendered as 'snelkoppelingen' (menu_add_to_shortcuts).

### C. Grammar, agreement & spelling

- `promote_search_widget_dialog_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-nl/strings.xml` — Comma splice and misplaced/duplicated adverb make the sentence ungrammatical and awkward.
    - Current: `We laten u nu verdergaan met uw privénavigatie, u kunt de volgende keer sneller van start gaan nu met de %1$s-widget op uw startscherm.`
    - Source: `We’ll leave you to your private browsing, but get a quicker start next time with the %1$s widget on your Home screen.`
    - Suggest: `We laten u verdergaan met uw privénavigatie, maar u kunt de volgende keer sneller van start gaan met de %1$s-widget op uw startscherm.`
    - The source uses ‘but’ to join the clauses; the Dutch joins two main clauses with only a comma and repeats ‘nu’ in an ungrammatical position (‘van start gaan nu met’).

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
