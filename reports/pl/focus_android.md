# Focus for Android l10n QA — pl

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

Also for pl: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `polish-double` 84 | **polish-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2, `en` 3 | _mixed_ |
| nbsp | `total` 724, `before-punctuation` 20 | **total** |
| register | `informal` 9 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `crash_report_send_crash_label` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — The translation says "report the crash to Mozilla" using a form that reads as reporting Mozilla itself/omits "report" object correctly.
    - Current: `Zgłoś awarię Mozilli`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Wyślij zgłoszenie awarii do Mozilli`
    - Source is "Send crash report to Mozilla"; "Zgłoś awarię Mozilli" reads as "Report Mozilla's crash" (genitive attached to awaria) rather than sending the report to Mozilla, and it is a checkbox label, not an action command.
- `menu_custom_tab_branding` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — "Powered by %1$s" is rendered as "Funkcja %1$s" ("%1$s feature"), which changes the meaning.
    - Current: `Funkcja %1$s`
    - Source: `Powered by %1$s`
    - Suggest: `Obsługiwane przez %1$s`
    - The source is a branding note meaning the tab is powered by the app; "Funkcja %1$s" says the opposite relation (that this is a feature of the app).
- `onboarding_first_screen_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — "No distractions" is translated as "Skupiona na celu" (focused on the goal), changing the meaning.
    - Current: `Skupiona na celu.`
    - Source: `Fast. Private. No distractions.`
    - Suggest: `Bez rozpraszaczy.`
    - The source says "No distractions"; the Polish states the browser is goal-focused, which is a different claim.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — Plural "custom URLs" rendered as singular in Polish.
    - Current: `Usuń inny adres`
    - Source: `Remove custom URLs`
    - Suggest: `Usuń inne adresy`
    - The source "Remove custom URLs" is plural (screen for removing multiple URLs); the translation says "remove one other address".

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

_One line each in `locales/pl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pl/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
