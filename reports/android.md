# Firefox for Android, Focus, and the shared Android Components — l10n QA

- **Generated:** 2026-10-19
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,849 raised, 372 fixed (9%), 3,133 open
- **Closed by a person:** 27 dismissed, 68 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (41)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

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
- **`ko`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "that you use it" is rendered as "사용 방법" (how you use it), which the developer comment explicitly rules out.
    - Current: `사용 방법을`
    - Suggest: `사용 중이라는 사실을`
- **`ko`** `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
- **`th`** `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
- **`th`** `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The Thai says the user shares how they use Firefox, but the source only says that they use it.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Suggest: `และการที่คุณใช้ Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
- **`th`** `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
- **`th`** `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ Mozilla`
    - Suggest: `และการที่คุณใช้งาน Firefox กับพันธมิตรด้านการตลาดของ Mozilla`
- **`th`** `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The quantifier "many of" is dropped, so the Thai says Firefox protects against the most common trackers as a whole rather than many of them.
    - Current: `ปกป้องคุณจากตัวติดตามที่พบบ่อยที่สุดซึ่งติดตาม`
    - Suggest: `ปกป้องคุณจากตัวติดตามจำนวนมากที่พบบ่อยที่สุดซึ่งติดตาม`
- **`th`** `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "That you use it" is rendered as "how you use it" (อย่างไร), so the setting now describes sharing usage details.
    - Current: `และคุณใช้มันอย่างไร`
    - Suggest: `และการที่คุณใช้งาน Firefox อยู่`
- **`uk`** `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "So you're always up to date on how to stay protected" became "so you're always protected", a guarantee of protection the source doesn't make.
    - Current: `щоб завжди бути захищеними`
    - Suggest: `щоб завжди знати, як залишатися захищеними`
- **`uk`** `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - The hedge "helps stop" became the absolute "Forbid companies from tracking", and "one tap" was dropped.
    - Current: `Забороніть компаніям стежити за вашими діями онлайн.`
    - Suggest: `Один дотик допомагає завадити компаніям стежити за вашими діями онлайн.`
- **`vi`** `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "help Firefox win" is rendered as "so that Firefox can continue", which suggests Firefox's survival depends on the user's consent.
    - Current: `để Firefox có thể tiếp tục`
    - Suggest: `để giúp Firefox chiến thắng`
- **`vi`** `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "many of the most common trackers" loses "many of", so the text claims protection from the most common trackers without limit.
    - Current: `khỏi các trình theo dõi phổ biến nhất`
    - Suggest: `khỏi nhiều trình theo dõi phổ biến nhất`
- _…and 11 more, in the per-locale reports linked below._

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1627)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,638 | 164 | **141** | 58 | 0 | 0 | 0 |
| [cs](cs/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **121** | 75 | 11 | 2 | 0 |
| [de](de/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **106** | 61 | 1 | 0 | 0 |
| [el](el/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **41** | 17 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **1** | 1 | 0 | 3 | 64 |
| [es-AR](es-AR/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **115** | 44 | 7 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,732 | 70 | **120** | 52 | 1 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,761 | 41 | **145** | 84 | 12 | 0 | 0 |
| [fa](fa/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,793 | 9 | **120** | 51 | 36 | 0 | 0 |
| [fi](fi/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,800 | 2 | **51** | 20 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **73** | 54 | 9 | 0 | 0 |
| [fy-NL](fy-NL/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **166** | 56 | 13 | 0 | 0 |
| [hi-IN](hi-IN/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,703 | 99 | **26** | 6 | 213 | 8 | 0 |
| [hu](hu/android.md) | 2026-10-19 | incremental | `57c409b0` | 2,802 | 0 | **148** | 77 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,793 | 9 | **165** | 91 | 4 | 0 | 0 |
| [it](it/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,802 | 0 | **1** | 1 | 43 | 11 | 4 |
| [ja](ja/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,792 | 10 | **150** | 118 | 1 | 0 | 0 |
| [ko](ko/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,802 | 0 | **95** | 44 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,802 | 0 | **64** | 35 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,800 | 2 | **83** | 58 | 5 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,798 | 4 | **106** | 68 | 8 | 3 | 0 |
| [pt-PT](pt-PT/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,552 | 0 | **73** | 23 | 0 | 0 | 0 |
| [ro](ro/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,798 | 4 | **90** | 29 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,802 | 0 | **154** | 87 | 1 | 0 | 0 |
| [sk](sk/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,802 | 0 | **57** | 30 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,779 | 23 | **117** | 65 | 1 | 0 | 0 |
| [sv-SE](sv-SE/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,802 | 0 | **78** | 30 | 0 | 0 | 0 |
| [th](th/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,685 | 117 | **51** | 27 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,802 | 0 | **138** | 75 | 5 | 0 | 0 |
| [uk](uk/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,802 | 0 | **57** | 25 | 0 | 0 | 0 |
| [vi](vi/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,798 | 4 | **59** | 30 | 0 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-10-19 | incremental | `7ee8e61a` | 2,797 | 5 | **149** | 102 | 0 | 0 | 0 |
| [zh-TW](zh-TW/android.md) | 2026-10-19 | checks-only | `ea17dbc8` | 2,802 | 0 | **72** | 33 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

**Not reviewed yet:** `ar`, `fa`, `ko`, `pt-PT`, `ro`, `ru`, `sk`, `sv-SE`, `vi`, `zh-TW`. They have only been through the deterministic checks; the reviewer has not read them. The next run does the baseline.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
