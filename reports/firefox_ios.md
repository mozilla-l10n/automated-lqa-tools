# Firefox for iOS — l10n QA

- **Generated:** 2026-10-19
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,836 raised, 203 fixed (5%), 2,349 open
- **Closed by a person:** 29 dismissed, 52 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (66)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`ar`** `This action will clear all of your private data, including history from your synced devices.` — `Shared/en-US.lproj/ClearHistoryConfirm.strings`
    - Translation says all private data is erased from synced devices, whereas the source says all private data is cleared, including history from synced devices.
    - Current: `سيمحي هذا الإجراء كل بياناتك الخاصة من الأجهزة المتزامنة، بما في ذلك التأريخ.`
    - Suggest: `سيمحي هذا الإجراء كل بياناتك الخاصة، بما في ذلك التأريخ من أجهزتك المتزامنة.`
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
- **`da`** `Onboarding.Welcome.Description.TreatementA.v120` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
- **`da`** `Onboarding.Welcome.Description.v120` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "helps stop" is rendered as "forhindrer" (prevents), turning a hedged claim into a guarantee.
    - Current: `forhindrer virksomheder i at følge dig`
    - Suggest: `hjælper med at forhindre virksomheder i at følge dig`
- **`da`** `CoverSheet.v24.ETP.Description` — `Shared/en-US.lproj/Localizable.strings`
    - The hedge "helps stop" has become "forhindrer" (prevents), so the text now says tracking protection fully stops ads from following the user.
    - Current: `forhindrer reklamer i at følge dig`
    - Suggest: `hjælper med at forhindre reklamer i at følge dig`
- **`de`** `TabToolbar.Accessibility.DataClearance.v122` — `Shared/Supporting Files/en-US.lproj/TabToolbar.strings`
    - "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Suggest: `Datenlöschung`
- **`el`** `Onboarding.Welcome.Description.TreatementA.v120` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "helps stop" is rendered as "stops", which turns a modest claim into an absolute promise.
    - Current: `σταματά τις εταιρείες από το να σας ακολουθούν`
    - Suggest: `βοηθά να σταματήσουν οι εταιρείες να σας ακολουθούν`
- **`el`** `Onboarding.Welcome.Description.v120` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "helps stop" is rendered as "stops", which turns a modest claim into an absolute promise.
    - Current: `σταματά τις εταιρείες από το να σας ακολουθούν`
    - Suggest: `βοηθά να σταματήσουν οι εταιρείες να σας ακολουθούν`
- **`el`** `This action will clear all of your private data, including history from your synced devices.` — `Shared/en-US.lproj/ClearHistoryConfirm.strings`
    - Because of how the sentence is built, the Greek says all private data (and history) is deleted from synced devices, not local private data plus history from synced devices.
    - Current: `Αυτή η ενέργεια θα διαγράψει όλα τα ιδιωτικά σας δεδομένα, καθώς και το ιστορικό, από τις συγχρονισμένες συσκευές σας.`
    - Suggest: `Αυτή η ενέργεια θα διαγράψει όλα τα ιδιωτικά σας δεδομένα, συμπεριλαμβανομένου του ιστορικού από τις συγχρονισμένες συσκευές σας.`
- **`el`** `CoverSheet.v24.ETP.Description` — `Shared/en-US.lproj/Localizable.strings`
    - The hedge "helps stop" is dropped, so the Greek claims outright that ETP stops ads from tracking the user.
    - Current: `εμποδίζει την καταγραφή σας από διαφημίσεις`
    - Suggest: `βοηθά στην αποτροπή της καταγραφής σας από διαφημίσεις`
- **`el`** `Settings.TrackingProtection.ProtectionCellFooter` — `Shared/en-US.lproj/Localizable.strings`
    - The Greek drops the hedge 'helps' and says the feature stops advertisers from tracking you outright.
    - Current: `εμποδίζει την καταγραφή της περιήγησής σας από διαφημιστές`
    - Suggest: `βοηθά στην αποτροπή της καταγραφής της περιήγησής σας από διαφημιστές`
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
- **`fa`** `Well, this is embarrassing.` — `Shared/en-US.lproj/Localizable.strings`
    - "this is embarrassing" is rendered as "we are very sorry", an apology the source does not make.
    - Current: `راستش، بسیار متاسفیم.`
    - Suggest: `خب، این شرم‌آور است.`
- **`fi`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" is rendered as "how you use it", widening the data shared with marketing partners.
    - Current: `ja kuinka käytät sitä`
    - Suggest: `ja että käytät sitä`
