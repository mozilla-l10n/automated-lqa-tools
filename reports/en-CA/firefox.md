# Firefox l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f2e9b7fce093` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `37560db2354a` |
| **Previous run** | 2026-08-21 @ `a9b9a116b725` |
| **Mode** | incremental |
| **Strings reviewed this run** | 33 of 18,115 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for en-CA: [android](android.md)

---

## Changes in this run

### 🆕 New findings (3)

- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — The quoted format literal is mangled: "left,top,right,bottom" became "”“eft,top,right,bottom".
    - Current: `”“eft,top,right,bottom”`
    - Source: `The “coords” attribute of the <area shape="rect"> tag is not in the “left,top,right,bottom” format.`
    - Suggest: `“left,top,right,bottom”`
    - The en-US source names the literal attribute format "left,top,right,bottom"; the target lost the initial "l" and has stray/reversed quote marks, making the message wrong and unreadable.
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — "anymore" was needlessly reworded to "any longer", a change not required by en-CA.
    - Current: `does not have any effect outside the prolog any longer`
    - Source: `<?%1$S?> processing instruction does not have any effect outside the prolog anymore (see bug 360119).`
    - Suggest: `does not have any effect outside the prolog anymore`
    - en-CA does not differ from en-US here; the substitution is an unnecessary divergence from the source wording.
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — Only the title was adapted to "Colour" while the related value remains inconsistent; "Color Scheme" here refers to the UI feature name shown alongside untouched sibling labels.
    - Current: `title: Colour Scheme Auto`
    - Source: `(value): Auto title: Color Scheme Auto`
    - Suggest: `title: Color Scheme Auto`
    - Reader Mode's colour-scheme labels are inconsistent if only this one is adapted; the en-US term is used for the same control elsewhere in the file.

### ✅ Fixed since the last run (2)

- `PINotInProlog` — `dom/chrome/layout/xul.properties` — "anymore" was needlessly reworded to "any longer", a change not required by en-CA.
    - Current: `does not have any effect outside the prolog any longer`
    - Source: `<?%1$S?> processing instruction does not have any effect outside the prolog anymore (see bug 360119).`
    - Suggest: `does not have any effect outside the prolog anymore`
    - en-CA does not differ from en-US here; the substitution is an unnecessary divergence from the source wording.
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — Only the title was adapted to "Colour" while the related value remains inconsistent; "Color Scheme" here refers to the UI feature name shown alongside untouched sibling labels.
    - Current: `title: Colour Scheme Auto`
    - Source: `(value): Auto title: Color Scheme Auto`
    - Suggest: `title: Color Scheme Auto`
    - Reader Mode's colour-scheme labels are inconsistent if only this one is adapted; the en-US term is used for the same control elsewhere in the file.

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
| Files | 360 |
| Strings | 18,115 |
| Missing strings | 58 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 1 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**58 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 16
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 7
- `browser/browser/appmenu.ftl` — 5
- `browser/browser/sidebar.ftl` — 5
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `browser/browser/ipProtection.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/preferences/formAutofill.ftl` — 2
- `devtools/client/debugger.properties` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/profiles.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 756, `curly-single` 68, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1115, `straight` 4 | **typographic** |
| ellipsis | `char` 460 | **char** |
| dash | `em` 109, `en` 3 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (4)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 2 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — The quoted format literal is mangled: "left,top,right,bottom" became "”“eft,top,right,bottom".
    - Current: `”“eft,top,right,bottom”`
    - Source: `The “coords” attribute of the <area shape="rect"> tag is not in the “left,top,right,bottom” format.`
    - Suggest: `“left,top,right,bottom”`
    - The en-US source names the literal attribute format "left,top,right,bottom"; the target lost the initial "l" and has stray/reversed quote marks, making the message wrong and unreadable.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — `recommended-theme-1` still uses the en-US form “color”
    - Current: `Feeling creative? <a data-l10n-name="link">Build your own theme with Firefox Color.</a>`
    - Suggest: `colour`
    - This locale writes “colour” for “color” in 69 other strings and keeps “color” in 4. This string is byte-identical to en-US, so the substitution looks simply to have been missed.

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `Kilo` — `browser/installer/override.properties` — The NSIS kilobyte unit prefix was changed from "K" to "k", a change no en-CA convention calls for.
    - Current: `Kilo = k`
    - Source: `K`
    - Suggest: `Kilo = K`
    - This value is concatenated by NSIS into the byte-size readout (e.g. "1.5 KB"); the sibling values Byte/Mega/Giga were left as B/M/G. Canadian English has no convention that requires lowercasing this symbol, so the single-letter change is an unnecessary deviation from the source.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name of the licence document "Mozilla Public License" has been respelled as "Mozilla Public Licence".
    - Current: `Mozilla Public Licence`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `Mozilla Public License`
    - "Mozilla Public License" is the official title of a specific legal document (as used in the MPL header of every file in this tree, including this one); the -ce/-se spelling rule for the common noun does not apply to a proper name. Both occurrences in the string are affected, including the linked <a data-l10n-name="mozilla-public-license-link"> text.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/en-CA/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (10)

- `document_properties_kb` — `browser/pdfviewer/viewer.properties` — fixed 2026-08-21
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — fixed 2026-08-21
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-21
- `newtab-picture-attribution-license` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-20
- `media-file-size` — `browser/browser/pageInfo.ftl` — fixed 2026-08-20
- `fontinspector.fontLicense` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `fontinspector.fontLicenseInfoUrl` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — fixed 2026-08-20
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-20
- `download-utils-kilobyte` — `toolkit/toolkit/downloads/downloadUtils.ftl` — fixed 2026-08-20
