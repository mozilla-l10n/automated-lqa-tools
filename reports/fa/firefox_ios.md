# Firefox iOS l10n QA — fa

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-17 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1 of 547 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fa: [android](android.md)

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
| Files | 22 |
| Strings | 547 |
| Missing strings | 1,403 |
| Obsolete strings | 0 |
| Files absent from the locale | 75 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**1,403 strings** are not translated yet, concentrated in:

- `fa/firefox-ios.xliff` — 182
- `Shared/Supporting Files/en-US.lproj/Onboarding.strings` — 158
- `Shared/Supporting Files/en-US.lproj/MainMenu.strings` — 151
- `Shared/Supporting Files/en-US.lproj/Settings.strings` — 151
- `Shared/Supporting Files/en-US.lproj/WorldCup.strings` — 73
- `Shared/Supporting Files/en-US.lproj/WebCompatReporter.strings` — 52
- `Shared/Supporting Files/en-US.lproj/EditAddress.strings` — 48
- `Shared/Supporting Files/en-US.lproj/EnhancedTrackingProtection.strings` — 43
- `Shared/Supporting Files/en-US.lproj/AppIconSelection.strings` — 42
- `Shared/Supporting Files/en-US.lproj/Bookmarks.strings` — 32
- `Shared/Supporting Files/en-US.lproj/NativeErrorPage.strings` — 32
- `Shared/Supporting Files/en-US.lproj/Translations.strings` — 31

**Files absent from the locale:**

- `Extensions/ActionExtension/en-US.lproj/InfoPlist.strings`
- `Shared/Supporting Files/en-US.lproj/ActivityStream.strings`
- `Shared/Supporting Files/en-US.lproj/AddressToolbar.strings`
- `Shared/Supporting Files/en-US.lproj/Alert.strings`
- `Shared/Supporting Files/en-US.lproj/Alerts.strings`
- `Shared/Supporting Files/en-US.lproj/AppIconSelection.strings`
- `Shared/Supporting Files/en-US.lproj/BiometricAuthentication.strings`
- `Shared/Supporting Files/en-US.lproj/Bookmarks.strings`
- `Shared/Supporting Files/en-US.lproj/BottomSheet.strings`
- `Shared/Supporting Files/en-US.lproj/Camera.strings`
- `Shared/Supporting Files/en-US.lproj/ContextualHints.strings`
- `Shared/Supporting Files/en-US.lproj/CredentialProvider.strings`
- `Shared/Supporting Files/en-US.lproj/Credentials.strings`
- `Shared/Supporting Files/en-US.lproj/CustomizeFirefoxHome.strings`
- `Shared/Supporting Files/en-US.lproj/DisplayCard.strings`
- `Shared/Supporting Files/en-US.lproj/Edit Card.strings`
- `Shared/Supporting Files/en-US.lproj/EditAddress.strings`
- `Shared/Supporting Files/en-US.lproj/EditCard.strings`
- `Shared/Supporting Files/en-US.lproj/EngagementNotification.strings`
- `Shared/Supporting Files/en-US.lproj/EnhancedTrackingProtection.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1 | **guillemet** |
| ellipsis | `char` 5 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (88)

> **Reads as a deliberate edit (7).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `fa/firefox-ios.xliff` — "tapping" rendered as "tapping and holding", and "book plus icon" loses the plus.
    - Current: `با تپ کردن و نگه داشتن آیکون کتاب`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `با تپ کردن آیکون کتاب به‌همراه علامت مثبت`
    - The source says simply "tapping the book plus icon"; the translation instructs a tap-and-hold gesture, giving the user wrong instructions.
- `Settings.Disconnect.Body` — `fa/firefox-ios.xliff` — The qualifier "browsing data" is rendered as just "any data", widening the claim about what is not deleted.
    - Current: `هیچ گونه اطلاعاتی از روی دستگاه شما پاک نخواهد کرد`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `هیچ‌گونه اطلاعات مرور شما را از روی این دستگاه پاک نخواهد کرد`
    - en-US says it won’t delete any of your browsing data on this device; the translation drops "browsing", asserting that no data at all is deleted.
- `Settings.SendUsage.Message` — `fa/firefox-ios.xliff` — The translation drops "strives to" and "provide", asserting Mozilla only collects data that helps improve Firefox.
    - Current: `موزیلا تنها اطلاعاتی که به بهینه‌سازی فایرفاکس برای همه کمک می‌کند را جمع‌آوری می‌کند.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `موزیلا تلاش می‌کند تنها اطلاعاتی را جمع‌آوری کند که برای ارائه و بهبود فایرفاکس برای همه لازم است.`
    - The source is a hedged statement of effort ("strives to only collect what we need"); the translation turns it into an unqualified claim about the product's data collection.
- `Settings.WebsiteData.ConfirmPrompt` — `fa/firefox-ios.xliff` — "will clear" weakened to "can clear" (می‌تواند حذف کند).
    - Current: `این اقدام می تواند تمام اطلاعات پایگاه اینترنتی را حذف کند`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `این اقدام تمام اطلاعات پایگاه اینترنتی را حذف می‌کند`
    - The source states the action will clear all website data; the target says it may/can, changing the certainty of the stated behaviour.
