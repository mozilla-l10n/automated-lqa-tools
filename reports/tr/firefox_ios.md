# Firefox iOS l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 1,910 of 1,910 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for tr: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (77)

- `CreditCard.SnackBar.RemoveCardSublabel.v112` — `tr/firefox-ios.xliff` — Turkish says "This card will be removed" instead of "This will remove the card from all of your synced devices", altering the subject.
    - Current: `Bu kart, eşitlenen tüm cihazlarınızdan kaldırılacaktır.`
    - Source: `This will remove the card from all of your synced devices.`
    - Suggest: `Bu işlem, kartı eşitlenen tüm cihazlarınızdan kaldıracaktır.`
    - The source subject is the action ("This will remove the card..."), not the card itself; the translation drops the reference to the confirmed action.
- `Settings.AppIconSelection.AppIconNames.Twilight.Title.v137` — `tr/firefox-ios.xliff` — "Twilight" is translated as "Şafak" (dawn) instead of dusk/twilight.
    - Current: `Şafak`
    - Source: `Twilight`
    - Suggest: `Alacakaranlık`
    - Twilight means dusk/alacakaranlık; "Şafak" means dawn/daybreak, a different time of day, and the icon set already has Sunrise (Gün doğumu) and Sunset (Gün batımı).
- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `tr/firefox-ios.xliff` — Section heading "Basics" rendered as the adjective "Basit" (simple) rather than a noun heading.
    - Current: `Basit`
    - Source: `Basics`
    - Suggest: `Temel`
    - The source is a plural noun section heading meaning basic variants; "Basit" means "simple", not "basics", and is inconsistent with the other noun headings (Renkler, Renk geçişleri).
- `Settings.Home.Option.Stories.v140` — `tr/firefox-ios.xliff` — "Stories" is translated as "Haberler" (News), which names a different thing than the source.
    - Current: `Haberler`
    - Source: `Stories`
    - Suggest: `Hikâyeler`
    - The source term is "Stories" (recommended articles/stories section), not "News". Related strings in the same file render Stories-type content as "makaleler/yazılar"; "Haberler" means news.
- `Settings.Home.Option.TopStories.v143` — `tr/firefox-ios.xliff` — "Top Stories" is rendered as "İlginç yazılar" (Interesting writings), which loses "Top" and conflicts with the other Stories strings in this screen.
    - Current: `İlginç yazılar`
    - Source: `Top Stories`
    - Suggest: `Öne çıkan hikâyeler`
    - "Top" is not conveyed and "Stories" is rendered inconsistently with the other Stories options on the same settings screen ("Haberler", "makaleler").
- `Addresses.EditAddress.AutofillAddressDistrict.v129` — `tr/firefox-ios.xliff` — "District" and "County" are both translated as "İlçe" on the same address form, making the two distinct fields indistinguishable.
    - Current: `İlçe`
    - Source: `District`
    - Suggest: `Semt`
    - Addresses.EditAddress.AutofillAddressCounty.v129 already uses "İlçe" for "County"; two separate address fields on the same screen must not share the same label.
- `Addresses.EditAddress.AutofillAddressProvince.v129` — `tr/firefox-ios.xliff` — "Province" is translated as "İl", which conflicts with the standard rendering and is inconsistent with the other administrative-division labels in the same form.
    - Current: `İl`
    - Source: `Province`
    - Suggest: `Eyalet/Bölge`
    - In this address form "State" is already "Eyalet" and "Prefecture" is "Vilayet"; "Province" normally maps to "Eyalet/Bölge" or "Vilayet". "İl" is the Turkish administrative unit used for the city/state field and creates ambiguity within the same screen.
- `Engagement.Notification.Body.v112` — `tr/firefox-ios.xliff` — Turkish adds "restoranları" (restaurants), which is not in the source's generic "Find something nearby".
    - Current: `İster yakınınızdaki restoranları bulun, ister eğlenceli bir şeyler keşfedin.`
    - Source: `Find something nearby. Or discover something fun.`
    - Suggest: `İster yakınınızdaki bir şeyi bulun, ister eğlenceli bir şeyler keşfedin.`
    - The en-US text is generic ("Find something nearby"); the translation narrows it to restaurants, adding content not in the source.
- `Engagement.Notification.Treatment.B.Body.v114` — `tr/firefox-ios.xliff` — Uses the informal singular imperative "gezin" while the sibling notification strings use the polite plural form ("gezinin", "deneyin", "bulun").
    - Current: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezin.`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezinin.`
    - Register inconsistency within the same feature: all other Engagement notification strings address the user with the formal/plural imperative.
- `CloseTab.ArrivingNotification.title.v133` — `tr/firefox-ios.xliff` — The Turkish reads "Firefox's tabs closed" instead of "Firefox tabs closed: <count>", and the possessive suffix on the app name is wrong for the intended meaning.
    - Current: `%1$@ sekmeleri kapatıldı: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ sekmeleri kapatıldı: %2$@ sekme`
    - Source is "%1$@ tabs closed: %2$@" where %2$@ is the number of tabs; the Turkish leaves the trailing number bare so it reads ambiguously, and ideally should mark it as a count.
- `MainMenu.SettingsSection.AccessibilityLabels.WhatsNew.v132` — `tr/firefox-ios.xliff` — Wrong apostrophe suffix for "Firefox": should be "%@'taki" → correct vowel harmony gives "Firefox'taki", but the placeholder form used is inconsistent with app name ending.
    - Current: `%@’taki yenilikler`
    - Source: `New in %@`
    - Suggest: `%@’teki yenilikler`
    - Turkish vowel harmony: "Firefox" final vowel is "o"… however the last pronounced syllable of "Firefox" in Turkish is "foks", a front-vowel-less form; standard Turkish usage is "Firefox'taki". Flagging low value.
- `MainMenu.AccessibilityLabels.DismissBanner.142` — `tr/firefox-ios.xliff` — "banner" is translated as "Bildirim" (notification) instead of banner.
    - Current: `Bildirimi kapat`
    - Source: `Dismiss banner`
    - Suggest: `Banner’ı kapat`
    - The source refers to the header banner on top of the menu, not a notification; other strings in this file refer to the same element as "banner" (HeaderBanner).
- `MainMenu.SettingsSection.WhatsNew.Title.v131` — `tr/firefox-ios.xliff` — Wrong Turkish suffix after the app-name placeholder: "%@’taki" should be "%@’teki".
    - Current: `%@’taki yenilikler`
    - Source: `New in %@`
    - Suggest: `%@’teki yenilikler`
    - The app name is Firefox, whose last vowel "o" requires the front/back harmony form used with a hard consonant "x" — Turkish convention renders Firefox'taki. However for the generic placeholder the standard Mozilla tr rendering is "%@ sürümündeki yenilikler"; at minimum the current locked "’taki" is a hard-coded suffix that does not agree with all app names (Focus, Klar → Focus'taki/Klar'daki).
- `Microsurvey.Prompt.TitleLabel.v127` — `tr/firefox-ios.xliff` — "It only takes a minute" is translated as "birkaç dakika" (a few minutes) instead of one minute.
    - Current: `Yalnızca birkaç dakika sürer.`
    - Source: `Help us make %@ better. It only takes a minute.`
    - Suggest: `Yalnızca bir dakikanızı alır.`
    - The source says the survey takes only a minute; the Turkish says several minutes, overstating the time required.
