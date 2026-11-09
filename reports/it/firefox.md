# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f82b652e600a` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-09 @ `f278b81a68aa` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 17,106 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for it: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (5)

- `dom-manifest-id-is-invalid` — `dom/dom/manifest.ftl` — "The id member" is rendered as "the member's id".
    - Current: `L’id del membro`
    - Source: `The id member did not resolve to a valid URL.`
    - Suggest: `Il membro id`
    - The en-US means the manifest member called "id". "L’id del membro" means the id of a member.
- `dom-manifest-id-not-same-origin` — `dom/dom/manifest.ftl` — "The id member" is rendered as "the member's id".
    - Current: `L’id del membro deve`
    - Source: `The id member must have the same origin as the start_url member.`
    - Suggest: `Il membro id deve`
    - The en-US means the manifest member called "id". "L’id del membro" means the id of a member.
- `dom-manifest-image-repeated-purposes` — `dom/dom/manifest.ftl` — "Repeated purpose(s)" is rendered as "more than one purpose".
    - Current: `include più di uno scopo (“purpose”)`
    - Source: `{ $memberName } item at index { $index } includes repeated purpose(s): { $purposes }.`
    - Suggest: `include scopi (“purpose”) ripetuti`
    - The warning is about duplicated purpose values. Having more than one purpose is valid, so the Italian describes the wrong problem.
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — "The scope URL" is rendered as "the URL's scope".
    - Current: `L’ambito dell’URL deve`
    - Source: `The scope URL must be same origin as document.`
    - Suggest: `L’URL dell’ambito deve`
    - The en-US means the URL given for the scope. The Italian says the scope of a URL.
- `dom-manifest-scope-url-invalid` — `dom/dom/manifest.ftl` — "The scope URL" is rendered as "the URL's scope".
    - Current: `L’ambito dell’URL`
    - Source: `The scope URL is invalid.`
    - Suggest: `L’URL dell’ambito`
    - The en-US means the URL given for the scope. The Italian says the scope of a URL, which reverses the relationship.

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
| Files | 341 |
| Strings | 17,106 |
| Missing strings | 0 |
| Obsolete strings | 2 |
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

_229 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 979, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1787, `straight` 6 | **typographic** |
| ellipsis | `char` 419 | **char** |
| dash | `em` 53, `en` 17 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 739, `formal` 47 | **informal** |

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

### Dismissed by hand (9)

- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Correct as is
- `about-private-browsing-spotlight-basics-strict-tracking` — `browser/browser/aboutPrivateBrowsing.ftl` — Stronger is not more effective
- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — Clearer as is
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — That's the OS string.
- `imported-safari-reading-list` — `browser/browser/migration.ftl` — Elenco lettura is correct
- `migration-imported-safari-reading-list` — `browser/browser/migrationWizard.ftl` — Elenco lettura is correct
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — Element is there
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — Element is there
- `ssl-error-missing-extended-master-secret` — `toolkit/toolkit/neterror/nsserrors.ftl` — “Extension” is there

_One line each in `locales/it/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/it/dismissed.txt` brings the finding back now._

### Suppressed as false positives (2)

- **`it-crittare`** (1) — `crittare` and its forms (`critta`, `crittato`) are the correct Italian verb for "to encrypt" — not a typo for `criptare`. Confirmed by the maintainer. Scoped to spelling findings so a mistranslation in the same string still reports.
    - `credit-card-save-doorhanger-description`
- **`it-disegnata`** (1) — `disegnata` in about-private-browsing-focus-promo-text is deliberate wording, confirmed by the maintainer.
    - `about-private-browsing-focus-promo-text`

_Suppressions live in `locales/it/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (79)

- `dom-manifest-id-is-invalid` — `dom/dom/manifest.ftl` — fixed 2026-11-09
- `dom-manifest-id-not-same-origin` — `dom/dom/manifest.ftl` — fixed 2026-11-09
- `dom-manifest-image-repeated-purposes` — `dom/dom/manifest.ftl` — fixed 2026-11-09
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — fixed 2026-11-09
- `dom-manifest-scope-url-invalid` — `dom/dom/manifest.ftl` — fixed 2026-11-09
- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-10-30
- `urlbar-result-menu-remove-top-site` — `browser/browser/browser.ftl` — fixed 2026-10-30
- `taskbar-tabs-social-callout-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-10-30
- `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl` — fixed 2026-10-30
- `ip-protection-site-rules-edit-button` — `browser/browser/ipProtection.ftl` — fixed 2026-10-30
- `toolbar-button-mini-window` — `browser/browser/miniWindow.ftl` — fixed 2026-10-30
- `newtab-stocks-search-hint` — `browser/browser/newtab/newtab.ftl` — fixed 2026-10-30
- `newtab-wallpaper-firefox-hills-light` — `browser/browser/newtab/newtab.ftl` — fixed 2026-10-30
- `newtab-wallpaper-firefox-sitting-hill-dark` — `browser/browser/newtab/newtab.ftl` — fixed 2026-10-30
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-10-30
- `item-cookies-site-data-description2` — `browser/browser/sanitize.ftl` — fixed 2026-10-30
- `jsonlScopeName` — `devtools/client/netmonitor.properties` — fixed 2026-10-30
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — fixed 2026-10-30
- `detail-contributions-button` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-10-30
- `neterror-search-cta-search-button` — `toolkit/toolkit/neterror/netError.ftl` — fixed 2026-10-30
- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — fixed 2026-10-19
- `tab-groups-onboarding-saved-groups-title-3` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-10-19
- `sync-syncing-across-devices-heading-3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-10-19
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
