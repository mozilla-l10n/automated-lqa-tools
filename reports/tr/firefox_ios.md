# Firefox iOS l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `8f5aca68ae4b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 5 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for tr: [android](android.md) · [firefox](firefox.md)

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

- `tr/firefox-ios.xliff` — 19
- `tr/firefox-ios.xliff` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 10, `curly-double` 6 | _mixed_ |
| apostrophe | `typographic` 105 | **typographic** |
| ellipsis | `char` 21 | **char** |
| register | `formal` 7 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (83)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `tr/firefox-ios.xliff` — "For on-device AI" qualifier dropped, so the Turkish asserts all downloaded AI models are removed.
    - Current: `Cihaza indirilmiş yapay zekâ modelleri kaldırılacaktır.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Cihaz üzerinde çalışan yapay zekâ için indirilmiş modeller kaldırılır.`
    - The source restricts model removal to on-device AI features; the Turkish states it unconditionally, changing what the product says it does.
- `Settings.Rollouts.Message.v148` — `tr/firefox-ios.xliff` — "between updates" is translated as "in every update", reversing the point that improvements happen without an update.
    - Current: `%@ her güncellemede özellikleri`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@, güncellemeler arasında özellikleri`
    - Source says changes are applied remotely between updates; "her güncellemede" (with every update) says the opposite.
- `Settings.SendUsage.Message` — `tr/firefox-ios.xliff` — Turkish drops "to provide" and "for everyone", and uses "daha da geliştirmek" (improve further) only.
    - Current: `Mozilla, yalnızca Firefox’u daha da geliştirmek için ihtiyaç duyduğumuz verileri toplar.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla, Firefox’u herkese sunmak ve geliştirmek için yalnızca ihtiyaç duyduğumuz verileri toplamaya çalışır.`
    - The source says Mozilla strives to only collect what is needed to provide and improve Firefox for everyone; the Turkish omits "provide", "for everyone" and the "strives" hedge, stating flatly that Mozilla only collects needed data.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 45 |
| 3 | Degraded language (grammar, spelling, terminology) | 35 |
| 4 | Cosmetic (typography, spacing) | 3 |

### A. Functional, markup, variables & plurals

- `FirefoxHomepage.Pocket.Footer.Title.v116` — `tr/firefox-ios.xliff` — Placeholder roles are swapped: %2$@ (app name) is used as the "powered by" source and %1$@ (Pocket) as the family name.
    - Current: `%2$@ ailesinden %1$@ desteğiyle.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `%1$@ desteğiyle. %2$@ ailesinden bir ürün.`
    - The comment says %1$@ is Pocket and %2$@ is the app name; the source means "Powered by Pocket. Part of the Firefox family." The Turkish reads "Powered by Pocket from the Firefox family" — actually it renders as "%2$@ ailesinden %1$@ desteğiyle" which attributes the family to the wrong element order, losing the two-sentence meaning.
