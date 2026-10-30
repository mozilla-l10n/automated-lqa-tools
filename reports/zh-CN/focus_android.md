# Focus for Android l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 249 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for zh-CN: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 1 |
| Strings | 249 |
| Missing strings | 1 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**1 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 75 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1027 | **punctuation** |
| register | `informal` 3, `formal` 262 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (18)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 13 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `advertising` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Advertising" tracker category is rendered as "营销" (marketing) instead of "广告".
    - Current: `营销`
    - Source: `Advertising`
    - Suggest: `广告`
    - The source names the advertising tracker category; "营销" means marketing, a different category name than the en-US "Advertising".
- `menu_add_to_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Add to Shortcuts" is translated as "添加快捷方式" (Add a shortcut), losing the target "Shortcuts" list referenced by the developer comment.
    - Current: `添加快捷方式`
    - Source: `Add to Shortcuts`
    - Suggest: `添加到快捷方式`
    - The source means adding the site to the Shortcuts section on the Home screen; the current text reads as generically creating a shortcut and is inconsistent with menu_add_to_home_screen (添加到主屏幕).
- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Remove from Shortcuts" is rendered as "remove the shortcut", losing the reference to the Shortcuts list.
    - Current: `移除快捷方式`
    - Source: `Remove from Shortcuts`
    - Suggest: `从快捷方式中移除`
    - The source means removing the site from the Shortcuts collection; the translation reads as deleting a shortcut generically and drops the "from Shortcuts" target.
- `onboarding_first_screen_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "No distractions" is mistranslated as "高效率" (high efficiency).
    - Current: `快速，隐私，高效率。`
    - Source: `Fast. Private. No distractions.`
    - Suggest: `快速。隐私。无干扰。`
    - The source's third attribute is the absence of distractions, not efficiency.
- `preference_autocomplete_topsite_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "over 450 popular URLs" is rendered as "热门网站" (popular websites) instead of URLs/网址.
    - Current: `超过 450 个热门网站`
    - Source: `Enable to have %s autocomplete over 450 popular URLs in the address bar.`
    - Suggest: `超过 450 个热门网址`
    - Source says "450 popular URLs"; other strings in the same screen consistently translate URL as 网址.
- `preference_option_phone_feature_ask_to_allow` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Ask to allow" is rendered as "始终询问" ("always ask"), adding "always" which is not in the source.
    - Current: `始终询问`
    - Source: `Ask to allow`
    - Suggest: `请求允许`
    - The source says "Ask to allow"; the developer comment mentions the permission must be asked, but the standard Mozilla zh-CN rendering is "请求允许" rather than "始终询问".
- `preference_privacy_and_security_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "data choices" is rendered as "数据反馈" (data feedback), which changes the meaning.
    - Current: `跟踪、Cookie、数据反馈`
    - Source: `Tracking, cookies, data choices`
    - Suggest: `跟踪、Cookie、数据选择`
    - The source "data choices" refers to user choices about data collection, not to sending feedback data.
- `preference_privacy_block_content_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "some pages" is translated as "部分网站" (some sites) instead of pages.
    - Current: `启用可能导致部分网站运作不正常`
    - Source: `Enabling may cause some pages to behave unexpectedly`
    - Suggest: `启用可能导致部分页面运作不正常`
    - The source says "pages", not "sites"; Focus distinguishes site vs page elsewhere.
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — The descriptive statement is turned into an imperative request ("请使用指纹解锁").
    - Current: `请使用指纹解锁。`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `可使用指纹解锁。`
    - The source "Unlock using fingerprint if…" describes what the setting does; "请" makes it an instruction to the user, altering the meaning of the preference summary.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Translation says "we do not save browsing history" instead of the source's "we never save and cannot restore this tab".
    - Current: `我们不会保存浏览历史，因此无法还原此标签页。`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `我们绝不会保存，也无法还原此标签页。`
    - The source says the private browser never saves this tab, not that it doesn't save browsing history; the added causal claim is not in the source.
- `tab_crash_report_headline` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Translation adds "and has crashed" which is not in the source, and contains a stray fullwidth-plus-space punctuation.
    - Current: `抱歉， 此标签页出现问题并已崩溃。`
    - Source: `Sorry. We’re having a problem with this tab.`
    - Suggest: `抱歉，此标签页出现问题。`
    - Source is "Sorry. We’re having a problem with this tab." — no crash statement; also the comma is followed by a spurious space.
- `tool_tip_dismiss_button_content_description` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Dismiss" rendered as "知道了" (Got it) for a close-button content description.
    - Current: `知道了`
    - Source: `Dismiss`
    - Suggest: `关闭`
    - The developer comment says this is the content description of the "X" button that closes the tooltip; screen readers should announce a dismiss/close action.
- `tool_tip_title` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Title rewritten as "Protecting you is my primary duty" instead of "You’re protected!".
    - Current: `保护您是我的首要职责`
    - Source: `You’re protected!`
    - Suggest: `您已受到保护！`
    - The source states the user is protected; the translation invents a first-person mission statement.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `biometric_prompt_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Uses informal "你" while the locale convention is the formal "您".
    - Current: `你可以验证指纹以继续当前应用会话。`
    - Source: `You can use your fingerprint to continue your current app session.`
    - Suggest: `您可以验证指纹以继续当前应用会话。`
    - zh-CN register convention for this tree is formal (您); neighboring strings such as cfr_cookie_banner and cfr_for_start_browsing use 您.
- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Enhanced Tracking Protection" is translated as "跟踪保护", losing "Enhanced" and diverging from the established term 增强型跟踪保护.
    - Current: `将禁用跟踪保护功能`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `将禁用增强型跟踪保护功能`
    - The same term is rendered 增强型跟踪保护 in enhanced_tracking_protection; here "Enhanced" is dropped.
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — Uses informal "你" while the locale convention is the formal "您".
    - Current: `用你的方式搜你所寻`
    - Source: `Your search, your way`
    - Suggest: `用您的方式搜您所寻`
    - The zh-CN tree is established as formal register (您); neighboring first-run strings such as firstrun_privacy_text and firstrun_shortcut_text use 您.
- `preference_performance_block_webfonts` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Block" is rendered as "拦截" here but as "阻止" in the neighboring Block JavaScript preference, an inconsistency on the same settings screen.
    - Current: `拦截网络字体`
    - Source: `Block web fonts`
    - Suggest: `阻止网络字体`
    - preference_performance_block_javascript translates "Block" as "阻止"; the same term on the same surface should be consistent.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-zh-rCN/strings.xml` — "Block" is translated as 阻止 here but as 拦截 in the neighbouring cookie-blocking option strings.
    - Current: `阻止 Cookie`
    - Source: `Block cookies`
    - Suggest: `拦截 Cookie`
    - On the same settings screen preference_privacy_should_block_cookies_cross_site_option uses 拦截跨站 Cookie, so the category title should use the same verb.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/zh-CN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
