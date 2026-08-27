# Firefox l10n QA — ja

| | |
|---|---|
| **Generated** | 2026-08-27 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `caafd8e1597e` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 18,182 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ja: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 360 |
| Strings | 18,182 |
| Missing strings | 34 |
| Obsolete strings | 6 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 21 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**34 strings** are not translated yet, concentrated in:

- `toolkit/services/aboutSyncLog.ftl` — 26
- `browser/browser/newtab/newtab.ftl` — 6
- `toolkit/toolkit/pdfviewer/embedFallback.ftl` — 2

**Files absent from the locale:**

- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

**Files present but identical to en-US:**

- `security/manager/chrome/pipnss/nsserrors.properties`
- `toolkit/toolkit/about/aboutMozilla.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 491, `curly-single` 193, `straight-double` 122, `corner` 7 | _mixed_ |
| apostrophe | `typographic` 270, `straight` 12 | **typographic** |
| ellipsis | `ascii` 460 | **ascii** |
| dash | `em` 81, `en` 1 | **em** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 11 | _mixed_ |
| fullwidth | `punctuation` 5736 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (100)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 8 |
| 2 | Wrong content (says something other than the English) | 30 |
| 3 | Degraded language (grammar, spelling, terminology) | 29 |
| 4 | Cosmetic (typography, spacing) | 33 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-dialog-title` — `browser/browser/aboutLogins.ftl` — `about-logins-confirm-remove-all-dialog-title` has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] { $count } 件のログイン情報を消去しますか？ [other] { $count } 件のすべてのログイン情報を消去しますか？`
    - Source: `{$count ->} [one] Remove { $count } login? [other] Remove all { $count } logins?`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-logins-confirm-remove-all-dialog-title2` — `browser/browser/aboutLogins.ftl` — `about-logins-confirm-remove-all-dialog-title2` has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] { $count } 件のパスワードを消去しますか？ [other] { $count } 件のすべてのパスワードを消去しますか？`
    - Source: `{$count ->} [one] Remove { $count } password? [other] Remove all { $count } passwords?`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — `about-logins-confirm-remove-all-sync-dialog-title` has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] すべての端末から { $count } 件のログイン情報を消去しますか？ [other] すべての端末から { $count } 件のすべてのログイン情報を消去しますか？`
    - Source: `{$count ->} [one] Remove { $count } login from all devices? [other] Remove all { $count } logins from all devices?`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-logins-confirm-remove-all-sync-dialog-title2` — `browser/browser/aboutLogins.ftl` — `about-logins-confirm-remove-all-sync-dialog-title2` has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] { $count } 件のパスワードを全端末から消去しますか？ [other] { $count } 件のすべてのパスワードを全端末から消去しますか？`
    - Source: `{$count ->} [one] Remove { $count } password from all devices? [other] Remove all { $count } passwords from all devices?`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `fxa-menu-device-view-all-synced-tabs` — `browser/browser/appmenu.ftl` — `fxa-menu-device-view-all-synced-tabs` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] { $tabCount } 個の同期したタブを表示 [other] 全 { $tabCount } 個の同期したタブを表示`
    - Source: `label: {$tabCount ->} [one] View { $tabCount } Synced Tab [other] View All { $tabCount } Synced Tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `menu-share-copy-links` — `browser/browser/browser.ftl` — `menu-share-copy-links` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] リンクをコピー [other] { $count } 個のリンクをコピー`
    - Source: `accesskey: L label: {$count ->} [one] Copy Link [other] Copy { $count } Links`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `content-sharing-tabs-title` — `browser/browser/contentSharing.ftl` — `content-sharing-tabs-title` has plural variant ['one'], which ja does not have
    - Current: `{$count ->} [one] { $count } 個のタブ [other] { $count } 個のタブ`
    - Source: `{$count ->} [one] { $count } tab [other] { $count } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — `downloads-files-not-downloaded` has plural variant ['one'], which ja does not have
    - Current: `{$num ->} [one] ファイルのダウンロードを中止しました。 [other] { $num } 個のファイルのダウンロードを中止しました。`
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-new-passwords` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-new-passwords` has plural variant ['one'], which ja does not have
    - Current: `{$newEntries ->} [one] { $newEntries } 件追加しました [other] { $newEntries } 件追加しました`
    - Source: `{$newEntries ->} [one] { $newEntries } added [other] { $newEntries } added`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-updated-passwords` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-updated-passwords` has plural variant ['one'], which ja does not have
    - Current: `{$updatedEntries ->} [one] { $updatedEntries } 件更新しました [other] { $updatedEntries } 件更新しました`
    - Source: `{$updatedEntries ->} [one] { $updatedEntries } updated [other] { $updatedEntries } updated`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — comment states this is the standalone label under the big number; ja is a fragment ending in 、 that depends on the separate newtab-privacy-across-sites. → a self-contained label, e.g. 今日ブロックしたトラッカー
    - Source: `{$count ->} [one] Tracker blocked today [other] Trackers blocked today`
    - Suggest: `今日ブロックしたトラッカー`
