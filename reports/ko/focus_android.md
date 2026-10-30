# Focus for Android l10n QA — ko

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

Also for ko: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 9, `straight-double` 4, `curly-single` 1 | _mixed_ |
| apostrophe | `typographic` 1, `straight` 1 | _mixed_ |
| ellipsis | `char` 21 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (15)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
    - The source only says Mozilla *strives* to collect only what it needs. The Korean drops 'strives' and states it as a certain fact about the product's data collection, which is a stronger guarantee than the source gives.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "%1$s puts you in control" is rendered as "you can use %1$s with various features".
    - Current: `%1$s를 여러 기능으로 사용할 수 있습니다.`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `%1$s로 직접 제어할 수 있습니다.`
    - The source says the app gives the user control. The Korean says the app can be used for many features, which is a different claim.
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The translation says the site itself was stopped, not that it was stopped from spying on the user.
    - Current: `사용자를 감시하는 이 사이트를 중지했습니다`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `이 사이트가 사용자를 감시하지 못하도록 막았습니다`
    - The source says 'We stopped this site from spying on you', meaning the tracking was blocked. The Korean reads as 'we stopped (halted) this site that spies on the user', which describes a different action.
- `preference_auto_battery_theme` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "절전 모드로 설정" means "set to battery saver mode", not "set by Battery Saver".
    - Current: `절전 모드로 설정`
    - Source: `Set by Battery Saver`
    - Suggest: `절전 모드에 따라 설정`
    - Per the comment, this option makes Battery Saver decide the dark or light theme. In Korean, '~로 설정' reads as switching something into power-saving mode.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
    - The source only says Mozilla *strives* to collect only what it needs. The Korean drops 'strives' and states it as a certain fact about the product's data collection, which is a stronger guarantee than the source gives.
- `promote_search_widget_dialog_picture_content_description` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — 'Search widget' (a noun naming the widget) is translated as the action 'search for widgets'.
    - Current: `위젯 검색하기`
    - Source: `Search widget`
    - Suggest: `검색 위젯`
    - The developer comment says this describes a picture of the search widget. 위젯 검색하기 means 'search for a widget', so a screen reader would describe the image wrongly.

### C. Grammar, agreement & spelling

- `find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Spacing error: the bound noun 내 must be written as a separate word.
    - Current: `페이지내 검색`
    - Source: `Find in Page`
    - Suggest: `페이지 내 검색`
    - Under standard Korean spacing rules, 내 (meaning 'within') is a bound noun and is written with a space after the noun it follows.
- `onboarding_first_screen_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The subtitle ends sentences with full stops after a connective (-고) and a modifier (-는), so it reads as ungrammatical Korean.
    - Current: `빠르고. 사생활 보호되고. 방해 없는.`
    - Source: `Fast. Private. No distractions.`
    - Suggest: `빠름. 사생활 보호. 방해 없음.`
    - "Fast. Private. No distractions." is three short phrases that each stand alone. The Korean puts a full stop after word forms that need something to follow them: "빠르고" and "보호되고" end in "-고" ("and…"), and "없는" needs a noun after it. A noun-style ending (빠름 / 사생활 보호 / 방해 없음) keeps the three short phrases and is grammatical.
- `preference_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "데이타" is a non-standard spelling of "데이터".
    - Current: `데이타`
    - Source: `Cookies and Site Data`
    - Suggest: `데이터`
    - Standard Korean spelling of 'data' is 데이터. The locale uses it elsewhere too.
- `preference_category_data_choices` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "데이타" is a non-standard spelling of "데이터".
    - Current: `데이타 선택`
    - Source: `Data Choices`
    - Suggest: `데이터 선택`
    - Standard Korean spelling of 'data' is 데이터.
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Misspelling: "에상치" should be "예상치".
    - Current: `에상치 못한`
    - Source: `Pages may load faster, but may also behave unexpectedly`
    - Suggest: `예상치 못한`
    - The correct spelling of 'unexpected' is 예상치 못한; 에상치 is a typo.
- `preference_privacy_and_security_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Non-standard spelling "데이타" instead of the standard "데이터".
    - Current: `데이타`
    - Source: `Tracking, cookies, data choices`
    - Suggest: `데이터`
    - Standard Korean orthography for 'data' is 데이터.
- `preference_privacy_should_block_cookies_third_party_tracker_cookies_option` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The particle 만 is wrongly separated from the noun it attaches to.
    - Current: `쿠키 만 차단`
    - Source: `Block 3rd-party tracker cookies only`
    - Suggest: `쿠키만 차단`
    - Under Korean spacing rules, particles such as 만 attach to the preceding noun. The sibling string also writes it as 쿠키만.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The negative adverb 못 needs a space before the verb: 못 찍게.
    - Current: `못찍게`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `못 찍게`
    - Standard Korean spacing writes the adverb 못 apart from the verb it modifies.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Misspelling: 헤제 should be 해제 (unlock).
    - Current: `잠금 헤제에`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `잠금 해제에`
    - The correct Korean word for 'unlock/release' is 해제; 헤제 is a spelling error.
- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The connective ending '-는지' is wrongly split into '-는 지'.
    - Current: `일치하는 지`
    - Source: `Check that search string matches Example format`
    - Suggest: `일치하는지`
    - In '일치하는지', '-는지' is a connective ending for an indirect question ('whether it matches'), so Korean spelling rules write it attached. Spacing it as '는 지' is only correct when 지 is the bound noun for elapsed time, which is not the meaning here.

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ko/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