- `NativeErrorPage.ButtonLabel.v131` — `tr/firefox-ios.xliff` — "Reload" is rendered as "Tazele" instead of the standard Firefox Turkish term "Yeniden yükle".
    - Current: `Tazele`
    - Source: `Reload`
    - Suggest: `Yeniden yükle`
    - The established Turkish Firefox term for Reload/Refresh is "Yeniden yükle"; "Tazele" is colloquial and inconsistent with the rest of the product.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `tr/firefox-ios.xliff` — Informal second-person singular "dokun" breaks the formal address used in the surrounding Default Browser Popup strings.
    - Current: `Bu iletiyi kapatıp Atla’ya dokun.`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `Bu iletiyi kapatıp Atla’ya dokunun.`
    - Sibling strings in the same popup (DefaultBrowserPopup.SecondLabel "dokunun", FirstLabel "gidin") use the formal plural form; this string switches to informal singular, an inconsistent register on the same screen.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `tr/firefox-ios.xliff` — "the browser" is rendered as "uygulamayı" (the app) instead of "tarayıcıyı".
    - Current: `uygulamayı geliştirmemize`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmemize`
    - The source says "To help improve the browser"; the Turkish says "the app", which is a different term than the source's "browser".
- `Onboarding.Modern.TermsOfService.AgreementButtonTitle.v145` — `tr/firefox-ios.xliff` — "Continue" rendered as "İleri" (Next), inconsistent with the v140 string on the same screen which uses "Devam et".
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam et`
    - The identical source "Continue" is translated "Devam et" in Onboarding.Modern.TermsOfService.AgreementButtonTitle.v140 for the same Terms of Service screen; "İleri" means "Next" and breaks consistency with the accompanying agreement text "Devam ettiğinizde…".
- `Onboarding.Modern.TermsOfService.ManagePreferenceAgreement.v145` — `tr/firefox-ios.xliff` — "the browser" translated as "uygulamayı" (the app) instead of "tarayıcıyı".
    - Current: `uygulamayı geliştirmemize`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmemize`
    - Source says "To help improve the browser"; the v140 counterpart correctly uses "tarayıcıyı".
- `PasswordAutofill.SignInWithSavedPassword.v124` — `tr/firefox-ios.xliff` — Future/intent "You'll sign into %@" is rendered as present continuous "you are signing in".
    - Current: `%@ sitesine giriş yapıyorsunuz`
    - Source: `You’ll sign into %@`
    - Suggest: `%@ sitesine giriş yapacaksınız`
    - The en-US says the user will sign in (future), whereas the Turkish states the action is currently happening.
- `UnifiedSearch.SearchEngineSelection.TopTitle.Title.v133` — `tr/firefox-ios.xliff` — "This time search in:" is translated as "Burada ara:" (Search here), losing the "this time" meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu kez şurada ara:`
    - The source emphasizes a one-time engine choice ("This time"); the Turkish only says "Search here", dropping that meaning.
- `UnifiedSearch.SearchEngineSelection.AccessibilityLabels.TopTitle.Label.v133` — `tr/firefox-ios.xliff` — Accessibility label for "This time search in:" omits the "this time" meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu kez şurada ara:`
    - Same as the visible title: the one-off nature of the engine selection ("This time") is not conveyed.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `tr/firefox-ios.xliff` — "Trending Searches" rendered as "Arama trendleri" here but as "gündeminde" elsewhere; inconsistent with the section title wording.
    - Current: `Arama trendlerini göster`
    - Source: `Show Trending Searches`
    - Suggest: `Trend aramaları göster`
    - The same feature (trending searches) is named differently across strings in the same feature file; "Arama trendleri" (search trends) reverses the head noun of "trending searches".
- `Addresses.Settings.SecureSaveInfo.Description.v130` — `tr/firefox-ios.xliff` — Case mismatch: "Bilgilerinizi ... hızlıca erişmek" requires the dative "bilgilerinize" for the verb "erişmek".
    - Current: `Bilgilerinizi daha sonra hızlıca erişmek için güvenli bir şekilde kaydedin.`
    - Source: `Securely save your information to get quick access to it later.`
    - Suggest: `Bilgilerinize daha sonra hızlıca erişebilmek için bilgilerinizi güvenli bir şekilde kaydedin.`
    - The verb "erişmek" governs the dative case; as written the accusative object of "kaydedin" is wrongly reused as the object of "erişmek", producing ungrammatical Turkish.
- `Search.Google.Title.v108` — `tr/firefox-ios.xliff` — "Google Search" section header translated as an imperative "Google’da Ara" instead of a noun phrase consistent with the sibling header "%@ araması".
    - Current: `Google’da Ara`
    - Source: `Google Search`
    - Suggest: `Google araması`
    - The string is a section header parallel to Search.EngineSection.Title ("%@ araması"); rendering it as a command is inconsistent within the same screen.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `tr/firefox-ios.xliff` — The condition "For on-device AI" is dropped, turning a conditional statement into an unconditional one.
    - Current: `Cihaza indirilmiş yapay zekâ modelleri kaldırılacaktır.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Cihaz üzerinde çalışan yapay zekâ için indirilmiş tüm modeller kaldırılır.`
    - The source qualifies the removal of downloaded models to on-device AI ("For on-device AI, any downloaded models are removed."); the translation omits this qualifier.
- `Settings.DailyUsagePing.Message.v135` — `tr/firefox-ios.xliff` — The placeholder (company name, e.g. Mozilla) is misplaced so the text reads "active Mozilla users" instead of "helps Mozilla estimate active users".
    - Current: `Bu sayede aktif %@ kullanıcılarının sayısını tahmin edebiliriz.`
    - Source: `This helps %@ to estimate active users.`
    - Suggest: `Bu, %@ kuruluşunun aktif kullanıcı sayısını tahmin etmesine yardımcı olur.`
    - En-US says this helps %@ (Mozilla) estimate active users; the Turkish says "we can estimate the number of active %@ users", changing both the subject and the meaning.
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `tr/firefox-ios.xliff` — The second clause "and how to get the most out of %@" is dropped from the translation.
    - Current: `%@ tarayıcısının kullanışlı özelliklerini öğrenin.`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `%@ tarayıcısının kullanışlı özelliklerini ve ondan en iyi şekilde nasıl yararlanabileceğinizi öğrenin.`
    - En-US: "Learn about useful features and how to get the most out of %@." Half of the source meaning is missing.
- `Settings.Rollouts.Message.v148` — `tr/firefox-ios.xliff` — "between updates" is mistranslated as "with every update" (her güncellemede).
    - Current: `%@ her güncellemede özellikleri, performansı ve kararlılığı iyileştirecektir.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@, güncellemeler arasında özellikleri, performansı ve kararlılığı iyileştirecektir.`
    - En-US says improvements happen between updates (i.e. without an app update); the Turkish says they happen at every update, reversing the intended meaning.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `tr/firefox-ios.xliff` — Wrong apostrophe suffix vowel for the app name; Turkish requires "-tan" only after back vowels, and "Firefox" takes "-tan" but the placeholder is separated incorrectly with the wrong harmony form.
    - Current: `%@’tan`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `%@’ten`
    - The app name is Firefox, whose final syllable vowel (o... x) — the Turkish convention used elsewhere in Firefox iOS is "Firefox’ten". Consistency with other strings requires the front-vowel form.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `tr/firefox-ios.xliff` — "This page may be restricted" is rendered with an added "içerik içeriyor" construction that mixes the two clauses awkwardly and misstates the meaning.
    - Current: `Bu sayfa kısıtlanmış veya çoğunlukla görsel içerik içeriyor olabilir.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Bu sayfa kısıtlanmış veya çoğunlukla görsel içerikli olabilir.`
    - The source says the page may be restricted or mostly visual; the current wording reads "this page may contain restricted or mostly visual content", shifting the meaning.
- `Summarizer.ToastLabel.v149` — `tr/firefox-ios.xliff` — "Summary not available" translated with the Arabic-origin "mevcut değil" where standard Firefox tr wording is "kullanılamıyor"/"yok".
    - Current: `Özet mevcut değil`
    - Source: `Summary not available`
    - Suggest: `Özet kullanılamıyor`
    - "not available" is consistently rendered as "kullanılamıyor" in Firefox tr; "mevcut değil" is off-terminology.
- `TabTrayOneDayAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Day Ago" is rendered as "1 gün" ("1 day"), dropping the "ago" relative-time meaning.
    - Current: `1 gün`
    - Source: `1 Day Ago`
    - Suggest: `1 gün önce`
    - The source refers to a point in time (tabs older than 1 day ago); "1 gün" only means "1 day", losing "ago". Sibling strings (1 Week/Month Ago) share the same issue.
