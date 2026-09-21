# Firefox iOS l10n QA — ja

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ja: [android](android.md) · [firefox](firefox.md)

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
| Files | 97 |
| Strings | 1,927 |
| Missing strings | 23 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**23 strings** are not translated yet, concentrated in:

- `ja/firefox-ios.xliff` — 17
- `ja/firefox-ios.xliff` — 6

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 11, `curly-double` 3 | **corner** |
| ellipsis | `char` 11, `ascii` 11 | _mixed_ |
| fullwidth | `punctuation` 396 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (110)

> **Reads as a deliberate edit (7).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `NSFaceIDUsageDescription` — `ja/firefox-ios.xliff` — "payment methods" is rendered as 「暗号化されたカード情報」 (encrypted card information), adding a claim not in the source.
    - Current: `保存されたログイン情報と暗号化されたカード情報にアクセスするには Face ID が必要です。`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `保存されたパスワードと支払い方法にアクセスするには Firefox は Face ID を必要とします。`
    - The en-US says "your saved passwords and payment methods"; the Japanese asserts the card data is encrypted, which the source never states, and drops the Firefox subject.
- `NSLocationWhenInUseUsageDescription` — `ja/firefox-ios.xliff` — "may request your location" is rendered as a present-tense assertion that visited sites are requesting your location.
    - Current: `訪れたウェブサイトがあなたの位置情報を要求しています。`
    - Source: `Websites you visit may request your location.`
    - Suggest: `訪れたウェブサイトがあなたの位置情報を要求することがあります。`
    - The en-US source states a possibility ("may request"), while the Japanese asserts that sites are currently requesting the location.
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `ja/firefox-ios.xliff` — "Leave no traces on this device" is rendered as "We won't let this device be tracked", which asserts something different from the source.
    - Current: `この端末を追跡させません`
    - Source: `Leave no traces on this device`
    - Suggest: `この端末に痕跡を残しません`
    - The en-US says no traces (cookies, history, site data) are left on the device; the Japanese claims the device will not be tracked, a different privacy claim the source never makes.
- `Onboarding.Customization.Intro.Title.v123` — `ja/firefox-ios.xliff` — Title translated as "privacy protection" instead of "puts you in control".
    - Current: `%@ でプライバシー保護`
    - Source: `%@ puts you in control`
    - Suggest: `%@ なら思いのまま`
    - The en-US says "%@ puts you in control" (about customization control), not about privacy protection; the Japanese asserts a different product claim.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `ja/firefox-ios.xliff` — "interaction data" rendered as 「対話データ」 (dialogue/conversation data) instead of 利用状況データ/インタラクションデータ.
    - Current: `診断情報と対話データ`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `診断データとインタラクションデータ`
    - en-US "diagnostic and interaction data" refers to usage/interaction telemetry; 「対話データ」 implies conversation data, asserting the product collects something different from what the source says.
- `WebCompatReporter.Preview.Data.PageLanguages.v155` — `ja/firefox-ios.xliff` — A bullet-point noun phrase is rendered as a past-tense sentence, changing the meaning.
    - Current: `言語設定がこのページに送信されました`
    - Source: `Language preferences sent to this page`
    - Suggest: `このページに送信された言語設定`
    - The source "Language preferences sent to this page" is a noun phrase listing data included in the report; the Japanese states as a completed fact that language preferences were sent to the page.
- `Settings.TrackingProtection.ProtectionCellFooter` — `ja/firefox-ios.xliff` — "helps stop advertisers from tracking your browsing" is rendered as an absolute claim of blocking tracking ads.
    - Current: `ユーザーの行動を追跡する広告を阻止します`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `広告会社によるユーザーの閲覧の追跡を防ぐのに役立ちます`
    - The source says it "helps stop" advertisers from tracking browsing; the Japanese asserts that it blocks tracking ads outright, overstating what the product does.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 60 |
| 3 | Degraded language (grammar, spelling, terminology) | 44 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

- `WorldCup.HomepageWidget.CountDown.HourLabel.v151` — `ja/firefox-ios.xliff` — Two-character translation 「時間」 will be truncated to a misleading label; a single character is required.
    - Current: `時間`
    - Source: `H`
    - Suggest: `時`
    - The developer comment says the layout allows 1–2 characters and to use a single-character equivalent where one exists; Japanese has 「時」 for hours, and 「時間」 risks truncation issues.

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `ja/firefox-ios.xliff` — "payment methods" is rendered as 「暗号化されたカード情報」 (encrypted card information), adding a claim not in the source.
    - Current: `保存されたログイン情報と暗号化されたカード情報にアクセスするには Face ID が必要です。`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `保存されたパスワードと支払い方法にアクセスするには Firefox は Face ID を必要とします。`
    - The en-US says "your saved passwords and payment methods"; the Japanese asserts the card data is encrypted, which the source never states, and drops the Firefox subject.
- `NSLocationWhenInUseUsageDescription` — `ja/firefox-ios.xliff` — "may request your location" is rendered as a present-tense assertion that visited sites are requesting your location.
    - Current: `訪れたウェブサイトがあなたの位置情報を要求しています。`
    - Source: `Websites you visit may request your location.`
    - Suggest: `訪れたウェブサイトがあなたの位置情報を要求することがあります。`
    - The en-US source states a possibility ("may request"), while the Japanese asserts that sites are currently requesting the location.
