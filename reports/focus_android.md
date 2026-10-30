# Firefox Focus for Android — l10n QA

- **Generated:** 2026-10-30
- **Locales tracked:** 33 (33 with recorded state)
- **Findings:** 503 raised, 27 fixed (5%), 345 open
- **Closed by a person:** 1 dismissed, 9 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (3)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`el`** `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - The translation drops "reported", so it claims Focus blocks all deceptive, attack, malware and unwanted-software sites, not just reported ones.
    - Current: `Φραγή ιστοτόπων εξαπάτησης`
    - Suggest: `Φραγή αναφερόμενων ιστοτόπων εξαπάτησης`
- **`ko`** `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
- **`vi`** `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values/strings.xml`
    - The Vietnamese drops "strives to", so an effort becomes a flat statement that Mozilla collects only what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần cung cấp`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần để cung cấp`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (164)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/focus_android.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **17** | 6 | 0 | 0 | 0 |
| [cs](cs/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **18** | 11 | 4 | 0 | 0 |
| [de](de/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **7** | 5 | 0 | 0 | 0 |
| [el](el/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **9** | 2 | 0 | 0 | 0 |
| [en-CA](en-CA/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **0** | 0 | 1 | 0 | 0 |
| [en-GB](en-GB/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **0** | 0 | 0 | 1 | 9 |
| [es-AR](es-AR/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **13** | 3 | 0 | 0 | 0 |
| [es-ES](es-ES/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **10** | 4 | 0 | 0 | 0 |
| [es-MX](es-MX/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **15** | 9 | 0 | 0 | 0 |
| [fa](fa/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **12** | 5 | 18 | 0 | 0 |
| [fi](fi/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **8** | 4 | 0 | 0 | 0 |
| [fr](fr/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **4** | 2 | 1 | 0 | 0 |
| [fy-NL](fy-NL/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **20** | 10 | 0 | 0 | 0 |
| [hi-IN](hi-IN/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 170 | 80 | **26** | 6 | 0 | 0 | 0 |
| [hu](hu/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **17** | 11 | 0 | 0 | 0 |
| [id](id/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 241 | 9 | **15** | 7 | 0 | 0 | 0 |
| [it](it/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **0** | 0 | 2 | 0 | 0 |
| [ja](ja/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **9** | 9 | 0 | 0 | 0 |
| [ko](ko/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **15** | 5 | 0 | 0 | 0 |
| [nl](nl/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **4** | 3 | 0 | 0 | 0 |
| [pl](pl/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **4** | 4 | 0 | 0 | 0 |
| [pt-BR](pt-BR/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **11** | 7 | 1 | 0 | 0 |
| [ro](ro/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **2** | 0 | 0 | 0 | 0 |
| [ru](ru/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **14** | 10 | 0 | 0 | 0 |
| [sk](sk/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **8** | 3 | 0 | 0 | 0 |
| [sl](sl/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **18** | 8 | 0 | 0 | 0 |
| [sv-SE](sv-SE/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **5** | 1 | 0 | 0 | 0 |
| [th](th/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **5** | 1 | 0 | 0 | 0 |
| [tr](tr/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **17** | 8 | 0 | 0 | 0 |
| [uk](uk/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **7** | 2 | 0 | 0 | 0 |
| [vi](vi/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **8** | 3 | 0 | 0 | 0 |
| [zh-CN](zh-CN/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 249 | 1 | **18** | 13 | 0 | 0 | 0 |
| [zh-TW](zh-TW/focus_android.md) | 2026-10-30 | checks-only | `f1e4f544` | 250 | 0 | **9** | 2 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

**Not reviewed yet:** `ar`, `cs`, `de`, `el`, `en-CA`, `en-GB`, `es-AR`, `es-ES`, `es-MX`, `fa`, `fi`, `fr`, `fy-NL`, `hi-IN`, `hu`, `id`, `it`, `ja`, `ko`, `nl`, `pl`, `pt-BR`, `ro`, `ru`, `sk`, `sl`, `sv-SE`, `th`, `tr`, `uk`, `vi`, `zh-CN`, `zh-TW`. They have only been through the deterministic checks; the reviewer has not read them. The next run does the baseline.

## Adding a locale

Add its code to `focus_android/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `focus_android/locales/<code>/suppressions.yaml`, or better, a sentence in `focus_android/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
