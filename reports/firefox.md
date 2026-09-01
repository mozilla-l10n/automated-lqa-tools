# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-09-01
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 5,943 raised, 2,178 fixed (36%), 3,688 open
- **Closed by a person:** 18 dismissed, 15 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (0)

_None. The reviewer sets this flag only on a finding where the localized text changes what the product says about itself, its users or its behaviour; it is left unset on the vast majority of mistranslations._

### Broken output — impact 1 (333)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 83 · `cs` 54 · `es-AR` 50 · `ru` 46 · `hu` 31 · `fy-NL` 13 · `nl` 12 · `pt-BR` 12 · `pl` 11 · `ja` 8 · `en-GB` 4 · `tr` 4 · `zh-CN` 4 · `fr` 1

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
- **`es-AR`** `mathmltable` — `dom/chrome/accessibility/AccessFu.properties`
    - “math table” rendered as the truncated non-word “tabla mat”.
    - Current: `mathmltable = tabla mat`
    - Suggest: `mathmltable = tabla matemática`
- **`es-AR`** `clientSocketMisconfiguration` — `dom/chrome/appstrings.properties`
    - Missing accent on the interrogative “cómo”.
    - Current: `no sabe como comunicarse con el servidor`
    - Suggest: `no sabe cómo comunicarse con el servidor`
- **`fr`** `about-networking-ssl-tokens-summary-compression` — `toolkit/toolkit/about/aboutNetworking.ftl`
    - The plural selector expression is malformed: the selector line ends with a stray `}` and the variants are not properly formed, which breaks the Fluent message.
    - Current: `{$saved ->}`
    - Suggest: `{ $saved ->`
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
- _…and 318 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1422)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,219 | 0 | **264** | 175 | 1 | 0 | 0 |
| [de](de/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,406 | 0 | **16** | 11 | 71 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,172 | 47 | **0** | 0 | 14 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,219 | 0 | **17** | 11 | 12 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,188 | 31 | **304** | 175 | 142 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 17,183 | 1,036 | **30** | 18 | 111 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 17,841 | 378 | **21** | 6 | 205 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,406 | 0 | **19** | 7 | 59 | 0 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,174 | 45 | **506** | 138 | 334 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,213 | 6 | **276** | 153 | 4 | 0 | 0 |
| [id](id/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 15,531 | 2,688 | **329** | 257 | 1 | 0 | 0 |
| [it](it/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,416 | 0 | **3** | 0 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,185 | 45 | **100** | 38 | 270 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,174 | 45 | **356** | 132 | 137 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,208 | 11 | **72** | 52 | 170 | 2 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,213 | 6 | **563** | 205 | 138 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,213 | 6 | **597** | 315 | 177 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 17,645 | 574 | **37** | 5 | 44 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 18,151 | 68 | **124** | 45 | 185 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-09-01 | incremental | `bcd40327` | 17,994 | 225 | **54** | 12 | 47 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
