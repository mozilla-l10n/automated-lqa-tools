# Firefox l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `4f181c236f19` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `aadbf7c9bb44` |
| **Previous run** | 2026-11-16 @ `d1d139c060cf` |
| **Mode** | incremental |
| **Strings reviewed this run** | 245 of 16,251 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (11)

- `reg-app-desc` — `browser/installer/custom.ftl` — The aside is set off with hyphens; the locale uses the en dash for this.
    - Current: `okrepljene varnostne možnosti - vključno z zaščito pred spletno krajo identitete - in`
    - Source: `{ $BrandShortName } delivers safe, easy web browsing. A familiar user interface, enhanced security features including protection from online identity theft, and integrated search let you get the most out of the web.`
    - Suggest: `okrepljene varnostne možnosti – vključno z zaščito pred spletno krajo identitete – in`
    - The sl conventions use the en dash (150 vs 13 em) for dashes. A spaced hyphen marking off an aside breaks that convention.
- `warn-min-supported-osver-cpu-msg` — `browser/installer/custom.ftl` — Brand name is not declined in the genitive after "različica".
    - Current: `Ta različica { $BrandShortName } zahteva`
    - Source: `Sorry, { $BrandShortName } can’t be installed. This version of { $BrandShortName } requires { $MinSupportedVer } or newer and a processor with { $MinSupportedCPU } support. Please click the OK button for additional info…`
    - Suggest: `Ta različica { $BrandShortName }a zahteva`
    - "Ta različica" needs the genitive form of the brand name. The sibling strings warn-min-supported-osver-msg and warn-min-supported-cpu-msg correctly use "{ $BrandShortName }a".
- `warn-restart-required-upgrade` — `browser/installer/custom.ftl` — Double space after the comma.
    - Current: `{ $BrandShortName },  morate`
    - Source: `Your computer must be restarted to complete a previous upgrade of { $BrandShortName }. Do you want to reboot now?`
    - Suggest: `{ $BrandShortName }, morate`
    - There are two spaces between words in the text the user reads.
- `banner-check-existing` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `namestitve ...`
    - Source: `Checking existing installation…`
    - Suggest: `namestitve …`
    - The locale convention is the single ellipsis character (420 vs 40), and en-US uses … with no space.
- `status-install-app` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `{ $BrandShortName } ...`
    - Source: `Installing { $BrandShortName }…`
    - Suggest: `{ $BrandShortName } …`
    - The locale convention is the single ellipsis character.
- `status-uninstall-main` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `{ $BrandShortName } ...`
    - Source: `Uninstalling { $BrandShortName }…`
    - Suggest: `{ $BrandShortName } …`
    - The locale convention is the single ellipsis character.
- `status-cleanup` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `urejanje ...`
    - Source: `A Little Housekeeping…`
    - Suggest: `urejanje …`
    - The locale convention is the single ellipsis character.
- `mui-untext-confirm-title` — `browser/installer/mui.ftl` — The brand name follows the noun "Odstranjevanje" without being declined and without a governing noun, which is ungrammatical.
    - Current: `Odstranjevanje { $BrandFullNameDA }`
    - Source: `Uninstall { $BrandFullNameDA }`
    - Suggest: `Odstranjevanje programa { $BrandFullNameDA }`
    - After a verbal noun, Slovenian needs the genitive. The name can't be declined here, so the sibling strings put "programa" before it (e.g. "Zaključevanje odstranjevanja programa { $BrandFullNameDA }"). This title leaves the name as a bare nominative with no governing noun.
- `nsis-browse-btn` — `browser/installer/override.ftl` — The label uses three ASCII dots with a space before them instead of the ellipsis character the locale uses by convention.
    - Current: `Prebrskaj ...`
    - Source: `(value): Browse… accesskey: r`
    - Suggest: `Prebrskaj …`
    - The en-US uses the ellipsis character (…), and the sl convention is the ellipsis character (420 against 40 uses of three dots). The space before it is also non-standard.
