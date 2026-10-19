# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-12 @ `9b5f3e8ca0a3` |
| **Mode** | incremental |
| **Strings reviewed this run** | 139 of 16,742 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (4)

- `ipprotection-site-inclusions-callout-description-1` — `browser/browser/ipProtection.ftl` — The end of the sentence means "where you don't have any" instead of "where you don't want/need it".
    - Current: `là où vous n’en avez pas.`
    - Source: `Turn on VPN when you want extra privacy or location-based browsing, and off where you don’t.`
    - Suggest: `là où vous n’en avez pas besoin.`
    - The en-US "and off where you don’t" means where you don't want the VPN on. The French "là où vous n’en avez pas" cuts off the verb and reads as "where you don't have any", which makes no sense here.
- `view-source-invalid-input-text` — `toolkit/toolkit/global/viewSource.ftl` — "Line number" is rendered as "nombre" (an amount) with no mention of a line, and the final period is missing.
    - Current: `Le nombre spécifié est invalide`
    - Source: `The line number entered is invalid.`
    - Suggest: `Le numéro de ligne saisi est invalide.`
    - The source says "The line number entered is invalid." "Nombre" means a quantity, not an identifying number ("numéro"). The word "ligne" is dropped, which doesn't match the sibling string "Saisissez le numéro de ligne". The source also ends with a full stop.
- `tab-groups-onboarding-session-restore-title-3` — `browser/browser/newtab/onboarding.ftl` — The phrase « à tout moment » appears twice in the same sentence.
    - Current: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets » à tout moment.`
    - Source: `Reopen your tab groups from the “Search and manage tabs” menu anytime.`
    - Suggest: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets ».`
    - The en-US has 'anytime' only once. Saying « à tout moment » twice is a redundancy error that makes the sentence ungrammatical in French.
- `SpeechRecognitionLangDefaultedToUserLanguageWarning` — `dom/chrome/dom/dom.properties` — "user’s preferred language" is rendered as "la langue préférée utilisée", which drops the user and reads awkwardly.
    - Current: `la langue préférée utilisée`
    - Source: `SpeechRecognition.lang is unset and this document declares no language, so speech will be recognized in the user’s preferred language. Set SpeechRecognition.lang, or a lang attribute on the document’s root element.`
    - Suggest: `la langue préférée de l’utilisateur`
    - The en-US says speech is recognized in the user’s preferred language. The French "la langue préférée utilisée" ("the preferred language used") leaves out whose preference it is and is unidiomatic.

### ✅ Fixed since the last run (3)

- `genai-prompts-summarize-page` — `browser/browser/genai.ftl` — Redundant/incorrect phrasing "résumer l’adresse web à l’adresse" instead of summarizing the webpage at the URL.
    - Current: `Veuillez résumer l’adresse web à l’adresse { $url }`
    - Source: `Please summarize the webpage at { $url } using precise and concise language. Use headers and bulleted lists in the summary, to make it scannable. Maintain the meaning and factual accuracy.`
    - Suggest: `Veuillez résumer la page web à l’adresse { $url }`
    - The source asks to summarize the webpage at $url; the French says "summarize the web address at the address $url", duplicating "adresse" and naming the wrong object.
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — "AI Controls" settings section name mangled into "d’IA Controls".
    - Current: `les paramètres d’IA Controls de l’utilisateur`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `les paramètres AI Controls de l’utilisateur`
    - The developer comment says "AI Controls" is the name of a Firefox settings section; half-translating it to "IA Controls" produces a name that does not exist and is grammatically broken.
- `about-sync-log-row-success` — `toolkit/services/aboutSyncLog.ftl` — Em dash replaced by a colon, inconsistent with the sibling error string.
    - Current: `Succès : { $date }`
    - Source: `heading: Success — { $date }`
    - Suggest: `Succès — { $date }`
    - en-US uses "Success — { $date }" and the parallel string about-sync-log-row-error keeps the em dash in French; the locale convention is the em dash.

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
| Files | 338 |
| Strings | 16,742 |
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

