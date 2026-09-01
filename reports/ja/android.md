# Android l10n QA — ja

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **Previous run** | 2026-08-24 @ `e8622a909368` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 2,717 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ja: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (1)

- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — Markup tags are misplaced: text falls outside the { <li> } elements and the second bullet drops the "forward slashes" instruction.
    - Current: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> }{ </li> } のようなものになります。 { <li> }スラッシュ ({ <strong> }/{ </strong> }) { </li> }が使われているか確認してください。`
    - Source: `{ <ul> } { <li> }Web addresses are usually written like { <strong> }http://www.example.com/{ </strong> }{ </li> } { <li> }Make sure that you’re using forward slashes (i.e. { <strong> }/{ </strong> }).{ </li> } { </ul> }`
    - Suggest: `{ <li> }ウェブのアドレスは通常 { <strong> }http://www.example.com/{ </strong> } のようなものになります。{ </li> } { <li> }スラッシュ ({ <strong> }/{ </strong> }) が使われているか確認してください。{ </li> }`
    - The closing { </li> } tags appear before the trailing Japanese text, so the sentences render outside the list items, unlike the en-US source where each sentence is fully inside { <li> }.

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (16)

- `sports_widget_champions_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Champions" of the World Cup is rendered as 優勝者 (individual winner) rather than the winning team/champions.
    - Current: `2026 ワールドカップ優勝者`
    - Suggest: `2026 ワールドカップ優勝チーム`
    - The widget celebrates the winning national team in a soccer tournament; 優勝者 denotes an individual person, which misnames the subject.
- `sports_widget_countdown_hours` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Countdown hour abbreviation exceeds the 1–2 character limit hinted, but 時間 is 2 chars — actually fine.
    - Current: `時間`
    - Suggest: `時`
    - The developer comment asks for a single-character equivalent where one exists; Japanese has 時 for hours, and 時間 risks truncation issues in the countdown pill.
- `sports_widget_countdown_remaining_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Translation says "until the match starts" although the source only announces the generic remaining time.
    - Current: `試合開始まであと %1$d 日 %2$d 時間 %3$d 分。`
    - Suggest: `残り時間。%1$d 日 %2$d 時間 %3$d 分。`
    - The source is "Remaining time. Days: %1$d. Hours: %2$d. Minutes: %3$d." with no mention of a match start; adding 試合開始まで introduces content not in the source.
- `sports_widget_live_score_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Soccer scores are rendered as "ポイント" (points), which is not in the source and is wrong for soccer goals.
    - Current: `%1$s %2$d ポイント、%3$s %4$d ポイント、%5$s、ライブ`
    - Suggest: `%1$s %2$d、%3$s %4$d、%5$s、ライブ`
    - The source is just "%1$s %2$d, %3$s %4$d, %5$s, live"; the added unit "ポイント" introduces content not present and mislabels soccer goals as points.
- `sports_widget_match_elapsed_minutes` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Placeholder may contain "90+3", so appending 分 after it is fine, but the label drops "in minutes" wording; more importantly the value can be non-numeric.
    - Current: `経過時間: %1$s 分`
    - Suggest: `経過時間 (分): %1$s`
    - Source is "Elapsed time in minutes: %1$s" where the unit qualifies the label, not the value; the clock value can be "90+3", so "90+3 分" reads incorrectly.
- `sports_widget_round_of_16` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Round of 16" is rendered as 「ラウンド 16」 instead of the standard Japanese soccer term.
    - Current: `ラウンド 16`
    - Suggest: `ラウンド 16 (ベスト 16)`
    - Round of 16 is the last-16 stage; 「ラウンド 16」 reverses the meaning of the numeral (it reads as "the 16th round") and the standard term is ベスト16/決勝トーナメント1回戦.
- `sports_widget_team_followed_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Check back for match info" (an instruction to the user to return later) is translated as a statement that info will be updated.
    - Current: `大会が近づくにつれて、試合情報が更新されます。`
    - Suggest: `大会が近づいたら、また試合情報を確認してください。`
    - The source asks the user to check back; the translation drops the call to action and asserts that information will be updated.
- `sports_widget_upcoming` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Upcoming" as a section header for matches that have not started yet is rendered as 「近日公開」 (coming soon, for media releases).
    - Current: `近日公開`
    - Suggest: `今後の試合`
    - The developer comment says this is a section header for upcoming soccer matches; 近日公開 means "coming soon (release)" and is wrong for scheduled matches.
- `cookie_banner_exception_panel_title_state_off_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — Half-width question mark used where the locale convention is fullwidth punctuation.
    - Current: `無効にしますか?`
    - Suggest: `無効にしますか？`
    - The ja tree uses fullwidth punctuation (e.g. enable_search_suggestion_title2 uses ？).
- `cookie_banner_exception_panel_title_state_on_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — Half-width question mark used where the locale convention is fullwidth punctuation.
    - Current: `有効にしますか?`
    - Suggest: `有効にしますか？`
    - The ja tree uses fullwidth punctuation; sibling strings in this batch use ？.
