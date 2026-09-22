# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-09-21
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 6,256 raised, 2,102 fixed (33%), 3,527 open
- **Closed by a person:** 19 dismissed, 15 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (11)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`de`** `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
    - "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
- **`hu`** `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl`
    - The description reverses who needs the extra privacy, asserting that the sites must provide privacy rather than that the user wants extra privacy on them.
    - Current: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknek fokozott adatvédelmet kell biztosítaniuk, vagy ki kell kapcsolni a VPN-t.`
    - Suggest: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknél fokozott adatvédelemre van szükség, vagy amelyeknél ki kell kapcsolni a VPN-t.`
- **`hu`** `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl`
    - "delete stored payment method information" was rendered as "akar használni" (wants to use) instead of "törölni akarja" (wants to delete).
    - Current: `A { -brand-short-name } tárolt fizetésimód-információkat akar használni.`
    - Suggest: `A { -brand-short-name } törölni akarja a tárolt fizetésimód-információkat.`
- **`ja`** `refresh-reinstalled-profile-infobar-message` — `browser/browser/newtab/asrouter.ftl`
    - Adds a claim about a leftover previous profile that the en-US does not make.
    - Current: `{ -brand-short-name } が再インストールされ前回のプロファイルが残っています。新品の状態にリフレッシュしますか？`
    - Suggest: `{ -brand-short-name } を再インストールされたようです。新品のような状態にクリーンアップしましょうか？`
- **`ja`** `onboarding-refresh-fro-import-header` — `browser/browser/newtab/onboarding.ftl`
    - "Bring in your data" (import data) is rendered as "We protect your personal data".
    - Current: `個人データを守ります`
    - Suggest: `データを引き継ぎましょう`
- **`ja`** `speech-recognition-model-download-message` — `browser/browser/permissions.ftl`
    - "the audio never leaves your device" is rendered as "the audio only remains on this device", and "~{ $sizeMB } MB" (approximately) is rendered as "{ $sizeMB } MB or less".
    - Current: `音声はこの端末にしか残りません。セットアップを続けると、音声認識モデル ({ $sizeMB } MB 以下) のデータがダウンロードされます。`
    - Suggest: `音声が端末外に送信されることはありません。セットアップを続けると、音声認識モデル (約 { $sizeMB } MB) のデータがダウンロードされます。`
- **`ja`** `tls-key-logging-notice-nav` — `browser/browser/preferences/preferences.ftl`
    - The source's hedged "may see" is rendered as a definite "can see", asserting that traffic is being read.
    - Current: `使用中のアプリまたはサービスは暗号化された通信を見ることができます。`
    - Suggest: `アプリまたはサービスが暗号化された通信を閲覧できる状態になっている可能性があります。`
- **`ja`** `about-sync-log-page-header` — `toolkit/services/aboutSyncLog.ftl`
    - "Diagnostic logs written by sync." is translated as "diagnoses the logs written by sync", turning a noun phrase into an action.
    - Current: `description: 同期機能により書き込まれたログを診断します。`
    - Suggest: `description: 同期機能により書き込まれた診断ログです。`
- **`ru`** `nova-early-access-infobar-title` — `browser/browser/newtab/asrouter.ftl`
    - "is getting a new look" (future/ongoing) translated as a completed change "Обновлён внешний вид".
    - Current: `<strong>Обновлён внешний вид { -brand-product-name }.</strong>`
    - Suggest: `<strong>У { -brand-product-name } скоро появится новый облик.</strong>`
- **`sl`** `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl`
    - The purpose clause is mistranslated so that the sentence reads "To improve the { -brand-product-name } browser" and merges the subject, changing which product is being improved and who sends the data.
    - Current: `Za izboljšanje brskalnika { -brand-product-name } { -vendor-short-name } pošilja diagnostične podatke in podatke o uporabi.`
    - Suggest: `Za izboljšanje brskalnika { -brand-product-name } pošilja { -vendor-short-name } diagnostične podatke in podatke o uporabi.`
- **`tr`** `newtab-privacy-message-info-4` — `browser/browser/newtab/newtab.ftl`
    - "protection by default" rendered as "protection anytime, anywhere", dropping the default-setting meaning.
    - Current: `{ -brand-short-name } demek her an, her yerde korunma demektir.`
    - Suggest: `{ -brand-short-name } demek varsayılan olarak korunma demektir.`

### Broken output — impact 1 (287)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 66 · `es-AR` 48 · `ru` 44 · `cs` 41 · `hu` 26 · `fy-NL` 12 · `pt-BR` 11 · `nl` 10 · `pl` 10 · `ja` 8 · `en-GB` 4 · `zh-CN` 4 · `tr` 3

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
- **`nl`** `about-logins-copy-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl`
    - about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
    - Suggest: `…message2-macosx`
- _…and 272 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1390)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **239** | 158 | 3 | 0 | 0 |
| [de](de/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,447 | 0 | **23** | 14 | 42 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,246 | 0 | **0** | 0 | 15 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **16** | 11 | 13 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,201 | 32 | **273** | 155 | 142 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 15,167 | 1,066 | **36** | 20 | 113 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 15,810 | 423 | **43** | 14 | 205 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,433 | 0 | **26** | 9 | 62 | 1 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **457** | 128 | 274 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,170 | 63 | **243** | 139 | 5 | 0 | 0 |
| [id](id/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 13,716 | 2,517 | **278** | 216 | 1 | 0 | 0 |
| [it](it/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,460 | 0 | **10** | 2 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,183 | 54 | **123** | 57 | 271 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **339** | 126 | 127 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **75** | 53 | 168 | 2 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **526** | 193 | 138 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,233 | 0 | **556** | 296 | 182 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 15,583 | 650 | **43** | 12 | 43 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,175 | 58 | **149** | 54 | 193 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-09-21 | incremental | `3f7b6c3c` | 16,005 | 228 | **72** | 20 | 49 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
