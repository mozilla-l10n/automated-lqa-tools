# Focus for Android l10n QA — fy-NL

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
| quotes | `curly-single` 16 | **curly-single** |
| apostrophe | `typographic` 104 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (20)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 10 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
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
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Back-button instruction wrongly says "press the back gesture" instead of pressing the back button, duplicating the gesture string.
    - Current: `druk it gebear werom`
    - Source: `Drag from top & press back to exit`
    - Suggest: `druk op de weromknop`
    - Source is "press back to exit" (hardware/back button), not a gesture; the gesture wording belongs to exit_fullscreen_with_gesture_short.
- `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Singular "Tab's browsing history" rendered as plural "of the tabs".
    - Current: `Jo sneupskiednis fan de ljepblêden is wiske.`
    - Source: `Tab’s browsing history has been erased.`
    - Suggest: `De sneupskiednis fan it ljepblêd is wiske.`
    - Source refers to a single tab's browsing history; the translation says the history of the tabs (plural) and adds "Jo" (your).
- `firstrun_shortcut_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "shortcuts" translated as "keppelingen" (links) instead of "fluchkeppelingen" (shortcuts).
    - Current: `Foegje keppelingen ta oan jo startskerm`
    - Source: `Add shortcuts to your home screen`
    - Suggest: `Foegje fluchkeppelingen ta oan jo startskerm`
    - Source says "Add shortcuts to your home screen"; elsewhere (menu_add_to_shortcuts) "Shortcuts" is "fluchkeppelingen", while "keppelingen" means links.
- `preference_advanced_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Developer tools" is rendered as "Untwikkelersark" (singular/odd form) — should be the plural "Untwikkeldersark"/"Ark foar ûntwikkelers", and the word is misspelled without the initial circumflex.
    - Current: `Untwikkelersark`
    - Source: `Developer tools`
    - Suggest: `Ûntwikkelersark`
    - Frisian "ûntwikkelder/ûntwikkeler" starts with û (circumflex); "Untwikkelersark" is a spelling error.
- `preference_crashes` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Crashes" (app crash reports) is translated as "Ungelokken" (accidents), the wrong sense, and also lacks the Frisian accented initial letter.
    - Current: `Ungelokken`
    - Source: `Crashes`
    - Suggest: `Fêstrinnen`
    - The developer comment says this links to Focus crash reports; "ûngelokken" means real-world accidents, not software crashes. Also the initial U should be Û.
- `preference_privacy_should_block_cookies_third_party_only_option` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — The verb "blokkearje" (block) is missing, so the option reads "Only third-party cookies" instead of "Block 3rd-party cookies only".
    - Current: `Allinnich cookies fan tredden`
    - Source: `Block 3rd-party cookies only`
    - Suggest: `Allinnich cookies fan tredden blokkearje`
    - Source is "Block 3rd-party cookies only"; the parallel option string for tracker cookies correctly ends in "blokkearje".
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Coordination makes "apps" and "taking screenshots" both objects of switching, distorting the meaning.
    - Current: `Websiden ferstopje by wikseljen fan apps en meitsjen fan skermôfdrukken blokkearje.`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `Websiden ferstopje by it wikseljen fan apps en it meitsjen fan skermôfdrukken blokkearje.`
    - Source: hide webpages when switching apps AND block taking screenshots; current wording reads as "switching apps and taking screenshots".
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — "Shortcuts" (pinned website shortcuts) is rendered as "fluchtoetsen" (keyboard shortcuts).
    - Current: `fluchtoetsen`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `fluchkeppelingen`
    - The developer comment explains Shortcuts are pinned favourite websites, not keyboard shortcuts.

### C. Grammar, agreement & spelling

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on “Us” (should be “Ús”).
    - Current: `Us missy is it fersoargjen`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Ús missy is it fersoargjen`
    - The Frisian possessive “ús” keeps its accent when capitalized.
- `crash_report_send_crash_label` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Ungelokrapport".
    - Current: `Ungelokrapport`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Ûngelokrapport`
    - The Frisian word is "ûngelok"; capitalized at sentence start it must be "Û", as elsewhere the locale uses proper diacritics (e.g. "ÚT").
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Dutch spelling "bij" used instead of Frisian "by".
    - Current: `Wolkom bij %1$s`
    - Source: `Welcome to %1$s`
    - Suggest: `Wolkom by %1$s`
    - In Frisian the preposition is "by"; "bij" is the Dutch form (Frisian "bij" means the insect).
- `phone_feature_blocked_step_permissions` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Dutch word "Machtigingen" used instead of Frisian "Machtigingen" spelling/term.
    - Current: `2. Tik op { <b> }Machtigingen{ </b> }`
    - Source: `2. Tap { <b> }Permissions{ </b> }`
    - Suggest: `2. Tik op { <b> }Tastimmingen{ </b> }`
    - "Machtigingen" is Dutch; the Frisian term for Android permissions is "Tastimmingen" (or "Machtigings"), consistent with other permission strings.
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untskoattelje".
    - Current: `Untskoattelje`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `Ûntskoattelje`
    - Frisian spelling requires Û; the same verb is written "ûntskoatteljen" in preference_security_biometric.
- `preference_state_off` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Ut" (Off).
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Ût`
    - The Frisian word for "off" is "Út/Ût" with a diacritic; plain "Ut" is a misspelling.
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Misspelling of "Bygelyks".
    - Current: `Bygelyls`
    - Source: `Example: example.com/search/?q=%s`
    - Suggest: `Bygelyks`
    - "Bygelyls" is a typo for the Frisian "Bygelyks" (Example/For example).
- `show_biometric_button_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Ûntskoattelje".
    - Current: `Untskoattelje`
    - Source: `Unlock`
    - Suggest: `Ûntskoattelje`
    - Frisian spells the prefix "ûnt-" with a circumflex; "Untskoattelje" is misspelled.
- `tabs_tray_action_add_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-fy-rNL/strings.xml` — Adjective agreement error: 'ljepblêd' is neuter, so the attributive adjective should be 'Nij', not 'Nije'.
    - Current: `Nije ljepblêd tafoegje`
    - Source: `Add new tab`
    - Suggest: `Nij ljepblêd tafoegje`
    - In Frisian, indefinite neuter nouns take the uninflected adjective form ('in nij ljepblêd'), as also used correctly in tip_open_in_new_tab ('in nij ljepblêd').

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

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
