# Firefox iOS l10n QA — ar

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | baseline |
| **Strings reviewed this run** | 1,175 of 1,175 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ar: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (51)

- `Settings.AppIconSelection.AppIconNames.Pixelated.Title.v136` — `ar/firefox-ios.xliff` — "مبلورة" means "crystallized", not "pixelated", and its feminine form doesn't match the other masculine icon names.
    - Current: `مبلورة`
    - Source: `Pixelated`
    - Suggest: `مُبكسَل`
    - The comment describes a pixelated version of the icon. مبلورة (from بلورة, crystal) means crystallized or clarified, so it names the wrong visual style. The feminine form also clashes with the masculine adjectives used for the other icon names (أزرق، مشتعل، مبسط).
- `Addresses.BottomSheet.UseSavedAddressBottomSheet.v124` — `ar/firefox-ios.xliff` — The object of the verb «استخدِم» needs the accusative ending, but it is written without it.
    - Current: `عنوان محفوظ`
    - Source: `Use a saved address?`
    - Suggest: `عنوانًا محفوظًا`
    - «عنوان محفوظ» is the object of «استخدِم», so it needs the accusative ending with tanween: «عنوانًا محفوظًا».
- `Bookmarks.Menu.DeletedBookmark.v131` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“%@”`
    - Source: `Deleted “%@”`
    - Suggest: `«%@»`
    - Guillemets are the established quotation marks for this locale.
- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“العلامات المرجعية”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `«العلامات المرجعية»`
    - Guillemets are the established quotation marks for this locale.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“%@”`
    - Source: `Saved in “%@”`
    - Suggest: `«%@»`
    - Guillemets are the established quotation marks for this locale.
- `Addresses.EditAddress.AutofillAddAddressTitle.v129` — `ar/firefox-ios.xliff` — The imperative 'Add' is misspelled as ضِف instead of أضِف, and the object lacks the accusative ending.
    - Current: `ضِف عنوان`
    - Source: `Add address`
    - Suggest: `أضِف عنوانًا`
    - The imperative of أضاف (to add) is أضِف. ضِف comes from ضاف (to host a guest), so it is a spelling error. The object should also take the accusative: عنوانًا.
- `Addresses.EditAddress.AutofillAddressName.v129` — `ar/firefox-ios.xliff` — اسم is written with a hamza on the alif (الإِسم), which is a spelling error.
    - Current: `الإِسم`
    - Source: `Name`
    - Suggest: `الاسم`
    - The alif in اسم is a connecting alif (hamzat wasl) and takes no hamza. The correct form is الاسم.
- `Addresses.Toast.AddressRemovedConfirmation.v129` — `ar/firefox-ios.xliff` — The verb doesn't agree with its feminine subject: تم should be تمت before إزالة.
    - Current: `تم إزالة العنوان`
    - Source: `Address Removed`
    - Suggest: `تمت إزالة العنوان`
    - إزالة is a feminine verbal noun and the subject of تم, so the verb should be feminine: تمت.
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `ar/firefox-ios.xliff` — The verb بدا ("looked/seemed") is misspelled as بدى.
    - Current: `بدى`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `بدا`
    - This verb's root ends in waw (يبدو), so the past tense is written with alif: بدا. Writing بدى is a common spelling error.
- `Notification.Fallback.Title.v113` — `ar/firefox-ios.xliff` — The app name comes before the noun in English order, which is ungrammatical in Arabic.
    - Current: `%@ نصيحة`
    - Source: `%@ Tip`
    - Suggest: `نصيحة من %@`
    - The source means 'Tip from Firefox'. In Arabic the noun comes first in this kind of phrase (نصيحة %@ or نصيحة من %@). Putting %@ before نصيحة copies the English order and reads ungrammatically.
- `Search.EngineSection.Title.v108` — `ar/firefox-ios.xliff` — Word order follows English; in Arabic the engine name must follow 'بحث' as the second term of the construct.
    - Current: `%@ بحث`
    - Source: `%@ search`
    - Suggest: `بحث %@`
    - The source means '<engine> search'. Arabic puts the head noun first (بحث جوجل), as this locale already does in Search.Google.Title.v108. Putting the name first gives an ungrammatical 'Google بحث'. The string has a single %@, so moving it is safe.
