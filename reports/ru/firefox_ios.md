# Firefox iOS l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 10 of 1,916 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ru: [android](android.md) · [firefox](firefox.md)

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
| Files | 96 |
| Strings | 1,916 |
| Missing strings | 2 |
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

**2 strings** are not translated yet, concentrated in:

- `ru/firefox-ios.xliff` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 23 | **guillemet** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 6, `en` 1 | **em** |
| register | `informal` 77, `formal` 274 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (76)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 47 |
| 3 | Degraded language (grammar, spelling, terminology) | 24 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

- `CloseTab.ArrivingNotification.title.v133` — `ru/firefox-ios.xliff` — Placeholders swapped in meaning: %1$@ is the app name and %2$@ the tab count, but the translation reads them as count then name.
    - Current: `Закрыто %1$@ вкладок: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ закрыл вкладок: %2$@`
    - Per the developer comment %1$@ is the app name (e.g. Firefox) and %2$@ is the number of tabs; the Russian text places the app name where a number is expected ("Закрыто Firefox вкладок: 5"), producing nonsense.

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSFaceIDUsageDescription` — `ru/firefox-ios.xliff` — "saved passwords and payment methods" is rendered as "сохранённым логинам и зашифрованным картам" (saved logins and encrypted cards).
    - Current: `Firefox требует Face ID для доступа к вашим сохранённым логинам и зашифрованным картам.`
    - Source: `Firefox requires Face ID to access your saved passwords and payment methods.`
    - Suggest: `Для доступа к вашим сохранённым паролям и способам оплаты Firefox требуется Face ID.`
    - The source says "passwords" and "payment methods"; the translation says "logins" and "encrypted cards", changing the content.
- `Alerts.RestoreTabs.Button.Yes.v109` — `ru/firefox-ios.xliff` — Button action "Restore tabs" translated as a noun phrase "Восстановление вкладок" instead of an imperative.
    - Current: `Восстановление вкладок`
    - Source: `Restore tabs`
    - Suggest: `Восстановить вкладки`
    - This is the affirmative action button; the source is an imperative verb phrase, not a noun ("Restoring tabs").
- `Bookmarks.Menu.MoreOptionsA11yLabel.v136` — `ru/firefox-ios.xliff` — "More options" translated as "Другие настройки" (other settings), which is wrong per the comment about a menu of more actions.
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Другие действия`
    - The button opens a modal with more actions, not settings; "настройки" means settings.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `ru/firefox-ios.xliff` — "Townland" (a rural land division in Ireland) is mistranslated as "Городская земля" (urban/city land).
    - Current: `Городская земля`
    - Source: `Townland`
    - Suggest: `Тауленд`
    - The developer comment states a townland is a specific type of land division used in rural areas; "Городская земля" means "city/urban land", the opposite of rural.
- `MainMenu.Account.SignedIn.Description.v141` — `ru/firefox-ios.xliff` — "back up" is translated as «резервируете», which means "reserve/book", not "back up".
    - Current: `Управляйте тем, что вы резервируете и синхронизируете`
    - Source: `Manage what you back up and sync`
    - Suggest: `Управляйте тем, что вы копируете в резервную копию и синхронизируете`
    - The source refers to backing up data; «резервировать» in Russian normally means to reserve, not to create a backup.
- `MainMenu.ToolsSection.AccessibilityLabels.SummarizePage.v142` — `ru/firefox-ios.xliff` — "Summarize Page" (an action) is rendered as a noun phrase "Резюме по странице".
    - Current: `Резюме по странице`
    - Source: `Summarize Page`
    - Suggest: `Обобщить страницу`
    - The source is an imperative action label for the item that summarizes the webpage content; the Russian noun phrase means "summary of the page", not the action, and is inconsistent with other action labels like "Перевести страницу".
