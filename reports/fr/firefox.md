# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `74047c5347bc` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-09 @ `f82b652e600a` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,104 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 341 |
| Strings | 17,104 |
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

_229 strings. These files exist in the locale tree but not in the en-US reference — they are maintained elsewhere. The model review is a comparison against en-US, so it skips them entirely; only the checks that need no reference ran. Nothing reported from these files means nothing was looked for, not that they are clean._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1053, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5194, `straight` 10 | **typographic** |
| ellipsis | `char` 411 | **char** |
| dash | `em` 45, `en` 9 | **em** |
| nbsp | `total` 4079, `before-punctuation` 1789 | _mixed_ |
| register | `formal` 2930 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (20)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 13 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — The tooltip omits the term "fenêtre" for the Classic window, producing the ungrammatical/incomplete "entre une { -smart-window-brand-name } et classique".
    - Current: `Basculer entre une { -smart-window-brand-name } et classique`
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic Windows`
    - Suggest: `Basculer entre les fenêtres { -smart-window-brand-name } et classiques`
    - en-US says "Switch between Smart and Classic Windows"; the French drops the noun for the second item, leaving "et classique" dangling without a noun.
- `contextual-manager-passwords-delete-all-confirm-button` — `browser/browser/contextual-manager.ftl` — The singular variant says “Tout supprimer” (Delete all), but the source says just “Delete” when there is one password.
    - Current: `[one] Tout supprimer`
    - Source: `{$total ->} [1] Delete [other] Delete all`
    - Suggest: `[one] Supprimer`
    - The en-US deliberately uses “Delete” for one password and “Delete all” for several. The French uses “Delete all” in both cases.
- `newtab-widget-wrexhamafc-view-table` — `browser/browser/newtab/newtab.ftl` — In football, “Table” means the league table, which is “Classement” in French, not “Tableau”.
    - Current: `Tableau`
    - Source: `Table`
    - Suggest: `Classement`
    - The view options Matches/Table/Fixtures are football terms. Here “Table” is the league standings, and French says “classement” for that. “Tableau” reads as a generic table or chart.
- `hnt-card-extensions-header` — `browser/browser/newtab/onboarding.ftl` — The header is garbled and ungrammatical, and does not say "Boost Firefox with extensions".
    - Current: `Plus de { -brand-short-name } d’extensions`
    - Source: `Boost { -brand-short-name } with extensions`
    - Suggest: `Boostez { -brand-short-name } avec des extensions`
    - The en-US says "Boost {brand} with extensions". The French "Plus de Firefox d’extensions" reads roughly as "more of Firefox of extensions". It is ungrammatical and does not get the meaning across.
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — "Keep a chatbot in view" rendered as "Gardez un œil sur un chatbot" (keep an eye on a chatbot), reversing who watches whom.
    - Current: `Gardez un œil sur un chatbot pendant votre navigation.`
    - Source: `description: Keep a chatbot in view as you browse. Choose from multiple providers and switch anytime. label: AI chatbot providers in sidebar`
    - Suggest: `Gardez un chatbot sous les yeux pendant votre navigation.`
    - The en-US means the chatbot stays visible while browsing, not that the user should monitor the chatbot.
- `ConnectionAllowlistRedirectBlocked` — `dom/chrome/security/security.properties` — The do-not-translate identifier Connection-Allowlist was translated as « Connexion-Allowlist ».
    - Current: `Connexion-Allowlist`
    - Source: `Connection-Allowlist: The page’s settings blocked a redirect of %1$S.`
    - Suggest: `Connection-Allowlist`
    - The developer comment says not to translate Connection-Allowlist. It is a header/policy name, and the sibling string keeps it in English.
- `ConnectionAllowlistReportOnlyRedirectBlocked` — `dom/chrome/security/security.properties` — "Redirect of %1$S" became "redirection vers %1$S" (redirect to).
    - Current: `une redirection vers %1$S`
    - Source: `Connection-Allowlist: (Report-Only policy) The page’s settings would block a redirect of %1$S.`
    - Suggest: `une redirection de %1$S`
    - The comment says %1$S is the URI of the resource that was redirected, not where it was redirected to. The sibling string correctly uses « de ».
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — "The scope URL" was rendered as « La portée de l’URL » (the scope of the URL).
    - Current: `La portée de l’URL doit`
    - Source: `The scope URL must be same origin as document.`
    - Suggest: `L’URL de portée doit`
    - It is the scope URL that must share the document's origin, not the scope of a URL.
- `dom-manifest-scope-url-invalid` — `dom/dom/manifest.ftl` — "The scope URL" was rendered as « La portée de l’URL » (the scope of the URL).
    - Current: `La portée de l’URL est invalide.`
    - Source: `The scope URL is invalid.`
    - Suggest: `L’URL de portée est invalide.`
    - The message is about the manifest's scope URL being invalid, not about the scope of some URL.
- `pippki-get-pkcs12-password-message` — `security/manager/security/pippki/pippki.ftl` — The prompt is garbled and doesn't say this is the password used to encrypt the certificate backup.
    - Current: `Veuillez saisir le mot de passe portable de sécurité protégeant ce certificat de sécurité et la clé privée :`
    - Source: `Please enter the password that was used to encrypt this certificate backup:`
    - Suggest: `Veuillez saisir le mot de passe utilisé pour chiffrer cette sauvegarde de certificat :`
    - The source asks for the password that was used to encrypt this certificate backup. "mot de passe portable de sécurité" is meaningless, and the private key and "certificat de sécurité" are not in the source.
- `about-sync-log-count` — `toolkit/services/aboutSyncLog.ftl` — "log"/"logs" translated as "entrée(s)" (entries) instead of "journal/journaux", inconsistent with the rest of the file.
    - Current: `[one] { $count } entrée [other] { $count } entrées`
    - Source: `{$count ->} [one] { $count } log [other] { $count } logs`
    - Suggest: `[one] { $count } journal [other] { $count } journaux`
    - The en-US counts logs (files), and the surrounding strings render "logs" as "journaux"; "entrées" means log entries, a different unit.
- `pdfjs-open-attachments-inline` — `toolkit/toolkit/about/aboutSupport.ftl` — "Inline" mistranslated as "dans les messages", adding a message context absent from the source.
    - Current: `Ouvrir les PDF joints dans les messages`
    - Source: `Open PDF Attachments Inline`
    - Suggest: `Ouvrir les pièces jointes PDF de façon intégrée`
    - The source "Open PDF Attachments Inline" refers to opening attachments inline in the viewer, not within messages.
- `download-ui-confirm-offline-message` — `toolkit/toolkit/downloads/downloadUI.ftl` — "progress may be lost" is rendered as a progress being interrupted.
    - Current: `mais une progression pourra être interrompue`
    - Source: `{ -brand-short-name } will try to resume downloads when you’re back online, but progress may be lost.`
    - Suggest: `mais leur progression pourrait être perdue`
    - The source says progress may be lost, not interrupted. The matching quit message correctly uses "perdue".

### C. Grammar, agreement & spelling

- `tab-groups-onboarding-session-restore-title-3` — `browser/browser/newtab/onboarding.ftl` — The phrase « à tout moment » appears twice in the same sentence.
    - Current: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets » à tout moment.`
    - Source: `Reopen your tab groups from the “Search and manage tabs” menu anytime.`
    - Suggest: `Rouvrez à tout moment vos groupes d’onglets depuis le menu « Rechercher et gérer les onglets ».`
    - The en-US has 'anytime' only once. Saying « à tout moment » twice is a redundancy error that makes the sentence ungrammatical in French.
