# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-11-23 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `4f181c236f19` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `aadbf7c9bb44` |
| **Previous run** | 2026-11-16 @ `d1d139c060cf` |
| **Mode** | incremental |
| **Strings reviewed this run** | 317 of 17,349 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fr: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (5)

- `smartwindow-onboarding-default-window` — `browser/browser/aiWindow.ftl` — "from other apps" is rendered as "depuis { -brand-short-name }", so the French talks about links opened from Firefox itself.
    - Current: `à l’ouverture de liens depuis { -brand-short-name }`
    - Source: `description: Use it when { -brand-short-name } starts, restarts, or opens links from other apps. label: Start in { -smart-window-brand-name }`
    - Suggest: `à l’ouverture de liens depuis d’autres applications, au démarrage ou au redémarrage de { -brand-short-name }`
    - The en-US means links opened from other apps when Firefox starts or restarts. The French drops "other apps" and says the links come from Firefox, which is a different fact.
- `smartwindow-onboarding-memories-description` — `browser/browser/aiWindow.ftl` — The indirect object pronoun "leur" is wrongly written "leurs".
    - Current: `Ces souvenirs leurs permettent`
    - Source: `{ -smart-window-brand-name } can learn from chats, browsing, or both to create memories. It uses them to personalize your experience over time.`
    - Suggest: `Ces souvenirs leur permettent`
    - Before a verb, the pronoun "leur" never takes an s.
- `ai-window-memories-section-v2` — `browser/browser/aiFeatures.ftl` — "Memories" is rendered as "mémoires" in the description but as "Souvenirs" in the label of the same string and in the onboarding strings.
    - Current: `pour créer des mémoires. Elles sont utilisées`
    - Source: `description: { -brand-short-name } can learn from your activity to create memories. They’re used to help tailor your experience and are stored locally on your device. label: Memories`
    - Suggest: `pour créer des souvenirs. Ils sont utilisés`
    - The feature is called "Souvenirs" everywhere else. "Des mémoires" can read as memoirs or computer memory, so it is the wrong term here.
- `about-webauthn-logging-warning` — `toolkit/toolkit/about/aboutWebauthn.ftl` — The pronoun "la" is feminine but refers to the masculine noun "journal".
    - Current: `avant de la partager`
    - Source: `The log may contain personal information, such as user names, account identifiers and website addresses. Review it before sharing.`
    - Suggest: `avant de le partager`
    - "Le journal" is masculine. The earlier "Vérifiez-le" is correct, so "la partager" is an agreement error.
- `credit-card-label-with-security-code-3` — `toolkit/toolkit/payments/payments.ftl` — In the aria-label, "saved" is translated as "économisés" (saved money), and in the plural.
    - Current: `{ $securityCode } économisés`
    - Source: `(value): { $label } \| { $securityCode } saved aria-label: { $ariaLabel }, { $securityCode } saved`
    - Suggest: `{ $securityCode } enregistré`
    - Here "saved" means stored, as the visible label shows with "enregistré". "Économisés" means saved as in money, and it doesn't agree with the single code either. Screen-reader users would hear a different and wrong label.

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
| Files | 346 |
| Strings | 17,349 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 10 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
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
| quotes | `guillemet` 1078, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5289, `straight` 10 | **typographic** |
| ellipsis | `char` 421 | **char** |
| dash | `em` 45, `en` 9 | **em** |
| nbsp | `total` 4209, `before-punctuation` 1833 | _mixed_ |
| register | `formal` 2982 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (12)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 7 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `smartwindow-onboarding-default-window` — `browser/browser/aiWindow.ftl` — "from other apps" is rendered as "depuis { -brand-short-name }", so the French talks about links opened from Firefox itself.
    - Current: `à l’ouverture de liens depuis { -brand-short-name }`
    - Source: `description: Use it when { -brand-short-name } starts, restarts, or opens links from other apps. label: Start in { -smart-window-brand-name }`
    - Suggest: `à l’ouverture de liens depuis d’autres applications, au démarrage ou au redémarrage de { -brand-short-name }`
    - The en-US means links opened from other apps when Firefox starts or restarts. The French drops "other apps" and says the links come from Firefox, which is a different fact.
