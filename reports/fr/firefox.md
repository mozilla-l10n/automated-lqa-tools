# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `324a294b9f2a` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9251d435ac24` |
| **Previous run** | 2026-11-05 @ `181c4859abf3` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 17,089 |

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
| Strings | 17,089 |
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
| apostrophe | `typographic` 5191, `straight` 10 | **typographic** |
| ellipsis | `char` 411 | **char** |
| dash | `em` 45, `en` 9 | **em** |
| nbsp | `total` 4078, `before-punctuation` 1789 | _mixed_ |
| register | `formal` 2930 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (42)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 19 |
| 3 | Degraded language (grammar, spelling, terminology) | 18 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — The tooltip omits the term "fenêtre" for the Classic window, producing the ungrammatical/incomplete "entre une { -smart-window-brand-name } et classique".
    - Current: `Basculer entre une { -smart-window-brand-name } et classique`
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic Windows`
    - Suggest: `Basculer entre les fenêtres { -smart-window-brand-name } et classiques`
    - en-US says "Switch between Smart and Classic Windows"; the French drops the noun for the second item, leaving "et classique" dangling without a noun.
- `contextual-manager-passwords-delete-all-title` — `browser/browser/contextual-manager.ftl` — The singular variant reads as "delete password number 1?" instead of "delete 1 password?".
    - Current: `Supprimer le mot de passe { $total } ?`
    - Source: `{$total ->} [one] Delete { $total } password? [other] Delete { $total } passwords?`
    - Suggest: `Supprimer { $total } mot de passe ?`
    - The source says "Delete { $total } password?". Placing the number after "le mot de passe" turns the count into an identifier.
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
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — The tooltip uses "Open" as a verb, but the source means tabs that are open.
    - Current: `Ouvrir des onglets depuis vos autres appareils`
    - Source: `accesskey: t label: Open tabs tooltiptext: Open tabs from your other devices`
    - Suggest: `Onglets ouverts sur vos autres appareils`
    - The developer comment says "Open tabs" is a modified noun (tabs that are open).
- `tls-key-logging-notice-nav` — `browser/browser/preferences/preferences.ftl` — "may see your encrypted traffic" translated as "pourrait accéder à" (could access), altering the claim.
    - Current: `pourrait accéder à votre trafic chiffré`
    - Source: `label: An app or service may see your encrypted traffic.`
    - Suggest: `pourrait voir votre trafic chiffré`
    - en-US says an app or service may see the traffic; "accéder à" asserts access rather than visibility.
- `move-to-start-alt` — `browser/browser/tabContextMenu.ftl` — "Start" (a position in the tab strip) is translated as the verb "Démarrer".
    - Current: `Démarrer`
    - Source: `accesskey: S label: Start`
    - Suggest: `Début`
    - The developer comment says this moves the tab to the start of the tab strip. It is a position, and it pairs with "Fin".
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — The label reads as "Duplicate the tabs" (a command) instead of naming the duplicate tabs to close.
    - Current: `Dupliquer les onglets`
    - Source: `accesskey: x label: Duplicate Tabs`
    - Suggest: `Onglets en double`
    - The comment says the item, under "Close Multiple", closes duplicates of the selected tab. "Dupliquer" tells the user it copies tabs.
- `SpeechRecognitionLangDefaultedToUserLanguageWarning` — `dom/chrome/dom/dom.properties` — "user’s preferred language" is rendered as "la langue préférée utilisée", which drops the user and reads awkwardly.
    - Current: `la langue préférée utilisée`
    - Source: `SpeechRecognition.lang is unset and this document declares no language, so speech will be recognized in the user’s preferred language. Set SpeechRecognition.lang, or a lang attribute on the document’s root element.`
    - Suggest: `la langue préférée de l’utilisateur`
    - The en-US says speech is recognized in the user’s preferred language. The French "la langue préférée utilisée" ("the preferred language used") leaves out whose preference it is and is unidiomatic.
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
- `about-logging-preset-vpn-description` — `toolkit/toolkit/about/aboutLogging.ftl` — "Log modules" (verb phrase: enable logging for modules) rendered as a noun phrase "Modules de journalisation".
    - Current: `Modules de journalisation pour diagnostiquer`
    - Source: `Log modules to diagnose IP Protection (VPN) issues`
    - Suggest: `Journaliser les modules permettant de diagnostiquer`
    - The source is a description of a logging preset instructing which modules to log; "Modules de journalisation" means "logging modules", a different thing.
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
- `text-action-copy-clean-link-to-highlight-2` — `toolkit/toolkit/global/textActions.ftl` — « lien nettoyé à surligner » means a link to be highlighted, not a clean link pointing to the highlighted text.
    - Current: `Copier le lien nettoyé à surligner`
    - Source: `accesskey: k label: Copy Clean Link to Highlight`
    - Suggest: `Copier le lien nettoyé du surlignage`
    - The developer comment says this creates a link with a text fragment pointing to the current selection, with trackers removed. « à surligner » reads as 'to be highlighted'. It also doesn't match the sibling string « Copier le lien du surlignage ».

### C. Grammar, agreement & spelling

- `extension-classic-oled-name` — `browser/browser/appExtensionFields.ftl` — The acronym OLED is written in lowercase and in an unnatural word order.
    - Current: `Oled noir`
    - Source: `OLED Black`
    - Suggest: `Noir OLED`
    - OLED is an acronym and stays uppercase. The theme is a black theme for OLED screens, so French says "Noir OLED".
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
- `about-processes-site-tab-count` — `toolkit/toolkit/about/aboutProcesses.ftl` — The singular variant puts the noun before the number and keeps it plural: « (onglets 1) ».
    - Current: `(onglets { $count })`
    - Source: `{$count ->} [one] ({ $count } tab) [other] ({ $count } tabs)`
    - Suggest: `({ $count } onglet)`
    - The en-US is "(1 tab)". The French needs the number first and the singular noun, matching the other variant.
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
- `close-tabs-to-the-start-alt` — `browser/browser/tabContextMenu.ftl` — "Tabs" is translated as "Tabulations" instead of "Onglets".
    - Current: `Tabulations à gauche`
    - Source: `accesskey: l label: Tabs to Left`
    - Suggest: `Onglets à gauche`
    - Browser tabs are "onglets" in fr, and the sibling labels use "Onglets". "Tabulations" means tab characters.
- `about-debugging-worker-status-running` — `devtools/client/aboutdebugging.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
    - Source: `Running`