_222 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1044, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5118, `straight` 10 | **typographic** |
| ellipsis | `char` 409 | **char** |
| dash | `em` 43, `en` 9 | **em** |
| nbsp | `total` 4012, `before-punctuation` 1753 | _mixed_ |
| register | `formal` 2858 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (33)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 15 |
| 3 | Degraded language (grammar, spelling, terminology) | 14 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — The tooltip omits the term "fenêtre" for the Classic window, producing the ungrammatical/incomplete "entre une { -smart-window-brand-name } et classique".
    - Current: `Basculer entre une { -smart-window-brand-name } et classique`
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic Windows`
    - Suggest: `Basculer entre les fenêtres { -smart-window-brand-name } et classiques`
    - en-US says "Switch between Smart and Classic Windows"; the French drops the noun for the second item, leaving "et classique" dangling without a noun.
- `appmenuitem-relay-description2` — `browser/browser/appmenu.ftl` — "Helps prevent spam" (descriptive, hedged) rendered as an imperative "Limitez le spam", dropping the "helps" hedge and changing the statement into a user instruction.
    - Current: `Limitez le spam dans votre boîte de réception`
    - Source: `Helps prevent spam in your inbox`
    - Suggest: `Aide à limiter le spam dans votre boîte de réception`
    - The en-US is a description of what the feature does, hedged with "Helps"; the French turns it into an imperative promise to the user.
- `ipprotection-site-inclusions-callout-description` — `browser/browser/ipProtection.ftl` — "location-based browsing" is rendered as accessing sites from another location, changing the meaning.
    - Current: `Activez-le sur les sites où vous souhaitez renforcer votre confidentialité ou y accéder depuis un autre emplacement`
    - Source: `Turn it on when you want extra privacy or location-based browsing, and off where you don’t.`
    - Suggest: `Activez-le lorsque vous souhaitez renforcer votre confidentialité ou naviguer en fonction de votre localisation`
    - The en-US says "when you want extra privacy or location-based browsing"; the French adds "sur les sites" and reinterprets it as accessing sites from another location.
- `ipprotection-site-inclusions-callout-description-1` — `browser/browser/ipProtection.ftl` — The end of the sentence means "where you don't have any" instead of "where you don't want/need it".
    - Current: `là où vous n’en avez pas.`
    - Source: `Turn on VPN when you want extra privacy or location-based browsing, and off where you don’t.`
    - Suggest: `là où vous n’en avez pas besoin.`
    - The en-US "and off where you don’t" means where you don't want the VPN on. The French "là où vous n’en avez pas" cuts off the verb and reads as "where you don't have any", which makes no sense here.
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
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — "Keep a chatbot in view" rendered as "Gardez un œil sur un chatbot" (keep an eye on a chatbot), reversing who watches whom.
    - Current: `Gardez un œil sur un chatbot pendant votre navigation.`
    - Source: `description: Keep a chatbot in view as you browse. Choose from multiple providers and switch anytime. label: AI chatbot providers in sidebar`
    - Suggest: `Gardez un chatbot sous les yeux pendant votre navigation.`
    - The en-US means the chatbot stays visible while browsing, not that the user should monitor the chatbot.
- `tls-key-logging-notice-nav` — `browser/browser/preferences/preferences.ftl` — "may see your encrypted traffic" translated as "pourrait accéder à" (could access), altering the claim.
    - Current: `pourrait accéder à votre trafic chiffré`
    - Source: `label: An app or service may see your encrypted traffic.`
    - Suggest: `pourrait voir votre trafic chiffré`
    - en-US says an app or service may see the traffic; "accéder à" asserts access rather than visibility.
- `SpeechRecognitionLangDefaultedToUserLanguageWarning` — `dom/chrome/dom/dom.properties` — "user’s preferred language" is rendered as "la langue préférée utilisée", which drops the user and reads awkwardly.
    - Current: `la langue préférée utilisée`
    - Source: `SpeechRecognition.lang is unset and this document declares no language, so speech will be recognized in the user’s preferred language. Set SpeechRecognition.lang, or a lang attribute on the document’s root element.`
    - Suggest: `la langue préférée de l’utilisateur`
    - The en-US says speech is recognized in the user’s preferred language. The French "la langue préférée utilisée" ("the preferred language used") leaves out whose preference it is and is unidiomatic.
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

- `tab-groups-onboarding-session-restore-title-3` — `browser/browser/newtab/onboarding.ftl` — The phrase « à tout moment » appears twice in the same sentence.
    - Current: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets » à tout moment.`
    - Source: `Reopen your tab groups from the “Search and manage tabs” menu anytime.`
    - Suggest: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets ».`
    - The en-US has 'anytime' only once. Saying « à tout moment » twice is a redundancy error that makes the sentence ungrammatical in French.
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
- `view-source-invalid-input-text` — `toolkit/toolkit/global/viewSource.ftl` — "Line number" is rendered as "nombre" (an amount) with no mention of a line, and the final period is missing.
    - Current: `Le nombre spécifié est invalide`
    - Source: `The line number entered is invalid.`
    - Suggest: `Le numéro de ligne saisi est invalide.`
    - The source says "The line number entered is invalid." "Nombre" means a quantity, not an identifying number ("numéro"). The word "ligne" is dropped, which doesn't match the sibling string "Saisissez le numéro de ligne". The source also ends with a full stop.

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5118 times against 10 straight.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1044 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1044 occurrences).
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5118 times against 10 straight.

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

### Fixed to date (72)

- `genai-prompts-summarize-page` — `browser/browser/genai.ftl` — fixed 2026-10-19
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — fixed 2026-10-19
- `about-sync-log-row-success` — `toolkit/services/aboutSyncLog.ftl` — fixed 2026-10-19
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-10-12
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-10-12
- `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-10-12
- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — fixed 2026-10-12
- `autocomplete-delete-address-entry` — `toolkit/toolkit/main-window/autocomplete.ftl` — fixed 2026-10-12
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