- `This action will clear all of your private data, including history from your synced devices.` — `ar/firefox-ios.xliff` — Translation says all private data is erased from synced devices, whereas the source says all private data is cleared, including history from synced devices.
    - Current: `سيمحي هذا الإجراء كل بياناتك الخاصة من الأجهزة المتزامنة، بما في ذلك التأريخ.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `سيمحي هذا الإجراء كل بياناتك الخاصة، بما في ذلك التأريخ من أجهزتك المتزامنة.`
    - In the source only history comes from the synced devices. The ar attaches 'from the synced devices' to all private data, which tells the user that far more will be deleted on other devices than the product does.
- `DefaultBrowserCard.NextLevel.Title.v108` — `ar/firefox-ios.xliff` — The imperative is in the feminine form (اِرتَقي), unlike the masculine address used everywhere else.
    - Current: `اِرتَقي`
    - Source: `Elevate Everyday Browsing`
    - Suggest: `ارتقِ`
    - The masculine imperative of ارتقى is ارتقِ. ارتقي is feminine, which clashes with the locale's masculine address (اختر, استأنف).
- `DefaultBrowserCard.BetterInternet.Title.v108` — `ar/firefox-ios.xliff` — 'Default' is rendered as الدائم ('permanent') instead of the established الافتراضي, and the pronoun in جعله has no antecedent.
    - Current: `جعله متصفحك الدائم`
    - Source: `Default to a Better Internet`
    - Suggest: `جعل Firefox متصفحك الافتراضي`
    - The sibling banner strings on the same screen render 'default browser' as المتصفح الافتراضي. الدائم means 'permanent', which is a different concept.
- `A username and password are being requested by %@.` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to the next word.
    - Current: `و كلمة السر`
    - Source: `A username and password are being requested by %@.`
    - Suggest: `وكلمة السر`
    - In Arabic spelling, the conjunction و is always attached to the word that follows it.
- `A username and password are being requested by %@. The site says: %@` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to the next word.
    - Current: `و كلمة السر`
    - Source: `A username and password are being requested by %1$@. The site says: %2$@`
    - Suggest: `وكلمة السر`
    - In Arabic spelling, the conjunction و is always attached to the word that follows it.
- `DefaultBrowserOnboarding.Description2` — `ar/firefox-ios.xliff` — Curly double quotes are used instead of the locale's guillemets.
    - Current: `”تطبيق المتصفح الافتراضي“`
    - Source: `2. Tap Default Browser App`
    - Suggest: `«تطبيق المتصفح الافتراضي»`
    - The ar locale convention for quotation marks is guillemets.
- `Added page to Reading List` — `ar/firefox-ios.xliff` — The confirmation message is translated as a command ("Add the page") instead of a past-tense report ("Page added").
    - Current: `أضِف الصفحة إلى قائمة القراءة`
    - Source: `Added page to Reading List`
    - Suggest: `أُضيفت الصفحة إلى قائمة القراءة`
    - The developer comment says VoiceOver speaks this after the page has been added, so it must report a finished action. The Arabic uses the command form, which tells the user to add the page.
- `FxA.ManageAccount` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to الأجهزة.
    - Current: `و الأجهزة`
    - Source: `Manage Account & Devices`
    - Suggest: `والأجهزة`
    - In Arabic orthography the conjunction و is always attached to the following word; a space after it is a spelling error.
- `FirefoxHomepage.Shortcuts.Sponsored.v100` — `ar/firefox-ios.xliff` — 'Sponsored' on a shortcut tile is rendered as 'sponsored result', which adds a wrong noun and goes against the comment's request to keep it as short as possible.
    - Current: `نتيجة مموّلة`
    - Source: `Sponsored`
    - Suggest: `مموّل`
    - The label marks a sponsored shortcut tile, not a search result, and the developer comment says space is limited and asks for the shortest possible text; the single adjective is enough.
- `HistoryPanel.EmptySyncedTabsState.Title` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script, and Sync is rendered with a different term than elsewhere in the file.
    - Current: `مزامنة فايرفوكس`
    - Source: `Firefox Sync`
    - Suggest: `تزامن Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script, as it does in FxHomepage.Wallpaper.ButtonLabel.v99. The rest of the file uses «تزامن» for Sync.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script.
    - Current: `فَيَرفُكس`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script, as it does elsewhere in this file.
- `HistoryPanel.ClearHistoryButtonTitle` — `ar/firefox-ios.xliff` — 'Recent' is translated as 'current' (الحالي).
    - Current: `التأريخ الحالي`
    - Source: `Clear Recent History…`
    - Suggest: `التأريخ الحديث`
    - The source says 'Clear Recent History…'. الحالي means 'current', not 'recent'.
- `Keyboard.Shortcuts.ClearRecentHistory` — `ar/firefox-ios.xliff` — "Recent" is translated as "الحالي" (current) instead of "recent".
    - Current: `التأريخ الحالي`
    - Source: `Clear Recent History`
    - Suggest: `التأريخ الحديث`
    - The source says "Clear Recent History", meaning history from a recent time range. "الحالي" means "current", which is a different idea and does not tell the user the shortcut clears only recent history.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `ar/firefox-ios.xliff` — "History" is spelled "التاريخ" here, but "التأريخ" in every other history string on the same panel.
    - Current: `يزيل التاريخ (بما في ذلك التاريخ الذي`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `يزيل التأريخ (بما في ذلك التأريخ الذي`
    - All the other History panel and shortcut strings use "التأريخ" for browsing history (for example the section title, "No history found" and "Synced History"). This string is the only one that switches to "التاريخ".
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `ar/firefox-ios.xliff` — The conjunction "و" is written apart from the next word, with a space after it.
    - Current: `و تجاهل`
    - Source: `Reload Ignoring Cache`
    - Suggest: `وتجاهل`
    - In Arabic spelling, "و" (and) is joined directly to the word that follows it, with no space.
