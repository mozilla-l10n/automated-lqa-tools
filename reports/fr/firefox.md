# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-10-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ff2ee909fb8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9228382dd70d` |
| **Previous run** | 2026-09-28 @ `92e0a4895124` |
| **Mode** | incremental |
| **Strings reviewed this run** | 62 of 16,582 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (4)

- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — `autocomplete-delete-address-entry` uses a straight apostrophe
    - Current: `Supprimer l'adresse { $entry }`
    - Source: `Delete address { $entry }`
    - The tree uses ’ 5063 times against 11 straight.
- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — Straight apostrophe used instead of the typographic apostrophe required by the locale.
    - Current: `Supprimer l'adresse`
    - Source: `Delete address { $entry }`
    - Suggest: `Supprimer l’adresse`
    - The locale convention is the typographic apostrophe ’ (5633 vs 10).
- `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl` — "You aren’t syncing anything… yet" is rendered as "you don't have to sync anything", changing the meaning.
    - Current: `Vous ne devez rien synchroniser… pour l’instant.`
    - Source: `description: You aren’t syncing anything… yet. Choose what to sync on this device. label: Manage synced data`
    - Suggest: `Vous ne synchronisez rien… pour l’instant.`
    - The en-US states a fact about the current state (nothing is being synced), not an absence of obligation.
- `newtab-stocks-widget-menu-button2` — `browser/browser/newtab/newtab.ftl` — "Finance options" mistranslated as "Options de financement" (funding options).
    - Current: `Options de financement`
    - Source: `aria-label: Finance options title: Finance options`
    - Suggest: `Options de finance`
    - "Finance" here names the finance/stocks widget; "financement" means funding, a different concept.

### ✅ Fixed since the last run (2)

- `ipprotection-feature-introduction-description-inclusions` — `browser/browser/ipProtection.ftl` — "as you browse" is rendered twice, producing a redundant duplicated phrase.
    - Current: `Lorsque vous naviguez, vous pouvez masquer votre localisation pour <a data-l10n-name="learn-more-vpn">plus de confidentialité</a> pendant votre navigation.`
    - Source: `Help hide your location for <a data-l10n-name="learn-more-vpn">extra privacy</a> as you browse. Set the VPN on or off for certain sites.`
    - Suggest: `Masquez votre localisation pour <a data-l10n-name="learn-more-vpn">plus de confidentialité</a> pendant votre navigation.`
    - The source has a single "as you browse"; the French repeats it as both "Lorsque vous naviguez" and "pendant votre navigation".
