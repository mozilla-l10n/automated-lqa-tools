# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-10-18
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,856 raised, 372 fixed (9%), 3,140 open
- **Closed by a person:** 27 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (57)

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
- **`fi`** `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Suggest: `että käytät sitä`
- **`fi`** `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Suggest: `että käytät sitä`
- **`fi`** `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Suggest: `ja että käytät sitä`
- **`fi`** `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Suggest: `ja että käytät sitä`
- **`fi`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "miten löysit Firefoxin ja käytät sitä" reads as sharing how you use Firefox, not that you use it.
    - Current: `miten löysit Firefoxin ja käytät sitä`
    - Suggest: `miten löysit Firefoxin ja että käytät sitä`
- **`ko`** `felt_privacy_desc_card_title` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - Dropping 'on this device' widens the claim to leaving no traces anywhere.
    - Current: `흔적 남기지 않기`
    - Suggest: `이 기기에 흔적 남기지 않기`
- **`ko`** `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - 'Helps protect your data' becomes a flat claim that the feature prevents data leakage between tabs.
    - Current: `탭 간 데이터 유출을 방지합니다`
    - Suggest: `탭 간 데이터를 보호하는 데 도움이 됩니다`
- **`ko`** `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
- **`ko`** `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
- **`ko`** `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
- **`ko`** `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
- **`ko`** `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "will cause websites to break" is softened to "may break" (깨질 수 있음), copying the wording of the third-party cookies option.
    - Current: `웹 사이트가 깨질 수 있음`
    - Suggest: `웹 사이트가 깨짐`
- **`ko`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is rendered as "사용 방법" (how you use it), which the developer comment explicitly rules out.
    - Current: `사용 방법을`
    - Suggest: `사용 중이라는 사실을`
- **`ko`** `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
- **`pt-PT`** `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The hedged "might… be risky" becomes the certain "é perigoso" (is dangerous).
    - Current: `e é perigoso para o seu dispositivo`
    - Suggest: `e ser arriscado para o seu dispositivo`
- **`ro`** `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values/strings.xml`
    - The translation says entered data "will not be saved" where the source says it "may not be saved".
    - Current: `nu vor fi salvate`
    - Suggest: `s-ar putea să nu fie salvate`
- **`ru`** `mozac_menu_banner_dismiss_description` — `mozilla-mobile/android-components/components/compose/menu/src/main/res/values/strings.xml`
    - "Dismiss promotion" is rendered as "Hide the advertisement", calling the in-menu promotional banner an ad.
    - Current: `Скрыть рекламу`
    - Suggest: `Закрыть промо-баннер`
- **`sk`** `nimbus_notification_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "private" is translated as "bezpečný" (secure), so the product calls itself secure rather than private.
    - Current: `rýchly a bezpečný`
    - Suggest: `rýchly a súkromný`
- _…and 27 more, in the per-locale reports linked below._

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1634)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,638 | 164 | **142** | 59 | 0 | 0 | 0 |
| [cs](cs/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,793 | 9 | **121** | 75 | 11 | 2 | 0 |
| [de](de/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **106** | 61 | 1 | 0 | 0 |
| [el](el/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **41** | 17 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **115** | 44 | 7 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,732 | 70 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,761 | 41 | **145** | 84 | 12 | 0 | 0 |
| [fa](fa/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,793 | 9 | **121** | 52 | 36 | 0 | 0 |
| [fi](fi/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,800 | 2 | **51** | 20 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **73** | 54 | 9 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **166** | 56 | 13 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,703 | 99 | **26** | 6 | 213 | 8 | 0 |
| [hu](hu/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,789 | 13 | **165** | 91 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **1** | 1 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,792 | 10 | **150** | 118 | 1 | 0 | 0 |
| [ko](ko/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **95** | 44 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **64** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,798 | 4 | **83** | 58 | 5 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,798 | 4 | **106** | 68 | 8 | 3 | 0 |
| [pt-PT](pt-PT/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,552 | 0 | **74** | 24 | 0 | 0 | 0 |
| [ro](ro/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,798 | 4 | **91** | 30 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **154** | 87 | 1 | 0 | 0 |
| [sk](sk/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **57** | 30 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,779 | 23 | **117** | 65 | 1 | 0 | 0 |
| [sv-SE](sv-SE/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **78** | 30 | 0 | 0 | 0 |
| [th](th/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,685 | 117 | **51** | 27 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **138** | 75 | 5 | 0 | 0 |
| [uk](uk/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **57** | 25 | 0 | 0 | 0 |
| [vi](vi/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,798 | 4 | **60** | 31 | 0 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,797 | 5 | **149** | 102 | 0 | 0 | 0 |
| [zh-TW](zh-TW/android.md) | 2026-10-18 | incremental | `dd8ca757` | 2,802 | 0 | **74** | 35 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