- `cookie_banner_reject_all_option_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "when possible" is rendered as "可能な限り減らします", attaching the qualifier to the wrong clause.
    - Current: `Cookie 同意確認を自動的に拒否することで、表示されるバナーを可能な限り減らします。`
    - Suggest: `可能な場合は Cookie 要求を自動的に拒否することで、表示されるバナーを減らします。`
    - In the source "when possible" qualifies the automatic rejection of cookie requests, not the extent of banner reduction.
- `cookie_banner_report_a_site_snackbar_label` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Request to support site submitted" is mistranslated as a request sent to a "support site".
    - Current: `サポートサイトへのリクエストが送信されました。`
    - Suggest: `このサイトのサポートをリクエストしました。`
    - The source means a request for the site to be supported (by cookie banner reduction) was submitted, not a request sent to a support site.
- `cookie_banner_the_site_was_reported` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Request to support site submitted" is mistranslated as a request sent to a "support site".
    - Current: `サポートサイトへのリクエストが送信されました。`
    - Suggest: `このサイトのサポートをリクエストしました。`
    - The source means a request to add support for this site was submitted; the Japanese says a request was sent to a support site.
- `menu_trackers_blocked_title` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Trackers blocked" is rendered as 「ブロックされた追跡」 instead of the established term for trackers (トラッカー).
    - Current: `ブロックされた追跡`
    - Suggest: `ブロックしたトラッカー`
    - The source refers to trackers (tracking scripts/entities), which Mozilla ja consistently renders as トラッカー; 追跡 means the act of tracking, not the trackers themselves.
- `preference_open_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Switch to link in new tab" mistranslated as "switch to the link inside the new tab".
    - Current: `新しいタブ内のリンクへすぐに切り替えます`
    - Suggest: `リンクを新しいタブで開いたらすぐに切り替えます`
    - Per the developer comment the preference switches to the newly opened tab immediately; the translation says switching to a link located inside a new tab.
- `preference_search_installed_search_engines` — `mozilla-mobile/focus-android/app/src/main/res/values-ja/strings.xml` — "Installed search engines" is translated as "selectable search engines".
    - Current: `選択可能な検索エンジン`
    - Suggest: `インストール済みの検索エンジン`
    - The developer comment says this is a header for the list of installed search engines; 選択可能 (selectable) states something different from the source.

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 43 |
| Strings | 2,717 |
| Missing strings | 18 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 1 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**18 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — 13
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ja/strings.xml` — 5

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 10, `corner` 2 | **curly-double** |
| ellipsis | `char` 11, `ascii` 10 | _mixed_ |
| fullwidth | `punctuation` 711 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (144)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 112 |
| 3 | Degraded language (grammar, spelling, terminology) | 25 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

- `downloads_delete_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — `downloads_delete_dialog_title` has plural variant ['one'], which ja does not have
    - Current: `{$quantity ->} [one] ファイルを削除しますか？ [other] %d 個のファイルを削除しますか？`
    - Source: `{$quantity ->} [one] Delete file? [other] Delete %d files?`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_content_crashed_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — "Content crashed" is translated as コンテンツデータのクラッシュ, introducing データ not in the source.
    - Current: `コンテンツデータのクラッシュ`
    - Source: `Content crashed`
    - Suggest: `コンテンツがクラッシュしました`
    - The source refers to the content process crashing, not to "content data"; the added データ changes the meaning.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — "the device's network connection" is rendered as コンピューターのネットワーク接続 (computer), wrong on a mobile browser.
    - Current: `他のサイトも表示できない場合、コンピューターのネットワーク接続を確認してください。`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `他のサイトも表示できない場合、端末のネットワーク接続を確認してください。`
    - The source says "Check the device’s network connection"; other strings in this file translate device as 端末.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — “device” is translated as コンピューター (computer) in a mobile browser context.
    - Current: `コンピューターが有効なネットワークに接続されているか確認してください。`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `端末が有効なネットワークに接続されているか確認してください。`
    - The source says “Is the device connected to an active network?”; ja renders it as “computer”, which names the wrong thing on a mobile app.
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — The example domain mozilla.org was changed to mozilla.jp, altering the source's example.
    - Current: `リクエストされたアドレスのポート (例えば mozilla.jp のポート 80 であれば { <q> }mozilla.jp:80{ </q> })`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `リクエストされたアドレスのポート (例えば mozilla.org のポート 80 であれば { <q> }mozilla.org:80{ </q> })`
    - The source uses “mozilla.org:80” as the example; substituting a different domain (mozilla.jp) changes the content and misrepresents the brand's domain.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — “your device” is translated as ご利用のコンピューター (your computer).
    - Current: `ご利用のコンピューターではなくサーバーの設定に問題がある`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `ご利用の端末ではなくサーバーの設定に問題がある`
    - The source says “a server configuration issue and not your device”; ja renders device as computer, inconsistent with 端末 used elsewhere in the same file.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — “device” is translated as コンピューター (computer) in a mobile browser context.
    - Current: `コンピューターが有効なネットワークに接続されているか確認してください。`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `端末が有効なネットワークに接続されているか確認してください。`
    - The source reads “Is the device connected to an active network?”; ja says “computer”, which is not what the source names (other strings in this batch use 端末 for device).
- `mozac_feature_addons_admin_install_only` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — The reason clause is mistranslated: the source says the add-on can only be installed by an organization using enterprise policies, which isn't supported on this platform, but the Japanese reads as an unrelated contrastive statement.
    - Current: `これはエンタープライズポリシーを使用する組織によってインストールすることができますが、このプラットフォームではサポートされていません。`
    - Source: `%1$s could not be installed because it can only be installed by an organization using enterprise policies, which isn‘t supported on this platform.`
    - Suggest: `これはエンタープライズポリシーを使用する組織によってのみインストールできますが、この方法はこのプラットフォームではサポートされていません。`
    - The source's "only be installed by" (排他) is dropped, changing the meaning of why installation failed.