- `ScanQRCode.PermissionError.Message.v100` — `ar/firefox-ios.xliff` — Quotation marks are mismatched: the first pair is ‘…’ but the second is reversed ’…‘.
    - Current: `’Firefox‘`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `«Firefox»`
    - The two quoted items use opposite quote orientation in the same sentence, and the locale convention is guillemets.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `ar/firefox-ios.xliff` — The word has tanween damm (ٌ) where it needs a single damma (ُ).
    - Current: `أٌضيف`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `أُضيف`
    - The passive verb is spelled أُضيف with a damma. Tanween is a misspelling on a verb.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `ar/firefox-ios.xliff` — Reader View is rendered «منظور القراءة» here but «منظور القارئ» in the Reader View string in the same file.
    - Current: `منظور القراءة`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `منظور القارئ`
    - The same feature name should be translated the same way everywhere. The «Reader View» string itself uses منظور القارئ.
- `SentTab.NoTabArrivingNotification.title` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script instead of being kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox Sync`
    - Suggest: `Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script. Other strings in this file already use "حساب Firefox".
- `Settings.AddressBar.SectionTitle.v138` — `ar/firefox-ios.xliff` — "Address Bar" appears as the singular "شريط العنوان" here but as the plural "شريط العناوين" in the settings entry for the same feature.
    - Current: `موضع شريط العنوان`
    - Source: `Address Bar Placement`
    - Suggest: `موضع شريط العناوين`
    - The same term on the same settings screen should be translated consistently. Settings.AddressBar.SettingsTitle.v138 uses "شريط العناوين".
- `Settings.Home.Option.Description.v101` — `ar/firefox-ios.xliff` — The brand name Firefox is written in Arabic script as فايرفوكس instead of being left as Firefox.
    - Current: `فايرفوكس`
    - Source: `Choose what’s included on the Firefox homepage.`
    - Suggest: `Firefox`
    - Firefox is a brand that must stay untranslated. Other strings in the same file (e.g. Settings.Disconnect.Body, Settings.FxA.Title) keep it in Latin script.
- `Settings.Home.Option.Wallpaper.Accessibility.AmethystWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, amethyst pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; other strings in the same file (e.g. StartAtHome.Description) keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.BeachHillsWallpaper.v100` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, beach hills pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.CeruleanWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, cerulean pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.SunriseWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, sunrise pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.SwitchTitle.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Change wallpaper by tapping Firefox homepage logo`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Passwords.OnboardingMessage.v103` — `ar/firefox-ios.xliff` — The alternatives "Face ID, Touch ID or a device passcode" are joined with "and" (و), so the text claims all three protect the passwords at once.
    - Current: `ببصمة الوجه (Face ID) وبصمة الإصبع (Touch ID) ورمز الجهاز السري`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `ببصمة الوجه (Face ID) أو بصمة الإصبع (Touch ID) أو رمز الجهاز السري`
    - The en-US lists alternatives with "or". The Arabic uses و (and), which changes the meaning to all three methods together.
- `Settings.SendUsage.Message` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word, but in Arabic it attaches to the word that follows.
    - Current: `و تحسينه`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `وتحسينه`
    - Arabic spelling attaches the conjunction و directly to the next word, so the space is a spelling error.
- `Settings.WebsiteData.ConfirmPrompt` — `ar/firefox-ios.xliff` — "all of your website data" is rendered as data of "your website" (singular, owned by the user) instead of data from all websites.
    - Current: `كل بيانات موقعك`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `كل بيانات المواقع`
    - The source means stored data from websites the user has visited, not data about the user's own website.
- `ShareExtension.LoadInBackgroundActionDone.Title` — `ar/firefox-ios.xliff` — "Loading in Firefox" (ongoing) is translated in the past passive ("was loaded"), which claims the load has already finished.
    - Current: `حُمّل في Firefox`
    - Source: `Loading in Firefox`
    - Suggest: `يُحمَّل في Firefox`
    - The source describes a load that is still in progress. The translation says it is complete.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `ar/firefox-ios.xliff` — A description of what the Standard level does is written as a command to the user ("allow") instead of a third-person statement.
    - Current: `اسمح ببعض`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `تسمح ببعض`
    - en-US "Allows..." describes the protection level. The imperative form tells the user to do something.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `ar/firefox-ios.xliff` — A description of what the Strict level does is written as a command to the user ("block") instead of a third-person statement.
    - Current: `احجب متعقّبات`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `تحجب متعقّبات`
    - en-US "Blocks..." describes the protection level. The imperative form tells the user to do something.
