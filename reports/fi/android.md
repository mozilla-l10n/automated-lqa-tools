# Android l10n QA — fi

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,791 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not finish this run.** It stopped at batch 1 of 70: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'tool_choice: type "tool" and "any" are not supported for this model.'}, 'request_id': 'req_011Cg5kaSkbHWnJbqoSi2DYg'}. What it read is here and is kept; the strings it never reached are unreviewed, and the next run resumes at the first of them.

Also for fi: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (1)

- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — `never_translate_site_header_preference` quotes “Älä käännä koskaan tätä sivustoa” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Älä koskaan käännä sivustoa”
    - Current: `Uuden sivuston lisääminen: Käy sivustolla ja valitse käännösvalikosta “Älä käännä koskaan tätä sivustoa”.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Älä koskaan käännä sivustoa`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

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
| Files | 45 |
| Strings | 2,791 |
| Missing strings | 7 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**7 strings** are not translated yet, concentrated in:

- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fi/strings.xml` — 4
- `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — 2
- `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 9, `straight-double` 7 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `en` 3 | **en** |

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

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — `never_translate_site_header_preference` quotes “Älä käännä koskaan tätä sivustoa” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Älä koskaan käännä sivustoa”
    - Current: `Uuden sivuston lisääminen: Käy sivustolla ja valitse käännösvalikosta “Älä käännä koskaan tätä sivustoa”.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Älä koskaan käännä sivustoa`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