- `mozac_feature_addons_permissions_user_scripts_extra_warning` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — "extensions or sources you trust" is mistranslated so that "trusted" only modifies sources, allowing any extension's scripts.
    - Current: `拡張機能や信頼できるソースからのスクリプト以外は実行しないでください。`
    - Source: `Unverified scripts can pose security and privacy risks. Only run scripts from extensions or sources you trust.`
    - Suggest: `信頼できる拡張機能やソースからのスクリプト以外は実行しないでください。`
    - The source says to run only scripts from extensions or sources you trust; the Japanese reads "extensions, or trusted sources", dropping the trust qualifier from extensions and weakening the security warning.
- `mozac_feature_addons_status_incompatible` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — The translation drops "your version of", changing the meaning to the add-on being incompatible with the app version generically.
    - Current: `%1$s は %2$s のバージョン (%3$s) と互換性がありません。`
    - Source: `%1$s is not compatible with your version of %2$s (version %3$s).`
    - Suggest: `%1$s はお使いの %2$s のバージョン (%3$s) と互換性がありません。`
    - Source is "%1$s is not compatible with your version of %2$s (version %3$s)." — the possessive "your version" indicates the user's installed version.
- `mozac_feature_addons_supported_checker_notification_channel` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — "Supported" is dropped from the notification channel name.
    - Current: `アドオンチェッカー`
    - Source: `Supported add-ons checker`
    - Suggest: `対応アドオンチェッカー`
    - Source is "Supported add-ons checker"; the channel is specifically about newly supported add-ons.
- `mozac_feature_addons_updater_dialog_last_attempt` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — "Last attempt:" is rendered as "last check date", adding "日" (date) and changing "attempt" to "check".
    - Current: `最終確認日:`
    - Source: `Last attempt:`
    - Suggest: `前回の試行:`
    - Source label is "Last attempt:" for the last add-on update attempt.
- `mozac_feature_addons_updater_status_no_update_available` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — Adds "アドオン" not present in source; the status field refers to a single add-on's update status, not "no add-ons with updates".
    - Current: `更新可能なアドオンはありません`
    - Source: `No update available`
    - Suggest: `更新はありません`
    - Source "No update available" is a status value for one add-on; the translation says "There are no add-ons available for update".
- `mozac_feature_addons_updater_status_successfully_updated` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — Adds "アドオン" which is not in the source status string.
    - Current: `アドオンの更新が完了しました`
    - Source: `Successfully updated`
    - Suggest: `更新が完了しました`
    - Source is "Successfully updated", a status field value with no subject noun.
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — Cause and effect are reversed: the source says the extensions stopped working, which made the system unstable.
    - Current: `システムを不安定にしている 1 個以上の拡張機能が動作を停止しました。`
    - Source: `One or more extensions stopped working, making your system unstable.`
    - Suggest: `1 個以上の拡張機能が動作を停止し、システムが不安定になりました。`
    - Source "One or more extensions stopped working, making your system unstable." — the instability is the result of the stoppage, not an attribute of the extensions.
- `mozac_feature_applinks_destination_url` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-ja/strings.xml` — "Destination URL" is rendered as 送信先 URL ("send-to/recipient URL"), which implies sending data rather than the link's destination.
    - Current: `送信先 URL`
    - Source: `Destination URL`
    - Suggest: `リンク先 URL`
    - The developer comment says it is the label for the destination URL of the link in the details section; 送信先 means the recipient of something sent (e.g. mail), not a navigation target.
- `switch_to_tab_description` — `mozilla-mobile/android-components/components/feature/awesomebar/src/main/res/values-ja/strings.xml` — "Switch to tab" is translated as タブを表示 ("Show tab"), losing the switch-to-an-already-open-tab meaning.
    - Current: `タブを表示`
    - Source: `Switch to tab`
    - Suggest: `タブに切り替え`
    - The comment states the suggestion represents an already opened tab and distinguishes it from history suggestions; 表示 does not convey switching.
- `mozac_feature_downloads_cancel_active_private_downloads_warning_content_body` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ja/strings.xml` — "Private tabs" is rendered as "プライベートウィンドウ" (private windows) instead of tabs.
    - Current: `すべてのプライベートウィンドウを今すぐ閉じると`
    - Source: `If you close all Private tabs now, %1$s download will be canceled. Are you sure you want to leave Private Browsing?`
    - Suggest: `すべてのプライベートタブを今すぐ閉じると`
    - The source says "If you close all Private tabs now"; on Android this refers to tabs, not windows.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-ja/strings.xml` — "choose tabs to close" is mistranslated as simply "close tabs", losing the choice/selection meaning.
    - Current: `タブを閉じてください`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `閉じるタブを選択してください`
    - The source offers the option of choosing which tabs to close (the companion button leads to the tabs tray to select sensitive tabs); the translation just orders closing tabs.
- `mozac_feature_prompts_suggest_strong_password_message` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ja/strings.xml` — Dialog title "Use strong password: %1$s" is rendered as an imperative request to the user rather than a label introducing the generated password.
    - Current: `強固なパスワードを使用してください: %1$s`
    - Source: `Use strong password: %1$s`
    - Suggest: `強固なパスワードを使用: %1$s`
    - The source is a title labeling the suggested password, matching the sibling title "Use strong password?"; "〜してください" turns it into a command to the user.
- `search_widget_content_description` — `mozilla-mobile/android-components/components/feature/search/src/main/res/values-ja/strings.xml` — "Open a new %1$s tab" is mistranslated as "open in a new tab of %1$s".
    - Current: `%1$s の新しいタブで開く`
    - Source: `Open a new %1$s tab`
    - Suggest: `%1$s の新しいタブを開く`
    - The source means opening a new tab, not opening something in an existing/new tab; the particle で changes the meaning.