- `info-exposed-passwords-found` — `browser/browser/protections.ftl` — { $count } 件のパスワードが全漏洩データから見つかりました — 件のパスワードが全漏洩データから見つかりました
    - Current: `{ $count } 件のパスワードが全漏洩データから見つかりました`
    - Source: `{$count ->} [one] Password exposed across all breaches [other] Passwords exposed across all breaches`
    - Suggest: `件のパスワードが全漏洩データから見つかりました`
- `info-known-breaches-found` — `browser/browser/protections.ftl` — { $count } 件の既知の漏洩データが見つかりました — 件の既知の漏洩データが見つかりました
    - Current: `{ $count } 件の既知の漏洩データが見つかりました`
    - Source: `{$count ->} [one] Known data breach has exposed your information [other] Known data breaches have exposed your information`
    - Suggest: `件の既知の漏洩データが見つかりました`
- `info-monitored-emails` — `browser/browser/protections.ftl` — { $count } 個のメールアドレスを監視しています — 個のメールアドレスを監視しています
    - Current: `{ $count } 個のメールアドレスを監視しています`
    - Source: `{$count ->} [one] Email address being monitored [other] Email addresses being monitored`
    - Suggest: `個のメールアドレスを監視しています`
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — `recently-closed-window-panel-tooltip` has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } ({ $tabCount } 個のタブ、{ $closedAt } に閉じた) [other] { $winTitle } ({ $tabCount } 個のタブ、{ $closedAt } に閉じた)`
    - Source: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } ({ $tabCount } tab, closed at { $closedAt }) [other] { $winTitle } ({ $tabCount } tabs, closed at { $closedAt })`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `protections-milestone` — `browser/browser/siteProtections.ftl` — `protections-milestone` has plural variant ['one'], which ja does not have
    - Current: `{$trackerCount ->} [one] { $date } 以降、{ -brand-short-name } は { $trackerCount } 個のトラッカーをブロックしました [other] { $date } 以降、{ -brand-short-name } は { $trackerCount } 個以上のトラッカーをブロックしました`
    - Source: `{$trackerCount ->} [one] { -brand-short-name } blocked { $trackerCount } tracker since { $date } [other] { -brand-short-name } blocked over { $trackerCount } trackers since { $date }`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `synced-tabs-context-open-in-window` — `browser/browser/syncedTabs.ftl` — group comment requires these to match places.ftl; en-US is "Open in New Window" with no "link". Current リンクを新しいウィンドウで開く → 新しいウィンドウで開く.
    - Current: `リンクを新しいウィンドウで開く`
    - Source: `accesskey: N label: Open in New Window`
    - Suggest: `新しいウィンドウで開く`
