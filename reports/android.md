# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-10-05
- **Locales tracked:** 22 (22 with recorded state)
- **Findings:** 2,950 raised, 282 fixed (9%), 2,331 open
- **Closed by a person:** 24 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (8)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`fa`** `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
    - First paragraph translates the net-interrupt message instead of "The network link was interrupted while negotiating a connection."
    - Current: `مرورگر با موفقیت متصل شد ، اما هنگام انتقال اطلاعات ، اتصال قطع شد. لطفا دوباره امتحان کنید.`
    - Suggest: `پیوند شبکه در هنگام برقراری اتّصال قطع شد. لطفاً دوباره تلاش کنید.`
- **`fa`** `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
    - "The connection was reset" is rendered as "the connection was re-established", reversing the meaning of the error.
    - Current: `اتصال از نو برقرار شد`
    - Suggest: `اتصال بازنشانی شد`
- **`fa`** `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
    - "Incorrect settings can interfere with Web browsing" rendered as a certainty ("prevents Web browsing").
    - Current: `تنظیمات نادرست آن مانع از مرور وب می‌شود.`
    - Suggest: `تنظیمات نادرست می‌تواند در مرور وب اختلال ایجاد کند.`
- **`fa`** `mozac_feature_addons_permissions_all_urls_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values/strings.xml`
    - Adds "all" to the data being accessed, which the source does not say.
    - Current: `دسترسی به تمامی اطلاعات شما برای تمامی پایگاه های اینترنتی`
    - Suggest: `دسترسی به داده‌های شما برای همهٔ وب‌گاه‌ها`
- **`fa`** `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The translation adds "at random" which the source does not say.
    - Current: `یکی از آن‌ها را به‌صورت تصادفی برای استفادهٔ مجدد انتخاب کردیم`
    - Suggest: `یکی از آن‌ها را برای استفادهٔ مجدد برایتان انتخاب کردیم`
- **`fa`** `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "private" is rendered as "امن" (secure/safe) instead of "خصوصی" (private).
    - Current: `‏Firefox سریع و امن است`
    - Suggest: `‏Firefox سریع و خصوصی است`
- **`fa`** `feedback_erase_custom_tab` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - Singular "Tab's browsing history" rendered as plural "tabs of the browser".
    - Current: `تاریخچه زبانه‌های مرورگر پاک شده است.`
    - Suggest: `تاریخچهٔ مرور زبانه پاک شده است.`
- **`fa`** `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - "we never save and cannot restore this tab" rendered as "we cannot save and restore this tab", losing the "never save" assertion.
    - Current: `به عنوان یک مرورگر خصوصی نمی توانیم این زبانه را ذخیره و بازیابی کنیم.`
    - Suggest: `به عنوان یک مرورگر خصوصی، ما هرگز این زبانه را ذخیره نمی‌کنیم و نمی‌توانیم آن را بازیابی کنیم.`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1277)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **133** | 76 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **105** | 60 | 1 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **122** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,737 | 50 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,760 | 27 | **156** | 84 | 1 | 0 | 0 |
| [fa](fa/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,625 | 162 | **139** | 60 | 5 | 0 | 0 |
| [fr](fr/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **76** | 53 | 5 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,752 | 35 | **167** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,666 | 121 | **26** | 6 | 213 | 8 | 0 |
| [hu](hu/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,779 | 8 | **165** | 91 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **1** | 1 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,783 | 4 | **150** | 118 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,746 | 41 | **88** | 63 | 0 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **117** | 70 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,787 | 0 | **155** | 88 | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,772 | 15 | **117** | 65 | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,781 | 6 | **138** | 75 | 5 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-10-05 | incremental | `d82f3577` | 2,733 | 54 | **144** | 99 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