- `TabTrayOneWeekAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Week Ago" is rendered as "1 hafta" ("1 week"), dropping "ago".
    - Current: `1 hafta`
    - Source: `1 Week Ago`
    - Suggest: `1 hafta önce`
    - The label denotes a relative time point ("ago"); the Turkish only says "1 week".
- `TabTrayOneMonthAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Month Ago" is rendered as "1 ay" ("1 month"), dropping "ago".
    - Current: `1 ay`
    - Source: `1 Month Ago`
    - Suggest: `1 ay önce`
    - The label denotes a relative time point ("ago"); the Turkish only says "1 month".
- `TermsOfUse.Title.v142` — `tr/firefox-ios.xliff` — "We’ve got an update" is translated as "Bir haberimiz var" ("We have some news"), losing the notion of an update.
    - Current: `Bir haberimiz var`
    - Source: `We’ve got an update`
    - Suggest: `Bir güncellememiz var`
    - The developer comment states the title indicates there is an update to the terms of use; the Turkish says only "we have news".
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `tr/firefox-ios.xliff` — "Sync" is translated as the adjective/participle "Eşitlenen" ("synced") instead of the noun "Eşitleme".
    - Current: `Eşitlenen`
    - Source: `Sync`
    - Suggest: `Eşitleme`
    - Source is the noun "Sync" as a tab-selector title; "Eşitlenen" is a dangling participle ("the synced ...") without a head noun.
- `WebCompatReporter.AdditionalInfo.FooterText.v154` — `tr/firefox-ios.xliff` — Ungrammatical double structure "iyileştirmemize için yardımcı" (superfluous "için" after a dative verbal noun).
    - Current: `iyileştirmemize için yardımcı oluyor`
    - Source: `Your report helps us understand and fix issues in %1$@ to make it better for everyone. %2$@`
    - Suggest: `iyileştirmemize yardımcı oluyor`
    - "-memize" already carries the dative case required by "yardımcı olmak"; adding "için" is grammatically incorrect.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `tr/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered as "gelişmiş izlenme koruması" instead of the established Firefox term "Gelişmiş İzlenme Koruması".
    - Current: `Bu sitenin gelişmiş izlenme koruması ayarı`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Bu sitenin Gelişmiş İzlenme Koruması ayarı`
    - Enhanced Tracking Protection is a Firefox feature name capitalized in Turkish Firefox localization as "Gelişmiş İzlenme Koruması".
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `tr/firefox-ios.xliff` — "Captions are missing" translated as "Altyazılar görünmüyor" (captions are not visible) instead of missing.
    - Current: `Altyazılar görünmüyor`
    - Source: `Captions are missing`
    - Suggest: `Altyazılar eksik`
    - The source says the captions are missing/absent, not that they are not displayed.
- `WorldCup.GroupPhase.GroupStageLabel.v151` — `tr/firefox-ios.xliff` — "Group Stage" (tournament phase) is rendered as "Grup maçı" (group match), naming a single match rather than the phase.
    - Current: `Grup maçı`
    - Source: `Group Stage`
    - Suggest: `Grup aşaması`
    - The developer comment says this is the generic label indicating the Group Stage phase; Turkish "Grup maçı" means "group match", not the stage/phase.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `tr/firefox-ios.xliff` — "Get custom wallpaper" is translated as "Kişisel duvar kâğıdını indir" (download the personal wallpaper), altering the meaning with a definite object and "download".
    - Current: `Kişisel duvar kâğıdını indir`
    - Source: `Get custom wallpaper`
    - Suggest: `Özel duvar kâğıdı edinin`
    - The source refers to obtaining a custom (özel) wallpaper, not downloading a specific personal one; "kişisel" and the definite accusative change the meaning.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `tr/firefox-ios.xliff` — Inconsistent/incorrect apostrophe suffix casing: "16’LI TUR" should follow vowel harmony as "16’LI" vs the parallel "32’Lİ" — the correct form for 16 (on altı) is "16’LI"? see rationale.
    - Current: `16’LI TUR`
    - Source: `ROUND OF 16`
    - Suggest: `SON 16 TURU`
    - "Round of 16" in Turkish football usage is "Son 16 Turu"; "16’LI TUR" is not an established term and is inconsistent with the sibling string. The suffix also mismatches the sibling "32’Lİ TUR" pattern.
- `Enter passcode` — `tr/firefox-ios.xliff` — "passcode" translated as "Parola" (password) instead of "parola kodu/geçiş kodu".
    - Current: `Parolayı girin`
    - Source: `Enter passcode`
    - Suggest: `Geçiş kodunu girin`
    - The source distinguishes passcode from password; Turkish "parola" means password, which conflicts with the passcode terminology used on iOS.
- `This action will clear all of your private data, including history from your synced devices.` — `tr/firefox-ios.xliff` — "private data" rendered as "kişisel verileriniz" (personal data) instead of "özel verileriniz".
    - Current: `tüm kişisel verilerinizi`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `tüm özel verilerinizi`
    - The source says "private data", a distinct product term (Private Data / Özel veriler) in Firefox settings, not "personal data".
- `Saved Logins` — `tr/firefox-ios.xliff` — "Saved Logins" is rendered as "Kayıtlı hesaplar" (saved accounts) instead of saved logins/passwords.
    - Current: `Kayıtlı hesaplar`
    - Source: `Saved Logins`
    - Suggest: `Kayıtlı hesap bilgileri`
    - The developer comment says this clears passwords and login data; "hesaplar" means "accounts", which is a different concept from stored logins/credentials.
- `DefaultBrowserCard.BetterInternet.Title.v108` — `tr/firefox-ios.xliff` — "Default to a Better Internet" is translated as "Hep daha iyi bir internet" ("Always a better internet"), losing the call to set the default browser.
    - Current: `Hep daha iyi bir internet`
    - Source: `Default to a Better Internet`
    - Suggest: `Daha iyi bir interneti saptanmış yapın`
    - The source is a play on "default" prompting the user to set Firefox as the default browser; the Turkish drops that meaning entirely and says "always a better internet".
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `tr/firefox-ios.xliff` — "3,000+ trackers" is translated as "3.000 takip kodunu", dropping the "+" (more than).
    - Current: `ortalama 3.000 takip kodunu engelliyor`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `ortalama 3.000’den fazla takip kodunu engelliyor`
    - The en-US states over 3,000 trackers per user per month; the Turkish states exactly 3,000, changing the factual claim.
