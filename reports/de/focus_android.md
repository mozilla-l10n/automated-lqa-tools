# Focus for Android l10n QA — de

| | |
|---|---|
| **Generated** | 2026-11-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `66b4c732bf9d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `66b4c732bf9d` |
| **Previous run** | 2026-11-05 @ `f8e5f3a985cd` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 250 |

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
| quotes | `german-double` 23, `curly-double` 1 | **german-double** |
| ellipsis | `char` 22 | **char** |
| dash | `en` 7 | **en** |
| register | `formal` 676 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (2)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `cfr_for_start_browsing` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "as you go" is mistranslated as "bei der Gelegenheit auch noch", which changes the meaning.
    - Current: `und wir blockieren Tracker und bei der Gelegenheit auch noch andere schädliche Elemente`
    - Source: `Start your private browsing session, and we’ll block trackers and other bad stuff as you go.`
    - Suggest: `und wir blockieren dabei Tracker und andere schädliche Elemente`
    - The source says trackers and other bad stuff are blocked as you browse; the German implies blocking other bad stuff is a casual side effect ("bei der Gelegenheit auch noch"), which is not the source meaning.
- `preference_privacy_block_content_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Enabling" is not rendered; the German says "This can cause…" without the condition of activating the setting.
    - Current: `Dies kann dazu führen, dass manche Seiten sich ungewöhnlich verhalten`
    - Source: `Enabling may cause some pages to behave unexpectedly`
    - Suggest: `Das Aktivieren kann dazu führen, dass sich manche Seiten unerwartet verhalten`
    - The source conditions the warning on enabling the option; the translation drops that.

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
