# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `2eb8d2e6cb72` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `36e745f2f7d9` |
| **Previous run** | 2026-10-30 @ `3b1e357fad9d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 16,961 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for it: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (6)

- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — The security claim is attached to the wrong subject and the sentence structure changes the meaning ("Riavviando { -brand-short-name }, continuerà..." implies the OS/browser continues).
    - Current: `Riavviando { -brand-short-name }, continuerà a funzionare normalmente e in sicurezza.`
    - Source: `This can happen during a long browsing session, or when your operating system updates { -brand-short-name }. Restarting keeps { -brand-short-name } secure and working normally.`
    - Suggest: `Il riavvio consente a { -brand-short-name } di restare sicuro e di funzionare normalmente.`
    - En-US: "Restarting keeps { -brand-short-name } secure and working normally." The Italian gerund construction leaves the subject of "continuerà" dangling and turns the statement into a promise that something will keep working, rather than that restarting keeps the browser secure.
- `urlbar-result-menu-remove-top-site` — `browser/browser/browser.ftl` — "Remove this top site" is rendered as "Rimuovi dai siti principali" (remove from top sites) instead of removing the site itself.
    - Current: `Rimuovi dai siti principali`
    - Source: `(value): Remove this top site accesskey: T`
    - Suggest: `Rimuovi questo sito principale`
    - The en-US action removes this top site entry; the Italian states removal from the top sites list, which changes the object of the action.
- `newtab-stocks-search-hint` — `browser/browser/newtab/newtab.ftl` — "Search for symbols" is translated as "Cerca azioni" (search for stocks) instead of ticker symbols.
    - Current: `Cerca azioni o aziende da aggiungere alla tua lista`
    - Source: `Search for symbols or companies to add to your watchlist`
    - Suggest: `Cerca simboli o aziende da aggiungere alla tua lista di controllo`
    - En-US says "symbols or companies"; the sibling strings correctly render "symbol" as "simbolo" ("Cerca per nome o simbolo"), so "azioni" is inconsistent and drops the ticker-symbol meaning.
- `newtab-wallpaper-firefox-sitting-hill-dark` — `browser/browser/newtab/newtab.ftl` — "sitting" rendered as "accovacciata" (crouching), inconsistent with the parallel string which uses "seduta".
    - Current: `Una volpe accovacciata su colline viola scuro`
    - Source: `A fox sitting on dark purple hills`
    - Suggest: `Una volpe seduta su colline viola scuro`
    - en-US says "A fox sitting on dark purple hills"; the companion string newtab-wallpaper-firefox-sitting-hill-light translates the same "sitting" as "seduta". "Accovacciata" means crouching.
- `item-cookies-site-data-description2` — `browser/browser/sanitize.ftl` — The phrase "dai siti" appears twice in a row.
    - Current: `Ti disconnette dai siti dai siti`
    - Source: `Signs you out and may clear shopping carts`
    - Suggest: `Ti disconnette dai siti`
    - The repeated words are a typo. The en-US says only "Signs you out".
- `neterror-search-cta-search-button` — `toolkit/toolkit/neterror/netError.ftl` — Tooltip translated as an imperative command instead of a description of what the button does.
    - Current: `tooltiptext: Apri i risultati di ricerca in una nuova scheda`
    - Source: `accesskey: c label: Search tooltiptext: Opens search results in a new tab`
    - Suggest: `tooltiptext: Apre i risultati di ricerca in una nuova scheda`
    - The en-US "Opens search results in a new tab" is descriptive (it doubles as the accessible description, per the developer comment), not an instruction to the user.

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
| Files | 340 |
| Strings | 16,961 |
| Missing strings | 4 |
| Obsolete strings | 69 |
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

**4 strings** are not translated yet, concentrated in:

- `toolkit/toolkit/formautofill/formAutofill.ftl` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

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

_222 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 965, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1769, `straight` 6 | **typographic** |
| ellipsis | `char` 418 | **char** |
| dash | `em` 53, `en` 17 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 731, `formal` 47 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-private-browsing-spotlight-basics-strict-tracking` — `browser/browser/aboutPrivateBrowsing.ftl` — "stronger tracking protections" rendered as "più aggressiva" (more aggressive).
    - Current: `per una protezione antitracciamento più aggressiva`
    - Source: `Switch to Strict in settings for stronger tracking protections.`
    - Suggest: `per una protezione antitracciamento più efficace`
    - The source says the protection is stronger, not more aggressive; "aggressiva" carries a different connotation than en-US "stronger".

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (10)

- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — Correct as is
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — On purpose, because the alternative is hard to read "nascondere a qualcuno".
- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — Clearer as is
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — That's the OS string.
- `imported-safari-reading-list` — `browser/browser/migration.ftl` — Elenco lettura is correct
- `ipprotection-feature-introduction-description-private-browsing-3` — `browser/browser/ipProtection.ftl` — On purpose for better flow
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

### Fixed to date (74)

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
- `onboarding-infrequent-import-primary-button` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-26
- `select-bookmark-desc` — `browser/browser/preferences/selectBookmark.ftl` — fixed 2026-07-26
- `protections-panel-etp-on-header` — `browser/browser/protectionsPanel.ftl` — fixed 2026-07-26
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — fixed 2026-07-26
- `add-engine-no-url` — `browser/browser/search.ftl` — fixed 2026-07-26
