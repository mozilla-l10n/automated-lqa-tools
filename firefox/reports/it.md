# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,350 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (4)

- `smartwindow-onboarding-title` — `browser/browser/newtab/onboarding.ftl` — `smartwindow-onboarding-title` calls `-smart-window-brand-name` with ['capitalization', 'plural-form'], but that term selects on ['form']
  - Current: `Rendi { -smart-window-brand-name } il tuo punto di partenza`
  - The term falls back to its catch-all variant, so the intended form is never selected.
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — Malformed closing tag `</a >` in `about-glean-about-data-list-item-dictionary`
  - Current: `Per consultare l’elenco dei dati raccolti da { -glean-brand-name } per applicazione, fare riferimento al <a data-l10n-name="glean-dictionary-link">Dizionario { -glean-brand-name }</a >.`
  - en-US: `To browse the list of data collected by { -glean-brand-name } per application, please consult the <a data-l10n-name="glean-dictionary-link">{ -glean-brand-name } Dictionary</a>.`
  - Whitespace inside a closing tag makes it render as literal text.
- `felt-error-warning-elevation-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-elevation-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `Impossibile installare un aggiornamento a causa di privilegi di sistema insufficienti. Contattare l'amministratore per assistenza.`
  - The tree uses ’ 1923 times against 8 straight.
- `felt-error-warning-elevation-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-elevation-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `Impossibile installare un aggiornamento a causa di privilegi di sistema insufficienti. Contattare l'amministratore per assistenza.`
  - The tree uses ’ 1923 times against 8 straight.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 370 |
| Strings | 18,350 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 1 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 1 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 1046, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1923, `straight` 8 | **typographic** |
| ellipsis | `char` 481 | **char** |
| dash | `em` 75, `en` 18 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 760, `formal` 59 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 2 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `smartwindow-onboarding-title` — `browser/browser/newtab/onboarding.ftl` — `smartwindow-onboarding-title` calls `-smart-window-brand-name` with ['capitalization', 'plural-form'], but that term selects on ['form']
  - Current: `Rendi { -smart-window-brand-name } il tuo punto di partenza`
  - The term falls back to its catch-all variant, so the intended form is never selected.
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — Malformed closing tag `</a >` in `about-glean-about-data-list-item-dictionary`
  - Current: `Per consultare l’elenco dei dati raccolti da { -glean-brand-name } per applicazione, fare riferimento al <a data-l10n-name="glean-dictionary-link">Dizionario { -glean-brand-name }</a >.`
  - en-US: `To browse the list of data collected by { -glean-brand-name } per application, please consult the <a data-l10n-name="glean-dictionary-link">{ -glean-brand-name } Dictionary</a>.`
  - Whitespace inside a closing tag makes it render as literal text.

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `ssl-error-missing-extended-master-secret` — `toolkit/toolkit/neterror/nsserrors.ftl` — drop leftover correct — ✅

### D. Terminology, register & consistency

- `imported-safari-reading-list` — `browser/browser/migration.ftl` — Elenco lettura is correct. Dismissed.
- `migration-imported-safari-reading-list` — `browser/browser/migrationWizard.ftl` — Elenco lettura is correct. Dismissed.
- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — ⚠️ existing-user-privacy-notice-update-message — browser/browser/termsofuse.ftl:11 — still Informativa sulla privacy mid-sentence vs lowercase in lines 9/20.
- `select-translations-panel-try-another-language-label` — `browser/browser/translations.ftl` — ⚠️ select-translations-panel-try-another-language-label — browser/browser/translations.ftl:213 — still lingua sorgente vs lingua di origine (line 85).

### E. Typography, punctuation & spacing

- `felt-error-warning-elevation-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-elevation-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `Impossibile installare un aggiornamento a causa di privilegi di sistema insufficienti. Contattare l'amministratore per assistenza.`
  - The tree uses ’ 1923 times against 8 straight.
- `felt-error-warning-elevation-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-elevation-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `Impossibile installare un aggiornamento a causa di privilegi di sistema insufficienti. Contattare l'amministratore per assistenza.`
  - The tree uses ’ 1923 times against 8 straight.

---

## 4. Appendix

### Suppressed as false positives (2)

- **`it-critta`** (1) — `critta` is correct — `crittare` means to encrypt. Confirmed by the maintainer.
  - `credit-card-save-doorhanger-description`
- **`it-disegnata`** (1) — `disegnata` in about-private-browsing-focus-promo-text is deliberate wording, confirmed by the maintainer.
  - `about-private-browsing-focus-promo-text`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Resolved to date (51)

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
- `about-webrtc-rtp-stats-heading` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-07-26
- `abuse-report-broken-suggestions-sitepermission` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-07-26
- `choose-dialog-privatebrowsing-disabled` — `toolkit/toolkit/global/handlerDialog.ftl` — fixed 2026-07-26
- `process-type-utility-actor-windows-file-dialog` — `toolkit/toolkit/global/processTypes.ftl` — fixed 2026-07-26
- `language-name-tw` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-07-26