- `Settings.AppIconSelection.AppIconNames.DarkPurple.Title.v136` — `ja/firefox-ios.xliff` — "Dark Purple" is rendered as 小紫, which is not the color "dark purple".
    - Current: `小紫`
    - Source: `Dark Purple`
    - Suggest: `ダークパープル`
    - The source names the icon color "Dark Purple"; 小紫 is not a standard Japanese color term for dark purple (濃紫/ダークパープル) and misnames the icon.
- `Settings.AppIconSelection.AppIconNames.Fun.Flaming.Title.146` — `ja/firefox-ios.xliff` — "Flaming" (fox with flames) is translated as 炎上, which means an online flame war/backlash.
    - Current: `炎上`
    - Source: `Flaming`
    - Suggest: `フレイム`
    - The developer comment says the icon is a fox outline with flames; 炎上 in Japanese primarily means a social-media pile-on, not a flame decoration.
- `Settings.AppIconSelection.AppIconNames.GoldenHour.Title.v137` — `ja/firefox-ios.xliff` — "Golden Hour" is translated as マジックアワー (magic hour), a different term.
    - Current: `マジックアワー`
    - Source: `Golden Hour`
    - Suggest: `ゴールデンアワー`
    - The source is "Golden Hour" and the sibling string "Blue Hour" is transliterated as ブルーアワー; マジックアワー refers to a different (broader) concept and is inconsistent with the sibling icon name.
- `Settings.AppIconSelection.AppIconNames.Minimal.Title.v139` — `ja/firefox-ios.xliff` — "Minimal" is rendered as "モノクロ" (monochrome), which names a color property rather than a simplified design.
    - Current: `モノクロ`
    - Source: `Minimal`
    - Suggest: `ミニマル`
    - The developer comment says the icon is a minimal, flattened and simplified version of the default icon; it says nothing about being monochrome.
- `Biometry.Screen.UniversalAuthenticationReason.v115` — `ja/firefox-ios.xliff` — The prompt asking the user to authenticate is rendered as the app stating it will authenticate access to passwords.
    - Current: `パスワードへのアクセスを認証します。`
    - Source: `Authenticate to access passwords.`
    - Suggest: `パスワードにアクセスするには認証してください。`
    - The en-US "Authenticate to access passwords." is an instruction to the user (as in the v122 variant, translated as 「…アクセスするには認証してください。」); the Japanese instead reads as the system declaring it authenticates the access.
- `Bookmarks.EmptyState.Root.ButtonTitle.v136` — `ja/firefox-ios.xliff` — "Sign in to Sync" is rendered as if "Sync" were a product name to log into, but the comment states Sync is a verb (sign in in order to sync).
    - Current: `Sync にログイン`
    - Source: `Sign in to Sync`
    - Suggest: `ログインして同期`
    - The developer comment explicitly says "Sync" is used as a verb; the button starts a sign-in flow to a Mozilla Account so data can be synced, not a login to a service called "Sync".
- `Bookmarks.Menu.AllBookmarks.v131` — `ja/firefox-ios.xliff` — Back button label "All" is expanded to "すべてのブックマーク", which is longer than the source for a tight navigation back button.
    - Current: `すべてのブックマーク`
    - Source: `All`
    - Suggest: `すべて`
    - The source is the short back-button label "All"; the expansion adds words not in the source and risks truncation in a navigation bar back button.
- `ContextualHints.Toolbar.GoogleLens.Title.v154` — `ja/firefox-ios.xliff` — Brand name "Google Lens" is partially translated as "Google レンズ".
    - Current: `Google レンズで検索`
    - Source: `Search With Google Lens`
    - Suggest: `Google Lens で検索`
    - Product/brand names should not be translated; the source is "Google Lens".
- `ContextualHints.Translations.Title.v145` — `ja/firefox-ios.xliff` — Idiomatic "Speaks Your Language" rendered literally as "はあなたの言語で話します" (the app talks).
    - Current: `%@ はあなたの言語で話します`
    - Source: `%@ Speaks Your Language`
    - Suggest: `%@ はあなたの言語に対応します`
    - The en-US means the app supports/understands the user's language (translation feature), not that it literally speaks.
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `ja/firefox-ios.xliff` — "Township" is rendered as 郡区, an unusual/incorrect term for a township-level administrative division.
    - Current: `村または郡区`
    - Source: `Village or Township`
    - Suggest: `村または町`
    - The source is "Village or Township"; 郡区 is not a recognized Japanese address component, whereas 町 (or 郷/町村) conveys township. The label would be meaningless to users.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `ja/firefox-ios.xliff` — "Fingerprinters" is translated as 「フィンガープリント」 (fingerprints) rather than the agents that perform fingerprinting.
    - Current: `フィンガープリント: %@`
    - Source: `Tracking content: %@`
    - Suggest: `フィンガープリント採取: %@`
    - Per the developer comment, %@ is the number of fingerprinters detected; the source names the trackers, not fingerprints themselves.