- `AddPass.Error.Message` — `tr/firefox-ios.xliff` — "Pass" (Wallet kartı/bileti) is mistranslated as "Parola" (password).
    - Current: `Parola Wallet’a eklenirken bir hata oluştu.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Kart Wallet’a eklenirken bir hata oluştu.`
    - The developer comment references Apple Wallet passes; "pass" is a Wallet card/ticket, not a password ("parola").
- `AddPass.Error.Title` — `tr/firefox-ios.xliff` — "Pass" (Wallet kartı) mistranslated as "Parola" (password).
    - Current: `Parola eklenemedi`
    - Source: `Failed to Add Pass`
    - Suggest: `Kart eklenemedi`
    - Per the developer comment this is the Apple Wallet 'Add Pass Failed' alert; a Wallet pass is not a password.
- `Logins.PasscodeRequirement.Warning` — `tr/firefox-ios.xliff` — The Turkish says the user must "set" a device passcode rather than that a passcode must be enabled, and drops "for Firefox" as a separate notion by turning it into a possessive.
    - Current: `Firefox’un otomatik doldurma özelliğini kullanmak için cihaz parolasını ayarlamalısınız.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Firefox’ta otomatik doldurma özelliğini kullanmak için cihazınızda parola etkin olmalıdır.`
    - Source: "To use the AutoFill feature for Firefox, you must have a device passcode enabled." — the requirement is that a passcode be enabled, not that the user configure a specific passcode.
- `Logins` — `tr/firefox-ios.xliff` — "Logins" is rendered as "Hesaplar" (Accounts), which is the wrong term for saved logins/passwords.
    - Current: `Hesaplar`
    - Source: `Logins`
    - Suggest: `Hesap bilgileri`
    - The source term is "Logins" (saved credentials), not "Accounts"; "Hesaplar" collides with the Firefox Account terminology used elsewhere in settings.
- `Menu.RemovePin.Confirm2.v99` — `tr/firefox-ios.xliff` — "Shortcuts" is rendered as "Kestirmeler" here but as "Kısayollar" in the related shortcut string on the same screen.
    - Current: `Kestirmelerden kaldırıldı`
    - Source: `Removed from Shortcuts`
    - Suggest: `Kısayollardan kaldırıldı`
    - Menu.RemovedFromShortcuts.v99 translates "Shortcuts" as "Kısayollar"; the confirmation toast for the same action must use the same term.
- `Oops! Firefox crashed` — `tr/firefox-ios.xliff` — The interjection "Oops!" is dropped from the translation.
    - Current: `Firefox çöktü`
    - Source: `Oops! Firefox crashed`
    - Suggest: `Hay aksi! Firefox çöktü`
    - The en-US title starts with "Oops!", which is omitted in the Turkish string.
- `Privacy` — `tr/firefox-ios.xliff` — Section title is written in all caps unlike the source and other section titles.
    - Current: `GİZLİLİK`
    - Source: `Privacy`
    - Suggest: `Gizlilik`
    - The en-US source is "Privacy" in sentence case; iOS applies its own capitalization to section headers, so hardcoded uppercase deviates from the source and from sibling titles like "Hızlı arama motorları".
- `Settings.Disconnect.Body` — `tr/firefox-ios.xliff` — "browsing data" is narrowed to "gezinti geçmişiniz" (browsing history).
    - Current: `bu cihazdaki gezinti geçmişiniz silinmeyecek`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `bu cihazdaki gezinti verileriniz silinmeyecek`
    - The source says none of your browsing data will be deleted, not just browsing history.
- _…and 17 more._

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
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 10, `curly-double` 6 | _mixed_ |
| apostrophe | `typographic` 104 | **typographic** |
| ellipsis | `char` 20 | **char** |
| register | `formal` 7 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (77)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 45 |
| 3 | Degraded language (grammar, spelling, terminology) | 29 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `CreditCard.SnackBar.RemoveCardSublabel.v112` — `tr/firefox-ios.xliff` — Turkish says "This card will be removed" instead of "This will remove the card from all of your synced devices", altering the subject.
    - Current: `Bu kart, eşitlenen tüm cihazlarınızdan kaldırılacaktır.`
    - Source: `This will remove the card from all of your synced devices.`
    - Suggest: `Bu işlem, kartı eşitlenen tüm cihazlarınızdan kaldıracaktır.`
    - The source subject is the action ("This will remove the card..."), not the card itself; the translation drops the reference to the confirmed action.
- `Settings.AppIconSelection.AppIconNames.Twilight.Title.v137` — `tr/firefox-ios.xliff` — "Twilight" is translated as "Şafak" (dawn) instead of dusk/twilight.
    - Current: `Şafak`
    - Source: `Twilight`
    - Suggest: `Alacakaranlık`
    - Twilight means dusk/alacakaranlık; "Şafak" means dawn/daybreak, a different time of day, and the icon set already has Sunrise (Gün doğumu) and Sunset (Gün batımı).
- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `tr/firefox-ios.xliff` — Section heading "Basics" rendered as the adjective "Basit" (simple) rather than a noun heading.
    - Current: `Basit`
    - Source: `Basics`
    - Suggest: `Temel`
    - The source is a plural noun section heading meaning basic variants; "Basit" means "simple", not "basics", and is inconsistent with the other noun headings (Renkler, Renk geçişleri).
- `Settings.Home.Option.Stories.v140` — `tr/firefox-ios.xliff` — "Stories" is translated as "Haberler" (News), which names a different thing than the source.
    - Current: `Haberler`
    - Source: `Stories`
    - Suggest: `Hikâyeler`
    - The source term is "Stories" (recommended articles/stories section), not "News". Related strings in the same file render Stories-type content as "makaleler/yazılar"; "Haberler" means news.
- `Addresses.EditAddress.AutofillAddressProvince.v129` — `tr/firefox-ios.xliff` — "Province" is translated as "İl", which conflicts with the standard rendering and is inconsistent with the other administrative-division labels in the same form.
    - Current: `İl`
    - Source: `Province`
    - Suggest: `Eyalet/Bölge`
    - In this address form "State" is already "Eyalet" and "Prefecture" is "Vilayet"; "Province" normally maps to "Eyalet/Bölge" or "Vilayet". "İl" is the Turkish administrative unit used for the city/state field and creates ambiguity within the same screen.
- `Engagement.Notification.Body.v112` — `tr/firefox-ios.xliff` — Turkish adds "restoranları" (restaurants), which is not in the source's generic "Find something nearby".
    - Current: `İster yakınınızdaki restoranları bulun, ister eğlenceli bir şeyler keşfedin.`
    - Source: `Find something nearby. Or discover something fun.`
    - Suggest: `İster yakınınızdaki bir şeyi bulun, ister eğlenceli bir şeyler keşfedin.`
    - The en-US text is generic ("Find something nearby"); the translation narrows it to restaurants, adding content not in the source.
- `CloseTab.ArrivingNotification.title.v133` — `tr/firefox-ios.xliff` — The Turkish reads "Firefox's tabs closed" instead of "Firefox tabs closed: <count>", and the possessive suffix on the app name is wrong for the intended meaning.
    - Current: `%1$@ sekmeleri kapatıldı: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ sekmeleri kapatıldı: %2$@ sekme`
    - Source is "%1$@ tabs closed: %2$@" where %2$@ is the number of tabs; the Turkish leaves the trailing number bare so it reads ambiguously, and ideally should mark it as a count.
- `MainMenu.AccessibilityLabels.DismissBanner.142` — `tr/firefox-ios.xliff` — "banner" is translated as "Bildirim" (notification) instead of banner.
    - Current: `Bildirimi kapat`
    - Source: `Dismiss banner`
    - Suggest: `Banner’ı kapat`
    - The source refers to the header banner on top of the menu, not a notification; other strings in this file refer to the same element as "banner" (HeaderBanner).