- `Well, this is embarrassing.` — `fa/firefox-ios.xliff` — "this is embarrassing" is rendered as "we are very sorry", an apology the source does not make.
    - Current: `راستش، بسیار متاسفیم.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `خب، این شرم‌آور است.`
    - The en-US expresses embarrassment about the situation, not an apology from the product.
- `Logins will be permanently removed.` — `fa/firefox-ios.xliff` — Future-tense warning rendered as past tense, telling the user the deletion already happened.
    - Current: `ورود‌ها برای همیشه حذف شد.`
    - Source: `Logins will be permanently removed.`
    - Suggest: `ورودها برای همیشه حذف خواهند شد.`
    - The en-US is a warning prompt before deletion ("will be permanently removed"); the Persian past tense «حذف شد» states the removal is already done.
- `Logins will be removed from all connected devices.` — `fa/firefox-ios.xliff` — Future tense rendered as past tense and "connected devices" reduced to "all devices".
    - Current: `ورود‌ها بر روی تمامی دستگاه‌ها حذف شد.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `ورودها از همه دستگاه‌های متصل حذف خواهند شد.`
    - Source is a pre-deletion warning: "will be removed from all connected devices"; the translation uses past tense and drops "connected".

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 41 |
| 3 | Degraded language (grammar, spelling, terminology) | 38 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Use your fingerprint to access Logins now.` — `fa/firefox-ios.xliff` — "Logins" translated as "ورود" (act of logging in) rather than saved logins.
    - Current: `استفاده از اثرانگشت برای دسترسی به ورود.`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `برای دسترسی به ورودها از اثر انگشت خود استفاده کنید.`
    - The source refers to the saved Logins list (rendered elsewhere in this batch as "ورودهای ذخیره شده"); the singular "ورود" reads as the action of logging in.
- `DefaultBrowserOnboarding.Description2` — `fa/firefox-ios.xliff` — Instruction step mistranslated as "Set as default browser" instead of "Tap Default Browser App".
    - Current: `۲. تبدیل به مرورگر پیش‌فرض`
    - Source: `2. Tap Default Browser App`
    - Suggest: `۲. روی «مرورگر پیش‌فرض» ضربه بزنید`
    - The source is a step telling the user to tap the "Default Browser App" setting; the translation instead duplicates the menu label "Set as Default Browser", losing the action instruction.
- `AddPass.Error.Message` — `fa/firefox-ios.xliff` — "pass" (Wallet pass) is translated as "گذرواژه" (password).
    - Current: `یک خطا هنگام اضافه کردن گذرواژه به Wallet رُخ داد.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `یک خطا هنگام اضافه کردن کارت (pass) به Wallet رُخ داد.`
    - The comment points to Apple Wallet: a "pass" is a Wallet pass/ticket, not a password ("گذرواژه").
- `AddPass.Error.Title` — `fa/firefox-ios.xliff` — "Add Pass" rendered as adding a password instead of a Wallet pass.
    - Current: `اضافه کردن گذرواژه شکست خورد`
    - Source: `Failed to Add Pass`
    - Suggest: `اضافه کردن کارت (pass) شکست خورد`
    - Per the developer comment this is the Apple Wallet 'Add Pass Failed' alert; "گذرواژه" means password.
- `CoverSheet.v24.ETP.Description` — `fa/firefox-ios.xliff` — The ETP description is mistranslated: it tells the user they stop ads "from around themselves", drops "even more" and leaves "Strict" untranslated/unlocalized.
    - Current: `حفاظت از ردیابی پیشرفته داخلی به شما کمک می کند تبلیغات را از اطراف خود متوقف کنید. برای مسدود کردن ردیابها ، تبلیغات و پنجره های بیشتر ، Strict را روشن کنید.`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `«حفاظت پیشرفته در برابر ردیابی» داخلی کمک می‌کند تبلیغات شما را در وب دنبال نکنند. برای مسدود کردن ردیاب‌ها، تبلیغات و پنجره‌های بازشوی بیشتر، حالت «سخت‌گیرانه» را روشن کنید.`
    - Source says ETP helps stop ads from following you around and to turn on Strict to block even more trackers, ads and popups; the Persian says the user stops ads "from around themselves" and omits "popups" as a distinct item (پنجره‌های بازشو), while "Strict" is the name of a setting that is localized elsewhere.
- `Downloads.CancelDialog.Title` — `fa/firefox-ios.xliff` — "Cancel Download" is rendered as "لغو کنسل" ("cancel cancel"), losing the word "download".
    - Current: `لغو کنسل`
    - Source: `Cancel Download`
    - Suggest: `لغو دریافت`
    - The source title is "Cancel Download"; the noun "download" was replaced by a second word meaning "cancel".
- `ErrorPages.VisitOnce.Button` — `fa/firefox-ios.xliff` — "Visit site anyway" rendered awkwardly as "visit the website in any case".
    - Current: `بازدید از پایگاه اینترنتی در هر صورتی`
    - Source: `Visit site anyway`
    - Suggest: `با این حال از پایگاه اینترنتی بازدید شود`
    - "در هر صورتی" is ungrammatical (should be "در هر صورت") and the button label does not read as an action.
- `ExternalLink.AppStore.GenericConfirmationTitle` — `fa/firefox-ios.xliff` — Question rendered as "Are you opening this link in an external app?" instead of an offer to open it.
    - Current: `این پیوند را در برنامه خارجی باز می‌کنید؟`
    - Source: `Open this link in external app?`
    - Suggest: `این پیوند در برنامه خارجی باز شود؟`
    - Source asks for confirmation to open the link ("Open this link in external app?"), as rendered correctly in the sibling App Store string.
- `HistoryPanel.ClearHistoryMenuOptionTheLastHour` — `fa/firefox-ios.xliff` — "The Last Hour" translated as "ساعت قبل" (the previous hour) rather than "ساعت گذشته".
    - Current: `ساعت قبل`
    - Source: `The Last Hour`
    - Suggest: `ساعت گذشته`
    - The option clears history for the last hour; "ساعت قبل" reads as "the hour before" rather than the past hour.
- `HistoryPanel.EmptyState.Title` — `fa/firefox-ios.xliff` — Adds "بیشتر" (most) and uses an object marker, changing "websites you've visited recently" into "websites you have visited most recently" with broken syntax.
    - Current: `پایگاه‌های اینترنتی را که اخیرا بیشتر بازدید کرده‌اید در اینجا نمایش داده می‌شوند.`
    - Source: `Websites you’ve visited recently will show up here.`
    - Suggest: `پایگاه‌های اینترنتی که اخیراً بازدید کرده‌اید در اینجا نمایش داده می‌شوند.`
    - The source says simply "Websites you’ve visited recently"; "بیشتر" adds a frequency claim not in the source, and the accusative "را" is ungrammatical with the passive verb.
