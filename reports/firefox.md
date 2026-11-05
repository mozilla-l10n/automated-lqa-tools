# Firefox (desktop + shared toolkit/dom strings) — l10n QA

- **Generated:** 2026-11-05
- **Locales tracked:** 30 (30 with recorded state)
- **Findings:** 9,622 raised, 2,288 fixed (23%), 6,631 open
- **Closed by a person:** 49 dismissed, 16 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (9)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`es-MX`** `toolbar-button-forget` — `browser/browser/browser.ftl`
    - Tooltip drops "some", claiming the button forgets the browsing history as a whole.
    - Current: `Olvidar el historial de navegación`
    - Suggest: `Olvidar parte del historial de navegación`
- **`hu`** `about-private-browsing-private-window-redesign-subheader` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "is designed to protect your privacy" rendered as an unconditional "protects your privacy".
    - Current: `a beépített követés elleni védelmének köszönhetően megvédi a magánszféráját`
    - Suggest: `úgy lett tervezve, hogy a beépített követés elleni védelemmel megvédje a magánszféráját böngészés közben`
- **`hu`** `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl`
    - "delete stored payment method information" was rendered as "akar használni" (wants to use) instead of "törölni akarja" (wants to delete).
    - Current: `A { -brand-short-name } tárolt fizetésimód-információkat akar használni.`
    - Suggest: `A { -brand-short-name } törölni akarja a tárolt fizetésimód-információkat.`
- **`ja`** `about-private-browsing-spotlight-basics-no-sell-data` — `browser/browser/aboutPrivateBrowsing.ftl`
    - The translation says the browser checks site involvement and does not sell/share the user's data, instead of automatically asking participating sites not to sell or share it.
    - Current: `{ -brand-short-name } はサイトへの関与を自動的に確認し、あなたの個人データを販売または共有しません。`
    - Suggest: `{ -brand-short-name } は対応サイトに対して、あなたの個人データを販売または共有しないよう自動的に要求します。`
- **`ja`** `onboarding-refresh-fro-import-subtitle` — `browser/browser/newtab/onboarding.ftl`
    - "It stays yours" (you keep ownership of the data) is rendered as "user data stays only here", a claim about where the data is kept.
    - Current: `ユーザーデータはここにしか残りません。`
    - Suggest: `データはあなたのものです。`
- **`ru`** `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl`
    - "don’t clear all of your data" reversed into "do not delete any of your data".
    - Current: `не удаляют какие-либо ваши данные`
    - Suggest: `не удаляют все ваши данные`
- **`vi`** `security-technical-encrypted-description` — `browser/browser/pageInfo.ftl`
    - "It is therefore unlikely that anyone read this page" is rendered as an absolute "no one could read this page".
    - Current: `Do đó, không ai có thể đọc trang này khi nó di chuyển trên mạng.`
    - Suggest: `Do đó, khó có khả năng ai đó đã đọc được trang này khi nó di chuyển trên mạng.`
- **`vi`** `pageInfo_Privacy_Encrypted2` — `security/manager/chrome/pippki/pippki.properties`
    - "It is unlikely that anyone read this page" was rendered as "no one could read this page", which turns a likelihood into a guarantee.
    - Current: `Do đó, không ai có thể đọc trang này khi nó di chuyển trên mạng.`
    - Suggest: `Do đó, khó có khả năng ai đó đã đọc được trang này khi nó di chuyển trên mạng.`
- **`vi`** `reset-primary-password-text` — `security/manager/security/pippki/pippki.ftl`
    - The translation adds "form data" to the list of things deleted when resetting the Primary Password, which the source never mentions.
    - Current: `toàn bộ các mật khẩu web, email, dữ liệu biểu mẫu, chứng chỉ và khóa cá nhân đã lưu`
    - Suggest: `toàn bộ các mật khẩu web và email, chứng chỉ cá nhân và khóa riêng đã lưu`