- `contextual-manager-passwords-delete-all-confirm-button` — `browser/browser/contextual-manager.ftl` — The singular variant says “Tout supprimer” (Delete all), but the source says just “Delete” when there is one password.
    - Current: `[one] Tout supprimer`
    - Source: `{$total ->} [1] Delete [other] Delete all`
    - Suggest: `[one] Supprimer`
    - The en-US deliberately uses “Delete” for one password and “Delete all” for several. The French uses “Delete all” in both cases.
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
- `download-ui-confirm-offline-title` — `toolkit/toolkit/downloads/downloadUI.ftl` — The singular variant says "le passer hors connexion", which takes the download offline instead of the browser.
    - Current: `Arrêter 1 téléchargement et le passer hors connexion ?`
    - Source: `{$downloadsCount ->} [1] Stop 1 download and go offline? [other] Stop { $downloadsCount } downloads and go offline?`
    - Suggest: `Arrêter 1 téléchargement et passer hors connexion ?`
    - In en-US, "go offline" means the browser goes offline, not the download. The pronoun "le" makes the download the thing going offline, which is wrong and reads badly. The plural variant gets it right with "et passer hors connexion".
- `credit-card-label-with-security-code-3` — `toolkit/toolkit/payments/payments.ftl` — In the aria-label, "saved" is translated as "économisés" (saved money), and in the plural.
    - Current: `{ $securityCode } économisés`
    - Source: `(value): { $label } \| { $securityCode } saved aria-label: { $ariaLabel }, { $securityCode } saved`
    - Suggest: `{ $securityCode } enregistré`
    - Here "saved" means stored, as the visible label shows with "enregistré". "Économisés" means saved as in money, and it doesn't agree with the single code either. Screen-reader users would hear a different and wrong label.

### C. Grammar, agreement & spelling

- `smartwindow-onboarding-memories-description` — `browser/browser/aiWindow.ftl` — The indirect object pronoun "leur" is wrongly written "leurs".
    - Current: `Ces souvenirs leurs permettent`
    - Source: `{ -smart-window-brand-name } can learn from chats, browsing, or both to create memories. It uses them to personalize your experience over time.`
    - Suggest: `Ces souvenirs leur permettent`
    - Before a verb, the pronoun "leur" never takes an s.
- `about-webauthn-logging-warning` — `toolkit/toolkit/about/aboutWebauthn.ftl` — The pronoun "la" is feminine but refers to the masculine noun "journal".
    - Current: `avant de la partager`
    - Source: `The log may contain personal information, such as user names, account identifiers and website addresses. Review it before sharing.`
    - Suggest: `avant de le partager`
    - "Le journal" is masculine. The earlier "Vérifiez-le" is correct, so "la partager" is an agreement error.

### D. Terminology, register & consistency

- `ai-window-memories-section-v2` — `browser/browser/aiFeatures.ftl` — "Memories" is rendered as "mémoires" in the description but as "Souvenirs" in the label of the same string and in the onboarding strings.
    - Current: `pour créer des mémoires. Elles sont utilisées`
    - Source: `description: { -brand-short-name } can learn from your activity to create memories. They’re used to help tailor your experience and are stored locally on your device. label: Memories`
    - Suggest: `pour créer des souvenirs. Ils sont utilisés`
    - The feature is called "Souvenirs" everywhere else. "Des mémoires" can read as memoirs or computer memory, so it is the wrong term here.

### E. Typography, punctuation & spacing

- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5289 times against 10 straight.
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
    - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
    - The tree uses ’ 5289 times against 10 straight.

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

### Fixed to date (106)

- `toolbar-switcher-customizable-label-v2` — `browser/browser/aiWindow.ftl` — fixed 2026-11-16
- `genai-menu-summarize-with-ai` — `browser/browser/genai.ftl` — fixed 2026-11-16
- `newtab-widget-wrexhamafc-view-table` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-16
- `hnt-card-extensions-header` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-16
- `tab-groups-onboarding-session-restore-title-3` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-16
- `preferences-ai-controls-sidebar-chatbot-group-3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-16
- `sync-engine-settings2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-16
- `ConnectionAllowlistRedirectBlocked` — `dom/chrome/security/security.properties` — fixed 2026-11-16
- `ConnectionAllowlistReportOnlyRedirectBlocked` — `dom/chrome/security/security.properties` — fixed 2026-11-16
- `dom-manifest-image-unsupported-purposes` — `dom/dom/manifest.ftl` — fixed 2026-11-16
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — fixed 2026-11-16
- `dom-manifest-scope-url-invalid` — `dom/dom/manifest.ftl` — fixed 2026-11-16
- `download-ui-confirm-offline-message` — `toolkit/toolkit/downloads/downloadUI.ftl` — fixed 2026-11-16
- `download-ui-confirm-offline-title` — `toolkit/toolkit/downloads/downloadUI.ftl` — fixed 2026-11-16
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
