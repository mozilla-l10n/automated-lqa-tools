# Firefox l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-08-27 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `caafd8e1597e` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 18,110 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for tr: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 360 |
| Strings | 18,110 |
| Missing strings | 100 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 5 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 27 |

### Completeness

**100 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 41
- `toolkit/services/aboutSyncLog.ftl` — 26
- `toolkit/toolkit/about/url-classifier.ftl` — 10
- `browser/browser/ipProtection.ftl` — 9
- `browser/browser/firefoxView.ftl` — 5
- `browser/browser/newtab/onboarding.ftl` — 4
- `devtools/client/inspector.ftl` — 3
- `toolkit/toolkit/pdfviewer/embedFallback.ftl` — 2

**Files absent from the locale:**

- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 675, `curly-single` 166, `straight-double` 29 | **curly-double** |
| apostrophe | `typographic` 963, `straight` 50 | **typographic** |
| ellipsis | `char` 460 | **char** |
| dash | `em` 72, `en` 2 | **em** |
| nbsp | `total` 9, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 2, `formal` 58 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 27 strings** — 27 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BadOpaqueRedirectInterceptionWithURL`, `BlockAutoplayWebAudioStartError`, `InterceptedErrorResponseWithURL`, `InterceptedUsedResponseWithURL`, `LenientThisWarning`, `ManifestIdIsInvalid`, `MediaEMENoCodecsDeprecatedWarning`, `NavigatorGetUserMediaWarning`, `PEDisallowedImportRule`, `PushMessageBadCryptoError`, `PushMessageBadSalt`, `RewriteYouTubeEmbedPathParams` …and 15 more

---

## 3. Open findings (121)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 62 |
| 4 | Cosmetic (typography, spacing) | 15 |

### A. Functional, markup, variables & plurals

- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — `fxa-signout-dialog-body-aiwindow` calls `-smart-window-brand-name` with ['plural-form'], but that term selects on ['form']
    - Current: `Eşitlenen veriler hesabınızda kalmaya devam edecek. Açık olan { -smart-window-brand-name } klasik pencerelere dönüşecek.`
    - Source: `Synced data will remain in your account. Open { -smart-window-brand-name } will switch to Classic Windows.`
    - Suggest: `{ -smart-window-brand-name(form: "lowercase-plural") }`
    - The term falls back to its catch-all variant, so the intended form is never selected.
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
- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — The plural variant drops "all"/does not match the source wording distinction and reads awkwardly.
    - Current: `[other] { $count } hesabın hepsi tüm cihazlardan silinsin mi?`
    - Source: `{$count ->} [one] Remove { $count } login from all devices? [other] Remove all { $count } logins from all devices?`
    - Suggest: `[other] { $count } hesabın tümü tüm cihazlardan silinsin mi?`
    - en-US plural is "Remove all { $count } logins from all devices?"; the Turkish "hesabın hepsi tüm cihazlardan" is ungrammatical/redundant phrasing.
- `extension-colorways-bold-name` — `browser/browser/appExtensionFields.ftl` — developer comment not followed. The comment states "Bold" is used in the sense of bravery. Current "Koyu" means dark and duplicates extension-firefox-compact-dark-name. → "Cesur".
    - Source: `{ $colorway-name } — Bold`
    - Suggest: `"Cesur".`
- `extension-nova-dusk-name` — `browser/browser/appExtensionFields.ftl` — "Dusk" (just after sunset) is translated as "Şafak" (dawn), the opposite time of day.
    - Current: `Şafak`
    - Source: `Dusk`
    - Suggest: `Alacakaranlık`
    - The developer comment says the name refers to the sky just after sunset; "Şafak" means dawn/daybreak.
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
- `mr2022-background-update-toast-title` — `browser/browser/newtab/asrouter.ftl` — the fourth sentence "No compromises." is dropped entirely.
    - Source: `New { -brand-short-name }. More private. Fewer trackers. No compromises.`
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — "gereksiz özelliklerle dolu halde gelmez" ≠ en "isn't preloaded like other Big Tech browsers" (= not pre-installed on the device). The second sentence "That's the point." is also dropped.
    - Source: `{ -brand-product-name } isn’t preloaded like other Big Tech browsers. That’s the point.`
- `media-count` — `browser/browser/pageInfo.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
    - Source: `label: Count`
    - Suggest: `"Sayı"`
- `fonts-langgroup-header` — `browser/browser/preferences/fonts.ftl` — "Karakter kümesi" (character set) ≠ en "Fonts for" (a language-group selector).
    - Source: `(value): Fonts for accesskey: F`