- `mozac_feature_sitepermissions_do_not_ask_again_on_this_site2` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-ja/strings.xml` — "Remember decision for this site" is translated without the "for this site" scope.
    - Current: `今後も同様に処理する`
    - Source: `Remember decision for this site`
    - Suggest: `このサイトでの決定を記憶する`
    - The source scopes the checkbox to the current site; the sibling string ...site4 correctly includes 「このサイトでは」. Dropping it changes the meaning to a global setting.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ja/strings.xml` — The translation misrenders "summaries that stay in your control" as the user managing the summaries app creates.
    - Current: `一度ダウンロードしておけば、%s が作成するページの要約をユーザーが管理できます。`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `一度ダウンロードするだけで、%s はあなたの管理下にとどまるページ要約を作成できるようになります。`
    - The source says the one-time download enables %s to create page summaries that remain under the user's control (i.e. processed on device); the Japanese instead states the user can manage the summaries created by %s.
- `mozac_lib_crash_no_crashes` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ja/strings.xml` — "No crash reports have been submitted." is translated as "送信したクラッシュレポートはありません" but the surrounding intent is a list of crashes; the passive source is fine, though the target implies the user submitted them.
    - Current: `送信したクラッシュレポートはありません。`
    - Source: `No crash reports have been submitted.`
    - Suggest: `送信されたクラッシュレポートはありません。`
    - The source is passive and does not attribute the action to the user; 送信した reads as "reports that (I) submitted".
- `my_longest_fox_is` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-ja/strings.xml` — "My longest fox is %1$d!" is rendered as "私の得点は最長 %1$d フォックスです", which mixes in "score" and mistranslates the sentence subject.
    - Current: `私の得点は最長 %1$d フォックスです！`
    - Source: `My longest fox is %1$d! #longfox %2$s`
    - Suggest: `私の最長フォックスは %1$d です！`
    - The source says the longest fox is N; the target says "my score is at most/longest N fox", changing the meaning by introducing 得点 (score) and misplacing 最長.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Department" as an administrative division (Nicaragua, Colombia) is translated as 部門 (organizational department).
    - Current: `部門`
    - Source: `Department`
    - Suggest: `県 (デパルタメント)`
    - The developer comment states this is a key administrative division in countries like Nicaragua and Colombia, not a corporate/organizational department; 部門 means a division of an organization.
- `addresses_pin` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Pin" (India's Postal Index Number) is rendered as PIN, which in Japanese reads as a security PIN code rather than a postal code.
    - Current: `PIN`
    - Source: `Pin`
    - Suggest: `PIN コード (郵便番号)`
    - The developer comment clarifies this is the Postal Index Number used in India, an address/postal field, but the bare "PIN" in Japanese UI conventionally means a personal identification number.
- `addresses_province` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Province" is rendered as 都道府県, the Japan-specific term already used for both Prefecture and State, so the field name is wrong and indistinguishable.
    - Current: `都道府県`
    - Source: `Province`
    - Suggest: `州・県`
    - The developer comment says this label is used when "province" should be used (non-Japanese addresses); 都道府県 specifically denotes Japanese prefectures and duplicates addresses_prefecture/addresses_state.
- `ai_controls_banner_headline` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "You always have a choice in %s" is rendered as "%s has choices", dropping the user as the subject.
    - Current: `%s には常に選択肢があります`
    - Source: `You always have a choice in %s`
    - Suggest: `%s では、常にあなたに選択肢があります`
    - The source says the user always has a choice within the app; the translation reads as the app itself having options, losing the user-agency meaning.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "you can unblock anything you want to keep using" is turned into an imperative instruction to the user.
    - Current: `引き続き使用したい機能はブロックを解除してください。`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `その後、引き続き使用したい機能はいつでもブロックを解除できます。`
    - The source states a capability ("you can unblock"), not a directive; the translation tells the user to unblock, changing the meaning.
- `alternative_app_icon_option_flaming` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Flaming" is translated as 「炎上」, which in Japanese means an online backlash/flame war, not a flame-covered design.
    - Current: `炎上`
    - Source: `Flaming`
    - Suggest: `フレイム`
    - Per the developer comment the icon shows the logo surrounded by flames; 「炎上」 conveys an internet flaming scandal and is misleading.
- `alternative_app_icon_option_gradient_golden_hour` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Golden Hour" is translated as "マジックアワー" (magic hour), a different term.
    - Current: `マジックアワー`
    - Source: `Golden Hour`
    - Suggest: `ゴールデンアワー`
    - Golden hour and magic hour are distinct terms; the icon name should transliterate the source name, consistent with 「ブルーアワー」 for Blue Hour.