- `TodayWidget.ClosePrivateTabsLabelV2` — `tr/firefox-ios.xliff` — The two-line layout is broken: the line break falls after a single word "Gizli" leaving "sekmeleri kapat" on line two.
    - Current: `Gizli sekmeleri kapat`
    - Source: `Close Private Tabs`
    - Suggest: `Gizli sekmeleri kapat`
    - The source splits the label into two balanced lines ("Close" / "Private Tabs"); the Turkish break splits the noun phrase awkwardly.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.AppIconNames.Twilight.Title.v137` — `tr/firefox-ios.xliff` — "Twilight" (dusk) is translated as "Şafak" (dawn), the opposite time of day.
    - Current: `Şafak`
    - Source: `Twilight`
    - Suggest: `Alacakaranlık`
    - The source "Twilight" refers to dusk/alacakaranlık; "Şafak" means dawn/daybreak, which is also confusable with the separate "Sunrise" (Gün doğumu) icon in the same list.
- `Settings.AppIconSelection.SectionNames.Basics.Title.v139` — `tr/firefox-ios.xliff` — Section heading "Basics" rendered as the adjective "Basit" (simple) instead of a noun heading like "Temel".
    - Current: `Basit`
    - Source: `Basics`
    - Suggest: `Temeller`
    - "Basics" is a section name for the basic icon variants; "Basit" means "simple", not "basics", and does not match the plural section-heading pattern of the neighbouring "Renkler"/"Renk geçişleri".
- `Settings.Home.Option.Stories.v140` — `tr/firefox-ios.xliff` — "Stories" is rendered as "Haberler" (News), which names a different content type.
    - Current: `Haberler`
    - Source: `Stories`
    - Suggest: `Hikâyeler`
    - The source term is "Stories" (recommended articles/stories section), not "News"; other related strings in the same file translate stories as "makaleler/yazılar", so "Haberler" is both wrong and inconsistent.
- `Settings.Home.Option.ThoughtProvokingStories.subtitle.v116` — `tr/firefox-ios.xliff` — "powered by" rendered as "derlenen" (compiled by), changing the meaning.
    - Current: `%@ tarafından derlenen makaleler`
    - Source: `Articles powered by %@`
    - Suggest: `%@ destekli makaleler`
    - The source says the articles are powered by Pocket, not compiled/curated by it.
- `Settings.Home.Option.TopStories.v143` — `tr/firefox-ios.xliff` — "Top Stories" translated as "İlginç yazılar" (Interesting articles), losing the "top/most popular" meaning.
    - Current: `İlginç yazılar`
    - Source: `Top Stories`
    - Suggest: `Öne çıkan yazılar`
    - The source says "Top Stories"; "İlginç" means "interesting", not "top/featured".
- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `tr/firefox-ios.xliff` — "Prefecture" translated as "Vilayet" (province), the Japanese administrative division term is "Prefektür".
    - Current: `Vilayet`
    - Source: `Prefecture`
    - Suggest: `Prefektür`
    - Per the developer comment this is the Japanese-style prefecture field; "Vilayet" is the Ottoman/Turkish province term and names a different division.
- `Addresses.EditAddress.AutofillAddressProvince.v129` — `tr/firefox-ios.xliff` — "Province" is rendered "İl", the same concept Turkish uses for state/province, conflicting with the separate "State" field and losing the distinction.
    - Current: `İl`
    - Source: `Province`
    - Suggest: `Eyalet/Bölge (ör. "İl/Bölge" ayrımı) – örn. "Eyalet" yerine "İl", "Province" için "Vilayet/Bölge"`
    - The file contains both Province and State as distinct labels; rendering Province as "İl" while State is "Eyalet" is defensible, but Province in Turkish address forms is normally "İl/Eyalet" distinction—flagged as possible terminology overlap.
- `Engagement.Notification.Body.v112` — `tr/firefox-ios.xliff` — The translation invents "restaurants nearby" where the source says only "something nearby".
    - Current: `İster yakınınızdaki restoranları bulun, ister eğlenceli bir şeyler keşfedin.`
    - Source: `Find something nearby. Or discover something fun.`
    - Suggest: `İster yakınınızdaki bir şeyi bulun, ister eğlenceli bir şeyler keşfedin.`
    - en-US "Find something nearby" is generic; the Turkish narrows it to restaurants, adding content not in the source.
- `FirefoxHomepage.FeltPrivacyUI.Body.v122` — `tr/firefox-ios.xliff` — "deletes" rendered as "temizler" (clears) while the same feature elsewhere uses "silindi"; minor but inconsistent term for deletion.
    - Current: `site verilerinizi temizler`
    - Source: `%@ deletes your cookies, history, and site data when you close all your private tabs.`
    - Suggest: `site verilerinizi siler`
    - The source says "deletes"; the sibling string FeltDeletion.Link uses "silindi" for the same action, so "temizler" is inconsistent within the same feature.
- `MainMenu.AccessibilityLabels.DismissBanner.142` — `tr/firefox-ios.xliff` — "banner" translated as "Bildirim" (notification) instead of banner.
    - Current: `Bildirimi kapat`
    - Source: `Dismiss banner`
    - Suggest: `Banner’ı kapat`
    - The developer comment specifies the dismiss button for the header banner on top of the menu; "Bildirim" means notification, a different UI element.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `tr/firefox-ios.xliff` — "your support team might have more info" rendered as an assertion that the support team can give information, dropping the "more info" nuance.
    - Current: `destek ekibiniz size bilgi verebilir`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `destek ekibiniz daha fazla bilgi verebilir`
    - The source says the support team might have more info; the Turkish drops "more", weakening the meaning.
- `Onboarding.Customization.Intro.Continue.Action.v123` — `tr/firefox-ios.xliff` — Button label adds "tarayıcısını" (the browser) which the source does not contain, and lengthens a button.
    - Current: `%@ tarayıcısını özelleştirin`
    - Source: `Customize %@`
    - Suggest: `%@ tarayıcısını özelleştir`
    - Source is the button action "Customize %@"; sibling buttons in the same flow use the imperative short form ("Kaydet ve devam et", "Atla"), so the -in form is inconsistent register for a button.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `tr/firefox-ios.xliff` — "and that you use it" is mistranslated as "and that you use [it]" merged into "how you discovered and used it", losing the meaning.
    - Current: `%1$@’u nasıl keşfettiğinizi ve kullandığınızı`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `%1$@’u nasıl keşfettiğinizi ve kullandığınız bilgisini`
    - The source says the shared data is how you discovered Firefox and the fact that you use it; the Turkish reads as "how you discovered and how you used it", which asserts sharing usage details.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `tr/firefox-ios.xliff` — "the browser" is rendered as "uygulamayı geliştirmemize" ("to help us improve the app"), adding a first-person claim not in the source.
    - Current: `uygulamayı geliştirmemize yardımcı olmak için`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmeye yardımcı olmak için`
    - The en-US says "To help improve the browser"; the Turkish says "to help us improve the app", changing the object and adding "us".
- `Onboarding.Modern.TermsOfService.ManagePreferenceAgreement.v145` — `tr/firefox-ios.xliff` — "the browser" translated as "uygulamayı" (the app), inconsistent with the v140 variant of the same string which uses "tarayıcıyı".
    - Current: `uygulamayı geliştirmemize`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `tarayıcıyı geliştirmemize`
    - Source says "To help improve the browser"; the identical v140 string is rendered "tarayıcıyı". "uygulamayı" means "the app".
