# Focus for Android l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `f7a886b5b048` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [Firefox for Android](android.md) · [Firefox](firefox.md)

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
| quotes | `curly-single` 16 | **curly-single** |
| apostrophe | `typographic` 104 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (5)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Dismiss" is translated as "Fuortsmite" (delete/throw away) instead of dismissing/closing the overlay.
    - Current: `Fuortsmite`
    - Source: `Dismiss`
    - Suggest: `Slute`
    - Per the developer comment the action dismisses the overlay and returns to the browser; ‘Fuortsmite’ means to discard/delete, which suggests data removal.
- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Dismiss" (close/hide the message) is translated as "Fuortsmite" (delete).
    - Current: `Fuortsmite`
    - Source: `Dismiss`
    - Suggest: `Slute`
    - The developer comment says the button dismisses a message; "Fuortsmite" means delete/remove, which conveys a destructive action not present in the source.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Coordination makes "apps" and "taking screenshots" both objects of switching, distorting the meaning.
    - Current: `Websiden ferstopje by wikseljen fan apps en meitsjen fan skermôfdrukken blokkearje.`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `Websiden ferstopje by it wikseljen fan apps en it meitsjen fan skermôfdrukken blokkearje.`
    - Source: hide webpages when switching apps AND block taking screenshots; current wording reads as "switching apps and taking screenshots".

### C. Grammar, agreement & spelling

- `phone_feature_blocked_step_permissions` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Dutch word "Machtigingen" used instead of Frisian "Machtigingen" spelling/term.
    - Current: `2. Tik op { <b> }Machtigingen{ </b> }`
    - Source: `2. Tap { <b> }Permissions{ </b> }`
    - Suggest: `2. Tik op { <b> }Tastimmingen{ </b> }`
    - "Machtigingen" is Dutch; the Frisian term for Android permissions is "Tastimmingen" (or "Machtigings"), consistent with other permission strings.

### D. Terminology, register & consistency

- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "search string" rendered as "sykterm" here but "syksterm" in search_add_error_empty_search on the same screen.
    - Current: `sykterm`
    - Source: `Check that search string matches Example format`
    - Suggest: `syksterm`
    - The same source term "search string" is translated inconsistently within the same settings surface (search_add_error_empty_search uses "syksterm").

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (6)

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 417523ee): Frisian orthography customarily omits diacritics on capital letters (cf. 'Us Heit', 'Us Mem'), so 'Us' is the expected capitalized form of 'ús'.
- `crash_report_send_crash_label` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 3b5342fa): Frisian customarily drops the circumflex on a capital initial (as in 'Us Mem'), so 'Ungelok-' is the normal capitalized spelling.
- `preference_advanced_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string 2f9db6da): The fy-NL tree writes capital Û as U (e.g. 'Untskoattelje'), and 'Untwikkelersark' is a correct compound for 'developer tools'.
- `preference_crashes` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05, string 790b91f0): Mozilla fy-NL uses 'ûngelok' (e.g. ûngelokrapporten) as the term for software crashes, and capital Û is written U in this tree (cf. 'Untskoattelje').
- `preference_state_off` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 1c0d693a): Frisian customarily omits diacritics on capital letters, so 'Ut' is the normal capitalized form of 'út'.
- `show_biometric_button_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06, string 3a59d31b): Frisian customarily omits diacritics on capital letters, so 'Untskoattelje' is the normal capitalized spelling of 'ûntskoattelje'.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/fy-NL/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (8)

- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_privacy_should_block_cookies_third_party_only_option` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `tabs_tray_action_add_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