- `alternative_app_icon_option_purple_dark` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Dark Purple" is rendered as 小紫, which is a plant name (Callicarpa dichotoma), not a dark shade of purple.
    - Current: `小紫`
    - Source: `Dark Purple`
    - Suggest: `濃い紫`
    - The source means a dark shade of purple for the app icon color variant; 小紫 names a shrub and does not convey "dark purple".
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Added 「設定で」 and misstates the action: the source asks the user to select a language to manage the preferences, not to select languages in settings.
    - Current: `設定で [常に翻訳する] 言語と [翻訳しない] 言語を選択します。`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `[常に翻訳する] と [翻訳しない] の設定を管理する言語を選択してください。`
    - The en-US string instructs the user to pick a language in order to manage the "always translate"/"never translate" preferences; the target changes the meaning and inserts "in settings".
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — The translation reverses the direction: source says Firefox will never offer to translate sites in this language, target says it won't offer to translate sites into this language.
    - Current: `%1$s はサイトをこの言語に翻訳可能であることを通知しません。`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `%1$s はこの言語のサイトの翻訳を提案しません。`
    - "sites in this language" means sites written in this language (source language), not translating into this language.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "sites in this language" is mistranslated as translating sites into this language.
    - Current: `%1$s がサイトをこの言語に翻訳可能であることを通知します。`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `%1$s はこの言語のサイトの翻訳を提案します。`
    - The source refers to sites written in this language being offered for translation, not translation into this language; the parallel string automatic_translation_option_always_translate_summary_preference correctly uses 「この言語のページ」.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Navigate back" is rendered as "go back to the previous page", which is wrong for a bookmarks navigation bar back button.
    - Current: `前のページへ戻る`
    - Source: `Navigate back`
    - Suggest: `戻る`
    - The developer comment says this is the content description for the bookmark navigation bar back button; it navigates back in the bookmark folder hierarchy/screen, not to a previous web page.
- `browser_menu_sign_back_in_to_sync` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Sign back in to sync" is rendered as "log in and return to Sync", mistranslating "back in" as returning to Sync.
    - Current: `ログインして Sync に戻る`
    - Source: `Sign back in to sync`
    - Suggest: `再ログインして同期`
    - The source means to sign in again in order to sync; the Japanese says "log in and go back to Sync", which changes the meaning (the caption string confirms the context is re-authentication for syncing).
- `certificate_warning_homepage_card_hcw2_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Less than 7 days to update" is rendered as "残り 7 日以内に更新してください", an awkward and imprecise rendering of the remaining-time statement.
    - Current: `残り 7 日以内に更新してください`
    - Source: `Less than 7 days to left to update`
    - Suggest: `更新まで残り 7 日を切りました`
    - The source is a statement that fewer than 7 days remain to update, not an instruction phrased as "within the remaining 7 days".
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "on March 14" is rendered as "3 月 14 日以降" (from March 14 onward), changing the stated date semantics.
    - Current: `アドオンと一部の機能が 3 月 14 日以降に動作しなくなります。`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `アドオンと一部の機能が 3 月 14 日に動作しなくなります。`
    - The source says features stop working on March 14, not "from March 14 onward"; the added 以降 is not in the source.
- `certificate_warning_push_notification_pnw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "tomorrow" is rendered as "明日以降" (from tomorrow onward), adding meaning not in the source.
    - Current: `明日以降、一部の機能が動作しなくなります。`
    - Source: `Some features will stop working tomorrow.`
    - Suggest: `明日、一部の機能が動作しなくなります。`
    - The source states features stop working tomorrow; 以降 adds "onward", which the source does not say.
- `certificate_warning_push_notification_update_recommended_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — The noun phrase "Update recommended" is translated as an imperative "更新してください".
    - Current: `更新してください`
    - Source: `Update recommended`
    - Suggest: `更新を推奨します`
    - The developer comment states "Update" is a noun; the source is a recommendation notice, not a command.
- `collections_migration_homepage_card_message` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "a simpler way" is rendered as "さらに簡単な" (even easier), adding a comparison not in the source.
    - Current: `タブをさらに簡単に整理する方法があります`
    - Source: `There’s a simpler way to keep your tabs organized`
    - Suggest: `タブをもっと簡単に整理する方法があります`
    - The source says there is a simpler way to keep tabs organized; "さらに" implies an additional degree beyond an existing easy method.
- `content_description_gallery` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Brand name "Google Lens" is partly translated as "Google レンズ".
    - Current: `Google レンズに送信する`
    - Source: `Choose from gallery to send to Google Lens`
    - Suggest: `Google Lens に送信する`
    - Product/brand names must stay untranslated; the source is "Google Lens".
- `content_description_take_photo` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Brand name "Google Lens" is partly translated as "Google レンズ".
    - Current: `Google レンズに送信する`
    - Source: `Take photo and send to Google Lens`
    - Suggest: `Google Lens に送信する`
    - Product/brand names must stay untranslated; the source is "Google Lens".
- `context_menu_open_image_with_google_lens` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Brand name "Google Lens" is partly translated as "Google レンズ".
    - Current: `Google レンズで検索`
    - Source: `Search with Google Lens`
    - Suggest: `Google Lens で検索`
    - Product/brand names must stay untranslated; the source is "Google Lens".
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Navigate back" is rendered as "go back to the previous page", which refers to a web page rather than the settings screen back button.
    - Current: `前のページへ戻る`
    - Source: `Navigate back`
    - Suggest: `前に戻る`
    - The source is a generic "Navigate back" content description for the credit card feature top bar back button; "ページ" (page) introduces content not in the source and misdescribes the control.
- `debug_drawer_addresses_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Addresses" (postal addresses feature) is rendered as "アドレス", which means email/URL address, inconsistent with the related strings that use "住所".
    - Current: `アドレス`
    - Source: `Addresses`
    - Suggest: `住所`
    - The Debug Drawer Addresses feature is about postal addresses; sibling strings debug_drawer_add_new_address, debug_drawer_addresses_management_header and debug_drawer_delete_all_addresses all translate address as "住所".
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Content description says "go back to the previous page" instead of navigating back within the debug drawer.
    - Current: `前のページへ戻ります`
    - Source: `Navigate back`
    - Suggest: `前に戻ります`
    - The developer comment says this navigates back within the debug drawer, not to a previous web page; "ページ" introduces content not in the source "Navigate back".