- `Onboarding.Sync.Title.v120` — `tr/firefox-ios.xliff` — "Stay encrypted" is rendered as the vague "securely", dropping the encryption claim.
    - Current: `Cihazlarınız arasında güvenle geçiş yapın`
    - Source: `Stay encrypted when you hop between devices`
    - Suggest: `Cihazlarınız arasında geçiş yaparken şifreli kalın`
    - The source specifically promises encryption when hopping between devices; "güvenle" only says "safely".
- `PasswordAutofill.SignInWithSavedPassword.v124` — `tr/firefox-ios.xliff` — Future "You'll sign into %@" rendered as present progressive "you are signing in".
    - Current: `%@ sitesine giriş yapıyorsunuz`
    - Source: `You’ll sign into %@`
    - Suggest: `%@ sitesine giriş yapacaksınız`
    - The en-US "You’ll sign into %@" states what will happen if the saved password is used; the Turkish states it is happening now.
- `PrivacyDashboard.CategoryAccessibilityLabel.v156` — `tr/firefox-ios.xliff` — Accessibility label adds "takip kodu" (tracker) although %1$@ is already the category name and %2$@ the count.
    - Current: `%1$@, %2$@ takip kodu engellendi`
    - Source: `%1$@, blocked: %2$@`
    - Suggest: `%1$@, engellenen: %2$@`
    - Per the comment, %1$@ is the category name (e.g. Fingerprinters) and %2$@ the count; the source is "%1$@, blocked: %2$@". Inserting "takip kodu" mislabels e.g. cookies/content categories as trackers.
- `SecondaryButton.Label.v112` — `tr/firefox-ios.xliff` — "No Thanks" rendered as just "Hayır", dropping the "thanks" politeness element.
    - Current: `Hayır`
    - Source: `No Thanks`
    - Suggest: `Hayır, teşekkürler`
    - The source is "No Thanks"; Turkish convention for this button is "Hayır, teşekkürler". "Hayır" alone drops part of the source meaning/register.
- `UnifiedSearch.SearchEngineSelection.AccessibilityLabels.TopTitle.Label.v133` — `tr/firefox-ios.xliff` — "This time search in:" is rendered as "Burada ara:" ("Search here"), losing the "this time" one-off meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu defalık şurada ara:`
    - The source says the chosen engine applies only to this search ("This time search in:"); the Turkish drops "this time" entirely and says "Search here".
- `UnifiedSearch.SearchEngineSelection.TopTitle.Title.v133` — `tr/firefox-ios.xliff` — "This time search in:" is rendered as "Burada ara:" ("Search here"), losing the "this time" one-off meaning.
    - Current: `Burada ara:`
    - Source: `This time search in:`
    - Suggest: `Bu defalık şurada ara:`
    - The source indicates the engine choice applies only to the current search; the Turkish omits "this time".
- `Search.Google.Title.v108` — `tr/firefox-ios.xliff` — Section header "Google Search" translated as an imperative "Google’da Ara" ("Search on Google") instead of a noun phrase.
    - Current: `Google’da Ara`
    - Source: `Google Search`
    - Suggest: `Google araması`
    - This is a section header separating suggestion results, parallel to "%@ araması" for Search.EngineSection.Title; rendering it as a command is inconsistent and wrong in register for a header.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `tr/firefox-ios.xliff` — "For on-device AI" qualifier dropped, so the Turkish asserts all downloaded AI models are removed.
    - Current: `Cihaza indirilmiş yapay zekâ modelleri kaldırılacaktır.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Cihaz üzerinde çalışan yapay zekâ için indirilmiş modeller kaldırılır.`
    - The source restricts model removal to on-device AI features; the Turkish states it unconditionally, changing what the product says it does.
- `Settings.DailyUsagePing.Message.v135` — `tr/firefox-ios.xliff` — The %@ company name is turned into a modifier of "users", so the sentence claims to count Mozilla's users instead of helping Mozilla estimate active users.
    - Current: `Bu sayede aktif %@ kullanıcılarının sayısını tahmin edebiliriz.`
    - Source: `This helps %@ to estimate active users.`
    - Suggest: `Bu, %@’nın aktif kullanıcı sayısını tahmin etmesine yardımcı olur.`
    - Source: "This helps %@ to estimate active users." — %@ is the company name (Mozilla), the subject that estimates, not a qualifier of the users; the translation also shifts to first person "we".
- `Settings.Notifications.SyncNotificationsStatus.v112` — `tr/firefox-ios.xliff` — "sign in on another device" is rendered as signing in "from" another device, changing the meaning.
    - Current: `başka bir cihazdan giriş yaptığınızda`
    - Source: `This must be turned on to receive tabs and get notified when you sign in on another device.`
    - Suggest: `başka bir cihazda giriş yaptığınızda`
    - The source says you get notified when you sign in on another device; "cihazdan" (from another device) is a different claim.
- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `tr/firefox-ios.xliff` — The second clause "and how to get the most out of %@" is dropped from the translation.
    - Current: `%@ tarayıcısının kullanışlı özelliklerini öğrenin.`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `%@ tarayıcısının kullanışlı özelliklerini ve ondan en iyi şekilde nasıl yararlanacağınızı öğrenin.`
    - Source: "Learn about useful features and how to get the most out of %@." — half the sentence is missing.
- `Settings.Rollouts.Message.v148` — `tr/firefox-ios.xliff` — "between updates" is translated as "in every update", reversing the point that improvements happen without an update.
    - Current: `%@ her güncellemede özellikleri`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@, güncellemeler arasında özellikleri`
    - Source says changes are applied remotely between updates; "her güncellemede" (with every update) says the opposite.
