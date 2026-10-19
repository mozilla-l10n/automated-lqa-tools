# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-10-19
- **Locales tracked:** 29 (29 with recorded state)
- **Findings:** 8,989 raised, 2,128 fixed (23%), 6,221 open
- **Closed by a person:** 19 dismissed, 16 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (31)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`cs`** `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl`
    - "Private Windows won’t reopen" translated as "Anonymní okna nelze znovu otevřít" (private windows cannot be reopened), stating an impossibility rather than a choice.
    - Current: `Anonymní okna nelze z důvodu ochrany vašeho soukromí znovu otevřít.`
    - Suggest: `Anonymní okna se z důvodu ochrany vašeho soukromí znovu neotevřou.`
- **`de`** `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl`
    - "Nice work organizing your tabs" is turned into a factual claim that the user's tabs are now perfectly organized.
    - Current: `Ihre Tabs sind jetzt bestens organisiert`
    - Suggest: `Gut gemacht beim Organisieren Ihrer Tabs`
- **`de`** `permissions-allow-app-links` — `browser/browser/preferences/preferences.ftl`
    - The German drops "ask", so it says sites may open app links rather than ask to open them.
    - Current: `Websites erlauben, App-Links zu öffnen.`
    - Suggest: `Websites erlauben, das Öffnen von App-Links anzufragen.`
- **`de`** `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
    - "Split" (PDFs aufteilen/teilen in Einzeldokumente) is rendered as "PDFs teilen", which in German primarily means "share".
    - Current: `PDFs teilen, zusammenführen und mehr.`
    - Suggest: `PDFs aufteilen, zusammenführen und mehr.`
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
- **`id`** `site-data-clear-all-prompt-text` — `browser/browser/preferences/siteDataSettings.ftl`
    - "This may sign you out" is rendered as a certainty ("akan" = will).
    - Current: `Ini akan mengeluarkan Anda dari situs web`
    - Suggest: `Ini mungkin akan mengeluarkan Anda dari situs web`
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
- **`ja`** `site-data-clear-all-prompt-text` — `browser/browser/preferences/siteDataSettings.ftl`
    - The hedge "may" is dropped, so the Japanese says clearing data will definitely sign the user out and delete offline content.
    - Current: `これにより、ウェブサイトからログアウトされ、オフラインのウェブコンテンツが削除されます。`
    - Suggest: `これにより、ウェブサイトからログアウトされたり、オフラインのウェブコンテンツが削除されたりする場合があります。`
- **`ja`** `about-sync-log-page-header` — `toolkit/services/aboutSyncLog.ftl`
    - "Diagnostic logs written by sync." is translated as "diagnoses the logs written by sync", turning a noun phrase into an action.
    - Current: `description: 同期機能により書き込まれたログを診断します。`
    - Suggest: `description: 同期機能により書き込まれた診断ログです。`
- **`nl`** `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl`
    - "may not be restored" rendered as "kan niet worden hersteld", turning a possibility into a certainty that unsaved work cannot be restored.
    - Current: `zoals tekst in een formulier, kan niet worden hersteld`
    - Suggest: `zoals tekst in een formulier, kan mogelijk niet worden hersteld`
- **`pl`** `credit-card-save-doorhanger-description-security-code` — `toolkit/toolkit/formautofill/formAutofill.ftl`
    - The Polish reverses the statement "only you can use them" into "nobody else can use them" — actually it drops the assurance that the user can use them.
    - Current: `dzięki czemu nikt inny nie może używać ich do wypełniania formularzy płatności`
    - Suggest: `dzięki czemu tylko Ty możesz używać ich do wypełniania formularzy płatności`
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
- **`tr`** `welcome-back-onboarding-card-label-pdf` — `browser/browser/newtab/onboarding.ftl`
    - "Highlight" is rendered as "işaretleyin" (mark) and "work with PDFs" as "düzenleyin" (edit).
    - Current: `PDF’leri işaretleyin, imzalayın ve düzenleyin`
    - Suggest: `PDF’leri vurgulayın, imzalayın ve PDF’lerle çalışın`
- **`vi`** `TimeoutSyncXHRWarning` — `dom/chrome/dom/dom.properties`
    - "No longer" was added where the source just says "not supported".
    - Current: `không còn được hỗ trợ`
    - Suggest: `không được hỗ trợ`
- **`vi`** `pageInfo_Privacy_Encrypted2` — `security/manager/chrome/pippki/pippki.properties`
    - "It is unlikely that anyone read this page" was rendered as "no one could read this page", which turns a likelihood into a guarantee.
    - Current: `Do đó, không ai có thể đọc trang này khi nó di chuyển trên mạng.`
    - Suggest: `Do đó, khó có khả năng ai đó đã đọc được trang này khi nó di chuyển trên mạng.`
- **`vi`** `reset-primary-password-text` — `security/manager/security/pippki/pippki.ftl`
    - The translation adds "form data" to the list of things deleted when resetting the Primary Password, which the source never mentions.
    - Current: `toàn bộ các mật khẩu web, email, dữ liệu biểu mẫu, chứng chỉ và khóa cá nhân đã lưu`
    - Suggest: `toàn bộ các mật khẩu web và email, chứng chỉ cá nhân và khóa riêng đã lưu`
- _…and 1 more, in the per-locale reports linked below._

### Broken output — impact 1 (1754)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`vi` 214 · `sv-SE` 212 · `ar` 200 · `pt-PT` 184 · `sk` 152 · `el` 143 · `zh-TW` 141 · `uk` 112 · `fi` 108 · `id` 66 · `es-AR` 48 · `ru` 44 · `cs` 41 · `hu` 26 · `fy-NL` 12 · `pt-BR` 11 · `nl` 10 · `pl` 10 · `ja` 8 · `en-GB` 5 · `zh-CN` 4 · `tr` 3

- **`ar`** `about-logins-import-report-row-description-modified2` — `browser/browser/aboutLogins.ftl`
    - Gender disagreement: feminine verb and adjective with the masculine noun “الولوج”.
    - Current: `حُدّثت الولوج الموجودة`
    - Suggest: `حُدّث الولوج الموجود`
- **`ar`** `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl`
    - Misspelled hamza in “لإضافة”.
    - Current: `لاضافة`
    - Suggest: `لإضافة`
- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
    - `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