- `Menu.EnhancedTrackingProtection.On.Header.v128` — `ja/firefox-ios.xliff` — "If we spot something" is translated as "if there is a problem", losing that Firefox is the one detecting it.
    - Current: `何か問題があればお知らせします`
    - Source: `You’re protected. If we spot something, we’ll let you know.`
    - Suggest: `何か検出されたらお知らせします`
    - The source says the browser will notify the user if it spots something; the translation makes it a generic "if there's a problem".
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `ja/firefox-ios.xliff` — "Leave no traces on this device" is rendered as "We won't let this device be tracked", which asserts something different from the source.
    - Current: `この端末を追跡させません`
    - Source: `Leave no traces on this device`
    - Suggest: `この端末に痕跡を残しません`
    - The en-US says no traces (cookies, history, site data) are left on the device; the Japanese claims the device will not be tracked, a different privacy claim the source never makes.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `ja/firefox-ios.xliff` — "Your tabs are syncing!" is rendered as a passive/future statement rather than reporting that syncing is happening now.
    - Current: `タブが同期されます！`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `タブを同期しています！`
    - The en-US states syncing is currently in progress; 「同期されます」 reads as a future/general statement.
- `MainMenu.Account.SyncError.Title.v131` — `ja/firefox-ios.xliff` — "Sign back in to sync" is mistranslated as "log in and return to Sync".
    - Current: `ログインして Sync に戻る`
    - Source: `Sign back in to sync`
    - Suggest: `再度ログインして同期`
    - The source asks the user to sign in again in order to resume syncing; the Japanese says to log in and go back to Sync, misreading "back" as a destination and treating "sync" as a product name.
- `MainMenu.HeaderBanner.Title.v142` — `ja/firefox-ios.xliff` — "Make %@ your default" is expanded to "default web browser", adding wording not in the source.
    - Current: `%@ をデフォルトウェブブラウザーにしましょう`
    - Source: `Make %@ your default`
    - Suggest: `%@ を既定のブラウザーにしましょう`
    - The source says only "your default"; also ja Firefox uses 既定/デフォルトのブラウザー rather than the coined デフォルトウェブブラウザー.
- `MainMenu.ToolsSection.AccessibilityLabels.LessOptions.v141` — `ja/firefox-ios.xliff` — “Less” is rendered as “詳細を隠す” (hide details) rather than as the counterpart of “More” (fewer options).
    - Current: `詳細を隠す`
    - Source: `Less`
    - Suggest: `少なく表示`
    - The comment says the action hides some menu options in the section; “詳細” (details) is not what is hidden, and it does not pair with the “More” label.
- `MainMenu.ToolsSection.LessOptions.Title.v141` — `ja/firefox-ios.xliff` — "Less" is rendered as "詳細を隠す" (hide details) instead of the counterpart of "その他" (More).
    - Current: `詳細を隠す`
    - Source: `Less`
    - Suggest: `表示を減らす`
    - The source "Less" hides some menu options; its pair "More" is translated as 「その他」. 「詳細を隠す」 means "hide details", which is not what the action does and does not pair with 「その他」.
- `NativeErrorPage.BadCertDomain.AdvancedWarning1.v149` — `ja/firefox-ios.xliff` — "You might need to" is rendered as a definite necessity, losing the hedge.
    - Current: `Wi-Fi ネットワークにログインするか、VPN 設定を確認する必要があります。`
    - Source: `You might need to sign in to your Wi-Fi network, or check your VPN settings.`
    - Suggest: `Wi-Fi ネットワークにログインするか、VPN 設定を確認する必要があるかもしれません。`
    - The en-US uses "might need to"; the Japanese asserts that it is required.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `ja/firefox-ios.xliff` — "your support team might have more info" is turned into an instruction to contact the support team.
    - Current: `社内ネットワークを使用している場合は、技術サポートチームにお問い合わせください。`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `社内ネットワークを使用している場合は、技術サポートチームが詳しい情報を持っているかもしれません。`
    - The source only says the support team might have more information; it does not instruct the user to contact them.
- `NativeErrorPage.BadCertDomain.TitleLabel.v149` — `ja/firefox-ios.xliff` — "Something doesn’t look right" (uncertain appearance) is rendered as an assertion that a problem is occurring.
    - Current: `気を付けてください。何か問題が起こっています。`
    - Source: `Be careful. Something doesn’t look right.`
    - Suggest: `気を付けてください。何かおかしいようです。`
    - The en-US hedges ("doesn't look right"); the Japanese states as fact that a problem is occurring.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `ja/firefox-ios.xliff` — "your default" is expanded to "デフォルトウェブブラウザー", while the related label uses "デフォルトブラウザーアプリ".
    - Current: `*%@ をデフォルトウェブブラウザーに設定済みですか？*`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `*%@ をすでにデフォルトブラウザーに設定していますか？*`
    - Inconsistent term for the default browser setting within the same popup (デフォルトブラウザーアプリ in SecondLabel).
- `DefaultBrowserPopup.FirstLabel.v114` — `ja/firefox-ios.xliff` — iOS "Settings" is translated as 環境設定 here, inconsistent with 設定 used in the same popup's button title.
    - Current: `1. *環境設定* を開く`
    - Source: `1. Go to *Settings*`
    - Suggest: `1. *設定* を開く`
    - The source is "Settings" (the iOS Settings app), rendered 設定 in DefaultBrowserPopup.ButtonTitle on the same card; 環境設定 names a different, non-existent item.
