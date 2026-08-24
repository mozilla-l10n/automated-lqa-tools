# Firefox iOS l10n QA — ja

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **Previous run** | 2026-08-22 @ `112744e9d020` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,910 |

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
| Files | 95 |
| Strings | 1,910 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 11, `curly-double` 3 | **corner** |
| ellipsis | `char` 11, `ascii` 9 | _mixed_ |
| fullwidth | `punctuation` 394 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (116)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 77 |
| 3 | Degraded language (grammar, spelling, terminology) | 25 |
| 4 | Cosmetic (typography, spacing) | 14 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `ja/firefox-ios.xliff` — "saved passwords" is rendered as "保存されたログイン情報" (saved login information) and "payment methods" as "暗号化されたカード情報" (encrypted card information), adding/changing meaning.
    - Current: `保存されたログイン情報と暗号化されたカード情報にアクセスするには Face ID が必要です。`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `保存されたパスワードと支払い方法にアクセスするには Firefox は Face ID を必要とします。`
    - The en-US says "saved passwords and payment methods"; the translation says login information and "encrypted" card information, which is not in the source, and drops the subject Firefox.
- `NSLocationWhenInUseUsageDescription` — `ja/firefox-ios.xliff` — "may request" (possibility) is translated as "要求しています" (is currently requesting).
    - Current: `訪れたウェブサイトがあなたの位置情報を要求しています。`
    - Source: `Websites you visit may request your location.`
    - Suggest: `訪れたウェブサイトがあなたの位置情報を要求することがあります。`
    - The source states a potential future behavior ("may request"), not an ongoing action.
- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `ja/firefox-ios.xliff` — The accessibility hint is rendered as an imperative request to the user rather than a description of the action performed.
    - Current: `%@ のアプリアイコンを選択してください`
    - Source: `Select the %@ app icon`
    - Suggest: `%@ のアプリアイコンを選択します`
    - VoiceOver hints describe what happens when the row is activated ("Select the %@ app icon"); 〜してください turns it into an instruction to the user.
- `Settings.AppIconSelection.AppIconNames.DarkPurple.Title.v136` — `ja/firefox-ios.xliff` — "Dark Purple" is rendered as 小紫, which is not a color name for dark purple.
    - Current: `小紫`
    - Source: `Dark Purple`
    - Suggest: `ダークパープル`
    - The source names the icon's dark purple background. 小紫 (a shrub name / "small purple") does not convey "dark purple"; other color icons use katakana or standard color words.
- `Settings.AppIconSelection.AppIconNames.Fun.Flaming.Title.146` — `ja/firefox-ios.xliff` — "Flaming" (fox outline with flames) is translated as 炎上, meaning an online flame-war/backlash.
    - Current: `炎上`
    - Source: `Flaming`
    - Suggest: `フレイム`
    - The developer comment says the icon is a fox outline with flames; 炎上 in Japanese usage means a public online pile-on, not a flaming design.
- `Settings.AppIconSelection.AppIconNames.GoldenHour.Title.v137` — `ja/firefox-ios.xliff` — "Golden Hour" is translated as マジックアワー (Magic Hour), a different term, inconsistent with ブルーアワー used for "Blue Hour".
    - Current: `マジックアワー`
    - Source: `Golden Hour`
    - Suggest: `ゴールデンアワー`
    - Golden hour and magic hour are distinct terms; the sibling string Blue Hour is transliterated as ブルーアワー, so this should be ゴールデンアワー.
- `Settings.AppIconSelection.AppIconNames.Minimal.Title.v139` — `ja/firefox-ios.xliff` — "Minimal" is translated as モノクロ (monochrome), which states something the source does not.
    - Current: `モノクロ`
    - Source: `Minimal`
    - Suggest: `ミニマル`
    - The comment says the icon flattens and simplifies the default icon; it is about minimalism, not being black and white.
- `Addresses.BottomSheet.UseSavedAddressBottomSheet.v124` — `ja/firefox-ios.xliff` — "address" here means a postal address, but it is translated as "アドレス" (email/URL address).
    - Current: `保存したアドレスを使用しますか？`
    - Source: `Use a saved address?`
    - Suggest: `保存した住所を使用しますか？`
    - The developer comment says the user is entering an address and is prompted to use a saved address; other strings in EditAddress.strings correctly use 住所. "アドレス" in Japanese normally means an email address or URL.
- `ContextualHints.Translations.Title.v145` — `ja/firefox-ios.xliff` — "Speaks Your Language" is rendered too literally as "あなたの言語で話します".
    - Current: `%@ はあなたの言語で話します`
    - Source: `%@ Speaks Your Language`
    - Suggest: `%@ はあなたの言語に対応します`
    - The source is an idiom meaning the app supports/understands the user's language (a translation feature hint), not that the app literally speaks.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Fingerprinter.v129` — `ja/firefox-ios.xliff` — "Fingerprinters" (the trackers) is rendered as "フィンガープリント" (fingerprint), naming the technique rather than the trackers.
    - Current: `フィンガープリント: %@`
    - Source: `Fingerprinters: %@`
    - Suggest: `フィンガープリント採取: %@`
    - The source counts fingerprinters (scripts that collect fingerprints); Firefox ja uses 「フィンガープリント採取」 for this. 「フィンガープリント」 alone means the fingerprint itself.