- `nsis-file-error-no-ignore` — `browser/installer/override.ftl` — There are two spaces between "če" and "želite" in text the user sees.
    - Current: `če  želite`
    - Source: `Error opening file for writing:  { $FilePath }  Click Retry to try again, or Cancel to stop the installation.`
    - Suggest: `če želite`
    - The extra space appears in the dialog text the user reads. The sister string nsis-file-error uses a single space in the same phrase.
- `dialog-button-revert` — `toolkit/toolkit/global/dialog.ftl` — "Revert" is translated as "Obrni" (turn/flip over) instead of a word meaning restore to the previous state.
    - Current: `Obrni`
    - Source: `accesskey: R label: Revert`
    - Suggest: `Povrni`
    - en-US "Revert" means going back to the previous saved state. "Obrni" means turn, flip or reverse direction, so the button label says the wrong thing. "Povrni" is the usual Slovenian word for revert/restore. The access key will need updating to match.

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
| Files | 335 |
| Strings | 16,251 |
| Missing strings | 869 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 28 |

### Completeness

**869 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 156
- `browser/browser/ipProtection.ftl` — 91
- `browser/browser/aiWindowContent.ftl` — 61
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 54
- `dom/chrome/dom/dom.properties` — 53
- `browser/browser/preferences/preferences.ftl` — 46
- `browser/browser/newtab/newtab.ftl` — 45
- `browser/browser/aiFeatures.ftl` — 33
- `dom/chrome/security/security.properties` — 30
- `toolkit/toolkit/about/aboutProcesses.ftl` — 30
- `browser/browser/newtab/onboarding.ftl` — 25
- `browser/browser/genai.ftl` — 20

**Files absent from the locale:**