- `Onboarding.Customization.Intro.Title.v123` — `ja/firefox-ios.xliff` — Title translated as "privacy protection" instead of "puts you in control".
    - Current: `%@ でプライバシー保護`
    - Source: `%@ puts you in control`
    - Suggest: `%@ なら思いのまま`
    - The en-US says "%@ puts you in control" (about customization control), not about privacy protection; the Japanese asserts a different product claim.
- `Onboarding.Customization.Theme.Description.v123` — `ja/firefox-ios.xliff` — "See the web in the best light" rendered as "view the web at the optimal brightness".
    - Current: `最適な明るさでウェブをご覧ください。`
    - Source: `See the web in the best light.`
    - Suggest: `ウェブを最適な見た目でご覧ください。`
    - The source refers to choosing a theme (light/dark appearance), not screen brightness.
- `Onboarding.Customization.Theme.System.Action.v123` — `ja/firefox-ios.xliff` — "System Auto" translated as "システムテーマ", dropping the automatic aspect.
    - Current: `システムテーマ`
    - Source: `System Auto`
    - Suggest: `システム自動`
    - The option is "System Auto" (follow the system automatically); the Japanese only says "system theme".
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `ja/firefox-ios.xliff` — Dropped the "putting you in control" clause from the source.
    - Current: `お気に入りのテーマを選択するか、%@ を端末の設定に合わせられます。`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `お気に入りのテーマを選択するか、%@ を端末の設定に合わせて、思いのままにカスタマイズできます。`
    - The en-US ends with "putting you in control", which is not rendered in the Japanese.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `ja/firefox-ios.xliff` — Statement turned into a request/instruction to share data.
    - Current: `%2$@ のマーケティングパートナーと共有してください。`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `%2$@ のマーケティングパートナーと共有します。`
    - The en-US describes what is shared; the imperative "共有してください" makes the product instruct the user to share their data.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `ja/firefox-ios.xliff` — "interaction data" rendered as 「対話データ」 (dialogue/conversation data) instead of 利用状況データ/インタラクションデータ.
    - Current: `診断情報と対話データ`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `診断データとインタラクションデータ`
    - en-US "diagnostic and interaction data" refers to usage/interaction telemetry; 「対話データ」 implies conversation data, asserting the product collects something different from what the source says.
- `Onboarding.Modern.TermsOfService.Title.v145` — `ja/firefox-ios.xliff` — "Take charge of the internet" is translated as "インターネットを導く" (lead/guide the internet) instead of taking control of one's own internet experience.
    - Current: `インターネットを導く`
    - Source: `Take charge of the internet`
    - Suggest: `インターネットの主導権を握ろう`
    - "Take charge of" means to take control, not to guide/lead something. The Japanese changes the meaning.
- `Onboarding.Wallpaper.Description.v114` — `ja/firefox-ios.xliff` — "a wallpaper that speaks to you" is rendered literally as a wallpaper that talks to you.
    - Current: `あなたに語りかける壁紙を選んでください。`
    - Source: `Choose a wallpaper that speaks to you.`
    - Suggest: `あなたの心に響く壁紙を選んでください。`
    - The English idiom "speaks to you" means "appeals to you / resonates with you", not literally addressing the user.
- `PrivacyDashboard.HeaderLabelForNoTrackersBlocked.v155` — `ja/firefox-ios.xliff` — Present/future statement "Firefox blocks trackers as you browse, you’ll see them here" is rendered as if trackers have already been blocked.
    - Current: `閲覧中に %@ がブロックしたトラッカーがここに表示されます。`
    - Source: `%@ blocks trackers as you browse, you’ll see them here.`
    - Suggest: `%@ は閲覧中にトラッカーをブロックします。ブロックしたトラッカーはここに表示されます。`
    - This string is shown when no trackers have been blocked yet; the past-tense Japanese implies trackers were already blocked and will be listed.
- `CreditCard.RememberCard.SecondaryButtonTitle.v115` — `ja/firefox-ios.xliff` — "Not Now" is translated as "今回は記憶しない" ("Don't remember this time"), which states something the source does not.
    - Current: `今回は記憶しない`
    - Source: `Not Now`
    - Suggest: `今はしない`
    - The source is simply "Not Now", a deferral; the Japanese asserts a decision not to save the card.
- `SearchZero.RecentSearches.SectionTitle.v146` — `ja/firefox-ios.xliff` — "Recent Searches" is rendered as "recently searched sites", introducing "sites" which the source never mentions.
    - Current: `最近検索したサイト`
    - Source: `Recent Searches`
    - Suggest: `最近の検索`
    - The section lists the user's recent search queries, not visited sites; the related toggle string uses 最近検索したもの, confirming the inconsistency.
