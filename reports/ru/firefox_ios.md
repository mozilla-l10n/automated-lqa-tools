# Firefox iOS l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 29 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ru: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (3)

- `QuickAnswers.Tip.Title.v158` — `ru/firefox-ios.xliff` — "Ask Out Loud for Quick Answers" is rendered as "Ask quick questions out loud", swapping the feature name onto the questions.
    - Current: `Задать быстрые вопросы вслух`
    - Source: `Ask Out Loud for Quick Answers`
    - Suggest: `Задайте вопрос вслух и получите быстрые ответы`
    - The source says to ask aloud in order to get Quick Answers (the feature name); the Russian says to ask "quick questions", losing the feature name and changing the meaning.
- `QuickAnswers.Errors.OpenSettings.v158` — `ru/firefox-ios.xliff` — iOS Settings app is rendered "Параметры" instead of the established Apple/Firefox iOS term "Настройки".
    - Current: `Открыть Параметры`
    - Source: `Open Settings`
    - Suggest: `Открыть Настройки`
    - The comment says the button opens the iOS Settings app, which is called «Настройки» in Russian iOS; «Параметры» is the Windows term.
- `QuickAnswers.Errors.PermissionAlertTitle.v158` — `ru/firefox-ios.xliff` — "Settings" rendered as "Параметры" instead of the iOS term "Настройки".
    - Current: `Изменить Параметры для Быстрых ответов`
    - Source: `Change Settings to Use Quick Answers`
    - Suggest: `Изменить Настройки для Быстрых ответов`
    - Refers to the iOS Settings app, localized as «Настройки» on iOS.

### ✅ Fixed since the last run (1)

- `Open & Fill` — `ru/firefox-ios.xliff` — Unwarranted capital letter mid-phrase in Russian.
    - Current: `Открыть и Заполнить`
    - Source: `Open & Fill`
    - Suggest: `Открыть и заполнить`
    - Russian sentence-case rules do not capitalize the second verb; en-US title case must not be copied.

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
| Strings | 1,950 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 23 | **guillemet** |
| ellipsis | `char` 23 | **char** |
| dash | `em` 6, `en` 1 | **em** |
| register | `informal` 83, `formal` 279 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (91)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `NSFaceIDUsageDescription` — `ru/firefox-ios.xliff` — "saved passwords and payment methods" translated as "сохранённым логинам и зашифрованным картам" (saved logins and encrypted cards).
    - Current: `Firefox требует Face ID для доступа к вашим сохранённым логинам и зашифрованным картам.`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Firefox требует Face ID для доступа к вашим сохранённым паролям и способам оплаты.`
    - The source says "passwords" and "payment methods"; the translation says "logins" and "encrypted cards", asserting encryption the source never mentions and naming different data.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 43 |
| 3 | Degraded language (grammar, spelling, terminology) | 45 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `ru/firefox-ios.xliff` — "saved passwords and payment methods" translated as "сохранённым логинам и зашифрованным картам" (saved logins and encrypted cards).
    - Current: `Firefox требует Face ID для доступа к вашим сохранённым логинам и зашифрованным картам.`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Firefox требует Face ID для доступа к вашим сохранённым паролям и способам оплаты.`
    - The source says "passwords" and "payment methods"; the translation says "logins" and "encrypted cards", asserting encryption the source never mentions and naming different data.
- `Alerts.RestoreTabs.Button.Yes.v109` — `ru/firefox-ios.xliff` — Action button rendered as a noun phrase ("Restoring tabs") instead of the imperative "Restore tabs".
    - Current: `Восстановление вкладок`
    - Source: `Restore tabs`
    - Suggest: `Восстановить вкладки`
    - The source is the affirmative action button "Restore tabs"; the Russian verbal noun reads as a process title, not a confirming action.
- `Bookmarks.EmptyState.Root.ButtonTitle.v136` — `ru/firefox-ios.xliff` — "Sign in to Sync" rendered as "Войти в Синхронизацию", treating Sync as a place/product name rather than the verb described in the comment.
    - Current: `Войти в Синхронизацию`
    - Source: `Sign in to Sync`
    - Suggest: `Войти для синхронизации`
    - The developer comment states "Sync" is used as a verb (sign in in order to sync); the Russian reads "log into Synchronization".
- `Bookmarks.Menu.MoreOptionsA11yLabel.v136` — `ru/firefox-ios.xliff` — "More options" translated as "Другие настройки" (other settings) instead of options/actions.
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Другие параметры`
    - The button opens a modal with more actions, not settings; "настройки" wrongly implies app settings.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `ru/firefox-ios.xliff` — "Townland" (a rural land division) is translated as "Городская земля" ("urban land"), the opposite of its meaning.
    - Current: `Городская земля`
    - Source: `Townland`
    - Suggest: `Таунленд`
    - The developer comment states a townland is a land division used in rural areas; "Городская земля" means urban/city land.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `ru/firefox-ios.xliff` — "Part of the %2$@ family" rendered as "Часть семьи" (a human family) instead of "семейства" (product family).
    - Current: `Часть семьи %2$@.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `Часть семейства %2$@.`
    - In en-US "family" refers to a family of products; Russian "семья" means a household/kin group, while the product sense is "семейство".
