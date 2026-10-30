# Focus for Android l10n QA — th

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 249 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for th: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md)

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
| Strings | 249 |
| Missing strings | 1 |
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

**1 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 2 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2 | **em** |

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

- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Continuing could be risky" is rendered as "you should not continue".
    - Current: `และคุณไม่ควรดำเนินการต่อ`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `และการดำเนินการต่ออาจมีความเสี่ยง`
    - The source says continuing could be risky. The translation tells the user not to continue, which is an instruction and stronger than the original statement of possible risk.

### C. Grammar, agreement & spelling

- `onboarding_second_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Browser" is misspelled as บราวเซอร์ instead of the standard เบราว์เซอร์.
    - Current: `บราวเซอร์อื่นๆ`
    - Source: `%1$s isn’t like other browsers`
    - Suggest: `เบราว์เซอร์อื่นๆ`
    - The standard Thai spelling of "browser", which Mozilla's Thai products also use, is เบราว์เซอร์. บราวเซอร์ is a common misspelling.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — 'Unlock' is spelled ปลดล็อค here, but the summary on the same preference uses the standard spelling ปลดล็อก.
    - Current: `ปลดล็อค`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `ปลดล็อก`
    - The standard Thai spelling of 'lock' is ล็อก, and preference_security_biometric_summary2 already uses ปลดล็อก. The title and its summary appear together, so they should match.

### D. Terminology, register & consistency

- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Shortcuts" is rendered as "คำสั่งลัด", but the matching Add item uses "ทางลัด".
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Remove from Shortcuts`
    - Suggest: `ลบออกจากทางลัด`
    - menu_add_to_shortcuts and firstrun_shortcut_title both use ทางลัด for the same home-screen shortcuts feature. The Add and Remove menu items should match.
- `notification_erase_text_android_14_1` — `mozilla-mobile/focus-android/app/src/main/res/values-th/strings.xml` — "Erase browsing history" is rendered as "ลบประวัติการเรียกดู", while the title of the same notification and the rest of the app use "ล้างประวัติการท่องเว็บ".
    - Current: `ลบประวัติการเรียกดูของคุณ`
    - Source: `Tap or swipe this notification to securely erase your browsing history.`
    - Suggest: `ล้างประวัติการท่องเว็บของคุณ`
    - The notification title (notification_erase_title_android_14) and the other erase strings use ล้างประวัติการท่องเว็บ. Using a different term in the body of the same notification is inconsistent.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/th/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