- `Addresses.Settings.SavedAddressesSectionTitle.v124` — `ja/firefox-ios.xliff` — "SAVED ADDRESSES" (postal addresses) is translated as アドレス, which in Japanese normally means email/URL address, while other strings in the same screen use 住所.
    - Current: `保存したアドレス`
    - Source: `SAVED ADDRESSES`
    - Suggest: `保存した住所`
    - The same screen translates "Manage addresses" as 住所の管理 and "Address for %@" as %@ の住所; アドレス here is inconsistent and misleading for postal addresses.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `ja/firefox-ios.xliff` — The relation "in %@" is mistranslated so that the features appear "to" the app rather than within it.
    - Current: `AI 機能強化、または関連するポップアップが %@ に表示されなくなります`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `AI 機能強化、または関連するポップアップが %@ 内で表示されなくなります`
    - Source: "you won’t see new or current AI enhancements in %@, or pop-ups about them" — the enhancements are shown inside the app to the user.
- `Settings.Autoplay.BlockAudio.v137` — `ja/firefox-ios.xliff` — "Block Audio" rendered as "音声ありをブロック" (block content with audio).
    - Current: `音声ありをブロック`
    - Source: `Block Audio`
    - Suggest: `音声をブロック`
    - The source blocks audio; the sibling options use 「音声と動画をブロック」 and 「音声と動画を許可」, so the wording should be consistent as 「音声をブロック」.
- `Settings.Browsing.Tabs.v137` — `ja/firefox-ios.xliff` — "Tabs" is translated as "タブグループ" (Tab Groups).
    - Current: `タブグループ`
    - Source: `Tabs`
    - Suggest: `タブ`
    - The source is simply "Tabs", a section title for tab customization; "タブグループ" means "tab groups", a different feature.
- `Settings.DailyUsagePing.Title.v135` — `ja/firefox-ios.xliff` — "Daily Usage Ping" is rendered as "send daily usage frequency", changing the meaning.
    - Current: `毎日の使用頻度を送信する`
    - Source: `Daily Usage Ping`
    - Suggest: `1 日ごとの使用状況の送信`
    - The source is the noun label "Daily Usage Ping" (a daily ping indicating the app was used), not "usage frequency". "使用頻度" asserts that frequency-of-use data is sent, which the source does not say.
- `Settings.Rollouts.Message.v148` — `ja/firefox-ios.xliff` — "between updates" is mistranslated as "with each update" (更新ごとに), reversing the point of the sentence.
    - Current: `%@ は更新ごとに機能、パフォーマンス、安定性が向上しています。`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@ は更新の間にも機能、パフォーマンス、安定性を改善します。`
    - The source says improvements happen between updates (applied remotely), while the Japanese says they happen with each update, contradicting the following sentence about remote application.
- `Settings.Search.GoogleLens.Title.v153` — `ja/firefox-ios.xliff` — Product name "Google Lens" is partially translated as "Google レンズ".
    - Current: `Google レンズ`
    - Source: `Google Lens`
    - Suggest: `Google Lens`
    - "Google Lens" is a product/brand name; the description string keeps "Google" untranslated and the brand should not be transliterated.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Title.v124.v2` — `ja/firefox-ios.xliff` — Title "Suggestions from the Web" translated with an added verb "include" not present in the source.
    - Current: `ウェブからの提案を含める`
    - Source: `Suggestions from the Web`
    - Suggest: `ウェブからの提案`
    - The source is a noun-phrase title, not an instruction to include suggestions.
- `Settings.Studies.Message.v148` — `ja/firefox-ios.xliff` — "improves quality for everyone" is rendered as "improves everyone's quality", making the object the users rather than the product.
    - Current: `全員の品質を向上させます`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `すべてのユーザーにとっての品質を向上させます`
    - The source says testing features improves quality (of the product) for everyone; the Japanese literally says it improves everyone's quality, which is a different claim.
- `Settings.Studies.Title.v148` — `ja/firefox-ios.xliff` — "Allow Feature Studies" translated as allowing surveys about feature usage.
    - Current: `機能の使用調査を許可する`
    - Source: `Allow Feature Studies`
    - Suggest: `機能の調査を許可する`
    - The source refers to studies (experiments) of features, not surveys of feature usage; "使用" adds meaning not in the source.
- `Settings.Summarize.FooterTitle.v142` — `ja/firefox-ios.xliff` — "access to summarize pages" mistranslated as access to a "summary page".
    - Current: `要約ページへのアクセスを提供します。`
    - Source: `Provides access to summarize pages.`
    - Suggest: `ページを要約する機能へのアクセスを提供します。`
    - The source means the toggle provides access to the page-summarizing feature, not access to a page called "要約ページ".
- `SendTo.NoDevicesFound.Message.v119` — `ja/firefox-ios.xliff` — Translation drops "other" and "available to sync", changing the meaning to "no devices connected to this account were found".
    - Current: `このアカウントに接続された端末が見つかりませんでした。`
    - Source: `You don’t have any other devices connected to this account available to sync.`
    - Suggest: `このアカウントには、同期可能な他の端末が接続されていません。`
    - The source says there are no other devices connected to this account available to sync; the Japanese asserts no devices at all are connected.