- `Microsurvey.Prompt.TitleLabel.v127` — `tr/firefox-ios.xliff` — "It only takes a minute" is translated as "birkaç dakika" (a few minutes) instead of one minute.
    - Current: `Yalnızca birkaç dakika sürer.`
    - Source: `Help us make %@ better. It only takes a minute.`
    - Suggest: `Yalnızca bir dakikanızı alır.`
    - The source says the survey takes only a minute; the Turkish says several minutes, overstating the time required.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `tr/firefox-ios.xliff` — "the browser" is rendered as "uygulamayı" (the app) instead of "tarayıcıyı".
    - Current: `uygulamayı geliştirmemize`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmemize`
    - The source says "To help improve the browser"; the Turkish says "the app", which is a different term than the source's "browser".
- `Onboarding.Modern.TermsOfService.ManagePreferenceAgreement.v145` — `tr/firefox-ios.xliff` — "the browser" translated as "uygulamayı" (the app) instead of "tarayıcıyı".
    - Current: `uygulamayı geliştirmemize`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmemize`
    - Source says "To help improve the browser"; the v140 counterpart correctly uses "tarayıcıyı".
- `PasswordAutofill.SignInWithSavedPassword.v124` — `tr/firefox-ios.xliff` — Future/intent "You'll sign into %@" is rendered as present continuous "you are signing in".
    - Current: `%@ sitesine giriş yapıyorsunuz`
    - Source: `You’ll sign into %@`
    - Suggest: `%@ sitesine giriş yapacaksınız`
    - The en-US says the user will sign in (future), whereas the Turkish states the action is currently happening.
- `UnifiedSearch.SearchEngineSelection.AccessibilityLabels.TopTitle.Label.v133` — `tr/firefox-ios.xliff` — Accessibility label for "This time search in:" omits the "this time" meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu kez şurada ara:`
    - Same as the visible title: the one-off nature of the engine selection ("This time") is not conveyed.
- `UnifiedSearch.SearchEngineSelection.TopTitle.Title.v133` — `tr/firefox-ios.xliff` — "This time search in:" is translated as "Burada ara:" (Search here), losing the "this time" meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu kez şurada ara:`
    - The source emphasizes a one-time engine choice ("This time"); the Turkish only says "Search here", dropping that meaning.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `tr/firefox-ios.xliff` — The condition "For on-device AI" is dropped, turning a conditional statement into an unconditional one.
    - Current: `Cihaza indirilmiş yapay zekâ modelleri kaldırılacaktır.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Cihaz üzerinde çalışan yapay zekâ için indirilmiş tüm modeller kaldırılır.`
    - The source qualifies the removal of downloaded models to on-device AI ("For on-device AI, any downloaded models are removed."); the translation omits this qualifier.
- `Settings.DailyUsagePing.Message.v135` — `tr/firefox-ios.xliff` — The placeholder (company name, e.g. Mozilla) is misplaced so the text reads "active Mozilla users" instead of "helps Mozilla estimate active users".
    - Current: `Bu sayede aktif %@ kullanıcılarının sayısını tahmin edebiliriz.`
    - Source: `This helps %@ to estimate active users.`
    - Suggest: `Bu, %@ kuruluşunun aktif kullanıcı sayısını tahmin etmesine yardımcı olur.`
    - En-US says this helps %@ (Mozilla) estimate active users; the Turkish says "we can estimate the number of active %@ users", changing both the subject and the meaning.
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `tr/firefox-ios.xliff` — The second clause "and how to get the most out of %@" is dropped from the translation.
    - Current: `%@ tarayıcısının kullanışlı özelliklerini öğrenin.`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `%@ tarayıcısının kullanışlı özelliklerini ve ondan en iyi şekilde nasıl yararlanabileceğinizi öğrenin.`
    - En-US: "Learn about useful features and how to get the most out of %@." Half of the source meaning is missing.
- `Settings.Rollouts.Message.v148` — `tr/firefox-ios.xliff` — "between updates" is mistranslated as "with every update" (her güncellemede).
    - Current: `%@ her güncellemede özellikleri, performansı ve kararlılığı iyileştirecektir.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@, güncellemeler arasında özellikleri, performansı ve kararlılığı iyileştirecektir.`
    - En-US says improvements happen between updates (i.e. without an app update); the Turkish says they happen at every update, reversing the intended meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" is translated as "paylaşıldı" (shared) instead of "gönderildi" (sent).
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ ile gönderildi`
    - The source says the link was sent from Firefox; "paylaşıldı" means "was shared", changing the meaning.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `tr/firefox-ios.xliff` — "This page may be restricted" is rendered with an added "içerik içeriyor" construction that mixes the two clauses awkwardly and misstates the meaning.
    - Current: `Bu sayfa kısıtlanmış veya çoğunlukla görsel içerik içeriyor olabilir.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Bu sayfa kısıtlanmış veya çoğunlukla görsel içerikli olabilir.`
    - The source says the page may be restricted or mostly visual; the current wording reads "this page may contain restricted or mostly visual content", shifting the meaning.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `tr/firefox-ios.xliff` — "Sync" is translated as the adjective/participle "Eşitlenen" ("synced") instead of the noun "Eşitleme".
    - Current: `Eşitlenen`
    - Source: `Sync`
    - Suggest: `Eşitleme`
    - Source is the noun "Sync" as a tab-selector title; "Eşitlenen" is a dangling participle ("the synced ...") without a head noun.
- `TabTrayOneDayAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Day Ago" is rendered as "1 gün" ("1 day"), dropping the "ago" relative-time meaning.
    - Current: `1 gün`
    - Source: `1 Day Ago`
    - Suggest: `1 gün önce`
    - The source refers to a point in time (tabs older than 1 day ago); "1 gün" only means "1 day", losing "ago". Sibling strings (1 Week/Month Ago) share the same issue.
