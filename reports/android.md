# Firefox for Android and the shared Android Components — l10n QA

- **Generated:** 2026-11-09
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,360 raised, 640 fixed (19%), 2,408 open
- **Closed by a person:** 60 dismissed, 59 suppressed by rule
- **Closed by the fixer:** 45 — the suggestions workflow's model judged them wrong or could not confirm them; no person has decided, and each lapses when its string changes

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (23)

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
- **`vi`** `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "help Firefox win" is rendered as "so that Firefox can continue", which suggests Firefox's survival depends on the user's consent.
    - Current: `để Firefox có thể tiếp tục`
    - Suggest: `để giúp Firefox chiến thắng`
- **`vi`** `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values/strings.xml`
    - "many of the most common trackers" loses "many of", so the text claims protection from the most common trackers without limit.
    - Current: `khỏi các trình theo dõi phổ biến nhất`
    - Suggest: `khỏi nhiều trình theo dõi phổ biến nhất`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (1305)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed | Closed by fixer |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,366 | 235 | **121** | 49 | 0 | 0 | 0 | 0 |
| [cs](cs/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,581 | 20 | **101** | 65 | 7 | 2 | 0 | 0 |
| [de](de/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **53** | 34 | 42 | 5 | 0 | 3 |
| [el](el/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,590 | 11 | **30** | 13 | 0 | 0 | 0 | 0 |
| [en-CA](en-CA/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,576 | 25 | **0** | 0 | 0 | 0 | 0 | 0 |
| [en-GB](en-GB/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **2** | 1 | 0 | 2 | 55 | 0 |
| [es-AR](es-AR/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **102** | 41 | 7 | 0 | 0 | 0 |
| [es-ES](es-ES/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,457 | 144 | **110** | 48 | 1 | 0 | 0 | 0 |
| [es-MX](es-MX/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,486 | 115 | **130** | 75 | 12 | 0 | 0 | 0 |
| [fa](fa/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **63** | 25 | 78 | 0 | 0 | 0 |
| [fi](fi/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,555 | 46 | **44** | 16 | 0 | 0 | 0 | 0 |
| [fr](fr/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **47** | 35 | 27 | 2 | 0 | 5 |
| [fy-NL](fy-NL/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **17** | 9 | 87 | 7 | 0 | 24 |
| [hi-IN](hi-IN/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,507 | 94 | **0** | 0 | 213 | 8 | 0 | 0 |
| [hu](hu/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **128** | 67 | 0 | 0 | 0 | 0 |
| [id](id/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,599 | 2 | **151** | 86 | 4 | 0 | 0 | 0 |
| [it](it/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **0** | 0 | 43 | 11 | 4 | 0 |
| [ja](ja/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,576 | 25 | **141** | 110 | 1 | 0 | 0 | 0 |
| [ko](ko/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **81** | 39 | 0 | 0 | 0 | 0 |
| [nl](nl/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **57** | 31 | 4 | 0 | 0 | 0 |
| [pl](pl/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,576 | 25 | **79** | 55 | 5 | 1 | 0 | 0 |
| [pt-BR](pt-BR/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,598 | 3 | **94** | 61 | 7 | 4 | 0 | 0 |
| [pt-PT](pt-PT/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **73** | 24 | 2 | 0 | 0 | 0 |
| [ro](ro/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,527 | 74 | **88** | 29 | 0 | 0 | 0 | 0 |
| [ru](ru/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,601 | 0 | **144** | 81 | 1 | 0 | 0 | 0 |
| [sk](sk/android.md) | 2026-11-09 | incremental | `f7a886b5` | 2,576 | 25 | **47** | 26 | 2 | 0 | 0 | 0 |
| [sl](sl/android.md) | 2026-11-09 | incremental | `eb586799` | 2,542 | 59 | **43** | 27 | 38 | 5 | 0 | 13 |
| [sv-SE](sv-SE/android.md) | 2026-11-09 | incremental | `eb586799` | 2,601 | 0 | **70** | 29 | 2 | 0 | 0 | 0 |
| [th](th/android.md) | 2026-11-09 | incremental | `eb586799` | 2,410 | 191 | **46** | 26 | 0 | 0 | 0 | 0 |
| [tr](tr/android.md) | 2026-11-09 | incremental | `eb586799` | 2,592 | 9 | **122** | 67 | 5 | 0 | 0 | 0 |
| [uk](uk/android.md) | 2026-11-09 | incremental | `eb586799` | 2,525 | 76 | **46** | 21 | 3 | 0 | 0 | 0 |
| [vi](vi/android.md) | 2026-11-09 | incremental | `eb586799` | 2,525 | 76 | **50** | 27 | 1 | 0 | 0 | 0 |
| [zh-CN](zh-CN/android.md) | 2026-11-09 | incremental | `eb586799` | 2,521 | 80 | **127** | 87 | 0 | 0 | 0 | 0 |
| [zh-TW](zh-TW/android.md) | 2026-11-09 | incremental | `eb586799` | 2,601 | 0 | **1** | 1 | 48 | 13 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `android/locales/<code>/suppressions.yaml`, or better, a sentence in `android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
