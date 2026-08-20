# Firefox l10n QA — en-CA

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `fef20cd7efc2` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `b95608d528c8` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,115 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.



---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (9)

- `newtab-picture-attribution-license` — `browser/browser/newtab/newtab.ftl` — Noun "license" left in the en-US spelling while the locale consistently uses "licence" for the noun elsewhere.
  - Current: `View the { $license } license`
  - Source: `aria-label: View the { $license } license`
  - Suggest: `View the { $license } licence`
  - en-CA uses the noun/verb split: this tree has "Mozilla Public Licence" and "licences" (toolkit/toolkit/about/aboutRights.ftl), "Licence information" (toolkit/toolkit/about/aboutAddons.ftl, aboutPlugins.ftl) and "Licence Agreement" / "licence agreement" (browser/installer/override.properties). Here "license" is a noun (the picture's licence), so it should follow the same adaptation.
- `media-file-size` — `browser/browser/pageInfo.ftl` — The kilobyte abbreviation is written "kB" here but "KB" in properties-general-size a few lines above in the same file, so the Page Info dialog shows two different spellings of the same unit.
  - Current: `media-file-size = { $size } kB`
  - Source: `{ $size } KB`
  - Suggest: `media-file-size = { $size } KB`
  - en-US uses "KB" in both strings; en-CA changed only this one. Within pageInfo.ftl, properties-general-size still reads "{ $kb } KB ({ $bytes } bytes)", so the same dialog displays both "KB" and "kB". No en-CA convention requires "kB" (the tree is mixed: toolkit/toolkit/about/aboutPerformance.ftl and aboutProcesses.ftl use "KB"), so the file-internal inconsistency is the defect.
- `fontinspector.fontLicense` — `devtools/client/font-inspector.properties` — Noun "License" left in the en-US spelling; this locale consistently uses "Licence" for the noun.
  - Current: `fontinspector.fontLicense = License:`
  - Source: `License:`
  - Suggest: `fontinspector.fontLicense = Licence:`
  - en-CA distinguishes the noun "licence" from the verb "license", and the tree does this consistently: "Licence information" (toolkit/toolkit/about/aboutPlugins.ftl, toolkit/toolkit/about/aboutAddons.ftl), "Licence Agreement"/"licence agreement" (browser/installer/override.properties), "Mozilla Public Licence" and "open source licences" (toolkit/toolkit/about/aboutRights.ftl). This label is the fon…
- `fontinspector.fontLicenseInfoUrl` — `devtools/client/font-inspector.properties` — Noun "License" left in the en-US spelling in the licence-URL label.
  - Current: `fontinspector.fontLicenseInfoUrl = License Info URL:`
  - Source: `License Info URL:`
  - Suggest: `fontinspector.fontLicenseInfoUrl = Licence Info URL:`
  - Same rule as fontinspector.fontLicense: the locale uses the noun "licence" throughout (aboutPlugins.ftl, aboutAddons.ftl, aboutRights.ftl, browser/installer/override.properties), so this attributive noun should read "Licence".
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — The opening curly quote before the coordinate format was replaced with a closing curly quote, leaving a mismatched quote pair.
  - Current: `”left,top,right,bottom”`
  - Source: `The “coords” attribute of the <area shape="rect"> tag is not in the “left,top,right,bottom” format.`
  - Suggest: `“left,top,right,bottom”`
  - Every other quoted literal in this string and in the neighbouring ImageMap* strings uses the “…” pair; here the opening mark is U+201D (right double quotation mark) instead of U+201C, so the quoted format string renders with two closing quotes. This is damage introduced by the locale's quote substitution, not a variant convention.
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — The XML technical term "prolog" was changed to "prologue", which is not the name of the XML construct and contradicts the same term left as "prolog" in the adjacent string.
  - Current: `outside the prologue any longer`
  - Source: `<?%1$S?> processing instruction does not have any effect outside the prolog anymore (see bug 360119).`
  - Suggest: `outside the prolog any longer`
  - "Prolog" here is the XML specification's term for the part of a document before the root element (the string ID is PINotInProlog). "Prologue" is the ordinary-English word and does not name this construct; en-CA also keeps "prolog" in PINotInProlog2 on the next line, so the tree is internally inconsistent. This is an over-correction inside a technical term, not a spelling variant.
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — "Color Scheme Auto" keeps the en-US spelling while the three sibling strings in the same file use "Colour Scheme".
  - Current: `Color Scheme Auto`
  - Source: `(value): Auto title: Color Scheme Auto`
  - Suggest: `Colour Scheme Auto`
  - about-reader-color-scheme-light/dark/sepia all read "Colour Scheme …", and every other UI string in the tree that contains this word uses "Colour" (printUI, containers, colors.ftl, newtab, pdfviewer). The only exceptions are the brand name "Firefox Color", so this lone "Color" is an inconsistent adaptation.
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — `about-reader-color-scheme-auto` still uses the en-US form “color”
  - Current: `(value): Auto title: Color Scheme Auto`
  - Suggest: `colour`
  - This locale writes “colour” for “color” in 68 other strings and keeps “color” in 5. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `download-utils-kilobyte` — `toolkit/toolkit/downloads/downloadUtils.ftl` — The kilobyte unit is rendered "kB" here while the rest of the locale's size UI (including pdfviewer in this same partition) uses "KB".
  - Current: `download-utils-kilobyte = kB`
  - Source: `KB`
  - Suggest: `download-utils-kilobyte = KB`
  - en-US has "KB" here, and en-CA keeps "KB" in toolkit/toolkit/pdfviewer/viewer.ftl (pdfjs-document-properties-size-kb), toolkit/toolkit/about/aboutProcesses.ftl (memory-unit-KB), aboutPerformance.ftl (size-KB) and aboutNetworking.ftl. en-CA has no distinct convention requiring the SI "kB" form, so the download panel showing "1.1 of 11.1 kB" is out of step with "111 KB" shown elsewhere in the same…

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
| Missing strings | 48 |
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

**48 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/sidebar.ftl` — 5
- `browser/browser/preferences/preferences.ftl` — 5
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `browser/browser/appmenu.ftl` — 3
- `browser/browser/ipProtection.ftl` — 2
- `devtools/client/debugger.properties` — 2
- `browser/browser/profiles.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `toolkit/toolkit/about/aboutPDF.ftl` — 1
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1

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
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `document_properties_kb` — `browser/pdfviewer/viewer.properties` — PDF viewer file-size unit written "kB" here but "KB" in the identical Fluent-migrated string elsewhere in the locale, and inconsistent with the adjacent "MB" line.
  - Current: `{{size_kb}} kB ({{size_b}} bytes)`
  - Source: `{{size_kb}} KB ({{size_b}} bytes)`
  - Suggest: `{{size_kb}} KB ({{size_b}} bytes)`
  - The same PDF viewer document-properties string in toolkit/toolkit/pdfviewer/viewer.ftl:110 reads "{ NUMBER($kb, …) } KB ({ $b } bytes)", and the next entry here (document_properties_mb) uses the upper-case "MB". en-CA has no convention requiring lower-case "k"; browser/browser/pageInfo.ftl also uses "KB" for the same kind of file-size display. Using "kB" only in this one copy makes the same UI st…

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

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (9)

- `newtab-picture-attribution-license` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-20
- `media-file-size` — `browser/browser/pageInfo.ftl` — fixed 2026-08-20
- `fontinspector.fontLicense` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `fontinspector.fontLicenseInfoUrl` — `devtools/client/font-inspector.properties` — fixed 2026-08-20
- `ImageMapRectBoundsError` — `dom/chrome/layout/layout_errors.properties` — fixed 2026-08-20
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — fixed 2026-08-20
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-20
- `about-reader-color-scheme-auto` — `toolkit/toolkit/about/aboutReader.ftl` — fixed 2026-08-20
- `download-utils-kilobyte` — `toolkit/toolkit/downloads/downloadUtils.ftl` — fixed 2026-08-20
