# Firefox for iOS — l10n QA

- **Generated:** 2026-09-17
- **Locales tracked:** 21 (21 with recorded state)
- **Findings:** 2,724 raised, 38 fixed (1%), 1,502 open
- **Closed by a person:** 21 dismissed, 52 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (40)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`cs`** `This action will clear all of your private data, including history from your synced devices.` — `Shared/en-US.lproj/ClearHistoryConfirm.strings`
    - "all of your private data" is rendered as "všechna vaše data", dropping "private"/soukromá.
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
- **`cs`** `Settings.SendUsage.Message` — `Shared/en-US.lproj/Localizable.strings`
    - Translation drops "only collect what we need to provide" and "for everyone", asserting a different claim about data collection.
    - Current: `Mozilla sbírá jenom informace potřebné pro vylepšování Firefoxu.`
    - Suggest: `Mozilla se snaží sbírat jen data, která potřebuje k poskytování a vylepšování Firefoxu pro všechny.`
- **`cs`** `Settings.TrackingProtection.ProtectionCellFooter` — `Shared/en-US.lproj/Localizable.strings`
    - "helps stop advertisers from tracking" rendered as the absolute "zabrání inzerentům sledovat" (will prevent advertisers from tracking).
    - Current: `zabrání inzerentům sledovat vás na internetu`
    - Suggest: `pomáhá zabránit inzerentům ve sledování vašeho prohlížení`
- **`de`** `TabToolbar.Accessibility.DataClearance.v122` — `Shared/Supporting Files/en-US.lproj/TabToolbar.strings`
    - "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Suggest: `Datenlöschung`
- **`es-AR`** `Settings.Rollouts.Message.v148` — `Shared/Supporting Files/en-US.lproj/Settings.strings`
    - Present/future "Changes applied remotely" rendered in past tense, asserting changes were already applied.
    - Current: `Los cambios se aplicaron remotamente.`
    - Suggest: `Los cambios se aplican remotamente.`
- **`es-ES`** `Menu.TrackingProtectionDescription.ContentTrackers` — `Shared/en-US.lproj/Localizable.strings`
    - "can make websites load faster" rendered as a certainty ("hará que").
    - Current: `Bloquearlos hará que los sitios web carguen más rápido`
    - Suggest: `Bloquearlos puede hacer que los sitios web carguen más rápido`
- **`es-ES`** `Menu.TrackingProtectionDescription.SocialNetworksNew` — `Shared/en-US.lproj/Localizable.strings`
    - The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener…`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de…`
