# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-08-24
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,827 raised, 2,010 fixed (34%), 3,769 open
- **Closed by a person:** 15 dismissed, 3 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (365)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 84 · `es-AR` 70 · `cs` 55 · `ru` 49 · `hu` 34 · `fy-NL` 13 · `nl` 12 · `pt-BR` 12 · `pl` 11 · `en-GB` 8 · `ja` 8 · `tr` 4 · `zh-CN` 4 · `fr` 1

- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
  - `appmenuitem-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
  - Current: `Nové { -smart-window-brand-name }`
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
- _…and 350 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1439)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,180 | 0 | **259** | 175 | 0 | 0 | 0 |
| [de](de/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,180 | 0 | **16** | 11 | 71 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,139 | 41 | **1** | 0 | 14 | 0 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,180 | 0 | **33** | 20 | 7 | 0 | 0 |
| [es-AR](es-AR/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,150 | 30 | **421** | 240 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 17,185 | 995 | **30** | 18 | 111 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 17,847 | 333 | **21** | 6 | 205 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,367 | 0 | **16** | 4 | 55 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,180 | 0 | **505** | 138 | 334 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,165 | 15 | **277** | 154 | 0 | 0 | 0 |
| [id](id/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 15,494 | 2,686 | **330** | 258 | 0 | 0 | 0 |
| [it](it/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,397 | 6 | **0** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-08-24 | incremental | `e59d5107` | 18,135 | 45 | **98** | 37 | 269 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-08-24 | incremental | `907043d6` | 18,180 | 0 | **356** | 132 | 137 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-08-24 | incremental | `907043d6` | 17,885 | 295 | **48** | 37 | 166 | 0 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-08-24 | incremental | `907043d6` | 18,180 | 0 | **564** | 205 | 138 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-08-24 | incremental | `907043d6` | 18,169 | 11 | **594** | 315 | 173 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-08-24 | incremental | `907043d6` | 17,550 | 630 | **33** | 4 | 44 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-08-24 | recheck | `39e5663f` | 18,064 | 116 | **113** | 38 | 183 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-08-24 | incremental | `907043d6` | 17,981 | 199 | **54** | 12 | 47 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
