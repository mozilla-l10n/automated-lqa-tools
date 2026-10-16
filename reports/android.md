# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-10-16
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,180 raised, 321 fixed (10%), 2,515 open
- **Closed by a person:** 27 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (13)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`ar`** `inactive_tabs_auto_close_message_description` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The Arabic says Firefox will close inactive tabs automatically, but the source only says it can.
    - Current: `سيُغلق Firefox التبويبات التي لم تعرضها منذ شهر تلقائيًا.`
    - Suggest: `يمكن لـ Firefox إغلاق التبويبات التي لم تعرضها خلال الشهر الماضي.`
- **`ar`** `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The subtitle promises the user will always be protected, where the source only says they will stay up to date on how to stay protected.
    - Current: `لتبقى محميًا دائمًا`
    - Suggest: `لتبقى على اطلاع دائم بكيفية الحفاظ على حمايتك`
- **`ar`** `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
- **`ar`** `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
- **`ar`** `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "helps stop" became "is sufficient to prevent", turning a hedged claim into a guarantee.
    - Current: `نقرة واحدة كفيلة بمنع الشركات من التجسس`
    - Suggest: `نقرة واحدة تساعد في منع الشركات من التجسس`
- **`el`** `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The hedge "helps protect" is rendered as a flat claim that the feature protects your data.
    - Current: `που προστατεύει τα δεδομένα σας`
    - Suggest: `που συμβάλλει στην προστασία των δεδομένων σας`
- **`el`** `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The hedge "helps" is dropped, so the Greek says one tap stops companies spying instead of helping to stop them.
    - Current: `Ένα πάτημα εμποδίζει τις εταιρείες`
    - Suggest: `Ένα πάτημα βοηθά να εμποδίσετε τις εταιρείες`
- **`el`** `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - The translation drops "reported", so it claims Focus blocks all deceptive, attack, malware and unwanted-software sites, not just reported ones.
    - Current: `Φραγή ιστοτόπων εξαπάτησης`
    - Suggest: `Φραγή αναφερόμενων ιστοτόπων εξαπάτησης`
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

### Wrong content — impact 2 (1343)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,638 | 160 | **142** | 59 | 0 | 0 | 0 |
| [cs](cs/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **132** | 75 | 0 | 2 | 0 |
| [de](de/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **105** | 60 | 1 | 0 | 0 |
| [el](el/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,793 | 5 | **41** | 17 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,782 | 11 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-10-12 | incremental | `a400fea3` | 2,793 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **122** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,732 | 61 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,755 | 38 | **156** | 84 | 1 | 0 | 0 |
| [fa](fa/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **120** | 51 | 36 | 0 | 0 |
| [fi](fi/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,791 | 7 | **1** | 1 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **74** | 54 | 8 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,783 | 10 | **178** | 59 | 0 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,703 | 90 | **26** | 6 | 213 | 8 | 0 |
| [hu](hu/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,780 | 13 | **165** | 91 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **1** | 1 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,792 | 1 | **150** | 118 | 1 | 0 | 0 |
| [ko](ko/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **0** | 0 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,785 | 8 | **63** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,782 | 11 | **83** | 58 | 5 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,788 | 5 | **114** | 70 | 0 | 3 | 0 |
| [pt-PT](pt-PT/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,548 | 0 | **3** | 0 | 0 | 0 | 0 |
| [ro](ro/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **0** | 0 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **154** | 87 | 1 | 0 | 0 |
| [sk](sk/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **2** | 0 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,775 | 18 | **117** | 65 | 1 | 0 | 0 |
| [sv-SE](sv-SE/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **1** | 1 | 0 | 0 | 0 |
| [th](th/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,685 | 113 | **2** | 0 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,793 | 0 | **138** | 75 | 5 | 0 | 0 |
| [uk](uk/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **3** | 0 | 0 | 0 | 0 |
| [vi](vi/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **2** | 0 | 0 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-10-12 | incremental | `9d543f9c` | 2,788 | 5 | **149** | 102 | 0 | 0 | 0 |
| [zh-TW](zh-TW/android.md) | 2026-10-16 | baseline | `4d7697d1` | 2,798 | 0 | **2** | 0 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

**Reviewed only in part:** `fi`, `ko`, `pt-PT`, `ro`, `sk`, `sv-SE`, `th`, `uk`, `vi`, `zh-TW`. The reviewer stopped early; the strings it never reached are unreviewed. Each locale's own page says where it stopped.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
