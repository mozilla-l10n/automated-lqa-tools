# Focus for Android l10n QA — fi

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

Also for fi: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 9, `straight-double` 7 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `en` 3 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (8)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The second sentence changes 'You don't need to open the app or see what's running in your browser' into 'you don't need to open the app to see the information from your browser'.
    - Current: `Sinun ei tarvitse avata sovellusta nähdäksesi tiedot selaimestasi.`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Sinun ei tarvitse avata sovellusta tai nähdä, mitä selaimessasi on auki.`
    - The source lists two things the user doesn't need to do: open the app, or see what's running in the browser. The Finnish makes 'see' a purpose clause ('to see the information from your browser'), so it suggests the notification shows browser data without opening the app. That is not what the source says.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The plural "custom URLs" is translated as the singular "mukautettu osoite".
    - Current: `Poista mukautettu osoite`
    - Source: `Remove custom URLs`
    - Suggest: `Poista mukautetut osoitteet`
    - The source title is "Remove custom URLs" (plural). The screen lets the user select and remove several URLs, as the matching content description "delete all selected custom autocomplete URLs" shows. The Finnish says only one address is removed.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The Finnish says "Block all cookies", but the source only says "Block cookies".
    - Current: `Estä kaikki evästeet`
    - Source: `Block cookies`
    - Suggest: `Estä evästeet`
    - The source "Block cookies" doesn't say "all". This setting has options (e.g. blocking third-party cookies only), so adding "kaikki" (all) suggests every cookie gets blocked, which is wrong.
- `preference_search_remove_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — Plural 'search engines' rendered as singular 'hakukone'.
    - Current: `Poista hakukone`
    - Source: `Remove search engines`
    - Suggest: `Poista hakukoneita`
    - Source title is 'Remove search engines' (plural, a screen for removing engines from the list); Finnish says 'Remove search engine'.

### C. Grammar, agreement & spelling

- `contextmenu_erased_images_note2` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The comma before the subordinate clause starting with 'kun' is missing.
    - Current: `{ </b> } kun`
    - Source: `Saved and shared images { <b> }will not be{ </b> } deleted when you erase %1$s history`
    - Suggest: `{ </b> }, kun`
    - Finnish punctuation rules require a comma before a subordinate clause introduced by 'kun' ('ei poisteta, kun tyhjennät…').
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The object of 'käyttää' is the bare 'HTTPS' with no case ending, and the word 'connection' from the source is missing.
    - Current: `yrittää käyttää HTTPS aina kun`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `yrittää käyttää HTTPS-yhteyttä aina, kun`
    - The verb 'käyttää' needs its object in the partitive case, so an uninflected 'HTTPS' is ungrammatical. The source says 'an HTTPS connection', which is naturally 'HTTPS-yhteyttä'. Finnish also requires a comma before the 'kun' clause.

### D. Terminology, register & consistency

- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — eIDAS term 'qualified' rendered as 'kelvollinen' (valid) instead of the regulation's official Finnish term 'hyväksytty'.
    - Current: `kelvollinen`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `hyväksytty`
    - The comment explains this is the eIDAS 'qualified' certificate status; the Finnish version of the eIDAS regulation uses 'hyväksytty' (e.g. 'hyväksytty varmenne'), while 'kelvollinen' means valid/eligible.

### E. Typography, punctuation & spacing

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The full stop at the end of the mission sentence is missing before the line break.
    - Current: `avointa Internetiä{ <br/> }`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `avointa Internetiä.{ <br/> }`
    - The source sentence 'Our mission is to foster a healthy, open Internet.' ends with a period, and so do the other sentences in the Finnish text. This one runs straight into the 'Lue lisää' link without one.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
