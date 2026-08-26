# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-08-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b82b7a344c63` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 36 of 18,397 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (4)

- `pdfjs-embed-fallback-open-button` — `toolkit/toolkit/pdfviewer/embedFallback.ftl` — "Open PDF" refers to this specific PDF, but the French uses the indefinite article "un PDF".
    - Current: `Ouvrir un PDF`
    - Source: `Open PDF`
    - Suggest: `Ouvrir le PDF`
    - The button opens the PDF that can’t be displayed inline; "Ouvrir un PDF" suggests choosing/opening some PDF file instead.
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — The singular plural form reads "{ $count } de journal", which is ungrammatical.
    - Current: `{ $count } de journal`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `{ $count } journal`
    - en-US is "{ $count } log"; the French singular should be "1 journal", not "1 de journal".
- `about-sync-log-filter-date-all` — `toolkit/services/aboutSyncLog.ftl` — "All time" (a date range filter) is rendered as "Toujours" (always) instead of a time-range label.
    - Current: `label: Toujours`
    - Source: `label: All time`
    - Suggest: `label: Tout l’historique`
    - The option filters logs over the entire period; "Toujours" means "always" and does not express the date range.
- `about-sync-log-title` — `toolkit/services/aboutSyncLog.ftl` — Title adds a definite article not present in the English label "Sync logs".
    - Current: `Les journaux de synchronisation`
    - Source: `Sync logs`
    - Suggest: `Journaux de synchronisation`
    - en-US "Sync logs" is an article-less page title; French titles/headings in this file (e.g. "Journaux de diagnostic") omit the article.

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
| Strings | 18,397 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 1 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 4 |

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
| quotes | `guillemet` 1132, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5640, `straight` 10 | **typographic** |
| ellipsis | `char` 472 | **char** |
| dash | `em` 68, `en` 8 | **em** |
| nbsp | `total` 4454, `before-punctuation` 2000 | _mixed_ |
| register | `formal` 3193 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (20)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
    - Current: `B`
    - Source: `accesskey: B aria-label: Bookmarks toolbarname: Bookmarks Toolbar`
    - The label is “Marque-pages”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — `about-networking-ssl-tokens-summary-compression` references ['total'], which en-US does not pass
    - Current: `{$total ->} [one] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisé) [other] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisés)`
    - Source: `{ $decompressedLength } → { $compressedLength } B ({ $saved }% saved)`
    - Suggest: `{ $decompressedLength } → { $compressedLength } B ({ $saved }% saved)`
    - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.

### B. Mistranslation, reversed meaning, wrong names & brand

- `aiwindow-firstrun-default-checkbox-label` — `browser/browser/aiWindow.ftl` — brand form lower-plural renders "dans une fenêtres intelligentes" → use lower-singular (EN is singular; matches line 164).
    - Source: `Always open { -brand-product-name } in { -smart-window-brand-name }`
- `about-sync-log-filter-date-all` — `toolkit/services/aboutSyncLog.ftl` — "All time" (a date range filter) is rendered as "Toujours" (always) instead of a time-range label.
    - Current: `label: Toujours`
    - Source: `label: All time`
    - Suggest: `label: Tout l’historique`
    - The option filters logs over the entire period; "Toujours" means "always" and does not express the date range.
- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — toolkit/toolkit/about/aboutGlean.ftl:133,135 — both say "axe des abscisses" but EN references the Y-axis → axe des ordonnées; line 135 is also internally contradictory ("décalage vertical … abscisses").
    - Source: `Y-axis X offset`
    - Suggest: `axe des ordonnées`
- `pdfjs-embed-fallback-open-button` — `toolkit/toolkit/pdfviewer/embedFallback.ftl` — "Open PDF" refers to this specific PDF, but the French uses the indefinite article "un PDF".
    - Current: `Ouvrir un PDF`
    - Source: `Open PDF`
    - Suggest: `Ouvrir le PDF`
    - The button opens the PDF that can’t be displayed inline; "Ouvrir un PDF" suggests choosing/opening some PDF file instead.

### C. Grammar, agreement & spelling

- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — The singular plural form reads "{ $count } de journal", which is ungrammatical.
    - Current: `{ $count } de journal`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `{ $count } journal`
    - en-US is "{ $count } log"; the French singular should be "1 journal", not "1 de journal".

### D. Terminology, register & consistency