- `ipprotection-feature-introduction-description-private-browsing-1` — `browser/browser/ipProtection.ftl` — The second sentence's ending is mistranslated and truncated, losing the meaning "and off where you don’t [want it]".
    - Current: `et le désactiver là où vous n’en avez pas`
    - Source: `Help hide your location for <a data-l10n-name="learn-more-vpn">extra privacy</a> as you browse. Set rules to turn on the VPN for extra privacy or location-based browsing, and off where you don’t.`
    - Suggest: `et le désactiver là où vous n’en avez pas besoin`
    - The en-US says "and off where you don’t" (i.e. where you don't want extra privacy); the French ends with "là où vous n’en avez pas", which is incomplete and meaningless in French.

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
| Files | 336 |
| Strings | 16,582 |
| Missing strings | 0 |
| Obsolete strings | 0 |
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
| Typography deviations from this locale's own norm | 5 |

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

_227 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1035, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5063, `straight` 11 | **typographic** |
| ellipsis | `char` 401 | **char** |
| dash | `em` 42, `en` 9 | **em** |
| nbsp | `total` 3985, `before-punctuation` 1744 | _mixed_ |
| register | `formal` 2836 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (35)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — "help keep your browsing private from others on this device" loses the "from others" element, changing the claim.
    - Current: `Les fenêtres privées permettent de garder votre navigation privée sur cet appareil.`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Les fenêtres privées permettent de préserver la confidentialité de votre navigation vis-à-vis des autres personnes qui utilisent cet appareil.`
    - The en-US scopes the privacy benefit to other users of the device; the French implies browsing is kept private on the device generally, a broader claim than the source makes.
- `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl` — "You aren’t syncing anything… yet" is rendered as "you don't have to sync anything", changing the meaning.
    - Current: `Vous ne devez rien synchroniser… pour l’instant.`
    - Source: `description: You aren’t syncing anything… yet. Choose what to sync on this device. label: Manage synced data`
    - Suggest: `Vous ne synchronisez rien… pour l’instant.`
    - The en-US states a fact about the current state (nothing is being synced), not an absence of obligation.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 13 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — "help keep your browsing private from others on this device" loses the "from others" element, changing the claim.
    - Current: `Les fenêtres privées permettent de garder votre navigation privée sur cet appareil.`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Les fenêtres privées permettent de préserver la confidentialité de votre navigation vis-à-vis des autres personnes qui utilisent cet appareil.`
    - The en-US scopes the privacy benefit to other users of the device; the French implies browsing is kept private on the device generally, a broader claim than the source makes.
- `ipprotection-site-inclusions-callout-description` — `browser/browser/ipProtection.ftl` — "location-based browsing" is rendered as accessing sites from another location, changing the meaning.
    - Current: `Activez-le sur les sites où vous souhaitez renforcer votre confidentialité ou y accéder depuis un autre emplacement`
    - Source: `Turn it on when you want extra privacy or location-based browsing, and off where you don’t.`
    - Suggest: `Activez-le lorsque vous souhaitez renforcer votre confidentialité ou naviguer en fonction de votre localisation`
    - The en-US says "when you want extra privacy or location-based browsing"; the French adds "sur les sites" and reinterprets it as accessing sites from another location.
- `site-rules-status-heading` — `browser/browser/ipProtection.ftl` — "Your rule" translated as "Règle personnalisée" ("Custom rule") instead of a possessive referring to the user's rule.
    - Current: `Règle personnalisée`
    - Source: `Your rule`
    - Suggest: `Votre règle`
    - The source heading is "Your rule"; "Règle personnalisée" drops the possessive and introduces the notion of customization not present in the source.
- `refresh-unused-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — "for a fresh, like-new experience" rendered as "pour profiter d’une meilleure navigation" ("for better browsing"), a different claim.
    - Current: `pour profiter d’une meilleure navigation ?`
    - Source: `It looks like you haven’t started { -brand-short-name } in a while. Do you want to clean it up for a fresh, like-new experience? And by the way, welcome back!`
    - Suggest: `pour retrouver une expérience comme neuve ?`
    - The en-US promises a fresh, like-new state after cleanup, not improved browsing performance; the French makes a claim the source does not.
- `newtab-custom-widget-crossword-toggle` — `browser/browser/newtab/newtab.ftl` — "Crossword" translated as "Mots fléchés" (arrow-word puzzle), a different puzzle type.
    - Current: `label: Mots fléchés`
    - Source: `label: Crossword`
    - Suggest: `label: Mots croisés`
    - A crossword is "mots croisés" in French; "mots fléchés" is a distinct puzzle format.
- `newtab-stocks-widget-menu-button2` — `browser/browser/newtab/newtab.ftl` — "Finance options" mistranslated as "Options de financement" (funding options).
    - Current: `Options de financement`
    - Source: `aria-label: Finance options title: Finance options`
    - Suggest: `Options de finance`
    - "Finance" here names the finance/stocks widget; "financement" means funding, a different concept.
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — "Keep a chatbot in view" rendered as "Gardez un œil sur un chatbot" (keep an eye on a chatbot), reversing who watches whom.
    - Current: `Gardez un œil sur un chatbot pendant votre navigation.`
    - Source: `description: Keep a chatbot in view as you browse. Choose from multiple providers and switch anytime. label: AI chatbot providers in sidebar`
    - Suggest: `Gardez un chatbot sous les yeux pendant votre navigation.`
    - The en-US means the chatbot stays visible while browsing, not that the user should monitor the chatbot.
- `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl` — "You aren’t syncing anything… yet" is rendered as "you don't have to sync anything", changing the meaning.
    - Current: `Vous ne devez rien synchroniser… pour l’instant.`
    - Source: `description: You aren’t syncing anything… yet. Choose what to sync on this device. label: Manage synced data`
    - Suggest: `Vous ne synchronisez rien… pour l’instant.`
    - The en-US states a fact about the current state (nothing is being synced), not an absence of obligation.
- `tls-key-logging-notice-nav` — `browser/browser/preferences/preferences.ftl` — "may see your encrypted traffic" translated as "pourrait accéder à" (could access), altering the claim.
    - Current: `pourrait accéder à votre trafic chiffré`
    - Source: `label: An app or service may see your encrypted traffic.`
    - Suggest: `pourrait voir votre trafic chiffré`
    - en-US says an app or service may see the traffic; "accéder à" asserts access rather than visibility.
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — "AI Controls" settings section name mangled into "d’IA Controls".
    - Current: `les paramètres d’IA Controls de l’utilisateur`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `les paramètres AI Controls de l’utilisateur`
    - The developer comment says "AI Controls" is the name of a Firefox settings section; half-translating it to "IA Controls" produces a name that does not exist and is grammatically broken.
- `PermissionsPolicyInvalidAllowValue` — `dom/chrome/security/security.properties` — "Skipping" is dropped, so the message no longer says the unsupported value is ignored.
    - Current: `Permissions Policy : valeur allow non prise en charge « %S ».`
    - Source: `Permissions Policy: Skipping unsupported allow value “%S”.`
    - Suggest: `Permissions Policy : valeur allow non prise en charge « %S » ignorée.`
    - en-US "Skipping unsupported allow value" indicates the value is skipped; the French omits that information, unlike the parallel string PermissionsPolicyUnsupportedFeatureName which keeps "ignoré".
- `PermissionsPolicyInvalidEmptyAllowValue` — `dom/chrome/security/security.properties` — The verb "Skipping" (ignored) is dropped, so the message no longer states the list is being skipped.
    - Current: `Permissions Policy : liste allow vide pour la fonctionnalité « %S ».`
    - Source: `Permissions Policy: Skipping empty allow list for feature: “%S”.`
    - Suggest: `Permissions Policy : liste allow vide ignorée pour la fonctionnalité « %S ».`
    - en-US "Skipping empty allow list for feature" states the item is skipped; the French only reports that the list is empty.
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log"/"logs" translated as "entrée(s)" (entries) instead of "journal/journaux", inconsistent with the rest of the file.
    - Current: `[one] { $count } entrée [other] { $count } entrées`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } journal [other] { $count } journaux`
    - The en-US counts logs (files), and the surrounding strings render "logs" as "journaux"; "entrées" means log entries, a different unit.
- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — toolkit/toolkit/about/aboutGlean.ftl:133,135 — both say "axe des abscisses" but EN references the Y-axis → axe des ordonnées; line 135 is also internally contradictory ("décalage vertical … abscisses").
    - Source: `Y-axis X offset`
    - Suggest: `axe des ordonnées`
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — "Log modules" (verb phrase: enable logging for modules) rendered as a noun phrase "Modules de journalisation".
    - Current: `Modules de journalisation pour diagnostiquer`
    - Source: `Log modules to diagnose IP Protection (VPN) issues`
    - Suggest: `Journaliser les modules permettant de diagnostiquer`
    - The source is a description of a logging preset instructing which modules to log; "Modules de journalisation" means "logging modules", a different thing.
- `about-pdf-features-intro` — `toolkit/toolkit/about/aboutPDF.ftl` — "right where you browse" (in the browser itself) is rendered as "où que vous soyez" (wherever you are).
    - Current: `Lisez, annotez et signez des fichiers PDF où que vous soyez.`
    - Source: `Read, mark up, and sign PDFs right where you browse. It’s simple, free, and private.`
    - Suggest: `Lisez, annotez et signez des fichiers PDF directement dans votre navigateur.`
    - The en-US says the PDF tools work right inside the browsing experience, not that they work from anywhere/any location.
- `pdfjs-open-attachments-inline` — `toolkit/toolkit/about/aboutSupport.ftl` — "Inline" mistranslated as "dans les messages", adding a message context absent from the source.
    - Current: `Ouvrir les PDF joints dans les messages`
    - Source: `Open PDF Attachments Inline`
    - Suggest: `Ouvrir les pièces jointes PDF de façon intégrée`
    - The source "Open PDF Attachments Inline" refers to opening attachments inline in the viewer, not within messages.

### C. Grammar, agreement & spelling

- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — Wrong pronoun gender/agreement: "Ils" refers to "Les fenêtres privées" (feminine plural) and should be "Elles".
    - Current: `Ils ne vous rendent pas anonyme`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Elles ne vous rendent pas anonyme`
    - The antecedent is "Les fenêtres privées", feminine plural, so the subject pronoun must be "Elles".
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — Verb "exporter" is in the infinitive instead of the imperative, breaking the list of imperatives.
    - Current: `Réorganisez, supprimez, fusionnez et exporter des pages.`
    - Source: `Reorder, remove, merge, and export pages.`
    - Suggest: `Réorganisez, supprimez, fusionnez et exportez des pages.`
    - The other verbs are imperative (« Réorganisez, supprimez, fusionnez »); « exporter » should be « exportez » to match the en-US imperative "export".

### D. Terminology, register & consistency

- `appmenuitem-share-firefox-title2` — `browser/browser/appmenu.ftl` — "Share { -brand-product-name }" is rendered "Partager" here while all other referral strings use "Recommander".
    - Current: `Partager { -brand-product-name }`
    - Source: `Share { -brand-product-name }`
    - Suggest: `Recommander { -brand-product-name }`
    - The developer comment says this button links to the Referrals page, the same surface as appmenu-referrals2, menu-referrals2 and referrals-link2, which all translate "Share" as "Recommander"; the inconsistent term is wrong here.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Nouveautés” but the string it names, `releaseNotes-link`, reads “Notes de version”
    - Current: `Contrôler la page « Nouveautés » après une mise à jour. Laissez cette règle vide pour désactiver la page après une mise à jour.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Notes de version`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
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
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-cpu-almost-idle (.title) — toolkit/toolkit/about/aboutProcesses.ftl:167 — "Temps CPU total" vs "Temps total de CPU" (lines 161/170); align.
    - Source: `(value): < 0.1% title: Total CPU time: { $total }{ $unit }`
    - Suggest: `.title`

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5063 times against 11 straight.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1035 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1035 occurrences).
- `about-sync-log-row-success` — `toolkit/services/aboutSyncLog.ftl` — Em dash replaced by a colon, inconsistent with the sibling error string.
    - Current: `Succès : { $date }`
    - Source: `heading: Success — { $date }`
    - Suggest: `Succès — { $date }`
    - en-US uses "Success — { $date }" and the parallel string about-sync-log-row-error keeps the em dash in French; the locale convention is the em dash.
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5063 times against 11 straight.
- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — `autocomplete-delete-address-entry` uses a straight apostrophe
    - Current: `Supprimer l'adresse { $entry }`
    - Source: `Delete address { $entry }`
    - The tree uses ’ 5063 times against 11 straight.
- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — Straight apostrophe used instead of the typographic apostrophe required by the locale.
    - Current: `Supprimer l'adresse`
    - Source: `Delete address { $entry }`
    - Suggest: `Supprimer l’adresse`
    - The locale convention is the typographic apostrophe ’ (5633 vs 10).

---

## 4. Appendix

### Dismissed by hand (1)

- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — the message is valid Fluent; the reviewer read the flattened rendering `{$saved ->} [one] …` as if it were the file and reported a stray brace that is not there

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — raised by `accesskey`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (64)

- `ipprotection-feature-introduction-description-inclusions` — `browser/browser/ipProtection.ftl` — fixed 2026-10-05
- `ipprotection-feature-introduction-description-private-browsing-1` — `browser/browser/ipProtection.ftl` — fixed 2026-10-05
- `pdf-features-notification` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — fixed 2026-09-21
- `newtab-privacy-empty-state-tally` — `browser/browser/newtab/newtab.ftl` — fixed 2026-09-14
- `aiwindow-firstrun-default-checkbox-label` — `browser/browser/aiWindow.ftl` — fixed 2026-09-03
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-09-01
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — fixed 2026-08-31
- `about-sync-log-filter-date-all` — `toolkit/services/aboutSyncLog.ftl` — fixed 2026-08-31
- `pdfjs-embed-fallback-open-button` — `toolkit/toolkit/pdfviewer/embedFallback.ftl` — fixed 2026-08-31
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