- `serviceworker-worker-status-running` — `devtools/client/application.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
    - Source: `Running`
- `dom-manifest-image-unsupported-purposes` — `dom/dom/manifest.ftl` — The plural variant uses « fins » for "purposes" while the singular variant and sibling strings use « objectif(s) ».
    - Current: `contient des fins non prises en charge`
    - Source: `{$count ->} [one] { $memberName } item at index { $index } includes an unsupported purpose: { $purposes }. [other] { $memberName } item at index { $index } includes unsupported purposes: { $purposes }.`
    - Suggest: `possède des objectifs non pris en charge`
    - The same term "purpose" is translated differently within one message and across the manifest strings.
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-cpu-almost-idle (.title) — toolkit/toolkit/about/aboutProcesses.ftl:167 — "Temps CPU total" vs "Temps total de CPU" (lines 161/170); align.
    - Source: `(value): < 0.1% title: Total CPU time: { $total }{ $unit }`
    - Suggest: `.title`
- `about-processes-reload-site` — `toolkit/toolkit/about/aboutProcesses.ftl` — "Reload" is « Recharger » here but « Actualiser » in the other reload strings, and « depuis » wrongly suggests the reload comes from the site.
    - Current: `Recharger les onglets depuis { $site }`
    - Source: `title: Reload tabs from { $site }`
    - Suggest: `Actualiser les onglets de { $site }`
    - about-processes-reload-tab and bulk-reload-tabs use « Actualiser ». "Tabs from site" means the tabs belonging to the site, as the unload string's « de » shows.

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5191 times against 10 straight.
- `sync-engine-payment-methods3` — `browser/browser/preferences/preferences.ftl` — The tooltip starts with a lowercase letter.
    - Current: `moyens de paiement enregistrés`
    - Source: `accesskey: n label: Payment methods tooltiptext: Payment methods you’ve saved`
    - Suggest: `Moyens de paiement enregistrés`
    - The source and the sibling tooltips start with a capital letter.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1053 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `guillemet` (1053 occurrences).
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5191 times against 10 straight.

---

## 4. Appendix

### Dismissed by hand (2)

- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — pontoon-rejected (2026-11-02): rejected in Pontoon without comment; reason unclear
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — the message is valid Fluent; the reviewer read the flattened rendering `{$saved ->} [one] …` as if it were the file and reported a stray brace that is not there

_One line each in `locales/fr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — raised by `accesskey`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (80)

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
