# Firefox l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-11-08 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `363d50704369` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-05 @ `324a294b9f2a` |
| **Mode** | incremental |
| **Strings reviewed this run** | 3 of 16,754 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-CA: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 331 |
| Strings | 16,754 |
| Missing strings | 121 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 1 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**121 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/onboarding.ftl` — 22
- `toolkit/toolkit/about/aboutProcesses.ftl` — 19
- `browser/browser/tabContextMenu.ftl` — 14
- `browser/browser/appExtensionFields.ftl` — 11
- `browser/browser/newtab/newtab.ftl` — 11
- `toolkit/toolkit/downloads/downloadUI.ftl` — 10
- `browser/browser/contextual-manager.ftl` — 8
- `browser/browser/preferences/preferences.ftl` — 5
- `browser/browser/browser.ftl` — 4
- `browser/browser/tabbrowser.ftl` — 3
- `dom/chrome/dom/dom.properties` — 3
- `browser/browser/genai.ftl` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 699, `curly-single` 64, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1010, `straight` 4 | **typographic** |
| ellipsis | `char` 400 | **char** |
| dash | `em` 84, `en` 3 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

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

### Dismissed by hand (1)

- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Firefox Color is the same of the feature

_One line each in `locales/en-CA/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (15)

- `urlbar-searchmode-dropmarker2` — `browser/browser/browser.ftl` — fixed 2026-09-14
- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — fixed 2026-08-24
- `Kilo` — `browser/installer/override.properties` — fixed 2026-08-21
- `document_properties_kb` — `browser/pdfviewer/viewer.properties` — fixed 2026-08-21
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — fixed 2026-08-21
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — fixed 2026-08-21
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — fixed 2026-08-21
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-21
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-21
- `newtab-picture-attribution-license` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-20
- `media-file-size` — `browser/browser/pageInfo.ftl` — fixed 2026-08-20
- `fontinspector.fontLicense` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `fontinspector.fontLicenseInfoUrl` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-20
- `download-utils-kilobyte` — `toolkit/toolkit/downloads/downloadUtils.ftl` — fixed 2026-08-20
