# Android l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `afd16223d876` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,897 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for hu: [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (2)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Próbálja újra” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Újrapróbálkozás”
  - Current: `{ <p> }A böngésző kapcsolat nélküli módban van, ezért nem tud csatlakozni a kért elemhez.{ </p> } { <ul> } { <li> }Csatlakoztatva van a számítógép a hálózathoz?{ </li> } { <li> }Nyomja meg a „Próbálja újra” gombot az on…`
  - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
  - Suggest: `Újrapróbálkozás`
  - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — `firstrun_shortcut_text` quotes “Hozzáadás a kezdőképernyőre” but the string it names, `menu_add_to_home_screen`, reads “Kezdőképernyőhöz adás”
  - Current: `Térjen vissza gyorsan a kedvenc oldalaihoz a %1$sban. Csak válassza a „Hozzáadás a kezdőképernyőre” lehetőséget a %1$s menüből.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Kezdőképernyőhöz adás`
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
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**11 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-hu/strings.xml` — 11

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 17 | **polish-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 6 | **en** |

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

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hu/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “Próbálja újra” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “Újrapróbálkozás”
  - Current: `{ <p> }A böngésző kapcsolat nélküli módban van, ezért nem tud csatlakozni a kért elemhez.{ </p> } { <ul> } { <li> }Csatlakoztatva van a számítógép a hálózathoz?{ </li> } { <li> }Nyomja meg a „Próbálja újra” gombot az on…`
  - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
  - Suggest: `Újrapróbálkozás`
  - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — `firstrun_shortcut_text` quotes “Hozzáadás a kezdőképernyőre” but the string it names, `menu_add_to_home_screen`, reads “Kezdőképernyőhöz adás”
  - Current: `Térjen vissza gyorsan a kedvenc oldalaihoz a %1$sban. Csak válassza a „Hozzáadás a kezdőképernyőre” lehetőséget a %1$s menüből.`
  - Source: `Return to your favorite sites in %1$s quickly. Just select “Add to Home screen” from the %1$s menu.`
  - Suggest: `Kezdőképernyőhöz adás`
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