- `Settings.Search.GoogleLens.Footnote.v153` — `tr/firefox-ios.xliff` — "enabled above" becomes "enabled from above" and "while browsing" is dropped.
    - Current: `Yalnızca yukarıdan Google etkinleştirildiğinde ve aktif arama motorunuz olarak ayarlandığında kullanılabilir.`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Yalnızca Google yukarıda etkinleştirildiğinde ve gezinirken aktif arama motorunuz olduğunda kullanılabilir.`
    - Source: "Available only when Google is enabled above and is your active search engine while browsing." — "while browsing" is missing and "yukarıdan" misstates "above" as the means of enabling.
- `Settings.Studies.Message.v148` — `tr/firefox-ios.xliff` — "test features" translated as "yeni özellikleri test eder" adding "new", and the clause is restructured into a first-person claim.
    - Current: `%@ rastgele bazı kullanıcıları seçerek yeni özellikleri test eder. Böylece herkes için kaliteyi artırabiliriz.`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `%@ özellikleri test etmek için rastgele kullanıcılar seçer, bu da herkes için kaliteyi artırır.`
    - The source says the app selects users to test features, which improves quality for everyone; the Turkish adds "new" and turns the result clause into "so we can improve quality", a statement the source does not make.
- `Settings.Translation.AutoTranslate.Footer.v151` — `tr/firefox-ios.xliff` — "top preferred language" is rendered as just "tercih ettiğiniz dile", dropping "top".
    - Current: `Sayfaları tercih ettiğiniz dile otomatik olarak çevirir.`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `Sayfaları en çok tercih ettiğiniz dile otomatik olarak çevirir.`
    - The source specifies the top (first) preferred language in the preferred-languages list, not just any preferred language; the distinction matters on a screen where multiple preferred languages can be added.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" is rendered as "shared with/via %2$@" but the Turkish phrasing says the link was shared *with* the app rather than sent from Firefox.
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ tarayıcısından gönderildi`
    - The source states the link was sent from the browser (Firefox); "%2$@ ile paylaşıldı" reads as "shared with %2$@", changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" mistranslated as "shared with %2$@".
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@ tarayıcısından gönderildi`
    - The source says the link was sent from the app (Firefox), not shared with it.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `tr/firefox-ios.xliff` — "Sent from %2$@" mistranslated as "shared with %2$@".
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ tarayıcısından gönderildi`
    - The source says the link was sent from the app (Firefox), not shared with it.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `tr/firefox-ios.xliff` — "Sent from %2$@" mistranslated as "shared with %2$@".
    - Current: `%2$@ ile paylaşıldı`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@ tarayıcısından gönderildi`
    - The source says the link was sent from the app (Firefox), not shared with it.
- `WebCompatReporter.Fields.ChooseSubOptionAccessibilityHint.v156` — `tr/firefox-ios.xliff` — "specific problem" rendered as plain "bir sorun", losing the distinction between issue type and specific problem.
    - Current: `Seçtiğiniz sorun türüyle ilgili bir sorun seçin`
    - Source: `Choose a specific problem for your selected issue type`
    - Suggest: `Seçtiğiniz sorun türü için belirli bir sorun seçin`
    - The source asks the user to choose a specific problem for the selected issue type; omitting "specific" makes the hint circular and unclear.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `tr/firefox-ios.xliff` — "Captions are missing" translated as "captions are not visible" instead of "missing".
    - Current: `Altyazılar görünmüyor`
    - Source: `Captions are missing`
    - Suggest: `Altyazılar eksik`
    - The source says the captions are missing (absent), not that they are not displayed; elsewhere in the same screen "missing" is rendered as "eksik" (Missing items → Öğeler eksik, Media controls are broken or missing → ... veya eksik).
- `WorldCup.GroupPhase.GroupStageLabel.v151` — `tr/firefox-ios.xliff` — "Group Stage" is rendered as "Grup maçı" (group match) instead of the tournament phase name.
    - Current: `Grup maçı`
    - Source: `Group Stage`
    - Suggest: `Grup aşaması`
    - The source names the tournament phase (Group Stage), not a single match; the established Turkish football term is "grup aşaması".
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `tr/firefox-ios.xliff` — "Get custom wallpaper" translated as "Kişisel duvar kâğıdını indir" (download your personal wallpaper).
    - Current: `Kişisel duvar kâğıdını indir`
    - Source: `Get custom wallpaper`
    - Suggest: `Özel duvar kâğıdını edinin`
    - "Custom" here means a special/themed wallpaper provided by the app, not the user's personal one; "kişisel" wrongly implies the user's own wallpaper.
- `WorldCup.HomepageWidget.RoundPhase.WinWorldCupLabel.v151` — `tr/firefox-ios.xliff` — Plural "CHAMPIONS" rendered as singular "ŞAMPİYONU".
    - Current: `2026 DÜNYA KUPASI ŞAMPİYONU`
    - Source: `2026 WORLD CUP CHAMPIONS`
    - Suggest: `2026 DÜNYA KUPASI ŞAMPİYONLARI`
    - The source says "2026 WORLD CUP CHAMPIONS" (plural, the winning team); the Turkish uses the singular form.
- `Enter passcode` — `tr/firefox-ios.xliff` — "passcode" is translated as "parola" (password) instead of the passcode/PIN term.
    - Current: `Parolayı girin`
    - Source: `Enter passcode`
    - Suggest: `Geçiş kodunu girin`
    - The source refers to the device/app passcode, not a password; "parola" is the established Firefox term for "password" and conflicts with it on the same authentication screen.
- `This action will clear all of your private data, including history from your synced devices.` — `tr/firefox-ios.xliff` — "private data" rendered as "kişisel verilerinizi" (personal data) rather than private/özel data.
    - Current: `tüm kişisel verilerinizi kaldıracaktır`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `tüm özel verilerinizi temizleyecektir`
    - The source says "private data"; "kişisel veri" means personal data (a distinct legal/privacy term) and misstates what is cleared.
- `Spotlight Index` — `tr/firefox-ios.xliff` — Apple's "Spotlight" brand name dropped from the translation.
    - Current: `Arama indeksi`
    - Source: `Spotlight Index`
    - Suggest: `Spotlight indeksi`
    - The developer comment explicitly refers to Apple's “Spotlight Search”; the brand name should be retained as in the source.
- `ActivityStream.JumpBackIn.SectionTitle` — `tr/firefox-ios.xliff` — "Jump Back In" is rendered as "Açık sekmeler" (Open tabs), which names a different section.
    - Current: `Açık sekmeler`
    - Source: `Jump Back In`
    - Suggest: `Kaldığınız yerden devam edin`
    - The source is the "Jump Back In" section title for recently viewed tabs; "Açık sekmeler" means "Open tabs", a different feature name in Firefox.
- `AddPass.Error.Message` — `tr/firefox-ios.xliff` — "pass" (Wallet kartı/bilet) is mistranslated as "Parola" (password).
    - Current: `Parola Wallet’a eklenirken bir hata oluştu.`
    - Source: `An error occured while adding the pass to Wallet. Please try again later.`
    - Suggest: `Kart Wallet’a eklenirken bir hata oluştu.`
    - The developer comment points to Apple Wallet passes; "pass" is a Wallet pass (kart/bilet), not a password ("parola").
- `AddPass.Error.Title` — `tr/firefox-ios.xliff` — "Pass" in "Failed to Add Pass" is mistranslated as "Parola" (password).
    - Current: `Parola eklenemedi`
    - Source: `Failed to Add Pass`
    - Suggest: `Kart eklenemedi`
    - The alert concerns adding an Apple Wallet pass, not a password.
- `BreachAlerts.Link` — `tr/firefox-ios.xliff` — "Go to" rendered as "Git" loses the sense of leading to the breached site link.
    - Current: `Git`
    - Source: `Go to`
    - Suggest: `Şuraya git:`
    - The comment says the string leads into a link to the breached website; "Go to" is a prefix to a URL, while "Git" alone reads as a standalone button.
- `FirefoxHome.Pocket.SectionTitle` — `tr/firefox-ios.xliff` — "Stories" translated as "makaleler" (articles) instead of "hikâyeler/öyküler".
    - Current: `Merak uyandıran makaleler`
    - Source: `Thought-Provoking Stories`
    - Suggest: `Merak uyandıran hikâyeler`
    - The source says "Thought-Provoking Stories"; "makaleler" means articles, a different term than the Stories/Pocket story terminology used elsewhere.
- `Menu.RemoveBookmark.Confirm` — `tr/firefox-ios.xliff` — "Bookmark Removed" translated as "silindi" (deleted) instead of "kaldırıldı" (removed), inconsistent with the button label "Kaldır".
    - Current: `Yer imi silindi`
    - Source: `Bookmark Removed`
    - Suggest: `Yer imi kaldırıldı`
    - The source verb is "Removed", matching Menu.RemoveBookmark.Label.v99 "Kaldır"; "silindi" means deleted.
- `SentTab_TabArrivingNotification_WithDevice_title` — `tr/firefox-ios.xliff` — "Tab received from %@" is rendered as "%@ sent a tab", changing the meaning and grammar of the notification title.
    - Current: `%@ sekme gönderdi`
    - Source: `Tab received from %@`
    - Suggest: `%@ cihazından sekme alındı`
    - The source states a tab was received from the named device; the Turkish asserts the device sent a tab, an active statement not in the source and inconsistent with the sibling title "Sekme alındı".
- `Settings.Home.Option.JumpBackIn` — `tr/firefox-ios.xliff` — "Jump Back In" is rendered as "Açık sekmeler" (Open tabs), naming a different homepage section.
    - Current: `Açık sekmeler`
    - Source: `Jump Back In`
    - Suggest: `Kaldığın yerden devam et`
    - The source is the name of the "Jump Back In" homepage section; "Açık sekmeler" means "Open tabs", which is a different feature/section name and misidentifies the toggle.
- `Settings.Home.Option.Wallpaper.CollectionTitle` — `tr/firefox-ios.xliff` — Wallpaper section title translated as "AÇILIŞ EKRANI" (Opening screen) instead of wallpaper.
    - Current: `AÇILIŞ EKRANI`
    - Source: `OPENING SCREEN`
    - Suggest: `DUVAR KÂĞIDI`
    - Per the developer comment this titles the wallpaper settings section; the en-US source string "OPENING SCREEN" appears reused, but the Turkish repeats the Start-at-Home title and does not describe the wallpaper section.
- `Settings.SendUsage.Message` — `tr/firefox-ios.xliff` — Turkish drops "to provide" and "for everyone", and uses "daha da geliştirmek" (improve further) only.
    - Current: `Mozilla, yalnızca Firefox’u daha da geliştirmek için ihtiyaç duyduğumuz verileri toplar.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla, Firefox’u herkese sunmak ve geliştirmek için yalnızca ihtiyaç duyduğumuz verileri toplamaya çalışır.`
    - The source says Mozilla strives to only collect what is needed to provide and improve Firefox for everyone; the Turkish omits "provide", "for everyone" and the "strives" hedge, stating flatly that Mozilla only collects needed data.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `tr/firefox-ios.xliff` — "a few moments" rendered as "birkaç dakika" (a few minutes).
    - Current: `Birkaç dakika sonra yeniden deneyin.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `Birazdan yeniden deneyin.`
    - The source says "in a few moments", not a specific number of minutes.
