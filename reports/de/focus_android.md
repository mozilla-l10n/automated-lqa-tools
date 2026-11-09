# Focus for Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `f7a886b5b048` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for de: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `german-double` 23, `curly-double` 1 | **german-double** |
| ellipsis | `char` 22 | **char** |
| dash | `en` 7 | **en** |
| register | `formal` 658 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (0)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (2)

- `cfr_for_start_browsing` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 5f5e3a51): unreliable finding: "bei der Gelegenheit auch noch" is a free, idiomatic rendering of "as you go" that still conveys trackers and other harmful elements being blocked during the session; changing it would be stylistic.
- `preference_privacy_block_content_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — auto-suggest (2026-11-09, string 6f991eb6): unreliable finding: As a summary shown under the setting toggle, "Dies" naturally refers to enabling the setting, so the condition is implied and the warning's meaning is preserved.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/de/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (5)

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `menu_open_with_a_browser2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — fixed 2026-11-03
