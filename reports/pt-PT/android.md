# Android l10n QA — pt-PT

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,548 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not finish this run.** It stopped at batch 1 of 64: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'tool_choice: type "tool" and "any" are not supported for this model.'}, 'request_id': 'req_011Cg5kab8894VLz9s7xMEx6'}. What it read is here and is kept; the strings it never reached are unreviewed, and the next run resumes at the first of them.

Also for pt-PT: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (3)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }O navegador está a operar no modo desligado e não consegue estabelecer ligação ao objeto solicitado.{ </p> } { <ul> } { <li> }O computador está ligado a uma rede ativa?{ </li> } { <li> }Pressione "Tentar novament…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Exclui automaticamente os dados de navegação quando seleciona "Sair" no menu principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `O endereço web deve conter "https://" ou "http://"`
    - Source: `Web address must contain “https://” or “http://”`
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
| Files | 44 |
| Strings | 2,548 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 3 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 3 | **curly-double** |
| apostrophe | `typographic` 1 | **typographic** |
| ellipsis | `char` 19 | **char** |
| dash | `em` 1, `en` 1 | _mixed_ |
| nbsp | `total` 7 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (3)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-pt-rPT/strings.xml` — `mozac_browser_errorpages_offline_message` uses straight double quotes
    - Current: `{ <p> }O navegador está a operar no modo desligado e não consegue estabelecer ligação ao objeto solicitado.{ </p> } { <ul> } { <li> }O computador está ligado a uma rede ativa?{ </li> } { <li> }Pressione "Tentar novament…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `O endereço web deve conter "https://" ou "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-pt-rPT/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Exclui automaticamente os dados de navegação quando seleciona "Sair" no menu principal`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (13 occurrences).

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pt-PT/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