- `MainMenu.Submenus.Save.AccessibilityLabels.AddToHomeScreen.Subtitle.v132` — `ru/firefox-ios.xliff` — "Home" (the iOS Home screen) is translated as the adverb «Домой» ("homewards").
    - Current: `Домой`
    - Source: `Home`
    - Suggest: `Домашний экран`
    - The developer comment says this refers to the Add to Home screen tool for the iOS Home screen; «Домой» means "to home / homewards", not the Home screen.
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `ru/firefox-ios.xliff` — "Unselected" (state label) is rendered as an action/event "Выбор снят" (selection removed).
    - Current: `Выбор снят`
    - Source: `Unselected`
    - Suggest: `Не выбрано`
    - The accessibility label states the static state that the survey option is not selected, not that a selection was just cleared.
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `ru/firefox-ios.xliff` — Link text placeholder %2$@ (Wayback Machine) is presented as part of the archive's name rather than as a source within the Internet Archive.
    - Current: `в Интернет-архиве %2$@`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `в %2$@ от Internet Archive`
    - Source says the app can look for an earlier version "from the Internet Archive’s Wayback Machine"; the target reads as "in the Internet Archive Wayback Machine" without the possessive relation, making the tappable link text ungrammatical in context.
- `NativeErrorPage.Wayback.Error.Title.v154` — `ru/firefox-ios.xliff` — "Unable to connect" translated as "Попытка соединения не удалась" (the connection attempt failed), a different statement.
    - Current: `Попытка соединения не удалась`
    - Source: `Unable to connect`
    - Suggest: `Не удалось соединиться`
    - Source is a short title stating inability to connect; the target reframes it as a failed attempt and is much longer for a title.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `ru/firefox-ios.xliff` — "have %@ match your device" mistranslated as "wait until %@ matches your device".
    - Current: `или подождите, пока %@ будет соответствовать вашему устройству`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `или позвольте %@ подстроиться под ваше устройство`
    - The source offers the option to let Firefox follow the device theme; the Russian tells the user to wait for Firefox to match the device, which is not what the source says.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `ru/firefox-ios.xliff` — "have %@ match your device" is mistranslated as "wait until %@ matches your device".
    - Current: `или подождите, пока %@ будет соответствовать вашему устройству`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `или позвольте %@ подстроиться под ваше устройство`
    - The source offers the option to let the app follow the device theme, not to wait for it to do so.
- `PrivacyDashboard.HeaderLabel.v155` — `ru/firefox-ios.xliff` — Header is a label under a bold count; Russian phrasing loses the count-caption structure.
    - Current: `На этой неделе заблокированы трекеры`
    - Source: `Trackers blocked this week`
    - Suggest: `Трекеров заблокировано на этой неделе`
    - The developer comment says the number of blocked trackers appears in bold above this text, so the label must read as a caption for that number (genitive), not a standalone sentence.
- `QuickAnswers.Tip.Title.v158` — `ru/firefox-ios.xliff` — "Ask Out Loud for Quick Answers" is rendered as "Ask quick questions out loud", swapping the feature name onto the questions.
    - Current: `Задать быстрые вопросы вслух`
    - Source: `Ask Out Loud for Quick Answers`
    - Suggest: `Задайте вопрос вслух и получите быстрые ответы`
    - The source says to ask aloud in order to get Quick Answers (the feature name); the Russian says to ask "quick questions", losing the feature name and changing the meaning.
