# Focus for Android l10n QA — el

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

Also for el: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `guillemet` 45 | **guillemet** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — The translation drops "reported", so it claims Focus blocks all deceptive, attack, malware and unwanted-software sites, not just reported ones.
    - Current: `Φραγή ιστοτόπων εξαπάτησης`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `Φραγή αναφερόμενων ιστοτόπων εξαπάτησης`
    - The source limits blocking to sites that have been reported. Without that limit, the Greek promises more protection than the feature gives.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — The translation drops "reported", so it claims Focus blocks all deceptive, attack, malware and unwanted-software sites, not just reported ones.
    - Current: `Φραγή ιστοτόπων εξαπάτησης`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `Φραγή αναφερόμενων ιστοτόπων εξαπάτησης`
    - The source limits blocking to sites that have been reported. Without that limit, the Greek promises more protection than the feature gives.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — The source's reason, "As a private browser", is rendered as "For security reasons".
    - Current: `Για λόγους ασφαλείας, δεν αποθηκεύουμε`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `Ως ιδιωτικό πρόγραμμα περιήγησης, δεν αποθηκεύουμε ποτέ`
    - The en-US explains that the tab can't be restored because Focus is a private browser that never saves tabs. The Greek gives a different reason (security) and drops "never".

### C. Grammar, agreement & spelling

- `dialog_addtohomescreen_action_add` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — Missing accent in «Προσθηκη».
    - Current: `Προσθηκη`
    - Source: `Add`
    - Suggest: `Προσθήκη`
    - Mixed-case Greek requires the tonos; the correct spelling is «Προσθήκη», as used elsewhere (e.g. menu_add_to_home_screen).
- `dialog_addtohomescreen_action_cancel` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — Missing accent in «Ακυρωση».
    - Current: `Ακυρωση`
    - Source: `Cancel`
    - Suggest: `Ακύρωση`
    - Mixed-case Greek requires the tonos; correct spelling is «Ακύρωση».
- `enable_search_suggestions_no` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — Missing accent on capital initial in «Οχι».
    - Current: `Οχι`
    - Source: `No`
    - Suggest: `Όχι`
    - In mixed case, an initial capital vowel keeps its tonos; correct spelling is «Όχι».
- `search_add_manually_save` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — Missing accent in "Αποθηκευση".
    - Current: `Αποθηκευση`
    - Source: `Save`
    - Suggest: `Αποθήκευση`
    - Greek spelling needs the accent on the antepenultimate syllable: Αποθήκευση.

### D. Terminology, register & consistency

- `exit_fullscreen_with_gesture_short` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — Translation is 78 characters, exceeding the 68-character limit set in the developer comment.
    - Current: `Σύρετε από το πάνω μέρος και χρησιμοποιήστε τη χειρονομία επιστροφής για έξοδο`
    - Source: `Drag from top & use back gesture to exit`
    - Suggest: `Σύρετε από πάνω και κάντε χειρονομία επιστροφής για έξοδο`
    - Developer comment: 'This text should be as short as possible, max 68 chars'; the current text is 78 characters and may be truncated.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — "Qualified" in the eIDAS sense is translated as "Πιστοποιημένο" ("certified") instead of the regulation's Greek term "εγκεκριμένο".
    - Current: `Πιστοποιημένο όπως ορίζει`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Εγκεκριμένο όπως ορίζει`
    - The developer comment says this is the eIDAS term "qualified" (as in QWAC). As I understand it, the Greek text of the regulation uses "εγκεκριμένο" (e.g. "εγκεκριμένο πιστοποιητικό"), so "πιστοποιημένο" doesn't match the legal wording.
- `shortcut_erase_and_open_short_label` — `mozilla-mobile/focus-android/app/src/main/res/values-el/strings.xml` — The short shortcut label is 20 characters, double the 10-character maximum set in the developer comment.
    - Current: `Διαγραφή και άνοιγμα`
    - Source: `Erase & open`
    - Suggest: `Διαγρ./άνοιγμα`
    - The developer comment says Android recommends at most 10 characters for this launcher label. The Greek is 20 characters and will be cut off on the home screen.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/el/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
