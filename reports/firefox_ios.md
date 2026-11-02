# Firefox for iOS — l10n QA

- **Generated:** 2026-11-02
- **Locales tracked:** 34 (34 with recorded state)
- **Findings:** 3,822 raised, 221 fixed (5%), 2,309 open
- **Closed by a person:** 37 dismissed, 52 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (21)

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
- **`de`** `TabToolbar.Accessibility.DataClearance.v122` — `Shared/Supporting Files/en-US.lproj/TabToolbar.strings`
    - "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Suggest: `Datenlöschung`
- **`el`** `This action will clear all of your private data, including history from your synced devices.` — `Shared/en-US.lproj/ClearHistoryConfirm.strings`
    - Because of how the sentence is built, the Greek says all private data (and history) is deleted from synced devices, not local private data plus history from synced devices.
    - Current: `Αυτή η ενέργεια θα διαγράψει όλα τα ιδιωτικά σας δεδομένα, καθώς και το ιστορικό, από τις συγχρονισμένες συσκευές σας.`
    - Suggest: `Αυτή η ενέργεια θα διαγράψει όλα τα ιδιωτικά σας δεδομένα, συμπεριλαμβανομένου του ιστορικού από τις συγχρονισμένες συσκευές σας.`
- **`es-ES`** `Menu.TrackingProtectionDescription.SocialNetworksNew` — `Shared/en-US.lproj/Localizable.strings`
    - The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener…`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de…`
- **`fi`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" is rendered as "how you use it", widening the data shared with marketing partners.
    - Current: `ja kuinka käytät sitä`
    - Suggest: `ja että käytät sitä`
- **`hu`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
- **`id`** `QuickAnswers.PrivacyBanner.Description.v158` — `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`
    - The negation only applies to the first item, so the translation states that the app does use data to train AI models and uses the voice to identify the user.
    - Current: `%@ tidak menyimpan audio atau pertanyaan Anda, menggunakan data Anda untuk melatih model AI, atau menggunakan suara Anda untuk mengidentifikasi Anda.`
    - Suggest: `%@ tidak menyimpan audio atau pertanyaan Anda, tidak menggunakan data Anda untuk melatih model AI, dan tidak menggunakan suara Anda untuk mengidentifikasi Anda.`
- **`id`** `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en-US.lproj/PrivateBrowsing.strings`
    - "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
- **`ja`** `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `Shared/Supporting Files/en-US.lproj/FirefoxHomepage.strings`
    - "Leave no traces on this device" is rendered as "We won't let this device be tracked", which asserts something different from the source.
    - Current: `この端末を追跡させません`
    - Suggest: `この端末に痕跡を残しません`
- **`ja`** `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "interaction data" rendered as 「対話データ」 (dialogue/conversation data) instead of 利用状況データ/インタラクションデータ.
    - Current: `診断情報と対話データ`
    - Suggest: `診断データとインタラクションデータ`
- **`ko`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "and that you use it" is translated as "and how you use it", which claims usage behaviour is shared with marketing partners.
    - Current: `%1$@를 발견한 방법과 사용 방법을 공유하세요`
    - Suggest: `%1$@를 발견한 방법과 %1$@를 사용한다는 사실을 공유하세요`
- **`pt-PT`** `Keyboard.Shortcuts.ClearRecentHistory` — `Shared/en-US.lproj/Localizable.strings`
    - "Recent" is dropped, so the label says it clears the whole history.
    - Current: `Limpar histórico`
    - Suggest: `Limpar histórico recente`
- **`sk`** `NSMicrophoneUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - The translation leaves out that Firefox uploads the recorded audio; it only mentions recording.
    - Current: `na nahrávanie zvuku`
    - Suggest: `na nahrávanie a nahrávanie zvuku na server`
- **`th`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "and that you use it" is rendered as "and how you use it", which says more data is shared with marketing partners than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ %2$@`
    - Suggest: `และการที่คุณใช้งานอยู่ ให้กับพันธมิตรด้านการตลาดของ %2$@`