- `TabTrayOneMonthAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Month Ago" is rendered as "1 ay" ("1 month"), dropping "ago".
    - Current: `1 ay`
    - Source: `1 Month Ago`
    - Suggest: `1 ay önce`
    - The label denotes a relative time point ("ago"); the Turkish only says "1 month".
- `TabTrayOneWeekAgoTitle.v140` — `tr/firefox-ios.xliff` — "1 Week Ago" is rendered as "1 hafta" ("1 week"), dropping "ago".
    - Current: `1 hafta`
    - Source: `1 Week Ago`
    - Suggest: `1 hafta önce`
    - The label denotes a relative time point ("ago"); the Turkish only says "1 week".
- `TermsOfUse.Title.v142` — `tr/firefox-ios.xliff` — "We’ve got an update" is translated as "Bir haberimiz var" ("We have some news"), losing the notion of an update.
    - Current: `Bir haberimiz var`
    - Source: `We’ve got an update`
    - Suggest: `Bir güncellememiz var`
    - The developer comment states the title indicates there is an update to the terms of use; the Turkish says only "we have news".
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `tr/firefox-ios.xliff` — "Captions are missing" translated as "Altyazılar görünmüyor" (captions are not visible) instead of missing.
    - Current: `Altyazılar görünmüyor`
    - Source: `Captions are missing`
    - Suggest: `Altyazılar eksik`
    - The source says the captions are missing/absent, not that they are not displayed.
- `WorldCup.GroupPhase.GroupStageLabel.v151` — `tr/firefox-ios.xliff` — "Group Stage" (tournament phase) is rendered as "Grup maçı" (group match), naming a single match rather than the phase.
    - Current: `Grup maçı`
    - Source: `Group Stage`
    - Suggest: `Grup aşaması`
    - The developer comment says this is the generic label indicating the Group Stage phase; Turkish "Grup maçı" means "group match", not the stage/phase.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `tr/firefox-ios.xliff` — "Get custom wallpaper" is translated as "Kişisel duvar kâğıdını indir" (download the personal wallpaper), altering the meaning with a definite object and "download".
    - Current: `Kişisel duvar kâğıdını indir`
    - Source: `Get custom wallpaper`
    - Suggest: `Özel duvar kâğıdı edinin`
    - The source refers to obtaining a custom (özel) wallpaper, not downloading a specific personal one; "kişisel" and the definite accusative change the meaning.
- `This action will clear all of your private data, including history from your synced devices.` — `tr/firefox-ios.xliff` — "private data" rendered as "kişisel verileriniz" (personal data) instead of "özel verileriniz".
    - Current: `tüm kişisel verilerinizi`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `tüm özel verilerinizi`
    - The source says "private data", a distinct product term (Private Data / Özel veriler) in Firefox settings, not "personal data".
- `Saved Logins` — `tr/firefox-ios.xliff` — "Saved Logins" is rendered as "Kayıtlı hesaplar" (saved accounts) instead of saved logins/passwords.
    - Current: `Kayıtlı hesaplar`
    - Source: `Saved Logins`
    - Suggest: `Kayıtlı hesap bilgileri`
    - The developer comment says this clears passwords and login data; "hesaplar" means "accounts", which is a different concept from stored logins/credentials.
- `DefaultBrowserCard.BetterInternet.Title.v108` — `tr/firefox-ios.xliff` — "Default to a Better Internet" is translated as "Hep daha iyi bir internet" ("Always a better internet"), losing the call to set the default browser.
    - Current: `Hep daha iyi bir internet`
    - Source: `Default to a Better Internet`
    - Suggest: `Daha iyi bir interneti saptanmış yapın`
    - The source is a play on "default" prompting the user to set Firefox as the default browser; the Turkish drops that meaning entirely and says "always a better internet".
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `tr/firefox-ios.xliff` — "3,000+ trackers" is translated as "3.000 takip kodunu", dropping the "+" (more than).
    - Current: `ortalama 3.000 takip kodunu engelliyor`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `ortalama 3.000’den fazla takip kodunu engelliyor`
    - The en-US states over 3,000 trackers per user per month; the Turkish states exactly 3,000, changing the factual claim.
- `AddPass.Error.Message` — `tr/firefox-ios.xliff` — "Pass" (Wallet kartı/bileti) is mistranslated as "Parola" (password).
    - Current: `Parola Wallet’a eklenirken bir hata oluştu.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Kart Wallet’a eklenirken bir hata oluştu.`
    - The developer comment references Apple Wallet passes; "pass" is a Wallet card/ticket, not a password ("parola").
- `AddPass.Error.Title` — `tr/firefox-ios.xliff` — "Pass" (Wallet kartı) mistranslated as "Parola" (password).
    - Current: `Parola eklenemedi`
    - Source: `Failed to Add Pass`
    - Suggest: `Kart eklenemedi`
    - Per the developer comment this is the Apple Wallet 'Add Pass Failed' alert; a Wallet pass is not a password.
- `Logins.PasscodeRequirement.Warning` — `tr/firefox-ios.xliff` — The Turkish says the user must "set" a device passcode rather than that a passcode must be enabled, and drops "for Firefox" as a separate notion by turning it into a possessive.
    - Current: `Firefox’un otomatik doldurma özelliğini kullanmak için cihaz parolasını ayarlamalısınız.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Firefox’ta otomatik doldurma özelliğini kullanmak için cihazınızda parola etkin olmalıdır.`
    - Source: "To use the AutoFill feature for Firefox, you must have a device passcode enabled." — the requirement is that a passcode be enabled, not that the user configure a specific passcode.
- `Oops! Firefox crashed` — `tr/firefox-ios.xliff` — The interjection "Oops!" is dropped from the translation.
    - Current: `Firefox çöktü`
    - Source: `Oops! Firefox crashed`
    - Suggest: `Hay aksi! Firefox çöktü`
    - The en-US title starts with "Oops!", which is omitted in the Turkish string.
- `Settings.Disconnect.Body` — `tr/firefox-ios.xliff` — "browsing data" is narrowed to "gezinti geçmişiniz" (browsing history).
    - Current: `bu cihazdaki gezinti geçmişiniz silinmeyecek`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `bu cihazdaki gezinti verileriniz silinmeyecek`
    - The source says none of your browsing data will be deleted, not just browsing history.
- `Settings.DisplayTheme.SwitchMode.SectionHeader` — `tr/firefox-ios.xliff` — "Switch Mode" (a section title, i.e. the mode of switching) is rendered as the imperative command "MODU DEĞİŞTİR" ("change the mode").
    - Current: `MODU DEĞİŞTİR`
    - Source: `Switch Mode`
    - Suggest: `DEĞİŞTİRME MODU`
    - The source is a noun-phrase section title naming the switching mode, not an instruction to change a mode; the Turkish imperative reverses the grammatical role.
- `Settings.Home.Option.JumpBackIn` — `tr/firefox-ios.xliff` — "Jump Back In" is translated as "Açık sekmeler" (Open tabs), naming a different homepage section.
    - Current: `Açık sekmeler`
    - Source: `Jump Back In`
    - Suggest: `Kaldığın yerden devam et`
    - The setting toggles the "Jump Back In" section; "Açık sekmeler" means "Open tabs", which is a different feature name and inconsistent with the Firefox naming used elsewhere.
- `more than a month ago` — `tr/firefox-ios.xliff` — "bir aydan önce" means "before one month" rather than "more than a month ago".
    - Current: `bir aydan önce`
    - Source: `more than a month ago`
    - Suggest: `bir aydan eski`
    - The source is a relative date for items older than a month; the sibling string "more than a week ago" is rendered "bir haftadan eski", so this is both wrong and inconsistent.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `tr/firefox-ios.xliff` — "new bookmarks" rendered as "kaydettiğiniz yer imleri" (bookmarks you saved), dropping "new".
    - Current: `kaydettiğiniz yer imleri saklanacaktır`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `yeni yer imleriniz kaydedilecektir`
    - The source says new bookmarks will be saved; the translation changes the meaning to "the bookmarks you saved will be kept".
- `TodayWidget.TopSitesGalleryTitle` — `tr/firefox-ios.xliff` — "Top Sites" rendered as "Sık Kullanılanlar" (Favorites), the wrong feature name.
    - Current: `Sık Kullanılanlar`
    - Source: `Top Sites`
    - Suggest: `En Çok Ziyaret Edilenler`
    - "Top Sites" is the frequently/recently visited sites feature, not bookmarks/favorites; "Sık Kullanılanlar" names a different concept.

### C. Grammar, agreement & spelling

- `MainMenu.SettingsSection.AccessibilityLabels.WhatsNew.v132` — `tr/firefox-ios.xliff` — Wrong apostrophe suffix for "Firefox": should be "%@'taki" → correct vowel harmony gives "Firefox'taki", but the placeholder form used is inconsistent with app name ending.
    - Current: `%@’taki yenilikler`
    - Source: `New in %@`
    - Suggest: `%@’teki yenilikler`
    - Turkish vowel harmony: "Firefox" final vowel is "o"… however the last pronounced syllable of "Firefox" in Turkish is "foks", a front-vowel-less form; standard Turkish usage is "Firefox'taki". Flagging low value.
- `MainMenu.SettingsSection.WhatsNew.Title.v131` — `tr/firefox-ios.xliff` — Wrong Turkish suffix after the app-name placeholder: "%@’taki" should be "%@’teki".
    - Current: `%@’taki yenilikler`
    - Source: `New in %@`
    - Suggest: `%@’teki yenilikler`
    - The app name is Firefox, whose last vowel "o" requires the front/back harmony form used with a hard consonant "x" — Turkish convention renders Firefox'taki. However for the generic placeholder the standard Mozilla tr rendering is "%@ sürümündeki yenilikler"; at minimum the current locked "’taki" is a hard-coded suffix that does not agree with all app names (Focus, Klar → Focus'taki/Klar'daki).
- `Addresses.Settings.SecureSaveInfo.Description.v130` — `tr/firefox-ios.xliff` — Case mismatch: "Bilgilerinizi ... hızlıca erişmek" requires the dative "bilgilerinize" for the verb "erişmek".
    - Current: `Bilgilerinizi daha sonra hızlıca erişmek için güvenli bir şekilde kaydedin.`
    - Source: `Securely save your information to get quick access to it later.`
    - Suggest: `Bilgilerinize daha sonra hızlıca erişebilmek için bilgilerinizi güvenli bir şekilde kaydedin.`
    - The verb "erişmek" governs the dative case; as written the accusative object of "kaydedin" is wrongly reused as the object of "erişmek", producing ungrammatical Turkish.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `tr/firefox-ios.xliff` — Wrong apostrophe suffix vowel for the app name; Turkish requires "-tan" only after back vowels, and "Firefox" takes "-tan" but the placeholder is separated incorrectly with the wrong harmony form.
    - Current: `%@’tan`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `%@’ten`
    - The app name is Firefox, whose final syllable vowel (o... x) — the Turkish convention used elsewhere in Firefox iOS is "Firefox’ten". Consistency with other strings requires the front-vowel form.
- `WebCompatReporter.AdditionalInfo.FooterText.v154` — `tr/firefox-ios.xliff` — Ungrammatical double structure "iyileştirmemize için yardımcı" (superfluous "için" after a dative verbal noun).
    - Current: `iyileştirmemize için yardımcı oluyor`
    - Source: `Your report helps us understand and fix issues in %1$@ to make it better for everyone. %2$@`
    - Suggest: `iyileştirmemize yardımcı oluyor`
    - "-memize" already carries the dative case required by "yardımcı olmak"; adding "için" is grammatically incorrect.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `tr/firefox-ios.xliff` — Inconsistent/incorrect apostrophe suffix casing: "16’LI TUR" should follow vowel harmony as "16’LI" vs the parallel "32’Lİ" — the correct form for 16 (on altı) is "16’LI"? see rationale.
    - Current: `16’LI TUR`
    - Source: `ROUND OF 16`
    - Suggest: `SON 16 TURU`
    - "Round of 16" in Turkish football usage is "Son 16 Turu"; "16’LI TUR" is not an established term and is inconsistent with the sibling string. The suffix also mismatches the sibling "32’Lİ TUR" pattern.
- `TranslationToastHandler.PromptTranslate.Title` — `tr/firefox-ios.xliff` — The translated prompt drops the verb, leaving "Bu sayfa %1$@." without "appears to be in".
    - Current: `Bu sayfa %1$@. %3$@ ile %2$@ye çevrilsin mi?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Bu sayfa %1$@ dilinde görünüyor. %3$@ ile %2$@ diline çevrilsin mi?`
    - en-US says "This page appears to be in %1$@"; the Turkish sentence has no predicate and loses the meaning "appears to be in [language]".
- `Menu.DownloadPDF.Label.v129` — `tr/firefox-ios.xliff` — Incorrect Turkish apostrophe suffix on the acronym PDF; accusative should be "PDF’yi".
    - Current: `PDF’i indir`
    - Source: `Download PDF`
    - Suggest: `PDF’yi indir`
    - "PDF" is read as "pedefe", ending in a vowel sound, so the accusative suffix requires the buffer -y-: PDF’yi.
- `PzSrmZ-scEmjs` — `tr/firefox-ios.xliff` — Missing accusative suffix on "seçtiğiniz"; should be "seçtiğinizi".
    - Current: `seçtiğiniz onaylar mısınız?`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `seçtiğinizi onaylar mısınız?`
    - The verb "onaylamak" requires the accusative object marker, as used correctly in the parallel strings PzSrmZ-2GqvPe and PzSrmZ-eHmH1H.
- `PzSrmZ-xRJbBP` — `tr/firefox-ios.xliff` — Missing accusative suffix on "seçtiğiniz"; should be "seçtiğinizi".
    - Current: `seçtiğiniz onaylar mısınız?`
    - Source: `Just to confirm, you wanted ‘New Search’?`
    - Suggest: `seçtiğinizi onaylar mısınız?`
    - The verb "onaylamak" requires the accusative object marker, as used correctly in the parallel strings PzSrmZ-2GqvPe and PzSrmZ-eHmH1H.

### D. Terminology, register & consistency

- `Settings.Home.Option.TopStories.v143` — `tr/firefox-ios.xliff` — "Top Stories" is rendered as "İlginç yazılar" (Interesting writings), which loses "Top" and conflicts with the other Stories strings in this screen.
    - Current: `İlginç yazılar`
    - Source: `Top Stories`
    - Suggest: `Öne çıkan hikâyeler`
    - "Top" is not conveyed and "Stories" is rendered inconsistently with the other Stories options on the same settings screen ("Haberler", "makaleler").
- `Addresses.EditAddress.AutofillAddressDistrict.v129` — `tr/firefox-ios.xliff` — "District" and "County" are both translated as "İlçe" on the same address form, making the two distinct fields indistinguishable.
    - Current: `İlçe`
    - Source: `District`
    - Suggest: `Semt`
    - Addresses.EditAddress.AutofillAddressCounty.v129 already uses "İlçe" for "County"; two separate address fields on the same screen must not share the same label.
- `Engagement.Notification.Treatment.B.Body.v114` — `tr/firefox-ios.xliff` — Uses the informal singular imperative "gezin" while the sibling notification strings use the polite plural form ("gezinin", "deneyin", "bulun").
    - Current: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezin.`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezinin.`
    - Register inconsistency within the same feature: all other Engagement notification strings address the user with the formal/plural imperative.
- `NativeErrorPage.ButtonLabel.v131` — `tr/firefox-ios.xliff` — "Reload" is rendered as "Tazele" instead of the standard Firefox Turkish term "Yeniden yükle".
    - Current: `Tazele`
    - Source: `Reload`
    - Suggest: `Yeniden yükle`
    - The established Turkish Firefox term for Reload/Refresh is "Yeniden yükle"; "Tazele" is colloquial and inconsistent with the rest of the product.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `tr/firefox-ios.xliff` — Informal second-person singular "dokun" breaks the formal address used in the surrounding Default Browser Popup strings.
    - Current: `Bu iletiyi kapatıp Atla’ya dokun.`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `Bu iletiyi kapatıp Atla’ya dokunun.`
    - Sibling strings in the same popup (DefaultBrowserPopup.SecondLabel "dokunun", FirstLabel "gidin") use the formal plural form; this string switches to informal singular, an inconsistent register on the same screen.
- `Onboarding.Modern.TermsOfService.AgreementButtonTitle.v145` — `tr/firefox-ios.xliff` — "Continue" rendered as "İleri" (Next), inconsistent with the v140 string on the same screen which uses "Devam et".
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam et`
    - The identical source "Continue" is translated "Devam et" in Onboarding.Modern.TermsOfService.AgreementButtonTitle.v140 for the same Terms of Service screen; "İleri" means "Next" and breaks consistency with the accompanying agreement text "Devam ettiğinizde…".
