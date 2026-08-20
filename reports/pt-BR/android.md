# Android l10n QA — pt-BR

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,897 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for pt-BR: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (4)

- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` quotes “Adicionar à tela inicial” but the string it names, `menu_add_to_home_screen`, reads “Adicionar à tela do dispositivo”
  - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Adicionar à tela do dispositivo`
  - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
  - Current: `Excluir automaticamente os dados de navegação selecionados abaixo ao tocar em "Sair" no menu principal`
  - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
  - The locale's quote convention is `curly-double` (13 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
  - Current: `O endereço web deve conter "https://" ou "http://"`
  - Source: `Web address must contain “https://” or “http://”`
  - The locale's quote convention is `curly-double` (13 occurrences).
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
  - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - The locale's quote convention is `curly-double` (13 occurrences).

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
| Strings | 2,897 |
| Missing strings | 11 |
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
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 3 |

### Completeness

**11 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — 11

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 3 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |
| register | `informal` 239 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` quotes “Adicionar à tela inicial” but the string it names, `menu_add_to_home_screen`, reads “Adicionar à tela do dispositivo”
  - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Adicionar à tela do dispositivo`
  - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

### E. Typography, punctuation & spacing

- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
  - Current: `O endereço web deve conter "https://" ou "http://"`
  - Source: `Web address must contain “https://” or “http://”`
  - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rBR/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
  - Current: `Excluir automaticamente os dados de navegação selecionados abaixo ao tocar em "Sair" no menu principal`
  - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
  - The locale's quote convention is `curly-double` (13 occurrences).
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
  - Current: `Volte rapidamente a seus sites preferidos no %1$s. Basta usar "Adicionar à tela inicial" no menu do %1$s.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - The locale's quote convention is `curly-double` (13 occurrences).

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
