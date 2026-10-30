# Focus for Android l10n QA — uk

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

Also for uk: [Firefox for Android](android.md) · [Firefox](firefox.md)

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
| quotes | `curly-double` 13, `straight-double` 10 | _mixed_ |
| apostrophe | `typographic` 111, `straight` 3 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 9 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (7)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "Your favorite URLs" (the list the user builds) is translated as "URLs of popular sites".
    - Current: `URL-адреси популярних сайтів`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `ваші улюблені URL-адреси`
    - The source and the developer comment both refer to the user's own list of URLs. "Популярних сайтів" mixes this up with the separate built-in list of 450 popular URLs (preference_autocomplete_topsite_summary2), so it misdescribes what the toggle does.
- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — "HTTPS-Only Mode" is rendered as "HTTPS-режим", which drops the "only" meaning.
    - Current: `HTTPS-режим`
    - Source: `HTTPS-Only Mode`
    - Suggest: `Режим лише HTTPS`
    - The source names a mode that allows only HTTPS connections. "HTTPS-режим" just means "HTTPS mode" and loses the restriction. Firefox uses "Режим лише HTTPS" for this.

### C. Grammar, agreement & spelling

- `menu_about` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The menu item is the bare preposition "Про" with no object, so it reads as unfinished.
    - Current: `Про`
    - Source: `About`
    - Suggest: `Про програму`
    - In English, "About" works on its own as a menu label. In Ukrainian, "Про" needs an object (for example "Про програму"). On its own it is ungrammatical.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The example nouns are in the nominative case but should agree with the genitive "активності".
    - Current: `наприклад, дотики і прокручування`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `наприклад, дотиків і прокручування`
    - "Дотики і прокручування" are examples of the activity being measured ("вимірювання активності"), so they need the same genitive case.

### D. Terminology, register & consistency

- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Forward-navigation content description uses a noun ("Перехід уперед") while its paired back-navigation string uses an imperative verb ("Перейти назад").
    - Current: `Перехід уперед`
    - Source: `Navigate forward`
    - Suggest: `Перейти вперед`
    - The two buttons are paired screen-reader labels on the same toolbar ("Navigate back"/"Navigate forward"); they should share the same verbal form for consistency.

### E. Typography, punctuation & spacing

- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — Missing comma before the participial phrase "перейшовши до…".
    - Current: `Змініть це налаштування перейшовши`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `Змініть це налаштування, перейшовши`
    - Ukrainian punctuation requires a comma to set off a дієприслівниковий зворот; without it the sentence is grammatically mis-punctuated.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-uk/strings.xml` — The final sentence has lost the full stop that ends the source sentence.
    - Current: `посередницькі сертифікати{ </label> }`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `посередницькі сертифікати.{ </label> }`
    - The en-US sentence ends with a period before </label>. The Ukrainian leaves it out, although the first sentence in the same string keeps its period.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/uk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