- `Settings.TrackingProtectionOption.NormalBrowsingLabelOn` — `ar/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered differently here than in the footers and alert on the same screen.
    - Current: `الحماية الموسّعة من التعقب`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `الحماية المحسّنة من التتبّع`
    - The footer and alert strings use الحماية المحسّنة من التتبّع for the same feature name. A feature name should be the same everywhere on the screen.
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `ar/firefox-ios.xliff` — "Standard" is translated as معياري here but as قياسية in the option label it reflects.
    - Current: `معياري`
    - Source: `Standard`
    - Suggest: `قياسية`
    - This status shows the selected option, which is labelled قياسية (المبدئي). The term and its grammatical gender should match that label.
- `TabsTray.InactiveTabs.SectionTitle.Opened.Accessibility.v103` — `ar/firefox-ios.xliff` — Uses «التبويبات» for tabs where the rest of the tab tray, including the paired «View Inactive Tabs» string, uses «الألسنة».
    - Current: `إخفاء التبويبات غير النشطة`
    - Source: `Hide Inactive Tabs`
    - Suggest: `أخفِ الألسنة غير النشطة`
    - Its counterpart reads «أظهر الألسنة غير النشطة» and the section title is «الألسنة غير النشطة». Switching to «التبويبات» on the same control is inconsistent. The verbal noun also breaks the imperative pattern of the paired string.
- `TopSites.RemovePage.Button` — `ar/firefox-ios.xliff` — A hyphen replaces the em dash that the source and the locale conventions both use.
    - Current: `أزل الصفحة - %@`
    - Source: `Remove page — %@`
    - Suggest: `أزل الصفحة — %@`
    - The source uses an em dash and the locale convention is the em dash.
- `Open & Fill` — `ar/firefox-ios.xliff` — The conjunction «و» is written as a separate word; in Arabic it must attach to the following word.
    - Current: `افتح و املأ`
    - Source: `Open & Fill`
    - Suggest: `افتح واملأ`
    - Arabic orthography requires the single-letter conjunction و to be written joined to the word after it. The space here is a spelling error in the menu item for "Open & Fill".
- `TodayWidget.TopSitesGalleryDescription` — `ar/firefox-ios.xliff` — The translation drops "recently": it only mentions the most visited sites, not recently visited ones.
    - Current: `المواقع الأكثر زيارة`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `المواقع التي تزورها كثيرًا ومؤخرًا`
    - The en-US says the widget adds shortcuts to frequently and recently visited sites. The Arabic says only "most visited sites", which leaves out recently visited ones.
- `PzSrmZ-2GqvPe` — `ar/firefox-ios.xliff` — Uses curly double quotes instead of the locale's guillemets.
    - Current: `”الانتقال إلى الرابط المنسوخ“`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `«الانتقال إلى الرابط المنسوخ»`
    - The ar conventions list guillemets as the established quotation style.

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
| Files | 71 |
| Strings | 1,175 |
| Missing strings | 752 |
| Obsolete strings | 0 |
| Files absent from the locale | 26 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**752 strings** are not translated yet, concentrated in:

- `ar/firefox-ios.xliff` — 141
- `ar/firefox-ios.xliff` — 133
- `ar/firefox-ios.xliff` — 81
- `Shared/Supporting Files/en-US.lproj/WebCompatReporter.strings` — 52
- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings` — 43
- `Shared/Supporting Files/en-US.lproj/NativeErrorPage.strings` — 36
- `Shared/Supporting Files/en-US.lproj/Translations.strings` — 31
- `Shared/Supporting Files/en-US.lproj/Summarizer.strings` — 21
- `ar/firefox-ios.xliff` — 16
- `ar/firefox-ios.xliff` — 15
- `Shared/Supporting Files/en-US.lproj/TermsOfUse.strings` — 15
- `ar/firefox-ios.xliff` — 12

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/BrowserDataTransfer.strings`
- `Shared/Supporting Files/en-US.lproj/Camera.strings`
- `Shared/Supporting Files/en-US.lproj/GoogleLens.strings`
- `Shared/Supporting Files/en-US.lproj/NativeErrorPage.strings`
- `Shared/Supporting Files/en-US.lproj/PasswordGenerator.strings`
- `Shared/Supporting Files/en-US.lproj/PrivacyDashboard.strings`
- `Shared/Supporting Files/en-US.lproj/QRCode.strings`
- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`
- `Shared/Supporting Files/en-US.lproj/ReaderModeBar.strings`
- `Shared/Supporting Files/en-US.lproj/RelayMask.strings`
- `Shared/Supporting Files/en-US.lproj/ScanQRCode.strings`
- `Shared/Supporting Files/en-US.lproj/SearchEngineSelection.strings`
- `Shared/Supporting Files/en-US.lproj/SearchZero.strings`
- `Shared/Supporting Files/en-US.lproj/Share.strings`
- `Shared/Supporting Files/en-US.lproj/SocialMediaApp.strings`
- `Shared/Supporting Files/en-US.lproj/SocialShare.strings`
- `Shared/Supporting Files/en-US.lproj/SuggestedSites.strings`
- `Shared/Supporting Files/en-US.lproj/Summarize.strings`
- `Shared/Supporting Files/en-US.lproj/Summarizer.strings`
- `Shared/Supporting Files/en-US.lproj/TabToolbar.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 9, `curly-double` 3, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 2 | **typographic** |
| ellipsis | `char` 5 | **char** |
| dash | `em` 1 | **em** |
| nbsp | `total` 7 | **total** |
| fullwidth | `punctuation` 1 | **punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (51)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `This action will clear all of your private data, including history from your synced devices.` — `ar/firefox-ios.xliff` — Translation says all private data is erased from synced devices, whereas the source says all private data is cleared, including history from synced devices.
    - Current: `سيمحي هذا الإجراء كل بياناتك الخاصة من الأجهزة المتزامنة، بما في ذلك التأريخ.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `سيمحي هذا الإجراء كل بياناتك الخاصة، بما في ذلك التأريخ من أجهزتك المتزامنة.`
    - In the source only history comes from the synced devices. The ar attaches 'from the synced devices' to all private data, which tells the user that far more will be deleted on other devices than the product does.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 12 |