- `Hotkeys.CloseTab.DiscoveryTitle` — `fa/firefox-ios.xliff` — "Close Tab" is rendered as the noun phrase "closed tabs" instead of the action of closing the current tab.
    - Current: `زبانه‌های بسته شده`
    - Source: `Close Tab`
    - Suggest: `بستن زبانه`
    - The source is the command "Close Tab" (closing the current tab, per the comment); the translation means "closed tabs".
- `Light` — `fa/firefox-ios.xliff` — "Light" (light theme) is translated as "نور" (light/ray) instead of the theme name "روشن".
    - Current: `نور`
    - Source: `Light`
    - Suggest: `روشن`
    - The developer comment says this is the Light theme setting in Reading View; "نور" means the physical light/ray, not the light theme.
- `Logins` — `fa/firefox-ios.xliff` — "Logins" (saved credentials) rendered as "ورود" (the act of logging in).
    - Current: `ورود`
    - Source: `Logins`
    - Suggest: `ورودها`
    - The comment describes a toggle for syncing saved logins; the singular verbal noun "ورود" names the act of signing in, not the stored logins.
- `Menu.AddToReadingList.Confirm` — `fa/firefox-ios.xliff` — "Reading List" is rendered as "فهرست پخش" (playlist) instead of "فهرست خواندن".
    - Current: `به فهرست پخش اضافه شد`
    - Source: `Added To Reading List`
    - Suggest: `به فهرست خواندن اضافه شد`
    - The source and comment refer to the reading list; "فهرست پخش" means playlist, a different feature.
- `Menu.Copy.Title` — `fa/firefox-ios.xliff` — "Copy Address" translated as "برداشت آدرس" instead of "رونوشت آدرس" (copy).
    - Current: `برداشت آدرس`
    - Source: `Copy Address`
    - Suggest: `رونوشت آدرس`
    - The button copies the URL; "برداشت" means take/withdraw, and the same file uses "رونوشت" for copy in Menu.CopyURL.Confirm.
- `Menu.PasteAndGo.Title` — `fa/firefox-ios.xliff` — "Paste & Go" is translated as "برداشتن و چسباندن" (cut/copy and paste), losing the "Go" action.
    - Current: `برداشتن و چسباندن`
    - Source: `Paste & Go`
    - Suggest: `چسباندن و رفتن`
    - The comment says the button pastes and navigates to a URL; the translation says "take and paste" instead.
- `Menu.TrackingProtectionBlockedContent.Title` — `fa/firefox-ios.xliff` — "Tracking content" rendered as the imperative/verbal phrase "tracking content" (following content) instead of the noun phrase "tracker content".
    - Current: `دنبال کردن محتوا`
    - Source: `Tracking content`
    - Suggest: `محتوای ردیاب`
    - The source is a noun phrase naming a category of blocked content (content that contains trackers); the Persian says "following/tracking the content", i.e. an action performed on content, which reverses the relationship.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `fa/firefox-ios.xliff` — The clause "how much social media companies can see what you do online" drops the "what you do online" element, changing the claim to what companies "seek to see".
    - Current: `باعث کاهش میزان چیزی شود که شبکه های اجتماعی در پی دیدن آن هستند`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `باعث کاهش میزان دیدِ شبکه‌های اجتماعی از فعالیت‌های آنلاین شما شود`
    - The source states blocking reduces how much social media companies can see of your online activity; the Persian says it reduces the amount of "what they seek to see", losing the online-activity object and the ability sense.
- `PhotonMenu.close` — `fa/firefox-ios.xliff` — The "Close" button is translated as the adjective "بسته" (closed) instead of the verb "بستن".
    - Current: `بسته`
    - Source: `Close`
    - Suggest: `بستن`
    - Developer comment says it is a button for closing the menu; Persian button labels use the infinitive «بستن», while «بسته» means "closed/package".
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `fa/firefox-ios.xliff` — "tapping" rendered as "tapping and holding", and "book plus icon" loses the plus.
    - Current: `با تپ کردن و نگه داشتن آیکون کتاب`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `با تپ کردن آیکون کتاب به‌همراه علامت مثبت`
    - The source says simply "tapping the book plus icon"; the translation instructs a tap-and-hold gesture, giving the user wrong instructions.
- `Search.ThirdPartyEngines.AddSuccess` — `fa/firefox-ios.xliff` — Success confirmation "Added Search engine!" translated as an action label "Add search engine".
    - Current: `افزودن موتور جست‌وجو`
    - Source: `Added Search engine!`
    - Suggest: `موتور جست‌وجو افزوده شد!`
    - The source is a success message stating the engine was added; the translation reads as an infinitive/action "adding a search engine", losing the completed state.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `fa/firefox-ios.xliff` — "title or URL" translated as "title and URL".
    - Current: `با این عنوان و آدرس`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `با این عنوان یا آدرس`
    - The source's disjunction (either matching title or matching URL) is turned into a conjunction, changing the condition described.
- `SendTo.NoDevicesFound.Message` — `fa/firefox-ios.xliff` — "this Firefox Account" reduced to "Firefox", dropping the account reference.
    - Current: `متصل به فایرفاکس برای همگام‌سازی ندارید`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `متصل به این حساب فایرفاکس برای همگام‌سازی ندارید`
    - The source refers to devices connected to this Firefox Account, not to Firefox generally.
