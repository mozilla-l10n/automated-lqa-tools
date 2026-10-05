# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-10-05
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 6,375 raised, 2,108 fixed (33%), 3,638 open
- **Closed by a person:** 19 dismissed, 15 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (23)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`cs`** `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl`
    - "Private Windows won’t reopen" translated as "Anonymní okna nelze znovu otevřít" (private windows cannot be reopened), stating an impossibility rather than a choice.
    - Current: `Anonymní okna nelze z důvodu ochrany vašeho soukromí znovu otevřít.`
    - Suggest: `Anonymní okna se z důvodu ochrany vašeho soukromí znovu neotevřou.`
- **`de`** `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
    - "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
- **`fr`** `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "help keep your browsing private from others on this device" loses the "from others" element, changing the claim.
    - Current: `Les fenêtres privées permettent de garder votre navigation privée sur cet appareil.`
    - Suggest: `Les fenêtres privées permettent de préserver la confidentialité de votre navigation vis-à-vis des autres personnes qui utilisent cet appareil.`
- **`fr`** `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl`
    - "You aren’t syncing anything… yet" is rendered as "you don't have to sync anything", changing the meaning.
    - Current: `Vous ne devez rien synchroniser… pour l’instant.`
    - Suggest: `Vous ne synchronisez rien… pour l’instant.`
- **`hu`** `about-private-browsing-private-window-redesign-subheader` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "is designed to protect your privacy" rendered as an unconditional "protects your privacy".
    - Current: `a beépített követés elleni védelmének köszönhetően megvédi a magánszféráját`
    - Suggest: `úgy lett tervezve, hogy a beépített követés elleni védelemmel megvédje a magánszféráját böngészés közben`
- **`hu`** `restart-required-intro2` — `browser/browser/aboutRestartRequired.ftl`
    - "needs to finish an update. Restart to..." rendered as statements that the browser finishes the update and will restart itself, dropping the instruction to the user.
    - Current: `A { -brand-short-name } befejezi a frissítést. Újraindul, hogy a dolgok biztonságosak és zökkenőmentesek legyenek.`
    - Suggest: `A { -brand-short-name }nak be kell fejeznie a frissítést. Indítsa újra, hogy a dolgok biztonságosak és zökkenőmentesek legyenek.`
- **`hu`** `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl`
    - The description reverses who needs the extra privacy, asserting that the sites must provide privacy rather than that the user wants extra privacy on them.
    - Current: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknek fokozott adatvédelmet kell biztosítaniuk, vagy ki kell kapcsolni a VPN-t.`
    - Suggest: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknél fokozott adatvédelemre van szükség, vagy amelyeknél ki kell kapcsolni a VPN-t.`
- **`hu`** `about-pdf-features-intro` — `toolkit/toolkit/about/aboutPDF.ftl`
    - "private" rendered as "biztonságos" (secure).
    - Current: `Egyszerű, ingyenes és biztonságos.`
    - Suggest: `Egyszerű, ingyenes és privát.`
- **`hu`** `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl`
    - "delete stored payment method information" was rendered as "akar használni" (wants to use) instead of "törölni akarja" (wants to delete).
    - Current: `A { -brand-short-name } tárolt fizetésimód-információkat akar használni.`
    - Suggest: `A { -brand-short-name } törölni akarja a tárolt fizetésimód-információkat.`