- `sync-engine-settings2` — `browser/browser/preferences/preferences.ftl` — The tooltip keeps English word order and isn't grammatical French.
    - Current: `{ -brand-short-name } paramètres le cas échéant`
    - Source: `accesskey: s label: Settings tooltiptext: { -brand-short-name } settings where applicable`
    - Suggest: `Paramètres de { -brand-short-name }, le cas échéant`
    - French needs "Paramètres de X". A brand name placed before the noun is not grammatical.
- `download-ui-confirm-offline-title` — `toolkit/toolkit/downloads/downloadUI.ftl` — The [1] variant adds a spurious pronoun, giving the ungrammatical "et le passer hors connexion".
    - Current: `et le passer hors connexion`
    - Source: `{$downloadsCount ->} [1] Stop 1 download and go offline? [other] Stop { $downloadsCount } downloads and go offline?`
    - Suggest: `et passer hors connexion`
    - The source says "Stop 1 download and go offline?". "le passer" makes the download the object of going offline, which is ungrammatical and doesn't match the other variants.

### D. Terminology, register & consistency

- `genai-menu-summarize-with-ai` — `browser/browser/genai.ftl` — The menu command uses the imperative instead of the infinitive used for French menu items.
    - Current: `Résumez avec l’IA`
    - Source: `Summarize with AI`
    - Suggest: `Résumer avec l’IA`
    - French Firefox menu commands use the infinitive, as the sibling string "Demander à l’IA…" does. The imperative "Résumez" is inconsistent with that.
- `dom-manifest-image-unsupported-purposes` — `dom/dom/manifest.ftl` — The plural variant uses « fins » for "purposes" while the singular variant and sibling strings use « objectif(s) ».
    - Current: `contient des fins non prises en charge`
    - Source: `{$count ->} [one] { $memberName } item at index { $index } includes an unsupported purpose: { $purposes }. [other] { $memberName } item at index { $index } includes unsupported purposes: { $purposes }.`
    - Suggest: `possède des objectifs non pris en charge`
    - The same term "purpose" is translated differently within one message and across the manifest strings.

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5194 times against 10 straight.
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5194 times against 10 straight.

---

## 4. Appendix

### Dismissed by hand (3)

- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — the message is valid Fluent; the reviewer read the flattened rendering `{$saved ->} [one] …` as if it were the file and reported a stray brace that is not there
- `text-action-copy-clean-link-to-highlight-2` — `toolkit/toolkit/global/textActions.ftl` — pontoon-rejected (2026-11-09): rejected in Pontoon without comment; likely reason (inferred): The suggestion was the same as the original ("C"), so it changed nothing; the finding is about the wording of the label, not this accesskey value.

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (12)

- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — auto-suggest (2026-11-09, string 8360ea4e): unreliable finding: The quotes delimit code-like attribute values (key="%S"), where straight quotes are plausible and guillemets would be odd.
- `WinConflict2` — `dom/chrome/dom/dom.properties` — auto-suggest (2026-11-09, string b70cb64b): unreliable finding: The quotes delimit code-like attribute values (key="%S"), where straight quotes are plausible and guillemets would be odd.
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — auto-suggest (2026-11-09, string fbc154d8): unreliable finding: "Log modules" in a preset description can be read as a noun phrase, so « Modules de journalisation » is plausible.
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — auto-suggest (2026-11-09, string d97dc52d): unreliable finding: The finding gives no quote or rationale, and the sibling wording it mentions cannot be checked here; « Temps CPU total » is correct as it stands.
- `fonts-default-serif` — `browser/browser/preferences/fonts.ftl` — auto-suggest (2026-11-09, string bc03c67e): unreliable finding: « Serif » is correct as is; the finding gives no evidence which spelling should prevail.
- `fonts-sans-serif` — `browser/browser/preferences/fonts.ftl` — auto-suggest (2026-11-09, string c8d1069a): unreliable finding: Both « sérif » and « serif » are accepted French spellings; without seeing the sibling lines it cannot be determined which side is the outlier to align.
- `fonts-serif` — `browser/browser/preferences/fonts.ftl` — auto-suggest (2026-11-09, string 0ebde28e): unreliable finding: Both « Sérif » and « Serif » are accepted French spellings; which form the file should settle on cannot be confirmed from here.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — auto-suggest (2026-11-09, string f756ccb7): unreliable finding: « Nouveautés » is the usual French name for the post-update page; it is unclear the policy text must match the link label.
- `refresh-unused-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl` — auto-suggest (2026-11-09, string a0163a27): unreliable finding: « coup de jeune » already conveys the fresh/like-new idea; the rest is acceptable marketing adaptation.
- `serviceworker-worker-status-running` — `devtools/client/application.ftl` — auto-suggest (2026-11-09, string 5bffb1ab): unreliable finding: « En cours d’exécution » is the correct rendering of Running; any alignment should be done on the other file's terse « Exécution », not here.
- `site-rules-status-heading` — `browser/browser/ipProtection.ftl` — auto-suggest (2026-11-09, string ebbcc306): unreliable finding: « Règle personnalisée » is a plausible, idiomatic heading for a user-set rule; the change is stylistic.
- `tls-key-logging-notice-nav` — `browser/browser/preferences/preferences.ftl` — auto-suggest (2026-11-09, string 730bf67e): unreliable finding: « pourrait accéder à » conveys essentially the same possibility as « may see »; the change is stylistic.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/fr/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — raised by `accesskey`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (92)

- `newtab-widget-wrexhamafc-view-matches` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-09
- `about-debugging-worker-status-running` — `devtools/client/aboutdebugging.ftl` — fixed 2026-11-09
- `extension-classic-oled-name` — `browser/browser/appExtensionFields.ftl` — fixed 2026-11-08
- `contextual-manager-passwords-delete-all-title` — `browser/browser/contextual-manager.ftl` — fixed 2026-11-08
- `sync-engine-payment-methods3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-08
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-08
- `close-tabs-to-the-start-alt` — `browser/browser/tabContextMenu.ftl` — fixed 2026-11-08
- `move-to-start-alt` — `browser/browser/tabContextMenu.ftl` — fixed 2026-11-08
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — fixed 2026-11-08
- `SpeechRecognitionLangDefaultedToUserLanguageWarning` — `dom/chrome/dom/dom.properties` — fixed 2026-11-08
- `about-processes-reload-site` — `toolkit/toolkit/about/aboutProcesses.ftl` — fixed 2026-11-08
- `about-processes-site-tab-count` — `toolkit/toolkit/about/aboutProcesses.ftl` — fixed 2026-11-08
- `newtab-custom-widget-crossword-toggle` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-02
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — fixed 2026-11-02
- `PermissionsPolicyInvalidAllowValue` — `dom/chrome/security/security.properties` — fixed 2026-11-02
- `PermissionsPolicyInvalidEmptyAllowValue` — `dom/chrome/security/security.properties` — fixed 2026-11-02
- `about-pdf-feature-organize-description` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-02
- `about-pdf-features-intro` — `toolkit/toolkit/about/aboutPDF.ftl` — fixed 2026-11-02
- `view-source-invalid-input-text` — `toolkit/toolkit/global/viewSource.ftl` — fixed 2026-11-02
- `ipprotection-site-inclusions-callout-description-1` — `browser/browser/ipProtection.ftl` — fixed 2026-10-26
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