- `SentTab_TabArrivingNotification_NoDevice_body` — `fa/firefox-ios.xliff` — Singular "another device" rendered as plural "other devices".
    - Current: `از دستگاه‌های دیگری رسیده است`
    - Source: `New tab arrived from another device.`
    - Suggest: `از دستگاه دیگری رسیده است`
    - The source says the tab arrived from another (single) device.
- `Settings.AddCustomEngine.URLPlaceholder` — `fa/firefox-ios.xliff` — "Query" is mistranslated as "رکورد جست‌وجو" (search record).
    - Current: `رکورد جست‌وجو را با %s جایگزین کنید`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `عبارت جست‌وجو را با %s جایگزین کنید`
    - The source asks the user to replace the query string with %s; "رکورد" (record) is not the query term.
- `Settings.CopyAppVersion.Title` — `fa/firefox-ios.xliff` — "Copied to clipboard" is rendered as an infinitive/action phrase "pouring into clipboard" rather than a completed confirmation.
    - Current: `ریختن داخل کلیپ بورد`
    - Source: `Copied to clipboard`
    - Suggest: `در حافظهٔ موقت رونوشت شد`
    - The source is a confirmation that the version was copied; the Persian uses "ریختن" (pouring) as an action noun, not stating the copy happened.
- `Settings.Disconnect.Body` — `fa/firefox-ios.xliff` — The qualifier "browsing data" is rendered as just "any data", widening the claim about what is not deleted.
    - Current: `هیچ گونه اطلاعاتی از روی دستگاه شما پاک نخواهد کرد`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `هیچ‌گونه اطلاعات مرور شما را از روی این دستگاه پاک نخواهد کرد`
    - en-US says it won’t delete any of your browsing data on this device; the translation drops "browsing", asserting that no data at all is deleted.
- `Settings.DisplayTheme.SwitchMode.SectionHeader` — `fa/firefox-ios.xliff` — "Switch Mode" rendered as "حالت تغییر" reverses the head noun (mode of change instead of switching mode).
    - Current: `حالت تغییر`
    - Source: `Switch Mode`
    - Suggest: `حالت تغییر زمینه`
    - The section header controls how the theme switches; the Persian phrase inverts the noun relation and reads as "change mode" ambiguously.
- `Settings.OpenWith.SectionName` — `fa/firefox-ios.xliff` — "Mail App" left partly untranslated as the English word "Mail".
    - Current: `برنامه Mail`
    - Source: `Mail App`
    - Suggest: `برنامهٔ پست الکترونیکی`
    - "Mail" here is a generic app category, not a brand to keep in English; elsewhere in the same screen the locale uses «پست‌الکترونیکی».
- `Settings.SendUsage.Message` — `fa/firefox-ios.xliff` — The translation drops "strives to" and "provide", asserting Mozilla only collects data that helps improve Firefox.
    - Current: `موزیلا تنها اطلاعاتی که به بهینه‌سازی فایرفاکس برای همه کمک می‌کند را جمع‌آوری می‌کند.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `موزیلا تلاش می‌کند تنها اطلاعاتی را جمع‌آوری کند که برای ارائه و بهبود فایرفاکس برای همه لازم است.`
    - The source is a hedged statement of effort ("strives to only collect what we need"); the translation turns it into an unqualified claim about the product's data collection.
- `Settings.ShowLinkPreviews.Title` — `fa/firefox-ios.xliff` — "Show Link Previews" is rendered with "پخش" (play/broadcast) instead of "نمایش" (show).
    - Current: `پخش پیش نمایش پیوند`
    - Source: `Show Link Previews`
    - Suggest: `نمایش پیش‌نمایش پیوندها`
    - The source means to display link previews; «پخش» means to play/broadcast, which is the wrong verb and inconsistent with «نمایش» used elsewhere in this file.
- `Settings.TrackingProtection.ProtectionCellFooter` — `fa/firefox-ios.xliff` — The translation says it helps stop "tracking of ads in your browsing" instead of stopping advertisers from tracking your browsing.
    - Current: `به جلوگیری از ردیابی تبلیغات در مرور شما کمک می کند`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `به جلوگیری از ردیابی مرور شما توسط تبلیغ‌کنندگان کمک می‌کند`
    - The en-US says advertisers track you; the Persian reverses the roles, saying ads are being tracked.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `fa/firefox-ios.xliff` — "some ad tracking" is rendered as "چند دنبال کننده" (a few trackers), changing the object of the permission.
    - Current: `به چند دنبال کننده اجازه فعالیت داده می‌شود`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `برخی ردیابی‌های تبلیغاتی مجاز است`
    - The source allows some ad tracking, not a specific small number of trackers.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `fa/firefox-ios.xliff` — "popups" is dropped; the translation says "more trackers, ads and windows" with "more" attached to the wrong noun.
    - Current: `ردگیرها ، تبلیغات و پنجره های بیشتر را مسدود می کند`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `ردگیرها، تبلیغات و پنجره‌های بازشوی بیشتری را مسدود می‌کند`
    - The source says "Blocks more trackers, ads, and popups"; "پنجره‌ها" alone means plain windows, not popups.
- `Settings.TrackingProtectionOption.NormalBrowsingLabelOn` — `fa/firefox-ios.xliff` — "Enhanced Tracking Protection" rendered as "optimizing protection from followers", reversing the head noun and mistranslating "trackers".
    - Current: `بهینه سازی محافظت از دنبال کنندگان`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `محافظت پیشرفته در برابر ردگیری`
    - The source is a noun phrase "Enhanced Tracking Protection"; the target reads as "optimization of protection of followers", i.e. protecting the trackers, and is inconsistent with "محافظت در برابر ردگیری" used for Tracking Protection in the same screen.
- `Settings.WebsiteData.ConfirmPrompt` — `fa/firefox-ios.xliff` — "will clear" weakened to "can clear" (می‌تواند حذف کند).
    - Current: `این اقدام می تواند تمام اطلاعات پایگاه اینترنتی را حذف کند`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `این اقدام تمام اطلاعات پایگاه اینترنتی را حذف می‌کند`
    - The source states the action will clear all website data; the target says it may/can, changing the certainty of the stated behaviour.
- `Tab %@ of %@` — `fa/firefox-ios.xliff` — English "of" left untranslated in the VoiceOver tab position string.
    - Current: `زبانه %1$@ of %2$@`
    - Source: `Tab %1$@ of %2$@`
    - Suggest: `زبانه %1$@ از %2$@`
    - "of" should be rendered as "از" in Persian; leaving English is untranslated content read aloud by VoiceOver.
- `Tabs %@ to %@ of %@` — `fa/firefox-ios.xliff` — English "to" and "of" left untranslated in the VoiceOver tab range string.
    - Current: `زبانه‌های %1$@ to %2$@ of %3$@`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `زبانه‌های %1$@ تا %2$@ از %3$@`
    - The connectors "to"/"of" remain in English, so VoiceOver reads English words in a Persian sentence.
- `TranslationToastHandler.PromptTranslate.Title` — `fa/firefox-ios.xliff` — The translation reverses the roles of the target language and the translation service.
    - Current: `%2$@ به %3$@ ترجمه شود؟`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `با %3$@ به %2$@ ترجمه شود؟`
    - Per the comment, %2$@ is the local language and %3$@ is the service name; the source says "Translate to %2$@ with %3$@", but the target reads "translate %2$@ into %3$@".
- `Welcome to your Reading List` — `fa/firefox-ios.xliff` — "Reading List" is rendered as "reader view" instead of the reading list feature.
    - Current: `به نمای خواندن خوش‌ آمدید`
    - Source: `Welcome to your Reading List`
    - Suggest: `به فهرست خواندنی خود خوش آمدید`
    - The source refers to the user's Reading List, not to Reader View (نمای خواندن).
- `Well, this is embarrassing.` — `fa/firefox-ios.xliff` — "this is embarrassing" is rendered as "we are very sorry", an apology the source does not make.
    - Current: `راستش، بسیار متاسفیم.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `خب، این شرم‌آور است.`
    - The en-US expresses embarrassment about the situation, not an apology from the product.
