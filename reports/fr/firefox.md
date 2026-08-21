# Firefox l10n QA — fr

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `a9b9a116b725` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `37560db2354a` |
| **Previous run** | 2026-08-20 @ `fef20cd7efc2` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,348 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for fr: [android](android.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (21)

- `browser-main-window-window-titles` — `browser/browser/browser.ftl` — browser-main-window-window-titles (.data-content-title-private) — browser/browser/browser.ftl:20 — double regular space before "(navigation privée)".
  - Source: `data-content-title-default: { $content-title } — { -brand-full-name } data-content-title-private: { $content-title } — { -brand-full-name } Private Browsing data-title-default: { -brand-full-name } data-title-private: {…`
  - Suggest: `.data-content-title-private`
- `contextual-manager-passwords-breached-origin-heading-and-message` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-breached-origin-heading-and-message (.message) — browser/browser/contextual-manager.ftl:202 — FR: "…ou ayant fuités." → ayant fuité (participle with "ayant", no preceding object, invariable).
  - Source: `heading: Password change recommended message: Passwords from this website were reported stolen or leaked. Change your password to protect your account.`
  - Suggest: `ayant fuité`
- `contextual-manager-passwords-remove-all-title` — `browser/browser/contextual-manager.ftl` — two consecutive spaces (U+00A0 + U+202F) between { $total } and "mots".
  - Source: `{$total ->} [1] Remove password? [other] Remove all { $total } passwords?`
- `customkeys-conflict-confirm` — `browser/browser/customkeys.ftl` — regular space before ? (siblings use NBSP).
  - Source: `This key is already assigned to { $conflict }. Do you want to replace it?`
- `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl` — browser/browser/featureCallout.ftl:239,254 — FR: "êtes vous d'accord" → êtes-vous (inversion hyphen).
  - Source: `To what extent do you agree or disagree with this statement:<br/> “The { -brand-short-name } sidebar helps me be more productive”?`
  - Suggest: `êtes-vous`
- `sidebar-genai-survey-productive-question` — `browser/browser/featureCallout.ftl` — browser/browser/featureCallout.ftl:239,254 — FR: "êtes vous d'accord" → êtes-vous (inversion hyphen).
  - Source: `To what extent do you agree or disagree with this statement:<br/> “The AI chatbot in the sidebar helps me be more productive”?`
  - Suggest: `êtes-vous`
- `newtab-clock-widget-edit-item-with-nickname` — `browser/browser/newtab/newtab.ftl` — newtab-clock-widget-edit-item-with-nickname (.aria-label) — browser/browser/newtab/newtab.ftl:1608 — regular space before : (parallel string line 1629 uses NBSP).
  - Source: `aria-label: { $city }, nickname: { $nickname }`
  - Suggest: `.aria-label`
- `multi-profile-spotlight-title` — `browser/browser/newtab/onboarding.ftl` — regular space before !.
  - Source: `Say hello to { -brand-product-name } profiles`
- `places-delete-bookmark` — `browser/browser/places.ftl` — FR: "Supprimer le marque page" / "les marques pages" → marque-page / marque-pages (hyphen; wrong plural).
  - Source: `accesskey: D label: {$count ->} [1] Delete Bookmark [other] Delete Bookmarks`
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — browser/browser/policies/policies-descriptions.ftl:92,132 — missing trailing period (all sibling descriptions end with one).
  - Source: `Configure generative AI features.`
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — browser/browser/policies/policies-descriptions.ftl:92,132 — missing trailing period (all sibling descriptions end with one).
  - Source: `Enable or disable Picture-in-Picture.`
- `app-manager-handle-file` — `browser/browser/preferences/applicationManager.ftl` — browser/browser/preferences/applicationManager.ftl:13,16 — FR: "…utilisées pour Liens { $type }." / "…pour Contenu { $type }." → …pour gérer les liens { $type }. / …pour gérer le contenu { $type }. (verb "handle/gérer" dropped, noun wrongly capitalized).
  - Source: `The following applications can be used to handle { $type } content.`
  - Suggest: `…pour gérer les liens { $type }.`
- `app-manager-handle-protocol` — `browser/browser/preferences/applicationManager.ftl` — browser/browser/preferences/applicationManager.ftl:13,16 — FR: "…utilisées pour Liens { $type }." / "…pour Contenu { $type }." → …pour gérer les liens { $type }. / …pour gérer le contenu { $type }. (verb "handle/gérer" dropped, noun wrongly capitalized).
  - Source: `The following applications can be used to handle { $type } links.`
  - Suggest: `…pour gérer les liens { $type }.`
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — FR: "quelques uns" → quelques-uns (hyphen).
  - Source: `You’re using Resist Fingerprinting (RFP), which replaces some of { -brand-short-name }’s fingerprinting protection settings. This might cause some sites to break.`
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — FR: "quelques uns" → quelques-uns (hyphen).
  - Source: `message: You’re using Resist Fingerprinting (RFP), which replaces some of { -brand-short-name }’s fingerprinting protection settings. This might cause some sites to break.`
- `settings-redesign-promo` — `browser/browser/preferences/preferences.ftl` — settings-redesign-promo (.heading) — browser/browser/preferences/preferences.ftl:2251 — regular space before !.
  - Source: `heading: Same settings, new look! message: We reorganized this page so it’s easier to scan and explore. Your personal settings haven’t changed, and everything’s still here. Tip: use search to jump straight to what you n…`
  - Suggest: `.heading`
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — browser/browser/translations.ftl:12,16 — FR: "Bêta" → Beta (comment: must stay untranslated to match the un-localized BETA icon).
  - Source: `tooltiptext: Translate this page - Beta`
  - Suggest: `Beta`
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — inverted <strong> tags: FR: "</strong>{ $property }<strong> n'a aucun effet…" → <strong>{ $property }</strong> … (property isn't bolded; following text wrongly is).
  - Source: `<strong>{ $property }</strong> has no effect on this element since it cannot be applied to internal table elements where <strong>border-collapse</strong> is set to <strong>collapse</strong> on the parent table element.`
- `learn-more` — `devtools/client/tooltips.ftl` — trailing space inside <span data-l10n-name="link">En savoir plus </span>.
  - Source: `<span data-l10n-name="link">Learn more</span>`
- `support-remote-experiments-see-about-studies` — `toolkit/toolkit/about/aboutSupport.ftl` — double space "ce type".
  - Source: `See <a data-l10n-name="support-about-studies-link">about:studies</a> for more information, including how to disable individual experiments or to disable { -brand-short-name } from running this type of experiment in the…`
- `third-party-detail-occurrences` — `toolkit/toolkit/about/aboutThirdParty.ftl` — third-party-detail-occurrences (.title) — toolkit/toolkit/about/aboutThirdParty.ftl:13 — FR: "Nombre de fois dont ce module a été chargé." → Nombre de fois que ce module a été chargé.
  - Source: `(value): Occurrences title: How many times this module was loaded.`
  - Suggest: `Nombre de fois que ce module a été chargé.`

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 370 |
| Strings | 18,348 |
| Missing strings | 12 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 1 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 1 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 1 |
| Typography deviations from this locale's own norm | 4 |

### Completeness

**12 strings** are not translated yet, concentrated in:

- `browser/browser/appmenu.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/newtab/newtab.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1132, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5633, `straight` 10 | **typographic** |
| ellipsis | `char` 472 | **char** |
| dash | `em` 68, `en` 8 | **em** |
| nbsp | `total` 4446, `before-punctuation` 1997 | _mixed_ |
| register | `formal` 3187 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (37)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 17 |
| 4 | Cosmetic (typography, spacing) | 11 |

### A. Functional, markup, variables & plurals

- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
  - Current: `B`
  - Source: `accesskey: B aria-label: Bookmarks toolbarname: Bookmarks Toolbar`
  - The label is “Marque-pages”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl` — Unbalanced markup in `sidebar-callout-survey-productive-question`
  - Current: `Jusqu’à quel point êtes-vous d’accord ou non avec cette affirmation :</br> « Le panneau latéral de { -brand-short-name } m’aide à être plus productif·tive » ?`
  - Source: `To what extent do you agree or disagree with this statement:<br/> “The { -brand-short-name } sidebar helps me be more productive”?`
  - Suggest: `To what extent do you agree or disagree with this statement:<br/> “The { -brand-short-name } sidebar helps me be more productive”?`
  - Tags must open and close in the same order as en-US.
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — inverted <strong> tags: FR: "</strong>{ $property }<strong> n'a aucun effet…" → <strong>{ $property }</strong> … (property isn't bolded; following text wrongly is).
  - Source: `<strong>{ $property }</strong> has no effect on this element since it cannot be applied to internal table elements where <strong>border-collapse</strong> is set to <strong>collapse</strong> on the parent table element.`
- `learn-more` — `devtools/client/tooltips.ftl` — trailing space inside <span data-l10n-name="link">En savoir plus </span>.
  - Source: `<span data-l10n-name="link">Learn more</span>`
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — `about-networking-ssl-tokens-summary-compression` switches on ['total'], which en-US does not pass (it provides ['compressedLength', 'decompressedLength', 'saved'])
  - Current: `{$total ->} [one] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisé) [other] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisés)`
  - Source: `{ $decompressedLength } → { $compressedLength } B ({ $saved }% saved)`
  - Suggest: `{ $decompressedLength } → { $compressedLength } B ({ $saved }% saved)`
  - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.

### B. Mistranslation, reversed meaning, wrong names & brand

- `aiwindow-firstrun-default-checkbox-label` — `browser/browser/aiWindow.ftl` — brand form lower-plural renders "dans une fenêtres intelligentes" → use lower-singular (EN is singular; matches line 164).
  - Source: `Always open { -brand-product-name } in { -smart-window-brand-name }`
- `app-manager-handle-file` — `browser/browser/preferences/applicationManager.ftl` — browser/browser/preferences/applicationManager.ftl:13,16 — FR: "…utilisées pour Liens { $type }." / "…pour Contenu { $type }." → …pour gérer les liens { $type }. / …pour gérer le contenu { $type }. (verb "handle/gérer" dropped, noun wrongly capitalized).
  - Source: `The following applications can be used to handle { $type } content.`
  - Suggest: `…pour gérer les liens { $type }.`
- `app-manager-handle-protocol` — `browser/browser/preferences/applicationManager.ftl` — browser/browser/preferences/applicationManager.ftl:13,16 — FR: "…utilisées pour Liens { $type }." / "…pour Contenu { $type }." → …pour gérer les liens { $type }. / …pour gérer le contenu { $type }. (verb "handle/gérer" dropped, noun wrongly capitalized).
  - Source: `The following applications can be used to handle { $type } links.`
  - Suggest: `…pour gérer les liens { $type }.`
- `about-glean-metrics-table-settings-timelines-vertical-line-x-offset` — `toolkit/toolkit/about/aboutGlean.ftl` — toolkit/toolkit/about/aboutGlean.ftl:133,135 — both say "axe des abscisses" but EN references the Y-axis → axe des ordonnées; line 135 is also internally contradictory ("décalage vertical … abscisses").
  - Source: `Y-axis X offset`
  - Suggest: `axe des ordonnées`

### C. Grammar, agreement & spelling

- `contextual-manager-passwords-breached-origin-heading-and-message` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-breached-origin-heading-and-message (.message) — browser/browser/contextual-manager.ftl:202 — FR: "…ou ayant fuités." → ayant fuité (participle with "ayant", no preceding object, invariable).
  - Source: `heading: Password change recommended message: Passwords from this website were reported stolen or leaked. Change your password to protect your account.`
  - Suggest: `ayant fuité`
- `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl` — browser/browser/featureCallout.ftl:239,254 — FR: "êtes vous d'accord" → êtes-vous (inversion hyphen).
  - Source: `To what extent do you agree or disagree with this statement:<br/> “The { -brand-short-name } sidebar helps me be more productive”?`
  - Suggest: `êtes-vous`
- `sidebar-genai-survey-productive-question` — `browser/browser/featureCallout.ftl` — browser/browser/featureCallout.ftl:239,254 — FR: "êtes vous d'accord" → êtes-vous (inversion hyphen).
  - Source: `To what extent do you agree or disagree with this statement:<br/> “The AI chatbot in the sidebar helps me be more productive”?`
  - Suggest: `êtes-vous`
- `places-delete-bookmark` — `browser/browser/places.ftl` — FR: "Supprimer le marque page" / "les marques pages" → marque-page / marque-pages (hyphen; wrong plural).
  - Source: `accesskey: D label: {$count ->} [1] Delete Bookmark [other] Delete Bookmarks`
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — FR: "quelques uns" → quelques-uns (hyphen).
  - Source: `You’re using Resist Fingerprinting (RFP), which replaces some of { -brand-short-name }’s fingerprinting protection settings. This might cause some sites to break.`
- `preferences-etp-rfp-warning-message` — `browser/browser/preferences/preferences.ftl` — browser/browser/preferences/preferences.ftl:1995,2702 — FR: "quelques uns" → quelques-uns (hyphen).
  - Source: `message: You’re using Resist Fingerprinting (RFP), which replaces some of { -brand-short-name }’s fingerprinting protection settings. This might cause some sites to break.`
- `third-party-detail-occurrences` — `toolkit/toolkit/about/aboutThirdParty.ftl` — third-party-detail-occurrences (.title) — toolkit/toolkit/about/aboutThirdParty.ftl:13 — FR: "Nombre de fois dont ce module a été chargé." → Nombre de fois que ce module a été chargé.
  - Source: `(value): Occurrences title: How many times this module was loaded.`
  - Suggest: `Nombre de fois que ce module a été chargé.`

### D. Terminology, register & consistency

- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — browser/browser/policies/policies-descriptions.ftl:92,132 — missing trailing period (all sibling descriptions end with one).
  - Source: `Configure generative AI features.`
- `policy-PictureInPicture` — `browser/browser/policies/policies-descriptions.ftl` — browser/browser/policies/policies-descriptions.ftl:92,132 — missing trailing period (all sibling descriptions end with one).
  - Source: `Enable or disable Picture-in-Picture.`
- `fonts-default-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
  - Source: `label: Serif`
- `fonts-sans-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
  - Source: `(value): Sans-serif accesskey: n`
- `fonts-serif` — `browser/browser/preferences/fonts.ftl` — browser/browser/preferences/fonts.ftl:79,81,84,86 — "Serif"/"Sans serif" vs "Sérif"/"Sans sérif" in one file; pick one.
  - Source: `(value): Serif accesskey: S`
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — browser/browser/translations.ftl:12,16 — FR: "Bêta" → Beta (comment: must stay untranslated to match the un-localized BETA icon).
  - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
  - Suggest: `Beta`
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — browser/browser/translations.ftl:12,16 — FR: "Bêta" → Beta (comment: must stay untranslated to match the un-localized BETA icon).
  - Source: `tooltiptext: Translate this page - Beta`
  - Suggest: `Beta`
- `about-debugging-worker-status-running` — `devtools/client/aboutdebugging.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
  - Source: `Running`
- `serviceworker-worker-status-running` — `devtools/client/application.ftl` — serviceworker-worker-status-running vs about-debugging-worker-status-running — devtools/client/application.ftl:43 vs devtools/client/aboutdebugging.ftl:312 — "En cours d'exécution" vs "Exécution" for the same "Running" status; align.
  - Source: `Running`
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-cpu-almost-idle (.title) — toolkit/toolkit/about/aboutProcesses.ftl:167 — "Temps CPU total" vs "Temps total de CPU" (lines 161/170); align.
  - Source: `(value): < 0.1% title: Total CPU time: { $total }{ $unit }`
  - Suggest: `.title`

### E. Typography, punctuation & spacing

- `browser-main-window-window-titles` — `browser/browser/browser.ftl` — browser-main-window-window-titles (.data-content-title-private) — browser/browser/browser.ftl:20 — double regular space before "(navigation privée)".
  - Source: `data-content-title-default: { $content-title } — { -brand-full-name } data-content-title-private: { $content-title } — { -brand-full-name } Private Browsing data-title-default: { -brand-full-name } data-title-private: {…`
  - Suggest: `.data-content-title-private`
- `contextual-manager-passwords-remove-all-title` — `browser/browser/contextual-manager.ftl` — two consecutive spaces (U+00A0 + U+202F) between { $total } and "mots".
  - Source: `{$total ->} [1] Remove password? [other] Remove all { $total } passwords?`
- `customkeys-conflict-confirm` — `browser/browser/customkeys.ftl` — regular space before ? (siblings use NBSP).
  - Source: `This key is already assigned to { $conflict }. Do you want to replace it?`
- `felt-error-warning-download-attempt-failed-contact-admin` — `browser/browser/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
  - The tree uses ’ 5633 times against 10 straight.
- `newtab-clock-widget-edit-item-with-nickname` — `browser/browser/newtab/newtab.ftl` — newtab-clock-widget-edit-item-with-nickname (.aria-label) — browser/browser/newtab/newtab.ftl:1608 — regular space before : (parallel string line 1629 uses NBSP).
  - Source: `aria-label: { $city }, nickname: { $nickname }`
  - Suggest: `.aria-label`
- `multi-profile-spotlight-title` — `browser/browser/newtab/onboarding.ftl` — regular space before !.
  - Source: `Say hello to { -brand-product-name } profiles`
- `settings-redesign-promo` — `browser/browser/preferences/preferences.ftl` — settings-redesign-promo (.heading) — browser/browser/preferences/preferences.ftl:2251 — regular space before !.
  - Source: `heading: Same settings, new look! message: We reorganized this page so it’s easier to scan and explore. Your personal settings haven’t changed, and everything’s still here. Tip: use search to jump straight to what you n…`
  - Suggest: `.heading`
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
  - Current: `L’évènement « key » n’est pas disponible dans GTK2 : key="%S" modifiers="%S" id="%S"`
  - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
  - The locale's quote convention is `guillemet` (1132 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
  - Current: `L’évènement « key » n’est pas disponible pour certaines dispositions de clavier : key="%S" modifiers="%S" id="%S"`
  - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
  - The locale's quote convention is `guillemet` (1132 occurrences).
- `support-remote-experiments-see-about-studies` — `toolkit/toolkit/about/aboutSupport.ftl` — double space "ce type".
  - Source: `See <a data-l10n-name="support-about-studies-link">about:studies</a> for more information, including how to disable individual experiments or to disable { -brand-short-name } from running this type of experiment in the…`
- `felt-error-warning-download-attempt-failed-contact-admin` — `toolkit/toolkit/enterprise/felt.ftl` — `felt-error-warning-download-attempt-failed-contact-admin` uses a straight apostrophe
  - Current: `La dernière mise à jour n'a pas pu être téléchargée. Si le problème persiste, contactez votre administrateur pour obtenir de l’aide.`
  - The tree uses ’ 5633 times against 10 straight.

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

### Resolved to date (31)

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
- `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-07-26
- `fission-status-enabled-by-rollout` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-26
- `media-hdcp-22-compatible` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-26
- `sandbox-sys-call-age` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-26
- `about-webauthn-auth-option-false` — `toolkit/toolkit/about/aboutWebauthn.ftl` — fixed 2026-07-26
- `url-classifier-content-classifier-force-third-party` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-26
- `url-classifier-content-classifier-probe-blocking-btn` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-26
- `url-classifier-content-classifier-verdict-hit` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-26
- `url-classifier-content-classifier-verdict-miss` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-26
- `contentanalysis-operationtype-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — fixed 2026-07-26
- `autofill-category-organization` — `toolkit/toolkit/formautofill/formAutofill.ftl` — fixed 2026-07-26
- `sec-error-bad-template` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-26
- `sec-error-unsupported-ec-point-form` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-26
- `ssl-error-decompression-failure-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-07-26
- `pdfjs-find-match-count-limit` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-07-26