- **`it`** `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "help keep your browsing private" rendered as an absolute "impediscono" (prevent), dropping the hedge.
    - Current: `Le finestre anonime impediscono agli altri utenti di questo dispositivo di vedere la tua attività di navigazione.`
    - Suggest: `Le finestre anonime aiutano a nascondere la tua attività di navigazione agli altri utenti di questo dispositivo.`
- **`ja`** `about-private-browsing-spotlight-basics-no-sell-data` — `browser/browser/aboutPrivateBrowsing.ftl`
    - The translation says the browser checks site involvement and does not sell/share the user's data, instead of automatically asking participating sites not to sell or share it.
    - Current: `{ -brand-short-name } はサイトへの関与を自動的に確認し、あなたの個人データを販売または共有しません。`
    - Suggest: `{ -brand-short-name } は対応サイトに対して、あなたの個人データを販売または共有しないよう自動的に要求します。`
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
- **`nl`** `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl`
    - "may not be restored" rendered as "kan niet worden hersteld", turning a possibility into a certainty that unsaved work cannot be restored.
    - Current: `zoals tekst in een formulier, kan niet worden hersteld`
    - Suggest: `zoals tekst in een formulier, kan mogelijk niet worden hersteld`
- **`ru`** `about-private-browsing-spotlight-basics-activity-seen` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "Some activity may still be seen by sites…" mistranslated as "Some sites … may track some activity".
    - Current: `Некоторые сайты, поисковые системы, интернет-провайдеры или ваш работодатель могут отслеживать некоторую активность.`
    - Suggest: `Некоторая активность всё же может быть видна сайтам, поисковым системам, интернет-провайдерам или вашему работодателю.`
- **`ru`** `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "don’t clear all of your data" reversed into "do not delete any of your data".
    - Current: `не удаляют какие-либо ваши данные`
    - Suggest: `не удаляют все ваши данные`
- **`ru`** `restart-required-multiple-instances-answer` — `browser/browser/aboutRestartRequired.ftl`
    - "the open one can be left on an older version" mistranslated as a permission/action "the open one can be left" addressed to the user.
    - Current: `открытый можно оставить в более старой версии`
    - Suggest: `открытый может остаться на более старой версии`
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

### Broken output — impact 1 (289)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`id` 66 · `es-AR` 48 · `ru` 44 · `cs` 41 · `hu` 26 · `fy-NL` 12 · `pt-BR` 11 · `nl` 10 · `pl` 10 · `ja` 8 · `en-GB` 6 · `zh-CN` 4 · `tr` 3

- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
    - `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
    - `appmenuitem-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
- **`en-GB`** `urlbar-result-menu-remove-top-site` — `browser/browser/browser.ftl`
    - Access key changed from uppercase "T" to lowercase "t", which no longer matches the source's access key.
    - Current: `accesskey: t`
    - Suggest: `accesskey: T`
- **`en-GB`** `main-context-menu-inspect-a11y-properties2` — `browser/browser/browserContext.ftl`
    - Access key changed from "y" to "I" although the label is identical to the source.
    - Current: `accesskey: I`
    - Suggest: `accesskey: y`
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
- _…and 274 more, in the per-locale reports linked below._

### Wrong content — impact 2 (1446)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **247** | 160 | 3 | 0 | 0 |
| [de](de/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,582 | 0 | **30** | 16 | 42 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **0** | 0 | 15 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **18** | 13 | 13 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,308 | 47 | **277** | 156 | 143 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 15,170 | 1,185 | **36** | 20 | 113 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 15,826 | 529 | **44** | 15 | 205 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,582 | 0 | **35** | 15 | 64 | 1 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,251 | 104 | **459** | 130 | 274 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **254** | 146 | 5 | 0 | 0 |
| [id](id/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 13,724 | 2,631 | **278** | 216 | 1 | 0 | 0 |
| [it](it/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,584 | 0 | **18** | 6 | 56 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,305 | 50 | **135** | 68 | 273 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,315 | 40 | **342** | 127 | 127 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,251 | 104 | **79** | 53 | 168 | 2 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **532** | 194 | 138 | 5 | 0 |
| [ru](ru/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,355 | 0 | **574** | 306 | 182 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 15,714 | 641 | **50** | 15 | 44 | 0 | 1 |
| [tr](tr/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,334 | 21 | **157** | 58 | 193 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-10-05 | incremental | `ff2ee909` | 16,021 | 334 | **73** | 21 | 49 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