- `Summarizer.Error.MissingPageContent.Message.v142` — `ja/firefox-ios.xliff` — "hit summarize" is rendered as "click" instead of tap on a touch-only phone UI.
    - Current: `「要約」をクリックしてください`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `「要約」をタップしてください`
    - The source says "hit summarize"; on iOS the interaction is a tap, and the ja text instructs the user to click, which is impossible on the device.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `ja/firefox-ios.xliff` — "This page may be restricted or mostly visual" is mistranslated as "not everything on this page is displayed".
    - Current: `このページはすべてが表示されていない可能性があります。`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `このページは制限されている、または主に画像や映像で構成されている可能性があります。`
    - The source explains the page may be access-restricted or mostly visual content; the ja claims parts of the page are not being displayed, which is a different statement about the product's behaviour.
- `TabLocation.ETP.Off.Secure.A11y.Label.v119` — `ja/firefox-ios.xliff` — Two independent sentences are joined with a contrastive "but", adding a relation the source does not state.
    - Current: `接続は安全ですが、強化型トラッキング防止がオフになっています。`
    - Source: `Secure connection. Enhanced Tracking Protection is off.`
    - Suggest: `接続は安全です。強化型トラッキング防止がオフになっています。`
    - en-US has two separate statements ("Secure connection. Enhanced Tracking Protection is off."); the ja uses "〜ですが" implying a contrast/concession not present in the source.
- `TermsOfUse.Link.HereText.v147` — `ja/firefox-ios.xliff` — Link text "here" is rendered as "利用規約について" (About the Terms of Use), which does not fit the surrounding sentence and states something the source does not.
    - Current: `利用規約について`
    - Source: `here`
    - Suggest: `こちら`
    - The source is simply the word 'here' inserted into '詳細は %@ をご覧ください。'; translating it as '利用規約について' changes the link label's meaning and produces '詳細は 利用規約について をご覧ください。'
- `Toolbar.ReaderModeWithSummarizer.Button.v150` — `ja/firefox-ios.xliff` — "Page summary available" is rendered as a statement that the user can summarize the page content, changing the meaning.
    - Current: `ページの内容を要約できます。`
    - Source: `Reader View. Page summary available.`
    - Suggest: `ページの要約を利用できます。`
    - The source states that a summary is available for the page (a badge indicator), not that the page content can be summarized by the user.
- `Translations.LanguagePicker.Title.v151` — `ja/firefox-ios.xliff` — "Translate Page to…" loses the "to…" indicating a target language choice, and is identical to the unrelated Sheet title.
    - Current: `ページを翻訳…`
    - Source: `Translate Page to…`
    - Suggest: `ページを次の言語に翻訳…`
    - The source is the title of a picker listing target languages ("Translate Page to…"); the translation drops the target-language element and duplicates Translations.Sheet.TitleLabel ("ページを翻訳").
- `Upgrade.Welcome.Description.v114` — `ja/firefox-ios.xliff` — "Same commitment to people over profits" is mistranslated as an "equal commitment beyond profits".
    - Current: `利益を超えて人々への平等なコミットメント。`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `利益よりも人を優先する変わらぬ姿勢。`
    - "Same" means the commitment is unchanged, not "equal (平等な)"; and "people over profits" means prioritizing people over profits, not "beyond profits".
- `WebCompatReporter.Preview.Data.PageLanguages.v155` — `ja/firefox-ios.xliff` — A bullet-point noun phrase is rendered as a past-tense sentence, changing the meaning.
    - Current: `言語設定がこのページに送信されました`
    - Source: `Language preferences sent to this page`
    - Suggest: `このページに送信された言語設定`
    - The source "Language preferences sent to this page" is a noun phrase listing data included in the report; the Japanese states as a completed fact that language preferences were sent to the page.
- `WebCompatReporter.SubOption.BrowserBlocked.v154` — `ja/firefox-ios.xliff` — Order of the two conditions is reversed relative to the source.
    - Current: `ブラウザーがサポートされていない、またはブロックされている`
    - Source: `Browser is blocked or unsupported`
    - Suggest: `ブラウザーがブロックされている、またはサポートされていない`
    - Source is "Browser is blocked or unsupported"; the translation swaps the order of the alternatives.
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `ja/firefox-ios.xliff` — "Upcoming" (an upcoming match) is translated as "近日公開", which means "coming soon" for a release/publication, not an upcoming match.
    - Current: `近日公開`
    - Source: `Upcoming`
    - Suggest: `開催予定`
    - The developer comment says this labels an upcoming match in the round phase. 「近日公開」 is used for releases (films, features) being published soon and is wrong for a scheduled match.
- `WorldCup.HomepageWidget.TemporaryView.Description.v151` — `ja/firefox-ios.xliff` — "as the World Cup approaches" is rendered as 「ワールドカップ開催についての」, attaching the phrase to the topic of the updates rather than the timing.
    - Current: `ワールドカップ開催についての最新情報をお伝えします`
    - Source: `We’ll keep you updated as the World Cup approaches`
    - Suggest: `ワールドカップ開催が近づくにつれて最新情報をお伝えします`
    - The source says updates will be provided as the World Cup approaches; the translation says updates about the World Cup being held, losing the temporal meaning.
- `Menu.ZoomPage.DecreaseZoom.AccessibilityLabel.v113` — `ja/firefox-ios.xliff` — Adds "縮小する" not present in the source "Decrease Zoom Level".
    - Current: `ズームレベルを下げて縮小する`
    - Source: `Decrease Zoom Level`
    - Suggest: `ズームレベルを下げる`
    - The source is simply "Decrease Zoom Level"; the added 「縮小する」 is extra content not in the en-US string.