- `debug_drawer_override_home_region_permanently` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — The translation drops "permanently", losing the distinction from the temporary override button.
    - Current: `ホームリージョンを上書きする`
    - Source: `Override home region permanently`
    - Suggest: `ホームリージョンを恒久的に上書き`
    - Source is "Override home region permanently"; without 恒久的に the label is indistinguishable from the temporary override actions.
- `debug_drawer_tab_tools_tab_quantity_exceed_max_error` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Exceeded the maximum" is translated as "上限に達しました" (reached the maximum) instead of exceeded.
    - Current: `に達しました`
    - Source: `Exceeded the maximum number of tabs (%1$s) that can be generated in one operation`
    - Suggest: `を超えました`
    - The source says the entered quantity exceeded the maximum; "達しました" means merely reached it, which is a different condition for this error message.
- `delete_browsing_data_prompt_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — The translation says the data is deleted "from %s" rather than that %s (the app) will delete the selected data.
    - Current: `選択した閲覧データを %s から削除します。`
    - Source: `%s will delete the selected browsing data.`
    - Suggest: `%s は選択した閲覧データを削除します。`
    - %s is the app name (e.g. Firefox) and is the subject performing the deletion, not the location the data is removed from.
- `delete_history_prompt_button_today_and_yesterday` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Today and yesterday" is rendered in reversed order as "昨日と今日".
    - Current: `昨日と今日`
    - Source: `Today and yesterday`
    - Suggest: `今日と昨日`
    - Source order is "Today and yesterday"; the translation reverses the terms.
- `download_languages_item_content_description_delete_in_progress_state` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "In progress" is rendered as 「削除中」 (deleting), adding meaning not in the source.
    - Current: `削除中`
    - Source: `In progress`
    - Suggest: `進行中`
    - The source string is the generic "In progress"; the Japanese states "deleting", which is a different (more specific) message than the source text.
- `etp_social_media_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Social Media Trackers" is rendered as "SNS メディアトラッカー", mixing SNS and メディア incorrectly.
    - Current: `SNS メディアトラッカー`
    - Source: `Social Media Trackers`
    - Suggest: `ソーシャルメディアトラッカー`
    - The source refers to social media trackers; "SNS メディア" is a redundant/incorrect coinage and inconsistent with the description string which uses ソーシャルネットワーク.
- `extension_process_crash_dialog_retry_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Button label is translated as an instruction to the user rather than the action "Try restarting extensions".
    - Current: `拡張機能を再起動してみてください`
    - Source: `Try restarting extensions`
    - Suggest: `拡張機能の再起動を試す`
    - This is a button label; the source is an action the button performs, not a polite request to the user.
- `felt_privacy_desc_card_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Leave no traces on this device" is mistranslated as "Do not let this device track you".
    - Current: `この端末を追跡させません`
    - Source: `Leave no traces on this device`
    - Suggest: `この端末に痕跡を残しません`
    - The source says no traces are left on the device; the translation says the device is prevented from tracking, which is a different meaning.
- `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "An extra barrier between websites" is rendered vaguely as "追加機能", losing the barrier-between-websites meaning.
    - Current: `タブ間でデータ保護を強化する追加機能です。`
    - Source: `An extra barrier between websites that helps protect your data across tabs. May affect performance, stability, website compatibility, and how browsing history is saved.`
    - Suggest: `ウェブサイト間に追加の隔壁を設け、タブをまたいだデータの保護を助けます。`
    - The source describes a barrier between websites protecting data across tabs; the translation omits "between websites" and replaces "barrier" with a generic "additional feature".
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — The notification title implies closing tabs of the app named by %1$s rather than "%1$s: N tabs closed".
    - Current: `%1$s のタブを %2$d 個閉じました`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s: %2$d 個のタブを閉じました`
    - %1$s is the app name used as a notification title prefix; "%1$s のタブ" wrongly reads as "tabs belonging to <app>" being closed, whereas the source states the app closed N tabs.
- `ip_protection_data_limit_reached_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Adds "初め" (first of the month) which is not in the source.
    - Current: `アクセスは来月初めにリセットされます。`
    - Source: `You’ve used all %1$d GB of your VPN data. Access resets next month.`
    - Suggest: `アクセスは来月リセットされます。`
    - Source says "Access resets next month." without specifying the beginning of the month; the parallel snackbar string correctly renders it as 来月リセットされます。
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "残り" (remaining) is inserted, changing the meaning of the reset value.
    - Current: `毎月初めに残り %1$.0f GB にリセットされます。`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `毎月初めに %1$.0f GB にリセットされます。`
    - Source is "Resets to %1$.0f GB on the first of every month." — %1$.0f is the total monthly allowance, not a remaining amount.
- _…and 55 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_feature_addons_migrated_from_a_previous_version_label` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — Missing possessive particle makes the phrase read as "the previous version %1$s" instead of "a previous version of %1$s".
    - Current: `以前のバージョン %1$s から移行されました`
    - Source: `This add-on was migrated from a previous version of %1$s`
    - Suggest: `以前のバージョンの %1$s から移行されました`
    - %1$s is the app name (Firefox); the source says "a previous version of %1$s", requiring の between バージョン and the app name.
- `mozac_feature_addons_permissions_data_collection_optional_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ja/strings.xml` — Double particle error: 「次のデータを収集を求めます」 uses を twice.
    - Current: `この拡張機能は次のデータを収集を求めます`
    - Source: `The developer says the extension wants to collect: %1$s`
    - Suggest: `この拡張機能は次のデータの収集を求めます`
    - Ungrammatical Japanese; the object marker を appears twice in the same clause. Source: "the extension wants to collect: ...".
