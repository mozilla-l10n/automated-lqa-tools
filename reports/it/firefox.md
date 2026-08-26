# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b82b7a344c63` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 36 of 18,403 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for it: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log/logs" rendered as "registrazione/registrazioni", inconsistent with "registro/registri" used for the same term everywhere else in this file.
    - Current: `[one] { $count } registrazione [other] { $count } registrazioni`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } registro [other] { $count } registri`
    - The rest of the file translates "log(s)" as "registro/registri" (about-sync-log-title, -clear-button, -empty-filtered); "registrazione" means a recording/entry and is inconsistent on the same surface.
- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — "No sync logs have been recorded" changed to state that no sync activity was recorded.
    - Current: `Non è stata registrata alcuna attività di sincronizzazione.`
    - Source: `No sync logs have been recorded.`
    - Suggest: `Non è stato registrato alcun registro di sincronizzazione.`
    - The source says no log files exist; the Italian asserts that no synchronization activity occurred, which is a different claim about the product's behaviour.

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
| Files | 372 |
| Strings | 18,403 |
| Missing strings | 0 |
| Obsolete strings | 6 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Files with no en-US counterpart

- `browser/branding/enterprise/brand.ftl`
- `browser/branding/enterprise/brand.properties`
- `browser/browser/enterprise/enterprise-policies-descriptions.ftl`
- `browser/browser/enterprise/enterprise.ftl`
- `browser/browser/enterprise/felt.ftl`
- `browser/chrome/overrides/enterprise.properties`
- `dom/chrome/enterprise.properties`
- `toolkit/crashreporter/crashreporter-enterprise.ftl`
- `toolkit/toolkit/enterprise/enterprise.ftl`
- `toolkit/toolkit/enterprise/felt.ftl`

_187 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 1046, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1925, `straight` 6 | **typographic** |
| ellipsis | `char` 481 | **char** |
| dash | `em` 75, `en` 18 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 761, `formal` 59 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (2)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — "No sync logs have been recorded" changed to state that no sync activity was recorded.
    - Current: `Non è stata registrata alcuna attività di sincronizzazione.`
    - Source: `No sync logs have been recorded.`
    - Suggest: `Non è stato registrato alcun registro di sincronizzazione.`
    - The source says no log files exist; the Italian asserts that no synchronization activity occurred, which is a different claim about the product's behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 1 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — "No sync logs have been recorded" changed to state that no sync activity was recorded.
    - Current: `Non è stata registrata alcuna attività di sincronizzazione.`
    - Source: `No sync logs have been recorded.`
    - Suggest: `Non è stato registrato alcun registro di sincronizzazione.`
    - The source says no log files exist; the Italian asserts that no synchronization activity occurred, which is a different claim about the product's behaviour.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log/logs" rendered as "registrazione/registrazioni", inconsistent with "registro/registri" used for the same term everywhere else in this file.
    - Current: `[one] { $count } registrazione [other] { $count } registrazioni`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } registro [other] { $count } registri`
    - The rest of the file translates "log(s)" as "registro/registri" (about-sync-log-title, -clear-button, -empty-filtered); "registrazione" means a recording/entry and is inconsistent on the same surface.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (6)

- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — That's the OS string.
- `imported-safari-reading-list` — `browser/browser/migration.ftl` — Elenco lettura is correct
- `migration-imported-safari-reading-list` — `browser/browser/migrationWizard.ftl` — Elenco lettura is correct
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — Element is there
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — Element is there
- `ssl-error-missing-extended-master-secret` — `toolkit/toolkit/neterror/nsserrors.ftl` — “Extension” is there

_One line each in `locales/it/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (2)

- **`it-crittare`** (1) — `crittare` and its forms (`critta`, `crittato`) are the correct Italian verb for "to encrypt" — not a typo for `criptare`. Confirmed by the maintainer. Scoped to spelling findings so a mistranslation in the same string still reports.
    - `credit-card-save-doorhanger-description`
- **`it-disegnata`** (1) — `disegnata` in about-private-browsing-focus-promo-text is deliberate wording, confirmed by the maintainer.
    - `about-private-browsing-focus-promo-text`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (56)

- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — fixed 2026-08-21
- `select-translations-panel-try-another-language-label` — `browser/browser/translations.ftl` — fixed 2026-08-21
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — fixed 2026-08-21
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — fixed 2026-08-21
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — fixed 2026-08-21
- `aiwindow-firstrun-memories-privacy-title` — `browser/browser/aiWindow.ftl` — fixed 2026-07-26
- `action-log-searching-tabs` — `browser/browser/aiWindowContent.ftl` — fixed 2026-07-26
- `appmenuitem-banner-update-unsupported` — `browser/browser/appmenu.ftl` — fixed 2026-07-26
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — fixed 2026-07-26
- `confirmation-hint-pin-tab-description` — `browser/browser/confirmationHints.ftl` — fixed 2026-07-26
- `customkeys-conflict-confirm-body` — `browser/browser/customkeys.ftl` — fixed 2026-07-26
- `perplexity-callout-theme-1-subtitle-2` — `browser/browser/featureCallout.ftl` — fixed 2026-07-26
- `launch-on-login-autostart-infobar-message` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-26
- `newtab-weather-see-forecast` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-26
- `newtab-widget-section-minimize` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-26
- `newtab-widget-timer-start-aria` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-26
- `mr2022-onboarding-privacy-segmentation-image-alt` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-26
- `onboarding-infrequent-import-primary-button` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-26
- `select-bookmark-desc` — `browser/browser/preferences/selectBookmark.ftl` — fixed 2026-07-26
- `protections-panel-etp-on-header` — `browser/browser/protectionsPanel.ftl` — fixed 2026-07-26
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — fixed 2026-07-26
- `add-engine-no-url` — `browser/browser/search.ftl` — fixed 2026-07-26
- `open-desktop-prefs` — `browser/browser/setDesktopBackground.ftl` — fixed 2026-07-26
- `protections-milestone` — `browser/browser/siteProtections.ftl` — fixed 2026-07-26
- `tab-note-preview-expand` — `browser/browser/tabbrowser.ftl` — fixed 2026-07-26
- `tabbrowser-container-tab-title` — `browser/browser/tabbrowser.ftl` — fixed 2026-07-26
- `select-translations-panel-init-failure-message` — `browser/browser/translations.ftl` — fixed 2026-07-26
- `about-debugging-runtime-service-workers-not-compatible` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-26
- `inactive-scroll-padding-when-not-scroll-container` — `devtools/client/tooltips.ftl` — fixed 2026-07-26
- `xslt-call-to-key-not-allowed` — `dom/dom/xslt.ftl` — fixed 2026-07-26
- `delete-ssl-override-impact` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-26
- `crashreporter-plea` — `toolkit/crashreporter/crashreporter.ftl` — fixed 2026-07-26
- `rights-intro-point-5-unbranded` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-07-26
- `rights-webservices-term-3` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-07-26
- `rights-webservices-term-unbranded` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-07-26
- `rights-webservices-unbranded` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-07-26
- `about-telemetry-page-subtitle` — `toolkit/toolkit/about/aboutTelemetry.ftl` — fixed 2026-07-26
- `third-party-button-open` — `toolkit/toolkit/about/aboutThirdParty.ftl` — fixed 2026-07-26
- `about-translations-policy-disabled-info-message` — `toolkit/toolkit/about/aboutTranslations.ftl` — fixed 2026-07-26
- `about-webrtc-remote-send-ssrc` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-07-26