- **`cs`** `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl`
    - `appmenuitem-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
- **`el`** `account-connection-disconnected` — `browser/browser/accounts.ftl`
    - Misspelling of «υπολογιστής».
    - Current: `Αυτός ο υπολογιστείς έχει αποσυνδεθεί.`
    - Suggest: `Αυτός ο υπολογιστής έχει αποσυνδεθεί.`
- **`el`** `ai-window-no-memories` — `browser/browser/aiFeatures.ftl`
    - Wrong article gender before «δραστηριότητά σας».
    - Current: `μαθαίνει από το δραστηριότητά σας`
    - Suggest: `μαθαίνει από τη δραστηριότητά σας`
- **`en-GB`** `urlbar-result-menu-remove-top-site` — `browser/browser/browser.ftl`
    - Access key changed from uppercase "T" to lowercase "t", which no longer matches the source's access key.
    - Current: `accesskey: t`
    - Suggest: `accesskey: T`
- **`en-GB`** `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl`
    - UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
    - Current: `Allow file selection dialogues.`
    - Suggest: `Allow file selection dialogs.`
- **`es-AR`** `mathmltable` — `dom/chrome/accessibility/AccessFu.properties`
    - “math table” rendered as the truncated non-word “tabla mat”.
    - Current: `mathmltable = tabla mat`
    - Suggest: `mathmltable = tabla matemática`
- **`es-AR`** `clientSocketMisconfiguration` — `dom/chrome/appstrings.properties`
    - Missing accent on the interrogative “cómo”.
    - Current: `no sabe como comunicarse con el servidor`
    - Suggest: `no sabe cómo comunicarse con el servidor`
- **`fi`** `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl`
    - Stray " a>" fragment appears as visible text at the end of the sentence.
    - Current: `tiedostosta</a> a>.`
    - Suggest: `tiedostosta</a>.`
- **`fi`** `about-logins-vulnerable-alert-text2` — `browser/browser/aboutLogins.ftl`
    - Misspelled verb form "vuosivat" instead of "vuotivat".
    - Current: `jonka tiedot todennäköisesti vuosivat`
    - Suggest: `jonka tiedot todennäköisesti vuotivat`
- **`fy-NL`** `error-try-again` — `browser/browser/aboutRobots.ftl`
    - .label2 left in English while the value is translated
- **`fy-NL`** `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl`
    - Left in English: "Last updated: …"
- **`hu`** `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl`
    - The singular branches say “passwords” instead of “password”.
    - Current: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszavakat az összes szinkronizált eszközéről.`
    - Suggest: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszót az összes szinkronizált eszközéről.`
- _…and 1739 more, in the per-locale reports linked below._

### Wrong content — impact 2 (2320)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 13,351 | 3,169 | **345** | 314 | 0 | 0 | 0 |
| [cs](cs/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,457 | 63 | **249** | 163 | 4 | 0 | 0 |
| [de](de/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,742 | 0 | **40** | 21 | 42 | 0 | 0 |
| [el](el/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **211** | 208 | 0 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,542 | 0 | **0** | 0 | 15 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **19** | 12 | 14 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,490 | 30 | **280** | 157 | 143 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 15,224 | 1,296 | **40** | 23 | 113 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 15,868 | 652 | **47** | 15 | 205 | 0 | 0 |
| [fi](fi/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,036 | 484 | **155** | 145 | 0 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,742 | 0 | **33** | 15 | 72 | 1 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,477 | 43 | **470** | 134 | 275 | 4 | 0 |
| [hu](hu/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,477 | 43 | **260** | 147 | 6 | 0 | 0 |
| [id](id/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 13,799 | 2,721 | **282** | 218 | 2 | 0 | 0 |
| [it](it/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,768 | 0 | **18** | 6 | 59 | 6 | 2 |
| [ja](ja/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,351 | 184 | **136** | 69 | 273 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,500 | 20 | **345** | 127 | 127 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,477 | 43 | **84** | 58 | 168 | 2 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,477 | 43 | **538** | 193 | 141 | 5 | 0 |
| [pt-PT](pt-PT/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **308** | 306 | 0 | 0 | 0 |
| [ru](ru/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **589** | 309 | 182 | 0 | 0 |
| [sk](sk/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **220** | 220 | 0 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 15,838 | 682 | **50** | 15 | 44 | 0 | 2 |
| [sv-SE](sv-SE/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **329** | 308 | 0 | 0 | 0 |
| [tr](tr/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **163** | 61 | 193 | 0 | 0 |
| [uk](uk/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 15,270 | 1,250 | **200** | 194 | 0 | 0 | 0 |
| [vi](vi/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,165 | 355 | **497** | 394 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,126 | 394 | **77** | 25 | 50 | 0 | 0 |
| [zh-TW](zh-TW/firefox.md) | 2026-10-19 | incremental | `ba8eba58` | 16,520 | 0 | **236** | 217 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
