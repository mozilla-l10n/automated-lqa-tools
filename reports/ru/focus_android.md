# Focus for Android l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 250 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for ru: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Strings | 250 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 43, `straight-double` 2 | **guillemet** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 6 | **em** |
| register | `informal` 146, `formal` 484 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (14)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 10 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Erase to delete cookies as well as search and browsing history" is translated as two separate actions "Стирайте и удаляйте", losing the meaning that erasing deletes the data.
    - Current: `Стирайте и удаляйте куки, историю поиска и просмотра`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `Стирайте, чтобы удалить куки, а также историю поиска и просмотра`
    - The source describes the Erase action which deletes cookies and history; the translation turns it into two unrelated verbs.
- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Dismiss" is rendered as "Пропустить" (skip) instead of a closing/dismissing action.
    - Current: `Пропустить`
    - Source: `Dismiss`
    - Suggest: `Закрыть`
    - Per the developer comment, tapping the overlay dismisses typing mode and returns to the browser; "Пропустить" means "skip", not "dismiss/close".
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Your search, your way" is rendered as "Ваш поиск, Ваш Интернет" ("your Internet"), which changes the meaning and adds an incorrect capital letter.
    - Current: `Ваш поиск, Ваш Интернет`
    - Source: `Your search, your way`
    - Suggest: `Ваш поиск — по-вашему`
    - The source says "your way" (how you like it), not "your Internet"; also "Ваш" mid-sentence is wrongly capitalized.
- `notification_erase_text_android_14_1` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "swipe this notification" is rendered as "снимите", which does not convey swiping the notification away.
    - Current: `Нажмите или снимите это уведомление`
    - Source: `Tap or swipe this notification to securely erase your browsing history.`
    - Suggest: `Нажмите или смахните это уведомление`
    - The source instructs the user to tap or swipe the notification; "снимите" (remove/take off) is not the swipe gesture and reads as a different action.
- `preference_block_autoplay_audio_only_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Recommended" is translated as "Желательно" (desirable) instead of "Рекомендуется".
    - Current: `Желательно`
    - Source: `Recommended`
    - Suggest: `Рекомендуется`
    - The source marks this option as the recommended setting; "Желательно" means "desirable/preferably" and is not the standard rendering of "Recommended".
- `preference_category_web_content` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Web Content" is translated as "Сетевое содержимое" (network content).
    - Current: `Сетевое содержимое`
    - Source: `Web Content`
    - Suggest: `Веб-содержимое`
    - The source term is "Web content"; "сетевое" means "network", and the file elsewhere uses "веб-" (веб-сайты, веб-шрифты).
- `preference_option_phone_feature_allowed` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Allowed" (a state label) is rendered as the imperative verb "Разрешить" (Allow).
    - Current: `Разрешить`
    - Source: `Allowed`
    - Suggest: `Разрешено`
    - The developer comment says this is a label indicating the permission state "Allowed", not an action; the adjacent "Blocked" label has the same problem.
- `preference_option_phone_feature_blocked` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Blocked" (a state label) is rendered as the imperative verb "Блокировать" (Block).
    - Current: `Блокировать`
    - Source: `Blocked`
    - Suggest: `Заблокировано`
    - Per the developer comment this label indicates the permission is blocked, a state, not an action to perform.
- `preference_phone_feature_media_key_system_access` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "DRM-controlled content" is translated as "copyright-protected content", losing the DRM reference.
    - Current: `Защищённое авторским правом содержимое`
    - Source: `DRM-controlled content`
    - Suggest: `Содержимое,控制ируемое DRM`
    - The source refers specifically to DRM (EME) controlled content, not to copyright protection in general; Firefox uses "Содержимое, контролируемое DRM".
- `preference_search_restore` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — Translation drops "default", changing "Restore default search engines" to "Restore search engines".
    - Current: `Восстановить поисковые системы`
    - Source: `Restore default search engines`
    - Suggest: `Восстановить поисковые системы по умолчанию`
    - The source and developer comment specify restoring the default list of search engines; "default" is omitted in the target.
- `preference_subitem_autocomplete` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "URL Autocomplete" is rendered as "URL-адрес автодополнения" ("URL of the autocomplete"), reversing the meaning.
    - Current: `URL-адрес автодополнения`
    - Source: `URL Autocomplete`
    - Suggest: `Автодополнение URL`
    - The source names a settings screen for URL autocomplete behavior; the Russian says "URL address of autocomplete", which is a different, nonsensical meaning.

### C. Grammar, agreement & spelling

- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — Placeholder for the app name is left ungoverned, producing "автодополнение Firefox Focus URL ваших любимых сайтов", which garbles the sentence.
    - Current: `Включить автодополнение %s URL ваших любимых сайтов.`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `Включите, чтобы %s автоматически дополнял URL ваших любимых сайтов.`
    - The source says "Enable to have %s autocomplete your favorite URLs"; the Russian juxtaposes the app name and "URL" without any grammatical link, unlike the parallel string preference_autocomplete_topsite_summary2 which uses "в %s".

### D. Terminology, register & consistency

- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "Navigate forward" translated as bare "Вперёд", inconsistent with "Перейти назад" used for the paired back button.
    - Current: `Вперёд`
    - Source: `Navigate forward`
    - Suggest: `Перейти вперёд`
    - The paired string content_description_back uses "Перейти назад" for "Navigate back"; the forward counterpart drops the verb, breaking consistency on the same surface.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-ru/strings.xml` — "top sites" translated as colloquial "топ сайтов" instead of the established term.
    - Current: `Для топа сайтов`
    - Source: `For top sites`
    - Suggest: `Для топ сайтов`
    - "Top sites" is a UI feature name; "топа сайтов" is colloquial and inconsistent with the term used elsewhere (top site strings).

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ru/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
