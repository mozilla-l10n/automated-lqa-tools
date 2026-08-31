# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-31
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,942 raised, 2,165 fixed (36%), 3,702 open
- **Closed by a person:** 16 dismissed, 15 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (2)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`pl`** `aiwindow-feedback-disclaimer` — `browser/browser/aiWindow.ftl`
  - "Submitting shares your feedback and this chat" is translated without stating that the data is shared, only that it "helps".
  - Current: `Przesłanie opinii i treści tej rozmowy pomoże { -brand-shorter-name } ulepszyć { -smart-window-brand-name }.`
  - Suggest: `Przesłanie spowoduje udostępnienie Twojej opinii i treści tej rozmowy, aby pomóc { -brand-shorter-name } ulepszyć { -smart-window-brand-name }.`
- **`pl`** `aiwindow-firstrun-memories-privacy-title` — `browser/browser/aiWindow.ftl`
  - "Private by design" translated as "Domyślnie prywatne" (private by default), which asserts a different privacy claim.
  - Current: `Domyślnie prywatne`
  - Suggest: `Prywatne z założenia`

### Broken output — impact 1 (344)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 84 · `cs` 55 · `es-AR` 53 · `ru` 49 · `hu` 34 · `fy-NL` 13 · `nl` 12 · `pt-BR` 12 · `pl` 11 · `ja` 8 · `en-GB` 4 · `tr` 4 · `zh-CN` 4 · `fr` 1

- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `appmenuitem-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
- **`en-GB`** `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl`
  - UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
  - Current: `Allow file selection dialogues.`
  - Suggest: `Allow file selection dialogs.`
- **`en-GB`** `policy-UseSystemPrintDialog` — `browser/browser/policies/policies-descriptions.ftl`
  - "print dialogue" conflicts with "print dialog" used in the locale's printing files.
  - Current: `Print using the system print dialogue.`
  - Suggest: `Print using the system print dialog.`
- **`es-AR`** `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl`
  - Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
  - Current: `Introducimos <a data-l10n-name="terms-of-use">Términos de uso</a> y actualizamos nuestra <a data-l10n-name="privacy-notice">Nota de privacidad</a >.<br><br> Tómese un momento para revisar y aceptar.…`
  - Suggest: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-…`
- **`es-AR`** `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix` — `devtools/client/tooltips.ftl`
  - Malformed closing tag `</strong >` in `inactive-css-not-grid-or-flex-or-absolutely-positioned-item-fix`
  - Current: `Intente agregar <strong>position:absolute</strong> al elemento, o <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong > o <strong>display:inline-flex</st…`
  - Suggest: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong>, <strong>display:flex</strong>, <strong>display:inline-grid</strong>, or <strong>display:inline-flex</st…`
- **`fr`** `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl`
  - `about-networking-ssl-tokens-summary-compression` references ['total'], which en-US does not pass
  - Current: `{$total ->} [one] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisé) [other] { $decompressedLength } → { $compressedLength } o ({ $saved } % économisés)`
  - Suggest: `{ $decompressedLength } → { $compressedLength } B ({ $saved }% saved)`
- **`fy-NL`** `error-try-again` — `browser/browser/aboutRobots.ftl`
  - .label2 left in English while the value is translated
- **`fy-NL`** `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl`
  - Left in English: "Last updated: …"
- **`hu`** `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl`
  - The singular branches say “passwords” instead of “password”.
  - Current: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszavakat az összes szinkronizált eszközéről.`
  - Suggest: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszót az összes szinkronizált eszközéről.`
- **`hu`** `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl`
  - The action is attributed to the user rather than reported as completed by the assistant.
  - Current: `Létrehozta a(z) „{ $label }” csoportot, és megnyitott { $count } lapot.`
  - Suggest: `A(z) „{ $label }” csoport létrehozva és { $count } lap megnyitva.`
- **`id`** `update-policy-disabled` — `browser/browser/aboutDialog.ftl`
  - Polite pronoun "Anda" written lowercase
  - Current: `Pembaruan dinonaktifkan oleh organisasi anda.`
  - Suggest: `Pembaruan dinonaktifkan oleh organisasi Anda`
- **`id`** `about-logins-import-file-picker-tsv-filter-title` — `browser/browser/aboutLogins.ftl`
  - macOS "TSV Document" rendered as "Berkas TSV" (File)
  - Current: `[macos] Berkas TSV`
  - Suggest: `[macos] Dokumen TSV`
- **`ja`** `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl`
  - comment states this is the standalone label under the big number; ja is a fragment ending in 、 that depends on the separate newtab-privacy-across-sites. → a self-contained label, e.g. 今日ブロックしたトラッカー
  - Suggest: `今日ブロックしたトラッカー`
- **`ja`** `info-exposed-passwords-found` — `browser/browser/protections.ftl`
  - { $count } 件のパスワードが全漏洩データから見つかりました — 件のパスワードが全漏洩データから見つかりました
  - Current: `{ $count } 件のパスワードが全漏洩データから見つかりました`
  - Suggest: `件のパスワードが全漏洩データから見つかりました`
- _…and 329 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1425)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,219 | 0 | **265** | 176 | 0 | 0 | 0 |
| [de](de/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,406 | 0 | **16** | 11 | 71 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,172 | 47 | **0** | 0 | 14 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,213 | 6 | **17** | 11 | 12 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,182 | 37 | **307** | 178 | 139 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 17,183 | 1,036 | **30** | 18 | 111 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 17,841 | 378 | **21** | 6 | 205 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,406 | 0 | **19** | 7 | 58 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,174 | 45 | **506** | 138 | 334 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,213 | 6 | **280** | 157 | 0 | 0 | 0 |
| [id](id/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 15,531 | 2,688 | **330** | 258 | 0 | 0 | 0 |
| [it](it/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,406 | 0 | **3** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,185 | 45 | **100** | 38 | 270 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,174 | 45 | **356** | 132 | 137 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,208 | 11 | **74** | 54 | 170 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,213 | 6 | **563** | 205 | 138 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,213 | 6 | **600** | 318 | 174 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 17,645 | 574 | **37** | 5 | 44 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 18,151 | 68 | **124** | 45 | 185 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-31 | incremental | `67b14d26` | 17,994 | 225 | **54** | 12 | 47 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