- `TopSites.RemovePage.Button` — `tr/firefox-ios.xliff` — "Remove page" translated as "Sayfayı sil" (delete page) instead of remove.
    - Current: `Sayfayı sil - %@`
    - Source: `Remove page — %@`
    - Suggest: `Sayfayı kaldır — %@`
    - Source says remove the site from the top sites panel, not delete; also the em dash of the source was replaced with a hyphen.
- `more than a month ago` — `tr/firefox-ios.xliff` — "more than a month ago" is rendered as "bir aydan önce", which means "before one month" rather than "more than a month ago".
    - Current: `bir aydan önce`
    - Source: `more than a month ago`
    - Suggest: `bir aydan eski`
    - The source is a relative date meaning older than a month; the parallel string "more than a week ago" is correctly rendered "bir haftadan eski". "bir aydan önce" is ungrammatical/wrong in Turkish for this meaning.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `tr/firefox-ios.xliff` — "new bookmarks" is rendered as "kaydettiğiniz yer imleri" (bookmarks you saved), losing "new".
    - Current: `ama kaydettiğiniz yer imleri saklanacaktır`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `ama yeni yer imleriniz kaydedilecektir`
    - The source says new bookmarks will be saved; the Turkish says the bookmarks you saved will be kept, a different claim about behaviour.