- `You don’t have any tabs open in Firefox on your other devices.` — `fa/firefox-ios.xliff` — "any tabs open" is rendered as "any other open tabs", misplacing "other".
    - Current: `شما هیچ‌گونه زبانه باز دیگری در فایرفاکس در دستگاه‌های دیگر ندارید.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `شما هیچ زبانهٔ بازی در فایرفاکس روی دستگاه‌های دیگر خود ندارید.`
    - In the source "other" modifies devices only; the translation adds "other" to tabs as well.
- `more than a week ago` — `fa/firefox-ios.xliff` — "more than a week ago" is rendered as "more than a few weeks ago".
    - Current: `بیش از چند هفته قبل`
    - Source: `more than a week ago`
    - Suggest: `بیش از یک هفته قبل`
    - The source says one week, not several weeks.
- `read` — `fa/firefox-ios.xliff` — "read" (past participle/adjective) is translated as the verbal noun "reading".
    - Current: `خواندن`
    - Source: `read`
    - Suggest: `خوانده‌شده`
    - The comment states it is a past participle functioning as an adjective describing an article already read; the counterpart string uses خوانده‌ نشده.
- `Enter Search Mode` — `fa/firefox-ios.xliff` — "Enter" (the verb, to go into search mode) mistranslated as "entering/inputting".
    - Current: `وارد‌کردن حالت جست‌و‌جو`
    - Source: `Enter Search Mode`
    - Suggest: `ورود به حالت جست‌و‌جو`
    - The accessibility label means entering/activating search mode; «وارد‌کردن» means to input something, not to enter a mode.
- `Logins will be permanently removed.` — `fa/firefox-ios.xliff` — Future-tense warning rendered as past tense, telling the user the deletion already happened.
    - Current: `ورود‌ها برای همیشه حذف شد.`
    - Source: `Logins will be permanently removed.`
    - Suggest: `ورودها برای همیشه حذف خواهند شد.`
    - The en-US is a warning prompt before deletion ("will be permanently removed"); the Persian past tense «حذف شد» states the removal is already done.
- `Logins will be removed from all connected devices.` — `fa/firefox-ios.xliff` — Future tense rendered as past tense and "connected devices" reduced to "all devices".
    - Current: `ورود‌ها بر روی تمامی دستگاه‌ها حذف شد.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `ورودها از همه دستگاه‌های متصل حذف خواهند شد.`
    - Source is a pre-deletion warning: "will be removed from all connected devices"; the translation uses past tense and drops "connected".
- `Open & Fill` — `fa/firefox-ios.xliff` — Menu action "Open & Fill" rendered as a past participle/adjective instead of a command.
    - Current: `باز‌شده و پر`
    - Source: `Open & Fill`
    - Suggest: `باز کردن و پر کردن`
    - This is a text-selection menu item (an action). «باز‌شده و پر» means "opened and full", not the actions Open and Fill.
- `Menu.SharePageAction.Title` — `fa/firefox-ios.xliff` — "Share Page With…" translated as "Share address with…".
    - Current: `اشتراک‌گذاری آدرس با…`
    - Source: `Share Page With…`
    - Suggest: `اشتراک‌گذاری صفحه با…`
    - The source and comment refer to sharing the page, not the address/URL.
- `Menu.ViewMobileSiteAction.Title` — `fa/firefox-ios.xliff` — "Site" dropped from "Request Mobile Site", unlike the parallel desktop string.
    - Current: `درخواست نسخه تلفن‌همراه`
    - Source: `Request Mobile Site`
    - Suggest: `درخواست نسخه تلفن‌همراه پایگاه`
    - The desktop counterpart renders "Site" as «پایگاه»; here the noun is missing, making the label incomplete and inconsistent on the same menu.
