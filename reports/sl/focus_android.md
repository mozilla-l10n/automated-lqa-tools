# Focus for Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `3c577835f1fc` |
| **Previous run** | 2026-11-09 @ `f7a886b5b048` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `straight-double` 17, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 5 | **en** |
| register | `informal` 4, `formal` 90 | **formal** |

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

- `preference_auto_battery_theme` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Set by Battery Saver" is rendered as an imperative "Set the battery saver", reversing the meaning.
    - Current: `Nastavi ohranjevalnik baterije`
    - Source: `Set by Battery Saver`
    - Suggest: `Nastavi ohranjevalnik baterije → "Nastavi ohranjevalnik baterije" naj bo "Nastavi varčevanje z baterijo" (tj. "Določi ohranjevalnik baterije")`
    - The source means the theme is determined by the Battery Saver setting; the Slovenian reads as a command to set/configure the battery saver, i.e. the battery saver becomes the object rather than the agent.

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

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (11)

- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string eab6c12f): unreliable finding: "V redu" is a common, acceptable label for a button that dismisses a prompt; the action is the same.
- `menu_share` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 76af4239): Slovenian typography and the sl Mozilla localization put a space before an ellipsis that follows a complete word (e.g. "Shrani kot …").
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string d09e626c): unreliable finding: "zavračanje vsebine" is a plausible rendering of content blocking and no evidence of an established conflicting term is shown.
- `preference_https_only_summary3` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string d6b1c3b4): unreliable finding: "vzpostaviti povezavo" implicitly refers to connecting to sites; the meaning is preserved.
- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string b60e8bc8): Straight double quotes are the measured majority convention in the sl tree, and quoting a mode name is a legitimate stylistic choice.
- `preference_licensing_info` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string a487408b): "Dovoljenje" is the standard Slovenian term for a software licence (e.g. GPL = "Splošno javno dovoljenje GNU").
- `preference_privacy_secure_mode` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string e54b2d59): unreliable finding: "Skrivni način" is a reasonable rendering of Stealth; the alternative is a matter of preference.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 4429dd49): unreliable finding: No inconsistent top-site term is shown; "glavne strani" is a plausible rendering.
- `search_add_error_duplicate_name` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 3f62f692): unreliable finding: Slovenian has no articles; the sentence naturally reads as some installed search engine using the name.
- `share_dialog_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string 869b596f): unreliable finding: "preko" is an accepted standard variant of "prek" in Slovenian; the change is stylistic.
- `social` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-09, string bc37e965): unreliable finding: As a tracker category label, "Družbeni" (implied "sledilci") is plausibly acceptable.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (6)

- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_privacy_should_block_cookies_cross_site_option` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_privacy_should_block_cookies_yes_option2` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