- `TodayWidget.TopSitesGalleryTitle` — `tr/firefox-ios.xliff` — "Top Sites" translated as "Sık Kullanılanlar" (Favorites) instead of the established "En çok ziyaret edilen siteler".
    - Current: `Sık Kullanılanlar`
    - Source: `Top Sites`
    - Suggest: `En Çok Ziyaret Edilen Siteler`
    - "Sık Kullanılanlar" is the standard Turkish term for Favorites/Bookmarks and names a different feature than Top Sites.

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.AppIconNames.Midday.Title.v137` — `tr/firefox-ios.xliff` — "Midday" translated as colloquial "Öğlen" instead of the standard noun "Öğle".
    - Current: `Öğlen`
    - Source: `Midday`
    - Suggest: `Öğle`
    - "Öğlen" is a colloquial adverbial form; the standard Turkish noun for midday used as a label is "Öğle".
- `Addresses.Settings.SecureSaveInfo.Description.v130` — `tr/firefox-ios.xliff` — Case error: "Bilgilerinizi ... hızlıca erişmek" — the verb "erişmek" requires the dative "bilgilerinize".
    - Current: `Bilgilerinizi daha sonra hızlıca erişmek için güvenli bir şekilde kaydedin.`
    - Source: `Securely save your information to get quick access to it later.`
    - Suggest: `Bilgilerinize daha sonra hızlıca erişebilmek için bilgilerinizi güvenli bir şekilde kaydedin.`
    - "erişmek" governs the dative case; the sentence as written is ungrammatical.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `tr/firefox-ios.xliff` — Redundant/awkward wording "görsel içerik içeriyor" duplicates the noun "içerik".
    - Current: `çoğunlukla görsel içerik içeriyor olabilir`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `çoğunlukla görsel ağırlıklı olabilir`
    - The source reads "may be restricted or mostly visual"; the Turkish repeats "içerik ... içeriyor", which is ungrammatical-sounding repetition.
- `TermsOfUse.TitleValue2.v147` — `tr/firefox-ios.xliff` — Wrong apostrophe suffix vowel harmony for "Firefox": should be ’ten, not ’tan.
    - Current: `%@’tan bir not`
    - Source: `A note from %@`
    - Suggest: `%@’ten bir not`
    - The app name is Firefox; the ablative suffix after front-vowel final syllable "-fox"... Turkish convention for Firefox is "Firefox’tan"? Actually Firefox is pronounced with back vowel 'o', so "Firefox’tan" is used across Mozilla tr. Flagging only if inconsistent.
- `WebCompatReporter.AdditionalInfo.FooterText.v154` — `tr/firefox-ios.xliff` — Ungrammatical double construction "iyileştirmemize için" in the footer text.
    - Current: `böylece uygulamayı herkes için iyileştirmemize için yardımcı oluyor`
    - Source: `Your report helps us understand and fix issues in %1$@ to make it better for everyone. %2$@`
    - Suggest: `böylece uygulamayı herkes için iyileştirmemize yardımcı oluyor`
    - "iyileştirmemize" already carries the dative required by "yardımcı oluyor"; the extra "için" makes the sentence ungrammatical.
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `tr/firefox-ios.xliff` — Vowel harmony/suffix error: "16’LI TUR" should be "16’LIK TUR" or, consistent with the Round-of-32 string, "16’LI" must match the pattern used elsewhere.
    - Current: `16’LI TUR`
    - Source: `ROUND OF 16`
    - Suggest: `16’LİK TUR`
    - "16" (on altı) ends in the vowel ı, so the suffix is -lık, not -lı; the parallel string uses "32’Lİ TUR" (otuz iki → -lik), showing inconsistent suffixation.
- `Settings.Home.Option.Wallpaper.SwitchTitle.v99` — `tr/firefox-ios.xliff` — Toggle label rendered as an imperative sentence rather than a noun phrase title.
    - Current: `Giriş sayfasındaki Firefox logosuna dokunarak duvar kâğıdını değiştirin`
    - Source: `Change wallpaper by tapping Firefox homepage logo`
    - Suggest: `Giriş sayfasındaki Firefox logosuna dokunarak duvar kâğıdını değiştir`
    - The source is a switch title describing the function ("Change wallpaper by tapping..."), not an instruction to the user; the imperative "değiştirin" misreads it as a command.
- `TranslationToastHandler.PromptTranslate.Title` — `tr/firefox-ios.xliff` — The first sentence drops "appears to be in", leaving an ungrammatical fragment "Bu sayfa %1$@."
    - Current: `Bu sayfa %1$@. %3$@ ile %2$@ye çevrilsin mi?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Bu sayfa %1$@ dilinde görünüyor. %3$@ ile %2$@ diline çevrilsin mi?`
    - en-US: "This page appears to be in %1$@." The Turkish omits the verb and the word "dilinde", producing an incomplete sentence; also the suffix on %2$@ ("%2$@ye") cannot agree with an arbitrary language name.
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

- `LoginsList.NoLoginsFound.Description.v122` — `tr/firefox-ios.xliff` — "sync" is rendered as "senkronize" while the rest of the tr localization uses "eşitle" (cf. Bookmarks.EmptyState.Root.ButtonTitle "Eşitlemek için giriş yap").
    - Current: `senkronize ettiğiniz`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `eşitlediğiniz`
    - Terminology inconsistency: Firefox tr consistently translates "sync" as "eşitleme", not "senkronizasyon".
- `CreditCard.EditCard.ExpiredDateTitle.v112` — `tr/firefox-ios.xliff` — "Son kullanım tarihi" is inconsistent with "Son kullanma tarihi" used for the expiration field in the same screen.
    - Current: `Son kullanım tarihi: %@`
    - Source: `Expires %@`
    - Suggest: `Son kullanma tarihi: %@`
    - CreditCard.EditCard.CardExpirationDateTitle.v112 uses "Son kullanma tarihi"; the same source term should be rendered consistently within the screen.
- `Engagement.Notification.Treatment.B.Body.v114` — `tr/firefox-ios.xliff` — Informal imperative "gezin" breaks the locale's formal register used in the sibling notification strings.
    - Current: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezin.`
    - Source: `Browse with no saved cookies or history in %@.`
    - Suggest: `%@ ile çerezleriniz ve geçmişiniz kaydedilmeden gezinin.`
    - The tr locale uses the formal address form (e.g. "Gizli gezintiyi deneyin", "İz bırakmadan gezinin" in the same file); "gezin" is the informal second-person singular.