- **`fa`** `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `Shared/en-US.lproj/Localizable.strings`
    - "tapping" rendered as "tapping and holding", and "book plus icon" loses the plus.
    - Current: `با تپ کردن و نگه داشتن آیکون کتاب`
    - Suggest: `با تپ کردن آیکون کتاب به‌همراه علامت مثبت`
- **`fa`** `Settings.Disconnect.Body` — `Shared/en-US.lproj/Localizable.strings`
    - The qualifier "browsing data" is rendered as just "any data", widening the claim about what is not deleted.
    - Current: `هیچ گونه اطلاعاتی از روی دستگاه شما پاک نخواهد کرد`
    - Suggest: `هیچ‌گونه اطلاعات مرور شما را از روی این دستگاه پاک نخواهد کرد`
- **`fa`** `Settings.SendUsage.Message` — `Shared/en-US.lproj/Localizable.strings`
    - The translation drops "strives to" and "provide", asserting Mozilla only collects data that helps improve Firefox.
    - Current: `موزیلا تنها اطلاعاتی که به بهینه‌سازی فایرفاکس برای همه کمک می‌کند را جمع‌آوری می‌کند.`
    - Suggest: `موزیلا تلاش می‌کند تنها اطلاعاتی را جمع‌آوری کند که برای ارائه و بهبود فایرفاکس برای همه لازم است.`
- **`fa`** `Settings.WebsiteData.ConfirmPrompt` — `Shared/en-US.lproj/Localizable.strings`
    - "will clear" weakened to "can clear" (می‌تواند حذف کند).
    - Current: `این اقدام می تواند تمام اطلاعات پایگاه اینترنتی را حذف کند`
    - Suggest: `این اقدام تمام اطلاعات پایگاه اینترنتی را حذف می‌کند`
- **`fa`** `Well, this is embarrassing.` — `Shared/en-US.lproj/Localizable.strings`
    - "this is embarrassing" is rendered as "we are very sorry", an apology the source does not make.
    - Current: `راستش، بسیار متاسفیم.`
    - Suggest: `خب، این شرم‌آور است.`
- **`fa`** `Logins will be permanently removed.` — `Shared/en-US.lproj/LoginManager.strings`
    - Future-tense warning rendered as past tense, telling the user the deletion already happened.
    - Current: `ورود‌ها برای همیشه حذف شد.`
    - Suggest: `ورودها برای همیشه حذف خواهند شد.`
- **`fa`** `Logins will be removed from all connected devices.` — `Shared/en-US.lproj/LoginManager.strings`
    - Future tense rendered as past tense and "connected devices" reduced to "all devices".
    - Current: `ورود‌ها بر روی تمامی دستگاه‌ها حذف شد.`
    - Suggest: `ورودها از همه دستگاه‌های متصل حذف خواهند شد.`
- **`hi-IN`** `NSMicrophoneUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
- **`hu`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
- **`hu`** `Menu.TrackingProtectionDescription.Fingerprinters` — `Shared/en-US.lproj/Localizable.strings`
    - "can be used to track you" rendered as a definite statement "használnak" (they use it), dropping the modality.
    - Current: `amelyet aztán a böngészése követésére használnak`
    - Suggest: `amely aztán a böngészése követésére használható`
- **`id`** `Search.ThirdPartyEngines.DuplicateErrorMessage` — `Shared/en-US.lproj/Localizable.strings`
    - Error message translated as a success ("has been successfully added") instead of stating the engine was already added.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
- **`id`** `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en-US.lproj/PrivateBrowsing.strings`
    - "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
- **`ja`** `NSFaceIDUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - "payment methods" is rendered as 「暗号化されたカード情報」 (encrypted card information), adding a claim not in the source.
    - Current: `保存されたログイン情報と暗号化されたカード情報にアクセスするには Face ID が必要です。`
    - Suggest: `保存されたパスワードと支払い方法にアクセスするには Firefox は Face ID を必要とします。`
- **`ja`** `NSLocationWhenInUseUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - "may request your location" is rendered as a present-tense assertion that visited sites are requesting your location.
    - Current: `訪れたウェブサイトがあなたの位置情報を要求しています。`
    - Suggest: `訪れたウェブサイトがあなたの位置情報を要求することがあります。`
- **`ja`** `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `Shared/Supporting Files/en-US.lproj/FirefoxHomepage.strings`
    - "Leave no traces on this device" is rendered as "We won't let this device be tracked", which asserts something different from the source.
    - Current: `この端末を追跡させません`
    - Suggest: `この端末に痕跡を残しません`
- **`ja`** `Onboarding.Customization.Intro.Title.v123` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - Title translated as "privacy protection" instead of "puts you in control".
    - Current: `%@ でプライバシー保護`
    - Suggest: `%@ なら思いのまま`
- **`ja`** `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "interaction data" rendered as 「対話データ」 (dialogue/conversation data) instead of 利用状況データ/インタラクションデータ.
    - Current: `診断情報と対話データ`
    - Suggest: `診断データとインタラクションデータ`
- **`ja`** `WebCompatReporter.Preview.Data.PageLanguages.v155` — `Shared/Supporting Files/en-US.lproj/WebCompatReporter.strings`
    - A bullet-point noun phrase is rendered as a past-tense sentence, changing the meaning.
    - Current: `言語設定がこのページに送信されました`
    - Suggest: `このページに送信された言語設定`