- `MainMenu.ToolsSection.SummarizePage.Title.v142` — `ru/firefox-ios.xliff` — "Summarize Page" (an action) is rendered as a noun phrase "Резюме по странице".
    - Current: `Резюме по странице`
    - Source: `Summarize Page`
    - Suggest: `Обобщить страницу`
    - The developer comment says this is the title for the action that will summarize the content of the webpage; the Russian noun phrase names a summary rather than the action, unlike the parallel item "Перевести страницу".
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `ru/firefox-ios.xliff` — "have %@ match your device" is mistranslated as "wait until %@ matches your device".
    - Current: `или подождите, пока %@ будет соответствовать вашему устройству, передав вам контроль`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `или позвольте %@ подстроиться под ваше устройство — контроль в ваших руках`
    - The source means letting the app follow the device theme, not waiting for it; "подождите, пока" changes the meaning.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `ru/firefox-ios.xliff` — "have %@ match your device" is mistranslated as "wait until %@ matches your device".
    - Current: `или подождите, пока %@ будет соответствовать вашему устройству`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `или позвольте %@ подстроиться под ваше устройство`
    - The source means letting the app follow the device theme, not waiting for it; "подождите, пока" introduces a meaning absent from en-US.
- `RelayMask.UseRelayEmailMaskFromKeyboard.v146` — `ru/firefox-ios.xliff` — Keyboard hint rendered as an imperative plural instead of the infinitive singular action label "Use email mask".
    - Current: `Используйте псевдонимы эл. почты`
    - Source: `Use email mask`
    - Suggest: `Использовать псевдоним эл. почты`
    - Source is a singular action label "Use email mask", matching PasswordAutofill's "Использовать сохранённый пароль"; the translation uses an imperative verb and plural noun.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `ru/firefox-ios.xliff` — Translation reverses the meaning: it asks to open the app rather than allow the app to open the URL.
    - Current: `Разрешить открыть %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Разрешить %@ открыть эту ссылку?`
    - %@ is the app name; the source asks permission for the app to open the scanned URL, but the Russian reads "Allow opening <app>?"
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `ru/firefox-ios.xliff` — The words "device Settings" lost the "device" qualifier in the navigation path.
    - Current: `Включите их, выбрав «Настройки» > «Уведомления» > «%2$@»`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Включите их, перейдя в «Настройки» устройства > «Уведомления» > «%2$@»`
    - The source specifies "device Settings" to distinguish iOS Settings from the app's own settings; the translation drops "device".
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `ru/firefox-ios.xliff` — Setting title translated as an imperative instruction instead of a feature name.
    - Current: `Прокрутите, чтобы скрыть вкладку и адресную строку`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Прокрутка для скрытия панели вкладок и адресной строки`
    - The en-US string is the title of a toggle option naming the autohide feature ("Scroll to Hide Tab and Address Bar"), not a command to the user; the Russian imperative "Прокрутите" tells the user to scroll.
- `Settings.Summarize.SummarizePagesTitle.v142` — `ru/firefox-ios.xliff` — "Summarize Pages" (a toggle action) translated as the noun phrase "Резюме по страницам", duplicating the section title.
    - Current: `Резюме по страницам`
    - Source: `Summarize Pages`
    - Suggest: `Создавать резюме страниц`
    - The source is a verb phrase for a toggle that enables summarizing pages; the translation reads as a noun "summaries by pages" and is confusable with the section title "Резюме страниц".
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `ru/firefox-ios.xliff` — «ссылкой на %2$@» wrongly says "a link to <social app>" instead of sharing a link in/on the social app.
    - Current: `когда вы делитесь ссылкой на %2$@`
    - Source: `Spread the word about %1$@ every time you share a link on %2$@.`
    - Suggest: `когда вы делитесь ссылкой в %2$@`
    - In en-US "share a link on %2$@" means sharing via the social media app (e.g. WhatsApp); the Russian «ссылкой на WhatsApp» reads as a link pointing to WhatsApp.
- `Summarizer.Error.MissingPageContent.Message.v142` — `ru/firefox-ios.xliff` — "Wait for it to finish" mistranslated as «Дождитесь её завершения» referring to the page rather than loading, and "hit summarize" loses the button reference.
    - Current: `Дождитесь её завершения, затем нажмите, чтобы резюмировать.`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `Дождитесь окончания загрузки, затем нажмите кнопку резюмирования.`
    - En-US tells the user to wait for loading to finish and then press the summarize button; the Russian says "wait for its completion, then tap to summarize", which is ambiguous and drops the reference to the summarize control.
