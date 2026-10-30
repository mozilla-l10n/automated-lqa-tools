# Focus for Android l10n QA — de

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

Also for de: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `german-double` 22, `curly-double` 1, `straight-double` 1 | **german-double** |
| ellipsis | `char` 22 | **char** |
| dash | `en` 6 | **en** |
| register | `formal` 658 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (7)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Search and browse right in the app" is translated as "Suchen und blättern Sie in der App", where "blättern" means paging/leafing rather than web browsing.
    - Current: `Suchen und blättern Sie in der App`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Suchen und surfen Sie direkt in der App`
    - "browse" here means browsing the web; "blättern" is the wrong sense and "right in the app" (direkt) is dropped.
- `cfr_for_start_browsing` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "as you go" is mistranslated as "bei der Gelegenheit auch noch", which changes the meaning.
    - Current: `und wir blockieren Tracker und bei der Gelegenheit auch noch andere schädliche Elemente`
    - Source: `Start your private browsing session, and we’ll block trackers and other bad stuff as you go.`
    - Suggest: `und wir blockieren dabei Tracker und andere schädliche Elemente`
    - The source says trackers and other bad stuff are blocked as you browse; the German implies blocking other bad stuff is a casual side effect ("bei der Gelegenheit auch noch"), which is not the source meaning.
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — The modal "may" of "Pages may load faster" is dropped, turning a possibility into a statement of fact.
    - Current: `Seiten laden schneller, verhalten sich aber möglicherweise unerwartet`
    - Source: `Pages may load faster, but may also behave unexpectedly`
    - Suggest: `Seiten laden möglicherweise schneller, verhalten sich aber eventuell unerwartet`
    - Source says "Pages may load faster"; the German asserts they do load faster.
- `preference_privacy_block_content_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Enabling" is not rendered; the German says "This can cause…" without the condition of activating the setting.
    - Current: `Dies kann dazu führen, dass manche Seiten sich ungewöhnlich verhalten`
    - Source: `Enabling may cause some pages to behave unexpectedly`
    - Suggest: `Das Aktivieren kann dazu führen, dass sich manche Seiten unerwartet verhalten`
    - The source conditions the warning on enabling the option; the translation drops that.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — "Regulation" (EU) 2024/1183 is a Verordnung, not a Richtlinie (directive).
    - Current: `Qualifiziert im Sinne der Richtlinie (EU) 2024/1183.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Qualifiziert im Sinne der Verordnung (EU) 2024/1183.`
    - EU legal terminology: "Regulation" = "Verordnung"; "Richtlinie" would be "Directive", naming the wrong legal instrument.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Misspelling of "Aussteller" as "Austeller".
    - Current: `das Zertifikat vom Austeller selbst signiert wurde`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `das Zertifikat vom Aussteller selbst signiert wurde`
    - "Austeller" is a typo; the correct German spelling is "Aussteller", as used earlier in the same string ("der Aussteller des Zertifikats").

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `menu_open_with_a_browser2` — `mozilla-mobile/focus-android/app/src/main/res/values-de/strings.xml` — Missing space before the ellipsis, inconsistent with the German convention used in menu_share ("Teilen …").
    - Current: `Öffnen in…`
    - Source: `Open in…`
    - Suggest: `Öffnen in …`
    - German typography (and the sibling string menu_share) places a space before the ellipsis character.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/de/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