| 3 | Degraded language (grammar, spelling, terminology) | 32 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.AppIconNames.Pixelated.Title.v136` — `ar/firefox-ios.xliff` — "مبلورة" means "crystallized", not "pixelated", and its feminine form doesn't match the other masculine icon names.
    - Current: `مبلورة`
    - Source: `Pixelated`
    - Suggest: `مُبكسَل`
    - The comment describes a pixelated version of the icon. مبلورة (from بلورة, crystal) means crystallized or clarified, so it names the wrong visual style. The feminine form also clashes with the masculine adjectives used for the other icon names (أزرق، مشتعل، مبسط).
- `This action will clear all of your private data, including history from your synced devices.` — `ar/firefox-ios.xliff` — Translation says all private data is erased from synced devices, whereas the source says all private data is cleared, including history from synced devices.
    - Current: `سيمحي هذا الإجراء كل بياناتك الخاصة من الأجهزة المتزامنة، بما في ذلك التأريخ.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `سيمحي هذا الإجراء كل بياناتك الخاصة، بما في ذلك التأريخ من أجهزتك المتزامنة.`
    - In the source only history comes from the synced devices. The ar attaches 'from the synced devices' to all private data, which tells the user that far more will be deleted on other devices than the product does.
- `Added page to Reading List` — `ar/firefox-ios.xliff` — The confirmation message is translated as a command ("Add the page") instead of a past-tense report ("Page added").
    - Current: `أضِف الصفحة إلى قائمة القراءة`
    - Source: `Added page to Reading List`
    - Suggest: `أُضيفت الصفحة إلى قائمة القراءة`
    - The developer comment says VoiceOver speaks this after the page has been added, so it must report a finished action. The Arabic uses the command form, which tells the user to add the page.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script.
    - Current: `فَيَرفُكس`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script, as it does elsewhere in this file.
- `HistoryPanel.ClearHistoryButtonTitle` — `ar/firefox-ios.xliff` — 'Recent' is translated as 'current' (الحالي).
    - Current: `التأريخ الحالي`
    - Source: `Clear Recent History…`
    - Suggest: `التأريخ الحديث`
    - The source says 'Clear Recent History…'. الحالي means 'current', not 'recent'.
- `HistoryPanel.EmptySyncedTabsState.Title` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script, and Sync is rendered with a different term than elsewhere in the file.
    - Current: `مزامنة فايرفوكس`
    - Source: `Firefox Sync`
    - Suggest: `تزامن Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script, as it does in FxHomepage.Wallpaper.ButtonLabel.v99. The rest of the file uses «تزامن» for Sync.
- `Keyboard.Shortcuts.ClearRecentHistory` — `ar/firefox-ios.xliff` — "Recent" is translated as "الحالي" (current) instead of "recent".
    - Current: `التأريخ الحالي`
    - Source: `Clear Recent History`
    - Suggest: `التأريخ الحديث`
    - The source says "Clear Recent History", meaning history from a recent time range. "الحالي" means "current", which is a different idea and does not tell the user the shortcut clears only recent history.
- `SentTab.NoTabArrivingNotification.title` — `ar/firefox-ios.xliff` — The brand name Firefox is transliterated into Arabic script instead of being kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox Sync`
    - Suggest: `Firefox`
    - Firefox is a do-not-translate brand and must stay in Latin script. Other strings in this file already use "حساب Firefox".