- `RelayMask.UseRelayEmailMaskFromKeyboard.v146` — `ru/firefox-ios.xliff` — Singular imperative-neutral "Use email mask" rendered as plural "Используйте псевдонимы" (use email masks).
    - Current: `Используйте псевдонимы эл. почты`
    - Source: `Use email mask`
    - Suggest: `Использовать псевдоним эл. почты`
    - The source is a keyboard hint action label for inserting one mask (singular); the translation is plural and phrased as an instruction to the user, inconsistent with other action labels like "Использовать надёжный пароль".
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `ru/firefox-ios.xliff` — Meaning reversed: %@ is the app name, so it should be "Разрешить %@ открыть?" not "Разрешить открыть %@?"
    - Current: `Разрешить открыть %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Разрешить открытие в %@?`
    - Per the developer comment %@ is the app name (e.g. Firefox); the source asks permission for the app to open a URL, while the Russian asks permission to open the app itself.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `ru/firefox-ios.xliff` — Setting title translated as an imperative instruction instead of a noun phrase naming the option.
    - Current: `Прокрутите, чтобы скрыть вкладку и адресную строку`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Прокрутка скрывает панель вкладок и адресную строку`
    - The en-US "Scroll to Hide Tab and Address Bar" is a toggle label for the autohide feature, not a command to the user to scroll.
- `Settings.Summarize.SummarizePagesTitle.v142` — `ru/firefox-ios.xliff` — "Summarize Pages" (a toggle action) is rendered as the noun phrase "Резюме по страницам", which also conflicts with the section title "Резюме страниц".
    - Current: `Резюме по страницам`
    - Source: `Summarize Pages`
    - Suggest: `Создавать резюме страниц`
    - The source is a verb phrase naming the toggled action; the translation is a noun phrase nearly identical to the section title "Page Summaries" ("Резюме страниц"), making the two indistinguishable.
- `Settings.Translation.AutoTranslate.Footer.v151` — `ru/firefox-ios.xliff` — "your top preferred language" is reduced to "предпочитаемый язык", dropping that it is the highest-ranked preferred language.
    - Current: `на предпочитаемый язык`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `на ваш основной предпочитаемый язык`
    - The source specifies the top language in the preferred-languages list, which matters because the list can contain several languages.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `ru/firefox-ios.xliff` — "share a link on %2$@" (share in the social app) is rendered as "делитесь ссылкой на %2$@", which means sharing a link *to* that app.
    - Current: `когда вы делитесь ссылкой на %2$@`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `когда вы делитесь ссылкой в %2$@`
    - %2$@ is the social media app name; the source means sharing a link within that app, not a link pointing to it. The title string correctly uses "делитесь в %2$@".
- `Summarizer.Error.MissingPageContent.Message.v142` — `ru/firefox-ios.xliff` — "Wait for it to finish" mistranslated as "Дождитесь её завершения" referring to the page rather than loading, and the meaning drifts.
    - Current: `Дождитесь её завершения, затем нажмите, чтобы резюмировать.`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `Дождитесь окончания загрузки, затем нажмите «Резюмировать».`
    - The source tells the user to wait for loading to finish; "дождитесь её завершения" with "её" agreeing with "страница" says to wait for the page to finish/end, which is not what the source says.
- `Summarizer.Error.Unknown.Message.v142` — `ru/firefox-ios.xliff` — "Try again later." is expanded into "Подождите некоторое время и попробуйте снова", adding content not in the source.
    - Current: `Подождите некоторое время и попробуйте снова.`
    - Source: `Error summarizing page. Try again later.`
    - Suggest: `Попробуйте позже.`
    - The source only says to try again later; the translation adds an instruction to wait some time.
- `Summarizer.ToS.InfoPanel.AllowButton.Accessibility.Label.v145` — `ru/firefox-ios.xliff` — "Accept consent" rendered literally as "Принять согласие", which is not idiomatic and does not convey giving consent.
    - Current: `Принять согласие`
    - Source: `Accept consent`
    - Suggest: `Дать согласие`
    - The a11y label is for the allow/accept button; "принять согласие" is meaningless in Russian.
- `Upgrade.Welcome.Description.v114` — `ru/firefox-ios.xliff` — "Same commitment" loses "same" and is rephrased as a contrast about chasing profit.
    - Current: `Обязательство перед людьми, а не погоня за прибылью.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Та же приверженность интересам людей, а не прибыли.`
    - The source stresses continuity ("Same commitment to people over profits"); the Russian drops "same".
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `ru/firefox-ios.xliff` — "Hostnames" translated as "Имена", losing the host-name meaning.
    - Current: `Имена трекеров`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Имена хостов трекеров`
    - The source specifies hostnames of trackers, not merely their names.
- `WebCompatReporter.Preview.Data.PageElements.v155` — `ru/firefox-ios.xliff` — "have been known to cause" is rendered as a factual "вызывают", dropping the hedge.
    - Current: `которые вызывают проблемы с сайтами`
    - Source: `Information about page elements that have been known to cause site issues`
    - Suggest: `которые, как известно, могут вызывать проблемы с сайтами`
    - The source says elements "have been known to cause" issues — a hedged statement; the Russian asserts they do cause issues.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `ru/firefox-ios.xliff` — "match data" mistranslated as "данные о совпадениях" (data about matches/coincidences in the search sense) instead of football match data.
    - Current: `данные о совпадениях`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `данные о матчах`
    - In the World Cup context "match" means a football game (матч), not a text/search match (совпадение).
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `ru/firefox-ios.xliff` — "live" was attached to the wrong element, producing "and other information live" instead of "live match updates".
    - Current: `Получайте обновления по матчам и другую информацию в прямом эфире.`
    - Source: `Get live match updates and more.`
    - Suggest: `Получайте обновления матчей в прямом эфире и не только.`
    - The source qualifies the match updates as live ("live match updates and more"); the translation shifts "в прямом эфире" to modify "другую информацию".
- `WorldCup.HomepageWidget.FollowTeamCard.Title.v151` — `ru/firefox-ios.xliff` — "Keep Tabs on the World Cup" translated literally as browser tabs, which the developer comment explicitly forbids.
    - Current: `Оставить вкладки о ЧМ`
    - Source: `Keep Tabs on the World Cup`
    - Suggest: `Следите за ЧМ`
    - The comment says the idiom means staying informed and must not be translated literally as physical 'tabs'; "Оставить вкладки о ЧМ" means "Leave tabs about the World Cup" and loses the meaning.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `ru/firefox-ios.xliff` — "Get custom wallpaper" rendered as "Загрузить собственные обои" (upload your own wallpaper), changing the action.
    - Current: `Загрузить собственные обои`
    - Source: `Get custom wallpaper`
    - Suggest: `Получить особые обои`
    - The button selects a provided custom wallpaper, not uploads the user's own image; "собственные" plus "загрузить" implies the user supplies the file.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `ru/firefox-ios.xliff` — "Try refreshing" rendered as "обновить страницу" (refresh the page), but the widget refreshes match data, not a page.
    - Current: `Попробуйте обновить страницу через несколько минут.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Попробуйте обновить через несколько минут.`
    - The source says "Try refreshing in a few minutes" about the widget's match data; adding "страницу" asserts a page reload that doesn't exist here.
