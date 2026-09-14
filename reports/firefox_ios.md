# Firefox for iOS — l10n QA

- **Generated:** 2026-09-14
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 2,655 raised, 38 fixed (1%), 1,433 open
- **Closed by a person:** 21 dismissed, 52 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (60)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`cs`** `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "trusted for over 20 years" is rendered as "which you have trusted for over 20 years", asserting the user's trust rather than general trust.
    - Current: `Přináší nezisková organizace %@, které důvěřujete již více než 20 let`
    - Suggest: `Přináší nezisková organizace %@, které se důvěřuje již více než 20 let`
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
- **`de`** `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "trusted for over 20 years" is rendered as "der wir seit über 20 Jahren vertrauen" ("whom we have trusted for over 20 years"), reversing who trusts whom.
    - Current: `Von der gemeinnützigen Organisation %@, der wir seit über 20 Jahren vertrauen`
    - Suggest: `Von der gemeinnützigen Organisation %@, der seit über 20 Jahren vertraut wird`
- **`de`** `TabToolbar.Accessibility.DataClearance.v122` — `Shared/Supporting Files/en-US.lproj/TabToolbar.strings`
    - "Data Clearance" (deleting private session data) is translated as "Datenfreigabe", which means data sharing/release.
    - Current: `Datenfreigabe`
    - Suggest: `Datenlöschung`
- **`de`** `Settings.Studies.Toggle.Message` — `Shared/en-US.lproj/Localizable.strings`
    - "may install and run studies" (possibility) is rendered as "darf … installieren" (is permitted to), changing the meaning.
    - Current: `Firefox darf von Zeit zu Zeit Studien installieren und laufen lassen.`
    - Suggest: `Firefox kann von Zeit zu Zeit Studien installieren und ausführen.`
- **`es-AR`** `Settings.Rollouts.Message.v148` — `Shared/Supporting Files/en-US.lproj/Settings.strings`
    - Present/future "Changes applied remotely" rendered in past tense, asserting changes were already applied.
    - Current: `Los cambios se aplicaron remotamente.`
    - Suggest: `Los cambios se aplican remotamente.`
- **`es-ES`** `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "for everyone" is rendered as "para los usuarios en todo el mundo" (for users all over the world), adding a claim not in the source.
    - Current: `para los usuarios en todo el mundo`
    - Suggest: `para todos`
- **`es-ES`** `Menu.TrackingProtectionDescription.ContentTrackers` — `Shared/en-US.lproj/Localizable.strings`
    - "can make websites load faster" rendered as a certainty ("hará que").
    - Current: `Bloquearlos hará que los sitios web carguen más rápido`
    - Suggest: `Bloquearlos puede hacer que los sitios web carguen más rápido`
- **`es-ES`** `Menu.TrackingProtectionDescription.SocialNetworksNew` — `Shared/en-US.lproj/Localizable.strings`
    - The Spanish reverses the relationship (social networks place trackers ON other websites) and overstates the effect of blocking.
    - Current: `Las redes sociales colocan rastreadores para que otros sitios web construyan un perfil más completo dirigido a ti. Si bloqueas estos rastreadores, muchas empresas de medios sociales dejarán de tener…`
    - Suggest: `Las redes sociales colocan rastreadores en otros sitios web para crear un perfil tuyo más completo y segmentado. Bloquear estos rastreadores reduce lo que las empresas de redes sociales pueden ver de…`
- **`es-MX`** `FirefoxHomepage.TrackerBlocker.NoTrackersBlocked.v153` — `Shared/Supporting Files/en-US.lproj/FirefoxHomepage.strings`
    - "You’re Protected" is translated as "Protección de navegación activada" (Browsing protection enabled), which states something different from the source.
    - Current: `Protección de navegación activada`
    - Suggest: `Estás protegido`
- **`es-MX`** `MainMenu.HeaderBanner.Subtitle.v142` — `Shared/Supporting Files/en-US.lproj/MainMenu.strings`
    - Subtitle adds content not in the source and changes "Takes seconds" to "takes only a second" plus invented "change your preferences".
    - Current: `Toma solo un segundo y puedes cambiar tus preferencias cuando quieras.`
    - Suggest: `Toma solo unos segundos. Cámbialo cuando quieras.`
- **`es-MX`** `Onboarding.Modern.BrandRefresh.Welcome.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - Relative clause with subjunctive changes the meaning from blocking all companies from spying to only blocking those that do spy.
    - Current: `bloqueamos automáticamente a las empresas que espíen tus clics`
    - Suggest: `bloqueamos automáticamente que las empresas espíen tus clics`