- `more-from-moz-mozilla-monitor-us-description` — `browser/browser/preferences/moreFromMozilla.ftl` — "Automatically" dropped.
    - Source: `Automatically take back your exposed personal info.`
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
- `exception-mgr-supplemental-warning` — `security/manager/security/certificates/certManager.ftl` — "Legitimate" dropped; the whole point of the warning is that legitimate sites never ask this.
    - Source: `Legitimate banks, stores, and other public sites will not ask you to do this.`
- `devmgr-button-unload` — `security/manager/security/certificates/deviceManager.ftl` — "Boşalt" (empty/pour out) → "Kaldır" (en "Unload" a PKCS#11 module).
    - Source: `accesskey: U label: Unload`
    - Suggest: `"Kaldır"`
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
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — "ara verildi" vs the status string newtab-sports-widget-suspended "Askıya alındı".
    - Source: `aria-label: { $homeTeam } vs. { $awayTeam }, suspended`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Mobil cihazla eşitle” but the string it names, `sync-to-mobile-button-label`, reads “Mobil cihazla eşitleyin”
    - Current: `{ -brand-product-name } uygulamasını mobil cihazınıza indirmek için QR kodunu okutun. İndirdikten sonra parolalarınıza, yer imlerinize ve diğer bilgilerinize erişmek için “Mobil cihazla eşitle” seçeneğini seçin.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Mobil cihazla eşitleyin`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `add-engine-dialog` — `browser/browser/preferences/addEngine.ftl` — see also S4.
    - Source: `buttonaccesskeyaccept: A buttonlabelaccept: Add Engine`
- `autofill-add-new-address-title` — `browser/browser/preferences/formAutofill.ftl` — see also S4.
    - Source: `Add New Address`
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
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — "güvenlik cihazı" vs "güvenlik aygıtı" used in devmgr-window, unable-to-toggle-fips, pkcs12-dup-data, certmgr-token-name, change-password-token.
    - Source: `Please authenticate to the security device ({ $tokenName }). How to do so depends on the device (for example, using a fingerprint reader or entering a code with a keypad).`
- `about-glean-about-data-header` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
    - Source: `About Data`
- `about-glean-category-about-data` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
    - Source: `About Data`
- `about-glean-label-for-tag-pings` — `toolkit/toolkit/about/aboutGlean.ftl` — "pinglerinizi"; every other occurrence in the file uses "ping'ler" with an apostrophe.
    - Source: `In the preceding field ensure there is a memorable debug tag so you can recognize your pings later.`
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
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `accesskey: R label: Enter Reader View`
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Disable the feature to restart in Safe Mode. Note: the Shift key to enter Safe Mode can only be disabled on Windows using Group Policy.`
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `accesskey: E description: Add websites that can open pop-ups and use third-party redirects. label: Manage exceptions searchkeywords: popups`
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `rights-intro-point-3` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Some features in { -brand-short-name }, such as the Crash Reporter, give you the option to provide feedback to { -vendor-short-name }. By choosing to submit feedback, you give { -vendor-short-name } permission to use th…`
- `rights-intro-point-4` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `How we use your personal information and feedback submitted to { -vendor-short-name } through { -brand-short-name } is described in the <a data-l10n-name="mozilla-privacy-policy-link">{ -brand-short-name } Privacy Polic…`
- `rights-webservices-term-1` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{ -vendor-short-name } and its contributors, licensors and partners work to provide the most accurate and up-to-date Services. However, we cannot guarantee that this information is comprehensive and error-free. For exam…`
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{ -vendor-short-name } may update these terms as necessary from time to time. These terms may not be modified or canceled without { -vendor-short-name }’s written agreement.`
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `about-webrtc-save-page-dialog-title` — `toolkit/toolkit/about/aboutWebrtc.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `save about:webrtc as`
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `With this feature enabled, { -brand-short-name } supports the JPEG XL (JXL) format. This is an enhanced image file format that supports lossless transition from traditional JPEG files. See <a data-l10n-name="bugzilla">b…`
- `neterror-unknown-socket-type-psm-installed` — `toolkit/toolkit/neterror/netError.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Check to make sure your system has the Personal Security Manager installed.`

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

### Fixed to date (185)

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
- `report-broken-site-panel-intro-text` — `browser/browser/reportBrokenSite.ftl` — fixed 2026-08-24
- `set-background-stretch` — `browser/browser/setDesktopBackground.ftl` — fixed 2026-08-24
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — fixed 2026-08-24
- `webrtc-reason-for-no-permanent-allow-audio` — `browser/browser/webrtcIndicator.ftl` — fixed 2026-08-24
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — fixed 2026-08-24
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — fixed 2026-08-24
- `storage-table-type-cache-hint` — `devtools/client/storage.ftl` — fixed 2026-08-24
- `styleeditor-filter-input` — `devtools/client/styleeditor.ftl` — fixed 2026-08-24