- `Settings.Home.Option.Description.v101` — `ar/firefox-ios.xliff` — The brand name Firefox is written in Arabic script as فايرفوكس instead of being left as Firefox.
    - Current: `فايرفوكس`
    - Source: `Choose what’s included on the Firefox homepage.`
    - Suggest: `Firefox`
    - Firefox is a brand that must stay untranslated. Other strings in the same file (e.g. Settings.Disconnect.Body, Settings.FxA.Title) keep it in Latin script.
- `Settings.Home.Option.Wallpaper.Accessibility.AmethystWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, amethyst pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; other strings in the same file (e.g. StartAtHome.Description) keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.BeachHillsWallpaper.v100` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, beach hills pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.CeruleanWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, cerulean pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.SunriseWallpaper.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, sunrise pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Home.Option.Wallpaper.SwitchTitle.v99` — `ar/firefox-ios.xliff` — Brand name Firefox is transliterated into Arabic script instead of kept as is.
    - Current: `فايرفوكس`
    - Source: `Change wallpaper by tapping Firefox homepage logo`
    - Suggest: `Firefox`
    - Firefox must remain untranslated; inconsistent with other strings in the file that keep 'Firefox'.
- `Settings.Passwords.OnboardingMessage.v103` — `ar/firefox-ios.xliff` — The alternatives "Face ID, Touch ID or a device passcode" are joined with "and" (و), so the text claims all three protect the passwords at once.
    - Current: `ببصمة الوجه (Face ID) وبصمة الإصبع (Touch ID) ورمز الجهاز السري`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `ببصمة الوجه (Face ID) أو بصمة الإصبع (Touch ID) أو رمز الجهاز السري`
    - The en-US lists alternatives with "or". The Arabic uses و (and), which changes the meaning to all three methods together.
- `Settings.WebsiteData.ConfirmPrompt` — `ar/firefox-ios.xliff` — "all of your website data" is rendered as data of "your website" (singular, owned by the user) instead of data from all websites.
    - Current: `كل بيانات موقعك`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `كل بيانات المواقع`
    - The source means stored data from websites the user has visited, not data about the user's own website.
- `ShareExtension.LoadInBackgroundActionDone.Title` — `ar/firefox-ios.xliff` — "Loading in Firefox" (ongoing) is translated in the past passive ("was loaded"), which claims the load has already finished.
    - Current: `حُمّل في Firefox`
    - Source: `Loading in Firefox`
    - Suggest: `يُحمَّل في Firefox`
    - The source describes a load that is still in progress. The translation says it is complete.
- `TodayWidget.TopSitesGalleryDescription` — `ar/firefox-ios.xliff` — The translation drops "recently": it only mentions the most visited sites, not recently visited ones.
    - Current: `المواقع الأكثر زيارة`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `المواقع التي تزورها كثيرًا ومؤخرًا`
    - The en-US says the widget adds shortcuts to frequently and recently visited sites. The Arabic says only "most visited sites", which leaves out recently visited ones.

### C. Grammar, agreement & spelling

- `Addresses.BottomSheet.UseSavedAddressBottomSheet.v124` — `ar/firefox-ios.xliff` — The object of the verb «استخدِم» needs the accusative ending, but it is written without it.
    - Current: `عنوان محفوظ`
    - Source: `Use a saved address?`
    - Suggest: `عنوانًا محفوظًا`
    - «عنوان محفوظ» is the object of «استخدِم», so it needs the accusative ending with tanween: «عنوانًا محفوظًا».
- `Addresses.EditAddress.AutofillAddAddressTitle.v129` — `ar/firefox-ios.xliff` — The imperative 'Add' is misspelled as ضِف instead of أضِف, and the object lacks the accusative ending.
    - Current: `ضِف عنوان`
    - Source: `Add address`
    - Suggest: `أضِف عنوانًا`
    - The imperative of أضاف (to add) is أضِف. ضِف comes from ضاف (to host a guest), so it is a spelling error. The object should also take the accusative: عنوانًا.
- `Addresses.EditAddress.AutofillAddressName.v129` — `ar/firefox-ios.xliff` — اسم is written with a hamza on the alif (الإِسم), which is a spelling error.
    - Current: `الإِسم`
    - Source: `Name`
    - Suggest: `الاسم`
    - The alif in اسم is a connecting alif (hamzat wasl) and takes no hamza. The correct form is الاسم.
- `Addresses.Toast.AddressRemovedConfirmation.v129` — `ar/firefox-ios.xliff` — The verb doesn't agree with its feminine subject: تم should be تمت before إزالة.
    - Current: `تم إزالة العنوان`
    - Source: `Address Removed`
    - Suggest: `تمت إزالة العنوان`
    - إزالة is a feminine verbal noun and the subject of تم, so the verb should be feminine: تمت.
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `ar/firefox-ios.xliff` — The verb بدا ("looked/seemed") is misspelled as بدى.
    - Current: `بدى`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `بدا`
    - This verb's root ends in waw (يبدو), so the past tense is written with alif: بدا. Writing بدى is a common spelling error.
- `Notification.Fallback.Title.v113` — `ar/firefox-ios.xliff` — The app name comes before the noun in English order, which is ungrammatical in Arabic.
    - Current: `%@ نصيحة`
    - Source: `%@ Tip`
    - Suggest: `نصيحة من %@`
    - The source means 'Tip from Firefox'. In Arabic the noun comes first in this kind of phrase (نصيحة %@ or نصيحة من %@). Putting %@ before نصيحة copies the English order and reads ungrammatically.
- `Search.EngineSection.Title.v108` — `ar/firefox-ios.xliff` — Word order follows English; in Arabic the engine name must follow 'بحث' as the second term of the construct.
    - Current: `%@ بحث`
    - Source: `%@ search`
    - Suggest: `بحث %@`
    - The source means '<engine> search'. Arabic puts the head noun first (بحث جوجل), as this locale already does in Search.Google.Title.v108. Putting the name first gives an ungrammatical 'Google بحث'. The string has a single %@, so moving it is safe.
- `DefaultBrowserCard.NextLevel.Title.v108` — `ar/firefox-ios.xliff` — The imperative is in the feminine form (اِرتَقي), unlike the masculine address used everywhere else.
    - Current: `اِرتَقي`
    - Source: `Elevate Everyday Browsing`
    - Suggest: `ارتقِ`
    - The masculine imperative of ارتقى is ارتقِ. ارتقي is feminine, which clashes with the locale's masculine address (اختر, استأنف).
- `A username and password are being requested by %@.` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to the next word.
    - Current: `و كلمة السر`
    - Source: `A username and password are being requested by %@.`
    - Suggest: `وكلمة السر`
    - In Arabic spelling, the conjunction و is always attached to the word that follows it.
- `A username and password are being requested by %@. The site says: %@` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to the next word.
    - Current: `و كلمة السر`
    - Source: `A username and password are being requested by %1$@. The site says: %2$@`
    - Suggest: `وكلمة السر`
    - In Arabic spelling, the conjunction و is always attached to the word that follows it.
- `FxA.ManageAccount` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word instead of being attached to الأجهزة.
    - Current: `و الأجهزة`
    - Source: `Manage Account & Devices`
    - Suggest: `والأجهزة`
    - In Arabic orthography the conjunction و is always attached to the following word; a space after it is a spelling error.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `ar/firefox-ios.xliff` — The conjunction "و" is written apart from the next word, with a space after it.
    - Current: `و تجاهل`
    - Source: `Reload Ignoring Cache`
    - Suggest: `وتجاهل`
    - In Arabic spelling, "و" (and) is joined directly to the word that follows it, with no space.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `ar/firefox-ios.xliff` — The word has tanween damm (ٌ) where it needs a single damma (ُ).
    - Current: `أٌضيف`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `أُضيف`
    - The passive verb is spelled أُضيف with a damma. Tanween is a misspelling on a verb.
- `Settings.SendUsage.Message` — `ar/firefox-ios.xliff` — The conjunction و is written as a separate word, but in Arabic it attaches to the word that follows.
    - Current: `و تحسينه`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `وتحسينه`
    - Arabic spelling attaches the conjunction و directly to the next word, so the space is a spelling error.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `ar/firefox-ios.xliff` — A description of what the Standard level does is written as a command to the user ("allow") instead of a third-person statement.
    - Current: `اسمح ببعض`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `تسمح ببعض`
    - en-US "Allows..." describes the protection level. The imperative form tells the user to do something.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `ar/firefox-ios.xliff` — A description of what the Strict level does is written as a command to the user ("block") instead of a third-person statement.
    - Current: `احجب متعقّبات`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `تحجب متعقّبات`
    - en-US "Blocks..." describes the protection level. The imperative form tells the user to do something.
- `Open & Fill` — `ar/firefox-ios.xliff` — The conjunction «و» is written as a separate word; in Arabic it must attach to the following word.
    - Current: `افتح و املأ`
    - Source: `Open & Fill`
    - Suggest: `افتح واملأ`
    - Arabic orthography requires the single-letter conjunction و to be written joined to the word after it. The space here is a spelling error in the menu item for "Open & Fill".

### D. Terminology, register & consistency

- `DefaultBrowserCard.BetterInternet.Title.v108` — `ar/firefox-ios.xliff` — 'Default' is rendered as الدائم ('permanent') instead of the established الافتراضي, and the pronoun in جعله has no antecedent.
    - Current: `جعله متصفحك الدائم`
    - Source: `Default to a Better Internet`
    - Suggest: `جعل Firefox متصفحك الافتراضي`
    - The sibling banner strings on the same screen render 'default browser' as المتصفح الافتراضي. الدائم means 'permanent', which is a different concept.
- `FirefoxHomepage.Shortcuts.Sponsored.v100` — `ar/firefox-ios.xliff` — 'Sponsored' on a shortcut tile is rendered as 'sponsored result', which adds a wrong noun and goes against the comment's request to keep it as short as possible.
    - Current: `نتيجة مموّلة`
    - Source: `Sponsored`
    - Suggest: `مموّل`
    - The label marks a sponsored shortcut tile, not a search result, and the developer comment says space is limited and asks for the shortest possible text; the single adjective is enough.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `ar/firefox-ios.xliff` — "History" is spelled "التاريخ" here, but "التأريخ" in every other history string on the same panel.
    - Current: `يزيل التاريخ (بما في ذلك التاريخ الذي`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `يزيل التأريخ (بما في ذلك التأريخ الذي`
    - All the other History panel and shortcut strings use "التأريخ" for browsing history (for example the section title, "No history found" and "Synced History"). This string is the only one that switches to "التاريخ".
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `ar/firefox-ios.xliff` — Reader View is rendered «منظور القراءة» here but «منظور القارئ» in the Reader View string in the same file.
    - Current: `منظور القراءة`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `منظور القارئ`
    - The same feature name should be translated the same way everywhere. The «Reader View» string itself uses منظور القارئ.
- `Settings.AddressBar.SectionTitle.v138` — `ar/firefox-ios.xliff` — "Address Bar" appears as the singular "شريط العنوان" here but as the plural "شريط العناوين" in the settings entry for the same feature.
    - Current: `موضع شريط العنوان`
    - Source: `Address Bar Placement`
    - Suggest: `موضع شريط العناوين`
    - The same term on the same settings screen should be translated consistently. Settings.AddressBar.SettingsTitle.v138 uses "شريط العناوين".
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `ar/firefox-ios.xliff` — "Standard" is translated as معياري here but as قياسية in the option label it reflects.
    - Current: `معياري`
    - Source: `Standard`
    - Suggest: `قياسية`
    - This status shows the selected option, which is labelled قياسية (المبدئي). The term and its grammatical gender should match that label.
- `Settings.TrackingProtectionOption.NormalBrowsingLabelOn` — `ar/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered differently here than in the footers and alert on the same screen.
    - Current: `الحماية الموسّعة من التعقب`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `الحماية المحسّنة من التتبّع`
    - The footer and alert strings use الحماية المحسّنة من التتبّع for the same feature name. A feature name should be the same everywhere on the screen.
- `TabsTray.InactiveTabs.SectionTitle.Opened.Accessibility.v103` — `ar/firefox-ios.xliff` — Uses «التبويبات» for tabs where the rest of the tab tray, including the paired «View Inactive Tabs» string, uses «الألسنة».
    - Current: `إخفاء التبويبات غير النشطة`
    - Source: `Hide Inactive Tabs`
    - Suggest: `أخفِ الألسنة غير النشطة`
    - Its counterpart reads «أظهر الألسنة غير النشطة» and the section title is «الألسنة غير النشطة». Switching to «التبويبات» on the same control is inconsistent. The verbal noun also breaks the imperative pattern of the paired string.

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.DeletedBookmark.v131` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“%@”`
    - Source: `Deleted “%@”`
    - Suggest: `«%@»`
    - Guillemets are the established quotation marks for this locale.
- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“العلامات المرجعية”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `«العلامات المرجعية»`
    - Guillemets are the established quotation marks for this locale.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `ar/firefox-ios.xliff` — This string uses curly double quotes instead of the locale's guillemets.
    - Current: `“%@”`
    - Source: `Saved in “%@”`
    - Suggest: `«%@»`
    - Guillemets are the established quotation marks for this locale.
- `DefaultBrowserOnboarding.Description2` — `ar/firefox-ios.xliff` — Curly double quotes are used instead of the locale's guillemets.
    - Current: `”تطبيق المتصفح الافتراضي“`
    - Source: `2. Tap Default Browser App`
    - Suggest: `«تطبيق المتصفح الافتراضي»`
    - The ar locale convention for quotation marks is guillemets.
- `ScanQRCode.PermissionError.Message.v100` — `ar/firefox-ios.xliff` — Quotation marks are mismatched: the first pair is ‘…’ but the second is reversed ’…‘.
    - Current: `’Firefox‘`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `«Firefox»`
    - The two quoted items use opposite quote orientation in the same sentence, and the locale convention is guillemets.
- `TopSites.RemovePage.Button` — `ar/firefox-ios.xliff` — A hyphen replaces the em dash that the source and the locale conventions both use.
    - Current: `أزل الصفحة - %@`
    - Source: `Remove page — %@`
    - Suggest: `أزل الصفحة — %@`
    - The source uses an em dash and the locale convention is the em dash.
- `PzSrmZ-2GqvPe` — `ar/firefox-ios.xliff` — Uses curly double quotes instead of the locale's guillemets.
    - Current: `”الانتقال إلى الرابط المنسوخ“`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `«الانتقال إلى الرابط المنسوخ»`
    - The ar conventions list guillemets as the established quotation style.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ar/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