- `NativeErrorPage.ButtonLabel.v131` — `tr/firefox-ios.xliff` — "Reload" translated as "Tazele" instead of the standard Firefox term "Yeniden yükle".
    - Current: `Tazele`
    - Source: `Reload`
    - Suggest: `Yeniden yükle`
    - Firefox tr consistently uses "Yeniden yükle" for Reload; "Tazele" is not the established term.
- `DefaultBrowserPopup.DescriptionFooter.v124` — `tr/firefox-ios.xliff` — Informal imperative "dokun" breaks the formal register used in the surrounding Default Browser Popup strings.
    - Current: `Bu iletiyi kapatıp Atla’ya dokun.`
    - Source: `*Is %@ already your default?* Close this message and tap Skip.`
    - Suggest: `Bu iletiyi kapatıp Atla’ya dokunun.`
    - The locale convention is formal address, and the sibling strings use "dokunun"/"gidin"; this string uses the informal singular "dokun".
- `Onboarding.Modern.Welcome.Title.v145` — `tr/firefox-ios.xliff` — "trackers" rendered as "takip kodları" whereas the established Firefox tr term for trackers in this context is "takipçiler".
    - Current: `Ürpertici takip kodlarına veda edin`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `Ürpertici takipçilere veda edin`
    - Firefox tr uses "takipçi" for tracker (e.g. "izlenme koruması"); "takip kodu" is a different, script-specific term.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `tr/firefox-ios.xliff` — "Trending Searches" is translated as "Arama trendleri" here but as "gündem" in the related section title, and it is inconsistent with "Son aramaları göster".
    - Current: `Arama trendlerini göster`
    - Source: `Show Trending Searches`
    - Suggest: `Gündemdeki aramaları göster`
    - The same feature term is rendered differently within the same SearchZero screen group ("%@ gündeminde" vs "Arama trendleri"), creating terminology inconsistency.