- `Menu.EnhancedTrackingProtection.Details.Verifier.v128` — `ja/firefox-ios.xliff` — "Verified by %@" is rendered as "認証局: %@" (Certificate authority: %@), changing the phrasing/meaning.
    - Current: `認証局: %@`
    - Source: `Verified by %@`
    - Suggest: `%@ により認証されています`
    - The source states who verified the site; the translation labels the value as a certificate authority, which is a different statement than the source.
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `ja/firefox-ios.xliff` — "Leave no traces on this device" is mistranslated as "この端末を追跡させません" (we won't let this device be tracked).
    - Current: `この端末を追跡させません`
    - Source: `Leave no traces on this device`
    - Suggest: `この端末に痕跡を残しません`
    - The source is about leaving no traces/data on the device, not about preventing tracking of the device.
- `ContextualHints.FirefoxHomepage.JumpBackIn.SyncedTab.v106` — `ja/firefox-ios.xliff` — "Your tabs are syncing!" is rendered as a passive/future statement rather than reporting that syncing is happening.
    - Current: `タブが同期されます！`
    - Source: `Your tabs are syncing! Pick up where you left off on your other device.`
    - Suggest: `タブを同期しています！`
    - The en-US states that the tabs are currently syncing (an accomplished/ongoing state), not that they will be synced.
- `MainMenu.Account.SyncError.Title.v131` — `ja/firefox-ios.xliff` — "Sign back in to sync" is mistranslated as "log in and return to Sync".
    - Current: `ログインして Sync に戻る`
    - Source: `Sign back in to sync`
    - Suggest: `再ログインして同期`
    - The source means the user must sign in again in order to resume syncing; the Japanese says "log in and go back to Sync", changing the meaning.
- `MainMenu.HeaderBanner.Title.v142` — `ja/firefox-ios.xliff` — "your default" is expanded to "default web browser" adding wording not in the source.
    - Current: `%@ をデフォルトウェブブラウザーにしましょう`
    - Source: `Make %@ your default`
    - Suggest: `%@ をデフォルトにしましょう`
    - Source is "Make %@ your default"; the added "ウェブブラウザー" is not in the source and lengthens a tight banner title.
- `MainMenu.ToolsSection.LessOptions.Title.v141` — `ja/firefox-ios.xliff` — "Less" is translated as "詳細を隠す" which does not correspond to the counterpart "その他" used for "More".
    - Current: `詳細を隠す`
    - Source: `Less`
    - Suggest: `表示を減らす`
    - The source pair is More/Less (show more or fewer menu options). "その他" (More) and "詳細を隠す" (hide details) are inconsistent as a toggle pair; the label should express showing fewer options.
- `NativeErrorPage.BadCertDomain.AdvancedWarning1.v149` — `ja/firefox-ios.xliff` — "might need to" is translated as a definite necessity.
    - Current: `必要があります。`
    - Source: `You might need to sign in to your Wi-Fi network, or check your VPN settings.`
    - Suggest: `必要があるかもしれません。`
    - Source expresses possibility ("You might need to"), not certainty.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `ja/firefox-ios.xliff` — The translation instructs the user to contact the support team instead of stating that the support team might have more info.
    - Current: `技術サポートチームにお問い合わせください`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `技術サポートチームが詳しい情報を持っているかもしれません`
    - Source says "your support team might have more info" — a statement of possibility, not an imperative to contact them.
- `NativeErrorPage.BadCertDomain.TitleLabel.v149` — `ja/firefox-ios.xliff` — "Something doesn’t look right" (appears to be something wrong) is rendered as a definite statement that a problem is occurring.
    - Current: `何か問題が起こっています。`
    - Source: `Be careful. Something doesn’t look right.`
    - Suggest: `何か問題があるようです。`
    - The en-US hedges with "doesn’t look right"; the Japanese asserts a problem as fact.
- `NativeErrorPage.GenericError.TitleLabel.v131` — `ja/firefox-ios.xliff` — "Something doesn’t look right" is rendered as a definite assertion that a problem is occurring.
    - Current: `何か問題が起こっています。`
    - Source: `Be careful. Something doesn’t look right.`
    - Suggest: `何か問題があるようです。`
    - The en-US hedges with "doesn’t look right"; the Japanese asserts a problem as fact.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `ja/firefox-ios.xliff` — "already your default?" translated as "設定済みですか？" adds "ウェブブラウザーに設定" but drops "already" nuance is fine; however "デフォルトウェブブラウザー" is inconsistent with "デフォルトブラウザー" used elsewhere on the same card.
    - Current: `デフォルトウェブブラウザー`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `デフォルトブラウザー`
    - The same card uses デフォルトブラウザー (Title) and デフォルトブラウザーアプリ (SecondLabel); デフォルトウェブブラウザー is an inconsistent rendering of the same term.
- `DefaultBrowserPopup.FirstLabel.v114` — `ja/firefox-ios.xliff` — "Settings" rendered as 環境設定 while the sibling button string uses 設定, and iOS's app is 設定.
    - Current: `1. *環境設定* を開く`
    - Source: `1. Go to *Settings*`
    - Suggest: `1. *設定* を開く`
    - The iOS Settings app is called 設定 in Japanese, and DefaultBrowserPopup.ButtonTitle.v114 on the same card uses 設定; 環境設定 is inconsistent and does not match the on-device label the user must find.
- `Onboarding.Customization.Intro.Title.v123` — `ja/firefox-ios.xliff` — Translation says "privacy protection" instead of "puts you in control".
    - Current: `%@ でプライバシー保護`
    - Source: `%@ puts you in control`
    - Suggest: `%@ で思いのままに`
    - The source "%@ puts you in control" is about user control over customization, not privacy protection.
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `ja/firefox-ios.xliff` — The title adds "turn on" which is not in the source; the source states notifications help you stay safer.
    - Current: `通知をオンにして %@ で安全性を高めましょう`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `通知は %@ での安全性を高めるのに役立ちます`
    - en-US "Notifications help you stay safer with %@" is a statement about the benefit of notifications, not an instruction to turn them on (that is the separate button string).
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `ja/firefox-ios.xliff` — "interaction data" is rendered as "対話データ" (dialogue/conversation data), which is the wrong term.
    - Current: `診断情報と対話データ`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `診断データと利用状況データ`
    - "interaction data" means data about how the user interacts with the app; "対話データ" reads as conversation data, a different meaning (Mozilla's standard ja wording is 「診断データと利用状況データ」).
- `Onboarding.Modern.BrandRefresh.Welcome.ActionTreatmentA.v148` — `ja/firefox-ios.xliff` — "ウェブ" is added; the source says "Default Browser", not "Default Web Browser".
    - Current: `デフォルトウェブブラウザーに設定`
    - Source: `Set as Default Browser`
    - Suggest: `既定のブラウザーに設定`
    - The source is "Set as Default Browser"; the translation inserts "ウェブ" which is not in the source.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `ja/firefox-ios.xliff` — "your top sites" is translated but "all in one place" is rendered as "利用できます", losing the sense that they appear together in one place; also acceptable—main issue is none.
    - Current: `がすべて 1 か所で利用できます`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `がすべて 1 か所に表示されます`
    - The source says the items appear all in one place, not that they are "available for use" in one place; 表示されます conveys the intended meaning.
- `Onboarding.Modern.TermsOfService.Title.v145` — `ja/firefox-ios.xliff` — "Take charge of the internet" is rendered as "インターネットを導く" (lead/guide the internet) instead of taking control.
    - Current: `インターネットを導く`
    - Source: `Take charge of the internet`
    - Suggest: `インターネットを自分の手に`
    - "Take charge of" means to take control/be in charge, not to lead or guide something.
- `Onboarding.Sync.Title.v120` — `ja/firefox-ios.xliff` — "Stay encrypted" (user stays encrypted) is rendered as the app maintaining the encrypted state, and the title reads as a statement about the app rather than about the user.
    - Current: `端末間の移動時に暗号化した状態を維持します`
    - Source: `Stay encrypted when you hop between devices`
    - Suggest: `端末間を移動しても暗号化された状態を維持`
    - The source says the user's data remains encrypted (passive), while 暗号化した状態 implies the subject performs the encryption; a passive form matches the en-US meaning.
- `CreditCard.RememberCard.SecondaryButtonTitle.v115` — `ja/firefox-ios.xliff` — "Not Now" is translated as "Do not remember this time", changing the meaning.
    - Current: `今回は記憶しない`
    - Source: `Not Now`
    - Suggest: `後で`
    - The source is a simple deferral button "Not Now"; the Japanese asserts a refusal to save, which is different content from postponing.
- `SearchZero.RecentSearches.SectionTitle.v146` — `ja/firefox-ios.xliff` — "Recent Searches" is rendered as "recently searched sites", changing the meaning from search terms to sites.
    - Current: `最近検索したサイト`
    - Source: `Recent Searches`
    - Suggest: `最近の検索`
    - The source refers to recent searches (search queries), not sites; the related toggle string correctly uses 最近検索したもの.
- `Addresses.Settings.SavedAddressesSectionTitle.v124` — `ja/firefox-ios.xliff` — "Addresses" (postal addresses) is translated as アドレス, which in Japanese means email/web address.
    - Current: `保存したアドレス`
    - Source: `SAVED ADDRESSES`
    - Suggest: `保存した住所`
    - The comment states these are postal addresses; other strings in the same file use 住所 (Addresses.ManageAddressesButton, Addresses.Settings.ListItemA11y), making アドレス inconsistent and misleading.
- `Settings.AIControls.HeaderCard.Title.v151` — `ja/firefox-ios.xliff` — "You always have a choice in %@" is translated as "%@ には常に選択肢があります", losing the subject "you".
    - Current: `%@ には常に選択肢があります`
    - Source: `You always have a choice in %@`
    - Suggest: `%@ では常にあなたに選択肢があります`
    - The source states the user always has a choice within the app; the Japanese reads as if the app itself has options.
- `Settings.Autoplay.BlockAudio.v137` — `ja/firefox-ios.xliff` — "Block Audio" is rendered as "音声ありをブロック" ("block ones with audio"), which does not match the source.
    - Current: `音声ありをブロック`
    - Source: `Block Audio`
    - Suggest: `音声をブロック`
    - The source "Block Audio" simply means blocking audio autoplay; the sibling strings use 音声と動画をブロック for "Block Audio and Video", so "音声をブロック" is the consistent and accurate rendering.
- `Settings.Browsing.Tabs.v137` — `ja/firefox-ios.xliff` — "Tabs" is translated as "タブグループ" (tab groups) instead of "タブ".
    - Current: `タブグループ`
    - Source: `Tabs`
    - Suggest: `タブ`
    - The source is "Tabs", the title for Tabs customization under Browsing settings; "タブグループ" means "tab groups", a different concept.
- `Settings.DailyUsagePing.Title.v135` — `ja/firefox-ios.xliff` — "Daily Usage Ping" is rendered as "毎日の使用頻度を送信する" (send daily usage frequency), altering the meaning.
    - Current: `毎日の使用頻度を送信する`
    - Source: `Daily Usage Ping`
    - Suggest: `1 日 1 回の使用状況핑グ`
    - The source is a noun label naming the "Daily Usage Ping"; the translation invents "usage frequency" and adds "send", which is not in the source.
- `Settings.Rollouts.Message.v148` — `ja/firefox-ios.xliff` — "between updates" is mistranslated as "更新ごとに" (with each update), reversing the intended meaning.
    - Current: `%@ は更新ごとに機能、パフォーマンス、安定性が向上しています。`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@ は更新と更新の間にも機能、パフォーマンス、安定性を改善します。`
    - The source says improvements happen between updates (remotely), not at each update.
- `Settings.Search.GoogleLens.Title.v153` — `ja/firefox-ios.xliff` — The product name "Google Lens" is partly translated as "Google レンズ".
    - Current: `Google レンズ`
    - Source: `Google Lens`
    - Suggest: `Google Lens`
    - "Google Lens" is a product/brand name and should remain untranslated, as it is in the accompanying description strings' context.
- `Settings.Studies.Message.v148` — `ja/firefox-ios.xliff` — "improves quality for everyone" rendered as "全員の品質を向上させます" (improves everyone's quality), which misstates the meaning.
    - Current: `全員の品質を向上させます`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `すべての人のために品質を向上させます`
    - The source says testing improves the product's quality for everyone, not that it improves the quality of everyone.
- `Settings.Studies.Title.v148` — `ja/firefox-ios.xliff` — "Allow Feature Studies" is translated as "機能の使用調査" (usage surveys of features), adding "使用" not in the source.
    - Current: `機能の使用調査を許可する`
    - Source: `Allow Feature Studies`
    - Suggest: `機能の調査を許可する`
    - The source refers to studies (experiments) of features, not usage surveys.
- `Settings.Summarize.FooterTitle.v142` — `ja/firefox-ios.xliff` — "summarize pages" (the action of summarizing pages) is mistranslated as "要約ページ" (summary pages).
    - Current: `要約ページへのアクセスを提供します。`
    - Source: `Provides access to summarize pages.`
    - Suggest: `ページの要約機能へのアクセスを提供します。`
    - The source describes access to the page-summarization feature, not to "summary pages"; the related toggle title is translated as ページを要約する.
- `SendTo.NoDevicesFound.Message.v119` — `ja/firefox-ios.xliff` — Translation drops "other" and "available to sync" and changes the meaning to "no devices were found".
    - Current: `このアカウントに接続された端末が見つかりませんでした。`
    - Source: `You don’t have any other devices connected to this account available to sync.`
    - Suggest: `このアカウントには、同期可能な他の端末が接続されていません。`
    - The source states there are no other devices connected to this account that are available to sync; the translation omits "other" and "available to sync".
- `Summarizer.Error.MissingPageContent.Message.v142` — `ja/firefox-ios.xliff` — "hit summarize" is rendered as "クリック" (click) on a touch device where the source implies tapping/pressing.
    - Current: `「要約」をクリックしてください`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `「要約」をタップしてください`
    - This is an iOS phone UI; the source says "hit summarize", and other strings in the same feature use タップ (e.g. ContextualHints.Summarize.Description). "クリック" is wrong for touch input.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `ja/firefox-ios.xliff` — The second sentence mistranslates "This page may be restricted or mostly visual."
    - Current: `このページはすべてが表示されていない可能性があります。`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `このページは制限されているか、大部分が画像などの視覚的コンテンツである可能性があります。`
    - The source says the page may be restricted or mostly visual content; the translation says the page may not be fully displayed, which is a different statement.
- `TabLocation.ETP.Off.Secure.A11y.Label.v119` — `ja/firefox-ios.xliff` — Two independent sentences were joined with an adversative "but", adding a contrast not in the source.
    - Current: `接続は安全ですが、強化型トラッキング防止がオフになっています。`
    - Source: `Secure connection. Enhanced Tracking Protection is off.`
    - Suggest: `接続は安全です。強化型トラッキング防止がオフになっています。`
    - The source is two separate statements: "Secure connection. Enhanced Tracking Protection is off." The parallel string TabLocation.ETP.Off.NotSecure keeps them separate.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `ja/firefox-ios.xliff` — "Sync" here is the Firefox Sync feature name used as a tab-tray section title, but it is translated as the generic verb 「同期」 while the related button in the same file uses 「タブを同期」.
    - Current: `同期`
    - Source: `Sync`
    - Suggest: `同期タブ`
    - The developer comment says it is "The title on the button to look at synced tabs." 「同期」 alone reads as the action "synchronize" rather than naming the synced-tabs section.
- `TabTrayCloseTabsOlderThanTitle.v140` — `ja/firefox-ios.xliff` — Translation adds "日数" (number of days) although the menu offers day, week and month options.
    - Current: `次の日数より古いタブを閉じる…`
    - Source: `Close tabs older than…`
    - Suggest: `次の期間より古いタブを閉じる…`
    - en-US is "Close tabs older than…" with no unit; the submenu includes 1 week and 1 month, so restricting to days is wrong content.
- `TermsOfUse.Link.HereText.v147` — `ja/firefox-ios.xliff` — The link text "here" is rendered as 「利用規約について」 ("about the Terms of Use"), inventing content not in the source.
    - Current: `利用規約について`
    - Source: `here`
    - Suggest: `こちら`
    - Source is simply "here", inserted into "You can learn more %@."; the ja parent string 「詳細は %@ をご覧ください。」 expects a simple "こちら".
- `Translations.LanguagePicker.Title.v151` — `ja/firefox-ios.xliff` — The "to…" part of "Translate Page to…" is dropped, making the title identical to the plain "Translate Page" sheet title.
    - Current: `ページを翻訳…`
    - Source: `Translate Page to…`
    - Suggest: `ページを次の言語に翻訳…`
    - The source is "Translate Page to…", a title for a picker listing target languages; the translation omits the target-language notion and collides with Translations.Sheet.TitleLabel.v145 ("Translate Page" = ページを翻訳).
- `Upgrade.Welcome.Description.v114` — `ja/firefox-ios.xliff` — 'Same commitment to people over profits' is mistranslated as '利益を超えて人々への平等なコミットメント', adding '平等な' (equal) and losing 'Same'.
    - Current: `利益を超えて人々への平等なコミットメント。`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `利益よりも人々を優先する変わらぬ姿勢。`
    - The source says the commitment is unchanged (Same) and prioritizes people over profits; the Japanese says an 'equal' commitment, which is not in the source and drops the 'same/unchanged' meaning.
- `WebCompatReporter.Preview.Data.PageLanguages.v155` — `ja/firefox-ios.xliff` — The bullet item is translated as a sentence stating that language preferences were sent, instead of a noun phrase naming the data sent to the page.
    - Current: `言語設定がこのページに送信されました`
    - Source: `Language preferences sent to this page`
    - Suggest: `このページに送信された言語設定`
    - The en-US 'Language preferences sent to this page' is a noun phrase listing the data included in the report (like the other bullets); the Japanese turns it into a past-tense statement 'Language preferences were sent to this page'.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `ja/firefox-ios.xliff` — "Please refresh" is rendered as "refresh the page", adding a page reference not in the source.
    - Current: `ページを更新してください。`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `更新してください。`
    - The source asks the user to refresh the widget's match data, not a web page; the widget is on the Firefox homepage and there is no page to reload.
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `ja/firefox-ios.xliff` — "Upcoming" (an upcoming match) is translated as 近日公開, which means an upcoming release/publication, not an upcoming match.
    - Current: `近日公開`
    - Source: `Upcoming`
    - Suggest: `開催予定`
    - The developer comment says this labels an upcoming match in the round phase; 近日公開 means "coming soon (release)" and is wrong for a scheduled match.
- `WorldCup.HomepageWidget.TemporaryView.Description.v151` — `ja/firefox-ios.xliff` — "as the World Cup approaches" is rendered as "about the World Cup being held", losing the meaning of the approaching event.
    - Current: `ワールドカップ開催についての最新情報をお伝えします`
    - Source: `We’ll keep you updated as the World Cup approaches`
    - Suggest: `ワールドカップ開催が近づくにつれて最新情報をお伝えします`
    - The source states updates will be provided as the World Cup approaches; the Japanese drops the temporal "approaches" sense.
- `Use your fingerprint to access Logins now.` — `ja/firefox-ios.xliff` — Translation says "log in using fingerprint" instead of "use your fingerprint to access saved Logins".
    - Current: `指紋認証を利用してログインする。`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `指紋認証を利用してログイン情報にアクセスします。`
    - The source means using Touch ID to access the stored Logins list, not to sign in; the Japanese reverses the object of the action.
- `DefaultBrowserOnboarding.Button` — `ja/firefox-ios.xliff` — "Go to Settings" refers to the iOS Settings app, rendered as 環境設定 (Preferences) instead of 設定.
    - Current: `環境設定を開く`
    - Source: `Go to Settings`
    - Suggest: `設定を開く`
    - The developer comment says this opens the iOS system settings; iOS's Settings app is called 設定 in Japanese, and the related string DefaultBrowserOnboarding.Screenshot refers to the iOS settings page. 環境設定 names a different thing and is inconsistent with the platform term.
- `DefaultBrowserOnboarding.Description1` — `ja/firefox-ios.xliff` — Step 1 "Go to Settings" uses 環境設定 instead of the iOS Settings app name 設定.
    - Current: `1. 環境設定を開く`
    - Source: `1. Go to Settings`
    - Suggest: `1. 設定を開く`
    - This step instructs the user to open the iOS Settings app, which is named 設定 in Japanese; 環境設定 (Preferences) points at a different thing and conflicts with the following steps describing the iOS settings screen.
- `Next in-page result` — `ja/firefox-ios.xliff` — Accessibility label translated as "search for next in page" instead of "next in-page result".
    - Current: `ページ内で次を検索`
    - Source: `Next in-page result`
    - Suggest: `ページ内の次の検索結果`
    - The source names a result ("Next in-page result"), not an action of searching; the Japanese turns the noun label into a search command.
- `Previous in-page result` — `ja/firefox-ios.xliff` — Accessibility label translated as "search for previous in page" instead of "previous in-page result".
    - Current: `ページ内で前を検索`
    - Source: `Previous in-page result`
    - Suggest: `ページ内の前の検索結果`
    - The source names a result ("Previous in-page result"), not a search action; the Japanese changes the meaning of the accessibility label.
- `LibraryPanel.History.Title.v138` — `ja/firefox-ios.xliff` — "synced history from other devices" is rendered as "synced from other devices" without specifying history, but more importantly no defect—see rationale.
    - Current: `他の端末から同期されたものを含む`
    - Source: `Deletes history (including synced history from other devices), cookies, and other browsing data.`
    - Suggest: `他の端末から同期された履歴を含む`
    - The source specifies "synced history from other devices"; the Japanese drops 履歴 leaving a vague "もの".
- _…and 21 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Onboarding.Customization.Intro.Description.v123` — `ja/firefox-ios.xliff` — Duplicated particle "の" in "あなたののブラウジングスタイル".
    - Current: `あなたののブラウジングスタイル`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `あなたのブラウジングスタイル`
    - Typo: the possessive particle の is repeated.
- `Onboarding.Modern.BrandRefresh.Sync.Description.v148` — `ja/firefox-ios.xliff` — Particle mismatch: 「〜を…アクセスできます」 is ungrammatical.
    - Current: `ブックマーク、パスワードなどをどの端末からでも簡単にアクセスできます。`
    - Source: `Grab bookmarks, passwords, and more on any device in a snap. Your personal data stays safe and secure with encryption.`
    - Suggest: `ブックマーク、パスワードなどにどの端末からでも簡単にアクセスできます。`
    - The verb アクセスする takes に, not を; as written the sentence is grammatically incorrect.
- `Onboarding.Modern.Sync.Description.v145` — `ja/firefox-ios.xliff` — Typo: 「保護されおり」 is missing a character (should be 「保護されており」).
    - Current: `データはすべて暗号化して保護されおり`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `データはすべて暗号化して保護されており`
    - 「保護されおり」 is ungrammatical; the correct form of the te-form + おり is 「保護されており」.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `ja/firefox-ios.xliff` — Toggle label uses a sentence-final verb form inconsistent with the parallel recent-searches toggle.
    - Current: `トレンド検索を表示します`
    - Source: `Show Trending Searches`
    - Suggest: `トレンド検索を表示する`
    - Source "Show Trending Searches" is a toggle title; the sibling toggle Settings.SearchZero.RecentSearches.Toggle uses ～を表示する, so ～します is inconsistent register for a settings label.
- `Send a crash report so Mozilla can fix the problem?` — `ja/firefox-ios.xliff` — Typo: "いただだける" should be "いただける".
    - Current: `ご協力いただだける方は`
    - Source: `Send a crash report so Mozilla can fix the problem?`
    - Suggest: `ご協力いただける方は`
    - Duplicated character "だ" — spelling error in the Japanese text.
- `Deselect All` — `ja/firefox-ios.xliff` — "Deselect All" is rendered as 全選択を解除 ("cancel select-all") rather than deselecting all items.
    - Current: `全選択を解除`
    - Source: `Deselect All`
    - Suggest: `すべての選択を解除`
    - The source means deselect all logins; 全選択 refers to the select-all state, not to all selected items, and pairs poorly with すべて選択 for Select All.

### D. Terminology, register & consistency

- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v153b` — `ja/firefox-ios.xliff` — "Trackers" is translated as 追跡 (the act of tracking) instead of the standard Firefox term トラッカー.
    - Current: `ブロックされた追跡: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ブロックしたトラッカー: %@`
    - The source counts trackers (entities), and Firefox ja consistently uses トラッカー for "tracker"; 追跡 means "tracking".
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v155` — `ja/firefox-ios.xliff` — "Trackers" is translated as 追跡 (the act of tracking) instead of the standard Firefox term トラッカー.
    - Current: `ブロックされた追跡: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ブロックしたトラッカー: %@`
    - The source counts trackers (entities), and Firefox ja consistently uses トラッカー for "tracker"; 追跡 means "tracking".
- `MainMenu.SettingsSection.AccessibilityLabels.Settings.v132` — `ja/firefox-ios.xliff` — "Settings" is rendered as 環境設定 in the accessibility label but 設定 in the visible title on the same screen.
    - Current: `環境設定`
    - Source: `Settings`
    - Suggest: `設定`
    - MainMenu.SettingsSection.Settings.Title.v131 uses 設定 for the same source term; the accessibility label for the same menu item must match.
- `NativeErrorPage.BadCertDomain.AdvancedButton.v149` — `ja/firefox-ios.xliff` — "Advanced" and its paired "Hide advanced" use inconsistent terminology (詳細 vs 上級者向けの情報).
    - Current: `詳細へ進む`
    - Source: `Advanced`
    - Suggest: `詳細情報`
    - The show/hide pair on the same screen should use the same term for "advanced"; here one is 詳細 and the other 上級者向けの情報.
- `Onboarding.Modern.Welcome.ActionTreatmentA.v145` — `ja/firefox-ios.xliff` — "Set as Default Browser" translated as 「デフォルトウェブブラウザーに設定」, inconsistent with the v140 string 「デフォルトブラウザーに設定」.
    - Current: `デフォルトウェブブラウザーに設定`
    - Source: `Set as Default Browser`
    - Suggest: `デフォルトブラウザーに設定`
    - The source is identical to Onboarding.Modern.Welcome.ActionTreatementA.v140 ("Set as Default Browser"), which is translated 「デフォルトブラウザーに設定」; the added 「ウェブ」 is not in the source and creates inconsistency on the same screen.
- `Onboarding.Wallpaper.Action.v114` — `ja/firefox-ios.xliff` — Button label is rendered as a descriptive sentence instead of an imperative action label.
    - Current: `壁紙を設定します`
    - Source: `Set Wallpaper`
    - Suggest: `壁紙を設定`
    - The developer comment says this is a button action ("Set Wallpaper"); Japanese button labels use the noun/imperative form, not the polite declarative "〜します", which reads as a description rather than an action.
- `PrivacyDashboard.Fingerprinters.v155` — `ja/firefox-ios.xliff` — "Fingerprinters" (the trackers themselves) is rendered as the act of fingerprinting rather than as the agents being blocked.
    - Current: `フィンガープリント採取`
    - Source: `Fingerprinters`
    - Suggest: `フィンガープリント採取者`
    - The label counts how many fingerprinters were blocked; Firefox ja uses 「フィンガープリント採取者」 for the blocked entities, consistent with the other item labels (トラッカー, Cookie) which name things, not actions.
- `CreditCard.Settings.AddCard.AccessibilityLabel.v121` — `ja/firefox-ios.xliff` — Button accessibility label translated as a polite sentence instead of a noun label.
    - Current: `カードを追加します`
    - Source: `Add Card`
    - Suggest: `カードを追加`
    - Source "Add Card" is a button label; Japanese button labels use the noun form, consistent with other labels in this file (e.g. カード情報を管理).
- `TermsOfUse.TitleValue2.v147` — `ja/firefox-ios.xliff` — "A note from %@" translated as 「%@ からのメモ」, where メモ (memo/scratch note) is the wrong sense of "note".
    - Current: `%@ からのメモ`
    - Source: `A note from %@`
    - Suggest: `%@ からのお知らせ`
    - In this context "note" means a short message from the vendor, not a personal memo; メモ misleads users on a Terms of Use sheet title.
- `CoverSheet.v24.ETP.Settings.Button` — `ja/firefox-ios.xliff` — "Go to Settings" is rendered as 環境設定 (Preferences) instead of the iOS-standard 設定 used elsewhere in this file.
    - Current: `環境設定を開く`
    - Source: `Go to Settings`
    - Suggest: `設定を開く`
    - Other strings in the same batch translate "settings" as 設定 (e.g. ContextualHints.TabTray.InactiveTabs.CallToAction "設定でオフにする", ContextualHints.SearchBarPlacement.CallToAction "ツールバー設定"); 環境設定 is the desktop Preferences term and is inconsistent on iOS.
- `History` — `ja/firefox-ios.xliff` — "History" is translated as 表示履歴 while the other History strings in the same file use 履歴.
    - Current: `表示履歴`
    - Source: `History`
    - Suggest: `履歴`
    - Source is simply "History" (sync toggle); HistoryPanel.HistoryBackButton.Title translates the same term as 履歴, creating inconsistency.
- `InactiveTabs.TabTray.CloseButtonTitle` — `ja/firefox-ios.xliff` — Button label is translated as a polite sentence rather than a button action label.
    - Current: `休止中のタブをすべて閉じます`
    - Source: `Close All Inactive Tabs`
    - Suggest: `休止中のタブをすべて閉じる`
    - The developer comment says this is a button the user taps; "Close All Inactive Tabs" should be an imperative/noun-style button label, not the polite declarative "閉じます" (other button labels in this batch, e.g. Close Tab "タブを閉じる", use the plain form).
- `Open Settings` — `ja/firefox-ios.xliff` — "Open Settings" is rendered as 「環境設定を開く」 (Preferences), while iOS Japanese uses 設定 for Settings.
    - Current: `環境設定を開く`
    - Source: `Open Settings`
    - Suggest: `設定を開く`
    - On iOS the system app and Firefox's own Settings screen are called 設定; 環境設定 is the macOS/desktop term and is inconsistent with the source term "Settings".
- `SendTo.NotSignedIn.Message` — `ja/firefox-ios.xliff` — "Settings" rendered as 環境設定 instead of 設定, inconsistent with other strings in the same file.
    - Current: `環境設定からログイン`
    - Source: `Please open Firefox, go to Settings and sign in to continue.`
    - Suggest: `設定からログイン`
    - The en-US source says "go to Settings"; on iOS the app's Settings is 設定 (as used in ScanQRCode.PermissionError.Message.v100 and the Search settings string). 環境設定 is the desktop Preferences term.
- `just now` — `ja/firefox-ios.xliff` — "just now" rendered as 直前, which means "immediately before" rather than the relative time "just now".
    - Current: `直前`
    - Source: `just now`
    - Suggest: `たった今`
    - The developer comment says this is a relative time for a tab visited within the last few moments; the standard Japanese rendering is たった今, whereas 直前 reads as "right before (something)".

### E. Typography, punctuation & spacing

- `Bookmarks.EmptyState.Nested.Title.v135` — `ja/firefox-ios.xliff` — Trailing period added to a title that has none in the source.
    - Current: `このフォルダーは空です。`
    - Source: `This folder is empty`
    - Suggest: `このフォルダーは空です`
    - The en-US placeholder title "This folder is empty" has no ending punctuation; other titles in this file (e.g. "ブックマークがありません") also omit it.
- `MainMenu.Account.SigningOut.Title.v154` — `ja/firefox-ios.xliff` — ASCII three-dot ellipsis used instead of the ellipsis character in the source.
    - Current: `ログアウトしています...`
    - Source: `Signing out…`
    - Suggest: `ログアウトしています…`
    - The en-US source uses the single ellipsis character "…"; the Japanese uses three ASCII periods.
- `MainMenu.Submenus.Tools.ReportBrokenSite.Title.v133` — `ja/firefox-ios.xliff` — Ellipsis rendered as three ASCII periods instead of the ellipsis character used in the source.
    - Current: `動作しないサイトを報告...`
    - Source: `Report Broken Site…`
    - Suggest: `動作しないサイトを報告…`
    - The en-US source uses the single ellipsis character "…"; the target substitutes three full stops.
- `MainMenu.ToolsSection.FindInPage.Title.v131` — `ja/firefox-ios.xliff` — Three ASCII periods used instead of the ellipsis character present in the source.
    - Current: `ページ内を検索...`
    - Source: `Find in Page…`
    - Suggest: `ページ内を検索…`
    - The source uses the single ellipsis character "…"; other strings in the same file (e.g. ページを翻訳…) correctly use it.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `ja/firefox-ios.xliff` — Extra space after the Japanese comma before "Internet Archive".
    - Current: `は、 Internet Archive の`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `は、Internet Archive の`
    - A full-width comma should not be followed by an additional space.
- `NativeErrorPage.Wayback.Error.NotFound.v155` — `ja/firefox-ios.xliff` — Missing sentence-final period present in the source.
    - Current: `アーカイブされたバージョンは見つかりませんでした`
    - Source: `No archived version found.`
    - Suggest: `アーカイブされたバージョンは見つかりませんでした。`
    - Source "No archived version found." ends with a period, and sibling strings in this file keep the full stop.
- `WebCompatReporter.IssueSection.CategoryPlaceholder.v154` — `ja/firefox-ios.xliff` — The ellipsis character from the source is rendered as three ASCII periods.
    - Current: `問題の種類を選択してください...`
    - Source: `Choose issue type…`
    - Suggest: `問題の種類を選択してください…`
    - The en-US string uses the ellipsis character '…'; the translation substitutes three full stops.
- `WebCompatReporter.Preview.Data.PrivateBrowsingStatus.v155` — `ja/firefox-ios.xliff` — A full-width colon is followed by an extra space before the following text.
    - Current: `プライベートブラウジングの状態： オンまたはオフ`
    - Source: `Private browsing status: on or off`
    - Suggest: `プライベートブラウジングの状態: オンまたはオフ`
    - Japanese typography does not use a space after a full-width colon; either use a full-width colon with no space or a half-width colon followed by a space.
- `WebView.DocumentLoadingLabel.v137` — `ja/firefox-ios.xliff` — Ellipsis rendered as three ASCII periods instead of the ellipsis character used in the source.
    - Current: `読み込み中...`
    - Source: `Loading…`
    - Suggest: `読み込み中…`
    - The en-US source uses the single ellipsis character “…”; Firefox ja strings consistently keep “…”.
- `WorldCup.HomepageWidget.FTLabel.v151` — `ja/firefox-ios.xliff` — Half-width parentheses used in Japanese text where full-width parentheses are conventional.
    - Current: `(フルタイム)`
    - Source: `(Full Time)`
    - Suggest: `（フルタイム）`
    - Japanese typography convention uses full-width parentheses around full-width (kana) content.
- `HistoryPanel.ClearHistoryButtonTitle` — `ja/firefox-ios.xliff` — Uses three ASCII periods instead of the ellipsis character used in the source.
    - Current: `最近の履歴を消去...`
    - Source: `Clear Recent History…`
    - Suggest: `最近の履歴を消去…`
    - The en-US string ends with the ellipsis character "…"; the Japanese uses "...".
- `Settings.Sync.SigningOut.Title.v154` — `ja/firefox-ios.xliff` — ASCII three dots used instead of the ellipsis character present in the source.
    - Current: `ログアウトしています...`
    - Source: `Signing out…`
    - Suggest: `ログアウトしています…`
    - The en-US source uses the single-character ellipsis "…"; Japanese typography also expects …
- `Menu.SharePageAction.Title` — `ja/firefox-ios.xliff` — Ellipsis rendered as three ASCII periods instead of the ellipsis character used in the source.
    - Current: `ページを共有...`
    - Source: `Share Page With…`
    - Suggest: `ページを共有…`
    - The en-US source uses the single-character ellipsis “…” (Share Page With…); the translation substitutes three full stops.
- `TodayWidget.MoreTabsLabel` — `ja/firefox-ios.xliff` — Ellipsis rendered as three ASCII periods instead of the ellipsis character used in the source.
    - Current: `その他 %d 個...`
    - Source: `+%d More…`
    - Suggest: `その他 %d 個…`
    - The source “+%d More…” uses the single ellipsis character; the translation uses three periods.

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
