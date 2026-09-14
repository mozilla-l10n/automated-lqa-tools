# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `e44f1369fb6d` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `8ffd279d75ec` |
| **Previous run** | 2026-09-07 @ `3c0c507b8d42` |
| **Mode** | incremental |
| **Strings reviewed this run** | 115 of 16,368 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (7)

- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Nouveautés” but the string it names, `releaseNotes-link`, reads “Notes de version”
    - Current: `Contrôler la page « Nouveautés » après une mise à jour. Laissez cette règle vide pour désactiver la page après une mise à jour.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Notes de version`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `fxa-menu-signed-out-description` — `browser/browser/sync.ftl` — "You’re signed out" is rendered as "Déconnexion réussie" ("Sign-out successful"), asserting a successful action rather than stating the current state.
    - Current: `Déconnexion réussie`
    - Source: `You’re signed out`
    - Suggest: `Vous êtes déconnecté·e`
    - The en-US states a status (the user is signed out); the French claims the sign-out operation succeeded, which is a different assertion and misleading in the app menu row where it stands in for the email.
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
- `about-sync-log-row-success` — `toolkit/services/aboutSyncLog.ftl` — Em dash replaced by a colon, inconsistent with the sibling error string.
    - Current: `Succès : { $date }`
    - Source: `heading: Success — { $date }`
    - Suggest: `Succès — { $date }`
    - en-US uses "Success — { $date }" and the parallel string about-sync-log-row-error keeps the em dash in French; the locale convention is the em dash.
- `pdf-features-notification` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — aria-label pluralized and heading adds "à télécharger" (to download), which the source never says.
    - Current: `Les fichiers PDF sont encore plus faciles à télécharger en { -brand-short-name }.`
    - Source: `aria-label: Notification heading: PDFs just got easier in { -brand-short-name }.`
    - Suggest: `Les fichiers PDF sont encore plus faciles à utiliser dans { -brand-short-name }.`
    - Source is "PDFs just got easier in { -brand-short-name }." — nothing about downloading; also "en" should be "dans" before the brand name, and aria-label "Notification" was rendered as plural "Notifications".
- `pdfjs-open-attachments-inline` — `toolkit/toolkit/about/aboutSupport.ftl` — "Inline" mistranslated as "dans les messages", adding a message context absent from the source.
    - Current: `Ouvrir les PDF joints dans les messages`
    - Source: `Open PDF Attachments Inline`
    - Suggest: `Ouvrir les pièces jointes PDF de façon intégrée`
    - The source "Open PDF Attachments Inline" refers to opening attachments inline in the viewer, not within messages.

### ✅ Fixed since the last run (1)

- `newtab-privacy-empty-state-tally` — `browser/browser/newtab/newtab.ftl` — "running tally" rendered as "pointage", a scoring term that does not convey a running total of blocked trackers.
    - Current: `Consultez le pointage en cours ici.`
    - Source: `See a running tally here.`
    - Suggest: `Consultez le total en cours ici.`
    - The comment explains "a running tally" is a total that keeps updating (alternative: "See a running total here"); "pointage" means a score/tally-mark in a game context and is misleading here.

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
| Strings | 16,368 |
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

_200 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1027, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5013, `straight` 10 | **typographic** |
| ellipsis | `char` 400 | **char** |
| dash | `em` 42, `en` 8 | **em** |
| nbsp | `total` 3940, `before-punctuation` 1720 | _mixed_ |
| register | `formal` 2776 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (24)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `fxa-menu-signed-out-description` — `browser/browser/sync.ftl` — "You’re signed out" is rendered as "Déconnexion réussie" ("Sign-out successful"), asserting a successful action rather than stating the current state.
    - Current: `Déconnexion réussie`
    - Source: `You’re signed out`
    - Suggest: `Vous êtes déconnecté·e`
    - The en-US states a status (the user is signed out); the French claims the sign-out operation succeeded, which is a different assertion and misleading in the app menu row where it stands in for the email.