- _…and 26 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Onboarding.Customization.Intro.Description.v123` — `ja/firefox-ios.xliff` — Duplicated particle "の" in "あなたののブラウジングスタイル".
    - Current: `あなたののブラウジングスタイル`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `あなたのブラウジングスタイル`
    - Typo: the possessive particle の is repeated, producing ungrammatical Japanese.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `ja/firefox-ios.xliff` — Particle mismatch: "ブックマーク、パスワードなどをどの端末からでも簡単にアクセスできます" uses を with アクセス.
    - Current: `ブックマーク、パスワードなどをどの端末からでも簡単にアクセスできます。`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `ブックマーク、パスワードなどにどの端末からでも簡単にアクセスできます。`
    - アクセスできる takes に, not を; the sentence is ungrammatical.
- `Onboarding.Modern.Sync.Description.v145` — `ja/firefox-ios.xliff` — Typo: 「保護されおり」 is missing the て (should be 保護されており).
    - Current: `暗号化して保護されおり`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `暗号化して保護されており`
    - Grammatical/spelling error in the Japanese verb form; 保護される + ており requires 「保護されており」.
- `FxAPush_DeviceConnected_body` — `ja/firefox-ios.xliff` — Wrong particle: "%@ に接続しました" reads as Sync connecting to the device rather than the device connecting to Sync.
    - Current: `Firefox Sync が %@ に接続しました`
    - Source: `Firefox Sync has connected to %@`
    - Suggest: `%@ が Firefox Sync に接続しました`
    - The comment says another device has connected to FxA; %@ is the newly connected device, so it should be the subject.
- `Send a crash report so Mozilla can fix the problem?` — `ja/firefox-ios.xliff` — Typo: 「いただだける」 has a duplicated だ.
    - Current: `ご協力いただだける方は`
    - Source: `Send a crash report so Mozilla can fix the problem?`
    - Suggest: `ご協力いただける方は`
    - The Japanese contains a spelling error (だだ instead of だ) in 「いただける」.

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Details.Trackers.v128` — `ja/firefox-ios.xliff` — "Trackers blocked" is rendered as 「ブロックされた追跡」, inconsistent with 「トラッカー」 used for "trackers" elsewhere on the same screen.
    - Current: `ブロックされた追跡: %@`
    - Source: `Trackers blocked: %@`
    - Suggest: `ブロックされたトラッカー: %@`
    - The same source term "trackers" is translated as トラッカー in the other strings on this screen (ソーシャルメディアトラッカー, トラッキングコンテンツ, トラッカーが見つかりませんでした); 「追跡」 (the act of tracking) is inconsistent and wrong for a count of trackers.
- `FirefoxHome.PrivacyNotice.PrivacyNoticeLink.v148` — `ja/firefox-ios.xliff` — "Privacy Notice" is rendered as 「プライバシー通知」 instead of the established Mozilla term 「プライバシー通知書」/「プライバシーポリシー」.
    - Current: `プライバシー通知`
    - Source: `Privacy Notice`
    - Suggest: `プライバシー通知書`
    - Mozilla ja uses 「プライバシー通知書」 for the Privacy Notice document; 「プライバシー通知」 reads as a notification rather than the legal document linked here.
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v153b` — `ja/firefox-ios.xliff` — "Trackers" is translated as 「追跡」 (tracking) instead of the established 「トラッカー」.
    - Current: `ブロックされた追跡: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ブロックしたトラッカー数: %@`
    - The count is of trackers (entities), not of tracking; other Firefox ja strings use 「トラッカー」.
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v155` — `ja/firefox-ios.xliff` — "Trackers" is rendered as 「追跡」 (tracking) instead of the established Firefox term 「トラッカー」.
    - Current: `ブロックされた追跡: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ブロックしたトラッカー: %@`
    - The source counts trackers (entities), not acts of tracking; Firefox ja uses トラッカー for "tracker".
- `MainMenu.SettingsSection.AccessibilityLabels.Settings.v132` — `ja/firefox-ios.xliff` — The accessibility label for Settings uses 環境設定 while the visible title for the same item uses 設定.
    - Current: `環境設定`
    - Source: `Settings`
    - Suggest: `設定`
    - MainMenu.SettingsSection.Settings.Title.v131 translates the same source "Settings" as 設定; the accessibility label for the identical menu item must match.
- `Onboarding.Modern.Welcome.ActionTreatmentA.v145` — `ja/firefox-ios.xliff` — "Set as Default Browser" rendered as "デフォルトウェブブラウザーに設定", inconsistent with the v140 string "デフォルトブラウザーに設定" for identical source text.
    - Current: `デフォルトウェブブラウザーに設定`
    - Source: `Set as Default Browser`
    - Suggest: `デフォルトブラウザーに設定`
    - Same en-US source "Set as Default Browser" is translated two different ways in the same file/screen; the source has no "web".
