# Android l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `4d7697d1b89b` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 0 of 2,798 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not finish this run.** It stopped at batch 1 of 70: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'tool_choice: type "tool" and "any" are not supported for this model.'}, 'request_id': 'req_011Cg5kb6gNUwKTkjkGwavPR'}. What it read is here and is kept; the strings it never reached are unreviewed, and the next run resumes at the first of them.

Also for zh-TW: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `nova_onboarding_customize_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `nova_onboarding_customize_prompt_body` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。 [other] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。`
    - Source: `{$quantity ->} [one] %1$s blocked %2$,d tracker while you roamed the web. [other] %1$s blocked %2$,d trackers while you roamed the web.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `downloads_delete_dialog_title` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 要刪除檔案嗎？ [other] 要刪除 %d 個檔案嗎？`
    - Source: `{$quantity ->} [one] Delete file? [other] Delete %d files?`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

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
| Strings | 2,798 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 2 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1071 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (2)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `downloads_delete_dialog_title` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 要刪除檔案嗎？ [other] 要刪除 %d 個檔案嗎？`
    - Source: `{$quantity ->} [one] Delete file? [other] Delete %d files?`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `nova_onboarding_customize_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-zh-rTW/strings.xml` — `nova_onboarding_customize_prompt_body` has plural variant ['one'], which zh-TW does not have
    - Current: `{$quantity ->} [one] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。 [other] 在您上網時，%1$s 封鎖了 %2$,d 組追蹤器。`
    - Source: `{$quantity ->} [one] %1$s blocked %2$,d tracker while you roamed the web. [other] %1$s blocked %2$,d trackers while you roamed the web.`
    - zh-TW has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

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

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