- `pdf-features-notification` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — aria-label pluralized and heading adds "à télécharger" (to download), which the source never says.
    - Current: `Les fichiers PDF sont encore plus faciles à télécharger en { -brand-short-name }.`
    - Source: `aria-label: Notification heading: PDFs just got easier in { -brand-short-name }.`
    - Suggest: `Les fichiers PDF sont encore plus faciles à utiliser dans { -brand-short-name }.`
    - Source is "PDFs just got easier in { -brand-short-name }." — nothing about downloading; also "en" should be "dans" before the brand name, and aria-label "Notification" was rendered as plural "Notifications".

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 11 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

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
- `fxa-menu-signed-out-description` — `browser/browser/sync.ftl` — "You’re signed out" is rendered as "Déconnexion réussie" ("Sign-out successful"), asserting a successful action rather than stating the current state.
    - Current: `Déconnexion réussie`
    - Source: `You’re signed out`
    - Suggest: `Vous êtes déconnecté·e`
    - The en-US states a status (the user is signed out); the French claims the sign-out operation succeeded, which is a different assertion and misleading in the app menu row where it stands in for the email.
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — "AI Controls" settings section name mangled into "d’IA Controls".
    - Current: `les paramètres d’IA Controls de l’utilisateur`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `les paramètres AI Controls de l’utilisateur`
    - The developer comment says "AI Controls" is the name of a Firefox settings section; half-translating it to "IA Controls" produces a name that does not exist and is grammatically broken.
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log"/"logs" translated as "entrée(s)" (entries) instead of "journal/journaux", inconsistent with the rest of the file.
    - Current: `[one] { $count } entrée [other] { $count } entrées`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } journal [other] { $count } journaux`
    - The en-US counts logs (files), and the surrounding strings render "logs" as "journaux"; "entrées" means log entries, a different unit.
- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — toolkit/toolkit/about/aboutGlean.ftl:133,135 — both say "axe des abscisses" but EN references the Y-axis → axe des ordonnées; line 135 is also internally contradictory ("décalage vertical … abscisses").
    - Source: `Y-axis X offset`
    - Suggest: `axe des ordonnées`
- `pdfjs-open-attachments-inline` — `toolkit/toolkit/about/aboutSupport.ftl` — "Inline" mistranslated as "dans les messages", adding a message context absent from the source.
    - Current: `Ouvrir les PDF joints dans les messages`
    - Source: `Open PDF Attachments Inline`
    - Suggest: `Ouvrir les pièces jointes PDF de façon intégrée`
    - The source "Open PDF Attachments Inline" refers to opening attachments inline in the viewer, not within messages.
- `pdf-features-notification` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — aria-label pluralized and heading adds "à télécharger" (to download), which the source never says.
    - Current: `Les fichiers PDF sont encore plus faciles à télécharger en { -brand-short-name }.`
    - Source: `aria-label: Notification heading: PDFs just got easier in { -brand-short-name }.`
    - Suggest: `Les fichiers PDF sont encore plus faciles à utiliser dans { -brand-short-name }.`
    - Source is "PDFs just got easier in { -brand-short-name }." — nothing about downloading; also "en" should be "dans" before the brand name, and aria-label "Notification" was rendered as plural "Notifications".

### C. Grammar, agreement & spelling

_Nothing in this category._

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
    - The tree uses ’ 5013 times against 10 straight.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1027 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1027 occurrences).
- `about-sync-log-row-success` — `toolkit/services/aboutSyncLog.ftl` — Em dash replaced by a colon, inconsistent with the sibling error string.
    - Current: `Succès : { $date }`
    - Source: `heading: Success — { $date }`
    - Suggest: `Succès — { $date }`
    - en-US uses "Success — { $date }" and the parallel string about-sync-log-row-error keeps the em dash in French; the locale convention is the em dash.
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5013 times against 10 straight.

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

### Fixed to date (61)

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
- `tabbrowser-manager-mute-tab` — `browser/browser/tabbrowser.ftl` — fixed 2026-07-26
- `accessibility-text-label-issue-area` — `devtools/client/accessibility.ftl` — fixed 2026-07-26
- `network-menu-summary-tooltip-domcontentloaded` — `devtools/client/netmonitor.ftl` — fixed 2026-07-26