- **`tr`** `Settings.SendUsage.Message` — `Shared/en-US.lproj/Localizable.strings`
    - Turkish drops "to provide" and "for everyone", and uses "daha da geliştirmek" (improve further) only.
    - Current: `Mozilla, yalnızca Firefox’u daha da geliştirmek için ihtiyaç duyduğumuz verileri toplar.`
    - Suggest: `Mozilla, Firefox’u herkese sunmak ve geliştirmek için yalnızca ihtiyaç duyduğumuz verileri toplamaya çalışır.`
- **`vi`** `Settings.Home.Option.ThoughtProvokingStories.v116` — `Shared/Supporting Files/en-US.lproj/CustomizeFirefoxHome.strings`
    - "Thought-Provoking" is rendered as "kích động tư tưởng", which means inciting or agitating ideology.
    - Current: `Những câu chuyện kích động tư tưởng`
    - Suggest: `Những câu chuyện gợi suy ngẫm`
- **`vi`** `Upgrade.Welcome.Description.v114` — `Shared/Supporting Files/en-US.lproj/Upgrade.strings`
    - "people over profits" is rendered as "commitment to people for profit", reversing the mission statement.
    - Current: `Cùng cam kết với mọi người vì lợi nhuận.`
    - Suggest: `Vẫn cam kết đặt con người lên trên lợi nhuận.`
- **`vi`** `Settings.SendUsage.Message` — `Shared/en-US.lproj/Localizable.strings`
    - "strives to" is dropped, turning an aspiration into a flat claim that Mozilla only collects what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần`
- **`zh-TW`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "and that you use it" is rendered as "and how you use it", so the text describes more data being shared than the source says.
    - Current: `以及是如何使用的`
    - Suggest: `以及您正在使用它的事實`

### Broken output — impact 1 (1)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`de` 1

- **`de`** `TranslationToastHandler.PromptTranslate.Title` — `Shared/en-US.lproj/Localizable.strings`
    - Reordered numbered placeholders are fine, but %1$@ preceded by "auf" should agree; main issue is the swapped order of %3$@ and %2$@ relative to the source sentence structure.
    - Current: `Mit %3$@ auf %2$@ übersetzen?`
    - Suggest: `Mit %3$@ in %2$@ übersetzen?`

### Wrong content — impact 2 (1060)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [ar](ar/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,245 | 728 | **51** | 12 | 0 | 0 | 0 |
| [cs](cs/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **91** | 53 | 2 | 1 | 0 |
| [da](da/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,915 | 58 | **35** | 7 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **87** | 30 | 2 | 0 | 0 |
| [el](el/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **47** | 7 | 1 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **2** | 0 | 16 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **9** | 4 | 3 | 0 | 50 |
| [es-AR](es-AR/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **96** | 41 | 4 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,848 | 125 | **57** | 31 | 0 | 1 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,896 | 77 | **125** | 65 | 1 | 0 | 0 |
| [fa](fa/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,915 | 58 | **406** | 207 | 66 | 0 | 0 |
| [fi](fi/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **41** | 18 | 0 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **26** | 19 | 20 | 7 | 0 |
| [hi-IN](hi-IN/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,876 | 97 | **15** | 12 | 79 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **89** | 37 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **93** | 34 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **0** | 0 | 20 | 22 | 2 |
| [ja](ja/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **108** | 59 | 0 | 0 | 0 |
| [ko](ko/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **96** | 44 | 0 | 0 | 0 |
| [nb-NO](nb-NO/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **31** | 5 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **52** | 22 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **61** | 36 | 2 | 4 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **50** | 32 | 3 | 2 | 0 |
| [pt-PT](pt-PT/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **66** | 17 | 0 | 0 | 0 |
| [ro](ro/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **42** | 22 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **88** | 38 | 1 | 0 | 0 |
| [sk](sk/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **36** | 14 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,896 | 77 | **79** | 34 | 0 | 0 | 0 |
| [sv-SE](sv-SE/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **49** | 17 | 0 | 0 | 0 |
| [th](th/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,885 | 88 | **36** | 18 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **82** | 44 | 0 | 0 | 0 |
| [vi](vi/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,927 | 46 | **68** | 32 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,909 | 64 | **62** | 35 | 1 | 0 | 0 |
| [zh-TW](zh-TW/firefox_ios.md) | 2026-11-02 | incremental | `14a6f5ae` | 1,973 | 0 | **33** | 15 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
