# Focus for Android l10n QA — sk

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

Also for sk: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 8, `german-double` 7, `straight-double` 4 | _mixed_ |
| apostrophe | `straight` 2 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 4 | **en** |
| nbsp | `total` 8 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (8)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — "Your search, your way" is translated as "Browsing your way", replacing search with browsing.
    - Current: `Prehliadanie podľa vás`
    - Source: `Your search, your way`
    - Suggest: `Vyhľadávanie podľa vás`
    - The source title refers to search (this is the Search page of the first-run tour), but "Prehliadanie" means browsing, so the title is about the wrong feature.
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The Slovak drops the clause "or see what's running in your browser" and changes "session" to "history".
    - Current: `Nemusíte ani otvárať aplikáciu.`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Nemusíte otvárať aplikáciu ani vidieť, čo je spustené vo vašom prehliadači.`
    - The source says the user does not need to open the app or see what is running in the browser. The translation keeps only the first part, so content that conveys the discreet-erase benefit is missing.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The translation leaves out "measure" and the "tapping" example from the source.
    - Current: `na zbieranie a analýzu údajov o aktivitách, napríklad o posúvaní sa na stránke`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `na zbieranie, analýzu a meranie aktivít, ako je ťukanie a posúvanie`
    - The source says "collect, analyze and measure activities like tapping and scrolling"; the Slovak keeps only collecting/analysis and only scrolling.

### C. Grammar, agreement & spelling

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Possessive pronoun in instrumental singular is misspelled as "Našim" instead of "Naším".
    - Current: `Našim poslaním`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Naším poslaním`
    - Instrumental singular of "náš" is "naším" (long í); "našim" is the dative plural form.
- `preference_privacy_block_ads_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Missing comma before the subordinate clause "aj keď".
    - Current: `Niektoré reklamy vás sledujú aj keď na ne nekliknete`
    - Source: `Some ads track site visits, even if you don’t click the ads`
    - Suggest: `Niektoré reklamy vás sledujú, aj keď na ne nekliknete`
    - Slovak punctuation rules require a comma before the conjunction "aj keď" that introduces a subordinate clause.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — Genitive plural 'aplikácii' is misspelled; it should be 'aplikácií'.
    - Current: `nedávnych aplikácii`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `nedávnych aplikácií`
    - The genitive plural after 'nedávnych' needs the long í ending, so it is 'aplikácií'.
- `promote_search_widget_button_text` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — The button label uses the third-person 'Pridá' ('it adds') instead of the infinitive used for actions.
    - Current: `Pridá miniaplikáciu`
    - Source: `Add widget to home screen`
    - Suggest: `Pridať miniaplikáciu`
    - This is a button label for an action. Slovak UI uses the infinitive for actions, as in other strings here ('Pridať ďalší vyhľadávací modul').

### D. Terminology, register & consistency

- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-sk/strings.xml` — This string writes "súbory cookies", but the cookie options right next to it write "súbory cookie".
    - Current: `súbory cookies`
    - Source: `Block cookies`
    - Suggest: `súbory cookie`
    - The three cookie options under this heading all use "súbory cookie", which is the usual Slovak form. Only the category title uses the plural "cookies", so the same term appears two ways on one screen.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