- `appmenuitem-share-firefox-title2` — `browser/browser/appmenu.ftl` — "Share { -brand-product-name }" is rendered "Partager" here while all other referral strings use "Recommander".
    - Current: `Partager { -brand-product-name }`
    - Source: `Share { -brand-product-name }`
    - Suggest: `Recommander { -brand-product-name }`
    - The developer comment says this button links to the Referrals page, the same surface as appmenu-referrals2, menu-referrals2 and referrals-link2, which all translate "Share" as "Recommander"; the inconsistent term is wrong here.
- `fonts-default-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
    - Source: `label: Serif`
- `fonts-sans-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
    - Source: `(value): Sans-serif accesskey: n`
- `fonts-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
    - Source: `(value): Serif accesskey: S`
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — browser/browser/translations.ftl:12,16 — FR: "Bêta" → Beta (comment: must stay untranslated to match the un-localized BETA icon).
    - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
    - Suggest: `Beta`
- `about-debugging-worker-status-running` — `devtools/client/aboutdebugging.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
    - Source: `Running`
- `serviceworker-worker-status-running` — `devtools/client/application.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
    - Source: `Running`
- `about-sync-log-title` — `toolkit/services/aboutSyncLog.ftl` — Title adds a definite article not present in the English label "Sync logs".
    - Current: `Les journaux de synchronisation`
    - Source: `Sync logs`
    - Suggest: `Journaux de synchronisation`
    - en-US "Sync logs" is an article-less page title; French titles/headings in this file (e.g. "Journaux de diagnostic") omit the article.
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-cpu-almost-idle (.title) — toolkit/toolkit/about/aboutProcesses.ftl:167 — "Temps CPU total" vs "Temps total de CPU" (lines 161/170); align.
    - Source: `(value): < 0.1% title: Total CPU time: { $total }{ $unit }`
    - Suggest: `.title`

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5640 times against 10 straight.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1132 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1132 occurrences).
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5640 times against 10 straight.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (55)

- `browser-main-window-window-titles` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `contextual-manager-passwords-breached-origin-heading-and-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-24
- `contextual-manager-passwords-remove-all-title` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-24
- `customkeys-conflict-confirm` — `browser/browser/customkeys.ftl` — fixed 2026-08-24
- `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `sidebar-genai-survey-productive-question` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `newtab-clock-widget-edit-item-with-nickname` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `multi-profile-spotlight-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `places-delete-bookmark` — `browser/browser/places.ftl` — fixed 2026-08-24
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-24
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-24
- `app-manager-handle-file` — `browser/browser/preferences/applicationManager.ftl` — fixed 2026-08-24
- `app-manager-handle-protocol` — `browser/browser/preferences/applicationManager.ftl` — fixed 2026-08-24
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `settings-redesign-promo` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — fixed 2026-08-24
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — fixed 2026-08-24
- `learn-more` — `devtools/client/tooltips.ftl` — fixed 2026-08-24
- `support-remote-experiments-see-about-studies` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-08-24
- `third-party-detail-occurrences` — `toolkit/toolkit/about/aboutThirdParty.ftl` — fixed 2026-08-24
- `migration-wizard-progress-success-bookmarks` — `browser/browser/migrationWizard.ftl` — fixed 2026-07-26
- `newtab-privacy-message-info-7` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-26
- `onboarding-new-user-survey-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-26
- `autofill-card-network-cartebancaire` — `browser/browser/preferences/formAutofill.ftl` — fixed 2026-07-26
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-26
- `monitor-breaches-resolved-description` — `browser/browser/protections.ftl` — fixed 2026-07-26
- `tabbrowser-container-tab-title` — `browser/browser/tabbrowser.ftl` — fixed 2026-07-26
- `tabbrowser-manager-mute-tab` — `browser/browser/tabbrowser.ftl` — fixed 2026-07-26
- `accessibility-text-label-issue-area` — `devtools/client/accessibility.ftl` — fixed 2026-07-26
- `network-menu-summary-tooltip-domcontentloaded` — `devtools/client/netmonitor.ftl` — fixed 2026-07-26
- `inactive-css-not-block` — `devtools/client/tooltips.ftl` — fixed 2026-07-26
- `xslt-transform-error` — `dom/dom/xslt.ftl` — fixed 2026-07-26
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-26
- `change-password-token` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-07-26
- `about-glean-category-adhoc-testing` — `toolkit/toolkit/about/aboutGlean.ftl` — fixed 2026-07-26
- `about-networking-dns-domain` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-07-26