- `Search.Google.Title.v108` — `tr/firefox-ios.xliff` — "Google Search" section header translated as an imperative "Google’da Ara" instead of a noun phrase consistent with the sibling header "%@ araması".
    - Current: `Google’da Ara`
    - Source: `Google Search`
    - Suggest: `Google araması`
    - The string is a section header parallel to Search.EngineSection.Title ("%@ araması"); rendering it as a command is inconsistent within the same screen.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `tr/firefox-ios.xliff` — "Trending Searches" rendered as "Arama trendleri" here but as "gündeminde" elsewhere; inconsistent with the section title wording.
    - Current: `Arama trendlerini göster`
    - Source: `Show Trending Searches`
    - Suggest: `Trend aramaları göster`
    - The same feature (trending searches) is named differently across strings in the same feature file; "Arama trendleri" (search trends) reverses the head noun of "trending searches".
- `Summarizer.ToastLabel.v149` — `tr/firefox-ios.xliff` — "Summary not available" translated with the Arabic-origin "mevcut değil" where standard Firefox tr wording is "kullanılamıyor"/"yok".
    - Current: `Özet mevcut değil`
    - Source: `Summary not available`
    - Suggest: `Özet kullanılamıyor`
    - "not available" is consistently rendered as "kullanılamıyor" in Firefox tr; "mevcut değil" is off-terminology.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `tr/firefox-ios.xliff` — "Enhanced Tracking Protection" is rendered as "gelişmiş izlenme koruması" instead of the established Firefox term "Gelişmiş İzlenme Koruması".
    - Current: `Bu sitenin gelişmiş izlenme koruması ayarı`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Bu sitenin Gelişmiş İzlenme Koruması ayarı`
    - Enhanced Tracking Protection is a Firefox feature name capitalized in Turkish Firefox localization as "Gelişmiş İzlenme Koruması".
- `Enter passcode` — `tr/firefox-ios.xliff` — "passcode" translated as "Parola" (password) instead of "parola kodu/geçiş kodu".
    - Current: `Parolayı girin`
    - Source: `Enter passcode`
    - Suggest: `Geçiş kodunu girin`
    - The source distinguishes passcode from password; Turkish "parola" means password, which conflicts with the passcode terminology used on iOS.
- `Logins` — `tr/firefox-ios.xliff` — "Logins" is rendered as "Hesaplar" (Accounts), which is the wrong term for saved logins/passwords.
    - Current: `Hesaplar`
    - Source: `Logins`
    - Suggest: `Hesap bilgileri`
    - The source term is "Logins" (saved credentials), not "Accounts"; "Hesaplar" collides with the Firefox Account terminology used elsewhere in settings.
- `Menu.RemovePin.Confirm2.v99` — `tr/firefox-ios.xliff` — "Shortcuts" is rendered as "Kestirmeler" here but as "Kısayollar" in the related shortcut string on the same screen.
    - Current: `Kestirmelerden kaldırıldı`
    - Source: `Removed from Shortcuts`
    - Suggest: `Kısayollardan kaldırıldı`
    - Menu.RemovedFromShortcuts.v99 translates "Shortcuts" as "Kısayollar"; the confirmation toast for the same action must use the same term.
- `Logins will be permanently removed.` — `tr/firefox-ios.xliff` — "Logins" is rendered as "Hesaplar" (accounts) instead of the established term for logins/passwords.
    - Current: `Hesaplar kalıcı olarak silinecektir.`
    - Source: `Logins will be permanently removed.`
    - Suggest: `Hesap bilgileri kalıcı olarak silinecektir.`
    - "Logins" means saved login credentials, not accounts; elsewhere in this file the concept is rendered as "parola"/login credentials, making "Hesaplar" inconsistent and inaccurate.
- `Logins will be removed from all connected devices.` — `tr/firefox-ios.xliff` — "Logins" is rendered as "Hesaplar" (accounts) instead of the login-credentials term used elsewhere in the file.
    - Current: `Hesaplar tüm bağlı cihazlardan silinecektir.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `Hesap bilgileri tüm bağlı cihazlardan silinecektir.`
    - "Logins" refers to stored credentials, not user accounts; the same file uses "parola" for the same concept, so "Hesaplar" is inconsistent.
