# Firefox l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `e44f1369fb6d` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `8ffd279d75ec` |
| **Previous run** | 2026-09-07 @ `3c0c507b8d42` |
| **Mode** | incremental |
| **Strings reviewed this run** | 116 of 16,144 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for tr: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (31)

- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Yenilikler” but the string it names, `releaseNotes-link`, reads “Yeni neler var?”
    - Current: `Güncelleme sonrası “Yenilikler” sayfasını değiştir. Güncelleme sonrası sayfasını devre dışı bırakmak istiyorsanız bu ilkeyi boş olarak ayarlayabilirsiniz.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Yeni neler var?`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `MediaEMENoCodecsDeprecatedWarning` — `dom/chrome/dom/dom.properties` — `MediaEMENoCodecsDeprecatedWarning` uses straight double quotes
    - Current: `contentType olmadan "codecs" ifadesine sahip audioCapabilities ve videoCapabilities içeren MediaKeySystemConfiguration adayını aktarmadan navigator.requestMediaKeySystemAccess() çağrısı gerçekleştirmek (%S adresinde) ar…`
    - Source: `Calling navigator.requestMediaKeySystemAccess() (at %S) passing a candidate MediaKeySystemConfiguration containing audioCapabilities or videoCapabilities without a contentType with a “codecs” string is deprecated and wi…`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `BlockAutoplayWebAudioStartError` — `dom/chrome/dom/dom.properties` — `BlockAutoplayWebAudioStartError` uses a straight apostrophe
    - Current: `Bir AudioContext'in otomatik başlaması engellendi. AudioContext, sayfadaki bir kullanıcı hareketinden sonra oluşturulmalı veya devam ettirilmelidir.`
    - Source: `An AudioContext was prevented from starting automatically. It must be created or resumed after a user gesture on the page.`
    - The tree uses ’ 861 times against 46 straight.
- `LenientThisWarning` — `dom/chrome/dom/dom.properties` — `LenientThisWarning` uses a straight apostrophe
    - Current: `“this” nesnesi yanlış olduğundan [LenientThis] içeren özelliğin get veya set'i yok sayılıyor.`
    - Source: `Ignoring get or set of property that has [LenientThis] because the “this” object is incorrect.`
    - The tree uses ’ 861 times against 46 straight.
- `NavigatorGetUserMediaWarning` — `dom/chrome/dom/dom.properties` — `NavigatorGetUserMediaWarning` uses a straight apostrophe
    - Current: `navigator.mozGetUserMedia'nın yerini navigator.mediaDevices.getUserMedia almıştır`
    - Source: `navigator.mozGetUserMedia has been replaced by navigator.mediaDevices.getUserMedia`
    - The tree uses ’ 861 times against 46 straight.
- `InterceptedErrorResponseWithURL` — `dom/chrome/dom/dom.properties` — `InterceptedErrorResponseWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, FetchEvent.respondWith()'e bir Error Response aktardı. Bu genellikle ServiceWorker'ın geçersiz bir fetch() çağrısı yaptığını gösterir.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed an Error Response to FetchEvent.respondWith(). This typically means the ServiceWorker performed an invalid fetch() call.`
    - The tree uses ’ 861 times against 46 straight.
- `InterceptedUsedResponseWithURL` — `dom/chrome/dom/dom.properties` — `InterceptedUsedResponseWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, FetchEvent.respondWith()'e kullanılmış bir Response aktardı. Bir Response'un gövdesi yalnızca bir kez okunabilir. Gövdeye birden fazla kez ulaşmak için Response.clone() kullanın.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed a used Response to FetchEvent.respondWith(). The body of a Response may only be read once. Use Response.clone() to access the body multiple times.`
    - The tree uses ’ 861 times against 46 straight.
- `BadOpaqueRedirectInterceptionWithURL` — `dom/chrome/dom/dom.properties` — `BadOpaqueRedirectInterceptionWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, navigasyon dışı bir FetchEvent'i işlerken FetchEvent.respondWith()'e bir opaqueredirect Response aktardı.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed an opaqueredirect Response to FetchEvent.respondWith() while handling a non-navigation FetchEvent.`
    - The tree uses ’ 861 times against 46 straight.
- `ManifestIdIsInvalid` — `dom/chrome/dom/dom.properties` — `ManifestIdIsInvalid` uses a straight apostrophe
    - Current: `id elemanı geçerli bir URL'ye işaret etmiyor.`
    - Source: `The id member did not resolve to a valid URL.`
    - The tree uses ’ 861 times against 46 straight.
- `TargetPrincipalDoesNotMatch` — `dom/chrome/dom/dom.properties` — `TargetPrincipalDoesNotMatch` uses a straight apostrophe
    - Current: `'DOMWindow'da 'postMessage' çalıştırılamadı. Sağlanan hedef köken ('%S') alıcının pencere kökeniyle ('%S') eşleşmiyor.`
    - Source: `Failed to execute ‘postMessage’ on ‘DOMWindow’: The target origin provided (‘%S’) does not match the recipient window’s origin (‘%S’).`
    - The tree uses ’ 861 times against 46 straight.
- `RewriteYouTubeEmbedPathParams` — `dom/chrome/dom/dom.properties` — `RewriteYouTubeEmbedPathParams` uses a straight apostrophe
    - Current: `Eski tarz YouTube Flash embed (%S) yerine iframe embed (%S) yazılıyor. iframe embed'lerindeki parametreler desteklenmediği için dönüştürüldüler. Mümkünse lütfen sayfayı güncelleyerek embed/object yerine iframe kullanın.`
    - Source: `Rewriting old-style YouTube Flash embed (%S) to iframe embed (%S). Params were unsupported by iframe embeds and converted. Please update page to use iframe instead of embed/object, if possible.`
    - The tree uses ’ 861 times against 46 straight.