- `WorldCup.HomepageWidget.SettingsButtonAccessibilityLabel.v151` — `ru/firefox-ios.xliff` — "More options" translated as "Другие настройки" (other settings).
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Другие параметры`
    - The source is "More options" for a panel of actions (Share, Remove), not settings.
- `This action will clear all of your private data, including history from your synced devices.` — `ru/firefox-ios.xliff` — "from your synced devices" rendered as "со всех синхронизированных устройств" (from all synced devices).
    - Current: `включая историю со всех синхронизированных устройств`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `включая историю с ваших синхронизированных устройств`
    - The source does not say "all"; adding "всех" overstates the scope of the deletion.
- `LibraryPanel.History.Title.v138` — `ru/firefox-ios.xliff` — "synced history from other devices" is rendered as just "историю с других устройств", dropping "synced".
    - Current: `включая историю с других устройств`
    - Source: `Deletes history (including synced history from other devices), cookies, and other browsing data.`
    - Suggest: `включая синхронизированную историю с других устройств`
    - The en-US specifies synced history from other devices; the Russian omits that it is synchronized history.
- `AddPass.Error.Message` — `ru/firefox-ios.xliff` — "later" is dropped from "Please try again later".
    - Current: `Пожалуйста, попробуйте снова.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Пожалуйста, попробуйте позже.`
    - The source says "try again later"; the translation omits "later".
- `AddPass.Error.Message` — `ru/firefox-ios.xliff` — "Pass" (Wallet pass/card) is mistranslated as "пароль" (password).
    - Current: `Произошла ошибка при добавлении пароля в Wallet.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Произошла ошибка при добавлении карты в Wallet.`
    - The comment points to Apple Wallet passes (tickets/cards), not passwords; "пароль" means password.
- `AddPass.Error.Title` — `ru/firefox-ios.xliff` — "Pass" (Wallet pass) mistranslated as "пароль" (password).
    - Current: `Не удалось добавить пароль`
    - Source: `Failed to Add Pass`
    - Suggest: `Не удалось добавить карту`
    - The alert is about failing to add a Wallet pass, not a password.
- `ErrorPages.CertWarning.Title` — `ru/firefox-ios.xliff` — "This Connection is Untrusted" translated as "Ваше соединение не защищено" (not secure) — wrong meaning and person.
    - Current: `Ваше соединение не защищено`
    - Source: `This Connection is Untrusted`
    - Suggest: `Это соединение не является доверенным`
    - The source states the connection is untrusted (certificate not trusted), not that it is unencrypted/unprotected.
- `Facebook` — `ru/firefox-ios.xliff` — Brand name "Facebook" transliterated instead of kept as-is.
    - Current: `Фейсбук`
    - Source: `Facebook`
    - Suggest: `Facebook`
    - Facebook is a brand name and should not be transliterated/translated; the source is the tile title "Facebook".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `ru/firefox-ios.xliff` — "Tab pickup" (tabs received from other devices) rendered as "Выбор вкладки" (choosing a tab).
    - Current: `Выбор вкладки`
    - Source: `Tab pickup`
    - Suggest: `Вкладки с других устройств`
    - Per the developer comment, this label marks the cell showing a recent tab synced from another device, not an action of selecting a tab.
- `Keyboard.Shortcuts.ShowBookmarks` — `ru/firefox-ios.xliff` — Adds "все" (all) which is not in the source "Show Bookmarks".
    - Current: `Показать все закладки`
    - Source: `Show Bookmarks`
    - Suggest: `Показать закладки`
    - Source is "Show Bookmarks"; compare Keyboard.Shortcuts.ShowHistory "Show History" → "Показать историю" without "все".
- `Keyboard.Shortcuts.ShowDownloads` — `ru/firefox-ios.xliff` — Adds "все" (all) which is not in the source "Show Downloads".
    - Current: `Показать все загрузки`
    - Source: `Show Downloads`
    - Suggest: `Показать загрузки`
    - Source is "Show Downloads"; the added quantifier is not present in en-US.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `ru/firefox-ios.xliff` — "history synced from other devices" is rendered as "историю с других устройств", dropping the notion of syncing.
    - Current: `включая историю с других устройств`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `включая историю, синхронизированную с других устройств`
    - The source specifies synced history; the translation omits the sync qualifier.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `ru/firefox-ios.xliff` — "more complete and targeted" rendered as "более полный таргетированный" without the conjunction, and the second clause changes meaning from "reduces how much social media companies can see what you do online" to "reduces the amount of information collected by them".
    - Current: `Блокировка этих трекеров уменьшит количество собираемой ими информации о вашей деятельности в Интернете.`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `Блокировка этих трекеров ограничивает возможность социальных сетей отслеживать ваши действия в Интернете.`
    - The source says blocking reduces how much social media companies can see of your online activity; the translation says it reduces the amount of information collected, which is a different claim.
- `SendTo.Error.Title` — `ru/firefox-ios.xliff` — Redundant/tautological rendering: "Нельзя поделиться ссылкой, которой вы пытаетесь поделиться" loses the source meaning of a link that cannot be shared.
    - Current: `Нельзя поделиться ссылкой, которой вы пытаетесь поделиться.`
    - Source: `The link you are trying to share cannot be shared.`
    - Suggest: `Ссылкой, которой вы пытаетесь поделиться, невозможно поделиться.`
    - The English says the link the user is trying to share cannot be shared; the Russian phrasing is circular and reads as nonsense, obscuring the error.
- `SendTo.NoDevicesFound.Message` — `ru/firefox-ios.xliff` — "any other devices" translated as "ни одного устройства", dropping "other".
    - Current: `У вас нет ни одного устройства, подключённого`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `У вас нет других устройств, подключённых`
    - The source says the user has no *other* devices connected; the Russian claims the user has no devices at all.
- `Settings.Disconnect.Button` — `ru/firefox-ios.xliff` — "Disconnect Sync" is rendered without "Sync", making it identical to the plain "Disconnect" button.
    - Current: `Отсоединить`
    - Source: `Disconnect Sync`
    - Suggest: `Отключить синхронизацию`
    - The source distinguishes "Disconnect Sync" (settings button) from "Disconnect" (alert action); both were translated as "Отсоединить", dropping "Sync".
- `Settings.Disconnect.Title` — `ru/firefox-ios.xliff` — "Disconnect Sync?" loses the object "Sync" in the translation.
    - Current: `Отсоединить?`
    - Source: `Disconnect Sync?`
    - Suggest: `Отключить синхронизацию?`
    - The source asks to disconnect Sync; the Russian just says "Disconnect?" with no object, dropping the meaning of what is being disconnected.
- `Settings.Home.Option.JumpBackIn` — `ru/firefox-ios.xliff` — "Jump Back In" (name of the homepage section for resuming browsing) is rendered as a truncated, dangling phrase "Перейти обратно в" that ends with a preposition and names nothing.
    - Current: `Перейти обратно в`
    - Source: `Jump Back In`
    - Suggest: `Возврат к недавнему`
    - The source is a section title meaning "resume where you left off"; the Russian is a literal word-by-word rendering ending in the stranded preposition "в", which is ungrammatical as a standalone title and does not convey the section's meaning.
- `Settings.Passwords.FingerPrintReason.v103` — `ru/firefox-ios.xliff` — "now" is mistranslated as "теперь используйте", turning the prompt into an instruction about a change rather than "use your fingerprint to access passwords now".
    - Current: `Для доступа к паролям теперь используйте отпечаток.`
    - Source: `Use your fingerprint to access passwords now.`
    - Suggest: `Используйте отпечаток пальца, чтобы получить доступ к паролям.`
    - The en-US string is a Touch ID prompt asking the user to authenticate at this moment; the Russian says fingerprint is now (from now on) the way to access passwords.
- `Settings.ShowLinkPreviews.Title` — `ru/firefox-ios.xliff` — "Show Link Previews" is rendered with the imperative/perfective "Показать" instead of the setting label form "Показывать", and singular "ссылки".
    - Current: `Показать предпросмотр ссылки`
    - Source: `Show Link Previews`
    - Suggest: `Показывать предпросмотр ссылок`
    - This is a toggle setting title (cf. Settings.ShowLoginsInAppMenu.Title "Показывать в меню приложения"); the source is plural "Link Previews" describing ongoing behaviour.
- `Show Tour` — `ru/firefox-ios.xliff` — "Show Tour" rendered as "Провести тур" (conduct a tour) instead of showing the tour again.
    - Current: `Провести тур`
    - Source: `Show Tour`
    - Suggest: `Показать тур`
    - The setting shows the on-boarding tour again; "Провести" means to conduct/hold a tour, not display it.
- `Twitter` — `ru/firefox-ios.xliff` — Brand name "Twitter" is transliterated instead of kept as-is.
    - Current: `Твиттер`
    - Source: `Twitter`
    - Suggest: `Twitter`
    - Twitter is a brand/product name for a top-site tile and must not be translated or transliterated.
- `Unsorted Bookmarks` — `ru/firefox-ios.xliff` — "Unsorted Bookmarks" is rendered as "Неподшитые закладки" instead of the standard Firefox term "Несортированные закладки".
    - Current: `Неподшитые закладки`
    - Source: `Unsorted Bookmarks`
    - Suggest: `Несортированные закладки`
    - "Неподшитые" (un-filed/un-stitched) is not the established Russian Firefox term for the Unsorted Bookmarks folder and does not convey "unsorted".
- `TodayWidget.QuickViewGalleryDescriptionV2` — `ru/firefox-ios.xliff` — "Add shortcuts to your open tabs" is translated as adding shortcuts onto the open tabs rather than shortcuts to them.
    - Current: `Добавьте ярлыки на открытые вкладки.`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `Добавьте ярлыки к открытым вкладкам.`
    - The source means creating shortcuts leading to the user's open tabs; "ярлыки на открытые вкладки" reads as placing shortcuts onto the tabs.
- `eHmH1H` — `ru/firefox-ios.xliff` — "Clear Private Tabs" translated as "Закрыть" (close) instead of "Очистить/Удалить".
    - Current: `Закрыть приватные вкладки`
    - Source: `Clear Private Tabs`
    - Suggest: `Очистить приватные вкладки`
    - The source verb is "Clear", not "Close"; closing and clearing are distinct actions in Firefox.

### C. Grammar, agreement & spelling

- `AddressToolbar.GoogleLens.ContextMenu.PhotoLibraryActionTitle.v153` — `ru/firefox-ios.xliff` — "Фото-библиотека" is incorrectly hyphenated; the iOS term is "Фотопленка"/"Медиатека" and Russian compounds with фото- are written solid.
    - Current: `Фото-библиотека`
    - Source: `Photo Library`
    - Suggest: `Медиатека`
    - Russian orthography joins фото- compounds without a hyphen (фотобиблиотека); Apple's iOS term for Photo Library is "Медиатека".
- `Bookmarks.Menu.DeletedBookmark.v131` — `ru/firefox-ios.xliff` — Misspelled participle "Удалёна" (should be "Удалена").
    - Current: `Удалёна «%@»`
    - Source: `Deleted “%@”`
    - Suggest: `Удалена «%@»`
    - The short passive participle of "удалить" is "удалена", without ё. Also the source "Deleted “%@”" is gender-neutral; but at minimum the spelling is wrong.
- `Bookmarks.Menu.EditBookmarkMobileGroupLabel.v154` — `ru/firefox-ios.xliff` — "Mobile" as a folder-group header rendered with masculine adjective "Мобильный" which does not agree with "папки"/bookmarks context.
    - Current: `Мобильный`
    - Source: `Mobile`
    - Suggest: `Мобильные`
    - Header for the group of mobile bookmark folders; paired string uses "МОБИЛЬНЫЕ ЗАКЛАДКИ". A bare masculine singular adjective is ungrammatical as a group label.
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `ru/firefox-ios.xliff` — "поселок" is missing the ё used consistently elsewhere in this file.
    - Current: `Деревня или поселок`
    - Source: `Village or Township`
    - Suggest: `Деревня или посёлок`
    - The file consistently uses ё (удалён, сохранён, СОХРАНЁННЫЕ); "поселок" should be "посёлок".
- `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `ru/firefox-ios.xliff` — Ungrammatical calque "блокируем компании от отслеживания".
    - Current: `автоматически блокируем компании от отслеживания ваших кликов`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `автоматически не даём компаниям следить за вашими кликами`
    - Russian does not use the construction "блокировать кого-либо от чего-либо"; it is a literal calque of the English "block ... from".
