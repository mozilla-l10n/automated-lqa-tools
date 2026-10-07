# Firefox iOS l10n QA — fa

| | |
|---|---|
| **Generated** | 2026-10-07 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e7f33082c399` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e7f33082c399` |
| **Previous run** | 2026-10-05 @ `ef278c60f343` |
| **Mode** | incremental |
| **Strings reviewed this run** | 16 of 1,984 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fa: [android](android.md)

---

## Changes in this run

### 🆕 New findings (2)

- `Onboarding.MultiDay.NotificationCard.BodyText.v159` — `fa/firefox-ios.xliff` — "protection updates" rendered as "security updates" (امنیتی) instead of protection/حفاظت.
    - Current: `به‌روزرسانی‌های امنیتی`
    - Source: `Get %@ protection updates, tips, and your privacy report.`
    - Suggest: `به‌روزرسانی‌های حفاظتی`
    - The source says "%@ protection updates" (updates about the browser's protections), not security updates; امنیتی means "security", a different claim about what the notifications contain.
- `NativeErrorPage.GenericError.Description.v158` — `fa/firefox-ios.xliff` — "Check your connection settings" expanded to "your internet connection settings".
    - Current: `تنظیمات اتصال به اینترنت خود را بررسی کرده و دوباره تلاش کنید.`
    - Source: `The site may be temporarily unavailable, it may have moved to a different address, or your firewall or proxy may be blocking the connection.  Check your connection settings and try again.`
    - Suggest: `تنظیمات اتصال خود را بررسی کرده و دوباره تلاش کنید.`
    - The source refers generically to connection settings (which may include firewall/proxy settings), not specifically internet connection settings.

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
| Strings | 1,984 |
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
| quotes | `curly-single` 8, `guillemet` 5, `curly-double` 3 | _mixed_ |
| apostrophe | `typographic` 37 | **typographic** |
| ellipsis | `char` 27 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (462)

> **Reads as a deliberate edit (4).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `fa/firefox-ios.xliff` — "tapping" rendered as "tapping and holding", and "book plus icon" loses the plus.
    - Current: `با تپ کردن و نگه داشتن آیکون کتاب`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `با تپ کردن آیکون کتاب به‌همراه علامت مثبت`
    - The source says simply "tapping the book plus icon"; the translation instructs a tap-and-hold gesture, giving the user wrong instructions.
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
| 1 | Broken output (blank value, broken markup, wrong variable) | 3 |
| 2 | Wrong content (says something other than the English) | 230 |
| 3 | Degraded language (grammar, spelling, terminology) | 224 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

- `WorldCup.GroupPhase.GroupD.Title.v151` — `fa/firefox-ios.xliff` — The group letter "D" is missing from the translation.
    - Current: `گروه`
    - Source: `Group D`
    - Suggest: `گروه D`
    - Source is "Group D"; the identifying letter was dropped, leaving an unidentifiable label.
- `WorldCup.HomepageWidget.CountDown.DayLabel.v151` — `fa/firefox-ios.xliff` — Placeholder text "ترجمه‌نشده" shipped instead of a 1–2 character day abbreviation.
    - Current: `ترجمه‌نشده`
    - Source: `D`
    - Suggest: `ر`
    - The comment limits the string to 1–2 characters as an abbreviation for "Days"; the target is a literal "untranslated" marker that will be truncated to nonsense.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Alerts.RestoreTabs.Title.v109.v2` — `fa/firefox-ios.xliff` — The word "crashed" is left untranslated and the rest is ungrammatical word salad.
    - Current: `%@ crashed. بازیابی شما زبانه‌ها؟`
    - Source: `%@ crashed. Restore your tabs?`
    - Suggest: `%@ از کار افتاد. زبانه‌های شما بازیابی شود؟`
    - The source "%@ crashed. Restore your tabs?" is only half-translated; "crashed" remains in English and "بازیابی شما زبانه‌ها؟" has wrong word order/possessive.
- `Settings.AppIconSelection.AppIconNames.Fun.Cool.Title.146` — `fa/firefox-ios.xliff` — "Cool" (stylish, fox with sunglasses) translated as "خنک" (cool in temperature).
    - Current: `خنک`
    - Source: `Cool`
    - Suggest: `باحال`
    - The developer comment describes a fox with sunglasses, i.e. "cool" in the sense of stylish, not low temperature.
- `Bookmarks.EmptyState.Root.Body.v135` — `fa/firefox-ios.xliff` — Translation is partially untranslated and garbled, leaving English fragments and broken grammar.
    - Current: `ما’ll also grab نشانک‌ها از دیگر همگام‌شده دستگاه‌ها.`
    - Source: `Save sites as you browse. We’ll also grab bookmarks from other synced devices.`
    - Suggest: `ما نشانک‌ها را از دیگر دستگاه‌های همگام‌شده نیز دریافت می‌کنیم.`
    - The en-US "We’ll also grab bookmarks from other synced devices." is left half-English ("’ll also grab") and the Persian word order is broken.
- `Bookmarks.EmptyState.Root.BodySignedOut.v135` — `fa/firefox-ios.xliff` — Second sentence is left mostly in English and garbled.
    - Current: `Sign در به grab نشانک‌ها از دیگر همگام‌شده دستگاه‌ها.`
    - Source: `Save sites as you browse. Sign in to grab bookmarks from other synced devices.`
    - Suggest: `برای دریافت نشانک‌ها از دیگر دستگاه‌های همگام‌شده وارد شوید.`
    - The en-US "Sign in to grab bookmarks from other synced devices." is left untranslated/broken ("Sign در به grab").
- `Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136` — `fa/firefox-ios.xliff` — "BOOKMARKS" is left in English and corrupted with the Persian word "تأیید" inserted.
    - Current: `رومیزی BOتأییدMARKS`
    - Source: `DESKTOP BOOKMARKS`
    - Suggest: `نشانک‌های رومیزی`
    - The source is "DESKTOP BOOKMARKS"; the target contains the garbled token "BOتأییدMARKS" instead of a translation of "BOOKMARKS".
- `Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154` — `fa/firefox-ios.xliff` — "BOOKMARKS" is left in English and corrupted with the Persian word "تأیید" inserted.
    - Current: `تلفن همراه BOتأییدMARKS`
    - Source: `MOBILE BOOKMARKS`
    - Suggest: `نشانک‌های تلفن همراه`
    - The source is "MOBILE BOOKMARKS"; the target contains the garbled token "BOتأییدMARKS" instead of a translation of "BOOKMARKS".
- `Addresses.EditAddress.AutofillAddressPin.v129` — `fa/firefox-ios.xliff` — "Pin" (the Indian Postal Index Number) is translated as the verb "to pin/attach".
    - Current: `سنجاق کردن`
    - Source: `Pin`
    - Suggest: `کد پستی (PIN)`
    - The developer comment states this is the PIN (Postal Index Number) field used in India, not the action of pinning something.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `fa/firefox-ios.xliff` — "Post town" is left half-untranslated as "Post شهر".
    - Current: `Post شهر`
    - Source: `Post town`
    - Suggest: `شهر پستی`
    - The English word "Post" remains untranslated and mixed into the Persian text, producing a nonsensical label for the post town field.
- `CreditCard.EditCard.ToggleToAllowAutofillTitle.v122` — `fa/firefox-ios.xliff` — "Save and Fill" is rendered as "ذخیره و پرکردن خودکار" (save and autofill), adding "automatic" not present in the source.
    - Current: `ذخیره و پرکردن خودکار روش‌های پرداخت`
    - Source: `Save and Fill Payment Methods`
    - Suggest: `ذخیره و پرکردن روش‌های پرداخت`
    - The en-US says "Save and Fill Payment Methods"; the translation adds "خودکار" (automatic), which the source label does not state.
- `Menu.EnhancedTrackingProtection.Certificates.CommonName.v131` — `fa/firefox-ios.xliff` — "Common Name" is left half-untranslated as "Common نام", producing a nonsensical mixed-language label.
    - Current: `Common نام`
    - Source: `Common Name`
    - Suggest: `نام مشترک (Common Name)`
    - The source term "Common Name" is a certificate field; the translation mechanically renders only "Name" into Persian and leaves "Common" in English, which is not a valid Persian phrase.
- `Menu.EnhancedTrackingProtection.Details.NoTrackers.v131` — `fa/firefox-ios.xliff` — "No trackers found" translated as "no tracking found" instead of trackers (ردیاب).
    - Current: `ردیابی پیدا نشد`
    - Source: `No trackers found`
    - Suggest: `ردیابی پیدا نشد → ردیابی‌کننده‌ای پیدا نشد`
    - Other strings in the same file use «ردیاب» for "tracker"; here «ردیابی» means "tracking", an inconsistent and inaccurate term for the noun "trackers".
- `ExternalLink.ExternalInvalidLinkMessage.v136` — `fa/firefox-ios.xliff` — String is a broken mix of untranslated English words and Persian, unintelligible to users.
    - Current: `برنامه required به باز کردن آن پیوند می‌تواند’t باشد found.`
    - Source: `The application required to open that link can’t be found.`
    - Suggest: `برنامهٔ لازم برای باز کردن آن پیوند پیدا نشد.`
    - The source says the required application can't be found; the target leaves "required", "can’t", "found" in English and is grammatically broken.
- `FirefoxHome.PrivacyNotice.Body.v148` — `fa/firefox-ios.xliff` — Partially untranslated, ungrammatical rendering mixing English fragments.
    - Current: `ما’ve به‌روزرسانی‌شده ما %1$@ به reflect جدیدترین ویژگی‌ها در %2$@. %3$@`
    - Source: `We’ve updated our %1$@ to reflect the latest features in %2$@. %3$@`
    - Suggest: `ما %1$@ خود را به‌روزرسانی کردیم تا جدیدترین ویژگی‌های %2$@ را بازتاب دهد. %3$@`
    - Source: "We’ve updated our %1$@ to reflect the latest features in %2$@." The target keeps "’ve" and "reflect" in English and is not grammatical Persian.
- `FirefoxHomepage.FeltPrivacyUI.Body.v122` — `fa/firefox-ios.xliff` — String largely untranslated and corrupted, with English words and Latin commas.
    - Current: `%@ deletes شما کوکی‌ها, تاریخچه, و وبگاه datیک when شما بستن همه شما خصوصی زبانه‌ها.`
    - Source: `%@ deletes your cookies, history, and site data when you close all your private tabs.`
    - Suggest: `%@ وقتی همهٔ زبانه‌های خصوصی خود را ببندید، کوکی‌ها، تاریخچه و داده‌های وبگاه شما را حذف می‌کند.`
    - Source: "%@ deletes your cookies, history, and site data when you close all your private tabs." The target leaves "deletes", "when", "dat" untranslated and is ungrammatical.
- `ContextualHints.MainMenu.MenuRedesign.Body.v142` — `fa/firefox-ios.xliff` — Translation left partly in English with untranslated words "at" and "fingertips".
    - Current: `نشانک‌ها, تاریخچه, و تنظیمات — همه at شما fingertips.`
    - Source: `Bookmarks, history, and settings — all at your fingertips.`
    - Suggest: `نشانک‌ها، تاریخچه و تنظیمات — همه در دسترس شما.`
    - The en-US "all at your fingertips" is not translated; English words remain inside the Persian string, and Latin commas are used instead of Persian «،».
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `fa/firefox-ios.xliff` — Untranslated English words and garbled word order render the sentence meaningless in Persian.
    - Current: `یافتن what شما need سریع‌تر, از خصوصی مرور به ذخیره عمل‌ها.`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `آنچه را نیاز دارید سریع‌تر پیدا کنید، از مرور خصوصی تا عمل‌های ذخیره.`
    - Source "Find what you need faster, from private browsing to save actions." is only partially translated; "what", "need" remain English and the phrase structure is broken.
- `ContextualHints.MainMenu.NewMenu.Title.v132` — `fa/firefox-ios.xliff` — "streamlined" left untranslated in English.
    - Current: `جدید: streamlined منو`
    - Source: `New: streamlined menu`
    - Suggest: `جدید: منوی ساده‌شده`
    - The source word "streamlined" is not translated, leaving English in the Persian UI.
- `MainMenu.Account.AccessibilityLabels.MainButton.v132` — `fa/firefox-ios.xliff` — "Sign in" left untranslated, producing a mixed English/Persian accessibility label.
    - Current: `Sign در به همگام‌سازی گذرواژه‌ها, زبانه‌ها, و بیشتر`
    - Source: `Sign in to sync passwords, tabs, and more`
    - Suggest: `برای همگام‌سازی گذرواژه‌ها، زبانه‌ها و بیشتر وارد شوید`
    - Source "Sign in to sync passwords, tabs, and more" is partly untranslated and syntactically broken.
- `MainMenu.Account.SignedIn.Description.v141` — `fa/firefox-ios.xliff` — English words "what" and "back up" left untranslated.
    - Current: `مدیریت what شما back up و همگام‌سازی`
    - Source: `Manage what you back up and sync`
    - Suggest: `مدیریت آنچه پشتیبان‌گیری و همگام‌سازی می‌کنید`
    - Source "Manage what you back up and sync" is only partially translated, leaving English in the Persian UI.
- `MainMenu.Account.SyncError.Title.v131` — `fa/firefox-ios.xliff` — "Sign back in" left untranslated, producing a broken mixed-language string.
    - Current: `Sign back در به همگام‌سازی`
    - Source: `Sign back in to sync`
    - Suggest: `برای همگام‌سازی دوباره وارد شوید`
    - Source "Sign back in to sync" is not translated into Persian.
- `MainMenu.HeaderBanner.Subtitle.v142` — `fa/firefox-ios.xliff` — "Takes" left untranslated in English.
    - Current: `Takes ثانیه. تغییر هر زمان.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `چند ثانیه طول می‌کشد. هر زمان تغییر دهید.`
    - Source "Takes seconds. Change anytime." is only partially translated.
- `MainMenu.HeaderBanner.Title.v142` — `fa/firefox-ios.xliff` — "Make" left untranslated and sentence structure broken.
    - Current: `Make %@ شما پیش‌فرض`
    - Source: `Make %@ your default`
    - Suggest: `%@ را پیش‌فرض خود کنید`
    - Source "Make %@ your default" is not properly translated into Persian.
- `Microsurvey.Survey.OptionsOrder.AccessibilityLabel.v129` — `fa/firefox-ios.xliff` — "out of" mistranslated literally as "بیرونِ" (outside of) instead of the counting sense "از".
    - Current: `%1$@ بیرونِ %2$@`
    - Source: `%1$@ out of %2$@`
    - Suggest: `%1$@ از %2$@`
    - The comment says the output is like "1 out of 6", i.e. item N of M; "بیرونِ" means "outside of" and is nonsense here.
- `NativeErrorPage.GenericError.Description.v158` — `fa/firefox-ios.xliff` — "Check your connection settings" expanded to "your internet connection settings".
    - Current: `تنظیمات اتصال به اینترنت خود را بررسی کرده و دوباره تلاش کنید.`
    - Source: `The site may be temporarily unavailable, it may have moved to a different address, or your firewall or proxy may be blocking the connection.  Check your connection settings and try again.`
    - Suggest: `تنظیمات اتصال خود را بررسی کرده و دوباره تلاش کنید.`
    - The source refers generically to connection settings (which may include firewall/proxy settings), not specifically internet connection settings.
- `DefaultBrowserPopup.FirstLabel.v114` — `fa/firefox-ios.xliff` — English word "Go" left untranslated in the Persian instruction.
    - Current: `1. Go به *تنظیمات*`
    - Source: `1. Go to *Settings*`
    - Suggest: `۱. به *تنظیمات* بروید`
    - The source "1. Go to *Settings*" is only partially translated; "Go" remains English, producing a mixed-language instruction.
- `DefaultBrowserPopup.SecondLabel.v114` — `fa/firefox-ios.xliff` — "Tap" left untranslated and "Default Browser App" word order is garbled.
    - Current: `2. Tap *پیش‌فرض مرورگر برنامه*`
    - Source: `2. Tap *Default Browser App*`
    - Suggest: `۲. روی *برنامهٔ مرورگر پیش‌فرض* بزنید`
    - The verb "Tap" is untranslated and the noun phrase is rendered in English word order, which is ungrammatical in Persian.
- `Onboarding.Customization.Intro.Description.v123` — `fa/firefox-ios.xliff` — Word-for-word garbled rendering with untranslated English words and a mistranslation of "match" as "مسابقه" (competition).
    - Current: `تنظیم شما پوسته و نوار ابزار به مسابقه شما unique مرور style.`
    - Source: `Set your theme and toolbar to match your unique browsing style.`
    - Suggest: `پوسته و نوار ابزار خود را طوری تنظیم کنید که با سبک مرور منحصربه‌فرد شما هماهنگ باشد.`
    - The source says to set theme and toolbar to match the user's unique browsing style; the target leaves "unique" and "style" in English and renders "match" as "مسابقه" (a contest), making it meaningless.
- `Onboarding.Customization.Theme.Description.v123` — `fa/firefox-ios.xliff` — Untranslated "See" and a nonsensical rendering of "in the best light".
    - Current: `See وب در بهترین روشن.`
    - Source: `See the web in the best light.`
    - Suggest: `وب را در بهترین حالت ببینید.`
    - The English verb is left untranslated and "best light" is rendered word-for-word as "بهترین روشن", which is ungrammatical and meaningless.
- `Onboarding.IntroDescriptionPart1.v114` — `fa/firefox-ios.xliff` — "For good" (for the benefit of good) mistranslated as "برای همیشه" (forever).
    - Current: `برای همیشه.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `برای خیر.`
    - "For good" here means for the common good, not "forever"; "برای همیشه" states a different fact.
- `Onboarding.IntroDescriptionPart2.v114` — `fa/firefox-ios.xliff` — English words "Committed" and "promise" left untranslated and word order garbled.
    - Current: `Committed به promiseِ یک بهتر اینترنت برای همه.`
    - Source: `Committed to the promise of a better Internet for everyone.`
    - Suggest: `متعهد به وعدهٔ اینترنتی بهتر برای همه.`
    - The source sentence is only partially translated, leaving English words and an ungrammatical Persian noun phrase.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `fa/firefox-ios.xliff` — Largely untranslated and garbled: "have", "putting" left in English and "match" rendered as "مسابقه" (competition).
    - Current: `انتخاب کنید شما موردعلاقه پوسته یا have %@ مسابقه شما دستگاه, putting شما در کنترل.`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `پوستهٔ موردعلاقهٔ خود را انتخاب کنید یا بگذارید %@ با دستگاه شما هماهنگ شود، تا کنترل در دست شما باشد.`
    - The source asks the user to pick a theme or have the app match the device; the target keeps English words, mistranslates "match" as a contest, and uses an English comma.
- `Onboarding.Modern.BrandRefresh.Marketing.LearnMoreLink.v148` — `fa/firefox-ios.xliff` — Link text left partly in English and ungrammatical.
    - Current: `How ما استفاده داده`
    - Source: `How we use the data`
    - Suggest: `چگونه از داده‌ها استفاده می‌کنیم`
    - "How we use the data" is partially untranslated ("How") and the remainder is not grammatical Persian.
- `Onboarding.Modern.BrandRefresh.Marketing.Title.v148` — `fa/firefox-ios.xliff` — Title left partly in English and ungrammatical.
    - Current: `کمک ما build یک بهتر اینترنت`
    - Source: `Help us build a better internet`
    - Suggest: `به ما کمک کنید اینترنت بهتری بسازیم`
    - "Help us build a better internet" is rendered word-for-word with "build" untranslated.
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `fa/firefox-ios.xliff` — Title is corrupted: "Notifications" became "خیرtifications" and most of the sentence is untranslated English.
    - Current: `خیرtifications کمک شما stay safer با %@`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `اعلان‌ها به شما کمک می‌کنند با %@ ایمن‌تر بمانید`
    - The source "Notifications help you stay safer with %@" has been mangled by a bad find-and-replace ("No" → "خیر") and left largely in English.
- `Onboarding.Modern.BrandRefresh.Sync.SignIn.Action.v148` — `fa/firefox-ios.xliff` — Button label left partly in English.
    - Current: `Start در حال همگام‌سازی`
    - Source: `Start Syncing`
    - Suggest: `شروع همگام‌سازی`
    - "Start Syncing" retains the untranslated word "Start" and the rest is ungrammatical.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `fa/firefox-ios.xliff` — Button title left untranslated in English.
    - Current: `Agree و continue`
    - Source: `Agree and continue`
    - Suggest: `پذیرش و ادامه`
    - "Agree and continue" was not translated apart from the conjunction.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `fa/firefox-ios.xliff` — Agreement text is largely untranslated and corrupted ("datیک"), with a Latin comma.
    - Current: `به کمک بهبود مرورگر, %1$@ sends تشخیصی و تعامل datیک به %2$@. %3$@`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `برای کمک به بهبود مرورگر، %1$@ داده‌های تشخیصی و تعاملی را به %2$@ ارسال می‌کند. %3$@`
    - The source sentence is left mostly in English and "data" has been mangled into "datیک".
- `Onboarding.Modern.BrandRefresh.TermsOfUse.PrivacyNoticeAgreement.v148` — `fa/firefox-ios.xliff` — Agreement text left partly in English and ungrammatical.
    - Current: `%1$@ cares about شما حریم خصوصی. خواندن بیشتر در ما %2$@`
    - Source: `%1$@ cares about your privacy. Read more in our %2$@`
    - Suggest: `%1$@ به حریم خصوصی شما اهمیت می‌دهد. در %2$@ ما بیشتر بخوانید`
    - "cares about" is untranslated and the remainder follows English word order.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.TermsOfUseAgreement.v148` — `fa/firefox-ios.xliff` — Agreement text left partly in English.
    - Current: `By continuing, شما agree به %@`
    - Source: `By continuing, you agree to the %@`
    - Suggest: `با ادامه دادن، شما %@ را می‌پذیرید`
    - "By continuing" and "agree" remain untranslated English.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Title.v148` — `fa/firefox-ios.xliff` — Title left partly in English and word-for-word.
    - Current: `دریافت ready به اجرا free`
    - Source: `Get ready to run free`
    - Suggest: `آمادهٔ آزادی شوید`
    - "Get ready to run free" is rendered literally with "ready" and "free" untranslated.
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148.v2` — `fa/firefox-ios.xliff` — Title left partly in English ("built-in") and word-for-word.
    - Current: `باز کردن شما پیوندها با built-in حریم خصوصی`
    - Source: `Open your links with built-in privacy`
    - Suggest: `پیوندهای خود را با حریم خصوصی داخلی باز کنید`
    - "built-in" is untranslated and the sentence follows English word order.
- `Onboarding.Modern.BrandRefresh.Welcome.TitleV3.v149` — `fa/firefox-ios.xliff` — Title left partly in English ("built-in") and word-for-word.
    - Current: `باز کردن همه شما پیوندها با built-in حریم خصوصی`
    - Source: `Open all your links with built-in privacy`
    - Suggest: `همهٔ پیوندهای خود را با حریم خصوصی داخلی باز کنید`
    - "built-in" is untranslated and the sentence follows English word order.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `fa/firefox-ios.xliff` — Description is a word-for-word machine rendering with untranslated English and a mistranslated "match".
    - Current: `انتخاب کنید شما موردعلاقه پوسته یا have %@ مسابقه شما دستگاه, putting شما در کنترل.`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `پوستهٔ موردعلاقه‌تان را انتخاب کنید یا بگذارید %@ با دستگاه شما هماهنگ شود تا کنترل در دست شما باشد.`
    - "have" and "putting" are untranslated, and "match" is rendered as "مسابقه" (a contest) instead of matching the device theme.
- `Onboarding.Modern.Customization.Toolbar.Title.v140` — `fa/firefox-ios.xliff` — Title left half-untranslated and ungrammatical word salad instead of "Choose where to put your address bar".
    - Current: `انتخاب کنید where به put شما نشانی نوار`
    - Source: `Choose where to put your address bar`
    - Suggest: `انتخاب کنید نوار نشانی کجا قرار بگیرد`
    - English words "where" and "put" remain untranslated and the word order is not Persian; the meaning of the source title is lost.
- `Onboarding.Modern.Sync.Description.v145` — `fa/firefox-ios.xliff` — Largely untranslated and incoherent; English words remain and the encryption sentence is broken.
    - Current: `شما نشانک‌ها, گذرواژه‌ها, و بیشتر همگام‌سازی در هر دستگاه. Everything’ محافظت‌شده با encryption, so فقط شمامی‌تواند دسترسی it.`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `نشانک‌ها، گذرواژه‌ها و موارد دیگر روی هر دستگاهی همگام‌سازی می‌شوند. همه‌چیز با رمزگذاری محافظت می‌شود، بنابراین فقط شما می‌توانید به آن دسترسی داشته باشید.`
    - The source sentence is not rendered in Persian: "Everything’", "encryption", "so", "it" are left in English and "شمامی‌تواند" is a run-together ungrammatical form.
- `Onboarding.Modern.Sync.SignIn.Action.v140` — `fa/firefox-ios.xliff` — "Start" left untranslated and "Syncing" rendered as a progress state.
    - Current: `Start در حال همگام‌سازی`
    - Source: `Start Syncing`
    - Suggest: `شروع همگام‌سازی`
    - The button label "Start Syncing" is an action; the target leaves "Start" in English and uses "در حال همگام‌سازی" (currently syncing).
- `Onboarding.Modern.Sync.SignIn.Action.v145` — `fa/firefox-ios.xliff` — "Start" left untranslated and "Syncing" rendered as a progress state.
    - Current: `Start در حال همگام‌سازی`
    - Source: `Start Syncing`
    - Suggest: `شروع همگام‌سازی`
    - The button label "Start Syncing" is an action; the target leaves "Start" in English and uses "در حال همگام‌سازی" (currently syncing).
- `Onboarding.Modern.Sync.Title.v145` — `fa/firefox-ios.xliff` — Title largely untranslated: "Take" and "adventures" remain in English and the phrase is ungrammatical.
    - Current: `Take %@ در همه شما مرور adventures`
    - Source: `Take %@ on all your browsing adventures`
    - Suggest: `%@ را در همهٔ ماجراجویی‌های مرور خود همراه داشته باشید`
    - The source "Take %@ on all your browsing adventures" is not rendered in Persian.
- `Onboarding.Modern.TermsOfService.ManagePreferenceAgreement.v140` — `fa/firefox-ios.xliff` — Partially untranslated and corrupted: "sends" in English and "datیک" for "data".
    - Current: `به کمک بهبود مرورگر, %1$@ sends تشخیصی و تعامل datیک به %2$@. %3$@`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `برای کمک به بهبود مرورگر، %1$@ داده‌های تشخیصی و تعاملی را به %2$@ ارسال می‌کند. %3$@`
    - The verb "sends" is untranslated and "data" was mangled into "datیک"; Latin comma used instead of Persian comma.
- `Onboarding.Modern.TermsOfService.ManagePreferenceAgreement.v145` — `fa/firefox-ios.xliff` — Partially untranslated and corrupted: "sends" in English and "datیک" for "data".
    - Current: `به کمک بهبود مرورگر, %1$@ sends تشخیصی و تعامل datیک به %2$@. %3$@`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `برای کمک به بهبود مرورگر، %1$@ داده‌های تشخیصی و تعاملی را به %2$@ ارسال می‌کند. %3$@`
    - The verb "sends" is untranslated and "data" was mangled into "datیک"; Latin comma used instead of Persian comma.
- `Onboarding.Modern.TermsOfService.PrivacyNoticeAgreement.v140` — `fa/firefox-ios.xliff` — "cares about" left untranslated and the sentence is ungrammatical Persian.
    - Current: `%1$@ cares about شما حریم خصوصی. خواندن بیشتر در ما %2$@`
    - Source: `%1$@ cares about your privacy. Read more in our %2$@`
    - Suggest: `%1$@ به حریم خصوصی شما اهمیت می‌دهد. در %2$@ ما بیشتر بخوانید`
    - A key verb phrase remains in English and the possessive/word order is not Persian.
- `Onboarding.Modern.TermsOfService.PrivacyNoticeAgreement.v145` — `fa/firefox-ios.xliff` — "cares about" left untranslated and the sentence is ungrammatical Persian.
    - Current: `%1$@ cares about شما حریم خصوصی. خواندن بیشتر در ما %2$@`
    - Source: `%1$@ cares about your privacy. Read more in our %2$@`
    - Suggest: `%1$@ به حریم خصوصی شما اهمیت می‌دهد. در %2$@ ما بیشتر بخوانید`
    - A key verb phrase remains in English and the possessive/word order is not Persian.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.Title.v140` — `fa/firefox-ios.xliff` — "make" left untranslated and the sentence is ungrammatical.
    - Current: `کمک ما make %@ بهتر`
    - Source: `Help us make %@ better`
    - Suggest: `به ما کمک کنید %@ را بهتر کنیم`
    - The verb "make" remains English and the imperative "Help us make %@ better" is not conveyed grammatically.
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `fa/firefox-ios.xliff` — Three separate lines merged into one run-on and partly untranslated ("sites lightning").
    - Current: `بارگذاری sites lightning سریع خودکار ردیابی محافظت همگام‌سازی در همه شما دستگاه‌ها`
    - Source: `Load sites lightning fast Automatic tracking protection Sync on all your devices`
    - Suggest: `بارگذاری فوق‌سریع وبگاه‌ها محافظت خودکار در برابر ردیابی همگام‌سازی روی همهٔ دستگاه‌های شما`
    - The source has three distinct lines; the target runs them together and leaves "sites lightning" untranslated, making the text incomprehensible.
- `Onboarding.Modern.TermsOfService.TermsOfServiceAgreement.v140` — `fa/firefox-ios.xliff` — Mostly untranslated: "By continuing" and "agree" remain in English.
    - Current: `By continuing, شما agree به %@`
    - Source: `By continuing, you agree to the %@`
    - Suggest: `با ادامه دادن، شما با %@ موافقت می‌کنید`
    - Key parts of the source sentence are left in English.
- `Onboarding.Modern.TermsOfService.TermsOfServiceAgreement.v145` — `fa/firefox-ios.xliff` — Mostly untranslated: "By continuing" and "agree" remain in English.
    - Current: `By continuing, شما agree به %@`
    - Source: `By continuing, you agree to the %@`
    - Suggest: `با ادامه دادن، شما با %@ موافقت می‌کنید`
    - Key parts of the source sentence are left in English.
- `Onboarding.Modern.TermsOfService.Title.v140` — `fa/firefox-ios.xliff` — "Upgrade" left untranslated and phrase ungrammatical.
    - Current: `Upgrade شما مرور`
    - Source: `Upgrade your browsing`
    - Suggest: `مرور خود را ارتقا دهید`
    - The source verb is not translated and the possessive construction is not Persian.
- `Onboarding.Modern.TermsOfService.Title.v145` — `fa/firefox-ios.xliff` — "Take charge" left untranslated in the title.
    - Current: `Take chargeِ اینترنت`
    - Source: `Take charge of the internet`
    - Suggest: `کنترل اینترنت را به دست بگیرید`
    - The main verb phrase of "Take charge of the internet" is untranslated English with a stray Persian ezafe attached.
- `Onboarding.MultiDay.NotificationCard.BodyText.v159` — `fa/firefox-ios.xliff` — "protection updates" rendered as "security updates" (امنیتی) instead of protection/حفاظت.
    - Current: `به‌روزرسانی‌های امنیتی`
    - Source: `Get %@ protection updates, tips, and your privacy report.`
    - Suggest: `به‌روزرسانی‌های حفاظتی`
    - The source says "%@ protection updates" (updates about the browser's protections), not security updates; امنیتی means "security", a different claim about what the notifications contain.
- `Onboarding.Notification.Title.v120` — `fa/firefox-ios.xliff` — Title is garbled machine output mixing English and a mistranslated "No" fragment instead of translating "Notifications help you stay safer".
    - Current: `خیرtifications کمک شما stay safer با %@`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `اعلان‌ها به شما کمک می‌کنند با %@ ایمن‌تر بمانید`
    - "Notifications" was partially translated as «خیر» (no) plus the leftover "tifications", and "stay safer" is left in English; the string is unreadable in Persian.
- _…and 151 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Alerts.AddToCalendar.Body.v134` — `fa/firefox-ios.xliff` — Translation is broken machine output: contains untranslated English word "asking" and ungrammatical Persian.
    - Current: `%@ است asking به دریافت یک پرونده و افزودن یک رویداد به شما تقویم.`
    - Source: `%@ is asking to download a file and add an event to your calendar.`
    - Suggest: `%@ درخواست دارد یک پرونده دریافت کند و رویدادی به تقویم شما بیفزاید.`
    - The en-US says "%@ is asking to download a file and add an event to your calendar." The target leaves "asking" in English and has broken syntax ("به شما تقویم" instead of "به تقویم شما").
- `Alerts.AddToCalendar.BodyDefault.v134` — `fa/firefox-ios.xliff` — Translation is broken machine output: contains untranslated English word "asking" and ungrammatical Persian.
    - Current: `این وبگاه است asking به دریافت یک پرونده و افزودن یک رویداد به شما تقویم.`
    - Source: `This site is asking to download a file and add an event to your calendar.`
    - Suggest: `این وبگاه درخواست دارد یک پرونده دریافت کند و رویدادی به تقویم شما بیفزاید.`
    - The en-US says "This site is asking to download a file and add an event to your calendar." The target leaves "asking" in English and has broken word order ("به شما تقویم").
- `Alerts.FeltDeletion.Body.v122` — `fa/firefox-ios.xliff` — Ungrammatical word-by-word rendering with Latin commas instead of Persian commas.
    - Current: `بستن همه خصوصی زبانه‌ها و حذف کردن تاریخچه, کوکی‌ها, و همه دیگر وبگاه داده.`
    - Source: `Close all private tabs and delete history, cookies, and all other site data.`
    - Suggest: `بستن همهٔ زبانه‌های خصوصی و حذف تاریخچه، کوکی‌ها و همهٔ داده‌های دیگر وبگاه‌ها.`
    - The source "Close all private tabs and delete history, cookies, and all other site data." is rendered with English adjective order ("همه خصوصی زبانه‌ها", "همه دیگر وبگاه داده") which is not valid Persian, and uses ASCII commas instead of the Persian comma «،».
- `Settings.AppIconSelection.AppIconNames.BlueHour.Title.v137` — `fa/firefox-ios.xliff` — "Blue Hour" rendered with reversed Persian word order, yielding nonsense.
    - Current: `آبی ساعت`
    - Source: `Blue Hour`
    - Suggest: `ساعت آبی`
    - Persian noun-adjective order requires "ساعت آبی"; compare the correctly ordered "ساعت طلایی" for Golden Hour in the same screen.
- `Settings.AppIconSelection.AppIconNames.DarkPurple.Title.v136` — `fa/firefox-ios.xliff` — "Dark Purple" rendered with reversed word order.
    - Current: `تیره بنفش`
    - Source: `Dark Purple`
    - Suggest: `بنفش تیره`
    - In Persian the modifier follows the noun/colour: "بنفش تیره" means dark purple; "تیره بنفش" is ungrammatical.
- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `fa/firefox-ios.xliff` — Stray English "d" suffix attached to the Persian verb, and non-guillemet quotes.
    - Current: `ذخیرهd در “نشانک‌ها”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `در «نشانک‌ها» ذخیره شد`
    - "Saved" was partially replaced leaving "ذخیرهd", which is not a Persian word; the locale convention is guillemets, as used in Bookmarks.Menu.DeletedBookmark.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `fa/firefox-ios.xliff` — Stray English "d" suffix attached to the Persian verb, and non-guillemet quotes.
    - Current: `ذخیرهd در “%@”`
    - Source: `Saved in “%@”`
    - Suggest: `در «%@» ذخیره شد`
    - "Saved" was partially replaced leaving "ذخیرهd", which is not a Persian word; the locale convention is guillemets.
- `CameraAccess.DisabledAlertMessage.v153` — `fa/firefox-ios.xliff` — The Persian text is ungrammatical word-salad, apparently machine-generated, and does not convey the source instruction.
    - Current: `رفتن به تنظیمات > %@ در شما دستگاه به اجازه Firefox به استفاده شما دوربین.`
    - Source: `Go to Settings > %@ on your device to allow Firefox to use your camera.`
    - Suggest: `در دستگاه خود به تنظیمات > %@ بروید تا به Firefox اجازه دهید از دوربین شما استفاده کند.`
    - The source says "Go to Settings > %@ on your device to allow Firefox to use your camera." The target is a literal word-by-word rendering with wrong word order and wrong particles ("در شما دستگاه", "به اجازه", "استفاده شما دوربین"), which is not comprehensible Persian.
- `ContextualHints.Translations.Title.v145` — `fa/firefox-ios.xliff` — Untranslated English word "Speaks" left in the string and word order is ungrammatical.
    - Current: `%@ Speaks شما زبان`
    - Source: `%@ Speaks Your Language`
    - Suggest: `%@ به زبان شما صحبت می‌کند`
    - The source "%@ Speaks Your Language" should be fully translated; "Speaks" remains in English and "شما زبان" is an incorrect possessive construction.
- `Settings.Home.Option.ThoughtProvokingStories.subtitle.v116` — `fa/firefox-ios.xliff` — The English word "by" is left untranslated inside the Persian string.
    - Current: `مقاله‌ها ارائه‌شده by %@`
    - Source: `Articles powered by %@`
    - Suggest: `مقاله‌ها ارائه‌شده توسط %@`
    - Source "Articles powered by %@"; the preposition "by" was not translated into Persian.
- `Addresses.EditAddress.Alert.Title.v129` — `fa/firefox-ios.xliff` — Corrupted translation: "Address" was partially translated leaving the mangled token "افزودنress".
    - Current: `حذف افزودنress`
    - Source: `Remove Address`
    - Suggest: `حذف نشانی`
    - Source is "Remove Address"; the target reads "حذف افزودنress", where "Add" was replaced by "افزودن" inside the word "Address", producing nonsense.
- `Addresses.EditAddress.RemoveAddressButtonTitle.v129` — `fa/firefox-ios.xliff` — Translation contains a corrupted mix of Persian and leftover English characters instead of "Remove Address".
    - Current: `حذف افزودنress`
    - Source: `Remove Address`
    - Suggest: `حذف نشانی`
    - The source is "Remove Address"; the target reads "delete add-ress" with a stray English fragment "ress" and the wrong word "افزودن" (add).
- `Menu.EnhancedTrackingProtection.Certificates.IssuerName.v131` — `fa/firefox-ios.xliff` — "صادرکننده نام" reverses the Persian noun-modifier order; it should be "نام صادرکننده".
    - Current: `صادرکننده نام`
    - Source: `Issuer Name`
    - Suggest: `نام صادرکننده`
    - Persian ezafe order puts the head noun first: "Issuer Name" = "نام صادرکننده". As written it reads "issuer name" word-by-word in English order and is ungrammatical.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNames.v131` — `fa/firefox-ios.xliff` — "موضوع Alt نامs" contains a stray English plural "s" attached to the Persian word and wrong word order.
    - Current: `موضوع Alt نامs`
    - Source: `Subject Alt Names`
    - Suggest: `نام‌های جایگزین موضوع`
    - The English plural suffix "s" has been appended to the Persian "نام", and the phrase keeps English word order; the result is not valid Persian.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNamesDNSName.v131` — `fa/firefox-ios.xliff` — "DNS نام" uses English word order; Persian requires "نام DNS".
    - Current: `DNS نام`
    - Source: `DNS Name`
    - Suggest: `نام DNS`
    - In Persian the head noun precedes the modifier, so "DNS Name" is "نام DNS".
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `fa/firefox-ios.xliff` — "موضوع نام" reverses the Persian word order; it should be "نام موضوع".
    - Current: `موضوع نام`
    - Source: `Subject Name`
    - Suggest: `نام موضوع`
    - Persian ezafe order requires the head noun "نام" first: "Subject Name" = "نام موضوع".
- `Menu.EnhancedTrackingProtection.On.Title.v128` — `fa/firefox-ios.xliff` — Ungrammatical word-salad rendering of "%@ is on guard".
    - Current: `%@ است در محافظ`
    - Source: `%@ is on guard`
    - Suggest: `%@ نگهبانی می‌دهد`
    - The Persian "%@ است در محافظ" is not grammatical Persian word order and does not convey "is on guard".
- `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `fa/firefox-ios.xliff` — Untranslated English fragment "’re" left inside the Persian string, producing broken text.
    - Current: `شما’re محافظت‌شده`
    - Source: `You’re Protected`
    - Suggest: `شما محافظت می‌شوید`
    - The source "You’re Protected" was machine-mangled; the English contraction remnant "’re" remains in the Persian text.
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v153b` — `fa/firefox-ios.xliff` — Ungrammatical word-for-word rendering of "Trackers Blocked".
    - Current: `ردیاب‌ها مسدود: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ردیاب‌های مسدودشده: %@`
    - "ردیاب‌ها مسدود" is not grammatical Persian; the adjective/participle must agree via ezafe as "ردیاب‌های مسدودشده".
- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v155` — `fa/firefox-ios.xliff` — Ungrammatical word-for-word rendering of "Trackers Blocked".
    - Current: `ردیاب‌ها مسدود: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `ردیاب‌های مسدودشده: %@`
    - "ردیاب‌ها مسدود" is not grammatical Persian; it needs ezafe and the participle form.
- `LoginsList.Title.v122` — `fa/firefox-ios.xliff` — Word order reversed: adjective placed before the noun, which is ungrammatical in Persian.
    - Current: `ذخیره‌شده گذرواژه‌ها`
    - Source: `SAVED PASSWORDS`
    - Suggest: `گذرواژه‌های ذخیره‌شده`
    - Persian places the modifier after the noun with ezafe; "ذخیره‌شده گذرواژه‌ها" is a literal English word order.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `fa/firefox-ios.xliff` — Partially untranslated and ungrammatical: English "by" left in, and "خانواده" misplaced.
    - Current: `ارائه‌شده by %1$@. بخشِ %2$@ خانواده.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `ارائه‌شده توسط %1$@. بخشی از خانوادهٔ %2$@.`
    - The English preposition "by" remains untranslated and the second sentence has English word order, making it unreadable in Persian.
- `CloseTab.ArrivingNotification.title.v133` — `fa/firefox-ios.xliff` — Ungrammatical literal word order for "%1$@ tabs closed".
    - Current: `%1$@ زبانه‌ها بسته‌شده: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `زبانه‌های بسته‌شدهٔ %1$@: %2$@`
    - The Persian lacks ezafe linking and copies English word order, yielding ungrammatical text.
- `ContextualHints.FirefoxHomepage.JumpBackIn.PersonalizedHome` — `fa/firefox-ios.xliff` — String is largely untranslated/garbled, with English words, English commas, and a missing space ("resultsخواهد").
    - Current: `Meet شما شخصی‌سازی‌شده صفحهٔ اصلی. اخیر زبانه‌ها, نشانک‌ها, و جست‌و‌جو resultsخواهد ظاهر می‌شوند here.`
    - Source: `Meet your personalized homepage. Recent tabs, bookmarks, and search results will appear here.`
    - Suggest: `با صفحهٔ اصلی شخصی‌سازی‌شدهٔ خود آشنا شوید. زبانه‌های اخیر، نشانک‌ها و نتایج جست‌وجو اینجا ظاهر می‌شوند.`
    - Mixed English ("Meet", "results", "here"), broken word order and a missing space make the hint unreadable.
- `KeyboardAccessory.NextButton.Accessibility.Label.v124` — `fa/firefox-ios.xliff` — Partially untranslated: "form field" left in English.
    - Current: `بعدی form field`
    - Source: `Next form field`
    - Suggest: `فیلد بعدی فرم`
    - The source "Next form field" is only half-translated; the English words remain.
- `KeyboardAccessory.PreviousButton.Accessibility.Label.v124` — `fa/firefox-ios.xliff` — Partially untranslated: "form field" left in English.
    - Current: `قبلی form field`
    - Source: `Previous form field`
    - Suggest: `فیلد قبلی فرم`
    - The source "Previous form field" is only half-translated; the English words remain.
- `MainMenu.Account.SyncError.Description.v131` — `fa/firefox-ios.xliff` — "Syncing paused" rendered with a redundant progressive phrase that contradicts itself.
    - Current: `در حال همگام‌سازی متوقف‌شده`
    - Source: `Syncing paused`
    - Suggest: `همگام‌سازی متوقف شد`
    - "در حال همگام‌سازی" means "syncing in progress", which conflicts with "متوقف‌شده" (paused); the source states that syncing is paused.
- `MainMenu.SettingsSection.AccessibilityLabels.CustomizeHomepage.v132` — `fa/firefox-ios.xliff` — Hybrid word "سفارشیize" contains a stray English suffix.
    - Current: `سفارشیize صفحهٔ اصلی`
    - Source: `Customize Homepage`
    - Suggest: `سفارشی‌سازی صفحهٔ اصلی`
    - "Customize" was partly machine-translated, leaving "ize" attached to the Persian word.
- `MainMenu.SettingsSection.CustomizeHomepage.Title.v131` — `fa/firefox-ios.xliff` — Untranslated English fragment "ize" left inside the Persian word, producing "سفارشیize".
    - Current: `سفارشیize صفحهٔ اصلی`
    - Source: `Customize Homepage`
    - Suggest: `سفارشی‌سازی صفحهٔ اصلی`
    - The source is "Customize Homepage"; the target contains a corrupted hybrid word mixing Persian "سفارشی" with the English suffix "ize".
- `Microsurvey.Survey.PrivacyPolicyLink.v127` — `fa/firefox-ios.xliff` — The word "notice" is left untranslated, producing a mixed English/Persian string.
    - Current: `حریم خصوصی notice`
    - Source: `Privacy notice`
    - Suggest: `اعلامیهٔ حریم خصوصی`
    - en-US "Privacy notice" must be fully translated; "notice" remains in English.
- `NativeErrorPage.NoInternetConnection.Description.v131` — `fa/firefox-ios.xliff` — Translation is partly untranslated and ungrammatical word-for-word Persian.
    - Current: `تلاش کنید connecting در یک متفاوت دستگاه. بررسی شما مودم یا مسیریاب. قطع اتصال و اتصال مجدد به Wi-Fi.`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `اتصال با دستگاهی دیگر را امتحان کنید. مودم یا مسیریاب خود را بررسی کنید. اتصال Wi-Fi را قطع و دوباره وصل کنید.`
    - "connecting" is left in English and the syntax ("بررسی شما مودم", "یک متفاوت دستگاه") is not grammatical Persian.
- `NativeErrorPage.NoInternetConnection.TitleLabel.v131` — `fa/firefox-ios.xliff` — String is largely untranslated and ungrammatical, including a stray apostrophe.
    - Current: `Looks like وجود دارد’ یک مشکل با شما اینترنت اتصال.`
    - Source: `Looks like there’s a problem with your internet connection.`
    - Suggest: `به نظر می‌رسد مشکلی در اتصال اینترنت شما وجود دارد.`
    - en-US "Looks like there’s a problem with your internet connection." is rendered with untranslated English and broken Persian word order.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `fa/firefox-ios.xliff` — String left in English instead of being translated.
    - Current: `Checking Archive…`
    - Source: `Checking the Archive…`
    - Suggest: `در حال بررسی بایگانی…`
    - en-US "Checking the Archive…" is a user-visible button label and should be in Persian, as elsewhere in the file "archive" is "بایگانی".
- `Onboarding.Customization.Intro.Continue.Action.v123` — `fa/firefox-ios.xliff` — Half-translated word "سفارشیize" mixes Persian and English.
    - Current: `سفارشیize %@`
    - Source: `Customize %@`
    - Suggest: `شخصی‌سازی %@`
    - "Customize" was partly translated leaving the English suffix "ize" attached, producing a nonsense word.
- `Onboarding.Customization.Intro.Title.v123` — `fa/firefox-ios.xliff` — English verb "puts" left untranslated.
    - Current: `%@ puts شما در کنترل`
    - Source: `%@ puts you in control`
    - Suggest: `%@ کنترل را به شما می‌دهد`
    - The source "%@ puts you in control" is only partly translated, leaving the English verb in the Persian sentence.
- `Onboarding.Customization.Theme.Title.v123` — `fa/firefox-ios.xliff` — Ungrammatical English word order in Persian title.
    - Current: `انتخاب کنید یک پوسته`
    - Source: `Pick a theme`
    - Suggest: `یک پوسته انتخاب کنید`
    - Persian places the object before the verb; the literal English order is ungrammatical.
- `Onboarding.Customization.Theme.Title.v143` — `fa/firefox-ios.xliff` — Ungrammatical word order and wrong possessive form for "your theme".
    - Current: `انتخاب کنید شما پوسته`
    - Source: `Choose your theme`
    - Suggest: `پوستهٔ خود را انتخاب کنید`
    - "شما پوسته" is an English-style possessive that is ungrammatical in Persian, and the verb is misplaced.
- `Onboarding.Customization.Toolbar.Title.v123` — `fa/firefox-ios.xliff` — Ungrammatical English word order for "Pick a toolbar placement".
    - Current: `انتخاب کنید یک نوار ابزار جایگاه`
    - Source: `Pick a toolbar placement`
    - Suggest: `جایگاه نوار ابزار را انتخاب کنید`
    - The noun phrase and verb follow English order, which is ungrammatical in Persian.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Title.v148` — `fa/firefox-ios.xliff` — Word-for-word machine rendering produces ungrammatical Persian for "Pick your theme".
    - Current: `انتخاب کنید شما پوسته`
    - Source: `Pick your theme`
    - Suggest: `پوستهٔ خود را انتخاب کنید`
    - The source "Pick your theme" is rendered with English word order, yielding broken Persian syntax.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Title.v148` — `fa/firefox-ios.xliff` — "Choose your address bar" is rendered with English word order and a reversed compound, producing ungrammatical Persian.
    - Current: `انتخاب کنید شما نشانی نوار`
    - Source: `Choose your address bar`
    - Suggest: `نوار نشانی خود را انتخاب کنید`
    - "نشانی نوار" reverses the Persian compound "نوار نشانی" and the sentence order is not Persian.
- `Onboarding.Modern.BrandRefresh.Notification.TurnOn.Action.v148` — `fa/firefox-ios.xliff` — "Turn on notifications" rendered literally as "روشن در اعلان‌ها", which is not Persian.
    - Current: `روشن در اعلان‌ها`
    - Source: `Turn on notifications`
    - Suggest: `روشن کردن اعلان‌ها`
    - The phrasal verb "turn on" was translated word-by-word ("on" → "در"), producing a meaningless button label.
- `Onboarding.Modern.Customization.Theme.Title.v145` — `fa/firefox-ios.xliff` — Word-for-word machine rendering produces ungrammatical Persian for "Pick your theme".
    - Current: `انتخاب کنید شما پوسته`
    - Source: `Pick your theme`
    - Suggest: `پوستهٔ خود را انتخاب کنید`
    - The source "Pick your theme" is rendered with English word order, yielding broken Persian syntax.
- `Onboarding.Modern.Customization.Toolbar.Title.v145` — `fa/firefox-ios.xliff` — Ungrammatical literal word-by-word rendering of "Choose your address bar".
    - Current: `انتخاب کنید شما نشانی نوار`
    - Source: `Choose your address bar`
    - Suggest: `نوار نشانی خود را انتخاب کنید`
    - Persian requires the possessive and noun-adjective order; "شما نشانی نوار" is not grammatical Persian.
- `Onboarding.Modern.Sync.Description.v140` — `fa/firefox-ios.xliff` — Ungrammatical word-for-word rendering with Latin commas instead of Persian commas.
    - Current: `دریافت شما نشانک‌ها, تاریخچه, و گذرواژه‌ها در هر دستگاه.`
    - Source: `Get your bookmarks, history, and passwords on any device.`
    - Suggest: `نشانک‌ها، تاریخچه و گذرواژه‌های خود را روی هر دستگاهی دریافت کنید.`
    - "دریافت شما نشانک‌ها" is not Persian grammar, and Latin commas are used instead of the Persian comma «،».
- `Onboarding.Modern.Sync.Skip.Action.v140` — `fa/firefox-ios.xliff` — Corrupted rendering "خیرt" for "Not now".
    - Current: `خیرt اکنون`
    - Source: `Not now`
    - Suggest: `اکنون نه`
    - The English "Not" was partially replaced leaving a stray Latin "t"; the result is not a valid Persian phrase.
- `Onboarding.Modern.Sync.Skip.Action.v145` — `fa/firefox-ios.xliff` — Corrupted rendering "خیرt" for "Not now".
    - Current: `خیرt اکنون`
    - Source: `Not now`
    - Suggest: `اکنون نه`
    - The English "Not" was partially replaced leaving a stray Latin "t"; the result is not a valid Persian phrase.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendCrashReportsTitle.v140` — `fa/firefox-ios.xliff` — Corrupted hybrid word "خودکارally" and ungrammatical word order.
    - Current: `خودکارally ارسال خرابی گزارش‌ها`
    - Source: `Automatically send crash reports`
    - Suggest: `ارسال خودکار گزارش‌های خرابی`
    - "Automatically" was partially replaced leaving the English suffix "ally"; noun phrase order is also wrong.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataTitle.v140` — `fa/firefox-ios.xliff` — Corrupted word "datیک" for "data" and ungrammatical phrase order.
    - Current: `ارسال فنی و تعامل datیک به %@`
    - Source: `Send technical and interaction data to %@`
    - Suggest: `ارسال داده‌های فنی و تعاملی به %@`
    - "data" was mangled into "datیک" and the adjectives are not attached to a noun in Persian order.
- `Onboarding.TermsOfService.PrivacyPreferences.SendCrashReportsTitle.v135` — `fa/firefox-ios.xliff` — Title contains the untranslated English suffix "ally" and reversed word order.
    - Current: `خودکارally ارسال خرابی گزارش‌ها`
    - Source: `Automatically send crash reports`
    - Suggest: `ارسال خودکار گزارش‌های خرابی`
    - "Automatically" was half-translated as «خودکارally» and "crash reports" is rendered in English word order, producing invalid Persian.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataTitle.v135` — `fa/firefox-ios.xliff` — Title contains the nonsense word «datیک» instead of «داده‌ها».
    - Current: `ارسال فنی و تعامل datیک به %@`
    - Source: `Send technical and interaction data to %@`
    - Suggest: `ارسال داده‌های فنی و تعاملی به %@`
    - "data" was not translated and appears as a garbled mix of Latin and Persian letters.
- `Onboarding.TermsOfService.Subtitle.v136` — `fa/firefox-ios.xliff` — Subtitle uses English word order producing ungrammatical Persian.
    - Current: `سریع و امن وب مرور`
    - Source: `Fast and secure web browsing`
    - Suggest: `مرور سریع و امن وب`
    - A literal word-for-word rendering of "Fast and secure web browsing" that is not valid Persian syntax.
- `PasswordAutofill.UseSavedPasswordFromHeader.v124` — `fa/firefox-ios.xliff` — Word order is English-style and ungrammatical in Persian.
    - Current: `استفاده ذخیره‌شده گذرواژه؟`
    - Source: `Use saved password?`
    - Suggest: `از گذرواژهٔ ذخیره‌شده استفاده شود؟`
    - Persian requires noun before adjective and a proper verb phrase; the current string is a word-by-word calque.
- `PasswordAutofill.UseSavedPasswordFromKeyboard.v124` — `fa/firefox-ios.xliff` — Word order is English-style and ungrammatical in Persian.
    - Current: `استفاده ذخیره‌شده گذرواژه`
    - Source: `Use saved password`
    - Suggest: `استفاده از گذرواژهٔ ذخیره‌شده`
    - Word-by-word calque; Persian needs noun-adjective order and the preposition "از".
- `PasswordGenerator.UsePasswordButtonLabel.v132` — `fa/firefox-ios.xliff` — Missing preposition; ungrammatical Persian.
    - Current: `استفاده گذرواژه`
    - Source: `Use Password`
    - Suggest: `استفاده از گذرواژه`
    - Persian requires "از" after "استفاده"; the current form is a calque of English.
- `PrivacyDashboard.Fingerprinters.v155` — `fa/firefox-ios.xliff` — Misspelling of "کنندگان".
    - Current: `برداشت کنندگاه اثر انگشت`
    - Source: `Fingerprinters`
    - Suggest: `برداشت‌کنندگان اثر انگشت`
    - "کنندگاه" is not a word; the correct plural agent form is "کنندگان".
- `PrivacyDashboard.HeaderLabel.v155` — `fa/firefox-ios.xliff` — Ungrammatical calque; missing participle form "مسدودشده".
    - Current: `ردیاب‌ها مسدود این هفته`
    - Source: `Trackers blocked this week`
    - Suggest: `ردیاب‌های مسدودشده در این هفته`
    - "ردیاب‌ها مسدود این هفته" is not grammatical Persian for "Trackers blocked this week".
- `PrivacyDashboard.HeaderLabelAccessibilityLabel.v156` — `fa/firefox-ios.xliff` — Ungrammatical calque; missing participle form "مسدودشده".
    - Current: `ردیاب‌ها مسدود این هفته: %@`
    - Source: `Trackers blocked this week: %@`
    - Suggest: `ردیاب‌های مسدودشده در این هفته: %@`
    - Same broken construction as the header label; not grammatical Persian.
- `QuickAnswers.AccessibilityLabels.OpenQuickAnswers.v158` — `fa/firefox-ios.xliff` — Adjective-noun order reversed: "سریع پاسخ‌ها" instead of "پاسخ‌های سریع".
    - Current: `باز کردن سریع پاسخ‌ها`
    - Source: `Open Quick Answers`
    - Suggest: `باز کردن پاسخ‌های سریع`
    - Persian puts the adjective after the noun; the current text reads as "quickly opening answers".
- `QuickAnswers.ContentView.SearchingSources.v158` — `fa/firefox-ios.xliff` — English "-ing" suffix appended to a Persian word.
    - Current: `جست‌و‌جوing منابع…`
    - Source: `Searching sources…`
    - Suggest: `در حال جست‌وجوی منابع…`
    - "جست‌و‌جوing" is a corrupted hybrid of Persian and English morphology.
- `QuickAnswers.Errors.DailyLimitMessage.v158` — `fa/firefox-ios.xliff` — Word-by-word machine rendering with broken Persian word order and untranslated feature name structure.
    - Current: `تلاش کنید سریع پاسخ‌ها دوباره فردا.`
    - Source: `Try Quick Answers again tomorrow.`
    - Suggest: `فردا دوباره پاسخ‌های سریع را امتحان کنید.`
    - The en-US 'Try Quick Answers again tomorrow.' is rendered as ungrammatical Persian with English word order; 'سریع پاسخ‌ها' also reverses the Persian noun-adjective order.
- _…and 167 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Switch.Title.v128` — `fa/firefox-ios.xliff` — "Enhanced Tracking Protection" mistranslated as "optimizing protection from followers" and inconsistent with «ردیاب» used elsewhere in this file.
    - Current: `بهینه سازی محافظت از دنبال کنندگان`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `محافظت پیشرفته در برابر ردیابی`
    - The source names the feature "Enhanced Tracking Protection"; the target says "optimization of protection of/from followers", uses a different term for trackers than the rest of the screen, and reads as protecting trackers rather than from them.
- `RelayMask.RelayEmailMaskInsertedA11yAnnouncement.v147` — `fa/firefox-ios.xliff` — 'رایانامه پوشان درج‌شده' uses reversed compound order inconsistent with the rest of the file.
    - Current: `رایانامه پوشان درج‌شده`
    - Source: `Email mask inserted`
    - Suggest: `پوشان رایانامه درج شد`
    - Other strings in the same file use 'پوشان رایانامه'; the current order is an English calque.
- `RelayMask.RelayEmailMaskSettingsManageEmailMasks.v146` — `fa/firefox-ios.xliff` — 'رایانامه پوشان‌ها' reverses the compound order used elsewhere in the same file.
    - Current: `مدیریت رایانامه پوشان‌ها`
    - Source: `Manage Email Masks`
    - Suggest: `مدیریت پوشان‌های رایانامه`
    - Other strings in RelayMask.strings use 'پوشان‌های رایانامه'; this one is inconsistent and ungrammatical.
- `RelayMask.RelayEmailMaskSettingsTitle.v146` — `fa/firefox-ios.xliff` — 'رایانامه پوشان‌ها' reverses the compound order used elsewhere in the same file.
    - Current: `رایانامه پوشان‌ها`
    - Source: `Email Masks`
    - Suggest: `پوشان‌های رایانامه`
    - Inconsistent with 'پوشان‌های رایانامه' used in other strings of the same settings screen, and not grammatical Persian.
- `SearchZero.TrendingSearches.SectionTitle.v146` — `fa/firefox-ios.xliff` — "Trending" rendered as the non-word "رونددار".
    - Current: `رونددار در %@`
    - Source: `Trending on %@`
    - Suggest: `پرطرفدار در %@`
    - "رونددار" is not an established Persian term for "trending"; standard renderings are "پرطرفدار" or "داغ".
- `DefaultBrowserOnboarding.Description1` — `fa/firefox-ios.xliff` — Informal imperative "برو" conflicts with the formal imperative used in the sibling steps ("لمس کنید", "انتخاب کنید").
    - Current: `۱. برو به تنظیمات`
    - Source: `1. Go to Settings`
    - Suggest: `۱. به تنظیمات بروید`
    - The two following onboarding steps use the formal plural imperative; this step uses the informal singular, an inconsistent register on the same card.
- `ClipboardToast.GoToCopiedLink.Title` — `fa/firefox-ios.xliff` — Colloquial/spoken register ("بریم") instead of the standard formal written form used throughout the UI.
    - Current: `به پیوند رونوشت‌شده بریم؟`
    - Source: `Go to copied link?`
    - Suggest: `به پیوند رونوشت‌شده بروید؟`
    - All other strings in this file use formal written Persian; "بریم" is informal colloquial and breaks the established register.
- `Downloads.Alert.DownloadNow` — `fa/firefox-ios.xliff` — Button label rendered as a full imperative sentence instead of a short action label.
    - Current: `هم‌اکنون دریافت کنید`
    - Source: `Download Now`
    - Suggest: `هم‌اکنون دریافت`
    - The comment identifies it as a button label; other download buttons here use noun forms ("لغو دریافت").
- `Logins.PasscodeRequirement.Warning` — `fa/firefox-ios.xliff` — "device passcode" translated as رمز عبور (password) rather than the passcode term.
    - Current: `باید رمز عبور دستگاه را فعال کرده باشید`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `باید رمز عبور (گذرواژه) دستگاه را فعال کرده باشید`
    - The file consistently uses گذرواژه for password; passcode should be distinguished, e.g. رمز دستگاه, to avoid confusion with Firefox passwords discussed in the same screen.
- `Menu.EnhancedTrackingProtectionOff.Title` — `fa/firefox-ios.xliff` — "site" translated as پایگاه instead of the standard سایت used elsewhere in the same file.
    - Current: `محافظت‌ها برای این پایگاه‌ خاموش است`
    - Source: `Protections are OFF for this site`
    - Suggest: `محافظت‌ها برای این سایت خاموش است`
    - LibraryPanel.History.ClearGroupedTabsTitle renders "sites" as سایت‌ها; using پایگاه here (plus a stray ZWNJ before the space) is inconsistent terminology on related screens.
- `Menu.EnhancedTrackingProtectionOn.Title` — `fa/firefox-ios.xliff` — "site" translated as پایگاه instead of the standard سایت used elsewhere in the same file.
    - Current: `محافظت‌ها برای این پایگاه‌ روشن است`
    - Source: `Protections are ON for this site`
    - Suggest: `محافظت‌ها برای این سایت روشن است`
    - Inconsistent with سایت used in other strings of this file; also contains a stray ZWNJ before the space.
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

- `Settings.AutofillAndPassword.Title.v137` — `fa/firefox-ios.xliff` — The ampersand is kept instead of the Persian conjunction "و".
    - Current: `پرکردن‌های خودکار & گذرواژه‌ها`
    - Source: `Autofills & Passwords`
    - Suggest: `پرکردن‌های خودکار و گذرواژه‌ها`
    - In Persian the "&" is not used as a conjunction; it should be rendered as "و".
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `fa/firefox-ios.xliff` — Stray standalone ezāfe diacritic with spaces in "دور ِ 16".
    - Current: `دور ِ 16`
    - Source: `ROUND OF 16`
    - Suggest: `دور ۱۶ تیمی`
    - The kasra is written as a separate character surrounded by spaces, which is not valid Persian typography; the phrase for 'Round of 16' is "دور ۱۶ تیمی" / "یک‌هشتم نهایی".
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `fa/firefox-ios.xliff` — Stray standalone ezāfe diacritic with spaces in "دور ِ 32".
    - Current: `دور ِ 32`
    - Source: `ROUND OF 32`
    - Suggest: `دور ۳۲ تیمی`
    - The kasra is written as a separate space-delimited character, which is invalid Persian typography.
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

### Fixed to date (38)

- `Use your fingerprint to access Logins now.` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `This action will clear all of your private data, including history from your synced devices.` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `DefaultBrowserCard.Description` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `DefaultBrowserCard.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `DefaultBrowserOnboarding.Description1` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `DefaultBrowserOnboarding.Description2` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `AddPass.Error.Message` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `AddPass.Error.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `BreachAlerts.Description` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Changes font type.` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ContextMenu.BookmarkLinkButtonTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ContextMenu.CopyImageButtonTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ContextMenu.OpenInNewTabButtonTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `CoverSheet.v24.ETP.Description` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Downloads.CancelDialog.Message` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Downloads.CancelDialog.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Downloads.Toast.Cancelled.LabelText` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Downloads.Toast.Failed.LabelText` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Downloads.Toast.MultipleFiles.DescriptionText` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ErrorPages.VisitOnce.Button` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ExternalLink.AppStore.GenericConfirmationTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `HistoryPanel.ClearHistoryMenuOptionTheLastHour` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `HistoryPanel.EmptyState.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Hotkeys.CloseTab.DiscoveryTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Hotkeys.PrivateMode.DiscoveryTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `InactiveTabs.TabTray.CloseButtonTitle` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Light` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Logins` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Menu.AddToReadingList.Confirm` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Menu.Copy.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `SendTo.NoDevicesFound.Message` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Settings.ClearAllWebsiteData.Clear.Button` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Settings.Disconnect.Body` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Settings.SendUsage.Message` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `Settings.WebsiteData.ConfirmPrompt` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `ShareExtension.SeachInFirefoxAction.Title` — `fa/firefox-ios.xliff` — fixed 2026-10-05
- `You don’t have any tabs open in Firefox on your other devices.` — `fa/firefox-ios.xliff` — fixed 2026-10-05