- `Summarizer.Error.Unknown.Message.v142` — `ru/firefox-ios.xliff` — Adds "wait a while" text not present in the source.
    - Current: `Подождите некоторое время и попробуйте снова.`
    - Source: `Error summarizing page. Try again later.`
    - Suggest: `Попробуйте снова позже.`
    - Source is simply "Try again later."; the Russian invents an extra instruction to wait some time.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `ru/firefox-ios.xliff` — "Hostnames of trackers" is rendered as "Имена трекеров", dropping the host/domain notion.
    - Current: `Имена трекеров, заблокированных на этой странице`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Имена хостов трекеров, заблокированных на этой странице`
    - The source specifies hostnames (домены/имена хостов), not just tracker names.
- `WebCompatReporter.Preview.Data.PageElements.v155` — `ru/firefox-ios.xliff` — "that have been known to cause" is translated as a plain present statement "которые вызывают", asserting the elements always cause issues.
    - Current: `которые вызывают проблемы с сайтами`
    - Source: `Information about page elements that have been known to cause site issues`
    - Suggest: `которые, как известно, могут вызывать проблемы с сайтами`
    - The English hedges with "have been known to cause"; the Russian states it as fact.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `ru/firefox-ios.xliff` — "Follow Along" rendered as "подписаться" (subscribe), losing the meaning of continuing to follow the tournament.
    - Current: `Всё ещё хотите подписаться?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Всё ещё хотите следить за событиями?`
    - The source asks whether the user still wants to follow the World Cup after their team was eliminated, not whether they want to subscribe to something.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `ru/firefox-ios.xliff` — "match data" mistranslated as "данные о совпадениях" (data about matches/coincidences in the search sense) instead of football match data.
    - Current: `данные о совпадениях`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `данные о матче`
    - The widget is about football matches; "совпадение" means a coincidence/search match, not a sports match. Other strings in the same file correctly use "матч".
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `ru/firefox-ios.xliff` — "live match updates" mis-parsed: "в прямом эфире" was attached to the whole sentence including "другую информацию".
    - Current: `Получайте обновления по матчам и другую информацию в прямом эфире.`
    - Source: `Get live match updates and more.`
    - Suggest: `Получайте обновления матчей в прямом эфире и не только.`
    - In the source "live" modifies "match updates"; the Russian word order makes it modify everything and changes the meaning.
- `WorldCup.HomepageWidget.FollowTeamCard.Title.v151` — `ru/firefox-ios.xliff` — "Keep Tabs on the World Cup" translated literally as browser tabs, which the developer comment explicitly forbids.
    - Current: `Оставить вкладки о ЧМ`
    - Source: `Keep Tabs on the World Cup`
    - Suggest: `Следите за ЧМ`
    - The comment states the idiom means staying informed and must not be translated literally as physical 'tabs'; "Оставить вкладки" is meaningless in Russian here.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `ru/firefox-ios.xliff` — "Get custom wallpaper" translated as "Загрузить собственные обои" (upload/download your own wallpaper).
    - Current: `Загрузить собственные обои`
    - Source: `Get custom wallpaper`
    - Suggest: `Получить特special обои`
    - The button selects a provided themed wallpaper, not uploading the user's own image.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `ru/firefox-ios.xliff` — Added "страницу" (page) which is not in the source; the refresh is of the widget data, not a page.
    - Current: `Попробуйте обновить страницу через несколько минут.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Попробуйте обновить через несколько минут.`
    - Source says "Try refreshing in a few minutes" with no mention of a page; the widget refreshes match data.
- `WorldCup.HomepageWidget.SettingsButtonAccessibilityLabel.v151` — `ru/firefox-ios.xliff` — "More options" is translated as "Другие настройки" (Other settings) instead of "Другие параметры/Дополнительные действия".
    - Current: `Другие настройки`
    - Source: `More options`
    - Suggest: `Другие параметры`
    - The source says "More options", and the comment says it opens a panel with more options related to the widget, not settings.
- `This action will clear all of your private data, including history from your synced devices.` — `ru/firefox-ios.xliff` — "your synced devices" rendered as "всех синхронизированных устройств", adding "all" which is not in the source.
    - Current: `включая историю со всех синхронизированных устройств`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `включая историю с ваших синхронизированных устройств`
    - The source says "your synced devices"; "всех" (all) is an added quantifier not present in en-US.
- `AddPass.Error.Message` — `ru/firefox-ios.xliff` — "pass" (Wallet pass/card) is mistranslated as "пароль" (password).
    - Current: `Произошла ошибка при добавлении пароля в Wallet. Пожалуйста, попробуйте снова.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Произошла ошибка при добавлении карты в Wallet. Пожалуйста, попробуйте снова.`
    - The developer comment points to Apple Wallet: "pass" is a Wallet pass (ticket/card), not a password.
- `AddPass.Error.Title` — `ru/firefox-ios.xliff` — "Pass" (Wallet pass) mistranslated as "пароль" (password).
    - Current: `Не удалось добавить пароль`
    - Source: `Failed to Add Pass`
    - Suggest: `Не удалось добавить карту`
    - The 'Add Pass Failed' alert refers to an Apple Wallet pass, not a password.
- `ContextMenu.BookmarkLinkButtonTitle` — `ru/firefox-ios.xliff` — "Bookmark Link" translated without the "link" object, losing the distinction from bookmarking the page.
    - Current: `Добавить в закладки`
    - Source: `Bookmark Link`
    - Suggest: `Добавить ссылку в закладки`
    - The source specifies bookmarking a link URL (per developer comment), while other context-menu items in the same group keep the object ("Копировать ссылку", "Поделиться ссылкой").
- `ErrorPages.CertWarning.Title` — `ru/firefox-ios.xliff` — "This Connection is Untrusted" is rendered as "Your connection is not secure", changing the meaning.
    - Current: `Ваше соединение не защищено`
    - Source: `This Connection is Untrusted`
    - Suggest: `Это соединение не является доверенным`
    - The source says the connection is untrusted (certificate trust), not that it is unsecured; also "This" was changed to "Your".
- `Facebook` — `ru/firefox-ios.xliff` — The brand name Facebook was transliterated instead of kept as-is.
    - Current: `Фейсбук`
    - Source: `Facebook`
    - Suggest: `Facebook`
    - Brand names such as Facebook must remain untranslated; the tile title should read "Facebook".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `ru/firefox-ios.xliff` — "Tab pickup" (picking up a tab from another device) is mistranslated as "Tab selection".
    - Current: `Выбор вкладки`
    - Source: `Tab pickup`
    - Suggest: `Вкладки с других устройств`
    - Per the developer comment, this label identifies the synced-tab cell showing a recent tab from another device, not a tab chooser.
- `Send Report` — `ru/firefox-ios.xliff` — "Send Report" (crash report) rendered as "Отправить сообщение" (send message).
    - Current: `Отправить сообщение`
    - Source: `Send Report`
    - Suggest: `Отправить отчёт`
    - The developer comment says this is the crash dialog button; "сообщение" means message, not report.
- `SendTo.Error.Title` — `ru/firefox-ios.xliff` — Awkward tautological rendering repeats "поделиться" instead of "cannot be shared".
    - Current: `Нельзя поделиться ссылкой, которой вы пытаетесь поделиться.`
    - Source: `The link you are trying to share cannot be shared.`
    - Suggest: `Ссылкой, которой вы пытаетесь поделиться, нельзя поделиться.`
    - The source says the link you are trying to share cannot be shared; the Russian is a circular repetition that reads as an error.
- `SendTo.NoDevicesFound.Message` — `ru/firefox-ios.xliff` — "any other devices" translated as "ни одного устройства", dropping "other".
    - Current: `У вас нет ни одного устройства, подключённого`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `У вас нет других устройств, подключённых`
    - The source specifies other devices besides this one; the translation says the user has no devices at all.
- `Settings.Disconnect.Button` — `ru/firefox-ios.xliff` — "Disconnect Sync" is rendered as just "Отсоединить", dropping the Sync reference.
    - Current: `Отсоединить`
    - Source: `Disconnect Sync`
    - Suggest: `Отключить Синхронизацию`
    - The source specifies disconnecting Sync; the translation omits the object, making it identical to the plain "Disconnect" button string.
- `Settings.Disconnect.Title` — `ru/firefox-ios.xliff` — "Disconnect Sync?" translated without the Sync reference.
    - Current: `Отсоединить?`
    - Source: `Disconnect Sync?`
    - Suggest: `Отключить Синхронизацию?`
    - The alert title in en-US names Sync as the thing being disconnected; the Russian drops it.
- `Settings.DisplayTheme.SystemTheme.SwitchTitle` — `ru/firefox-ios.xliff` — Order of "Light/Dark" is reversed in the Russian translation.
    - Current: `Использовать системную тёмную/светлую тему`
    - Source: `Use System Light/Dark Mode`
    - Suggest: `Использовать системную светлую/тёмную тему`
    - The source is "Use System Light/Dark Mode"; the translation swaps light and dark.
- `Settings.Home.Option.JumpBackIn` — `ru/firefox-ios.xliff` — "Jump Back In" is translated as a dangling preposition phrase that is ungrammatical/incomplete in Russian.
    - Current: `Перейти обратно в`
    - Source: `Jump Back In`
    - Suggest: `Возврат к недавнему`
    - The section title "Jump Back In" means resuming recent tabs; the Russian ends with a stranded preposition "в" and reads as broken text.
- `Settings.Passwords.FingerPrintReason.v103` — `ru/firefox-ios.xliff` — "now" is misattached, changing the meaning to "from now on use your fingerprint" instead of "use your fingerprint to access passwords now".
    - Current: `Для доступа к паролям теперь используйте отпечаток.`
    - Source: `Use your fingerprint to access passwords now.`
    - Suggest: `Используйте отпечаток пальца для доступа к паролям.`
    - The source prompts the user to authenticate now with a fingerprint; the translation reads as an instruction that from now on a fingerprint should be used.
- `Settings.ShowLinkPreviews.Title` — `ru/firefox-ios.xliff` — Toggle title rendered as an imperative "Показать" (show once) instead of the ongoing setting "Показывать", and singular "ссылки" instead of plural.
    - Current: `Показать предпросмотр ссылки`
    - Source: `Show Link Previews`
    - Suggest: `Показывать предпросмотр ссылок`
    - It is a persistent setting for link previews (plural in source), parallel to Settings.ShowLoginsInAppMenu.Title which correctly uses "Показывать".
- `Show Tour` — `ru/firefox-ios.xliff` — "Show Tour" is rendered as "Провести тур" (conduct a tour) instead of showing the onboarding tour again.
    - Current: `Провести тур`
    - Source: `Show Tour`
    - Suggest: `Показать тур`
    - The developer comment says the setting shows the on-boarding screen again; "Провести тур" means to conduct/give a tour, not to display it.
- `Twitter` — `ru/firefox-ios.xliff` — Brand name Twitter transliterated instead of kept in Latin script.
    - Current: `Твиттер`
    - Source: `Twitter`
    - Suggest: `Twitter`
    - Twitter is a brand name and should remain untranslated, as in the source tile title.
- `fxa.signin.ready-to-scan` — `ru/firefox-ios.xliff` — "Ready to Scan" translated as "Scan QR code", changing the meaning.
    - Current: `Сканировать QR-код`
    - Source: `Ready to Scan`
    - Suggest: `Готов к сканированию`
    - Source says "Ready to Scan"; the translation states a different action label than the source.
- `Menu.SharePageAction.Title` — `ru/firefox-ios.xliff` — "Share Page With…" is rendered as "Поделиться через…", dropping the object "Page".
    - Current: `Поделиться через…`
    - Source: `Share Page With…`
    - Suggest: `Поделиться страницей через…`
    - The source explicitly names the page being shared; the translation omits it.
- `eHmH1H` — `ru/firefox-ios.xliff` — "Clear Private Tabs" translated as "Закрыть" (close) instead of "Очистить/Удалить".
    - Current: `Закрыть приватные вкладки`
    - Source: `Clear Private Tabs`
    - Suggest: `Очистить приватные вкладки`
    - The source verb is "Clear", not "Close"; closing and clearing are distinct actions in Firefox.

### C. Grammar, agreement & spelling

- `AddressToolbar.GoogleLens.ContextMenu.PhotoLibraryActionTitle.v153` — `ru/firefox-ios.xliff` — "Фото-библиотека" is misspelled with a hyphen; the iOS standard term is "Медиатека"/"Фотогалерея".
    - Current: `Фото-библиотека`
    - Source: `Photo Library`
    - Suggest: `Медиатека`
    - Russian compounds with "фото" are written solid, not hyphenated; iOS uses "Медиатека" for the photo library.
- `Settings.AppIconSelection.AppIconNames.DarkPurple.Title.v136` — `ru/firefox-ios.xliff` — Missing letter "ё"/inconsistent spelling: "Темно-фиолетовый" should be "Тёмно-фиолетовый" for consistency with "Тёмный", "Зелёный", "Жёлтый".
    - Current: `Темно-фиолетовый`
    - Source: `Dark Purple`
    - Suggest: `Тёмно-фиолетовый`
    - The same file uses ё consistently (Тёмный, Зелёный, Жёлтый); here the ё is dropped, making the spelling inconsistent within the same screen.
- `Bookmarks.Menu.DeletedBookmark.v131` — `ru/firefox-ios.xliff` — Misspelled participle "Удалёна" instead of "Удалена".
    - Current: `Удалёна «%@»`
    - Source: `Deleted “%@”`
    - Suggest: `Удалена «%@»`
    - The short participle of "удалить" is "удалена"; the ё spelling is incorrect.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `ru/firefox-ios.xliff` — "Часть семьи" is the wrong wording for a product family; should be "семейства".
    - Current: `Часть семьи %2$@.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `Часть семейства %2$@.`
    - "Family" here refers to a product family (семейство продуктов), not a human family; "семья" is incorrect terminology in Russian.