- `No logins found` — `tr/firefox-ios.xliff` — "logins" translated as "hesap" (account) rather than saved login credentials.
    - Current: `Hiç hesap bulunamadı`
    - Source: `No logins found`
    - Suggest: `Hiç hesap bilgisi bulunamadı`
    - The string appears in the Logins list; "logins" are stored credentials, not accounts, and the parallel string NoLoginsFound.Title.v122 uses "Parola".
- `TodayWidget.GoToCopiedLinkLabelV1` — `tr/firefox-ios.xliff` — "link" left as an English loanword instead of the standard Turkish term "bağlantı".
    - Current: `Kopyalanan linke git`
    - Source: `Go to copied link`
    - Suggest: `Kopyalanan bağlantıya git`
    - Firefox Turkish consistently uses "bağlantı" for "link"; "link" is an unadapted anglicism inconsistent with product terminology.
- `TodayWidget.GoToCopiedLinkLabelV2` — `tr/firefox-ios.xliff` — "link" left as an English loanword instead of the standard Turkish term "bağlantı".
    - Current: `Kopyalanan linke git`
    - Source: `Go to Copied Link`
    - Suggest: `Kopyalanan bağlantıya git`
    - Firefox Turkish consistently uses "bağlantı" for "link"; also the source is split over two lines for the widget layout while the translation is one line.
- `PzSrmZ-eHmH1H` — `tr/firefox-ios.xliff` — "Private Tabs" translated as "Özel Sekmeleri" instead of the term "Gizli sekmeler" used elsewhere for the same menu item.
    - Current: `‘Özel Sekmeleri Temizle’`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘Gizli Sekmeleri Temizle’`
    - The menu item eHmH1H and the matching label fi3W24-eHmH1H both use "Gizli sekmeleri temizle"; this confirmation label must reference the same wording.

### E. Typography, punctuation & spacing

- `Privacy` — `tr/firefox-ios.xliff` — Section title is written in all caps unlike the source and other section titles.
    - Current: `GİZLİLİK`
    - Source: `Privacy`
    - Suggest: `Gizlilik`
    - The en-US source is "Privacy" in sentence case; iOS applies its own capitalization to section headers, so hardcoded uppercase deviates from the source and from sibling titles like "Hızlı arama motorları".
- `Settings.Appearance.WebsiteAppearance.SectionHeader.v137` — `tr/firefox-ios.xliff` — Section header is rendered in all caps unlike the source and the parallel "Tarayıcı Teması" header.
    - Current: `WEB SİTESİ GÖRÜNÜMÜ`
    - Source: `Website Appearance`
    - Suggest: `Web sitesi görünümü`
    - The en-US source is "Website Appearance" in title case; the sibling section header Settings.Appearance.BrowserTheme uses normal casing, so all-caps is an inconsistent typographic deviation.
- `TopSites.RemovePage.Button` — `tr/firefox-ios.xliff` — Em dash in the source replaced with a hyphen.
    - Current: `Sayfayı sil - %@`
    - Source: `Remove page — %@`
    - Suggest: `Sayfayı sil — %@`
    - The en-US string uses an em dash (—) as separator; the Turkish uses a plain hyphen.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/tr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