### Broken output — impact 1 (1899)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`sv-SE` 212 · `vi` 212 · `ar` 200 · `pt-PT` 183 · `ko` 159 · `sk` 152 · `el` 142 · `zh-TW` 140 · `uk` 112 · `fi` 108 · `id` 66 · `es-AR` 48 · `ru` 44 · `cs` 41 · `hu` 26 · `pt-BR` 11 · `pl` 10 · `nl` 9 · `ja` 8 · `en-GB` 5 · `fy-NL` 4 · `zh-CN` 4 · `tr` 3

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
- **`fy-NL`** `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl`
    - Left in English ("Stylesheet Pretty Print") while both siblings are translated
- **`hu`** `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl`
    - The singular branches say “passwords” instead of “password”.
    - Current: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszavakat az összes szinkronizált eszközéről.`
    - Suggest: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszót az összes szinkronizált eszközéről.`
- _…and 1884 more, in the per-locale reports linked below._

### Wrong content — impact 2 (2520)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/firefox.md) | 2026-11-05 | incremental | `324a294b` | 13,554 | 3,306 | **362** | 321 | 0 | 0 | 0 |
| [cs](cs/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,755 | 105 | **255** | 167 | 4 | 0 | 0 |
| [de](de/firefox.md) | 2026-11-05 | incremental | `324a294b` | 17,089 | 0 | **27** | 15 | 58 | 8 | 0 |
| [el](el/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,755 | 105 | **219** | 210 | 0 | 0 | 0 |
| [en-CA](en-CA/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,754 | 106 | **0** | 0 | 15 | 1 | 0 |
| [en-GB](en-GB/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,755 | 105 | **21** | 12 | 14 | 0 | 12 |
| [es-AR](es-AR/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,796 | 64 | **297** | 159 | 143 | 0 | 0 |
| [es-ES](es-ES/firefox.md) | 2026-11-05 | incremental | `324a294b` | 15,371 | 1,489 | **44** | 24 | 113 | 0 | 0 |
| [es-MX](es-MX/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,119 | 741 | **79** | 28 | 205 | 0 | 0 |
| [fi](fi/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,206 | 654 | **157** | 147 | 0 | 0 | 0 |
| [fr](fr/firefox.md) | 2026-11-05 | incremental | `324a294b` | 17,089 | 0 | **42** | 19 | 80 | 2 | 0 |
| [fy-NL](fy-NL/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,755 | 105 | **402** | 122 | 366 | 14 | 0 |
| [hu](hu/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,816 | 44 | **275** | 155 | 7 | 0 | 0 |
| [id](id/firefox.md) | 2026-11-05 | incremental | `324a294b` | 13,922 | 2,938 | **291** | 221 | 2 | 0 | 0 |
| [it](it/firefox.md) | 2026-11-05 | incremental | `324a294b` | 17,090 | 0 | **5** | 5 | 74 | 9 | 2 |
| [ja](ja/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,773 | 105 | **150** | 76 | 274 | 0 | 0 |
| [ko](ko/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,755 | 105 | **288** | 279 | 0 | 0 | 0 |
| [nl](nl/firefox.md) | 2026-11-05 | incremental | `324a294b` | 16,815 | 45 | **339** | 128 | 138 | 0 | 0 |
| [pl](pl/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,755 | 105 | **84** | 59 | 168 | 2 | 0 |
| [pt-BR](pt-BR/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,755 | 105 | **549** | 192 | 141 | 5 | 0 |
| [pt-PT](pt-PT/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,773 | 87 | **320** | 310 | 0 | 0 | 0 |
| [ru](ru/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,860 | 0 | **610** | 319 | 182 | 0 | 0 |
| [sk](sk/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,755 | 105 | **229** | 223 | 2 | 0 | 0 |
| [sl](sl/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,011 | 849 | **32** | 9 | 58 | 8 | 2 |
| [sv-SE](sv-SE/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,860 | 0 | **352** | 316 | 0 | 0 | 0 |
| [tr](tr/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,751 | 109 | **167** | 62 | 193 | 0 | 0 |
| [uk](uk/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 15,393 | 1,467 | **203** | 194 | 0 | 0 | 0 |
| [vi](vi/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,321 | 539 | **501** | 396 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,435 | 425 | **78** | 26 | 51 | 0 | 0 |
| [zh-TW](zh-TW/firefox.md) | 2026-11-05 | incremental | `cabf9140` | 16,860 | 0 | **253** | 225 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
