# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-23
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,801 raised, 1,411 fixed (24%), 4,342 open
- **Closed by a person:** 15 dismissed, 3 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (424)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 84 · `es-AR` 70 · `cs` 54 · `ru` 50 · `hu` 34 · `fy-NL` 26 · `nl` 23 · `pt-BR` 15 · `pl` 13 · `ja` 12 · `de` 10 · `es-MX` 9 · `en-GB` 8 · `zh-CN` 6 · `fr` 4 · `tr` 4 · `es-ES` 2

- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
- **`cs`** `menu-file-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `menu-file-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
- **`de`** `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl`
  - Malformed closing tag `</span >` in `about-logins-import-dialog-items-no-change2`
  - Current: `{$count ->} [one] <span>Doppelte Einträge gefunden:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(nicht importiert)</span > [other] <span>Doppelte Einträge gefund…`
  - Suggest: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
- **`de`** `appmenuitem-new-window` — `browser/browser/appmenu.ftl`
  - appmenuitem-new-window (.label) — browser/browser/appmenu.ftl:27 — stray soft hyphen U+00AD before "Neues Fenster" (byte-confirmed c2 ad). Remove it.
  - Suggest: `.label`
- **`en-GB`** `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl`
  - "Sync" left untranslated while every sibling string in the same block renders it "Synchronise".
  - Current: `Sync backs up most of your data`
  - Suggest: `Synchronise backs up most of your data`
- **`en-GB`** `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl`
  - UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
  - Current: `Allow file selection dialogues.`
  - Suggest: `Allow file selection dialogs.`
- **`es-AR`** `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl`
  - Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
  - Current: `Introducimos <a data-l10n-name="terms-of-use">Términos de uso</a> y actualizamos nuestra <a data-l10n-name="privacy-notice">Nota de privacidad</a >.<br><br> Tómese un momento para revisar y aceptar.…`
  - Suggest: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-…`
- **`es-AR`** `heapview.field.count.tooltip` — `devtools/client/memory.properties`
  - Typo “excluyeno” instead of “excluyendo”
  - Current: `excluyeno subgrupos`
  - Suggest: `excluyendo subgrupos`
- **`es-ES`** `general-meta-tags` — `browser/browser/pageInfo.ftl`
  - the [one] plural variant is garbled: it renders "Meta (1 etiqueta)" followed by four duplicated untranslated "Meta (1 tag)" lines → collapse to a single [one] Meta (1 etiqueta).
  - Current: `[one]`
  - Suggest: `[one] Meta (1 etiqueta)`
- **`es-ES`** `inactive-css-no-width-height` — `devtools/client/tooltips.ftl`
  - missing space after </strong> glues words ("propiedadno tiene") → add a space.
  - Suggest: `add a space.`
- **`es-MX`** `login-intro-instructions-fxa-settings` — `browser/browser/aboutLogins.ftl`
  - Missing spaces gluing text/tags: login-intro-instructions-fxa-settings (Ajustes>), main-context-menu-edit-bookmark-with-shortcut (marcador({ $shortcut })), fp-certerror-bad-domain-why-dangerous-body (ser.{ -brand-short-name }), about-logging-log-tutorial (Vea<a…>), rights-webservices (encontrar<a…>).
  - Suggest: `Ajustes>`
- **`es-MX`** `account-tabs-closed-remotely` — `browser/browser/accounts.ftl`
  - account-tabs-closed-remotely (accounts.ftl) — missing spaces around brand: { $closedCount }{ -brand-short-name } pestaña renders e.g. "1Firefox…".
- **`fr`** `sidebar-callout-survey-productive-question` — `browser/browser/featureCallout.ftl`
  - Unbalanced markup in `sidebar-callout-survey-productive-question`
  - Current: `Jusqu’à quel point êtes-vous d’accord ou non avec cette affirmation :</br> « Le panneau latéral de { -brand-short-name } m’aide à être plus productif·tive » ?`
  - Suggest: `To what extent do you agree or disagree with this statement:<br/> “The { -brand-short-name } sidebar helps me be more productive”?`
- **`fr`** `inactive-css-border-image` — `devtools/client/tooltips.ftl`
  - inverted <strong> tags: FR: "</strong>{ $property }<strong> n'a aucun effet…" → <strong>{ $property }</strong> … (property isn't bolded; following text wrongly is).
- **`fy-NL`** `error-try-again` — `browser/browser/aboutRobots.ftl`
  - .label2 left in English while the value is translated
- _…and 409 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1618)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,169 | 11 | **258** | 174 | 0 | 0 | 0 |
| [de](de/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,169 | 11 | **50** | 23 | 35 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,139 | 41 | **2** | 0 | 13 | 0 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,180 | 0 | **34** | 20 | 6 | 0 | 0 |
| [es-AR](es-AR/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,148 | 32 | **421** | 240 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-22 | incremental | `9441127e` | 17,185 | 995 | **101** | 43 | 39 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-22 | incremental | `9441127e` | 17,847 | 333 | **133** | 54 | 93 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,367 | 0 | **40** | 10 | 31 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,139 | 41 | **588** | 177 | 245 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,124 | 56 | **274** | 153 | 0 | 0 | 0 |
| [id](id/firefox.md) | 2026-08-22 | incremental | `9441127e` | 15,494 | 2,686 | **330** | 258 | 0 | 0 | 0 |
| [it](it/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,367 | 0 | **0** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,135 | 45 | **178** | 69 | 189 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,164 | 16 | **377** | 149 | 115 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-08-22 | incremental | `9441127e` | 17,874 | 306 | **83** | 50 | 127 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,135 | 45 | **568** | 208 | 131 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,169 | 11 | **595** | 316 | 172 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-08-22 | incremental | `9441127e` | 17,541 | 639 | **35** | 5 | 42 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-08-22 | incremental | `9441127e` | 18,007 | 173 | **200** | 72 | 91 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-22 | incremental | `9441127e` | 17,981 | 199 | **75** | 21 | 26 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
