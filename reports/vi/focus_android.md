# Focus for Android l10n QA — vi

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

Also for vi: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 13, `straight-double` 2 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (8)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — The Vietnamese drops "strives to", so an effort becomes a flat statement that Mozilla collects only what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần cung cấp`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần để cung cấp`
    - The source says Mozilla strives to collect only what it needs. The Vietnamese leaves out the effort and states it as fact, which changes how certain the claim about data collection is.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — "produced by Mozilla" is translated as "founded by Mozilla" (được sáng lập bởi).
    - Current: `được sáng lập bởi Mozilla`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `được phát triển bởi Mozilla`
    - "sáng lập" means to found an organisation, not to make a product. The source says Focus is produced (made) by Mozilla.
- `cfr_for_toolbar_delete_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — "start fresh" is rendered as "bắt đầu làm mới", which reads as "start refreshing".
    - Current: `bắt đầu làm mới trên một thẻ mới`
    - Source: `Tap here to trash it all — history, cookies, everything — and start fresh on a new tab.`
    - Suggest: `bắt đầu lại từ đầu trên một thẻ mới`
    - In browser UI, "làm mới" is the usual term for refresh/reload. The source means starting over with a clean slate in a new tab, not refreshing anything.
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — The general "tries to use" is rendered in the past tense as "đã thử" ("tried").
    - Current: `%1$s đã thử kết nối HTTPS bất cứ khi nào có thể`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `%1$s luôn cố gắng sử dụng kết nối HTTPS bất cứ khi nào có thể`
    - The source describes the app's usual behaviour ("whenever possible"), not a single attempt in the past. A past-tense verb clashes with "bất cứ khi nào có thể" ("whenever possible").
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — The Vietnamese drops "strives to", so an effort becomes a flat statement that Mozilla collects only what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần cung cấp`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần để cung cấp`
    - The source says Mozilla strives to collect only what it needs. The Vietnamese leaves out the effort and states it as fact, which changes how certain the claim about data collection is.
- `preference_phone_feature_media_key_system_access` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — "Nội dung DRM được kiểm soát" reads as "controlled DRM content", not "content controlled by DRM".
    - Current: `Nội dung DRM được kiểm soát`
    - Source: `DRM-controlled content`
    - Suggest: `Nội dung được kiểm soát bằng DRM`
    - The source means content that DRM controls (EME access). The Vietnamese word order makes "được kiểm soát" describe DRM content, which changes the meaning.

### C. Grammar, agreement & spelling

- `onboarding_second_screen_subtitle_two` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — Typo "trifnh" instead of "trình" in "trình duyệt".
    - Current: `trifnh duyệt`
    - Source: `Make %1$s your default to protect your data with every link you open.`
    - Suggest: `trình duyệt`
    - "trifnh" is not a Vietnamese word. It is a Telex input slip for "trình" (browser = "trình duyệt").
- `preference_search_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — Misspelling: "tự đồng điền" should be "tự động điền" (autocomplete).
    - Current: `tự đồng điền`
    - Source: `Set default, autocomplete`
    - Suggest: `tự động điền`
    - "đồng" is a typo for "động"; the term for autocomplete is "tự động điền".
- `preference_subitem_autocomplete` — `mozilla-mobile/focus-android/app/src/main/res/values-vi/strings.xml` — Word order makes it mean "a URL that autofills" instead of the feature that autocompletes URLs.
    - Current: `URL tự động điền`
    - Source: `URL Autocomplete`
    - Suggest: `Tự động điền URL`
    - Vietnamese puts the head word first, so "URL tự động điền" describes a kind of URL. The setting is the URL autocomplete feature, which is "Tự động điền URL".

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/vi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
