# Focus for Android l10n QA — sv-SE

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

Also for sv-SE: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `straight-double` 9, `curly-double` 6 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (5)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `preference_privacy_should_block_cookies_cross_site_option` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — "Cross-site cookies" is rendered as "globala kakor" (global cookies), which names the wrong thing.
    - Current: `globala kakor`
    - Source: `Block cross-site cookies`
    - Suggest: `kakor mellan webbplatser`
    - The source says cross-site, meaning cookies shared between different sites, not 'global' cookies. Firefox sv-SE elsewhere uses 'mellan webbplatser'.

### C. Grammar, agreement & spelling

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — Ungrammatical phrase: "för" is missing before "att" in the purpose clause.
    - Current: `uppdatera inställningar att tillåta trackers`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `uppdatera inställningar för att tillåta spårare`
    - 'update settings to allow trackers' needs 'för att' in Swedish. 'uppdatera inställningar att tillåta' is ungrammatical.
- `onboarding_first_screen_terms_of_use_link_2` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The link text is in the indefinite form but is inserted into a sentence that needs the definite form.
    - Current: `användarvillkor för Firefox`
    - Source: `Firefox Terms of Use`
    - Suggest: `användarvillkoren för Firefox`
    - This link is substituted into 'Genom att fortsätta godkänner du %1$s.', which gives 'godkänner du användarvillkor för Firefox'. The source refers to the specific Firefox Terms of Use ('agree to the Firefox Terms of Use'), so Swedish needs the definite form 'användarvillkoren'.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The imperative 'Dölj' is paired with the present-tense 'blockerar', so the two verbs don't match.
    - Current: `och blockerar skärmdumpar`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `och blockera skärmdumpar`
    - The source uses two parallel imperatives ('Hide ... and block ...'), so the second verb should also be in the imperative.

### D. Terminology, register & consistency

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-sv-rSE/strings.xml` — The English word 'trackers' is used, but the same app uses 'spårare' elsewhere.
    - Current: `Blockera trackers`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Blockera spårare`
    - cfr_for_start_browsing in Focus renders trackers as 'spårare'. The About text keeps the English loanword, so the term is inconsistent within the same app.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sv-SE/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