- `tabbrowser-close-tabs-button` — `browser/browser/tabbrowser.ftl` — `tabbrowser-close-tabs-button` (`.tooltiptext`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブを閉じます [other] { $tabCount } 個のタブを閉じます`
    - Source: `tooltiptext: {$tabCount ->} [one] Close tab [other] Close { $tabCount } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-close-tabs-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-close-tabs-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブを閉じます [other] { $tabCount } 個のタブを閉じます`
    - Source: `label: {$tabCount ->} [one] Close tab [other] Close { $tabCount } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-mute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-mute-tab-audio-background-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブをミュートにします [other] { $tabCount } 個のタブをミュートにします`
    - Source: `label: {$tabCount ->} [one] Mute tab [other] Mute { $tabCount } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-mute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-mute-tab-audio-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブをミュートにします ({ $shortcut }) [other] { $tabCount } 個のタブをミュートにします ({ $shortcut })`
    - Source: `label: {$tabCount ->} [one] Mute tab ({ $shortcut }) [other] Mute { $tabCount } tabs ({ $shortcut })`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-unblock-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unblock-tab-audio-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブの音声を再生します [other] { $tabCount } 個のタブの音声を再生します`
    - Source: `label: {$tabCount ->} [one] Play tab [other] Play { $tabCount } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unmute-tab-audio-background-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブのミュートを解除します [other] { $tabCount } 個のタブのミュートを解除します`
    - Source: `label: {$tabCount ->} [one] Unmute tab [other] Unmute { $tabCount } tabs`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unmute-tab-audio-tooltip` (`.label`) has plural variant ['one'], which ja does not have
    - Current: `{$tabCount ->} [one] タブのミュートを解除します ({ $shortcut }) [other] { $tabCount } 個のタブのミュートを解除します ({ $shortcut })`
    - Source: `label: {$tabCount ->} [one] Unmute tab ({ $shortcut }) [other] Unmute { $tabCount } tabs ({ $shortcut })`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `xpath-binary-expected` — `dom/dom/xslt.ftl` — A6 — Fluent value-concatenation format broken (dom/dom/xslt.ftl). These strings are concatenated at runtime with the offending URL / character / expression, so en-US ends each with :. ja replaced the colon with 。, orphaning the appended detail. Affects xslt-load-recursion, xpath-illegal-char, xpath-binary-expected. Sibling xpath- strings in the same file correctly keep the colon, confirming these…
    - Source: `XPath parse failure: binary operator expected:`
    - Suggest: `:`
- `xpath-illegal-char` — `dom/dom/xslt.ftl` — A6 — Fluent value-concatenation format broken (dom/dom/xslt.ftl). These strings are concatenated at runtime with the offending URL / character / expression, so en-US ends each with :. ja replaced the colon with 。, orphaning the appended detail. Affects xslt-load-recursion, xpath-illegal-char, xpath-binary-expected. Sibling xpath- strings in the same file correctly keep the colon, confirming these…
    - Source: `XPath parse failure: illegal character found:`
    - Suggest: `:`
- `xslt-load-recursion` — `dom/dom/xslt.ftl` — A6 — Fluent value-concatenation format broken (dom/dom/xslt.ftl). These strings are concatenated at runtime with the offending URL / character / expression, so en-US ends each with :. ja replaced the colon with 。, orphaning the appended detail. Affects xslt-load-recursion, xpath-illegal-char, xpath-binary-expected. Sibling xpath- strings in the same file correctly keep the colon, confirming these…
    - Source: `An XSLT stylesheet directly or indirectly imports or includes itself:`
    - Suggest: `:`
- `about-webauthn-results-pin-invalid-error` — `toolkit/toolkit/about/aboutWebauthn.ftl` — `about-webauthn-results-pin-invalid-error` has plural variant ['one'], which ja does not have
    - Current: `{$retriesLeft ->} [0] エラー: PIN が正しくありません。もう一度試してください。 [one] エラー: PIN が正しくありません。もう一度試してください。試行回数は残り 1 回です。 [other] エラー: PIN が正しくありません。もう一度試してください。試行回数は残り { $retriesLeft } 回です。`
    - Source: `{$retriesLeft ->} [0] Error: Incorrect PIN. Try again. [one] Error: Incorrect PIN. Try again. You have one attempt left. [other] Error: Incorrect PIN. Try again. You have { $retriesLeft } attempts left.`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-webauthn-samples-still-needed` — `toolkit/toolkit/about/aboutWebauthn.ftl` — `about-webauthn-samples-still-needed` has plural variant ['one'], which ja does not have
    - Current: `{$repeatCount ->} [one] あと { $repeatCount } 個のサンプルが必要です。 [other] あと { $repeatCount } 個のサンプルが必要です。`
    - Source: `{$repeatCount ->} [one] { $repeatCount } sample still needed. [other] { $repeatCount } samples still needed.`
    - ja has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-private-browsing-felt-privacy-v1-info-header` — `browser/browser/aboutPrivateBrowsing.ftl` — about-private-browsing-felt-privacy-v1-info-header (aboutPrivateBrowsing.ftl) — "Leave no traces on this device" → この端末を追跡させません. → この端末に痕跡を残しません Verified.
    - Source: `Leave no traces on this device`
    - Suggest: `この端末を追跡させません`
- `trustpanel-blocker-description` — `browser/browser/browser.ftl` — trustpanel-blocker-description (browser.ftl) — text copied from trustpanel-etp-description-disabled, adding a condition absent from en-US. → …そのため、できるだけ多くのトラッカーをブロックします。
    - Source: `{ -brand-product-name } thinks companies should follow you less. So we block as many as we can.`
    - Suggest: `…そのため、できるだけ多くのトラッカーをブロックします。`
- `ipprotection-bandwidth-upgrade-title` — `browser/browser/ipProtection.ftl` — ipprotection-bandwidth-upgrade-title (ipProtection.ftl) — "Like built-in VPN?" is a question, read as "similar to". → 組み込み VPN が気に入りましたか？ …
    - Source: `Like built-in VPN? Get even more protection outside { -brand-product-name } with { -mozilla-vpn-brand-name }.`
    - Suggest: `組み込み VPN が気に入りましたか？ …`
- `containers-sites-card-header` — `browser/browser/preferences/preferences.ftl` — The description translates "a site"/"the site" as "このサイト" (this site), implying a specific site rather than any site in general.
    - Current: `専用コンテナーを選ぶと、{ -brand-short-name } でこのサイトを開く時に毎回このコンテナーが使用されます。`
    - Source: `description: Choose a container for a site and { -brand-short-name } will use it every time the site opens. label: Site-specific containers`
    - Suggest: `サイトごとにコンテナーを選ぶと、{ -brand-short-name } はそのサイトを開くたびに毎回そのコンテナーを使用します。`
    - en-US says "Choose a container for a site and { -brand-short-name } will use it every time the site opens" — generic; the Japanese uses deictic 「この」 referring to a particular site, changing the meaning of this settings card header description.
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — "dangerous and deceptive content" is two categories; ja merges them into one modifier, unlike security-browsing-protection.
    - Source: `description: Your exposure to scams and malware from websites is increased. label: Dangerous and deceptive content is not blocked`
- `tabs-group-header2` — `browser/browser/preferences/preferences.ftl` — en-US is the section header "Tabs" ("group" in the ID refers to the preferences groupbox); タブグループ now also collides with the real Tab Groups feature. → タブ Verified.
    - Current: `タブグループ`
    - Source: `label: Tabs`
    - Suggest: `タブ`
- `monitor-breaches-unresolved-description` — `browser/browser/protections.ftl` — monitor-breaches-unresolved-description (protections.ftl) — "taking steps to protect your info" → 段階に進めます ("advance to a stage").
    - Source: `After reviewing breach details and taking steps to protect your info, you can mark breaches as resolved.`
    - Suggest: `段階に進めます`
- `protection-report-page-summary` — `browser/browser/protections.ftl` — dev comment says this variant shows when all protections are off, "which is why we use the word 'can'". ja is byte-identical to protection-report-page-summary-default and asserts active protection. → …プライバシーを保護できます。 Verified.
    - Source: `{ -brand-short-name } can protect your privacy behind the scenes while you browse. This is a personalized summary of those protections, including tools to take control of your online security.`
    - Suggest: `…プライバシーを保護できます。`
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — see G and H.
    - Source: `{ -brand-short-name } blocked this page because it might attempt to install malicious software that may steal or delete personal information on your computer.`
- `inactive-css-no-principal-box` — `devtools/client/tooltips.ftl` — the topic { $property } is attached to the subordinate clause, so it says the property does not create a principal box rather than the element.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it does not create a principal box.`
- `inactive-css-no-size-containment` — `devtools/client/tooltips.ftl` — the topic { $property } is attached to the subordinate clause, so it says the property does not create a principal box rather than the element.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it has no size containment.`
- `treetable` — `dom/chrome/accessibility/AccessFu.properties` — "tree table" is rendered as 「折りたたみリスト」 (collapsible list), which names a different accessibility role.
    - Current: `折りたたみリスト`
    - Source: `tree table`
    - Suggest: `ツリーテーブル`
    - The source is the accessibility role name "tree table"; "折りたたみリスト" (collapsible list) does not denote a table role and mis-announces the element to screen reader users.
- `about-logging-title` — `toolkit/toolkit/about/aboutLogging.ftl` — about-logging-title (aboutLogging.ftl) — "About Logging" → HTTP ログについて; the page now covers media, gfx, WebRTC and WebGPU presets. → ログについて Verified.
    - Source: `About Logging`
    - Suggest: `HTTP ログについて`
- `about-networking-logging` — `toolkit/toolkit/about/aboutNetworking.ftl` — about-networking-logging (aboutNetworking.ftl) — same over-specification; the row links to the general about:logging page. → ログ記録
    - Source: `Logging`
    - Suggest: `ログ記録`
- `profiles-launch-profile` — `toolkit/toolkit/about/aboutProfiles.ftl` — profiles-launch-profile (aboutProfiles.ftl) — "Launch profile in new browser" → 別のプロセスで ("in another process"). → 新しいブラウザーで起動
    - Source: `Launch profile in new browser`
    - Suggest: `別のプロセスで`
- `effective-content-sandbox-level` — `toolkit/toolkit/about/aboutSupport.ftl` — effective-content-sandbox-level (aboutSupport.ftl) — "Effective" (value in force) → 効果的な ("efficacious"). → 実効の Verified.
    - Source: `Effective Content Process Sandbox Level`
    - Suggest: `効果的な`
- `virtual-monitor-disp` — `toolkit/toolkit/about/aboutSupport.ftl` — virtual-monitor-disp (aboutSupport.ftl) — "Virtual Monitor Display" → 仮想デスクトップ, an unrelated OS feature. → 仮想モニターの表示 Verified.
    - Source: `Virtual Monitor Display`
    - Suggest: `仮想デスクトップ`
- `about-telemetry-keyed-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "Keyed" read as "key/principal" (主要な). Keyed scalars are indexed by string keys. → キー付きスカラー / キー付きヒストグラム Verified.
    - Current: `主要な`
    - Source: `Keyed Scalars`
    - Suggest: `キー付きスカラー`
- `about-telemetry-show-subsession-data` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "subsession" rendered as "submitted" (送信データ). → サブセッションデータを表示 Verified.
    - Current: `送信データ`
    - Source: `Show subsession data`
    - Suggest: `サブセッションデータを表示`
- `about-webauthn-auth-info-uv-modality` — `toolkit/toolkit/about/aboutWebauthn.ftl` — about-webauthn-auth-option-uv (+ -alwaysuv, -makecreduvnotrqd, about-webauthn-auth-info-uv-modality) — CTAP2 "user verification" (PIN or biometrics) → 生体認証 (biometrics only). → ユーザー検証 (UV) Verified.
    - Source: `User verification modality`
    - Suggest: `生体認証`
- `about-webauthn-auth-option-uv` — `toolkit/toolkit/about/aboutWebauthn.ftl` — about-webauthn-auth-option-uv (+ -alwaysuv, -makecreduvnotrqd, about-webauthn-auth-info-uv-modality) — CTAP2 "user verification" (PIN or biometrics) → 生体認証 (biometrics only). → ユーザー検証 (UV) Verified.
    - Source: `User verification`
    - Suggest: `生体認証`
- `about-webrtc-local-candidate` — `toolkit/toolkit/about/aboutWebrtc.ftl` — about-webrtc-local-candidate (+ -remote-candidate, -raw-candidates-heading, -raw-local-candidate, -raw-remote-candidate, -raw-cand-, -trickle-caption-msg) — ICE "candidate" rendered 通信情報 ("communication info") throughout, losing the spec term and making the ICE tables unreadable against the standard. → 候補 / ICE 候補
    - Current: `通信情報`
    - Source: `Local Candidate`
    - Suggest: `候補`
- `webext-perms-header-data-collection-is-none` — `toolkit/toolkit/global/extensions.ftl` — adds a qualifier not in the source and contradicts the neighbouring 必要なデータ収集. Current 任意のデータ収集: → データ収集:
    - Current: `任意のデータ収集:`
    - Source: `Data collection:`
    - Suggest: `データ収集:`
- `webext-perms-host-description-all-urls` — `toolkit/toolkit/global/extensions.ftl` — modifier scope: 保存された attaches to ウェブサイト, giving "all saved websites". → すべてのウェブサイトのユーザーデータへのアクセス
    - Current: `保存された`
    - Source: `Access your data for all websites`
    - Suggest: `すべてのウェブサイトのユーザーデータへのアクセス`
- `language-name-ie` — `toolkit/toolkit/intl/languageNames.ftl` — Interlingue — インターリング — インターリングエ — truncated; ia = インターリングア is a different language
    - Current: `インターリング`
    - Source: `Interlingue`
    - Suggest: `インターリングエ`
- `pdfjs-editor-alt-text-add-description-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "setting" (scene/surroundings) taken as "settings/configuration". → 被写体や場面、動作
    - Source: `Aim for 1-2 sentences that describe the subject, setting, or actions.`
    - Suggest: `被写体や場面、動作`
- `remove-primary-password-warning1` — `toolkit/toolkit/preferences/preferences.ftl` — see S2 for the term; no other defect.
    - Source: `Your Primary Password is used to protect sensitive information like logins and passwords.`
- `print-progress` — `toolkit/toolkit/printing/printDialogs.ftl` — "Progress:" is a noun label before a percentage; ja 進行中: = "in progress:". → 進行状況:
    - Current: `進行中:`
    - Source: `value: Progress:`
    - Suggest: `進行状況:`
- `webauthn-register-direct-prompt` — `toolkit/toolkit/webauthnDialog.ftl` — webauthn-register-direct-prompt (webauthnDialog.ftl) — modifier scope: reads as "information about additional security keys" rather than "additional information about the security key". → split the privacy clause into its own sentence.
    - Source: `{ $hostname } is requesting extended information about your security key, which may affect your privacy.`
    - Suggest: `split the privacy clause into its own sentence.`

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-dialog-message` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-dialog-message, -all-sync-dialog-message, -all-dialog-message2, -all-sync-dialog-message3 — browser/browser/aboutLogins.ftl — ここ表示される → ここに表示される (all four). Verified.
    - Current: `ここ表示される`
    - Source: `{$count ->} [1] This will remove the login you’ve saved to { -brand-short-name } and any breach alerts that appear here. You won’t be able to undo this action. [other] This will remove the logins you’ve saved to { -bran…`
    - Suggest: `ここに表示される`
- `addon-local-install-error-file-access` — `browser/browser/addonNotifications.ftl` — double が: 必要なファイルが変更できなかった → 必要なファイルを変更できなかった (cf. addon-install-error-file-access).
    - Current: `必要なファイルが変更できなかった`
    - Source: `{ $addonName } could not be installed because { -brand-short-name } cannot modify the needed file.`
    - Suggest: `必要なファイルを変更できなかった`
- `backup-service-error-recovery-failed` — `browser/browser/backupSettings.ftl` — { -brand-short-name } に復元できませんでした → は復元できませんでした.
    - Current: `{ -brand-short-name } に復元できませんでした`
    - Source: `heading: { -brand-short-name } couldn’t restore message: Restart { -brand-short-name } and try restoring your backup again.`
    - Suggest: `は復元できませんでした`
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — active subject 私たち with passive 通知されます → 通知します.
    - Current: `通知されます`
    - Source: `All passwords are encrypted and we’ll watch out for breaches and alerts if you’re affected.`
    - Suggest: `通知します`
- `ip-protection-bandwidth-left-gb` — `browser/browser/ipProtection.ftl` — browser/browser/ipProtection.ftl — 残り attaches to $maxUsage, giving "of the remaining {max} GB, {left} GB". → { $maxUsage } GB 中、残り { $usageLeft } GB (the pattern already used correctly in ipprotection-message-bandwidth-warning.message).
    - Current: `$maxUsage`
    - Source: `{ $usageLeft } GB of { $maxUsage } GB left`
    - Suggest: `{ $maxUsage } GB 中、残り { $usageLeft } GB`
- `newtab-pocket-cta-text` — `browser/browser/newtab/newtab.ftl` — お気に入りに記事 → お気に入りの記事.
    - Current: `お気に入りに記事`
    - Source: `Save the stories you love in { -pocket-brand-name }, and fuel your mind with fascinating reads.`
    - Suggest: `お気に入りの記事`
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — two を: リスクフリーの環境を試してください → 環境で試してください.
    - Current: `リスクフリーの環境を試してください`
    - Source: `Try { -mozilla-vpn-brand-name } risk-free and see why TechRadar says, “its speed, simplicity and low monthly price make it worth a look.”`
    - Suggest: `環境で試してください`
- `report-broken-site-panel-reason-deceptive-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — predicate-less noun (サイトが詐欺) where all siblings are full predicates. → サイトが詐欺的である
    - Current: `サイトが詐欺`
    - Source: `label: Site is deceptive`
    - Suggest: `サイトが詐欺的である`
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — あなた個人情報 → あなたの個人情報.
    - Current: `あなた個人情報`
    - Source: `{ -brand-short-name } blocked this page because it might attempt to install malicious software that may steal or delete personal information on your computer.`
    - Suggest: `あなたの個人情報`
- `tab-group-editor-action-ungroup` — `browser/browser/tabbrowser.ftl` — グループを解放 ("liberate/free"); 解放 is already used for tab unloading in tab-context-unload-n-tabs. → グループを解除 Verified.
    - Source: `label: Ungroup tabs`
    - Suggest: `グループを解除`
- `toolbar-context-menu-reopen-closed-tabs` — `browser/browser/toolbarContextMenu.ftl` — 開きなおす → 開き直す (the form used in tabContextMenu.ftl and recentlyClosed.ftl).
    - Current: `開きなおす`
    - Source: `accesskey: o label: {$tabCount ->} [1] Reopen Closed Tab [other] Reopen Closed Tabs`
    - Suggest: `開き直す`

### D. Terminology, register & consistency

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — (not imported) left in English while every sibling uses (インポートされませんでした).
    - Current: `(not imported)`
    - Source: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Suggest: `(インポートされませんでした)`
- `aiwindow-firstrun-model-personal-label` — `browser/browser/aiWindow.ftl` — aiwindow-firstrun-model-personal-label, aiwindow-input-model-select-button-label-personal — browser/browser/aiWindow.ftl — the "Personal" model is パーソナル in aiFeatures.ftl but 私的 here.
    - Source: `Personal`
- `aiwindow-input-model-select-button-label-personal` — `browser/browser/aiWindow.ftl` — aiwindow-firstrun-model-personal-label, aiwindow-input-model-select-button-label-personal — browser/browser/aiWindow.ftl — the "Personal" model is パーソナル in aiFeatures.ftl but 私的 here.
    - Source: `Personal`
- `settings-data-toggle-encryption-label2` — `browser/browser/backupSettings.ftl` — same en-US sentence as settings-sensitive-data-encryption-description, but "Back up" → 保護. → バックアップし
    - Source: `description: Back up your passwords and payment methods, plus keep all your data safe with encryption. label: Back up your sensitive data`
    - Suggest: `保護`
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “Web ブラウザー” but the string it names, `desktop-entry-generic-name`, reads “ウェブブラウザー”
    - Current: `ステップ 1: Windows の [設定] > [アプリ] > [既定のアプリ] を開きます ステップ 2: “Web ブラウザー” まで下へスクロールします ステップ 3: アイコンをクリックし、{ -brand-short-name } を選んでください`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `ウェブブラウザー`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body vs spotlight-peace-mind-body — browser/browser/newtab/asrouter.ftl — same figure formatted 3000 件以上 and 3,000 以上 in one file.
    - Source: `Every month, { -brand-short-name } blocks an average of 3,000+ trackers per user, giving you safe, speedy access to the good internet.`
- `newtab-picture-image-alt` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — 今日の写真 vs 今日の一枚 in four other strings for the same object.
    - Source: `Wikimedia Commons picture of the day`
    - Suggest: `今日の写真`
- `newtab-picture-show-button` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — 今日の写真 vs 今日の一枚 in four other strings for the same object.
    - Source: `aria-label: Show today’s picture title: Show today’s picture`
    - Suggest: `今日の写真`
- `newtab-stocks-search-input` — `browser/browser/newtab/newtab.ftl` — The placeholder for the search input is rendered as a verb phrase "〜します" instead of a noun/placeholder form.
    - Current: `placeholder: 企業名または銘柄コードで検索します`
    - Source: `aria-label: Search by name or symbol placeholder: Search by name or symbol`
    - Suggest: `placeholder: 企業名または銘柄コードで検索`
    - The developer comment says this is a placeholder text in the input field; the locale convention reserves 〜します for .title tooltips, not placeholders, and the identical aria-label uses the noun form.
- `newtab-weather-menu-change-temperature-units-fahrenheit` — `browser/browser/newtab/newtab.ftl` — browser/browser/newtab/newtab.ftl — ファーレンハイト度 / セルシウス度 vs 華氏 / 摂氏 in the option labels of the same menu.
    - Source: `Switch to Fahrenheit`
    - Suggest: `ファーレンハイト度`
- `safeb-blocked-malware-page-learn-more-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — "Phishing and Malware Protection" rendered 偽装サイトとマルウェアからの防護機能, differing from its three sibling strings (フィッシング詐欺とマルウェアからの保護機能).
    - Current: `偽装サイトとマルウェアからの防護機能`
    - Source: `Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_support'>support.mozilla.org</a>.`
    - Suggest: `フィッシング詐欺とマルウェアからの保護機能`
- `item-site-prefs` — `browser/browser/sanitize.ftl` — browser/browser/sanitize.ftl — same en-US "Site settings" as サイト設定 and サイトの設定 in one file.
    - Source: `accesskey: i label: Site settings`
    - Suggest: `サイト設定`
- `item-site-settings` — `browser/browser/sanitize.ftl` — browser/browser/sanitize.ftl — same en-US "Site settings" as サイト設定 and サイトの設定 in one file.
    - Source: `accesskey: S label: Site settings`
    - Suggest: `サイト設定`
- `tab-context-reverse-split-view` — `browser/browser/tabbrowser.ftl` — same en-US "Reverse Tabs" is 左右のタブを入れ替える here and タブ順を反転 in split-view-menuitem-reverse-tabs.
    - Current: `左右のタブを入れ替える`
    - Source: `accesskey: r label: Reverse Tabs`
    - Suggest: `タブ順を反転`
- `toolbar-context-menu-bookmark-selected-tab` — `browser/browser/toolbarContextMenu.ftl` — browser/browser/toolbarContextMenu.ftl — ブックマーク... as a verb vs ブックマークに追加... in tabContextMenu.ftl for the same action.
    - Source: `accesskey: T label: Bookmark Selected Tab…`
    - Suggest: `ブックマーク...`
- `options-context-inspector` — `devtools/client/toolbox-options.ftl` — the Inspector panel name rendered with the verb for the Inspect action (調査); the same file's tooltips say インスペクター.
    - Current: `調査`
    - Source: `Inspector`
    - Suggest: `インスペクター`
- `toolbox-meatball-menu-splitconsole-label` — `devtools/client/toolbox.ftl` — devtools/client/toolbox.ftl — "Split Console" is 分割コンソール in toolbox-options.ftl. Current コンソールペインを表示/隠す.
    - Source: `Show Split Console`
    - Suggest: `分割コンソール`
- `webext-perms-header-optional-required-perms` — `toolkit/toolkit/global/extensions.ftl` — toolkit/toolkit/global/extensions.ftl — permissions are 権限 elsewhere in the file but 許可/許可設定 here.
    - Source: `New permissions:`
    - Suggest: `権限`
- `webext-perms-optional-perms-header` — `toolkit/toolkit/global/extensions.ftl` — toolkit/toolkit/global/extensions.ftl — permissions are 権限 elsewhere in the file but 許可/許可設定 here.
    - Source: `{ $extension } requests additional permissions.`
    - Suggest: `権限`

### E. Typography, punctuation & spacing

- `smartwindow-assistant-error-request-blocked-header` — `browser/browser/aiWindowContent.ftl` — { -smart-window-brand-name }がサーバーに → } がサーバーに. Verified.
    - Current: `{ -smart-window-brand-name }がサーバーに`
    - Source: `{ -smart-window-brand-name } couldn’t reach the server. Try a different network, or disable your VPN.`
    - Suggest: `} がサーバーに`
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — browser/browser/migrationWizard.ftl.
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — I10 — Duplicated text. spotlight-better-internet-body (browser/browser/newtab/asrouter.ftl) — すべての人にとって appears twice in one sentence (cf. mr2022-onboarding-gratitude-subtitle, correct).
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet more open, accessible, and better for everyone.`
- `autofill-card-search-term-credit-cards` — `browser/browser/preferences/formAutofill.ftl` — Not a defect: autofill-card-search-term-credit-cards (browser/browser/preferences/formAutofill.ftl) also uses ASCII commas, but its dev comment says it is a never-displayed comma-separated keyword list. Verified.
    - Source: `credit cards, credit, cards, debit cards, debit, wallet, checkout`
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — translate-attribution, extension-controlled-enable, settings-translations-subpage-never-translate-sites-description, sync-mobile-promo — browser/browser/preferences/preferences.ftl. Verified (translate-attribution).
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — translate-attribution, extension-controlled-enable, settings-translations-subpage-never-translate-sites-description, sync-mobile-promo — browser/browser/preferences/preferences.ftl. Verified (translate-attribution).
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
- `sync-mobile-promo` — `browser/browser/preferences/preferences.ftl` — translate-attribution, extension-controlled-enable, settings-translations-subpage-never-translate-sites-description, sync-mobile-promo — browser/browser/preferences/preferences.ftl. Verified (translate-attribution).
    - Source: `Download Firefox for <img data-l10n-name="android-icon"/> <a data-l10n-name="android-link">Android</a> or <img data-l10n-name="ios-icon"/> <a data-l10n-name="ios-link">iOS</a> to sync with your mobile device.`
- `xslt-aborted` — `dom/dom/xslt.ftl` — dom/dom/xslt.ftl.
    - Source: `XSLT transformation was terminated by <xsl:message>.`
- `console-stacktrace` — `mobile/android/mobile/android/geckoViewConsole.ftl` — two ASCII commas between Japanese-labelled fields. Verified.
    - Source: `Stack trace from { $filename }, function { $functionName }, line { $lineNumber }.`
- `set-password-reenter` — `toolkit/toolkit/preferences/preferences.ftl` — set-password-reenter.label, set-password-reenter-password — toolkit/toolkit/preferences/preferences.ftl — same.
    - Source: `label: Re-enter password:`
- `set-password-reenter-password` — `toolkit/toolkit/preferences/preferences.ftl` — set-password-reenter.label, set-password-reenter-password — toolkit/toolkit/preferences/preferences.ftl — same.
    - Source: `Re-enter password:`
- `printui-paper-letter` — `toolkit/toolkit/printing/printUI.ftl` — Not defects — leave as-is: printui-paper-letter / -legal / -tabloid (toolkit/toolkit/printing/printUI.ftl) use " as an inch mark (8.5"x11").
    - Source: `US Letter`
    - Suggest: `-legal`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ja/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `autofill-address-family-name` — `browser/browser/preferences/formAutofill.ftl` — raised by `legacy`, withdrawn 2026-08-21

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (270)

- `abuse-report-policy-reason-v2` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-08-25
- `about-logins-import-dialog-error-unable-to-read-description` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `webext-imported-addons` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-24
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — fixed 2026-08-24
- `aiwindow-firstrun-memories-title` — `browser/browser/aiWindow.ftl` — fixed 2026-08-24
- `smart-window-confirm-close-tabs` — `browser/browser/aiWindow.ftl` — fixed 2026-08-24
- `aiwindow-memories-callout-description` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-24
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-24
- `sharing-warning-disable-for-session` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `contextual-manager-passwords-vulnerable-password-heading-and-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-24
- `customkeys-conflict-confirm` — `browser/browser/customkeys.ftl` — fixed 2026-08-24
- `default-browser-guidance-notification-v2-body` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-08-24
- `perplexity-callout-theme-1-subtitle-2` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `windows-10-eos-sync-new-device-title-2` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `firefoxview-dont-remember-history-empty-header-2` — `browser/browser/firefoxView.ftl` — fixed 2026-08-24
- `firefoxview-recentlyclosed-empty-header` — `browser/browser/firefoxView.ftl` — fixed 2026-08-24
- `ip-protection-vpn-upgrade-link` — `browser/browser/ipProtection.ftl` — fixed 2026-08-24
- `menu-history-clear-recent-history` — `browser/browser/menubar.ftl` — fixed 2026-08-24
- `menu-history-synced-tabs` — `browser/browser/menubar.ftl` — fixed 2026-08-24
- `spotlight-better-internet-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-24
- `mr2022-onboarding-get-started-primary-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `onboarding-refresh-pin-set-default-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `policy-DisableAppUpdate` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-24
- `fonts-langgroup-georgian` — `browser/browser/preferences/fonts.ftl` — fixed 2026-08-24
- `fonts-langgroup-trad-chinese-hk` — `browser/browser/preferences/fonts.ftl` — fixed 2026-08-24
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `home-section` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-ai-controls-block-ai-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-ai-controls-blocked-message` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-web-appearance-footer` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-web-appearance-link` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `search-keyword-warning-engine` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `security-enable-safe-browsing` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `sync-currently-syncing-addresses` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `sync-engine-addresses` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `translate-attribution` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `restored-profile-page-header-description` — `browser/browser/profiles.ftl` — fixed 2026-08-24
- `info-exposed-passwords-resolved` — `browser/browser/protections.ftl` — fixed 2026-08-24