- `browser/browser/autoTabGrouping.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 268, `straight-double` 264, `curly-single` 50, `guillemet` 5 | _mixed_ |
| apostrophe | `typographic` 50, `straight` 51 | _mixed_ |
| ellipsis | `char` 369, `ascii` 38 | **char** |
| dash | `em` 15, `en` 120 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 8 | _mixed_ |
| register | `informal` 8, `formal` 542 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 28 strings** — 28 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `about-debugging-sidebar-runtime-item-waiting-for-browser`, `about-logins-menu-menuitem-export-logins2`, `browser-languages-downloading`, `browser-languages-search`, `browser-languages-searching`, `choose-other-app-window-title`, `crashreporter-button-details`, `crashreporter-resubmit-status`, `diffing.state.taking-diff`, `diffing.state.taking-diff.full`, `fxa-menu-send-tab-to-device-syncnotready`, `home-homepage-custom-url` …and 16 more

---

## 3. Open findings (21)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 4 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 10 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — The purpose clause is mistranslated so that the sentence reads "To improve the { -brand-product-name } browser" and merges the subject, changing which product is being improved and who sends the data.
    - Current: `Za izboljšanje brskalnika { -brand-product-name } { -vendor-short-name } pošilja diagnostične podatke in podatke o uporabi.`
    - Source: `By continuing, you agree to the <a data-l10n-name="terms_of_use">{ -brand-product-name } Terms of Use</a> and our <a data-l10n-name="privacy_notice">Privacy Notice</a>. To help improve the browser, { -brand-product-name…`
    - Suggest: `Za izboljšanje brskalnika { -brand-product-name } pošilja { -vendor-short-name } diagnostične podatke in podatke o uporabi.`
    - In en-US the subject is { -brand-product-name } which sends data to { -vendor-short-name }; the Slovenian makes { -vendor-short-name } the sender and attaches the brand name to "brskalnika", reversing the roles and dropping the recipient.
- `speech-recognition-model-download-message` — `browser/browser/permissions.ftl` — The Slovenian drops "when you continue" and mangles "the audio never leaves your device" into a relative clause saying the device never leaves the audio.
    - Current: `V { -brand-short-name } prepoznavanje govora poteka na napravi, ki je zvok v nobenem trenutku ne zapusti. V ta namen bo na napravo preneslo ~{ $sizeMB } MB podatkov.`
    - Source: `{ -brand-short-name } runs speech recognition locally, so the audio never leaves your device. To set this up, a ~{ $sizeMB } MB download will start when you continue.`
    - Suggest: `V { -brand-short-name } prepoznavanje govora poteka krajevno, zato zvok nikoli ne zapusti vaše naprave. Za nastavitev se bo ob nadaljevanju začel prenos velikosti ~{ $sizeMB } MB.`
    - The en-US says the download will start when you continue; the target states it will simply be downloaded, omitting the condition, and the second sentence also lacks a subject ("bo na napravo preneslo").
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — "Podvoji zavihke" is the command "duplicate tabs", but the item names the duplicate tabs that the Close Multiple submenu will close.
    - Current: `Podvoji zavihke`
    - Source: `accesskey: x label: Duplicate Tabs`
    - Suggest: `Podvojene zavihke`
    - The developer comment says this label sits under "Close Multiple" and closes all duplicate tabs. The Slovenian imperative tells the user it will create duplicates, so the menu says the opposite of what it does.
- `options-stylesheets-in-the-debugger-tooltip` — `devtools/client/toolbox-options.ftl` — Tooltip drops "and view" from "List and view stylesheets in the debugger".
    - Current: `Prikaži seznam slogovnih predlog v razhroščevalniku`
    - Source: `title: List and view stylesheets in the debugger`
    - Suggest: `Prikaži seznam slogovnih predlog in si jih oglej v razhroščevalniku`
    - The en-US says "List and view stylesheets"; the Slovenian only mentions listing them.
- `dialog-button-revert` — `toolkit/toolkit/global/dialog.ftl` — "Revert" is translated as "Obrni" (turn/flip over) instead of a word meaning restore to the previous state.
    - Current: `Obrni`
    - Source: `accesskey: R label: Revert`
    - Suggest: `Povrni`
    - en-US "Revert" means going back to the previous saved state. "Obrni" means turn, flip or reverse direction, so the button label says the wrong thing. "Povrni" is the usual Slovenian word for revert/restore. The access key will need updating to match.

### C. Grammar, agreement & spelling

- `warn-min-supported-osver-cpu-msg` — `browser/installer/custom.ftl` — Brand name is not declined in the genitive after "različica".
    - Current: `Ta različica { $BrandShortName } zahteva`
    - Source: `Sorry, { $BrandShortName } can’t be installed. This version of { $BrandShortName } requires { $MinSupportedVer } or newer and a processor with { $MinSupportedCPU } support. Please click the OK button for additional info…`
    - Suggest: `Ta različica { $BrandShortName }a zahteva`
    - "Ta različica" needs the genitive form of the brand name. The sibling strings warn-min-supported-osver-msg and warn-min-supported-cpu-msg correctly use "{ $BrandShortName }a".
- `mui-untext-confirm-title` — `browser/installer/mui.ftl` — The brand name follows the noun "Odstranjevanje" without being declined and without a governing noun, which is ungrammatical.
    - Current: `Odstranjevanje { $BrandFullNameDA }`
    - Source: `Uninstall { $BrandFullNameDA }`
    - Suggest: `Odstranjevanje programa { $BrandFullNameDA }`
    - After a verbal noun, Slovenian needs the genitive. The name can't be declined here, so the sibling strings put "programa" before it (e.g. "Zaključevanje odstranjevanja programa { $BrandFullNameDA }"). This title leaves the name as a bare nominative with no governing noun.

### D. Terminology, register & consistency

- `mini-window-overlay-instructions` — `browser/browser/miniWindow.ftl` — "Mini okno" is capitalized here, but every other string writes it as "mini okno".
    - Current: `v Mini okno`
    - Source: `Drag or click to select an area to move to a Mini Window. It’ll stay on top while you browse.`
    - Suggest: `v mini okno`
    - The other miniWindow.ftl strings (e.g. "Premakni v mini okno", "Izberite, kaj premakniti v mini okno") write the feature name in lowercase.
- `newtab-section-block-button` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
    - Source: `Block`
    - Suggest: `standardize on one verb.`
- `newtab-section-block-topic` — `browser/browser/newtab/newtab.ftl` — newtab "Block" verb — browser/browser/newtab/newtab.ftl — Inconsistent across the same feature: newtab-section-block-button etc. use "Prepovej/Prepovedano/Dovoli" while the topic strings (newtab-section-block-topic etc.) use "Blokiraj/Blokirano/Odblokiraj". → standardize on one verb.
    - Source: `aria-label: Block { $topic }`
    - Suggest: `standardize on one verb.`
- `newtab-section-follow-button` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
    - Source: `Follow`
    - Suggest: `pick one verb.`
- `newtab-section-follow-topic` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — "slediti" (newtab-section-follow-button etc.) vs "spremljati" (newtab-section-follow-topic etc.) within the same feature. → pick one verb.
    - Source: `aria-label: Follow { $topic }`
    - Suggest: `pick one verb.`

### E. Typography, punctuation & spacing

- `banner-check-existing` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `namestitve ...`
    - Source: `Checking existing installation…`
    - Suggest: `namestitve …`
    - The locale convention is the single ellipsis character (420 vs 40), and en-US uses … with no space.
- `reg-app-desc` — `browser/installer/custom.ftl` — The aside is set off with hyphens; the locale uses the en dash for this.
    - Current: `okrepljene varnostne možnosti - vključno z zaščito pred spletno krajo identitete - in`
    - Source: `{ $BrandShortName } delivers safe, easy web browsing. A familiar user interface, enhanced security features including protection from online identity theft, and integrated search let you get the most out of the web.`
    - Suggest: `okrepljene varnostne možnosti – vključno z zaščito pred spletno krajo identitete – in`
    - The sl conventions use the en dash (150 vs 13 em) for dashes. A spaced hyphen marking off an aside breaks that convention.
- `status-cleanup` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `urejanje ...`
    - Source: `A Little Housekeeping…`
    - Suggest: `urejanje …`
    - The locale convention is the single ellipsis character.
- `status-install-app` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `{ $BrandShortName } ...`
    - Source: `Installing { $BrandShortName }…`
    - Suggest: `{ $BrandShortName } …`
    - The locale convention is the single ellipsis character.
- `status-uninstall-main` — `browser/installer/custom.ftl` — Uses a space plus three ASCII dots instead of the ellipsis character.
    - Current: `{ $BrandShortName } ...`
    - Source: `Uninstalling { $BrandShortName }…`
    - Suggest: `{ $BrandShortName } …`
    - The locale convention is the single ellipsis character.
- `warn-restart-required-upgrade` — `browser/installer/custom.ftl` — Double space after the comma.
    - Current: `{ $BrandShortName },  morate`
    - Source: `Your computer must be restarted to complete a previous upgrade of { $BrandShortName }. Do you want to reboot now?`
    - Suggest: `{ $BrandShortName }, morate`
    - There are two spaces between words in the text the user reads.
- `nsis-browse-btn` — `browser/installer/override.ftl` — The label uses three ASCII dots with a space before them instead of the ellipsis character the locale uses by convention.
    - Current: `Prebrskaj ...`
    - Source: `(value): Browse… accesskey: r`
    - Suggest: `Prebrskaj …`
    - The en-US uses the ellipsis character (…), and the sl convention is the ellipsis character (420 against 40 uses of three dots). The space before it is also non-standard.
- `nsis-file-error-no-ignore` — `browser/installer/override.ftl` — There are two spaces between "če" and "želite" in text the user sees.
    - Current: `če  želite`
    - Source: `Error opening file for writing:  { $FilePath }  Click Retry to try again, or Cancel to stop the installation.`
    - Suggest: `če želite`
    - The extra space appears in the dialog text the user reads. The sister string nsis-file-error uses a single space in the same phrase.
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — btp-warning-tracker-classified ([two]) — toolkit/toolkit/global/antiTracking.ftl — Missing space before the variable: "v naslednjih{ $gracePeriodSeconds } sekundah" → "v naslednjih { $gracePeriodSeconds } sekundah" (the [few]/[other] variants have the space).
    - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
    - Suggest: `[few]`

---

## 4. Appendix

### Dismissed by hand (5)

- `appmenu-fxa-sign-in-promo-heading2` — `browser/browser/appmenu.ftl` — pontoon-rejected (2026-11-04): rejected in Pontoon without comment; reason unclear
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Sprememba na narobe. Citirani niz (backup-folder-name) je "Obnovi podatke". https://pontoon.mozilla.org/sl/firefox/browser/browser/backupSettings.ftl/?string=324818</p>
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; likely reason (inferred): The quoted text is probably a button label, and this locale's convention is that short button labels use the informal singular imperative, so "Obnovi podatke" likely matches the actual button rather than the "Obnovite podatke" header the finding compared it to.
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Ni potrebe po spreminjanju, pravilno je oboje.</p>
- `onboarding-genai-sidebar-title` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-03): rejected in Pontoon without comment; likely reason (inferred): The finding itself says both "preskusiti" and "preizkusiti" are valid and marks it low priority, so the reviewer probably saw a purely stylistic change that wasn't needed.

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (15)

- `about-pdf-feature-comments-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — auto-suggest (2026-11-09, string ee5fb1e1): unreliable finding: 'Pišite opombe' is a natural heading for the notes feature; 'Dodajte' would be a stylistic preference.
- `about-pdf-feature-presentation-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — auto-suggest (2026-11-09, string e8811c55): unreliable finding: In the about:pdf context 'dokumente' clearly means PDFs; omission is not clearly a defect.
- `newtab-recent-searches-row-remove` — `browser/browser/newtab/newtab.ftl` — auto-suggest (2026-11-03, string 2aea1636): The sl tree uses straight double quotes (259) and curly double quotes (268) about equally, so straight quotes are an accepted convention.
- `newtab-stocks-search-loading` — `browser/browser/newtab/newtab.ftl` — auto-suggest (2026-11-09, string 7b2ef640): Slovenian spelling rules put a space before an ellipsis that follows a whole word ('Nalaganje …'); this is the locale's standard.
- `options-experimental-label` — `devtools/client/toolbox-options.ftl` — auto-suggest (2026-11-09, string fae16250): unreliable finding: "Zmogljivosti" is used for "features" in Slovenian software localization; changing it is a matter of preference.
- `password-rules-email-description2` — `browser/browser/backupSettings.ftl` — auto-suggest (2026-11-09, string b5b2e01d): A predicate noun after negated 'biti' stays in the nominative ('To ni e-poštni naslov'); the genitive is only used for negated existence. The lowercase start may be on purpose.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — auto-suggest (2026-11-09, string 2fa73412): unreliable finding: The policy describes the page that opens after an update, not necessarily the menu link label, so "Kaj je novega" is plausibly acceptable.
- `refresh-reinstalled-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — auto-suggest (2026-11-09, string 0b410d55): unreliable finding: 'nameščen na novo' still conveys a reinstall; leaving out the user as the one who did it is a style choice, not a mistranslation.
- `refresh-unused-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — auto-suggest (2026-11-09, string ca644fff): unreliable finding: 'očistiti navlake' is an idiomatic way to say 'clean up' and matches what the refresh feature does; the change would be stylistic.
- `support-remote-experiments-title` — `toolkit/toolkit/about/aboutSupport.ftl` — auto-suggest (2026-11-09, string cd199e87): unreliable finding: 'Poskusi na daljavo' is an acceptable rendering of remotely delivered experiments; the alternative is a stylistic choice.
- `sync-engine-addresses` — `browser/browser/preferences/preferences.ftl` — auto-suggest (2026-11-09, string c1bd1374): unreliable finding: The sibling sync labels cannot be seen here; the accusative may follow a sentence-style pattern, so the inconsistency cannot be confirmed.
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — auto-suggest (2026-11-03, string 878a0d6f): After "glasnost" the noun is in genitive, and genitive dual and plural of zavihek are both "zavihkov" (dveh/treh zavihkov), so the forms are correct.
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — auto-suggest (2026-11-03, string 6adb9ae8): After "glasnost" the noun is in genitive, and genitive dual and plural of zavihek are both "zavihkov" (dveh/treh zavihkov); the mute string uses accusative, hence differs.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — auto-suggest (2026-11-09, string a3c02400): The quoted UI name is "lokalnega načina", which is the correctly inflected (genitive) form of the label "Lokalni način"; "z uporabo" is not inside the quotes.
- `user-context-color-violet` — `toolkit/toolkit/global/contextual-identity.ftl` — auto-suggest (2026-11-09, string a2cdbde8): unreliable finding: The feminine 'Vijolična' may be deliberate, to tell violet apart from purple ('Vijolično'), and gray is feminine too, so changing the gender would be a stylistic choice rather than fixing a confirmed error.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (2)

- **`sl-brand-case-params`** (2) — Brand terms carry a `sklon` case parameter; correct Slovenian.
    - `smartwindow-assistant-error-account-header`, `firefox-relay-must-login-to-fxa`

_Suppressions live in `locales/sl/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (2)

- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (70)

- `content-sharing-modal-generic-error-2` — `browser/browser/contentSharing.ftl` — fixed 2026-11-16
- `security-technical-weak-cipher` — `browser/browser/pageInfo.ftl` — fixed 2026-11-16
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-16
- `fonts-langgroup-kannada` — `browser/browser/preferences/fonts.ftl` — fixed 2026-11-16
- `dom-manifest-id-not-same-origin` — `dom/dom/manifest.ftl` — fixed 2026-11-16
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-11-16
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-16
- `about-pdf-feature-organize-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-16
- `touch-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-11-16
- `wheel-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-11-16
- `certificate-viewer-certificate-authority` — `toolkit/toolkit/about/certviewer.ftl` — fixed 2026-11-16
- `contentanalysis-slow-agent-dialog-body-file-and-more` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — fixed 2026-11-16
- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — fixed 2026-11-05
- `decoder-doctor-unsupported-libavcodec-message` — `browser/browser/browser.ftl` — fixed 2026-11-05
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — fixed 2026-11-05
- `newtab-wallpaper-firefox-desert-light` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `newtab-wallpaper-your-images-folder` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `privacy-metrics-cookies` — `browser/browser/protections.ftl` — fixed 2026-11-05
- `outline.placeholder.functions` — `devtools/client/debugger.properties` — fixed 2026-11-05
- `inactive-css-not-display-block-on-floated-fix` — `devtools/client/tooltips.ftl` — fixed 2026-11-05
- `network-connection-status-connecting` — `netwerk/netwerk/necko.ftl` — fixed 2026-11-05
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-11-05
- `about-networking-ssl-tokens-new` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-11-05
- `about-pdf-feature-annotate-heading` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-05
- `language-name-ti` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-11-05
- `main-context-menu-media-video-leave-fullscreen` — `browser/browser/browserContext.ftl` — fixed 2026-09-28
- `pkcs12-decode-err` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `about-logins-confirm-export-dialog-message2` — `browser/browser/aboutLogins.ftl` — fixed 2026-07-29 (undated)
- `restore-page-problem-desc` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-07-29 (undated)
- `addon-mlmodel-removal-body` — `browser/browser/addonNotifications.ftl` — fixed 2026-07-29 (undated)
- `crashed-subframe-message` — `browser/browser/contentCrash.ftl` — fixed 2026-07-29 (undated)
- `contextual-manager-export-passwords-dialog-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-07-29 (undated)
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — fixed 2026-07-29 (undated)
- `vpn-error-alert-body` — `browser/browser/ipProtection.ftl` — fixed 2026-07-29 (undated)
- `migration-wizard-migrator-display-name-file-password-csv` — `browser/browser/migrationWizard.ftl` — fixed 2026-07-29 (undated)
- `newtab-widget-lists-button-add-item` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-29 (undated)
- `policy-AIControls` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
- `policy-PopupBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-29 (undated)
