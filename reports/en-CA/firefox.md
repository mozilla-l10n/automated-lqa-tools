# Firefox l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `4f181c236f19` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `aadbf7c9bb44` |
| **Previous run** | 2026-11-16 @ `d1d139c060cf` |
| **Mode** | incremental |
| **Strings reviewed this run** | 317 of 17,154 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-CA: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (1)

- `main-context-menu-open-link-split-view-2` — `browser/browser/browserContext.ftl` — Access key `M` of `main-context-menu-open-link-split-view-2` is not present in its label
    - Current: `M`
    - The label is “Open in Split View”. An access key not in the label cannot be underlined and is unreachable by keyboard.

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
| Files | 337 |
| Strings | 17,154 |
| Missing strings | 0 |
| Obsolete strings | 26 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 1 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 1 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Files with no en-US counterpart

- `browser/browser/windowLock.ftl`

_8 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 699, `curly-single` 64, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1058, `straight` 4 | **typographic** |
| ellipsis | `char` 411 | **char** |
| dash | `em` 84, `en` 3 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `main-context-menu-open-link-split-view-2` — `browser/browser/browserContext.ftl` — Access key `M` of `main-context-menu-open-link-split-view-2` is not present in its label
    - Current: `M`
    - The label is “Open in Split View”. An access key not in the label cannot be underlined and is unreachable by keyboard.

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

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/en-CA/dismissed.txt` brings the finding back now._

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