- `TodayWidget.GoToCopiedLinkLabelV1` — `fa/firefox-ios.xliff` — "copied link" rendered as "پیوند برداشت شده" (picked-up/taken link) instead of copied link.
    - Current: `برو به پیوند برداشت شده`
    - Source: `Go to copied link`
    - Suggest: `برو به پیوند رونوشت‌شده`
    - The source and comment say "Go to link pasted on the clipboard" / copied link; "برداشت شده" means removed/taken, not copied. The parallel string V2 correctly uses "رونوشت شده".

### C. Grammar, agreement & spelling

- `This action will clear all of your private data, including history from your synced devices.` — `fa/firefox-ios.xliff` — Garbled clause: "تاریخچه که از روی دستگاه‌های همگام شما وجود دارد" is ungrammatical.
    - Current: `شامل تاریخچه که از روی دستگاه‌های همگام شما وجود دارد`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `شامل تاریخچهٔ دستگاه‌های همگام‌شدهٔ شما`
    - The relative clause lacks the required ezafe/relative construction and reads as broken Persian compared with the source "including history from your synced devices".
- `DefaultBrowserCard.Title` — `fa/firefox-ios.xliff` — Spelling error "یش‌فرض" instead of "پیش‌فرض" and missing object marker "را".
    - Current: `مرورگر یش‌فرض خود تغییر دهید`
    - Source: `Switch Your Default Browser`
    - Suggest: `مرورگر پیش‌فرض خود را تغییر دهید`
    - "یش‌فرض" is a misspelling of "پیش‌فرض" (default), and the direct-object marker "را" is missing, making the sentence ungrammatical.
- `ContextMenu.BookmarkLinkButtonTitle` — `fa/firefox-ios.xliff` — Word order reversed: «پیوند نشانک» means "bookmark's link" rather than the action "Bookmark Link".
    - Current: `پیوند نشانک`
    - Source: `Bookmark Link`
    - Suggest: `نشانک‌گذاری پیوند`
    - The string is a context menu action for bookmarking a link URL; the Persian noun order makes it a possessive phrase with the wrong meaning.
- `ContextMenu.DownloadLinkButtonTitle` — `fa/firefox-ios.xliff` — Word order reversed: «پیوند دریافت» reads as "receive link" noun phrase incorrectly instead of "download the link".
    - Current: `پیوند دریافت`
    - Source: `Download Link`
    - Suggest: `دریافت پیوند`
    - Source is the command "Download Link"; Persian head-modifier order requires «دریافت پیوند», as done correctly in «همرسانی پیوند» for "Share Link".
- `Downloads` — `fa/firefox-ios.xliff` — Doubled ZWNJ/spacing artifact in "دریافت‌‌ها".
    - Current: `دریافت‌‌ها`
    - Source: `Downloads`
    - Suggest: `دریافت‌ها`
    - Contains two zero-width non-joiners where one is required; the sibling string Downloads.Toast.GoToDownloads.Button uses the correct single form.
- `Downloads.Toast.Cancelled.LabelText` — `fa/firefox-ios.xliff` — Singular "Download Cancelled" rendered as a plural noun phrase with an incorrectly spaced ezafe plural.
    - Current: `دریافت های لغو شده`
    - Source: `Download Cancelled`
    - Suggest: `دریافت لغو شد`
    - Source is a status toast "Download Cancelled" (a sentence about one download), not "cancelled downloads"; also "های" must be attached with ZWNJ as "دریافت‌ها".
- `Downloads.Toast.Failed.LabelText` — `fa/firefox-ios.xliff` — "Download Failed" rendered as plural "faulty downloads" with incorrect spacing.
    - Current: `دریافت های اشکال دار`
    - Source: `Download Failed`
    - Suggest: `دریافت ناموفق بود`
    - Source is a toast confirming that the download has failed; the target is a plural noun phrase meaning "defective downloads" and misspaces the plural suffix.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `fa/firefox-ios.xliff` — Spelling error "در سدد" (should be "درصدد") plus colloquial "رو میخورند".
    - Current: `در سدد استفاده`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `درصدد استفاده`
    - "سدد" is a misspelling of "صدد"; the phrase «درصدد» is the correct form.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `fa/firefox-ios.xliff` — Spelling error: "کنندگاه" should be "کنندگان".
    - Current: `برداشت کنندگاه اثر انگشت`
    - Source: `Fingerprinters`
    - Suggest: `برداشت کنندگان اثر انگشت`
    - Plural suffix is misspelled (کنندگاه instead of کنندگان).
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `fa/firefox-ios.xliff` — Spelling error: "وفتی" should be "وقتی".
    - Current: `وفتی در عنوان بار نمایش داده شد`
    - Source: `Open articles in Reader View by tapping the book icon when it appears in the title bar.`
    - Suggest: `وقتی در نوار عنوان نمایش داده شد`
    - Typo (و+ف instead of و+ق) and "عنوان بار" reverses the Persian word order for "title bar" (نوار عنوان).
- `Search.ThirdPartyEngines.FailedMessage` — `fa/firefox-ios.xliff` — Ungrammatical phrasing mixing "قادر به" with "وجود ندارد".
    - Current: `قادر به افزودن سرویس دهنده جست‌و‌جو وجود ندارد.`
    - Source: `The search provider could not be added.`
    - Suggest: `سرویس‌دهنده جست‌وجو اضافه نشد.`
    - "قادر به ... وجود ندارد" is not valid Persian; the source simply says the provider could not be added.
- `Settings.ClearAllWebsiteData.Clear.Button` — `fa/firefox-ios.xliff` — "all Website Data" rendered with singular "پایگاه اینترنتی" though the source is plural/all websites.
    - Current: `پاک‌سازی تمام اطلاعات پایگاه اینترنتی`
    - Source: `Clear All Website Data`
    - Suggest: `پاک‌سازی تمام اطلاعات پایگاه‌های اینترنتی`
    - The button clears data for all websites; other strings in the same file use the plural "پایگاه‌های اینترنتی".
