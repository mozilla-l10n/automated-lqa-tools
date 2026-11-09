# Focus for Android l10n QA — zh-TW

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `eb5867992b38` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `eb5867992b38` |
| **Previous run** | 2026-11-09 @ `bf7b409a0435` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-TW: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1111 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

### Proposed conventions — not applied (1)

Recurring reasons in this locale's tool-written dismissals. Nothing here reaches the reviewer until a person adds it to `focus_android/locales/zh-TW/conventions.md`; an inferred reason is a model's guess at why a Pontoon reviewer said no.

- When the approved translation is already accurate, do not raise a finding that only swaps in a synonym or another equally valid wording. zh-TW reviewers have repeatedly rejected such rewrites as "interchangeable" or "not better from original translation". Examples: 報表 and 報告 are both acceptable for a crash "report" button. Different measure words (quantifiers) for permission items are also interchangeable. Rewording a remove-bookmark menu item or a "recommended" label gains nothing either. Still flag the translation when it actually changes or loses meaning, for example when an "older than %S months" condition is rendered as just "%S months ago". Also flag glossary violations and leftover untranslated English.
    _Behind it: 8 dismissals, 8 of them rejected in Pontoon._

    - `mozac_feature_addons_permissions_browser_settings_description_for_update` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
    - `mozac_feature_addons_permissions_content_description_item` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable for quantifiers for permission items</p>
    - `home_bookmarks_menu_item_remove` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangable</p>
    - `ip_protection_location_recommended_label` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>interchangeable; not better from original translation</p>
    - `protection_panel_banner_protected_no_blocked_trackers_description` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
    - `startup_crash_positive` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>
    - `trackers_blocked_empty` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>not better from original translation</p>
    - `unsubmitted_crash_dialog_positive_button` (android) — _rejected, reviewer's comment_: 93Rx_ofmgBDhnz4QZD1aHlOg0uY: <p>報表, 報告 for is interchangable</p>

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

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/zh-TW/dismissed.txt` brings the finding back now._

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
