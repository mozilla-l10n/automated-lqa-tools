# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-10-12
- **Locales tracked:** 22 (22 with recorded state)
- **Findings:** 2,981 raised, 321 fixed (10%), 2,316 open
- **Closed by a person:** 27 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (5)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`fa`** `mozac_browser_errorpages_net_reset_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
    - "The connection was reset" is rendered as "the connection was re-established", reversing the meaning of the error.
    - Current: `اتصال از نو برقرار شد`
    - Suggest: `اتصال بازنشانی شد`
- **`fa`** `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values/strings.xml`
    - "Incorrect settings can interfere with Web browsing" rendered as a certainty ("prevents Web browsing").
    - Current: `تنظیمات نادرست آن مانع از مرور وب می‌شود.`
    - Suggest: `تنظیمات نادرست می‌تواند در مرور وب اختلال ایجاد کند.`
- **`fa`** `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The translation adds "at random" which the source does not say.
    - Current: `یکی از آن‌ها را به‌صورت تصادفی برای استفادهٔ مجدد انتخاب کردیم`
    - Suggest: `یکی از آن‌ها را برای استفادهٔ مجدد برایتان انتخاب کردیم`
- **`fa`** `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "private" is rendered as "امن" (secure/safe) instead of "خصوصی" (private).
    - Current: `‏Firefox سریع و امن است`
    - Suggest: `‏Firefox سریع و خصوصی است`
- **`ru`** `mozac_menu_banner_dismiss_description` — `mozilla-mobile/android-components/components/compose/menu/src/main/res/values/strings.xml`
    - "Dismiss promotion" is rendered as "Hide the advertisement", calling the in-menu promotional banner an ad.
    - Current: `Скрыть рекламу`
    - Suggest: `Закрыть промо-баннер`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1265)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **132** | 75 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **105** | 60 | 1 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,782 | 11 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **122** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,732 | 61 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,755 | 38 | **156** | 84 | 1 | 0 | 0 |
| [fa](fa/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **120** | 51 | 36 | 0 | 0 |
| [fr](fr/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **74** | 54 | 8 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,783 | 10 | **178** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,703 | 90 | **26** | 6 | 213 | 8 | 0 |
| [hu](hu/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,780 | 13 | **165** | 91 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **1** | 1 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,792 | 1 | **150** | 118 | 1 | 0 | 0 |
| [nl](nl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,785 | 8 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,782 | 11 | **83** | 58 | 5 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,788 | 5 | **114** | 70 | 0 | 3 | 0 |
| [ru](ru/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **154** | 87 | 1 | 0 | 0 |
| [sl](sl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,775 | 18 | **117** | 65 | 1 | 0 | 0 |
| [tr](tr/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **138** | 75 | 5 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,788 | 5 | **149** | 102 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
