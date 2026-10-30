# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `6c76c457ee95` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `110b6b510435` |
| **Previous run** | 2026-10-26 @ `6c76c457ee95` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 16,836 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for it: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 340 |
| Strings | 16,836 |
| Missing strings | 0 |
| Obsolete strings | 19 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
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

_222 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 963, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1764, `straight` 6 | **typographic** |
| ellipsis | `char` 416 | **char** |
| dash | `em` 51, `en` 17 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 722, `formal` 47 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (19)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — "help keep your browsing private" rendered as an absolute "impediscono" (prevent), dropping the hedge.
    - Current: `Le finestre anonime impediscono agli altri utenti di questo dispositivo di vedere la tua attività di navigazione.`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Le finestre anonime aiutano a nascondere la tua attività di navigazione agli altri utenti di questo dispositivo.`
    - The source says Private Windows "help keep" browsing private; the Italian asserts they outright prevent other users from seeing the activity, a stronger promise than the product makes.
- `ipprotection-feature-introduction-description-private-browsing-3` — `browser/browser/ipProtection.ftl` — The hedge 'Help' is dropped, so the Italian claims the VPN hides the user's location outright.
    - Current: `Nascondi la tua posizione mentre navighi.`
    - Source: `Help hide your location as you browse. Set rules to turn on VPN when you want <a data-l10n-name="learn-more-vpn">extra privacy</a> or location-based browsing, and off when you don’t.`
    - Suggest: `Aiuta a nascondere la tua posizione mentre navighi.`
    - en-US 'Help hide your location' is a hedged claim. 'Nascondi la tua posizione' promises full concealment, which is a protection the product does not guarantee.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 6 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

- `detail-contributions-button` — `toolkit/toolkit/about/aboutAddons.ftl` — Access key `C` of `detail-contributions-button` is not present in its label
    - Current: `C`
    - Source: `(value): Contribute accesskey: C title: Contribute to the development of this add-on`
    - The label is “Fai una donazione”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-private-browsing-spotlight-basics-strict-tracking` — `browser/browser/aboutPrivateBrowsing.ftl` — "stronger tracking protections" rendered as "più aggressiva" (more aggressive).
    - Current: `per una protezione antitracciamento più aggressiva`
    - Source: `Switch to Strict in settings for stronger tracking protections.`
    - Suggest: `per una protezione antitracciamento più efficace`
    - The source says the protection is stronger, not more aggressive; "aggressiva" carries a different connotation than en-US "stronger".
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — "help keep your browsing private" rendered as an absolute "impediscono" (prevent), dropping the hedge.
    - Current: `Le finestre anonime impediscono agli altri utenti di questo dispositivo di vedere la tua attività di navigazione.`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Le finestre anonime aiutano a nascondere la tua attività di navigazione agli altri utenti di questo dispositivo.`
    - The source says Private Windows "help keep" browsing private; the Italian asserts they outright prevent other users from seeing the activity, a stronger promise than the product makes.
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
- `ipprotection-feature-introduction-description-private-browsing-3` — `browser/browser/ipProtection.ftl` — The hedge 'Help' is dropped, so the Italian claims the VPN hides the user's location outright.
    - Current: `Nascondi la tua posizione mentre navighi.`
    - Source: `Help hide your location as you browse. Set rules to turn on VPN when you want <a data-l10n-name="learn-more-vpn">extra privacy</a> or location-based browsing, and off when you don’t.`
    - Suggest: `Aiuta a nascondere la tua posizione mentre navighi.`
    - en-US 'Help hide your location' is a hedged claim. 'Nascondi la tua posizione' promises full concealment, which is a protection the product does not guarantee.
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
- `jsonlScopeName` — `devtools/client/netmonitor.properties` — "JSON Lines" is a format name (JSONL/NDJSON) and should not be translated as "Righe JSON".
    - Current: `Righe JSON`
    - Source: `JSON Lines`
    - Suggest: `JSON Lines`
    - The developer comment identifies it as the JSON Lines (JSONL/NDJSON) payload format name; format names are kept in English in DevTools panel labels (e.g. JSON, XML).
- `about-sync-log-empty` — `toolkit/services/aboutSyncLog.ftl` — "No sync logs have been recorded" rendered as "no log was found", changing the meaning from recording to searching.
    - Current: `Non è stato trovato alcun registro di sincronizzazione.`
    - Source: `No sync logs have been recorded.`
    - Suggest: `Non è stato registrato alcun registro di sincronizzazione.`
    - The en-US says logs have not been recorded, not that a search failed to find them.
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — "Log modules" (verb + object: log the modules) rendered as the noun phrase "Moduli di registrazione".
    - Current: `Moduli di registrazione per diagnosticare problemi con la VPN integrata (IP Protection).`
    - Source: `Log modules to diagnose IP Protection (VPN) issues`
    - Suggest: `Registra i moduli per diagnosticare problemi con IP Protection (VPN).`
    - The en-US is an imperative describing the preset action ("Log modules to diagnose…"), not a noun phrase; also "IP Protection (VPN)" is reversed and expanded to "VPN integrata (IP Protection)".
- `neterror-search-cta-search-button` — `toolkit/toolkit/neterror/netError.ftl` — Tooltip translated as an imperative command instead of a description of what the button does.
    - Current: `tooltiptext: Apri i risultati di ricerca in una nuova scheda`
    - Source: `accesskey: c label: Search tooltiptext: Opens search results in a new tab`
    - Suggest: `tooltiptext: Apre i risultati di ricerca in una nuova scheda`
    - The en-US "Opens search results in a new tab" is descriptive (it doubles as the accessible description, per the developer comment), not an instruction to the user.

### C. Grammar, agreement & spelling

- `ip-protection-site-rules-edit-button` — `browser/browser/ipProtection.ftl` — Ungrammatical preposition: "relativa per" should be "relativa a" (or just "per").
    - Current: `la regola relativa per { $website }`
    - Source: `aria-label: Edit the rule for { $website } title: Edit`
    - Suggest: `la regola relativa a { $website }`
    - "Relativa" takes the preposition "a"; "relativa per" is ungrammatical Italian. The sibling delete button uses plain "la regola per".
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — Label uses singular "Fornitore" where the source is plural "providers".
    - Current: `label: Fornitore di chatbot IA nella barra laterale`
    - Source: `description: Keep a chatbot in view as you browse. Choose from multiple providers and switch anytime. label: AI chatbot providers in sidebar`
    - Suggest: `label: Fornitori di chatbot IA nella barra laterale`
    - en-US "AI chatbot providers in sidebar" is plural, and the accompanying description mentions choosing among multiple providers ("diversi fornitori").

### D. Terminology, register & consistency

- `toolbar-button-mini-window` — `browser/browser/miniWindow.ftl` — The tooltip renders the feature name 'Mini Window' as 'finestra ridotta' instead of the 'mini finestra' used everywhere else.
    - Current: `Utilizza finestra ridotta`
    - Source: `label: Mini Window tooltiptext: Use Mini Window`
    - Suggest: `Utilizza mini finestra`
    - The feature is called 'Mini finestra' in this string's own label and in every other Mini Window string. The tooltip names it differently, so the two are inconsistent.
- `newtab-wallpaper-firefox-hills-light` — `browser/browser/newtab/newtab.ftl` — "light hills" rendered as "colline chiare" here but "colline luminose" in the other light-hills strings.
    - Current: `Una volpe corre su colline chiare`
    - Source: `A fox running over light hills`
    - Suggest: `Una volpe corre su colline luminose`
    - The same en-US term "light hills" is translated inconsistently across newtab-wallpaper-firefox-sitting-hill-light and newtab-wallpaper-firefox-sky-light ("colline luminose") within the same surface.
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log/logs" translated as "registrazione/registrazioni" instead of the "registro/registri" used consistently elsewhere in the same page.
    - Current: `[one] { $count } registrazione [other] { $count } registrazioni`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } registro [other] { $count } registri`
    - Every other string in this file renders "log(s)" as "registro/registri"; "registrazione" means a recording, an inconsistent term on the same surface.

### E. Typography, punctuation & spacing

- `taskbar-tabs-social-callout-subtitle` — `browser/browser/featureCallout.ftl` — The sentence has no final full stop, unlike the en-US source and the other callout subtitles in this batch.
    - Current: `protetta da { -brand-short-name }`
    - Source: `Launch your social sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `protetta da { -brand-short-name }.`
    - The en-US ends with a period, and every other taskbar-tabs callout subtitle in this batch ends with one in Italian. This string alone drops it.
- `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl` — Double space and missing article in the button label.
    - Current: `Gestisci  regole per i siti web`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage website rules`
    - Suggest: `Gestisci le regole per i siti web`
    - The label contains a doubled space between "Gestisci" and "regole" and drops the article used in the identical string ip-protection-site-rules-header ("Gestisci le regole per i siti web").

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

### Fixed to date (59)

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