- `Menu.ZoomPage.CurrentZoomLevel.AccessibilityLabel.v113` — `ja/firefox-ios.xliff` — "ズーム レベル" with an inserted space is inconsistent with 「ズームレベル」 used in the sibling zoom strings.
    - Current: `現在のズーム レベル: %@`
    - Source: `Current Zoom Level: %@`
    - Suggest: `現在のズームレベル: %@`
    - The same term "Zoom Level" is rendered 「ズームレベル」 in the increase/decrease labels on the same Zoom Page Bar screen; the spaced form is inconsistent.
- `DefaultBrowserOnboarding.Button` — `ja/firefox-ios.xliff` — iOS "Settings" app is rendered as 「環境設定」 instead of the standard iOS term 「設定」.
    - Current: `環境設定を開く`
    - Source: `Go to Settings`
    - Suggest: `設定を開く`
    - The source refers to the iOS Settings app, which in Japanese iOS is 「設定」. 「環境設定」 is the macOS/desktop preferences term and does not match the on-device UI the user must navigate to.
- `DefaultBrowserOnboarding.Description1` — `ja/firefox-ios.xliff` — iOS "Settings" app is rendered as 「環境設定」 instead of the standard iOS term 「設定」.
    - Current: `1. 環境設定を開く`
    - Source: `1. Go to Settings`
    - Suggest: `1. 設定を開く`
    - Step 1 of the default-browser instructions tells the user to open the iOS Settings app, labelled 「設定」 on the device; 「環境設定」 is the desktop preferences term and misleads the user.
- `CoverSheet.v24.ETP.Settings.Button` — `ja/firefox-ios.xliff` — "Go to Settings" is rendered as 環境設定 (Preferences) while every other string in this batch uses 設定 for Settings.
    - Current: `環境設定を開く`
    - Source: `Go to Settings`
    - Suggest: `設定を開く`
    - en-US "Settings" is consistently 設定 elsewhere (ツールバー設定, 設定でオフにする, ディスプレイ設定); iOS Firefox's settings screen is 設定, not 環境設定.
- `Decrease text size` — `ja/firefox-ios.xliff` — Accessibility label is phrased as a sentence ("...します") instead of a noun label matching the source.
    - Current: `文字サイズを縮小します`
    - Source: `Decrease text size`
    - Suggest: `文字サイズを縮小`
    - The source is a button accessibility label "Decrease text size"; other accessibility labels in this batch use plain noun/verb forms.
- `Settings.TrackingProtectionOption.BlockListStrict` — `ja/firefox-ios.xliff` — "Strict" translated as 広範囲 (broad/extensive) instead of the standard 厳格.
    - Current: `広範囲`
    - Source: `Strict`
    - Suggest: `厳格`
    - The protection level "Strict" is rendered inconsistently with the standard Firefox ja term 「厳格」; 広範囲 means "wide range".

### E. Typography, punctuation & spacing

- `GoogleLens.Interstitial.LoadingLabel.v156` — `ja/firefox-ios.xliff` — ASCII three-dot ellipsis used where the source has a single ellipsis character.
    - Current: `画像の検索結果を取得中...`
    - Source: `Finding Image Results…`
    - Suggest: `画像の検索結果を取得中…`
    - The en-US uses the ellipsis character “…”; the target uses three ASCII periods.
- `MainMenu.Submenus.Tools.ReportBrokenSite.Title.v133` — `ja/firefox-ios.xliff` — Three ASCII periods used instead of the ellipsis character present in the source.
    - Current: `動作しないサイトを報告...`
    - Source: `Report Broken Site…`
    - Suggest: `動作しないサイトを報告…`
    - The source uses the single ellipsis character “…”; the Japanese uses three ASCII dots.
- `MainMenu.ToolsSection.FindInPage.Title.v131` — `ja/firefox-ios.xliff` — ASCII three-dot sequence used instead of the ellipsis character used elsewhere in the file.
    - Current: `ページ内を検索...`
    - Source: `Find in Page…`
    - Suggest: `ページ内を検索…`
    - Other strings in the same file (Translate Page…, Translated…) use the ellipsis character 「…」; this one uses three ASCII periods, an inconsistency on the same menu screen.
- `WebCompatReporter.Preview.Data.PrivateBrowsingStatus.v155` — `ja/firefox-ios.xliff` — Stray space after the fullwidth colon.
    - Current: `プライベートブラウジングの状態： オンまたはオフ`
    - Source: `Private browsing status: on or off`
    - Suggest: `プライベートブラウジングの状態：オンまたはオフ`
    - A fullwidth colon already includes trailing spacing; the extra halfwidth space is a typographic defect in Japanese text.
- `Menu.SharePageAction.Title` — `ja/firefox-ios.xliff` — ASCII three-dot ellipsis used where the source has a single ellipsis character.
    - Current: `ページを共有...`
    - Source: `Share Page With…`
    - Suggest: `ページを共有…`
    - The source uses the ellipsis character "…"; the Japanese uses three ASCII periods.
- `TodayWidget.MoreTabsLabel` — `ja/firefox-ios.xliff` — ASCII three-dot sequence used instead of the ellipsis character present in the source.
    - Current: `その他 %d 個...`
    - Source: `+%d More…`
    - Suggest: `その他 %d 個…`
    - The en-US string uses the ellipsis character "…"; the target substitutes three ASCII periods.

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
