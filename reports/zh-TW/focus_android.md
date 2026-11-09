# Focus for Android l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **Previous run** | 2026-11-08 @ `c1a76afc1b60` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (5)

- `phone_feature_blocked_intro` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon used instead of the locale's full-width punctuation.
    - Current: `若要允許:`
    - Source: `To allow it:`
    - Suggest: `若要允許：`
    - zh-TW convention is full-width punctuation (1071 occurrences); a half-width colon after CJK text deviates.
- `preference_autocomplete_add_example2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — Half-width colon plus space used instead of the locale's full-width colon.
    - Current: `例如: mozilla.org`
    - Source: `Example: mozilla.org`
    - Suggest: `例如：mozilla.org`
    - zh-TW convention is full-width punctuation (1071 occurrences); a half-width colon followed by a space breaks that convention.
- `preference_search_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — "Set default" is rendered as "set as default browser", but this category is about the default search engine.
    - Current: `設為預設瀏覽器`
    - Source: `Set default, autocomplete`
    - Suggest: `設定預設搜尋引擎`
    - The developer comment says this summary describes the search settings screen, where the user sets the default search engine. It is not about making the app the default browser.
- `preference_select_preferred_engine` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — The string uses a halfwidth colon instead of the fullwidth colon used in zh-TW.
    - Current: `搜尋引擎:`
    - Source: `Select your preferred engine:`
    - Suggest: `搜尋引擎：`
    - The locale convention is fullwidth punctuation (1071 occurrences).
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — A half-width colon is used where the locale convention calls for full-width punctuation.
    - Current: `例如:`
    - Source: `Example: example.com/search/?q=%s`
    - Suggest: `例如：`
    - zh-TW uses full-width punctuation throughout the tree.

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
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1111 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (0)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

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

### Dismissed by hand (2)

- `tool_tip_title` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `trackers_count_note` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — pontoon-rejected (2026-11-08): rejected in Pontoon: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>%s is actually replaced with "YYYY 年 MM 月 DD 日" so there should not be a space between %s and 起</p>

_One line each in `locales/zh-TW/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (5)

- `phone_feature_blocked_intro` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-09
- `preference_autocomplete_add_example2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-09
- `preference_search_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-09
- `preference_select_preferred_engine` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-09
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rTW/strings.xml` — fixed 2026-11-09