- **`es-MX`** `TermsOfUse.Description.v142` — `Shared/Supporting Files/en-US.lproj/TermsOfUse.strings`
    - "We've introduced a %@ Terms of Use" is rendered as "we have updated" the Terms of Use, changing new terms into updated terms.
    - Current: `Hemos actualizado los Términos de uso de %@ y nuestro Aviso de privacidad.`
    - Suggest: `Presentamos los Términos de uso de %@ y actualizamos nuestro Aviso de privacidad.`
- **`es-MX`** `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en-US.lproj/PrivateBrowsing.strings`
    - The translation adds "de esta sesión" and drops "any of your", altering the scope of what Firefox will not remember.
    - Current: `Firefox no recordará el historial ni las cookies de esta sesión, pero guardará marcadores que agregues.`
    - Suggest: `Firefox no recordará nada de tu historial ni tus cookies, pero se guardarán los marcadores nuevos.`
- **`fr`** `Addresses.EditAddress.AutofillAddressZip.v129` — `Shared/Supporting Files/en-US.lproj/EditAddress.strings`
    - "ZIP Code" is translated with an added parenthetical "(États-Unis)" that the source does not contain.
    - Current: `Code postal (États-Unis)`
    - Suggest: `Code postal`
- **`hi-IN`** `NSMicrophoneUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
- **`hi-IN`** `Oops! Firefox crashed` — `Shared/en-US.lproj/Localizable.strings`
    - "crashed" is rendered as "नष्ट हो गया" (was destroyed), which is not the software sense of crashing.
    - Current: `उफ़! Firefox नष्ट हो गया`
    - Suggest: `उफ़! Firefox क्रैश हो गया`
- **`hu`** `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
- **`hu`** `Menu.TrackingProtectionDescription.Fingerprinters` — `Shared/en-US.lproj/Localizable.strings`
    - "can be used to track you" rendered as a definite statement "használnak" (they use it), dropping the modality.
    - Current: `amelyet aztán a böngészése követésére használnak`
    - Suggest: `amely aztán a böngészése követésére használható`
- **`id`** `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `Shared/Supporting Files/en-US.lproj/Onboarding.strings`
    - "won't sell you out" (won't betray you) is rendered literally as "tidak akan menjual Anda" (won't sell you), changing the meaning.
    - Current: `tidak akan menjual Anda`
    - Suggest: `tidak akan mengkhianati Anda`
- **`id`** `Search.ThirdPartyEngines.DuplicateErrorMessage` — `Shared/en-US.lproj/Localizable.strings`
    - Error message translated as a success ("has been successfully added") instead of stating the engine was already added.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
- **`id`** `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `Shared/en-US.lproj/PrivateBrowsing.strings`
    - "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
- **`it`** `BreachAlerts.Description` — `Shared/en-US.lproj/Localizable.strings`
    - "leaked or stolen" is rendered as "rubate o diffuse pubblicamente" ("publicly disclosed"), and the source's "Passwords were leaked" is turned into a claim about this specific website's passwords.
    - Current: `le password di questo sito web sono state rubate o diffuse pubblicamente`
    - Suggest: `alcune password sono state diffuse o rubate`
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
- _…and 30 more, in the per-locale reports linked below._

### Broken output — impact 1 (1)

The value does not render as intended: a blank string, broken markup, a variable the source never passes.

`de` 1

- **`de`** `TranslationToastHandler.PromptTranslate.Title` — `Shared/en-US.lproj/Localizable.strings`
    - Reordered numbered placeholders are fine, but %1$@ preceded by "auf" should agree; main issue is the swapped order of %3$@ and %2$@ relative to the source sentence structure.
    - Current: `Mit %3$@ auf %2$@ übersetzen?`
    - Suggest: `Mit %3$@ in %2$@ übersetzen?`

### Wrong content — impact 2 (710)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **94** | 54 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **90** | 28 | 2 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,911 | 11 | **2** | 0 | 16 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **8** | 4 | 3 | 0 | 50 |
| [es-AR](es-AR/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **100** | 44 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **64** | 34 | 0 | 0 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,883 | 39 | **126** | 68 | 1 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **45** | 30 | 0 | 0 | 0 |
| [hi-IN](hi-IN/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 602 | 1,320 | **79** | 33 | 0 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **94** | 40 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **97** | 37 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **8** | 6 | 16 | 21 | 2 |
| [ja](ja/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **113** | 63 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,918 | 4 | **49** | 22 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **72** | 40 | 0 | 0 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **57** | 35 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **89** | 42 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,919 | 3 | **91** | 42 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **85** | 47 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-09-14 | incremental | `e8592a89` | 1,922 | 0 | **70** | 42 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.