- `Settings.LoginsAndPasswordsTitle` — `fa/firefox-ios.xliff` — Incorrect plural spacing: «ورود ها» should be written «ورودها».
    - Current: `ورود ها و کلمات عبور`
    - Source: `Logins & Passwords`
    - Suggest: `ورودها و گذرواژه‌ها`
    - Persian plural suffix «ها» must be attached or joined with ZWNJ, not a plain space; the same file writes «ورودها» correctly in Settings.SaveLogins.Title.
- `ShareExtension.SeachInFirefoxAction.Title` — `fa/firefox-ios.xliff` — "این" typo instead of the preposition "در" in "Search in Firefox".
    - Current: `جست‌وجو این فایرفاکس`
    - Source: `Search in Firefox`
    - Suggest: `جست‌وجو در فایرفاکس`
    - The source means "Search in Firefox"; "این" (this) makes the phrase ungrammatical.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `fa/firefox-ios.xliff` — Duplicated adverb "دوباره مجددا" (again again).
    - Current: `چند لحظه دیگر دوباره مجددا اقدام بفرمایید.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `چند لحظه دیگر دوباره اقدام کنید.`
    - "دوباره" and "مجدداً" are synonyms; using both is a redundancy error not present in the source.
- `Web content` — `fa/firefox-ios.xliff` — Missing ezafe: "محتوا وب" should be "محتوای وب".
    - Current: `محتوا وب`
    - Source: `Web content`
    - Suggest: `محتوای وب`
    - Persian requires the ezafe suffix -ی on محتوا when followed by وب.
- `more than a month ago` — `fa/firefox-ios.xliff` — The "ago" part is dropped, leaving "more than a month".
    - Current: `بیش از یک ماه`
    - Source: `more than a month ago`
    - Suggest: `بیش از یک ماه قبل`
    - The source is a relative past date "more than a month ago"; without قبل/پیش the string reads as a duration.
- `Search Settings` — `fa/firefox-ios.xliff` — "جست‌و جو" has a stray space instead of consistent ZWNJ spelling "جست‌وجو".
    - Current: `تنظیمات جست‌و جو`
    - Source: `Search Settings`
    - Suggest: `تنظیمات جست‌وجو`
    - The word is written with a space in the middle, inconsistent with the standard "جست‌وجو" used elsewhere in the batch.
- `TodayWidget.TopSitesGalleryDescription` — `fa/firefox-ios.xliff` — Missing ZWNJ in "سایتهای" and missing final hamza/adverb form "اخیراً".
    - Current: `میانبرهایی را به سایتهای مکرر و اخیرا بازدید شده اضافه کنید.`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `میان‌برهایی را به سایت‌های پربازدید و اخیراً بازدیدشده اضافه کنید.`
    - Persian orthography requires ZWNJ before the plural suffix (سایت‌های) and the tanwin on اخیراً; also "سایت‌های مکرر" (frequent sites) is ungrammatical for "frequently visited sites".

### D. Terminology, register & consistency

- `ContextMenu.CopyImageButtonTitle` — `fa/firefox-ios.xliff` — "Copy" is rendered as «برداشت» (pick up/withdraw) instead of the standard «رونوشت/کپی», inconsistent with ClipboardToast.GoToCopiedLink.Title which uses «رونوشت».
    - Current: `برداشت تصویر`
    - Source: `Copy Image`
    - Suggest: `رونوشت از تصویر`
    - The same source term "copy" is translated «رونوشت» in ClipboardToast.GoToCopiedLink.Title but «برداشت» here, which does not mean copy in Persian.
- `ContextMenu.OpenInNewTabButtonTitle` — `fa/firefox-ios.xliff` — "Tab" is rendered as «تب» here while other strings in the same file use «زبانه».
    - Current: `بازکردن در تب جدید`
    - Source: `Open in New Tab`
    - Suggest: `بازکردن در زبانهٔ جدید`
    - ContextMenu.ButtonToast.NewTabOpened.LabelText and Closing tab use «زبانه» for tab; using «تب» on the same screen group is inconsistent.
- `Downloads.CancelDialog.Message` — `fa/firefox-ios.xliff` — Uses the loanword "کنسل" instead of the standard term "لغو" used elsewhere on the same screen.
    - Current: `کنسل کنید`
    - Source: `Are you sure you want to cancel this download?`
    - Suggest: `لغو کنید`
    - The same dialog's Cancel button uses "لغو"; "کنسل" is inconsistent colloquial terminology.
- `Hotkeys.PrivateMode.DiscoveryTitle` — `fa/firefox-ios.xliff` — "Private Browsing Mode" uses "ناشناس" (anonymous/incognito) while the related string uses "خصوصی" for private.
    - Current: `حالت مرورِ ناشناس`
    - Source: `Private Browsing Mode`
    - Suggest: `حالت مرورِ خصوصی`
    - Firefox terminology for "private" is "خصوصی", as used in Hotkeys.NewPrivateTab.DiscoveryTitle in the same screen; "ناشناس" is inconsistent.
- `InactiveTabs.TabTray.CloseButtonTitle` — `fa/firefox-ios.xliff` — Uses "برگه" for "tab" while the rest of the file consistently uses "زبانه".
    - Current: `بستن همه برگه‌های غیرفعال`
    - Source: `Close All Inactive Tabs`
    - Suggest: `بستن همه زبانه‌های غیرفعال`
    - "Tab" is rendered "زبانه" throughout this file (New Tab, Show Next Tab, etc.); "برگه" is an inconsistent term.
- `Menu.WhatsNew.Title` — `fa/firefox-ios.xliff` — Colloquial/spoken register ("اومده") used for a UI menu title.
    - Current: `چه چیز جدیدی اومده`
    - Source: `What’s New`
    - Suggest: `تازه‌ها`
    - "اومده" is informal spoken Persian; UI titles use standard written register (e.g. «تازه‌ها» or «چه چیزهای جدیدی آمده»).
- `Search.ThirdPartyEngines.FormErrorMessage` — `fa/firefox-ios.xliff` — Colloquial spoken form "رو" instead of the written object marker "را".
    - Current: `تمام فیلدها رو به طور صحیح`
    - Source: `Please fill all fields correctly.`
    - Suggest: `تمام فیلدها را به طور صحیح`
    - "رو" is spoken register; UI text requires the written form "را".
- `Settings.DisplayTheme.SectionFooter` — `fa/firefox-ios.xliff` — "Theme" is rendered "تم" here while the rest of the theme settings screen uses "زمینه".
    - Current: `تم بطور خودکار`
    - Source: `The theme will automatically change based on your display brightness. You can set the threshold where the theme changes. The circle indicates your display’s current brightness.`
    - Suggest: `زمینه بطور خودکار`
    - Settings.DisplayTheme.Title.v2 and related headers use "زمینه" for Theme; mixing "تم" on the same screen is inconsistent terminology.
- `TodayWidget.QuickViewGalleryDescriptionV2` — `fa/firefox-ios.xliff` — "tabs" rendered as "برگه" here while all other strings in this file use "زبانه"; also missing ZWNJ in "سایتهای"-style plural "برگه های".
    - Current: `میانبرها را به برگه های باز خود اضافه کنید.`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `میان‌برها را به زبانه‌های باز خود اضافه کنید.`
    - Terminology inconsistency within the same file (TodayWidget.ClosePrivateTabsButton, NoOpenTabsLabel, SearchInPrivateTabLabelV2 all use زبانه) plus missing ZWNJ before the plural suffix.

### E. Typography, punctuation & spacing

- `DefaultBrowserCard.Description` — `fa/firefox-ios.xliff` — Space before commas instead of after ("سایت ها ، ایمیل ها").
    - Current: `پیوندهای وب سایت ها ، ایمیل ها و پیام ها را`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `پیوندهای وب‌سایت‌ها، ایمیل‌ها و پیام‌ها را`
    - Persian punctuation places the comma immediately after the preceding word; the space before the comma is a typography error.
- `DefaultBrowserOnboarding.Description1` — `fa/firefox-ios.xliff` — Step numbering inconsistent: Latin digits here and in step 3 but Persian digit in step 2.
    - Current: `1. برو به تنظیمات`
    - Source: `1. Go to Settings`
    - Suggest: `۱. برو به تنظیمات`
    - The three onboarding steps appear together on one screen; mixing "1.", "۲." and "3." is inconsistent numbering.
- `BreachAlerts.Description` — `fa/firefox-ios.xliff` — Spaces placed before commas and a broken-off verb suffix («داده اید», «گذرواژه ها») violate Persian punctuation and ZWNJ conventions.
    - Current: `از آخرین باری که گذرواژه خود را تغییر داده اید ، گذرواژه ها درز کرده یا به سرقت رفته اند. برای محافظت از این حساب ، وارد سایت شوید و گذرواژه خود را تغییر دهید.`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `از آخرین باری که گذرواژه خود را تغییر داده‌اید، گذرواژه‌ها درز کرده یا به سرقت رفته‌اند. برای محافظت از این حساب، وارد سایت شوید و گذرواژه خود را تغییر دهید.`
    - Persian punctuation places the comma «،» directly after the preceding word with no space before it, and plural/verb suffixes attach with ZWNJ.
- `Changes font type.` — `fa/firefox-ios.xliff` — Missing sentence-final period present in the source.
    - Current: `تغییر نوع فونت`
    - Source: `Changes font type.`
    - Suggest: `تغییر نوع فونت.`
    - Source "Changes font type." ends with a period, as does the sibling string "Changes color theme." which was translated with a period.
- `Downloads.Toast.MultipleFiles.DescriptionText` — `fa/firefox-ios.xliff` — Missing spaces around the numbers in "1از%d پرونده".
    - Current: `1از%d پرونده`
    - Source: `1 of %d files`
    - Suggest: `۱ از %d پرونده`
    - The source "1 of %d files" has spaces separating the words; the target runs the digit, preposition and placeholder together.
- `ScanQRCode.Instructions.Label` — `fa/firefox-ios.xliff` — Missing space between "کد" and "QR".
    - Current: `کدQR`
    - Source: `Align QR code within frame to scan`
    - Suggest: `کد QR`
    - Other strings in the same group write "کد QR" with a space; here the words are run together.
- `SendTo.Error.Message` — `fa/firefox-ios.xliff` — Missing spaces around the conjunction between HTTP and HTTPS.
    - Current: `پیوند‌های HTTPوHTTPS`
    - Source: `Only HTTP and HTTPS links can be shared.`
    - Suggest: `پیوند‌های HTTP و HTTPS`
    - The words are run together without spaces, unlike the source's "HTTP and HTTPS".
- `Welcome to your Reading List` — `fa/firefox-ios.xliff` — Stray space after the ZWNJ in "خوش‌ آمدید".
    - Current: `خوش‌ آمدید`
    - Source: `Welcome to your Reading List`
    - Suggest: `خوش آمدید`
    - A zero-width non-joiner immediately followed by a space produces incorrect spacing.
- `TodayWidget.QuickActionGalleryDescription` — `fa/firefox-ios.xliff` — Space before the comma ("ابزارک ،") violates Persian punctuation spacing.
    - Current: `پس از افزودن ابزارک ، آن را`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `پس از افزودن ابزارک، آن را`
    - In Persian the comma attaches to the preceding word with no space before it.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fa/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