- `download_language_file_dialog_message_all_languages` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Missing particle: 「翻訳のプライバシー保つため」 lacks 「を」.
    - Current: `翻訳のプライバシー保つため`
    - Source: `We download partial languages to your cache to keep translations private.`
    - Suggest: `翻訳のプライバシーを保つため`
    - The noun 「プライバシー」 requires the object particle 「を」 before 「保つ」; as written the sentence is ungrammatical.
- `tabs_header_normal_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Normal Tabs Open" is rendered as "通常の開いているタブ", an ungrammatical modifier order inconsistent with the private tabs string.
    - Current: `通常の開いているタブ`
    - Source: `Normal Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `開いている通常のタブ`
    - Parallel string tabs_header_private_tabs_counter_title uses "開いているプライベートタブ"; "通常の開いているタブ" misplaces the modifier.
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Synced Tabs Open" is rendered as "同期した開いているタブ", an ungrammatical modifier order.
    - Current: `同期した開いているタブ`
    - Source: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `開いている同期タブ`
    - "Synced" should modify "tabs", parallel to the private tabs string "開いているプライベートタブ".

### D. Terminology, register & consistency

- `mozac_browser_errorpages_security_bad_hsts_cert_advanced` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — “Advanced…” is rendered as 詳細情報 here but 詳細設定 in the parallel bad_cert string, and uses ASCII dots instead of the ellipsis character.
    - Current: `詳細情報...`
    - Source: `Advanced…`
    - Suggest: `詳細設定…`
    - Same source string “Advanced…” in mozac_browser_errorpages_security_bad_cert_advanced is translated 詳細設定…; the two buttons on equivalent error pages should match.
- `mozac_feature_downloads_notification_channel` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ja/strings.xml` — Notification channel name "Downloads" rendered as "ダウンロード一覧" (downloads list) instead of the standard "ダウンロード".
    - Current: `ダウンロード一覧`
    - Source: `Downloads`
    - Suggest: `ダウンロード`
    - This is the name of the notification channel for download notifications, not a list UI; the established term is ダウンロード.
- `a11y_action_label_wallpaper_collection_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Talkback action label is translated as a full sentence instead of a verb phrase that completes "Double tap to…".
    - Current: `このコレクションの詳細についてはリンク先をご覧ください`
    - Source: `open link to learn more about this collection`
    - Suggest: `このコレクションの詳細を見るためリンクを開く`
    - Per the developer comment, Talkback appends this to "Double tap to…", so it must be an action phrase like the other labels (折りたたむ, 展開する), not an imperative sentence addressed to the user.
- `ai_controls_block_ai_title` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "AI enhancements" is rendered as 「AI 支援」 here but as 「AI 機能強化」 in the sibling description and banner strings.
    - Current: `AI 支援をブロックする`
    - Source: `Block AI enhancements`
    - Suggest: `AI 機能強化をブロックする`
    - ai_controls_block_ai_description and ai_controls_blocked_info_banner use 「AI 機能強化」 for the same source term on the same screen; the inconsistency is confusing.
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "clear" is rendered as 削除 here but 消去 in the parallel confirm_clear_permissions_* strings.
    - Current: `このサイトのこの許可設定を削除してもよろしいですか？`
    - Source: `Are you sure that you want to clear this permission for this site?`
    - Suggest: `このサイトのこの許可設定を消去してもよろしいですか？`
    - Same source verb "clear" on the same dialog surface should use one term consistently.
- `debug_drawer_override_current_region_label` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — A text field label is rendered as a sentence with a verb ending, unlike the source noun-phrase label.
    - Current: `現在のリージョンを上書きします`
    - Source: `Override current region`
    - Suggest: `現在のリージョンを上書き`
    - Per the developer comment this is a text field label, not a descriptive sentence; the parallel button string debug_drawer_override_region uses the noun form "上書き".
- `debug_drawer_override_home_region_label` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — A text field label is rendered as a sentence with a verb ending, unlike the source noun-phrase label.
    - Current: `ホームリージョンを上書きします`
    - Source: `Override home region`
    - Suggest: `ホームリージョンを上書き`
    - Per the developer comment this is a text field label; sibling strings use the noun form "上書き".
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "region" is rendered as "地域" here but as "リージョン" in every other Region Tools string.
    - Current: `ホームと現在の地域値`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `ホームと現在のリージョンの値`
    - Inconsistent terminology within the same Debug Drawer Region Tools surface, where debug_drawer_region_tools_title, debug_drawer_home_region_label and debug_drawer_current_region_label all use リージョン.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "trackers" is rendered as 追跡者 instead of the established term トラッカー used for tracking blocking in Firefox.
    - Current: `追跡者を捕まえよう`
    - Source: `Help catch trackers`
    - Suggest: `トラッカーを捕まえよう`
    - Elsewhere in the product "trackers" (blocked trackers card) is translated as トラッカー; 追跡者 means a person following someone and is inconsistent terminology on the same surface.
- `likert_scale_option_5` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Very satisfied" and "Very dissatisfied" use inconsistent renderings of "Very" within the same likert scale.
    - Current: `非常に不満`
    - Source: `Very dissatisfied`
    - Suggest: `とても不満`
    - likert_scale_option_1 renders "Very satisfied" as とても満足; the symmetric scale endpoint should use the same intensifier for consistency on the same surface.
- `onboarding_redesign_sync_body` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "encryption" mistranslated as 暗号 (cipher) instead of 暗号化.
    - Current: `すべて暗号で保護されます。`
    - Source: `Get bookmarks, tabs, and passwords on any device. All protected with encryption.`
    - Suggest: `すべて暗号化で保護されます。`
    - The source says "All protected with encryption"; 暗号 means "cipher/code", the standard Japanese term for encryption is 暗号化.