- `MainMenu.ToolsSection.AccessibilityLabels.WebsiteDarkMode.Title.v142` — `ru/firefox-ios.xliff` — Missing ё in "Темный" is inconsistent with the ё usage elsewhere in the batch ("займёт").
    - Current: `Темный режим веб-сайта`
    - Source: `Website Dark Mode`
    - Suggest: `Тёмный режим веб-сайта`
    - The locale writes ё (e.g. "займёт всего минуту"), so "Темный" should be "Тёмный" for spelling consistency.
- `Onboarding.Modern.Sync.Description.v145` — `ru/firefox-ios.xliff` — Misspelled participle "защищёно".
    - Current: `Всё защищёно шифрованием`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Всё защищено шифрованием`
    - The short participle is spelled "защищено", not "защищёно".
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `ru/firefox-ios.xliff` — Awkward/ungrammatical word order in the accessibility label for closing onboarding.
    - Current: `Закрыть и выйти из %@ обучения`
    - Source: `Close and exit %@ onboarding`
    - Suggest: `Закрыть и выйти из обучения %@`
    - In Russian the app name placeholder cannot precede the noun as an unmarked modifier; "из %@ обучения" is ungrammatical. The source means "exit the %@ onboarding".
- `Settings.Studies.Title.v148` — `ru/firefox-ios.xliff` — Plural "Feature Studies" rendered as singular "исследование".
    - Current: `Разрешить исследование функций`
    - Source: `Allow Feature Studies`
    - Suggest: `Разрешить исследования функций`
    - The source says "Allow Feature Studies" (plural), matching the related string that uses "исследования".
- `SentFromFirefox.SocialShare.SettingsToggle.Title.v134` — `ru/firefox-ios.xliff` — Toggle title rendered as an imperative command instead of a noun phrase label.
    - Current: `Включите ссылку на скачивание %1$@, когда делитесь в %2$@`
    - Source: `Include %1$@ Download Link on %2$@ Shares`
    - Suggest: `Включать ссылку на скачивание %1$@ при отправке в %2$@`
    - The source "Include %1$@ Download Link on %2$@ Shares" is a setting label, not an instruction to the user; the imperative «Включите» misstates it as a command.
- `WorldCup.GroupPhase.GroupA.Title.v151` — `ru/firefox-ios.xliff` — Group letter A rendered with Cyrillic "А" while Groups B and C keep Latin letters, breaking consistency.
    - Current: `Группа А`
    - Source: `Group A`
    - Suggest: `Группа A`
    - The source uses the Latin letter A as a group identifier; the neighboring strings Group B and Group C keep Latin B and C, so the Cyrillic А here is inconsistent and can sort/display differently.
- `Use your fingerprint to access Logins now.` — `ru/firefox-ios.xliff` — Misplaced adverb changes the meaning: "Для доступа к Логинам теперь используйте отпечаток" reads as "from now on use your fingerprint".
    - Current: `Для доступа к Логинам теперь используйте отпечаток.`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `Используйте отпечаток пальца для доступа к логинам.`
    - The source "now" refers to the present prompt action; the Russian word order turns it into a change-of-behaviour statement, and "Логинам" is needlessly capitalized.
- `Settings.Appearance.WebsiteDarkModeToggle.Title.v137` — `ru/firefox-ios.xliff` — Missing "ё" in "Тёмный", inconsistent with the neighbouring strings that use "тёмный"/"Тёмная".
    - Current: `Темный режим веб-сайта`
    - Source: `Website Dark Mode`
    - Suggest: `Тёмный режим веб-сайта`
    - The adjacent description string uses "тёмный вид" and the theme option uses "Тёмная"; this string spells it without ё, an inconsistent spelling on the same screen.
- `Settings.Home.Option.StartAtHome.Description` — `ru/firefox-ios.xliff` — Missing diaeresis in "вернетесь".
    - Current: `когда вернетесь в Firefox`
    - Source: `Choose what you see when you return to Firefox.`
    - Suggest: `когда вернётесь в Firefox`
    - Other strings in this batch consistently use ё (тёмную, четырёх, посещённые); spelling should be вернётесь.
- `SyncState.Offline.Title` — `ru/firefox-ios.xliff` — Misspelling of "офлайн".
    - Current: `Синхронизация оффлайн`
    - Source: `Sync is offline`
    - Suggest: `Синхронизация офлайн`
    - The normative Russian spelling per the orthographic dictionary is "офлайн" with one "ф".
- `Open & Fill` — `ru/firefox-ios.xliff` — Second word incorrectly capitalized in Russian.
    - Current: `Открыть и Заполнить`
    - Source: `Open & Fill`
    - Suggest: `Открыть и заполнить`
    - Russian does not use English-style title case; "Заполнить" should be lowercase mid-sentence.
- `TodayWidget.QuickViewGalleryDescriptionV2` — `ru/firefox-ios.xliff` — Wrong preposition/case: "ярлыки на открытые вкладки" should be "ярлыки открытых вкладок".
    - Current: `Добавьте ярлыки на открытые вкладки.`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `Добавьте ярлыки открытых вкладок.`
    - The source means "Add shortcuts to your open tabs" i.e. shortcuts leading to open tabs; the Russian "ярлыки на открытые вкладки" is ungrammatical — the correct construction is genitive "ярлыки открытых вкладок".
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

- `MainMenu.PanelLinkSection.AccessibilityLabels.History.v132` — `ru/firefox-ios.xliff` — "History" is rendered as «Журнал» in the accessibility label but as «История» in the visible title for the same menu item.
    - Current: `Журнал`
    - Source: `History`
    - Suggest: `История`
    - MainMenu.PanelLinkSection.History.Title.v131 translates the same source term "History" as «История»; the accessibility label for the same control must match.
- `Settings.Search.PrivateSession.Setting.v124` — `ru/firefox-ios.xliff` — "Private Sessions" rendered as "приватных окнах" (private windows), inconsistent with the other strings on the same screen that use "приватных сеансах".
    - Current: `Показывать в приватных окнах`
    - Source: `Show in Private Sessions`
    - Suggest: `Показывать в приватных сеансах`
    - Source says "Private Sessions"; sibling strings Settings.Search.PrivateSession.Description.v125 and Settings.Search.Suggest.PrivateSession.Description.v125 translate it as "приватных сеансах", so this label is inconsistent and says "windows" instead of "sessions".
- `Summarizer.Error.RateLimited.Message.v142` — `ru/firefox-ios.xliff` — First-person «Не могу справиться» is out of register for an app error message.
    - Current: `Не могу справиться с этим сейчас.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Не удалось обработать эту страницу сейчас.`
    - En-US "Can’t handle this one at the moment" is impersonal; Russian UI convention avoids the app speaking in first person singular.
- `Logins.WelcomeView.TurnOnAutoFill` — `ru/firefox-ios.xliff` — Button label uses imperative plural verb form instead of the noun/infinitive form used for buttons.
    - Current: `Включите автозаполнение`
    - Source: `Turn on AutoFill`
    - Suggest: `Включить автозаполнение`
    - "Turn on AutoFill" is a button title; Russian UI buttons use the infinitive ("Включить"), not the addressed imperative "Включите", which reads as an instruction to the user.
- `Unsorted Bookmarks` — `ru/firefox-ios.xliff` — "Unsorted Bookmarks" translated as "Неподшитые закладки", which is not the Russian Firefox term.
    - Current: `Неподшитые закладки`
    - Source: `Unsorted Bookmarks`
    - Suggest: `Несортированные закладки`
    - "Неподшитые" (unfiled/unstitched) is not standard; Firefox ru uses "Несортированные закладки" for the unsorted bookmarks folder.

### E. Typography, punctuation & spacing

- `Settings.Search.Suggest.AddressBarSetting.Title.v124` — `ru/firefox-ios.xliff` — Hyphen used where a Russian dash is required between clauses.
    - Current: `Адресная строка - Firefox Suggest`
    - Source: `Address bar - Firefox Suggest`
    - Suggest: `Адресная строка — Firefox Suggest`
    - Russian typography uses an em dash surrounded by spaces, not a hyphen, in this separator position.
- `Summarizer.Footnote.Label.v144` — `ru/firefox-ios.xliff` — Capital letter after a colon mid-sentence.
    - Current: `Примечание: При резюмировании могут быть ошибки.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Примечание: при резюмировании могут быть ошибки.`
    - In Russian, a lowercase letter follows a colon when the following clause is not a quotation or proper noun.
- `Could not add page to Reading List. Maybe it’s already there?` — `ru/firefox-ios.xliff` — Missing comma after the introductory phrase "Может быть".
    - Current: `Может быть она уже там?`
    - Source: `Could not add page to Reading List. Maybe it’s already there?`
    - Suggest: `Может быть, она уже там?`
    - In Russian, «может быть» as a parenthetical requires a comma before the following clause.
- `TopSites.RemovePage.Button` — `ru/firefox-ios.xliff` — Em dash of the source replaced with an en dash.
    - Current: `Удалить страницу – %@`
    - Source: `Remove page — %@`
    - Suggest: `Удалить страницу — %@`
    - The source uses an em dash (—); the Russian uses an en dash (–), deviating from the source typography.
- `Well, this is embarrassing.` — `ru/firefox-ios.xliff` — Terminal period from the source sentence is missing.
    - Current: `Ой, вот ведь незадача`
    - Source: `Well, this is embarrassing.`
    - Suggest: `Ой, вот ведь незадача.`
    - The en-US title ends with a period; the translation drops it.

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