- **`fi`** `CoverSheet.v24.ETP.Description` — `Shared/en-US.lproj/Localizable.strings`
    - The hedge "helps stop" is rendered as an unqualified "stops", so the Finnish promises full prevention of ad tracking.
    - Current: `estää mainoksia seuraamasta sinua`
    - Suggest: `auttaa estämään mainoksia seuraamasta sinua`
- **`hu`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
- **`hu`** `Menu.TrackingProtectionDescription.Fingerprinters` — `Shared/en-US.lproj/Localizable.strings`
    - "can be used to track you" rendered as a definite statement "használnak" (they use it), dropping the modality.
    - Current: `amelyet aztán a böngészése követésére használnak`
    - Suggest: `amely aztán a böngészése követésére használható`
- **`id`** `QuickAnswers.PrivacyBanner.Description.v158` — `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`
    - The negation only applies to the first item, so the translation states that the app does use data to train AI models and uses the voice to identify the user.
    - Current: `%@ tidak menyimpan audio atau pertanyaan Anda, menggunakan data Anda untuk melatih model AI, atau menggunakan suara Anda untuk mengidentifikasi Anda.`
    - Suggest: `%@ tidak menyimpan audio atau pertanyaan Anda, tidak menggunakan data Anda untuk melatih model AI, dan tidak menggunakan suara Anda untuk mengidentifikasi Anda.`
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
- **`ja`** `QuickAnswers.OptInRedesign.NoTrainingDescription.v158` — `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`
    - "our systems" narrowed to "our AI systems".
    - Current: `私たちの AI システムの学習`
    - Suggest: `私たちのシステムの学習`
- _…and 36 more, in the per-locale reports linked below._

### Broken output — impact 1 (1)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`de` 1

- **`de`** `TranslationToastHandler.PromptTranslate.Title` — `Shared/en-US.lproj/Localizable.strings`
    - Reordered numbered placeholders are fine, but %1$@ preceded by "auf" should agree; main issue is the swapped order of %3$@ and %2$@ relative to the source sentence structure.
    - Current: `Mit %3$@ auf %2$@ übersetzen?`
    - Suggest: `Mit %3$@ in %2$@ übersetzen?`

### Wrong content — impact 2 (1099)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,175 | 752 | **51** | 12 | 0 | 0 | 0 |
| [cs](cs/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,918 | 9 | **91** | 53 | 2 | 1 | 0 |
| [da](da/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,847 | 80 | **33** | 8 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **87** | 30 | 2 | 0 | 0 |
| [el](el/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,922 | 5 | **51** | 10 | 0 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,837 | 90 | **2** | 0 | 16 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **9** | 4 | 3 | 0 | 50 |
| [es-AR](es-AR/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **97** | 42 | 4 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,848 | 79 | **58** | 32 | 0 | 1 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,896 | 31 | **125** | 65 | 1 | 0 | 0 |
| [fa](fa/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,915 | 12 | **407** | 208 | 66 | 0 | 0 |
| [fi](fi/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,907 | 20 | **41** | 19 | 0 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **48** | 29 | 2 | 0 | 0 |
| [hi-IN](hi-IN/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,876 | 51 | **16** | 13 | 79 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,915 | 12 | **90** | 38 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **93** | 34 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **2** | 1 | 21 | 21 | 2 |
| [ja](ja/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,915 | 12 | **112** | 63 | 0 | 0 | 0 |
| [ko](ko/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **95** | 44 | 0 | 0 | 0 |
| [nb-NO](nb-NO/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,915 | 12 | **34** | 8 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,918 | 9 | **51** | 22 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,915 | 12 | **62** | 37 | 2 | 4 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **51** | 33 | 3 | 2 | 0 |
| [pt-PT](pt-PT/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **65** | 17 | 0 | 0 | 0 |
| [ro](ro/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **40** | 21 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **86** | 39 | 1 | 0 | 0 |
| [sk](sk/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **36** | 15 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,872 | 55 | **82** | 36 | 0 | 0 | 0 |
| [sv-SE](sv-SE/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **49** | 17 | 0 | 0 | 0 |
| [th](th/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,885 | 42 | **37** | 19 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **83** | 44 | 0 | 0 | 0 |
| [vi](vi/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **68** | 32 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,909 | 18 | **67** | 40 | 1 | 0 | 0 |
| [zh-TW](zh-TW/firefox_ios.md) | 2026-10-19 | incremental | `ec61063c` | 1,927 | 0 | **30** | 15 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