- **`ja`** `Settings.TrackingProtection.ProtectionCellFooter` — `Shared/en-US.lproj/Localizable.strings`
    - "helps stop advertisers from tracking your browsing" is rendered as an absolute claim of blocking tracking ads.
    - Current: `ユーザーの行動を追跡する広告を阻止します`
    - Suggest: `広告会社によるユーザーの閲覧の追跡を防ぐのに役立ちます`
- **`pl`** `Settings.Studies.Title.v148` — `Shared/Supporting Files/en-US.lproj/Settings.strings`
    - "Allow Feature Studies" is rendered as "Zezwól na badanie korzystania z funkcji", which says the app studies how the user uses features rather than allowing feature studies (experiments).
    - Current: `Zezwól na badanie korzystania z funkcji`
    - Suggest: `Zezwól na badania funkcji`
- **`pl`** `Search.ThirdPartyEngines.AddMessage` — `Shared/en-US.lproj/Localizable.strings`
    - Translation adds a claim about managing the engine in settings that the source does not contain.
    - Current: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania i będzie można nią zarządzać poprzez ustawienia.`
    - Suggest: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania.`
- **`pt-BR`** `Settings.Rollouts.Message.v148` — `Shared/Supporting Files/en-US.lproj/Settings.strings`
    - "between updates" was rendered as "a cada atualização" (with each update), reversing the meaning.
    - Current: `melhora funcionalidades, desempenho e estabilidade a cada atualização`
    - Suggest: `melhora funcionalidades, desempenho e estabilidade entre atualizações`
- **`pt-BR`** `Block Pop-up Windows` — `Shared/en-US.lproj/Localizable.strings`
    - Translation adds "ou abas" (or tabs), which the source does not say.
    - Current: `Bloquear abertura de janelas ou abas`
    - Suggest: `Bloquear janelas pop-up`
- _…and 10 more, in the per-locale reports linked below._

### Broken output — impact 1 (1)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`de` 1

- **`de`** `TranslationToastHandler.PromptTranslate.Title` — `Shared/en-US.lproj/Localizable.strings`
    - Reordered numbered placeholders are fine, but %1$@ preceded by "auf" should agree; main issue is the swapped order of %3$@ and %2$@ relative to the source sentence structure.
    - Current: `Mit %3$@ auf %2$@ übersetzen?`
    - Suggest: `Mit %3$@ in %2$@ übersetzen?`

### Wrong content — impact 2 (732)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **93** | 53 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **88** | 26 | 2 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,911 | 11 | **2** | 0 | 16 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **8** | 4 | 3 | 0 | 50 |
| [es-AR](es-AR/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **100** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **63** | 33 | 0 | 0 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,883 | 39 | **122** | 64 | 1 | 0 | 0 |
| [fa](fa/firefox_ios.md) | 2026-09-17 | baseline | `8f5aca68` | 546 | 1,376 | **88** | 41 | 0 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **44** | 29 | 0 | 0 | 0 |
| [hi-IN](hi-IN/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 602 | 1,320 | **79** | 33 | 0 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **94** | 40 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **97** | 37 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **7** | 5 | 16 | 21 | 2 |
| [ja](ja/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **110** | 60 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,918 | 4 | **49** | 22 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **71** | 39 | 0 | 0 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **57** | 35 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **89** | 42 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,919 | 3 | **89** | 40 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **83** | 45 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-09-14 | checks-only | `8f5aca68` | 1,922 | 0 | **69** | 41 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

**Not reviewed yet:** `cs`, `de`, `es-ES`, `es-MX`, `fr`, `hi-IN`, `id`, `it`, `ja`, `nl`, `pl`, `sl`, `tr`, `zh-CN`. They have only been through the deterministic checks; the reviewer has not read them. The next run does the baseline.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
