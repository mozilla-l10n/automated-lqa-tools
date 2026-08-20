# Android l10n QA — id

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,592 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for id: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (2)

- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — `never_translate_site_header_preference` quotes “Jangan terjemahkan situs ini” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Jangan pernah terjemahkan situs ini”
  - Current: `Untuk menambahkan situs baru: Kunjungi dan pilih “Jangan terjemahkan situs ini” dari menu terjemahan.`
  - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
  - Suggest: `Jangan pernah terjemahkan situs ini`
  - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — `firstrun_shortcut_text` quotes “Tambahkan ke layar Beranda” but the string it names, `menu_add_to_home_screen`, reads “Tambahkan ke Beranda”
  - Current: `Kembali ke situs favorit Anda di %1$s dengan cepat. Cukup pilih "Tambahkan ke layar Beranda" dari menu %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Tambahkan ke Beranda`
  - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

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
| Strings | 2,592 |
| Missing strings | 316 |
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
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**316 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — 305
- `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — 8
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-in/strings.xml` — 2
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-in/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 11, `straight-double` 6 | _mixed_ |
| ellipsis | `char` 19 | **char** |
| dash | `em` 3 | **em** |

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

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — `never_translate_site_header_preference` quotes “Jangan terjemahkan situs ini” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Jangan pernah terjemahkan situs ini”
  - Current: `Untuk menambahkan situs baru: Kunjungi dan pilih “Jangan terjemahkan situs ini” dari menu terjemahan.`
  - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
  - Suggest: `Jangan pernah terjemahkan situs ini`
  - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — `firstrun_shortcut_text` quotes “Tambahkan ke layar Beranda” but the string it names, `menu_add_to_home_screen`, reads “Tambahkan ke Beranda”
  - Current: `Kembali ke situs favorit Anda di %1$s dengan cepat. Cukup pilih "Tambahkan ke layar Beranda" dari menu %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Tambahkan ke Beranda`
  - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
