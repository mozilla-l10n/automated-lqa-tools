# Focus for Android l10n QA — ja

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

Also for ja: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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

- `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 10, `corner` 2 | **curly-double** |
| ellipsis | `char` 11, `ascii` 10 | _mixed_ |
| fullwidth | `punctuation` 728 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (9)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 9 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Search and browse right in the app" is mistranslated as "search and browse appropriately in the app".
    - Current: `アプリで適切に検索、閲覧`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `アプリ内で直接検索、閲覧`
    - "right in the app" means "directly within the app", not "appropriately" (適切に).
- `menu_add_to_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Add to Shortcuts" is rendered as "Add a shortcut", losing the destination (the Shortcuts list) and conflicting with the parallel item "ホーム画面に追加".
    - Current: `ショートカットを追加`
    - Source: `Add to Shortcuts`
    - Suggest: `ショートカットに追加`
    - The source means adding the current site to the Shortcuts list (per developer comment), i.e. 「ショートカットに追加」; 「ショートカットを追加」 says a shortcut is being created rather than added to Shortcuts.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — Translation adds content not present in the source ("後で再度試してみてください").
    - Current: `この問題は恐らく一時的なものですので、後で再度試してみてください。`
    - Source: `This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server. { <br/> }{ <br/> } If you’ve connected to this server successfully in the past, the error may be temporar…`
    - Suggest: `この問題は一時的なものである可能性があります。`
    - The source only says "the error may be temporary"; the instruction to try again later is invented.
- `preference_daily_usage_ping_title` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Daily usage ping" is rendered as "send daily usage frequency", changing the meaning.
    - Current: `毎日の使用頻度を送信する`
    - Source: `Daily usage ping`
    - Suggest: `1 日 1 回の使用状況 ping`
    - The source names a data item (a daily usage ping), not a frequency of use; "使用頻度" (usage frequency) is wrong content and the added "送信する" is not in the source.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — Past-tense statement about what the user has already done is rendered as a future/general action.
    - Current: `これらのサイトではコンテンツブロッキングを無効にします。`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `これらのウェブサイトではコンテンツブロックを無効にしています。`
    - Source "You have disabled content blocking for these websites." describes the current state of the exception list; the translation reads as "will disable".
- `preference_privacy_block_social_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — The translation says the trackers "are displayed like share buttons" instead of "display functionality like share buttons".
    - Current: `ユーザーの訪問を追跡するためサイトに埋め込まれ、共有ボタンのように表示されます`
    - Source: `Embedded on sites to track your visits and to display functionality like share buttons`
    - Suggest: `ユーザーの訪問を追跡したり、共有ボタンなどの機能を表示したりするためサイトに埋め込まれます`
    - Source: "Embedded on sites to track your visits and to display functionality like share buttons" — the second purpose is providing/displaying features such as share buttons, not the tracker itself appearing like a share button.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "potentially dangerous and deceptive sites" is rendered as a single category "potentially dangerous deceptive sites", dropping the conjunction.
    - Current: `潜在的に危険な詐欺サイトをブロック`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `危険な可能性のあるサイトや詐欺サイトをブロック`
    - The source lists two kinds of sites (dangerous and deceptive); the translation merges them into one, narrowing the meaning.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "For top sites" is rendered as 人気サイト (popular sites) without the "for" relation and using a different term than the app's top sites terminology.
    - Current: `人気サイト`
    - Source: `For top sites`
    - Suggest: `トップサイト用`
    - The paired string "For sites you add" is translated 追加したサイト; here 人気サイト mistranslates "top sites", which elsewhere in Focus (remove_top_site / rename_top_site context) refers to the Top Sites feature.
- `search_add_error_duplicate_name` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — The translation says a search engine with the same name is already installed, instead of an installed search engine already using that name — meaning is shifted and "that name" is lost.
    - Current: `同名の検索エンジンがすでにインストールされています。`
    - Source: `An installed search engine is already using that name.`
    - Suggest: `インストール済みの検索エンジンがすでにその名前を使用しています。`
    - Source: "An installed search engine is already using that name." The error is about the name entered by the user being taken; the Japanese reads as if a same-named engine is installed, dropping the reference to the entered name.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ja/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