- `Logins` — `tr/firefox-ios.xliff` — "Logins" (sync setting for saved logins/passwords) is translated as "Hesaplar" (Accounts).
    - Current: `Hesaplar`
    - Source: `Logins`
    - Suggest: `Hesap bilgileri`
    - The source refers to saved logins (usernames/passwords) synced, not user accounts; Firefox tr uses "Hesap bilgileri"/"Parolalar" for logins, while "Hesaplar" means Accounts and conflicts with the Firefox Account terminology.
- `Menu.RemovedFromShortcuts.v99` — `tr/firefox-ios.xliff` — "Shortcuts" is rendered "Kısayollar" here but "Kestirmeler" in the related toast on the same feature.
    - Current: `Kısayollardan kaldır`
    - Source: `Remove from Shortcuts`
    - Suggest: `Kestirmelerden kaldır`
    - Menu.RemovePin.Confirm2.v99 translates "Removed from Shortcuts" as "Kestirmelerden kaldırıldı"; the button and its confirmation toast must use the same term for Shortcuts.
- `Settings.SaveLogins.Title` — `tr/firefox-ios.xliff` — "Save Logins" translated as "Hesapları kaydet" (Save accounts) instead of the login/credential term.
    - Current: `Hesapları kaydet`
    - Source: `Save Logins`
    - Suggest: `Hesap bilgilerini kaydet`
    - "Logins" refers to saved credentials, not accounts; the established Firefox tr term is "hesap bilgileri" / "giriş bilgileri".
- `TodayWidget.QuickActionsGalleryTitleV2` — `tr/firefox-ios.xliff` — "Shortcuts" is translated as "Kestirmeleri" here while every other string in the same file uses "kısayol".
    - Current: `Firefox Kestirmeleri`
    - Source: `Firefox Shortcuts`
    - Suggest: `Firefox Kısayolları`
    - Terminology inconsistency within the same Today widget file, where Shortcut/shortcuts is consistently rendered "kısayol".
- `PzSrmZ-eHmH1H` — `tr/firefox-ios.xliff` — "Private Tabs" translated as "Özel Sekmeleri" instead of the term "Gizli sekmeler" used elsewhere for the same menu item.
    - Current: `‘Özel Sekmeleri Temizle’`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘Gizli Sekmeleri Temizle’`
    - The menu item eHmH1H and the matching label fi3W24-eHmH1H both use "Gizli sekmeleri temizle"; this confirmation label must reference the same wording.

### E. Typography, punctuation & spacing

- `CreditCard.EditCard.ViewCreditCardTitle.v116` — `tr/firefox-ios.xliff` — Inconsistent sentence casing: "Kartı Görüntüle" capitalizes the second word while all sibling strings in the same file use sentence case (e.g. "Kart ekle", "Kartı kaldır").
    - Current: `Kartı Görüntüle`
    - Source: `View Card`
    - Suggest: `Kartı görüntüle`
    - Turkish does not use title case; the rest of the EditCard strings consistently use sentence case.
- `FirefoxHome.Stories.Minutes.v140` — `tr/firefox-ios.xliff` — Stray period in abbreviated minutes label, inconsistent with FirefoxHome.Pocket.Minutes.v99 ("%d dk").
    - Current: `%d dk.`
    - Source: `min: %d`
    - Suggest: `%d dk`
    - The comment says minutes must be abbreviated due to space constraints; the parallel string uses "%d dk" without a period, so the trailing period is inconsistent typography.

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

### Fixed to date (0)

_Nothing fixed yet._