- `PushMessageBadSalt` — `dom/chrome/dom/dom.properties` — `PushMessageBadSalt` uses straight double quotes
    - Current: `‘%1$S’ kapsamı için ServiceWorker bir push iletisini çözmeyi başaramadı. ‘Encryption‘ üst bilgisinde yer alan ‘salt‘ değişkeni base64url olarak kodlanmış (https://tools.ietf.org/html/rfc7515#appendix-C) ve kodlamadan ön…`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘salt‘ parameter in the ‘Encryption‘ header must be base64url-encoded (https://tools.ietf.org/html/rfc7515#appendix-C), and be at least 16 bytes b…`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `PushMessageBadCryptoError` — `dom/chrome/dom/dom.properties` — `PushMessageBadCryptoError` uses a straight apostrophe
    - Current: `'%1$S' kapsamının ServiceWorker'ı bir anında ilet mesajını çözemedi. Şifreleme ile ilgili yardım için lütfen https://developer.mozilla.org/docs/Web/API/Push_API/Using_the_Push_API#Encryption adresine bakın.`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. For help with encryption, please see https://developer.mozilla.org/docs/Web/API/Push_API/Using_the_Push_API#Encryption`
    - The tree uses ’ 861 times against 46 straight.
- `SVGRefLoopWarning` — `dom/chrome/dom/dom.properties` — `SVGRefLoopWarning` uses a straight apostrophe
    - Current: `%S SVG'si (“%S” kimliğine sahip) bir başvuru döngüsüne sahip.`
    - Source: `The SVG <%S> with ID “%S” has a reference loop.`
    - The tree uses ’ 861 times against 46 straight.
- `SVGDeselectAllWarning` — `dom/chrome/dom/dom.properties` — `SVGDeselectAllWarning` uses a straight apostrophe
    - Current: `SVGSVGElement.deselectAll, Selection API'sindeki işlevle benzer olduğu için kullanımdan kaldırılmıştır.`
    - Source: `SVGSVGElement.deselectAll is deprecated as it duplicates functionality from the Selection API.`
    - The tree uses ’ 861 times against 46 straight.
- `ScriptSourceMalformed` — `dom/chrome/dom/dom.properties` — `ScriptSourceMalformed` uses a straight apostrophe
    - Current: `<script> kaynak URI'sı kusurlu: “%S”.`
    - Source: `<script> source URI is malformed: “%S”.`
    - The tree uses ’ 861 times against 46 straight.
- `PEDisallowedImportRule` — `dom/chrome/layout/css.properties` — `PEDisallowedImportRule` uses straight double quotes
    - Current: `@import kuralları, "constructed" stil sayfalarında henüz geçerli değildir.`
    - Source: `@import rules are not yet valid in constructed stylesheets.`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `errProcessingInstruction` — `dom/chrome/layout/htmlparser.properties` — `errProcessingInstruction` uses a straight apostrophe
    - Current: `“<?” görüldü. Olası sebep: HTML içinde XML işleme talimatı girişimi. (XML işleme talimatları HTML'de desteklenmez.)`
    - Source: `Saw “<?”. Probable cause: Attempt to use an XML processing instruction in HTML. (XML processing instructions are not supported in HTML.)`
    - The tree uses ’ 861 times against 46 straight.
- `reader-view-enter-button` — `browser/browser/browser.ftl` — `reader-view-enter-button` uses a straight apostrophe
    - Current: `Okuyucu Görünümü'ne geç`
    - Source: `aria-label: Enter Reader View`
    - The tree uses ’ 861 times against 46 straight.
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — `menu-view-enter-readerview` uses a straight apostrophe
    - Current: `Okuyucu Görünümü'ne geç`
    - Source: `accesskey: R label: Enter Reader View`
    - The tree uses ’ 861 times against 46 straight.
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — `connection-dns-over-https-url-item-default` uses a straight apostrophe
    - Current: `DNS'i HTTPS üzerinden çözümlemek için varsayılan URL'yi kullan`
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
    - The tree uses ’ 861 times against 46 straight.
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — `policy-DisableSafeMode` uses a straight apostrophe
    - Current: `Güvenli kipte yeniden başlatma özelliğini devre dışı bırak. Not: Güvenli kipe girmek için kullanılan Shift tuşu, Windows'ta ancak Grup İlkesi ile devre dışı bırakılabilir.`
    - Source: `Disable the feature to restart in Safe Mode. Note: the Shift key to enter Safe Mode can only be disabled on Windows using Group Policy.`
    - The tree uses ’ 861 times against 46 straight.
- `about-glean-label-for-tag-pings-with-requirements` — `toolkit/toolkit/about/aboutGlean.ftl` — `about-glean-label-for-tag-pings-with-requirements` uses a straight apostrophe
    - Current: `Ping'lerinizi daha sonra tanıyabilmeniz için akılda kalıcı bir hata ayıklama etiketi <span>(en fazla 20 karakter; yalnızca harf, rakam ve “-”)</span> belirleyin.`
    - Source: `Set a memorable debug tag <span>(20 characters or fewer, alphanumerics and - only)</span> so you can recognize your pings later.`
    - The tree uses ’ 861 times against 46 straight.
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — `profiles-opendir` uses a straight apostrophe
    - Current: `{$sel_1 ->} [macos] Finder'da göster [windows] Klasörü aç [other] Dizini aç`
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
    - The tree uses ’ 861 times against 46 straight.
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — `show-dir-label` uses a straight apostrophe
    - Current: `{$sel_1 ->} [macos] Finder'da göster [windows] Klasörü aç [other] Dizini aç`
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
    - The tree uses ’ 861 times against 46 straight.
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — The Turkish drops the subject "SpeechRecognition" reporting itself as unavailable and turns "refuses to start" into a passive "could not be started".
    - Current: `SpeechRecognition kullanılamadığını bildirdi ve başlatılamadı`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `SpeechRecognition kendisini kullanılamaz olarak bildiriyor ve başlatılmayı reddediyor`
    - en-US: “SpeechRecognition reports itself as unavailable and refuses to start.” The Turkish says the API reported that something (unspecified) is unavailable and that it could not be started, changing both the reflexive meaning and the deliberate refusal into a failure.
- `speech-recognition-model-download-message` — `browser/browser/permissions.ftl` — The approximate size marker "~" is dropped, and "when you continue" is rendered as "when you continue with the installation".
    - Current: `Kuruluma devam ettiğinizde { $sizeMB } MB boyutunda bir indirme başlatılacaktır.`
    - Source: `{ -brand-short-name } runs speech recognition locally, so the audio never leaves your device. To set this up, a ~{ $sizeMB } MB download will start when you continue.`
    - Suggest: `Devam ettiğinizde ~{ $sizeMB } MB boyutunda bir indirme başlatılacaktır.`
    - en-US says “a ~{ $sizeMB } MB download will start when you continue”; the tilde indicating an approximate size is missing, so the size is presented as exact.
- `newtab-privacy-empty-state-tally` — `browser/browser/newtab/newtab.ftl` — "See a running tally here." is reduced to "Rakamlara bakın." losing the running/continuously updating total meaning.
    - Current: `Rakamlara bakın.`
    - Source: `See a running tally here.`
    - Suggest: `Güncel toplamı buradan görebilirsiniz.`
    - The developer comment explains the string refers to a continuously updating total shown here; the Turkish only says “Look at the numbers.”, dropping both “running tally” and “here”.
- `autocomplete-remove-password-os-auth-dialog-message-win` — `toolkit/toolkit/main-window/autocomplete.ftl` — Turkish says "we can better protect your accounts", whereas the source says this helps protect the security of your accounts (the action helps, not the vendor).
    - Current: `Bu sayede hesaplarınızı daha güvenli bir şekilde koruyabiliriz.`
    - Source: `To delete your password, enter your Windows login credentials. This helps protect the security of your accounts.`
    - Suggest: `Bu, hesaplarınızın güvenliğini korumaya yardımcı olur.`
    - en-US: "This helps protect the security of your accounts." The Turkish introduces a first-person claim ("we can protect") that the source never makes.
- `appmenuitem-relay-description2` — `browser/browser/appmenu.ftl` — Descriptive statement turned into an imperative and the "helps prevent" nuance lost.
    - Current: `Gelen kutunuzu spam’den koruyun`
    - Source: `Helps prevent spam in your inbox`
    - Suggest: `Gelen kutunuzdaki spam’i önlemeye yardımcı olur`
    - en-US "Helps prevent spam in your inbox" is a description of the feature, not an instruction to the user.
- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — "identification" translated as "tanımlama bilgisi", which is the established Turkish term for "cookie".
    - Current: `geçerli ve doğrulanmış tanımlama bilgisi sunuyor`
    - Source: `This site provides valid, verified identification.  There is no need to add an exception.`
    - Suggest: `geçerli ve doğrulanmış kimlik bilgileri sunuyor`
    - "tanımlama bilgisi" means cookie in Mozilla Turkish terminology; the source refers to site identification/identity information.

### ✅ Fixed since the last run (7)

- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `This site provides valid, verified identification.  There is no need to add an exception.`
- `delete-ssl-override-confirm` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `Are you sure you want to delete this server exception?`
- `delete-ssl-override-impact` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `If you delete a server exception, you restore the usual security checks for that server and require it uses a valid certificate.`
- `delete-ssl-override-title` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `title: Delete Server Certificate Exception`
- `exception-mgr` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `title: Add Security Exception`
- `exception-mgr-extra-button` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `accesskey: C label: Confirm Security Exception`
- `exception-mgr-permanent` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
    - Source: `accesskey: P label: Permanently store this exception`

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (11)

- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — The plural variant drops "all"/does not match the source wording distinction and reads awkwardly.
    - Current: `[other] { $count } hesabın hepsi tüm cihazlardan silinsin mi?`
    - Suggest: `[other] { $count } hesabın tümü tüm cihazlardan silinsin mi?`
    - en-US plural is "Remove all { $count } logins from all devices?"; the Turkish "hesabın hepsi tüm cihazlardan" is ungrammatical/redundant phrasing.
- `extension-colorways-bold-name` — `browser/browser/appExtensionFields.ftl` — developer comment not followed. The comment states "Bold" is used in the sense of bravery. Current "Koyu" means dark and duplicates extension-firefox-compact-dark-name. → "Cesur".
    - Suggest: `"Cesur".`
- `add-engine-dialog` — `browser/browser/preferences/addEngine.ftl` — see also S4.
- `autofill-add-new-address-title` — `browser/browser/preferences/formAutofill.ftl` — see also S4.
- `more-from-moz-mozilla-monitor-us-description` — `browser/browser/preferences/moreFromMozilla.ftl` — "Automatically" dropped.
- `about-glean-label-for-tag-pings` — `toolkit/toolkit/about/aboutGlean.ftl` — "pinglerinizi"; every other occurrence in the file uses "ping'ler" with an apostrophe.
- `rights-intro-point-3` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-intro-point-4` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-webservices-term-1` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `neterror-unknown-socket-type-psm-installed` — `toolkit/toolkit/neterror/netError.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 326 |
| Strings | 16,144 |
| Missing strings | 24 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 6 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 24 |

### Completeness

**24 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/onboarding.ftl` — 9
- `browser/browser/newtab/newtab.ftl` — 6
- `toolkit/toolkit/formautofill/formAutofill.ftl` — 3
- `dom/chrome/dom/dom.properties` — 2
- `toolkit/services/aboutSyncLog.ftl` — 2
- `browser/browser/ipProtection.ftl` — 1
- `toolkit/toolkit/main-window/autocomplete.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 603, `curly-single` 156, `straight-double` 29 | **curly-double** |
| apostrophe | `typographic` 861, `straight` 46 | **typographic** |
| ellipsis | `char` 388 | **char** |
| dash | `em` 44, `en` 2 | **em** |
| nbsp | `total` 6, `before-punctuation` 2, `space-before-punctuation` 5 | _mixed_ |
| register | `informal` 2, `formal` 46 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (147)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `newtab-privacy-across-sites` — `browser/browser/newtab/newtab.ftl` — Turkish adds a claim that Firefox protected the user, which the source does not say.
    - Current: `{ $count } sitede sizi koruduk`
    - Source: `{$count ->} [one] Across { $count } site [other] Across { $count } sites`
    - Suggest: `{ $count } sitede engellendi`
    - en-US is just "Across { $count } sites" (developer comment: "Blocked across { $count } sites"); the target asserts "we protected you on { $count } sites", a claim about the product's behaviour that the source never makes.
- `newtab-privacy-message-info-4` — `browser/browser/newtab/newtab.ftl` — "protection by default" rendered as "protection anytime, anywhere", dropping the default-setting meaning.
    - Current: `{ -brand-short-name } demek her an, her yerde korunma demektir.`
    - Source: `Choosing { -brand-short-name } means choosing protection by default.`
    - Suggest: `{ -brand-short-name } demek varsayılan olarak korunma demektir.`
    - The source says choosing the browser means protection is on by default; "her an, her yerde" (anytime, anywhere) is a different claim not present in the en-US.
- `autocomplete-remove-password-os-auth-dialog-message-win` — `toolkit/toolkit/main-window/autocomplete.ftl` — Turkish says "we can better protect your accounts", whereas the source says this helps protect the security of your accounts (the action helps, not the vendor).
    - Current: `Bu sayede hesaplarınızı daha güvenli bir şekilde koruyabiliriz.`
    - Source: `To delete your password, enter your Windows login credentials. This helps protect the security of your accounts.`
    - Suggest: `Bu, hesaplarınızın güvenliğini korumaya yardımcı olur.`
    - en-US: "This helps protect the security of your accounts." The Turkish introduces a first-person claim ("we can protect") that the source never makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 3 |
| 2 | Wrong content (says something other than the English) | 51 |
| 3 | Degraded language (grammar, spelling, terminology) | 59 |
| 4 | Cosmetic (typography, spacing) | 34 |

### A. Functional, markup, variables & plurals

- `autofill-address-country` — `browser/browser/preferences/formAutofill.ftl` — "Ülke" for en "Country or Region"; "or Region" dropped, and it now collides with autofill-address-country-only = "Ülke".
    - Source: `Country or Region`
- `autofill-address-county` — `browser/browser/preferences/formAutofill.ftl` — "İlçe", already used by autofill-address-district (District). County is a first-level division listed next to Province/State.
    - Source: `County`
- `autofill-address-name` — `browser/browser/preferences/formAutofill.ftl` — "Ad", identical to autofill-address-given-name (First Name) → "Ad soyad".
    - Source: `Name`
    - Suggest: `"Ad soyad".`

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The singular ([1]/[one]) variants say "all passwords" instead of "the password".
    - Current: `[1] Bu işlem { -brand-short-name } tarayıcınıza kaydettiğiniz tüm parolaları eşitlenen tüm cihazlardan silecektir.`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `[1] Bu işlem { -brand-short-name } tarayıcınıza kaydettiğiniz parolayı eşitlenen tüm cihazlardan silecektir.`
    - en-US singular says "This will remove the password saved to…" (one password); the Turkish singular variants say "tüm parolaları" (all passwords), matching the plural form instead.
- `extension-nova-dusk-name` — `browser/browser/appExtensionFields.ftl` — "Dusk" (just after sunset) is translated as "Şafak" (dawn), the opposite time of day.
    - Current: `Şafak`
    - Source: `Dusk`
    - Suggest: `Alacakaranlık`
    - The developer comment says the name refers to the sky just after sunset; "Şafak" means dawn/daybreak.
- `appmenuitem-relay-description2` — `browser/browser/appmenu.ftl` — Descriptive statement turned into an imperative and the "helps prevent" nuance lost.
    - Current: `Gelen kutunuzu spam’den koruyun`
    - Source: `Helps prevent spam in your inbox`
    - Suggest: `Gelen kutunuzdaki spam’i önlemeye yardımcı olur`
    - en-US "Helps prevent spam in your inbox" is a description of the feature, not an instruction to the user.
- `urlbar-result-weather-title` — `browser/browser/browser.ftl` — city and region swapped: { $region }, { $city } → { $city }, { $region } (cf. urlbar-result-weather-title-with-country).
    - Current: `{ $region }, { $city }`
    - Source: `<strong>{ $temperature }°{ $unit }</strong> in { $city }, { $region }`
    - Suggest: `{ $city }, { $region }`
- `taskbar-tabs-email-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — "protected by { -brand-short-name }" is rendered as "{ -brand-short-name } güvencesiyle korunan" ("protected under the guarantee of"), adding a claim of assurance not in the source.
    - Current: `{ -brand-short-name } güvencesiyle korunan yalın bir pencerede`
    - Source: `Launch your email sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `{ -brand-short-name } tarafından korunan yalın bir pencerede`
    - The en-US only says the window is protected by the browser; "güvencesiyle" adds a guarantee/warranty claim the source never makes.
- `taskbar-tabs-gaming-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — Adds a comparative "daha yalın" ("more streamlined") not present in the source, and renders "protected by" as "güvencesiyle".
    - Current: `{ -brand-short-name } güvencesiyle korunan daha yalın bir pencerede`
    - Source: `Launch your gaming sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `{ -brand-short-name } tarafından korunan yalın bir pencerede`
    - The en-US says "a streamlined window protected by { -brand-short-name }" with no comparison, and "güvencesiyle" adds a guarantee claim; it is also inconsistent with the parallel email/value-prop strings.
- `ip-protection-vpn-upgrade-link` — `browser/browser/ipProtection.ftl` — "up to five devices" is rendered as "beş ayrı cihazda", dropping the "up to" limit.
    - Current: `beş ayrı cihazda`
    - Source: `description: Choose custom VPN locations and add protection to all your apps on up to five devices, whether you’re at home or on public Wi-Fi. label: Get even more protection outside { -brand-short-name } with { -mozill…`
    - Suggest: `en fazla beş cihazda`
    - The en-US says "on up to five devices"; the Turkish states flatly "on five separate devices", losing the maximum-limit meaning.
- `ipprotection-connection-status-blocked-error-description-1` — `browser/browser/ipProtection.ftl` — Definite statement "limit where you can use VPN" weakened to "may limit".
    - Current: `VPN’i kullanabileceğiniz yerleri sınırlayabilir`
    - Source: `Local laws and restrictions limit where you can use VPN. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `VPN’i kullanabileceğiniz yerleri sınırlıyor`
    - en-US "limit" is a factual statement explaining why the connection is blocked; the Turkish "sınırlayabilir" (may limit) weakens it into speculation.
- `ipprotection-summer-promo-offramp-subscriber-description` — `browser/browser/ipProtection.ftl` — Statement of fact "You now get" turned into a possibility "you can have".
    - Current: `artık sınırsız bant genişliğine ve daha fazla konuma sahip olabilirsiniz`
    - Source: `You now get unlimited bandwidth and more locations as a { -mozilla-vpn-brand-name } subscriber.`
    - Suggest: `artık sınırsız bant genişliğine ve daha fazla konuma sahipsiniz`
    - The source tells subscribers they now have these benefits; "sahip olabilirsiniz" makes it a conditional possibility.
- `mr2022-background-update-toast-title` — `browser/browser/newtab/asrouter.ftl` — the fourth sentence "No compromises." is dropped entirely.
    - Source: `New { -brand-short-name }. More private. Fewer trackers. No compromises.`
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — "gereksiz özelliklerle dolu halde gelmez" ≠ en "isn't preloaded like other Big Tech browsers" (= not pre-installed on the device). The second sentence "That's the point." is also dropped.
    - Source: `{ -brand-product-name } isn’t preloaded like other Big Tech browsers. That’s the point.`
- `newtab-privacy-across-sites` — `browser/browser/newtab/newtab.ftl` — Turkish adds a claim that Firefox protected the user, which the source does not say.
    - Current: `{ $count } sitede sizi koruduk`
    - Source: `{$count ->} [one] Across { $count } site [other] Across { $count } sites`
    - Suggest: `{ $count } sitede engellendi`
    - en-US is just "Across { $count } sites" (developer comment: "Blocked across { $count } sites"); the target asserts "we protected you on { $count } sites", a claim about the product's behaviour that the source never makes.
- `newtab-privacy-empty-state-tally` — `browser/browser/newtab/newtab.ftl` — "See a running tally here." is reduced to "Rakamlara bakın." losing the running/continuously updating total meaning.
    - Current: `Rakamlara bakın.`
    - Source: `See a running tally here.`
    - Suggest: `Güncel toplamı buradan görebilirsiniz.`
    - The developer comment explains the string refers to a continuously updating total shown here; the Turkish only says “Look at the numbers.”, dropping both “running tally” and “here”.
- `newtab-privacy-etp-off-faster-browsing` — `browser/browser/newtab/newtab.ftl` — "Fewer trackers" translated as "Be tracked less" instead of referring to trackers.
    - Current: `Daha az takip edilin.`
    - Source: `Faster browsing. Fewer trackers.`
    - Suggest: `Daha az takip kodu.`
    - en-US "Fewer trackers" is a noun phrase about trackers; the Turkish turns it into an imperative claim about the user being tracked less. Elsewhere in this batch "trackers" is rendered "takip kodları".
- `newtab-privacy-message-info-10` — `browser/browser/newtab/newtab.ftl` — "strong, unique logins" translated as "strong and unique accounts".
    - Current: `güçlü ve benzersiz hesaplar kullanmak`
    - Source: `Save passwords in { -brand-short-name } to use strong, unique logins everywhere.`
    - Suggest: `güçlü ve benzersiz giriş bilgileri kullanmak`
    - "logins" refers to login credentials, not accounts ("hesaplar"); the Turkish changes the meaning of what the user is advised to use.
- `newtab-privacy-message-info-4` — `browser/browser/newtab/newtab.ftl` — "protection by default" rendered as "protection anytime, anywhere", dropping the default-setting meaning.
    - Current: `{ -brand-short-name } demek her an, her yerde korunma demektir.`
    - Source: `Choosing { -brand-short-name } means choosing protection by default.`
    - Suggest: `{ -brand-short-name } demek varsayılan olarak korunma demektir.`
    - The source says choosing the browser means protection is on by default; "her an, her yerde" (anytime, anywhere) is a different claim not present in the en-US.
- `newtab-privacy-message-promo-relay-3` — `browser/browser/newtab/newtab.ftl` — "email masks" translated as "e-posta maskesi" but the sentence drops the "keep private" agent structure and, more importantly, omits that the masks are the thing being obtained free — meaning shifted from "Get 50 free email masks" to a fragment.
    - Current: `Gerçek e-posta adresinizi gizli tutmanızı sağlayacak 50 e-posta maskesi ücretsiz.`
    - Source: `Get 50 free email masks to help keep your real email private.`
    - Suggest: `Gerçek e-posta adresinizi gizli tutmanıza yardımcı olacak 50 ücretsiz e-posta maskesi edinin.`
    - The en-US is an imperative call to action ("Get 50 free email masks…"); the Turkish is a verbless noun phrase and loses the "Get" action.
- `newtab-privacy-message-promo-signin-1` — `browser/browser/newtab/newtab.ftl` — "encrypted" dropped and replaced by vague "güvenle saklayın".
    - Current: `tüm cihazlarınızda güvenle saklayın`
    - Source: `Keep bookmarks, passwords, and tabs encrypted across devices with your { -vendor-short-name } account.`
    - Suggest: `tüm cihazlarınızda şifreli olarak saklayın`
    - The en-US specifically states data is kept encrypted across devices; the Turkish only says "store securely", losing the encryption claim.
- `media-count` — `browser/browser/pageInfo.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
    - Source: `label: Count`
    - Suggest: `"Sayı"`
- `speech-recognition-model-download-message` — `browser/browser/permissions.ftl` — The approximate size marker "~" is dropped, and "when you continue" is rendered as "when you continue with the installation".
    - Current: `Kuruluma devam ettiğinizde { $sizeMB } MB boyutunda bir indirme başlatılacaktır.`
    - Source: `{ -brand-short-name } runs speech recognition locally, so the audio never leaves your device. To set this up, a ~{ $sizeMB } MB download will start when you continue.`
    - Suggest: `Devam ettiğinizde ~{ $sizeMB } MB boyutunda bir indirme başlatılacaktır.`
    - en-US says “a ~{ $sizeMB } MB download will start when you continue”; the tilde indicating an approximate size is missing, so the size is presented as exact.
- `fonts-langgroup-header` — `browser/browser/preferences/fonts.ftl` — "Karakter kümesi" (character set) ≠ en "Fonts for" (a language-group selector).
    - Source: `(value): Fonts for accesskey: F`
- `containers-sites-card-header` — `browser/browser/preferences/preferences.ftl` — The description drops the meaning "choose a container for a site" and instead presupposes the container is already chosen.
    - Current: `Özel kapsayıcı seçtiğiniz siteleri her açtığınızda { -brand-short-name } bu kapsayıcıyı kullanır.`
    - Source: `description: Choose a container for a site and { -brand-short-name } will use it every time the site opens. label: Site-specific containers`
    - Suggest: `Bir site için kapsayıcı seçin; { -brand-short-name } site her açıldığında bu kapsayıcıyı kullansın.`
    - The en-US instructs the user to choose a container for a site; the Turkish only describes what happens afterwards, losing the instruction.
- `settings-keyboard-shortcuts-group` — `browser/browser/preferences/preferences.ftl` — "kolaylaştırın" (make it easier) ≠ en "Control how you move around and interact with".
    - Source: `description: Control how you move around and interact with { -brand-short-name }. label: Keyboard shortcuts`
- `should-restart-ok` — `browser/browser/preferences/preferences.ftl` — "now" dropped; the OK button is now byte-identical to should-restart-title.
    - Source: `Restart { -brand-short-name } now`
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — "Tabs sharing devices" is rendered as "Sekme paylaşan cihazlar" (devices that share tabs), reversing subject and object.
    - Current: `Sekme paylaşan cihazlar`
    - Source: `accesskey: d label: Tabs sharing devices`
    - Suggest: `Cihaz paylaşan sekmeler`
    - The en-US means tabs that are sharing devices (camera/microphone); the Turkish says devices sharing tabs.
- `inspector-emulation-panel-reduced-motion-no-preference` — `devtools/client/inspector.ftl` — The aria-label says "do not specify any preference" instead of "Enable no preference for reduced motion emulation", dropping the "enable" action.
    - Current: `Daha az hareket öykünümü için herhangi bir tercih belirtme`
    - Source: `(value): No preference aria-label: Enable no preference for reduced motion emulation`
    - Suggest: `Azaltılmış hareket öykünümü için “tercih yok” seçeneğini etkinleştir`
    - en-US is "Enable no preference for reduced motion emulation"; the Turkish renders it as a negative imperative ("do not specify a preference") and omits "Enable". It also uses "Daha az hareket" whereas the sibling strings consistently use "Azaltılmış hareket".
- `SpeechRecognitionBlockedByAIControlsWarning` — `dom/chrome/dom/dom.properties` — The Turkish drops the subject "SpeechRecognition" reporting itself as unavailable and turns "refuses to start" into a passive "could not be started".
    - Current: `SpeechRecognition kullanılamadığını bildirdi ve başlatılamadı`
    - Source: `On-device speech recognition is turned off in the user’s AI Controls settings, so SpeechRecognition reports itself as unavailable and refuses to start.`
    - Suggest: `SpeechRecognition kendisini kullanılamaz olarak bildiriyor ve başlatılmayı reddediyor`
    - en-US: “SpeechRecognition reports itself as unavailable and refuses to start.” The Turkish says the API reported that something (unspecified) is unavailable and that it could not be started, changing both the reflexive meaning and the deliberate refusal into a failure.
- `exception-mgr-supplemental-warning` — `security/manager/security/certificates/certManager.ftl` — "Legitimate" dropped; the whole point of the warning is that legitimate sites never ask this.
    - Source: `Legitimate banks, stores, and other public sites will not ask you to do this.`
- `devmgr-button-unload` — `security/manager/security/certificates/deviceManager.ftl` — "Boşalt" (empty/pour out) → "Kaldır" (en "Unload" a PKCS#11 module).
    - Source: `accesskey: U label: Unload`
    - Suggest: `"Kaldır"`
- `about-sync-log-view-error` — `toolkit/services/aboutSyncLog.ftl` — Past-tense failure statement rendered as present/ongoing tense.
    - Current: `Bu günlük dosyası okunamıyor.`
    - Source: `Could not read this log file.`
    - Suggest: `Bu günlük dosyası okunamadı.`
    - en-US "Could not read this log file." reports a completed failure; the Turkish says "cannot be read" (ongoing).
- `find-more-themes-promo` — `toolkit/toolkit/about/aboutAddons.ftl` — The message reverses the relation: source says pick a style that makes Firefox feel like yours, Turkish says pick the Firefox style that suits your taste.
    - Current: `Tarzınıza uygun { -brand-product-name } stilini seçin.`
    - Source: `heading: Find more fresh looks message: Choose a style that makes { -brand-product-name } feel like yours.`
    - Suggest: `{ -brand-product-name } tarayıcısını size ait gibi gösteren bir stil seçin.`
    - en-US: "Choose a style that makes { -brand-product-name } feel like yours." The Turkish loses the "feel like yours" idea and instead implies choosing among Firefox's own styles.
- `about-networking-ssl-tokens-compression-details` — `toolkit/toolkit/about/aboutNetworking.ftl` — "Tokens" (TLS resumption tokens) translated as "Jetonlar", a wrong technical term.
    - Current: `Jetonlar: { $tokenLength } B.`
    - Source: `title: Tokens: { $tokenLength } B. Encoded: { $decompressedLength } → { $compressedLength } B.`
    - Suggest: `Token’lar: { $tokenLength } B.`
    - Per the developer comment these are raw TLS resumption tokens; "jeton" (coin/game token) is not the security term used for TLS tokens.
- `place-database-stats-count` — `toolkit/toolkit/about/aboutSupport.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
    - Source: `Count`
    - Suggest: `"Sayı"`
- `processes-count` — `toolkit/toolkit/about/aboutSupport.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
    - Source: `Count`
    - Suggest: `"Sayı"`
- `about-webauthn-auth-info-max-rpids-for-set-min-pin-length` — `toolkit/toolkit/about/aboutWebauthn.ftl` — "relying" dropped from "relying party IDs", leaving "taraf kimliği" ambiguous.
    - Source: `Max relying party IDs for set minimum PIN length`
- `about-webauthn-auth-info-preferred-platform-uv-attempts` — `toolkit/toolkit/about/aboutWebauthn.ftl` — parses as "platform user's verification" instead of "platform user verification".
    - Source: `Preferred platform user verification attempts`
- `url-classifier-content-classifier-force-third-party` — `toolkit/toolkit/about/url-classifier.ftl` — "Force" is dropped, weakening the checkbox label to "treat as third-party".
    - Current: `Üst çerçeveye göre üçüncü taraf olarak değerlendir`
    - Source: `Force third-party to top frame`
    - Suggest: `Üst çerçeveye göre üçüncü taraf olmaya zorla`
    - The developer comment states this forces third-party treatment regardless of the URLs entered; "değerlendir" loses the forcing semantics.
- `csp-error-illegal-protocol` — `toolkit/toolkit/global/cspErrors.ftl` — the colon belongs to { $scheme }: "yasaklı bir { $scheme } içeriyor: protokol kaynağı" → "yasaklı bir { $scheme }: protokol kaynağı içeriyor".
    - Current: `{ $scheme }`
    - Source: `‘{ $directive }’ directive contains a forbidden { $scheme }: protocol source`
    - Suggest: `"yasaklı bir { $scheme }: protokol kaynağı içeriyor".`
- `theme-picker-dusk` — `toolkit/toolkit/global/theme-picker.ftl` — "Dusk" (just after sunset) is translated as "Şafak" (dawn), the opposite time of day.
    - Current: `Şafak`
    - Source: `label: Dusk`
    - Suggest: `Alacakaranlık`
    - The developer comment says the name refers to the sky just after sunset; "Şafak" means dawn/daybreak.
- `theme-picker-dusk-aria-label` — `toolkit/toolkit/global/theme-picker.ftl` — "Dusk" (just after sunset) is translated as "Şafak" (dawn), the opposite time of day.
    - Current: `Şafak`
    - Source: `aria-label: Dusk`
    - Suggest: `Alacakaranlık`
    - The developer comment says the name refers to the sky just after sunset; "Şafak" means dawn/daybreak.
- `language-name-si` — `toolkit/toolkit/intl/languageNames.ftl` — Sinhala — Seylanca — Sinhalaca — outdated exonym from "Ceylon".
    - Source: `Sinhala`
- `autocomplete-remove-password-os-auth-dialog-message-win` — `toolkit/toolkit/main-window/autocomplete.ftl` — Turkish says "we can better protect your accounts", whereas the source says this helps protect the security of your accounts (the action helps, not the vendor).
    - Current: `Bu sayede hesaplarınızı daha güvenli bir şekilde koruyabiliriz.`
    - Source: `To delete your password, enter your Windows login credentials. This helps protect the security of your accounts.`
    - Suggest: `Bu, hesaplarınızın güvenliğini korumaya yardımcı olur.`
    - en-US: "This helps protect the security of your accounts." The Turkish introduces a first-person claim ("we can protect") that the source never makes.
- `sec-error-ocsp-bad-http-response` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-ocsp-bad-http-response, sec-error-ocsp-unknown-response-status — "aldı"/"karşılaştı" → "döndürdü" (en "returned").
    - Source: `The OCSP server returned unexpected/invalid HTTP data.`
    - Suggest: `"döndürdü"`
- `sec-error-ocsp-unknown-response-status` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-ocsp-bad-http-response, sec-error-ocsp-unknown-response-status — "aldı"/"karşılaştı" → "döndürdü" (en "returned").
    - Source: `The OCSP server returned an unrecognizable status.`
    - Suggest: `"döndürdü"`
- `sec-error-unsupported-ec-point-form` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-unsupported-elliptic-curve, sec-error-unsupported-ec-point-form — "oval eğri" → "eliptik eğri".
    - Source: `Unsupported elliptic curve point form.`
    - Suggest: `"eliptik eğri".`
- `sec-error-unsupported-elliptic-curve` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-unsupported-elliptic-curve, sec-error-unsupported-ec-point-form — "oval eğri" → "eliptik eğri".
    - Source: `Unsupported elliptic curve.`
    - Suggest: `"eliptik eğri".`
- `ssl-error-handshake-failure-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — "kabul edilebilir sayıda güvenlik değişkeniyle" ≠ en "an acceptable set of security parameters".
    - Source: `SSL peer was unable to negotiate an acceptable set of security parameters.`
- `ssl-error-md5-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
    - Source: `MD5 digest function failed.`
- `ssl-error-sha-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
    - Source: `SHA-1 digest function failed.`
- `xp-java-cert-not-exists-error` — `toolkit/toolkit/neterror/nsserrors.ftl` — xp-java-remove-principal-error, xp-java-cert-not-exists-error — "Baş bölüm" → "Asıl (principal)".
    - Source: `This principal doesn’t have a certificate`
    - Suggest: `"Asıl`
- `xp-java-remove-principal-error` — `toolkit/toolkit/neterror/nsserrors.ftl` — xp-java-remove-principal-error, xp-java-cert-not-exists-error — "Baş bölüm" → "Asıl (principal)".
    - Source: `Couldn’t remove the principal`
    - Suggest: `"Asıl`

### C. Grammar, agreement & spelling

- `backup-folder-name` — `browser/browser/backupSettings.ftl` — Geri Yukleme — Geri Yükleme
    - Source: `Restore { -brand-product-name }`
- `newtab-stocks-in-watchlist` — `browser/browser/newtab/newtab.ftl` — Sentence is incomplete/ungrammatical and adds "zaten" (already), which the source does not say.
    - Current: `{ $name } zaten takip listenize`
    - Source: `{ $name } is in your watchlist`
    - Suggest: `{ $name } takip listenizde`
    - en-US "{ $name } is in your watchlist" states the stock is in the watchlist; the Turkish uses the dative "listenize" with no verb, leaving a broken fragment, and inserts "zaten".
- `restored-profile-page-learn-more` — `browser/browser/profiles.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `protections-panel-description-shim-allowed-learn-more` — `browser/browser/protectionsPanel.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `existing-user-tou-learn-more` — `browser/browser/termsofuse.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `translations-panel-learn-more-link` — `browser/browser/translations.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `whypaused-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on breakpoint`
- `whypaused-event-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on event breakpoint`
- `whypaused-promise-rejection` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on promise rejection`
- `ssl-error-cert-kea-mismatch` — `toolkit/toolkit/neterror/nsserrors.ftl` — anahtar değiş algoritması — anahtar değişim algoritması
    - Source: `The certificate provided cannot be used with the selected key exchange algorithm.`

### D. Terminology, register & consistency

- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Verilerimi geri yükle” but the string it names, `restore-from-backup-header`, reads “Verilerinizi geri yükleyin”
    - Current: `“Verilerimi geri yükle”ye tıklayıp bu dosyayı seçin`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Verilerinizi geri yükleyin`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Verilerimi geri yükle” but the string it names, `restore-from-backup-header`, reads “Verilerinizi geri yükleyin”
    - Current: `“Verilerimi geri yükle”ye tıklayıp bu dosyayı seçin`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Verilerinizi geri yükleyin`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `contextual-manager-password-login-line-with-alert` — `browser/browser/contextual-manager.ftl` — "(Dikkat)" vs "(Uyarı)" in the two parallel strings.
    - Source: `aria-label: Copy password (Warning) title: Copy password (Warning)`
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “Web tarayıcısı” but the string it names, `desktop-entry-generic-name`, reads “Web Tarayıcısı”
    - Current: `1. adım: Ayarlar > Varsayılan uygulamalar kısmına gidin 2. adım: Aşağı inerek “Web tarayıcısı” ayarını bulun 3. adım: Bu ayara girip { -brand-short-name } tarayıcısını seçin`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `Web Tarayıcısı`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `menu-application-set-as-default` — `browser/browser/menubar.ftl` — "saptanmış tarayıcı"; every other string in the locale uses "varsayılan".
    - Source: `label: Set { -brand-shorter-name } as Default Browser`
- `migration-wizard-safari-permissions-sub-header` — `browser/browser/migrationWizard.ftl` — "yer işaretleri"; the only occurrence in the whole locale — everywhere else bookmarks are "yer imleri".
    - Source: `To import Safari bookmarks and browsing history:`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — "saptanmış tarayıcı"; every other string in the locale uses "varsayılan".
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
- `newtab-clock-widget-custom-timezone-input` — `browser/browser/newtab/newtab.ftl` — "UTC offset" translated as "UTC farklılığına" instead of the standard "UTC farkı/kayması".
    - Current: `Şehre, saat dilimine veya UTC farklılığına göre ara`
    - Source: `aria-label: Time zone label: Time zone placeholder: Search by city, time zone, or UTC offset`
    - Suggest: `Şehre, saat dilimine veya UTC farkına göre ara`
    - "farklılık" means dissimilarity/diversity, not a numeric time offset; the standard Turkish term for UTC offset is "UTC farkı".
- `newtab-clock-widget-input-nickname` — `browser/browser/newtab/newtab.ftl` — ".label = Ad" for en "Nickname"; newtab-clock-widget-edit-item-with-nickname uses "takma adı", and plain "Ad" collides with a real name field (the dev comment warns about this).
    - Source: `aria-label: Nickname (optional) label: Nickname (optional) placeholder: Add a nickname`
- `newtab-recent-searches-menu-learn-more` — `browser/browser/newtab/newtab.ftl` — "Learn more" rendered in informal imperative ("al") instead of the formal "Daha fazla bilgi alın".
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The locale convention is formal siz; informal singular imperative violates the established register.
- `newtab-spaces-tab-widgets` — `browser/browser/newtab/newtab.ftl` — "Widgets" rendered as "Araçlar" (tools) instead of the established Turkish term for widgets.
    - Current: `Araçlar`
    - Source: `Widgets`
    - Suggest: `Widget’lar`
    - en-US "Widgets" refers to UI widgets; "Araçlar" means "Tools" and is used elsewhere for Tools menus, causing terminology confusion.
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — "ara verildi" vs the status string newtab-sports-widget-suspended "Askıya alındı".
    - Source: `aria-label: { $homeTeam } vs. { $awayTeam }, suspended`
- `newtab-widget-section-show-widgets` — `browser/browser/newtab/newtab.ftl` — "widgets" rendered as "Araçlar" (tools) rather than the established Turkish term for widgets.
    - Current: `aria-label: Araçlar bölümünü göster`
    - Source: `aria-label: Show the widgets section title: Show widgets`
    - Suggest: `aria-label: Widget’lar bölümünü göster`
    - en-US "widgets" is a specific UI term; "araç" is the standard translation for "tool", which is a different concept used elsewhere in the UI.
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Mobil cihazla eşitle” but the string it names, `sync-to-mobile-button-label`, reads “Mobil cihazla eşitleyin”
    - Current: `{ -brand-product-name } uygulamasını mobil cihazınıza indirmek için QR kodunu okutun. İndirdikten sonra parolalarınıza, yer imlerinize ve diğer bilgilerinize erişmek için “Mobil cihazla eşitle” seçeneğini seçin.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Mobil cihazla eşitleyin`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — `policy-OverridePostUpdatePage` quotes “Yenilikler” but the string it names, `releaseNotes-link`, reads “Yeni neler var?”
    - Current: `Güncelleme sonrası “Yenilikler” sayfasını değiştir. Güncelleme sonrası sayfasını devre dışı bırakmak istiyorsanız bu ilkeyi boş olarak ayarlayabilirsiniz.`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Yeni neler var?`
    - In the source this string quotes “What’s New”, which is exactly the value of `releaseNotes-link` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `autofill-addresses-add-button` — `browser/browser/preferences/preferences.ftl` — see also S4.
    - Source: `Add new address`
- `preferences-ai-controls-translations-control` — `browser/browser/preferences/preferences.ftl` — "Çeviri" vs "Çeviriler" everywhere else.
    - Source: `description: Seamlessly browse the web in your preferred language. label: Translations`
- `remove-engine-remove` — `browser/browser/preferences/preferences.ftl` — "Sil" vs the triggering control search-remove-engine "Kaldır".
    - Source: `Remove`
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — "yanıltıcı" vs "aldatıcı" used for en "deceptive" in security-enable-safe-browsing, security-browsing-protection, browsing-protection-group2.
    - Source: `description: Your exposure to scams and malware from websites is increased. label: Dangerous and deceptive content is not blocked`
- `safeb-blocked-unwanted-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — "kötü amaçlı yazılım" vs "zararlı yazılım" in the three sibling strings.
    - Source: `Learn more about harmful and unwanted software at <a data-l10n-name='learn_more_link'>Unwanted Software Policy</a>. Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_…`
- `add-engine-dialog2` — `browser/browser/search.ftl` — see also S4.
    - Source: `buttonaccesskeyaccept: A buttonlabelaccept: Add Engine buttonlabelextra1: Advanced`
- `styleeditor-new-button` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `accesskey: N tooltiptext: Create and append a new style sheet to the document`
- `styleeditor-save-button` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `(value): Save accesskey: S tooltiptext: Save this style sheet to a file`
- `styleeditor-stylesheet-all-filtered` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `No matching style sheet has been found.`
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `accesskey: S tooltiptext: Toggle style sheet visibility`
- `styleeditor-visibility-toggle-system` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `tooltiptext: System style sheets can’t be disabled`
- `options-context-triggers-page-refresh-persists` — `devtools/client/toolbox-options.ftl` — "(sayfayı tazeler)" vs "sayfayı yeniden yükler" in the two sibling strings.
    - Source: `(reloads the page)`
- `options-stylesheets-in-the-debugger-label` — `devtools/client/toolbox-options.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `Show stylesheets in the debugger`
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “yerel modu” but the string it names, `options-local-mode-label`, reads “Yerel mod”
    - Current: `Bu belgeyi ayarlar panelinden etkinleştirebileceğiniz geliştirici araçları “yerel modu”nu kullanarak “{ $url }” adresinden de açabilirsiniz.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Yerel mod`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — "identification" translated as "tanımlama bilgisi", which is the established Turkish term for "cookie".
    - Current: `geçerli ve doğrulanmış tanımlama bilgisi sunuyor`
    - Source: `This site provides valid, verified identification.  There is no need to add an exception.`
    - Suggest: `geçerli ve doğrulanmış kimlik bilgileri sunuyor`
    - "tanımlama bilgisi" means cookie in Mozilla Turkish terminology; the source refers to site identification/identity information.
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — "güvenlik cihazı" vs "güvenlik aygıtı" used in devmgr-window, unable-to-toggle-fips, pkcs12-dup-data, certmgr-token-name, change-password-token.
    - Source: `Please authenticate to the security device ({ $tokenName }). How to do so depends on the device (for example, using a fingerprint reader or entering a code with a keypad).`
- `about-glean-about-data-header` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
    - Source: `About Data`
- `about-glean-category-about-data` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
    - Source: `About Data`
- `main-thread-no-omtc` — `toolkit/toolkit/about/aboutSupport.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
    - Source: `main thread, no OMTC`
- `about-telemetry-slow-sql-main` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
    - Source: `Slow SQL Statements on Main Thread`
- `about-telemetry-slow-sql-other` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
    - Source: `Slow SQL Statements on Helper Threads`
- `about-telemetry-slow-sql-statement` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "İfade" vs the section heading about-telemetry-slow-sql-section "Deyimleri".
    - Source: `Statement`
- `certificate-viewer-given-name` — `toolkit/toolkit/about/certviewer.ftl` — "Adı", identical to certificate-viewer-name; the two certificate fields become indistinguishable → "Ön adı".
    - Source: `Given Name`
    - Suggest: `"Ön adı".`
- `wizard-macos-button-next` — `toolkit/toolkit/global/wizard.ftl` — "İleri" for the macOS "Continue" variant, while profile-creation-explanation-4 tells macOS users to press "Devam düğmesine".
    - Source: `accesskey: C label: Continue`
- `neterror-search-cta-learn-more` — `toolkit/toolkit/neterror/netError.ftl` — "Learn more" rendered in informal imperative ("al") instead of the formal "Daha fazla bilgi alın".
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The locale convention is formal siz; other UI strings in this batch use formal imperatives ("deneyin", "kabul edin").
- `neterror-search-cta-reload-button` — `toolkit/toolkit/neterror/netError.ftl` — "Reload" is rendered as "Tazele" instead of the established Firefox tr term "Yeniden yükle".
    - Current: `label: Tazele`
    - Source: `accesskey: R label: Reload`
    - Suggest: `label: Yeniden yükle`
    - In Firefox tr, "Reload" is consistently translated as "Yeniden yükle"; "Tazele" is not the product's terminology and is inconsistent with other reload controls.
- `pdfjs-editor-alt-text-button-label` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Alternatif metin" in 4 strings vs "Alt metin" in ~20.
    - Source: `Alt text`
- `pdfjs-editor-alt-text-settings-create-model-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görme engelli kişilere" narrows en "people who can't see the image"; pdfjs-editor-alt-text-dialog-description renders the same source correctly.
    - Source: `Suggests descriptions to help people who can’t see the image or when the image doesn’t load.`
- `pdfjs-editor-new-alt-text-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görme engelli kişilere" narrows en "people who can't see the image"; pdfjs-editor-alt-text-dialog-description renders the same source correctly.
    - Source: `Short description for people who can’t see the image or when the image doesn’t load.`
- `pdfjs-editor-undo-bar-message-stamp` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görsel silindi" vs "Resim" used in every other image string.
    - Source: `Image removed`
- `margin-group-label-inches` — `toolkit/toolkit/printing/printDialogs.ftl` — "Kenarlar" (edges) vs printui-margins "Kenar boşlukları".
    - Source: `value: Margins (inches)`
- `margin-group-label-metric` — `toolkit/toolkit/printing/printDialogs.ftl` — "Kenarlar" (edges) vs printui-margins "Kenar boşlukları".
    - Source: `value: Margins (millimeters)`
- `print-setup` — `toolkit/toolkit/printing/printDialogs.ftl` — "Sayfa Yapısı" vs the menu item that opens it, printpreview-page-setup "Sayfa düzeni…".
    - Source: `title: Page Setup`
- `printui-sheets-count` — `toolkit/toolkit/printing/printUI.ftl` — "{ $sheetCount } sayfa" for en "sheets of paper", while "sayfa" is already page; printui-pages-per-sheet uses "yaprak".
    - Source: `{$sheetCount ->} [one] { $sheetCount } sheet of paper [other] { $sheetCount } sheets of paper`

### E. Typography, punctuation & spacing

- `reader-view-enter-button` — `browser/browser/browser.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `aria-label: Enter Reader View`
- `reader-view-enter-button` — `browser/browser/browser.ftl` — `reader-view-enter-button` uses a straight apostrophe
    - Current: `Okuyucu Görünümü'ne geç`
    - Source: `aria-label: Enter Reader View`
    - The tree uses ’ 861 times against 46 straight.
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `accesskey: R label: Enter Reader View`
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — `menu-view-enter-readerview` uses a straight apostrophe
    - Current: `Okuyucu Görünümü'ne geç`
    - Source: `accesskey: R label: Enter Reader View`
    - The tree uses ’ 861 times against 46 straight.
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Disable the feature to restart in Safe Mode. Note: the Shift key to enter Safe Mode can only be disabled on Windows using Group Policy.`
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — `policy-DisableSafeMode` uses a straight apostrophe
    - Current: `Güvenli kipte yeniden başlatma özelliğini devre dışı bırak. Not: Güvenli kipe girmek için kullanılan Shift tuşu, Windows'ta ancak Grup İlkesi ile devre dışı bırakılabilir.`
    - Source: `Disable the feature to restart in Safe Mode. Note: the Shift key to enter Safe Mode can only be disabled on Windows using Group Policy.`
    - The tree uses ’ 861 times against 46 straight.
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — `connection-dns-over-https-url-item-default` uses a straight apostrophe
    - Current: `DNS'i HTTPS üzerinden çözümlemek için varsayılan URL'yi kullan`
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
    - The tree uses ’ 861 times against 46 straight.
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `accesskey: E description: Add websites that can open pop-ups and use third-party redirects. label: Manage exceptions searchkeywords: popups`
- `BadOpaqueRedirectInterceptionWithURL` — `dom/chrome/dom/dom.properties` — `BadOpaqueRedirectInterceptionWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, navigasyon dışı bir FetchEvent'i işlerken FetchEvent.respondWith()'e bir opaqueredirect Response aktardı.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed an opaqueredirect Response to FetchEvent.respondWith() while handling a non-navigation FetchEvent.`
    - The tree uses ’ 861 times against 46 straight.
- `BlockAutoplayWebAudioStartError` — `dom/chrome/dom/dom.properties` — `BlockAutoplayWebAudioStartError` uses a straight apostrophe
    - Current: `Bir AudioContext'in otomatik başlaması engellendi. AudioContext, sayfadaki bir kullanıcı hareketinden sonra oluşturulmalı veya devam ettirilmelidir.`
    - Source: `An AudioContext was prevented from starting automatically. It must be created or resumed after a user gesture on the page.`
    - The tree uses ’ 861 times against 46 straight.
- `InterceptedErrorResponseWithURL` — `dom/chrome/dom/dom.properties` — `InterceptedErrorResponseWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, FetchEvent.respondWith()'e bir Error Response aktardı. Bu genellikle ServiceWorker'ın geçersiz bir fetch() çağrısı yaptığını gösterir.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed an Error Response to FetchEvent.respondWith(). This typically means the ServiceWorker performed an invalid fetch() call.`
    - The tree uses ’ 861 times against 46 straight.
- `InterceptedUsedResponseWithURL` — `dom/chrome/dom/dom.properties` — `InterceptedUsedResponseWithURL` uses a straight apostrophe
    - Current: `'%S' yüklenemedi. Bir ServiceWorker, FetchEvent.respondWith()'e kullanılmış bir Response aktardı. Bir Response'un gövdesi yalnızca bir kez okunabilir. Gövdeye birden fazla kez ulaşmak için Response.clone() kullanın.`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed a used Response to FetchEvent.respondWith(). The body of a Response may only be read once. Use Response.clone() to access the body multiple times.`
    - The tree uses ’ 861 times against 46 straight.
- `LenientThisWarning` — `dom/chrome/dom/dom.properties` — `LenientThisWarning` uses a straight apostrophe
    - Current: `“this” nesnesi yanlış olduğundan [LenientThis] içeren özelliğin get veya set'i yok sayılıyor.`
    - Source: `Ignoring get or set of property that has [LenientThis] because the “this” object is incorrect.`
    - The tree uses ’ 861 times against 46 straight.
- `ManifestIdIsInvalid` — `dom/chrome/dom/dom.properties` — `ManifestIdIsInvalid` uses a straight apostrophe
    - Current: `id elemanı geçerli bir URL'ye işaret etmiyor.`
    - Source: `The id member did not resolve to a valid URL.`
    - The tree uses ’ 861 times against 46 straight.
- `MediaEMENoCodecsDeprecatedWarning` — `dom/chrome/dom/dom.properties` — `MediaEMENoCodecsDeprecatedWarning` uses straight double quotes
    - Current: `contentType olmadan "codecs" ifadesine sahip audioCapabilities ve videoCapabilities içeren MediaKeySystemConfiguration adayını aktarmadan navigator.requestMediaKeySystemAccess() çağrısı gerçekleştirmek (%S adresinde) ar…`
    - Source: `Calling navigator.requestMediaKeySystemAccess() (at %S) passing a candidate MediaKeySystemConfiguration containing audioCapabilities or videoCapabilities without a contentType with a “codecs” string is deprecated and wi…`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `NavigatorGetUserMediaWarning` — `dom/chrome/dom/dom.properties` — `NavigatorGetUserMediaWarning` uses a straight apostrophe
    - Current: `navigator.mozGetUserMedia'nın yerini navigator.mediaDevices.getUserMedia almıştır`
    - Source: `navigator.mozGetUserMedia has been replaced by navigator.mediaDevices.getUserMedia`
    - The tree uses ’ 861 times against 46 straight.
- `PushMessageBadCryptoError` — `dom/chrome/dom/dom.properties` — `PushMessageBadCryptoError` uses a straight apostrophe
    - Current: `'%1$S' kapsamının ServiceWorker'ı bir anında ilet mesajını çözemedi. Şifreleme ile ilgili yardım için lütfen https://developer.mozilla.org/docs/Web/API/Push_API/Using_the_Push_API#Encryption adresine bakın.`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. For help with encryption, please see https://developer.mozilla.org/docs/Web/API/Push_API/Using_the_Push_API#Encryption`
    - The tree uses ’ 861 times against 46 straight.
- `PushMessageBadSalt` — `dom/chrome/dom/dom.properties` — `PushMessageBadSalt` uses straight double quotes
    - Current: `‘%1$S’ kapsamı için ServiceWorker bir push iletisini çözmeyi başaramadı. ‘Encryption‘ üst bilgisinde yer alan ‘salt‘ değişkeni base64url olarak kodlanmış (https://tools.ietf.org/html/rfc7515#appendix-C) ve kodlamadan ön…`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘salt‘ parameter in the ‘Encryption‘ header must be base64url-encoded (https://tools.ietf.org/html/rfc7515#appendix-C), and be at least 16 bytes b…`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `RewriteYouTubeEmbedPathParams` — `dom/chrome/dom/dom.properties` — `RewriteYouTubeEmbedPathParams` uses a straight apostrophe
    - Current: `Eski tarz YouTube Flash embed (%S) yerine iframe embed (%S) yazılıyor. iframe embed'lerindeki parametreler desteklenmediği için dönüştürüldüler. Mümkünse lütfen sayfayı güncelleyerek embed/object yerine iframe kullanın.`
    - Source: `Rewriting old-style YouTube Flash embed (%S) to iframe embed (%S). Params were unsupported by iframe embeds and converted. Please update page to use iframe instead of embed/object, if possible.`
    - The tree uses ’ 861 times against 46 straight.
- `SVGDeselectAllWarning` — `dom/chrome/dom/dom.properties` — `SVGDeselectAllWarning` uses a straight apostrophe
    - Current: `SVGSVGElement.deselectAll, Selection API'sindeki işlevle benzer olduğu için kullanımdan kaldırılmıştır.`
    - Source: `SVGSVGElement.deselectAll is deprecated as it duplicates functionality from the Selection API.`
    - The tree uses ’ 861 times against 46 straight.
- `SVGRefLoopWarning` — `dom/chrome/dom/dom.properties` — `SVGRefLoopWarning` uses a straight apostrophe
    - Current: `%S SVG'si (“%S” kimliğine sahip) bir başvuru döngüsüne sahip.`
    - Source: `The SVG <%S> with ID “%S” has a reference loop.`
    - The tree uses ’ 861 times against 46 straight.
- `ScriptSourceMalformed` — `dom/chrome/dom/dom.properties` — `ScriptSourceMalformed` uses a straight apostrophe
    - Current: `<script> kaynak URI'sı kusurlu: “%S”.`
    - Source: `<script> source URI is malformed: “%S”.`
    - The tree uses ’ 861 times against 46 straight.
- `TargetPrincipalDoesNotMatch` — `dom/chrome/dom/dom.properties` — `TargetPrincipalDoesNotMatch` uses a straight apostrophe
    - Current: `'DOMWindow'da 'postMessage' çalıştırılamadı. Sağlanan hedef köken ('%S') alıcının pencere kökeniyle ('%S') eşleşmiyor.`
    - Source: `Failed to execute ‘postMessage’ on ‘DOMWindow’: The target origin provided (‘%S’) does not match the recipient window’s origin (‘%S’).`
    - The tree uses ’ 861 times against 46 straight.
- `PEDisallowedImportRule` — `dom/chrome/layout/css.properties` — `PEDisallowedImportRule` uses straight double quotes
    - Current: `@import kuralları, "constructed" stil sayfalarında henüz geçerli değildir.`
    - Source: `@import rules are not yet valid in constructed stylesheets.`
    - The locale's quote convention is `curly-double` (603 occurrences).
- `errProcessingInstruction` — `dom/chrome/layout/htmlparser.properties` — `errProcessingInstruction` uses a straight apostrophe
    - Current: `“<?” görüldü. Olası sebep: HTML içinde XML işleme talimatı girişimi. (XML işleme talimatları HTML'de desteklenmez.)`
    - Source: `Saw “<?”. Probable cause: Attempt to use an XML processing instruction in HTML. (XML processing instructions are not supported in HTML.)`
    - The tree uses ’ 861 times against 46 straight.
- `about-glean-label-for-tag-pings-with-requirements` — `toolkit/toolkit/about/aboutGlean.ftl` — `about-glean-label-for-tag-pings-with-requirements` uses a straight apostrophe
    - Current: `Ping'lerinizi daha sonra tanıyabilmeniz için akılda kalıcı bir hata ayıklama etiketi <span>(en fazla 20 karakter; yalnızca harf, rakam ve “-”)</span> belirleyin.`
    - Source: `Set a memorable debug tag <span>(20 characters or fewer, alphanumerics and - only)</span> so you can recognize your pings later.`
    - The tree uses ’ 861 times against 46 straight.
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — `profiles-opendir` uses a straight apostrophe
    - Current: `{$sel_1 ->} [macos] Finder'da göster [windows] Klasörü aç [other] Dizini aç`
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
    - The tree uses ’ 861 times against 46 straight.
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — `show-dir-label` uses a straight apostrophe
    - Current: `{$sel_1 ->} [macos] Finder'da göster [windows] Klasörü aç [other] Dizini aç`
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
    - The tree uses ’ 861 times against 46 straight.
- `about-webrtc-save-page-dialog-title` — `toolkit/toolkit/about/aboutWebrtc.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `save about:webrtc as`
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `With this feature enabled, { -brand-short-name } supports the JPEG XL (JXL) format. This is an enhanced image file format that supports lossless transition from traditional JPEG files. See <a data-l10n-name="bugzilla">b…`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/tr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — raised by `term_params`, withdrawn 2026-09-02

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (193)

- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `delete-ssl-override-confirm` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `delete-ssl-override-impact` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `delete-ssl-override-title` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `exception-mgr` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `exception-mgr-extra-button` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `exception-mgr-permanent` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-09-14
- `ipprotection-feature-introduction-text-summer-promo-1` — `browser/browser/ipProtection.ftl` — fixed 2026-09-07
- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-24
- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `reset-pbm-panel-description` — `browser/browser/browser.ftl` — fixed 2026-08-24
- `callout-firefox-view-tab-pickup-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `pin-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `firefox-relay-must-login-to-fxa` — `browser/browser/firefoxRelay.ftl` — fixed 2026-08-24
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — fixed 2026-08-24
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-sports-widget-message-survey-body` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `newtab-weather-menu-temperature-option-celsius` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `onboarding-refresh-import-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `tab-groups-onboarding-create-group-title-3` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `tab-groups-onboarding-saved-groups-title-3` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `tab-groups-onboarding-session-restore-title-2` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `places-view-sortby-name` — `browser/browser/places.ftl` — fixed 2026-08-24
- `policy-FirefoxHome2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-24
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — fixed 2026-08-24
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `content-blocking-cross-site-tracking-cookies-plus-isolate` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-ai-controls-on-device-group` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-copy-profile-header` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `sitedata-total-size` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `space-alert-under-5gb-message2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — fixed 2026-08-24
- `profiles-cyan-theme-title` — `browser/browser/profiles.ftl` — fixed 2026-08-24
- `monitor-partial-breaches-motivation-description` — `browser/browser/protections.ftl` — fixed 2026-08-24
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — fixed 2026-08-24