- `preferences_credit_cards_sync_cards` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Sync cards" is rendered as "クレジットカード情報" while the neighbouring card strings use 「カード情報」.
    - Current: `クレジットカード情報を同期`
    - Source: `Sync cards`
    - Suggest: `カード情報を同期`
    - Sibling strings (preferences_credit_cards_add_credit_card_2, _manage_saved_cards_2, _sync_cards_across_devices) all translate "card" as 「カード情報」; only this one adds 「クレジット」, an inconsistency on the same settings surface.
- `preferences_privacy_report` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Privacy report" is rendered as プライバシー報告 here but プライバシーレポート in the related title string on the same screen.
    - Current: `プライバシー報告`
    - Source: `Privacy report`
    - Suggest: `プライバシーレポート`
    - The same feature name must be consistent on the same surface; preferences_privacy_report_title uses プライバシーレポート.
- `privacy_notice_updated_homepage_message_privacy_notice` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Privacy Notice" is translated as プライバシー通知 instead of the established Mozilla ja term プライバシー通知書/プライバシーノーティス.
    - Current: `プライバシー通知`
    - Source: `Privacy Notice`
    - Suggest: `プライバシー通知書`
    - Mozilla's ja localization consistently uses プライバシー通知書 for the legal document "Privacy Notice"; プライバシー通知 reads as a notification rather than the policy document.
- `protection_panel_etp_toggle_label` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Enhanced Tracking Protection" is rendered inconsistently with the surrounding protection panel strings, which use 追跡防止/トラッキング防止 variants.
    - Current: `強化型トラッキング防止`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `強化型トラッキング保護`
    - The established Mozilla ja term for Enhanced Tracking Protection is 強化型トラッキング保護; the panel also uses 追跡防止 elsewhere, so the same source term appears in three different forms on one surface.
- `protection_panel_num_trackers_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — "Trackers" is translated as 追跡 here while other strings in the same panel use トラッカー.
    - Current: `ブロックされた追跡: %d`
    - Source: `Trackers blocked: %d`
    - Suggest: `ブロックしたトラッカー: %d`
    - protection_panel_banner_protected_blocked_trackers_description and protection_panel_etp_disabled_no_trackers_blocked render "trackers" as トラッカー; 追跡 means "tracking" (the act), not the trackers themselves.
- `webcompat_reporter_reason_site_is_deceptive` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Dropdown option is rendered as a full sentence with polite copula, inconsistent with the other reason options which are all plain-form noun/verb phrases.
    - Current: `これは詐欺サイトです`
    - Source: `This site is deceptive`
    - Suggest: `サイトが詐欺的である`
    - All sibling reason strings (サイトが読み込まれない, サイトの動作が遅い, etc.) use plain form; this one uses です polite form, breaking register consistency within the same dropdown.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — Missing sentence-final period after 再度試してください in the first paragraph.
    - Current: `ネットワーク接続の確立中にリンクが切れました。再度試してください{ </p> }`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `ネットワーク接続の確立中にリンクが切れました。再度試してください。{ </p> }`
    - The source sentence "Please try again." ends with a period; the ja text omits the fullwidth 。 used elsewhere in the same string set.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Closing curly quotes are wrong: opening quote used as closing quote in both quoted URLs.
    - Current: `“https://“ または “http://“`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” または “http://”`
    - The source uses “https://” and “http://” with proper closing right double quotation marks; the target repeats the left quote as the closing mark.
- `ip_protection_menu_limit_reached` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Missing space between the GB unit and the following Japanese text, inconsistent with other VPN strings.
    - Current: `%1$d GBの上限に達しました`
    - Source: `%1$d GB limit reached`
    - Suggest: `%1$d GB の上限に達しました`
    - Other strings in the same feature (e.g. ip_protection_data_limit_reached_description) use a space after "GB" before Japanese text.
- `setup_checklist_subtitle_3_steps_first_step` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Stray space before the fullwidth comma in "3 ステップ中 、1 ステップ".
    - Current: `3 ステップ中 、1 ステップを完了しました。`
    - Source: `Great start! You’ve completed 1 out of 3 steps.`
    - Suggest: `3 ステップ中、1 ステップを完了しました。`
    - A space is inserted between 中 and the fullwidth comma, unlike the parallel strings (e.g. setup_checklist_subtitle_5_steps_second_step) which write "5 ステップ中、2 ステップ".
- `setup_checklist_subtitle_5_steps_first_step` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Stray space before the fullwidth comma in "5 ステップ中 、1 ステップ".
    - Current: `5 ステップ中 、1 ステップを完了しました。`
    - Source: `Great start! You’ve completed 1 out of 5 steps.`
    - Suggest: `5 ステップ中、1 ステップを完了しました。`
    - A space precedes the fullwidth comma, inconsistent with the sibling strings that use "5 ステップ中、2 ステップ".
- `setup_checklist_subtitle_6_steps_first_step` — `mozilla-mobile/fenix/app/src/main/res/values-ja/strings.xml` — Stray space before the fullwidth comma in "6 ステップ中 、1 ステップ".
    - Current: `6 ステップ中 、1 ステップを完了しました。`
    - Source: `Great start! You’ve completed 1 out of 6 steps.`
    - Suggest: `6 ステップ中、1 ステップを完了しました。`
    - A space precedes the fullwidth comma, inconsistent with the sibling strings that use "6 ステップ中、2 ステップ".

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

### Fixed to date (1)

- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ja/strings.xml` — fixed 2026-09-01