- `Onboarding.Modern.Sync.Description.v145` — `ru/firefox-ios.xliff` — Misspelling of the short participle "защищено".
    - Current: `Всё защищёно шифрованием`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Всё защищено шифрованием`
    - The correct spelling is "защищено"; "защищёно" is not a valid form.
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `ru/firefox-ios.xliff` — Awkward/ungrammatical word order: the app name placeholder is inserted as an adjective-like modifier before "обучения".
    - Current: `Закрыть и выйти из %@ обучения`
    - Source: `Close and exit %@ onboarding`
    - Suggest: `Закрыть и выйти из обучения %@`
    - In Russian a proper-name modifier cannot precede the noun without a genitive/appositive construction; "из %@ обучения" reads as broken grammar. The source means "exit the %@ onboarding".
- `Settings.Studies.Title.v148` — `ru/firefox-ios.xliff` — "Feature Studies" rendered with singular "исследование" where the plural "исследования" is required.
    - Current: `Разрешить исследование функций`
    - Source: `Allow Feature Studies`
    - Suggest: `Разрешить исследования функций`
    - The source "Allow Feature Studies" is plural, matching the other Studies strings ("Устанавливать и запускать исследования").
- `Settings.Translation.ToggleFooter.v151` — `ru/firefox-ios.xliff` — Case error: "с панели инструментов и меню" leaves "меню" governed incorrectly, and the preposition is not repeated.
    - Current: `удалить перевод с панели инструментов и меню`
    - Source: `Turn this off to remove translation from the toolbar and menu.`
    - Suggest: `удалить перевод с панели инструментов и из меню`
    - "Remove from the toolbar and menu" requires "из меню"; "с ... меню" is ungrammatical.
- `Summarizer.Footnote.Label.v144` — `ru/firefox-ios.xliff` — Capital letter after a colon mid-sentence: "Примечание: При резюмировании".
    - Current: `Примечание: При резюмировании могут быть ошибки.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Примечание: при резюмировании могут быть ошибки.`
    - In Russian, the word after a colon in this construction is lowercase.
- `WorldCup.GroupPhase.GroupA.Title.v151` — `ru/firefox-ios.xliff` — Group letter A rendered with Cyrillic "А" while all other groups keep Latin letters, breaking consistency.
    - Current: `Группа А`
    - Source: `Group A`
    - Suggest: `Группа A`
    - Groups B–L use the Latin letter; the Cyrillic А is inconsistent and may not match the official group labels.
- `WorldCup.HomepageWidget.RoundPhase.UpcomingLabel.v151` — `ru/firefox-ios.xliff` — "Upcoming" for a single upcoming match is translated in the plural.
    - Current: `Предстоящие`
    - Source: `Upcoming`
    - Suggest: `Предстоящий`
    - The developer comment says the label is for an upcoming match (singular); the plural form does not agree.
- `Use your fingerprint to access Logins now.` — `ru/firefox-ios.xliff` — Word order makes "now" modify "use" oddly and reads as an instruction change.
    - Current: `Для доступа к Логинам теперь используйте отпечаток.`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `Используйте отпечаток пальца для доступа к Логинам.`
    - The source "Use your fingerprint to access Logins now" prompts the user to authenticate now, not to state that fingerprints are now the method ("теперь").
- `Last month` — `ru/firefox-ios.xliff` — Section header uses "Последний месяц" where the standard Russian section label is "Прошлый месяц".
    - Current: `Последний месяц`
    - Source: `Last month`
    - Suggest: `Прошлый месяц`
    - "Last month" as a time-period grouping header is "Прошлый месяц"; "Последний месяц" reads as "the final month".
- `Last week` — `ru/firefox-ios.xliff` — Section header uses nominative "Последняя неделя" where the standard Russian section label is "Прошлая неделя".
    - Current: `Последняя неделя`
    - Source: `Last week`
    - Suggest: `Прошлая неделя`
    - "Last week" as a time-period section header is "Прошлая неделя"; "Последняя неделя" means "the final week".
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `ru/firefox-ios.xliff` — "Фотопленку" is missing the letter ё used elsewhere in the batch and the standard spelling is «Фотоплёнку».
    - Current: `«Фотопленку»`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `«Фотоплёнку»`
    - Inconsistent with the rest of the batch, which uses ё (счёт, веб-сёрфинг).
- `Settings.Appearance.WebsiteDarkModeToggle.Title.v137` — `ru/firefox-ios.xliff` — "Темный" is missing the ё used consistently elsewhere in this group ("тёмный вид", "Тёмная").
    - Current: `Темный режим веб-сайта`
    - Source: `Website Dark Mode`
    - Suggest: `Тёмный режим веб-сайта`
    - Neighbouring strings in the same Appearance section use "тёмный"/"Тёмная" with ё, so this is an inconsistent spelling within one screen.
- `Settings.Home.Option.StartAtHome.Description` — `ru/firefox-ios.xliff` — Missing ё in "вернетесь" inconsistent with the rest of the batch, which uses ё ("четырёх", "посещённые").
    - Current: `когда вернетесь в Firefox`
    - Source: `Choose what you see when you return to Firefox.`
    - Suggest: `когда вернётесь в Firefox`
    - The locale consistently writes ё elsewhere in these strings; "вернетесь" should be "вернётесь".
- `LoginList.DeleteToast.v135` — `ru/firefox-ios.xliff` — Missing 'ё' spelling consistency: 'удален' should be 'удалён' as used elsewhere in the file.
    - Current: `Пароль удален`
    - Source: `Password removed`
    - Suggest: `Пароль удалён`
    - The same file uses 'подключённых' with ё; 'удален' is inconsistent spelling.
- `eqyNJg` — `ru/firefox-ios.xliff` — Singular "Quick Action" rendered as plural "Быстрые действия".
    - Current: `Быстрые действия`
    - Source: `Quick Action`
    - Suggest: `Быстрое действие`
    - The source is singular "Quick Action" (title of the widget), while the neighbouring string eV8mOT correctly uses singular "Тип быстрого действия".
- `w9jdPK` — `ru/firefox-ios.xliff` — Singular "Quick Action" rendered as plural "Быстрые действия".
    - Current: `Быстрые действия`
    - Source: `Quick Action`
    - Suggest: `Быстрое действие`
    - The source label is singular "Quick Action" for the dropdown menu label; the plural form does not match.

### D. Terminology, register & consistency

- `MainMenu.PanelLinkSection.History.Title.v131` — `ru/firefox-ios.xliff` — "History" is rendered as «История» in the menu title but as «Журнал» in the accessibility label for the same item.
    - Current: `История`
    - Source: `History`
    - Suggest: `Журнал`
    - MainMenu.PanelLinkSection.AccessibilityLabels.History.v132 translates the same source term "History" as «Журнал»; Firefox's established Russian term for the History panel is «Журнал», so the two labels for one menu item are inconsistent.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `ru/firefox-ios.xliff` — "your top sites" rendered as the awkward calque "ваш топ сайтов".
    - Current: `ваш топ сайтов`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `ваши топ сайты`
    - "Top Sites" is an established Firefox UI feature name rendered as «Топ сайтов»/«Популярные сайты»; "ваш топ сайтов" is a possessive misconstruction of the feature name.
- `QuickAnswers.Errors.OpenSettings.v158` — `ru/firefox-ios.xliff` — iOS Settings app is rendered "Параметры" instead of the established Apple/Firefox iOS term "Настройки".
    - Current: `Открыть Параметры`
    - Source: `Open Settings`
    - Suggest: `Открыть Настройки`
    - The comment says the button opens the iOS Settings app, which is called «Настройки» in Russian iOS; «Параметры» is the Windows term.
- `QuickAnswers.Errors.PermissionAlertTitle.v158` — `ru/firefox-ios.xliff` — "Settings" rendered as "Параметры" instead of the iOS term "Настройки".
    - Current: `Изменить Параметры для Быстрых ответов`
    - Source: `Change Settings to Use Quick Answers`
    - Suggest: `Изменить Настройки для Быстрых ответов`
    - Refers to the iOS Settings app, localized as «Настройки» on iOS.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `ru/firefox-ios.xliff` — "Trending Searches" is translated as «популярные поисковые запросы» here while the corresponding section title uses «Популярные», creating inconsistency with the parallel Recent Searches toggle.
    - Current: `Показать популярные поисковые запросы`
    - Source: `Show Trending Searches`
    - Suggest: `Показать популярные запросы`
    - The parallel toggle Settings.SearchZero.RecentSearches.Toggle.v146 uses «Показать недавние запросы»; the same term "searches" should be rendered identically in the two adjacent settings toggles.
- `Settings.AIControls.AIPoweredFeaturesSection.PageSummariesSection.Title.v151` — `ru/firefox-ios.xliff` — "Summaries" is rendered as «Резюме» here but as «сводки» in the sibling message on the same screen.
    - Current: `Резюме страниц`
    - Source: `Page Summaries`
    - Suggest: `Сводки страниц`
    - The adjacent string Settings.AIControls.AIPoweredFeaturesSection.PageSummariesSection.Message.v151 translates the same source term "summaries" as «сводки»; the section title and its description on the same screen must use one term.
- `Settings.Search.PrivateSession.Setting.v124` — `ru/firefox-ios.xliff` — "Private Sessions" rendered as «приватных окнах» (private windows), inconsistent with «приватных сеансах» used in the related description strings.
    - Current: `Показывать в приватных окнах`
    - Source: `Show in Private Sessions`
    - Suggest: `Показывать в приватных сеансах`
    - The source says "Private Sessions"; the adjacent descriptions (Settings.Search.PrivateSession.Description.v125, Settings.Search.Suggest.PrivateSession.Description.v125) use «приватных сеансах» on the same screen.
- `Summarizer.Error.RateLimited.Message.v142` — `ru/firefox-ios.xliff` — "Can't handle this one at the moment" rendered in the first person "Не могу справиться с этим сейчас", making the app speak as "I".
    - Current: `Не могу справиться с этим сейчас.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Сейчас не удаётся обработать эту страницу.`
    - The English is impersonal; the Russian first-person form deviates from the locale's impersonal/formal register used in the other error messages in this file.
- `Summarizer.Loading.Label.v142` — `ru/firefox-ios.xliff` — "Summarizing…" translated in the first person singular "Резюмирую…", making the app speak as "I".
    - Current: `Резюмирую…`
    - Source: `Summarizing…`
    - Suggest: `Резюмирование…`
    - The source is a neutral progress label; the Russian first-person form is inconsistent with the formal, impersonal register used elsewhere.
- `Keyboard.Shortcuts.ClearRecentHistory` — `ru/firefox-ios.xliff` — Shortcut action rendered as a noun phrase instead of an imperative verb, inconsistent with the other shortcut labels in the same overlay.
    - Current: `Удаление недавней истории`
    - Source: `Clear Recent History`
    - Suggest: `Очистить недавнюю историю`
    - "Clear Recent History" is an action label; all sibling shortcuts (Добавить закладку, Показать историю, Перезагрузить…) use the imperative form.
- `Send Report` — `ru/firefox-ios.xliff` — "Report" (crash report) rendered as "сообщение" without qualification.
    - Current: `Отправить сообщение`
    - Source: `Send Report`
    - Suggest: `Отправить отчёт`
    - The button accompanies the crash-report dialog; "сообщение" means "message" and loses the report sense.
- `TabTrayButtons.Accessibility.ShowTabs.v106` — `ru/firefox-ios.xliff` — "Show Tabs" translated with imperfective "Отображать" instead of the action label "Показать вкладки".
    - Current: `Отображать вкладки`
    - Source: `Show Tabs`
    - Suggest: `Показать вкладки`
    - This is the accessibility label for a button action; other Show* labels in the same file use "Показать" (e.g. "Показать все вкладки"), making this inconsistent.

### E. Typography, punctuation & spacing

- `Could not add page to Reading List. Maybe it’s already there?` — `ru/firefox-ios.xliff` — Missing comma after the introductory phrase «Может быть».
    - Current: `Может быть она уже там?`
    - Source: `Could not add page to Reading List. Maybe it’s already there?`
    - Suggest: `Может быть, она уже там?`
    - In Russian, «может быть» as a parenthetical requires a comma before the clause it introduces.
- `TopSites.RemovePage.Button` — `ru/firefox-ios.xliff` — En dash/hyphen used where the source and locale convention use an em dash.
    - Current: `Удалить страницу – %@`
    - Source: `Remove page — %@`
    - Suggest: `Удалить страницу — %@`
    - Source uses an em dash (—) and the locale's house dash is the em dash.

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

### Fixed to date (1)

- `Open & Fill` — `ru/firefox-ios.xliff` — fixed 2026-09-21
